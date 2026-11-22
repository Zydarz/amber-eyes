# -*- coding: utf-8 -*-
"""Doi ten nen trong bang shot + spec: t4_* -> tk04_* (Tap 04 VN/EN/JA).

Vay sao: script dung video doc assets/bg/<nen>.png. Anh nen 16:9 goc cua Tap 04
nam o assets/bg/_raw/t4_*.png (khong ton tai o assets/bg/), con nen DOC 9:16 cho
TikTok nam o assets/bg/tk04_*.png => phai tro toi ten tk04_* (dung quy uoc
Tap 02/tap 03: tk02_/tk03_ trong clip, t2_/t3_ la anh goc).

Chay: py -3 .work/_tk_patch_bgname_t04.py
"""
import io
import json
import os
import re
import shutil
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_src_t04 import PAIRS  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
TIK = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK")
DST = os.path.join(ROOT, "assets/bg")

PLANS = {
    "Tap04": "KE_HOACH_CLIP_TAP04.md",
    "Tap04_EN": "KE_HOACH_CLIP_TAP04_EN.md",
    "Tap04_JA": "KE_HOACH_CLIP_TAP04_JA.md",
}
SPECS = {
    "Tap04": "SPEC_AUDIO_CLIP_TAP04.json",
    "Tap04_EN": "SPEC_AUDIO_CLIP_TAP04.json",
    "Tap04_JA": "SPEC_AUDIO_CLIP_TAP04.json",
}

# chi doi token t4_ -> tk04_, khong vao chuoi da co tk04_
PAT = re.compile(r"(?<!tk)(?<!tk0)\bt4_([a-z0-9_]+)\b")

VALID = {n for n, _ in PAIRS}


def patch_text(txt):
    return PAT.sub(lambda m: "tk04_" + m.group(1), txt)


def main():
    bak = os.path.join(ROOT, ".work/_cu", "tk04_bgname_%s" % time.strftime("%Y%m%d_%H%M"))
    ok = True
    for d, fn in PLANS.items():
        src = os.path.join(TIK, d, fn)
        shutil.copy2(src, os.path.join(bak, d + "__" + fn) if os.path.isdir(bak)
                     else bak) if False else None
    os.makedirs(bak, exist_ok=True)
    for d, fn in PLANS.items():
        src = os.path.join(TIK, d, fn)
        shutil.copy2(src, os.path.join(bak, "%s__%s" % (d, fn)))
    for d, fn in SPECS.items():
        src = os.path.join(TIK, d, fn)
        shutil.copy2(src, os.path.join(bak, "%s__%s" % (d, fn)))

    # --- 1. ke hoach ---
    for d, fn in PLANS.items():
        p = os.path.join(TIK, d, fn)
        txt = io.open(p, encoding="utf-8").read()
        before = len(PAT.findall(txt))
        new = patch_text(txt)
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        left = len(PAT.findall(new))
        print("ke hoach %-10s doi %d token · con lai t4_: %d" % (d, before, left))
        if left:
            ok = False

    # --- 2. spec ---
    for d, fn in SPECS.items():
        p = os.path.join(TIK, d, fn)
        txt = io.open(p, encoding="utf-8-sig").read()
        before = len(PAT.findall(txt))
        new = patch_text(txt)
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        left = len(PAT.findall(new))
        print("spec    %-10s doi %d token · con lai t4_: %d" % (d, before, left))
        if left:
            ok = False

    # --- 3. kiem chung: moi token tk04_ deu co file that ---
    print("\n=== KIEM CHUNG ===")
    for d, fn in list(PLANS.items()) + list(SPECS.items()):
        p = os.path.join(TIK, d, fn)
        txt = io.open(p, encoding="utf-8-sig").read()
        toks = set(re.findall(r"tk04_[a-z0-9_]+", txt))
        miss = [t for t in toks if not os.path.exists(os.path.join(DST, t + ".png"))]
        unknown = [t for t in toks if t not in VALID]
        print("%-28s token=%2d · thieu file=%s · ngoai danh sach=%s"
              % (d + "/" + fn, len(toks), miss if miss else "khong co",
                 unknown if unknown else "khong co"))
        if miss or unknown:
            ok = False

    print("\nbackup: %s" % bak)
    print("KET QUA:", "DAT" if ok else "LOI")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
