# -*- coding: utf-8 -*-
"""Hau ky anh nen DOC 9:16 cho clip TikTok Tap 02.

Tien trinh (tuong ung 00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §4, giong Tap 01):
  1. LANCZOS ve 1080x1920 (dung 9:16 cua TikTok)
  2. Giam saturation 35% · tang contrast 15%
  3. Noir vignette 45% o 4 goc · hat phim 35mm Gaussian (seed 42)

Input : .work/tk_img_raw_t02/tk02_<ten>.jpg   (anh goc do connector sinh)
Output: assets/bg/tk02_<ten>.png
Ghi provenance.json (L7) cho tung file.

Script CHAY LAI DUOC: chi xu ly nhung anh da co trong tk_img_raw_t02/
(bo qua anh chua sinh duoc do het credit) va khong ghi trung dong provenance.
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
# Dung chung ham toi vung chu voi script nen du phong (T22) de 2 bo ve cung nguong.
from _tk_fallback_crop_t02 import (  # noqa: E402
    HOOK_BAND, SUB_BAND, SX0, SX1, TARGET_HOOK, TARGET_SUB, _band_profile, darken_text_bands,
)

# Vung chu THAT cua pipeline video Tap 01 (.work/_build_tk01_video.py)
TEXT_HOOK = (300, 700)     # chu hook (76 px)
TEXT_SUB = (1020, 1230)    # chu phu de (44 px)
STREAK_TH = 120            # nguong "sang"
STREAK_PCT = 0.70          # >70% pixel trong 1 dong vuot nguong = vet ngang


def _max_streak_frac(gray, y0, y1):
    """Ty le lon nhat cua 1 dong nao trong [y0,y1) vuot nguong sang."""
    reg = gray[y0:y1, SX0:SX1]
    if reg.size == 0:
        return 0.0
    return float((reg > STREAK_TH).mean(axis=1).max())


def darken_bands_strict(img):
    """Chon depth toi vung chu sao cho:
       1. mean vung hook <= TARGET_HOOK, mean vung sub <= TARGET_SUB
       2. KHONG con dong nao vuot nguong sang tren >70% chieu rong (vet ngang)
    Tra (img, depth, hook_mean, sub_mean, streak_frac).
    """
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
        ok = (hook <= TARGET_HOOK and sub <= TARGET_SUB and streak <= STREAK_PCT)
        if ok:
            best = (Image.fromarray(g), float(depth), hook, sub, streak)
            break
    if best is None:
        # dat depth toi da: uu tien giu dung nguong mean, chap nhan vet ngang con lai
        depth = 0.60
        prof = _band_profile(h, depth)
        out = np.clip(arr * prof[:, None, None], 0, 255).astype(np.uint8)
        g = np.asarray(Image.fromarray(out).convert("L"), dtype=np.float32)
        hook = float(g[HOOK_BAND[0]:HOOK_BAND[1], SX0:SX1].mean())
        sub = float(g[SUB_BAND[0]:SUB_BAND[1], SX0:SX1].mean())
        streak = max(_max_streak_frac(g, *TEXT_HOOK), _max_streak_frac(g, *TEXT_SUB))
        best = (Image.fromarray(out), depth, hook, sub, streak)
    return best
ROOT = HERE.parent
RAW = HERE / "tk_img_raw_t02"
DST = ROOT / "assets" / "bg"
PROV = ROOT / "provenance.json"

W, H = 1080, 1920

PROMPT_PROV = (
    "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, "
    "bold black ink linework, high contrast psychological chiaroscuro lighting, "
    "deep pitch-black shadows, cold desaturated grey-blue palette, faded eerie retro colors, "
    "decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style ... "
    "Recompose the scene of Picture 1 as a full-bleed vertical 9:16 illustration ... "
    "keep the upper third and the lower third as quiet, dark, low-contrast shadow areas ... "
    "no text, no letters, no numbers, no signs, no logos, no watermark"
)


def noir_grade(img):
    """Giam saturation 35% · tang contrast 15% (dung chuan kenh)."""
    img = ImageEnhance.Color(img).enhance(0.65)
    img = ImageEnhance.Contrast(img).enhance(1.15)
    return img


def vignette_grain(img, seed=42):
    """Vignette 45% o goc · hat phim 35mm (dung chuan kenh)."""
    arr = np.array(img, dtype=np.float32)
    h, w, c = arr.shape
    y, x = np.ogrid[:h, :w]
    cx, cy = w / 2, h / 2
    dist = np.sqrt((x - cx) ** 2 + (y - cy) ** 2)
    max_dist = np.sqrt(cx ** 2 + cy ** 2)
    vig = 1.0 - 0.45 * (dist / max_dist) ** 1.8
    vig = np.clip(vig, 0.4, 1.0)[:, :, np.newaxis]
    arr = arr * vig
    np.random.seed(seed)
    grain = np.random.normal(0, 7.5, arr.shape)
    return Image.fromarray(np.clip(arr + grain, 0, 255).astype(np.uint8))


def main():
    DST.mkdir(parents=True, exist_ok=True)
    raws = sorted(list(RAW.glob("tk02_*.jpg")) + list(RAW.glob("tk02_*.png")))
    if not raws:
        raise SystemExit("khong co anh tho nao trong %s" % RAW)

    # L5: sao luu provenance truoc khi ghi
    bak = HERE / "_cu" / ("tk02_provenance_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROV, bak / "provenance.json")
    # L5: sao luu ca ANH NEN DICH truoc khi ghi de (18 anh du phong se bi thay bang AI that)
    bakimg = HERE / "_cu" / ("tk02_bg_duphong_%s" % time.strftime("%Y%m%d_%H%M"))
    bakimg.mkdir(parents=True, exist_ok=True)
    n_bak = 0
    for rp in raws:
        name = rp.stem[len("tk02_"):]
        d = DST / ("tk02_%s.png" % name)
        if d.exists():
            shutil.copy2(d, bakimg / d.name)
            n_bak += 1
    prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    index = {it.get("file"): it for it in items}
    added = 0
    updated = 0
    report = []

    for rp in raws:
        name = rp.stem[len("tk02_"):]
        src16 = "t2_%s" % name

        dst = DST / ("tk02_%s.png" % name)
        with Image.open(rp) as im:
            src_size = im.size
            im = im.convert("RGB")
            im = im.resize((W, H), Image.Resampling.LANCZOS)
            im = noir_grade(im)
            im = vignette_grain(im)
            # T22: dam bao vung chu hook + phu de du toi (chu trang tren nen sang = mat chu).
            # AI 9:16 KHONG bao dam vung chu toi (vi du tk02_folder_tree sub_mean = 145,6)
            # => chon depth toi khi mean dat nguong VA het vet ngang trong vung chu that.
            im, depth, hook_m, sub_m, streak = darken_bands_strict(im)
            note = "depth=%.2f hook=%.1f sub=%.1f streak=%.2f" % (depth, hook_m, sub_m, streak)
            im.save(dst, "PNG", optimize=True)

        kb = dst.stat().st_size / 1024
        report.append((name, "%dx%d -> %dx%d" % (src_size[0], src_size[1], W, H), kb, note))

        rel = "assets/bg/tk02_%s.png" % name
        new_row = {
            "file": rel,
            "loai": "nen 9:16 dung cho clip TikTok (dung chung moi ngon ngu)",
            "cong_cu": ("MiniMax image-generation (mcode-tools connector__matrix__generate_image) - "
                        "dung lai anh nen 16:9 Tap 02 (%s) lam anh tham chieu, aspect_ratio 9:16, area 2K; "
                        "hau ky noir theo 00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §4" % src16),
            "ngay": "2026-11-20",
            "prompt": PROMPT_PROV,
            "seed": None,
            "mo_ta": "nen doc 9:16 cho clip TikTok Tap 02 - %s" % name,
            "font": None,
            "dieu_khoan": ("Anh sinh boi mo hinh AI cua MiniMax qua mcode-tools; anh tham chieu la anh nen "
                           "16:9 do chinh kenh san xuat cua Tap 02. Moi dung kinh doanh: tach 1/3 tren va 1/3 duoi "
                           "de chu phu de + the chu an toan TikTok (x 120-780, y 240-1260)."),
            "kiem_tra_thuong_mai": ("dat (kich thuoc 1080x1920 dung chuan TikTok; mau noir khop 44 nen 16:9 "
                                    "cua Tap 02; moi chu se do them o buoc dung video)"),
        }
        if rel in index:
            # cap nhat dong dang co (truoc do la ban DU PHONG crop 16:9) -> bay la AI that
            row = index[rel]
            was_fallback = not row.get("prompt")
            row.update({k: v for k, v in new_row.items() if k != "file"})
            if was_fallback:
                row["mo_ta"] = "nen doc 9:16 cho clip TikTok Tap 02 - %s (AI that, thay the ban du phong crop 16:9)" % name
                row["kiem_tra_thuong_mai"] = (
                    "dat (AI that sinh 20/11/2026 thay cho ban du phong crop 16:9; kich thuoc 1080x1920 dung "
                    "chuan TikTok; mau noir khop 44 nen 16:9 cua Tap 02)")
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

    print("%-24s %-26s %8s  %s" % ("nen", "kich thuoc", "KB", "vung chu"))
    for name, info, kb, note in report:
        print("%-24s %-26s %8.0f  %s" % (name, info, kb, note))
    print()
    print("provenance: +%d dong · cap nhat %d dong · backup: %s" % (added, updated, bak))
    print("anh nen dich da backup: %d file -> %s" % (n_bak, bakimg))

    # anh con thieu
    reqs = []
    for rp in sorted(HERE.glob("_tk_img_req_t02_b*.json")):
        reqs += json.loads(rp.read_text(encoding="utf-8-sig"))["requests"]
    missing = [r["output_file"] for r in reqs if not (DST / ("%s.png" % r["output_file"])).exists()]
    if missing:
        print("CHUA CO (%d): %s" % (len(missing), ", ".join(missing)))


if __name__ == "__main__":
    main()
