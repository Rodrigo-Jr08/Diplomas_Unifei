from __future__ import annotations
from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum
from xsdata.models.datatype import XmlDate
from generated.leiaute_diploma_digital_v1_05 import TdadosIesEmissora
from generated.leiaute_historico_escolar_v1_05 import (
    TdadosMinimoCurso,
    TdadosMinimoCursoNsf,
)
from generated.tipos_basicos_v1_05 import (
    Tamb,
    TsimNao,
    Tversao,
)
from generated.xmldsig_core_schema_v1_1 import Signature

__NAMESPACE__ = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"


@dataclass(kw_only=True)
class TatividadeComplementar:
    """
    Tipo que define uma atividade complementar.
    """
    class Meta:
        name = "TAtividadeComplementar"

    codigo: str = field(
        metadata={
            "name": "Codigo",
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
        }
    )
    limite_carga_horaria_em_hora_relogio: Decimal = field(
        metadata={
            "name": "LimiteCargaHorariaEmHoraRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
@dataclass(kw_only=True)
class TcodigoArea:
    """
    Código da área associadas a Unidade Curricular.
    """
    class Meta:
        name = "TCodigoArea"

    codigo: str = field(
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class Tcodigos:
    """
    Tipo que define uma lista de códigos de critérios de integralização.
    """
    class Meta:
        name = "TCodigos"

    codigo: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class TcriterioLimitesCargas:
    """
    Tipo que defina horários lista de critérios de integralização.
    """
    class Meta:
        name = "TCriterioLimitesCargas"

    carga_horaria_minima: None | Decimal = field(
        default=None,
        metadata={
            "name": "CargaHorariaMinima",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
    carga_horaria_maxima: None | Decimal = field(
        default=None,
        metadata={
            "name": "CargaHorariaMaxima",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
    carga_horaria_para_total: None | Decimal = field(
        default=None,
        metadata={
            "name": "CargaHorariaParaTotal",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
@dataclass(kw_only=True)
class TdadoArea:
    """
    Tipo que define informações sobre uma das Áreas usadas neste currículo.
    """
    class Meta:
        name = "TDadoArea"

    codigo: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    nome: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Nome",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class Tementa:
    """
    Define a Ementa de uma Unidade Curricular.

    Composta por uma lista de itens de Ementa.
    """
    class Meta:
        name = "TEmenta"

    item_ementa: list[str] = field(
        default_factory=list,
        metadata={
            "name": "ItemEmenta",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
@dataclass(kw_only=True)
class TequivalenciaUnidadesCurriculares:
    """
    Determina as equivalencias de UnidadeCurricular.

    Para ser equivalente todos os CodigosUnidadeEquivalente de pelo menos
    uma UnidadesCurricularesEquivalente devem estar presentes no histórico.
    """
    class Meta:
        name = "TEquivalenciaUnidadesCurriculares"

    unidades_curriculares_equivalente: list[TequivalenciaUnidadesCurriculares.UnidadesCurricularesEquivalente] = field(
        default_factory=list,
        metadata={
            "name": "UnidadesCurricularesEquivalente",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )

    @dataclass(kw_only=True)
    class UnidadesCurricularesEquivalente:
        codigo_unidade_equivalente: list[str] = field(
            default_factory=list,
            metadata={
                "name": "CodigoUnidadeEquivalente",
                "type": "Element",
                "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
                "min_occurs": 1,
                "white_space": "collapse",
                "pattern": r'[\w\d\-\.]{1,}',
            }
        )
@dataclass(kw_only=True)
class Tetiqueta:
    """
    Etiqueta que qualifica a Unidade Curricular para fins de cômputo da
    integralização curricular.

    Caso NumeroHorasParaIntegralizacao esteja presente, este número de
    horas será utilizado para fins de contabilização de carga horária. Caso
    NumeroHorasParaIntegralizacao não esteja presente, será usado a carga
    horária da Unidade Curricular.
    """
    class Meta:
        name = "TEtiqueta"

    codigo: str = field(
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    carga_horaria_em_hora_aula: None | str = field(
        default=None,
        metadata={
            "name": "CargaHorariaEmHoraAula",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    carga_horaria_em_hora_relogio: None | Decimal = field(
        default=None,
        metadata={
            "name": "CargaHorariaEmHoraRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
@dataclass(kw_only=True)
class TpreRequisitosUnidadesCurriculares:
    """
    Lista de pré-requisitos de uma unidade curricular.

    Ou seja, unidades curriculares que devem ser cursadas antes que a
    presente Unidade Curricular possa ser cursada.
    """
    class Meta:
        name = "TPreRequisitosUnidadesCurriculares"

    codigo_dependencia: list[str] = field(
        default_factory=list,
        metadata={
            "name": "CodigoDependencia",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
            "white_space": "collapse",
            "pattern": r'[\w\d\-\.]{1,}',
        }
    )
@dataclass(kw_only=True)
class TsegurancaCurriculo:
    """
    Dados de segurança do currículo.
    """
    class Meta:
        name = "TSegurancaCurriculo"

    codigo_validacao: str = field(
        metadata={
            "name": "CodigoValidacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'\d{1,}\.[a-f0-9]{12,}',
        }
    )
class TtipoUnidadeCurricular(Enum):
    """
    Tipos de unidade curricular.
    """
    DISCIPLINA = 'Disciplina'
    M_DULO = 'Módulo'
    ATIVIDADE = 'Atividade'
    EST_GIO = 'Estágio'
    TRABALHO_DE_CONCLUS_O_DE_CURSO = 'Trabalho de Conclusão de Curso'
    MONOGRAFIA = 'Monografia'
    ARTIGO = 'Artigo'
    PROJETO = 'Projeto'
    PRODUTO = 'Produto'
    ATIVIDADE_COMPLEMENTAR = 'Atividade Complementar'
    ATIVIDADE_DE_EXTENS_O = 'Atividade de Extensão'
@dataclass(kw_only=True)
class Tareas:
    """
    Áreas/ênfases associadas a Unidade Curricular.
    """
    class Meta:
        name = "TAreas"

    area: list[TcodigoArea] = field(
        default_factory=list,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TatividadesComplementares:
    """
    Tipo que define uma lista de atividades complementar.
    """
    class Meta:
        name = "TAtividadesComplementares"

    atividade: list[TatividadeComplementar] = field(
        default_factory=list,
        metadata={
            "name": "Atividade",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
@dataclass(kw_only=True)
class TcriterioIntegralizacaoRotulos:
    """
    Tipo que define um critério de integralização que é atingindo quando o
    somatório de cargas horárias das Unidades Curriculares com etiquetas e
    tipo de unidade curricular atinge a Carga Horária Mínima, limitada a
    Carga Horária Máxima.

    :ivar codigo: O código será usado para referenciar este critério em
        CriterioIntegralizacaoExpressao
    :ivar unidade_curricular:
    :ivar etiqueta:
    :ivar cargas_horarias_criterio:
    """
    class Meta:
        name = "TCriterioIntegralizacaoRotulos"

    codigo: str = field(
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    unidade_curricular: None | TtipoUnidadeCurricular = field(
        default=None,
        metadata={
            "name": "UnidadeCurricular",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    etiqueta: list[str] = field(
        default_factory=list,
        metadata={
            "name": "Etiqueta",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    cargas_horarias_criterio: TcriterioLimitesCargas = field(
        metadata={
            "name": "CargasHorariasCriterio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TdadoEtiqueta:
    """
    Tipo que define informações sobre uma das etiquetas usadas neste
    currículo para classificação das unidades curriculares.
    """
    class Meta:
        name = "TDadoEtiqueta"

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
    aplicado_automaticamente_unidades_nao_pertencentes_ao_curriculo: None | TsimNao = field(
        default=None,
        metadata={
            "name": "AplicadoAutomaticamenteUnidadesNaoPertencentesAoCurriculo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class Tetiquetas:
    """
    Lista de Etiquetas, que qualificam a Unidade Curricular para fins de
    cômputo da integralização curricular.
    """
    class Meta:
        name = "TEtiquetas"

    etiqueta: list[Tetiqueta] = field(
        default_factory=list,
        metadata={
            "name": "Etiqueta",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
@dataclass(kw_only=True)
class Texpressao:
    """
    Tipo que define os possíveis operadores usados para definição de uma
    expressao.

    :ivar soma: Operador que permite computar um somatório de cargas
        horárias
    """
    class Meta:
        name = "TExpressao"

    soma: None | Tcodigos = field(
        default=None,
        metadata={
            "name": "Soma",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TinfAreas:
    """
    Tipo que define informações sobre as Áreas usadas neste currículo.
    """
    class Meta:
        name = "TInfAreas"

    area: list[TdadoArea] = field(
        default_factory=list,
        metadata={
            "name": "Area",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TcategoriaAtividadeComplementar:
    """
    Tipo que define um conjunto de atividades complementares associados a
    uma mesma categoria.
    """
    class Meta:
        name = "TCategoriaAtividadeComplementar"

    codigo: str = field(
        metadata={
            "name": "Codigo",
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
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    limite_carga_horaria_em_hora_relogio: None | Decimal = field(
        default=None,
        metadata={
            "name": "LimiteCargaHorariaEmHoraRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
    atividades: TatividadesComplementares = field(
        metadata={
            "name": "Atividades",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TcriterioIntegralizacaoExpressao:
    """
    Tipo que define um critério de integralização que é atingindo quando as
    cargas horárias calculadas a partir da expressão posta atingem a Carga
    Horária Mínima, limitada a Carga Horária Máxima.
    """
    class Meta:
        name = "TCriterioIntegralizacaoExpressao"

    codigo: str = field(
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_length": 1,
            "white_space": "preserve",
        }
    )
    expressao: Texpressao = field(
        metadata={
            "name": "Expressao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    cargas_horarias_criterio: TcriterioLimitesCargas = field(
        metadata={
            "name": "CargasHorariasCriterio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TinfEtiquetas:
    """
    Tipo que define informações sobre as etiquetas usadas neste currículo
    para classificação das unidades curriculares.
    """
    class Meta:
        name = "TInfEtiquetas"

    etiqueta: list[TdadoEtiqueta] = field(
        default_factory=list,
        metadata={
            "name": "Etiqueta",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
@dataclass(kw_only=True)
class TunidadeCurricular:
    """
    Tipo que define uma unidade curricular.
    """
    class Meta:
        name = "TUnidadeCurricular"

    tipo: TtipoUnidadeCurricular = field(
        metadata={
            "name": "Tipo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    codigo: str = field(
        metadata={
            "name": "Codigo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "collapse",
            "pattern": r'[\w\d\-\.]{1,}',
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
    carga_horaria_em_hora_aula: None | str = field(
        default=None,
        metadata={
            "name": "CargaHorariaEmHoraAula",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
        }
    )
    carga_horaria_em_hora_relogio: Decimal = field(
        metadata={
            "name": "CargaHorariaEmHoraRelogio",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": Decimal('0'),
            "fraction_digits": 2,
        }
    )
    ementa: None | Tementa = field(
        default=None,
        metadata={
            "name": "Ementa",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    fase: None | str = field(
        default=None,
        metadata={
            "name": "Fase",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "white_space": "preserve",
            "pattern": r'([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])(([\p{P}\p{Zs}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]])*([\p{P}]|[\p{IsBasicLatin}\p{IsLatin-1Supplement}\p{IsLatinExtended-A}\p{IsLatinExtended-B}-[\p{C}\p{Zs}]]))?',
        }
    )
    equivalencias: None | TequivalenciaUnidadesCurriculares = field(
        default=None,
        metadata={
            "name": "Equivalencias",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    pre_requisitos: None | TpreRequisitosUnidadesCurriculares = field(
        default=None,
        metadata={
            "name": "PreRequisitos",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    etiquetas: None | Tetiquetas = field(
        default=None,
        metadata={
            "name": "Etiquetas",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    areas: None | Tareas = field(
        default=None,
        metadata={
            "name": "Areas",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TinfCriteriosIntegralizacao:
    """
    Tipo que defina a lista de critérios de integralização.
    """
    class Meta:
        name = "TInfCriteriosIntegralizacao"

    criterio_integralizacao_rotulos: list[TcriterioIntegralizacaoRotulos] = field(
        default_factory=list,
        metadata={
            "name": "CriterioIntegralizacaoRotulos",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    criterio_integralizacao_expressao: list[TcriterioIntegralizacaoExpressao] = field(
        default_factory=list,
        metadata={
            "name": "CriterioIntegralizacaoExpressao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TinfEstruturaAtividadesComplementares:
    """
    Tipo que define a estruturação das atividades complementares que compõe
    a estrutura curricular do Curso.
    """
    class Meta:
        name = "TInfEstruturaAtividadesComplementares"

    categoria: list[TcategoriaAtividadeComplementar] = field(
        default_factory=list,
        metadata={
            "name": "Categoria",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
@dataclass(kw_only=True)
class TinfEstruturaCurricular:
    """
    Tipo que define as unidades que compõe a estrutura curricular do Curso.
    """
    class Meta:
        name = "TInfEstruturaCurricular"

    unidade_curricular: list[TunidadeCurricular] = field(
        default_factory=list,
        metadata={
            "name": "UnidadeCurricular",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_occurs": 1,
        }
    )
@dataclass(kw_only=True)
class TinfCurriculoEscolar:
    """
    Tipo que define o conjunto de informações referentes ao Currículo
    Escolar de um Curso.

    :ivar codigo_curriculo:
    :ivar data_curriculo:
    :ivar minutos_relogio_da_hora_aula:
    :ivar nome_para_areas:
    :ivar dados_curso:
    :ivar dados_curso_nsf:
    :ivar ies_emissora:
    :ivar inf_etiquetas:
    :ivar inf_areas:
    :ivar inf_estrutura_curricular:
    :ivar inf_estrutura_atividades_complementares:
    :ivar inf_criterios_integralizacao:
    :ivar seguranca_curriculo:
    :ivar informacoes_adicionais:
    :ivar versao: Versão do leiaute (v1.05)
    :ivar ambiente: Especifica o contexto no qual o Curriculo Escolar
        foi emitido. Apenas Curriculos Escolares emitidos no ambiente
        "Produção" são legalmente válidos. Caso não seja especificado, o
        Ambiente é "Produção" e o Curriculo Escolar é legalmente válido.
    """
    class Meta:
        name = "TInfCurriculoEscolar"

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
    data_curriculo: XmlDate = field(
        metadata={
            "name": "DataCurriculo",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    minutos_relogio_da_hora_aula: str = field(
        metadata={
            "name": "MinutosRelogioDaHoraAula",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
            "min_inclusive": "0",
            "pattern": r'[1-9][0-9]*',
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
    inf_etiquetas: TinfEtiquetas = field(
        metadata={
            "name": "infEtiquetas",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    inf_areas: TinfAreas = field(
        metadata={
            "name": "infAreas",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    inf_estrutura_curricular: TinfEstruturaCurricular = field(
        metadata={
            "name": "infEstruturaCurricular",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    inf_estrutura_atividades_complementares: None | TinfEstruturaAtividadesComplementares = field(
        default=None,
        metadata={
            "name": "infEstruturaAtividadesComplementares",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    inf_criterios_integralizacao: TinfCriteriosIntegralizacao = field(
        metadata={
            "name": "infCriteriosIntegralizacao",
            "type": "Element",
            "namespace": "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd",
        }
    )
    seguranca_curriculo: TsegurancaCurriculo = field(
        metadata={
            "name": "SegurancaCurriculo",
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
class TcurriculoEscolar:
    """
    Documento descritivo de um Currículo Escolar de um Projeto Pedagógico
    de Curso (PPC).
    """
    class Meta:
        name = "TCurriculoEscolar"

    inf_curriculo_escolar: TinfCurriculoEscolar = field(
        metadata={
            "name": "infCurriculoEscolar",
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