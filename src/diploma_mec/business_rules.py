from __future__ import annotations

import re
from typing import Any

from .errors import BusinessRuleError
from .ids import DIPLOMA_ID_RE, REGISTRATION_ID_RE, REQUEST_ID_RE, VALIDATION_CODE_RE, VIRTUAL_ID_RE


def exactly_one(*values: Any, labels: tuple[str, ...] | None = None) -> int:
    """
    Verifica se exatamente um dos valores fornecidos está definido (não nulo).
    
    Útil para garantir regras de negócio estruturais (como escolhas mutuamente 
    exclusivas em nós XML). 
    
    Args:
        *values (Any): Conjunto de valores variáveis a serem verificados.
        labels (tuple[str, ...] | None, opcional): Nomes amigáveis dos campos para 
                                                   exibição na mensagem de erro. 
        
    Returns:
        int: O número de valores definidos (sempre retornará 1 em caso de sucesso).
        
    Raises:
        BusinessRuleError: Se nenhum valor for preenchido (0) ou se mais de um 
                           valor for fornecido simultaneamente (>1).
    """
    count = sum(v is not None for v in values)
    if count != 1:
        names = labels or tuple(f"opção {i+1}" for i in range(len(values)))
        raise BusinessRuleError(
            "Exatamente uma alternativa deve ser preenchida: " + ", ".join(names)
        )
    return count


def validate_id_family(*, virtual_id: str, diploma_id: str, registration_id: str, request_id: str) -> None:
    """
    Valida a consistência e formatação da família de identificadores do diploma.
    
    Garante que todos os IDs envolvidos na emissão obedeçam às expressões regulares 
    definidas pelo MEC e compartilha a mesma base criptográfica (NONCE).
    
    Args:
        virtual_id (str): O identificador visual do diploma (prefixo VDip).
        diploma_id (str): O identificador do diploma acadêmico (prefixo Dip).
        registration_id (str): O identificador do registro (prefixo RDip).
        request_id (str): O identificador da requisição (prefixo ReqDip).
        
    Raises:
        BusinessRuleError: Se qualquer identificador falhar na validação da máscara (RegEx) 
                           ou se os sufixos numéricos (NONCE) não forem idênticos entre si.
    """
    checks = {
        "VDip": (virtual_id, VIRTUAL_ID_RE),
        "Dip": (diploma_id, DIPLOMA_ID_RE),
        "RDip": (registration_id, REGISTRATION_ID_RE),
        "ReqDip": (request_id, REQUEST_ID_RE),
    }
    for label, (value, pattern) in checks.items():
        if not pattern.fullmatch(value):
            raise BusinessRuleError(f"Identificador {label} inválido: {value!r}")

    suffixes = [virtual_id[4:], diploma_id[3:], registration_id[4:], request_id[6:]]
    if len(set(suffixes)) != 1:
        raise BusinessRuleError("VDip, Dip, RDip e ReqDip devem compartilhar o mesmo NONCE.")


def validate_validation_code(code: str) -> None:
    """
    Valida a integridade estrutural do código de validação do diploma.
    
    Verifica se a string fornecida corresponde ao formato exigido (códigos e-MEC 
    separados por ponto seguido de um token hexadecimal).
    
    Args:
        code (str): O código de validação gerado.
        
    Raises:
        BusinessRuleError: Se o código não corresponder à expressão regular esperada.
    """
    if not VALIDATION_CODE_RE.fullmatch(code):
        raise BusinessRuleError(
            "Código de validação deve seguir e-MEC emissora.e-MEC registradora.hexadecimal."
        )


def validate_https_url(url: str) -> None: 
    """
    Valida os requisitos mínimos de segurança e tamanho para URLs públicas.
    
    Garante que os links gerados para acesso ao diploma não ultrapassam o 
    limite de armazenamento no banco/XSD e forçam o tráfego criptografado.
    
    Args:
        url (str): O endereço web a ser verificado.
        
    Raises:
        BusinessRuleError: Se a URL não utilizar o protocolo HTTPS ou se o 
                           comprimento total ultrapassar 255 caracteres.
    """
    if not url.startswith("https://"):
        raise BusinessRuleError("URL pública deve utilizar HTTPS.")
    if len(url) > 255:
        raise BusinessRuleError("URL pública deve ter no máximo 255 caracteres.")