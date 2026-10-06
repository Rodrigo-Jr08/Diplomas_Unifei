from __future__ import annotations

import re
import secrets
from dataclasses import dataclass

NONCE_RE = re.compile(r"^[0-9]{44}$")
ID_PREFIXES = ("VDip", "Dip", "RDip", "ReqDip")
REQUEST_ID_RE = re.compile(r"^ReqDip[0-9]{44}$")
DIPLOMA_ID_RE = re.compile(r"^Dip[0-9]{44}$")
REGISTRATION_ID_RE = re.compile(r"^RDip[0-9]{44}$")
VIRTUAL_ID_RE = re.compile(r"^VDip[0-9]{44}$")
VALIDATION_CODE_RE = re.compile(r"^[0-9]+\.[0-9]+\.[a-f0-9]{12,}$")


def generate_nonce() -> str:
    """Gera o NONCE numérico de 44 dígitos exigido pelos identificadores v1.05."""
    return "".join(str(secrets.randbelow(10)) for _ in range(44))


def validate_nonce(nonce: str) -> None:
    if not NONCE_RE.fullmatch(nonce):
        raise ValueError("NONCE deve conter exatamente 44 dígitos numéricos.")


def validation_code(emec_issuer: str, emec_registrar: str) -> str:
    """Monta o código de segurança com sufixo hexadecimal de 12 chars."""
    if not emec_issuer.isdigit() or not emec_registrar.isdigit():
        raise ValueError("Os códigos e-MEC devem ser numéricos.")
    return f"{emec_issuer}.{emec_registrar}.{secrets.token_hex(6)}"


@dataclass(frozen=True)
class DiplomaIds:
    nonce: str
    virtual_id: str
    diploma_id: str
    registration_id: str
    request_id: str

    @classmethod
    def from_nonce(cls, nonce: str) -> "DiplomaIds":
        validate_nonce(nonce)
        return cls(
            nonce=nonce,
            virtual_id=f"VDip{nonce}",
            diploma_id=f"Dip{nonce}",
            registration_id=f"RDip{nonce}",
            request_id=f"ReqDip{nonce}",
        )

    @classmethod
    def new(cls) -> "DiplomaIds":
        return cls.from_nonce(generate_nonce())
