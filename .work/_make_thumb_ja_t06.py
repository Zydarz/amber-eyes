#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 06 JA — sinh thumbnail.png cho bản Nhật.

Gọi TRỰC TIẾP package.thumbnail() (A11 #72: KHÔNG gọi CLI package.py vì CLI
gọi thumbnail() + description() sẽ ghi đè mô tả đã xuất bản).

Dùng:  $env:AE_EP="06"; $env:AE_LANG="ja"; py -3 .work/_make_thumb_ja_t06.py
"""
import hashlib
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
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
print(f"thumb_bg : {ED.EP['thumb_bg']}")
print(f"-> {out.name}  {out.stat().st_size:,} byte")
print(f"   sha256 trước: {before}")
print(f"   sha256 sau  : {after}")
print(f"   {'ĐÃ GHI ĐÈ' if before and before != after else 'TẠO MỚI' if not before else 'KHÔNG ĐỔI'}")
