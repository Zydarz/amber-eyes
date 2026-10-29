#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chạy dịch nhiều tập song song: py -3 .work/run_all_ja.py [ep...] [--par N] [--workers W]"""
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

WORK = Path(__file__).parent
sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    par, workers, bchars, bitems = 5, 8, 2600, 14
    for a in sys.argv[1:]:
        if a.startswith("--par="):
            par = int(a.split("=")[1])
        if a.startswith("--workers="):
            workers = int(a.split("=")[1])
        if a.startswith("--batch-chars="):
            bchars = int(a.split("=")[1])
        if a.startswith("--batch-items="):
            bitems = int(a.split("=")[1])
    eps = args or [f"{i:02d}" for i in range(1, 30)]
    LOG = WORK / "ja_logs"
    LOG.mkdir(exist_ok=True)

    def run(ep):
        t0 = time.time()
        log = LOG / f"tap{ep}.log"
        with open(log, "w", encoding="utf-8") as fh:
            r = subprocess.run([sys.executable, str(WORK / "make_ja_scripts.py"), "--ep", ep,
                                "--workers", str(workers),
                                "--batch-chars", str(bchars),
                                "--batch-items", str(bitems)],
                               stdout=fh, stderr=subprocess.STDOUT, cwd=str(WORK.parent))
        dt = time.time() - t0
        print(f"Tap{ep}: rc={r.returncode} · {dt/60:.1f} phút · log={log.name}", flush=True)
        return ep, r.returncode

    t0 = time.time()
    with ThreadPoolExecutor(max_workers=par) as ex:
        list(ex.map(run, eps))
    print(f"XONG {len(eps)} tập trong {(time.time()-t0)/60:.1f} phút", flush=True)


if __name__ == "__main__":
    main()
