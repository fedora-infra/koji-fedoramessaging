from koji.context import context
from koji.plugin import run_callbacks

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
        "files_base_url": "http://files.example.com/work",
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
