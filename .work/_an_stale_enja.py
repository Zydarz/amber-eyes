#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ảnh tĩnh EN/JA đã cũ so với renderer HIỆN TẠI chưa?

Cách đo KHÔNG phá: render thử vào thư mục tạm rồi so hash với bộ đang có.
"""
import hashlib
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
TMP = WORK / "_stale_check"
TMP.mkdir(exist_ok=True)


def sha(p: Path):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def plan_rows(plan: Path):
    import re
    txt = plan.read_text(encoding="utf-8")
    m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", txt, re.M)
    sec = txt[m.end():]
    t = re.search(r"^\*\*Tổng:", sec, re.M)
    if t:
        sec = sec[: t.start()]
    out = {}
    for line in sec.splitlines():
        if re.match(r"\|\s*\d-\d+", line):
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            out[c[0]] = c[3]
    return out


def check(lang, folder, plan):
    env = dict(os.environ, AE_EP="03", AE_LANG=lang, PYTHONIOENCODING="utf-8")
    rows = plan_rows(ROOT / "02_SAN_XUAT" / plan)
    # các shot dùng mẫu T2 (hạt nhiễu nền đổi theo seed) + shot 1-00 (khung intro)
    targets = sorted([k for k, v in rows.items() if v.split()[0] == "T2"] + ["1-00"])
    dst = ROOT / ".work" / folder / "stills"
    print(f"\n=== {lang} — {len(targets)} shot nghi vấn (T2 + 1-00) ===")
    # render vào thư mục tạm: copy script dựng, trỏ output
    src_out = dst
    bak = WORK / f"_stills_bak_{lang}"
    if not bak.exists():
        bak.mkdir()
        for p in dst.glob("shot_*.png"):
            (bak / p.name).write_bytes(p.read_bytes())
    out = subprocess.run(
        [sys.executable, str(WORK / "build_video3.py"), "--stills", ",".join(targets)],
        cwd=ROOT, env=env, capture_output=True, text=True, encoding="utf-8", errors="replace")
    changed, same = [], []
    for sid in targets:
        p = dst / f"shot_{sid}.png"
        b = bak / f"shot_{sid}.png"
        if not p.exists() or not b.exists():
            continue
        (changed if sha(p) != sha(b) else same).append(sid)
    print(f"  KHÁC so với bản đang có (tức đã CŨ): {len(changed)} -> {changed}")
    print(f"  GIỐNG: {len(same)}")
    return changed


check("en", "video3_EN_t03", "Tap03_EN/KeHoach_Video_Tap03_EN.md")
check("ja", "video3_JA_t03", "Tap03_JA/KeHoach_Video_Tap03_JA.md")
