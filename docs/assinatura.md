# Assinatura digital

O projeto separa a assinatura do restante da geração porque o XSD não comprova autenticidade criptográfica.

O ponto de integração é `SignatureProvider`. Em produção, o provedor deve conectar o sistema ao mecanismo institucional de assinatura aprovado pela IES (por exemplo, um serviço/HSM ou outra infraestrutura que controle o certificado institucional) e produzir XAdES/PBAD conforme a política aplicável.

A assinatura fictícia foi propositalmente removida do fluxo principal. Um bloco `<Signature>` com bytes arbitrários pode satisfazer partes do XSD, mas não é uma assinatura criptograficamente válida.

A IN v1.05 também diferencia assinaturas internas e assinatura de arquivamento; portanto, a aplicação deve controlar a etapa processual da assinatura em vez de tratar todas como equivalentes.
