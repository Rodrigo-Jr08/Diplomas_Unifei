from __future__ import annotations

import hashlib
from dataclasses import dataclass
from pathlib import Path

from .serialization import serialize_xsdata, write_xml
from .validation import validate_xsd_text


@dataclass(frozen=True)
class XmlArtifact:
    path: Path
    sha256: str
    size: int
    xsd: Path


def generate_and_validate(model: object, *, xsd_path: str | Path, output_path: str | Path) -> XmlArtifact:
    
    xml_bytes = serialize_xsdata(model)
    validate_xsd_text(xml_bytes, xsd_path)
    path = write_xml(xml_bytes, output_path)
    digest = hashlib.sha256(xml_bytes).hexdigest()
    return XmlArtifact(path=path, sha256=digest, size=len(xml_bytes), xsd=Path(xsd_path))
