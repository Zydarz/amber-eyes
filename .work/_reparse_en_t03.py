#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sau khi sua ke hoach EN Tap03: chay lai parse_shots va chung minh chi 2-15 doi."""
import json
import os
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
BK = W / "_cu" / "en_t03_fix_20261103"

e = dict(os.environ)
e.update({"AE_EP": "03", "AE_LANG": "en", "PYTHONIOENCODING": "utf-8"})
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
diff = [sid for sid in o if o[sid] != n.get(sid)]
print(f"\nshot khac so voi ban luu: {len(diff)} {diff}")
for sid in diff:
    for k in n[sid]:
        if o[sid].get(k) != n[sid].get(k):
            print(f"  {sid}.{k}:")
            print(f"    cu  : {json.dumps(o[sid].get(k), ensure_ascii=False)[:220]}")
            print(f"    moi : {json.dumps(n[sid].get(k), ensure_ascii=False)[:220]}")

ok = diff == ["2-15"]
print("\nKET QUA:", "PASS - chi 2-15 doi" if ok else f"FAIL - doi {diff}")
sys.exit(0 if ok else 1)
