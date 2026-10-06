from __future__ import annotations
from dataclasses import dataclass, field
from enum import Enum
from generated.leiaute_diploma_digital_v1_05 import (
    TdadosDiploma,
    TdadosDiplomaNsf,
    TdadosDiplomaPorDecisaoJudicial,
    TinformacoesProcessoJudicial,
)
from generated.leiaute_historico_escolar_v1_05 import (
    ThistoricoEscolar,
    ThistoricoEscolarSegundaVia,
)
from generated.tipos_basicos_v1_05 import (
    Tamb,
    Tfiliacao,
    Tvazio,
    Tversao,
)
from generated.xmldsig_core_schema_v1_1 import Signature

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class TtermoResponsabilidade:
    """
    Tipo Termo Responsabilidade.
    """
    class Meta:
        name = "TTermoResponsabilidade"

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
    cargo: str = field(
        metadata={
            "name": "Cargo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    ato_designacao: None | bytes = field(
        default=None,
        metadata={
            "name": "AtoDesignacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "format": "base64",
        }
    )
class TtipoDocumentacao(Enum):
    """
    Tipo documentação associada.
    """
    DOCUMENTO_IDENTIDADE_DO_ALUNO = 'DocumentoIdentidadeDoAluno'
    PROVA_CONCLUSAO_ENSINO_MEDIO = 'ProvaConclusaoEnsinoMedio'
    PROVA_COLACAO = 'ProvaColacao'
    COMPROVACAO_ESTAGIO_CURRICULAR = 'ComprovacaoEstagioCurricular'
    CERTIDAO_NASCIMENTO = 'CertidaoNascimento'
    CERTIDAO_CASAMENTO = 'CertidaoCasamento'
    TITULO_ELEITOR = 'TituloEleitor'
    ATO_NATURALIZACAO = 'AtoNaturalizacao'
    OUTROS = 'Outros'
@dataclass(kw_only=True)
class TdadosPrivadosDiplomado:
    """
    Dados do Diplomado.
    """
    class Meta:
        name = "TDadosPrivadosDiplomado"

    filiacao: Tfiliacao = field(
        metadata={
            "name": "Filiacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    historico_escolar: ThistoricoEscolar = field(
        metadata={
            "name": "HistoricoEscolar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadosPrivadosDiplomadoPorDecisaoJudicial:
    """
    Dados do Diplomado para emissão devido a decisão judicial.
    """
    class Meta:
        name = "TDadosPrivadosDiplomadoPorDecisaoJudicial"

    filiacao: None | Tfiliacao = field(
        default=None,
        metadata={
            "name": "Filiacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    filiacao_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Filiacao_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    historico_escolar: None | ThistoricoEscolarSegundaVia = field(
        default=None,
        metadata={
            "name": "HistoricoEscolar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    historico_escolar_indisponivel: None | Tvazio = field(
        default=None,
        metadata={
            "name": "HistoricoEscolar_Indisponivel",
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
@dataclass(kw_only=True)
class TdadosPrivadosDiplomadoSegundaVia:
    """
    Dados do Diplomado para emissão de segunda via digital de diploma
    expedido em papel.
    """
    class Meta:
        name = "TDadosPrivadosDiplomadoSegundaVia"

    filiacao: Tfiliacao = field(
        metadata={
            "name": "Filiacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    historico_escolar: ThistoricoEscolarSegundaVia = field(
        metadata={
            "name": "HistoricoEscolar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdocumentacaoComprobatoria:
    """
    Tipo Documentação Comprobatória.
    """
    class Meta:
        name = "TDocumentacaoComprobatoria"

    documento: list[TdocumentacaoComprobatoria.Documento] = field(
        default_factory=list,
        metadata={
            "name": "Documento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )

    @dataclass(kw_only=True)
    class Documento:
        value: bytes = field(
            default=b'',
            metadata={
                "format": "base64",
            }
        )
        tipo: TtipoDocumentacao = field(
            metadata={
                "type": "Attribute",
            }
        )
        observacoes: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
            }
        )
@dataclass(kw_only=True)
class TdocumentacaoComprobatoriaPorDecisaoJudicial:
    """
    Tipo Documentação Comprobatória para emissões por decisão judicial.
    """
    class Meta:
        name = "TDocumentacaoComprobatoriaPorDecisaoJudicial"

    documento: list[TdocumentacaoComprobatoriaPorDecisaoJudicial.Documento] = field(
        default_factory=list,
        metadata={
            "name": "Documento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    documento_indisponivel: list[TdocumentacaoComprobatoriaPorDecisaoJudicial.DocumentoIndisponivel] = field(
        default_factory=list,
        metadata={
            "name": "Documento_Indisponivel",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )

    @dataclass(kw_only=True)
    class Documento:
        value: bytes = field(
            default=b'',
            metadata={
                "format": "base64",
            }
        )
        tipo: TtipoDocumentacao = field(
            metadata={
                "type": "Attribute",
            }
        )
        observacoes: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
            }
        )

    @dataclass(kw_only=True)
    class DocumentoIndisponivel:
        tipo: TtipoDocumentacao = field(
            metadata={
                "type": "Attribute",
            }
        )
        observacoes: None | str = field(
            default=None,
            metadata={
                "type": "Attribute",
                "white_space": "preserve",
                "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
            }
        )
@dataclass(kw_only=True)
class TregistroPorDecisaoJudicialReq:
    """
    Tipo Requisição de Registro de Diploma Digital emitido por decisão
    judicial.

    :ivar dados_diploma_por_decisao_judicial:
    :ivar dados_privados_diplomado:
    :ivar termo_responsabilidade_emissora:
    :ivar documentacao_comprobatoria:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar id: Id
    :ivar ambiente: Especifica o contexto no qual o Diploma foi emitido.
        Apenas Diplomas emitidos no ambiente "Produção" são legalmente
        válidos. Caso não seja especificado, o Ambiente é "Produção" e o
        Diploma é legalmente válido.
    """
    class Meta:
        name = "TRegistroPorDecisaoJudicialReq"

    dados_diploma_por_decisao_judicial: TdadosDiplomaPorDecisaoJudicial = field(
        metadata={
            "name": "DadosDiplomaPorDecisaoJudicial",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_privados_diplomado: TdadosPrivadosDiplomadoPorDecisaoJudicial = field(
        metadata={
            "name": "DadosPrivadosDiplomado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    termo_responsabilidade_emissora: None | TtermoResponsabilidade = field(
        default=None,
        metadata={
            "name": "TermoResponsabilidadeEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    documentacao_comprobatoria: None | TdocumentacaoComprobatoriaPorDecisaoJudicial = field(
        default=None,
        metadata={
            "name": "DocumentacaoComprobatoria",
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
            "pattern": r'ReqDip[0-9]{44}',
        }
    )
    ambiente: Tamb = field(
        default=Tamb.PRODU_O,
        metadata={
            "type": "Attribute",
        }
    )
@dataclass(kw_only=True)
class TregistroReq:
    """
    Tipo Requisição de Registro de Diploma Digital.

    :ivar dados_diploma:
    :ivar dados_privados_diplomado:
    :ivar termo_responsabilidade_emissora:
    :ivar documentacao_comprobatoria:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar id: Id
    :ivar ambiente: Especifica o contexto no qual o Diploma foi emitido.
        Apenas Diplomas emitidos no ambiente "Produção" são legalmente
        válidos. Caso não seja especificado, o Ambiente é "Produção" e o
        Diploma é legalmente válido.
    """
    class Meta:
        name = "TRegistroReq"

    dados_diploma: TdadosDiploma = field(
        metadata={
            "name": "DadosDiploma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_privados_diplomado: TdadosPrivadosDiplomado = field(
        metadata={
            "name": "DadosPrivadosDiplomado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    termo_responsabilidade_emissora: None | TtermoResponsabilidade = field(
        default=None,
        metadata={
            "name": "TermoResponsabilidadeEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    documentacao_comprobatoria: TdocumentacaoComprobatoria = field(
        metadata={
            "name": "DocumentacaoComprobatoria",
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
            "pattern": r'ReqDip[0-9]{44}',
        }
    )
    ambiente: Tamb = field(
        default=Tamb.PRODU_O,
        metadata={
            "type": "Attribute",
        }
    )
@dataclass(kw_only=True)
class TregistroReqNsf:
    """
    Tipo Requisição de Registro de Diploma Digital.

    :ivar dados_diploma_nsf:
    :ivar dados_privados_diplomado:
    :ivar termo_responsabilidade_emissora:
    :ivar documentacao_comprobatoria:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar id: Id
    :ivar ambiente: Especifica o contexto no qual o Diploma foi emitido.
        Apenas Diplomas emitidos no ambiente "Produção" são legalmente
        válidos. Caso não seja especificado, o Ambiente é "Produção" e o
        Diploma é legalmente válido.
    """
    class Meta:
        name = "TRegistroReqNSF"

    dados_diploma_nsf: TdadosDiplomaNsf = field(
        metadata={
            "name": "DadosDiplomaNSF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_privados_diplomado: TdadosPrivadosDiplomado = field(
        metadata={
            "name": "DadosPrivadosDiplomado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    termo_responsabilidade_emissora: None | TtermoResponsabilidade = field(
        default=None,
        metadata={
            "name": "TermoResponsabilidadeEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    documentacao_comprobatoria: None | TdocumentacaoComprobatoria = field(
        default=None,
        metadata={
            "name": "DocumentacaoComprobatoria",
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
            "pattern": r'ReqDip[0-9]{44}',
        }
    )
    ambiente: Tamb = field(
        default=Tamb.PRODU_O,
        metadata={
            "type": "Attribute",
        }
    )
@dataclass(kw_only=True)
class TregistroSegundaViaReq:
    """
    Tipo Requisição de Registro de Diploma Digital como segunda via de um
    diploma físico.

    :ivar dados_diploma:
    :ivar dados_diploma_nsf:
    :ivar dados_privados_diplomado:
    :ivar termo_responsabilidade_emissora:
    :ivar documentacao_comprobatoria:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar id: Id
    :ivar ambiente: Especifica o contexto no qual o Diploma foi emitido.
        Apenas Diplomas emitidos no ambiente "Produção" são legalmente
        válidos. Caso não seja especificado, o Ambiente é "Produção" e o
        Diploma é legalmente válido.
    """
    class Meta:
        name = "TRegistroSegundaViaReq"

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
    dados_privados_diplomado: TdadosPrivadosDiplomadoSegundaVia = field(
        metadata={
            "name": "DadosPrivadosDiplomado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    termo_responsabilidade_emissora: None | TtermoResponsabilidade = field(
        default=None,
        metadata={
            "name": "TermoResponsabilidadeEmissora",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    documentacao_comprobatoria: None | TdocumentacaoComprobatoria = field(
        default=None,
        metadata={
            "name": "DocumentacaoComprobatoria",
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
            "pattern": r'ReqDip[0-9]{44}',
        }
    )
    ambiente: Tamb = field(
        default=Tamb.PRODU_O,
        metadata={
            "type": "Attribute",
        }
    )
@dataclass(kw_only=True)
class TdocumentacaoAcademicaRegistro:
    """
    Tipo Documentação Acadêmica para Emissão e Registro.
    """
    class Meta:
        name = "TDocumentacaoAcademicaRegistro"

    registro_req: None | TregistroReq = field(
        default=None,
        metadata={
            "name": "RegistroReq",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    registro_req_nsf: None | TregistroReqNsf = field(
        default=None,
        metadata={
            "name": "RegistroReqNSF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    registro_segunda_via_req: None | TregistroSegundaViaReq = field(
        default=None,
        metadata={
            "name": "RegistroSegundaViaReq",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    registro_por_decisao_judicial_req: None | TregistroPorDecisaoJudicialReq = field(
        default=None,
        metadata={
            "name": "RegistroPorDecisaoJudicialReq",
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