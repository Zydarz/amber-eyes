# -*- coding: utf-8 -*-
"""Prototype phuong an 'nen 1 lan + chu 3 ngon ngu' cho 1 tap.
Kiem: byte-identical voi cach hien tai (VI) + do tiet kiem that."""
import os, sys, time, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))

import importlib

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

mods = {t: load(t) for t in [None, "en", "ja"]}
tag = {None: "vi", "en": "en", "ja": "ja"}

b = mods[None]
SH = b.SH

# ---- thong ke shot dac biet ----
n_bg2 = sum(1 for s in SH if s.get("bg2"))
trans = {}
for s in SH:
    trans[s.get("transition", "none")] = trans.get(s.get("transition", "none"), 0) + 1
print(f"Tap 08: {len(SH)} shot | co bg2: {n_bg2} | transition: {trans}")
print(f"  shot co intro: {sum(1 for s in SH if s['id']=='1-00')} | shot cuoi (fade): 1")

# ---- phan loai shot de biet nen co dung chung duoc khong ----
# bg_frame chung duoc khi: khong co bg2  (camera_box o giua shot luon p=0.5 -> doc lap ngon ngu)
SHARED_OK = [s for s in SH if not s.get("bg2")]
print(f"  nen dung chung duoc (khong bg2): {len(SHARED_OK)}/{len(SH)}")

# ---- kiem byte: lay 1 shot khong bg2, dung 2 cach ----
print()
print("=== Kiem byte: shot thuong (khong bg2) ===")
for sid in ["1-11", "4-14", "3-09", "2-05"]:
    s = {x["id"]: x for x in SH}[sid]
    t = (s["start"] + s["end"]) / 2
    fi = int(t * b.FPS)

    old = b.render(fi).convert("RGB")

    # cach moi: nen chung (fi chung) + chu + nhan vat
    new = b.bg_frame(s, t, fi)
    for e in b.build_elements(s):
        e.draw(new, t)
    b.draw_characters(new, t, fi, s)
    new = new.convert("RGB")

    h1 = hashlib.md5(old.tobytes()).hexdigest()[:12]
    h2 = hashlib.md5(new.tobytes()).hexdigest()[:12]
    diff = sum(1 for p, q in zip(old.getdata(), new.getdata()) if p != q) if h1 != h2 else 0
    print(f"  {sid}: hien tai={h1}  moi={h2}  -> {'KHONG DOI' if h1==h2 else f'KHAC ({diff} px)'}"
          f"  [transition={s.get('transition','none')}]")

# ---- do that cua 2 cach tren 25 shot ----
print()
print("=== Do 25 shot: VI ===")
ids = [s["id"] for s in SH[:25]]
t0 = time.perf_counter()
for sid in ids:
    s = {x["id"]: x for x in SH}[sid]
    t = (s["start"] + s["end"]) / 2
    b.render(int(t * b.FPS)).convert("RGB")
dt_old = time.perf_counter() - t0
print(f"  render 1 ngon ngu (25 shot): {dt_old:.1f} s  ({dt_old/25*1000:.0f} ms/shot)")

t0 = time.perf_counter()
for sid in ids:
    s = {x["id"]: x for x in SH}[sid]
    t = (s["start"] + s["end"]) / 2
    fi = int(t * b.FPS)
    base = b.bg_frame(s, t, fi)
    for lang, bb in mods.items():
        s2 = {x["id"]: x for x in bb.SH}[sid]
        f2 = base.copy()
        for e in bb.build_elements(s2):
            e.draw(f2, t)
        bb.draw_characters(f2, t, fi, s2)
dt_new = time.perf_counter() - t0
print(f"  nen 1 lan + chu 3 ngon ngu (25 shot): {dt_new:.1f} s  ({dt_new/25*1000:.0f} ms/shot)")
print(f"  => tiet kiem {dt_old-dt_new:.1f} s/25shot  -> x223 shot x... ")
print(f"  => uoc: hien tai 3 ngon ngu {dt_old*3/25*223/60:.1f} phut | moi {dt_new/25*223/60:.1f} phut")
