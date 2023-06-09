import datetime

import pytest
from koji.context import context
from koji.plugin import run_callbacks

TEST_DATA = {
    "start": {
        "kws": {
            "attribute": "state",
            "old": None,
            "new": 0,
            "info": {
                "build_id": 2211149,
                "cg_id": None,
                "completion_time": None,
                "completion_ts": None,
                "creation_event_id": 112309638,
                "creation_time": datetime.datetime(
                    2023, 6, 9, 8, 15, 54, 546350, tzinfo=datetime.timezone.utc
                ),
                "epoch": 0,
                "extra": None,
                "id": 2211149,
                "name": "Fedora-Cloud-Base-Vagrant",
                "nvr": "Fedora-Cloud-Base-Vagrant-37-20230609.0",
                "owner_id": 3445,
                "owner_name": "releng",
                "package_id": 21548,
                "package_name": "Fedora-Cloud-Base-Vagrant",
                "release": "20230609.0",
                "source": None,
                "start_time": datetime.datetime(
                    2023, 6, 9, 8, 15, 54, 513035, tzinfo=datetime.timezone.utc
                ),
                "start_ts": 1686298554.513035,
                "state": 0,
                "task_id": 101963955,
                "version": "37",
                "volume_id": 0,
                "volume_name": "DEFAULT",
                "cg_name": None,
            },
        },
        "msg": {
            "base_url": "https://koji.stg.fedoraproject.org",
            "files_base_url": "http://files.example.com/work",
            "name": "Fedora-Cloud-Base-Vagrant",
            "version": "37",
            "release": "20230609.0",
            "epoch": 0,
            "attribute": "state",
            "old": None,
            "new": 0,
            "build_id": 2211149,
            "url": "https://koji.stg.fedoraproject.org/koji/buildinfo?buildID=2211149",
            "task_id": 101963955,
            "request": (
                "Fedora-Cloud-Base-Vagrant",
                "38",
            ),
            "owner": "releng",
            "instance": "primary",
            "completion_time": None,
            "creation_time": "2023-06-09T08:15:54.546350+00:00",
            "task": {
                "children": [],
                "host_name": None,
                "id": 110011364,
                "owner": "dummy-user",
                "request": ("Fedora-Cloud-Base-Vagrant", "38"),
                "result": None,
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011364",
            },
        },
    },
    "complete": {
        "kws": {
            "attribute": "state",
            "old": 0,
            "new": 1,
            "info": {
                "build_id": 2211083,
                "cg_id": None,
                "completion_time": datetime.datetime(
                    2023, 6, 9, 7, 32, 16, 160696, tzinfo=datetime.timezone.utc
                ),
                "completion_ts": 1686295936.160696,
                "creation_event_id": 112308010,
                "creation_time": datetime.datetime(
                    2023, 6, 9, 7, 17, 25, 397820, tzinfo=datetime.timezone.utc
                ),
                "epoch": None,
                "extra": {
                    "source": {
                        "original_url": "git+https://src.fedoraproject.org/rpms/grep.git#799f88f953393ea45f722b71669744948c12a422"
                    }
                },
                "id": 2211083,
                "name": "grep",
                "nvr": "grep-3.11-1.fc39",
                "owner_id": 1289,
                "owner_name": "jskarvad",
                "package_id": 1023,
                "package_name": "grep",
                "release": "1.fc39",
                "source": "git+https://src.fedoraproject.org/rpms/grep.git#799f88f953393ea45f722b71669744948c12a422",
                "start_time": datetime.datetime(
                    2023, 6, 9, 7, 17, 25, 386593, tzinfo=datetime.timezone.utc
                ),
                "start_ts": 1686295045.386593,
                "state": 1,
                "task_id": 101962689,
                "version": "3.11",
                "volume_id": 0,
                "volume_name": "DEFAULT",
                "cg_name": None,
            },
        },
        "msg": {
            "base_url": "https://koji.stg.fedoraproject.org",
            "files_base_url": "http://files.example.com/work",
            "name": "grep",
            "version": "3.11",
            "release": "1.fc39",
            "epoch": None,
            "attribute": "state",
            "old": 0,
            "new": 1,
            "build_id": 2211083,
            "url": "https://koji.stg.fedoraproject.org/koji/buildinfo?buildID=2211083",
            "task_id": 101962689,
            "request": (
                "git+https://src.fedoraproject.org/rpms/grep.git#799f88f953393ea45f722b71669744948c12a422",
                "rawhide",
                {},
            ),
            "owner": "jskarvad",
            "instance": "primary",
            "completion_time": "2023-06-09T07:32:16.160696+00:00",
            "creation_time": "2023-06-09T07:17:25.397820+00:00",
            "task": {
                "children": [],
                "host_name": None,
                "id": 110011364,
                "owner": "dummy-user",
                "request": (
                    "git+https://src.fedoraproject.org/rpms/grep.git#799f88f953393ea45f722b71669744948c12a422",
                    "rawhide",
                    {},
                ),
                "result": None,
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011364",
            },
        },
    },
    "image": {
        "kws": {
            "attribute": "state",
            "old": 0,
            "new": 1,
            "info": {
                "build_id": 2211103,
                "cg_id": None,
                "completion_time": datetime.datetime(
                    2023, 6, 9, 7, 31, 20, 218065, tzinfo=datetime.timezone.utc
                ),
                "completion_ts": 1686295880.218065,
                "creation_event_id": 112308004,
                "creation_time": datetime.datetime(
                    2023, 6, 9, 7, 17, 4, 429699, tzinfo=datetime.timezone.utc
                ),
                "epoch": 0,
                "extra": None,
                "id": 2211103,
                "name": "Fedora-Cloud-Base-Vagrant",
                "nvr": "Fedora-Cloud-Base-Vagrant-38-20230609.0",
                "owner_id": 3445,
                "owner_name": "releng",
                "package_id": 21548,
                "package_name": "Fedora-Cloud-Base-Vagrant",
                "release": "20230609.0",
                "source": None,
                "start_time": datetime.datetime(
                    2023, 6, 9, 7, 17, 4, 385898, tzinfo=datetime.timezone.utc
                ),
                "start_ts": 1686295024.385898,
                "state": 1,
                "task_id": 101962703,
                "version": "38",
                "volume_id": 0,
                "volume_name": "DEFAULT",
                "cg_name": None,
            },
        },
        "msg": {
            "base_url": "https://koji.stg.fedoraproject.org",
            "files_base_url": "http://files.example.com/work",
            "name": "Fedora-Cloud-Base-Vagrant",
            "version": "38",
            "release": "20230609.0",
            "epoch": 0,
            "attribute": "state",
            "old": 0,
            "new": 1,
            "build_id": 2211103,
            "url": "https://koji.stg.fedoraproject.org/koji/buildinfo?buildID=2211103",
            "task_id": 101962703,
            "completion_time": "2023-06-09T07:31:20.218065+00:00",
            "creation_time": "2023-06-09T07:17:04.429699+00:00",
            "request": (
                "Fedora-Cloud-Base-Vagrant",
                "38",
            ),
            "owner": "releng",
            "instance": "primary",
            "task": {
                "children": [],
                "host_name": None,
                "id": 110011364,
                "owner": "dummy-user",
                "request": ("Fedora-Cloud-Base-Vagrant", "38"),
                "result": None,
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011364",
            },
        },
    },
    "fail": {
        "kws": {
            "attribute": "state",
            "old": 0,
            "new": 3,
            "info": {
                "build_id": 2211099,
                "cg_id": None,
                "completion_time": datetime.datetime(
                    2023, 6, 9, 7, 31, 20, 250419, tzinfo=datetime.timezone.utc
                ),
                "completion_ts": 1686295880.250419,
                "creation_event_id": 112307255,
                "creation_time": datetime.datetime(
                    2023, 6, 9, 6, 45, 50, 418152, tzinfo=datetime.timezone.utc
                ),
                "epoch": 0,
                "extra": None,
                "id": 2211099,
                "name": "Fedora-Container-Minimal-Base",
                "nvr": "Fedora-Container-Minimal-Base-38-20230609.0",
                "owner_id": 3445,
                "owner_name": "releng",
                "package_id": 23806,
                "package_name": "Fedora-Container-Minimal-Base",
                "release": "20230609.0",
                "source": None,
                "start_time": datetime.datetime(
                    2023, 6, 9, 6, 45, 50, 399675, tzinfo=datetime.timezone.utc
                ),
                "start_ts": 1686293150.399675,
                "state": 3,
                "task_id": 101962163,
                "version": "38",
                "volume_id": 0,
                "volume_name": "DEFAULT",
                "cg_name": None,
            },
        },
        "msg": {
            "base_url": "https://koji.stg.fedoraproject.org",
            "files_base_url": "http://files.example.com/work",
            "name": "Fedora-Container-Minimal-Base",
            "version": "38",
            "release": "20230609.0",
            "epoch": 0,
            "attribute": "state",
            "old": 0,
            "new": 3,
            "build_id": 2211099,
            "url": "https://koji.stg.fedoraproject.org/koji/buildinfo?buildID=2211099",
            "task_id": 101962163,
            "completion_time": "2023-06-09T07:31:20.250419+00:00",
            "creation_time": "2023-06-09T06:45:50.418152+00:00",
            "request": (
                "Fedora-Container-Minimal-Base",
                "38",
            ),
            "owner": "releng",
            "instance": "primary",
            "task": {
                "children": [],
                "host_name": None,
                "id": 110011364,
                "owner": "dummy-user",
                "request": ("Fedora-Container-Minimal-Base", "38"),
                "result": None,
                "url": "https://koji.stg.fedoraproject.org/koji/taskinfo?taskID=110011364",
            },
        },
    },
}


@pytest.mark.parametrize("event", ("start", "complete", "image", "fail"))
def test_simple(module, event):
    # Create tasks with subtasks when relevant
    _create_task = module["kojihub"].Task.side_effect

    def _create_task_with_info(task_id):
        t = _create_task(task_id)
        t.getInfo.return_value = {
            "id": 110011364,
            "request": TEST_DATA[event]["msg"]["request"],
            "owner": "dummy-user",
        }
        return t

    module["kojihub"].Task.side_effect = _create_task_with_info

    run_callbacks("postBuildStateChange", **TEST_DATA[event]["kws"])
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "build.state.change", "msg": TEST_DATA[event]["msg"]}
