from __future__ import annotations
from dataclasses import dataclass
from generated.leiaute_documentacao_academica_registro_diploma_digital_v1_05 import TdocumentacaoAcademicaRegistro

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class DocumentacaoAcademicaRegistro(TdocumentacaoAcademicaRegistro):
    """
    Documentação Acadêmica para Emissão e Registro de Diplomas Digitais.
    """
    class Meta:
        namespace = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"