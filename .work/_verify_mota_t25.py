# -*- coding: utf-8 -*-
"""Kiem tra file mo ta Tap25 vua sinh: do dai, moc chuong, rac token, tinh trang bang nguon."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
SAN = ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham"

EXPECT = {
    "VN": (SAN / "Tap25" / "mo_ta.txt",
           ["00:00", "00:23", "07:40", "13:22", "21:09", "28:09"]),
    "EN": (SAN / "Tap25_EN" / "description.txt",
           ["00:00", "00:25", "07:25", "13:07", "21:40", "28:49"]),
    "JA": (SAN / "Tap25_JA" / "description.txt",
           ["00:00", "00:23", "08:30", "15:10", "24:02", "32:13"]),
    "KO": (SAN / "Tap25_KO" / "description.txt",
           ["00:00", "00:23", "07:40", "13:22", "21:09", "28:09"]),
}

ALLOW_LATIN = {
    "Amber", "eyes", "AmberEyes", "TrueCrime", "Yoo", "Young", "chul", "YooYoungChul",
    "Kwon", "Il", "yong", "KwonIlYong", "Il-yong", "SBS", "SEOUL", "BONGWON",
    "NETFLIX", "RAINCOAT", "KILLER", "THE", "Korea", "Chasing", "Predator", "Those",
    "Who", "Read", "Evil", "Minds", "Special", "crime", "blind", "ASPD", "NPD", "MO",
    "SIGNATURE", "NARCISSISTIC", "INJURY", "GOD", "COMPLEX", "MORAL", "VIGILANTE",
    "DELUSION", "SOCIOPATHIC", "RESENTMENT", "PROFILER", "Introduce", "Act", "Ep",
    "Intro", "CHAPTER", "TIMESTAMPS", "PLEASE", "NOTE", "SOURCES", "CROSS", "CHECK",
    "Vigilantism", "Autopsy", "Psychological", "Displaced", "Aggression", "Survival",
    "RedFlags", "NarcissisticInjury", "DisplacedAggression", "SerialKillerProfiling",
    "SeoulMurders", "TheRaincoatKiller", "CriminalPsychology", "TamLyToiPham",
    "PhamVan", "HoiTo", "Unanswered", "Questions", "Documentary", "Series", "Special",
}

print("=" * 74)
print("1) DO DAI + MOC CHUONG")
print("=" * 74)
texts = {}
for lang, (p, times) in EXPECT.items():
    t = p.read_text(encoding="utf-8")
    texts[lang] = t
    found = re.findall(r"^(\d\d:\d\d) ", t, re.M)
    ok_len = len(t) <= 5000
    ok_chap = all(x in found for x in times)
    print(f"  {lang}: {len(t):5d} ky tu {'OK ' if ok_len else 'LO'} | "
          f"moc {found[:6]} {'OK' if ok_chap else 'LO THIEU ' + str(times)}")

print("\n" + "=" * 74)
print("2) RAC TOKEN LATIN TRONG JA/KO (bo qua URL + hashtag)")
print("=" * 74)
for lang in ("JA", "KO"):
    t = texts[lang]
    t2 = re.sub(r"https?://\S+", " ", t)
    t2 = re.sub(r"#[A-Za-z0-9]+", " ", t2)
    bad = []
    for m in re.finditer(r"[A-Za-z][A-Za-z\-']{1,}", t2):
        w = m.group(0)
        if w in ALLOW_LATIN:
            continue
        bad.append((w, t2[max(0, m.start()-40):m.end()+40].replace("\n", " ")))
    print(f"  {lang}: {len(bad)} token la")
    for w, c in bad[:12]:
        print(f"     '{w}' :: {c}")

print("\n" + "=" * 74)
print("3) BANG DOI CHIEU DA KIEM CHUNG (nguon_tham_khao*.md) — PHAI GIU NGUYEN")
print("=" * 74)
for p in [SAN / "Tap25" / "nguon_tham_khao.md", SAN / "Tap25_EN" / "nguon_tham_khao_EN.md",
          SAN / "Tap25_JA" / "nguon_tham_khao_JA.md", SAN / "Tap25_KO" / "nguon_tham_khao_KO.md"]:
    t = p.read_text(encoding="utf-8")
    print(f"  {p.parent.name}/{p.name}: {len(t)} ky tu | dong bang: {t.count('|')} | "
          f"co bang: {'|---' in t}")

print("\n" + "=" * 74)
print("4) KHOI NGUON MO TA (nguon_mo_ta*.txt) — PHAI CO LINK")
print("=" * 74)
for p in [SAN / "Tap25" / "nguon_mo_ta.txt", SAN / "Tap25_EN" / "nguon_mo_ta_EN.txt",
          SAN / "Tap25_JA" / "nguon_mo_ta_JA.txt", SAN / "Tap25_KO" / "nguon_mo_ta_KO.txt"]:
    t = p.read_text(encoding="utf-8")
    print(f"  {p.parent.name}/{p.name}: {len(t)} ky tu | link: {len(re.findall(r'https?://', t))}")

print("\n" + "=" * 74)
print("5) DOI CHIEU VOI KICH BAN: 10 CHI DAU + 4 CANH BAO DO")
print("=" * 74)
for lang in ("VN", "EN", "JA", "KO"):
    t = texts[lang]
    n_ind = len(re.findall(r"^\s*(?:\d{1,2}\.|[1-9]、|\d{1,2}막)", t, re.M))
    print(f"  {lang}: so muc danh so {n_ind} | co '10' trong tieu de: {'10' in t.splitlines()[0]}")
