# -*- coding: utf-8 -*-
"""Pipeline tự động cho 43 ảnh nền dọc TikTok Tập 54 (Kaggle FLUX).

Bước:
  1. Chờ & đẩy 2 kernel (k1/k2) — tự thử lại khi Kaggle báo
     "Maximum batch GPU session count of 2 reached" (đang có phiên GPU khác).
  2. Theo dõi trạng thái tới khi cả 2 COMPLETE (in tiến độ mỗi 2 phút).
  3. Tải output, giải nén PNG vào .work/tk_img_raw_t54/.
  4. Chạy hậu kỳ tại máy (LANCZOS 1080x1920 + tối vùng chữ) -> assets/bg/tk54_*.png
  5. Ghi provenance.json.

Chạy nền:  py -3 .work/_tk54_pipeline.py
"""
import json
import os
import pathlib
import subprocess
import sys
import time
import zipfile
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
WORK = ROOT / ".work"
KAGGLE_DIR = WORK / "kaggle_flux"
RAW = WORK / "tk_img_raw_t54"
BG = ROOT / "assets" / "bg"

K1 = "chiduong2026/amber-eyes-flux2-tk54-k1"
K2 = "chiduong2026/amber-eyes-flux2-tk54-k2"
DIR1 = KAGGLE_DIR / "tk54k1"
DIR2 = KAGGLE_DIR / "tk54k2"
OUT1 = KAGGLE_DIR / "out_tk54_k1"
OUT2 = KAGGLE_DIR / "out_tk54_k2"

PUSH_WAIT_S = 120          # giây giữa 2 lần thử push
WATCH_EVERY_S = 120       # giây giữa 2 lần hỏi trạng thái
MAX_WAIT_PUSH_S = 5 * 3600


def log(msg):
    print("[%s] %s" % (datetime.now().strftime("%H:%M:%S"), msg), flush=True)


def kaggle(*args):
    return subprocess.run([sys.executable, "-m", "kaggle"] + list(args),
                          capture_output=True, text=True)


def status(ref):
    r = kaggle("kernels", "status", ref)
    s = r.stdout.strip()
    if "COMPLETE" in s:
        return "COMPLETE"
    if "RUNNING" in s:
        return "RUNNING"
    if "QUEUED" in s:
        return "QUEUED"
    if "ERROR" in s:
        return "ERROR"
    return "UNKNOWN:" + s[:120]


def push(dirpath, tag):
    r = kaggle("kernels", "push", "-p", str(dirpath))
    txt = (r.stdout or "") + (r.stderr or "")
    if "Maximum batch GPU session count" in txt:
        return False, "het slot GPU"
    if r.returncode != 0:
        return False, txt.strip()[:300]
    return True, txt.strip()[:300]


def download_and_extract(ref, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    log("tai output %s ..." % ref)
    kaggle("kernels", "output", ref, "-p", str(out_dir))
    n = 0
    for z in sorted(out_dir.glob("*.zip")):
        try:
            with zipfile.ZipFile(z, "r") as zf:
                for item in zf.namelist():
                    if item.endswith(".png"):
                        target = RAW / pathlib.Path(item).name
                        with zf.open(item) as src, open(target, "wb") as dst:
                            dst.write(src.read())
                        n += 1
        except Exception as e:  # noqa: BLE001
            log("LOI giai nen %s: %s" % (z.name, e))
    log("-> %d anh PNG vao %s" % (n, RAW))
    return n


def wait_push(dirpath, tag):
    t0 = time.time()
    while time.time() - t0 < MAX_WAIT_PUSH_S:
        ok, msg = push(dirpath, tag)
        if ok:
            log("DA DAY KERNEL %s: %s" % (tag, msg))
            return True
        log("push %s that bai (%s) - thu lai sau %ds" % (tag, msg, PUSH_WAIT_S))
        time.sleep(PUSH_WAIT_S)
    return False


def wait_complete(ref):
    last = ""
    while True:
        s = status(ref)
        if s != last:
            log("%s => %s" % (ref, s))
            last = s
        if s == "COMPLETE":
            return True
        if s == "ERROR":
            log("KERNEL LOI: %s" % ref)
            return False
        time.sleep(WATCH_EVERY_S)


def main():
    RAW.mkdir(parents=True, exist_ok=True)
    BG.mkdir(parents=True, exist_ok=True)

    log("=== TAP 54 TIKTOK · 43 NEN DOC 9:16 (Kaggle FLUX) ===")
    ok1 = wait_push(DIR1, "K1")
    ok2 = wait_push(DIR2, "K2")
    if not (ok1 and ok2):
        log("KHONG DAY DUOC 2 KERNEL - dung tai day")
        return 1

    log("cho 2 kernel chay xong ...")
    d1 = wait_complete(K1)
    d2 = wait_complete(K2)
    if not (d1 and d2):
        log("co kernel khong COMPLETE")
        return 2

    n = 0
    n += download_and_extract(K1, OUT1)
    n += download_and_extract(K2, OUT2)
    log("tong anh tho: %d" % n)

    log("chay hau ky tai may ...")
    r = subprocess.run([sys.executable, str(HERE / "_tk_postprocess_t54.py")],
                       capture_output=True, text=True, cwd=str(ROOT))
    print(r.stdout, flush=True)
    if r.returncode != 0:
        print(r.stderr, flush=True)
        return 3

    jobs = json.loads((WORK / "bg_jobs_tk54.json").read_text(encoding="utf-8"))
    missing = [j["name"] for j in jobs if not (BG / ("%s.png" % j["name"])).exists()]
    log("nen thieu: %s" % (missing if missing else "khong co"))
    log("HOAN TAT")
    return 0


if __name__ == "__main__":
    sys.exit(main())
