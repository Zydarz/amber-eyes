#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quét RÁC do model lẫn vào tiếng Nhật.

Dạng rác điển hình:
  - từ Latin nằm GIỮA hai ký tự Nhật/Trung (VD "汚ら_bounds服", "网的 attentively築き")
  - từ Trung nằm giữa tiếng Nhật
  - ký tự lạ (control, fullwidth ASCII, ký tự thay thế)

    py -3 .work/_ja_scan_garbage.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
KB = ROOT / "01_KICH_BAN"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# từ Latin hợp lệ (giữ nguyên trong bản JA): tên riêng + thuật ngữ + từ vay
OK_LATIN = set("""
AMBER EYES FBI RCMP SWAT NCIS APA DSM ICD NYPD LAPD US UK USA Vietnam
Gaslighting Narcissistic Narcolepsy TS MTP LZ MAST CBT PTSD OCD ODD ADHD
BPD APD DLT MSW RDT CBT EMDR MBCT NLP BDSM S&M
Wikipedia Britannica Netflix Facebook YouTube Disney Pixar Google Amazon
Netflix Instagram TikTok Twitter
Hollywood Chernobyl Fukushima Titanic Titanic Hindenburg Enola Enola Gay
Kemper Manson Kemper Milgram Rosenhan Rosenhan Zimbardo Watson Watson
Dee Dee Gypsy Rose Blanchard Blanchard Kemper Edmund Clarnell Strandberg
Edmund Kemper Sara Taylor Sally Hallett Kemper Kemper
Cullen Charles McDaniel Stephen Collen Colleen Michelle Carter Jodi Arias
Yoo Young Choon Bertha X Bich Ha Pan Huei Hann Pan Jennifer Pan
Tom Kelly Bich Ha Khuê Khuê
Paul Karla Homolka Bernardo Barbie Ken
Karla Homolka Paul Bernardo
Cruz Nikolas Nikolas Dalia Dippolito Dippolito
Gaslighting Spellman Battered Betty Depressed Betty Betty Ford Betty
Yoo Samsung LS JYP YG Doosan Lotte Samsung Lotte SK Hynix Samsung
Tupper Janie Bobby
ISBN FBI FBI US US
Cognitive Behavioral Therapy
DUI DWI
Pedo Pedophile
""".split())

CJK = r"぀-ヿ㐀-䶿一-鿿"

# 1) Latin giữa ký tự CJK
rx_latin_mid = re.compile(rf"(?<=[{CJK}])[A-Za-z][A-Za-z_]{{1,}}(?=[{CJK}])")
# 2) Latin đứng riêng giữa CJK (có khoảng trắng)
rx_latin_word = re.compile(rf"(?<=[{CJK}])[A-Za-z][A-Za-z_]{{1,}}(?![A-Za-z])")
# 3) ký tự thay thế / control
rx_ctrl = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f\ufffd]")

n = 0
for i in range(1, 30):
    ep = "%02d" % i
    f = KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not f.exists():
        continue
    for ln_no, ln in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        hits = []
        for m in rx_latin_mid.finditer(ln):
            w = m.group(0)
            if w not in OK_LATIN:
                hits.append((m.start(), w, "latin-giua-CJK"))
        for m in rx_ctrl.finditer(ln):
            hits.append((m.start(), repr(m.group(0)), "ky-tu-lac"))
        if not hits:
            continue
        n += 1
        print(f"Tap{ep} d{ln_no}:")
        for pos, w, kind in hits:
            s = max(0, pos - 25)
            print(f"   [{kind}] {w}  ...{ln[s:pos+35]}...")
print(f"\nTONG {n} dong rac")
