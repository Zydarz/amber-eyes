# -*- coding: utf-8 -*-
"""(1) camera_box co phu thuoc ngon ngu khong?  (2) ghi PNG toi dia ton bao lau?"""
import os, sys, time, importlib
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))

def load(lang, ep="08"):
    for m in list(sys.modules):
        if m in ("build_video3", "edition"):
            del sys.modules[m]
    os.environ["AE_EP"] = ep
    if lang:
        os.environ["AE_LANG"] = lang
    else:
        os.environ.pop("AE_LANG", None)
    return importlib.import_module("build_video3")

mods = {l: load(l) for l in [None, "en", "ja"]}
tag = {None: "vi", "en": "en", "ja": "ja"}

print("=== (1) camera_box theo ngon ngu (t = giua shot cua chinh ngon ngu do) ===")
for sid in ["1-11", "3-09", "2-05", "4-14"]:
    boxes = {}
    durs = {}
    cams = {}
    for l, b in mods.items():
        s = {x["id"]: x for x in b.SH}[sid]
        t = (s["start"] + s["end"]) / 2
        fi = int(t * b.FPS)
        boxes[tag[l]] = tuple(round(v, 3) for v in b.camera_box(s, fi / b.FPS))
        durs[tag[l]] = round(s["end"] - s["start"], 2)
        cams[tag[l]] = s["camera"]
    same = len(set(boxes.values())) == 1
    print(f"  {sid}: camera={cams}  boxes={boxes}  -> {'GIONG' if same else 'KHAC'}")
    if not same:
        print(f"        do dai shot: {durs}")

print()
print("=== (2) Thoi gian + dung luong ghi PNG THAT vao dia ===")
vi = mods[None]
s = {x["id"]: x for x in vi.SH}["2-05"]
t = (s["start"] + s["end"]) / 2
fr = vi.render(int(t * vi.FPS)).convert("RGB")
tmp = ROOT / ".work" / "_pngbench"
tmp.mkdir(exist_ok=True)

for i, (label, kw) in enumerate([("PNG mac dinh (cl=6)", dict(format="PNG")),
                  ("PNG cl=3", dict(format="PNG", compress_level=3)),
                  ("PNG cl=1", dict(format="PNG", compress_level=1)),
                  ("PNG cl=0 (khong nen)", dict(format="PNG", compress_level=0)),
                  ("JPEG q92", dict(format="JPEG", quality=92)),
                  ("WebP q92", dict(format="WEBP", quality=92))]):
    p = tmp / f"x{i}.out"
    t0 = time.perf_counter()
    fr.save(p, **kw)
    dt = time.perf_counter() - t0
    print(f"  {label:24s}: {dt*1000:6.0f} ms   {p.stat().st_size/1e6:5.2f} MB")
    p.unlink()
tmp.rmdir()

print()
print("=== (3) RAM khi nap 3 module build_video3 cung luc ===")
try:
    import psutil
    pr = psutil.Process()
    print(f"  RSS sau khi nap 3 module: {pr.memory_info().rss/1e6:.0f} MB")
except ImportError:
    print("  (khong co psutil)")
