from koji.context import context
from koji.plugin import run_callbacks

TEST_DATA = {
    "kws": {
        "sigkey": "18b8e74c",
        "sighash": "e7556957058ad918c6264179d3bf5d31",
        "build": {
            "build_id": 2211158,
            "cg_id": None,
            "completion_time": 1686305099.0,
            "completion_ts": 1686305099.577939,
            "creation_event_id": 112310854,
            "creation_time": 1686301750.0,
            "creation_ts": 1686301750.627583,
            "epoch": None,
            "extra": {
                "source": {
                    "original_url": "git+https://src.fedoraproject.org/rpms/erlang.git#91e2729af1ab566845ee13023e2b49fab63b1d9a"
                }
            },
            "id": 2211158,
            "name": "erlang",
            "nvr": "erlang-26.0.1-1.fc39",
            "owner_id": 237,
            "owner_name": "peter",
            "package_id": 1681,
            "package_name": "erlang",
            "release": "1.fc39",
            "source": "git+https://src.fedoraproject.org/rpms/erlang.git#91e2729af1ab566845ee13023e2b49fab63b1d9a",
            "start_time": 1686301750.0,
            "start_ts": 1686301750.551941,
            "state": 1,
            "task_id": 101964746,
            "version": "26.0.1",
            "volume_id": 0,
            "volume_name": "DEFAULT",
            "cg_name": None,
        },
        "rpm": {
            "arch": "ppc64le",
            "build_id": 2211158,
            "buildroot_id": 43372466,
            "buildtime": 1686302220,
            "epoch": None,
            "external_repo_id": 0,
            "external_repo_name": "INTERNAL",
            "extra": None,
            "id": 34707522,
            "metadata_only": False,
            "name": "erlang-ssl",
            "payloadhash": "e76ed0ffd639ab9c6c5bf83b936f3f4a",
            "release": "1.fc39",
            "size": 1973193,
            "version": "26.0.1",
        },
    },
    "msg": {
        "sigkey": "18b8e74c",
        "sighash": "e7556957058ad918c6264179d3bf5d31",
        "base_url": "https://koji.stg.fedoraproject.org",
        "files_base_url": "http://files.example.com/work",
        "build": {
            "build_id": 2211158,
            "cg_id": None,
            "completion_time": 1686305099.0,
            "creation_event_id": 112310854,
            "creation_time": 1686301750.0,
            "creation_ts": 1686301750.627583,
            "epoch": None,
            "extra": {
                "source": {
                    "original_url": "git+https://src.fedoraproject.org/rpms/erlang.git#91e2729af1ab566845ee13023e2b49fab63b1d9a"
                }
            },
            "id": 2211158,
            "name": "erlang",
            "nvr": "erlang-26.0.1-1.fc39",
            "owner_id": 237,
            "owner_name": "peter",
            "package_id": 1681,
            "package_name": "erlang",
            "release": "1.fc39",
            "source": "git+https://src.fedoraproject.org/rpms/erlang.git#91e2729af1ab566845ee13023e2b49fab63b1d9a",
            "start_time": 1686301750.0,
            "state": 1,
            "task_id": 101964746,
            "version": "26.0.1",
            "volume_id": 0,
            "volume_name": "DEFAULT",
            "cg_name": None,
        },
        "rpm": {
            "arch": "ppc64le",
            "build_id": 2211158,
            "buildroot_id": 43372466,
            "buildtime": 1686302220,
            "epoch": None,
            "external_repo_id": 0,
            "external_repo_name": "INTERNAL",
            "extra": None,
            "id": 34707522,
            "metadata_only": False,
            "name": "erlang-ssl",
            "payloadhash": "e76ed0ffd639ab9c6c5bf83b936f3f4a",
            "release": "1.fc39",
            "size": 1973193,
            "version": "26.0.1",
        },
        "instance": "primary",
    },
}


def test_simple(module):
    run_callbacks("postRPMSign", **TEST_DATA["kws"])
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "rpm.sign", "msg": TEST_DATA["msg"]}
