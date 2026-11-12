# -*- coding: utf-8 -*-
"""BENCHMARK CÔNG BẰNG: xen kẽ A/B nhiều vòng (tránh lệch do lạnh/nóng).
Cùng số lượng PNG ghi ra cho mỗi phương án."""
import os, sys, time, importlib
from pathlib import Path
import numpy as np
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))
os.environ["AE_EP"] = "08"

def load(lang):
    for m in list(sys.modules):
        if m in ("build_video3", "edition"):
            del sys.modules[m]
    os.environ["AE_EP"] = "08"
    if lang:
        os.environ["AE_LANG"] = lang
    else:
        os.environ.pop("AE_LANG", None)
    return importlib.import_module("build_video3")

mods = {l: load(l) for l in [None, "en", "ja"]}
tag = {None: "vi", "en": "en", "ja": "ja"}
vi = mods[None]
SH = {l: {s["id"]: s for s in b.SH} for l, b in mods.items()}
N = 20
IDS = [s["id"] for s in vi.SH[:N]]
tmp = ROOT / ".work" / "_bench_fair"
tmp.mkdir(exist_ok=True)

def A(ids):
    for sid in ids:
        for l, b in mods.items():
            s = SH[l][sid]
            tt = (s["start"] + s["end"]) / 2
            fr = b.render(int(tt * b.FPS)).convert("RGB")
            fr.save(tmp / f"{tag[l]}_{sid}.png", format="PNG")

def B(ids):
    for sid in ids:
        sv = SH[None][sid]
        fi = int(((sv["start"] + sv["end"]) / 2) * vi.FPS)
        t = fi / vi.FPS
        base = vi.bg_frame(sv, t, fi)
        for l, b in mods.items():
            s = SH[l][sid]
            fr = base.copy()
            for e in b.build_elements(s):
                e.draw(fr, t)
            b.draw_characters(fr, t, fi, s)
            fr.convert("RGB").save(tmp / f"{tag[l]}_{sid}.png", format="PNG")

def Bpng1(ids):
    """B + ghi PNG compress_level=1"""
    for sid in ids:
        sv = SH[None][sid]
        fi = int(((sv["start"] + sv["end"]) / 2) * vi.FPS)
        t = fi / vi.FPS
        base = vi.bg_frame(sv, t, fi)
        for l, b in mods.items():
            s = SH[l][sid]
            fr = base.copy()
            for e in b.build_elements(s):
                e.draw(fr, t)
            b.draw_characters(fr, t, fi, s)
            fr.convert("RGB").save(tmp / f"{tag[l]}_{sid}.png", format="PNG", compress_level=1)

# warm-up
A(IDS[:3]); B(IDS[:3]); Bpng1(IDS[:3])
for f in tmp.glob("*.png"): f.unlink()

res = {"A": [], "B": [], "Bpng1": []}
ROUNDS = 3
for r in range(ROUNDS):
    for name, fn in [("A", A), ("B", B), ("Bpng1", Bpng1)]:
        t0 = time.perf_counter()
        fn(IDS)
        dt = time.perf_counter() - t0
        res[name].append(dt)
        for f in tmp.glob("*.png"): f.unlink()
    print(f"  vong {r+1}: " + " | ".join(f"{k} {res[k][-1]:.1f}s" for k in res))

print()
for k, v in res.items():
    m = np.median(v)
    print(f"  {k:6s}: median {m:5.1f} s / {N} shot  -> uoc 223 shot: {m/N*223/60:4.1f} phut")
ma, mb = np.median(res["A"]), np.median(res["B"])
print(f"  B vs A: {100*(1-mb/ma):.0f}% nhanh hon")
mb1 = np.median(res["Bpng1"])
print(f"  Bpng1 vs A: {100*(1-mb1/ma):.0f}% nhanh hon")
tmp.rmdir()
