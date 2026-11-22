#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Supervisor for Episode 20 Multilingual Higgs Production (VI -> EN -> JA).
Strictly follows QUY_TAC_HIGGS_MAC.md, AGENTS.md (Rule L11, Rule M6):
- Uses active virtualenv python: /Users/duonganhhai/ai/.venv/bin/python
- Executes VI, EN, JA sequentially.
- Logs output to prod_t20vi.log, prod_t20en.log, prod_t20ja.log.
- Periodically reports progress.
"""
import os
import sys
import time
import subprocess
import pathlib

WORK = pathlib.Path(__file__).resolve().parent
ROOT = WORK.parent
PYTHON = "/Users/duonganhhai/ai/.venv/bin/python"

LANGS = [
    ("vi", WORK / "generate_higgs_prod_t20vi.py", WORK / "prod_t20vi.log"),
    ("en", WORK / "generate_higgs_prod_t20en.py", WORK / "prod_t20en.log"),
    ("ja", WORK / "generate_higgs_prod_t20ja.py", WORK / "prod_t20ja.log"),
]

def check_log(log_path):
    if not log_path.exists():
        return ["Log not created yet."]
    lines = log_path.read_text(encoding="utf-8", errors="replace").splitlines()
    return lines[-10:] if lines else ["Empty log."]

def run_step(lang, script_path, log_path):
    print(f"\n=======================================================", flush=True)
    print(f"PIPELINE STEP: {lang.upper()} -> {script_path.name}", flush=True)
    print(f"=======================================================", flush=True)

    with open(log_path, "w", encoding="utf-8") as lf:
        proc = subprocess.Popen([PYTHON, "-u", str(script_path)], stdout=lf, stderr=subprocess.STDOUT)
        pid = proc.pid
    print(f"Launched process PID: {pid}", flush=True)

    start_time = time.time()
    last_check = time.time()

    while True:
        time.sleep(15)
        poll_res = proc.poll()
        alive = (poll_res is None)

        now = time.time()
        if now - last_check >= 120 or not alive:
            last_check = now
            elapsed_min = (now - start_time) / 60
            print(f"[{time.strftime('%H:%M:%S')}] Status {lang.upper()} (PID {pid}): Alive={alive}, Elapsed={elapsed_min:.1f}m", flush=True)
            tail = check_log(log_path)
            for l in tail[-3:]:
                print(f"   | {l}", flush=True)

        if not alive:
            print(f"Process PID {pid} has finished with code {poll_res}. Checking result...", flush=True)
            time.sleep(3)
            log_text = log_path.read_text(encoding="utf-8", errors="replace")
            if "ALL GENERATION, QC, TIMELINE, AND MASTER AUDIO COMPLETED" in log_text or "Master MP3" in log_text or "Re-synchronized subtitles after final audio master mix" in log_text:
                print(f"✅ {lang.upper()} finished successfully!", flush=True)
                return True
            else:
                print(f"⚠️ {lang.upper()} finished with possible errors (code {poll_res}). Check {log_path.name}!", flush=True)
                return False

def main():
    print("=" * 80, flush=True)
    print("STARTING SUPERVISOR FOR TAP 20 MULTILINGUAL PIPELINE (VI -> EN -> JA)", flush=True)
    print("=" * 80, flush=True)

    print("✅ VI already 100% completed successfully. Proceeding to EN and JA.", flush=True)

    # Step 2: EN
    ok = run_step("en", LANGS[1][1], LANGS[1][2])
    if not ok:
        print("❌ EN failed. Stopping pipeline.", flush=True)
        sys.exit(1)

    # Step 3: JA
    ok = run_step("ja", LANGS[2][1], LANGS[2][2])
    if not ok:
        print("❌ JA failed. Stopping pipeline.", flush=True)
        sys.exit(1)

    print("\n🎉 ALL LANGUAGES (VI, EN, JA) PIPELINE COMPLETED SUCCESSFULLY FOR TAP 20!", flush=True)

if __name__ == "__main__":
    main()
