# -*- coding: utf-8 -*-
"""Sinh 23 nen DOC 9:16 cho clip TikTok Tap 04 (MiniMax image-generation).

Buoc: upload anh nen 16:9 goc (assets/bg/_raw/t4_*) -> temp_url -> generate_image
(9:16, area 2K) -> giu node_id trong receipt -> _tk_download_imgs_t04.py tai anh.

LUU Y (T20): mcode-tools la wrapper .cmd => phai goi qua shell=True.
LUU Y (memory): allowance MiniMax het sau ~13-18 anh => lo 402. Lo 402 thi dung
fallback crop 0 dong cho phan con lai (khong dung pipeline).

usage:  py -3 .work/_tk_gen_bg_t04.py run [batch_size] [start_index]
"""
import io
import json
import os
import shutil
import subprocess
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_src_t04 import PAIRS, PROMPT, MIME, src_path  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:/TEST/Gax/amber-eyes"
HERE = os.path.join(ROOT, ".work")
OUT = os.path.join(HERE, "tk_img_raw_t04")
MT = shutil.which("mcode-tools")


def sh(args, timeout=900):
    p = subprocess.run(args, shell=True, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def run_json(args, timeout=900):
    rc, out, err = sh(args, timeout)
    txt = out.strip() or err.strip()
    try:
        return rc, json.loads(txt)
    except Exception:
        i = txt.find("{")
        if i >= 0:
            try:
                return rc, json.loads(txt[i:])
            except Exception:
                pass
        return rc, {"_raw": txt[:2000]}


def upload(path):
    rc, j = run_json([MT, "upload_temp_url", path], timeout=600)
    if rc != 0 or not isinstance(j, dict):
        return None
    return j.get("temp_url") or j.get("url")


def build(name, ref, url):
    mime = MIME[os.path.splitext(ref)[1].lower().lstrip(".")]
    return {
        "prompt": PROMPT,
        "reference_images": [{"url": url, "mime_type": mime}],
        "aspect_ratio": "9:16",
        "area": "2K",
        "n": 1,
        "output_format": "jpeg",
        "output_file": name,
    }


def generate(reqs, tag):
    af = os.path.join(HERE, "_tk_img_req_t04_%s.json" % tag)
    rf = os.path.join(HERE, "_tk_img_receipt_t04_%s.json" % tag)
    with io.open(af, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"requests": reqs}, f, ensure_ascii=False, indent=1)
    rc, j = run_json([MT, "connector", "call", "connector__matrix__generate_image",
                      "--args-file", af], timeout=1200)
    with io.open(rf, "w", encoding="utf-8", newline="\n") as f:
        json.dump(j, f, ensure_ascii=False, indent=1)
    return rc, j


def summarize(j):
    if not isinstance(j, dict):
        return str(j)[:400]
    out = []
    for k in ("code", "message", "status", "error"):
        if k in j:
            out.append("%s=%s" % (k, str(j[k])[:300]))
    si = j.get("success_items")
    if si is not None:
        out.append("success_items=%d" % len(si))
        for it in si[:10]:
            out.append("   %s -> %s" % (it.get("file_name"), it.get("node_id")))
    fi = j.get("failed_items")
    if fi is not None:
        out.append("failed_items=%d" % len(fi))
        for it in fi[:10]:
            out.append("   %s" % str(it)[:300])
    if not out:
        out.append(json.dumps(j, ensure_ascii=False)[:900])
    return "\n".join(out)


def main():
    os.makedirs(OUT, exist_ok=True)
    todo = list(PAIRS)
    if len(sys.argv) > 3:
        start = int(sys.argv[3])
        todo = todo[start:]
    batch = int(sys.argv[2]) if len(sys.argv) > 2 else 6
    tag = 1
    total_ok = 0
    blocked = False
    for i in range(0, len(todo), batch):
        chunk = todo[i:i + batch]
        reqs = []
        for name, ref in chunk:
            p = src_path(ref)
            if not os.path.exists(p):
                print("  THIEU NGUON", ref)
                continue
            u = upload(p)
            if not u:
                print("  UPLOAD FAIL", ref)
                continue
            reqs.append(build(name, ref, u))
            print("  upload ok: %-26s -> %s" % (ref, u[:70]))
        if not reqs:
            continue
        rc, j = generate(reqs, "b%d" % tag)
        print("--- batch %d (n=%d) rc=%d" % (tag, len(reqs), rc))
        print(summarize(j))
        txt = json.dumps(j, ensure_ascii=False).lower()
        if "402" in txt or "allowance" in txt or "insufficient" in txt:
            blocked = True
            print("!! CHAN CREDIT/ALLOWANCE - dung pipeline, phan con lai se dung fallback crop")
            break
        total_ok += len(j.get("success_items", []) or [])
        tag += 1
        time.sleep(2)

    print("\nTONG thanh cong trong pipeline AI: %d/%d" % (total_ok, len(todo)))
    if blocked:
        print("=> chay tiep: py -3 .work/_tk_download_imgs_t04.py")
        print("   roi:      py -3 .work/_tk_postprocess_t04.py")
        print("   roi:      py -3 .work/_tk_fallback_crop_t04.py  (nen con thieu)")


if __name__ == "__main__":
    main()
