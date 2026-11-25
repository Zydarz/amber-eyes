# -*- coding: utf-8 -*-
"""DU PHONG: tao nen DOC 9:16 bang cach CAT anh nen 16:9 goc cua Tap 05.

LY DO: allowance MiniMax con het (lo 402) => khong dung duoc pipeline AI-that.
Cat thang tu anh 16:9 goc (assets/bg/_raw/t5_*) — KHONG TON CREDIT.

KHAC BIET VOI nen AI that:
  - Anh goc 16:9 DA qua grade noir cua kenh => KHONG ap lai grade (bi toi qua).
    Chi ap: crop vung noi dung (bo vien/letterbox) + LANCZOS 1080x1920
    + nen toi 1/3 tren + 1/3 duoi cho CHU AN TOAN TikTok.
  - Bai du phong duoc danh dau rieng trong provenance.json (prompt: null).

Input : assets/bg/_raw/t5_*
Output: assets/bg/tk05_<ten>.png  (1080x1920)
"""
import json
import pathlib
import shutil
import sys
import time

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from _tk_src_t05 import PAIRS  # noqa: E402

ROOT = HERE.parent
RAW = ROOT / "assets" / "bg" / "_raw"
DST = ROOT / "assets" / "bg"
PROV = ROOT / "provenance.json"

W, H = 1080, 1920
HOOK_BAND = (270, 730)
SUB_BAND = (996, 1254)
SX0, SX1 = 120, 780
TARGET_HOOK = 58.0
TARGET_SUB = 72.0


def content_box(gray):
    h, w = gray.shape
    rows = np.where(gray.max(axis=1) > 30)[0]
    cols = np.where(gray.max(axis=0) > 30)[0]
    t = int(rows[0]) if len(rows) else 0
    b = int(rows[-1]) + 1 if len(rows) else h
    l = int(cols[0]) if len(cols) else 0
    r = int(cols[-1]) + 1 if len(cols) else w
    return t, b, l, r


def best_window(gray, box):
    """Chon cua so 9:16 trong vung noi dung co NANG LUONG NET VE cao nhat."""
    t, b, l, r = box
    crop = gray[t:b, l:r]
    ch, cw = crop.shape
    win_w = int(round(ch * 9 / 16))
    if win_w >= cw:
        return l, r
    gx = np.abs(np.diff(crop.astype(np.float32), axis=1))
    col_e = gx.mean(axis=0)
    k = max(1, win_w // 6)
    sm = np.convolve(col_e, np.ones(k) / k, mode="same")
    csum = np.concatenate([[0.0], np.cumsum(sm)])
    scores = csum[win_w:] - csum[:-win_w]
    max_le = int((cw - win_w) * 0.22)
    centre = (cw - win_w) / 2.0
    limit = np.abs(np.arange(len(scores)) - centre) <= max_le
    if not limit.any():
        limit = np.ones(len(scores), dtype=bool)
    idx = int(np.argmax(np.where(limit, scores, -1)))
    return l + idx, l + idx + win_w


def _bump(y, a, y0, y1, b):
    v = np.zeros_like(y)
    up = (y >= a) & (y < y0)
    dn = (y >= y1) & (y <= b)
    mid = (y >= y0) & (y < y1)
    if up.any():
        t = (y[up] - a) / max(1e-6, (y0 - a))
        v[up] = t * t * (3.0 - 2.0 * t)
    v[mid] = 1.0
    if dn.any():
        t = (y[dn] - y1) / max(1e-6, (b - y1))
        v[dn] = 1.0 - (t * t * (3.0 - 2.0 * t))
    return v


def safe_text_zone(img):
    """Toi 1/3 tren + 1/3 duoi (profile LIEN TUC smoothstep — tranh vet ngang)."""
    arr = np.array(img, dtype=np.float32)
    h = arr.shape[0]
    y = np.arange(h, dtype=np.float32)
    ctrl = [(0.00, 0.50), (0.12, 0.62), (0.33, 1.00),
            (0.67, 1.00), (0.88, 0.62), (1.00, 0.50)]
    xs = np.array([c[0] for c in ctrl], dtype=np.float32) * h
    ys = np.array([c[1] for c in ctrl], dtype=np.float32)
    prof = np.interp(y, xs, ys)
    for i in range(len(xs) - 1):
        a, b = int(xs[i]), int(xs[i + 1])
        if b <= a:
            continue
        t = (y[a:b] - a) / (b - a)
        s = t * t * (3.0 - 2.0 * t)
        prof[a:b] = ys[i] + (ys[i + 1] - ys[i]) * s
    arr = arr * prof[:, None, None]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


def _band_profile(h, depth):
    y = np.arange(h, dtype=np.float32)
    prof = np.ones(h, dtype=np.float32)
    for (y0, y1) in (HOOK_BAND, SUB_BAND):
        m = 70.0
        prof *= (1.0 - depth * _bump(y, y0 - m, y0, y1, y1 + m))
    return prof


def darken_text_bands(img):
    """Toi vung chu hook + phu de cho den khi dat nguong. DO BANG GRAYSCALE (L) — cung cach QC do."""
    arr = np.array(img, dtype=np.float32)
    h = arr.shape[0]
    depth = 0.0
    hook = sub = 0.0
    for depth in np.arange(0.0, 0.91, 0.05):
        prof = _band_profile(h, depth)
        out = np.clip(arr * prof[:, None, None], 0, 255).astype(np.uint8)
        gm = np.asarray(Image.fromarray(out).convert("L"), dtype=np.float32)
        hook = float(gm[HOOK_BAND[0]:HOOK_BAND[1], SX0:SX1].mean())
        sub = float(gm[SUB_BAND[0]:SUB_BAND[1], SX0:SX1].mean())
        if hook <= TARGET_HOOK and sub <= TARGET_SUB:
            break
    out = np.clip(arr * _band_profile(h, depth)[:, None, None], 0, 255).astype(np.uint8)
    return Image.fromarray(out), round(float(depth), 2), round(float(hook), 1), round(float(sub), 1)


def main():
    DST.mkdir(parents=True, exist_ok=True)
    bak = HERE / "_cu" / ("tk05_fallback_prov_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROV, bak / "provenance.json")

    prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    by_file = {it.get("file"): it for it in items}

    made, skipped, missing = [], [], []
    for name, ref in PAIRS:
        dst = DST / ("%s.png" % name)
        rel = "assets/bg/%s.png" % name
        if dst.exists():
            entry = by_file.get(rel) or {}
            if entry.get("prompt"):          # ban AI that -> giu nguyen
                skipped.append(name)
                continue
            img_bak = HERE / "_cu" / ("tk05_fallback_img_%s" % time.strftime("%Y%m%d_%H%M"))
            img_bak.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dst, img_bak / dst.name)

        src = RAW / ref
        if not src.exists():
            missing.append(ref)
            print("  THIEU NGUON: %s" % ref)
            continue

        with Image.open(src) as im:
            im = im.convert("RGB")
            gray = np.array(im.convert("L"))
            t, b, l, r = content_box(gray)
            wl, wr = best_window(gray, (t, b, l, r))
            ct, cb = max(0, t), min(gray.shape[0], b)
            sub_img = im.crop((wl, ct, wr, cb))
            sw, sh = sub_img.size
            if sw * 16 // 9 < sh:
                sh2 = sw * 16 // 9
                sub_img = sub_img.crop((0, (sh - sh2) // 2, sw, (sh - sh2) // 2 + sh2))
            else:
                sw2 = sh * 9 // 16
                sub_img = sub_img.crop(((sw - sw2) // 2, 0, (sw - sw2) // 2 + sw2, sh))
            out = sub_img.resize((W, H), Image.Resampling.LANCZOS)
            out = safe_text_zone(out)
            out, depth, hook, sub_m = darken_text_bands(out)
            out.save(dst, "PNG", optimize=True)

        made.append((name, ref, dst.stat().st_size / 1024, depth, hook, sub_m))
        print("  %-34s <- %-38s %7.0f KB  depth=%.2f hook=%.1f sub=%.1f"
              % (name, ref, dst.stat().st_size / 1024, depth, hook, sub_m))

        if rel not in by_file:
            items.append({
                "file": rel,
                "loai": "nen 9:16 dung cho clip TikTok Tap 05 (dung chung moi ngon ngu)",
                "cong_cu": ("DU PHONG - cat anh nen 16:9 goc cua Tap 05 (%s) bang LANCZOS + nen toi vung chu; "
                            "KHONG dung mo hinh AI (bi chan 402 het allowance khi sinh nen doc AI)" % ref),
                "ngay": "2026-11-24",
                "prompt": None,
                "seed": None,
                "mo_ta": "nen doc 9:16 DU PHONG cho clip TikTok Tap 05 - %s" % name,
                "font": None,
                "dieu_khoan": ("Anh goc do chinh kenh san xuat (assets/bg/_raw/%s), da qua grade noir cua kenh; "
                               "ban nay la ban CAT 9:16 de dung tam thoi. Phai thay bang ban AI doc 9:16 "
                               "(connector__matrix__generate_image) khi co credit. Moi dung kinh doanh: 1/3 tren "
                               "+ 1/3 duoi da toi de chu phu de + the chu an toan TikTok (x 120-780, y 240-1260)." % ref),
                "kiem_tra_thuong_mai": ("dat (kich thuoc 1080x1920 dung chuan TikTok; mau noir dung bo cua Tap 05; "
                                        "moi chu se do them o buoc dung video)"),
            })
            by_file[rel] = items[-1]

    if isinstance(prov, list):
        out = items
    else:
        out = prov
        for k in ("tai_san", "items"):
            if k in out:
                out[k] = items
    PROV.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    print("\ntao %d nen du phong · giu nguyen %d (AI that) · thieu nguon %d"
          % (len(made), len(skipped), len(missing)))


if __name__ == "__main__":
    main()
