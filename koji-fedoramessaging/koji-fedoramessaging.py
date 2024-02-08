# Version 0.1
#
# Koji callback plugin for sending notifications about events to fedora-messaging
# Copyright (c) 2009-2023 Red Hat, Inc.
#
# Source: https://github.com/fedora-infra/koji-fedoramessaging
#
# Authors:
#     Ralph Bean <rbean@redhat.com>
#     Mike Bonnet <mikeb@redhat.com>
#     Aurelien Bompard <abompard@fedoraproject.org>

import logging
import re

import fedora_messaging.api
import fedora_messaging.exceptions
import kojihub
import pkg_resources
from jsonschema.exceptions import ValidationError
from koji import PathInfo, read_config_files
from koji.context import context
from koji.plugin import callback, callbacks, ignore_error

MAX_KEY_LENGTH = 255

# Set the logger to something that the koji logging system understands.
# This way we can control the logging level of this plugin from koji's hub.conf
# by adding this 'koji._koji_plugin__koji-fedoramessaging:INFO' to the LogLevel
# conf value in hub.conf
log = logging.getLogger(f"koji.{__name__}")


def get_base_url(environ):
    host = environ.get("HTTP_X_FORWARDED_HOST", environ["SERVER_NAME"])
    url_scheme = environ.get("HTTP_X_FORWARDED_SCHEME", environ["wsgi.url_scheme"])
    return f"{url_scheme}://{host}"


def get_files_base_url(environ):
    cf = environ.get("koji.web.ConfigFile", "/etc/kojiweb/web.conf")
    cfdir = environ.get("koji.web.ConfigDir", "/etc/kojiweb/web.conf.d")
    kojiweb_config = read_config_files([cfdir, (cf, True)])
    return PathInfo(topdir=kojiweb_config.get("web", "KojiFilesURL").rstrip("/")).work()


def camel_to_dots(name):
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1.\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1.\2", s1).lower()


def serialize_datetime_in_task(task):
    date_fields = [
        "completion_time",
        "create_time",
        "start_time",
        "buildtime",
        "creation_ts",
        "creation_time",
    ]
    for date_key in date_fields:
        if task.get(date_key) is None:
            continue
        if isinstance(task[date_key], (float, int)):
            continue
        task[date_key] = task[date_key].replace(microsecond=0).timestamp()


def get_task_result(task_id):
    task = kojihub.Task(task_id)
    try:
        return task.getResult()
    except Exception as e:
        err_msg = f"Could not get the Task result of task {task.id}: {e}"
        log.warning(err_msg)
        return None


def get_owner(info):
    if "owner_name" in info:
        return info["owner_name"]
    elif "owner_id" in info:
        return kojihub.get_user(info["owner_id"])["name"]
    elif "owner" in info:
        return kojihub.get_user(info["owner"])["name"]
    else:
        return None


def get_full_task_info(task_info, base_url):
    task = kojihub.Task(task_info["id"])
    serialize_datetime_in_task(task_info)
    task_info["host_name"] = (
        kojihub.get_host(task_info["host_id"])["name"] if task_info.get("host_id") else None
    )
    task_info["url"] = f"{base_url}/koji/taskinfo?taskID={task.id}"
    task_info["result"] = get_task_result(task.id)
    task_info["owner"] = get_owner(task_info)
    if isinstance(task_info.get("request"), tuple):
        task_info["request"] = list(task_info["request"])
    task_info["children"] = []
    for child in task.getChildren():
        task_info["children"].append(get_full_task_info(child, base_url))
    return task_info


def get_message_body(topic, *args, **kws):
    msg = {}
    msg["base_url"] = get_base_url(context.environ)

    if topic == "package.list.change":
        msg["tag"] = kws["tag"]["name"]
        msg["package"] = kws["package"]["name"]
        msg["action"] = kws["action"]
        if "owner" in kws:
            msg["owner"] = kojihub.get_user(kws["owner"])["name"]
        else:
            msg["owner"] = None
        msg["block"] = kws.get("block", None)
        msg["extra_arches"] = kws.get("extra_arches", None)
        msg["force"] = kws.get("force", None)
        msg["update"] = kws.get("update", None)
    elif topic == "task.state.change":
        # Send the whole info dict along because it might have useful info.
        # For instance, it contains the mention of what format createAppliance
        # is using (raw or qcow2).
        msg["info"] = get_full_task_info(kws["info"], msg["base_url"])
        msg["method"] = msg["info"]["method"]
        msg["attribute"] = kws["attribute"]
        msg["old"] = kws["old"]
        msg["new"] = kws["new"]
        msg["id"] = msg["info"]["id"]
        msg["owner"] = msg["info"]["owner"]
        msg["files_base_url"] = get_files_base_url(context.environ)

        # extract a useful identifier from the request string
        request = kws["info"].get("request", ["/"])
        msg["srpm"] = request[0].split("/")[-1]

    elif topic == "build.state.change":
        info = kws["info"]
        msg["name"] = info["name"]
        msg["version"] = info["version"]
        msg["release"] = info["release"]
        msg["epoch"] = info.get("epoch")
        msg["attribute"] = kws["attribute"]
        msg["old"] = kws["old"]
        msg["new"] = kws["new"]
        msg["build_id"] = info.get("id", None)
        msg["task_id"] = info.get("task_id", None)
        msg["owner"] = get_owner(info)
        msg["files_base_url"] = get_files_base_url(context.environ)
        if msg["build_id"]:
            msg["url"] = f"{msg['base_url']}/koji/buildinfo?buildID={msg['build_id']}"
        else:
            # May happen on preBuildStateChange for new builds, no ID yet.
            # That said, we don't subscribe to that at the moment...
            msg["url"] = None

        if msg["task_id"]:
            task = kojihub.Task(msg["task_id"])
            msg["task"] = get_full_task_info(task.getInfo(request=True), msg["base_url"])
            msg["request"] = msg["task"]["request"]
        else:
            msg["task"] = None
            msg["request"] = None

        # Add the timestamps
        msg["creation_time"] = info["creation_time"].isoformat()
        msg["completion_time"] = (
            info["completion_time"].isoformat() if info["completion_time"] else None
        )

    elif topic == "import":
        # TODO -- import is currently unused.
        # Should we remove it?
        msg["type"] = kws["type"]
    elif topic in ("tag", "untag"):
        msg["tag"] = kws["tag"]["name"]
        build = kws["build"]
        msg["name"] = build["name"]
        msg["version"] = build["version"]
        msg["release"] = build["release"]
        msg["user"] = kws["user"]["name"]
        msg["owner"] = kojihub.get_user(kws["build"]["owner_id"])["name"]
        msg["tag_id"] = kws["tag"]["id"]
        msg["build_id"] = kws["build"]["id"]
    elif topic == "repo.init":
        msg["tag"] = kws["tag"]["name"]
        msg["tag_id"] = kws["tag"]["id"]
        msg["repo_id"] = kws["repo_id"]
    elif topic == "repo.done":
        msg["tag"] = kws["repo"]["tag_name"]
        msg["tag_id"] = kws["repo"]["tag_id"]
        msg["repo_id"] = kws["repo"]["id"]
    elif topic == "rpm.sign":
        if "attribute" in kws:
            # v1.10.1 and earlier
            msg["attribute"] = kws["attribute"]
            msg["old"] = kws["old"]
            msg["new"] = kws["new"]
            msg["info"] = kws["info"]
        else:
            # v1.11.0 (and maybe higher, but who knows)
            msg["sigkey"] = kws["sigkey"]
            msg["sighash"] = kws["sighash"]
            msg["build"] = kws["build"]
            msg["rpm"] = kws["rpm"]
            serialize_datetime_in_task(msg["build"])
            serialize_datetime_in_task(msg["rpm"])

    return msg


# This callback gets run for every koji event that starts with "post"
@callback(
    *[
        c
        for c in callbacks.keys()
        if c.startswith("post")
        and c
        not in [
            "postImport",  # This is kind of useless; also noisy.
            # This one is special, and is called every time, so ignore it.
            # Added here https://pagure.io/koji/pull-request/148
            "postCommit",
        ]
    ]
)
@ignore_error
def queue_message(cbtype, *args, **kws):
    if cbtype.startswith("post"):
        msgtype = cbtype[4:]
    else:
        msgtype = cbtype[3:]

    # Short-circuit ourselves for task events.  They are very spammy and we are
    # only interested in state changes to scratch builds (parent tasks).
    if cbtype == "postTaskStateChange":
        # only state changes
        if not kws.get("attribute", None) == "state":
            return
        # only parent tasks
        if kws.get("info", {}).get("parent"):
            return
        # only scratch builds
        request = kws.get("info", {}).get("request", [{}])[-1]
        if not isinstance(request, dict) or not request.get("scratch"):
            return

    # Don't publish these uninformative rpm.sign messages if there's no actual
    # sigkey present.  Koji apparently adds a dummy sig value when rpms are
    # first imported and there's no need to spam the world about that.
    if cbtype == "postRPMSign" and (
        kws.get("info", {}).get("sigkey") == "" or kws.get("sigkey") == ""
    ):
        return

    # Also, do not want to send a message on volume_id changes
    if cbtype == "postBuildStateChange" and kws.get("attribute") == "volume_id":
        return

    topic = camel_to_dots(msgtype)
    body = get_message_body(topic, *args, **kws)

    # We need this to distinguish between messages from primary koji
    # and the secondary hubs off for s390 and ppc.
    body["instance"] = "primary"

    # Last thing to do before publishing: scrub some problematic fields
    # These fields are floating points which get json-encoded differently on
    # rhel and fedora.
    problem_fields = ["weight", "start_ts", "create_ts", "completion_ts"]

    def scrub(obj):
        if isinstance(obj, list):
            return [scrub(item) for item in obj]
        if isinstance(obj, dict):
            return dict([(k, scrub(v)) for k, v in obj.items() if k not in problem_fields])
        return obj

    body = scrub(body)

    # Queue the message for later.
    # It will only get sent after postCommit is called.
    messages = getattr(context, "fedmsg_plugin_messages", [])
    messages.append(dict(topic=topic, msg=body))
    context.fedmsg_plugin_messages = messages


def get_message(topic, body):
    message_object = None

    for entry_point in pkg_resources.iter_entry_points("fedora.messages"):
        cls = entry_point.load()
        if cls.topic == topic:
            message_object = cls
            break
    if message_object is None:
        message_object = fedora_messaging.api.Message

    return message_object(topic=topic, body=body)


# Meanwhile, postCommit actually sends messages.
@callback("postCommit")
@ignore_error
def send_messages(cbtype, *args, **kws):
    messages = getattr(context, "fedmsg_plugin_messages", [])

    for message in messages:
        try:
            topic = f"buildsys.{message['topic']}"
            msg = get_message(topic, message["msg"])
            log.info(f"Publishing message on topic {topic}")
            log.debug(f"Message body {message['msg']}")
            try:
                fedora_messaging.api.publish(msg)
            except ValidationError as e:
                log.exception(
                    f"Schema for {topic} message (id {msg.id}) from Koji not valid "
                    f"trying to send message as generic fedoramessaging message. "
                    f"Error: {e}"
                )
                newmsg = fedora_messaging.api.Message(topic=topic, body=message["msg"])
                newmsg.id = msg.id
                fedora_messaging.api.publish(newmsg)
        except fedora_messaging.exceptions.PublishReturned as e:
            log.warning("Fedora Messaging broker rejected message %s: %s", msg.id, e)
        except fedora_messaging.exceptions.ConnectionException as e:
            log.warning("Error sending message %s: %s", msg.id, e)
        except Exception:
            log.exception("Un-expected error sending fedora-messaging message")
