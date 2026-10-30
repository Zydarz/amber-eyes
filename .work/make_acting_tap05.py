#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/acting_tap05.json — diễn xuất từng câu cho bản tiếng Việt Tập 05 (Dennis Rader - BTK).

Tuân thủ nghiêm ngặt quy tắc giọng đọc kênh AMBER EYES (AGENTS.md & TIÊU CHUẨN):
  1. G5 — Cao độ (pitch) LUÔN = 0 (bảo toàn danh tính vai, tránh lỗi '3 Host').
  2. G3 — Chỉ dùng 4 cảm xúc an toàn: neutral · sad · fearful · surprised.
  3. G4 — Lệch tốc độ kẹp chặt trong [-0.06, +0.02].
  4. G1 — CẤM '...' và '<#s#>' giữa câu; chỉ một thẻ <#0.35#> sau dấu ':' trước câu trích.
  5. G2 — Kịch tính đặt GIỮA các câu (_pause_after 0.2–1.0 s).
  6. G6 — Lời đọc không đổi chữ so với kịch bản gốc.
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

W = Path(__file__).resolve().parents[1] / ".work"
SCRIPT = json.loads((W / "script_tap05.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.09": "N1", "4.15": "N2"}

# Tốc độ gốc trong edition.CAST (bộ A): H 0.90 · D 0.95 · C 0.92 · N1 0.95 · N2 0.95
BASE_DELTA = {"H": -0.04, "D": -0.05, "C": -0.04, "N1": -0.03, "N2": -0.02}

# Mặc định theo hồi và vai: (cảm xúc, cao độ)
ACT_MOOD = {
    ("1", "H"): ("neutral", 0), ("1", "N1"): ("neutral", 0), ("1", "D"): ("neutral", 0),
    ("2", "H"): ("neutral", 0), ("2", "D"): ("neutral", 0),
    ("3", "H"): ("neutral", 0), ("3", "C"): ("neutral", 0),
    ("4", "H"): ("neutral", 0), ("4", "D"): ("neutral", 0), ("4", "N2"): ("sad", 0),
    ("5", "H"): ("neutral", 0), ("5", "C"): ("neutral", 0), ("5", "D"): ("neutral", 0),
}

# Các câu then chốt: [cảm xúc, lệch tốc độ (thêm vào BASE_DELTA), cao độ, alt_text | None, nghỉ thêm sau câu (s)]
KEY = {
    # ── HỒI 1 — Bức thư tái xuất sau 13 năm lặng căm, cú sốc Park City ────────────
    "1.03#1": ["neutral", -0.01, 0, None, 0.4],
    "1.03#4": ["neutral", -0.01, 0, None, 0.3],
    "1.03#5": ["fearful", -0.02, 0, None, 0.8],
    "1.05#1": ["neutral", 0.0, 0, None, 0.2],
    "1.05#3": ["neutral", -0.01, 0, None, 0.4],
    "1.05#4": ["fearful", -0.01, 0, None, 0.5],
    "1.05#5": ["sad", -0.02, 0, None, 0.8],
    "1.07#1": ["neutral", 0.0, 0, None, 0.3],
    "1.09#1": ["fearful", -0.01, 0, None, 0.3],
    "1.09#2": ["fearful", -0.01, 0, None, 0.4],
    "1.09#3": ["surprised", -0.02, 0, None, 0.8],
    "1.10#1": ["neutral", -0.01, 0, None, 0.4],
    "1.10#4": ["neutral", 0.0, 0, None, 0.3],
    "1.10#5": ["surprised", 0.0, 0, None, 0.4],
    "1.10#7": ["fearful", -0.02, 0, None, 0.8],
    "1.12#1": ["neutral", 0.0, 0, None, 0.3],
    "1.14#1": ["neutral", 0.0, 0, None, 0.3],
    "1.14#5": ["neutral", -0.01, 0, None, 0.4],
    "1.14#6": ["fearful", -0.01, 0, None, 0.5],
    "1.14#7": ["fearful", -0.02, 0, None, 0.9],
    "1.16#1": ["neutral", 0.0, 0, None, 0.2],
    "1.16#3": ["neutral", -0.01, 0, None, 0.6],

    # ── HỒI 2 — Hiện trường tội ác, chữ ký BTK, vỏ bọc hoàn hảo 30 năm ───────────
    "2.02#1": ["neutral", 0.0, 0, None, 0.2],
    "2.02#3": ["fearful", -0.01, 0, None, 0.4],
    "2.02#4": ["fearful", -0.02, 0, None, 0.6],
    "2.04#1": ["neutral", 0.0, 0, None, 0.3],
    "2.04#3": ["fearful", -0.01, 0, None, 0.5],
    "2.04#6": ["neutral", -0.01, 0, None, 0.4],
    "2.04#10": ["neutral", -0.01, 0, None, 0.5],
    "2.05#1": ["neutral", 0.0, 0, None, 0.2],
    "2.05#3": ["surprised", 0.0, 0, None, 0.4],
    "2.05#4": ["neutral", 0.0, 0, None, 0.3],
    "2.06#1": ["neutral", 0.0, 0, None, 0.2],
    "2.06#3": ["neutral", 0.0, 0, None, 0.2],
    "2.06#4": ["neutral", 0.0, 0, None, 0.2],
    "2.06#5": ["neutral", 0.0, 0, None, 0.3],
    "2.06#6": ["neutral", 0.0, 0, None, 0.3],
    "2.06#7": ["fearful", -0.02, 0, None, 0.8],
    "2.07#1": ["neutral", -0.01, 0, None, 0.3],
    "2.07#2": ["fearful", -0.02, 0, None, 0.5],
    "2.07#3": ["surprised", 0.0, 0, None, 0.4],
    "2.07#4": ["neutral", 0.0, 0, None, 0.4],

    # ── HỒI 3 — Phân mảnh tâm trí, ảo tưởng Nhân tố X, ái kỷ ác tính ─────────────
    "3.02#1": ["neutral", -0.01, 0, None, 0.3],
    "3.02#3": ["neutral", 0.0, 0, None, 0.3],
    "3.02#5": ["neutral", -0.01, 0, None, 0.4],
    "3.02#7": ["fearful", -0.02, 0, None, 0.6],
    "3.04#1": ["neutral", 0.0, 0, None, 0.3],
    "3.04#3": ["neutral", 0.0, 0, None, 0.4],
    "3.05#1": ["neutral", 0.0, 0, None, 0.3],
    "3.05#4": ["fearful", -0.01, 0, None, 0.5],
    "3.05#5": ["neutral", -0.01, 0, None, 0.5],
    "3.06#1": ["neutral", 0.0, 0, None, 0.3],
    "3.06#3": ["surprised", 0.0, 0, None, 0.4],
    "3.07#1": ["neutral", -0.01, 0, None, 0.3],
    "3.07#2": ["neutral", 0.0, 0, None, 0.3],
    "3.07#4": ["neutral", -0.01, 0, None, 0.4],
    "3.07#5": ["fearful", -0.01, 0, None, 0.4],
    "3.07#6": ["sad", -0.02, 0, None, 0.8],
    "3.07#7": ["sad", -0.02, 0, None, 0.8],
    "3.08#1": ["fearful", -0.01, 0, None, 0.3],
    "3.08#3": ["neutral", -0.01, 0, None, 0.5],

    # ── HỒI 4 — Bẫy công nghệ đĩa mềm tím, bắt giữ, Kerri Rawson sụp đổ ─────────
    "4.02#1": ["neutral", 0.0, 0, None, 0.3],
    "4.02#4": ["neutral", -0.01, 0, None, 0.3],
    "4.02#6": ["surprised", 0.0, 0, None, 0.4],
    "4.02#7": ["neutral", -0.01, 0, None, 0.4],
    "4.02#9": ["neutral", -0.01, 0, None, 0.5],
    "4.04#1": ["neutral", 0.0, 0, None, 0.2],
    "4.04#3": ["neutral", 0.0, 0, None, 0.3],
    "4.04#5": ["neutral", -0.01, 0, None, 0.4],
    "4.04#8": ["fearful", -0.02, 0, None, 0.8],
    "4.06#1": ["neutral", -0.01, 0, None, 0.3],
    "4.06#4": ["surprised", 0.0, 0, None, 0.4],
    "4.06#5": ["fearful", -0.01, 0, None, 0.4],
    "4.06#6": ["fearful", -0.02, 0, None, 0.8],
    "4.08#1": ["neutral", 0.0, 0, None, 0.3],
    "4.08#3": ["surprised", -0.01, 0, None, 0.5],
    "4.08#5": ["neutral", 0.0, 0, None, 0.3],
    "4.08#8": ["neutral", -0.01, 0, None, 0.4],
    "4.08#9": ["neutral", -0.02, 0, None, 0.8],
    "4.10#1": ["neutral", -0.01, 0, None, 0.3],
    "4.10#2": ["fearful", -0.01, 0, None, 0.4],
    "4.10#4": ["neutral", -0.01, 0, None, 0.4],
    "4.12#1": ["neutral", 0.0, 0, None, 0.3],
    "4.12#4": ["surprised", 0.0, 0, None, 0.4],
    "4.12#6": ["fearful", -0.01, 0, None, 0.4],
    "4.12#8": ["fearful", -0.02, 0, None, 0.8],
    "4.14#1": ["sad", -0.01, 0, None, 0.3],
    "4.14#2": ["sad", -0.01, 0, None, 0.4],
    "4.15#1": ["sad", -0.01, 0, None, 0.4],
    "4.15#2": ["sad", -0.01, 0, None, 0.4],
    "4.15#3": ["sad", -0.02, 0, None, 0.5],
    "4.15#4": ["sad", -0.02, 0, None, 0.9],

    # ── HỒI 5 — Phán quyết 175 năm, 4 Cảnh báo đỏ, lời kết thức tỉnh ────────────
    "5.02#1": ["neutral", 0.0, 0, None, 0.3],
    "5.02#3": ["fearful", -0.02, 0, None, 0.8],
    "5.02#4": ["neutral", 0.0, 0, None, 0.3],
    "5.02#5": ["sad", -0.02, 0, None, 0.7],
    "5.04#1": ["neutral", -0.01, 0, None, 0.3],
    "5.04#2": ["neutral", 0.0, 0, None, 0.3],
    "5.05#1": ["neutral", 0.0, 0, None, 0.2],
    "5.05#3": ["neutral", -0.01, 0, None, 0.4],
    "5.05#4": ["neutral", 0.0, 0, None, 0.2],
    "5.05#5": ["fearful", -0.01, 0, None, 0.4],
    "5.06#1": ["neutral", 0.0, 0, None, 0.2],
    "5.06#3": ["fearful", -0.01, 0, None, 0.4],
    "5.06#4": ["neutral", 0.0, 0, None, 0.2],
    "5.06#5": ["fearful", -0.02, 0, None, 0.6],
    "5.08#1": ["neutral", 0.0, 0, None, 0.3],
    "5.08#3": ["sad", -0.01, 0, None, 0.4],
    "5.08#4": ["fearful", -0.01, 0, None, 0.4],
    "5.08#5": ["neutral", -0.02, 0, None, 0.8],
    "5.10#1": ["neutral", 0.0, 0, None, 0.2],
    "5.10#2": ["neutral", -0.01, 0, None, 0.3],
    "5.10#3": ["neutral", -0.02, 0, None, 0.8],
}


def soften(raw):
    """Quy tắc G1: chỉ được một thẻ <#0.35#> sau dấu ':' đứng trước câu trích."""
    if ":" in raw and ("“" in raw or '"' in raw):
        k = raw.find(":")
        if k < len(raw) - 1 and raw[k + 1] in ' "“':
            raw = raw[:k + 1] + " <#0.35#>" + raw[k + 1:]
    s = raw.replace("“", "").replace("”", "").replace('"', "")
    return s


SAFE_EMO = ("neutral", "sad", "fearful", "surprised")


def main():
    acting, pause_after = {}, {}
    unknown = []
    for e in SCRIPT:
        if e["kind"] != "LOI":
            continue
        role = N_ELEMENT.get(e["id"], e["role"])
        act = e["id"].split(".")[0]
        emo0, pitch0 = ACT_MOOD.get((act, role), ("neutral", 0))
        n = len(e["sentences"])
        for k, s in enumerate(e["sentences"], 1):
            sid = s["id"]
            text = s["text"].replace("“", "").replace("”", "").replace('"', "")
            words = len(text.split())
            if sid in KEY:
                emo, dsp, pitch, alt, after = KEY[sid]
                dsp = round(BASE_DELTA[role] + dsp, 2)
            else:
                emo, pitch = emo0, pitch0
                dsp = BASE_DELTA[role] + (-0.03 if words <= 8 else 0.01 if words >= 30 else 0.0)
                if text.rstrip().endswith("?"):
                    emo = "surprised"
                dsp = round(dsp, 2)
                after = 0.0
            # G5: Cao độ LUÔN = 0
            pitch = 0
            if emo not in SAFE_EMO:
                emo = "neutral"
            # G4: Kẹp lệch tốc độ trong [-0.06, +0.02]
            dsp = max(-0.06, min(0.02, dsp))
            # G1 & G6: Lời đọc không đổi chữ, chỉ thêm thẻ hợp lệ
            alt = soften(s["text"])
            if alt == text:
                alt = None
            acting[sid] = [emo, dsp, pitch, alt]
            # G2: Giữ khoảng lặng sau câu từ 0.3s trở lên
            if after >= 0.3:
                pause_after[sid] = after

    # Kiểm tra tính toàn vẹn: mọi KEY phải có trong kịch bản
    real = set(acting)
    for sid in KEY:
        if sid not in real:
            unknown.append(sid)
    if unknown:
        raise SystemExit(f"LỖI: KEY chứa câu không tồn tại trong kịch bản: {unknown}")

    out = {
        "_doc": "Bảng diễn xuất Tập 05 (Dennis Rader - BTK) — bộ tham số an toàn (G1-G11) — sinh bởi make_acting_tap05.py",
        "_pause_after": pause_after,
        **acting
    }
    (W / "acting_tap05.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter
    emos = Counter(v[0] for v in acting.values())
    dsps = Counter(v[1] for v in acting.values())
    print(f"Thành công: {len(acting)} câu · {len(KEY)} mốc then chốt ({len(KEY)/len(acting)*100:.0f}%)")
    print(f"  Cảm xúc: {dict(emos)}")
    print(f"  Lệch tốc độ: {dict(sorted(dsps.items()))}")
    print(f"  Lời đọc riêng: {sum(1 for v in acting.values() if v[3])} câu có thẻ trích dẫn")
    print(f"  Nghỉ thêm (_pause_after): {len(pause_after)} mốc (tổng {sum(pause_after.values()):.1f} s)")
    print(f"  Ghi file: {W / 'acting_tap05.json'}")


if __name__ == "__main__":
    main()
