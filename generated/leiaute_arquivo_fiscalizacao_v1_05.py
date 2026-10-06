from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from generated.leiaute_diploma_digital_v1_05 import (
    TdadosIesEmissora,
    TdadosIesRegistradora,
    TlivroRegistro,
)
from generated.tipos_basicos_v1_05 import (
    Tamb,
    Tversao,
)
from generated.xmldsig_core_schema_v1_1 import Signature

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class TdiplomaFiscalizadoEmissora:
    """
    Informaçãoes sobre um diploma emitido.
    """
    class Meta:
        name = "TDiplomaFiscalizadoEmissora"

    codigo_diploma: str = field(
        metadata={
            "name": "CodigoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'\d{1,}\.\d{1,}\.[a-f0-9]{12,}',
        }
    )
    cpfdetentor: str = field(
        metadata={
            "name": "CPFDetentor",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 11,
            "white_space": "collapse",
            "pattern": r'[0-9]{11}',
        }
    )
    codigo_emeccurso: None | str = field(
        default=None,
        metadata={
            "name": "CodigoEMECCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    data_emissao: XmlDate = field(
        metadata={
            "name": "DataEmissao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_registro: XmlDate = field(
        metadata={
            "name": "DataRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    urlxmldo_diplomado: str = field(
        metadata={
            "name": "URLXMLdoDiplomado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 255,
            "pattern": r'http://.*',
        }
    )
    urlrvdd: str = field(
        metadata={
            "name": "URLRVDD",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 255,
            "pattern": r'http://.*',
        }
    )
    urlxmlde_registro_academico: None | str = field(
        default=None,
        metadata={
            "name": "URLXMLdeRegistroAcademico",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 255,
            "pattern": r'http://.*',
        }
    )
@dataclass(kw_only=True)
class TdiplomaFiscalizadoRegistradora:
    """
    Informações sobre um diploma registrado.
    """
    class Meta:
        name = "TDiplomaFiscalizadoRegistradora"

    codigo_diploma: str = field(
        metadata={
            "name": "CodigoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'\d{1,}\.\d{1,}\.[a-f0-9]{12,}',
        }
    )
    cpfdetentor: str = field(
        metadata={
            "name": "CPFDetentor",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 11,
            "white_space": "collapse",
            "pattern": r'[0-9]{11}',
        }
    )
    codigo_emecemissora: str = field(
        metadata={
            "name": "CodigoEMECEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    codigo_emeccurso: None | str = field(
        default=None,
        metadata={
            "name": "CodigoEMECCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    dados_registro: TlivroRegistro = field(
        metadata={
            "name": "DadosRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    id_documentacao_academica: str = field(
        metadata={
            "name": "IdDocumentacaoAcademica",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "pattern": r'ReqDip[0-9]{44}',
        }
    )
@dataclass(kw_only=True)
class TdiplomasFiscalizadosEmissora:
    """
    Lista de Diplomas Emitidos.
    """
    class Meta:
        name = "TDiplomasFiscalizadosEmissora"

    diploma_fiscalizado: list[TdiplomaFiscalizadoEmissora] = field(
        default_factory=list,
        metadata={
            "name": "DiplomaFiscalizado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
@dataclass(kw_only=True)
class TdiplomasFiscalizadosRegistradora:
    """
    Lista de Diplomas Registrados.
    """
    class Meta:
        name = "TDiplomasFiscalizadosRegistradora"

    diploma_fiscalizado: list[TdiplomaFiscalizadoRegistradora] = field(
        default_factory=list,
        metadata={
            "name": "DiplomaFiscalizado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
@dataclass(kw_only=True)
class TinfArquivoFiscalizacaoEmissora:
    """
    Tipo que define o conjunto de informações referentes ao Arquivo de
    Fiscalização da Emissora.

    :ivar data_inicio_fiscalizacao:
    :ivar iesemissora:
    :ivar diplomas_fiscalizados:
    :ivar data_fim_fiscalizacao:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar ambiente: Especifica o contexto no qual o Arquivo de
        Fiscalização foi emitido. Apenas Arquivos de Fiscalização
        emitidos no ambiente "Produção" são legalmente válidos. Caso não
        seja especificado, o Ambiente é "Produção" e o Arquivo de
        Fiscalização é legalmente válido.
    """
    class Meta:
        name = "TInfArquivoFiscalizacaoEmissora"

    data_inicio_fiscalizacao: XmlDate = field(
        metadata={
            "name": "DataInicioFiscalizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    iesemissora: TdadosIesEmissora = field(
        metadata={
            "name": "IESEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    diplomas_fiscalizados: TdiplomasFiscalizadosEmissora = field(
        metadata={
            "name": "DiplomasFiscalizados",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_fim_fiscalizacao: XmlDate = field(
        metadata={
            "name": "DataFimFiscalizacao",
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
class TinfArquivoFiscalizacaoRegistradora:
    """
    Tipo que define o conjunto de informações referentes a Lista de
    Diplomas Anulados.

    :ivar data_inicio_fiscalizacao:
    :ivar iesregistradora:
    :ivar diplomas_fiscalizados:
    :ivar data_fim_fiscalizacao:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar ambiente: Especifica o contexto no qual o Arquivo de
        Fiscalização foi emitido. Apenas Arquivos de Fiscalização
        emitidos no ambiente "Produção" são legalmente válidos. Caso não
        seja especificado, o Ambiente é "Produção" e o Arquivo de
        Fiscalização é legalmente válido.
    """
    class Meta:
        name = "TInfArquivoFiscalizacaoRegistradora"

    data_inicio_fiscalizacao: XmlDate = field(
        metadata={
            "name": "DataInicioFiscalizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    iesregistradora: TdadosIesRegistradora = field(
        metadata={
            "name": "IESRegistradora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    diplomas_fiscalizados: TdiplomasFiscalizadosRegistradora = field(
        metadata={
            "name": "DiplomasFiscalizados",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_fim_fiscalizacao: XmlDate = field(
        metadata={
            "name": "DataFimFiscalizacao",
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
class TarquivoFiscalizacao:
    """
    Lista de Diplomas Emitidos e Registrados em posse da IES para
    fiscalização pelo MEC.
    """
    class Meta:
        name = "TArquivoFiscalizacao"

    inf_arquivo_fiscalizacao_emissora: None | TinfArquivoFiscalizacaoEmissora = field(
        default=None,
        metadata={
            "name": "infArquivoFiscalizacaoEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    inf_arquivo_fiscalizacao_registradora: None | TinfArquivoFiscalizacaoRegistradora = field(
        default=None,
        metadata={
            "name": "infArquivoFiscalizacaoRegistradora",
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