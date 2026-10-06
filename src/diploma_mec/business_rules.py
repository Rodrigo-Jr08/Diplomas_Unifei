from __future__ import annotations

import re
from typing import Any

from .errors import BusinessRuleError
from .ids import DIPLOMA_ID_RE, REGISTRATION_ID_RE, REQUEST_ID_RE, VALIDATION_CODE_RE, VIRTUAL_ID_RE


def exactly_one(*values: Any, labels: tuple[str, ...] | None = None) -> int:
    count = sum(v is not None for v in values)
    if count != 1:
        names = labels or tuple(f"opção {i+1}" for i in range(len(values)))
        raise BusinessRuleError(
            "Exatamente uma alternativa deve ser preenchida: " + ", ".join(names)
        )
    return count


def validate_id_family(*, virtual_id: str, diploma_id: str, registration_id: str, request_id: str) -> None:
    checks = {
        "VDip": (virtual_id, VIRTUAL_ID_RE),
        "Dip": (diploma_id, DIPLOMA_ID_RE),
        "RDip": (registration_id, REGISTRATION_ID_RE),
        "ReqDip": (request_id, REQUEST_ID_RE),
    }
    for label, (value, pattern) in checks.items():
        if not pattern.fullmatch(value):
            raise BusinessRuleError(f"Identificador {label} inválido: {value!r}")

    suffixes = [virtual_id[4:], diploma_id[3:], registration_id[4:], request_id[6:]]
    if len(set(suffixes)) != 1:
        raise BusinessRuleError("VDip, Dip, RDip e ReqDip devem compartilhar o mesmo NONCE.")


def validate_validation_code(code: str) -> None:
    if not VALIDATION_CODE_RE.fullmatch(code):
        raise BusinessRuleError(
            "Código de validação deve seguir e-MEC emissora.e-MEC registradora.hexadecimal."
        )


def validate_https_url(url: str) -> None:
    if not url.startswith("https://"):
        raise BusinessRuleError("URL pública deve utilizar HTTPS.")
    if len(url) > 255:
        raise BusinessRuleError("URL pública deve ter no máximo 255 caracteres.")
