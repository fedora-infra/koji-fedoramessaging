import datetime

from koji.context import context
from koji.plugin import run_callbacks

TEST_DATA = {
    "kws": {
        "tag": {
            "arches": "aarch64 ppc64le s390x x86_64",
            "id": 68659,
            "locked": False,
            "maven_include_all": False,
            "maven_support": False,
            "name": "epel9-build-side-68659",
            "perm": None,
            "perm_id": None,
            "extra": {"sidetag": True, "sidetag_user": "ppisar", "sidetag_user_id": 1374},
        },
        "build": {
            "build_id": 2209268,
            "cg_id": None,
            "completion_time": datetime.datetime(
                2023, 6, 5, 14, 26, 48, 849836, tzinfo=datetime.timezone.utc
            ),
            "completion_ts": 1685975208.849836,
            "creation_event_id": 112163521,
            "creation_time": datetime.datetime(
                2023, 6, 5, 14, 25, 3, 570381, tzinfo=datetime.timezone.utc
            ),
            "creation_ts": 1685975103.570381,
            "epoch": None,
            "extra": {
                "source": {
                    "original_url": "git+https://src.fedoraproject.org/rpms/perl-GooCanvas2.git#e0e48a67b2e9cbedbcb69cb670aeb8c37810e1b5"
                }
            },
            "id": 2209268,
            "name": "perl-GooCanvas2",
            "nvr": "perl-GooCanvas2-0.06-17.el9",
            "owner_id": 1374,
            "owner_name": "ppisar",
            "package_id": 26487,
            "package_name": "perl-GooCanvas2",
            "release": "17.el9",
            "source": "git+https://src.fedoraproject.org/rpms/perl-GooCanvas2.git#e0e48a67b2e9cbedbcb69cb670aeb8c37810e1b5",
            "start_time": datetime.datetime(
                2023, 6, 5, 14, 25, 3, 564749, tzinfo=datetime.timezone.utc
            ),
            "start_ts": 1685975103.564749,
            "state": 1,
            "task_id": 101838875,
            "version": "0.06",
            "volume_id": 0,
            "volume_name": "DEFAULT",
            "cg_name": None,
        },
        "user": {"id": 1374, "name": "ppisar", "status": 0, "usertype": 0, "krb_principals": []},
        "force": None,
    },
    "msg": {
        "tag": "epel9-build-side-68659",
        "name": "perl-GooCanvas2",
        "version": "0.06",
        "release": "17.el9",
        "user": "ppisar",
        "owner": "dummy-user",
        "tag_id": 68659,
        "build_id": 2209268,
        "instance": "primary",
        "base_url": "https://koji.stg.fedoraproject.org",
    },
}


def test_simple(module):
    run_callbacks("postTag", **TEST_DATA["kws"])
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "tag", "msg": TEST_DATA["msg"]}
