import pytest
from koji.context import context
from koji.plugin import run_callbacks

KWS = {
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
}


def test_default_instance(module):
    assert module["get_instance"]() == "primary"


@pytest.mark.parametrize("fm_config", [{"koji_instance": "ppc"}], indirect=True)
def test_configured_instance(module):
    assert module["get_instance"]() == "ppc"


@pytest.mark.parametrize("fm_config", [{"koji_instance": "s390"}], indirect=True)
def test_configured_instance_in_message(module):
    run_callbacks("postRepoInit", **KWS)
    assert len(context.fedmsg_plugin_messages) == 1
    assert context.fedmsg_plugin_messages[0]["msg"]["instance"] == "s390"
