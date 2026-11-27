# -*- coding: utf-8 -*-
"""Kiem tra cuoi - Buoc 8 Tap 04."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
TK = ROOT / "02_SAN_XUAT" / "TIKTOK"
LANGS = [("VN", "Tap04"), ("EN", "Tap04_EN"), ("JA", "Tap04_JA")]
ok = True
for lang, d in LANGS:
    for n in range(1, 6):
        p = TK / d / f"Caption_TK{n}.txt"
        t = p.read_text(encoding="utf-8")
        has_aigc = ("tạo hình và giọng" in t) if lang == "VN" else \
                   ("AI assistance" in t) if lang == "EN" else ("AI技術" in t)
        has_notes = ("Ghi chú khi đăng" in t) if lang == "VN" else \
                    ("Publishing Notes" in t) if lang == "EN" else ("投稿時の注意事項" in t)
        body = t.split("\n\n---\n")[0]
        nchars = len(body.rstrip("\n"))
        flag = "OK " if (has_aigc and has_notes) else "THIEU"
        if flag != "OK ":
            ok = False
        print(f"{flag} {d}/Caption_TK{n}.txt  aigc={has_aigc} notes={has_notes} dan={nchars} ky tu")
    for fn in ("mo_ta.txt", "checklist_dang.md"):
        p = TK / d / fn
        print(f"{'OK ' if p.exists() else 'THIEU'} {d}/{fn}  ({p.stat().st_size if p.exists() else 0} byte)")
print("TAT CA FILE DONG GOI:" , "OK" if ok else "CO THIEU")
