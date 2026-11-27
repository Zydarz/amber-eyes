# -*- coding: utf-8 -*-
"""Noi khoi DESC_JA sach vao make_descriptions_t25.py + quet rac chuoi nghi trong 4 ngon ngu."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(r"D:/TEST/Gax/amber-eyes/.work")
gen = WORK / "make_descriptions_t25.py"
block = (WORK / "_t25_ja_block.txt").read_text(encoding="utf-8").strip()

txt = gen.read_text(encoding="utf-8")
start = txt.index('DESC_JA = """')
end = txt.index('"""', start + len('DESC_JA = """')) + 3
new = txt[:start] + block + txt[end:]
gen.write_text(new, encoding="utf-8", newline="")
print("Da thay khoi DESC_JA (do dai moi:", len(block), "ky tu)")

# Quet rac: ky tu lat hop ky / chuoi la tron tron 4 ngon ngu
ns = {"__name__": "not_main", "__file__": str(gen)}
exec(compile(gen.read_text(encoding="utf-8"), "gen", "exec"), ns)
descs = {"VN": ns["DESC_VI"], "EN": ns["DESC_EN"], "JA": ns["DESC_JA"], "KO": ns["DESC_KO"]}

LATIN_JUNK = ["obal", "Beneath", "suddenly", "Grupo", "standing", "gather",
              "soit", "syntax", "Writable", "corner", "metric", "ACD", "ENCINI",
              "discipline", "throw", "!", "metric", "Phpm", "wow"]
for lang, d in descs.items():
    print(f"\n--- {lang}: {len(d)} ky tu ---")
    for junk in LATIN_JUNK:
        if junk in d:
            i = d.index(junk)
            print(f"   [!] '{junk}' -> ...{d[max(0,i-60):i+60]}...")
    for m in re.finditer(r"[A-Za-z]{4,}", d):
        w = m.group(0)
        if w.upper() in {"AMBER", "EYES", "TRUE", "CRIME", "YOO", "YOUNG", "CHUL",
                         "KWON", "IL", "YONG", "SOCIOPATHIC", "RESENTMENT",
                         "NARCISSISTIC", "INJURY", "DISPLACED", "AGGRESSION",
                         "GOD", "COMPLEX", "MORAL", "NEUTRALIZATION", "VIGILANTE",
                         "DELUSION", "PROFILER", "SBS", "SEOUL", "BONGWON",
                         "NETFLIX", "DOCUMENTARY", "SERIES", "RAINCOAT", "KILLER",
                         "CHOSUN", "SCOURT", "SMPA", "IMUN", "DONG", "ABC",
                         "CHAPTER", "TIMESTAMPS", "PLEASE", "NOTE", "SOURCES",
                         "CROSS", "CHECK", "Intro", "Act", "Ep", "The"}:
            continue
        ctx = d[max(0, m.start()-45):m.end()+45].replace("\n", " ")
        print(f"   ? '{w}' :: {ctx}")
