# -*- coding: utf-8 -*-
"""Tập 11 — danh sách job lần 2 = 34 file thiếu + 1 file còn sót Real-ESRGAN (t11_obedient_accomplice_strings)."""
import json
from datetime import datetime
from pathlib import Path

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
BG = ROOT / "assets" / "bg"
jobs = json.loads((ROOT / ".work/bg_jobs_tap11_v3.json").read_text(encoding="utf-8"))
by = {j["name"]: j for j in jobs}

missing = [n for n in by if not (BG / f"{n}.png").exists()]

# ảnh tái dùng tên cũ nhưng file trên đĩa vẫn là bản 13/11 (Real-ESRGAN) -> phải sinh lại
stale_reused = []
for n in ["t11_obedient_accomplice_strings", "t11_fragile_beauty_manipulation"]:
    p = BG / f"{n}.png"
    if p.exists():
        d = datetime.fromtimestamp(p.stat().st_mtime).strftime("%Y-%m-%d")
        if d != "2026-11-16":
            stale_reused.append(n)
        else:
            print(f"  {n}: đã sinh lại 16/11 -> OK")

todo = missing + stale_reused
print(f"thiếu: {len(missing)} · sót bản cũ: {stale_reused} → TỔNG {len(todo)}")

out = [by[n] for n in todo]
(ROOT / ".work/bg_jobs_tap11_missing.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print("-> .work/bg_jobs_tap11_missing.json")
