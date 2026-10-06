class DiplomaMecError(Exception):
    """Erro base da aplicação."""


class ConfigurationError(DiplomaMecError):
    """Configuração/ambiente inválido."""


class BusinessRuleError(DiplomaMecError):
    """Regra de negócio do Diploma Digital violada."""


class SchemaValidationError(DiplomaMecError):
    """XML ou XSD inválido perante o schema."""


class SignatureError(DiplomaMecError):
    """Assinatura ausente, incompatível ou inválida."""
