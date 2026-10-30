#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/acting_tap04.json — diễn xuất từng câu cho bản tiếng Việt Tập 04 (vụ Charles Cullen).

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
SCRIPT = json.loads((W / "script_tap04.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.06": "N2"}

# Tốc độ gốc trong edition.CAST (bộ A): H 0.90 · D 0.95 · C 0.92 · N1 0.95 · N2 0.95
BASE_DELTA = {"H": -0.04, "D": -0.05, "C": -0.04, "N1": -0.03, "N2": -0.02}

# Mặc định theo hồi và vai: (cảm xúc, cao độ)
ACT_MOOD = {
    ("1", "H"): ("neutral", 0), ("1", "N1"): ("neutral", 0), ("1", "D"): ("neutral", 0),
    ("2", "H"): ("neutral", 0), ("2", "D"): ("neutral", 0), ("2", "C"): ("neutral", 0),
    ("3", "H"): ("neutral", 0), ("3", "C"): ("neutral", 0),
    ("4", "H"): ("neutral", 0), ("4", "D"): ("neutral", 0), ("4", "N2"): ("sad", 0),
    ("5", "H"): ("neutral", 0), ("5", "C"): ("neutral", 0), ("5", "D"): ("neutral", 0),
}

# Các câu then chốt: [cảm xúc, lệch tốc độ (thêm vào BASE_DELTA), cao độ, alt_text | None, nghỉ thêm sau câu (s)]
KEY = {
    # ── HỒI 1 — Ca trực đêm Somerset, Cha Gall tử vong, hé lộ 400 nạn nhân ──────────
    "1.03#1": ["neutral", -0.01, 0, None, 0.4],
    "1.03#4": ["neutral", -0.01, 0, None, 0.3],
    "1.05#2": ["neutral", 0.0, 0, None, 0.2],
    "1.05#3": ["neutral", -0.01, 0, None, 0.4],
    "1.07#1": ["neutral", 0.0, 0, None, 0.2],
    "1.07#4": ["sad", -0.01, 0, None, 0.5],
    "1.08#1": ["fearful", -0.01, 0, None, 0.3],
    "1.08#2": ["neutral", 0.0, 0, None, 0.2],
    "1.08#3": ["fearful", -0.02, 0, None, 0.8],
    "1.10#1": ["fearful", -0.01, 0, None, 0.4],
    "1.10#2": ["neutral", -0.01, 0, None, 0.3],
    "1.10#3": ["sad", -0.02, 0, None, 0.8],
    "1.12#1": ["neutral", 0.0, 0, None, 0.3],
    "1.14#1": ["neutral", 0.0, 0, None, 0.2],
    "1.14#3": ["neutral", -0.01, 0, None, 0.4],
    "1.14#4": ["fearful", -0.01, 0, None, 0.4],
    "1.14#5": ["neutral", 0.0, 0, None, 0.3],
    "1.14#6": ["fearful", -0.02, 0, None, 1.0],
    "1.16#1": ["neutral", 0.0, 0, None, 0.2],
    "1.16#2": ["neutral", -0.01, 0, None, 0.5],

    # ── HỒI 2 — Hiện trường vô trùng, thủ đoạn Pyxis, Somerset ém nhẹm 90 ngày ───────
    "2.02#1": ["neutral", 0.0, 0, None, 0.2],
    "2.02#2": ["neutral", -0.01, 0, None, 0.3],
    "2.02#3": ["fearful", -0.02, 0, None, 0.6],
    "2.04#1": ["neutral", -0.01, 0, None, 0.3],
    "2.04#2": ["neutral", 0.0, 0, None, 0.3],
    "2.06#1": ["neutral", 0.0, 0, None, 0.2],
    "2.06#4": ["neutral", -0.01, 0, None, 0.3],
    "2.06#7": ["neutral", 0.0, 0, None, 0.2],
    "2.06#8": ["neutral", -0.01, 0, None, 0.4],
    "2.06#9": ["neutral", 0.0, 0, None, 0.3],
    "2.06#10": ["fearful", -0.01, 0, None, 0.3],
    "2.06#11": ["fearful", -0.02, 0, None, 0.8],
    "2.07#1": ["sad", -0.01, 0, None, 0.3],
    "2.07#2": ["neutral", 0.0, 0, None, 0.2],
    "2.07#4": ["neutral", 0.0, 0, None, 0.3],
    "2.08#1": ["neutral", 0.0, 0, None, 0.2],
    "2.08#3": ["neutral", 0.0, 0, None, 0.3],
    "2.08#4": ["surprised", 0.01, 0, None, 0.4],
    "2.08#5": ["sad", -0.01, 0, None, 0.5],
    "2.08#6": ["sad", -0.02, 0, None, 0.8],
    "2.10#1": ["surprised", 0.0, 0, None, 0.4],
    "2.10#3": ["neutral", 0.0, 0, None, 0.3],
    "2.11#1": ["neutral", -0.01, 0, None, 0.3],
    "2.11#3": ["sad", -0.01, 0, None, 0.3],
    "2.11#5": ["sad", -0.01, 0, None, 0.3],
    "2.11#6": ["neutral", 0.0, 0, None, 0.4],
    "2.11#7": ["surprised", 0.0, 0, None, 0.3],
    "2.11#8": ["neutral", -0.01, 0, None, 0.3],
    "2.11#10": ["sad", -0.02, 0, None, 0.8],

    # ── HỒI 3 — Phức cảm Chúa trời, cơ chế ngụy biện, bẻ gãy mặt nạ ─────────────────
    "3.02#2": ["neutral", -0.01, 0, None, 0.4],
    "3.02#3": ["sad", -0.02, 0, None, 0.5],
    "3.02#4": ["neutral", 0.0, 0, None, 0.3],
    "3.02#5": ["fearful", -0.01, 0, None, 0.4],
    "3.02#6": ["neutral", 0.0, 0, None, 0.3],
    "3.04#1": ["sad", -0.01, 0, None, 0.3],
    "3.04#3": ["sad", -0.01, 0, None, 0.3],
    "3.04#4": ["sad", -0.02, 0, None, 0.6],
    "3.04#6": ["neutral", -0.01, 0, None, 0.6],
    "3.06#1": ["sad", -0.01, 0, None, 0.3],
    "3.06#2": ["neutral", 0.0, 0, None, 0.3],
    "3.07#1": ["neutral", 0.0, 0, None, 0.2],
    "3.07#4": ["fearful", -0.02, 0, None, 0.6],
    "3.07#5": ["fearful", -0.01, 0, None, 0.6],
    "3.08#1": ["fearful", -0.01, 0, None, 0.3],
    "3.08#2": ["neutral", 0.0, 0, None, 0.4],
    "3.09#1": ["neutral", 0.0, 0, None, 0.3],
    "3.09#5": ["neutral", 0.0, 0, None, 0.3],
    "3.09#6": ["fearful", -0.01, 0, None, 0.5],
    "3.09#7": ["fearful", -0.02, 0, None, 0.8],
    "3.10#1": ["sad", -0.01, 0, None, 0.3],
    "3.10#2": ["sad", -0.01, 0, None, 0.4],
    "3.10#3": ["neutral", -0.01, 0, None, 0.8],

    # ── HỒI 4 — Đấu trí thẩm vấn, Amy Loughren, phá vỡ phòng hỏi cung ───────────────
    "4.02#1": ["neutral", 0.0, 0, None, 0.3],
    "4.02#3": ["sad", -0.01, 0, None, 0.3],
    "4.02#5": ["neutral", -0.01, 0, None, 0.5],
    "4.04#1": ["fearful", -0.01, 0, None, 0.3],
    "4.04#2": ["neutral", 0.0, 0, None, 0.3],
    "4.04#3": ["fearful", -0.02, 0, None, 0.6],
    "4.04#5": ["neutral", -0.01, 0, None, 0.6],
    "4.06#1": ["sad", -0.01, 0, None, 0.3],
    "4.06#2": ["sad", -0.01, 0, None, 0.3],
    "4.06#5": ["fearful", -0.02, 0, None, 0.8],
    "4.08#1": ["fearful", -0.01, 0, None, 0.3],
    "4.08#3": ["fearful", -0.01, 0, None, 0.4],
    "4.08#5": ["fearful", -0.02, 0, None, 0.8],
    "4.11#1": ["neutral", 0.0, 0, None, 0.3],
    "4.11#3": ["neutral", -0.01, 0, None, 0.5],
    "4.12#1": ["neutral", -0.01, 0, None, 0.3],
    "4.12#3": ["sad", -0.01, 0, None, 0.3],
    "4.12#4": ["neutral", 0.0, 0, None, 0.3],
    "4.12#5": ["sad", -0.01, 0, None, 0.5],
    "4.12#6": ["sad", -0.01, 0, None, 0.5],
    "4.12#8": ["sad", -0.02, 0, None, 0.6],
    "4.12#9": ["sad", -0.01, 0, None, 0.5],
    "4.12#10": ["fearful", -0.02, 0, None, 1.0],

    # ── HỒI 5 — Phán quyết 18 chung thân, Đạo luật Cullen, 4 cảnh báo đỏ ────────────
    "5.02#1": ["neutral", 0.0, 0, None, 0.3],
    "5.02#2": ["neutral", 0.0, 0, None, 0.3],
    "5.02#3": ["neutral", -0.01, 0, None, 0.4],
    "5.02#4": ["neutral", -0.02, 0, None, 0.8],
    "5.02#5": ["neutral", -0.01, 0, None, 0.4],
    "5.02#6": ["sad", -0.01, 0, None, 0.6],
    "5.04#1": ["sad", -0.01, 0, None, 0.3],
    "5.04#2": ["sad", -0.02, 0, None, 0.6],
    "5.04#4": ["neutral", -0.01, 0, None, 0.5],
    "5.04#6": ["neutral", -0.01, 0, None, 0.5],
    "5.05#1": ["neutral", 0.0, 0, None, 0.3],
    "5.05#3": ["neutral", 0.0, 0, None, 0.4],
    "5.06#1": ["neutral", 0.0, 0, None, 0.3],
    "5.06#3": ["neutral", 0.0, 0, None, 0.4],
    "5.08#1": ["sad", -0.01, 0, None, 0.4],
    "5.08#2": ["fearful", -0.01, 0, None, 0.4],
    "5.08#3": ["sad", -0.02, 0, None, 0.6],
    "5.08#4": ["neutral", -0.01, 0, None, 0.8],
    "5.10#1": ["neutral", 0.0, 0, None, 0.3],
    "5.10#2": ["neutral", 0.0, 0, None, 0.3],
    "5.10#3": ["neutral", -0.01, 0, None, 1.0],
}


def auto_pauses(t):
    """Chỉ thêm một thẻ ngắt <#0.35#> sau dấu ':' đứng trước câu trích theo quy tắc G1."""
    return t


def soften(raw):
    """Quy tắc G1: CẤM '...' và thẻ ngắt giữa câu. Chỉ cho phép MỘT thẻ <#0.35#> sau dấu ':' trước trích dẫn."""
    q = raw.find("“")
    if q > 0:
        k = raw.rfind(":", 0, q)
        if k >= 0:
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
        "_doc": "Bảng diễn xuất Tập 04 (Charles Cullen) — bộ tham số an toàn (G1-G11) — sinh bởi make_acting_tap04.py",
        "_pause_after": pause_after,
        **acting
    }
    (W / "acting_tap04.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter
    emos = Counter(v[0] for v in acting.values())
    dsps = Counter(v[1] for v in acting.values())
    print(f"Thành công: {len(acting)} câu · {len(KEY)} mốc then chốt ({len(KEY)/len(acting)*100:.0f}%)")
    print(f"  Cảm xúc: {dict(emos)}")
    print(f"  Lệch tốc độ: {dict(sorted(dsps.items()))}")
    print(f"  Lời đọc riêng: {sum(1 for v in acting.values() if v[3])} câu có thẻ trích dẫn")
    print(f"  Nghỉ thêm (_pause_after): {len(pause_after)} mốc (tổng {sum(pause_after.values()):.1f} s)")
    print(f"  Ghi file: {W / 'acting_tap04.json'}")


if __name__ == "__main__":
    main()
