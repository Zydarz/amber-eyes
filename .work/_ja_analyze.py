#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phân tích cấu trúc 29 kịch bản VN: các dạng dòng, vai, nhịp nghỉ, tiêu đề hồi."""
import re
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "01_KICH_BAN"
OUT = Path(__file__).parent / "_ja_structure.txt"


def canonical(tap):
    """File VN chuẩn của tập: mới nhất trong TapXX, bỏ _ban_goc/_truoc_review/_EN."""
    d = ROOT / tap
    cands = [f for f in d.glob("kichban_*.md")
             if not re.search(r"(_ban_goc|_truoc_review|_EN)", f.name)]
    return max(cands, key=lambda p: p.stat().st_mtime)


def shape(line):
    s = line.strip()
    if not s:
        return "BLANK"
    if s == "---":
        return "HR"
    if s.startswith("|"):
        return "TABLE"
    if re.match(r"^##\s", s):
        return "H2"
    if re.match(r"^#\s", s):
        return "H1"
    if re.match(r"^\*\*\[[A-ZÀ-ỸĐ]+\]:\*\*", s):
        return "CUE"
    if re.match(r"^\*\*\[[^\]]+\]\*\*", s):
        return "PAUSE"
    if re.match(r"^\*\*[^*]+\*\*\s*(\*\(.*\)\*)?\s*:", s):
        return "ROLE"
    if re.match(r"^\*\s+", s):
        return "BULLET"
    if re.match(r"^\d+\.\s+", s):
        return "NUM"
    if s.startswith("*") or s.startswith("**"):
        return "EMPH"
    return "TEXT"


def main():
    shapes = Counter()
    roles = Counter()
    pause = Counter()
    headings = []
    table_rows = 0
    per_ep = []
    for i in range(1, 30):
        tap = f"Tap{i:02d}"
        f = canonical(tap)
        lines = f.read_text(encoding="utf-8").splitlines()
        c = Counter()
        acts = 0
        for ln in lines:
            sh = shape(ln)
            shapes[sh] += 1
            c[sh] += 1
            if sh == "H2" and re.match(r"^##\s*HỒI\s*\d", ln.strip()):
                acts += 1
            m = re.match(r"^\*\*([^*]+)\*\*", ln.strip())
            if m and sh in ("ROLE", "CUE"):
                roles[m.group(1)] += 1
            m = re.match(r"^\*\*\[(?:Nghỉ|Pause)([^\]]*)\]\*\*", ln.strip())
            if m:
                pause[m.group(1)[:40]] += 1
            if sh == "H2":
                headings.append(f"{tap}: {ln.strip()[:90]}")
        per_ep.append(f"{tap} | {f.name} | lines={len(lines)} | acts={acts} | {dict(c)}")
        table_rows += c["TABLE"]

    txt = ["=== PER EPISODE ==="] + per_ep + ["", "=== SHAPES ==="] + \
          [f"{k}: {v}" for k, v in shapes.most_common()] + ["", "=== ROLE/CUE LABELS ==="] + \
          [f"{k}: {v}" for k, v in roles.most_common()] + ["", "=== PAUSE FORMS ==="] + \
          [f"{k}: {v}" for k, v in pause.most_common(30)] + ["", "=== H2 HEADINGS (all) ==="] + headings
    OUT.write_text("\n".join(txt), encoding="utf-8")
    print(f"written {OUT}  (table rows total={table_rows})")


if __name__ == "__main__":
    main()
