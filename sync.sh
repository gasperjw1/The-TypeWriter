#!/bin/bash
# Syncs docs/index.html with script_maker.html
# Adjusts the describe/guide link for the docs context
# Run from the repo root: ./sync.sh

set -e

cp script_maker.html docs/index.html

# Rewrite docs/ links for the docs context (index.html is already inside docs/)
sed -i '' 's|href="docs/guide.html"|href="guide.html"|;s|href="docs/compare.html"|href="compare.html"|' docs/index.html 2>/dev/null \
  || sed -i 's|href="docs/guide.html"|href="guide.html"|;s|href="docs/compare.html"|href="compare.html"|' docs/index.html

echo "✓ docs/index.html synced with script_maker.html"
