#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S — Phan tich on dinh F0 theo cam xuc (G8) + kiem tra cac cau ASR rong (CER 100%)."""
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(__file__).resolve().parents[1] / ".work"
OUT = WORK / "cer_xac_minh_giong_nam"

rows = json.loads((OUT / "rows2.json").read_text(encoding="utf-8"))
man = json.loads((WORK / "tts_manifest_t02.json").read_text(encoding="utf-8"))
emo = {m["id"]: m["emotion"] for m in man}

groups = defaultdict(list)
for r in rows:
    groups[r["cand"]].append(r)

print("=" * 104)
print("ON DINH F0 THEO CAM XUC (G8) — cung 20 cau, dung emotion/speed production")
print("=" * 104)
for c, rs in sorted(groups.items(), key=lambda kv: -np.std([x["f0"] for x in kv[1] if x["f0"]] or [0])):
    f0s = [x["f0"] for x in rs if x["f0"]]
    print(f"\n{c}")
    print(f"   F0: min {min(f0s):.0f} · median {sorted(f0s)[len(f0s)//2]:.0f} · max {max(f0s):.0f} Hz"
          f"  →  DẢI {max(f0s)-min(f0s):.0f} Hz   std {np.std(f0s):.1f}")
    by = defaultdict(list)
    for x in rs:
        if x["f0"]:
            by[emo.get(x["id"], "?")].append((x["f0"], x["id"], x["cer"]))
    for e in sorted(by):
        v = [a for a, _, _ in by[e]]
        cs = [c2 for _, _, c2 in by[e]]
        print(f"     {e:11s} n={len(v):2d}  F0 tb {np.mean(v):6.1f} Hz  (min {min(v):.0f} max {max(v):.0f})"
              f"  CER tb {100*np.mean(cs):4.1f}%")

print("\n" + "=" * 104)
print("CAU CER 100% / BANG RONG — kiem tra raw ASR")
print("=" * 104)
for c, rs in groups.items():
    for x in rs:
        if x["cer"] >= 0.99 or not x["hyp"].strip():
            tag = f"p2_{x['id'].replace('.', '_').replace('#', '-')}"
            cands = [f for f in OUT.glob(f"asr_*_{tag}.json")]
            raw = json.loads(cands[0].read_text(encoding="utf-8")) if cands else {}
            print(f"\n{c} · {x['id']}  ({emo.get(x['id'])})")
            print(f"   CHUAN: {x['ref'][:120]}")
            print(f"   RAW  : {json.dumps(raw, ensure_ascii=False)[:260]}")

print("\n" + "=" * 104)
print("XEP HANG SAU KHI LOAI CAU RONG (cong bang hon)")
print("=" * 104)
res = []
for c, rs in groups.items():
    good = [x for x in rs if x["hyp"].strip()]
    cs = sorted(x["cer"] for x in good)
    f0s = [x["f0"] for x in good if x["f0"]]
    res.append((sum(cs) / len(cs), c, len(good), len(rs), cs[-1],
                sum(1 for x in cs if x > 0.02), sorted(f0s)[len(f0s) // 2],
                max(f0s) - min(f0s)))
res.sort()
print(f"{'voice_id':38s} {'n':>6s} {'CER tb':>8s} {'max':>7s} {'>2%':>6s} {'F0 med':>8s} {'F0 range':>9s}")
for mean, c, ng, nt, mx, over, f0m, rng in res:
    tag = f"({ng}/{nt} valid)" if ng != nt else ""
    print(f"{c:38s} {ng:6d} {100*mean:7.1f}% {100*mx:6.1f}% {over:4d}/{ng} {f0m:7.0f}Hz {rng:7.0f}Hz {tag}")
