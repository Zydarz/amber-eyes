# -*- coding: utf-8 -*-
"""Kiem chung phuong an:
  (a) bg_frame DUNG 1 LAN cho 3 ngon ngu (fi chung) -> xac nhan byte-identical
  (b) still hien tai cua VI co bang byte voi cach 'dung nen chung' khong? (regression)
  (c) draw_characters (badge/avatar) co phu thuoc ngon ngu khong?
  (d) PNG save: nen nen ?"""
import os, sys, time, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / ".work"))
os.environ["AE_EP"] = "08"

import importlib

def load(lang):
    for m in list(sys.modules):
        if m in ("build_video3", "edition"):
            del sys.modules[m]
    if lang:
        os.environ["AE_LANG"] = lang
    else:
        os.environ.pop("AE_LANG", None)
    return importlib.import_module("build_video3")

mods = {t: load(t) for t in [None, "en", "ja"]}
tag = {None: "vi", "en": "en", "ja": "ja"}
IDS = ["1-02", "1-11", "2-05", "3-09", "4-14", "5-20", "5-41"]

# ---------- (b) regression: still VI hien tai vs 'dung nen chung' ----------
print("=== (b) REGRESSION: still VI hien tai == dung nen chung (cung fi) ? ===")
for sid in IDS:
    b = mods[None]
    s = {x["id"]: x for x in b.SH}[sid]
    t = (s["start"] + s["end"]) / 2
    fi = int(t * b.FPS)

    fr_old = b.render(fi).convert("RGB")

    # cach moi: dung bg_frame 1 lan (fi chung = fi cua VI) + elements + characters
    fr_new = b.bg_frame(s, t, fi)
    for e in b.build_elements(s):
        e.draw(fr_new, t)
    b.draw_characters(fr_new, t, fi, s)
    fr_new = fr_new.convert("RGB")

    h1 = hashlib.md5(fr_old.tobytes()).hexdigest()[:12]
    h2 = hashlib.md5(fr_new.tobytes()).hexdigest()[:12]
    print(f"  {sid}: hien tai={h1}  moi={h2}  -> {'KHONG DOI' if h1==h2 else 'KHAC'}")

# ---------- (c) draw_characters phu thuoc ngon ngu? ----------
print()
print("=== (c) badge/avatar co phu thuoc ngon ngu khong? ===")
for sid in IDS:
    out = {}
    for lang, b in mods.items():
        s = {x["id"]: x for x in b.SH}[sid]
        t = (s["start"] + s["end"]) / 2
        fi = int(t * b.FPS)
        base = b.bg_frame(s, t, 10000)          # nen chung, fi chung
        for e in b.build_elements(s):
            e.draw(base, t)
        b.draw_characters(base, t, fi, s)       # fi thuc te -> phai dung rieng
        out[tag[lang]] = hashlib.md5(base.convert("RGB").tobytes()).hexdigest()[:12]
    same = len(set(out.values())) == 1
    print(f"  {sid}: {out} -> {'GIONG' if same else 'KHAC (avatar/vi tri badge theo ngon ngu)'}")

# ---------- (d) PNG save: compress_level ----------
print()
print("=== (d) thoi gian + dung luong luu PNG theo compress_level ===")
from PIL import Image
import io
b = mods[None]
s = {x["id"]: x for x in b.SH}["2-05"]
t = (s["start"] + s["end"]) / 2
fr = b.render(int(t * b.FPS)).convert("RGB")
for lv in (6, 3, 1, 0):
    buf = io.BytesIO()
    t0 = time.perf_counter()
    fr.save(buf, format="PNG", compress_level=lv)
    dt = (time.perf_counter() - t0) * 1000
    print(f"  compress_level={lv}: {dt:6.0f} ms   {buf.tell()/1e6:.2f} MB/anh")
buf = io.BytesIO()
t0 = time.perf_counter()
fr.save(buf, format="JPEG", quality=92)
print(f"  JPEG q92:          {(time.perf_counter()-t0)*1000:6.0f} ms   {buf.tell()/1e6:.2f} MB/anh")
