# -*- coding: utf-8 -*-
"""Giải nén PNG từ gói zip output Kaggle vào .work/tk_img_raw_t54/.

usage: py -3 .work/_extract_flux_tk54.py <thu_muc_out> [<thu_muc_zip>]
"""
import pathlib
import sys
import zipfile

HERE = pathlib.Path(__file__).resolve().parent
RAW = HERE / "tk_img_raw_t54"
RAW.mkdir(parents=True, exist_ok=True)

out_dir = pathlib.Path(sys.argv[1])
zips = sorted(out_dir.glob("*.zip"))
if len(sys.argv) > 2:
    zips = [pathlib.Path(sys.argv[2])]

n = 0
for z in zips:
    with zipfile.ZipFile(z, "r") as zf:
        for item in zf.namelist():
            if not item.endswith(".png"):
                continue
            name = pathlib.Path(item).name
            if not name.startswith("tk54_"):
                continue
            dst = RAW / name
            with zf.open(item) as src, open(dst, "wb") as d:
                d.write(src.read())
            n += 1
    print("  %s -> %d anh" % (z.name, n))

pngs = sorted(RAW.glob("tk54_*.png"))
jpg = sorted(RAW.glob("tk54_*.jpg"))
print("RAW: %d png (Kaggle) + %d jpg (MiniMax) = %d nen" % (len(pngs), len(jpg), len(pngs) + len(jpg)))
