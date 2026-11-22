# -*- coding: utf-8 -*-
"""Crop lai 3 nen doc bi cat mat chu the (fallback crop 16:9 -> 9:16).

Cua so 9:16 chi ro 864 px trong anh goc 2752 px nen 2 nguoi doi dien nhau
(interview_room) hoac 2 dieu tra vien (two_agents) khong the nam trong cung 1
cua so. Fix: chon cua so co chu the day du theo toa do tay (x0) cho tung anh.

Dung lai dung pipeline cua _tk_fallback_crop_t03.py: LANCZOS 1080x1920
+ safe_text_zone + darken_text_bands.
"""
import json
import os
import pathlib
import shutil
import sys
import time

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_fallback_crop_t03 import (  # noqa: E402
    RAW, DST, PROV, content_box, safe_text_zone, darken_text_bands, W, H,
)
from _tk_src_t03 import PAIRS  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent

# ten nen doc -> (ten file nguon, x0 theo pixel trong anh goc 2752 px)
WINDOWS = {
    "tk03_two_agents": ("t3_two_agents.png", 950),      # giu ca 2 dieu tra vien
    "tk03_interview_room": ("t3_interview_room.jpg", 700),  # giu 1 nguoi + ban
    "tk03_mother_shadow": ("t3_mother_shadow.jpg", 560),    # giu tron nguoi
}


def main():
    prov = json.loads(PROV.read_text(encoding="utf-8-sig"))
    items = prov if isinstance(prov, list) else prov.get("tai_san", prov.get("items", []))
    by_file = {it.get("file"): it for it in items}

    bak = HERE / "_cu" / ("tk03_recrop_img_%s" % time.strftime("%Y%m%d_%H%M"))
    bak.mkdir(parents=True, exist_ok=True)

    for name, (ref, x0) in WINDOWS.items():
        dst = DST / ("%s.png" % name)
        if dst.exists():
            shutil.copy2(dst, bak / dst.name)
        src = RAW / ref
        with Image.open(src) as im:
            im = im.convert("RGB")
            gray = np.array(im.convert("L"))
            t, b, l, r = content_box(gray)
            ch = b - t
            win_w = int(round(ch * 9 / 16))
            x0 = max(l, min(x0, r - win_w))
            x1 = x0 + win_w
            crop = im.crop((x0, t, x1, b))
            sw, sh = crop.size
            if sw * 16 // 9 < sh:
                sh2 = sw * 16 // 9
                crop = crop.crop((0, (sh - sh2) // 2, sw, (sh - sh2) // 2 + sh2))
            else:
                sw2 = sh * 9 // 16
                crop = crop.crop(((sw - sw2) // 2, 0, (sw - sw2) // 2 + sw2, sh))
            out = crop.resize((W, H), Image.Resampling.LANCZOS)
            out = safe_text_zone(out)
            out, depth, hook, sub_m = darken_text_bands(out)
            out.save(dst, "PNG", optimize=True)
        print("%-24s <- %-24s cua so x=[%d..%d]  depth=%.2f hook=%.1f sub=%.1f  %.0f KB"
              % (name, ref, x0, x0 + win_w, depth, hook, sub_m, dst.stat().st_size / 1024))

    print("\nbackup anh cu: %s" % bak)


if __name__ == "__main__":
    main()
