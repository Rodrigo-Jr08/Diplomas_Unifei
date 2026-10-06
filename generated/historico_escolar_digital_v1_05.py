from __future__ import annotations
from dataclasses import dataclass
from generated.leiaute_historico_escolar_v1_05 import (
    TdocumentoHistoricoEscolarDigital,
    TdocumentoHistoricoEscolarSegundaViaNatoFisico,
)

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class DocumentoHistoricoEscolarFinal(TdocumentoHistoricoEscolarDigital):
    """
    Documento Histórico Escolar Digital Final.
    """
    class Meta:
        namespace = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"
@dataclass(kw_only=True)
class DocumentoHistoricoEscolarParcial(TdocumentoHistoricoEscolarDigital):
    """
    Documento Histórico Escolar Digital Parcial.
    """
    class Meta:
        namespace = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"
@dataclass(kw_only=True)
class DocumentoHistoricoEscolarSegundaViaNatoFisico(TdocumentoHistoricoEscolarSegundaViaNatoFisico):
    """
    Documento de Segunda Via de Histórico Escolar Digital Nato Físico.
    """
    class Meta:
        namespace = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"