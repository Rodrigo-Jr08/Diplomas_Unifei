from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from xsdata.models.datatype import XmlDate
from generated.leiaute_diploma_digital_v1_05 import TdadosIesRegistradora
from generated.tipos_basicos_v1_05 import (
    Tamb,
    Tversao,
)
from generated.xmldsig_core_schema_v1_1 import Signature

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


class TmotivoAnulacao(Enum):
    """
    Tipo motivo de anulação de Diploma.
    """
    ERRO_DE_FATO = 'Erro de Fato'
    ERRO_DE_DIREITO = 'Erro de Direito'
    DECIS_O_JUDICIAL = 'Decisão Judicial'
    REEMISS_O_PARA_COMPLEMENTO_DE_INFORMA_O = 'Reemissão para Complemento de Informação'
    REEMISS_O_PARA_INCLUS_O_DE_HABILITA_O = 'Reemissão para Inclusão de Habilitação'
    REEMISS_O_PARA_ANOTA_AO_DE_REGISTRO = 'Reemissão para Anotaçao de Registro'
@dataclass(kw_only=True)
class TdiplomaAnulado:
    """
    Informações de anulação referentes a um Diploma.
    """
    class Meta:
        name = "TDiplomaAnulado"

    codigo_diploma_anulado: str = field(
        metadata={
            "name": "CodigoDiplomaAnulado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'\d{1,}\.\d{1,}\.[a-f0-9]{12,}',
        }
    )
    data_anulacao: XmlDate = field(
        metadata={
            "name": "DataAnulacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    motivo_anulacao: TmotivoAnulacao = field(
        metadata={
            "name": "MotivoAnulacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    anotacao_anulacao: None | str = field(
        default=None,
        metadata={
            "name": "AnotacaoAnulacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class TdiplomasAnulados:
    """
    Lista de Diplomas Anulados com Data de Anulação e Motivo.
    """
    class Meta:
        name = "TDiplomasAnulados"

    diploma_anulado: list[TdiplomaAnulado] = field(
        default_factory=list,
        metadata={
            "name": "DiplomaAnulado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TinfListaDiplomasAnulados:
    """
    Tipo que define o conjunto de informações referentes a Lista de
    Diplomas Anulados.

    :ivar numero_de_sequencia:
    :ivar iesregistradora:
    :ivar diplomas_anulados:
    :ivar data_maxima_proxima_atualizacao:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar ambiente: Especifica o contexto no qual a Lista de Diplomas
        foi emitida. Apenas Lista de Diplomas emitidas no ambiente
        "Produção" são legalmente válidos. Caso não seja especificado, o
        Ambiente é "Produção" e a Lista de Diplomas emitidas é
        legalmente válida.
    """
    class Meta:
        name = "TInfListaDiplomasAnulados"

    numero_de_sequencia: str = field(
        metadata={
            "name": "NumeroDeSequencia",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    iesregistradora: TdadosIesRegistradora = field(
        metadata={
            "name": "IESRegistradora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    diplomas_anulados: TdiplomasAnulados = field(
        metadata={
            "name": "DiplomasAnulados",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_maxima_proxima_atualizacao: XmlDate = field(
        metadata={
            "name": "DataMaximaProximaAtualizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    versao: Tversao = field(
        metadata={
            "type": "Attribute",
        }
    )
    ambiente: Tamb = field(
        default=Tamb.PRODU_O,
        metadata={
            "type": "Attribute",
        }
    )
@dataclass(kw_only=True)
class TlistaDiplomasAnulados:
    """
    Lista de Diplomas com Registro anulado por Registradora.
    """
    class Meta:
        name = "TListaDiplomasAnulados"

    inf_lista_diplomas_anulados: TinfListaDiplomasAnulados = field(
        metadata={
            "name": "infListaDiplomasAnulados",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    signature: Signature = field(
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )