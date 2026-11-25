# -*- coding: utf-8 -*-
"""Sua bang shot + spec Tap 05 (VI/EN/JA):
  (1) doi ten nen t5_* -> tk05_* (quy uoc Tap 02/03/04: tkXX_ la nen DOC, tXX_ la anh 16:9 goc)
  (2) tach TK4 cho dat H22 (nen toi da 5 shot / 37 s): TK4.01#9 -> tk05_narcissistic_throne
      va TK4.01#10 -> tk05_darkened_house_exterior

Chay: py -3 .work/_tk_patch_bgname_t05.py
Backup: .work/_cu/tk05_bgname_<timestamp>/
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
from _tk_src_t05 import PAIRS  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
TIK = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK")
DST = os.path.join(ROOT, "assets/bg")

PLANS = {
    "Tap05": "KE_HOACH_CLIP_TAP05.md",
    "Tap05_EN": "KE_HOACH_CLIP_TAP05_EN.md",
    "Tap05_JA": "KE_HOACH_CLIP_TAP05_JA.md",
}
SPECS = {d: "SPEC_AUDIO_CLIP_TAP05.json" for d in PLANS}

# chi doi token t5_ -> tk05_, khong vao chuoi da co tk05_
PAT = re.compile(r"(?<!tk)(?<!tk0)\bt5_([a-z0-9_]+)\b")

# --- tach TK4 cho H22: shot_id -> nen moi ---
REMAP = {
    "TK4.01#9": "tk05_narcissistic_throne",
    "TK4.01#10": "tk05_darkened_house_exterior",
}

VALID = {n for n, _ in PAIRS}


def patch_text(txt):
    """Doi ten t5_ -> tk05_ va tach nen TK4 (theo cot, khong regex lung tung)."""
    out = []
    for line in txt.split("\n"):
        line = PAT.sub(lambda m: "tk05_" + m.group(1), line)
        # tach TK4: gan nen moi cho 2 shot (theo cot "Nen")
        m = re.match(r"^\|\s*`?(TK4\.01#\d+)`?\s*\|(.*)$", line)
        if m:
            sid = m.group(1)
            if sid in REMAP:
                cells = m.group(2).split("|")
                # cells[0..] = Vai | Emotion | Speed | Nghi | Nen | Motion | ...
                for i, c in enumerate(cells):
                    if "tk05_kerri_rawson_tears" in c:
                        cells[i] = " `" + REMAP[sid] + "` "
                        break
                line = "| `%s` |%s" % (sid, "|".join(cells))
        out.append(line)
    return "\n".join(out)


def main():
    bak = os.path.join(ROOT, ".work/_cu", "tk05_bgname_%s" % time.strftime("%Y%m%d_%H%M"))
    os.makedirs(bak, exist_ok=True)
    for d, fn in PLANS.items():
        shutil.copy2(os.path.join(TIK, d, fn), os.path.join(bak, "%s__%s" % (d, fn)))
    for d, fn in SPECS.items():
        shutil.copy2(os.path.join(TIK, d, fn), os.path.join(bak, "%s__%s" % (d, fn)))

    ok = True

    # --- 1. ke hoach ---
    for d, fn in PLANS.items():
        p = os.path.join(TIK, d, fn)
        txt = io.open(p, encoding="utf-8").read()
        before = len(PAT.findall(txt))
        new = patch_text(txt)
        io.open(p, "w", encoding="utf-8", newline="\n").write(new)
        left = len(PAT.findall(new))
        print("ke hoach %-10s doi %2d token · con lai t5_: %d" % (d, before, left))
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
        print("spec    %-10s doi %2d token · con lai t5_: %d" % (d, before, left))
        if left:
            ok = False

    # --- 3. spec: gan nen moi cho 2 shot TK4 ---
    for d, fn in SPECS.items():
        p = os.path.join(TIK, d, fn)
        data = json.loads(io.open(p, encoding="utf-8-sig").read())
        n = 0
        for ck, c in data["clips"].items():
            for ln in c["lines"]:
                if ln.get("clip_line_id") in REMAP:
                    ln["bg"] = REMAP[ln["clip_line_id"]]
                    n += 1
        io.open(p, "w", encoding="utf-8", newline="\n").write(
            json.dumps(data, ensure_ascii=False, indent=1))
        print("spec    %-10s gan lai %d shot" % (d, n))
        if n != len(REMAP):
            ok = False

    # --- 4. kiem chung ---
    print("\n=== KIEM CHUNG ===")
    for d, fn in list(PLANS.items()) + list(SPECS.items()):
        p = os.path.join(TIK, d, fn)
        txt = io.open(p, encoding="utf-8-sig").read()
        toks = set(re.findall(r"tk05_[a-z0-9_]+", txt))
        miss = [t for t in toks if not os.path.exists(os.path.join(DST, t + ".png"))]
        unknown = [t for t in toks if t not in VALID]
        print("%-30s token=%2d · thieu file=%s · ngoai danh sach=%s"
              % (d + "/" + fn, len(toks), miss if miss else "khong co",
                 unknown if unknown else "khong co"))
        if miss or unknown:
            ok = False

    print("\nbackup: %s" % bak)
    print("KET QUA:", "DAT" if ok else "LOI")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
