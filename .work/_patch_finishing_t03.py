#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Toi uu finishing() — ket qua PHAI giong het (bit-for-bit), chi giam cap phat bo nho.

build_video3.py co KET THUONG HON TAP \\r\\n VA \\r\\n lan lan -> dung regex linh hoat,
tu giu nguyen he xuong dong cua tung khoi khi ghi lai.
"""
import re
import sys
from pathlib import Path

P = Path(r"D:\TEST\Gax\amber-eyes\.work\build_video3.py")
src = P.read_bytes().decode("utf-8")


def flex(lines):
    return r"\r*\n".join(re.escape(l) for l in lines)


def replace(src, old_lines, new_lines):
    m = re.search(flex(old_lines), src)
    if not m:
        return src, None
    sep = "\r\r\n" if "\r\r\n" in m.group(0) else "\r\n"
    block = sep.join(new_lines)
    return src[:m.start()] + block + src[m.end():], sep


PATCHES = [
    (["    a = arr.astype(np.float32) * VIGNETTE + GRAIN[fi % 6]",
      "",
      "    a[:, 1:, 0] = a[:, :-1, 0]                       # rgbashift ±1 (red one px right)",
      "",
      "    return np.clip(a, 0, 255).astype(np.uint8)"],
     ["    # dung buffer tai su dung de giam cap phat bo nho (ket qua giong het)",
      "    a = ABUF",
      "    np.multiply(arr, VIGNETTE, out=a)              # == arr.astype(f32) * VIGNETTE",
      "    np.add(a, GRAIN[fi % 6], out=a)",
      "",
      "    red = a[:, :, 0].copy()                        # tranh chong lap khi shift",
      "    a[:, 1:, 0] = red[:, :-1]                      # rgbashift ±1 (red one px right)",
      "",
      "    np.clip(a, 0, 255, out=a)",
      "    return a.astype(np.uint8)"]),

    (["VIGNETTE = None", "", "GRAIN = None"],
     ["VIGNETTE = None", "", "GRAIN = None", "", "ABUF = None"]),

    (["def finishing(arr, fi):", "", "    global VIGNETTE, GRAIN"],
     ["def finishing(arr, fi):", "", "    global VIGNETTE, GRAIN, ABUF"]),

    (["        GRAIN = [rng.normal(0, 5.5, (H, W, 1)).astype(np.float32) for _ in range(6)]"],
     ["        GRAIN = [rng.normal(0, 5.5, (H, W, 1)).astype(np.float32) for _ in range(6)]",
      "",
      "        ABUF = np.empty((H, W, 3), dtype=np.float32)"]),
]

fail = 0
for old, new in PATCHES:
    src, sep = replace(src, old, new)
    if sep is None:
        print(f"[FAIL] khong khop: {old[0][:70]!r}")
        fail += 1
        continue
    print(f"[OK ] {old[0][:70]!r}  (sep={sep!r})")

if fail:
    print("\nKHONG ghi file.")
    sys.exit(1)
with open(P, "w", encoding="utf-8", newline="") as f:
    f.write(src)
chk = P.read_bytes()
print("\nDa ghi. BOM:", chk[:3].hex(), "| CRLF:", chk.count(b"\r\r\n"), "| LF:", chk.count(b"\n"))
