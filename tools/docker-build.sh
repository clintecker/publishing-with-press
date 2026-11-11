#!/usr/bin/env bash
# Build a press book inside the pinned toolchain image, streaming the book in
# and dist/ out with tar (works even when the book lives outside colima's
# mounted $HOME). usage: docker-build.sh BOOK_DIR OUT_DIR target [target...]
set -euo pipefail
book="$1"; out="$2"; shift 2
press=/Users/clint/code/press
image="$(sed -n 's/^[[:space:]]*image:[[:space:]]*//p' "$press/.github/workflows/build.yml" | head -n1)"
docker volume inspect press-dev-pipcache >/dev/null 2>&1 || docker volume create press-dev-pipcache >/dev/null
mkdir -p "$out"
COPYFILE_DISABLE=1 tar --no-xattrs --no-mac-metadata -C "$book" --exclude=./build --exclude=./dist -cf - . | docker run --rm -i \
  -v "$press":/src:ro -v press-dev-pipcache:/root/.cache/pip \
  -e PYTHONPATH=/src/src -e PRESS_TARGETS="$*" "$image" bash -euo pipefail -c '
    pip install --break-system-packages -q -r /src/requirements-lock.txt >&2
    mkdir -p /work/book && tar -x -C /work/book && cd /work/book
    export BOOK_ROOT=/work/book
    for t in $PRESS_TARGETS; do echo "── press $t ──" >&2; python3 -m press "$t" >&2; done
    tar -C /work/book -cf - dist' | tar -x -C "$out"
echo "artifacts in $out/dist"
