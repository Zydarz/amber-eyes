#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat provenance cho caption + mo_ta TikTok TK1 (them link YouTube) va do do dai caption."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
PROV = ROOT / "provenance.json"
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
LINK = "https://youtu.be/lDVXjeFLn48"

cap = (D / "Caption_TK1.txt").read_text(encoding="utf-8")
caption = cap.split("---")[0].strip()
n = len(caption)
print("do dai caption: %d ky tu (gioi han 2200)" % n)
print("caption co link YouTube: %s" % ("co" if "lDVXjeFLn48" in caption else "KHONG"))

mota = (D / "mo_ta.txt").read_text(encoding="utf-8")
print("mo_ta co link YouTube: %s" % ("co" if LINK in mota else "KHONG"))

data = json.loads(PROV.read_text(encoding="utf-8"))
for e in data:
    f = e.get("file", "")
    if f == "02_SAN_XUAT/TIKTOK/Tap01/Caption_TK1.txt":
        e["mo_ta"] = ("caption %d ky tu (co link YouTube %s, khong click duoc tren TikTok - "
                      "link click duoc nam o o Links/Website cua bio) + dong AIGC bat buoc; "
                      "ban ghi chu khi dang tach rieng" % (n, LINK))
        e["kiem_tra_thuong_mai"] = ("dat (do dai caption %d ky tu < 2200; khop mau "
                                    "KE_HOACH_CLIP_TAP01.md §8 TK1)" % n)
    elif f == "02_SAN_XUAT/TIKTOK/Tap01/mo_ta.txt":
        e["mo_ta"] = ("mo ta + caption + hashtag + ghi chu danh cho clip TikTok TK1; "
                      "co link YouTube Tap 01 %s va huong dan dat o Links/Website cua bio" % LINK)
        e["kiem_tra_thuong_mai"] = ("dat (do dai caption %d ky tu < 2200; khop mau "
                                    "KE_HOACH_CLIP_TAP01.md §8 TK1)" % n)
PROV.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("provenance: %d dong (cap nhat 2 dong)" % len(data))
