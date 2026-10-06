from __future__ import annotations
from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDate
from generated.tipos_basicos_v1_05 import (
    Tamb,
    TcargosAssinantes,
    TgrauConferido,
    TmodalidadeCurso,
    TmodalidadeCursoNsf,
    Tnaturalidade,
    ToutroDocumentoIdentificacao,
    Trg,
    Tsexo,
    TtipoAto,
    TtipoAtoComAtoProprio,
    TtituloConferido,
    Tuf,
    Tvazio,
    Tversao,
)
from generated.xmldsig_core_schema_v1_1 import Signature

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class TdeclaracoesAcercaProcesso:
    """
    Declaracoes da IES sobre o processo judicial.
    """
    class Meta:
        name = "TDeclaracoesAcercaProcesso"

    declaracao: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Declaracao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class Thabilitacao:
    """
    Informações sobre Habilitacao.
    """
    class Meta:
        name = "THabilitacao"

    nome_habilitacao: str = field(
        metadata={
            "name": "NomeHabilitacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    data_habilitacao: XmlDate = field(
        metadata={
            "name": "DataHabilitacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TinformacoesProcessoJudicial:
    """
    Informações do processo judicial.
    """
    class Meta:
        name = "TInformacoesProcessoJudicial"

    numero_processo_judicial: str = field(
        metadata={
            "name": "NumeroProcessoJudicial",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'\d{7}\-\d{2}\.\d{4}\.\d\.\d{2}\.\d{4}',
        }
    )
    nome_juiz: str = field(
        metadata={
            "name": "NomeJuiz",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    decisao: None | str = field(
        default=None,
        metadata={
            "name": "Decisao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class TinformacoesTramitacaoEmec:
    """
    Informações sobre tramitação de processos EMEC.
    """
    class Meta:
        name = "TInformacoesTramitacaoEMEC"

    numero_processo: str = field(
        metadata={
            "name": "NumeroProcesso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    tipo_processo: str = field(
        metadata={
            "name": "TipoProcesso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    data_cadastro: XmlDate = field(
        metadata={
            "name": "DataCadastro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_protocolo: XmlDate = field(
        metadata={
            "name": "DataProtocolo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TlivroRegistro:
    """
    Dados do livro.
    """
    class Meta:
        name = "TLivroRegistro"

    livro_registro: str = field(
        metadata={
            "name": "LivroRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    numero_registro: None | str = field(
        default=None,
        metadata={
            "name": "NumeroRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    numero_folha_do_diploma: None | str = field(
        default=None,
        metadata={
            "name": "NumeroFolhaDoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    numero_sequencia_do_diploma: None | str = field(
        default=None,
        metadata={
            "name": "NumeroSequenciaDoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    processo_do_diploma: None | str = field(
        default=None,
        metadata={
            "name": "ProcessoDoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    data_colacao_grau: XmlDate = field(
        metadata={
            "name": "DataColacaoGrau",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_expedicao_diploma: XmlDate = field(
        metadata={
            "name": "DataExpedicaoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_registro_diploma: XmlDate = field(
        metadata={
            "name": "DataRegistroDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    responsavel_registro: TlivroRegistro.ResponsavelRegistro = field(
        metadata={
            "name": "ResponsavelRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )

    @dataclass(kw_only=True)
    class ResponsavelRegistro:
        nome: str = field(
            metadata={
                "name": "Nome",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
            }
        )
        cpf: str = field(
            metadata={
                "name": "CPF",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "max_length": 11,
                "white_space": "collapse",
                "pattern": r'[0-9]{11}',
            }
        )
        idou_numero_matricula: None | str = field(
            default=None,
            metadata={
                "name": "IDouNumeroMatricula",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "min_length": 1,
                "white_space": "preserve",
            }
        )
@dataclass(kw_only=True)
class TlivroRegistroNsf:
    """
    Dados do livro.
    """
    class Meta:
        name = "TLivroRegistroNSF"

    livro_registro: None | str = field(
        default=None,
        metadata={
            "name": "LivroRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    numero_registro: list[str] = field(
        default_factory=list,
        metadata={
            "name": "NumeroRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_occurs": 2,
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    numero_folha_do_diploma: None | str = field(
        default=None,
        metadata={
            "name": "NumeroFolhaDoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    numero_sequencia_do_diploma: None | str = field(
        default=None,
        metadata={
            "name": "NumeroSequenciaDoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    processo_do_diploma: None | str = field(
        default=None,
        metadata={
            "name": "ProcessoDoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    data_colacao_grau: XmlDate = field(
        metadata={
            "name": "DataColacaoGrau",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_expedicao_diploma: XmlDate = field(
        metadata={
            "name": "DataExpedicaoDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_registro_diploma: XmlDate = field(
        metadata={
            "name": "DataRegistroDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    responsavel_registro: TlivroRegistroNsf.ResponsavelRegistro = field(
        metadata={
            "name": "ResponsavelRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )

    @dataclass(kw_only=True)
    class ResponsavelRegistro:
        nome: str = field(
            metadata={
                "name": "Nome",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
            }
        )
        cpf: str = field(
            metadata={
                "name": "CPF",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "max_length": 11,
                "white_space": "collapse",
                "pattern": r'[0-9]{11}',
            }
        )
        idou_numero_matricula: None | str = field(
            default=None,
            metadata={
                "name": "IDouNumeroMatricula",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "min_length": 1,
                "white_space": "preserve",
            }
        )
@dataclass(kw_only=True)
class Tseguranca:
    """
    Dados de seguranca do diploma.
    """
    class Meta:
        name = "TSeguranca"

    codigo_validacao: str = field(
        metadata={
            "name": "CodigoValidacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'\d{1,}\.\d{1,}\.[a-f0-9]{12,}',
        }
    )
@dataclass(kw_only=True)
class TatoRegulatorio:
    """
    Ato regulatório.
    """
    class Meta:
        name = "TAtoRegulatorio"

    tipo: TtipoAto = field(
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    numero: str = field(
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'(S/N)|((\d)[-\d\w_/]*)',
        }
    )
    data: XmlDate = field(
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    veiculo_publicacao: None | str = field(
        default=None,
        metadata={
            "name": "VeiculoPublicacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    data_publicacao: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DataPublicacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    secao_publicacao: None | str = field(
        default=None,
        metadata={
            "name": "SecaoPublicacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    pagina_publicacao: None | str = field(
        default=None,
        metadata={
            "name": "PaginaPublicacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    numero_dou: None | str = field(
        default=None,
        metadata={
            "name": "NumeroDOU",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
@dataclass(kw_only=True)
class TatoRegulatorioComOuSemEmec:
    """
    Ato regulatório de reconhecimento.
    """
    class Meta:
        name = "TAtoRegulatorioComOuSemEMEC"

    informacoes_tramitacao_emec: None | TinformacoesTramitacaoEmec = field(
        default=None,
        metadata={
            "name": "InformacoesTramitacaoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    tipo: None | TtipoAtoComAtoProprio = field(
        default=None,
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    numero: None | str = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'(S/N)|((\d)[-\d\w_/]*)',
        }
    )
    data: None | XmlDate = field(
        default=None,
        metadata={
            "name": "Data",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    veiculo_publicacao: None | str = field(
        default=None,
        metadata={
            "name": "VeiculoPublicacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    data_publicacao: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DataPublicacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    secao_publicacao: None | str = field(
        default=None,
        metadata={
            "name": "SecaoPublicacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    pagina_publicacao: None | str = field(
        default=None,
        metadata={
            "name": "PaginaPublicacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    numero_dou: None | str = field(
        default=None,
        metadata={
            "name": "NumeroDOU",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
@dataclass(kw_only=True)
class TdadosDiplomado:
    """
    Dados do Diplomado.
    """
    class Meta:
        name = "TDadosDiplomado"

    id: str = field(
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    nome: str = field(
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    nome_social: None | str = field(
        default=None,
        metadata={
            "name": "NomeSocial",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    sexo: Tsexo = field(
        metadata={
            "name": "Sexo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    nacionalidade: str = field(
        metadata={
            "name": "Nacionalidade",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    naturalidade: Tnaturalidade = field(
        metadata={
            "name": "Naturalidade",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    cpf: str = field(
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 11,
            "white_space": "collapse",
            "pattern": r'[0-9]{11}',
        }
    )
    rg: None | Trg = field(
        default=None,
        metadata={
            "name": "RG",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    outro_documento_identificacao: None | ToutroDocumentoIdentificacao = field(
        default=None,
        metadata={
            "name": "OutroDocumentoIdentificacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_nascimento: XmlDate = field(
        metadata={
            "name": "DataNascimento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadosDiplomadoPorDecisaoJudicial:
    """
    Dados do Diplomado com flexibilizações por decisão judicial.
    """
    class Meta:
        name = "TDadosDiplomadoPorDecisaoJudicial"

    id: None | str = field(
        default=None,
        metadata={
            "name": "ID",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    id_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "ID_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    nome: str = field(
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    nome_social: None | str = field(
        default=None,
        metadata={
            "name": "NomeSocial",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    sexo: None | Tsexo = field(
        default=None,
        metadata={
            "name": "Sexo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    sexo_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Sexo_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    nacionalidade: None | str = field(
        default=None,
        metadata={
            "name": "Nacionalidade",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    nacionalidade_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Nacionalidade_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    naturalidade: None | Tnaturalidade = field(
        default=None,
        metadata={
            "name": "Naturalidade",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    naturalidade_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Naturalidade_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    cpf: str = field(
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 11,
            "white_space": "collapse",
            "pattern": r'[0-9]{11}',
        }
    )
    rg: None | Trg = field(
        default=None,
        metadata={
            "name": "RG",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    outro_documento_identificacao: None | ToutroDocumentoIdentificacao = field(
        default=None,
        metadata={
            "name": "OutroDocumentoIdentificacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_nascimento: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DataNascimento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_nascimento_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "DataNascimento_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class Tendereco:
    """
    Tipo Endereço.

    :ivar logradouro: Logradouro
    :ivar numero: Número
    :ivar complemento: Complemento
    :ivar bairro: Bairro
    :ivar codigo_municipio:
    :ivar nome_municipio:
    :ivar uf:
    :ivar nome_municipio_estrangeiro:
    :ivar cep: CEP
    """
    class Meta:
        name = "TEndereco"

    logradouro: str = field(
        metadata={
            "name": "Logradouro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 2,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    numero: None | str = field(
        default=None,
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    complemento: None | str = field(
        default=None,
        metadata={
            "name": "Complemento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    bairro: str = field(
        metadata={
            "name": "Bairro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 2,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    codigo_municipio: None | str = field(
        default=None,
        metadata={
            "name": "CodigoMunicipio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'[0-9]{7}',
        }
    )
    nome_municipio: None | str = field(
        default=None,
        metadata={
            "name": "NomeMunicipio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    uf: None | Tuf = field(
        default=None,
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    nome_municipio_estrangeiro: None | str = field(
        default=None,
        metadata={
            "name": "NomeMunicipioEstrangeiro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    cep: str = field(
        metadata={
            "name": "CEP",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'[0-9]{8}',
        }
    )
@dataclass(kw_only=True)
class TinfoAssinantes:
    """
    Informações de cargo dos assinantes.
    """
    class Meta:
        name = "TInfoAssinantes"

    assinante: list[TinfoAssinantes.Assinante] = field(
        default_factory=list,
        metadata={
            "name": "Assinante",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )

    @dataclass(kw_only=True)
    class Assinante:
        cpf: str = field(
            metadata={
                "name": "CPF",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "max_length": 11,
                "white_space": "collapse",
                "pattern": r'[0-9]{11}',
            }
        )
        cargo: None | TcargosAssinantes = field(
            default=None,
            metadata={
                "name": "Cargo",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            }
        )
        outro_cargo: None | str = field(
            default=None,
            metadata={
                "name": "OutroCargo",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "white_space": "preserve",
                "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
            }
        )
@dataclass(kw_only=True)
class TdadosIesEmissora:
    """
    Dados da IES Emissora.
    """
    class Meta:
        name = "TDadosIesEmissora"

    nome: str = field(
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    codigo_mec: str = field(
        metadata={
            "name": "CodigoMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    cnpj: str = field(
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r'[0-9]{14}',
        }
    )
    endereco: Tendereco = field(
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    credenciamento: TatoRegulatorioComOuSemEmec = field(
        metadata={
            "name": "Credenciamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    recredenciamento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "Recredenciamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    renovacao_de_recredenciamento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "RenovacaoDeRecredenciamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    mantenedora: None | TdadosIesEmissora.Mantenedora = field(
        default=None,
        metadata={
            "name": "Mantenedora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )

    @dataclass(kw_only=True)
    class Mantenedora:
        razao_social: str = field(
            metadata={
                "name": "RazaoSocial",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
            }
        )
        cnpj: str = field(
            metadata={
                "name": "CNPJ",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r'[0-9]{14}',
            }
        )
        endereco: Tendereco = field(
            metadata={
                "name": "Endereco",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            }
        )
@dataclass(kw_only=True)
class TdadosIesOriginalCursoPta:
    """
    Em caso da emissão de segunda via de Diploma ocorrer a partir de acervo
    de outra instituição absorvida pela IES Emissora por meio de Processo
    de Transferência Assistida, deve-se incluir a informação da IES de
    origem.
    """
    class Meta:
        name = "TDadosIesOriginalCursoPTA"

    nome: str = field(
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    codigo_mec: None | str = field(
        default=None,
        metadata={
            "name": "CodigoMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    codigo_mec_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "CodigoMEC_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    cnpj: None | str = field(
        default=None,
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r'[0-9]{14}',
        }
    )
    endereco: None | Tendereco = field(
        default=None,
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    descredenciamento: TatoRegulatorio = field(
        metadata={
            "name": "Descredenciamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadosIesRegistradora:
    """
    Dados da IES registradora.
    """
    class Meta:
        name = "TDadosIesRegistradora"

    nome: str = field(
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    codigo_mec: str = field(
        metadata={
            "name": "CodigoMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    cnpj: str = field(
        metadata={
            "name": "CNPJ",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 14,
            "white_space": "preserve",
            "pattern": r'[0-9]{14}',
        }
    )
    endereco: Tendereco = field(
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    credenciamento: TatoRegulatorioComOuSemEmec = field(
        metadata={
            "name": "Credenciamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    recredenciamento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "Recredenciamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    renovacao_de_recredenciamento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "RenovacaoDeRecredenciamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    ato_regulatorio_autorizacao_registro: None | TatoRegulatorio = field(
        default=None,
        metadata={
            "name": "AtoRegulatorioAutorizacaoRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    mantenedora: TdadosIesRegistradora.Mantenedora = field(
        metadata={
            "name": "Mantenedora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )

    @dataclass(kw_only=True)
    class Mantenedora:
        razao_social: str = field(
            metadata={
                "name": "RazaoSocial",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "min_length": 1,
                "max_length": 255,
                "white_space": "preserve",
                "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
            }
        )
        cnpj: str = field(
            metadata={
                "name": "CNPJ",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "max_length": 14,
                "white_space": "preserve",
                "pattern": r'[0-9]{14}',
            }
        )
        endereco: Tendereco = field(
            metadata={
                "name": "Endereco",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            }
        )
@dataclass(kw_only=True)
class Tpolo:
    """
    Dados do polo.
    """
    class Meta:
        name = "TPolo"

    nome: str = field(
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    endereco: Tendereco = field(
        metadata={
            "name": "Endereco",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    codigo_emec: None | str = field(
        default=None,
        metadata={
            "name": "CodigoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    sem_codigo_emec: None | TinformacoesTramitacaoEmec = field(
        default=None,
        metadata={
            "name": "SemCodigoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadosCurso:
    """
    Dados do curso.
    """
    class Meta:
        name = "TDadosCurso"

    nome_curso: str = field(
        metadata={
            "name": "NomeCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    codigo_curso_emec: None | str = field(
        default=None,
        metadata={
            "name": "CodigoCursoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    sem_codigo_curso_emec: None | TinformacoesTramitacaoEmec = field(
        default=None,
        metadata={
            "name": "SemCodigoCursoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    habilitacao: list[Thabilitacao] = field(
        default_factory=list,
        metadata={
            "name": "Habilitacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    modalidade: TmodalidadeCurso = field(
        metadata={
            "name": "Modalidade",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    titulo_conferido: TtituloConferido = field(
        metadata={
            "name": "TituloConferido",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    grau_conferido: TgrauConferido = field(
        metadata={
            "name": "GrauConferido",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    enfase: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Enfase",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    endereco_curso: Tendereco = field(
        metadata={
            "name": "EnderecoCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    polo: None | Tpolo = field(
        default=None,
        metadata={
            "name": "Polo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    autorizacao: TatoRegulatorioComOuSemEmec = field(
        metadata={
            "name": "Autorizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    reconhecimento: TatoRegulatorioComOuSemEmec = field(
        metadata={
            "name": "Reconhecimento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    renovacao_reconhecimento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "RenovacaoReconhecimento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadosCursoNsf:
    """
    Dados do curso de universidades fora do sistema federal - flexibiliza
    algumas exigências.
    """
    class Meta:
        name = "TDadosCursoNSF"

    nome_curso: str = field(
        metadata={
            "name": "NomeCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    codigo_curso_emec: None | str = field(
        default=None,
        metadata={
            "name": "CodigoCursoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    sem_codigo_curso_emec: None | TinformacoesTramitacaoEmec = field(
        default=None,
        metadata={
            "name": "SemCodigoCursoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    habilitacao: list[Thabilitacao] = field(
        default_factory=list,
        metadata={
            "name": "Habilitacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    modalidade: TmodalidadeCursoNsf = field(
        metadata={
            "name": "Modalidade",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    titulo_conferido: TtituloConferido = field(
        metadata={
            "name": "TituloConferido",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    grau_conferido: TgrauConferido = field(
        metadata={
            "name": "GrauConferido",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    endereco_curso: Tendereco = field(
        metadata={
            "name": "EnderecoCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    polo: None | Tpolo = field(
        default=None,
        metadata={
            "name": "Polo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    autorizacao: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "Autorizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    reconhecimento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "Reconhecimento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    renovacao_reconhecimento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "RenovacaoReconhecimento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadosCursoPorDecisaoJudicial:
    """
    Dados do curso para diplomas emitidos por decisão judicial.
    """
    class Meta:
        name = "TDadosCursoPorDecisaoJudicial"

    nome_curso: str = field(
        metadata={
            "name": "NomeCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    codigo_curso_emec: None | str = field(
        default=None,
        metadata={
            "name": "CodigoCursoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[0-9]+',
        }
    )
    sem_codigo_curso_emec: None | TinformacoesTramitacaoEmec = field(
        default=None,
        metadata={
            "name": "SemCodigoCursoEMEC",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    codigo_curso_emec_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "CodigoCursoEMEC_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    habilitacao: list[Thabilitacao] = field(
        default_factory=list,
        metadata={
            "name": "Habilitacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    modalidade: TmodalidadeCursoNsf = field(
        metadata={
            "name": "Modalidade",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    titulo_conferido: TtituloConferido = field(
        metadata={
            "name": "TituloConferido",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    grau_conferido: TgrauConferido = field(
        metadata={
            "name": "GrauConferido",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    endereco_curso: None | Tendereco = field(
        default=None,
        metadata={
            "name": "EnderecoCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    endereco_curso_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "EnderecoCurso_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    polo: None | Tpolo = field(
        default=None,
        metadata={
            "name": "Polo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    autorizacao: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "Autorizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    reconhecimento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "Reconhecimento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    renovacao_reconhecimento: None | TatoRegulatorioComOuSemEmec = field(
        default=None,
        metadata={
            "name": "RenovacaoReconhecimento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadosRegistro:
    """
    Tipo de dados do registro do diploma digital.

    :ivar ies_registradora:
    :ivar livro_registro:
    :ivar id_documentacao_academica:
    :ivar seguranca:
    :ivar informacoes_adicionais:
    :ivar assinantes:
    :ivar signature:
    :ivar id: Id
    """
    class Meta:
        name = "TDadosRegistro"

    ies_registradora: TdadosIesRegistradora = field(
        metadata={
            "name": "IesRegistradora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    livro_registro: TlivroRegistro = field(
        metadata={
            "name": "LivroRegistro",
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
    seguranca: Tseguranca = field(
        metadata={
            "name": "Seguranca",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    informacoes_adicionais: None | str = field(
        default=None,
        metadata={
            "name": "InformacoesAdicionais",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    assinantes: None | TinfoAssinantes = field(
        default=None,
        metadata={
            "name": "Assinantes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r'RDip[0-9]{44}',
        }
    )
@dataclass(kw_only=True)
class TdadosRegistroNsf:
    """
    Tipo de dados do registro do diploma digital flexibilizado para
    Universidades fora do sistema federal de ensino.

    :ivar ies_registradora:
    :ivar livro_registro:
    :ivar id_documentacao_academica:
    :ivar seguranca:
    :ivar informacoes_adicionais:
    :ivar assinantes:
    :ivar signature:
    :ivar id: Id
    """
    class Meta:
        name = "TDadosRegistroNSF"

    ies_registradora: TdadosIesRegistradora = field(
        metadata={
            "name": "IesRegistradora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    livro_registro: TlivroRegistroNsf = field(
        metadata={
            "name": "LivroRegistro",
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
    seguranca: Tseguranca = field(
        metadata={
            "name": "Seguranca",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    informacoes_adicionais: None | str = field(
        default=None,
        metadata={
            "name": "InformacoesAdicionais",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    assinantes: None | TinfoAssinantes = field(
        default=None,
        metadata={
            "name": "Assinantes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r'RDip[0-9]{44}',
        }
    )
@dataclass(kw_only=True)
class TdadosRegistroPorDecisaoJudicial:
    """
    Tipo de dados do registro do diploma digital para registro por decisão
    judicial.

    :ivar ies_registradora:
    :ivar livro_registro:
    :ivar id_documentacao_academica:
    :ivar seguranca:
    :ivar informacoes_processo_judicial:
    :ivar declaracoes_registradora_acerca_processo:
    :ivar informacoes_adicionais:
    :ivar assinantes:
    :ivar signature:
    :ivar id: Id
    """
    class Meta:
        name = "TDadosRegistroPorDecisaoJudicial"

    ies_registradora: TdadosIesRegistradora = field(
        metadata={
            "name": "IesRegistradora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    livro_registro: TlivroRegistroNsf = field(
        metadata={
            "name": "LivroRegistro",
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
    seguranca: Tseguranca = field(
        metadata={
            "name": "Seguranca",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    informacoes_processo_judicial: TinformacoesProcessoJudicial = field(
        metadata={
            "name": "InformacoesProcessoJudicial",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    declaracoes_registradora_acerca_processo: None | TdeclaracoesAcercaProcesso = field(
        default=None,
        metadata={
            "name": "DeclaracoesRegistradoraAcercaProcesso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    informacoes_adicionais: None | str = field(
        default=None,
        metadata={
            "name": "InformacoesAdicionais",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    assinantes: None | TinfoAssinantes = field(
        default=None,
        metadata={
            "name": "Assinantes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r'RDip[0-9]{44}',
        }
    )
@dataclass(kw_only=True)
class TdadosDiploma:
    """
    Tipo Diploma Digital.

    :ivar diplomado:
    :ivar data_conclusao:
    :ivar dados_curso:
    :ivar dados_ies_original_curso_pta:
    :ivar ies_emissora:
    :ivar assinantes:
    :ivar signature:
    :ivar id: Id
    """
    class Meta:
        name = "TDadosDiploma"

    diplomado: TdadosDiplomado = field(
        metadata={
            "name": "Diplomado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_conclusao: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DataConclusao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_curso: TdadosCurso = field(
        metadata={
            "name": "DadosCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_ies_original_curso_pta: None | TdadosIesOriginalCursoPta = field(
        default=None,
        metadata={
            "name": "DadosIesOriginalCursoPTA",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    ies_emissora: TdadosIesEmissora = field(
        metadata={
            "name": "IesEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    assinantes: None | TinfoAssinantes = field(
        default=None,
        metadata={
            "name": "Assinantes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r'Dip[0-9]{44}',
        }
    )
@dataclass(kw_only=True)
class TdadosDiplomaNsf:
    """
    Tipo Diploma Digital para Universidade fora do sistema federal de
    ensino - Flexibiliza a obrigatoriedade de alguns elementos.

    :ivar diplomado:
    :ivar data_conclusao:
    :ivar dados_curso:
    :ivar dados_ies_original_curso_pta:
    :ivar ies_emissora:
    :ivar assinantes:
    :ivar signature:
    :ivar id: Id
    """
    class Meta:
        name = "TDadosDiplomaNSF"

    diplomado: TdadosDiplomado = field(
        metadata={
            "name": "Diplomado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_conclusao: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DataConclusao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_curso: TdadosCursoNsf = field(
        metadata={
            "name": "DadosCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_ies_original_curso_pta: None | TdadosIesOriginalCursoPta = field(
        default=None,
        metadata={
            "name": "DadosIesOriginalCursoPTA",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    ies_emissora: TdadosIesEmissora = field(
        metadata={
            "name": "IesEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    assinantes: None | TinfoAssinantes = field(
        default=None,
        metadata={
            "name": "Assinantes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r'Dip[0-9]{44}',
        }
    )
@dataclass(kw_only=True)
class TdadosDiplomaPorDecisaoJudicial:
    """
    Tipo Diploma Digital para emissão de diplomas por força de decisão
    Judicial.

    :ivar diplomado:
    :ivar data_conclusao:
    :ivar dados_curso:
    :ivar dados_ies_original_curso_pta:
    :ivar ies_emissora:
    :ivar declaracoes_emissora_acerca_processo:
    :ivar assinantes:
    :ivar signature:
    :ivar id: Id
    """
    class Meta:
        name = "TDadosDiplomaPorDecisaoJudicial"

    diplomado: TdadosDiplomadoPorDecisaoJudicial = field(
        metadata={
            "name": "Diplomado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_conclusao: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DataConclusao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_curso: TdadosCursoPorDecisaoJudicial = field(
        metadata={
            "name": "DadosCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_ies_original_curso_pta: None | TdadosIesOriginalCursoPta = field(
        default=None,
        metadata={
            "name": "DadosIesOriginalCursoPTA",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    ies_emissora: TdadosIesEmissora = field(
        metadata={
            "name": "IesEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    declaracoes_emissora_acerca_processo: None | TdeclaracoesAcercaProcesso = field(
        default=None,
        metadata={
            "name": "DeclaracoesEmissoraAcercaProcesso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    assinantes: None | TinfoAssinantes = field(
        default=None,
        metadata={
            "name": "Assinantes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    signature: list[Signature] = field(
        default_factory=list,
        metadata={
            "name": "Signature",
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
            "min_occurs": 1,
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r'Dip[0-9]{44}',
        }
    )
@dataclass(kw_only=True)
class TinfDiploma:
    """
    Tipo Diploma Digital.

    :ivar dados_diploma:
    :ivar dados_diploma_nsf:
    :ivar dados_registro:
    :ivar dados_registro_nsf:
    :ivar dados_diploma_por_decisao_judicial:
    :ivar dados_registro_por_decisao_judicial:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar id: Id
    :ivar ambiente: Especifica o contexto no qual o Diploma foi emitido.
        Apenas Diplomas emitidos no ambiente "Produção" são legalmente
        válidos. Caso não seja especificado, o Ambiente é "Produção" e o
        Diploma é legalmente válido.
    """
    class Meta:
        name = "TInfDiploma"

    dados_diploma: None | TdadosDiploma = field(
        default=None,
        metadata={
            "name": "DadosDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_diploma_nsf: None | TdadosDiplomaNsf = field(
        default=None,
        metadata={
            "name": "DadosDiplomaNSF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_registro: None | TdadosRegistro = field(
        default=None,
        metadata={
            "name": "DadosRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_registro_nsf: None | TdadosRegistroNsf = field(
        default=None,
        metadata={
            "name": "DadosRegistroNSF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_diploma_por_decisao_judicial: None | TdadosDiplomaPorDecisaoJudicial = field(
        default=None,
        metadata={
            "name": "DadosDiplomaPorDecisaoJudicial",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_registro_por_decisao_judicial: None | TdadosRegistroPorDecisaoJudicial = field(
        default=None,
        metadata={
            "name": "DadosRegistroPorDecisaoJudicial",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    versao: Tversao = field(
        metadata={
            "type": "Attribute",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "pattern": r'VDip[0-9]{44}',
        }
    )
    ambiente: Tamb = field(
        default=Tamb.PRODU_O,
        metadata={
            "type": "Attribute",
        }
    )
@dataclass(kw_only=True)
class Tdiploma:
    """
    Tipo Diploma Digital.
    """
    class Meta:
        name = "TDiploma"

    inf_diploma: TinfDiploma = field(
        metadata={
            "name": "infDiploma",
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