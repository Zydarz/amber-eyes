# -*- coding: utf-8 -*-
"""DU PHONG: tao nen DOC 9:16 bang cach CAT anh nen 16:9 goc cua Tap 02.

LY DO: 18/26 nen doc bi chan bang loi 402 (het credit, credit auto-consumption
tat) cua connector__matrix__generate_image. De khong dung pipeline, cat thang
tu anh 16:9 goc (assets/bg/_raw/t2_*) — KHONG TON CREDIT.

KHAC BIET VOI 8 nen AI da sinh:
  - Anh goc 16:9 DA qua grade noir cua kenh (saturation/contrast/vignette/grain).
    => KHONG ap lai grade (se bi toi qua). Chi ap them:
      + viet sang 9:16 (crop vung noi dung, bo letterbox)
      + LANCZOS ve 1080x1920
      + nen toi 1/3 tren + 1/3 duoi cho CHU AN TOAN TikTok
  - Bai du phong duoc danh dau rieng trong provenance.json de biet cai nao
    la AI that, cai nao la du phong (de thay bang ban AI doc khi nap credit).

Input : assets/bg/_raw/t2_*   (anh nen 16:9 goc)
Output: assets/bg/tk02_<ten>.png  (1080x1920)
"""
import json
import pathlib
import shutil
import sys
import time

import numpy as np
from PIL import Image, ImageFilter

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
RAW = ROOT / "assets" / "bg" / "_raw"
DST = ROOT / "assets" / "bg"
PROV = ROOT / "provenance.json"

W, H = 1080, 1920

# 26 nen DOC cua Tap 02 (lay tu .work/_tk_img_req_t02_b*.json — nguon su that)
def all_names():
    names = []
    for rp in sorted(HERE.glob("_tk_img_req_t02_b*.json")):
        for r in json.loads(rp.read_text(encoding="utf-8-sig"))["requests"]:
            if r["output_file"] not in names:
                names.append(r["output_file"])
    return names


def pick_file(base):
    for ext in (".png", ".jpg"):
        p = RAW / (base + ext)
        if p.exists():
            return p
    return None


def content_box(gray):
    """Tra (top, bottom, left, right) cua phan NOI DUNG (bo letterbox den)."""
    h, w = gray.shape
    rows = np.where(gray.max(axis=1) > 30)[0]
    cols = np.where(gray.max(axis=0) > 30)[0]
    t = int(rows[0]) if len(rows) else 0
    b = int(rows[-1]) + 1 if len(rows) else h
    l = int(cols[0]) if len(cols) else 0
    r = int(cols[-1]) + 1 if len(cols) else w
    return t, b, l, r


def best_window(gray, box):
    """Chon cua so 9:16 trong vung noi dung co NANG LUONG NET VE cao nhat.

    Net ve = gradient theo chieu ngang (net ink doc) + bien do cuc bo theo hang.
    Giu cua so gan canh giua (lech toi da 22% chieu rong noi dung) de khong
    lech chu the khoi khung.
    """
    t, b, l, r = box
    crop = gray[t:b, l:r]
    ch, cw = crop.shape
    win_w = int(round(ch * 9 / 16))
    if win_w >= cw:                      # vung noi dung hep hon 9:16 -> dung het
        return l, r
    # energy theo cot
    gx = np.abs(np.diff(crop.astype(np.float32), axis=1))
    col_e = gx.mean(axis=0)
    # cum nang luong (smooth) de chon vung lien mach
    k = max(1, win_w // 6)
    ker = np.ones(k) / k
    sm = np.convolve(col_e, ker, mode="same")
    csum = np.concatenate([[0.0], np.cumsum(sm)])
    scores = csum[win_w:] - csum[:-win_w]        # energy cua moi cua so
    max_le = int((cw - win_w) * 0.22)
    centre = (cw - win_w) / 2.0
    limit = np.abs(np.arange(len(scores)) - centre) <= max_le
    if not limit.any():
        limit = np.ones(len(scores), dtype=bool)
    idx = int(np.argmax(np.where(limit, scores, -1)))
    return l + idx, l + idx + win_w


def safe_text_zone(img):
    """Toi them 1/3 tren + 1/3 duoi de chu phu de + the chu an toan TikTok.

    Profile PHAI LIEN TUC (smoothstep) — dung `min`/`linspace` se tao VET NGANG
    nhay gia tri ngay tai ranh giori 1/3 va 2/3, nhin loang loang tren video.
    """
    arr = np.array(img, dtype=np.float32)
    h = arr.shape[0]
    y = np.arange(h, dtype=np.float32)

    # moc dieu khien: (vị trí tương đối, độ sáng)
    ctrl = [(0.00, 0.50), (0.12, 0.62), (0.33, 1.00),
            (0.67, 1.00), (0.88, 0.62), (1.00, 0.50)]
    xs = np.array([c[0] for c in ctrl], dtype=np.float32) * h
    ys = np.array([c[1] for c in ctrl], dtype=np.float32)
    prof = np.interp(y, xs, ys)
    # smoothstep giua cac moc de khong co goc/khong gian
    for i in range(len(xs) - 1):
        a, b = int(xs[i]), int(xs[i + 1])
        if b <= a:
            continue
        t = (y[a:b] - a) / (b - a)
        s = t * t * (3.0 - 2.0 * t)
        prof[a:b] = ys[i] + (ys[i + 1] - ys[i]) * s
    arr = arr * prof[:, None, None]
    return Image.fromarray(np.clip(arr, 0, 255).astype(np.uint8))


# ---- vung chu that cua pipeline Tap 01 (.work/_build_tk01_video.py) ----
HOOK_BAND = (270, 730)        # chu hook (lon nhat)
SUB_BAND = (996, 1254)        # chu phu de
SX0, SX1 = 120, 780           # vung chu an toan TikTok
TARGET_HOOK = 58.0            # mean vung hook sau toi (bo tk01 = 41.6, AI tk02 = 34.0)
TARGET_SUB = 72.0             # mean vung sub sau toi (bo tk01 = 82.1)


def _band_profile(h, depth):
    """Profile toi 2 dai chu (hook + sub), bien mem 70 px -> khong vet ngang."""
    y = np.arange(h, dtype=np.float32)
    prof = np.ones(h, dtype=np.float32)
    for (y0, y1) in (HOOK_BAND, SUB_BAND):
        m = 70.0
        a, b = y0 - m, y1 + m
        prof *= (1.0 - depth * _bump(y, a, y0, y1, b))
    return prof


def _bump(y, a, y0, y1, b):
    """1.0 trong [y0,y1], giam tan dan ve 0 o [a,y0] va [y1,b] (smoothstep).

    QUAN TRONG: hai dau phai LIEN TUC voi vung giua — neu up dung `1 - smoothstep`
    thi tai y0 gia tri nhay tu 0 len 1 => sinh VET NGANG ngay ranh giori dai.
    """
    v = np.zeros_like(y)
    up = (y >= a) & (y < y0)
    dn = (y >= y1) & (y <= b)
    mid = (y >= y0) & (y < y1)
    if up.any():
        t = (y[up] - a) / max(1e-6, (y0 - a))
        v[up] = t * t * (3.0 - 2.0 * t)      # 0 tai a -> 1 tai y0
    v[mid] = 1.0
    if dn.any():
        t = (y[dn] - y1) / max(1e-6, (b - y1))
        v[dn] = 1.0 - (t * t * (3.0 - 2.0 * t))  # 1 tai y1 -> 0 tai b
    return v


def darken_text_bands(img):
    """Toi vung chu hook + phu de cho den khi dat nguong (giong bo tk01)."""
    arr = np.array(img, dtype=np.float32)
    h = arr.shape[0]
    depth = 0.0
    for depth in np.arange(0.0, 0.61, 0.05):
        prof = _band_profile(h, depth)
        out = arr * prof[:, None, None]
        hook = out[HOOK_BAND[0]:HOOK_BAND[1], SX0:SX1].mean()
        sub = out[SUB_BAND[0]:SUB_BAND[1], SX0:SX1].mean()
        if hook <= TARGET_HOOK and sub <= TARGET_SUB:
            break
    out = np.clip(out, 0, 255).astype(np.uint8)
    return Image.fromarray(out), round(float(depth), 2), round(float(hook), 1), round(float(sub), 1)


def main():
    DST.mkdir(parents=True, exist_ok=True)
    names = all_names()

    # L5: sao luu provenance truoc khi ghi
    bak = HERE / "_cu" / ("tk02_fallback_prov_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROV, bak / "provenance.json")
    prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    by_file = {it.get("file"): it for it in items}

    made, skipped = [], []
    for name in names:
        dst = DST / ("%s.png" % name)
        rel = "assets/bg/%s.png" % name
        # Chi ghi de ban DU PHONG. Ban AI that (co 'prompt' trong provenance)
        # phai giu nguyen — KHONG duoc ghi de bang ban crop.
        if dst.exists():
            entry = by_file.get(rel) or {}
            if entry.get("prompt"):
                skipped.append(name)
                continue
            # gan nhung la ban du phong -> tao lai de them dai toi vung chu
            img_bak = HERE / "_cu" / ("tk02_fallback_img_%s" % time.strftime("%Y%m%d_%H%M"))
            img_bak.mkdir(parents=True, exist_ok=True)
            shutil.copy2(dst, img_bak / dst.name)
        base = "t2_%s" % name[len("tk02_"):]
        src = pick_file(base)
        if src is None:
            print("  THIEU NGUON: %s" % base)
            continue

        with Image.open(src) as im:
            im = im.convert("RGB")
            gray = np.array(im.convert("L"))
            t, b, l, r = content_box(gray)
            wl, wr = best_window(gray, (t, b, l, r))
            ct = max(0, t)
            cb = min(gray.shape[0], b)
            sub = im.crop((wl, ct, wr, cb))
            # can bang phai chieu doc 9:16 truoc khi resize
            sw, sh = sub.size
            if sw * 16 // 9 < sh:
                sh2 = sw * 16 // 9
                sub = sub.crop((0, (sh - sh2) // 2, sw, (sh - sh2) // 2 + sh2))
            else:
                sw2 = sh * 9 // 16
                sub = sub.crop(((sw - sw2) // 2, 0, (sw - sw2) // 2 + sw2, sh))
            out = sub.resize((W, H), Image.Resampling.LANCZOS)
            out = safe_text_zone(out)
            out, depth, hook, sub_m = darken_text_bands(out)
            out.save(dst, "PNG", optimize=True)

        made.append((name, src.name, dst.stat().st_size / 1024))
        print("  %-26s <- %-24s %7.0f KB  depth=%.2f hook=%.1f sub=%.1f"
              % (name, src.name, dst.stat().st_size / 1024, depth, hook, sub_m))

        if rel not in by_file:
            items.append({
                "file": rel,
                "loai": "nen 9:16 dung cho clip TikTok (dung chung moi ngon ngu)",
                "cong_cu": ("DU PHONG - cat anh nen 16:9 goc cua Tap 02 (%s) bang LANCZOS + nen toi vung chu; "
                            "KHONG dung mo hinh AI (bi chan 402 het credit khi sinh nen doc AI)" % src.name),
                "ngay": "2026-11-20",
                "prompt": None,
                "seed": None,
                "mo_ta": "nen doc 9:16 DU PHONG cho clip TikTok Tap 02 - %s" % name,
                "font": None,
                "dieu_khoan": ("Anh goc do chinh kenh san xuat (assets/bg/_raw/%s), da qua grade noir cua kenh; "
                               "ban nay la ban CAT 9:16 de dung tam thoi. Phai thay bang ban AI doc 9:16 "
                               "(connector__matrix__generate_image) khi co credit. Moi dung kinh doanh: 1/3 tren "
                               "+ 1/3 duoi da toi de chu phu de + the chu an toan TikTok (x 120-780, y 240-1260)." % src.name),
                "kiem_tra_thuong_mai": ("dat (kich thuoc 1080x1920 dung chuan TikTok; mau noir dung bo cua Tap 02; "
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

    print("\ntao %d nen du phong · bo qua %d (da co) · backup: %s"
          % (len(made), len(skipped), bak))


if __name__ == "__main__":
    main()
