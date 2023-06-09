import os
import sys
from configparser import ConfigParser
from runpy import run_path
from unittest import mock

import fedora_messaging.api
import pytest
from koji.context import context
from koji.plugin import callbacks, register_callback

ENVIRON = {
    "UNIQUE_ID": "dummyuniqueid",
    "SCRIPT_URL": "/kojihub",
    "SCRIPT_URI": "http://koji.stg.fedoraproject.org/kojihub",
    "GATEWAY_INTERFACE": "CGI/1.1",
    "SERVER_PROTOCOL": "HTTP/1.1",
    "REQUEST_METHOD": "POST",
    "QUERY_STRING": "",
    "REQUEST_URI": "/kojihub",
    "SCRIPT_NAME": "/kojihub",
    "HTTP_HOST": "koji.stg.fedoraproject.org",
    "HTTP_USER_AGENT": "koji/1",
    "HTTP_ACCEPT_ENCODING": "gzip, deflate",
    "HTTP_ACCEPT": "*/*",
    "HTTP_KOJI_SESSION_ID": "123456789",
    "HTTP_KOJI_SESSION_KEY": "dummy-session-key",
    "HTTP_KOJI_SESSION_CALLNUM": "1",
    "CONTENT_TYPE": "text/xml",
    "HTTP_X_FORWARDED_SCHEME": "https",
    "HTTP_X_FEDORA_REQUESTID": "dummy-request-id",
    "HTTP_X_FORWARDED_FOR": "10.1.2.3",
    "HTTP_X_FORWARDED_HOST": "koji.stg.fedoraproject.org",
    "HTTP_X_FORWARDED_SERVER": "koji.fedoraproject.org",
    "CONTENT_LENGTH": "362",
    "HTTP_CONNECTION": "Keep-Alive",
    "SERVER_SIGNATURE": "",
    "SERVER_SOFTWARE": "Apache",
    "SERVER_NAME": "koji.stg.fedoraproject.org",
    "SERVER_ADDR": "10.4.5.6",
    "SERVER_PORT": "80",
    "REMOTE_ADDR": "10.1.2.3",
    "DOCUMENT_ROOT": "/var/www/html",
    "REQUEST_SCHEME": "http",
    "CONTEXT_PREFIX": "/kojihub",
    "CONTEXT_DOCUMENT_ROOT": "/usr/share/koji-hub/kojiapp.py",
    "SERVER_ADMIN": "root@localhost",
    "SCRIPT_FILENAME": "/usr/share/koji-hub/kojiapp.py",
    "REMOTE_PORT": "46789",
    "PATH_INFO": "",
    "mod_wsgi.script_name": "/kojihub",
    "mod_wsgi.path_info": "",
    "mod_wsgi.process_group": "",
    "mod_wsgi.application_group": "",
    "mod_wsgi.callable_object": "application",
    "mod_wsgi.request_handler": "wsgi-script",
    "mod_wsgi.handler_script": "",
    "mod_wsgi.script_reloading": "1",
    "mod_wsgi.listener_host": "",
    "mod_wsgi.listener_port": "80",
    "mod_wsgi.enable_sendfile": "0",
    "mod_wsgi.ignore_activity": "0",
    "mod_wsgi.request_start": "123456789",
    "mod_wsgi.request_id": "dummyrequestid",
    "mod_wsgi.script_start": "123456789",
    "wsgi.version": (1, 0),
    "wsgi.multithread": True,
    "wsgi.multiprocess": True,
    "wsgi.run_once": False,
    "wsgi.url_scheme": "http",
    "wsgi.errors": None,
    "wsgi.input": None,
    "wsgi.input_terminated": True,
    "wsgi.file_wrapper": None,
    "apache.version": (2, 4, 54),
    "mod_wsgi.version": (4, 9, 4),
    "mod_wsgi.total_requests": 42,
    "mod_wsgi.thread_id": 4,
    "mod_wsgi.thread_requests": 42,
}


@pytest.fixture
def mocked_config():
    config = ConfigParser()
    config.read_dict({"web": {"KojiFilesURL": "http://files.example.com/"}})
    with mock.patch("koji.read_config_files", return_value=config) as rcf:
        yield rcf


@pytest.fixture
def kojihub():
    mod = mock.Mock(name="kojihub")
    mod.get_host.return_value = {"name": "builder.example.com"}
    mod.get_user.return_value = {"name": "dummy-user"}
    mod._tasks = {}

    def _create_task(task_id):
        task = mock.Mock(name="task")
        task.id = task_id
        task.getChildren.side_effect = lambda: []
        task.getResult.return_value = None
        mod._tasks[task_id] = task
        return task

    mod.Task.side_effect = _create_task
    return mod


@pytest.fixture
def mocked_modules(mocked_config, kojihub):
    yield {
        "kojihub": kojihub,
        "read_config_files": mocked_config,
        "fedora_messaging.api": fedora_messaging.api,
    }


@pytest.fixture
def module(mocked_modules):
    context._threadclear()
    context.environ = ENVIRON.copy()
    with mock.patch.dict(sys.modules, mocked_modules):
        mod = run_path(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "koji-fedoramessaging/koji-fedoramessaging.py",
            ),
            run_name="koji-fedoramessaging.py",
        )
        _register_callbacks(mod)
        yield mod
        _clear_callbacks()


def _register_callbacks(mod):
    for entry in mod.values():
        if (
            callable(entry)
            and not isinstance(entry, mock.Mock)
            and getattr(entry, "callbacks", None)
        ):
            for cbtype in entry.callbacks:
                # Don't ignore errors
                entry.failure_is_an_option = False
                register_callback(cbtype, entry)


def _clear_callbacks():
    for funcs in callbacks.values():
        funcs.clear()
