# -*- coding: utf-8 -*-
"""Mốc chương ước lượng cho Tập 17 KO (chưa dựng audio).

Mô hình: tỉ trọng ký tự lời thoại theo hồi (đo trên kịch bản KO) + tốc độ đọc
hiệu chuẩn từ timeline KO Tập 02 đã đo thật. Đối chiếu: tổng ước lượng này vs
tỉ lệ KO/VI đo được ở Tập 02 (1,2863).
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"


def spoken_by_act(path, act_re):
    acts, cur = {}, None
    for line in path.read_text(encoding="utf-8").splitlines():
        s = line.strip()
        m = act_re.match(s)
        if m:
            cur = int(m.group(1))
            acts.setdefault(cur, [])
            continue
        if cur is None or not s:
            continue
        if s.startswith(("#", "---", "**", "[", "*", "|")):
            continue
        acts[cur].append(s)
    return {a: len("".join(v)) for a, v in acts.items()}


def mmss(t):
    t = int(t + 0.5)
    return f"{t // 60:02d}:{t % 60:02d}"


ko = spoken_by_act(ROOT / "01_KICH_BAN" / "Tap17_KO" / "kichban_tap17_KO.md", re.compile(r"^##\s*막\s*(\d)"))
ja = spoken_by_act(ROOT / "01_KICH_BAN" / "Tap17_JA" / "kichban_tap17_JA.md", re.compile(r"^##\s*第(\d)幕"))

JA_TOTAL = 2099.88
rate = sum(ja.values()) / JA_TOTAL

INTRO = 23.0
ko_sum = sum(ko.values())
t = INTRO
print(f"KO: {ko_sum:,} ký tự | tốc độ JA hiệu chuẩn {rate:.2f} ký tự/s | intro {INTRO}s")
for a in sorted(ko):
    dur = ko[a] / rate
    print(f"  act{a}: mốc {mmss(t)}  (dài {dur:6.1f}s)")
    t += dur
print(f"  TỔNG: {t:.1f}s = {mmss(t)}")
print(f"  Đối chiếu tỉ lệ KO/VI (t02) = 1,2863 -> {mmss(2026.64 * 1.2863)}")
