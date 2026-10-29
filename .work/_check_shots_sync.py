#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiểm tra bảng shot Tập 02 có đồng bộ với kế hoạch không.

parse_shots.py ghi đè .work/shots_t02.json. Script này:
  1. chép bản đang dùng ra file .bak
  2. chạy lại parse_shots.py
  3. so sánh, in ra phần khác nhau
  4. nếu khác -> trả lại bản cũ (render đang chạy dùng bản cũ)
"""
import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
W = ROOT / ".work"
SHOTS = W / "shots_t02.json"
BAK = W / "shots_t02.json.bak"

os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"

old = json.loads(SHOTS.read_text(encoding="utf-8"))
shutil.copy2(SHOTS, BAK)
r = subprocess.run([sys.executable, str(W / "parse_shots.py")], cwd=str(ROOT),
                   capture_output=True, text=True, encoding="utf-8")
print(r.stdout.strip())
if r.returncode != 0:
    print("parse_shots.py LOI:", r.stderr.strip())
    shutil.copy2(BAK, SHOTS)
    sys.exit(1)

new = json.loads(SHOTS.read_text(encoding="utf-8"))
if old == new:
    print("\n=> IDENTICAL: bang shot trong ke hoach trung voi bang dang dung.")
else:
    print("\n=> KHAC NHAU — chi tiet:")
    sa, sb = old["shots"], new["shots"]
    print(f"   so shot: cu {len(sa)} / moi {len(sb)}")
    for x, y in zip(sa, sb):
        if x != y:
            print(f"   --- {x['id']}")
            for k in x:
                if x[k] != y.get(k):
                    print(f"       {k}:")
                    print(f"          CU : {x[k]!r}")
                    print(f"          MOI: {y.get(k)!r}")
    shutil.copy2(BAK, SHOTS)          # tra lai ban render dang dung
    print("\n   -> da khoi phuc ban cu (render dang chay dung ban cu).")
    sys.exit(1)
