#!/usr/bin/env python3
"""Proof: the pipeline archetype (style guide 5.2 #1), Graphviz back end.

Sources at left, `press check`, pandoc with its Lua filters, a branch to the
PDF route and the other writers, one verifier, the artifacts stacked at right.
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import look  # noqa: E402
from look import dot_label as L, PROCESS, FILE, VERIFIER, FILLS  # noqa: E402

FILTERS = ["typographic-spacing", "set-pieces", "chapter-dropcap",
           "scene-break", "figure-numbering"]
ARTIFACTS = ["alice.pdf", "alice.epub", "alice.html", "alice.txt",
             "alice.docx", "alice-site.zip"]

body = f"""
  src1 [label={L("", mono_lines=["book/chapters/", "*.md"])}, {FILE}, fillcolor="{FILLS[0]}"];
  src2 [label={L("", mono_lines=["config/", "*.yaml"])}, {FILE}, fillcolor="{FILLS[0]}"];
  check [label={L("", mono_lines=["press", "check"])}, {PROCESS}, fillcolor="{FILLS[10]}"];
  pandoc [label={L("pandoc", mono_title=True, mono_lines=FILTERS)}, {PROCESS}, fillcolor="{FILLS[10]}"];
  latex [label={L("", mono_lines=["latexmk", "-lualatex"])}, {PROCESS}, fillcolor="{FILLS[10]}"];
  other [label={L("", mono_lines=["EPUB", "HTML", "chunked", "plain", "docx"])}, {PROCESS}, fillcolor="{FILLS[10]}"];
  verify [label={L("press", mono_lines=[]) .replace("</FONT>>", "</FONT><BR/><FONT FACE=\"Helvetica\" POINT-SIZE=\"8\">verify</FONT>>")}, {VERIFIER}, fillcolor="{FILLS[20]}"];
  subgraph cluster_dist {{
    label="dist/"; fontsize=7; fontname="{look.MONO_NAME}"; style="solid";
    color="black"; penwidth=0.5; margin=6;
"""
for i, a in enumerate(ARTIFACTS):
    body += f'    a{i} [label={L(a, mono_title=True)}, {FILE}, fillcolor="{FILLS[0]}", margin="0.07,0.03"];\n'
body += "    {rank=same; " + " -> ".join(f"a{i}" for i in reversed(range(len(ARTIFACTS)))) + " [style=invis];}\n  }\n"
body += """
  src1 -> check; src2 -> check;
  check -> pandoc;
  pandoc -> latex; pandoc -> other;
  latex -> verify; other -> verify;
  verify -> a2 [lhead=cluster_dist];
"""
look.render_dot("fig-00-proof-pipeline", body,
                look.figures_dir() / "00-proof-pipeline.png",
                measure="full", rankdir="LR", nodesep=0.12, ranksep=0.2,
                splines="polyline", graph_extra=", compound=true")
