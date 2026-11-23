# -*- coding: utf-8 -*-
"""QC bộ ảnh nền DỌC 9:16 cho clip TikTok Tập 54.

3 phần trong 1 lần chạy:
  1. ĐO   — kích thước, mean/max vùng hook (y 270-730) & phụ đề (y 996-1254),
            vệt ngang (>70% pixel trong 1 dòng vượt ngưỡng sáng 120).
            Ngưỡng: hook mean ≤ 58 · sub mean ≤ 72 · 0 vệt ngang.
  2. MONTAGE — 3 tờ, ô 384 px (≥384 sau khi resize, cạnh dài ≤ ~1568)
            để SOI MẮT 100 % nền mới (H2/H19).
  3. COVERAGE — 55 shot / 5 clip trong .work/_tk54_shot_table.json:
            nền có file thật, đúng 1080x1920, có dòng provenance,
            H22: 0 nền thừa · 0 shot mượn nền · mỗi nền ≤ 3 shot và ≤ 30 s.
"""
import glob
import json
import os
import sys

import numpy as np
from PIL import Image, ImageDraw, ImageFont

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HOOK = (270, 730)
SUB = (996, 1254)
X0, X1 = 120, 780
THRESH = 120
PCT = 0.70
ROOT = r"D:/TEST/Gax/amber-eyes"
BG = os.path.join(ROOT, "assets/bg")
MONT_DIR = os.path.join(ROOT, ".work/qc_montage")
SHOT_TABLE = os.path.join(ROOT, ".work/_tk54_shot_table.json")
PROV = os.path.join(ROOT, "provenance.json")


def bands(gray):
    out = {}
    for name, (y0, y1) in (("hook", HOOK), ("sub", SUB)):
        reg = gray[y0:y1, X0:X1]
        out[name] = (float(reg.mean()), float(reg.max()))
    return out


def streaks(gray):
    total = 0
    for (y0, y1) in (HOOK, SUB):
        reg = gray[y0:y1, X0:X1]
        frac = (reg > THRESH).mean(axis=1)
        run = best = 0
        for f in frac:
            if f > PCT:
                run += 1
                best = max(best, run)
            else:
                run = 0
        total += best
    return total


def measure():
    files = sorted(glob.glob(os.path.join(BG, "tk54_*.png")))
    print("=== 1. DO KICH THUOC + VUNG CHU (%d anh) ===" % len(files))
    print("%-38s %9s %8s %8s %8s %9s %6s" %
          ("file", "hook_mean", "hook_max", "sub_mean", "sub_max", "size", "ngang"))
    hm = hx = sm = sx = 0.0
    bad, fail, wrongsize = [], [], []
    thumbs = []
    for p in files:
        with Image.open(p) as im:
            size = im.size
            g = np.asarray(im.convert("L"), dtype=np.float32)
            rgb = im.convert("RGB")
        b = bands(g)
        st = streaks(g)
        hm += b["hook"][0]; hx = max(hx, b["hook"][1])
        sm += b["sub"][0]; sx = max(sx, b["sub"][1])
        if st:
            bad.append((os.path.basename(p), st))
        if b["hook"][0] > 58 or b["sub"][0] > 72:
            fail.append((os.path.basename(p), round(b["hook"][0], 1), round(b["sub"][0], 1)))
        if size != (1080, 1920):
            wrongsize.append((os.path.basename(p), size))
        thumbs.append((os.path.basename(p), rgb))
        print("%-38s %9.1f %8.1f %8.1f %8.1f %9s %6d" %
              (os.path.basename(p), b["hook"][0], b["hook"][1], b["sub"][0], b["sub"][1],
               "%dx%d" % size, st))
    n = max(1, len(files))
    print()
    print("TRUNG BINH hook mean %.1f · hook max %.1f · sub mean %.1f · sub max %.1f"
          % (hm / n, hx, sm / n, sx))
    print("anh co vet ngang: %d %s" % (len(bad), bad if bad else ""))
    print("anh vuot nguong vung chu: %d %s" % (len(fail), fail if fail else ""))
    print("anh sai kich thuoc: %d %s" % (len(wrongsize), wrongsize if wrongsize else ""))
    return files, thumbs


def montage(thumbs):
    """3 tờ montage: ô 384 px (cao 682), 4 cột x 4 hàng mỗi tờ."""
    os.makedirs(MONT_DIR, exist_ok=True)
    try:
        font = ImageFont.truetype("arial.ttf", max(14, 384 // 14))
    except Exception:  # noqa: BLE001
        font = ImageFont.load_default()
    COLS, ROWS = 4, 4
    CW = 384
    CH = int(CW * 9 / 16)
    PAD, LAB = 4, 26
    per = COLS * ROWS
    sheets = []
    for si in range(0, len(thumbs), per):
        chunk = thumbs[si:si + per]
        rows = (len(chunk) + COLS - 1) // COLS
        W = COLS * (CW + PAD)
        H = rows * (CH + LAB + PAD)
        sheet = Image.new("RGB", (W, H), (8, 8, 10))
        d = ImageDraw.Draw(sheet)
        for i, (name, rgb) in enumerate(chunk):
            c, r = i % COLS, i // COLS
            x, y = c * (CW + PAD), r * (CH + LAB + PAD)
            sheet.paste(rgb.resize((CW, CH), Image.Resampling.LANCZOS), (x, y))
            d.text((x + 3, y + CH + 4), name[5:-4][:30], font=font, fill=(232, 232, 238))
        out = os.path.join(MONT_DIR, "tk54_bg_sheet%d.jpg" % (si // per + 1))
        sheet.save(out, quality=90)
        sheets.append(out)
        print("  %s  %dx%d  %d anh" % (os.path.relpath(out, ROOT), W, H, len(chunk)))
    return sheets


def coverage():
    print("\n=== 3. COVERAGE 55 SHOT / 5 CLIP + H22 ===")
    table = json.loads(open(SHOT_TABLE, encoding="utf-8").read())
    prov = json.loads(open(PROV, encoding="utf-8-sig").read())
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    by_file = {it.get("file"): it for it in items}

    missing, badsize, noprov = [], [], []
    per_bg = {}
    total_shot = 0
    for clip in sorted(table):
        rows = table[clip]
        ok = 0
        for code, bg, mv, dur in rows:
            total_shot += 1
            p = os.path.join(BG, bg + ".png")
            if not os.path.exists(p):
                missing.append((code, bg))
                continue
            with Image.open(p) as im:
                if im.size != (1080, 1920):
                    badsize.append((bg, im.size))
            if ("assets/bg/%s.png" % bg) not in by_file:
                noprov.append(bg)
            d = per_bg.setdefault(bg, {"n": 0, "s": 0.0, "shots": []})
            d["n"] += 1
            d["s"] += dur
            d["shots"].append(code)
            ok += 1
        print("  %s : %d/%d shot co nen doc" % (clip, ok, len(rows)))

    jobs = json.loads(open(os.path.join(ROOT, ".work/bg_jobs_tk54.json"), encoding="utf-8").read())
    declared = {j["name"] for j in jobs}
    used = set(per_bg)
    unused = sorted(declared - used)
    undeclared = sorted(used - declared)

    print("\n  shot thieu nen:", missing if missing else "KHONG CO")
    print("  nen sai kich thuoc:", badsize if badsize else "KHONG CO")
    print("  thieu dong provenance:", sorted(set(noprov)) if noprov else "KHONG CO")
    print("  nen sinh ra MA KHONG DUNG (H22a):", unused if unused else "KHONG CO")
    print("  nen dung MA KHONG KHAI BAO:", undeclared if undeclared else "KHONG CO")

    print("\n  --- phan bo H22(c): toi da 3 shot / 30 s ---")
    viol = []
    for bg in sorted(per_bg):
        d = per_bg[bg]
        flag = ""
        if d["n"] > 3 or d["s"] > 30:
            flag = "  <<< VI PHAM"
            viol.append(bg)
        if d["n"] > 1:
            print("    %-38s %d shot %6.1f s  %s%s"
                  % (bg, d["n"], d["s"], ",".join(d["shots"]), flag))
    print("    nen dung 1 shot: %d" % sum(1 for v in per_bg.values() if v["n"] == 1))
    print("    VI PHAM H22:", viol if viol else "KHONG CO")
    print("\n  tong: %d shot · %d nen · shot/nen = %.2f"
          % (total_shot, len(used), total_shot / max(1, len(used))))
    return missing, badsize, unused, undeclared, viol


def main():
    files, thumbs = measure()
    print("\n=== 2. MONTAGE SOI MAT 100 %% (H2/H19) ===")
    sheets = montage(thumbs)
    coverage()
    print("\nXong.")


if __name__ == "__main__":
    main()
