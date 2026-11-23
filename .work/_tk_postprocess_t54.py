# -*- coding: utf-8 -*-
"""Hậu kỳ ảnh nền DỌC 9:16 cho clip TikTok Tập 54.

Input : .work/tk_img_raw_t54/tk54_*.png  (Kaggle FLUX đã LANCZOS 1080x1920 + grade noir
        + vignette + hạt phim 35mm trong worker)
Output: assets/bg/tk54_*.png  (1080x1920, đã tối vùng chữ hook + phụ đề)

Bước hậu kỳ tại máy (giống .work/_tk_postprocess_t04.py):
  1. LANCZOS về 1080x1920 (nếu chưa đúng kích thước)
  2. Tối vùng chữ hook + phụ đề cho tới khi mean đạt ngưỡng VÀ không còn dòng nào
     > 70% pixel vượt ngưỡng sáng (không vệt ngang)
  3. Ghi provenance.json (L7)

KHÔNG áp lại grade/vignette/grain ở đây: worker Kaggle đã áp rồi (áp 2 lần sẽ tối quá).
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
from _tk_fallback_crop_t04 import (  # noqa: E402
    HOOK_BAND, SUB_BAND, SX0, SX1, TARGET_HOOK, TARGET_SUB, _band_profile,
)
from _tk_postprocess_t04 import noir_grade, vignette_grain  # noqa: E402

ROOT = HERE.parent
RAW = HERE / "tk_img_raw_t54"
DST = ROOT / "assets" / "bg"
PROV = ROOT / "provenance.json"

W, H = 1080, 1920
# Dung DUNG dai QC (hook 270-730, sub 996-1254) de kiem vet ngang — dai rong hon
# dai dat chu nen phai toi hon (khong vet sang ra vung chu).
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
    """Chọn depth tối sao cho mean hook/sub đạt ngưỡng và không có vệt ngang."""
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


def main():
    DST.mkdir(parents=True, exist_ok=True)
    raws = sorted(list(RAW.glob("tk54_*.jpg")) + list(RAW.glob("tk54_*.png")))
    if not raws:
        raise SystemExit("khong co anh tho nao trong %s" % RAW)
    # uu tien MiniMax (.jpg, engine nền DỌC chuẩn của kênh) hơn Kaggle FLUX (.png)
    # khi cùng tên: giữ .jpg, bỏ .png — TRỪ khi tên nằm trong _tk54_flux_prefer.json
    # (bản MiniMax bị loại vì có chữ AI theo H2 ⇒ lấy bản FLUX)
    prefer_flux = set()
    pf = HERE / "_tk54_flux_prefer.json"
    if pf.exists():
        prefer_flux = set(json.loads(pf.read_text(encoding="utf-8")))
    have_jpg = {p.stem for p in raws if p.suffix.lower() == ".jpg"}
    raws = [p for p in raws
            if not (p.suffix.lower() == ".png" and p.stem in have_jpg
                    and p.stem not in prefer_flux)]

    bak = HERE / "_cu" / ("tk54_provenance_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROV, bak / "provenance.json")

    jobs = json.loads((HERE / "bg_jobs_tk54.json").read_text(encoding="utf-8"))
    job_map = {j["name"]: j for j in jobs}

    prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    index = {it.get("file"): it for it in items}
    added = updated = 0
    report = []

    for rp in raws:
        name = rp.stem
        dst = DST / ("%s.png" % name)
        with Image.open(rp) as im:
            src_size = im.size
            im = im.convert("RGB")
            # canh 9:16 truoc (nguon MiniMax 1536x2720 lech 0,4%) roi LANCZOS
            sw, sh = im.size
            target_ratio = W / H
            if abs((sw / sh) - target_ratio) > 1e-3:
                if (sw / sh) > target_ratio:      # rong hon -> cat 2 ben
                    nw = int(round(sh * target_ratio))
                    left = (sw - nw) // 2
                    im = im.crop((left, 0, left + nw, sh))
                else:                            # cao hon -> cat tren duoi
                    nh = int(round(sw / target_ratio))
                    top = (sh - nh) // 2
                    im = im.crop((0, top, sw, top + nh))
            if im.size != (W, H):
                im = im.resize((W, H), Image.Resampling.LANCZOS)
            # Anh KAGGLE FLUX (.png) da qua grade noir + vignette + grain TRONG worker
            # -> khong ap lai. Anh MiniMax (.jpg) chua qua gi -> ap tai day cho khop chuan.
            if rp.suffix.lower() in (".jpg", ".jpeg"):
                im = noir_grade(im)
                im = vignette_grain(im)
            im, depth, hook_m, sub_m, streak = darken_bands_strict(im)
            note = "depth=%.2f hook=%.1f sub=%.1f streak=%.2f" % (depth, hook_m, sub_m, streak)
            im.save(dst, "PNG", optimize=True)

        kb = dst.stat().st_size / 1024
        report.append((name, "%dx%d" % (src_size[0], src_size[1]), kb, note))

        rel = "assets/bg/%s.png" % name
        job = job_map.get(name, {})
        if rp.suffix.lower() in (".jpg", ".jpeg"):
            tool = ("MiniMax image-generation (mcode-tools connector__matrix__generate_image) - "
                    "prompt 4 tang chuan Deep Noir, aspect_ratio 9:16, area 2K, KHONG anh tham chieu; "
                    "hau ky tai may: canh 9:16 + LANCZOS 1080x1920 + grade noir (sat 0,65 · contrast 1,15) "
                    "+ vignette 45% + hat phim 35mm + toi vung chu hook/phu de")
            terms = ("Anh sinh boi mo hinh AI cua MiniMax qua mcode-tools (allowance goi, 0 dong); "
                     "moi dung kinh doanh: tach 1/3 tren va 1/3 duoi da toi de chu phu de "
                     "+ the chu an toan TikTok (x 120-780, y 240-1260).")
        else:
            tool = ("Kaggle GPU FLUX.2-klein-4B (Tesla T4) - FLUX.2 Community License / Black Forest Labs; "
                    "render 592x1056 -> LANCZOS 1080x1920; grade noir + vignette 45% + hat phim 35mm "
                    "trong worker; tai toi vung chu hook/phu de theo "
                    "00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md")
            terms = ("Anh sinh boi mo hinh AI FLUX.2-klein-4B tren Kaggle GPU; dung thuong mai theo "
                     "FLUX.2 Community License. Moi dung kinh doanh: tach 1/3 tren va 1/3 duoi da toi "
                     "de chu phu de + the chu an toan TikTok (x 120-780, y 240-1260).")
        new_row = {
            "file": rel,
            "loai": "nen doc 9:16 dung cho clip TikTok Tap 54 (dung chung moi ngon ngu)",
            "cong_cu": tool,
            "ngay": "2026-11-23",
            "prompt": job.get("prompt_core", ""),
            "seed": job.get("seed"),
            "mo_ta": "nen doc 9:16 cho clip TikTok Tap 54 - %s (%s)" % (name, job.get("desc", "")),
            "font": None,
            "dieu_khoan": terms,
            "kiem_tra_thuong_mai": ("dat (kich thuoc 1080x1920 dung chuan TikTok; mau noir khop bo nen TK "
                                    "da xuat ban; vung chu do lai bang may; soi mat 100% tren montage)"),
        }
        if rel in index:
            index[rel].update({k: v for k, v in new_row.items() if k != "file"})
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

    print("%-38s %-12s %8s  %s" % ("nen", "kich thuoc", "KB", "vung chu"))
    for name, size, kb, note in report:
        print("%-38s %-12s %8.0f  %s" % (name, size, kb, note))
    print("\nprovenance: +%d dong · cap nhat %d dong · backup: %s" % (added, updated, bak))

    missing = [j["name"] for j in jobs
               if not (DST / ("%s.png" % j["name"])).exists()]
    if missing:
        print("CHUA CO (%d): %s" % (len(missing), ", ".join(missing)))


if __name__ == "__main__":
    main()
