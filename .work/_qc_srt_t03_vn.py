#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap03 VN — cổng phụ đề: mỗi cue phải là câu gốc (không đổi chữ), và mốc cue
phải nằm trong khoảng đọc của câu đó trong timeline."""
import json
import re
import sys
import unicodedata
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
TL = json.loads((WORK / "timeline_s_t03.json").read_text(encoding="utf-8"))
SRT = ROOT / "02_SAN_XUAT/Tap03/xuat_ban/Tap03.srt"

blocks = [b for b in SRT.read_text(encoding="utf-8").strip().split("\n\n") if b.strip()]


def ts(s):
    h, m, sec, ms = re.match(r"(\d\d):(\d\d):(\d\d),(\d\d\d)", s).groups()
    return int(h) * 3600 + int(m) * 60 + int(sec) + int(ms) / 1000


def norm(t):
    t = unicodedata.normalize("NFC", t or "").lower()
    t = t.replace("“", '"').replace("”", '"').replace("’", "'")
    t = re.sub(r"[^\w\s]", " ", t)
    return " ".join(t.split())


cues = []
for b in blocks:
    lines = b.splitlines()
    a, e = lines[1].split(" --> ")
    body = lines[2:]
    txt = " ".join(body)
    cues.append((ts(a), ts(e), txt, body))

items = TL["items"]
print(f"cue: {len(cues)} · câu: {len(items)}")

# 1) cue phải truy về được câu gốc
bad, untraced = [], []
for i, (a, e, txt, body) in enumerate(cues, 1):
    raw = txt.strip()
    raw = re.sub(r"^\[[^\]]+\]\s*", "", raw)        # bỏ nhãn vai TRƯỚC khi chuẩn hoá
    n = norm(raw)
    hit = any(n and n in norm(it["text"]) for it in items)
    if not hit:
        untraced.append((i, a, txt[:60]))
print(f"[S1] cue truy được về câu gốc: {len(cues)-len(untraced)}/{len(cues)}")
for u in untraced[:8]:
    print(f"     ✗ cue {u[0]} @ {u[1]:.2f}s :: {u[2]!r}")

# 2) cue phải nằm trong khoảng đọc của câu (bỏ sai số cộng dồn)
off = []
for i, (a, e, txt, body) in enumerate(cues, 1):
    cand = [it for it in items if it["start"] - 0.6 <= a <= it["end"] + 0.6]
    if not cand:
        off.append((i, a, "không có câu nào đang đọc"))
print(f"[S2] cue có câu đang đọc: {len(cues)-len(off)}/{len(cues)}")
for o in off[:8]:
    print(f"     ✗ cue {o[0]} @ {o[1]:.2f}s :: {o[2]}")

# 3) cue không chồng lấn / không lùi
bad2 = []
for i in range(1, len(cues)):
    if cues[i][0] < cues[i - 1][0] - 0.001:
        bad2.append((i + 1, "lùi"))
    if cues[i][0] < cues[i - 1][1] - 0.001:
        bad2.append((i + 1, f"chồng {cues[i-1][1]-cues[i][0]:.3f}s"))
print(f"[S3] cue không lùi/không chồng: {'ĐẠT' if not bad2 else f'{len(bad2)} lỗi {bad2[:6]}'}")

# 4) độ dài dòng (theo từng DÒNG thật của cue)
long_lines = [(i, l) for i, (a, e, t, body) in enumerate(cues, 1)
              for l in body if len(l) > 42]
nlines = [(i, len(body)) for i, (a, e, t, body) in enumerate(cues, 1) if len(body) > 2]
print(f"[S4] dòng phụ đề > 42 ký tự: {len(long_lines)}")
for x in long_lines[:5]:
    print(f"     cue {x[0]}: {x[1][:60]!r}")
print(f"[S4] cue > 2 dòng: {len(nlines)} {nlines[:5]}")

print("=" * 70)
ok = not untraced and not off and not bad2
print("KẾT LUẬN:", "ĐẠT" if ok else "CÓ LỖI")
sys.exit(0 if ok else 1)
