#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vá T04: lớp tối mềm sau chữ khi nền sáng (H9) — T7: chỉ thêm nhánh mới.

1) edition.py: EPISODES["04"]["text_scrim"] = [8 shot nen sang]
2) build_video3.py:
   - them ham soft_scrim() (Pillow, H5)
   - nhanh T1: chen lop toi mem sau GRAD, phu dung khoi chu
   - nhanh T5 (bien "date"): do bề rộng chu thật roi chen lop toi
Khong sua hanh T01/T02: danh sach chi nam trong EPISODES["04"].
"""
import pathlib
import shutil
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BK = WORK / "_cu" / "scrim_t04_20261031"
BK.mkdir(parents=True, exist_ok=True)

SHOTS = ["1-06", "1-10", "1-15", "1-17", "2-08", "4-03", "4-07", "4-13"]

ed = WORK / "edition.py"
bv = WORK / "build_video3.py"
for f in (ed, bv):
    shutil.copy2(f, BK / f.name)
    print("backup ->", BK / f.name)


def patch(path, old, new, tag):
    s = path.read_text(encoding="utf-8")
    if new.split("\n")[0].strip() and new.split("\n")[0] in s and tag in s:
        print("  [skip]", tag, "- da co san")
        return
    if s.count(old) != 1:
        sys.exit("!! %s: khong tim thay DUNG 1 lan (%d): %r" % (path.name, s.count(old), old[:60]))
    path.write_text(s.replace(old, new), encoding="utf-8")
    print("  [ok] ", tag)


# ---------------------------------------------------------------- edition.py
old_ed = '''"thumb_bg": "t4_somerset_exterior",'''
new_ed = '''"thumb_bg": "t4_somerset_exterior",
        # H9: nen sang o dai chu -> them lop toi mem (chi T04; T01/T02 giu nguyen duong cu)
        "text_scrim": %s,''' % repr(SHOTS).replace("'", '"')
patch(ed, old_ed, new_ed, "edition.py: text_scrim")

# ------------------------------------------------------------ build_video3.py
old_helper = '''GRAD = None
DARK70 = None
'''
new_helper = '''def soft_scrim(x, y0, y1, w, alpha=170, feather=64):
    """Lop toi MEM (vien mo) de chu trang khong bi 'chim' khi nen sang (H9).

    Ve bang Pillow (H5) - khong dung AI ve chu.
    """
    mask = Image.new("L", (W, H), 0)
    ImageDraw.Draw(mask).rectangle([x, y0, x + w, y1], fill=alpha)
    mask = mask.filter(ImageFilter.GaussianBlur(feather))
    g = Image.new("RGBA", (W, H), (8, 8, 10, 0))
    g.putalpha(mask)
    return g


GRAD = None
DARK70 = None
'''
patch(bv, old_helper, new_helper, "build_video3.py: soft_scrim()")

old_t1 = '''            img = text_block(spec, 1180 if x_left < 200 else 1240)
            # stack segments upward from y=900
            els.append(("stack", t, img))
        els = stack_bottom(els, x_left, 900)
'''
new_t1 = '''            img = text_block(spec, 1180 if x_left < 200 else 1240)
            seg_imgs.append(img)
            # stack segments upward from y=900
            els.append(("stack", t, img))
        els = stack_bottom(els, x_left, 900)
        if shot["id"] in ED.EP.get("text_scrim", []):
            # H9: nen sang o dai chu -> lop toi mem dung khoi chu (Pillow, H5)
            tot = sum(i.height for i in seg_imgs) + 18 * max(0, len(seg_imgs) - 1)
            wid = max((i.width for i in seg_imgs), default=1180)
            els.insert(1, El(soft_scrim(x_left - 30, 900 - tot - 30, 900 + 34, wid + 60),
                             0, 0, st - 10, fade=0, rise=0))
'''
patch(bv, old_t1, new_t1, "build_video3.py: T1 scrim")

old_t1b = '''    if T in ("T1", None):
        els.append(El(GRAD, 0, 0, st - 10, fade=0, rise=0))
        for t, sg in zip(times, segs):
'''
new_t1b = '''    if T in ("T1", None):
        els.append(El(GRAD, 0, 0, st - 10, fade=0, rise=0))
        seg_imgs = []
        for t, sg in zip(times, segs):
'''
patch(bv, old_t1b, new_t1b, "build_video3.py: seg_imgs")

old_t5 = '''    elif T == "T5":
        els.append(El(DARK70 if shot["variant"] != "date" else GRAD, 0, 0, st - 10, fade=0, rise=0))
        els += t5_number(shot, times, col)
'''
new_t5 = '''    elif T == "T5":
        els.append(El(DARK70 if shot["variant"] != "date" else GRAD, 0, 0, st - 10, fade=0, rise=0))
        if shot["id"] in ED.EP.get("text_scrim", []):
            # H9: nen sang o dai chu -> do bề rộng chu thật roi lop toi mem
            X5 = 560 if bust_visible_at(st + 0.5) else 140
            wmax = 900
            for sg in shot["segments"]:
                for k, v in sg["elems"]:
                    if k == "bold":
                        bb = ImageDraw.Draw(Image.new("L", (4, 4))).textbbox((0, 0), v, font=F_MONO(150))
                        wmax = max(wmax, bb[2] - bb[0])
            els.append(El(soft_scrim(X5 - 30, 360, 800, wmax + 70), 0, 0, st - 10, fade=0, rise=0))
        els += t5_number(shot, times, col)
'''
patch(bv, old_t5, new_t5, "build_video3.py: T5 date scrim")

print("\n--- verify ---")
import py_compile
for f in (ed, bv):
    py_compile.compile(str(f), doraise=True)
    print("py_compile OK:", f.name)
sys.path.insert(0, str(WORK))
import os
os.environ["AE_EP"] = "04"
import edition as ED
scrim = ED.EPISODES["04"].get("text_scrim")
print("EPISODES[04]['text_scrim'] =", scrim)
assert scrim == SHOTS, scrim
print("OK")
