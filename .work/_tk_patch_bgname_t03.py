# -*- coding: utf-8 -*-
"""Doi ten nen trong clip TikTok Tap 03: t3_* (anh 16:9) -> tk03_* (anh doc 9:16).

LY DO: script dung video doc assets/bg/<nen>.png. Tap 02 dung tk02_* nen
dung. Tap 03 con tro toi t3_* => se crash "THIEU NEN assets/bg/t3_*.png".

Sua 3 noi (de sinh lai khong pha):
  1. .work/_build_tk_tap03.py + _build_tk_tap03_multilang.py  (nguon sinh .md + .json)
  2. 02_SAN_XUAT/TIKTOK/Tap03{,_EN,_JA}/SPEC_AUDIO_CLIP_TAP03.json
  3. 02_SAN_XUAT/TIKTOK/Tap03{,_EN,_JA}/KE_HOACH_CLIP_TAP03*.md  (bang shot)
Backup truoc khi sua (L5).
"""
import io
import json
import os
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:/TEST/Gax/amber-eyes"
WORK = os.path.join(ROOT, ".work")
BACKUP = os.path.join(WORK, "_cu", "tk03_bgname_%s" % time.strftime("%Y%m%d_%H%M"))

# --- 1. generator .py -------------------------------------------------------
GEN = [os.path.join(WORK, "_build_tk_tap03.py"),
       os.path.join(WORK, "_build_tk_tap03_multilang.py")]

# bg trong tuple:  ,"t3_xxx","still",
TUPLE = re.compile(r'"(t3_[a-z0-9_]+)"(\s*,\s*"(?:still|pan|push|pull)")')
# NEN_SRC:  "t3_xxx": "t3_xxx",
MAP = re.compile(r'"(t3_[a-z0-9_]+)"(\s*:\s*")t3_[a-z0-9_]+(")')

# --- 2. spec json ----------------------------------------------------------
SPECS = []
for lang in ("", "_EN", "_JA"):
    SPECS.append(os.path.join(ROOT, "02_SAN_XUAT/TIKTOK", "Tap03" + lang,
                               "SPEC_AUDIO_CLIP_TAP03%s.json" % lang))

# --- 3. plan md -------------------------------------------------------------
MDS = []
for lang in ("", "_EN", "_JA"):
    p = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK", "Tap03" + lang,
                     "KE_HOACH_CLIP_TAP03%s.md" % lang)
    if os.path.exists(p):
        MDS.append(p)

# dong bang shot:  | `TK1.01#1` | `t3_phone_booth` | still | 3.6 s |
ROW = re.compile(r"^(\|\s*`TK\d\.01#\d+`\s*\|\s*`)t3_([a-z0-9_]+)(`\s*\|.*)$", re.M)


def backup(path):
    dst = os.path.join(BACKUP, os.path.relpath(path, ROOT))
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(path, dst)


def main():
    os.makedirs(BACKUP, exist_ok=True)
    total = 0

    for p in GEN:
        if not os.path.exists(p):
            continue
        backup(p)
        s = io.open(p, encoding="utf-8").read()
        s, n1 = TUPLE.subn(r'"tk03_\1"\2', s)
        s, n2 = MAP.subn(r'"tk03_\1"\2t3_\1\3', s)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s)
        print("%-40s tuple=%d  NEN_SRC=%d" % (os.path.basename(p), n1, n2))
        total += n1 + n2

    for p in SPECS:
        if not os.path.exists(p):
            print("KHONG CO", p)
            continue
        backup(p)
        s = io.open(p, encoding="utf-8-sig").read()
        s, n = re.subn(r'("(?:bg|nen|background)"\s*:\s*")t3_([a-z0-9_]+)(")',
                       r"\1tk03_\2\3", s)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s)
        print("%-40s spec=%d" % (os.path.basename(p), n))
        total += n

    for p in MDS:
        backup(p)
        s = io.open(p, encoding="utf-8").read()
        s, n = ROW.subn(r"\1tk03_\2\3", s)
        io.open(p, "w", encoding="utf-8", newline="\n").write(s)
        print("%-40s bang shot=%d" % (os.path.basename(p), n))
        total += n

    print("\nTONG sua: %d choi · backup: %s" % (total, BACKUP))


if __name__ == "__main__":
    main()
