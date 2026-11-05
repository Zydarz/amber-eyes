#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tập 04 — dựng STEM TẠM cho 3 ngôn ngữ (chưa có audio master mới).

VÌ SAO CẦN: badge vai trên ảnh tĩnh vẽ sóng âm RMS theo vai. Không có
`.work/stems_t04*/` thì badge hiện ĐƯỜNG THẲNG (mất 26 thanh sóng). Master mp3
của Tập 04 đã bị xoá trong đợt dọn đĩa, và kịch bản v4 đã viết lại nên audio cũ
không còn khớp ⇒ không thể dựng stem thật.

CÁCH LÀM: dựng envelope "giọng nói" TỪ CHÍNH KỊCH BẢN MỚI — mỗi câu một chuỗi
xung theo số âm tiết (ước lượng từ chữ), đặt đúng vị trí câu trong timeline tạm.
Khi thu lại audio thật: xoá `.work/stems_t04*/` rồi chạy lại `_build_stems_*.py`
(tạo từ master) trước khi dựng lại ảnh.

Dùng:  py -3 .work/_build_stems_t04_tmp.py
"""
import hashlib
import json
import re
import sys
import wave
from pathlib import Path

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
SR = 16000
FPS = 30
ROLES = ("H", "D", "C", "N1", "N2")

CFG = [("vi", "timeline_s_t04.json", "stems_t04"),
       ("en", "timeline_s_EN_t04.json", "stems_EN_t04"),
       ("ja", "timeline_s_JA_t04.json", "stems_JA_t04")]


def syllables(text, lang):
    if lang == "ja":
        # kana + kanji: 1 âm tiết ≈ 1 kana; đếm kana (không kể kanji)
        kana = re.findall(r"[ぁ-ゖー]", text)
        return max(1, len(kana))
    words = re.findall(r"[^\W\d_]+", text, flags=re.UNICODE)
    n = 0
    for w in words:
        # số nguyên âm tiết (tiếng Việt) hoặc số âm tiết tiếng Anh xấp xỉ
        n += max(1, len(re.findall(r"[aeiouyàáâãèéêìíòóôõùúýỳỵăâđêôơư]+", w.lower())))
    return max(1, n)


def env_for_sentence(text, lang, dur):
    """Envelope 0..1 cho 1 câu, dạng xung âm tiết."""
    nsyl = syllables(text, lang)
    t = np.arange(int(dur * SR)) / SR
    if len(t) == 0:
        return t
    env = np.zeros(len(t), dtype=np.float64)
    # chia đều thời gian cho các âm tiết
    slot = dur / nsyl
    h = hashlib.md5(text.encode("utf-8")).digest()
    for i in range(nsyl):
        a = int(i * slot * SR)
        b = min(len(t), int((i + 1) * slot * SR))
        if b <= a:
            continue
        # xung raised-cosine + biên độ ngẫu nhiên có seed
        dur_syl = (b - a) / SR
        amp = 0.45 + 0.55 * (h[i % len(h)] / 255.0)
        # hình bao hình toàn cục: nhỏ ở đầu, lớn giữa, nhỏ cuối
        arc = 0.75 + 0.25 * np.sin(np.pi * (i + 0.5) / max(1, nsyl))
        seg = np.hanning(max(2, b - a))
        env[a:b] = np.maximum(env[a:b], amp * arc * seg[:b - a])
    return env


for lang, tl_name, out_name in CFG:
    tl = json.loads((W / tl_name).read_text(encoding="utf-8"))
    total = float(tl["total"])
    N = int((total + 1.0) * SR)
    stems = {r: np.zeros(N, dtype=np.float64) for r in ROLES}
    n_ok = 0
    for it in tl["items"]:
        r = it.get("role")
        if r not in stems:
            continue
        a = int(round(it["start"] * SR))
        b = int(round(it["end"] * SR))
        if b <= a or a >= N:
            continue
        b = min(b, N)
        env = env_for_sentence(it["text"], lang, (b - a) / SR)
        seg = np.zeros(b - a, dtype=np.float64)
        m = min(len(env), b - a)
        seg[:m] = env[:m]
        if m == 0:
            continue
        # đặt đè (câu có thể chồng nhau ở ranh giới)
        stems[r][a:b] = np.maximum(stems[r][a:b], seg)
        n_ok += 1
    out = W / out_name
    out.mkdir(parents=True, exist_ok=True)
    for r, s in stems.items():
        peak = float(np.abs(s).max())
        if peak > 0:
            s = s / peak * 0.9
        pcm = (np.clip(s, -1, 1) * 32767).astype(np.int16)
        with wave.open(str(out / f"{r}.wav"), "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SR)
            wf.writeframes(pcm.tobytes())
    print(f"[{lang}] {out_name}: {n_ok}/{len(tl['items'])} câu có envelope · "
          f"{N/SR:.1f} s · vai {sorted(stems)}")
print("xong")
