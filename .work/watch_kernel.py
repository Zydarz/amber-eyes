"""Theo doi mot kernel Kaggle: poll trang thai -> tai output khi COMPLETE.

Usage:
  python .work/watch_kernel.py --slug <slug> --out <dir> [--pattern "out_x/.*\\.(wav|json)"] [--timeout-min 180]

Quy tac an toan (tu memory):
  * `kaggle kernels output` LUON phai co --file-pattern (khong tai ca model ~10 GB)
  * `kaggle kernels logs` chi doc duoc khi kernel da COMPLETE/ERROR
"""
import argparse
import json
import pathlib
import re
import subprocess
import sys
import time

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
KAG = pathlib.Path.home() / "AppData" / "Local" / "kaggle-venv" / "Scripts" / "kaggle.exe"

ap = argparse.ArgumentParser()
ap.add_argument("--slug", required=True)
ap.add_argument("--out", required=True)
ap.add_argument("--pattern", default=r".*\.(wav|json)")
ap.add_argument("--timeout-min", type=int, default=180)
ap.add_argument("--poll", type=int, default=60)
a = ap.parse_args()

OUT = pathlib.Path(a.out)
OUT.mkdir(parents=True, exist_ok=True)
LOG = OUT / "_watch.log"


def run(cmd, timeout=1800):
    return subprocess.run(cmd, capture_output=True, text=True,
                          encoding="utf-8", errors="replace", timeout=timeout)


def log(msg):
    line = "[%s] %s" % (time.strftime("%H:%M:%S"), msg)
    print(line, flush=True)
    with LOG.open("a", encoding="utf-8") as f:
        f.write(line + "\n")


log("=== WATCH %s ===" % a.slug)
t0 = time.time()
status = None
while time.time() - t0 < a.timeout_min * 60:
    r = run([str(KAG), "kernels", "status", a.slug], timeout=120)
    m = re.search(r'has status "([^"]+)"', r.stdout or "")
    st = m.group(1).split(".")[-1] if m else "UNKNOWN"
    if st != status:
        log("trang thai: %s" % st)
        status = st
    if st in ("COMPLETE", "ERROR", "CANCELLED"):
        break
    time.sleep(a.poll)

if status == "COMPLETE":
    log("COMPLETE -> tai output")
    r = run([str(KAG), "kernels", "output", a.slug, "-p", str(OUT),
             "--file-pattern", a.pattern, "--force"], timeout=3600)
    log("output rc=%s" % r.returncode)
    if r.returncode != 0:
        log((r.stderr or r.stdout or "")[-800:])
    # CLI chi tai 1 TRANG (Tap 02 EN hoi 4: 100/102 wav, mat ca manifest — 31/10/2026).
    # Tai bu: lay manifest, roi tai dung ten file con thieu theo lo < 1 trang (max 200).
    prefix = a.pattern.split("/")[0] + "/" if "/" in a.pattern else ""
    for _ in range(2):
        if not list(OUT.rglob("higgs_manifest.json")):
            run([str(KAG), "kernels", "output", a.slug, "-p", str(OUT), "--page-size", "200",
                 "--file-pattern", prefix + r".*\.(json|log)", "--force"], timeout=1800)
    for man in OUT.rglob("higgs_manifest.json"):
        want = [x["file"] for x in json.loads(man.read_text(encoding="utf-8-sig")) if x.get("ok")]
        miss = [f for f in want if not (man.parent / f).exists()]
        log("manifest %s: %d file OK, thieu %d" % (man.parent.name, len(want), len(miss)))
        for i in range(0, len(miss), 150):
            pat = prefix + "(" + "|".join(re.escape(f) for f in miss[i:i + 150]) + ")"
            run([str(KAG), "kernels", "output", a.slug, "-p", str(OUT), "--page-size", "200",
                 "--file-pattern", pat, "--force"], timeout=3600)
        miss = [f for f in want if not (man.parent / f).exists()]
        log("sau tai bu: thieu %d %s" % (len(miss), miss[:5]))
    n_wav = len(list(OUT.rglob("*.wav")))
    n_js = len(list(OUT.rglob("*.json")))
    log("tai xong: %d wav, %d json" % (n_wav, n_js))
else:
    log("trang thai cuoi = %s -> lay logs" % status)
    r = run([str(KAG), "kernels", "logs", a.slug], timeout=900)
    txt = (r.stdout or "") + (r.stderr or "")
    (OUT / "_kernel_logs.txt").write_text(txt, encoding="utf-8")
    log("logs -> %s (%d ky tu)" % (OUT / "_kernel_logs.txt", len(txt)))
    print(txt[-6000:])
