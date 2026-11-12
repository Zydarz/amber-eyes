#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC — DANH SÁCH SHOT BẮT BUỘC SOI BẰNG MẮT (mỗi ngôn ngữ).

Mục đích (A9.5, chốt 12/11/2026): **đo tự động luôn chạy 100 %**, nhưng phần
"soi bằng mắt" chỉ làm trên nhóm shot có RỦI RO THẬT — để giảm token/thời gian
mà KHÔNG hạ ngưỡng chất lượng.

Bắt buộc soi mắt nếu rơi vào 1 trong 4 nhóm:
  1. Mẫu đặc biệt: T4 (lời kể), T8 (cờ), T10 (thẻ hồi), T2 (thẻ kết)
  2. Shot có `text_scrim` (lớp phủ làm đổi tương phản nền)
  3. Nền SÁNG ở vùng đặt chữ (đo trực tiếp trên file nền, ngưỡng --lum)
  4. Chữ dài (≥ --chars ký tự) ở ngôn ngữ đang xét ⇒ dễ tràn/dè

Dùng:
  py -3 .work/qc_eyeball_list.py --ep 10 --lang vi
  py -3 .work/qc_eyeball_list.py --ep 10 --lang ja --lum 90 --chars 120
"""
import argparse
import json
import pathlib
import re
import sys

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
W = ROOT / ".work"

ap = argparse.ArgumentParser()
ap.add_argument("--ep", required=True)
ap.add_argument("--lang", default="vi")
ap.add_argument("--lum", type=float, default=95.0, help="ngưỡng sáng vùng đặt chữ (0-255)")
ap.add_argument("--chars", type=int, default=120, help="ngưỡng chữ dài (ký tự)")
ap.add_argument("--json", default="", help="ghi danh sách ra file json")
a = ap.parse_args()

EP = a.ep
LG = a.lang.lower()
sh_file = W / (f"shots_{LG.upper()}_t{EP}.json" if LG != "vi" else f"shots_t{EP}.json")
if not sh_file.exists():
    print(f"x khong co {sh_file.name}")
    sys.exit(1)
shots = json.loads(sh_file.read_text(encoding="utf-8"))["shots"]

# --- lớp text_scrim theo tập (HỢP 3 ngôn ngữ) ---
ed = (W / "edition.py").read_text(encoding="utf-8")
i10 = ed.find(f'    "{EP}": {{')
i11 = ed.find(f'    "{int(EP) + 1:02d}": {{', i10)
seg = ed[i10:i11 if i11 > 0 else len(ed)]
m = re.search(r'"text_scrim": \[(.*?)\]', seg, re.S)
scrim = set(re.findall(r'"([^"]+)"', m.group(1))) if m else set()

# --- vùng đặt chữ T1 (khung 1920x1080) → quy đổi sang file nền 2112x1188 ---
BOX = (96, 1200, 820, 1070)                      # x0,x1,y0,y1 trong khung 1920x1080
sx, sy = 2112 / 1920.0, 1188 / 1080.0
BXY = (int(BOX[0] * sx), int(BOX[1] * sx), int(BOX[2] * sy), int(BOX[3] * sy))

_lum_cache = {}


def bg_lum(name):
    """Độ sáng trung bình của vùng đặt chữ trong file nền (None nếu không có file)."""
    if name in _lum_cache:
        return _lum_cache[name]
    p = ROOT / "assets" / "bg" / f"{name}.png"
    if not p.exists():
        _lum_cache[name] = None
        return None
    a = np.asarray(Image.open(p).convert("L"), dtype=np.float32)
    x0, x1, y0, y1 = BXY
    v = float(a[y0:y1, x0:x1].mean())
    _lum_cache[name] = v
    return v


SPECIAL = {"T4", "T8", "T10", "T2", "T4 lời kể"}
must, why = [], {}
for s in shots:
    sid = s["id"]
    tpl = str(s.get("template") or "")
    bg = s.get("bg")
    # chữ THẬT trên hình nằm ở segments[].elems = [[style, text], ...]
    txt = " ".join(str(e[1]) for seg_ in (s.get("segments") or [])
                   for e in (seg_.get("elems") or []) if isinstance(e, (list, tuple)) and len(e) > 1)
    if not txt:
        txt = " ".join(str(x) for x in (s.get("sentences") or []))
    reasons = []
    if tpl in SPECIAL or tpl.replace(" lời kể", "") in ("T4", "T8", "T10", "T2"):
        reasons.append("mẫu đặc biệt")
    if sid in scrim:
        reasons.append("có text_scrim")
    L = bg_lum(bg) if bg and bg != "void" else None
    if L is not None and L >= a.lum:
        reasons.append(f"nền sáng vùng chữ ({L:.0f})")
    if len(txt) >= a.chars:
        reasons.append(f"chữ dài ({len(txt)} ký tự)")
    if reasons:
        must.append(sid)
        why[sid] = reasons

print(f"[{LG.upper()}] tập {EP}: BẮT BUỘC soi mắt {len(must)}/{len(shots)} shot "
      f"({100.0 * len(must) / max(1, len(shots)):.0f} %) · ngưỡng lum={a.lum} chars={a.chars}")
if must:
    print("  " + ", ".join(must))
print(f"  ngưỡng H9 (đo tự động) KHÔNG đổi: 8 % — vẫn chạy 100 % shot × mọi ngôn ngữ")
print(f"  số shot được lược = {len(shots) - len(must)} (chỉ soi khi đo tự động báo vượt ngưỡng)")

if a.json:
    out = pathlib.Path(a.json)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps({"ep": EP, "lang": LG, "must": must, "why": why},
                              ensure_ascii=False, indent=1), encoding="utf-8")
    print("  ->", out)
