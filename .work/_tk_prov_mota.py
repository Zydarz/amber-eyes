#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them dong provenance cho mo_ta.txt cua clip TikTok TK1."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
PROV = ROOT / "provenance.json"
F = "02_SAN_XUAT/TIKTOK/Tap01/mo_ta.txt"

entry = {
    "file": F,
    "loai": "mo ta + caption + hashtag + ghi chu danh cho clip TikTok TK1",
    "cong_cu": "viet tay theo KE_HOACH_CLIP_TAP01.md muc 8 + mau mo ta tap 01",
    "ngay": "2026-11-19",
    "prompt": None,
    "seed": None,
    "mo_ta": ("caption 364 ky tu + dong AIGC bat buoc + khoi luu y an toan va hotline 111; "
              "ban mo ta day cua Tap 01 nam o 02_SAN_XUAT/Ho_So_Toi_Pham/Tap01/mo_ta.txt"),
    "font": None,
    "dieu_khoan": ("TikTok bat buoc nhan AIGC (toggle 'Noi dung do AI tao'); gioi han 2.200 ky tu; "
                   "khong dan phan ghi chu ky thuat vao caption."),
    "kiem_tra_thuong_mai": ("dat (khop mau trong KE_HOACH_CLIP_TAP01.md §8 TK1; kiem tra do dai "
                            "caption 364 ky tu < 2.200)"),
}


def main():
    data = json.loads(PROV.read_text(encoding="utf-8"))
    if any(e.get("file") == F for e in data):
        print("  da co dong -> bo qua")
        return
    data.append(entry)
    PROV.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("  provenance: them dong %s (tong %d)" % (F, len(data)))


if __name__ == "__main__":
    main()
