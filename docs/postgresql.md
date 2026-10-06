# Integração futura com PostgreSQL

A recomendação é não usar o XML como banco primário. Use PostgreSQL para dados normalizados e armazene o XML final assinado como artefato imutável em object storage (ou, quando necessário, em `bytea`).

## Entidades sugeridas

- `instituicoes`: nome, e-MEC, CNPJ, atos regulatórios.
- `cursos`: e-MEC, nome, modalidade, atos de autorização/reconhecimento, versão curricular.
- `alunos`: identificação acadêmica e dados necessários à emissão.
- `historicos`: versões do histórico e elementos acadêmicos.
- `diplomas`: NONCE, IDs VDip/Dip/RDip/ReqDip, código de validação, versão XSD, tipo de emissão, status, datas e referências aos artefatos.
- `assinaturas`: documento, papel do assinante, certificado, política, data/hora, estado de validação.
- `documentos_comprobatorios`: tipo, hash, tamanho, object-storage-key.
- `eventos_auditoria`: criação, validação, assinatura, publicação, anulação e reemissão.

## Regras de persistência

IDs como `ReqDip...`, `Dip...`, `RDip...` e `VDip...` devem ser únicos e auditáveis. O XML assinado deve ter hash SHA-256 persistido. O artefato assinado não deve ser alterado depois de publicado.

## Privacidade

A documentação acadêmica contém dados privados. Ela não deve ser tratada como o mesmo artefato público do diploma final. Controle de acesso, logs sem dados pessoais, criptografia em repouso e política de retenção devem ser considerados desde o começo.
