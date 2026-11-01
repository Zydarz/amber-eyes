import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
src = (ROOT / ".work" / "qc_shots_t04.py").read_text(encoding="utf-8")
src = src.split("def main()")[0]
ns = {"__file__": str(ROOT / ".work" / "qc_shots_t04.py")}
exec(compile(src, "qc", "exec"), ns)
norm_num = ns["norm_num"]

s = json.loads((ROOT / ".work" / "script_tap04.json").read_text(encoding="utf-8-sig"))
sent = {}
for el in s:
    if el.get("kind") != "LOI":
        continue
    for x in el["sentences"]:
        sent[x["id"]] = x["text"]

tbl = (ROOT / ".work" / "_shots_t04_new.md").read_text(encoding="utf-8-sig")
for line in tbl.splitlines():
    if line.startswith("| 3-11 "):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        print("CAU cell :", repr(cells[1]))
        codes = []
        for ma, x, y in re.findall(r"`(\d\.\d+)#(\d+)`(?:–`#(\d+)`)?", cells[1]):
            codes += [f"{ma}#{k}" for k in range(int(x), int(y or x) + 1)]
        print("codes    :", codes)
        body = " ".join(sent.get(c, "") for c in codes)
        print("body has 'hai mươi mối'? ", "hai mươi mối" in body)
        bn = norm_num(body)
        print("'21' in body_n?", "21" in bn)
        i = bn.find("michael")
        print("body_n around michael:", repr(bn[max(0, i - 40):i + 40]))
        print()
        print("chu cell :", repr(cells[5][:160]))
        break
