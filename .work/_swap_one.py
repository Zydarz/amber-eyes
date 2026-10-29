#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Doi file moi (co duoi _<guid>) vao ten ma SFX, ban cu chuyen sang _conflict/.

Usage: py -3 .work/_swap_one.py <ma_sfx> [<ma_sfx>...]
"""
import re
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\Audi")
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
CONFLICT = INBOX / "_conflict"
CONFLICT.mkdir(parents=True, exist_ok=True)

PAT = re.compile(r"^(?P<base>.+)_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

for code in sys.argv[1:]:
    target = INBOX / (code + ".mp3")
    found = None
    for folder in (INBOX, CONFLICT):
        for f in folder.glob(code + "_*.mp3"):
            m = PAT.match(f.stem)
            if m and m.group("base") == code:
                found = f
                break
        if found:
            break
    if not found:
        print(f"  {code}: khong tim thay file DUP")
        continue
    if target.exists():
        bak = CONFLICT / (code + "_old.mp3")
        shutil.move(str(target), str(bak))
        print(f"  backup {target.name} -> _conflict\\{bak.name}")
    shutil.move(str(found), str(target))
    print(f"  {code}: {found.name} -> {target.name} ({target.stat().st_size} bytes)")
