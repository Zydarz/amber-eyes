#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Debug lượt lệch số câu giữa bản VN và bản JA (theo parse_kichban).

    py -3 .work/_ja_diff_turn.py 01 03 04 05 20
"""
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import make_ja_scripts as M  # noqa: E402


def parse(path):
    out = HERE / f"_dbg_{path.stem}.json"
    subprocess.run([sys.executable, str(HERE / "parse_kichban.py"), str(path), str(out)],
                   check=True, capture_output=True)
    els = json.loads(out.read_text(encoding="utf-8"))
    out.unlink()
    return els


for ep in sys.argv[1:]:
    ja_path = HERE.parent / "01_KICH_BAN" / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not ja_path.exists():
        print(f"--- Tap{ep}: chưa có file JA")
        continue
    vn = [e for e in parse(M.canonical_vn(ep)) if e["kind"] == "LOI"]
    ja = [e for e in parse(ja_path) if e["kind"] == "LOI"]
    print(f"\n########## Tap{ep}: VN {len(vn)} lượt · JA {len(ja)} lượt")
    if len(vn) != len(ja):
        print("  !! lệch số lượt")
        continue
    for i, (a, b) in enumerate(zip(vn, ja), 1):
        na, nb = len(a["sentences"]), len(b["sentences"])
        if na == nb:
            continue
        print(f"\n--- lượt {i}: VN={na} câu  JA={nb} câu")
        print("  [VN] " + " ".join(a["sentences"][j]["text"] for j in range(na)))
        print("  [JA] " + " ".join(b["sentences"][j]["text"] for j in range(nb)))
        # tách từng câu
        print("  [VN từng câu]")
        for j, s in enumerate(a["sentences"], 1):
            print(f"     {j}. {s['text']}")
        print("  [JA từng câu]")
        for j, s in enumerate(b["sentences"], 1):
            print(f"     {j}. {s['text']}")
