from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


class Tamb(Enum):
    """
    Tipo Ambiente: Homologação / Produção.
    """
    PRODU_O = 'Produção'
    HOMOLOGA_O = 'Homologação'
@dataclass(kw_only=True)
class TcargaHoraria:
    """
    Tipo carga horária em Hora Aula ou em Hora Relógio.
    """
    class Meta:
        name = "TCargaHoraria"

    hora_aula: None | str = field(
        default=None,
        metadata={
            "name": "HoraAula",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    hora_relogio: None | Decimal = field(
        default=None,
        metadata={
            "name": "HoraRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
@dataclass(kw_only=True)
class TcargaHorariaComEtiqueta:
    """
    Tipo carga horária em Hora Aula ou em Hora Relógio.

    :ivar hora_aula:
    :ivar hora_relogio:
    :ivar etiqueta: Um código de etiqueta opcional conforme especificado
        no currículo em infEtiqueta. Isto permite categorizar dentro do
        currículo em que tivo de atividade a carga horária foi
        realizada.
    """
    class Meta:
        name = "TCargaHorariaComEtiqueta"

    hora_aula: None | str = field(
        default=None,
        metadata={
            "name": "HoraAula",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    hora_relogio: None | Decimal = field(
        default=None,
        metadata={
            "name": "HoraRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
    etiqueta: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
class TcargosAssinantes(Enum):
    """
    Cargos de assinantes do diploma digital.
    """
    REITOR = 'Reitor'
    REITOR_EM_EXERC_CIO = 'Reitor em Exercício'
    RESPONS_VEL_PELO_REGISTRO = 'Responsável pelo registro'
    COORDENADOR_DE_CURSO = 'Coordenador de Curso'
    SUBCOORDENADOR_DE_CURSO = 'Subcoordenador de Curso'
    COORDENADOR_DE_CURSO_EM_EXERC_CIO = 'Coordenador de Curso em exercício'
    CHEFE_DA_REA_DE_REGISTRO_DE_DIPLOMAS = 'Chefe da área de registro de diplomas'
    CHEFE_EM_EXERC_CIO_DA_REA_DE_REGISTRO_DE_DIPLOMAS = 'Chefe em exercício da área de registro de diplomas'
class Tconceito(Enum):
    """
    Tipo Conceito.
    """
    A = 'A+'
    A_1 = 'A'
    A_2 = 'A-'
    B = 'B+'
    B_1 = 'B'
    B_2 = 'B-'
    C = 'C+'
    C_1 = 'C'
    C_2 = 'C-'
    D = 'D+'
    D_1 = 'D'
    D_2 = 'D-'
    E = 'E+'
    E_1 = 'E'
    E_2 = 'E-'
    F = 'F+'
    F_1 = 'F'
    F_2 = 'F-'
class TconceitoRm(Enum):
    """
    Tipo Conceito RM.
    """
    A = 'A'
    B = 'B'
    C = 'C'
    APD = 'APD'
    APP = 'APP'
    APR = 'APR'
class TenumCondicaoEnade(Enum):
    """
    Condição do Estudante durante a prestação do Enade.
    """
    INGRESSANTE = 'Ingressante'
    CONCLUINTE = 'Concluinte'
class TenumMotivoNaoHabilitacaoAlunoEnadeHistorico(Enum):
    """
    Motivos de não habilitação no ENADE de acordo com Portaria Normativa
    MEC nº 840/2018.
    """
    ESTUDANTE_N_O_HABILITADO_AO_ENADE_EM_RAZ_O_DO_CALEND_RIO_DO_CICLO_AVALIATIVO = 'Estudante não habilitado ao Enade em razão do calendário do ciclo avaliativo'
    ESTUDANTE_N_O_HABILITADO_AO_ENADE_EM_RAZ_O_DA_NATUREZA_DO_PROJETO_PEDAG_GICO_DO_CURSO = 'Estudante não habilitado ao Enade em razão da natureza do projeto pedagógico do curso'
class TformaAcessoCurso(Enum):
    """
    Tipo forma de acesso ao curso.

    Será usado as mesmas formas usadas no Censo.
    """
    VESTIBULAR = 'Vestibular'
    ENEM = 'Enem'
    AVALIA_O_SERIADA = 'Avaliação Seriada'
    SELE_O_SIMPLIFICADA = 'Seleção Simplificada'
    EGRESSO_BI_LI = 'Egresso BI/LI'
    PEC_G = 'PEC-G'
    TRANSFER_NCIA_EX_OFFICIO = 'Transferência Ex Officio'
    DECIS_O_JUDICIAL = 'Decisão judicial'
    SELE_O_PARA_VAGAS_REMANESCENTES = 'Seleção para Vagas Remanescentes'
    SELE_O_PARA_VAGAS_DE_PROGRAMAS_ESPECIAIS = 'Seleção para Vagas de Programas Especiais'
class TgrauConferido(Enum):
    """
    Tipo grau conferido pelo curso.
    """
    TECN_LOGO = 'Tecnólogo'
    BACHARELADO = 'Bacharelado'
    LICENCIATURA = 'Licenciatura'
    CURSO_SEQUENCIAL = 'Curso sequencial'
@dataclass(kw_only=True)
class ThoraRelogioComEtiqueta:
    """
    :ivar value:
    :ivar etiqueta: Um código de etiqueta opcional conforme especificado
        no currículo em infEtiqueta. Isto permite categorizar dentro do
        currículo em que tivo de atividade a carga horária foi
        realizada.
    """
    class Meta:
        name = "THoraRelogioComEtiqueta"

    value: Decimal = field(
        metadata={
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
    etiqueta: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
class TmodalidadeCurso(Enum):
    """
    Tipo modalidade de curso.
    """
    PRESENCIAL = 'Presencial'
    EAD = 'EAD'
class TmodalidadeCursoNsf(Enum):
    """
    Tipo modalidade de curso para IES não.
    """
    PRESENCIAL = 'Presencial'
    EAD = 'EAD'
    SEMIPRESENCIAL = 'Semipresencial'
@dataclass(kw_only=True)
class ToutroDocumentoIdentificacao:
    """
    Tipo Outro Documento de Identificação.
    """
    class Meta:
        name = "TOutroDocumentoIdentificacao"

    tipo_documento: str = field(
        metadata={
            "name": "TipoDocumento",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    identificador: str = field(
        metadata={
            "name": "Identificador",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
class Tsexo(Enum):
    """
    Tipo Sexo.
    """
    F = 'F'
    M = 'M'
class TsimNao(Enum):
    """
    Tipo boolean indicando sim/não.
    """
    SIM = 'Sim'
    N_O = 'Não'
class TtipoAto(Enum):
    """
    Tipo de ato.
    """
    PARECER = 'Parecer'
    RESOLU_O = 'Resolução'
    DECRETO = 'Decreto'
    PORTARIA = 'Portaria'
    DELIBERA_O = 'Deliberação'
    DESPACHO = 'Despacho'
    LEI_FEDERAL = 'Lei Federal'
    LEI_ESTADUAL = 'Lei Estadual'
    LEI_MUNICIPAL = 'Lei Municipal'
class TtipoAtoComAtoProprio(Enum):
    """
    Tipo de ato.
    """
    PARECER = 'Parecer'
    RESOLU_O = 'Resolução'
    DECRETO = 'Decreto'
    PORTARIA = 'Portaria'
    DELIBERA_O = 'Deliberação'
    LEI_FEDERAL = 'Lei Federal'
    LEI_ESTADUAL = 'Lei Estadual'
    LEI_MUNICIPAL = 'Lei Municipal'
    ATO_PR_PRIO = 'Ato Próprio'
class Ttitulacao(Enum):
    """
    Tipo Titulação.
    """
    TECN_LOGO = 'Tecnólogo'
    GRADUA_O = 'Graduação'
    ESPECIALIZA_O = 'Especialização'
    MESTRADO = 'Mestrado'
    DOUTORADO = 'Doutorado'
class Ttitulo(Enum):
    """
    Tipos de títulos conferido pelo curso.
    """
    LICENCIADO = 'Licenciado'
    TECN_LOGO = 'Tecnólogo'
    BACHAREL = 'Bacharel'
    M_DICO = 'Médico'
class Tuf(Enum):
    """
    Tipo Sigla da UF.
    """
    AC = 'AC'
    AL = 'AL'
    AM = 'AM'
    AP = 'AP'
    BA = 'BA'
    CE = 'CE'
    DF = 'DF'
    ES = 'ES'
    GO = 'GO'
    MA = 'MA'
    MG = 'MG'
    MS = 'MS'
    MT = 'MT'
    PA = 'PA'
    PB = 'PB'
    PE = 'PE'
    PI = 'PI'
    PR = 'PR'
    RJ = 'RJ'
    RN = 'RN'
    RO = 'RO'
    RR = 'RR'
    RS = 'RS'
    SC = 'SC'
    SE = 'SE'
    SP = 'SP'
    TO = 'TO'
@dataclass(kw_only=True)
class Tvazio:
    """
    Tipo Vazio.
    """
    class Meta:
        name = "TVazio"
class Tversao(Enum):
    """
    Tipo Versão.
    """
    VALUE_1_05 = '1.05'
@dataclass(kw_only=True)
class Tnaturalidade:
    """
    Tipo naturalidade.
    """
    class Meta:
        name = "TNaturalidade"

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
@dataclass(kw_only=True)
class Tpessoa:
    """
    Tipo Pessoa com nome, nome social e sexo.
    """
    class Meta:
        name = "TPessoa"

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
@dataclass(kw_only=True)
class Trg:
    """
    Tipo RG.
    """
    class Meta:
        name = "TRg"

    numero: str = field(
        metadata={
            "name": "Numero",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "max_length": 15,
            "white_space": "collapse",
            "pattern": r'[a-zA-Z0-9]{4,15}',
        }
    )
    orgao_expedidor: None | str = field(
        default=None,
        metadata={
            "name": "OrgaoExpedidor",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    uf: Tuf = field(
        metadata={
            "name": "UF",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TtituloConferido:
    class Meta:
        name = "TTituloConferido"

    titulo: None | Ttitulo = field(
        default=None,
        metadata={
            "name": "Titulo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    outro_titulo: None | str = field(
        default=None,
        metadata={
            "name": "OutroTitulo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class Tfiliacao:
    class Meta:
        name = "TFiliacao"

    genitor: list[Tpessoa] = field(
        default_factory=list,
        metadata={
            "name": "Genitor",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )