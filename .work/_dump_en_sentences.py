#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dump script_tap02_EN.json sentences as plain text for reading."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

script = json.loads((W / "script_tap02_EN.json").read_text(encoding="utf-8"))
out = []
for e in script:
    if e.get("kind") != "LOI":
        continue
    out.append(f"=== ELEMENT {e.get('id')} | {e.get('title','')} ===")
    for s in e.get("sentences", []):
        out.append(f"{s['id']}\t{s['text']}")
    out.append("")

txt = "\n".join(out)
(W / "_en_sentences_dump.txt").write_text(txt, encoding="utf-8")
print("elements:", len([e for e in script if e.get("kind") == "LOI"]))
print("lines:", len(out))
print("chars:", len(txt))
