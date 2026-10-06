from __future__ import annotations

from pathlib import Path

from lxml import etree

from .constants import DS_NAMESPACE, MEC_NAMESPACE


def _clone_without_mec_prefix(node: etree._Element, is_root: bool = False) -> etree._Element:
    q = etree.QName(node)
    if q.namespace in (MEC_NAMESPACE, DS_NAMESPACE):
        tag = f"{{{q.namespace}}}{q.localname}"
    else:
        tag = node.tag

    if q.namespace == DS_NAMESPACE and q.localname == "Signature":
        nsmap = {None: DS_NAMESPACE}
    elif is_root:
        nsmap = {None: MEC_NAMESPACE}
    else:
        nsmap = None

    out = etree.Element(tag, nsmap=nsmap)
    for key, value in node.attrib.items():
        out.set(key, value)
    out.text = node.text
    out.tail = node.tail
    for child in node:
        out.append(_clone_without_mec_prefix(child))
    return out


def normalize_namespaces(xml_bytes: bytes) -> bytes:
    """Normaliza o namespace MEC para default e declara DS no próprio Signature."""
    root = etree.fromstring(xml_bytes)
    normalized = _clone_without_mec_prefix(root, is_root=True)
    return etree.tostring(
        normalized,
        encoding="UTF-8",
        xml_declaration=True,
        pretty_print=False,
    )


def serialize_xsdata(model: object) -> bytes:
    """Serializa um modelo xsdata sem indentação/whitespace de formatação."""
    try:
        from xsdata.formats.dataclass.serializers import XmlSerializer
        from xsdata.formats.dataclass.serializers.config import SerializerConfig
    except ImportError as exc:  # pragma: no cover - ambiente sem dependência opcional
        raise RuntimeError(
            "xsdata não está instalado. Execute `pip install -e .[dev]`."
        ) from exc

    serializer = XmlSerializer(config=SerializerConfig(pretty_print=False))
    xml = serializer.render(model, ns_map={None: MEC_NAMESPACE})
    return normalize_namespaces(xml.encode("utf-8"))


def write_xml(xml_bytes: bytes, path: str | Path) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(xml_bytes)
    return path
