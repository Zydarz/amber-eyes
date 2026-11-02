#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Harden t5_number: chu lon cu the 'ngay' phai tu co chu cho vua khung (H9).

build_video3.py dung ket thuong "\r\r\n" -> giu nguyen khi ghi lai.
"""
import sys
from pathlib import Path

P = Path(r"D:\TEST\Gax\amber-eyes\.work\build_video3.py")
src = P.read_bytes().decode("utf-8")
NL = "\r\r\n"

OLD = NL.join([
    '            if shot["variant"] == "date":',
    '                def f(fr, tt, big=big, t0=t, X=X):',
    '                    n = max(1, min(len(big), int((tt - t0) / 0.07) + 1))',
    '                    d = ImageDraw.Draw(fr)',
    '                    d.text((X, 400), big[:n], font=F_MONO(150), fill=C["text"] + (255,))',
    '                els.append(Dyn(f, t))',
])

NEW = NL.join([
    '            if shot["variant"] == "date":',
    '                # H9: chu lon phai vua khung. Tu giam co chu cho den khi vua W - X - 30',
    '                fz = 150',
    '                while fz > 40 and F_MONO(fz).getlength(big) > W - X - 30:',
    '                    fz -= 2',
    '                def f(fr, tt, big=big, t0=t, X=X, fz=fz):',
    '                    n = max(1, min(len(big), int((tt - t0) / 0.07) + 1))',
    '                    d = ImageDraw.Draw(fr)',
    '                    d.text((X, 400), big[:n], font=F_MONO(fz), fill=C["text"] + (255,))',
    '                els.append(Dyn(f, t))',
])

n = src.count(OLD)
if n != 1:
    print(f"[FAIL] khop {n} lan (can 1)")
    sys.exit(1)
src = src.replace(OLD, NEW)
with open(P, "w", encoding="utf-8", newline="") as f:
    f.write(src)
chk = P.read_bytes()
print("[OK ] da harden t5_number (tu co chu theo khung)")
print("     BOM:", chk[:3].hex(), "| CRLF:", chk.count(b"\r\r\n"), "| LF:", chk.count(b"\n"))
