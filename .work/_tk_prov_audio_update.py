#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cap nhat dong provenance cua audio TK1 theo ket qua QC that (18/11/2026)."""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
PROV = ROOT / "provenance.json"
WAV = "02_SAN_XUAT/TIKTOK/Tap01/TK1_master_audio.wav"
MP3 = "02_SAN_XUAT/TIKTOK/Tap01/TK1_master_audio.mp3"

QC = ("dat 8/11 cong (T4 do dai 66,60 s · T5 -16,0 LUFS / true peak -4,5 dBFS · T6 0 khoang cam "
      ">= 0,3 s · G6 khop spec 12/12 · G9 min 7,34 nua cung) · G12 CER khong dat nguong 2% "
      "(TB 6,72% tren 3 luot ASR, 11/12 cau >= 2%) · 6 cau co loi phat am that: #4 #5 #7 #9 #10 #12. "
      "Xem 02_SAN_XUAT/TIKTOK/Tap01/BaoCao_QC_TK1_Audio_20261118.md")

data = json.loads(PROV.read_text(encoding="utf-8"))
n = 0
for e in data:
    if e.get("file") == WAV:
        e["kiem_tra_thuong_mai"] = QC
        n += 1
    elif e.get("file") == MP3:
        e["kiem_tra_thuong_mai"] = ("dat (do lai tren MP3: -16,0 LUFS, true peak -4,5 dBFS, "
                                    "lech WAV-MP3 0,000 s; noi dung giong WAV)")
PROV.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("cap nhat %d dong" % n)
