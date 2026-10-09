from __future__ import annotations

from dataclasses import dataclass

from ..business_rules import exactly_one
from ..errors import BusinessRuleError


@dataclass(frozen=True)
class SecondViaIds:
    """
    Armazena os identificadores únicos gerados para a emissão de uma segunda via.

    Attributes:
        nonce (str): O código numérico aleatório de segurança.
        request_id (str): O identificador único da requisição.
        diploma_id (str): O identificador único do diploma correspondente.
    """
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
    Constrói e valida a estrutura raiz para a requisição de uma Segunda Via do diploma.

    A função recebe as referências das classes geradas pelo xsdata dinamicamente (injeção 
    de dependência) para evitar o acoplamento direto das regras de negócio com os detalhes 
    de importação do código autogerado. Além da montagem, aplica validações primárias 
    exigidas pelo padrão do MEC.

    Args:
        registro_cls (type): A classe de modelo para `RegistroSegundaViaReq`.
        root_cls (type): A classe de modelo raiz, geralmente `DocumentacaoAcademicaRegistro`.
        dados_diploma (object | None): O bloco de dados do diploma (obrigatório se não houver NSF).
        dados_diploma_nsf (object | None): O bloco de dados do diploma sem formatação (obrigatório se não houver dados normais).
        dados_privados_diplomado (object): O histórico e dados privados do aluno.
        versao (object): A versão do esquema XSD utilizado (ex: "1.05").
        request_id (str): O identificador da requisição. Deve iniciar com 'ReqDip' e ter exatamente 50 caracteres.
        termo_responsabilidade_emissora (object | None, opcional): Declaração de responsabilidade da instituição.
        documentacao_comprobatoria (object | None, opcional): Evidências ou documentos de suporte para a segunda via.
        ambiente (object | None, opcional): Define o ambiente de emissão (ex: Produção, Homologação).
        signature (object): O nó da assinatura digital XML.

    Returns:
        object: A instância instanciada da `root_cls`, contendo o registro completo e a assinatura, pronta para serialização.

    Raises:
        BusinessRuleError: Se o `request_id` for inválido (tamanho errado ou prefixo ausente) 
                           ou se violar a exclusividade entre `dados_diploma` e `dados_diploma_nsf` 
                           (não podem ser ambos nulos nem ambos preenchidos).
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