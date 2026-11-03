#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sao luu (L5) cac tep dau vao cua ban EN Tap03 truoc khi sua + kiem tra pipeline
plan -> shots co tai lap duoc khong.

python .work/_backup_en_t03.py [--apply-fix]
"""
import difflib
import json
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
BK = W / "_cu" / "en_t03_fix_20261103"

FILES = {
    "shots_EN_t03.json": W / "shots_EN_t03.json",
    "shots_text_tap03_EN.json": W / "shots_text_tap03_EN.json",
    "KeHoach_Video_Tap03_EN.md": ROOT / "02_SAN_XUAT" / "Tap03_EN" / "KeHoach_Video_Tap03_EN.md",
    "Tap03_EN.srt": ROOT / "02_SAN_XUAT" / "Tap03_EN" / "xuat_ban" / "Tap03_EN.srt",
}

BK.mkdir(parents=True, exist_ok=True)
for name, src in FILES.items():
    dst = BK / (name + ".bak")
    shutil.copy2(src, dst)
    print(f"backup {name} ({src.stat().st_size} B) -> {dst}")

# ---------------------------------------------------------------- tat lap pipeline
print("\n=== kiem tra pipeline plan -> shots (chay lai parse_shots, so sanh) ===")
env = {"AE_EP": "03", "AE_LANG": "en", "PYTHONIOENCODING": "utf-8"}
import os
e = dict(os.environ)
e.update(env)
r = subprocess.run([sys.executable, str(W / "parse_shots.py")], env=e, cwd=str(ROOT),
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print(r.stdout.strip())
if r.returncode != 0:
    print("STDERR:", r.stderr.strip()[-1500:])
    raise SystemExit("parse_shots that bai")

old = json.loads((BK / "shots_EN_t03.json.bak").read_text(encoding="utf-8"))
new = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))
o = {s["id"]: s for s in old["shots"]}
n = {s["id"]: s for s in new["shots"]}
print(f"\nshot: cu={len(o)} moi={len(n)}")
diff_ids = []
for sid in o:
    if o[sid] != n.get(sid):
        diff_ids.append(sid)
print(f"shot khac: {len(diff_ids)} {diff_ids[:20]}")
for sid in diff_ids[:6]:
    for k in n[sid]:
        if o[sid].get(k) != n[sid].get(k):
            print(f"  {sid}.{k}:")
            print(f"    cu  : {json.dumps(o[sid].get(k), ensure_ascii=False)[:200]}")
            print(f"    moi : {json.dumps(n[sid].get(k), ensure_ascii=False)[:200]}")
print("\nTOTAL:", json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["total"])
