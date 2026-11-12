#!/usr/bin/env bash
# usage: tools/desk-brief-appendix.sh <desk> <letter>  -> docs/briefs/desks/<desk>-<letter>.md
set -euo pipefail
desk="$1"; L="$2"
file=$(ls book/appendices/${L}-*.md | head -n1); slug=$(basename "$file" .md); slug="${slug#${L}-}"
U=$(echo "$L" | tr a-z A-Z)
mkdir -p docs/briefs/desks
out="docs/briefs/desks/${desk}-${L}.md"
sed -e "s#book/chapters/{NN}-{slug}.md#book/appendices/${L}-${slug}.md#g" -e "s/facts-{NN}.md/facts-${U}.md/g" -e "s/Chapter {N}/Appendix ${U}/g" -e "s/{NN}/${L}/g" -e "s/{N}/${U}/g" -e "s/{slug}/${slug}/g" "docs/squad/${desk}.md" > "$out"
echo "$out"
