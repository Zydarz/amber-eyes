# -*- coding: utf-8 -*-
"""END-TO-END: so sanh 2 cach render 223 anh tinh x 3 ngon ngu (ke ca ghi PNG).
CACH A (hien tai): moi ngon ngu render lai toan bo (nen + chu + nhan vat) roi ghi PNG.
CACH B (de xuat)  : nen render 1 lan (canonical), 3 ngon ngu chi ve them chu roi ghi PNG.
Kiem byte: 6 shot mau kiem tra anh VI co y het voi cach A khong."""
import os, sys, time, hashlib, importlib
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))

N = 25          # so shot mau
SAVE = True     # ghi PNG that vao dia (do nhat)

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

LANGS = [None, "en", "ja"]
mods = {l: load(l) for l in LANGS}
tag = {None: "vi", "en": "en", "ja": "ja"}

vi = mods[None]
SHVI = vi.SH
ids = [s["id"] for s in SHVI[:N]]
LAST_ID = SHVI[-1]["id"]

out = {}
for l, b in mods.items():
    d = ROOT / ".work" / f"_bench_{tag[l]}"
    d.mkdir(exist_ok=True)

# ---------------- CACH A ----------------
t0 = time.perf_counter()
for sid in ids:
    for l, b in mods.items():
        s = {x["id"]: x for x in b.SH}[sid]
        t = (s["start"] + s["end"]) / 2
        fr = b.render(int(t * b.FPS)).convert("RGB")
        if SAVE:
            fr.save(d / f"shot_{sid}.png")
        else:
            hashlib.md5(fr.tobytes()).hexdigest()
dt_a = time.perf_counter() - t0
print(f"CACH A (hien tai) 3 ngon ngu x {N} shot: {dt_a:.1f} s   -> uoc 223 shot: {dt_a/N*223/60:.1f} phut")

# ---------------- CACH B ----------------
t0 = time.perf_counter()
for sid in ids:
    # nen canonical: lay tu VI, dung t = fi/FPS dung convention cua render()
    sv = {x["id"]: x for x in SHVI}[sid]
    t_c = (sv["start"] + sv["end"]) / 2
    fi_c = int(t_c * vi.FPS)
    t_c = fi_c / vi.FPS

    special = (sid == LAST_ID)          # shot cuoi co fade-to-black
    if special:
        for l, b in mods.items():
            s = {x["id"]: x for x in b.SH}[sid]
            fr = b.render(int(((s["start"] + s["end"]) / 2) * b.FPS)).convert("RGB")
            if SAVE:
                fr.save(d / f"shot_{sid}.png")
        continue

    base = vi.bg_frame(sv, t_c, fi_c)
    for l, b in mods.items():
        s = {x["id"]: x for x in b.SH}[sid]
        fr = base.copy()
        for e in b.build_elements(s):
            e.draw(fr, t_c)
        b.draw_characters(fr, t_c, fi_c, s)
        fr = fr.convert("RGB")
        if SAVE:
            fr.save(d / f"shot_{sid}.png")
        else:
            hashlib.md5(fr.tobytes()).hexdigest()
dt_b = time.perf_counter() - t0
print(f"CACH B (nen 1 lan) 3 ngon ngu x {N} shot: {dt_b:.1f} s   -> uoc 223 shot: {dt_b/N*223/60:.1f} phut")
print(f"   => tiet kiem {dt_a-dt_b:.1f} s / {N} shot  ({100*(1-dt_b/dt_a):.0f}%)")
print(f"   => uoc 1 TAP: {dt_a/N*223/60:.1f} phut -> {dt_b/N*223/60:.1f} phut")

# ---------------- kiem byte ----------------
print()
print("=== Kiem byte VI (A vs B) ===")
bad = 0
for sid in ids:
    s = {x["id"]: x for x in SHVI}[sid]
    t = (s["start"] + s["end"]) / 2
    old = vi.render(int(t * vi.FPS)).convert("RGB")
    t_c = int(t * vi.FPS) / vi.FPS
    fi_c = int(t * vi.FPS)
    new = vi.bg_frame(s, t_c, fi_c)
    for e in vi.build_elements(s):
        e.draw(new, t_c)
    vi.draw_characters(new, t_c, fi_c, s)
    new = new.convert("RGB")
    d = np.abs(np.asarray(old, np.int16) - np.asarray(new, np.int16)).max(axis=2)
    n = int((d > 0).sum())
    if n:
        bad += 1
        print(f"  {sid}: KHAC {n} px maxdelta={d.max()}")
print(f"  {len(ids)-bad}/{len(ids)} shot byte-identical" + ("" if not bad else "  <-- canh bao"))

for l in LANGS:
    d = ROOT / ".work" / f"_bench_{tag[l]}"
    sz = sum(p.stat().st_size for p in d.glob("*.png"))
    print(f"  bench_{tag[l]}: {len(list(d.glob('*.png')))} png, {sz/1e6:.1f} MB")
