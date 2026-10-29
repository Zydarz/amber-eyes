#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sua file DUP (co duoi _<guid>) ve ten ma SFX dung, day ban cu sang _conflict/."""
import shutil
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\Audi")
INBOX = ROOT / "02_SAN_XUAT" / "sfx_youtube"
CONFLICT = INBOX / "_conflict"
CONFLICT.mkdir(parents=True, exist_ok=True)

GUID = "__H8X9__"
import re
PAT = re.compile(r"^(?P<base>.+)_[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")

dups = []
for f in sorted(INBOX.glob("*.mp3")):
    m = PAT.match(f.stem)
    if m:
        dups.append((f, m.group("base")))

if not dups:
    print("khong co file DUP nao")
for f, base in dups:
    target = INBOX / (base + ".mp3")
    if target.exists():
        bak = CONFLICT / (base + "_old.mp3")
        shutil.move(str(target), str(bak))
        print(f"  backup {target.name} -> _conflict\\{bak.name}")
    shutil.move(str(f), str(target))
    print(f"  DUP fix: {f.name} -> {target.name}")
