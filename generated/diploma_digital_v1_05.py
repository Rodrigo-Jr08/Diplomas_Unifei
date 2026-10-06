from __future__ import annotations
from dataclasses import dataclass
from generated.leiaute_diploma_digital_v1_05 import Tdiploma

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class Diploma(Tdiploma):
    """
    Diploma Digital.
    """
    class Meta:
        namespace = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"