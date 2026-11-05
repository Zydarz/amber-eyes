# -*- coding: utf-8 -*-
"""Tổng hợp trạng thái bảng shot / timeline / ảnh tĩnh của Tập 02 cho 4 ngôn ngữ.

python .work/_qc_all_t02.py
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r'D:/TEST/Gax/amber-eyes')
W = ROOT / ".work"

LANGS = [("VN", "vi", "02_SAN_XUAT/Tap02/KeHoach_Video_Tap02.md", "video3_t02", "timeline_s_t02.json", "shots_t02.json"),
         ("EN", "en", "02_SAN_XUAT/Tap02_EN/KeHoach_Video_Tap02_EN.md", "video3_EN_t02", "timeline_s_EN_t02.json", "shots_EN_t02.json"),
         ("JA", "ja", "02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md", "video3_JA_t02", "timeline_s_JA_t02.json", "shots_JA_t02.json"),
         ("KO", "ko", "02_SAN_XUAT/Tap02_KO/KeHoach_Video_Tap02_KO.md", "video3_KO_t02", "timeline_s_KO_t02.json", "shots_KO_t02.json")]

print(f"{'':4} {'dong shot':>9} {'co loi':>7} {'nghi':>5} {'cau':>5} {'tong(s)':>9} {'anh':>5}  ket luan")
for tag, _lang, plan_rel, vd, tl_name, sh_name in LANGS:
    plan = ROOT / plan_rel
    tl_p = W / tl_name
    sh_p = W / sh_name
    stills = W / vd / "stills"
    n_png = len(list(stills.glob("*.png"))) if stills.exists() else 0
    rows = 0
    if plan.exists():
        txt = plan.read_text(encoding="utf-8")
        m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", txt, re.M)
        if m:
            sec = txt[m.end():]
            sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
            rows = len([l for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)])
    tl = json.loads(tl_p.read_text(encoding="utf-8")) if tl_p.exists() else None
    sh = json.loads(sh_p.read_text(encoding="utf-8")) if sh_p.exists() else None
    n_sent = len(tl["items"]) if tl else 0
    n_shots = len(sh["shots"]) if sh else 0
    n_hold = len([s for s in sh["shots"] if s.get("hold")]) if sh else 0
    total = round(tl["total"], 2) if tl else 0
    print(f"{tag:4} {rows:>9} {n_shots - n_hold if sh else 0:>7} {n_hold:>5} {n_sent:>5} {total:>9} {n_png:>5}  "
          f"{'OK' if (rows == 161 and n_png == 161 and n_sent == 203) else 'CHUA XONG'}")

# thống kê thời lượng shot dài
print("\nShot > 15 s:")
for tag, _lang, plan_rel, vd, tl_name, sh_name in LANGS:
    sh_p = W / sh_name
    if not sh_p.exists():
        continue
    sh = json.loads(sh_p.read_text(encoding="utf-8"))
    longs = [(s["id"], round(s["end"] - s["start"], 1)) for s in sh["shots"] if s["end"] - s["start"] > 15]
    longs.sort(key=lambda x: -x[1])
    print(f"  {tag}: {len(longs)} shot > 15s · dài nhất {longs[:4]}")
