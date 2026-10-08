from __future__ import annotations

from decimal import Decimal
from pathlib import Path

from xsdata.models.datatype import XmlDate

from generated import *

from diploma_mec.builders.second_via import build_second_via_request
from diploma_mec.constants import DOCUMENTACAO_REGISTRO_XSD
from diploma_mec.ids import DiplomaIds
from diploma_mec.services import generate_and_validate
from diploma_mec.signing import build_development_signature


def ato_exemplo() -> TatoRegulatorioComOuSemEmec:
    return TatoRegulatorioComOuSemEmec(
        tipo=__import__("generated.tipos_basicos_v1_05", fromlist=["TtipoAtoComAtoProprio"]).TtipoAtoComAtoProprio.PORTARIA,
        numero="123",
        data=XmlDate.from_string("2020-01-01"),
    )


def main() -> None:
    ids = DiplomaIds.new()
    endereco = Tendereco(
        logradouro="Rua Exemplo", numero="100", bairro="Centro",
        codigo_municipio="3550308", nome_municipio="São Paulo", uf=Tuf.SP, cep="01000000"
    )
    naturalidade = __import__("generated.tipos_basicos_v1_05", fromlist=["Tnaturalidade"]).Tnaturalidade(
        codigo_municipio="3550308", nome_municipio="São Paulo", uf=Tuf.SP
    )
    aluno = TdadosDiplomado(
        id="RA-DEMO-001", nome="Aluno de Demonstração", sexo=Tsexo.M,
        nacionalidade="Brasileira", naturalidade=naturalidade, cpf="12345678901",
        rg=Trg(numero="123456789", orgao_expedidor="SSP", uf=Tuf.SP),
        data_nascimento=XmlDate.from_string("2000-01-01"),
    )
    ato = ato_exemplo()
    curso = TdadosCurso(
        nome_curso="Engenharia de Computação", codigo_curso_emec="123456",
        modalidade=TmodalidadeCurso.PRESENCIAL,
        titulo_conferido=TtituloConferido(titulo=Ttitulo.BACHAREL),
        grau_conferido=TgrauConferido.BACHARELADO, endereco_curso=endereco,
        autorizacao=ato, reconhecimento=ato,
    )
    ies = TdadosIesEmissora(
        nome="IES de Demonstração", codigo_mec="584", cnpj="21040003000106",
        endereco=endereco, credenciamento=ato,
    )
    assinatura_diploma = build_development_signature(ids.diploma_id)
    diploma = TdadosDiploma(
        diplomado=aluno, data_conclusao=XmlDate.from_string("2025-01-30"),
        dados_curso=curso, ies_emissora=ies, signature=[assinatura_diploma],
        id=ids.diploma_id,
    )

    historico = ThistoricoEscolarSegundaVia(
        codigo_curriculo="CUR-2020",
        elementos_historico=TelementosHistoricoSegundaViaNatoFisico(
            disciplina=[
                TentradaHistoricoDisciplinaSegundaViaNatoFisica(
                    codigo_disciplina="COMP101", 
                    nome_disciplina="Algoritmos",
                    periodo_letivo="2021.1",
                    carga_horaria=[TcargaHorariaComEtiqueta(hora_aula="60")],
                    nota=Decimal("8.50"),
                    aprovado=TdisciplinaAprovada(forma_integralizacao=TformaIntegralizacao.CURSADO),
                )
            ]
        ),
        data_emissao_historico=XmlDate.from_string("2026-10-05"),
        hora_emissao_historico="14:00:00",
        situacao_atual_discente=TsituacaoAtualDiscente(
            formado=TsituacaoFormado(
                data_conclusao_curso=XmlDate.from_string("2025-01-30"),
                data_colacao_grau=XmlDate.from_string("2025-02-10"),
                data_expedicao_diploma=XmlDate.from_string("2025-02-20"),
            )
        ),
        carga_horaria_curso_integralizada=TcargaHoraria(hora_aula="3600"),
        carga_horaria_curso=TcargaHoraria(hora_aula="3600"),
    )
    filiacao=Tfiliacao(genitor=[Tpessoa(nome="Genitor Demo 1", sexo=Tsexo.M), Tpessoa(nome="Genitor Demo 2", sexo=Tsexo.F)])
    privados=TdadosPrivadosDiplomadoSegundaVia(filiacao=filiacao, historico_escolar=historico)

    root=build_second_via_request(
        registro_cls=TregistroSegundaViaReq, root_cls=DocumentacaoAcademicaRegistro,
        dados_diploma=diploma, dados_diploma_nsf=None, dados_privados_diplomado=privados,
        versao=Tversao.VALUE_1_05, request_id=ids.request_id, ambiente=Tamb.HOMOLOGA_O,
        signature=build_development_signature(ids.request_id),
    )
    out=Path("output/segunda_via_demo.xml")
    artifact=generate_and_validate(root,xsd_path=DOCUMENTACAO_REGISTRO_XSD,output_path=out)
    artifact=generate_and_validate(root,xsd_path=DOCUMENTACAO_REGISTRO_XSD,output_path=out)
    print(f"XML válido perante o XSD: {artifact.path}")
    print(f"SHA-256: {artifact.sha256}")
    print("ATENÇÃO: assinatura e ambiente são apenas de desenvolvimento.")


if __name__ == "__main__":
    main()
