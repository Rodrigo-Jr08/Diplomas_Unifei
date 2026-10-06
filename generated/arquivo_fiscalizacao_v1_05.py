from __future__ import annotations
from dataclasses import dataclass
from generated.leiaute_arquivo_fiscalizacao_v1_05 import TarquivoFiscalizacao

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class ArquivoFiscalizacao(TarquivoFiscalizacao):
    """
    Arquivo com a Lista de Diplomas emtido e registrados para fiscalização
    pelo MEC.
    """
    class Meta:
        namespace = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"