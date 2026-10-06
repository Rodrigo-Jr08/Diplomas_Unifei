# Guia por módulo

| Arquivo | Responsabilidade |
|---|---|
| `constants.py` | namespaces, versão v1.05 e caminhos dos XSD |
| `ids.py` | NONCE de 44 dígitos, VDip/Dip/RDip/ReqDip e código de validação |
| `business_rules.py` | regras que o XSD não representa sozinho, como `choice` e vínculo do NONCE |
| `validation.py` | compilação/cache do XSD e validação do XML |
| `serialization.py` | serialização xsdata sem pretty print e normalização de namespace |
| `builders/second_via.py` | construção explícita do ramo de segunda via |
| `services.py` | orquestra geração, validação, gravação e SHA-256 |
| `signing.py` | contrato de assinatura e ponto de integração com infraestrutura real |
| `url.py` | regras básicas da URL pública HTTPS |
| `scripts/audit_xsds.py` | auditoria do pacote de XSD e compilação dos schemas locais |
| `sql/001_initial_schema.sql` | ponto de partida para a persistência PostgreSQL |

## Ordem de desenvolvimento recomendada

1. Fechar o pacote oficial XSD v1.05.
2. Gerar novamente `generated/` a partir desse pacote.
3. Implementar o mapper domínio -> modelo XSD.
4. Fechar a geração/validação estrutural de segunda via.
5. Implementar validações de negócio.
6. Integrar assinatura institucional/XAdES/PBAD.
7. Implementar armazenamento imutável, URL pública e status.
8. Só depois ligar o fluxo completo ao PostgreSQL.
