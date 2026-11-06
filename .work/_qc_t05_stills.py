#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC ảnh tĩnh Tập 05 — đủ ảnh, đúng ID, không ảnh sót từ bảng cũ, file không rỗng."""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

CASES = [
    ("VI", W / "shots_t05.json", W / "video3_t05/stills"),
    ("EN", W / "shots_EN_t05.json", W / "video3_EN_t05/stills"),
    ("JA", W / "shots_JA_t05.json", W / "video3_JA_t05/stills"),
]
# ID của bảng CŨ (83 shot) để phát hiện ảnh sót
OLD_IDS = set(json.loads((W / "_t05_old_rows_vi.json").read_text(encoding="utf-8"))["rows"])

all_ok = True
for tag, shots_f, stills_d in CASES:
    shots = json.loads(shots_f.read_text(encoding="utf-8"))["shots"]
    want = {s["id"] for s in shots}
    files = sorted(stills_d.glob("*.png")) if stills_d.exists() else []
    have = {f.stem.replace("shot_", "") for f in files}
    missing = sorted(want - have)
    extra = sorted(have - want)
    stale = sorted(x for x in extra if x in OLD_IDS)
    empty = [f.name for f in files if f.stat().st_size < 5000]
    tiny = [f.name for f in files if f.stat().st_size < 20000]
    ids = [s["id"] for s in shots]
    dup = sorted({x for x in ids if ids.count(x) > 1})
    ok = not (missing or extra or empty or dup)
    all_ok &= ok
    print(f"=== {tag} ===")
    print(f"  shot trong bảng: {len(shots)} · file png: {len(files)}")
    print(f"  thiếu ảnh : {len(missing)} {missing[:8]}")
    print(f"  ảnh thừa  : {len(extra)} {extra[:8]}")
    print(f"  ảnh sót từ bảng cũ : {len(stale)} {stale[:8]}")
    print(f"  file rỗng/nhỏ (<5 KB): {len(empty)} {empty[:5]}")
    print(f"  file nhỏ (<20 KB)   : {len(tiny)} {tiny[:5]}")
    print(f"  ID shot trùng nhau  : {len(dup)} {dup}")
    print(f"  => {'OK' if ok else 'LOI'}")
print("\nTONG: " + ("TAT CA 3 NGON NGU OK" if all_ok else "CO LOI"))
