#!/usr/bin/env bash
set -euo pipefail
desk="$1"; mkdir -p docs/briefs/desks
sed -e "s#book/chapters/{NN}-{slug}.md#book/chapters/00-preface.md#g" -e "s/facts-{NN}.md/facts-01.md/g" -e "s/Chapter {N}/the Preface/g" -e "s/{NN}/00/g" -e "s/{N}/0/g" -e "s/{slug}/preface/g" "docs/squad/${desk}.md" > "docs/briefs/desks/${desk}-00.md"; echo "docs/briefs/desks/${desk}-00.md"
