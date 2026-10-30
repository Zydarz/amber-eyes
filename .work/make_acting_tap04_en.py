#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh file diễn xuất TTS cho bản tiếng Anh Tập 04 -> .work/acting_tap04_EN.json.

Nguyên tắc (giữ đúng tiền lệ bản VN trong make_acting_tap04.py & make_acting_tap03_en.py):
  * cảm xúc lấy từ KEY / ACT_MOOD, chỉ giữ bộ an toàn 4 cảm xúc đã thử: neutral, sad, fearful, surprised;
  * CAO ĐỘ LUÔN = 0 (bộ an toàn đã duyệt cho Tập 02/03/04);
  * lệch tốc độ = lệch trong KEY (hoặc theo độ dài từ tiếng Anh),
    kẹp trong [-0,06 · +0,02] — tránh dồn > 40% vào một bậc;
  * lời đọc riêng = CÂU GỐC EN + đúng một thẻ <#0.35#> sau dấu ':' đứng trước
    câu trích (không đổi một chữ nào của kịch bản);
  * _pause_after = y hệt bản VN (cùng mốc khoảng lặng giữa câu).

Tự kiểm (exit != 0 nếu lỗi):
  1. đủ 161 câu EN trong kịch bản;
  2. lời đọc riêng: bỏ thẻ <#..#> + bỏ dấu nháy => đúng bằng câu EN gốc;
  3. không còn dấu nháy sót trong lời đọc riêng;
  4. cảm xúc trong bộ an toàn, cao độ = 0, lệch tốc độ trong [-0,06 · +0,02];
  5. không bậc tốc độ nào chiếm > 40% số câu.

python .work/make_acting_tap04_en.py
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"

sys.path.insert(0, str(W))
import make_acting_tap04 as VN  # noqa: E402  (KEY / ACT_MOOD / BASE_DELTA)

SCRIPT = json.loads((W / "script_tap04_EN.json").read_text(encoding="utf-8"))
VN_ACTING = json.loads((W / "acting_tap04.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.07": "N1", "4.06": "N2"}
SAFE_EMO = {"neutral", "sad", "fearful", "surprised"}

# Ngưỡng độ dài câu theo tiếng Anh (tiếng Anh dài hơn tiếng Việt ~1,4 lần số từ).
SHORT_W, MID1_W, MID2_W = 10, 16, 22
DSP_MIN, DSP_MAX = -0.06, 0.02


def strip_quotes(t):
    return t.replace("“", "").replace("”", "").replace('"', "").replace("‘", "").replace("’", "")


def soften_en(raw):
    """Đúng quy tắc của bản VN: lời đọc riêng dựng lại từ CÂU GỐC, chỉ thêm
    đúng một thẻ <#0.35#> sau dấu ':' đứng trước câu trích."""
    q = raw.find("“")
    if q > 0:
        k = raw.rfind(":", 0, q)
        if k >= 0:
            raw = raw[:k + 1] + " <#0.35#>" + raw[k + 1:]
    return strip_quotes(raw)


def main():
    acting, pause_after = {}, {}
    for e in SCRIPT:
        if e["kind"] != "LOI":
            continue
        role = N_ELEMENT.get(e["id"], e["role"])
        act = e["id"].split(".")[0]
        emo0, pitch0 = VN.ACT_MOOD.get((act, role), ("neutral", 0))
        for k, s in enumerate(e["sentences"], 1):
            sid = s["id"]
            text = strip_quotes(s["text"])
            words = len(text.split())
            if sid in VN.KEY:
                emo, dsp, pitch, alt, after = VN.KEY[sid]
            else:
                emo, pitch = emo0, pitch0
                dsp = (-0.05 if words <= SHORT_W else -0.02 if words <= MID1_W
                       else 0.0 if words <= MID2_W else 0.02)
                if text.rstrip().endswith("?"):
                    emo = "surprised"
            pitch = 0
            if emo not in SAFE_EMO:
                emo = "neutral"
            dsp = max(DSP_MIN, min(DSP_MAX, round(dsp, 2)))
            alt = soften_en(s["text"])
            acting[sid] = [emo, dsp, pitch, alt if alt != text else None]

    # khoảng lặng giữa câu: y hệt bản VN (đã duyệt trong acting_tap04.json)
    pause_after = {k: v for k, v in VN_ACTING.get("_pause_after", {}).items()}

    out = {"_doc": ("Diễn xuất từng câu cho TTS bản EN Tập 04. id: [cảm xúc, lệch tốc độ so với "
                    "tốc độ gốc của vai, cao độ (luôn 0), lời đọc riêng hoặc null]. Lời đọc riêng "
                    "dựng lại từ câu gốc EN, chỉ thêm một thẻ <#0.35#> sau dấu ':' đứng trước câu "
                    "trích. Mọi câu còn lại dùng quy tắc ngắt nghỉ tự động của tts_sentences.py. "
                    "Chữ trên màn hình và phụ đề không đổi. — xem make_acting_tap04_en.py"),
           "_pause_after": pause_after, **acting}
    (W / "acting_tap04_EN.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    # ------------------------------------------------------------------ tự kiểm
    errors = []
    # 1. đủ câu
    all_sids = [s["id"] for e in SCRIPT if e["kind"] == "LOI" for s in e["sentences"]]
    if len(all_sids) != 161 or len(acting) != 161:
        errors.append(f"Số câu kịch bản ({len(all_sids)}) hoặc acting ({len(acting)}) != 161")

    # 2. lời đọc riêng
    sents_map = {s["id"]: s["text"] for e in SCRIPT if e["kind"] == "LOI" for s in e["sentences"]}
    for sid, entry in acting.items():
        alt = entry[3]
        if alt is not None:
            clean_alt = re.sub(r"<#[\d.]+#>", "", alt).strip()
            clean_orig = strip_quotes(sents_map[sid]).strip()
            # bỏ khoảng trắng thừa
            clean_alt = re.sub(r"\s+", " ", clean_alt)
            clean_orig = re.sub(r"\s+", " ", clean_orig)
            if clean_alt != clean_orig:
                errors.append(f"[{sid}] Lời đọc riêng đổi chữ: '{clean_alt}' != '{clean_orig}'")
            if any(c in alt for c in "“”\""):
                errors.append(f"[{sid}] Lời đọc riêng còn dấu nháy: {alt}")

    # 3. phân phối cảm xúc, tốc độ
    emos = Counter(v[0] for v in acting.values())
    speeds = Counter(v[1] for v in acting.values())
    pitches = Counter(v[2] for v in acting.values())

    if any(p != 0 for p in pitches):
        errors.append(f"Cao độ khác 0: {pitches}")
    if any(emo not in SAFE_EMO for emo in emos):
        errors.append(f"Cảm xúc ngoài bộ an toàn: {emos}")

    top_speed_count = speeds.most_common(1)[0][1]
    if top_speed_count / len(acting) > 0.40:
        errors.append(f"Bậc tốc độ dồn quá 40%: {speeds.most_common(2)} / {len(acting)}")

    print(f"acting_tap04_EN.json: {len(acting)} câu | pause_after: {len(pause_after)} mốc")
    print(f"  Cảm xúc: {dict(emos)}")
    print(f"  Tốc độ: {dict(speeds)}")
    print(f"  Cao độ: {dict(pitches)}")

    if errors:
        print("\n!! PHÁT HIỆN LỖI:")
        for err in errors:
            print("  -", err)
        sys.exit(1)
    else:
        print("  -> TỰ KIỂM 100% ĐẠT CHUẨN!")


if __name__ == "__main__":
    main()
