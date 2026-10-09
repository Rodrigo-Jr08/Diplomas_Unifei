from __future__ import annotations

from pathlib import Path

from lxml import etree

from .constants import DS_NAMESPACE, MEC_NAMESPACE


def _clone_without_mec_prefix(node: etree._Element, is_root: bool = False) -> etree._Element:
    """
    Clona recursivamente um nó XML reestruturando os prefixos de namespace.
    
    Esta função interna percorre a árvore XML e remove os prefixos explícitos 
    relacionados ao MEC, tornando-o o namespace padrão na raiz. Também isola 
    a declaração do namespace de Assinatura Digital (DS) apenas na tag <Signature>.
    
    Args:
        node (etree._Element): O nó XML do lxml a ser processado.
        is_root (bool, opcional): Indica se o nó atual é a raiz do documento. 
                                  O padrão é False.
        
    Returns:
        etree._Element: Um novo nó XML clonado com os namespaces ajustados.
    """
    q = etree.QName(node)
    if q.namespace in (MEC_NAMESPACE, DS_NAMESPACE):
        tag = f"{{{q.namespace}}}{q.localname}"
    else:
        tag = node.tag

    if q.namespace == DS_NAMESPACE and q.localname == "Signature":
        nsmap = {None: DS_NAMESPACE}
    elif is_root:
        nsmap = {None: MEC_NAMESPACE}
    else:
        nsmap = None

    out = etree.Element(tag, nsmap=nsmap)
    for key, value in node.attrib.items():
        out.set(key, value)
    out.text = node.text
    out.tail = node.tail
    for child in node:
        out.append(_clone_without_mec_prefix(child))
    return out


def _normalize_namespaces(xml_bytes: bytes) -> bytes:
    """
    Normaliza a estrutura de namespaces de um documento XML em formato de bytes.
    
    Lê o XML bruto, aplica a transformação para definir o namespace MEC como 
    padrão global e declara o namespace DS (Digital Signature) localmente na 
    própria tag Signature. Retorna os bytes do XML reconstruído e codificado.
    
    Args:
        xml_bytes (bytes): O conteúdo original do documento XML em bytes.
        
    Returns:
        bytes: O documento XML normalizado, contendo a declaração XML (UTF-8).
    """
    root = etree.fromstring(xml_bytes)
    normalized = _clone_without_mec_prefix(root, is_root=True)
    return etree.tostring(
        normalized,
        encoding="UTF-8",
        xml_declaration=True,
        pretty_print=False,
    )


def serialize_xsdata(model: object, pretty_print: bool | None = None) -> bytes:
    """
    Serializa um modelo de dados (dataclass) xsdata para um documento XML.
    
    Converte as estruturas de objeto geradas pelo xsdata de volta para bytes XML. 
    A função verifica dinamicamente se a biblioteca xsdata está instalada antes 
    de tentar a serialização e, no final, passa o resultado pelo processo de 
    normalização de namespaces.
    
    Args:
        model (object): A instância do modelo de dados do xsdata a serializar.
        pretty_print (bool | None, opcional): Define se o XML de saída deve ter 
                                              indentação e quebras de linha para 
                                              leitura humana. O padrão é False.
        
    Returns:
        bytes: O XML final serializado e normalizado em formato de bytes.
        
    Raises:
        RuntimeError: Se o pacote 'xsdata' não estiver instalado no ambiente.
    """
    try:
        from xsdata.formats.dataclass.serializers import XmlSerializer
        from xsdata.formats.dataclass.serializers.config import SerializerConfig
    except ImportError as exc:  # pragma: no cover - ambiente sem dependência opcional
        raise RuntimeError(
            "xsdata não está instalado. Execute `pip install -e .[dev]`."
        ) from exc

    serializer = XmlSerializer(config=SerializerConfig(pretty_print=pretty_print or False))
    xml = serializer.render(model, ns_map={None: MEC_NAMESPACE})
    return _normalize_namespaces(xml.encode("utf-8"))


def write_xml(xml_bytes: bytes, path: str | Path) -> Path:
    """
    Grava os bytes de um documento XML num ficheiro local físico.
    
    Garante que todos os diretórios parentes necessários (pastas) sejam criados 
    automaticamente caso não existam no sistema, antes de escrever os dados.
    
    Args:
        xml_bytes (bytes): O conteúdo do documento XML a ser guardado.
        path (str | Path): O caminho e nome do ficheiro de destino.
        
    Returns:
        Path: O objeto Path absoluto ou relativo que aponta para o ficheiro criado.
    """
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(xml_bytes)
    return path