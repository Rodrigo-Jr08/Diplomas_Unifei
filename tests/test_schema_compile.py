from pathlib import Path

from lxml import etree


def test_local_xsds_compile():
    root = Path(__file__).resolve().parents[1] / "schemas"
    parser = etree.XMLParser(no_network=True, resolve_entities=False, load_dtd=False)
    xsds = sorted(root.glob("*.xsd"))
    assert xsds
    for path in xsds:
        document = etree.parse(str(path), parser)
        etree.XMLSchema(document)
