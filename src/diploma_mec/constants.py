from __future__ import annotations

from pathlib import Path

MEC_NAMESPACE = "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"
DS_NAMESPACE = "http://www.w3.org/2000/09/xmldsig#"
MEC_XSD_VERSION = "1.05"

PROJECT_ROOT = Path(__file__).resolve().parents[2]
SCHEMAS_DIR = PROJECT_ROOT / "schemas"
GENERATED_DIR = PROJECT_ROOT / "generated"

DOCUMENTACAO_REGISTRO_XSD = SCHEMAS_DIR / "DocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd"
LEIAUTE_DIPLOMA_XSD = SCHEMAS_DIR / "leiauteDiplomaDigital_v1.05.xsd"
LEIAUTE_DOCUMENTACAO_XSD = SCHEMAS_DIR / "leiauteDocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd"
LEIAUTE_HISTORICO_XSD = SCHEMAS_DIR / "leiauteHistoricoEscolar_v1.05.xsd"
TIPOS_BASICOS_XSD = SCHEMAS_DIR / "tiposBasicos_v1.05.xsd"
XMLDSIG_XSD = SCHEMAS_DIR / "xmldsig-core-schema_v1.1.xsd"

# O pacote oficial possui mais arquivos do que os presentes no ZIP original.
OFFICIAL_V105_FILES = (
    "DiplomaDigital_v1.05.xsd",
    "DocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd",
    "HistoricoEscolarDigital_v1.05.xsd",
    "ListaDiplomasAnulados_v1.05.xsd",
    "ArquivoFiscalizacao_v1.05.xsd",
    "CurriculoEscolarDigital_v1.05.xsd",
    "tiposBasicos_v1.05.xsd",
    "leiauteDiplomaDigital_v1.05.xsd",
    "leiauteDocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd",
    "leiauteHistoricoEscolar_v1.05.xsd",
    "leiauteListaDiplomasAnulados_v1.05.xsd",
    "leiauteArquivoFiscalizacao_v1.05.xsd",
    "leiauteCurriculoEscolar_v1.05.xsd",
    "xmldsig-core-schema_v1.1.xsd",
)
