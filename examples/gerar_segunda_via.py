from __future__ import annotations

"""
Exemplo de montagem de RegistroSegundaViaReq.

Este arquivo demonstra a arquitetura, mas os dados institucionais devem ser
substituídos pelos dados oficiais e, principalmente, o fluxo de assinatura deve
ser conectado ao mecanismo institucional de assinatura.
"""

from datetime import date
from pathlib import Path

# Exemplo de importação das classes geradas pelo xsdata.
# Os nomes refletem os arquivos existentes no projeto.
from xsdata.models.datatype import XmlDate

from generated import *

from diploma_mec.ids import DiplomaIds
from diploma_mec.builders.second_via import build_second_via_request
from diploma_mec.constants import DOCUMENTACAO_REGISTRO_XSD
from diploma_mec.services import generate_and_validate
from diploma_mec.signing import build_development_signature


def build_from_db_data(dados_diploma, historico, filiacao):
    """
    Esta é a fronteira ideal para o futuro PostgreSQL:
    - dados_diploma vem do mapper Banco -> modelo XSD;
    - historico é a representação de histórico de segunda via;
    - filiacao são os dados privados do diplomado.
    """
    ids = DiplomaIds.new()
    privados = TdadosPrivadosDiplomadoSegundaVia(
        filiacao=filiacao,
        historico_escolar=historico,
    )
    root = build_second_via_request(
        registro_cls=TregistroSegundaViaReq,
        root_cls=DocumentacaoAcademicaRegistro,
        dados_diploma=dados_diploma,
        dados_diploma_nsf=None,
        dados_privados_diplomado=privados,
        versao=Tversao.VALUE_1_05,
        request_id=ids.request_id,
        signature=build_development_signature(ids.request_id),
    )
    return root, ids


if __name__ == "__main__":
    print("Preencha build_from_db_data() com objetos vindos do seu domínio/mapper.")
    print(f"XSD: {DOCUMENTACAO_REGISTRO_XSD}")
