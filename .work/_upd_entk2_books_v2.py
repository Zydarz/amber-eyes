# -*- coding: utf-8 -*-
"""Cap nhat CSV + provenance cho EN TK2 Tap 04 SAU KHI TRON LAI master (BGM + ambience).

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

NOTE = ("Da dung video 9:16 co logo H29 + QC 14 cong DAT; master EN TK2 TRON LAI 27/11 "
        "(voice + bgm_ambient_deep co ducking + ambience -42 dB + loudnorm 2 luot) "
        "=> 72.34s - 11/11 cau - 0 khoang cam - 0 mau clip - I -16.0 LUFS - TP -4.48 dBFS "
        "(A11 #200 + #201)")

NEW_ROW = ",".join([
    "TK04_EN_2", "04_EN", "The Model Colleague", "Halo Effect of Pristine Scrubs", "72.34",
    "", "", "", "", "", "", "", "",
    "Da co master audio", NOTE,
])
assert len(NEW_ROW.split(",")) == 15

n = 0
for i in range(0, len(parts), 2):
    if parts[i].startswith("TK04_EN_2,"):
        parts[i] = NEW_ROW
        n += 1
CSV.write_bytes("".join(parts).encode("utf-8"))
raw2 = CSV.read_bytes()
print("CSV sau:   CRLF=", raw2.count(b"\r\n"), "LF-only=", raw2.count(b"\n") - raw2.count(b"\r\n"),
      "| cap nhat", n, "dong")

# ---------------- 2. provenance ----------------
PP = ROOT / "provenance.json"
BAK = ROOT / ".work" / "_cu" / f"provenance_tk04_entk2_mix_{datetime.now():%Y%m%d_%H%M}" / "provenance.json"
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
    # bo phan ghi chu loi cu (nhac nen / TP) roi viet lai toan bo
    g = re.sub(r"\s*DUNG LAI 27/11/2026:.*$", "", g, flags=re.S)
    it["ghi_chu"] = (
        g.rstrip() +
        " TRON LAI MASTER 27/11/2026 (nguoi dung cho phep): giong Higgs + bgm_ambient_deep.mp3 (ducking -24/-16 dB, "
        "smooth 0,2 s) + ambience phong kin -42 dB + fade cuoi 0,8 s + loudnorm 2 luot I=-16/TP=-1,5/LRA=11 "
        "(script .work/_remix_entk2.py; voice stem giu oi Tap04_EN/TK2_voice_stem.mp3 de ASR do moc thoi gian). "
        "KET QUA: 72,34 s - 11/11 cau khop 100% - 0 khoang cam >0,3 s - 0 mau >0 dBFS - I -16,0 LUFS - TP -4,48 dBFS. "
        "NHAC NEN: bgm_ambient_deep.mp3 (MiniMax) - file nay CO tren dia + co dong provenance day du => EN TK2 la clip "
        "DUY NHAT co nguon nhac nen truy vet duoc; 14 clip con lai dung bed da mat file nguon (T9/L7, can nguoi dung xac nhan). "
        "A11 #200 (ASR cua so + nguon mp3) va #201 (ASR phai chay tren voice stem) + AGENTS.md H30, H31.")
    it["cong_cu"] = it.get("cong_cu", "") + (
        "; master audio tron lai bang script .work/_remix_entk2.py (BGM + ambience + loudnorm 2 luot)")
print("provenance: doi", hit, "dong")
out = json.dumps(data, ensure_ascii=False, indent=2).replace("\n", "\r\n")
PP.write_bytes(out.encode("utf-8"))
print("da ghi provenance, tong", len(items), "muc")
