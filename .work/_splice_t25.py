# -*- coding: utf-8 -*-
"""Noi khoi DESC_VN / DESC_JA sach vao make_descriptions_t25.py, do do dai 4 ngon ngu,
quet rac ky tu rac (Latin lot trong JA/KO, token roi)."""
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
WORK = Path(r"D:/TEST/Gax/amber-eyes/.work")
gen = WORK / "make_descriptions_t25.py"

for var, blk_file in (("DESC_VI", "_t25_vn_block.txt"), ("DESC_EN", "_t25_en_block.txt"),
                      ("DESC_JA", "_t25_ja_block.txt")):
    block = (WORK / blk_file).read_text(encoding="utf-8").strip()
    txt = gen.read_text(encoding="utf-8")
    start = txt.index(f'{var} = """')
    end = txt.index('"""', start + len(f'{var} = """')) + 3
    gen.write_text(txt[:start] + block + txt[end:], encoding="utf-8", newline="")
    print(f"Da thay {var} ({len(block)} ky tu)")

ns = {"__name__": "not_main", "__file__": str(gen)}
exec(compile(gen.read_text(encoding="utf-8"), "gen", "exec"), ns)
D = {"VN": ns["DESC_VI"], "EN": ns["DESC_EN"], "JA": ns["DESC_JA"], "KO": ns["DESC_KO"]}

print("\n=== DO DAI (gioi han YouTube 5000) ===")
for k, v in D.items():
    print(f"  {k}: {len(v):5d}  {'PASS' if len(v) <= 5000 else 'FAIL'}  (du dia {5000 - len(v)})")

JUNK = ["obal", "Beneath", "suddenly", "Grupo", "standing", "gather", "soit",
        "syntax", "Writable", "corner", "metric", "ACD", "ENCINI", "discipline",
        "throw", "Discip", "Phpm", "집중시키는", "진행되는", "실행", "deserving",
        "Sioux", "Home", "Episode", "meant", "sentenc", "thrown", "died"]
print("\n=== QUET RAC TOKEN ===")
for k, v in D.items():
    for j in JUNK:
        if j in v:
            i = v.index(j)
            print(f"  [{k}] '{j}' :: ...{v[max(0, i-70):i+70]}...")

print("\n=== LATIN TRONG JA/KO (chi nen la thuat ngu) ===")
ALLOW = {"Amber", "eyes", "Yoo", "Young", "chul", "Kwon", "Il", "yong", "SBS",
         "SEOUL", "BONGWON", "NETFLIX", "RAINCOAT", "KILLER", "AMBER", "EYES",
         "TRUE", "CRIME", "NARCISSISTIC", "INJURY", "GOD", "COMPLEX", "MORAL",
         "VIGILANTE", "DELUSION", "SOCIOPATHIC", "RESENTMENT", "PROFILER",
         "KwonIlYong", "ASPD", "NPD", "MO", "SIGNATURE", "THE", "RAINCOAT",
         "KILLER", "SEXUAL", "MASSAGE"}
for k in ("JA", "KO"):
    for m in re.finditer(r"[A-Za-z][A-Za-z\-]{2,}", D[k]):
        w = m.group(0)
        if w in ALLOW or w.upper() in {x.upper() for x in ALLOW}:
            continue
        ctx = D[k][max(0, m.start()-50):m.end()+50].replace("\n", " ")
        print(f"  [{k}] '{w}' :: {ctx}")
print("\n=== XONG ===")
