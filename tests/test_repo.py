from koji.context import context
from koji.plugin import run_callbacks

kws = {
    "tag": {
        "arches": "aarch64 ppc64le s390x x86_64",
        "id": 10327,
        "locked": False,
        "maven_include_all": False,
        "maven_support": False,
        "name": "epel8-infra-build",
        "perm": "infra",
        "perm_id": 15,
        "extra": {"rpm.macro.dist": ".%{?fedora:fc%{fedora}}%{?rhel:el%{rhel}}.infra"},
    },
    "with_src": False,
    "with_debuginfo": False,
    "event": None,
    "repo_id": 9001678,
    "with_separate_src": False,
    "task_id": 110011335,
}


kws = {
    "tag": {
        "arches": "aarch64 ppc64le s390x x86_64",
        "id": 10316,
        "locked": False,
        "maven_include_all": False,
        "maven_support": False,
        "name": "epel8-build",
        "perm": "admin",
        "perm_id": 1,
        "extra": {"module_hotfixes": 1},
    },
    "with_src": False,
    "with_debuginfo": False,
    "event": None,
    "repo_id": 9001676,
    "with_separate_src": False,
    "task_id": 110011333,
}

kws = (
    {
        "tag": {
            "arches": "aarch64 ppc64le s390x x86_64",
            "id": 66810,
            "locked": False,
            "maven_include_all": False,
            "maven_support": False,
            "name": "epel8-build-side-66810",
            "perm": None,
            "perm_id": None,
            "extra": {
                "sidetag": True,
                "sidetag_user": "iucar",
                "sidetag_user_id": 4209,
            },
        },
        "with_src": False,
        "with_debuginfo": False,
        "event": None,
        "repo_id": 9001677,
        "with_separate_src": False,
        "task_id": 110011334,
    },
)

TEST_DATA = {
    "kws": {
        "tag": {
            "arches": "x86_64 ppc64 ppc64le aarch64",
            "id": 409,
            "locked": False,
            "maven_include_all": False,
            "maven_support": False,
            "name": "epel7-infra-mailman",
            "perm": "autosign",
            "perm_id": 17,
            "extra": {},
        },
        "with_src": False,
        "with_debuginfo": False,
        "event": None,
        "repo_id": 9001680,
        "with_separate_src": False,
        "task_id": 110011401,
    },
    "msg": {
        "base_url": "https://koji.stg.fedoraproject.org",
        "tag": "epel7-infra-mailman",
        "tag_id": 409,
        "repo_id": 9001680,
        "instance": "primary",
    },
}


def test_simple(module):
    run_callbacks("postRepoInit", **TEST_DATA["kws"])
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "repo.init", "msg": TEST_DATA["msg"]}
