from __future__ import annotations

from dataclasses import dataclass

from ..business_rules import exactly_one
from ..errors import BusinessRuleError


@dataclass(frozen=True)
class SecondViaIds:
    nonce: str
    request_id: str
    diploma_id: str


def build_second_via_request(
    *,
    registro_cls: type,
    root_cls: type,
    dados_diploma: object | None,
    dados_diploma_nsf: object | None,
    dados_privados_diplomado: object,
    versao: object,
    request_id: str,
    termo_responsabilidade_emissora: object | None = None,
    documentacao_comprobatoria: object | None = None,
    ambiente: object | None = None,
    signature: object,
) -> object:
    """
    Constrói o ramo RegistroSegundaViaReq.

    A função recebe classes geradas pelo xsdata para não acoplar regras de negócio
    aos detalhes de importação do código autogerado.
    """
    exactly_one(
        dados_diploma,
        dados_diploma_nsf,
        labels=("DadosDiploma", "DadosDiplomaNSF"),
    )

    if not request_id.startswith("ReqDip") or len(request_id) != 50:
        raise BusinessRuleError("request_id deve seguir ReqDip + 44 dígitos.")

    kwargs = {
        "dados_diploma": dados_diploma,
        "dados_diploma_nsf": dados_diploma_nsf,
        "dados_privados_diplomado": dados_privados_diplomado,
        "termo_responsabilidade_emissora": termo_responsabilidade_emissora,
        "documentacao_comprobatoria": documentacao_comprobatoria,
        "versao": versao,
        "id": request_id,
        "ambiente": ambiente,
    }
    registro = registro_cls(**kwargs)
    return root_cls(registro_segunda_via_req=registro, signature=signature)
