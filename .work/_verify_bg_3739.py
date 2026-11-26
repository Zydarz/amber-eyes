#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra ảnh nền Tập 37/38/39: file tồn tại, PNG mở được, đúng kích thước, đủ số lượng job."""
import json
import sys
from pathlib import Path

from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BG = ROOT / "assets" / "bg"

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

for ep in (37, 38, 39):
    jobs = json.loads((WORK / f"bg_jobs_tap{ep}.json").read_text(encoding="utf-8"))
    names = [j["name"] for j in jobs]
    bad, missing, ok = [], [], 0
    sizes = set()
    for n in names:
        p = BG / f"{n}.png"
        if not p.exists():
            missing.append(n)
            continue
        try:
            with Image.open(p) as im:
                im.verify()
            with Image.open(p) as im:
                sizes.add(im.size)
            ok += 1
        except Exception as e:
            bad.append(f"{n} ({type(e).__name__})")
    extra = [p.stem for p in BG.glob(f"t{ep}_*.png") if p.stem not in set(names)]
    print(f"Tập {ep}: job={len(names)} · file hợp lệ={ok} · thiếu={len(missing)} · hỏng={len(bad)} · thừa={len(extra)}")
    print(f"        kích thước: {sorted(sizes) if sizes else '-'}")
    for b in bad:
        print(f"        HỎNG: {b}")
    for m in missing:
        print(f"        THIẾU: {m}")
    if extra:
        print(f"        THỪA: {extra}")
