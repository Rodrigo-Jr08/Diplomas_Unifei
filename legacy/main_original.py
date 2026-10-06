import os
from xsdata.formats.dataclass.serializers import XmlSerializer  # type: ignore
from xsdata.formats.dataclass.serializers.config import SerializerConfig  # type: ignore
from xsdata.models.datatype import XmlDate, XmlTime  # type: ignore

# 1. Estrutura Raiz
from generated.documentacao_academica_registro_diploma_digital_v1_05 import DocumentacaoAcademicaRegistro

from generated.xmldsig_core_schema_v1_1 import (
    Signature,
    SignedInfo,
    SignatureValue,
    CanonicalizationMethod,
    SignatureMethod,
    Reference,
    DigestMethod,
)

# 2. Leiaute da Documentação Académica
from generated.leiaute_documentacao_academica_registro_diploma_digital_v1_05 import (
    TregistroReq,
    TdadosPrivadosDiplomado,
    TdocumentacaoComprobatoria,
)

# 3. Leiaute do Diploma Digital
from generated.leiaute_diploma_digital_v1_05 import (
    TdadosDiploma,
    TdadosDiplomado,
    TdadosCurso,
    TdadosIesEmissora,
    Tendereco,
)

# 4. Tipos Básicos (IN-05 Anexo I)
from generated.tipos_basicos_v1_05 import (
    Tnaturalidade,
    Tfiliacao,
    Tpessoa,
    TcargaHoraria,
    TformaAcessoCurso,
)

# 5. Leiaute do Histórico Escolar (IN-05 Anexo I - Seção 2.4)
from generated.leiaute_historico_escolar_v1_05 import (
    ThistoricoEscolar,
    TelementosHistorico,
    TentradaHistoricoDisciplina,
    Tdocente,
    Tdocentes,
    Tenade,
    TinformacoesEnade,
    TsituacaoAtualDiscente,
    TsituacaoFormado,
)


def gerar_xml_mock():
    print("Preenchendo dados simulados na estrutura de classes...")

    try:
        # --- A. AUXILIARES E ENDEREÇO ---
        naturalidade = Tnaturalidade(
            codigo_municipio=3132404,  # Código IBGE de Itajubá
            nome_municipio="Itajubá",
            uf="MG",
        )

        endereco_ies = Tendereco(
            logradouro="Av. BPS",
            numero="1303",
            complemento="Prédio Central",
            bairro="Pinheirinho",
            nome_municipio="Itajubá",
            uf="MG",
            cep="37500903",
        )

        # --- B. DADOS DO DIPLOMADO E CURSO ---
        dados_aluno = TdadosDiplomado(
            id="RA_UNIFEI_001",
            nome="Rodrigo Junior Lopes de Lira",
            nome_social="Rodrigo Junior Lopes de Lira",
            sexo="M",
            nacionalidade="Brasileira",
            naturalidade=naturalidade,
            cpf="11122233344",
            data_nascimento=XmlDate.from_string("2008-05-10"),
        )

        dados_curso = TdadosCurso(
            nome_curso="Engenharia da Computação",
            codigo_curso_emec="123456",
            modalidade="Presencial",
            titulo_conferido="Bacharel",
            grau_conferido="Graduação",
            endereco_curso="Itajubá",
            autorizacao="Ato Autorizacao 123",
            reconhecimento="Ato Reconhecimento 456",
        )

        dados_ies = TdadosIesEmissora(
            nome="Universidade Federal de Itajubá - UNIFEI",
            codigo_mec="584",
            cnpj="21040003000106",
            endereco=endereco_ies,
            credenciamento="Ato Credenciamento 789",
        )

        dados_diploma = TdadosDiploma(
            id="DIPLOMA_001",
            diplomado=dados_aluno,
            dados_curso=dados_curso,
            ies_emissora=dados_ies,
        )

        # --- C. CONSTRUÇÃO DO HISTÓRICO ESCOLAR ---
        filiacao_mock = Tfiliacao(
            genitor=[
                Tpessoa(nome="Nayara Pereira Barbosa", sexo="F"),
                Tpessoa(nome="Rodrigo Lopes de Lara", sexo="M"),
            ]
        )

        carga_integralizada = TcargaHoraria(hora_aula=3600)
        carga_curso = TcargaHoraria(hora_aula=3600)

        ingresso = ThistoricoEscolar.IngressoCurso(
            data=XmlDate.from_string("2023-02-01"),
            forma_acesso=TformaAcessoCurso.VESTIBULAR,
        )

        info_enade = TinformacoesEnade(
            condicao="Ingressante",
            edicao=2023,
        )

        enade_mock = Tenade(habilitado=[info_enade])

        situacao_formado = TsituacaoFormado(
            data_conclusao_curso=XmlDate.from_string("2026-08-30"),
            data_colacao_grau=XmlDate.from_string("2026-09-15"),
            data_expedicao_diploma=XmlDate.from_string("2026-10-01"),
        )
        situacao_discente = TsituacaoAtualDiscente(formado=situacao_formado)

        docente = Tdocente(
            nome="Professor Exemplo",
            cpf="00011122233",
            titulacao="Doutorado",
        )
        docentes_list = Tdocentes(docente=[docente])

        disciplina_mock = TentradaHistoricoDisciplina(
            codigo_disciplina="COM101",
            nome_disciplina="Algoritmos e Estruturas de Dados",
            periodo_letivo="2023.1",
            carga_horaria=[],
            docentes=docentes_list,
        )

        elementos_historico = TelementosHistorico(disciplina=[disciplina_mock])

        historico_escolar_obj = ThistoricoEscolar(
            codigo_curriculo="CURR-2023-01",
            elementos_historico=elementos_historico,
            data_emissao_historico=XmlDate.from_string("2026-10-05"),
            hora_emissao_historico=XmlTime.from_string("14:30:00"),
            situacao_atual_discente=situacao_discente,
            enade=enade_mock,
            carga_horaria_curso_integralizada=carga_integralizada,
            carga_horaria_curso=carga_curso,
            ingresso_curso=ingresso,
        )

        # --- D. DADOS PRIVADOS E DOCUMENTAÇÃO COMPROBATÓRIA ---
        dados_privados = TdadosPrivadosDiplomado(
            filiacao=filiacao_mock,
            historico_escolar=historico_escolar_obj,
        )

        documentacao = TdocumentacaoComprobatoria()

        # --- E. ÁRBORE DE REQUISIÇÃO ---
        registro = TregistroReq(
            versao="1.05",
            id="ReqDip12345678901234567890123456789012345678901234",
            dados_diploma=dados_diploma,
            dados_privados_diplomado=dados_privados,
            documentacao_comprobatoria=documentacao,
        )

        # --- F. MOCK DA ASSINATURA DIGITAL (XMLDSig) ---
        signed_info_mock = SignedInfo(
            canonicalization_method=CanonicalizationMethod(
                algorithm="http://www.w3.org/2001/10/xml-exc-c14n#"
            ),
            signature_method=SignatureMethod(
                algorithm="http://www.w3.org/2001/04/xmldsig-more#rsa-sha256"
            ),
            reference=[
                Reference(
                    digest_method=DigestMethod(
                        algorithm="http://www.w3.org/2001/04/xmlenc#sha256"
                    ),
                    digest_value=b"hash_simulado_bytes",
                    uri="#ReqDip12345678901234567890123456789012345678901234",
                )
            ],
        )

        signature_value_mock = SignatureValue(value=b"assinatura_simulada_bytes")

        assinatura_mock = Signature(
            signed_info=signed_info_mock,
            signature_value=signature_value_mock,
        )

        # --- G. RAIZ DO DOCUMENTO XML ---
        mock_data = DocumentacaoAcademicaRegistro(
            registro_req=registro,
            signature=assinatura_mock,
        )

    except TypeError as e:
        print(f"\n⚠️ Faltaram campos obrigatórios na criação de uma das classes!")
        print(f"Erro exato apontado pelo Python:\n -> {e}\n")
        return None

    # --- H. SERIALIZAÇÃO DO XML ---
    ns_map = {None: "http://portal.mec.gov.br/diplomadigital/arquivos-em-xsd"}
    config = SerializerConfig(pretty_print=True)
    serializer = XmlSerializer(config=config)

    xml_string = serializer.render(mock_data, ns_map=ns_map)

    caminho_arquivo = "diploma_teste.xml"
    with open(caminho_arquivo, "w", encoding="utf-8") as f:
        f.write(xml_string)

    print(f"✅ XML estrutural gerado com sucesso em '{caminho_arquivo}'!\n")
    return caminho_arquivo


def validar_xml_contra_xsd(xml_path, xsd_path):
    if not xml_path:
        return

    print(f"Iniciando validação rigorosa de {xml_path} contra o XSD...")

    try:
        xsd_doc = etree.parse(xsd_path)
        schema = etree.XMLSchema(xsd_doc)
        xml_doc = etree.parse(xml_path)

        schema.assertValid(xml_doc)
        print("✅ SUCESSO: O XML gerado é totalmente válido perante o MEC!")

    except etree.DocumentInvalid:
        print("❌ ERRO DE VALIDAÇÃO: O XML não atende às regras do XSD.")
        print("Detalhes do erro encontrados pelo lxml:")
        for error in schema.error_log:
            print(f" - Linha {error.line}: {error.message}")
    except Exception as e:
        print(f"⚠️ Erro inesperado ao ler os arquivos: {e}")


if __name__ == "__main__":
    caminho_xsd = "schemas/DocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd"

    xml_gerado = gerar_xml_mock()
    validar_xml_contra_xsd(xml_gerado, caminho_xsd)