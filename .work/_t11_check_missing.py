# -*- coding: utf-8 -*-
"""Liệt kê chunk nào còn THIẾU prompt (k>1) + nội dung câu để bổ sung."""
import collections
import sys

sys.path.insert(0, r"D:/TEST/Gax/amber-eyes/.work")
from _t11_chunk_plan import parse, build, MD  # noqa: E402
from _t11_new_bg_jobs import NEW  # noqa: E402

rows = parse(MD)
chunks, end_card = build(rows)
keep = collections.Counter()
miss = []
for i, c in enumerate(chunks):
    keep[c["parent"]] += 1
    if keep[c["parent"]] > 1:
        if i not in NEW:
            miss.append((i, c["parent"], c["n"], c["sec"],
                         [r["sid"] for r in c["rows"]],
                         [r["cau"] for r in c["rows"]],
                         [r["chu"] for r in c["rows"]]))
print("thiếu prompt:", len(miss))
for m in miss:
    print(f"\n[{m[0]}] parent={m[1]} n={m[2]} {m[3]}s sid={'/'.join(m[4])} cau={'/'.join(m[5])}")
    for t in m[6]:
        print("     ", t.replace("*", "")[:150])
print("\nDÙNG CHƯA (có trong NEW nhưng không khớp chunk):",
      sorted(set(NEW) - {i for i in range(len(chunks))}) )
