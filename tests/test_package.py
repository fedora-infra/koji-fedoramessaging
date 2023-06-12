from koji.context import context
from koji.plugin import run_callbacks

TEST_DATA = {
    "kws": {
        "action": "update",
        "tag": {
            "arches": "None",
            "id": 62875,
            "locked": False,
            "maven_include_all": False,
            "maven_support": False,
            "name": "f39",
            "perm": "autosign",
            "perm_id": 17,
            "extra": {"mock.new_chroot": 1, "mock.package_manager": "dnf"},
        },
        "package": {"id": 29829, "name": "nats-server"},
        "owner": 5170,
        "block": False,
        "extra_arches": "",
        "force": True,
        "update": True,
        "user": {
            "id": 428,
            "name": "bodhi",
            "status": 0,
            "usertype": 0,
            "krb_principals": ["bodhi/bodhi.fedoraproject.org@FEDORAPROJECT.ORG"],
        },
    },
    "msg": {
        "base_url": "https://koji.stg.fedoraproject.org",
        "tag": "f39",
        "package": "nats-server",
        "action": "update",
        "owner": "dummy-user",
        "block": False,
        "extra_arches": "",
        "force": True,
        "update": True,
        "instance": "primary",
    },
}


def test_simple(module):
    run_callbacks("postPackageListChange", **TEST_DATA["kws"])
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "package.list.change", "msg": TEST_DATA["msg"]}
