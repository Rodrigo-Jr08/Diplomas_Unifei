# 🎓 Projeto Diploma Digital MEC

> Base Python para **geração, serialização e validação de XMLs** do ecossistema Diploma Digital do MEC, com schemas XSD **v1.05**.

---

## 📌 1. Visão geral

Este projeto implementa uma base Python para **geração, serialização e validação de XMLs do ecossistema Diploma Digital do Ministério da Educação (MEC)**, utilizando como referência o pacote de schemas XSD da **versão 1.05**.

O foco funcional atual é a montagem de uma **Documentação Acadêmica para Registro** contendo o ramo `RegistroSegundaViaReq`, destinado ao cenário de segunda via digital de diploma originalmente emitido em suporte físico.

O projeto foi estruturado para separar:

- os schemas oficiais XSD;
- os modelos Python gerados a partir desses schemas;
- as regras de negócio;
- a construção dos documentos;
- a serialização XML;
- a validação estrutural;
- a assinatura;
- os serviços de geração;
- os testes;
- e a futura integração com dados acadêmicos reais.

### Escopo atual

O exemplo executável gera:

```text
output/segunda_via_demo.xml
```

O arquivo é construído com dados fictícios, serializado em XML e validado contra o XSD da Documentação Acadêmica.

> ⚠️ A assinatura utilizada pelo exemplo é **somente estrutural e de desenvolvimento**. Ela não é uma assinatura criptográfica institucional e não deve ser utilizada para emissão produtiva.

---

## 🏗️ 2. Arquitetura do projeto

O fluxo atual é:

```text
schemas/
    │
    ▼
XSD MEC v1.05
    │
    ▼
xsdata
    │
    ▼
generated/
    │
    ▼
builders + business_rules
    │
    ▼
modelo Python
    │
    ▼
serialization.py
    │
    ▼
XML em bytes
    │
    ▼
validation.py
    │
    ▼
XML validado pelo XSD
    │
    ▼
services.py
    │
    ├── grava arquivo XML
    │
    └── calcula SHA-256
```

A arquitetura planejada para integração institucional é:

```text
PostgreSQL da universidade
        │
        ▼
Repository
        │
        ▼
Modelo de domínio
        │
        ▼
Mapper
        │
        ▼
Modelos xsdata / builders
        │
        ▼
XML MEC
        │
        ▼
Validação XSD + regras de negócio
        │
        ▼
Assinatura institucional XAdES/PBAD
        │
        ▼
Validação final
        │
        ▼
Armazenamento e auditoria
```

O projeto não depende de um novo banco institucional para funcionar. A integração com o PostgreSQL real é uma etapa posterior.

---

## 📁 3. Estrutura de diretórios

```text
projeto_diploma_mec_profissional/
│
├── pyproject.toml                  # Dependências do projeto
├── requirements.txt
├── README.md
├── .gitignore
│
├── schemas/                        # 14 arquivos XSD do pacote MEC v1.05
│   ├── *.xsd
│   ├── manifest_v1.05.json
│   └── PACOTE_MEC_V105_STATUS.md
│
├── generated/                      # Modelos Python gerados pelo xsdata (código derivado)
│   └── *.py
│
├── src/
│   └── diploma_mec/
│       ├── __init__.py             # Define o pacote e sua versão
│       ├── constants.py            # Namespaces, versão 1.05, caminhos e XSDs
│       ├── ids.py                  # NONCE e identificadores (VDip, Dip, RDip, ReqDip)
│       ├── business_rules.py       # Regras que não dependem só do XSD
│       ├── errors.py               # Exceções específicas da aplicação
│       ├── url.py                  # URL pública única do diploma
│       ├── serialization.py        # Objetos xsdata para XML compacto
│       ├── validation.py           # Validação XML/XSD
│       ├── services.py             # Orquestração: gerar, validar, gravar, SHA-256
│       ├── signing.py              # Fronteira arquitetural da assinatura
│       └── builders/
│           ├── __init__.py
│           └── second_via.py       # Builder de RegistroSegundaViaReq
│
├── examples/
│   ├── README.md
│   ├── gerar_segunda_via.py        # Estrutura para futura integração com dados reais
│   └── gerar_segunda_via_demo.py   # Exemplo executável principal
│
├── tests/
│   ├── conftest.py                 # Configuração de apoio aos testes
│   ├── test_business_rules.py      # exactly_one()
│   ├── test_ids.py                 # NONCE, identificadores e código de validação
│   ├── test_invalid_legacy_xml.py  # Teste negativo com XML legado
│   ├── test_schema_compile.py      # Compilação dos XSDs locais
│   └── test_second_via_demo.py     # Geração do exemplo de segunda via
│
├── scripts/
│   └── audit_xsds.py               # Auditoria do pacote local de schemas
│
├── docs/                           # Documentação complementar
│   ├── alternativas_xml.md
│   ├── arquitetura.md
│   ├── assinatura.md
│   ├── auditoria_projeto.md
│   ├── fontes_e_normas.md
│   ├── guia_por_modulo.md
│   ├── postgresql.md
│   └── regras_mec_v105.md
│
├── legacy/                         # Protótipo anterior (fora do fluxo principal)
│   ├── main_original.py
│   └── diploma_teste.xml
│
├── sql/                            # Referência de modelagem da futura persistência
│   └── 001_initial_schema.sql
│
└── output/                         # Criada automaticamente ao executar o exemplo
    └── segunda_via_demo.xml
```

> 💡 A pasta `output/` é criada automaticamente quando o exemplo é executado.

---

## 🛠️ 4. Requisitos

### Python

O projeto requer:

```text
Python >= 3.11
```

### Dependências principais

As dependências são declaradas no `pyproject.toml`:

```text
lxml
xsdata
pytest
xmlschema
```

#### Função de cada biblioteca

| Biblioteca | Função |
| --- | --- |
| `lxml` | Manipulação de XML e validação com XMLSchema/XSD |
| `xsdata` | Geração de classes Python a partir dos XSDs e serialização dos objetos |
| `pytest` | Execução da suíte de testes |
| `xmlschema` | Ferramentas auxiliares para trabalho com schemas XSD |

---

## ⚙️ 5. Instalação e configuração

Abra o terminal na raiz do projeto.

### 5.1 Criar o ambiente virtual

```powershell
python -m venv .venv
```

### 5.2 Ativar no PowerShell

```powershell
.venv\Scripts\Activate.ps1
```

O terminal deverá apresentar algo semelhante a:

```text
(.venv) PS C:\...\projeto_diploma_mec_profissional>
```

### 5.3 Atualizar o pip

```powershell
python -m pip install --upgrade pip
```

### 5.4 Instalar o projeto e dependências de desenvolvimento

```powershell
pip install -e ".[dev]"
```

> 💡 A opção `-e` instala o projeto em modo editável, permitindo trabalhar diretamente sobre o código da pasta local.

---

## 🧪 6. Executar os testes

Na raiz do projeto:

```powershell
pytest
```

A suíte cobre:

- regras de negócio básicas;
- geração e coerência dos identificadores;
- código de validação;
- rejeição de XML legado inválido;
- compilação dos XSDs locais;
- geração do exemplo de segunda via.

Uma execução saudável apresenta todos os testes aprovados, por exemplo:

```text
9 passed
```

---

## 🚀 7. Gerar o XML de exemplo

Execute:

```powershell
python -m examples.gerar_segunda_via_demo
```

O programa deverá apresentar algo semelhante a:

```text
XML válido perante o XSD: output\segunda_via_demo.xml
SHA-256: <hash>
ATENÇÃO: assinatura e ambiente são apenas de desenvolvimento.
```

O arquivo estará em:

```text
output/segunda_via_demo.xml
```

Para conferir pelo PowerShell:

```powershell
dir output
```

---

## 🔄 8. O que acontece durante a geração

O exemplo `gerar_segunda_via_demo.py` executa, em linhas gerais, estas etapas:

```text
DiplomaIds.new()
        │
        ▼
criação do NONCE e dos identificadores
        │
        ▼
montagem dos dados do diplomado
        │
        ▼
montagem do curso
        │
        ▼
montagem da IES emissora
        │
        ▼
montagem de DadosDiploma
        │
        ▼
montagem do histórico de segunda via
        │
        ▼
montagem dos dados privados do diplomado
        │
        ▼
build_second_via_request()
        │
        ▼
DocumentacaoAcademicaRegistro
        │
        ▼
serialize_xsdata()
        │
        ▼
XML
        │
        ▼
validate_xsd_text()
        │
        ▼
write_xml()
        │
        ▼
SHA-256
```

---

## 📜 9. XSDs do MEC v1.05

A pasta `schemas/` contém os 14 arquivos XSD utilizados pelo pacote v1.05 do projeto.

Entre eles estão os schemas principais:

| Arquivo | Função |
| --- | --- |
| `DiplomaDigital_v1.05.xsd` | Estrutura do XML do Diploma Digital |
| `DocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd` | Estrutura da Documentação Acadêmica para Emissão e Registro |
| `HistoricoEscolarDigital_v1.05.xsd` | Estrutura do Histórico Escolar Digital |
| `CurriculoEscolarDigital_v1.05.xsd` | Estrutura do Currículo Escolar Digital |
| `ListaDiplomasAnulados_v1.05.xsd` | Estrutura da lista de diplomas anulados |
| `ArquivoFiscalizacao_v1.05.xsd` | Estrutura do arquivo de fiscalização |

Também existem schemas auxiliares, como:

```text
tiposBasicos_v1.05.xsd
leiauteDiplomaDigital_v1.05.xsd
leiauteDocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd
leiauteHistoricoEscolar_v1.05.xsd
leiauteListaDiplomasAnulados_v1.05.xsd
leiauteArquivoFiscalizacao_v1.05.xsd
leiauteCurriculoEscolar_v1.05.xsd
xmldsig-core-schema_v1.1.xsd
```

Os XSDs são o contrato estrutural utilizado para produzir e validar o XML.

---

## 🧬 10. Diretório `generated/`

O diretório `generated/` contém código Python produzido a partir dos XSDs utilizando `xsdata`.

Exemplos:

```text
generated/
├── diploma_digital_v1_05.py
├── documentacao_academica_registro_diploma_digital_v1_05.py
├── leiaute_diploma_digital_v1_05.py
├── leiaute_documentacao_academica_registro_diploma_digital_v1_05.py
├── leiaute_historico_escolar_v1_05.py
├── tipos_basicos_v1_05.py
└── xmldsig_core_schema_v1_1.py
```

Esses arquivos representam em Python os tipos definidos nos XSDs.

Por exemplo, um tipo definido no XSD pode aparecer no Python como:

```python
@dataclass
class TdadosDiploma:
    ...
```

O objetivo é permitir que o programa construa objetos tipados que posteriormente serão convertidos em XML.

### Regra de manutenção

> ⚠️ Os arquivos de `generated/` devem ser tratados como **código derivado**.

Quando os XSDs mudarem:

```text
novo XSD
   ↓
xsdata
   ↓
novo generated/
```

> ⚠️ As regras de negócio não devem ser colocadas dentro desses arquivos.

---

## 🧩 11. Módulos da aplicação

### 11.1 `src/diploma_mec/__init__.py`

Define o pacote Python `diploma_mec` e sua versão:

```python
__version__ = "0.1.0"
```

É o ponto básico de inicialização do pacote.

### 11.2 `constants.py`

Centraliza constantes utilizadas pelo projeto.

Principais responsabilidades:

- namespace principal do MEC;
- namespace XMLDSig;
- versão `1.05`;
- caminho da raiz do projeto;
- caminho dos schemas;
- caminho dos modelos gerados;
- caminhos dos principais XSDs;
- relação dos 14 arquivos do pacote v1.05.

Exemplos:

```python
MEC_NAMESPACE
DS_NAMESPACE
MEC_XSD_VERSION
SCHEMAS_DIR
DOCUMENTACAO_REGISTRO_XSD
```

Isso evita espalhar caminhos e identificadores de versão pelo código.

### 11.3 `ids.py`

Responsável pelos identificadores relacionados ao Diploma Digital.

Principais elementos:

```text
NONCE
VDip
Dip
RDip
ReqDip
código de validação
```

O `NONCE` utilizado pelo projeto possui 44 dígitos numéricos.

A classe:

```python
DiplomaIds
```

concentra os identificadores derivados do mesmo NONCE.

Exemplo conceitual:

```text
NONCE
  │
  ├── VDip + NONCE
  ├── Dip + NONCE
  ├── RDip + NONCE
  └── ReqDip + NONCE
```

O módulo também contém validações por expressão regular.

### 11.4 `business_rules.py`

Contém regras que não devem ficar dependentes exclusivamente do XSD.

A função:

```python
exactly_one()
```

garante que exatamente uma alternativa seja preenchida.

Ela é utilizada para representar escolhas como:

```text
DadosDiploma
OU
DadosDiplomaNSF
```

Também existem funções para:

- validar a família de IDs;
- conferir se todos os IDs compartilham o mesmo NONCE;
- validar o formato do código de validação;
- validar URLs HTTPS.

### 11.5 `errors.py`

Centraliza as exceções específicas da aplicação.

Hierarquia principal:

```text
DiplomaMecError
├── ConfigurationError
├── BusinessRuleError
├── SchemaValidationError
└── SignatureError
```

Isso permite diferenciar:

- erro de configuração;
- erro de regra de negócio;
- erro de XSD/XML;
- erro relacionado à assinatura.

### 11.6 `url.py`

Responsável pela construção da URL pública única associada ao diploma.

A função principal é:

```python
build_unique_diploma_url()
```

Ela verifica:

- uso de HTTPS;
- construção da URL a partir da URL institucional;
- tamanho máximo da URL.

### 11.7 `serialization.py`

Transforma os objetos Python gerados pelo `xsdata` em XML.

A função:

```python
serialize_xsdata()
```

utiliza:

```text
xsdata
```

para realizar a serialização.

Depois, o módulo normaliza os namespaces para seguir o padrão utilizado pelo projeto.

A serialização é feita sem `pretty_print`, produzindo XML compacto.

Também existe:

```python
write_xml()
```

que grava os bytes no arquivo:

```python
path.write_bytes(xml_bytes)
```

### 11.8 `validation.py`

É responsável pela validação XML/XSD.

A função:

```python
load_schema()
```

carrega e compila o XSD utilizando:

```text
lxml.etree.XMLSchema
```

O schema é armazenado em cache para evitar recompilação desnecessária.

Existem três operações principais:

```python
validate_xsd()
validate_xsd_text()
is_xsd_valid()
```

Elas permitem:

- validar um arquivo XML;
- validar XML ainda em memória;
- obter `True` ou `False` para uma validação.

O parser utiliza configurações como:

```text
no_network=True
resolve_entities=False
load_dtd=False
```

para manter o processo de validação controlado.

### 11.9 `services.py`

É a camada de orquestração da geração do artefato.

A função principal é:

```python
generate_and_validate()
```

Ela executa:

```text
modelo Python
    ↓
serialize_xsdata()
    ↓
XML em bytes
    ↓
validate_xsd_text()
    ↓
write_xml()
    ↓
SHA-256
```

O resultado é representado pela classe:

```python
XmlArtifact
```

que contém:

- caminho do arquivo;
- SHA-256;
- tamanho;
- XSD utilizado.

### 11.10 `signing.py`

Define a fronteira arquitetural da assinatura.

O contrato:

```python
SignatureProvider
```

representa o mecanismo que futuramente poderá assinar o XML por uma infraestrutura institucional.

Também existe:

```python
ProductionSignatureProvider
```

como ponto de integração para o mecanismo real.

O projeto possui ainda:

```python
build_development_signature()
```

para gerar uma estrutura XMLDSig de desenvolvimento capaz de exercitar o fluxo estrutural.

> ⚠️ **Essa assinatura:**
>
> - não é criptograficamente válida;
> - não autentica a instituição;
> - não possui validade jurídica;
> - não deve ser utilizada em produção.

A implementação produtiva deverá integrar a infraestrutura institucional e atender aos requisitos aplicáveis de assinatura digital, XAdES/PBAD e certificados.

---

## 🏭 12. Builder de segunda via

Arquivo:

```text
src/diploma_mec/builders/second_via.py
```

O builder:

```python
build_second_via_request()
```

é responsável por montar o ramo:

```text
RegistroSegundaViaReq
```

Ele recebe os modelos gerados pelo `xsdata` e monta:

```text
DocumentacaoAcademicaRegistro
└── RegistroSegundaViaReq
    ├── DadosDiploma ou DadosDiplomaNSF
    ├── DadosPrivadosDiplomado
    ├── TermoResponsabilidadeEmissora
    ├── DocumentacaoComprobatoria
    ├── versão
    ├── ID
    └── ambiente
```

Os dois primeiros elementos alternativos são controlados pela regra:

```python
exactly_one()
```

A classe:

```python
SecondViaIds
```

representa os identificadores relevantes ao fluxo de segunda via.

---

## 💡 13. Exemplos

### `examples/gerar_segunda_via_demo.py`

É o exemplo executável principal.

Ele utiliza classes geradas pelos XSDs para construir:

- endereço;
- naturalidade;
- diplomado;
- ato regulatório;
- curso;
- IES emissora;
- diploma;
- histórico escolar de segunda via;
- filiação;
- dados privados;
- registro de segunda via;
- documentação acadêmica;
- assinatura estrutural de desenvolvimento.

Depois chama:

```python
generate_and_validate()
```

e grava:

```text
output/segunda_via_demo.xml
```

Os dados utilizados são fictícios.

### `examples/gerar_segunda_via.py`

É uma estrutura de exemplo voltada para a futura integração com dados reais.

A função:

```python
build_from_db_data()
```

representa a fronteira onde, futuramente, dados vindos do domínio/mapper poderão ser transformados em objetos compatíveis com os XSDs.

A ideia arquitetural é:

```text
PostgreSQL
   ↓
Repository
   ↓
Mapper
   ↓
build_from_db_data()
   ↓
builder
   ↓
XML
```

---

## ✅ 14. Testes

A pasta `tests/` contém os testes automatizados.

### `test_business_rules.py`

Testa:

```python
exactly_one()
```

Verifica os cenários:

- exatamente uma opção;
- nenhuma opção;
- duas opções.

### `test_ids.py`

Testa:

- NONCE com 44 dígitos;
- vínculo entre os identificadores e o mesmo NONCE;
- formato do código de validação.

### `test_invalid_legacy_xml.py`

É um teste negativo.

Ele confirma que um XML legado que não atende ao XSD atual deve produzir:

```text
SchemaValidationError
```

### `test_schema_compile.py`

Percorre os XSDs locais e verifica se eles conseguem ser compilados pelo:

```text
lxml.etree.XMLSchema
```

### `test_second_via_demo.py`

Executa o exemplo de segunda via em uma pasta temporária e verifica se o XML foi criado.

### `conftest.py`

Contém configuração de apoio aos testes.

---

## 🔍 15. Auditoria dos XSDs

O script:

```text
scripts/audit_xsds.py
```

verifica o pacote local de schemas.

Ele confere:

- presença dos arquivos esperados;
- arquivos extras;
- compilação dos XSDs;
- referências relativas `schemaLocation`.

Pode ser executado com:

```powershell
python scripts\audit_xsds.py
```

---

## 📚 16. Documentação técnica

A pasta `docs/` contém documentação complementar.

| Documento | Conteúdo |
| --- | --- |
| `arquitetura.md` | Arquitetura e separação de responsabilidades |
| `guia_por_modulo.md` | Visão rápida dos módulos |
| `regras_mec_v105.md` | Regras relevantes da versão 1.05 |
| `assinatura.md` | Arquitetura de assinatura |
| `postgresql.md` | Integração futura com PostgreSQL |
| `alternativas_xml.md` | Alternativas técnicas para geração/validação XML |
| `fontes_e_normas.md` | Referências normativas e técnicas |
| `auditoria_projeto.md` | Descrição técnica da organização do protótipo |

---

## 🗃️ 17. Diretório `legacy/`

Contém materiais de referência do protótipo anterior:

```text
legacy/main_original.py
legacy/diploma_teste.xml
```

> ℹ️ Esses arquivos não fazem parte do fluxo principal de geração.

O XML legado é utilizado pelo teste negativo para garantir que uma estrutura inadequada não seja aceita pelo XSD.

---

## 🗄️ 18. Diretório `sql/`

Contém:

```text
sql/001_initial_schema.sql
```

Esse SQL representa uma referência de modelagem para a futura camada de persistência.

A arquitetura prevista é integrar o projeto ao **PostgreSQL já existente na instituição**, por meio de uma camada de acesso/repositório.

> ℹ️ O objetivo não é criar um banco institucional paralelo para substituir a base acadêmica existente.

---

## 🎭 19. Dados fictícios e dados reais

O exemplo atual usa dados fictícios, como:

```text
Aluno de Demonstração
Engenharia de Computação
IES de Demonstração
```

Na integração real, esses dados deverão vir das fontes institucionais.

A separação recomendada é:

```text
Banco institucional
        ↓
Repository
        ↓
Modelo de domínio
        ↓
Mapper
        ↓
Modelos xsdata
        ↓
Builder
        ↓
XML
```

> 💡 Essa separação evita colocar SQL diretamente dentro da montagem do XML.

---

## 📄 20. Documento gerado atualmente

O arquivo gerado pelo exemplo possui como raiz:

```xml
<DocumentacaoAcademicaRegistro>
```

e utiliza o ramo:

```xml
<RegistroSegundaViaReq>
```

> ⚠️ Portanto, o arquivo atual representa o fluxo de **Documentação Acadêmica para Registro**, e não deve ser confundido com um arquivo final independente do **Diploma Digital**.

A especificação do MEC possui diferentes documentos XML, incluindo:

- Diploma Digital;
- Documentação Acadêmica para Emissão e Registro;
- Histórico Escolar Digital;
- Currículo Escolar Digital;
- Lista de Diplomas Anulados;
- Arquivo de Fiscalização.

Cada documento possui seu próprio schema e finalidade.

---

## ⚖️ 21. Validação estrutural x conformidade de produção

A validação realizada atualmente demonstra que o XML:

```text
é bem formado
        +
atende ao XSD utilizado
```

> ⚠️ Isso não significa, por si só, que o documento esteja pronto para emissão institucional.

A conformidade produtiva também envolve, conforme o fluxo aplicável:

- regras de negócio;
- dados institucionais reais;
- identificadores corretos;
- assinatura digital institucional;
- requisitos de XAdES/PBAD;
- certificados;
- fluxo de emissora/registradora;
- armazenamento;
- auditoria;
- publicação e URL;
- controles de segurança e privacidade.

---

## 🔐 22. SHA-256

Depois de gerar e validar o XML, o projeto calcula um SHA-256:

```python
hashlib.sha256(xml_bytes).hexdigest()
```

O resultado é um **hash do conteúdo do arquivo**.

Ele pode ser utilizado para identificação e controle de integridade do artefato.

> ⚠️ SHA-256 não é assinatura digital.

| Conceito | Definição |
| --- | --- |
| **SHA-256** | impressão digital do conteúdo |
| **Assinatura digital** | mecanismo criptográfico de autenticação/integridade/autoria conforme a infraestrutura utilizada |

---

## 💻 23. Fluxo para desenvolvimento

A rotina básica de desenvolvimento é:

```powershell
# 1. Ativar ambiente
.venv\Scripts\Activate.ps1

# 2. Instalar/atualizar dependências quando necessário
pip install -e ".[dev]"

# 3. Rodar testes
pytest

# 4. Gerar XML de demonstração
python -m examples.gerar_segunda_via_demo

# 5. Conferir o arquivo
dir output
```

Arquivo esperado:

```text
output\segunda_via_demo.xml
```

---

## 🔧 24. Fluxo de manutenção

Quando uma nova versão oficial de XSD for adotada:

```text
novo pacote XSD
      ↓
atualizar schemas/
      ↓
regenerar generated/
      ↓
revisar imports
      ↓
revisar builders
      ↓
revisar regras de negócio
      ↓
atualizar testes
      ↓
validar XML
```

Os arquivos gerados devem ser regenerados a partir do schema correspondente, em vez de receber alterações manuais permanentes.

---

## 🎯 25. Princípio central do projeto

O projeto separa quatro conceitos:

| Conceito | Papel |
| --- | --- |
| **XSD** | define a estrutura permitida |
| **Modelo Python** | representa essa estrutura no código |
| **Builder / regras** | decide como os dados do negócio serão organizados |
| **XML** | é o documento concreto produzido |

A arquitetura permite que a aplicação evolua de um exemplo com dados fictícios para um fluxo institucional conectado ao banco acadêmico, mantendo separadas a fonte dos dados, as regras de negócio, a representação XSD e a geração do XML.

---

## 📊 26. Estado funcional do projeto

O projeto possui atualmente:

- ✅ pacote XSD MEC v1.05;
- ✅ modelos Python gerados com `xsdata`;
- ✅ geração de `DocumentacaoAcademicaRegistro`;
- ✅ suporte ao ramo `RegistroSegundaViaReq`;
- ✅ serialização XML;
- ✅ validação XSD;
- ✅ regras de identificadores;
- ✅ regras de escolha entre estruturas alternativas;
- ✅ geração de SHA-256;
- ✅ arquitetura de assinatura desacoplada;
- ✅ testes automatizados;
- ✅ exemplo executável;
- ✅ estrutura preparada para integração futura com PostgreSQL.

> ⚠️ A assinatura institucional real e o fluxo completo de produção devem ser implementados antes de qualquer uso para emissão oficial.

---

## ⚡ 27. Comando rápido

Depois que o ambiente estiver configurado:

```powershell
.venv\Scripts\Activate.ps1
pytest
python -m examples.gerar_segunda_via_demo
```

Resultado:

```text
output/
└── segunda_via_demo.xml
```
