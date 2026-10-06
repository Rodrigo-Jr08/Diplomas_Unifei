# Fontes técnicas e normativas usadas

## MEC

- INSTRUÇÃO NORMATIVA Nº 5, DE 14 DE OUTUBRO DE 2022 — aprova a versão 1.05 dos Anexos I, II e III da IN/SESU nº 1/2020.
- Página oficial “Pacote XSD v1.05” do Ministério da Educação — distribuição oficial e relação dos XSD.
- Verificador oficial da Estrutura XML do Diploma Digital — verificação estrutural contra XSD 1.05 e versões anteriores.
- Portaria MEC nº 70, de 24 de janeiro de 2025 — altera a Portaria MEC nº 554/2019 e explicita XML, XAdES, ICP-Brasil, política de assinatura de longo prazo e URL única.
- Portaria MEC nº 929, de 30 de dezembro de 2025 — altera o cronograma de pós-graduação stricto sensu e Residência em Saúde para contar da atualização técnica específica dos anexos da IN/SESU nº 1/2020.

## ITI / ICP-Brasil

- DOC-ICP-15.03 — Requisitos das Políticas de Assinatura Digital na ICP-Brasil, incluindo políticas XAdES e AD-RA.
- Instruções Normativas ITI publicadas em 2025 que alteram versões das políticas de assinatura.

## Bibliotecas

- xsdata — geração de classes Python a partir de XSD e XML serialization/data binding.
- lxml — construção/manipulação de árvore XML e validação com XMLSchema.
- xmlschema — alternativa schema-driven para validação e encode/decode de dados XSD/XML.

## Regra para atualização normativa

A versão do XSD e a versão da norma técnica devem ser tratadas como dados versionados. Não substituir arquivos históricos por uma versão nova. Quando surgir uma nova versão oficial, criar um pacote versionado separado, regenerar os modelos e executar a suíte de regressão contra as versões anteriores.
