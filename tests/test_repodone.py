import datetime

from koji.context import context
from koji.plugin import run_callbacks

TEST_DATA = {
    "kws": {
        "repo": {
            "create_event": 112308041,
            "create_ts": 1686295235.59291,
            "creation_time": datetime.datetime(
                2023, 6, 9, 7, 20, 35, 592910, tzinfo=datetime.timezone.utc
            ),
            "dist": False,
            "id": 5216957,
            "state": 0,
            "tag_id": 22493,
            "tag_name": "eln-build",
            "task_id": 101962739,
        },
        "data": {
            "src": [
                "tasks/2778/101962778",
                [
                    "3badaa17bf7f75730c28e46f35fc34cb3b211460a42e7568ba1dcb8a8fd71690-primary.xml.gz",
                    "a1a1e3e007e990b2b8177b9ada9a2ccd9c06aba5376007c273e3d010f1fa9c09-filelists.xml.gz",
                    "598c7679c72180c834ea80c7765dcbb15b13bbeccc10fc2f87daa7e09e9de92b-other.xml.gz",
                    "ba3af1324ab05f8ff8b35bf4a85713ed281523b09c6542a067b04ae73bf4e837-primary.sqlite.bz2",
                    "e8fb023500f64aba1921241879ea4e11d48a412d1f7c7d48a186e421d81c844e-filelists.sqlite.bz2",
                    "c54753019e02fe834c423ecd996e6aef391691461bd932ec406f635640f3ebe5-other.sqlite.bz2",
                    "f8dd440000f60f41daae9281d79989c77492d132fd712e786e0527ac70f3b1e5-comps.xml.gz",
                    "6e8d253941b329d7b812b0b363bfe84435b9bf00f67630805412cab8fa3d2133-comps.xml",
                    "repomd.xml",
                ],
            ],
            "i386": [
                "tasks/2779/101962779",
                [
                    "a0fa3b25835bc8886a2c084726d7c040a3aa2eaf3472cdaa7035d6cd4a5aefb1-primary.xml.gz",
                    "8f6b9eeff0de044c19f172ed444713afb62fd1659d93493bc131f8159b62df98-filelists.xml.gz",
                    "cee8257c019ea1feeb6a7c167a9ffdd9a6bc0c7ccc44361dbaae8f348ec64c2e-other.xml.gz",
                    "6256aa1c5a268c30b6e2e9c4496bfbea3167c4df06096cf3cbb70237064bded4-primary.sqlite.bz2",
                    "30d207a094706350e4cf5122b4142524d1e8e1796bbc4274eee3a0eed3e54332-filelists.sqlite.bz2",
                    "1229053565bc1c04f857eb70023d1982e6c151d4959cd87588b2a1180e9ece28-other.sqlite.bz2",
                    "f8dd440000f60f41daae9281d79989c77492d132fd712e786e0527ac70f3b1e5-comps.xml.gz",
                    "6e8d253941b329d7b812b0b363bfe84435b9bf00f67630805412cab8fa3d2133-comps.xml",
                    "repomd.xml",
                ],
            ],
            "x86_64": [
                "tasks/2780/101962780",
                [
                    "1bd32560dd5d7b45cbe6515a839ebf9e74b102745f510377f5d571d5fd5622cd-primary.xml.gz",
                    "60f603a3c04af2326eaa9e56e3027ef2099a227c2449bfee12870392cfaea0a2-filelists.xml.gz",
                    "1d741a27c02d097f68622b271b139d1d565d5f492f37a14bd960889d1e4f5b53-other.xml.gz",
                    "3f33657e839fa38ea461da046e75312e8e4675b4a9ac073569b848e104ccfd03-primary.sqlite.bz2",
                    "5e82fe723ce78bf8a56a06152c2816d8986815bb6ee36c891c4c01db21468b6b-filelists.sqlite.bz2",
                    "fda5816022ff543a509d1ca0307ff96f41c056e2c8d0ed7e08800665229d4dee-other.sqlite.bz2",
                    "f8dd440000f60f41daae9281d79989c77492d132fd712e786e0527ac70f3b1e5-comps.xml.gz",
                    "6e8d253941b329d7b812b0b363bfe84435b9bf00f67630805412cab8fa3d2133-comps.xml",
                    "repomd.xml",
                ],
            ],
            "aarch64": [
                "tasks/2781/101962781",
                [
                    "52c67fd4b5f4d70dad82c7d68bddec2a6a13cea8ca752d245407576e29fa103b-primary.xml.gz",
                    "c3de13813035761e6a8d2a93e2f164217668ff9935f85e480707501dcfd38e05-filelists.xml.gz",
                    "5f9e02c8636685c5c2711505d595c60647a28ed89de00f5434ee697b17d09b24-other.xml.gz",
                    "08d9d91598485785fcbfc09f667d07caa59ff943636cb3b477e79507b562737e-primary.sqlite.bz2",
                    "fc995c50236352b4ef9a9c03737a35969c027c6cb7ad1d3186bb5785a60a7a56-filelists.sqlite.bz2",
                    "fb3fc440abe1ed4821803bf57d92a6a9d1db3ac8fa848185d8a306308bc98222-other.sqlite.bz2",
                    "f8dd440000f60f41daae9281d79989c77492d132fd712e786e0527ac70f3b1e5-comps.xml.gz",
                    "6e8d253941b329d7b812b0b363bfe84435b9bf00f67630805412cab8fa3d2133-comps.xml",
                    "repomd.xml",
                ],
            ],
            "ppc64le": [
                "tasks/2782/101962782",
                [
                    "45230449d26e0eee4488df9af91c6fcaec5906a9f64f24ce672d31f5bd77dfc1-primary.xml.gz",
                    "165bad4c8d9c060fdb2b1545dea9455d998dc5be3306b79c02d816e7e7e27c27-filelists.xml.gz",
                    "a184f68f663b91b0c85e6d0e867494a4d80a8c1a71d186652ea9b9dd1c3cc91e-other.xml.gz",
                    "12288c64b9c72beb0e9870b8241480ea8dd681040288213f6b60c0dde4469f84-primary.sqlite.bz2",
                    "28b3e7ce2ca29b71f220feff44014ea52b40cfe4a6c15a6a9761b32f2edc6c16-filelists.sqlite.bz2",
                    "0092c37529d470b5fd00ee2255eefd5ebb61ce0bdfca0d51710c7bd97d1836d0-other.sqlite.bz2",
                    "f8dd440000f60f41daae9281d79989c77492d132fd712e786e0527ac70f3b1e5-comps.xml.gz",
                    "6e8d253941b329d7b812b0b363bfe84435b9bf00f67630805412cab8fa3d2133-comps.xml",
                    "repomd.xml",
                ],
            ],
            "s390x": [
                "tasks/2783/101962783",
                [
                    "7a058a0d48e917f5f24c3ba29f85d6d00b9b6f81f07137f667a7725ce2a70843-primary.xml.gz",
                    "c55fd50a6db25fde816264040ed6ed2879002fbba1a3ad142fbe3419b6229e8a-filelists.xml.gz",
                    "e3066877214d747b6f58bcfdf1f9cfeb2e8eb4cc966f19e43ff904d4bef0a5f4-other.xml.gz",
                    "9ec868b2417e7b5b1ce02dde3b8767d69f41eb704dbd1c2cedb6b7cd73b4603c-primary.sqlite.bz2",
                    "5fec2f03d847043dfb4227ba794ead02f5f7cfaf9109fd75a903fe5a10d34c57-filelists.sqlite.bz2",
                    "57d7534704c2185e2c3b3df2c5eaedcc4c94c5dc617ea9b5f109705fb89a43a3-other.sqlite.bz2",
                    "f8dd440000f60f41daae9281d79989c77492d132fd712e786e0527ac70f3b1e5-comps.xml.gz",
                    "6e8d253941b329d7b812b0b363bfe84435b9bf00f67630805412cab8fa3d2133-comps.xml",
                    "repomd.xml",
                ],
            ],
        },
        "expire": False,
    },
    "msg": {
        "tag": "eln-build",
        "tag_id": 22493,
        "repo_id": 5216957,
        "instance": "primary",
        "base_url": "https://koji.stg.fedoraproject.org",
    },
}


def test_simple(module):
    run_callbacks("postRepoDone", **TEST_DATA["kws"])
    assert len(context.fedmsg_plugin_messages) == 1
    msg = context.fedmsg_plugin_messages[0]
    assert msg == {"topic": "repo.done", "msg": TEST_DATA["msg"]}
