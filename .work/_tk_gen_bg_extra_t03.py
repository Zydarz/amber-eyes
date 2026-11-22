# -*- coding: utf-8 -*-
"""Sinh PHAN CON THIEU 16 nen doc 9:16 cho Tap 03 (sau khi het allowance lo 402).

Doc danh sach thieu tu .work/_tk_img_missing_t03.json (dong bo voi anh da tai),
upload lai anh 16:9 goc (URL tham chieu het han sau 1 gio) va goi generate_image.
Dung ngay pipeline cu neu allowance da reset; neu van 402 -> dung fallback crop 0 dong.
"""
import io
import json
import os
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _tk_src_t03 import PAIRS, PROMPT, MIME, src_path  # noqa: E402
from _tk_gen_bg_t03 import upload, build, generate, summarize, HERE  # noqa: E402

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

RAWOUT = os.path.join(HERE, "tk_img_raw_t03")
BATCH = 4


def main():
    miss_path = os.path.join(HERE, "_tk_img_missing_t03.json")
    if os.path.exists(miss_path):
        missing = json.loads(io.open(miss_path, encoding="utf-8").read())
    else:
        missing = [n for n, _ in PAIRS]
    todo = [(n, r) for n, r in PAIRS if n in missing]
    if not todo:
        print("khong con nen thieu")
        return
    print("nen thieu can sinh AI: %d" % len(todo))

    tag = 10
    ok = 0
    for i in range(0, len(todo), BATCH):
        chunk = todo[i:i + BATCH]
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
            print("  upload ok: %-26s" % ref)
        if not reqs:
            continue
        rc, j = generate(reqs, "x%d" % tag)
        print("--- batch x%d (n=%d) rc=%d" % (tag, len(reqs), rc))
        print(summarize(j))
        txt = json.dumps(j, ensure_ascii=False).lower()
        if "402" in txt or "allowance" in txt or "insufficient" in txt:
            print("!! van 402 - dung pipeline AI")
            break
        ok += len(j.get("success_items", []) or [])
        tag += 1
        time.sleep(2)
    print("\nAI that sinh them: %d" % ok)


if __name__ == "__main__":
    main()
