# -*- coding: utf-8 -*-
"""In danh sách nhóm nền (chunk) của Tập 11 kèm nội dung câu, để đặt tên + viết prompt."""
import collections
import sys

sys.path.insert(0, r"D:/TEST/Gax/amber-eyes/.work")
from _t11_chunk_plan import parse, build, MD  # noqa: E402

rows = parse(MD)
chunks, end = build(rows)
keep = collections.Counter()
out = []
for i, c in enumerate(chunks):
    keep[c["parent"]] += 1
    idx = keep[c["parent"]]
    new = c["parent"] if idx == 1 else f"{c['parent']}_v{idx}"
    out.append((i, new, c["parent"], c["n"], c["sec"],
                [r["sid"] for r in c["rows"]], [r["cau"] for r in c["rows"]],
                [r["chu"] for r in c["rows"]]))
print("nhom:", len(out), "| MANH:", sum(1 for o in out if o[1] != o[2]),
      "| giu ten cu:", sum(1 for o in out if o[1] == o[2]))
print("THE KET:", end["sid"], end["bg"])
for o in out:
    txt = " || ".join(x.replace("*", "") for x in o[7])
    print(f"[{o[0]:>3}] {o[1][:60]:<60} n={o[3]} {o[4]:>5}s {'/'.join(o[6]):<14} {txt[:130]}")
