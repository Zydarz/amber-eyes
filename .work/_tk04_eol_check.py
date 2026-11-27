# -*- coding: utf-8 -*-
"""Kiem tra line-ending + BOM cua caption Tap04/Tap03 va file txt mau."""
import pathlib
ROOT = pathlib.Path(__file__).resolve().parent.parent
for p in ["02_SAN_XUAT/TIKTOK/Tap04/Caption_TK1.txt",
          "02_SAN_XUAT/TIKTOK/Tap04_EN/Caption_TK1.txt",
          "02_SAN_XUAT/TIKTOK/Tap04_JA/Caption_TK1.txt",
          "02_SAN_XUAT/TIKTOK/Tap03/Caption_TK1.txt",
          "02_SAN_XUAT/TIKTOK/Tap03_EN/Caption_TK1.txt",
          "02_SAN_XUAT/TIKTOK/Tap03_JA/Caption_TK1.txt",
          "02_SAN_XUAT/TIKTOK/Tap01/mo_ta.txt",
          "02_SAN_XUAT/TIKTOK/Tap04/MoTa_Dai_TK1.txt",
          "02_SAN_XUAT/TIKTOK/Tap04/BAO_CAO_QC_TIKTOK_TAP04.md",
          "02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md"]:
    b = (ROOT / p).read_bytes()
    bom = b[:3] == b"\xef\xbb\xbf"
    crlf = b.count(b"\r\n")
    lf = b.count(b"\n") - crlf
    cr = b.count(b"\r") - crlf
    print(f"{p:60s} bom={bom} crlf={crlf} lf={lf} cr={cr} tail={b[-6:]!r}")
