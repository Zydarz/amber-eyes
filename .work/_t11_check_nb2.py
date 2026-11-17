import json
import pathlib
import re

for d in ["d1", "d2"]:
    p = pathlib.Path(f".work/kaggle_flux/{d}/flux2_generator.ipynb")
    nb = json.loads(p.read_text(encoding="utf-8"))
    code = "".join("".join(c["source"]) for c in nb["cells"] if c["cell_type"] == "code")
    seeds = sorted({int(s) for s in re.findall(r"'seed':\s*(\d+)", code)})
    names = re.findall(r"'name':\s*'(t11_[a-z0-9_]+)'", code)
    print(f"=== {d}")
    print(f"    so anh trong notebook: {len(names)}")
    print(f"    seed: {seeds[:3]} ... {seeds[-3:]}  (trung: {len(seeds) - len(set(seeds))})")
    print(f"    dau/cuoi: {names[0]} -> {names[-1]}")
    # kiem tra full prompt co BLANK khong
    nblank = code.count("completely blank and unmarked with no writing at all")
    print(f"    so prompt co 'completely blank...': {nblank}")
    # kiem tra co 'no text' trong NEG
    print(f"    NEG co 'strictly no text': {code.count('strictly no text')}")
