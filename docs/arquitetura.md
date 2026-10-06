# Arquitetura proposta

## Objetivo

Separar o projeto em cinco responsabilidades:

1. **Domínio/entrada**: dados acadêmicos vindos de formulário, API ou PostgreSQL.
2. **Mapper v1.05**: transforma dados do domínio nos modelos gerados a partir dos XSD.
3. **Serialização**: converte o modelo em bytes XML compactos e padroniza namespaces.
4. **Validação**: valida o XML contra o XSD e executa regras de negócio adicionais.
5. **Assinatura/persistência**: aplica XAdES/PBAD por um adaptador institucional e guarda o artefato imutável, hash e metadados.

O fluxo recomendado é:

`PostgreSQL -> domínio -> mapper v1.05 -> modelo xsdata -> XML compacto -> XSD -> regras de negócio -> assinatura XAdES/PBAD -> validação final -> armazenamento -> URL/status`

## Por que não colocar tudo no `main.py`?

O `main.py` original misturava dados de teste, montagem de objetos, assinatura fictícia, serialização e validação. Isso dificulta testes, manutenção e troca de fonte de dados.

## O que é autogerado

`generated/` deve ser considerado código derivado. Quando o XSD mudar, regenere. Não coloque regras de negócio dentro dos arquivos autogerados.

## XSD não é um template visual

O XSD define contrato estrutural: elementos, atributos, tipos, ordem, cardinalidade, choices, enums, padrões e namespaces. O XML é a instância concreta que deve cumprir esse contrato.
