# -*- coding: utf-8 -*-
"""Kiem chung: bg_frame co phu thuoc ngon ngu khong? (ve grain phase fi%6)
Va do phuong an: render nen 1 lan + ve chu 3 ngon ngu."""
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

IDS = ["1-02", "1-11", "2-05", "3-09", "4-14", "5-20"]
mods = {t: load(t) for t in [None, "en", "ja"]}
tag = {None: "vi", "en": "en", "ja": "ja"}

# --- 1) bg_frame voi fi CHUNG (cung grain phase) ---
print("=== 1) bg_frame voi fi chung (fix fi=10000) ===")
for sid in IDS:
    hs = {}
    for lang, b in mods.items():
        s = {x["id"]: x for x in b.SH}[sid]
        fr = b.bg_frame(s, (s["start"] + s["end"]) / 2, 10000)
        hs[tag[lang]] = hashlib.md5(fr.convert("RGB").tobytes()).hexdigest()[:12]
    same = len(set(hs.values())) == 1
    print(f"  {sid}: {hs} -> {'GIONG HET' if same else 'KHAC'}")

# --- 2) bg_frame voi fi THAT (grain phase khac) ---
print()
print("=== 2) bg_frame voi fi thuc te (tinh theo tung ngon ngu) ===")
for sid in IDS:
    hs = {}
    for lang, b in mods.items():
        s = {x["id"]: x for x in b.SH}[sid]
        t = (s["start"] + s["end"]) / 2
        fi = int(t * b.FPS)
        fr = b.bg_frame(s, t, fi)
        hs[tag[lang]] = (hashlib.md5(fr.convert("RGB").tobytes()).hexdigest()[:12], fi % 6)
    print(f"  {sid}: {hs}")

# --- 3) do phuong an: nen 1 lan + chu 3 ngon ngu ---
print()
print("=== 3) Do phuong an ===")
t0 = time.perf_counter()
tot_bg = 0
for sid in IDS:
    b = mods[None]
    s = {x["id"]: x for x in b.SH}[sid]
    t = (s["start"] + s["end"]) / 2
    fi = int(t * b.FPS)
    t1 = time.perf_counter()
    fr = b.bg_frame(s, t, fi)
    tot_bg += time.perf_counter() - t1
print(f"  bg_frame x1: {tot_bg/len(IDS)*1000:.0f} ms/shot")

# van chu 3 ngon ngu len cung 1 nen
t0 = time.perf_counter()
for sid in IDS:
    b = mods[None]
    s = {x["id"]: x for x in b.SH}[sid]
    t = (s["start"] + s["end"]) / 2
    fi = int(t * b.FPS)
    fr = b.bg_frame(s, t, fi)
    for lang, bb in mods.items():
        s2 = {x["id"]: x for x in bb.SH}[sid]
        els = bb.build_elements(s2)
        f2 = fr.copy()
        for e in els:
            e.draw(f2, t)
print(f"  [nen 1 lan] + chu 3 ngon ngu + 3 ban copy: {(time.perf_counter()-t0)/len(IDS)*1000:.0f} ms/shot")

# so sanh voi cach hien tai: 3 x (bg_frame + chu + draw)
t0 = time.perf_counter()
for sid in IDS:
    for lang, bb in mods.items():
        s2 = {x["id"]: x for x in bb.SH}[sid]
        t = (s2["start"] + s2["end"]) / 2
        fi = int(t * bb.FPS)
        fr = bb.bg_frame(s2, t, fi)
        els = bb.build_elements(s2)
        for e in els:
            e.draw(fr, t)
print(f"  [cach hien tai] 3 x (nen + chu + draw): {(time.perf_counter()-t0)/len(IDS)*1000:.0f} ms/shot")
