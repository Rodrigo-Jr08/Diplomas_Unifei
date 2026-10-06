from __future__ import annotations

import hashlib
from dataclasses import dataclass
from typing import Protocol

from .errors import SignatureError


@dataclass(frozen=True)
class SignatureResult:
    signed_xml: bytes
    provider: str
    production_ready: bool


class SignatureProvider(Protocol):
    """Contrato para o mecanismo institucional de assinatura."""

    def sign(self, xml_bytes: bytes, reference_id: str) -> SignatureResult:
        ...


class ProductionSignatureProvider:  # pragma: no cover - adaptador externo
    """Ponto de integração para HSM/assinador institucional/PBAD."""

    def sign(self, xml_bytes: bytes, reference_id: str) -> SignatureResult:
        raise SignatureError(
            "Integração de assinatura de produção não configurada. "
            "Não use assinatura fictícia em ambiente produtivo."
        )


def build_development_signature(reference_id: str):
    """
    Cria um objeto XMLDSig estrutural apenas para desenvolvimento/testes XSD.

    O digest e o valor de assinatura são deliberadamente não criptográficos.
    O XML resultante pode passar na validação estrutural do XSD, mas não é
    autenticado e não possui validade jurídica.
    """
    try:
        from generated.xmldsig_core_schema_v1_1 import (
            CanonicalizationMethod,
            DigestMethod,
            DigestValue,
            Reference,
            Signature,
            SignatureMethod,
            SignatureValue,
            SignedInfo,
        )
    except ImportError as exc:  # pragma: no cover
        raise SignatureError(
            "Não foi possível importar os modelos XMLDSig gerados. "
            "Confira se o pacote `generated/` está no PYTHONPATH."
        ) from exc

    digest = hashlib.sha256(reference_id.encode("utf-8")).digest()
    return Signature(
        signed_info=SignedInfo(
            canonicalization_method=CanonicalizationMethod(
                algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"
            ),
            signature_method=SignatureMethod(
                algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
            ),
            reference=[
                Reference(
                    digest_method=DigestMethod(
                        algorithm="http://www.w3.org/2001/04/xmlenc#sha256"
                    ),
                    digest_value=DigestValue(value=digest),
                    uri=f"#{reference_id}",
                )
            ],
        ),
        signature_value=SignatureValue(value=b"DEVELOPMENT_ONLY_NOT_A_REAL_SIGNATURE"),
    )
