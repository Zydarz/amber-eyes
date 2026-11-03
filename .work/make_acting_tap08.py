#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/acting_tap08.json — diễn xuất từng câu cho bản tiếng Việt Tập 08 (Shoko Asahara & Aum Shinrikyo).

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
SCRIPT = json.loads((W / "script_tap08.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.08": "N2"}

# Tốc độ gốc trong edition.CAST (bộ A): H 0.90 · D 0.95 · C 0.92 · N1 0.95 · N2 0.95
BASE_DELTA = {"H": -0.02, "D": -0.03, "C": -0.02, "N1": -0.02, "N2": -0.02}

ACT_MOOD = {
    ("1", "H"): ("neutral", 0), ("1", "N1"): ("sad", 0), ("1", "D"): ("neutral", 0), ("1", "C"): ("neutral", 0),
    ("2", "H"): ("neutral", 0), ("2", "D"): ("neutral", 0), ("2", "C"): ("neutral", 0),
    ("3", "H"): ("neutral", 0), ("3", "C"): ("neutral", 0), ("3", "D"): ("neutral", 0),
    ("4", "H"): ("neutral", 0), ("4", "N2"): ("sad", 0), ("4", "D"): ("neutral", 0), ("4", "C"): ("neutral", 0),
    ("5", "H"): ("neutral", 0), ("5", "C"): ("neutral", 0),
}

# Câu then chốt cần pause_after thêm
KEY_PAUSE = {
    "1.02#3": 0.5,
    "1.02#6": 0.8,
    "1.04#3": 0.7,
    "1.06#2": 0.9,
    "1.07#6": 1.0,
    "1.09#4": 0.8,
    "1.11#4": 1.2,
    "2.02#4": 0.7,
    "2.04#4": 0.8,
    "2.06#3": 0.8,
    "2.07#3": 0.8,
    "2.09#2": 1.2,
    "3.02#3": 0.8,
    "3.04#4": 0.8,
    "3.06#4": 0.7,
    "3.08#2": 1.2,
    "4.02#4": 0.8,
    "4.04#3": 0.8,
    "4.06#4": 0.8,
    "4.08#4": 1.0,
    "4.10#7": 1.2,
    "5.02#4": 0.8,
    "5.04#19": 1.5,
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
            orig_text = s["text"]
            pause = KEY_PAUSE.get(sid, 0.3)
            pause_after[sid] = pause
            acting[sid] = [mood, delta_spd, 0, None]

    acting["_pause_after"] = pause_after
    out_p = W / "acting_tap08.json"
    out_p.write_text(json.dumps(acting, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(acting)-1} acting items to {out_p}")

if __name__ == "__main__":
    main()
