#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chạy dịch 29 tập và TỰ ĐỘNG retry các tập còn mục hỏng.

    py -3 .work/_ja_run_retry.py [--par=5] [--workers=8] [--rounds=4] [eps...]

Mỗi vòng: chạy các tập còn thiếu mục (cache cho phép chỉ dịch lại phần thiếu),
đọc .work/ja_report/tapXX.json, lặp lại cho tới khi mọi tập sạch.
"""
import json
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

WORK = Path(__file__).parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
REPORT = WORK / "ja_report"
LOG = WORK / "ja_logs"


def missing_of(ep):
    p = REPORT / f"tap{ep}.json"
    if not p.exists():
        return ["<chưa có báo cáo>"]
    try:
        return json.loads(p.read_text(encoding="utf-8")).get("missing", [])
    except Exception:
        return ["<lỗi đọc báo cáo>"]


def run(ep, par, workers, bchars, bitems):
    log = LOG / f"tap{ep}.log"
    LOG.mkdir(exist_ok=True)
    t0 = time.time()
    with open(log, "a", encoding="utf-8") as fh:
        fh.write(f"\n===== vòng chạy {time.strftime('%H:%M:%S')} =====\n")
        fh.flush()
        r = subprocess.run([sys.executable, str(WORK / "make_ja_scripts.py"), "--ep", ep,
                            "--workers", str(workers),
                            "--batch-chars", str(bchars),
                            "--batch-items", str(bitems)],
                           stdout=fh, stderr=subprocess.STDOUT, cwd=str(WORK.parent))
    return ep, r.returncode, (time.time() - t0) / 60


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    par, workers, bchars, bitems, rounds = 5, 8, 2600, 14, 4
    for a in sys.argv[1:]:
        if a.startswith("--par="):
            par = int(a.split("=")[1])
        elif a.startswith("--workers="):
            workers = int(a.split("=")[1])
        elif a.startswith("--batch-chars="):
            bchars = int(a.split("=")[1])
        elif a.startswith("--batch-items="):
            bitems = int(a.split("=")[1])
        elif a.startswith("--rounds="):
            rounds = int(a.split("=")[1])
    eps = args or [f"{i:02d}" for i in range(1, 30)]

    for rd in range(1, rounds + 1):
        todo = [e for e in eps if missing_of(e)]
        if not todo:
            print(f"vòng {rd}: tất cả sạch.", flush=True)
            break
        print(f"\n=== vòng {rd}: chạy {len(todo)} tập còn thiếu "
              f"({', '.join(todo)}) ===", flush=True)
        t0 = time.time()
        with ThreadPoolExecutor(max_workers=par) as ex:
            for ep, rc, mins in ex.map(lambda e: run(e, par, workers, bchars, bitems), todo):
                left = missing_of(ep)
                print(f"  Tap{ep}: rc={rc} · {mins:.1f} phút · còn thiếu {len(left)}"
                      + (f" ({', '.join(left[:5])})" if left else ""), flush=True)
        print(f"  vòng {rd} xong sau {(time.time()-t0)/60:.1f} phút", flush=True)

    bad = {e: missing_of(e) for e in eps if missing_of(e)}
    print("\n=== KẾT ===")
    if bad:
        for e, m in bad.items():
            print(f"  Tap{e}: {len(m)} mục thiếu -> {m[:8]}")
    else:
        print("  29/29 tập không còn mục thiếu.")


if __name__ == "__main__":
    main()
