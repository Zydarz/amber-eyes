#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Đổi file mới (tên <ma>_<hậu tố bất kỳ>) vào đúng tên mã SFX, file cũ sang _conflict/.

Dùng: py -3 .work/_swap_named.py <ma_sfx> [<ma_sfx>...]
"""
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\Audi")
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
CONFLICT = INBOX / "_conflict"
CONFLICT.mkdir(parents=True, exist_ok=True)

for code in sys.argv[1:]:
    target = INBOX / (code + ".mp3")
    cands = [f for f in list(INBOX.glob(code + "_*")) + list(CONFLICT.glob(code + "_*"))
             if f.is_file() and f.name != code + ".mp3" and not f.name.endswith("_old.mp3")]
    if not cands:
        print("  %s: khong tim thay file moi" % code)
        continue
    src = max(cands, key=lambda p: p.stat().st_mtime)
    if target.exists():
        bak = CONFLICT / (code + "_old.mp3")
        shutil.move(str(target), str(bak))
        print("  backup %s -> _conflict\\%s" % (target.name, bak.name))
    shutil.move(str(src), str(target))
    print("  %s: %s -> %s (%d bytes)" % (code, src.name, target.name, target.stat().st_size))
