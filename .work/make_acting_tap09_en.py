#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh file diễn xuất TTS cho bản tiếng Anh Tập 09 -> .work/acting_tap09_EN.json.

Nguyên tắc:
  * Cảm xúc lấy từ ACT_MOOD của vai, chỉ giữ bộ 4 an toàn: neutral, sad, fearful, surprised;
  * CAO ĐỘ LUÔN = 0 (G5);
  * Lệch tốc độ = lệch trong BASE_DELTA hoặc theo độ dài câu, kẹp trong [-0.06, +0.02] (G4);
  * Lời đọc riêng = CÂU GỐC EN + đúng một thẻ <#0.35#> sau dấu ':' đứng trước câu trích (G1/G6);
  * _pause_after = khớp với bản VN theo mạch hồi và kết thúc lượt thoại (G2).
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
import make_acting_tap09 as VN  # noqa: E402

SCRIPT = json.loads((W / "script_tap09_EN.json").read_text(encoding="utf-8"))
VN_ACTING = json.loads((W / "acting_tap09.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.05": "N2"}
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
        act = str(e.get("act", e["id"].split(".")[0]))
        emo0, pitch0 = VN.ACT_MOOD.get((act, role), ("neutral", 0))
        base_dsp = VN.BASE_DELTA.get(role, 0.0)

        for k, s in enumerate(e["sentences"], 1):
            sid = s["id"]
            text = strip_quotes(s["text"])
            words = len(text.split())

            emo = emo0
            dsp = base_dsp + (-0.02 if words <= SHORT_W else -0.01 if words <= MID1_W
                              else 0.0 if words <= MID2_W else 0.01)
            if text.rstrip().endswith("?"):
                emo = "surprised"

            pitch = 0
            if emo not in SAFE_EMO:
                emo = "neutral"
            dsp = max(DSP_MIN, min(DSP_MAX, round(dsp, 2)))
            alt = soften_en(s["text"])
            acting[sid] = [emo, dsp, pitch, alt if alt != text else None]

    pause_after = {}
    vn_pa = VN_ACTING.get("_pause_after", {})
    for k, v in vn_pa.items():
        if k in acting:
            pause_after[k] = v

    for e in SCRIPT:
        if e["kind"] == "LOI":
            last_sid = e["sentences"][-1]["id"]
            vn_el = [sid for sid in vn_pa if sid.startswith(e["id"] + "#")]
            if vn_el:
                max_vn_sid = max(vn_el, key=lambda x: int(x.split("#")[1]))
                if last_sid not in pause_after and max_vn_sid in vn_pa:
                    pause_after[last_sid] = vn_pa[max_vn_sid]

    out = {
        "_doc": ("Diễn xuất từng câu cho TTS bản EN Tập 09. id: [cảm xúc, lệch tốc độ so với "
                 "tốc độ gốc của vai, cao độ (luôn 0), lời đọc riêng hoặc null]. Lời đọc riêng "
                 "dựng lại từ câu gốc EN, chỉ thêm một thẻ <#0.35#> sau dấu ':' đứng trước câu "
                 "trích. Mọi câu còn lại dùng quy tắc ngắt nghỉ tự động của tts_sentences.py. "
                 "Chữ trên màn hình và phụ đề không đổi."),
        "_pause_after": pause_after,
    }
    out.update(acting)

    out_p = W / "acting_tap09_EN.json"
    out_p.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Wrote {len(acting)} items to {out_p}")

if __name__ == "__main__":
    main()
