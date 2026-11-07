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

# Kịch bản viết lại 05/11/2026 (53 phần tử · 171 câu): mã câu cũ KHÔNG còn đúng (K4).
# Nghỉ kịch tính tính theo CẤU TRÚC, không theo mã câu cứng: câu cuối mỗi lượt thoại 0,8 s ·
# câu cuối lượt N1/N2 1,0 s · câu cuối lượt đứng ngay trước thẻ [NGHỈ]/[SFX] 1,2 s ·
# câu đầu lời mở "Đúng tám giờ sáng" 0,5 s. Còn lại 0,3 s.
KEY_PAUSE = {"1.02#3": 0.5}


def pause_for(elems, idx, s_idx, n_sent, role):
    if s_idx != n_sent - 1:
        return None
    nxt = elems[idx + 1]["kind"] if idx + 1 < len(elems) else "END"
    if nxt in ("NGHI", "SFX", "END"):
        return 1.2
    return 1.0 if role in ("N1", "N2") else 0.8


def main():
    acting = {}
    pause_after = {}

    for idx, elem in enumerate(SCRIPT):
        if elem.get("kind") != "LOI":
            continue
        act = str(elem.get("act", 1))
        role = N_ELEMENT.get(elem["id"], elem.get("role", "H"))
        mood, pitch = ACT_MOOD.get((act, role), ("neutral", 0))
        delta_spd = BASE_DELTA.get(role, 0.0)

        sents = elem.get("sentences", [])
        for k, s in enumerate(sents):
            sid = s["id"]
            orig_text = s["text"]
            pause = KEY_PAUSE.get(sid) or pause_for(SCRIPT, idx, k, len(sents), role) or 0.3
            pause_after[sid] = pause
            acting[sid] = [mood, delta_spd, 0, None]

    acting["_pause_after"] = pause_after
    out_p = W / "acting_tap08.json"
    out_p.write_text(json.dumps(acting, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(acting)-1} acting items to {out_p}")
    ja = {k: ([v[0], v[1], 0, None] if not k.startswith("_") else v) for k, v in acting.items()}
    (W / "acting_tap08_JA.json").write_text(json.dumps(ja, ensure_ascii=False, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
