import datetime
from copy import deepcopy

import pytest
from koji.context import context
from koji.plugin import run_callbacks

TEST_DATA = {
    "open": {
        "kws": {
            "attribute": "state",
            "old": "FREE",
            "new": "OPEN",
            "info": {
                "arch": "noarch",
                "awaited": None,
                "channel_id": 1,
                "completion_time": None,
                "completion_ts": None,
                "create_time": datetime.datetime(
                    2023, 6, 8, 9, 56, 21, 738084, tzinfo=datetime.timezone.utc
                ),
                "create_ts": 1686218181.738084,
                "host_id": 569,
                "id": 110011364,
                "label": None,
                "method": "build",
                "owner": 158,
                "parent": None,
                "priority": 20,
                "start_time": datetime.datetime(
                    2023, 6, 8, 9, 56, 21, 897874, tzinfo=datetime.timezone.utc
                ),
                "start_ts": 1686218181.897874,
                "state": 1,
                "waiting": None,
                "weight": 1.0,
                "request": (
                    "git+https://src.stg.fedoraproject.org/rpms/python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
                    "rawhide",
                    {"scratch": True},
                ),
            },
        },
        "msg": {
            "base_url": "https://koji.stg.fedoraproject.org",
            "files_base_url": "http://files.example.com/work",
            "info": {
                "arch": "noarch",
                "awaited": None,
                "channel_id": 1,
                "completion_time": None,
                "create_time": 1686218181.0,
                "host_id": 569,
                "id": 110011364,
                "label": None,
                "method": "build",
                "owner": 158,
                "parent": None,
                "priority": 20,
                "start_time": 1686218181.0,
                "state": 1,
                "waiting": None,
                "request": (
                    "git+https://src.stg.fedoraproject.org/rpms/python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
                    "rawhide",
                    {"scratch": True},
                ),
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011364",
                "result": None,
                "children": [],
            },
            "method": "build",
            "attribute": "state",
            "old": "FREE",
            "new": "OPEN",
            "id": 110011364,
            "srpm": "python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
            "owner": "dummy-user",
            "instance": "primary",
        },
    },
    "close": {
        "kws": {
            "attribute": "state",
            "old": "OPEN",
            "new": "CLOSED",
            "info": {
                "arch": "noarch",
                "awaited": None,
                "channel_id": 1,
                "completion_time": datetime.datetime(
                    2023, 6, 8, 10, 1, 9, 737291, tzinfo=datetime.timezone.utc
                ),
                "completion_ts": 1686218469.737291,
                "create_time": datetime.datetime(
                    2023, 6, 8, 9, 56, 21, 738084, tzinfo=datetime.timezone.utc
                ),
                "create_ts": 1686218181.738084,
                "host_id": 569,
                "id": 110011364,
                "label": None,
                "method": "build",
                "owner": 158,
                "parent": None,
                "priority": 20,
                "start_time": datetime.datetime(
                    2023, 6, 8, 9, 56, 21, 897874, tzinfo=datetime.timezone.utc
                ),
                "start_ts": 1686218181.897874,
                "state": 2,
                "waiting": False,
                "weight": 0.2,
                "request": (
                    "git+https://src.stg.fedoraproject.org/rpms/python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
                    "rawhide",
                    {"scratch": True},
                ),
                "result": None,
            },
        },
        "msg": {
            "base_url": "https://koji.stg.fedoraproject.org",
            "files_base_url": "http://files.example.com/work",
            "info": {
                "arch": "noarch",
                "awaited": None,
                "channel_id": 1,
                "completion_time": 1686218469.0,
                "create_time": 1686218181.0,
                "host_id": 569,
                "id": 110011364,
                "label": None,
                "method": "build",
                "owner": 158,
                "parent": None,
                "priority": 20,
                "start_time": 1686218181.0,
                "state": 2,
                "waiting": False,
                "request": (
                    "git+https://src.stg.fedoraproject.org/rpms/python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
                    "rawhide",
                    {"scratch": True},
                ),
                "result": None,
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011364",
                "children": [],
            },
            "method": "build",
            "attribute": "state",
            "old": "OPEN",
            "new": "CLOSED",
            "id": 110011364,
            "srpm": "python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
            "owner": "dummy-user",
            "instance": "primary",
        },
    },
    "fail": {
        "kws": {
            "attribute": "state",
            "old": "OPEN",
            "new": "FAILED",
            "info": {
                "arch": "noarch",
                "awaited": None,
                "channel_id": 1,
                "completion_time": datetime.datetime(
                    2023, 6, 8, 12, 12, 1, 529560, tzinfo=datetime.timezone.utc
                ),
                "completion_ts": 1686226321.52956,
                "create_time": datetime.datetime(
                    2023, 6, 8, 12, 8, 6, 480133, tzinfo=datetime.timezone.utc
                ),
                "create_ts": 1686226086.480133,
                "host_id": 569,
                "id": 110011398,
                "label": None,
                "method": "build",
                "owner": 5485,
                "parent": None,
                "priority": 50,
                "start_time": datetime.datetime(
                    2023, 6, 8, 12, 8, 6, 983868, tzinfo=datetime.timezone.utc
                ),
                "start_ts": 1686226086.983868,
                "state": 5,
                "waiting": True,
                "weight": 0.2,
                "request": (
                    "cli-build/1686226086.4513252.NoatzAfE/khal-0.11.2-1.fc38.src.rpm",
                    "rawhide",
                    {"scratch": True},
                ),
            },
        },
        "msg": {
            "base_url": "https://koji.stg.fedoraproject.org",
            "files_base_url": "http://files.example.com/work",
            "info": {
                "arch": "noarch",
                "awaited": None,
                "channel_id": 1,
                "completion_time": 1686226321.0,
                "create_time": 1686226086.0,
                "host_id": 569,
                "id": 110011398,
                "label": None,
                "method": "build",
                "owner": 5485,
                "parent": None,
                "priority": 50,
                "start_time": 1686226086.0,
                "state": 5,
                "waiting": True,
                "request": (
                    "cli-build/1686226086.4513252.NoatzAfE/khal-0.11.2-1.fc38.src.rpm",
                    "rawhide",
                    {"scratch": True},
                ),
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011398",
                "result": None,
                "children": [],
            },
            "method": "build",
            "attribute": "state",
            "old": "OPEN",
            "new": "FAILED",
            "id": 110011398,
            "srpm": "khal-0.11.2-1.fc38.src.rpm",
            "owner": "dummy-user",
            "instance": "primary",
        },
    },
    "cancel": {
        "kws": {
            "attribute": "state",
            "old": "OPEN",
            "new": "CANCELED",
            "info": {
                "arch": "noarch",
                "awaited": None,
                "channel_id": 1,
                "completion_time": datetime.datetime(
                    2023, 6, 8, 11, 59, 24, 333040, tzinfo=datetime.timezone.utc
                ),
                "completion_ts": 1686225564.33304,
                "create_time": datetime.datetime(
                    2023, 6, 8, 11, 59, 3, 868427, tzinfo=datetime.timezone.utc
                ),
                "create_ts": 1686225543.868427,
                "host_id": 569,
                "id": 110011396,
                "label": None,
                "method": "build",
                "owner": 158,
                "parent": None,
                "priority": 20,
                "start_time": datetime.datetime(
                    2023, 6, 8, 11, 59, 4, 436842, tzinfo=datetime.timezone.utc
                ),
                "start_ts": 1686225544.436842,
                "state": 3,
                "waiting": True,
                "weight": 0.2,
                "request": (
                    "git+https://src.stg.fedoraproject.org/rpms/python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
                    "rawhide",
                    {"scratch": True},
                ),
            },
        },
        "msg": {
            "base_url": "https://koji.stg.fedoraproject.org",
            "files_base_url": "http://files.example.com/work",
            "info": {
                "arch": "noarch",
                "awaited": None,
                "channel_id": 1,
                "completion_time": 1686225564.0,
                "create_time": 1686225543.0,
                "host_id": 569,
                "id": 110011396,
                "label": None,
                "method": "build",
                "owner": 158,
                "parent": None,
                "priority": 20,
                "start_time": 1686225544.0,
                "state": 3,
                "waiting": True,
                "request": (
                    "git+https://src.stg.fedoraproject.org/rpms/python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
                    "rawhide",
                    {"scratch": True},
                ),
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011396",
                "result": None,
                "children": [],
            },
            "method": "build",
            "attribute": "state",
            "old": "OPEN",
            "new": "CANCELED",
            "id": 110011396,
            "srpm": "python-atpublic.git#ae8818da76ae0d4ea00bac7c3c8e7d11608ea3b0",
            "owner": "dummy-user",
            "instance": "primary",
        },
    },
}

CLOSE_WITH_SUBTASKS_KWS = {
    "attribute": "state",
    "old": "OPEN",
    "new": "CLOSED",
    "info": {
        "arch": "noarch",
        "awaited": None,
        "channel_id": 1,
        "completion_time": datetime.datetime(
            2023, 6, 8, 11, 40, 31, 858334, tzinfo=datetime.timezone.utc
        ),
        "completion_ts": 1686224431.858334,
        "create_time": datetime.datetime(
            2023, 6, 8, 11, 35, 13, 123218, tzinfo=datetime.timezone.utc
        ),
        "create_ts": 1686224113.123218,
        "host_id": 570,
        "id": 110011389,
        "label": None,
        "method": "build",
        "owner": 5485,
        "parent": None,
        "priority": 50,
        "start_time": datetime.datetime(
            2023, 6, 8, 11, 35, 14, 48696, tzinfo=datetime.timezone.utc
        ),
        "start_ts": 1686224114.048696,
        "state": 2,
        "waiting": False,
        "weight": 0.2,
        "request": (
            "cli-build/1686224113.0942957.VtfzIqPe/golang-modernc-file-1.0.8-1.fc38.src.rpm",
            "rawhide",
            {"scratch": True},
        ),
        "result": None,
    },
}


CLOSE_WITH_SUBTASKS_MSG = {
    "base_url": "https://koji.stg.fedoraproject.org",
    "files_base_url": "http://files.example.com/work",
    "info": {
        "arch": "noarch",
        "awaited": None,
        "channel_id": 1,
        "completion_time": 1686224431.0,
        "create_time": 1686224113.0,
        "host_id": 570,
        "id": 110011389,
        "label": None,
        "method": "build",
        "owner": 5485,
        "parent": None,
        "priority": 50,
        "start_time": 1686224114.0,
        "state": 2,
        "waiting": False,
        "request": (
            "cli-build/1686224113.0942957.VtfzIqPe/golang-modernc-file-1.0.8-1.fc38.src.rpm",
            "rawhide",
            {"scratch": True},
        ),
        "result": None,
        "host_name": "builder.example.com",
        "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011389",
        "children": [
            {
                "arch": "noarch",
                "awaited": False,
                "channel_id": 1,
                "completion_time": 1686224226.0,
                "create_time": 1686224114.0,
                "host_id": 574,
                "id": 110011390,
                "label": "srpm",
                "method": "rebuildSRPM",
                "owner": 5485,
                "parent": 110011389,
                "priority": 49,
                "start_time": 1686224115.0,
                "state": 2,
                "waiting": None,
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011390",
                "result": {
                    "srpm": "tasks/1390/110011390/golang-modernc-file-1.0.8-1.fc39.src.rpm",
                    "logs": [
                        "tasks/1390/110011390/hw_info.log",
                        "tasks/1390/110011390/state.log",
                        "tasks/1390/110011390/build.log",
                        "tasks/1390/110011390/root.log",
                    ],
                    "brootid": 42474755,
                    "source": {
                        "source": "golang-modernc-file-1.0.8-1.fc39.src.rpm",
                        "url": "golang-modernc-file-1.0.8-1.fc39.src.rpm",
                    },
                },
                "children": [],
            },
            {
                "arch": "i386",
                "awaited": False,
                "channel_id": 1,
                "completion_time": 1686224344.0,
                "create_time": 1686224240.0,
                "host_id": 567,
                "id": 110011391,
                "label": "i686",
                "method": "buildArch",
                "owner": 5485,
                "parent": 110011389,
                "priority": 49,
                "start_time": 1686224243.0,
                "state": 2,
                "waiting": None,
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011391",
                "result": {
                    "rpms": [
                        "tasks/1391/110011391/golang-modernc-file-devel-1.0.8-1.fc39.noarch.rpm"
                    ],
                    "srpms": ["tasks/1391/110011391/golang-modernc-file-1.0.8-1.fc39.src.rpm"],
                    "logs": [
                        "tasks/1391/110011391/hw_info.log",
                        "tasks/1391/110011391/state.log",
                        "tasks/1391/110011391/build.log",
                        "tasks/1391/110011391/root.log",
                        "tasks/1391/110011391/mock_output.log",
                        "tasks/1391/110011391/noarch_rpmdiff.json",
                    ],
                    "brootid": 42474756,
                },
                "children": [],
            },
            {
                "arch": "x86_64",
                "awaited": False,
                "channel_id": 1,
                "completion_time": 1686224347.0,
                "create_time": 1686224240.0,
                "host_id": 568,
                "id": 110011392,
                "label": "x86_64",
                "method": "buildArch",
                "owner": 5485,
                "parent": 110011389,
                "priority": 49,
                "start_time": 1686224248.0,
                "state": 2,
                "waiting": None,
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011392",
                "result": {
                    "rpms": [
                        "tasks/1392/110011392/golang-modernc-file-devel-1.0.8-1.fc39.noarch.rpm"
                    ],
                    "srpms": [],
                    "logs": [
                        "tasks/1392/110011392/hw_info.log",
                        "tasks/1392/110011392/state.log",
                        "tasks/1392/110011392/build.log",
                        "tasks/1392/110011392/root.log",
                        "tasks/1392/110011392/mock_output.log",
                        "tasks/1392/110011392/noarch_rpmdiff.json",
                    ],
                    "brootid": 42474758,
                },
                "children": [],
            },
            {
                "arch": "s390x",
                "awaited": False,
                "channel_id": 1,
                "completion_time": 1686224333.0,
                "create_time": 1686224240.0,
                "host_id": 579,
                "id": 110011395,
                "label": "s390x",
                "method": "buildArch",
                "owner": 5485,
                "parent": 110011389,
                "priority": 49,
                "start_time": 1686224254.0,
                "state": 2,
                "waiting": None,
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011395",
                "result": {
                    "rpms": [
                        "tasks/1395/110011395/golang-modernc-file-devel-1.0.8-1.fc39.noarch.rpm"
                    ],
                    "srpms": [],
                    "logs": [
                        "tasks/1395/110011395/hw_info.log",
                        "tasks/1395/110011395/state.log",
                        "tasks/1395/110011395/build.log",
                        "tasks/1395/110011395/root.log",
                        "tasks/1395/110011395/mock_output.log",
                        "tasks/1395/110011395/noarch_rpmdiff.json",
                    ],
                    "brootid": 42474760,
                },
                "children": [],
            },
            {
                "arch": "ppc64le",
                "awaited": False,
                "channel_id": 1,
                "completion_time": 1686224352.0,
                "create_time": 1686224240.0,
                "host_id": 575,
                "id": 110011394,
                "label": "ppc64le",
                "method": "buildArch",
                "owner": 5485,
                "parent": 110011389,
                "priority": 49,
                "start_time": 1686224243.0,
                "state": 2,
                "waiting": None,
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011394",
                "result": {
                    "rpms": [
                        "tasks/1394/110011394/golang-modernc-file-devel-1.0.8-1.fc39.noarch.rpm"
                    ],
                    "srpms": [],
                    "logs": [
                        "tasks/1394/110011394/hw_info.log",
                        "tasks/1394/110011394/state.log",
                        "tasks/1394/110011394/build.log",
                        "tasks/1394/110011394/root.log",
                        "tasks/1394/110011394/mock_output.log",
                        "tasks/1394/110011394/noarch_rpmdiff.json",
                    ],
                    "brootid": 42474757,
                },
                "children": [],
            },
            {
                "arch": "aarch64",
                "awaited": False,
                "channel_id": 1,
                "completion_time": 1686224426.0,
                "create_time": 1686224240.0,
                "host_id": 571,
                "id": 110011393,
                "label": "aarch64",
                "method": "buildArch",
                "owner": 5485,
                "parent": 110011389,
                "priority": 49,
                "start_time": 1686224249.0,
                "state": 2,
                "waiting": None,
                "host_name": "builder.example.com",
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011393",
                "result": {
                    "rpms": [
                        "tasks/1393/110011393/golang-modernc-file-devel-1.0.8-1.fc39.noarch.rpm"
                    ],
                    "srpms": [],
                    "logs": [
                        "tasks/1393/110011393/hw_info.log",
                        "tasks/1393/110011393/state.log",
                        "tasks/1393/110011393/build.log",
                        "tasks/1393/110011393/root.log",
                        "tasks/1393/110011393/mock_output.log",
                        "tasks/1393/110011393/noarch_rpmdiff.json",
                    ],
                    "brootid": 42474759,
                },
                "children": [],
            },
        ],
    },
    "method": "build",
    "attribute": "state",
    "old": "OPEN",
    "new": "CLOSED",
    "id": 110011389,
    "srpm": "golang-modernc-file-1.0.8-1.fc38.src.rpm",
    "owner": "dummy-user",
    "instance": "primary",
}


@pytest.mark.parametrize("event", ("open", "close", "cancel", "fail"))
def test_simple(module, event):
    run_callbacks("postTaskStateChange", **TEST_DATA[event]["kws"])
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "task.state.change", "msg": TEST_DATA[event]["msg"]}


def test_with_subtasks(module):
    # Prepare the subtasks: remove what the plugin will generate
    subtasks = deepcopy(CLOSE_WITH_SUBTASKS_MSG["info"]["children"])
    for subt in subtasks:
        del subt["host_name"]
        del subt["url"]
        del subt["result"]
        del subt["children"]

    # Create tasks with subtasks when relevant
    _create_task = module["kojihub"].Task.side_effect

    def _create_task_with_subtasks(task_id):
        t = _create_task(task_id)
        t.getChildren.side_effect = lambda: subtasks if task_id == 110011389 else []

        # Fill the tasks results with what's expected
        def _get_result():
            subtask_ids = [t["id"] for t in subtasks]
            try:
                task_index = subtask_ids.index(task_id)
            except ValueError:
                return None
            return CLOSE_WITH_SUBTASKS_MSG["info"]["children"][task_index]["result"]

        t.getResult.side_effect = _get_result
        return t

    module["kojihub"].Task.side_effect = _create_task_with_subtasks
    run_callbacks("postTaskStateChange", **CLOSE_WITH_SUBTASKS_KWS)
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "task.state.change", "msg": CLOSE_WITH_SUBTASKS_MSG}


def test_no_publish_child_tasks(module):
    child_task = {
        "attribute": "state",
        "info": {
            "parent": 42,
        },
    }
    run_callbacks("postTaskStateChange", **child_task)
    assert not hasattr(context, "fedmsg_plugin_messages")


def test_only_publish_state_changes(module):
    not_a_state_change = {
        "attribute": "something-else",
    }
    run_callbacks("postTaskStateChange", **not_a_state_change)
    assert not hasattr(context, "fedmsg_plugin_messages")
