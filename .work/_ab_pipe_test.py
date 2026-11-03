#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""A/B: render cung mot vai shot voi pipe 4 KB (mac dinh) va pipe 4 MB (patch),
roi so byte. Neu giong het -> patch khong doi hinh 1 khung nao.

python .work/_ab_pipe_test.py
"""
import filecmp
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
SD = W / "video3_EN_t03" / "stills"
OUT = W / "_ab_pipe_test"
SHOTS = "1-00,1-01,1-07,2-15,3-03,5-21"

OUT.mkdir(parents=True, exist_ok=True)
for tag in ("A_unpatched", "B_patched"):
    d = OUT / tag
    if d.exists():
        shutil.rmtree(d)
    d.mkdir(parents=True)

env = dict(os.environ)
env.update({"AE_EP": "03", "AE_LANG": "en", "PYTHONIOENCODING": "utf-8"})

runs = [
    ("A_unpatched", [sys.executable, str(W / "build_video3.py"), "--stills", SHOTS]),
    ("B_patched", [sys.executable, str(W / "_render_patched.py"), "--stills", SHOTS]),
]
for tag, cmd in runs:
    print(f"\n=== {tag} ===")
    r = subprocess.run(cmd, env=env, cwd=str(ROOT), capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    print("rc =", r.returncode)
    if r.stderr.strip():
        print("stderr:", r.stderr.strip()[-600:])
    for sid in SHOTS.split(","):
        src = SD / f"shot_{sid}.png"
        if src.exists():
            shutil.copy2(src, OUT / tag / src.name)

print("\n=== so byte ===")
same = diff = 0
for sid in SHOTS.split(","):
    a = OUT / "A_unpatched" / f"shot_{sid}.png"
    b = OUT / "B_patched" / f"shot_{sid}.png"
    if not (a.exists() and b.exists()):
        print(f"  {sid}: THIEU ({a.exists()}/{b.exists()})")
        diff += 1
        continue
    eq = filecmp.cmp(a, b, shallow=False)
    same += eq
    diff += (not eq)
    print(f"  {sid}: {'GIONG' if eq else 'KHAC'}  ({a.stat().st_size} vs {b.stat().st_size} B)")
print(f"\nGIONG {same} · KHAC {diff}")
sys.exit(0 if diff == 0 else 1)
