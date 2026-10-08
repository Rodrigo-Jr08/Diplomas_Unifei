from __future__ import annotations

import re
from pathlib import Path
from lxml import etree

ROOT = Path(__file__).resolve().parents[1]
SCHEMAS = ROOT / "schemas"
EXPECTED = {
    "DiplomaDigital_v1.05.xsd",
    "DocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd",
    "HistoricoEscolarDigital_v1.05.xsd",
    "ListaDiplomasAnulados_v1.05.xsd",
    "ArquivoFiscalizacao_v1.05.xsd",
    "CurriculoEscolarDigital_v1.05.xsd",
    "tiposBasicos_v1.05.xsd",
    "leiauteDiplomaDigital_v1.05.xsd",
    "leiauteDocumentacaoAcademicaRegistroDiplomaDigital_v1.05.xsd",
    "leiauteHistoricoEscolar_v1.05.xsd",
    "leiauteListaDiplomasAnulados_v1.05.xsd",
    "leiauteArquivoFiscalizacao_v1.05.xsd",
    "leiauteCurriculoEscolar_v1.05.xsd",
    "xmldsig-core-schema_v1.1.xsd",
}

#Verificação de schemas no projeto antes de execução
def main() -> int:
    present = {p.name for p in SCHEMAS.glob("*.xsd")}
    missing = sorted(EXPECTED - present)
    unexpected = sorted(present - EXPECTED)
    print(f"XSD encontrados localmente: {len(present)}")
    if missing:
        print("Arquivos oficiais v1.05 ausentes no pacote local:")
        for name in missing:
            print(f"  - {name}")
    if unexpected:
        print("Arquivos XSD extras não previstos no manifesto:")
        for name in unexpected:
            print(f"  - {name}")

    errors = 0
    parser = etree.XMLParser(no_network=True, resolve_entities=False, load_dtd=False)
    for xsd in sorted(SCHEMAS.glob("*.xsd")):
        try:
            doc = etree.parse(str(xsd), parser)
            etree.XMLSchema(doc)
            print(f"OK  {xsd.name}")
        except Exception as exc:
            errors += 1
            print(f"ERR {xsd.name}: {exc}")

    # Também verifica explicitamente se cada schemaLocation relativo resolve.
    for xsd in sorted(SCHEMAS.glob("*.xsd")):
        text = xsd.read_text(encoding="utf-8")
        for ref in re.findall(r'(?:schemaLocation|location)="([^"]+)"', text):
            if "://" not in ref and not (SCHEMAS / ref).exists():
                errors += 1
                print(f"ERR {xsd.name}: referência não resolvida: {ref}")

    return 1 if missing or unexpected or errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
