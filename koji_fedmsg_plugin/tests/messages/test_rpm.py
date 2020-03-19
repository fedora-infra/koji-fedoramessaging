from koji_fedmsg_plugin.messages.rpm import SignV1


def test_rpm_sign_message():

    body = {
        "instance": "primary",
        "sigkey": "12c944d0",
        "rpm": {
            "build_id": 1478177,
            "name": "wine-opencl-debuginfo",
            "extra": None,
            "arch": "aarch64",
            "buildtime": 1584471339,
            "id": 20905366,
            "epoch": None,
            "version": "5.4",
            "metadata_only": False,
            "external_repo_id": 0,
            "release": "1.fc32",
            "size": 39178,
            "buildroot_id": 19890121,
            "external_repo_name": "INTERNAL",
            "payloadhash": "61affc5b3f9600cd0ade2126779abf62",
        },
        "build": {
            "cg_id": None,
            "package_name": "wine",
            "extra": {
                "source": {
                    "original_url": "git+https://src.fedoraproject.org/rpms/wine.git#f83582e8bcf2cbd1eaf693356cfc24731ab85e3f"
                }
            },
            "creation_time": 1584471219.0,
            "completion_time": 1584473659.0,
            "package_id": 4106,
            "cg_name": None,
            "id": 1478177,
            "build_id": 1478177,
            "epoch": None,
            "source": "git+https://src.fedoraproject.org/rpms/wine.git#f83582e8bcf2cbd1eaf693356cfc24731ab85e3f",
            "state": 1,
            "version": "5.4",
            "owner_id": 895,
            "owner_name": "mooninite",
            "nvr": "wine-5.4-1.fc32",
            "start_time": 1584471219.0,
            "creation_event_id": 53216169,
            "volume_id": 0,
            "creation_ts": 1584471219.82997,
            "name": "wine",
            "task_id": 42567650,
            "volume_name": "DEFAULT",
            "release": "1.fc32",
        },
        "sighash": "a1957f36d34d29c105f16aae79b19e85",
    }

    msg = SignV1(body=body)
    msg.validate()
    assert msg.sigkey == "12c944d0"
    assert msg.rpm["name"] == "wine-opencl-debuginfo"
    assert msg.build["package_name"] == "wine"
