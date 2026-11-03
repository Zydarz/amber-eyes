#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh lại mo ta Tap06 (A11 #70/#72): goi `description()` TRUC TIEP, khong goi CLI
=> khong go de thumbnail da xuat. Backup truoc (L5), do hash truoc/sau.

Usage: py -3 .work/_regen_desc_t06.py
"""
import hashlib
import os
import shutil
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
CU = WORK / "_cu" / "t06_mo_ta_truoc_nguon"
CU.mkdir(parents=True, exist_ok=True)


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()


def main():
    watched = ["mo_ta.txt", "nguon_tham_khao.md", "thumbnail.png", "Tap06_master.mp4"]
    before = {}
    for n in watched:
        p = OUT / n
        before[n] = sha(p) if p.exists() else None

    for n in ("mo_ta.txt", "nguon_tham_khao.md"):
        p = OUT / n
        if p.exists():
            shutil.copy2(p, CU / n)
    print(f"backup -> {CU}")

    import package  # noqa: E402  (import sau khi AE_EP đã set)
    chap = package.description()
    print("chapter:", chap)

    print("\n--- hash truoc / sau ---")
    changed = []
    for n in watched:
        p = OUT / n
        after = sha(p) if p.exists() else None
        same = "GIONG NGUYEN" if before[n] == after else "THAY DOI"
        if before[n] != after:
            changed.append(n)
        print(f"  {n:22} {same}  {str(before[n])[:12]} -> {str(after)[:12]}")

    txt = (OUT / "mo_ta.txt").read_text(encoding="utf-8")
    print(f"\nmo_ta.txt: {len(txt)} ký tự (YouTube giới hạn 5000)")
    if "\x00" in txt:
        raise SystemExit("CHẶN - mo_ta.txt chứa byte NUL")
    if txt.encode("utf-8")[:3] == b"\xef\xbb\xbf":
        raise SystemExit("CHẶN - mo_ta.txt có BOM")
    if len(txt) > 5000:
        raise SystemExit("CHẶN - mo_ta.txt vượt 5000 ký tự")
    for need in ("📚 NGUỒN THAM KHẢO", "http"):
        if need not in txt:
            raise SystemExit(f"CHẶN - mo_ta.txt thiếu mục {need}")
    print("OK  mo_ta.txt hợp lệ (UTF-8 không BOM, có khối nguồn, < 5000 ký tự)")

    tbl = (OUT / "nguon_tham_khao.md").read_text(encoding="utf-8")
    rows = sum(1 for L in tbl.splitlines() if L.startswith("| `"))
    print(f"OK  nguon_tham_khao.md: {rows} dòng dữ kiện")
    if changed != ["mo_ta.txt", "nguon_tham_khao.md"]:
        raise SystemExit(f"CHẶN - file ngoài dự kiến bị đổi: {changed}")
    print("OK  thumbnail.png và Tap06_master.mp4 KHÔNG đổi (không gọi thumbnail()/mux())")


if __name__ == "__main__":
    main()
