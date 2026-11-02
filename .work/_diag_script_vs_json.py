#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kich ban JA Tap02: markdown vs script_tap02_JA.json (thu tai) co giong nhau khong?"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

md = ROOT / "01_KICH_BAN/Tap02_JA/kichban_tap02_JA.md"
bak = ROOT / "01_KICH_BAN/Tap02_JA/kichban_tap02_JA_backup.md"
js = W / "script_tap02_JA.json"
for p in [md, bak, js, W / "timeline_s_JA_t02.json"]:
    if p.exists():
        print(f"  {p.name:<34} {p.stat().st_size:>8} byte · {p.stat().st_mtime}")
print()

env = dict(os.environ)
env["AE_LANG"] = "ja"
env["AE_EP"] = "02"
env["PYTHONIOENCODING"] = "utf-8"
tmp = W / "_tmp_reparse_tap02_JA.json"
if tmp.exists():
    tmp.unlink()
r = subprocess.run([sys.executable, str(W / "parse_kichban.py"), str(md), str(tmp)],
                   cwd=ROOT, env=env, capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
print("parse_kichban rc =", r.returncode)
print((r.stdout or "")[-600:])
if r.returncode != 0:
    print((r.stderr or "")[-800:])
    raise SystemExit(1)

new = json.loads(tmp.read_text(encoding="utf-8-sig"))
old = json.loads(js.read_text(encoding="utf-8-sig"))


def texts(d):
    out = []
    for turn in d.get("turns", d if isinstance(d, list) else []):
        if isinstance(turn, dict):
            for s in turn.get("sentences", []):
                out.append((turn.get("id"), s.get("id"), s.get("text") if isinstance(s, dict) else s))
    return out


tn, to = texts(new), texts(old)
print(f"\n  parse moi tu markdown: {len(tn)} cau")
print(f"  JSON dang dung (audio) : {len(to)} cau")

same = sum(1 for a, b in zip(tn, to) if a[2] == b[2])
print(f"  cau giong het: {same} / {min(len(tn), len(to))}")
diff = [(a, b) for a, b in zip(tn, to) if a[2] != b[2]]
print(f"  cau KHAC nhau: {len(diff)}")
for a, b in diff[:8]:
    print(f"    id {a[1]} vs {b[1]}")
    print(f"      markdown: {a[2][:90]!r}")
    print(f"      json    : {b[2][:90]!r}")

# file nao moi hon?
print()
for name, p in [("kichban_tap02_JA.md", md), ("kichban_tap02_JA_backup.md", bak),
                ("script_tap02_JA.json", js)]:
    if p.exists():
        print(f"  {name:<34} sua lan cuoi: {p.stat().st_mtime}")
