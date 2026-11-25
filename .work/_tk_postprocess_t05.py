# -*- coding: utf-8 -*-
"""Hau ky anh nen DOC 9:16 cho clip TikTok Tap 05 (AI that MiniMax).

Tien trinh (00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §4, giong Tap 01-04):
  1. Canh 9:16 (nguon MiniMax 1536x2720 lech ~0,4%) roi LANCZOS 1080x1920
  2. Giam saturation 35% · tang contrast 15%
  3. Noir vignette 45% o 4 goc · hat phim 35mm Gaussian (seed 42)
  4. Toi vung chu hook + phu de cho den khi mean dat nguong VA khong con dong nao
     >70% pixel vuot nguong sang (khong vet ngang) — dung DUNG dai QC 270-730 / 996-1254.

Input : .work/tk_img_raw_t05/tk05_<ten>.jpg
Output: assets/bg/tk05_<ten>.png
Ghi provenance.json (L7) cho tung file. Script chay lai duoc.
"""
import json
import pathlib
import shutil
import sys
import time

import numpy as np
from PIL import Image, ImageEnhance

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_fallback_crop_t04 import (  # noqa: E402
    HOOK_BAND, SUB_BAND, SX0, SX1, TARGET_HOOK, TARGET_SUB, _band_profile,
)
from _tk_src_t05 import PAIRS, PROMPT  # noqa: E402

ROOT = HERE.parent
RAW = HERE / "tk_img_raw_t05"
DST = ROOT / "assets" / "bg"
PROV = ROOT / "provenance.json"

W, H = 1080, 1920
TEXT_HOOK = HOOK_BAND
TEXT_SUB = SUB_BAND
STREAK_TH = 120
STREAK_PCT = 0.70


def _max_streak_frac(gray, y0, y1):
    reg = gray[y0:y1, SX0:SX1]
    if reg.size == 0:
        return 0.0
    return float((reg > STREAK_TH).mean(axis=1).max())


def darken_bands_strict(img):
    arr = np.array(img, dtype=np.float32)
    h = arr.shape[0]
    best = None
    for depth in np.arange(0.0, 0.66, 0.05):
        prof = _band_profile(h, float(depth))
        out = arr * prof[:, None, None]
        g = np.clip(out, 0, 255).astype(np.uint8)
        gm = np.asarray(Image.fromarray(g).convert("L"), dtype=np.float32)
        hook = float(gm[HOOK_BAND[0]:HOOK_BAND[1], SX0:SX1].mean())
        sub = float(gm[SUB_BAND[0]:SUB_BAND[1], SX0:SX1].mean())
        streak = max(_max_streak_frac(gm, *TEXT_HOOK), _max_streak_frac(gm, *TEXT_SUB))
        if hook <= TARGET_HOOK and sub <= TARGET_SUB and streak <= STREAK_PCT:
            best = (Image.fromarray(g), float(depth), hook, sub, streak)
            break
    if best is None:
        depth = 0.60
        prof = _band_profile(h, depth)
        out = np.clip(arr * prof[:, None, None], 0, 255).astype(np.uint8)
        g = np.asarray(Image.fromarray(out).convert("L"), dtype=np.float32)
        hook = float(g[HOOK_BAND[0]:HOOK_BAND[1], SX0:SX1].mean())
        sub = float(g[SUB_BAND[0]:SUB_BAND[1], SX0:SX1].mean())
        streak = max(_max_streak_frac(g, *TEXT_HOOK), _max_streak_frac(g, *TEXT_SUB))
        best = (Image.fromarray(out), depth, hook, sub, streak)
    return best


def noir_grade(img):
    img = ImageEnhance.Color(img).enhance(0.65)
    img = ImageEnhance.Contrast(img).enhance(1.15)
    return img


def vignette_grain(img, seed=42):
    arr = np.array(img, dtype=np.float32)
    h, w, c = arr.shape
    y, x = np.ogrid[:h, :w]
    cx, cy = w / 2, h / 2
    dist = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    max_dist = np.sqrt(cx ** 2 + cy ** 2)
    vig = np.clip(1.0 - 0.45 * (dist / max_dist) ** 1.8, 0.4, 1.0)[:, :, np.newaxis]
    arr = arr * vig
    np.random.seed(seed)
    grain = np.random.normal(0, 7.5, arr.shape)
    return Image.fromarray(np.clip(arr + grain, 0, 255).astype(np.uint8))


def crop_9x16(im):
    sw, sh = im.size
    ratio = W / H
    if abs((sw / sh) - ratio) <= 1e-3:
        return im
    if (sw / sh) > ratio:
        nw = int(round(sh * ratio))
        left = (sw - nw) // 2
        return im.crop((left, 0, left + nw, sh))
    nh = int(round(sw / ratio))
    top = (sh - nh) // 2
    return im.crop((0, top, sw, top + nh))


def main():
    DST.mkdir(parents=True, exist_ok=True)
    raws = sorted(list(RAW.glob("tk05_*.jpg")) + list(RAW.glob("tk05_*.png")))
    if not raws:
        raise SystemExit("khong co anh tho nao trong %s" % RAW)

    bak = HERE / "_cu" / ("tk05_provenance_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROV, bak / "provenance.json")

    ref_of = {n: r for n, r in PAIRS}
    prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    index = {it.get("file"): it for it in items}
    added = updated = 0
    report = []

    for rp in raws:
        name = rp.stem
        src16 = ref_of.get(name, "")
        dst = DST / ("%s.png" % name)
        with Image.open(rp) as im:
            src_size = im.size
            im = im.convert("RGB")
            im = crop_9x16(im)
            if im.size != (W, H):
                im = im.resize((W, H), Image.Resampling.LANCZOS)
            im = noir_grade(im)
            im = vignette_grain(im)
            im, depth, hook_m, sub_m, streak = darken_bands_strict(im)
            note = "depth=%.2f hook=%.1f sub=%.1f streak=%.2f" % (depth, hook_m, sub_m, streak)
            im.save(dst, "PNG", optimize=True)

        kb = dst.stat().st_size / 1024
        report.append((name, "%dx%d -> %dx%d" % (src_size[0], src_size[1], W, H), kb, note))

        rel = "assets/bg/%s.png" % name
        new_row = {
            "file": rel,
            "loai": "nen 9:16 dung cho clip TikTok Tap 05 (dung chung moi ngon ngu)",
            "cong_cu": ("MiniMax image-generation (mcode-tools connector__matrix__generate_image) - "
                        "dung lai anh nen 16:9 Tap 05 (%s) lam anh tham chieu, aspect_ratio 9:16, area 2K; "
                        "hau ky noir theo 00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §4" % src16),
            "ngay": "2026-11-24",
            "prompt": PROMPT,
            "seed": None,
            "mo_ta": "nen doc 9:16 cho clip TikTok Tap 05 - %s" % name,
            "font": None,
            "dieu_khoan": ("Anh sinh boi mo hinh AI cua MiniMax qua mcode-tools; anh tham chieu la anh nen "
                           "16:9 do chinh kenh san xuat cua Tap 05. Moi dung kinh doanh: tach 1/3 tren va "
                           "1/3 duoi de chu phu de + the chu an toan TikTok (x 120-780, y 240-1260)."),
            "kiem_tra_thuong_mai": ("dat (kich thuoc 1080x1920 dung chuan TikTok; mau noir khop bo nen 16:9 "
                                    "cua Tap 05; moi chu se do them o buoc dung video)"),
        }
        if rel in index:
            row = index[rel]
            was_fallback = not row.get("prompt")
            row.update({k: v for k, v in new_row.items() if k != "file"})
            if was_fallback:
                row["mo_ta"] = ("nen doc 9:16 cho clip TikTok Tap 05 - %s (AI that, thay the ban du phong crop 16:9)"
                                % name)
            updated += 1
        else:
            items.append(new_row)
            index[rel] = new_row
            added += 1

    if isinstance(prov, list):
        out = items
    else:
        out = prov
        for k in ("tai_san", "items"):
            if k in out:
                out[k] = items
    PROV.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    print("%-36s %-26s %8s  %s" % ("nen", "kich thuoc", "KB", "vung chu"))
    for name, size, kb, note in report:
        print("%-36s %-26s %8.0f  %s" % (name, size, kb, note))
    print("\nprovenance: +%d dong · cap nhat %d dong · backup: %s" % (added, updated, bak))

    missing = [n for n, _ in PAIRS if not (DST / ("%s.png" % n)).exists()]
    if missing:
        print("CHUA CO (%d): %s" % (len(missing), ", ".join(missing)))


if __name__ == "__main__":
    main()
