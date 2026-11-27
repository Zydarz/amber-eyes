# -*- coding: utf-8 -*-
"""Ghi 3 quyet dinh cua nguoi dung vao CSV theo doi + provenance (VN TK1/TK3 + 14 clip BGM + kernel Kaggle).

Giu NGUYEN line-ending tung dong (CSV) va format goc cua provenance.json (indent=2, CRLF, khong BOM).
"""
import json
import pathlib
import re
import shutil
import sys
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")

# ---------------- 1. CSV ----------------
CSV = ROOT / "02_SAN_XUAT" / "TIKTOK" / "BangTheoDoi_TikTok.csv"
raw = CSV.read_bytes()
txt = raw.decode("utf-8")
parts = re.split(r"(\r\n|\n|\r)", txt)

BASE = "Da dung video 9:16 co logo H29 + QC 14 cong"
NOTES = {
    "TK04_1": BASE + "; TRUOT T13 (tu cam 'sat hai' o TK1.01#6) - NGUOI DUNG se tu duyet kich ban (27/11)",
    "TK04_3": BASE + "; TRUOT T13 (tu cam 'sat hai' o TK3.01#9) - NGUOI DUNG se tu duyet kich ban (27/11)",
    "TK04_EN_2": BASE + " DAT; master EN TK2 TRON LAI 27/11 (voice + bgm_ambient_deep co ducking + ambience -42 dB + "
                        "loudnorm 2 luot) => 72.34s - 11/11 cau - 0 khoang cam - 0 mau clip - I -16.0 LUFS - TP -4.48 dBFS "
                        "(A11 #200 + #201)",
}
NOTES["TK04_EN_2"] = NOTES["TK04_EN_2"]
# 14 clip con lai: ghi chu nguon nhac nen cho 1 clip mau (TK04_2) + them ghi chu chung vao 14 clip
BED_NOTE = ("; NHAC NEN 14 clip con lai: bed da mat file nguon (T9/L7) - NGUOI DUNG se xac nhan (27/11)")
for cid in ["TK04_2", "TK04_4", "TK04_5", "TK04_EN_1", "TK04_EN_3", "TK04_EN_4", "TK04_EN_5",
            "TK04_JA_1", "TK04_JA_2", "TK04_JA_3", "TK04_JA_4", "TK04_JA_5"]:
    NOTES[cid] = BASE + " DAT" + BED_NOTE

n = 0
for i in range(0, len(parts), 2):
    ln = parts[i]
    cid = ln.split(",")[0]
    if cid not in NOTES:
        continue
    cells = ln.split(",")
    cells[-1] = NOTES[cid]
    parts[i] = ",".join(cells)
    n += 1
CSV.write_bytes("".join(parts).encode("utf-8"))
raw2 = CSV.read_bytes()
print("CSV: cap nhat", n, "dong | CRLF=", raw2.count(b"\r\n"), "LF-only=", raw2.count(b"\n") - raw2.count(b"\r\n"))
for ln in raw2.decode("utf-8").replace("\r\n", "\n").split("\n"):
    if ln.startswith(("TK04_1,", "TK04_EN_2,")):
        print("   ", len(ln.split(",")), "o |", ln[:150])

# ---------------- 2. provenance ----------------
PP = ROOT / "provenance.json"
BAK = ROOT / ".work" / "_cu" / f"provenance_tk04_decisions_{datetime.now():%Y%m%d_%H%M}" / "provenance.json"
BAK.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(PP, BAK)
print("backup provenance ->", BAK)

data = json.loads(PP.read_text(encoding="utf-8-sig"))
items = data if isinstance(data, list) else (data.get("tai_san") or data.get("items") or [])
VN_BAD = {"02_SAN_XUAT/TIKTOK/Tap04/TK1_video.mp4", "02_SAN_XUAT/TIKTOK/Tap04/TK3_video.mp4"}
EN_TK2 = "02_SAN_XUAT/TIKTOK/Tap04_EN/TK2_video.mp4"

DEC_T13 = (" QUYET DINH NGUOI DUNG 27/11/2026: nguoi dung se TU DUYET KICH BAN cho tu cam nay - "
           "AI khong tu sua (L2/L4). Khi cau doi => phai chay lai TTS cho cau do (Higgs Audio v3 chi chay tren "
           "Kaggle GPU/Apple MLX) => chay lai ASR + timeline + render + QC cho clip bi anh huong.")
DEC_BGM = (" QUYET DINH NGUOI DUNG 27/11/2026: nguoi dung se XAC NHAN nguon nhac nen cho clip nay "
           "(bed da mat file nguon - T9/L7). EN TK2 da duoc tach rieng: dung bgm_ambient_deep.mp3 co tren dia + "
           "co dong provenance day du => khong con vuong T9/L7.")

hit = 0
for it in items:
    f = it.get("file", "")
    if f in VN_BAD:
        it["ghi_chu"] = it.get("ghi_chu", "") + DEC_T13
        hit += 1
    elif f.startswith("02_SAN_XUAT/TIKTOK/") and f.endswith("_video.mp4") and f != EN_TK2:
        it["ghi_chu"] = it.get("ghi_chu", "") + DEC_BGM
        hit += 1
print("provenance: doi", hit, "dong")
out = json.dumps(data, ensure_ascii=False, indent=2).replace("\n", "\r\n")
PP.write_bytes(out.encode("utf-8"))
print("da ghi provenance, tong", len(items), "muc")
