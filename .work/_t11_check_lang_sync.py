# -*- coding: utf-8 -*-
"""Đối chiếu mã nền giữa 3 bảng shot Tập 11 (H17: cùng mã shot = cùng nền)."""
import re

FILES = {
    "VI": r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Ho_So_Toi_Pham/Tap11/KeHoach_Video_Tap11.md",
    "EN": r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Ho_So_Toi_Pham/Tap11_EN/KeHoach_Video_Tap11_EN.md",
    "JA": r"D:/TEST/Gax/amber-eyes/02_SAN_XUAT/Ho_So_Toi_Pham/Tap11_JA/KeHoach_Video_Tap11_JA.md",
}
PAT = re.compile(r"`(t\d+_[a-z0-9_]+)`")
ROW = re.compile(r"^\|\s*([1-5]-\d+)\s*\|(.*)$")

maps = {}
for lbl, p in FILES.items():
    t = open(p, encoding="utf-8").read()
    m = {}
    for line in t.split("\n"):
        mm = ROW.match(line)
        if not mm:
            continue
        sid = mm.group(1)
        c = PAT.search(mm.group(2))
        if c:
            m[sid] = c.group(1)
    maps[lbl] = m
    print(f"{lbl}: {len(m)} dòng có mã nền · {len(set(m.values()))} mã nền")

vi, en, ja = maps["VI"], maps["EN"], maps["JA"]
print("\nshot có ở cả 3 bảng:", len(set(vi) & set(en) & set(ja)))
diff_en = [s for s in vi if s in en and vi[s] != en[s]]
diff_ja = [s for s in vi if s in ja and vi[s] != ja[s]]
print("lệch VI↔EN:", len(diff_en), diff_en[:8])
print("lệch VI↔JA:", len(diff_ja), diff_ja[:8])
print("\nsample:")
for sid in ["1-01", "1-02", "2-13", "2-14", "3-21", "4-44", "5-46", "5-47"]:
    print(f"  {sid}: VI={vi.get(sid)} EN={en.get(sid)} JA={ja.get(sid)}")
