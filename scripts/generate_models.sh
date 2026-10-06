#!/usr/bin/env bash
set -euo pipefail

# Regenera apenas os modelos autogerados.
# Nunca edite manualmente os arquivos em generated/.
# Rode "xsdata generate --help" na versão instalada para conferir opções.

xsdata generate schemas --package generated
