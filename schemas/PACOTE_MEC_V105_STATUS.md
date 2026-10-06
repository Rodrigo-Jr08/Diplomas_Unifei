# Status do pacote XSD v1.05

O projeto contém os **14 arquivos XSD do pacote v1.05 utilizado pelo projeto**, com os nomes de arquivo padronizados conforme os `schemaLocation` esperados entre os próprios schemas.

Os arquivos foram mantidos como arquivos de schema; esta etapa não altera regras XML/XSD. A alteração realizada no repositório é de organização/nomenclatura local para que as referências internas sejam resolvidas corretamente em ambientes que diferenciam maiúsculas e minúsculas.

## Verificações realizadas

- 14/14 arquivos XSD presentes;
- todas as referências relativas de `schemaLocation` resolvidas;
- todos os 14 XSDs compilados individualmente com `lxml.etree.XMLSchema`;
- modelos Python regenerados com `xsdata` a partir do conjunto completo de schemas;
- imports do conjunto regenerado verificados;
- suíte `pytest` aprovada;
- exemplo de segunda via gerado e validado contra o XSD de Documentação Acadêmica.

> A validação acima demonstra consistência técnica do pacote local. Ela não substitui testes de conformidade institucional, assinatura ICP-Brasil/XAdES ou validação no ambiente oficial do MEC.
