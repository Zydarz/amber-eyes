#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Ghi 'ban mo ta dai' vao Caption_TK1.txt + mo_ta.txt + provenance."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
PROV = ROOT / "provenance.json"
LONG = D / "MoTa_Dai_TK1.txt"
CAP = D / "Caption_TK1.txt"
MOTA = D / "mo_ta.txt"

n = len(LONG.read_text(encoding="utf-8").strip())

# 1. Caption_TK1.txt -> them phan troi huong
c = CAP.read_text(encoding="utf-8")
if "MoTa_Dai_TK1.txt" not in c:
    c = c.replace(
        "- Nguyên văn chỉ dẫn trong caption + nhãn AIGC: 02_SAN_XUAT/TIKTOK/Tap01/KE_HOACH_CLIP_TAP01.md §8.",
        "- Nguyên văn chỉ dẫn trong caption + nhãn AIGC: 02_SAN_XUAT/TIKTOK/Tap01/KE_HOACH_CLIP_TAP01.md §8.\n"
        "- BẢN MÔ TẢ DÀI (%d ký tự / 4.000) dán vào ô Description của TikTok Studio: "
        "02_SAN_XUAT/TIKTOK/Tap01/MoTa_Dai_TK1.txt" % n)
    CAP.write_text(c, encoding="utf-8")
    print("  Caption_TK1.txt: them troi ban mo ta dai")

# 2. mo_ta.txt -> them phan troi huong
m = MOTA.read_text(encoding="utf-8")
if "MoTa_Dai_TK1.txt" not in m:
    m = m.replace(
        "- Link YouTube Tập 01: https://youtu.be/lDVXjeFLn48 → dán vào ô Links/Website của bio (xem [A2]).",
        "- Link YouTube Tập 01: https://youtu.be/lDVXjeFLn48 → dán vào ô Links/Website của bio (xem [A2]).\n"
        "- BẢN MÔ TẢ DÀI (%d ký tự / 4.000 — dán vào ô Description của TikTok Studio): "
        "02_SAN_XUAT/TIKTOK/Tap01/MoTa_Dai_TK1.txt" % n)
    MOTA.write_text(m, encoding="utf-8")
    print("  mo_ta.txt: them troi ban mo ta dai")

# 3. provenance
data = json.loads(PROV.read_text(encoding="utf-8"))
files = {e.get("file") for e in data}
for e in data:
    f = e.get("file", "")
    if f == "02_SAN_XUAT/TIKTOK/Tap01/Caption_TK1.txt":
        e["mo_ta"] = ("caption ngan 334 ky tu (co link YouTube youtu.be/lDVXjeFLn48, khong click duoc "
                      "tren TikTok - link click duoc nam o o Links/Website cua bio) + dong AIGC bat buoc; "
                      "ban ghi chu khi dang tach rieng; troi sang ban mo ta dai %d ky tu" % n)
    elif f == "02_SAN_XUAT/TIKTOK/Tap01/mo_ta.txt":
        e["mo_ta"] = ("mo ta + caption + hashtag + ghi chu danh cho clip TikTok TK1; co link YouTube "
                      "Tap 01 va huong dan dat o Links/Website cua bio; troi sang ban mo ta dai %d ky tu" % n)
f_long = "02_SAN_XUAT/TIKTOK/Tap01/MoTa_Dai_TK1.txt"
if f_long not in files:
    data.append({
        "file": f_long,
        "loai": "mo ta DAI cho truong Description cua TikTok Studio (4.000 ky tu)",
        "cong_cu": "viet tay theo mo ta tap 01 + mau KE_HOACH_CLIP_TAP01.md muc 8",
        "ngay": "2026-11-19",
        "prompt": None,
        "seed": None,
        "mo_ta": ("ban mo ta %d ky tu: hook + chu dan 1 + giai thich chi dau #2 (thu doan vs chu ky tam ly) "
                  "+ boi canh ho so + 10 chi dau tam ly + 9 nguon tham khao + lưu y + hotline 111 + 10 hashtag"
                  % n),
        "font": None,
        "dieu_khoan": ("TikTok chi hien ~100 ky tu dau truoc khi bam 'more' => phan hook phai o dau; "
                       "khong dung tu cam V9/A9.2 (da quet tu dong); link YouTube trong caption khong click duoc."),
        "kiem_tra_thuong_mai": ("dat (%d ky tu < 4.000; 0 tu cam V9/A9.2; 9 nguon tham khao truy ve "
                                "02_SAN_XUAT/Tap01/nguon_tham_khao.md + mo ta tap 01)" % n),
    })
PROV.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("  provenance: %d dong" % len(data))
