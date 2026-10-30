#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phan con lai THAT: doc 169 ma o muc 4, tru ca file da co trong assets/sfx va MP3 trong inbox."""
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"

lines = DOC.read_text(encoding="utf-8").splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith("## 4."))
rows = []
for l in lines[start:]:
    m = re.match(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*`([^`]+)`\s*\|", l)
    if m:
        rows.append({"n": int(m.group(1)), "file": m.group(2), "loai": m.group(3),
                     "taps": m.group(4), "dest": m.group(5)})

inbox = {p.stem for p in INBOX.glob("*.mp3")}
rem = []
for r in rows:
    code = r["file"].replace(".wav", "")
    has_asset = (ROOT / "assets" / "sfx" / r["file"]).exists() or (ROOT / r["dest"]).exists()
    if has_asset or code in inbox:
        continue
    rem.append(r)

rem.sort(key=lambda r: (-len([t for t in r["taps"].split(",") if t.strip()]), r["n"]))
print(f"Tong 169 | da co file/MP3: {len(rows)-len(rem)} | CON LAI: {len(rem)}")
print(f"inbox mp3 = {len(inbox)}\n")
for r in rem:
    ntap = len([t for t in r["taps"].split(",") if t.strip()])
    print(f"{r['n']:>3} {r['file']:<40} taps={ntap:<2} {r['taps'][:38]:<40} {r['dest']}")
