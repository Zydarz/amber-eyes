# -*- coding: utf-8 -*-
"""Sua DONG CSV TK04_EN_2 cho khop 15 o nhu cac dong TK04_* khac (ghi chu khong chua dau phay)."""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
CSV = pathlib.Path(r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv")
raw = CSV.read_bytes()
txt = raw.decode("utf-8")
parts = re.split(r"(\r\n|\n|\r)", txt)

NOTE = ("Da dung video 9:16 co logo H29 + QC 14 cong; DUNG LAI 27/11 tu master mp3 moi 72.34s "
        "(11/11 cau khop - A11 #200); TRUOT T6: 11 khoang cam >0.3s (master moi khong co nhac nen - "
        "nen im lang -70 dB) + TP -1.8 dBFS co 312 mau > 0 dBFS")

NEW_ROW = ",".join([
    "TK04_EN_2", "04_EN", "The Model Colleague", "Halo Effect of Pristine Scrubs", "72.34",
    "", "", "", "", "", "", "", "",
    "Da co master audio", NOTE,
])
assert len(NEW_ROW.split(",")) == 15, len(NEW_ROW.split(","))

n = 0
for i in range(0, len(parts), 2):
    if parts[i].startswith("TK04_EN_2,"):
        parts[i] = NEW_ROW
        n += 1
CSV.write_bytes("".join(parts).encode("utf-8"))
raw2 = CSV.read_bytes()
print("cap nhat", n, "dong | CRLF=", raw2.count(b"\r\n"), "LF-only=", raw2.count(b"\n") - raw2.count(b"\r\n"))
for ln in raw2.decode("utf-8").replace("\r\n", "\n").split("\n"):
    if ln.startswith("TK04_EN_2"):
        print("=> so o:", len(ln.split(",")))
        print(ln)
