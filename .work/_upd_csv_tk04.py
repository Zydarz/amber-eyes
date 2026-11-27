# -*- coding: utf-8 -*-
"""Cap nhat BangTheoDoi_TikTok.csv cho Tap 04 (VI/EN/JA) — GIU NGUYEN line-ending tung dong.

File co line-ending LOC (46 dong CRLF + 15 dong LF) => phai tach bang regex
giu separator, khong dung split('\\r\\n') (se gom 15 dong LF vao 1 phan tu).
"""
import pathlib
import re

p = pathlib.Path(r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/TIKTOK/BangTheoDoi_TikTok.csv")
raw = p.read_bytes()
print("truoc: CRLF=", raw.count(b"\r\n"), "LF-only=", raw.count(b"\n") - raw.count(b"\r\n"))
txt = raw.decode("utf-8")

BASE = "Da dung video 9:16 co logo H29 + QC 14 cong"
notes = {
    "TK04_1": BASE + "; TRUOT T13 (tu cam 'sat hai' o TK1.01#6)",
    "TK04_2": BASE + " DAT",
    "TK04_3": BASE + "; TRUOT T13 (tu cam 'sat hai' o TK3.01#9)",
    "TK04_4": BASE + " DAT",
    "TK04_5": BASE + " DAT",
    "TK04_EN_1": BASE + " DAT",
    "TK04_EN_2": BASE + " DAT; LOI AUDIO: thieu TK2.01#10 + #11, duoi 14.76s chi co nhac nen",
    "TK04_EN_3": BASE + " DAT",
    "TK04_EN_4": BASE + " DAT",
    "TK04_EN_5": BASE + " DAT",
    "TK04_JA_1": BASE + " DAT",
    "TK04_JA_2": BASE + " DAT",
    "TK04_JA_3": BASE + " DAT",
    "TK04_JA_4": BASE + " DAT",
    "TK04_JA_5": BASE + " DAT",
}

parts = re.split(r"(\r\n|\n|\r)", txt)
n = 0
for i in range(0, len(parts), 2):
    ln = parts[i]
    if not ln.startswith("TK04"):
        continue
    cid = ln.split(",")[0]
    if cid not in notes:
        continue
    cells = ln.split(",")
    cells[-1] = notes[cid]
    parts[i] = ",".join(cells)
    n += 1
out = "".join(parts)
p.write_bytes(out.encode("utf-8"))
raw2 = p.read_bytes()
print("sau:   CRLF=", raw2.count(b"\r\n"), "LF-only=", raw2.count(b"\n") - raw2.count(b"\r\n"),
      "| ket thuc:", repr(raw2[-3:]))
print("cap nhat", n, "dong")
