#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Supervisor script:
1. Chờ tiến trình Higgs Audio Tập 03 hoàn tất 100% (VI, EN, JA).
2. Tự động kích hoạt sản xuất Tập 04 (VI -> EN -> JA) theo quy chuẩn QUY_TAC_HIGGS_MAC.md.
"""
import os
import sys
import time
import subprocess
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
PYTHON = sys.executable
LOG_FILE = HERE / "higgs_prod_t04_all.log"

def is_pid_running(pid):
    try:
        os.kill(pid, 0)
        return True
    except OSError:
        return False

def check_process_running(pattern):
    try:
        out = subprocess.check_output(["pgrep", "-f", pattern], text=True).strip()
        return len(out) > 0
    except subprocess.CalledProcessError:
        return False

def log(msg):
    t_str = time.strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{t_str} {msg}"
    print(line, flush=True)
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(line + "\n")

def main():
    log("=" * 80)
    log("SUPERVISOR STARTED: WAITING FOR EPISODE 03 TO COMPLETE...")
    log("=" * 80)

    # Monitor Episode 03
    while True:
        t03_running = check_process_running("generate_higgs_prod_t03ja.py") or check_process_running("run_higgs_prod_t03_all.py")
        if not t03_running:
            log("Episode 03 processes are no longer active.")
            break
        # Still running
        log("Episode 03 JA is still running. Waiting 20 seconds...")
        time.sleep(20)

    # Verify Episode 03 deliverables
    master_ja = ROOT / "02_SAN_XUAT" / "Tap03_JA" / "xuat_ban" / "Tap03_JA_master.mp3"
    if master_ja.exists() and master_ja.stat().st_size > 1000000:
        log(f"✅ Verified Episode 03 JA Master Audio: {master_ja} ({master_ja.stat().st_size / 1024 / 1024:.2f} MB)")
    else:
        log("⚠ Warning: Master audio file for Tap03_JA not found or too small, but process ended.")

    log("Letting OS memory settle for 10 seconds before starting Episode 04...")
    time.sleep(10)

    # Now launch Episode 04 production
    log("\n" + "=" * 80)
    log("LAUNCHING EPISODE 04 MULTILINGUAL PRODUCTION (VI -> EN -> JA)...")
    log("=" * 80)

    runner_script = HERE / "run_higgs_prod_t04_all.py"
    t_start = time.time()
    
    with open(LOG_FILE, "a", encoding="utf-8") as out_f:
        ret = subprocess.run([PYTHON, str(runner_script)], stdout=out_f, stderr=subprocess.STDOUT)
    
    dur = time.time() - t_start
    if ret.returncode == 0:
        log(f"🎉 EPISODE 04 MULTILINGUAL PRODUCTION COMPLETED SUCCESSFULLY in {dur/60:.1f} minutes!")
    else:
        log(f"❌ EPISODE 04 PRODUCTION FAILED with exit code {ret.returncode} after {dur/60:.1f} minutes!")

if __name__ == "__main__":
    main()
