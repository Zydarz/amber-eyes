# -*- coding: utf-8 -*-
import json
import pathlib
import re

for p in sorted(pathlib.Path(r"D:/TEST/Gax/amber-eyes/.work/kaggle_flux").glob("t15k*/*.ipynb")):
    txt = p.read_text(encoding="utf-8")
    names = re.findall(r'"name": "([a-z0-9_]+)"', txt)
    seeds = re.findall(r'"seed": (\d+)', txt)
    print(p.name, "| so anh:", len(names), "| seed range:", (seeds[0], seeds[-1]) if seeds else "-")
    if names:
        print("   ", names[:3], "...", names[-2:])
