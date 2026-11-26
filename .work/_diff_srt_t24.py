#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""So SRT mới (sau khi chạy subtitles.py) với bản gốc đã xuất bản.

  py -3 .work/_diff_srt_t24.py vi en ja

Báo cáo: số cue, nội dung có giống 100 % không, sai lệch thời gian lớn nhất.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROD = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham"
BAK = ROOT / ".work" / "_cu" / "srt_t24_20261125"
FILES = {
    "vi": ("Tap24/xuat_ban/Tap24.srt", "Tap24.srt"),
    "en": ("Tap24_EN/xuat_ban/Tap24_EN.srt", "Tap24_EN.srt"),
    "ja": ("Tap24_JA/xuat_ban/Tap24_JA.srt", "Tap24_JA.srt"),
}


def parse(p):
    txt = Path(p).read_text(encoding="utf-8-sig")
    cues = []
    for block in re.split(r"\r?\n\r?\n", txt.strip()):
        lines = [l for l in block.split("\n") if l.strip()]
        if len(lines) < 2 or "-->" not in lines[1]:
            continue
        a, b = lines[1].split("-->")
        cues.append((ts(a.strip()), ts(b.strip()), "\n".join(lines[2:])))
    return cues


def ts(s):
    s = s.replace(",", ".")
    h, m, sec = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(sec)


def main():
    langs = sys.argv[1:] or ["vi", "en", "ja"]
    for lang in langs:
        rel, name = FILES[lang]
        new = parse(PROD / rel)
        old = parse(BAK / name)
        if len(new) != len(old):
            print(f"{lang}: SỐ CUE LỆCH — mới {len(new)} · gốc {len(old)}")
            continue
        txt_diff = sum(1 for a, b in zip(new, old) if a[2] != b[2])
        dmax = max(max(abs(a[0] - b[0]), abs(a[1] - b[1])) for a, b in zip(new, old))
        dstart = max(abs(a[0] - b[0]) for a, b in zip(new, old))
        dend = max(abs(a[1] - b[1]) for a, b in zip(new, old))
        print(f"{lang}: {len(new)} cue · nội dung khác {txt_diff} · "
              f"lệch max {dmax*1000:.0f} ms (đầu {dstart*1000:.0f} / cuối {dend*1000:.0f})")


if __name__ == "__main__":
    main()
