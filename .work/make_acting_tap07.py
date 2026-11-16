#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/acting_tap07.json — diễn xuất từng câu cho bản tiếng Việt Tập 07 (Michelle Carter & Conrad Roy).

Tuân thủ nghiêm ngặt quy tắc giọng đọc kênh AMBER EYES (AGENTS.md & TIÊU CHUẨN):
  1. G5 — Cao độ (pitch) LUÔN = 0 (bảo toàn danh tính vai, tránh lỗi '3 Host').
  2. G3 — Chỉ dùng 4 cảm xúc an toàn: neutral · sad · fearful · surprised.
  3. G4 — Lệch tốc độ kẹp chặt trong [-0.06, +0.02].
  4. G1 — CẤM '...' và '<#s#>' giữa câu; chỉ một thẻ <#0.35#> sau dấu ':' trước câu trích.
  5. G2 & A13 — Kịch tính đặt GIỮA các câu (_pause_after 0.3–1.2 s, trung vị >= 0.6 s, <= 25% < 0.4 s).
  6. G6 — Lời đọc không đổi chữ so với kịch bản gốc, chỉ thay số đặc biệt khi đọc (G11).
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

W = Path(__file__).resolve().parent
SCRIPT = json.loads((W / "script_tap07.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.03": "N2"}

# Tốc độ gốc trong edition.CAST (bộ A): H 0.90 · D 0.95 · C 0.92 · N1 0.95 · N2 0.95
BASE_DELTA = {"H": -0.04, "D": -0.05, "C": -0.04, "N1": -0.03, "N2": -0.02}

# Mặc định theo hồi và vai: (cảm xúc, cao độ)
ACT_MOOD = {
    ("1", "H"): ("neutral", 0), ("1", "N1"): ("sad", 0), ("1", "D"): ("neutral", 0), ("1", "C"): ("neutral", 0),
    ("2", "H"): ("neutral", 0), ("2", "D"): ("neutral", 0), ("2", "C"): ("neutral", 0),
    ("3", "H"): ("neutral", 0), ("3", "C"): ("neutral", 0), ("3", "D"): ("neutral", 0),
    ("4", "H"): ("neutral", 0), ("4", "N2"): ("fearful", 0), ("4", "D"): ("neutral", 0), ("4", "C"): ("neutral", 0),
    ("5", "H"): ("neutral", 0), ("5", "C"): ("neutral", 0),
}

# Lời đọc số đặc biệt (K7/G11):
SPOKEN = {
    "4.08#5": [("911", "chín một một")],
    "5.04#14": [("096 306 1414", "không chín sáu, ba không sáu, một bốn một bốn"),
                ("Tổng đài Quốc gia Bảo vệ Trẻ em 111", "Tổng đài Quốc gia Bảo vệ Trẻ em một một một")],
    "5.04#15": [("988", "chín tám tám")],
}

SAFE_EMO = ("neutral", "sad", "fearful", "surprised")


def soften(raw):
    """Quy tắc G1: chỉ được một thẻ <#0.35#> sau dấu ':' đứng trước câu trích."""
    if ":" in raw and ("“" in raw or '"' in raw):
        k = raw.find(":")
        if k < len(raw) - 1 and raw[k + 1] in ' "“':
            raw = raw[:k + 1] + " <#0.35#>" + raw[k + 1:]
    s = raw.replace("“", "").replace("”", "").replace('"', "")
    return s


def pause_for(elems, idx, s_idx, n_sent, role, text):
    """Tính nhịp nghỉ kịch tính giữa câu tuân thủ A13."""
    is_last = (s_idx == n_sent - 1)
    if is_last:
        nxt = elems[idx + 1]["kind"] if idx + 1 < len(elems) else "END"
        if nxt in ("NGHI", "SFX", "END"):
            return 1.0
        if role in ("N1", "N2"):
            return 0.8
        return 0.6
    # Trong cùng lượt thoại
    t_clean = text.rstrip("”\" ").strip()
    if t_clean.endswith("?"):
        return 0.5
    if len(text.split()) >= 25:
        return 0.4
    return 0.3


def main():
    acting = {}
    pause_after = {}

    for idx, e in enumerate(SCRIPT):
        if e.get("kind") != "LOI":
            continue
        role = N_ELEMENT.get(e["id"], e.get("role", "H"))
        act = str(e.get("act", 1))
        emo0, pitch0 = ACT_MOOD.get((act, role), ("neutral", 0))
        delta_spd = BASE_DELTA.get(role, 0.0)

        sents = e.get("sentences", [])
        n = len(sents)
        for k, s in enumerate(sents):
            sid = s["id"]
            raw_text = s["text"]
            text_no_quotes = raw_text.replace("“", "").replace("”", "").replace('"', "")
            words = len(text_no_quotes.split())

            emo = emo0
            if text_no_quotes.rstrip().endswith("?"):
                emo = "surprised"
            elif role == "N1" or "thảm kịch" in raw_text or "tuyệt vọng" in raw_text:
                emo = "sad"
            elif role == "N2" or "hoảng sợ" in raw_text or "rùng mình" in raw_text:
                emo = "fearful"

            if emo not in SAFE_EMO:
                emo = "neutral"

            dsp = delta_spd + (-0.02 if words <= 8 else 0.01 if words >= 30 else 0.0)
            dsp = max(-0.06, min(0.02, round(dsp, 2)))

            # G5: Cao độ LUÔN = 0
            pitch = 0

            # Lời đọc riêng (soften & SPOKEN)
            alt = soften(raw_text)
            for src, dst in SPOKEN.get(sid, []):
                assert src in alt, f"SPOKEN mismatch in {sid}: {src} not in {alt}"
                alt = alt.replace(src, dst)
            if alt == text_no_quotes:
                alt = None

            acting[sid] = [emo, dsp, pitch, alt]

            # Nhịp nghỉ A13
            p = pause_for(SCRIPT, idx, k, n, role, raw_text)
            pause_after[sid] = p

    out = {
        "_doc": "Bảng diễn xuất Tập 07 (Michelle Carter & Conrad Roy) — chuẩn A2 (219 câu) — sinh bởi make_acting_tap07.py",
        "_pause_after": pause_after,
        **acting
    }
    out_p = W / "acting_tap07.json"
    out_p.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    # Bản JA kế thừa cùng nhịp nghỉ và cảm xúc
    ja = {
        "_doc": "Bảng diễn xuất Tập 07 JA — chuẩn A2 (219 câu) — sinh bởi make_acting_tap07.py",
        "_pause_after": pause_after,
        **{k: ([v[0], v[1], 0, None] if not k.startswith("_") else v) for k, v in acting.items()}
    }
    out_ja = W / "acting_tap07_JA.json"
    out_ja.write_text(json.dumps(ja, ensure_ascii=False, indent=1), encoding="utf-8")

    print(f"Thành công: {len(acting)} câu.")
    print(f"  _pause_after: {len(pause_after)} mốc (tổng {sum(pause_after.values()):.1f} s)")
    print(f"  Ghi file: {out_p} và {out_ja}")


if __name__ == "__main__":
    main()
