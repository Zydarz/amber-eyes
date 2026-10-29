#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh file diễn xuất TTS cho bản tiếng Anh Tập 02 -> .work/acting_tap02_EN.json.

Nguyên tắc (giữ đúng tiền lệ bản VN trong make_acting_tap02.py):
  * cảm xúc lấy từ KEY / ACT_MOOD, chỉ giữ bộ an toàn 4 cảm xúc đã thử;
  * CAO ĐỘ LUÔN = 0 (bộ an toàn đã duyệt cho Tập 02/Tập 03);
  * lệch tốc độ = lệch trong KEY (KHÔNG cộng BASE_DELTA âm của bản VN),
    kẹp trong [-0,06 · +0,02] — giữ được tương phản 4-5 bậc thay vì dồn 51%
    vào một bậc như bản VN;
  * lời đọc riêng = CÂU GỐC EN + đúng một thẻ <#0.35#> sau dấu ':' đứng trước
    câu trích (không đổi một chữ nào của kịch bản);
  * _pause_after = y hệt bản VN (cùng 70 khoảng lặng, 27,2 s).

Tự kiểm (exit != 0 nếu lỗi):
  1. đủ 215 câu EN trong kịch bản;
  2. lời đọc riêng: bỏ thẻ <#..#> + bỏ dấu nháy => đúng bằng câu EN gốc;
  3. không còn dấu nháy sót trong lời đọc riêng;
  4. cảm xúc trong bộ an toàn, cao độ = 0, lệch tốc độ trong [-0,06 · +0,02];
  5. không bậc tốc độ nào chiếm > 40% số câu.

python .work/make_acting_tap02_en.py
"""
import json
import re
import sys
from collections import Counter
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
W = ROOT / ".work"

sys.path.insert(0, str(W))
import make_acting_tap02 as VN  # noqa: E402  (KEY / ACT_MOOD / SAFE_EMO / auto_pauses)

SCRIPT = json.loads((W / "script_tap02_EN.json").read_text(encoding="utf-8"))
VN_ACTING = json.loads((W / "acting_tap02.json").read_text(encoding="utf-8"))
N_ELEMENT = VN.N_ELEMENT
SAFE_EMO = VN.SAFE_EMO

# Ngưỡng độ dài câu theo tiếng Anh (tiếng Anh dài hơn tiếng Việt ~1,4 lần số từ).
# 4 bậc tốc độ, mỗi bậc ~25% số câu — tránh dồn vào một bậc như bản VN (51%).
SHORT_W, MID1_W, MID2_W = 10, 15, 20
DSP_MIN, DSP_MAX = -0.06, 0.02


def strip_quotes(t):
    return t.replace("“", "").replace("”", "").replace('"', "")


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
        n = len(e["sentences"])
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

    # khoảng lặng giữa câu: y hệt bản VN (đã duyệt, 70 chỗ / 27,2 s)
    pause_after = {k: v for k, v in VN_ACTING.get("_pause_after", {}).items()}

    out = {"_doc": ("Diễn xuất từng câu cho TTS bản EN Tập 02. id: [cảm xúc, lệch tốc độ so với "
                    "tốc độ gốc của vai, cao độ (luôn 0), lời đọc riêng hoặc null]. Lời đọc riêng "
                    "dựng lại từ câu gốc EN, chỉ thêm một thẻ <#0.35#> sau dấu ':' đứng trước câu "
                    "trích. Mọi câu còn lại dùng quy tắc ngắt nghỉ tự động của tts_sentences.py. "
                    "Chữ trên màn hình và phụ đề không đổi. — xem make_acting_tap02_en.py"),
           "_pause_after": pause_after, **acting}
    (W / "acting_tap02_EN.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    # ------------------------------------------------------------------ tự kiểm
    errors = []
    sids = [s["id"] for e in SCRIPT if e["kind"] == "LOI" for s in e["sentences"]]
    RAW = {s["id"]: s["text"] for e in SCRIPT if e["kind"] == "LOI" for s in e["sentences"]}
    for sid in sids:
        if sid not in acting:
            errors.append(f"{sid}: thiếu trong file diễn xuất")
    for sid in acting:
        if sid not in sids:
            errors.append(f"{sid}: có trong file diễn xuất nhưng không có trong kịch bản")
    for sid, v in acting.items():
        emo, dsp, pitch, alt = v
        if emo not in SAFE_EMO:
            errors.append(f"{sid}: cảm xúc '{emo}' ngoài bộ an toàn")
        if pitch != 0:
            errors.append(f"{sid}: cao độ {pitch} ≠ 0")
        if not (DSP_MIN <= dsp <= DSP_MAX):
            errors.append(f"{sid}: lệch tốc độ {dsp} ngoài [{DSP_MIN} · {DSP_MAX}]")
        if alt:
            if any(ch in alt for ch in "“”\""):
                errors.append(f"{sid}: lời đọc riêng còn dấu nháy")
            plain = re.sub(r"<#[\d.]+#>", "", alt)
            if " ".join(plain.split()) != " ".join(strip_quotes(RAW[sid]).split()):
                errors.append(f"{sid}: lời đọc riêng khác câu gốc EN")
    spd = Counter(v[1] for v in acting.values())
    worst, worst_n = max(spd.items(), key=lambda kv: kv[1])
    if worst_n > 0.40 * len(acting):
        errors.append(f"bậc tốc độ {worst} chiếm {worst_n}/{len(acting)} câu (>40%)")

    emos = Counter(v[0] for v in acting.values())
    print(f"{len(acting)} câu · {dict(emos)} · lời đọc riêng: {sum(1 for v in acting.values() if v[3])}"
          f" · nghỉ thêm: {len(pause_after)} ({sum(pause_after.values()):.1f} s)")
    print("tốc độ:", sorted(spd.items()), "· bậc nhiều nhất:", worst, worst_n)
    if errors:
        print("\n".join(errors))
        sys.exit(1)
    print("OK")


if __name__ == "__main__":
    main()
