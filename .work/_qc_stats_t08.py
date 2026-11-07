#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thống kê bảng shot + ảnh tĩnh Tập 08 (cho báo cáo QC)."""
import json
import statistics
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"

for lang, suf in (("vi", "_t08"), ("en", "_EN_t08"), ("ja", "_JA_t08")):
    sh = json.loads((W / f"shots{suf}.json").read_text(encoding="utf-8"))
    S = sh["shots"]
    tl = json.loads((W / f"timeline_s{suf}.json").read_text(encoding="utf-8"))
    dur = [round(s["end"] - s["start"], 1) for s in S]
    nsent = sum(len(s["sentences"]) for s in S)
    # chuoi nen lien tiep toi da
    run = best = 1
    for a, b in zip(S, S[1:]):
        run = run + 1 if a["bg"] == b["bg"] else 1
        best = max(best, run)
    tpl = {}
    for s in S:
        k = s["template"] or "(giu)"
        tpl[k] = tpl.get(k, 0) + 1
    roles = {}
    for s in S:
        if s["role"]:
            roles[s["role"]] = roles.get(s["role"], 0) + len(s["sentences"])
    bgs = {s["bg"] for s in S if s["bg"] != "void"}
    n_png = len(list((W / f"video3{suf}/stills").glob("shot_*.png")))
    print(f"== {lang.upper()}")
    print(f"  timeline {tl['total']:.1f}s ({int(tl['total']//60)}:{int(tl['total']%60):02d}) · "
          f"{len(tl['items'])} cau · {len(tl['markers'])} marker")
    print(f"  shot {len(S)} · phu cau {nsent}/{len(tl['items'])} · anh {n_png}")
    print(f"  thoi luong: TB {statistics.mean(dur):.1f}s · max {max(dur)}s · >15s: {sum(1 for d in dur if d>15)}")
    print(f"  nen lien tiep toi da toi da: {best} · loai nen {len(bgs)}")
    print(f"  mau: " + ", ".join(f"{k}×{v}" for k, v in sorted(tpl.items(), key=lambda x: -x[1])))
    print(f"  vai: " + ", ".join(f"{k}={v}" for k, v in sorted(roles.items())))
    longest = max(S, key=lambda s: s["end"] - s["start"])
    print(f"  shot dai nhat: {longest['id']} {longest['end']-longest['start']:.1f}s")
