#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 12 JA — sinh thumbnail.png cho bản Nhật (A11 #72)."""
import hashlib
import os
import sys
from pathlib import Path

os.environ["AE_EP"] = "12"
os.environ["AE_LANG"] = "ja"

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))

import edition as ED          # noqa: E402
import package as P           # noqa: E402

out = ED.OUT_DIR / "thumbnail.png"
before = hashlib.sha256(out.read_bytes()).hexdigest() if out.exists() else None

P.thumbnail()

after = hashlib.sha256(out.read_bytes()).hexdigest()
print(f"OUT_DIR  : {ED.OUT_DIR}")
print(f"thumb    : {ED.EP['thumb']}")
print(f"thumb_bg : {ED.EP.get('thumb_bg')}")
print(f"File     : {out} ({out.stat().st_size:,} bytes)")
print(f"Hash before: {before}")
print(f"Hash after : {after}")
print(f"Changed?   : {before != after}")
