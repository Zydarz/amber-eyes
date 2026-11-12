# -*- coding: utf-8 -*-
"""Biet moi + tach chi phi:
  A  : hien tai — moi ngon ngu render lai toan bo
  B1 : nen dung chung (crop+grain cua VI) + chu/avatar theo thoi diem RIENG tung ngon ngu
  B2 : chi dung chung phan CROP, grain theo fi rieng tung ngon ngu  -> byte-identical 3 ngon ngu
Tach: resize vs finishing (cai nao ton thoi gian)."""
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
vi = mods[None]
SH = {l: {s["id"]: s for s in b.SH} for l, b in mods.items()}
SHVI = SH[None]
IDS = [s["id"] for s in vi.SH[:25]]

# ---------- tach resize vs finishing ----------
print("=== 1) Chi phi trong bg_frame: resize vs finishing ===")
s = SHVI[IDS[3]]
t = (s["start"] + s["end"]) / 2
fi = int(t * vi.FPS)
img = vi.bg_image(s["bg"])
box = vi.camera_box(s, t)

t0 = time.perf_counter()
for _ in range(5):
    frame = img.resize((1920, 1080), Image.BILINEAR, box=box)
dt_resize = (time.perf_counter() - t0) / 5

arr = np.asarray(frame)
t0 = time.perf_counter()
for k in range(5):
    vi.finishing(arr, fi + k)
dt_finish = (time.perf_counter() - t0) / 5
print(f"  resize (2112x1188 -> 1920x1080): {dt_resize*1000:6.0f} ms")
print(f"  finishing (vignette+grain+shift): {dt_finish*1000:6.0f} ms")
print(f"  => ton: {'resize' if dt_resize>dt_finish else 'finishing'}")

# ---------- tach text/avatar ----------
print()
print("=== 2) Chi phi chu + avatar (3 ngon ngu, tren nen da san) ===")
base = vi.bg_frame(SHVI[IDS[3]], t, fi)
for l, b in mods.items():
    sh = SH[l][IDS[3]]
    t0 = time.perf_counter()
    for _ in range(5):
        els = b.build_elements(sh)
    dt_el = (time.perf_counter() - t0) / 5
    fr = base.copy()
    t0 = time.perf_counter()
    for e in els:
        e.draw(fr, t)
    dt_dr = time.perf_counter() - t0
    print(f"  [{tag[l]}] build_elements {dt_el*1000:5.1f} ms | draw {dt_dr*1000:5.1f} ms")

# ---------- B1 / B2 ----------
def build_A(sid):
    outs = {}
    for l, b in mods.items():
        s = SH[l][sid]
        tt = (s["start"] + s["end"]) / 2
        outs[l] = b.render(int(tt * b.FPS)).convert("RGB")
    return outs

def build_B1(sid):
    """nen chung (crop+grain cua VI), chu/avatar theo thoi diem rieng tung ngon ngu"""
    sv = SHVI[sid]
    fi_c = int(((sv["start"] + sv["end"]) / 2) * vi.FPS)
    t_c = fi_c / vi.FPS
    base = vi.bg_frame(sv, t_c, fi_c)
    outs = {}
    for l, b in mods.items():
        s = SH[l][sid]
        tt = (s["start"] + s["end"]) / 2
        fr = base.copy()
        for e in b.build_elements(s):
            e.draw(fr, tt)
        b.draw_characters(fr, tt, int(tt * b.FPS), s)
        outs[l] = fr.convert("RGB")
    return outs

def build_B2(sid):
    """chi dung chung CROP; grain theo fi rieng tung ngon ngu -> byte-identical"""
    sv = SHVI[sid]
    fi_c = int(((sv["start"] + sv["end"]) / 2) * vi.FPS)
    t_c = fi_c / vi.FPS
    img = vi.bg_image(sv["bg"])
    box = vi.camera_box(sv, t_c)
    crop = img.resize((1920, 1080), Image.BILINEAR, box=box)
    outs = {}
    for l, b in mods.items():
        s = SH[l][sid]
        tt = (s["start"] + s["end"]) / 2
        fi_l = int(tt * b.FPS)
        fr = Image.fromarray(b.finishing(np.asarray(crop), fi_l)).convert("RGBA")
        for e in b.build_elements(s):
            e.draw(fr, tt)
        b.draw_characters(fr, tt, fi_l, s)
        outs[l] = fr.convert("RGB")
    return outs

print()
print("=== 3) Fidelity: A vs B1 vs B2 ===")
for sid in ["1-11", "3-09", "2-05", "4-14"]:
    A = build_A(sid)
    B1 = build_B1(sid)
    B2 = build_B2(sid)
    line = f"  {sid}: "
    for l in mods:
        da = np.abs(np.asarray(A[l], np.int16) - np.asarray(B1[l], np.int16)).max(axis=2)
        db = np.abs(np.asarray(A[l], np.int16) - np.asarray(B2[l], np.int16)).max(axis=2)
        line += f"[{tag[l]}] B1:{int((da>0).sum())}px/mx{da.max()} B2:{int((db>0).sum())}px/mx{db.max()}  "
    print(line)

# ---------- timing ----------
print()
print("=== 4) End-to-end 25 shot x 3 ngon ngu (KHONG ghi file) ===")
for name, fn in [("A", build_A), ("B1", build_B1), ("B2", build_B2)]:
    t0 = time.perf_counter()
    for sid in IDS:
        fn(sid)
    dt = time.perf_counter() - t0
    print(f"  {name}: {dt:5.1f} s  ({dt/len(IDS)*1000:5.0f} ms/shot)  -> uoc 223 shot: {dt/len(IDS)*223/60:.1f} phut")
