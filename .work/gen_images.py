#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate 16:9 backgrounds with connector__matrix__generate_image.

usage: py -3 .work/gen_images.py <jobs.json> [--only name1,name2]
jobs.json: [{"name": "house_night", "prompt": "...", "ref": "assets/bg/x.png"?}]

For each job: call the connector (batches of 4), resolve node_id -> URL with
`mcode-tools get_asset_url`, download, save assets/bg/<name>.png at 2112x1188
and append a provenance record (tool, prompt, date).
"""
import json
import os
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

os.environ["PATH"] = r"C:\Users\ADMIN\.minimax\bin;" + os.environ.get("PATH", "")

from PIL import Image

ROOT = Path(r"D:\TEST\Gax\Audi")
OUT = ROOT / "assets" / "bg"
RAW = ROOT / "assets" / "bg" / "_raw"
LOG = ROOT / ".work" / "gen_log"
PROV = Path(os.environ.get("AE_PROV") or (ROOT / "provenance.json"))
TOOL = "connector__matrix__generate_image"

STYLE = ("Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink "
         "linework, deep chiaroscuro lighting, subtle mist and film grain, desaturated muted "
         "palette, ominous quiet tension, highly detailed. ")
NEG = (" Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
       "no watermark, no frame, no letterbox bars, full-bleed image.")


def mcode(args, timeout=600, tries=4):
    import time
    for n in range(tries):
        r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True,
                           text=True, encoding="utf-8", errors="replace", timeout=timeout)
        if r.returncode == 0 or "Network request failed" not in (r.stderr + r.stdout) or n == tries - 1:
            return r.returncode, r.stdout, r.stderr
        time.sleep(10 * (n + 1))


def upload(path):
    code, out, err = mcode(["upload-temp-url", str(path)], 300)
    if code != 0:
        raise RuntimeError(f"upload failed: {err[:300]}")
    j = json.loads(out)
    return j.get("url") or j.get("temp_url") or j.get("download_url")


def asset_url(node_id):
    code, out, err = mcode(["get_asset_url", node_id], 120)
    if code != 0:
        raise RuntimeError(f"get_asset_url failed: {err[:300]}")
    j = json.loads(out)
    return j.get("download_url") or j.get("url")


def trim_bars(im, thr=12):
    """Remove letterbox bars (near-black rows/cols at the edges)."""
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
    jobs = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if "--only" in sys.argv:
        keep = set(sys.argv[sys.argv.index("--only") + 1].split(","))
        jobs = [j for j in jobs if j["name"] in keep]
    if "--force" not in sys.argv:
        jobs = [j for j in jobs if not (OUT / f"{j['name']}.png").exists()]
    print(f"{len(jobs)} ảnh cần tạo", flush=True)
    for d in (OUT, RAW, LOG):
        d.mkdir(parents=True, exist_ok=True)
    prov = json.loads(PROV.read_text(encoding="utf-8")) if PROV.exists() else []
    failed = []
    for b in range(0, len(jobs), 4):
        batch = jobs[b:b + 4]
        reqs = []
        for j in batch:
            rq = {"prompt": STYLE + j["prompt"] + NEG, "aspect_ratio": "16:9",
                  "resolution": "2K", "output_file": j["name"]}
            if j.get("ref"):
                rq["input_urls"] = [upload(ROOT / j["ref"])]
            reqs.append(rq)
        args_file = LOG / f"req_{batch[0]['name']}.json"
        args_file.write_text(json.dumps({"requests": reqs}, ensure_ascii=False), encoding="utf-8")
        code, out, err = mcode(["connector", "call", TOOL, "--args-file", str(args_file)], 900)
        (LOG / f"res_{batch[0]['name']}.json").write_text(out or err, encoding="utf-8")
        if code != 0:
            print(f"!! batch {batch[0]['name']} failed: {err[:400]}")
            failed += [j["name"] for j in batch]
            continue
        res = json.loads(out)
        ok = {it.get("index", i): it for i, it in enumerate(res.get("success_items", []))}
        for f in res.get("failed_items", []):
            print(f"!! {batch[f['index']]['name']}: {f.get('error_msg')}")
            failed.append(batch[f["index"]]["name"])
        succ = res.get("success_items", [])
        for it in succ:
            fn = it["file_name"]
            name = next((j["name"] for j in batch if fn.startswith(j["name"])), None)
            if not name:
                print(f"!! cannot match {fn}")
                continue
            url = asset_url(it["node_id"])
            raw = RAW / fn
            urllib.request.urlretrieve(url, raw)
            im = Image.open(raw).convert("RGB")
            to_169(im).save(OUT / f"{name}.png")
            job = next(j for j in batch if j["name"] == name)
            prov = [p for p in prov if p["file"] != f"assets/bg/{name}.png"]
            prov.append({"file": f"assets/bg/{name}.png", "loai": "nền 16:9",
                         "cong_cu": f"{TOOL} (MiniMax qua mcode-tools)", "ngay": str(date.today()),
                         "prompt": STYLE + job["prompt"] + NEG, "seed": None,
                         "nguon_anh_tham_chieu": job.get("ref"), "kich_thuoc_goc": list(im.size),
                         "dieu_khoan": "<điều khoản thương mại của MiniMax — cần kiểm tra trước khi đăng>",
                         "kiem_tra_thuong_mai": "chưa"})
            PROV.write_text(json.dumps(prov, ensure_ascii=False, indent=1), encoding="utf-8")
            print(f"ok {name} {im.size}", flush=True)
    if failed:
        print("FAILED:", ",".join(failed))
        sys.exit(2)


if __name__ == "__main__":
    main()
