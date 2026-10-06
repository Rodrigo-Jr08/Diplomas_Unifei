from __future__ import annotations
from dataclasses import dataclass
from generated.leiaute_curriculo_escolar_v1_05 import TcurriculoEscolar

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class CurriculoEscolar(TcurriculoEscolar):
    """
    Documento de Descrição do Curriculo Escolar da Graduação.
    """
    class Meta:
        namespace = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"