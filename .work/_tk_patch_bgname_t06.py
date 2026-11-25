# -*- coding: utf-8 -*-
"""Sua bang shot + spec TikTok Tap 06 (VI/EN/JA):
  (1) doi ten nen t6_* -> tk06_* (quy uoc Tap 02/03/04/05: tkXX_ la nen DOC 9:16,
      tXX_ la anh 16:9 goc)
  (2) tach nen cho dat H22 (mot nen toi da 3 shot VA 30 s / clip):
      · TK3 t6_diner_booth_confrontation  (4 shot / 33,7-36,4 s)  -> tach TK3.01#7
      · TK5 t6_redflag_trick_handcuffs     (4 shot / 30,9-35,9 s)  -> tach TK5.01#6+#7
      · t6_psychological_mask_metaphor    (7 shot / 55-77 s ca tap) -> tach 4 shot
      · t6_two_faces_silhouette: khong co anh 16:9 goc -> dung nen moi tu
        t6_four_masks_psychiatric.jpg

Chay: py -3 .work/_tk_patch_bgname_t06.py
Backup: .work/_cu/tk06_bgname_<timestamp>/
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
from _tk_src_t06 import PAIRS  # noqa: E402

ROOT = r"D:/TEST/Gax/amber-eyes"
TIK = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK")
DST = os.path.join(ROOT, "assets/bg")

PLANS = {
    "Tap06": "KE_HOACH_CLIP_TAP06.md",
    "Tap06_EN": "KE_HOACH_CLIP_TAP06_EN.md",
    "Tap06_JA": "KE_HOACH_CLIP_TAP06_JA.md",
}
SPECS = {d: "SPEC_AUDIO_CLIP_TAP06.json" for d in PLANS}

# chi doi token t6_ -> tk06_, khong vao chuoi da co tk06_
PAT = re.compile(r"(?<!tk)(?<!tk0)\bt6_([a-z0-9_]+)\b")
ROW = re.compile(r"^\|\s*`?(TK\d\.01#\d+)`?\s*\|")
CELL_BG = re.compile(r"`?(tk06_[a-z0-9_]+)`?")

# --- tach nen cho H22: shot_id -> nen moi ---
REMAP = {
    "TK1.01#7": "tk06_psychological_mask_twin_silhouette",
    "TK2.01#6": "tk06_psychological_mask_twin_silhouette",
    "TK3.01#8": "tk06_psychological_mask_twin_silhouette",
    "TK3.01#7": "tk06_diner_counter_officers",
    "TK4.01#6": "tk06_compartmentalization_floor_section",
    "TK4.01#7": "tk06_two_faces_silhouette",
    "TK5.01#6": "tk06_handcuff_trick_demonstration",
    "TK5.01#7": "tk06_handcuff_trick_demonstration",
}

VALID = {n for n, _ in PAIRS}


def patch_text(txt):
    """Doi ten t6_ -> tk06_ va tach nen cho H22 (theo cot Nen cua dung shot)."""
    out = []
    for line in PAT.sub(lambda m: "tk06_" + m.group(1), txt).split("\n"):
        m = ROW.match(line)
        if m and m.group(1) in REMAP:
            cells = line.split("|")
            for i, c in enumerate(cells):
                if CELL_BG.search(c):
                    cells[i] = " `%s` " % REMAP[m.group(1)]
                    break
            line = "|".join(cells)
        out.append(line)
    return "\n".join(out)


def main():
    bak = os.path.join(ROOT, ".work/_cu", "tk06_bgname_%s" % time.strftime("%Y%m%d_%H%M"))
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
        print("ke hoach %-10s doi %2d token · con lai t6_: %d" % (d, before, left))
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
        print("spec    %-10s doi %2d token · con lai t6_: %d" % (d, before, left))
        if left:
            ok = False

    # --- 3. spec: gan nen moi cho 8 shot tach ---
    for d, fn in SPECS.items():
        p = os.path.join(TIK, d, fn)
        data = json.loads(io.open(p, encoding="utf-8-sig").read())
        n = 0
        for ck, c in data["clips"].items():
            for ln in c["lines"]:
                sid = ln.get("clip_line_id")
                if sid in REMAP:
                    ln["bg"] = REMAP[sid]
                    n += 1
        io.open(p, "w", encoding="utf-8", newline="\n").write(
            json.dumps(data, ensure_ascii=False, indent=1))
        print("spec    %-10s gan lai %d/%d shot" % (d, n, len(REMAP)))
        if n != len(REMAP):
            ok = False

    # --- 4. kiem chung ---
    print("\n=== KIEM CHUNG ===")
    for d, fn in list(PLANS.items()) + list(SPECS.items()):
        p = os.path.join(TIK, d, fn)
        txt = io.open(p, encoding="utf-8-sig").read()
        toks = set(re.findall(r"tk06_[a-z0-9_]+", txt))
        unknown = [t for t in toks if t not in VALID]
        miss = [t for t in toks if not os.path.exists(os.path.join(DST, t + ".png"))]
        print("%-34s token=%2d · ngoai danh sach=%s · thieu file=%s"
              % (d + "/" + fn, len(toks), unknown if unknown else "khong co",
                 len(miss)))
        if unknown:
            ok = False

    print("\nbackup: %s" % bak)
    print("KET QUA:", "DAT (thieu file la do anh chua sinh)" if ok else "LOI")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
