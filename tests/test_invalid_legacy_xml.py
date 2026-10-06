from pathlib import Path

import pytest

from diploma_mec.validation import validate_xsd
from diploma_mec.errors import SchemaValidationError


def test_original_fixture_is_not_accepted():
    root = Path(__file__).resolve().parents[1]
    xml = root / "legacy" / "diploma_teste.xml"
    xsd = root / "schemas" / "DocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd"
    with pytest.raises(SchemaValidationError):
        validate_xsd(xml, xsd)
