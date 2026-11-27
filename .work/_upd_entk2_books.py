# -*- coding: utf-8 -*-
"""Cap nhat CSV theo doi + provenance cho clip EN TK2 Tap 04 (master moi 27/11, 72,34 s, 11/11 cau).

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
print("CSV truoc: CRLF=", raw.count(b"\r\n"), "LF-only=", raw.count(b"\n") - raw.count(b"\r\n"))
txt = raw.decode("utf-8")
parts = re.split(r"(\r\n|\n|\r)", txt)

NEW_NOTE = ("Da dung video 9:16 co logo H29 + QC 14 cong; DUNG LAI 27/11 tu master mp3 moi 72.34s "
            "(11/11 cau, A11 #200); TRUOT T6 (11 khoang cam >0.3s - master moi khong co nhac nen, "
            "nen im lang -70 dB) + TP -1.8 dBFS co 312 mau > 0 dBFS")
n = 0
for i in range(0, len(parts), 2):
    ln = parts[i]
    if not ln.startswith("TK04_EN_2,"):
        continue
    cells = ln.split(",")
    cells[4] = "72.34"          # do_dai_s
    cells[-1] = NEW_NOTE
    parts[i] = ",".join(cells)
    n += 1
CSV.write_bytes("".join(parts).encode("utf-8"))
raw2 = CSV.read_bytes()
print("CSV sau:   CRLF=", raw2.count(b"\r\n"), "LF-only=", raw2.count(b"\n") - raw2.count(b"\r\n"),
      "| cap nhat", n, "dong")

# ---------------- 2. provenance ----------------
PP = ROOT / "provenance.json"
BAK = ROOT / ".work" / "_cu" / f"provenance_tk04_entk2_{datetime.now():%Y%m%d_%H%M}" / "provenance.json"
BAK.parent.mkdir(parents=True, exist_ok=True)
shutil.copy2(PP, BAK)
print("backup provenance ->", BAK)

data = json.loads(PP.read_text(encoding="utf-8-sig"))
items = data if isinstance(data, list) else (data.get("tai_san") or data.get("items") or [])
target = "02_SAN_XUAT/TIKTOK/Tap04_EN/TK2_video.mp4"
hit = 0
for it in items:
    if it.get("file") != target:
        continue
    hit += 1
    g = it.get("ghi_chu", "")
    # bo ghi chu loi cu ("thieu 2 cau") roi them ghi chu moi
    g = re.sub(r"\s*LƯU Ý: master audio EN TK2 chỉ có 9/11 câu[^.]*\.[^.]*\.\s*", " ", g)
    g = re.sub(r"\s*LƯU Ý: master audio EN TK2[^.]*\.\s*", " ", g)
    it["ghi_chu"] = (
        g.rstrip() +
        " DUNG LAI 27/11/2026: master EN TK2 mp3 moi (72,34 s, thay ban 70,90 s) da render lai clip — "
        "11/11 cau khop 100% (A11 #200: ASR phai chay theo cua so ngan; ASR ca file bi bo duoi 14,6 s). "
        "LOI AUDIO MOI tren master: 11 khoang cam >0,3 s (master moi khong co nhac nen, nen im lang -70 dB, "
        "8,1% file im lang tuyet doi) + true peak -1,8 dBFS voi 312 mau > 0 dBFS (can giam doc am). "
        "Chi con WAV cu 70,90 s tren dia (khong dung de dung nua) - can nguoi dung quyet dinh tao lai WAV tu mp3.")
    it["nguon_anh_tham_chieu"] = None
print("provenance: doi", hit, "dong")
out = json.dumps(data, ensure_ascii=False, indent=2).replace("\n", "\r\n")
PP.write_bytes(out.encode("utf-8"))
print("da ghi provenance, tong", len(items), "muc")
