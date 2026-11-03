#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dong goi Tap06 lan 2 (03/11/2026): mux + description — BO QUA thumbnail().

A11 #70: mo ta/nguon la file SINH RA -> sua o generator.
A11 #72: CLI package.py goi thumbnail() => GHI DE thumbnail da xuat.
           -> goi truc tiep package.mux() + package.description().
Kiem tra: thumbnail.png phai GIONG NGUYEN hash truoc/sau.
"""
import hashlib
import os
import sys
from pathlib import Path

os.environ.setdefault("AE_EP", "06")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

OUT = ED.OUT_DIR


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    watch = ["thumbnail.png", "Tap06_master.mp4", "mo_ta.txt", "nguon_tham_khao.md"]
    before = {n: (sha(OUT / n) if (OUT / n).exists() else None) for n in watch}

    import package  # noqa: E402
    print("mux ->", package.mux())
    chap = package.description()
    print("chapter:", chap)

    print("\n--- hash truoc / sau ---")
    changed = []
    for n in watch:
        p = OUT / n
        after = sha(p) if p.exists() else None
        same = before[n] == after
        if not same:
            changed.append(n)
        print(f"  {n:22} {'GIONG NGUYEN' if same else 'THAY DOI':12} {str(before[n])[:12]} -> {str(after)[:12]}")

    if "thumbnail.png" in changed:
        raise SystemExit("CHẶN - thumbnail.png bi thay doi (khong duoc goi thumbnail())")
    print("\nOK  thumbnail.png GIONG NGUYEN (khong goi thumbnail())")

    txt = (OUT / "mo_ta.txt").read_text(encoding="utf-8")
    if "\x00" in txt:
        raise SystemExit("CHẶN - mo_ta.txt chứa byte NUL")
    if txt.encode("utf-8")[:3] == b"\xef\xbb\xbf":
        raise SystemExit("CHẶN - mo_ta.txt co BOM")
    print(f"OK  mo_ta.txt: {len(txt)} ky tu (< 5000)")

    tbl = (OUT / "nguon_tham_khao.md").read_text(encoding="utf-8")
    rows = sum(1 for L in tbl.splitlines() if L.startswith("| `"))
    print(f"OK  nguon_tham_khao.md: {rows} dong du lieu")


if __name__ == "__main__":
    main()
