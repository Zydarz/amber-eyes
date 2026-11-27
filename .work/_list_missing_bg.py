#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Liệt kê ảnh nền tập 31/32 còn THIẾU file (để chạy lại gen_images_cf_tap3739.py khi hết ngày)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"

for ep in (31, 32):
    jobs = json.loads((ROOT / ".work" / f"bg_jobs_tap{ep:02d}.json").read_text(encoding="utf-8"))
    miss = [j["name"] for j in jobs if not (BG / f"{j['name']}.png").exists()]
    print(f"tap {ep}: {len(jobs) - len(miss)}/{len(jobs)} co file · THIEU {len(miss)}")
    for m in miss:
        print("   -", m)
