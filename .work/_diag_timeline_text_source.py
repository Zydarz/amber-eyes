#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Nguon text cua timeline (phu de) — build_audio3.py doc gi?"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

src = (W / "build_audio3.py").read_text(encoding="utf-8-sig")
print("=== build_audio3.py: dong nao lay 'text' ===")
for i, line in enumerate(src.splitlines(), 1):
    if re.search(r"tts_manifest|manifest|text\b", line) and (
            "timeline" in line or "manifest" in line or '"text"' in line or "'text'" in line
            or "it\[.text.\]" in line or "text=" in line):
        print(f"  {i:>4}: {line.rstrip()[:150]}")

print()
print("=== payload gui len Kaggle (higgs_payload_JA_t02.json) ===")
for f in ["kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_JA_t02.json",
          "kaggle_higgs/dataset_voxcpm2_ja/higgs_payload_r2_JA_t02.json",
          "kaggle_higgs/dataset_voxcpm2_ja/prod_spec_JA_t02.json"]:
    p = W / f
    if not p.exists():
        print(f"  {f}: KHONG CO")
        continue
    import json
    d = json.loads(p.read_text(encoding="utf-8-sig"))
    print(f"  {f} · {p.stat().st_mtime} · kieu={type(d).__name__} len={len(d)}")
    rows = d if isinstance(d, list) else d.get("items", d.get("rows", []))
    for r in rows:
        if isinstance(r, dict) and r.get("id") == "3.08#10":
            for k in ("text", "text_sent", "text_plain", "sentence"):
                if r.get(k):
                    print(f"      {k} = {r[k][:110]}")
            break
