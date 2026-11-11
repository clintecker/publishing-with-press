# Building this book

- Quick look (native, about 30 s): `~/code/.pwp-venv/bin/press check`,
  then `~/code/.pwp-venv/bin/press pdf`; `press render` writes page images
  to `build/rendered-book/`. Native TeX here now has `wrapfig` and
  `lettrine` (installed in user mode), but no epubcheck.
- The truth (the pinned toolchain image, about 40 s warm):
  `tools/docker-build.sh . build/docker all` or
  `tools/docker-build.sh . build/docker all verify-print coverwrap`.
  Artifacts land in `build/docker/dist/`. The script streams the book in
  with tar and strips macOS metadata, so no `._*` file reaches
  `assets/woodcuts/`.
- Commit before `press all`: the source edition packs the git index.
