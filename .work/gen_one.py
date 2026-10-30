#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh 1 anh nen theo ten, cho phep chon do phan giai (1K/2K/4K) va so lan thu.

usage: py -3 .work/gen_one.py t3_gavel [1K|2K|4K] [so_lan_thu]

Dung khi gen_images.py that (loi 500 cua connector khi post-processing).
"""
import json
import os
import subprocess
import sys
import time
import urllib.request
from datetime import date
from pathlib import Path

from PIL import Image

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
OUT = ROOT / "assets" / "bg"
RAW = OUT / "_raw"
LOG = WORK / "gen_log"
JOBS = WORK / "bg_jobs_tap03.json"
PROV = Path(os.environ.get("AE_PROV") or (ROOT / "provenance.json"))
TOOL = "connector__matrix__generate_image"

STYLE = ("Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink "
         "linework, deep chiaroscuro lighting, subtle mist and film grain, desaturated muted "
         "palette, ominous quiet tension, highly detailed. ")
NEG = (" Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
       "no watermark, no frame, no letterbox bars, full-bleed image.")


def mcode(args, timeout=600, tries=4):
    for n in range(tries):
        r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=timeout)
        if r.returncode == 0 or "Network request failed" not in (r.stderr + r.stdout) or n == tries - 1:
            return r.returncode, r.stdout, r.stderr
        time.sleep(10 * (n + 1))


def trim_bars(im, thr=12):
    import numpy as np
    a = np.asarray(im.convert("L"), np.float32)
    rows, cols = a.mean(axis=1), a.mean(axis=0)
    t = next(i for i, v in enumerate(rows) if v > thr)
    b = next(i for i, v in enumerate(rows[::-1]) if v > thr)
    l = next(i for i, v in enumerate(cols) if v > thr)
    r = next(i for i, v in enumerate(cols[::-1]) if v > thr)
    if max(t, b, l, r) > 2:
        im = im.crop((l + 2 if l else 0, t + 2 if t else 0,
                      im.width - (r + 2 if r else 0), im.height - (b + 2 if b else 0)))
    return im


def to_169(im, size=(2112, 1188)):
    im = trim_bars(im)
    w, h = im.size
    if abs(w / h - 16 / 9) > 0.01:
        if w / h > 16 / 9:
            nw = int(h * 16 / 9); im = im.crop(((w - nw) // 2, 0, (w - nw) // 2 + nw, h))
        else:
            nh = int(w * 9 / 16); im = im.crop((0, (h - nh) // 2, w, (h - nh) // 2 + nh))
    return im.resize(size, Image.LANCZOS)


def main():
    name = sys.argv[1]
    res = sys.argv[2] if len(sys.argv) > 2 else "2K"
    tries = int(sys.argv[3]) if len(sys.argv) > 3 else 3
    jobs = {j["name"]: j for j in json.loads(JOBS.read_text(encoding="utf-8"))}
    job = jobs[name]
    for d in (OUT, RAW, LOG):
        d.mkdir(parents=True, exist_ok=True)

    for attempt in range(1, tries + 1):
        req = {"prompt": STYLE + job["prompt"] + NEG, "aspect_ratio": "16:9",
               "resolution": res, "output_file": name}
        af = LOG / f"one_{name}_{res}.json"
        af.write_text(json.dumps({"requests": [req]}, ensure_ascii=False), encoding="utf-8")
        code, out, err = mcode(["connector", "call", TOOL, "--args-file", str(af)], 900)
        (LOG / f"res_one_{name}_{res}.json").write_text(out or err, encoding="utf-8")
        if code != 0:
            print(f"  lan {attempt}: connector rc={code}: {err[:200]}")
            time.sleep(20 * attempt)
            continue
        res_j = json.loads(out)
        succ = res_j.get("success_items", [])
        if not succ:
            msg = res_j.get("message", "")[:200]
            print(f"  lan {attempt}: that - {msg}")
            time.sleep(20 * attempt)
            continue
        it = succ[0]
        code2, out2, err2 = mcode(["get_asset_url", it["node_id"]], 120)
        if code2 != 0:
            print(f"  lan {attempt}: get_asset_url that: {err2[:200]}")
            time.sleep(10)
            continue
        url = json.loads(out2).get("download_url") or json.loads(out2).get("url")
        fn = it["file_name"]
        raw = RAW / fn
        urllib.request.urlretrieve(url, raw)
        im = Image.open(raw).convert("RGB")
        to_169(im).save(OUT / f"{name}.png")
        prov = json.loads(PROV.read_text(encoding="utf-8")) if PROV.exists() else []
        prov = [p for p in prov if p.get("file") != f"assets/bg/{name}.png"]
        prov.append({"file": f"assets/bg/{name}.png", "loai": "nen 16:9",
                     "cong_cu": f"{TOOL} (MiniMax qua mcode-tools)", "ngay": str(date.today()),
                     "prompt": STYLE + job["prompt"] + NEG, "seed": None,
                     "nguon_anh_tham_chieu": job.get("ref"), "kich_thuoc_goc": list(im.size),
                     "dieu_khoan": "<điều khoản thương mại của MiniMax — cần kiểm tra trước khi đăng>",
                     "kiem_tra_thuong_mai": "chua"})
        PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"OK {name} @{res} -> {im.size} (lan {attempt})")
        return
    print(f"THAT: {name} sau {tries} lan")
    sys.exit(2)


if __name__ == "__main__":
    main()
