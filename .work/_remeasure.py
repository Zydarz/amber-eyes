# -*- coding: utf-8 -*-
"""Do lai CHINH XAC chi phi: tach khoi tao 1 lan (VIGNETTE/GRAIN/ABUF) khoi chi phi moi lan goi."""
import os, sys, time, importlib
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))
os.environ["AE_EP"] = "08"

b = importlib.import_module("build_video3")
s = {x["id"]: x for x in b.SH}["2-05"]
t = (s["start"] + s["end"]) / 2
fi = int(t * b.FPS)

img = b.bg_image(s["bg"])
box = b.camera_box(s, t)

# --- BUOC 1: gia thuyet VGGAN voi thoi gian khoi tao ---
t0 = time.perf_counter()
frame = img.resize((1920, 1080), Image.BILINEAR, box=box)
arr = np.asarray(frame)
out = b.finishing(arr, fi)          # lần đầu: gồm VIGNETTE + GRAIN + ABUF
dt_first = (time.perf_counter() - t0) * 1000
print(f"LAN DAU (resize + finishing + khoi tao VIGNETTE/GRAIN/ABUF): {dt_first:.0f} ms")

# --- BUOC 2: chi phi thuan cua tung phan ---
N = 20
t0 = time.perf_counter()
for _ in range(N):
    frame2 = img.resize((1920, 1080), Image.BILINEAR, box=box)
dt_resize = (time.perf_counter() - t0) / N * 1000

arr2 = np.asarray(frame2)
t0 = time.perf_counter()
for k in range(N):
    b.finishing(arr2, fi + k)
dt_finish = (time.perf_counter() - t0) / N * 1000

print(f"resize thuan (N={N}):            {dt_resize:.0f} ms")
print(f"finishing thuan (N={N}):          {dt_finish:.0f} ms")
print(f"  -> khoi tao 1 lan (mua doi):    {dt_first - dt_resize - dt_finish:.0f} ms")

# --- BUOC 3: toan bo bg_frame (nhin chung) ---
t0 = time.perf_counter()
for k in range(N):
    b.bg_frame(s, t, fi + k)
dt_bgframe = (time.perf_counter() - t0) / N * 1000
print(f"bg_frame thuan (N={N}):           {dt_bgframe:.0f} ms")

# --- BUOC 4: ghi PNG that vao dia ---
tmp = ROOT / ".work" / "_pngbench2"
tmp.mkdir(exist_ok=True)
fr = b.render(fi).convert("RGB")
for i, kw in enumerate([dict(format="PNG"), dict(format="PNG", compress_level=3),
                        dict(format="PNG", compress_level=1), dict(format="JPEG", quality=92)]):
    p = tmp / f"x{i}"
    t0 = time.perf_counter()
    fr.save(p, **kw)
    print(f"ghi {str(kw):48s}: {(time.perf_counter()-t0)*1000:6.0f} ms  {p.stat().st_size/1e6:5.2f} MB")
    p.unlink()
tmp.rmdir()

# --- BUOC 5: chu + avatar ---
t0 = time.perf_counter()
for k in range(N):
    els = b.build_elements(s)
dt_el = (time.perf_counter() - t0) / N * 1000
fr2 = b.bg_frame(s, t, fi)
t0 = time.perf_counter()
for k in range(N):
    f2 = fr2.copy()
    for e in els:
        e.draw(f2, t)
dt_draw = (time.perf_counter() - t0) / N * 1000
print(f"build_elements: {dt_el:.0f} ms | copy+draw: {dt_draw:.0f} ms")

# --- BUOC 6: render() day du (gồm moi thu) ---
t0 = time.perf_counter()
for k in range(N):
    b.render(fi)
dt_render = (time.perf_counter() - t0) / N * 1000
print(f"render() day du: {dt_render:.0f} ms")
