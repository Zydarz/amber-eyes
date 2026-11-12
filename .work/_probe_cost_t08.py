# -*- coding: utf-8 -*-
"""Do chi phi render 1 anh tinh: tach bg_frame (khong phu thuoc ngon ngu) vs elements+draw (phu thuoc ngon ngu).
Do them bang byte de xac nhan bg_frame co giong het giua 3 ngon ngu hay khong."""
import os, sys, time, hashlib, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))

import importlib

def load(lang):
    for m in list(sys.modules):
        if m in ("build_video3", "edition") or m.startswith("build_video3"):
            del sys.modules[m]
    os.environ["AE_EP"] = "08"
    if lang:
        os.environ["AE_LANG"] = lang
    else:
        os.environ.pop("AE_LANG", None)
    b = importlib.import_module("build_video3")
    return b

IDS = ["1-02", "1-11", "2-05", "3-09", "4-14", "5-20"]

res = {}
for lang in [None, "en", "ja"]:
    b = load(lang)
    tag = lang or "vi"
    by_id = {s["id"]: s for s in b.SH}
    rows = []
    for sid in IDS:
        s = by_id.get(sid)
        if not s:
            continue
        t = (s["start"] + s["end"]) / 2
        fi = int(t * b.FPS)

        # --- thoi gian bg_frame (nen + camera + grain/vignette) ---
        t0 = time.perf_counter()
        for _ in range(3):
            fr_bg = b.bg_frame(s, t, fi)
        dt_bg = (time.perf_counter() - t0) / 3

        # --- thoi gian build_elements + draw (text) ---
        t0 = time.perf_counter()
        els = b.build_elements(s)
        dt_el = time.perf_counter() - t0

        fr = fr_bg.copy()
        t0 = time.perf_counter()
        for e in els:
            e.draw(fr, t)
        dt_draw = time.perf_counter() - t0

        # --- checksum nen frame (khong text) ---
        h_bg = hashlib.md5(fr_bg.convert("RGB").tobytes()).hexdigest()[:12]

        rows.append(dict(sid=sid, t=round(t, 2), fi=fi,
                         bg_ms=round(dt_bg * 1000, 1),
                         el_ms=round(dt_el * 1000, 1),
                         draw_ms=round(dt_draw * 1000, 1),
                         md5_bg=h_bg))
    res[tag] = rows
    print(f"[{tag}]")
    for r in rows:
        print("   ", r)

print()
for sid in IDS:
    hs = {k: next((r["md5_bg"] for r in v if r["sid"] == sid), None) for k, v in res.items()}
    same = len(set(hs.values())) == 1
    print(f"{sid}: md5_bg 3 ngon ngu = {hs}  -> {'GIONG HET' if same else 'KHAC NHAU'}")

print()
print("Tong thoi gian uoc tinh cho 223 shot (x1 lan render stills):")
for k, v in res.items():
    tot = sum(r["bg_ms"] + r["el_ms"] + r["draw_ms"] for r in v) / len(v)
    print(f"  {k}: {tot:.0f} ms/shot  ->  {tot*223/1000:.0f} s/tập")
