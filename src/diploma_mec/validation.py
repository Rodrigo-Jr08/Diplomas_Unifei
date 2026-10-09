from __future__ import annotations

from functools import lru_cache
from pathlib import Path

from lxml import etree

from .errors import SchemaValidationError


def _parser() -> etree.XMLParser:
    """
    Define e configura o parser XML padrão.
    
    Retorna um parser configurado para garantir maior segurança na leitura,
    desabilitando o acesso à rede e a resolução de entidades externas para 
    prevenir ataques do tipo XXE (XML External Entity).
    
    Returns:
        etree.XMLParser: A instância do parser configurado e seguro.
    """
    return etree.XMLParser(
        no_network=True,
        resolve_entities=False,
        load_dtd=False,
        remove_blank_text=False,
        huge_tree=False,
    )


@lru_cache(maxsize=32)
def _load_schema(xsd_path: str) -> etree.XMLSchema:
    """
    Carrega, compila e armazena em cache um esquema XSD.
    
    Lê o arquivo XSD a partir do caminho fornecido e o converte no formato 
    esperado pelo validador do lxml (etree.XMLSchema). O uso de cache 
    evita que o mesmo arquivo precise ser lido e compilado repetidas vezes.
    
    Args:
        xsd_path (str): O caminho absoluto ou relativo para o arquivo XSD.
        
    Returns:
        etree.XMLSchema: O esquema compilado e pronto para uso em validações.
        
    Raises:
        SchemaValidationError: Se o arquivo XSD não for encontrado no sistema ou 
                             se houver um erro de sintaxe/leitura durante a compilação.
    """
    path = Path(xsd_path).resolve()

    if not path.exists():
        raise SchemaValidationError(f"XSD não encontrado: {path}")
    try:
        doc = etree.parse(str(path), _parser())
        return etree.XMLSchema(doc)
    except (OSError, etree.XMLSchemaParseError, etree.XMLSyntaxError) as exc:
        raise SchemaValidationError(f"Não foi possível carregar/compilar o XSD {path}: {exc}") from exc


def validate_xsd(xml_path: str | Path, xsd_path: str | Path) -> None:
    """
    Valida um arquivo físico de XML contra um arquivo de regras XSD.
    
    Lê diretamente do disco o arquivo XML e verifica se a sua estrutura 
    e dados cumprem rigorosamente as exigências do esquema fornecido.
    
    Args:
        xml_path (str | Path): O caminho para o arquivo XML a ser validado.
        xsd_path (str | Path): O caminho para o arquivo XSD contendo as regras.
        
    Raises:
        SchemaValidationError: Se o XML for ilegível, malformado ou se violar 
                             qualquer regra estabelecida no arquivo XSD.
    """
    xml_path = Path(xml_path).resolve()
    schema = _load_schema(str(Path(xsd_path).resolve()))
    try:
        document = etree.parse(str(xml_path), _parser())
        schema.assertValid(document)
    except (OSError, etree.XMLSyntaxError) as exc:
        raise SchemaValidationError(f"XML inválido ou ilegível: {xml_path}: {exc}") from exc
    except etree.DocumentInvalid as exc:
        details = "\n".join(
            f"linha {e.line}: {e.message}" for e in schema.error_log
        )
        raise SchemaValidationError(
            f"XML não atende ao XSD {xsd_path}:\n{details}"
        ) from exc


def validate_xsd_text(xml_bytes: bytes, xsd_path: str | Path) -> None:
    """
    Valida o conteúdo de um XML em memória (bytes) contra um esquema XSD.
    
    Diferente de validate_xsd, esta função não lê arquivos do disco. 
    Ideal para validar payloads XML recebidos através de requisições de API 
    ou processos em memória.
    
    Args:
        xml_bytes (bytes): O conteúdo do documento XML formatado em bytes.
        xsd_path (str | Path): O caminho para o arquivo de esquema XSD.
        
    Raises:
        SchemaValidationError: Se o XML estiver malformado ou não cumprir 
                             as exigências estruturais do esquema.
    """
    schema = _load_schema(str(Path(xsd_path).resolve()))
    try:
        root = etree.fromstring(xml_bytes, parser=_parser())
        schema.assertValid(root)
    except etree.DocumentInvalid as exc:
        details = "\n".join(
            f"linha {e.line}: {e.message}" for e in schema.error_log
        )
        raise SchemaValidationError(
            f"XML não atende ao XSD {xsd_path}:\n{details}"
        ) from exc
    except etree.XMLSyntaxError as exc:
        raise SchemaValidationError(f"XML malformado: {exc}") from exc


def is_xsd_valid(xml_path: str | Path, xsd_path: str | Path) -> bool:
    """
    Verifica silenciosamente se um documento XML obedece a um esquema XSD.
    
    Esta função encapsula validate_xsd para não interromper a execução do 
    código com exceções em caso de falha, devolvendo apenas um booleano de controlo.
    
    Args:
        xml_path (str | Path): O caminho para o arquivo XML.
        xsd_path (str | Path): O caminho para o arquivo XSD.
        
    Returns:
        bool: True se o documento passar na validação perfeitamente. False se 
              houver qualquer erro de validação ou leitura.
    """
    try:
        validate_xsd(xml_path, xsd_path)
        return True
    except SchemaValidationError:
        return False