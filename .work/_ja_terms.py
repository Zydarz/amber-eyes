#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Rút thuật ngữ + tên riêng xuyên suốt 29 kịch bản để dựng glossary JA."""
import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi\01_KICH_BAN")
OUT = Path(__file__).parent / "_ja_terms.txt"


def canonical(tap):
    d = ROOT / tap
    c = [f for f in d.glob("kichban_*.md") if not re.search(r"(_ban_goc|_truoc_review|_EN)", f.name)]
    return max(c, key=lambda p: p.stat().st_mtime)


ACRONYM = re.compile(r"\b([A-Z]{2,6})\b")
VN_TERM = re.compile(
    r"\b((?:Hội chứng|Rối loạn|Loạn thần|Trầm cảm|Hưng phấn|Ám ảnh|Giác ngủ mơ|"
    r"Nhân cách|Hành vi|Áp lực|Tự sát|Không chấp nhận|Đau đớn|Nghiện nguy hiểm)[^,.;:!?()\"]{2,60})")
PROPER = re.compile(r"\b([A-Z][a-zA-Z'’]+(?:\s+(?:van|de|del|della|di|da|the)?\s*[A-Z][a-zA-Z'’]+){0,3})\b")
PLACE = re.compile(r"\b(?:tại|ở|thành phố|thị trấn|quận|bang|huyện)\s+([A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)?)")

SKIP = {
    "HOST", "SFX", "BGM", "FBI", "DSM", "AMP", "NOTE", "N", "D", "C", "H", "N1", "N2",
    "TTS", "AI", "CPU", "USA", "US", "DNA", "PTSD", "ADHD", "OCD", "BPD", "ASPD", "PD",
    "FDIA", "ID", "PD", "RC", "AA", "PR", "I", "II", "III", "IV", "V", "VI", "VII", "VIII",
}


def main():
    acr, term, prop, place = Counter(), Counter(), Counter(), Counter()
    for i in range(1, 30):
        f = canonical(f"Tap{i:02d}")
        txt = f.read_text(encoding="utf-8")
        for m in ACRONYM.findall(txt):
            if m not in SKIP:
                acr[m] += 1
        for m in VN_TERM.findall(txt):
            term[" ".join(m.split())] += 1
        for m in PROPER.findall(txt):
            w = m.strip()
            if len(w) > 3 and not w.startswith("The "):
                prop[w] += 1
        for m in PLACE.findall(txt):
            place[" ".join(m.split())] += 1

    def dump(title, c, n=120):
        return [f"### {title}"] + [f"{v:5d}  {k}" for k, v in c.most_common(n)] + [""]

    txt = (dump("ACRONYMS", acr, 90) + dump("VN TERMS", term, 110) +
           dump("PROPER NOUNS (multiword)", prop, 150) + dump("PLACES", place, 120))
    OUT.write_text("\n".join(txt), encoding="utf-8")
    print(f"written {OUT}")


if __name__ == "__main__":
    main()
