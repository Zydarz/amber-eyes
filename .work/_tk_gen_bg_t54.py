# -*- coding: utf-8 -*-
"""Sinh ảnh nền DỌC 9:16 cho TikTok Tập 54 bằng MiniMax image-generation.

Engine chính cho nền DỌC của kênh (cùng engine đã dùng cho tk01..tk04) — chạy
song song với Kaggle FLUX (dự phòng, 0 đồng) để không phải chờ slot GPU.

Prompt: ĐÚNG 4 tầng của chuẩn (STYLE_PREFIX + bối cảnh + mood + NEGATIVE) và
GIỐNG HỆT prompt Kaggle (import từ deploy_tk54) ⇒ 2 engine cho ra cùng ngôn ngữ cảnh.

LƯU Ý L4: allowance MiniMax là quota gói; KHÔNG bật credit auto-consumption.
Lỗi 402 ⇒ dừng ngay, phần còn lại để Kaggle FLUX.

usage: py -3 .work/_tk_gen_bg_t54.py [batch_size]
"""
import io
import json
import os
import pathlib
import shutil
import subprocess
import sys
import time

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(HERE / "kaggle_flux"))
from deploy_tk54 import STYLE_PREFIX, MOOD_ATMOSPHERE, COMPOSITION, NEGATIVE_SUFFIX  # noqa: E402
from _tk_data_tap54 import BGS, ORDER  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = HERE.parent
OUT = HERE / "tk_img_raw_t54"
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


def build_req(name):
    core = BGS[name][1]
    prompt = "%s%s, %s%s%s" % (STYLE_PREFIX, core, COMPOSITION, MOOD_ATMOSPHERE, NEGATIVE_SUFFIX)
    return {
        "prompt": prompt,
        "aspect_ratio": "9:16",
        "area": "2K",
        "n": 1,
        "output_format": "jpeg",
        "output_file": name,
    }


def generate(reqs, tag):
    af = HERE / ("_tk_img_req_t54_%s.json" % tag)
    rf = HERE / ("_tk_img_receipt_t54_%s.json" % tag)
    with io.open(af, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"requests": reqs}, f, ensure_ascii=False, indent=1)
    rc, j = run_json([MT, "connector", "call", "connector__matrix__generate_image",
                      "--args-file", str(af)], timeout=1800)
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
    OUT.mkdir(parents=True, exist_ok=True)
    batch = int(sys.argv[1]) if len(sys.argv) > 1 else 6

    # ua nhung nen da co file (resume)
    todo = []
    for name in ORDER:
        if (OUT / (name + ".jpg")).exists() or (OUT / (name + ".png")).exists():
            print("  skip (da co): %s" % name)
            continue
        todo.append(name)
    print("con %d nen can sinh" % len(todo))

    total_ok = 0
    blocked = False
    tag = 1
    for i in range(0, len(todo), batch):
        chunk = todo[i:i + batch]
        reqs = [build_req(n) for n in chunk]
        rc, j = generate(reqs, "b%d" % tag)
        print("--- lot %d (n=%d) rc=%d  [%s]" % (tag, len(reqs), rc, time.strftime("%H:%M:%S")))
        print(summarize(j), flush=True)
        txt = json.dumps(j, ensure_ascii=False).lower()
        if "402" in txt or "allowance" in txt or "insufficient balance" in txt:
            blocked = True
            print("!! CHAN ALLOWANCE (402) - dung, phan con lai de Kaggle FLUX")
            break
        total_ok += len(j.get("success_items", []) or [])
        tag += 1
        time.sleep(3)

    print("\nTONG THANH CONG: %d/%d" % (total_ok, len(todo)))
    if blocked:
        print("=> tai anh: py -3 .work/_tk_download_imgs_t54.py")


if __name__ == "__main__":
    main()
