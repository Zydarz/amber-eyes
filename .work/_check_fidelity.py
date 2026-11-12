# -*- coding: utf-8 -*-
"""Kiem do chinh xac cua CACH B cho EN/JA: anh B co khac anh that cua ngon ngu do khong?
Va kiem cac truong hop bien (bg2, shot cuoi fade, camera)."""
import os, sys, importlib, json
from pathlib import Path
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))

def load(lang, ep):
    for m in list(sys.modules):
        if m in ("build_video3", "edition"):
            del sys.modules[m]
    os.environ["AE_EP"] = ep
    if lang:
        os.environ["AE_LANG"] = lang
    else:
        os.environ.pop("AE_LANG", None)
    return importlib.import_module("build_video3")

# ---- 1) dem bg2 theo tap ----
print("=== Shot co bg2 (nen thu 2) theo tap ===")
for ep in ["07", "08"]:
    b = load(None, ep)
    n2 = [s["id"] for s in b.SH if s.get("bg2")]
    tr = {}
    for s in b.SH:
        tr[s.get("transition", "none")] = tr.get(s.get("transition", "none"), 0) + 1
    print(f"  tap {ep}: {len(b.SH)} shot | bg2: {len(n2)} {n2[:5]} | transition: {tr}")

# ---- 2) EN/JA: anh cach B vs anh that cua ngon ngu do ----
print()
print("=== EN/JA: cach B (nen dung chung cua VI) vs cach A (that) ===")
mods = {l: load(l, "08") for l in [None, "en", "ja"]}
tag = {None: "vi", "en": "en", "ja": "ja"}
vi = mods[None]
SHVI = vi.SH
LAST = SHVI[-1]["id"]

for sid in ["1-11", "3-09", "2-05", "4-14"]:
    sv = {x["id"]: x for x in SHVI}[sid]
    fi_c = int(((sv["start"] + sv["end"]) / 2) * vi.FPS)
    t_c = fi_c / vi.FPS
    base = vi.bg_frame(sv, t_c, fi_c)

    for l, b in mods.items():
        s = {x["id"]: x for x in b.SH}[sid]
        # A: that cua ngon ngu nay
        ta = (s["start"] + s["end"]) / 2
        old = b.render(int(ta * b.FPS)).convert("RGB")

        # B: nen dung chung + chu cua ngon ngu nay
        new = base.copy()
        for e in b.build_elements(s):
            e.draw(new, t_c)
        b.draw_characters(new, t_c, fi_c, s)
        new = new.convert("RGB")

        d = np.abs(np.asarray(old, np.int16) - np.asarray(new, np.int16)).max(axis=2)
        n = int((d > 0).sum())
        pct = 100 * n / (1920 * 1080)
        mx = int(d.max())
        verdict = "IDENTICAL" if n == 0 else ("vai thuoc 1-2px (grain) - vo hinh" if mx <= 12 else "CANH BAO")
        print(f"  {sid} [{tag[l]}]: khac {n} px ({pct:.2f}%) maxdelta={mx}  -> {verdict}")

# ---- 3) shot cuoi: fade-to-black ----
print()
print("=== Shot cuoi (fade) ===")
s = SHVI[-1]
print(f"  {s['id']}: {s['start']:.1f}..{s['end']:.1f} (do dai {s['end']-s['start']:.1f}s)")
print(f"  render() fade tu start+4.0 trong 3.0s -> giua shot da mo 50% den")
print(f"  => can render rieng (khong dung nen chung) cho shot nay")
