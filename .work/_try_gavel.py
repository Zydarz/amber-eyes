#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Lan cuoi cho t3_gavel: kiem tra dich vu con khoe khong, roi thu nhieu bien the prompt
voi nhieu do phan giai. Chi ghi file khi that bai."""
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np
from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
OUT = ROOT / "assets" / "bg"
RAW = OUT / "_raw"
LOG = WORK / "gen_log"
JOBS = WORK / "bg_jobs_tap03.json"
TOOL = "connector__matrix__generate_image"

STYLE = ("Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink "
         "linework, deep chiaroscuro lighting, subtle mist and film grain, desaturated muted "
         "palette, ominous quiet tension, highly detailed. ")
NEG = (" Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
       "no watermark, no frame, no letterbox bars, full-bleed image.")

VARIANTS = [
    ("bench", "2K",
     "An empty 1970s American courtroom at night seen from the gallery, a raised dark wood "
     "judge's bench, a small wooden mallet and round block resting on the bench top, one "
     "cold shaft of light from a high window, nobody present, no text, no emblem."),
    ("bench", "1K",
     "An empty 1970s American courtroom at night seen from the gallery, a raised dark wood "
     "judge's bench, a small wooden mallet and round block resting on the bench top, one "
     "cold shaft of light from a high window, nobody present, no text, no emblem."),
    ("hammer", "2K",
     "Close-up of a small wooden court mallet and a heavy round wooden block lying on a dark "
     "polished surface, cold raking light, deep shadow, still life, nobody present, no text, "
     "no writing."),
    ("hammer", "1K",
     "Close-up of a small wooden court mallet and a heavy round wooden block lying on a dark "
     "polished surface, cold raking light, deep shadow, still life, nobody present, no text, "
     "no writing."),
]


def mcode(args, timeout=420):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=timeout)
    return r.returncode, r.stdout, r.stderr


def to_169(im, size=(2112, 1188)):
    a = np.asarray(im.convert("L"), np.float32)
    rows, cols = a.mean(axis=1), a.mean(axis=0)
    try:
        t = next(i for i, v in enumerate(rows) if v > 12)
        b = next(i for i, v in enumerate(rows[::-1]) if v > 12)
        l = next(i for i, v in enumerate(cols) if v > 12)
        r = next(i for i, v in enumerate(cols[::-1]) if v > 12)
        if max(t, b, l, r) > 2:
            im = im.crop((l + 2 if l else 0, t + 2 if t else 0,
                          im.width - (r + 2 if r else 0), im.height - (b + 2 if b else 0)))
    except StopIteration:
        pass
    w, h = im.size
    if abs(w / h - 16 / 9) > 0.01:
        if w / h > 16 / 9:
            nw = int(h * 16 / 9); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
        else:
            nh = int(w * 9 / 16); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    return im.resize(size, Image.LANCZOS)


def call(prompt, res, tag):
    req = {"prompt": STYLE + prompt + NEG, "aspect_ratio": "16:9",
           "resolution": res, "output_file": "t3_gavel"}
    af = LOG / f"gavel_try_{tag}_{res}.json"
    af.write_text(json.dumps({"requests": [req]}, ensure_ascii=False), encoding="utf-8")
    try:
        code, out, err = mcode(["connector", "call", TOOL, "--args-file", str(af)], 420)
    except subprocess.TimeoutExpired:
        print(f"  [{tag}@{res}] TIMEOUT", flush=True)
        return None
    if code != 0:
        print(f"  [{tag}@{res}] rc={code}: {err[:160]}", flush=True)
        return None
    rj = json.loads(out)
    if not rj.get("success_items"):
        print(f"  [{tag}@{res}] that: {rj.get('message','')[:150]}", flush=True)
        return None
    return rj["success_items"][0]


for tag, res, prompt in VARIANTS:
    print(f"=== {tag} @{res} ===", flush=True)
    it = call(prompt, res, tag)
    if not it:
        time.sleep(8)
        continue
    c2, o2, e2 = mcode(["get_asset_url", it["node_id"]], 120)
    if c2 != 0:
        print(f"  get_asset_url that: {e2[:160]}", flush=True)
        continue
    url = json.loads(o2).get("download_url") or json.loads(o2).get("url")
    raw = RAW / it["file_name"]
    urllib.request.urlretrieve(url, raw)
    im = Image.open(raw).convert("RGB")
    to_169(im).save(OUT / "t3_gavel.png")
    # dong provenance cho anh moi
    jobs = json.loads(JOBS.read_text(encoding="utf-8"))
    for j in jobs:
        if j["name"] == "t3_gavel":
            j["prompt"] = prompt
    JOBS.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
    prov_p = ROOT / "provenance.json"
    prov = json.loads(prov_p.read_text(encoding="utf-8"))
    prov = [p for p in prov if p.get("file") != "assets/bg/t3_gavel.png"]
    from datetime import date
    prov.append({"file": "assets/bg/t3_gavel.png", "loai": "nen 16:9",
                 "cong_cu": f"{TOOL} (MiniMax qua mcode-tools)", "ngay": str(date.today()),
                 "prompt": STYLE + prompt + NEG, "seed": None, "nguon_anh_tham_chieu": None,
                 "kich_thuoc_goc": list(im.size),
                 "dieu_khoan": "<điều khoản thương mại của MiniMax — cần kiểm tra trước khi đăng>",
                 "kiem_tra_thuong_mai": "chưa"})
    prov_p.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"  OK -> assets/bg/t3_gavel.png ({im.size})", flush=True)
    sys.exit(0)

print("\nvan chua sinh duoc t3_gavel", flush=True)
sys.exit(2)
