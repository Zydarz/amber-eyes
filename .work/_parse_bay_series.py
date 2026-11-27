#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Parse 140 tap series Bay Tam Ly Va Hanh Vi bang parse_kichban.py de dem cau/tu that."""
import json, re, subprocess, sys, tempfile, os
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PARSER = ROOT / ".work" / "parse_kichban.py"
BASE = ROOT / "01_KICH_BAN" / "BayTamLyVaHanhVi"
OUT = ROOT / ".work" / "_bay_tap_parse"
OUT.mkdir(exist_ok=True)

# import parser de dung ham noi bo
sys.path.insert(0, str(ROOT / ".work"))
import importlib.util
spec = importlib.util.spec_from_file_location("pk", PARSER)
pk = importlib.util.module_from_spec(spec)
spec.loader.exec_module(pk)

taps = sorted([d for d in BASE.rglob("Tap*") if d.is_dir()],
              key=lambda d: int(re.search(r"Tap(\d+)", d.name).group(1)))
tot_sent = tot_words = 0
rows = []
fail = []
for d in taps:
    f = d / ("kichban_tap%s.md" % re.search(r"Tap(\d+)", d.name).group(1))
    if not f.exists():
        c = list(d.glob("kichban*.md"))
        f = c[0] if c else None
    if not f:
        fail.append((d.name, "khong co file"))
        continue
    out = OUT / (d.name + ".json")
    try:
        pk.parse_file(str(f), str(out))
        data = json.loads(out.read_text(encoding="utf-8"))
    except Exception as e:
        fail.append((d.name, str(e)[:60]))
        continue
    items = data if isinstance(data, list) else data.get("sentences", data.get("items", []))
    n = len(items)
    w = 0
    for it in items:
        if isinstance(it, dict):
            txt = it.get("text") or it.get("noi_dung") or it.get("sentence") or ""
        else:
            txt = str(it)
        w += len(txt.split())
    tot_sent += n
    tot_words += w
    rows.append((d.name, n, w))

print("=== SERIES BAY TAM LY VA HANH VI ===")
print("so tap parse thanh cong: %d / %d" % (len(rows), len(taps)))
print("TONG cau thoai: %d" % tot_sent)
print("TONG tu: %d" % tot_words)
print("trung binh cau/tap: %.1f" % (tot_sent / max(len(rows), 1)))
print("trung binh tu/tap: %.0f" % (tot_words / max(len(rows), 1)))
if fail:
    print("FAIL:", fail[:10])
lo = [r for r in rows if r[1] < 200]
print("tap <200 cau:", len(lo), lo[:10])
print("tap >280 cau:", len([r for r in rows if r[1] > 280]))
print("10 tap dau:", rows[:10])
print("10 tap cuoi:", rows[-10:])
