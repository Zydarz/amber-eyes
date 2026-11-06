#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/acting_tap09.json — diễn xuất từng câu cho bản tiếng Việt Tập 09 (Charles Manson & Gia đình Manson).

Tuân thủ nghiêm ngặt quy tắc giọng đọc kênh AMBER EYES (AGENTS.md & TIÊU CHUẨN):
  1. G5 — Cao độ (pitch) LUÔN = 0 (bảo toàn danh tính vai).
  2. G3 — Chỉ dùng cảm xúc an toàn (neutral/sad/fearful/surprised).
  3. G4 — Lệch tốc độ kẹp chặt trong [-0.06, +0.02].
  4. G1 — CẤM '...' và '<#s#>' giữa câu; chỉ một thẻ <#0.35#> sau dấu ':' trước câu trích.
  5. G2 — Kịch tính đặt GIỮA các câu (_pause_after 0.2–1.2 s).
  6. G6 — Lời đọc không đổi chữ so với kịch bản gốc.
"""
import json
import re
import sys
from pathlib import Path

W = Path(__file__).resolve().parent
SCRIPT = json.loads((W / "script_tap09.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.05": "N2"}

# Tốc độ gốc trong edition.CAST (bộ A): H 0.90 · D 0.95 · C 0.92 · N1 0.95 · N2 0.95
BASE_DELTA = {"H": -0.02, "D": -0.03, "C": -0.02, "N1": -0.02, "N2": -0.02}

ACT_MOOD = {
    ("1", "H"): ("neutral", 0), ("1", "N1"): ("sad", 0), ("1", "D"): ("neutral", 0),
    ("2", "H"): ("neutral", 0), ("2", "D"): ("neutral", 0), ("2", "C"): ("neutral", 0),
    ("3", "H"): ("neutral", 0), ("3", "C"): ("neutral", 0),
    ("4", "H"): ("neutral", 0), ("4", "D"): ("neutral", 0), ("4", "N2"): ("sad", 0), ("4", "C"): ("neutral", 0),
    ("5", "H"): ("neutral", 0), ("5", "D"): ("neutral", 0), ("5", "C"): ("neutral", 0),
}

# Câu then chốt cần pause_after thêm (kịch tính giữa các câu theo G2)
KEY_PAUSE = {
    "1.02#5": 0.8,
    "1.04#2": 0.7,
    "1.06#7": 0.8,
    "1.07#8": 1.0,
    "1.09#3": 0.8,
    "1.10#5": 0.8,
    "1.11#3": 1.2,
    "2.02#3": 0.7,
    "2.04#2": 0.8,
    "2.05#5": 0.8,
    "2.06#4": 0.8,
    "2.07#4": 0.8,
    "2.08#5": 0.8,
    "2.09#4": 0.8,
    "2.10#3": 0.8,
    "2.11#2": 1.2,
    "3.02#6": 0.9,
    "3.03#2": 0.8,
    "3.04#4": 0.8,
    "3.05#5": 0.8,
    "3.06#4": 0.8,
    "3.07#5": 0.8,
    "3.08#2": 0.9,
    "3.09#4": 0.8,
    "3.10#2": 1.2,
    "4.02#2": 0.8,
    "4.03#3": 0.8,
    "4.04#3": 0.8,
    "4.05#3": 1.0,
    "4.07#4": 0.8,
    "4.08#4": 0.8,
    "4.09#3": 0.8,
    "4.10#6": 0.8,
    "4.11#2": 1.2,
    "5.02#6": 0.8,
    "5.03#3": 0.8,
    "5.04#3": 0.8,
    "5.05#4": 0.6,
    "5.05#7": 0.6,
    "5.05#10": 0.6,
    "5.05#13": 0.6,
    "5.05#17": 1.0,
    "5.05#18": 1.5,
}

def main():
    acting = {}
    pause_after = {}

    for elem in SCRIPT:
        if elem.get("kind") != "LOI":
            continue
        act = str(elem.get("act", 1))
        role = N_ELEMENT.get(elem["id"], elem.get("role", "H"))
        mood, pitch = ACT_MOOD.get((act, role), ("neutral", 0))
        delta_spd = BASE_DELTA.get(role, 0.0)

        for s in elem.get("sentences", []):
            sid = s["id"]
            pause = KEY_PAUSE.get(sid, 0.3)
            pause_after[sid] = pause
            acting[sid] = [mood, delta_spd, 0, None]

    acting["_pause_after"] = pause_after
    out_p = W / "acting_tap09.json"
    out_p.write_text(json.dumps(acting, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(acting)-1} acting items to {out_p}")

if __name__ == "__main__":
    main()
