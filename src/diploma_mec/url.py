from __future__ import annotations

from urllib.parse import urljoin

from .errors import ConfigurationError


def build_unique_diploma_url(institutional_base_url: str, validation_code: str) -> str:
    base = institutional_base_url.rstrip("/") + "/"
    if not base.lower().startswith("https://"):
        raise ConfigurationError("A URL pública do diploma deve usar HTTPS.")
    url = urljoin(base, validation_code)
    if len(url) > 255:
        raise ConfigurationError("A URL única do diploma deve ter no máximo 255 caracteres.")
    return url
