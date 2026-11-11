#!/usr/bin/env bash
# usage: tools/desk-brief.sh <desk> <NN>  -> writes docs/briefs/desks/<desk>-<NN>.md with {N} {NN} {slug} filled
set -euo pipefail
desk="$1"; nn="$2"
file=$(ls book/chapters/${nn}-*.md | head -n1)
slug=$(basename "$file" .md); slug="${slug#${nn}-}"
n=$((10#$nn))
mkdir -p docs/briefs/desks
out="docs/briefs/desks/${desk}-${nn}.md"
sed -e "s/{NN}/${nn}/g" -e "s/{N}/${n}/g" -e "s/{slug}/${slug}/g" "docs/squad/${desk}.md" > "$out"
echo "$out"
