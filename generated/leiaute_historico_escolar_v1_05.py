from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from xsdata.models.datatype import XmlDate
from generated.leiaute_diploma_digital_v1_05 import (
    TatoRegulatorioComOuSemEmec,
    TdadosDiplomado,
    TdadosIesEmissora,
    Thabilitacao,
    TinformacoesTramitacaoEmec,
)
from generated.tipos_basicos_v1_05 import (
    Tamb,
    TcargaHoraria,
    TcargaHorariaComEtiqueta,
    Tconceito,
    TconceitoRm,
    TenumCondicaoEnade,
    TenumMotivoNaoHabilitacaoAlunoEnadeHistorico,
    TformaAcessoCurso,
    ThoraRelogioComEtiqueta,
    Ttitulacao,
    Tvazio,
    Tversao,
)
from generated.xmldsig_core_schema_v1_1 import Signature

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class TareaComNome:
    """
    Código e nome da Área/ênfase/linha de formação integralizada pelo
    aluno.
    """
    class Meta:
        name = "TAreaComNome"

    codigo: str = field(
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    nome: str = field(
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class TconcedenteEstagio:
    """
    Informações sobre Concedente onde foi realizado estágio.
    """
    class Meta:
        name = "TConcedenteEstagio"

    razao_social: None | str = field(
        default=None,
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
    nome_fantasia: None | str = field(
        default=None,
        metadata={
            "name": "NomeFantasia",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
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
    nome: None | str = field(
        default=None,
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
    cpf: None | str = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 11,
            "white_space": "collapse",
            "pattern": r'[0-9]{11}',
        }
    )
class TformaIntegralizacao(Enum):
    """
    Forma de integralização desta entrada no histórico.
    """
    CURSADO = 'Cursado'
    VALIDADO = 'Validado'
    APROVEITADO = 'Aproveitado'
@dataclass(kw_only=True)
class TsegurancaHistorico:
    """
    Dados de segurança do histórico.
    """
    class Meta:
        name = "TSegurancaHistorico"

    codigo_validacao: str = field(
        metadata={
            "name": "CodigoValidacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'\d{1,}\.[a-f0-9]{12,}',
        }
    )
@dataclass(kw_only=True)
class TsituacaoFormado:
    class Meta:
        name = "TSituacaoFormado"

    data_conclusao_curso: XmlDate = field(
        metadata={
            "name": "DataConclusaoCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
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
@dataclass(kw_only=True)
class TsituacaoIntercambio:
    class Meta:
        name = "TSituacaoIntercambio"

    instituicao: None | str = field(
        default=None,
        metadata={
            "name": "Instituicao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    pais: None | str = field(
        default=None,
        metadata={
            "name": "Pais",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    nome_programa_intercambio: None | str = field(
        default=None,
        metadata={
            "name": "NomeProgramaIntercambio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class TareasComNome:
    """
    Áreas/ênfases/linhas de formação integralizadas pelo aluno.
    """
    class Meta:
        name = "TAreasComNome"

    area: list[TareaComNome] = field(
        default_factory=list,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadosMinimoCurso:
    """
    Dados mínimos do curso.
    """
    class Meta:
        name = "TDadosMinimoCurso"

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
class TdadosMinimoCursoNsf:
    """
    Dados mínimos do curso para IES emissoras que não fazem parte do
    sistema federal de regulação.
    """
    class Meta:
        name = "TDadosMinimoCursoNSF"

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
class TdisciplinaAprovada:
    class Meta:
        name = "TDisciplinaAprovada"

    forma_integralizacao: None | TformaIntegralizacao = field(
        default=None,
        metadata={
            "name": "FormaIntegralizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    outra_forma_integralizacao: None | str = field(
        default=None,
        metadata={
            "name": "OutraFormaIntegralizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class Tdocente:
    """
    Informações sobre Docente responsável pela Entrada no Histórico.
    """
    class Meta:
        name = "TDocente"

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
    titulacao: Ttitulacao = field(
        metadata={
            "name": "Titulacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    lattes: None | str = field(
        default=None,
        metadata={
            "name": "Lattes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
            "pattern": r'http://lattes\.cnpq\.br/\d+',
        }
    )
    cpf: None | str = field(
        default=None,
        metadata={
            "name": "CPF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 11,
            "white_space": "collapse",
            "pattern": r'[0-9]{11}',
        }
    )
@dataclass(kw_only=True)
class TentradaHistoricoSituacaoDiscentePeriodoLetivo:
    class Meta:
        name = "TEntradaHistoricoSituacaoDiscentePeriodoLetivo"

    periodo_letivo: str = field(
        metadata={
            "name": "PeriodoLetivo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    trancamento: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Trancamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    matriculado_em_disciplina: None | Tvazio = field(
        default=None,
        metadata={
            "name": "MatriculadoEmDisciplina",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    licenca: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Licenca",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    intercambio_internacional: None | TsituacaoIntercambio = field(
        default=None,
        metadata={
            "name": "IntercambioInternacional",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    intercambio_nacional: None | TsituacaoIntercambio = field(
        default=None,
        metadata={
            "name": "IntercambioNacional",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    desistencia: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Desistencia",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    abandono: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Abandono",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    jubilado: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Jubilado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    formado: None | TsituacaoFormado = field(
        default=None,
        metadata={
            "name": "Formado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    outra_situacao: None | str = field(
        default=None,
        metadata={
            "name": "OutraSituacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class TinformacoesEnade:
    """
    Informações sobre condição do estudante e edição do Enade.
    """
    class Meta:
        name = "TInformacoesEnade"

    condicao: TenumCondicaoEnade = field(
        metadata={
            "name": "Condicao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    edicao: str = field(
        metadata={
            "name": "Edicao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'[0-9]{4}',
        }
    )
@dataclass(kw_only=True)
class TsituacaoAtualDiscente:
    class Meta:
        name = "TSituacaoAtualDiscente"

    periodo_letivo: None | str = field(
        default=None,
        metadata={
            "name": "PeriodoLetivo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    trancamento: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Trancamento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    matriculado_em_disciplina: None | Tvazio = field(
        default=None,
        metadata={
            "name": "MatriculadoEmDisciplina",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    licenca: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Licenca",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    intercambio_internacional: None | TsituacaoIntercambio = field(
        default=None,
        metadata={
            "name": "IntercambioInternacional",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    intercambio_nacional: None | TsituacaoIntercambio = field(
        default=None,
        metadata={
            "name": "IntercambioNacional",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    desistencia: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Desistencia",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    abandono: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Abandono",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    jubilado: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Jubilado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    formado: None | TsituacaoFormado = field(
        default=None,
        metadata={
            "name": "Formado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    outra_situacao: None | str = field(
        default=None,
        metadata={
            "name": "OutraSituacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class Tdocentes:
    """
    Relação de Docentes.
    """
    class Meta:
        name = "TDocentes"

    docente: list[Tdocente] = field(
        default_factory=list,
        metadata={
            "name": "Docente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
@dataclass(kw_only=True)
class TenadeNaoHabilitado(TinformacoesEnade):
    """
    Informações sobre estudantes não habilitados para o ENADE.
    """
    class Meta:
        name = "TEnadeNaoHabilitado"

    motivo: None | TenumMotivoNaoHabilitacaoAlunoEnadeHistorico = field(
        default=None,
        metadata={
            "name": "Motivo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    outro_motivo: None | str = field(
        default=None,
        metadata={
            "name": "OutroMotivo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class Tenade:
    """
    Informações sobre a participação no ENADE.
    """
    class Meta:
        name = "TEnade"

    habilitado: list[TinformacoesEnade] = field(
        default_factory=list,
        metadata={
            "name": "Habilitado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    nao_habilitado: list[TenadeNaoHabilitado] = field(
        default_factory=list,
        metadata={
            "name": "NaoHabilitado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    irregular: list[TinformacoesEnade] = field(
        default_factory=list,
        metadata={
            "name": "Irregular",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
@dataclass(kw_only=True)
class TentradaHistoricoAtividadeComplementar:
    class Meta:
        name = "TEntradaHistoricoAtividadeComplementar"

    codigo_atividade_complementar: str = field(
        metadata={
            "name": "CodigoAtividadeComplementar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'[\w\d\-\.]{1,}',
        }
    )
    data_inicio: XmlDate = field(
        metadata={
            "name": "DataInicio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_fim: XmlDate = field(
        metadata={
            "name": "DataFim",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_registro: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DataRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    tipo_atividade_complementar: str = field(
        metadata={
            "name": "TipoAtividadeComplementar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    descricao: None | str = field(
        default=None,
        metadata={
            "name": "Descricao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    carga_horaria_em_hora_relogio: list[ThoraRelogioComEtiqueta] = field(
        default_factory=list,
        metadata={
            "name": "CargaHorariaEmHoraRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
    docentes_responsaveis_pela_validacao: Tdocentes = field(
        metadata={
            "name": "DocentesResponsaveisPelaValidacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TentradaHistoricoAtividadeComplementarSegundaViaNatoFisica:
    class Meta:
        name = "TEntradaHistoricoAtividadeComplementarSegundaViaNatoFisica"

    codigo_atividade_complementar: None | str = field(
        default=None,
        metadata={
            "name": "CodigoAtividadeComplementar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'[\w\d\-\.]{1,}',
        }
    )
    data_inicio: XmlDate = field(
        metadata={
            "name": "DataInicio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_fim: XmlDate = field(
        metadata={
            "name": "DataFim",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_registro: None | XmlDate = field(
        default=None,
        metadata={
            "name": "DataRegistro",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    tipo_atividade_complementar: str = field(
        metadata={
            "name": "TipoAtividadeComplementar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    descricao: None | str = field(
        default=None,
        metadata={
            "name": "Descricao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    carga_horaria_em_hora_relogio: list[ThoraRelogioComEtiqueta] = field(
        default_factory=list,
        metadata={
            "name": "CargaHorariaEmHoraRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
    docentes_responsaveis_pela_validacao: Tdocentes = field(
        metadata={
            "name": "DocentesResponsaveisPelaValidacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TentradaHistoricoDisciplina:
    class Meta:
        name = "TEntradaHistoricoDisciplina"

    codigo_disciplina: str = field(
        metadata={
            "name": "CodigoDisciplina",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'[\w\d\-\.]{1,}',
        }
    )
    nome_disciplina: str = field(
        metadata={
            "name": "NomeDisciplina",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    periodo_letivo: str = field(
        metadata={
            "name": "PeriodoLetivo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    carga_horaria: list[TcargaHorariaComEtiqueta] = field(
        default_factory=list,
        metadata={
            "name": "CargaHoraria",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
    nota: None | Decimal = field(
        default=None,
        metadata={
            "name": "Nota",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "max_inclusive": Decimal('10'),
            "fraction_digits": 2,
        }
    )
    nota_ate_cem: None | Decimal = field(
        default=None,
        metadata={
            "name": "NotaAteCem",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "max_inclusive": Decimal('100'),
            "fraction_digits": 2,
        }
    )
    conceito: None | Tconceito = field(
        default=None,
        metadata={
            "name": "Conceito",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    conceito_rm: None | TconceitoRm = field(
        default=None,
        metadata={
            "name": "ConceitoRM",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    conceito_especifico_do_curso: None | str = field(
        default=None,
        metadata={
            "name": "ConceitoEspecificoDoCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    aprovado: None | TdisciplinaAprovada = field(
        default=None,
        metadata={
            "name": "Aprovado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    pendente: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Pendente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    reprovado: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Reprovado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    docentes: Tdocentes = field(
        metadata={
            "name": "Docentes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TentradaHistoricoDisciplinaSegundaViaNatoFisica:
    """
    Em segundas vias de históricos nato-físicos é flexibilizada a exigência
    da especificação do Docente.
    """
    class Meta:
        name = "TEntradaHistoricoDisciplinaSegundaViaNatoFisica"

    codigo_disciplina: None | str = field(
        default=None,
        metadata={
            "name": "CodigoDisciplina",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'[\w\d\-\.]{1,}',
        }
    )
    nome_disciplina: str = field(
        metadata={
            "name": "NomeDisciplina",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    periodo_letivo: str = field(
        metadata={
            "name": "PeriodoLetivo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    carga_horaria: list[TcargaHorariaComEtiqueta] = field(
        default_factory=list,
        metadata={
            "name": "CargaHoraria",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
    nota: None | Decimal = field(
        default=None,
        metadata={
            "name": "Nota",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "max_inclusive": Decimal('10'),
            "fraction_digits": 2,
        }
    )
    nota_ate_cem: None | Decimal = field(
        default=None,
        metadata={
            "name": "NotaAteCem",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "max_inclusive": Decimal('100'),
            "fraction_digits": 2,
        }
    )
    conceito: None | Tconceito = field(
        default=None,
        metadata={
            "name": "Conceito",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    conceito_rm: None | TconceitoRm = field(
        default=None,
        metadata={
            "name": "ConceitoRM",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    conceito_especifico_do_curso: None | str = field(
        default=None,
        metadata={
            "name": "ConceitoEspecificoDoCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    aprovado: None | TdisciplinaAprovada = field(
        default=None,
        metadata={
            "name": "Aprovado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    pendente: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Pendente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    reprovado: None | Tvazio = field(
        default=None,
        metadata={
            "name": "Reprovado",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    docentes: None | Tdocentes = field(
        default=None,
        metadata={
            "name": "Docentes",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TentradaHistoricoEstagio:
    class Meta:
        name = "TEntradaHistoricoEstagio"

    codigo_unidade_curricular: str = field(
        metadata={
            "name": "CodigoUnidadeCurricular",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'[\w\d\-\.]{1,}',
        }
    )
    data_inicio: XmlDate = field(
        metadata={
            "name": "DataInicio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_fim: XmlDate = field(
        metadata={
            "name": "DataFim",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    concedente: None | TconcedenteEstagio = field(
        default=None,
        metadata={
            "name": "Concedente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    descricao: None | str = field(
        default=None,
        metadata={
            "name": "Descricao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    carga_horaria_em_horas_relogio: list[ThoraRelogioComEtiqueta] = field(
        default_factory=list,
        metadata={
            "name": "CargaHorariaEmHorasRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
    docentes_orientadores: Tdocentes = field(
        metadata={
            "name": "DocentesOrientadores",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TentradaHistoricoEstagioSegundaViaNatoFisica:
    class Meta:
        name = "TEntradaHistoricoEstagioSegundaViaNatoFisica"

    codigo_unidade_curricular: str = field(
        metadata={
            "name": "CodigoUnidadeCurricular",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'[\w\d\-\.]{1,}',
        }
    )
    data_inicio: XmlDate = field(
        metadata={
            "name": "DataInicio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_fim: XmlDate = field(
        metadata={
            "name": "DataFim",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    concedente: None | TconcedenteEstagio = field(
        default=None,
        metadata={
            "name": "Concedente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    descricao: None | str = field(
        default=None,
        metadata={
            "name": "Descricao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    carga_horaria_em_horas_relogio: list[ThoraRelogioComEtiqueta] = field(
        default_factory=list,
        metadata={
            "name": "CargaHorariaEmHorasRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
    docentes_orientadores: Tdocentes = field(
        metadata={
            "name": "DocentesOrientadores",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TelementosHistorico:
    """
    Entradas do histórico escolar.
    """
    class Meta:
        name = "TElementosHistorico"

    disciplina: list[TentradaHistoricoDisciplina] = field(
        default_factory=list,
        metadata={
            "name": "Disciplina",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    atividade_complementar: list[TentradaHistoricoAtividadeComplementar] = field(
        default_factory=list,
        metadata={
            "name": "AtividadeComplementar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    estagio: list[TentradaHistoricoEstagio] = field(
        default_factory=list,
        metadata={
            "name": "Estagio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    situacao_discente: list[TentradaHistoricoSituacaoDiscentePeriodoLetivo] = field(
        default_factory=list,
        metadata={
            "name": "SituacaoDiscente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
@dataclass(kw_only=True)
class TelementosHistoricoSegundaViaNatoFisico:
    """
    Entradas do histórico escolar de segundas vias nato fisicas.
    """
    class Meta:
        name = "TElementosHistoricoSegundaViaNatoFisico"

    disciplina: list[TentradaHistoricoDisciplinaSegundaViaNatoFisica] = field(
        default_factory=list,
        metadata={
            "name": "Disciplina",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    atividade_complementar: list[TentradaHistoricoAtividadeComplementarSegundaViaNatoFisica] = field(
        default_factory=list,
        metadata={
            "name": "AtividadeComplementar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    estagio: list[TentradaHistoricoEstagioSegundaViaNatoFisica] = field(
        default_factory=list,
        metadata={
            "name": "Estagio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
    situacao_discente: list[TentradaHistoricoSituacaoDiscentePeriodoLetivo] = field(
        default_factory=list,
        metadata={
            "name": "SituacaoDiscente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "sequence": 1,
        }
    )
@dataclass(kw_only=True)
class ThistoricoEscolar:
    """
    Dados do historico.
    """
    class Meta:
        name = "THistoricoEscolar"

    codigo_curriculo: str = field(
        metadata={
            "name": "CodigoCurriculo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    elementos_historico: TelementosHistorico = field(
        metadata={
            "name": "ElementosHistorico",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    nome_para_areas: None | str = field(
        default=None,
        metadata={
            "name": "NomeParaAreas",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    areas: None | TareasComNome = field(
        default=None,
        metadata={
            "name": "Areas",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_emissao_historico: XmlDate = field(
        metadata={
            "name": "DataEmissaoHistorico",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    hora_emissao_historico: str = field(
        metadata={
            "name": "HoraEmissaoHistorico",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])',
        }
    )
    situacao_atual_discente: TsituacaoAtualDiscente = field(
        metadata={
            "name": "SituacaoAtualDiscente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    enade: Tenade = field(
        metadata={
            "name": "ENADE",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    carga_horaria_curso_integralizada: TcargaHoraria = field(
        metadata={
            "name": "CargaHorariaCursoIntegralizada",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    carga_horaria_curso: TcargaHoraria = field(
        metadata={
            "name": "CargaHorariaCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    ingresso_curso: ThistoricoEscolar.IngressoCurso = field(
        metadata={
            "name": "IngressoCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )

    @dataclass(kw_only=True)
    class IngressoCurso:
        data: XmlDate = field(
            metadata={
                "name": "Data",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            }
        )
        forma_acesso: TformaAcessoCurso = field(
            metadata={
                "name": "FormaAcesso",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            }
        )
@dataclass(kw_only=True)
class ThistoricoEscolarSegundaVia:
    """
    Dados do historico para segundas vias de históricos nato físicos.
    """
    class Meta:
        name = "THistoricoEscolarSegundaVia"

    codigo_curriculo: None | str = field(
        default=None,
        metadata={
            "name": "CodigoCurriculo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    elementos_historico: TelementosHistoricoSegundaViaNatoFisico = field(
        metadata={
            "name": "ElementosHistorico",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    nome_para_areas: None | str = field(
        default=None,
        metadata={
            "name": "NomeParaAreas",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    areas: None | TareasComNome = field(
        default=None,
        metadata={
            "name": "Areas",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    data_emissao_historico: XmlDate = field(
        metadata={
            "name": "DataEmissaoHistorico",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    hora_emissao_historico: str = field(
        metadata={
            "name": "HoraEmissaoHistorico",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'(([0-1][0-9])|([2][0-3])):([0-5][0-9]):([0-5][0-9])',
        }
    )
    situacao_atual_discente: TsituacaoAtualDiscente = field(
        metadata={
            "name": "SituacaoAtualDiscente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    enade: None | Tenade = field(
        default=None,
        metadata={
            "name": "ENADE",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    carga_horaria_curso_integralizada: TcargaHoraria = field(
        metadata={
            "name": "CargaHorariaCursoIntegralizada",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    carga_horaria_curso: TcargaHoraria = field(
        metadata={
            "name": "CargaHorariaCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    ingresso_curso: None | ThistoricoEscolarSegundaVia.IngressoCurso = field(
        default=None,
        metadata={
            "name": "IngressoCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )

    @dataclass(kw_only=True)
    class IngressoCurso:
        data: XmlDate = field(
            metadata={
                "name": "Data",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            }
        )
        forma_acesso: list[TformaAcessoCurso] = field(
            default_factory=list,
            metadata={
                "name": "FormaAcesso",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "min_occurs": 1,
            }
        )
        ano_mes_processo_seletivo: None | str = field(
            default=None,
            metadata={
                "name": "AnoMesProcessoSeletivo",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "white_space": "preserve",
                "pattern": r'[0-9]{4}-[0-9]{2}',
            }
        )
@dataclass(kw_only=True)
class TinfHistoricoEscolar:
    """
    Tipo que define o conjunto de informações referentes a um Histórico
    Escolar Digital.

    :ivar aluno:
    :ivar dados_curso:
    :ivar dados_curso_nsf:
    :ivar ies_emissora:
    :ivar historico_escolar:
    :ivar seguranca_historico:
    :ivar informacoes_adicionais:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar ambiente: Especifica o contexto no qual o Histórico foi
        emitido. Apenas Históricos emitidos no ambiente "Produção" são
        legalmente válidos. Caso não seja especificado, o Ambiente é
        "Produção" e o Histórico é legalmente válido.
    """
    class Meta:
        name = "TInfHistoricoEscolar"

    aluno: TdadosDiplomado = field(
        metadata={
            "name": "Aluno",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_curso: None | TdadosMinimoCurso = field(
        default=None,
        metadata={
            "name": "DadosCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_curso_nsf: None | TdadosMinimoCursoNsf = field(
        default=None,
        metadata={
            "name": "DadosCursoNSF",
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
    historico_escolar: ThistoricoEscolar = field(
        metadata={
            "name": "HistoricoEscolar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    seguranca_historico: TsegurancaHistorico = field(
        metadata={
            "name": "SegurancaHistorico",
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
class TinfHistoricoEscolarSegundaViaNatoFisico:
    """
    Tipo que define o conjunto de informações referentes a um Histórico
    Escolar Digital para segundas vias Nato Físicos.

    :ivar aluno:
    :ivar dados_curso:
    :ivar dados_curso_nsf:
    :ivar ies_emissora:
    :ivar historico_escolar:
    :ivar seguranca_historico:
    :ivar informacoes_adicionais:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar ambiente: Especifica o contexto no qual o Histórico foi
        emitido. Apenas Históricos emitidos no ambiente "Produção" são
        legalmente válidos. Caso não seja especificado, o Ambiente é
        "Produção" e o Histórico é legalmente válido.
    """
    class Meta:
        name = "TInfHistoricoEscolarSegundaViaNatoFisico"

    aluno: TdadosDiplomado = field(
        metadata={
            "name": "Aluno",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_curso: None | TdadosMinimoCurso = field(
        default=None,
        metadata={
            "name": "DadosCurso",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    dados_curso_nsf: None | TdadosMinimoCursoNsf = field(
        default=None,
        metadata={
            "name": "DadosCursoNSF",
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
    historico_escolar: ThistoricoEscolarSegundaVia = field(
        metadata={
            "name": "HistoricoEscolar",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    seguranca_historico: TsegurancaHistorico = field(
        metadata={
            "name": "SegurancaHistorico",
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
class TdocumentoHistoricoEscolarDigital:
    """
    Documento de Histórico Escolar Digital.
    """
    class Meta:
        name = "TDocumentoHistoricoEscolarDigital"

    inf_historico_escolar: TinfHistoricoEscolar = field(
        metadata={
            "name": "infHistoricoEscolar",
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
@dataclass(kw_only=True)
class TdocumentoHistoricoEscolarSegundaViaNatoFisico:
    """
    Documento de Histórico Escolar Digital para segundas vias Nato Físicos.
    """
    class Meta:
        name = "TDocumentoHistoricoEscolarSegundaViaNatoFisico"

    inf_historico_escolar: TinfHistoricoEscolarSegundaViaNatoFisico = field(
        metadata={
            "name": "infHistoricoEscolar",
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