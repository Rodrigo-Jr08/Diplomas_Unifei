from __future__ import annotations

from urllib.parse import urljoin

from .errors import ConfigurationError


def build_unique_diploma_url(institutional_base_url: str, validation_code: str) -> str:
    """
    Constrói a URL única e pública para validação do diploma digital.
    
    Junta a URL base da instituição com o código de validação, garantindo 
    a formatação correta das barras.
    
    Args:
        institutional_base_url (str): O endereço base do repositório da IES.
        validation_code (str): O código de segurança único do diploma.
        
    Returns:
        str: A URL final completa e validada.
        
    Raises:
        ConfigurationError: Se a URL base não utilizar HTTPS ou se a URL final exceder 255 caracteres.
    """
    
    base = institutional_base_url.rstrip("/") + "/"
    if not base.lower().startswith("https://"):
        raise ConfigurationError("A URL pública do diploma deve usar HTTPS.")
    url = urljoin(base, validation_code)
    if len(url) > 255:
        raise ConfigurationError("A URL única do diploma deve ter no máximo 255 caracteres.")
    return url
