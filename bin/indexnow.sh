#!/bin/bash
# IndexNow ping — notifies Bing (and Yandex, Naver, Seznam) that one or
# more URLs on thescriptwriter.app have changed, so they re-crawl within
# minutes instead of days.
#
# The IndexNow spec: https://www.indexnow.org/
# Bing endpoint:     https://api.indexnow.org/IndexNow
# Verification:      https://thescriptwriter.app/<KEY>.txt must contain
#                    just <KEY> on a single line.
#
# Usage:
#   ./bin/indexnow.sh                          # ping every URL in sitemap.xml
#   ./bin/indexnow.sh https://thescriptwriter.app/blog/new-post.html
#   ./bin/indexnow.sh url1 url2 url3           # multiple specific URLs
#   ./bin/indexnow.sh --dry-run [urls...]      # show what would be sent, don't POST
#
# Run after `git push` once GitHub Pages has rebuilt (usually ~30-60 seconds).
# A successful response is HTTP 200 or 202; 422 means a URL is outside the
# verified host.

set -e

HOST="thescriptwriter.app"
KEY="a72c523f5eaf157925b7cef3fde06abd"
KEY_LOCATION="https://${HOST}/${KEY}.txt"
API="https://api.indexnow.org/IndexNow"

DRY_RUN=0
if [[ "$1" == "--dry-run" ]]; then
  DRY_RUN=1
  shift
fi

# Gather URLs: explicit args if given, otherwise everything in sitemap.xml
declare -a urls
if [[ $# -gt 0 ]]; then
  urls=("$@")
else
  # Parse <loc> entries from the public sitemap. Falls back to local file if
  # the live site isn't reachable (e.g., DNS sandboxed during local testing).
  sitemap_xml=$(curl -fsSL "https://${HOST}/sitemap.xml" 2>/dev/null || cat "$(dirname "$0")/../docs/sitemap.xml")
  while IFS= read -r line; do
    [[ -n "$line" ]] && urls+=("$line")
  done < <(echo "$sitemap_xml" | grep -oE '<loc>[^<]+</loc>' | sed -E 's|</?loc>||g')
fi

if [[ ${#urls[@]} -eq 0 ]]; then
  echo "✗ No URLs to submit." >&2
  exit 1
fi

echo "→ IndexNow: ${#urls[@]} URL(s) to submit"
for u in "${urls[@]}"; do echo "    $u"; done

# Build the JSON payload (manually, no jq dependency)
url_list=""
for u in "${urls[@]}"; do
  esc=$(printf '%s' "$u" | sed 's/"/\\"/g')
  url_list+="\"${esc}\","
done
url_list="${url_list%,}"  # strip trailing comma

payload=$(cat <<JSON
{"host":"${HOST}","key":"${KEY}","keyLocation":"${KEY_LOCATION}","urlList":[${url_list}]}
JSON
)

if [[ $DRY_RUN -eq 1 ]]; then
  echo ""
  echo "→ DRY RUN — would POST to ${API}:"
  echo "$payload"
  exit 0
fi

echo ""
echo "→ POSTing to ${API}…"
response=$(curl -sS -w "\nHTTP_STATUS:%{http_code}" -X POST "$API" \
  -H "Content-Type: application/json; charset=utf-8" \
  -H "User-Agent: thescriptwriter.app-indexnow/1.0" \
  -d "$payload")

body=$(echo "$response" | sed '$d')
status=$(echo "$response" | tail -n 1 | sed 's/HTTP_STATUS://')

if [[ "$status" == "200" || "$status" == "202" ]]; then
  echo "✓ Accepted (HTTP $status). Bing will re-crawl within minutes."
elif [[ "$status" == "422" ]]; then
  echo "✗ HTTP 422 — at least one URL is outside the verified host '${HOST}'."
  echo "  Check that every URL starts with https://${HOST}/"
  echo "  Body: $body"
  exit 1
elif [[ "$status" == "403" ]]; then
  echo "✗ HTTP 403 — key verification failed."
  echo "  Confirm ${KEY_LOCATION} exists and contains exactly: ${KEY}"
  echo "  (Often this just means GitHub Pages hasn't rebuilt yet — wait 60s and retry.)"
  exit 1
else
  echo "✗ HTTP $status"
  [[ -n "$body" ]] && echo "  Body: $body"
  exit 1
fi
