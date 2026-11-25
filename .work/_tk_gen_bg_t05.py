# -*- coding: utf-8 -*-
"""Sinh 32 nen DOC 9:16 cho clip TikTok Tap 05 (MiniMax image-generation).

Buoc: upload anh nen 16:9 goc (assets/bg/_raw/t5_*) -> temp_url -> generate_image
(9:16, area 2K, co anh tham chieu) -> tai anh ngay -> giu node_id trong receipt.

Luu y (memory): allowance MiniMax het sau ~13-18 anh => lo 402. Lo 402 thi dung
fallback crop 9:16 tu anh 16:9 goc (0 dong) cho phan con lai.

usage: py -3 .work/_tk_gen_bg_t05.py [batch_size]
"""
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import time
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_src_t05 import PAIRS, PROMPT, MIME, src_path  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = r"D:/TEST/Gax/amber-eyes"
HERE = os.path.join(ROOT, ".work")
OUT = os.path.join(HERE, "tk_img_raw_t05")
MT = shutil.which("mcode-tools") or "mcode-tools"


def sh(args, timeout=900):
    p = subprocess.run(args, shell=True, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def run_json(args, timeout=900):
    rc, out, err = sh(args, timeout)
    txt = (out or "").strip() or (err or "").strip()
    try:
        return rc, json.loads(txt)
    except Exception:  # noqa: BLE001
        i = txt.find("{")
        if i >= 0:
            try:
                return rc, json.loads(txt[i:])
            except Exception:  # noqa: BLE001
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
    af = os.path.join(HERE, "_tk_img_req_t05_%s.json" % tag)
    rf = os.path.join(HERE, "_tk_img_receipt_t05_%s.json" % tag)
    with io.open(af, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"requests": reqs}, f, ensure_ascii=False, indent=1)
    rc, j = run_json([MT, "connector", "call", "connector__matrix__generate_image",
                      "--args-file", af], timeout=1800)
    with io.open(rf, "w", encoding="utf-8", newline="\n") as f:
        json.dump(j, f, ensure_ascii=False, indent=1)
    return rc, j


def get_asset_url(node):
    rc, out, err = sh([MT, "get_asset_url", node], timeout=300)
    txt = (out or "").strip() or (err or "").strip()
    try:
        return json.loads(txt)
    except Exception:  # noqa: BLE001
        i = txt.find("{")
        return json.loads(txt[i:]) if i >= 0 else {}


def download(items):
    ok, fail = 0, []
    for it in items:
        node = it.get("node_id")
        fname = it.get("file_name")
        if not node or not fname:
            continue
        dst = os.path.join(OUT, fname)
        if os.path.exists(dst):
            continue
        try:
            d = get_asset_url(node)
            url = d.get("download_url") or d.get("url")
            if not url:
                raise RuntimeError("khong co download_url")
            with urllib.request.urlopen(url, timeout=300) as r, open(dst, "wb") as f:
                shutil.copyfileobj(r, f)
            print("     tai xong %-40s %7.0f KB" % (fname, os.path.getsize(dst) / 1024))
            ok += 1
        except Exception as e:  # noqa: BLE001
            fail.append((fname, str(e)[:120]))
            print("     FAIL %-36s %s" % (fname, str(e)[:120]))
    return ok, fail


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
        for it in si[:12]:
            out.append("   %s -> %s" % (it.get("file_name"), it.get("node_id")))
    fi = j.get("failed_items")
    if fi is not None:
        out.append("failed_items=%d" % len(fi))
        for it in fi[:12]:
            out.append("   %s" % str(it)[:300])
    if not out:
        out.append(json.dumps(j, ensure_ascii=False)[:900])
    return "\n".join(out)


def main():
    os.makedirs(OUT, exist_ok=True)
    batch = int(sys.argv[1]) if len(sys.argv) > 1 else 6

    todo = [(n, r) for n, r in PAIRS
            if not os.path.exists(os.path.join(OUT, n + ".jpg"))
            and not os.path.exists(os.path.join(OUT, n + ".png"))]
    print("con %d nen can sinh (da co: %d)" % (len(todo), len(PAIRS) - len(todo)))

    total_ok = 0
    blocked = False
    tag = 1
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
            print("  upload ok: %-34s -> %s" % (ref, u[:60]))
        if not reqs:
            continue
        rc, j = generate(reqs, "b%d" % tag)
        print("--- lot %d (n=%d) rc=%d  [%s]" % (tag, len(reqs), rc, time.strftime("%H:%M:%S")))
        print(summarize(j), flush=True)
        txt = json.dumps(j, ensure_ascii=False).lower()
        if "402" in txt or "allowance" in txt or "insufficient" in txt:
            blocked = True
            print("!! CHAN ALLOWANCE (402) - dung, phan con lai dung fallback crop 9:16 tu anh 16:9 goc")
            break
        items = j.get("success_items") or []
        total_ok += len(items)
        download(items)
        tag += 1
        time.sleep(2)

    print("\nTONG THANH CONG AI: %d/%d" % (total_ok, len(PAIRS)))
    have = sum(1 for n, _ in PAIRS
               if os.path.exists(os.path.join(OUT, n + ".jpg"))
               or os.path.exists(os.path.join(OUT, n + ".png")))
    print("co file tho: %d/%d" % (have, len(PAIRS)))
    if blocked:
        print("=> chay tiep: py -3 .work/_tk_fallback_crop_t05.py  (crop 9:16 cho nen con thieu)")


if __name__ == "__main__":
    main()
