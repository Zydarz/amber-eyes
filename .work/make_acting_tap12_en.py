#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh file diễn xuất TTS cho bản tiếng Anh Tập 12 -> .work/acting_tap12_EN.json.

Nguyên tắc:
  * Cảm xúc lấy từ ACT_MOOD của vai, chỉ giữ bộ 4 an toàn: neutral, sad, fearful, surprised;
  * CAO ĐỘ LUÔN = 0 (G5);
  * Lệch tốc độ = lệch trong BASE_DELTA hoặc theo độ dài câu, kẹp trong [-0.06, +0.02] (G4);
  * Lời đọc riêng = CÂU GỐC EN + đúng một thẻ <#0.35#> sau dấu ':' đứng trước câu trích (G1/G6);
  * _pause_after = khớp với bản VN theo mạch hồi và kết thúc lượt thoại (G2/A13).
"""
import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

sys.path.insert(0, str(W))
import make_acting_tap12 as VN  # noqa: E402

SCRIPT = json.loads((W / "script_tap12_EN.json").read_text(encoding="utf-8"))
VN_ACTING = json.loads((W / "acting_tap12.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.10": "N2"}
SAFE_EMO = {"neutral", "sad", "fearful", "surprised"}

SHORT_W, MID1_W, MID2_W = 10, 16, 22
DSP_MIN, DSP_MAX = -0.06, 0.02

def strip_quotes(t):
    return t.replace("“", "").replace("”", "").replace('"', "").replace("‘", "").replace("’", "")

def soften_en(raw):
    q = raw.find("“")
    if q > 0:
        k = raw.rfind(":", 0, q)
        if k >= 0:
            raw = raw[:k + 1] + " <#0.35#>" + raw[k + 1:]
    return strip_quotes(raw)

def main():
    acting = {}
    for e in SCRIPT:
        if e["kind"] != "LOI":
            continue
        role = N_ELEMENT.get(e["id"], e["role"])
        act = str(e.get("act", 1))
        emo0, pitch0 = VN.ACT_MOOD.get((act, role), ("neutral", 0))
        base_dsp = VN.BASE_DELTA.get(role, 0.0)

        for k, s in enumerate(e["sentences"], 1):
            sid = s["id"]
            text = strip_quotes(s["text"])
            words = len(text.split())

            emo = emo0
            if text.rstrip().endswith("?"):
                emo = "surprised"
            if emo not in SAFE_EMO:
                emo = "neutral"

            if words <= SHORT_W:
                dsp = base_dsp - 0.01
            elif words <= MID1_W:
                dsp = base_dsp
            elif words <= MID2_W:
                dsp = base_dsp + 0.005
            else:
                dsp = base_dsp + 0.01
            dsp = max(DSP_MIN, min(DSP_MAX, round(dsp, 2)))

            aside = soften_en(s["text"])
            if aside == text:
                aside = None

            acting[sid] = [emo, dsp, 0, aside]

    acting["_doc"] = (
        "Diễn xuất từng câu cho TTS bản tiếng Anh Tập 12. id: [cảm xúc, lệch tốc độ, 0, aside]. "
        "Pitch luôn = 0 (G5); cảm xúc safe 4; speed clamp G4; pause_after kế thừa từ VN (A13)."
    )
    acting["_pause_after"] = VN_ACTING.get("_pause_after", {})

    out_p = W / "acting_tap12_EN.json"
    out_p.write_text(json.dumps(acting, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Created {out_p.name} with {len(acting) - 2} items.")

if __name__ == "__main__":
    main()
