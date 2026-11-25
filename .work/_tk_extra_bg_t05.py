# -*- coding: utf-8 -*-
"""Sinh THEM 2 nen doc 9:16 cho TK4 (de dat H22: nen cu da 5 shot / 37 s).

Chi tao 2 nen moi, KHONG dong vao 20 nen du phong da co.
Dung lai dung pipeline cua _tk_fallback_crop_t05.py (crop 9:16 tu anh 16:9 goc).
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
from _tk_fallback_crop_t05 import (  # noqa: E402
    RAW, DST, PROV, W, H, content_box, best_window, safe_text_zone, darken_text_bands,
)
from _tk_src_t05 import PAIRS  # noqa: E402

NEW = ["tk05_narcissistic_throne", "tk05_darkened_house_exterior"]


def main():
    bak = HERE / "_cu" / ("tk05_extra_prov_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PROV, bak / "provenance.json")

    prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    by_file = {it.get("file"): it for it in items}
    ref_of = dict(PAIRS)

    for name in NEW:
        ref = ref_of[name]
        src = RAW / ref
        if not src.exists():
            print("THIEU NGUON:", ref)
            continue
        dst = DST / ("%s.png" % name)
        with Image.open(src) as im:
            im = im.convert("RGB")
            gray = np.array(im.convert("L"))
            t, b, l, r = content_box(gray)
            wl, wr = best_window(gray, (t, b, l, r))
            ct, cb = max(0, t), min(gray.shape[0], b)
            sub = im.crop((wl, ct, wr, cb))
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

        rel = "assets/bg/%s.png" % name
        print("%-34s <- %-32s %7.0f KB  depth=%.2f hook=%.1f sub=%.1f"
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
    print("\nbackup:", bak)


if __name__ == "__main__":
    main()
