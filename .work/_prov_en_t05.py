#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them dong provenance cho thanh pham Tap05 EN (L7: moi tai san phai co dong).

Chi them dong CHUA co — khong ghi de.
Chay: py -3 .work/_prov_en_t05.py
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
P = ROOT / "provenance.json"
data = json.loads(P.read_text(encoding="utf-8"))
have = {d.get("file") for d in data}

rows = [
    {
        "file": "02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp3",
        "loai": "audio master bản tiếng Anh Tập 05 (1272,51 s, 192 kbps)",
        "cong_cu": "Boson AI Higgs Audio v3 (MLX, Mac mini M2) — .work/generate_higgs_prod_t05en.py; "
                   "trộn + loudnorm I=-16 LUFS (2 lượt, linear) + encode libmp3lame 192k",
        "ngay": "2026-11-03",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Boson AI Higgs Audio — kiểm tra điều khoản thương mại trước khi đăng "
                      "(ghi công trong mô tả YouTube theo QUY_TAC_AUDIO_HIGGS)",
        "kiem_tra_thuong_mai": "chưa",
        "ghi_chu": "164 câu · CER TB 1,04% · UTMOSv2 TB 3,37/5 · đo trên master: I=-16,3 LUFS, "
                   "true peak -1,9 dBFS. Dùng file này làm nguồn âm thanh cho video (wav trong .work "
                   "là bản cũ 1449,24 s — KHÔNG dùng để ghép).",
    },
    {
        "file": "02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN_master.mp4",
        "loai": "video xuất bản bản tiếng Anh Tập 05 (1920x1080@30, H.264 + AAC 192k)",
        "cong_cu": ".work/_build_video3_split.py (4 chunk theo frame, 6 worker, pipe 4 MB, "
                   "AE_FAST_FINISH) → .work/_mux_en_t05.py (concat 1 lần + limiter EN "
                   "limit=0,63 latency=1)",
        "ngay": "2026-11-04",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Kênh tự tạo (hình nền AI đã có dòng riêng; giọng Higgs xem dòng master mp3)",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "83 shot · 164/164 câu có lời · khớp timeline 1272,51 s ±0,05 s · "
                   "khớp A/V ≤20 ms so với master mp3",
    },
    {
        "file": "02_SAN_XUAT/Tap05_EN/xuat_ban/Tap05_EN.srt",
        "loai": "phụ đề bản tiếng Anh Tập 05 (356 cue)",
        "cong_cu": ".work/subtitles.py — tách từ timeline_s_EN_t05.json, nhãn vai tiếng Anh",
        "ngay": "2026-11-03",
        "prompt": None,
        "seed": None,
        "dieu_khoan": "Kênh tự tạo",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "câu cuối kết 21:02,710 = 1262,71 s khớp timeline; thẻ kết không có lời",
    },
]

added = 0
for r in rows:
    if r["file"] in have:
        print(f"  [Ton tai] {r['file']}")
        continue
    data.append(r)
    added += 1
    print(f"  [Them]    {r['file']}")

if added:
    P.write_text(json.dumps(data, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"xong: +{added} dong · tong {len(data)} dong")
