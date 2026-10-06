from __future__ import annotations
from dataclasses import dataclass
from generated.leiaute_lista_diplomas_anulados_v1_05 import TlistaDiplomasAnulados

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class ListaDiplomasAnulados(TlistaDiplomasAnulados):
    """
    Arquivo com a Lista de Diplomas com Registro Anulado.
    """
    class Meta:
        namespace = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"