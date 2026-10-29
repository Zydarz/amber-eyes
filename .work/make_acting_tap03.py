#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh .work/acting_tap03.json — diễn xuất từng câu cho bản tiếng Việt Tập 03 (vụ Edmund Kemper).

Nguyên tắc kế thừa từ Tập 01/02 (BaoCao_GiongDoc_Tap02.md):
  1. BỘ THAM SỐ AN TOÀN: chỉ dùng cảm xúc neutral · sad · fearful · surprised, cao độ LUÔN = 0.
     Bộ giọng đã thử ở Tập 02 chỉ được kiểm ở cao độ 0 — đổi cao độ hoặc dùng cảm xúc chưa
     thử làm giọng đổi "người".
  2. Tốc độ: lệch nhỏ so với giọng gốc, kẹp trong [-0,06 · +0,02]. Câu ngắn chậm hơn để "đóng đinh".
  3. Ngắt nghỉ: KHÔNG rải thẻ <#..#> trong câu (lượt 23/10 thử 23/10 thấy làm vụn ngữ điệu
     tiếng Việt) — chỉ thêm tự động sau ':' và '...'; kịch tính chuyển sang khoảng lặng GIỮA
     các câu qua _pause_after, để build_audio3 còn chỗ cho SFX.
  4. Lời đọc riêng chỉ thêm ngắt nghỉ, KHÔNG đổi chữ — phụ đề và chữ trên hình giữ nguyên kịch bản.

Định dạng giống acting_tap02.json: id -> [cảm xúc, lệch tốc độ, cao độ, lời đọc | null]
"""
import json
import re
from pathlib import Path

W = Path(r"D:\TEST\Gax\Audi\.work")
SCRIPT = json.loads((W / "script_tap03.json").read_text(encoding="utf-8"))
N_ELEMENT = {"1.09": "N1", "2.09": "N2"}

# Tốc độ gốc trong edition.CAST (bộ A): H 0.90 · D 0.95 · C 0.92 · N1 0.95 · N2 0.95
BASE_DELTA = {"H": -0.04, "D": -0.05, "C": -0.04, "N1": -0.03, "N2": -0.02}

# Mặc định theo hồi và vai: (cảm xúc, cao độ)
ACT_MOOD = {
    ("1", "H"): ("neutral", 0), ("1", "N1"): ("neutral", 0), ("1", "D"): ("neutral", -1),
    ("2", "H"): ("neutral", -1), ("2", "D"): ("neutral", -1), ("2", "N2"): ("sad", 0),
    ("3", "H"): ("sad", 0), ("3", "C"): ("neutral", 0),
    ("4", "H"): ("neutral", -1), ("4", "D"): ("neutral", 0),
    ("5", "H"): ("neutral", 0), ("5", "C"): ("neutral", 0), ("5", "D"): ("neutral", -1),
}

# Câu then chốt: [cảm xúc, lệch tốc độ (thêm vào BASE_DELTA), cao độ, lời đọc có ngắt nghỉ | None, nghỉ thêm sau câu (s)]
KEY = {
    # ── HỒI 1 — cuộc gọi 4 giờ sáng, hiện trường, bắt giữ ──────────────────────────
    "1.03#1": ["neutral", -0.01, 0, None, 0.3],
    "1.03#3": ["neutral", 0.0, 0, None, 0.2],
    "1.03#6": ["neutral", 0.02, 0, None, 0],
    "1.03#8": ["fearful", -0.02, 0, None, 0.8],
    "1.05#2": ["fearful", -0.01, 0, None, 0.3],
    "1.05#3": ["neutral", 0.0, 0, None, 0.5],
    "1.05#4": ["sad", -0.01, 0, None, 0],
    "1.05#5": ["sad", -0.01, 0, None, 0],
    "1.05#6": ["fearful", -0.02, 0, None, 0.6],
    "1.05#7": ["sad", -0.01, 0, None, 0.5],
    "1.07#1": ["neutral", 0.0, 0, None, 0],
    "1.07#2": ["neutral", 0.0, 0, None, 0.2],
    "1.07#4": ["neutral", 0.0, 0, None, 0.4],
    "1.09#1": ["neutral", 0.0, 0, None, 0],
    "1.09#4": ["neutral", 0.02, 0, None, 0.2],
    "1.09#6": ["sad", -0.01, 0, None, 0.3],
    "1.09#8": ["sad", -0.01, 0, None, 0.3],
    "1.09#9": ["sad", -0.02, 0, None, 0.6],
    "1.10#1": ["neutral", 0.0, 0, None, 0],
    "1.10#3": ["sad", -0.01, 0, None, 0.3],
    "1.10#4": ["neutral", 0.0, 0, None, 0.2],
    "1.10#7": ["neutral", 0.0, 0, None, 0.3],
    "1.10#8": ["neutral", 0.0, 0, None, 0],
    "1.10#10": ["fearful", -0.02, 0, None, 0.7],
    "1.10#11": ["fearful", -0.02, 0, None, 0.8],
    "1.10#12": ["sad", -0.01, 0, None, 0.2],
    "1.10#13": ["sad", -0.01, 0, None, 0.6],
    "1.10#14": ["neutral", 0.0, 0, None, 0],
    "1.13#1": ["neutral", 0.0, 0, None, 0.2],
    "1.13#2": ["neutral", 0.02, 0, None, 0.2],
    "1.13#3": ["surprised", 0.0, 0, None, 0.2],
    "1.13#5": ["fearful", -0.01, 0, None, 0.3],
    "1.13#6": ["neutral", 0.0, 0, None, 0.2],
    "1.13#9": ["neutral", -0.01, 0, None, 0.5],
    "1.15#1": ["neutral", 0.0, 0, None, 0],
    "1.15#2": ["neutral", 0.0, 0, None, 0.2],
    # ── HỒI 2 — thị trấn, các nạn nhân, chiếc xe, quán rượu ──────────────────────
    "2.02#1": ["neutral", 0.0, 0, None, 0],
    "2.02#2": ["neutral", 0.0, 0, None, 0.2],
    "2.02#3": ["fearful", -0.01, 0, None, 0.4],
    "2.04#1": ["sad", -0.01, 0, None, 0.3],
    "2.04#3": ["neutral", 0.02, 0, None, 0.2],
    "2.04#4": ["neutral", 0.0, 0, None, 0.2],
    "2.04#5": ["sad", -0.01, 0, None, 0.3],
    "2.04#6": ["sad", -0.01, 0, None, 0.2],
    "2.04#7": ["sad", -0.01, 0, None, 0.4],
    "2.04#8": ["sad", -0.01, 0, None, 0.2],
    "2.06#1": ["sad", -0.02, 0, None, 0.4],
    "2.06#2": ["fearful", -0.02, 0, None, 0.5],
    "2.06#3": ["neutral", 0.0, 0, None, 0.3],
    "2.06#4": ["neutral", 0.0, 0, None, 0.3],
    "2.06#5": ["neutral", 0.0, 0, None, 0],
    "2.07#1": ["neutral", -0.01, 0, None, 0],
    "2.07#2": ["neutral", 0.02, 0, None, 0.2],
    "2.07#3": ["neutral", 0.0, 0, None, 0.2],
    "2.07#5": ["neutral", -0.01, 0, None, 0.3],
    "2.07#10": ["neutral", -0.01, 0, None, 0.5],
    "2.07#11": ["fearful", -0.02, 0, None, 0.5],
    "2.07#14": ["fearful", -0.01, 0, None, 0.3],
    "2.07#15": ["surprised", 0.0, 0, None, 0.2],
    "2.08#1": ["surprised", -0.01, 0, None, 0],
    "2.08#2": ["neutral", -0.01, 0, None, 0.3],
    "2.08#3": ["neutral", 0.0, 0, None, 0],
    "2.09#2": ["neutral", 0.0, 0, None, 0],
    "2.09#5": ["sad", -0.01, 0, None, 0.3],
    "2.09#6": ["sad", -0.01, 0, None, 0.3],
    "2.09#7": ["sad", -0.01, 0, None, 0.4],
    "2.09#8": ["sad", -0.02, 0, None, 0.2],
    "2.09#9": ["sad", -0.02, 0, None, 0.8],
    # ── HỒI 3 — ba tầng bệnh lý ────────────────────────────────────────────────
    "3.02#1": ["neutral", 0.0, 0, None, 0],
    "3.02#2": ["sad", -0.02, 0, None, 0.3],
    "3.04#1": ["neutral", 0.0, 0, None, 0],
    "3.05#1": ["neutral", 0.0, 0, None, 0.2],
    "3.05#2": ["neutral", 0.0, 0, None, 0.2],
    "3.05#3": ["neutral", -0.01, 0, None, 0.4],
    "3.05#4": ["sad", 0.0, 0, None, 0.2],
    "3.05#6": ["sad", -0.02, 0, None, 0.4],
    "3.05#7": ["sad", -0.02, 0, None, 0.4],
    "3.05#8": ["sad", -0.01, 0, None, 0.2],
    "3.05#9": ["sad", -0.01, 0, None, 0.3],
    "3.05#10": ["sad", -0.02, 0, None, 0.5],
    "3.05#11": ["neutral", 0.0, 0, None, 0.2],
    "3.05#12": ["sad", -0.02, 0, None, 0.6],
    "3.07#1": ["surprised", 0.0, 0, None, 0],
    "3.08#1": ["neutral", -0.01, 0, None, 0.4],
    "3.08#2": ["fearful", -0.01, 0, None, 0.3],
    "3.08#3": ["neutral", 0.0, 0, None, 0.2],
    "3.08#5": ["sad", -0.01, 0, None, 0.3],
    "3.08#6": ["sad", -0.01, 0, None, 0.2],
    "3.08#7": ["fearful", -0.02, 0, None, 0.4],
    "3.08#8": ["fearful", -0.02, 0, None, 0.4],
    "3.08#10": ["fearful", -0.02, 0, None, 0.4],
    "3.08#11": ["sad", -0.02, 0, None, 0.6],
    "3.10#1": ["surprised", 0.0, 0, None, 0],
    "3.11#1": ["neutral", -0.01, 0, None, 0.4],
    "3.11#2": ["neutral", 0.0, 0, None, 0.2],
    "3.11#3": ["neutral", 0.0, 0, None, 0.2],
    "3.11#4": ["fearful", -0.02, 0, None, 0.4],
    "3.11#5": ["fearful", -0.02, 0, None, 0.4],
    "3.11#7": ["sad", -0.01, 0, None, 0.4],
    "3.11#8": ["sad", -0.02, 0, None, 0.8],
    # ── HỒI 4 — Vacaville 1978, Đặc vụ FBI ──────────────────────────────────────
    "4.02#1": ["neutral", -0.02, 0, None, 0.5],
    "4.02#2": ["neutral", -0.01, 0, None, 0.2],
    "4.02#3": ["neutral", 0.0, 0, None, 0.2],
    "4.02#5": ["surprised", -0.01, 0, None, 0.3],
    "4.04#1": ["neutral", 0.0, 0, None, 0],
    "4.05#1": ["surprised", -0.01, 0, None, 0.4],
    "4.05#3": ["neutral", -0.01, 0, None, 0.4],
    "4.05#4": ["neutral", 0.0, 0, None, 0.2],
    "4.05#6": ["neutral", -0.01, 0, None, 0.4],
    "4.05#8": ["sad", -0.01, 0, None, 0.3],
    "4.05#10": ["neutral", -0.01, 0, None, 0.4],
    "4.05#13": ["neutral", -0.01, 0, None, 0.2],
    "4.05#15": ["sad", -0.01, 0, None, 0.2],
    "4.05#16": ["sad", -0.02, 0, None, 0.6],
    "4.05#19": ["neutral", 0.0, 0, None, 0.4],
    "4.07#1": ["neutral", -0.01, 0, None, 0.3],
    "4.07#2": ["neutral", -0.01, 0, None, 0.4],
    "4.07#4": ["fearful", -0.01, 0, None, 0.3],
    "4.07#5": ["fearful", -0.02, 0, None, 0.4],
    "4.07#6": ["neutral", -0.01, 0, None, 0.4],
    "4.07#8": ["neutral", -0.01, 0, None, 0.4],
    "4.07#9": ["neutral", 0.0, 0, None, 0.2],
    "4.07#10": ["sad", -0.02, 0, None, 0.5],
    "4.08#1": ["neutral", 0.0, 0, None, 0.2],
    "4.08#3": ["neutral", 0.0, 0, None, 0.3],
    "4.08#4": ["neutral", -0.01, 0, None, 0.4],
    "4.08#5": ["sad", -0.01, 0, None, 0.3],
    "4.08#7": ["neutral", 0.0, 0, None, 0.2],
    # ── HỒI 5 — phiên tòa, 4 dấu hiệu đỏ, lời kết ───────────────────────────────
    "5.02#1": ["neutral", 0.0, 0, None, 0],
    "5.02#4": ["neutral", 0.0, 0, None, 0.2],
    "5.02#5": ["neutral", 0.0, 0, None, 0.3],
    "5.02#6": ["neutral", -0.01, 0, None, 0.4],
    "5.02#7": ["fearful", -0.02, 0, None, 0.8],
    "5.02#8": ["neutral", 0.0, 0, None, 0.2],
    "5.02#10": ["neutral", 0.0, 0, None, 0.2],
    "5.02#11": ["sad", -0.01, 0, None, 0.4],
    "5.02#12": ["sad", -0.01, 0, None, 0.2],
    "5.02#13": ["sad", -0.02, 0, None, 0.7],
    "5.04#1": ["neutral", 0.0, 0, None, 0],
    "5.05#1": ["neutral", -0.01, 0, None, 0.4],
    "5.05#2": ["neutral", 0.0, 0, None, 0.2],
    "5.05#3": ["neutral", 0.0, 0, None, 0.2],
    "5.05#4": ["sad", -0.02, 0, None, 0.4],
    "5.05#5": ["sad", -0.02, 0, None, 0.3],
    "5.05#6": ["sad", -0.02, 0, None, 0.5],
    "5.05#7": ["neutral", -0.01, 0, None, 0.4],
    "5.05#8": ["neutral", 0.0, 0, None, 0.2],
    "5.06#1": ["neutral", -0.01, 0, None, 0.4],
    "5.06#2": ["neutral", 0.0, 0, None, 0.2],
    "5.06#3": ["neutral", -0.01, 0, None, 0.4],
    "5.06#4": ["neutral", 0.0, 0, None, 0.2],
    "5.08#1": ["neutral", -0.01, 0, None, 0.4],
    "5.08#3": ["sad", -0.02, 0, None, 0.6],
    "5.08#4": ["neutral", -0.01, 0, None, 0.3],
    "5.08#5": ["surprised", -0.02, 0, None, 0.6],
    "5.08#6": ["neutral", 0.0, 0, None, 0.2],
    "5.08#7": ["sad", -0.01, 0, None, 0.3],
    "5.08#8": ["neutral", -0.01, 0, None, 0.3],
    "5.08#9": ["neutral", -0.01, 0, None, 0.5],
    "5.10#1": ["neutral", 0.0, 0, None, 0],
    "5.10#2": ["neutral", 0.0, 0, None, 0.2],
    "5.10#3": ["neutral", 0.0, 0, None, 0],
}


def auto_pauses(t):
    """Ngắt nghỉ tự động cho câu không có lời đọc riêng (giống quy tắc bản EN, chữ hoa tiếng Việt)."""
    t = re.sub(r"\.\.\.\s+(?!<#)", "... <#0.45#> ", t)
    t = re.sub(r"\s[–—]\s(?!<#)", ", <#0.2#> ", t)
    t = re.sub(r":\s+(?=[^\W\d_])(?!<#)", lambda m: ": <#0.3#> ", t)
    return t


def soften(raw, alt):
    """Thẻ ngắt giữa câu làm vụn ngữ điệu tiếng Việt ⇒ chỉ thêm MỘT thẻ ngay sau dấu ':'
    đứng trước câu trích. Kịch tính chuyển sang khoảng lặng GIỮA các câu (_pause_after)."""
    q = raw.find("“")
    if q > 0:
        k = raw.rfind(":", 0, q)
        if k >= 0:
            raw = raw[:k + 1] + " <#0.35#>" + raw[k + 1:]
    s = raw.replace("“", "").replace("”", "").replace('"', "")
    if alt and "(Signature)" not in alt and "(Signature)" in s:
        s = s.replace(" (Signature)", "")
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
                alt = alt if alt else (auto_pauses(text) if auto_pauses(text) != text else None)
            else:
                emo, pitch = emo0, pitch0
                dsp = BASE_DELTA[role] + (-0.05 if words <= 8 else 0.02 if words >= 30 else 0.0)
                if words <= 8:
                    pitch -= 1
                if text.rstrip().endswith("?"):
                    emo, pitch = "surprised", pitch + 1
                if k == n and n > 1:
                    pitch -= 1
                dsp = round(dsp, 2)
                alt = auto_pauses(text)
                alt = alt if alt != text else None
                after = 0.0
            pitch = max(-4, min(3, pitch))
            pitch = 0                      # bộ an toàn: cao độ ≠ 0 chưa được thử
            if emo not in SAFE_EMO:
                emo = "neutral"
            dsp = max(-0.06, min(0.02, dsp))
            alt = soften(s["text"], alt)
            if alt == text:
                alt = None
            acting[sid] = [emo, dsp, pitch, alt]
            # Chỉ giữ nghỉ thêm từ 0,4 s trở lên: Tập 02 dùng 27,2 s trên 215 câu là mốc đã duyệt;
            # giữ cả 0,2/0,3 s sẽ lên ~48 s và làm nhịp tập chậm hẳn. Khoảng lặng nhỏ đã được
            # auto_pauses() xử lý bằng thẻ <#..#> trong câu.
            if after >= 0.4:
                pause_after[sid] = after

    # KEY phải khớp câu có thật
    real = set(acting)
    for sid in KEY:
        if sid not in real:
            unknown.append(sid)
    if unknown:
        raise SystemExit(f"KEY troi ma cau khong ton tai: {unknown}")

    out = {"_doc": __doc__.strip().splitlines()[0] + " — xem make_acting_tap03.py",
           "_pause_after": pause_after, **acting}
    (W / "acting_tap03.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

    from collections import Counter
    emos = Counter(v[0] for v in acting.values())
    dsps = Counter(v[1] for v in acting.values())
    print(f"{len(acting)} cau · {len(KEY)} moc then chot ({len(KEY)/len(acting)*100:.0f}%)")
    print(f"  cam xuc: {dict(emos)}")
    print(f"  lech toc do: {dict(sorted(dsps.items()))}")
    print(f"  loi doc rieng: {sum(1 for v in acting.values() if v[3])} · nghi them: "
          f"{len(pause_after)} ({sum(pause_after.values()):.1f} s)")
    print(f"  ghi: {W / 'acting_tap03.json'}")


if __name__ == "__main__":
    main()
