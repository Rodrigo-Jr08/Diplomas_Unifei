# Regras v1.05 relevantes para este projeto

Este projeto usa como referência principal a IN/SESU nº 1/2020 e a versão 1.05 aprovada pela IN/SESU nº 5/2022, em conjunto com as alterações posteriores aplicáveis.

## Segunda via

Para a v1.05, `RegistroSegundaViaReq` é o ramo específico para segunda via digital de diploma originalmente emitido em suporte físico. Ele usa `TDadosPrivadosDiplomadoSegundaVia`, que por sua vez referencia o histórico escolar próprio para segunda via.

## IDs

Os blocos usam um NONCE compartilhado de 44 dígitos com os prefixos `VDip`, `Dip`, `RDip` e `ReqDip`, cada qual para sua finalidade.

## Segurança

O código de validação é derivado dos e-MEC emissor/registrador e um componente hexadecimal. O QR Code não é armazenado como imagem no XML; ele aponta para a URL definida para o diploma.

## XML

O XML deve ser UTF-8, sem comentários, sem anotações XSD e sem whitespace de formatação entre tags. A declaração de namespace segue o padrão da IN.

## Assinatura

A estrutura XMLDSig é apenas uma parte do problema. A assinatura precisa atender ao PBAD/XAdES e à política correspondente ao estágio do processo, além de ser validada antes da próxima assinatura.

## Regra XSD x regra normativa

Quando houver divergência entre `minOccurs` no XSD e texto descritivo da instrução normativa, não se deve assumir automaticamente que o XSD sozinho resolve a questão. Registre a discrepância, escolha uma política institucional e valide também regras de negócio/procedimento.
