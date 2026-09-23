#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 1 ]]; then
  echo "Usage: $0 path/to/document.qmd" >&2
  exit 1
fi

DOCUMENT="$1"

if [[ ! -f "$DOCUMENT" ]]; then
  echo "Document not found: $DOCUMENT" >&2
  exit 1
fi

# Render only the selected document using the website project settings.
quarto render "$DOCUMENT"

# Publish the existing website output without rendering the whole project again.
quarto publish gh-pages --no-render --no-prompt