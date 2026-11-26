#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""KIỂM CHỨNG timeline dựng lại: chạy subtitles.py và so SRT mới với SRT gốc."""
import os, re, shutil, subprocess, sys, difflib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BAK = WORK / "_cu" / "srt_t24_20261125"
BAK.mkdir(parents=True, exist_ok=True)

LANGS = [("vi", "Tap24", "Tap24.srt"), ("en", "Tap24_EN", "Tap24_EN.srt"),
         ("ja", "Tap24_JA", "Tap24_JA.srt")]

def ts2s(s):
    h, m, rest = s.split(":")
    return int(h) * 3600 + int(m) * 60 + float(rest.replace(",", "."))


fail = 0
for lang, epdir, srt in LANGS:
    src = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / epdir / "xuat_ban" / srt
    bak = BAK / f"{epdir}_{srt}"
    if not bak.exists():
        shutil.copy2(src, bak)
    env = os.environ.copy()
    env["AE_EP"] = "24"
    env["AE_LANG"] = lang
    r = subprocess.run([sys.executable, str(WORK / "subtitles.py")], env=env,
                       capture_output=True, text=True, encoding="utf-8", errors="replace", cwd=str(WORK))
    print(f"=== {lang.upper()} · subtitles.py: {(r.stdout or '').strip() or (r.stderr or '')[:200]}")
    a = bak.read_text(encoding="utf-8").replace("\r\n", "\n").strip().splitlines()
    b = src.read_text(encoding="utf-8").replace("\r\n", "\n").strip().splitlines()
    if a == b:
        print(f"    SRT KHỚP 100% ({len(a)} dòng) — timeline dựng lại CHÍNH XÁC")
        continue
    # so cue: (start, end, text)
    def cues(lines):
        out, i = [], 0
        while i < len(lines):
            if "-->" in lines[i] and i + 2 < len(lines):
                m = re.match(r"(\d+:\d+:\d+,\d+)\s*-->\s*(\d+:\d+:\d+,\d+)", lines[i])
                out.append((m.group(1), m.group(2), lines[i + 1].replace("\n", " | ")))
                i += 3
            else:
                i += 1
        return out
    ca, cb = cues(a), cues(b)
    print(f"    SRT KHÁC: gốc {len(ca)} cue · mới {len(cb)} cue")
    if len(ca) != len(cb):
        print("    → SỐ CUE KHÁC NHAU")
        fail += 1
        shutil.copy2(bak, src)
        continue
    diff_txt = 0
    max_dt = 0.0
    worst = []
    for x, y in zip(ca, cb):
        if x[2] != y[2]:
            diff_txt += 1
        dt = max(abs(ts2s(x[0]) - ts2s(y[0])), abs(ts2s(x[1]) - ts2s(y[1])))
        max_dt = max(max_dt, dt)
        if dt > 0.05 and len(worst) < 5:
            worst.append((x, y))
    print(f"    cue khác NỘI DUNG: {diff_txt} · sai lệch thời gian LỚN NHẤT: {max_dt*1000:.0f} ms")
    for x, y in worst:
        print(f"      gốc {x[0]}→{x[1]} | mới {y[0]}→{y[1]}")
    if diff_txt or max_dt > 0.05:
        fail += 1
        shutil.copy2(bak, src)      # giữ nguyên SRT gốc
        print(f"    → đã khôi phục SRT gốc từ {bak}")
    else:
        print(f"    → ĐẠT: nội dung 100% + thời gian lệch ≤ {max_dt*1000:.0f} ms (ngưỡng 50 ms)")
        shutil.copy2(bak, src)      # giữ nguyên SRT gốc (file đã đúng)
print("\nKẾT QUẢ:", "ĐẠT" if not fail else f"TRƯỢT {fail} ngôn ngữ")
sys.exit(1 if fail else 0)
