#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tinh phan con lai: doc manifest + doc muc 4 -> danh sach ma SFX chua co file."""
import json
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
MAP = ROOT / ".work" / "yt_map.tsv"
STATE = ROOT / ".work" / "yt_watch_state.json"
DOC = ROOT / "02_SAN_XUAT" / "Danh_Sach_SFX_Tap03-29.md"

used = []
if STATE.exists():
    st = json.loads(STATE.read_text(encoding="utf-8"))
    used = st.get("used", [])

man = []
if MAP.exists():
    for i, line in enumerate(MAP.read_text(encoding="utf-8-sig").splitlines(), 1):
        if not line.strip():
            continue
        p = line.split("\t")
        if len(p) >= 6:
            man.append({"line": i, "track": p[0], "ma": p[1], "dur": p[5], "used": p[1] in used})

lines = DOC.read_text(encoding="utf-8").splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith("## 4."))
rows = []
for l in lines[start:]:
    m = re.match(r"^\|\s*(\d+)\s*\|\s*`([^`]+)`\s*\|\s*([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*`([^`]+)`\s*\|", l)
    if m:
        rows.append({"n": int(m.group(1)), "file": m.group(2), "loai": m.group(3),
                     "taps": m.group(4), "dest": m.group(5)})

man_codes = {m["ma"] for m in man}
print(f"Tong mau trong doc muc 4: {len(rows)}")
print(f"Dong manifest: {len(man)}   used state: {len(used)}")
print("--- Dong manifest CHUA used (se bi anh huong) ---")
for m in man:
    if not m["used"]:
        print(f"  line{m['line']}: {m['track']} -> {m['ma']}  dur={m['dur']}")

print("\n--- Ma trong manifest KHONG nam trong 169 (hoac da xong) ---")
doc_codes = {r["file"].replace(".wav", "") for r in rows}
for m in man:
    if m["ma"] not in doc_codes:
        print(f"  line{m['line']}: {m['ma']} (track={m['track']}) used={m['used']}")

done = {r["file"].replace(".wav", "") for r in rows
        if (ROOT / "assets" / "sfx" / r["file"]).exists() or (ROOT / r["dest"]).exists()}
print(f"\nDa co file thuoc 169: {len(done)}   Con lai: {len(rows)-len(done)}")
print("\n=== CON LAI (theo so tap giam dan) ===")
rem = [r for r in rows if r["file"].replace(".wav", "") not in done]
rem.sort(key=lambda r: (-len([t for t in r["taps"].split(",") if t.strip()]), r["n"]))
for r in rem:
    ntap = len([t for t in r["taps"].split(",") if t.strip()])
    print(f"{r['n']:>3} {r['file']:<38} {r['loai']:<16} taps={ntap:<3} {r['taps'][:40]:<42} {r['dest']}")
