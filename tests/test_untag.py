import datetime

from koji.context import context
from koji.plugin import run_callbacks

TEST_DATA = {
    "kws": {
        "tag": {
            "arches": "",
            "id": 62882,
            "locked": False,
            "maven_include_all": False,
            "maven_support": False,
            "name": "f39-updates-testing-pending",
            "perm": "autosign",
            "perm_id": 17,
            "extra": {},
        },
        "build": {
            "build_id": 2211093,
            "cg_id": None,
            "completion_time": datetime.datetime(
                2023, 6, 9, 5, 55, 9, 530631, tzinfo=datetime.timezone.utc
            ),
            "completion_ts": 1686290109.530631,
            "creation_event_id": 112306142,
            "creation_time": datetime.datetime(
                2023, 6, 9, 5, 53, 40, 458795, tzinfo=datetime.timezone.utc
            ),
            "creation_ts": 1686290020.458795,
            "epoch": None,
            "extra": {
                "source": {
                    "original_url": "git+https://src.fedoraproject.org/rpms/dummy-test-package-gloster.git#9ca702f10b173817e8389e0832fd7505f434015f"
                }
            },
            "id": 2211093,
            "name": "dummy-test-package-gloster",
            "nvr": "dummy-test-package-gloster-0-10383.fc39",
            "owner_id": 5309,
            "owner_name": "packagerbot/os-control01.iad2.fedoraproject.org",
            "package_id": 30489,
            "package_name": "dummy-test-package-gloster",
            "release": "10383.fc39",
            "source": "git+https://src.fedoraproject.org/rpms/dummy-test-package-gloster.git#9ca702f10b173817e8389e0832fd7505f434015f",
            "start_time": datetime.datetime(
                2023, 6, 9, 5, 53, 40, 442810, tzinfo=datetime.timezone.utc
            ),
            "start_ts": 1686290020.44281,
            "state": 1,
            "task_id": 101961218,
            "version": "0",
            "volume_id": 0,
            "volume_name": "DEFAULT",
            "cg_name": None,
        },
        "user": {
            "id": 428,
            "name": "bodhi",
            "status": 0,
            "usertype": 0,
            "krb_principals": ["bodhi/bodhi.fedoraproject.org@FEDORAPROJECT.ORG"],
        },
        "force": True,
        "strict": True,
    },
    "msg": {
        "tag": "f39-updates-testing-pending",
        "name": "dummy-test-package-gloster",
        "version": "0",
        "release": "10383.fc39",
        "user": "bodhi",
        "owner": "dummy-user",
        "tag_id": 62882,
        "build_id": 2211093,
        "instance": "primary",
        "base_url": "https://koji.stg.fedoraproject.org",
    },
}


def test_simple(module):
    run_callbacks("postUntag", **TEST_DATA["kws"])
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "untag", "msg": TEST_DATA["msg"]}
