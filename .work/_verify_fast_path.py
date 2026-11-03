"""Kiem chung duong 'khoi tao lazy' cua finishing toi uu trong chinh _build_video3_split.py.

Render cung 1 frame bang ban goc (truoc khi patch) va bang ban da patch
(voi duong khoi tao moi) -> so sanh byte.
"""
import importlib
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

os.environ.setdefault("AE_EP", "06")
os.environ.setdefault("AE_FAST_FINISH", "1")
os.environ.setdefault("AE_PIPE_BUF", "4194304")
os.environ.setdefault("AE_VID", ".work/_verify_fast")

import build_video3 as B  # noqa: E402

ORIG_FIN = B.finishing
ORIG_RENDER = B.render

# 1) render bang ban GOC truoc khi patch
ref = {}
for fi in (0, 30, 1500, 9000, 20000, 37750):
    ref[fi] = ORIG_RENDER(fi).convert("RGB").tobytes()

# 2) nap lai module split (patch finishing) -> phai cho module moi
for m in ("_build_video3_split",):
    sys.modules.pop(m, None)
import _build_video3_split  # noqa: E402,F401

bad = []
for fi, want in ref.items():
    got = B.render(fi).convert("RGB").tobytes()
    if got != want:
        bad.append(fi)
    print(f"  fi={fi}: len={len(got)} {'OK' if got == want else 'MISMATCH'}")
if bad:
    raise SystemExit(f"CHẶN - frame lech o {bad}")
print("OK  render sau khi patch finishing == render ban goc (byte-for-byte)")
