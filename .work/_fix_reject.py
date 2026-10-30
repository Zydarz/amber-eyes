#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cài file .tmp bị collector từ chối vào đúng mã SFX (đổi với file cũ).

Dùng cho các lần tải lại (mã đã 'used' nên collector không khớp).
File nguồn nằm trong 02_SAN_XUAT/sfx_youtube/_reject/*.tmp
"""
import re
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parents[1]
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
REJECT = INBOX / "_reject"
CONFLICT = INBOX / "_conflict"
CONFLICT.mkdir(parents=True, exist_ok=True)

# ma_sfx <-> guid cua file .tmp bi reject (thu tu: beep 34s truoc, lock 31.7s sau)
PLAN = [
    ("fx_computer_beep_restore", "272c7bbc-69d7-471d-8c58-92700bcf84ec"),
    ("fx_metal_lock_open", "118afe77-3be0-49c3-9276-4514e79e2a3f"),
]

PAT = re.compile(r"^(?P<base>.+)_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

for code, guid in PLAN:
    src = REJECT / (guid + ".tmp")
    if not src.exists():
        print("  %s: khong tim thay %s" % (code, src.name))
        continue
    staged = CONFLICT / ("%s_%s.mp3" % (code, guid))
    shutil.move(str(src), str(staged))
    target = INBOX / (code + ".mp3")
    if target.exists():
        bak = CONFLICT / (code + "_old.mp3")
        shutil.move(str(target), str(bak))
        print("  backup %s -> _conflict\\%s" % (target.name, bak.name))
    shutil.move(str(staged), str(target))
    print("  %s: %s (%d bytes)" % (code, target.name, target.stat().st_size))
