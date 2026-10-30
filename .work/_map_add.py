#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them dong vao manifest tai lieu YouTube (.work/yt_map.tsv).

Dung:
  py -3 .work/_map_add.py "<ten track>|<ma sfx>|<loai>|<dest>|<the loai>|<dur>"
  py -3 .work/_map_add.py <file.txt>        # moi dong 1 truong, tach bang TAB hoac |
  (doc duong dan stdin neu khong co doi so)

Manifest: tên_track <TAB> mã_sfx <TAB> loại <TAB> thư_mục_đích <TAB> thể_loại_youtube <TAB> thời_lượng_giây
Thứ tự dòng = thứ tự bấm "Tải xuống" -> watcher ghép file .tmp theo thứ tự này.
"""
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

MAP = Path(__file__).resolve().parents[1] / ".work" / "yt_map.tsv"


def norm(line):
    p = [x.strip() for x in line.replace("\t", "|").split("|")]
    p = (p + [""] * 6)[:6]
    if not p[0] or not p[1]:
        raise ValueError("thieu ten track hoac ma sfx: %r" % line)
    try:
        p[5] = "%.2f" % float(p[5]) if p[5] else "0"
    except ValueError:
        p[5] = "0"
    return "\t".join(p)


def main():
    raw = sys.argv[1:]
    if not raw:
        raw = [ln for ln in sys.stdin.read().splitlines() if ln.strip()]
    elif len(raw) == 1 and Path(raw[0]).is_file():
        raw = [ln for ln in Path(raw[0]).read_text(encoding="utf-8-sig").splitlines() if ln.strip()]
    rows = [norm(ln) for ln in raw]
    MAP.parent.mkdir(parents=True, exist_ok=True)
    with open(MAP, "a", encoding="utf-8", newline="\n") as f:
        for r in rows:
            f.write(r + "\n")
    total = len([x for x in MAP.read_text(encoding="utf-8-sig").splitlines() if x.strip()])
    print("them %d dong (manifest moi co %d dong)" % (len(rows), total))
    for r in rows:
        print("  + " + r.replace("\t", " | "))


if __name__ == "__main__":
    main()
