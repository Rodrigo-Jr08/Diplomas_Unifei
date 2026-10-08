from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from lxml import etree

from .errors import SchemaValidationError


def _parser() -> etree.XMLParser:
    return etree.XMLParser(
        no_network=True,
        resolve_entities=False,
        load_dtd=False,
        remove_blank_text=False,
        huge_tree=False,
    )


@lru_cache(maxsize=32)
def load_schema(xsd_path: str) -> etree.XMLSchema:
    path = Path(xsd_path).resolve()

    if not path.exists():
        raise SchemaValidationError(f"XSD não encontrado: {path}")
    try:
        doc = etree.parse(str(path), _parser())
        return etree.XMLSchema(doc)
    except (OSError, etree.XMLSchemaParseError, etree.XMLSyntaxError) as exc:
        raise SchemaValidationError(f"Não foi possível carregar/compilar o XSD {path}: {exc}") from exc


def validate_xsd(xml_path: str | Path, xsd_path: str | Path) -> None:
    xml_path = Path(xml_path).resolve()
    schema = load_schema(str(Path(xsd_path).resolve()))
    try:
        document = etree.parse(str(xml_path), _parser())
        schema.assertValid(document)
    except (OSError, etree.XMLSyntaxError) as exc:
        raise SchemaValidationError(f"XML inválido ou ilegível: {xml_path}: {exc}") from exc
    except etree.DocumentInvalid as exc:
        details = "\n".join(
            f"linha {e.line}: {e.message}" for e in schema.error_log
        )
        raise SchemaValidationError(
            f"XML não atende ao XSD {xsd_path}:\n{details}"
        ) from exc


def validate_xsd_text(xml_bytes: bytes, xsd_path: str | Path) -> None:
    schema = load_schema(str(Path(xsd_path).resolve()))
    try:
        root = etree.fromstring(xml_bytes, parser=_parser())
        schema.assertValid(root)
    except etree.DocumentInvalid as exc:
        details = "\n".join(
            f"linha {e.line}: {e.message}" for e in schema.error_log
        )
        raise SchemaValidationError(
            f"XML não atende ao XSD {xsd_path}:\n{details}"
        ) from exc
    except etree.XMLSyntaxError as exc:
        raise SchemaValidationError(f"XML malformado: {exc}") from exc


def is_xsd_valid(xml_path: str | Path, xsd_path: str | Path) -> bool:
    try:
        validate_xsd(xml_path, xsd_path)
        return True
    except SchemaValidationError:
        return False
