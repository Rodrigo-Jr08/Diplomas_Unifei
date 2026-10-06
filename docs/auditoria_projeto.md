# Auditoria do protótipo original

## Estado encontrado

O ZIP original contém `main.py`, seis XSD, código autogerado em `generated/`, um XML de teste e um `test_env.py`. Não havia suíte de testes efetiva, documentação operacional ou separação clara entre domínio, construção XML, validação e assinatura.

## Falhas técnicas importantes

### 1. Execução

O `main.py` depende de `xsdata`, mas essa dependência não estava declarada em um arquivo de projeto e não estava instalada no ambiente analisado. A execução falhava antes da geração do XML.

### 2. Validação

`validar_xml_contra_xsd()` usa `etree` sem importar `lxml.etree`. Além disso, o parser não era configurado com `no_network=True` e o erro era misturado ao fluxo de geração.

### 3. Tipagem

O protótipo passa strings em vários pontos onde os modelos gerados exigem enums ou estruturas complexas, por exemplo UF, modalidade, grau, título conferido, endereço e atos regulatórios. Isso derrota justamente uma das vantagens de usar classes geradas a partir de XSD.

### 4. Identificadores

Os IDs do exemplo não respeitam a família de identificadores prevista pela v1.05. O projeto novo centraliza o NONCE de 44 dígitos e deriva os identificadores a partir dele.

### 5. Choice

O XML legado tenta colocar `RegistroReq`, `RegistroReqNSF`, `RegistroSegundaViaReq` e `RegistroPorDecisaoJudicialReq` ao mesmo tempo. A raiz possui uma escolha e somente uma alternativa deve ser emitida.

### 6. Segunda via

A segunda via não deve ser tratada como “primeira via com alguns campos a menos”. A v1.05 define explicitamente `RegistroSegundaViaReq` para segunda via digital de diploma originalmente expedido em suporte físico e usa uma estrutura própria de histórico para esse cenário.

### 7. Serialização

O protótipo usa `pretty_print=True`. Para este perfil do documento, o processo novo serializa de forma compacta e UTF-8, evitando whitespace de formatação introduzido pelo gerador.

### 8. Assinatura

O protótipo chama bytes arbitrários de assinatura. Isso não produz assinatura criptográfica. O projeto novo deixa a assinatura atrás de `SignatureProvider` e proíbe que um mock seja confundido com produção.

### 9. Escopo do XSD local

O pacote local agora contém os 14 XSDs v1.05 utilizados pelo projeto. O auditor verifica a presença do conjunto completo, resolve as referências `schemaLocation` e compila todos os schemas.

### 10. Manutenção

O código gerado deve ser descartável/regenerável. Regras de negócio devem ficar fora de `generated/`, ou qualquer regeneração destruirá correções manuais.
