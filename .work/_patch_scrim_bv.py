#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vá build_video3.py — lớp tối mềm sau chữ khi nền sáng (H9). T7: chỉ thêm nhánh mới.

QUAN TRONG: file build_video3.py có kết thúc dòng CR CR LF. Đọc/ghi bằng
newline='' để GIỮ NGUYÊN byte các dòng không sửa (git diff chỉ hiện phần thêm).
"""
import pathlib
import py_compile
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
bv = WORK / "build_video3.py"

s = bv.read_text(encoding="utf-8", newline="")
E = "\r\r\n" if "\r\r\n" in s else ("\r\n" if "\r\n" in s else "\n")
print("line ending:", repr(E))


def L(*lines):
    return E.join(lines)


def patch(old, new, tag):
    global s
    if s.count(old) != 1:
        sys.exit("!! %s: khong tim thay DUNG 1 lan (%d)" % (tag, s.count(old)))
    s = s.replace(old, new)
    print("  [ok]", tag)


# 1) ham soft_scrim
patch(
    L("GRAD = None", "DARK70 = None"),
    L(
        "def soft_scrim(x, y0, y1, w, alpha=170, feather=64):",
        '    """Lop toi MEM (vien mo) de chu trang khong bi \'chim\' khi nen sang (H9).',
        "",
        "    Ve bang Pillow (H5) - khong dung AI ve chu.",
        '    """',
        '    mask = Image.new("L", (W, H), 0)',
        "    ImageDraw.Draw(mask).rectangle([x, y0, x + w, y1], fill=alpha)",
        "    mask = mask.filter(ImageFilter.GaussianBlur(feather))",
        '    g = Image.new("RGBA", (W, H), (8, 8, 10, 0))',
        "    g.putalpha(mask)",
        "    return g",
        "",
        "",
        "GRAD = None",
        "DARK70 = None",
    ),
    "soft_scrim()",
)

# 2) T1: giu danh sach img de do vung chu
patch(
    L(
        '    if T in ("T1", None):',
        "        els.append(El(GRAD, 0, 0, st - 10, fade=0, rise=0))",
        "        for t, sg in zip(times, segs):",
    ),
    L(
        '    if T in ("T1", None):',
        "        els.append(El(GRAD, 0, 0, st - 10, fade=0, rise=0))",
        "        seg_imgs = []",
        "        for t, sg in zip(times, segs):",
    ),
    "T1: seg_imgs",
)

# 3) T1: chen lop toi mem sau khi xep khoi chu
patch(
    L(
        "            img = text_block(spec, 1180 if x_left < 200 else 1240)",
        "            # stack segments upward from y=900",
        '            els.append(("stack", t, img))',
        "        els = stack_bottom(els, x_left, 900)",
    ),
    L(
        "            img = text_block(spec, 1180 if x_left < 200 else 1240)",
        "            seg_imgs.append(img)",
        "            # stack segments upward from y=900",
        '            els.append(("stack", t, img))',
        "        els = stack_bottom(els, x_left, 900)",
        '        if shot["id"] in ED.EP.get("text_scrim", []):',
        "            # H9: nen sang o dai chu -> lop toi mem dung khoi chu (Pillow, H5)",
        "            tot = sum(i.height for i in seg_imgs) + 18 * max(0, len(seg_imgs) - 1)",
        "            wid = max((i.width for i in seg_imgs), default=1180)",
        "            els.insert(1, El(soft_scrim(x_left - 30, 900 - tot - 30, 900 + 34, wid + 60),",
        "                             0, 0, st - 10, fade=0, rise=0))",
    ),
    "T1: lop toi mem",
)

# 4) T5 bien 'date': do bề rộng chu thật roi lop toi
patch(
    L(
        '    elif T == "T5":',
        '        els.append(El(DARK70 if shot["variant"] != "date" else GRAD, 0, 0, st - 10, fade=0, rise=0))',
        "        els += t5_number(shot, times, col)",
    ),
    L(
        '    elif T == "T5":',
        '        els.append(El(DARK70 if shot["variant"] != "date" else GRAD, 0, 0, st - 10, fade=0, rise=0))',
        '        if shot["id"] in ED.EP.get("text_scrim", []):',
        "            # H9: nen sang o dai chu -> do bề rộng chu thật roi lop toi mem",
        "            X5 = 560 if bust_visible_at(st + 0.5) else 140",
        "            wmax = 900",
        '            for sg in shot["segments"]:',
        '                for k, v in sg["elems"]:',
        '                    if k == "bold":',
        '                        bb = ImageDraw.Draw(Image.new("L", (4, 4))).textbbox((0, 0), v, font=F_MONO(150))',
        "                        wmax = max(wmax, bb[2] - bb[0])",
        "            els.append(El(soft_scrim(X5 - 30, 360, 800, wmax + 70), 0, 0, st - 10, fade=0, rise=0))",
        "        els += t5_number(shot, times, col)",
    ),
    "T5: lop toi mem",
)

bv.write_text(s, encoding="utf-8", newline="")
py_compile.compile(str(bv), doraise=True)
print("py_compile OK")
raw = bv.read_bytes()
print("CRLF=%d CRCRLF=%d bytes=%d" % (raw.count(b"\r\n"), raw.count(b"\r\r\n"), len(raw)))
