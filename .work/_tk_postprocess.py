"""Hau ky anh nen DOC 9:16 cho clip TikTok Tap 01.

Tien trinh (theo 00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §4, doi tuong ung cho
khung doc):
  1. LANCZOS ve 1080x1920 (dung 9:16 cua TikTok)
  2. Giam saturation 35% · tang contrast 15%
  3. Noir vignette 45% o 4 goc · hat phim 35mm Gaussian (seed 42)

Input : .work/tk_img_raw/tk01_<ten>.jpg   (anh goc do connector sinh)
Output: assets/bg/tk01_<ten>.png
Ghi provenance.json (L7) cho tung file.
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
ROOT = HERE.parent
RAW = HERE / "tk_img_raw"
DST = ROOT / "assets" / "bg"
PROV = ROOT / "provenance.json"

W, H = 1080, 1920
NAMES = [
    "interrogation_gypsy", "crowd_house", "brain_desk", "records",
    "pinboard", "doll", "spotlight_deedee", "podcast_desk",
    "wheelchair_room", "cage", "cage_open", "hands",
    "house_night", "clinical", "crowd_away", "two_shadows",
]
MISSING = ["clinical", "crowd_away", "two_shadows"]  # bi chan credit (402) - chua co anh


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

    # L5: sao luu provenance truoc khi ghi
    bak = HERE / "_cu" / ("tk01_provenance_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROV, bak / "provenance.json")
    prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))

    existing = {it.get("file") for it in items}
    added = 0
    report = []

    for name in NAMES:
        raw = RAW / ("tk01_%s.jpg" % name)
        if not raw.exists():
            report.append((name, "THIEU (khong sinh duoc)", 0))
            continue

        dst = DST / ("tk01_%s.png" % name)
        with Image.open(raw) as im:
            src_size = im.size
            im = im.convert("RGB")
            im = im.resize((W, H), Image.Resampling.LANCZOS)
            im = noir_grade(im)
            im = vignette_grain(im)
            im.save(dst, "PNG", optimize=True)

        kb = dst.stat().st_size / 1024
        report.append((name, "%dx%d -> %dx%d" % (src_size[0], src_size[1], W, H), kb))

        rel = "assets/bg/tk01_%s.png" % name
        if rel not in existing:
            items.append({
                "file": rel,
                "loai": "nen 9:16 dung cho clip TikTok (dung chung moi ngon ngu)",
                "cong_cu": ("MiniMax image-generation (mcode-tools connector__matrix__generate_image) - "
                            "dung lai anh nen 16:9 Tap 01 lam anh tham chieu, aspect_ratio 9:16, area 2K; "
                            "hau ky noir theo 00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md §4"),
                "ngay": "2026-11-18",
                "prompt": ("A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, "
                           "bold black ink linework, high contrast psychological chiaroscuro lighting, "
                           "deep pitch-black shadows, cold desaturated grey-blue palette, faded eerie retro colors, "
                           "decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style ... "
                           "Recompose the scene of Picture 1 as a full-bleed vertical 9:16 illustration ... "
                           "keep the upper third and the lower third as quiet, dark, low-contrast shadow areas ... "
                           "no text, no letters, no numbers, no signs, no logos, no watermark"),
                "seed": None,
                "mo_ta": "nen doc 9:16 cho clip TikTok - %s" % name,
                "font": None,
                "dieu_khoan": ("Anh sinh boi mo hinh AI cua MiniMax qua mcode-tools; anh tham chieu la anh nen "
                               "16:9 do chinh kenh san xuat. Moi dung kinh doanh: tach 1/3 tren va 1/3 duoi "
                               "de chu phu de + the chu an toan TikTok (x 120-780, y 240-1260)."),
                "kiem_tra_thuong_mai": ("dat (kich thuoc 1080x1920 dung chuan TikTok; mau noir khop 44 nen 16:9 "
                                        "cua Tap 01; moi chu se do them o buoc dung video)"),
            })
            existing.add(rel)
            added += 1

    # Ghi provenance (giu nguyen format goc)
    if isinstance(prov, list):
        out = items
    else:
        out = prov
        for k in ("tai_san", "items"):
            if k in out:
                out[k] = items
    PROV.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    print("%-22s %-26s %8s" % ("nen", "kich thuoc", "KB"))
    for name, info, kb in report:
        print("%-22s %-26s %8s" % (name, info, ("%.0f" % kb) if isinstance(kb, float) else kb))
    print()
    print("provenance: +%d dong · backup: %s" % (added, bak))


if __name__ == "__main__":
    main()
