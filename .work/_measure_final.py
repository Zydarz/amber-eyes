# -*- coding: utf-8 -*-
"""Do tong hop cuoi, lap lai 3 lan de lay so trung binh (tranh nhieu do khi may ban)."""
import os, sys, time, importlib, io
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
fr = b.render(fi).convert("RGB")
tmp = ROOT / ".work" / "_pngbench3"
tmp.mkdir(exist_ok=True)

def med(fn, n=5):
    v = []
    for _ in range(n):
        t0 = time.perf_counter()
        fn()
        v.append(time.perf_counter() - t0)
    return float(np.median(v)) * 1000

print("=== ghi file (median 5 lan) ===")
for label, kw, ext in [("PNG cl=6 mac dinh", dict(format="PNG"), "png"),
                       ("PNG cl=1", dict(format="PNG", compress_level=1), "png"),
                       ("JPEG q92", dict(format="JPEG", quality=92), "jpg")]:
    p = tmp / f"x.{ext}"
    dt = med(lambda: fr.save(p, **kw))
    print(f"  {label:22s}: {dt:6.0f} ms   {p.stat().st_size/1e6:5.2f} MB")
    p.unlink()
tmp.rmdir()

print()
print("=== render() (median 5 lan) ===")
print(f"  render() 1 frame: {med(lambda: b.render(fi)):6.0f} ms")

print()
print("=== thanh phan bg_frame ===")
img = b.bg_image(s["bg"])
box = b.camera_box(s, t)
print(f"  resize:            {med(lambda: img.resize((1920,1080), Image.BILINEAR, box=box)):6.0f} ms")
frame = img.resize((1920,1080), Image.BILINEAR, box=box)
arr = np.asarray(frame)
print(f"  finishing():       {med(lambda: b.finishing(arr, fi)):6.0f} ms")
print(f"  bg_frame():        {med(lambda: b.bg_frame(s, t, fi)):6.0f} ms")

print()
print("=== chu + avatar ===")
els = b.build_elements(s)
print(f"  build_elements:    {med(lambda: b.build_elements(s)):6.0f} ms")
base = b.bg_frame(s, t, fi)
def drawonly():
    f2 = base.copy()
    for e in els:
        e.draw(f2, t)
print(f"  copy+draw chu:     {med(drawonly):6.0f} ms")

print()
print("=== uoc luong cho 1 tap 223 shot x 3 ngon ngu ===")
r = med(lambda: b.render(fi))
p = med(lambda: fr.save(io.BytesIO(), format="PNG"))
print(f"  render 1 frame: {r:.0f} ms | ghi PNG: {p:.0f} ms")
print(f"  A (3 x render + 3 x ghi): {3*(r+p)*223/1000/60:5.1f} phut")
print(f"  B (1 x render + 3 x (copy+draw) + 3 x ghi): {(r + 3*79 + 3*p)*223/1000/60:5.1f} phut")
print(f"  B' (nen chung 3 ngon ngu, ghi PNG cl=1): {(r + 3*79 + 3*med(lambda: fr.save(io.BytesIO(), format='PNG', compress_level=1)))*223/1000/60:5.1f} phut")
