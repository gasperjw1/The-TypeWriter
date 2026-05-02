#!/bin/bash
# Syncs docs/index.html with script_maker.html
# Adjusts the describe/guide link for the docs context
# Run from the repo root: ./sync.sh

set -e

cp script_maker.html docs/index.html
sed -i '' 's|href="docs/guide.html"|href="guide.html"|' docs/index.html 2>/dev/null \
  || sed -i 's|href="docs/guide.html"|href="guide.html"|' docs/index.html

echo "✓ docs/index.html synced with script_maker.html"
