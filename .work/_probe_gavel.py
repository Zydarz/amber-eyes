#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Thu t3_gavel voi output_file khac + do phan giai khac, de khoanh vung nguyen nhan fail."""
import json
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

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


def mcode(args, timeout=420):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True,
                       text=True, encoding="utf-8", errors="replace", timeout=timeout)
    return r.returncode, r.stdout, r.stderr


def to_169(im, size=(2112, 1188)):
    import numpy as np
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


from PIL import Image  # noqa: E402

jobs = {j["name"]: j for j in json.loads(JOBS.read_text(encoding="utf-8"))}
job = jobs["t3_gavel"]
prompt = STYLE + job["prompt"] + NEG

VARIANTS = [
    ("tap03gavel", "2K"),   # output_file khac
    ("t3_gavel", "1K"),     # cung ten, do phan giai khac
    ("t3_gavel", "4K"),     # cung ten, do phan giai cao hon
]

for outfile, res in VARIANTS:
    print(f"\n=== output_file={outfile}  resolution={res} ===", flush=True)
    req = {"prompt": prompt, "aspect_ratio": "16:9", "resolution": res, "output_file": outfile}
    af = LOG / f"probe_{outfile}_{res}.json"
    af.write_text(json.dumps({"requests": [req]}, ensure_ascii=False), encoding="utf-8")
    try:
        code, out, err = mcode(["connector", "call", TOOL, "--args-file", str(af)], 420)
    except subprocess.TimeoutExpired:
        print("  TIMEOUT (connector treo)")
        continue
    if code != 0:
        print(f"  rc={code}: {err[:200]}")
        continue
    rj = json.loads(out)
    if not rj.get("success_items"):
        print(f"  that: {rj.get('message','')[:200]}")
        continue
    it = rj["success_items"][0]
    c2, o2, e2 = mcode(["get_asset_url", it["node_id"]], 120)
    if c2 != 0:
        print(f"  get_asset_url that: {e2[:200]}")
        continue
    url = json.loads(o2).get("download_url") or json.loads(o2).get("url")
    raw = RAW / it["file_name"]
    urllib.request.urlretrieve(url, raw)
    im = Image.open(raw).convert("RGB")
    to_169(im).save(OUT / "t3_gavel.png")
    print(f"  OK -> assets/bg/t3_gavel.png  (goc {im.size})")
    sys.exit(0)

print("\nkhong variant nao thanh cong")
sys.exit(2)
