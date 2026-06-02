#!/bin/bash
# Syncs docs/index.html with script_maker.html
# Adjusts the describe/guide link for the docs context
# Run from the repo root: ./sync.sh

set -e

cp script_maker.html docs/index.html

# Rewrite docs/ links for the docs context (index.html is already inside docs/)
sed -i '' 's|href="docs/guide.html"|href="guide.html"|;s|href="docs/compare.html"|href="compare.html"|;s|href="docs/blog/"|href="blog/"|g;s|href="docs/privacy.html"|href="privacy.html"|g' docs/index.html 2>/dev/null \
  || sed -i 's|href="docs/guide.html"|href="guide.html"|;s|href="docs/compare.html"|href="compare.html"|;s|href="docs/blog/"|href="blog/"|g;s|href="docs/privacy.html"|href="privacy.html"|g' docs/index.html

# Rewrite PWA paths for the docs context (manifest, icons, SW are in same dir)
sed -i '' 's|href="docs/manifest.json"|href="manifest.json"|;s|href="docs/icon-192.png"|href="icon-192.png"|' docs/index.html 2>/dev/null \
  || sed -i 's|href="docs/manifest.json"|href="manifest.json"|;s|href="docs/icon-192.png"|href="icon-192.png"|' docs/index.html
sed -i '' "s|register('docs/sw.js'|register('sw.js'|" docs/index.html 2>/dev/null \
  || sed -i "s|register('docs/sw.js'|register('sw.js'|" docs/index.html

# Rewrite vendored JS paths (vendor/ is a sibling of index.html inside docs/)
sed -i '' 's|src="docs/vendor/|src="vendor/|g' docs/index.html 2>/dev/null \
  || sed -i 's|src="docs/vendor/|src="vendor/|g' docs/index.html

# Rewrite badge paths (badges/ is a sibling of index.html inside docs/)
sed -i '' 's|src="docs/badges/|src="badges/|g' docs/index.html 2>/dev/null \
  || sed -i 's|src="docs/badges/|src="badges/|g' docs/index.html

echo "✓ docs/index.html synced with script_maker.html"
