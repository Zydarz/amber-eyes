#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Master Production Runner for Episode 15 (Jodi Arias) across 3 Languages: VI, EN, JA.
Tuân thủ đầy đủ QUY_TAC_HIGGS_MAC.md, QUY_TAC_AUDIO_HIGGS.md và AGENTS.md:
- Chạy tuần tự từng ngôn ngữ để bảo vệ RAM 16GB (Rule M2).
- Giám sát Whisper CER, UTMOS MOS, G9 pitch separation, pause gate (A13), EBUR128 loudness.
- Xuất Audio Master MP3 & WAV cho từng ngôn ngữ.
"""
import os
import sys
import time
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
PYTHON = sys.executable

LANGS = [
    ("vi", "generate_higgs_prod_t15vi.py", "Tiếng Việt"),
    ("en", "generate_higgs_prod_t15en.py", "Tiếng Anh"),
    ("ja", "generate_higgs_prod_t15ja.py", "Tiếng Nhật"),
]

def main():
    print("=" * 80)
    print("STARTING FULL HIGGS PRODUCTION PIPELINE FOR EPISODE 15 (3 LANGUAGES)")
    print(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python interpreter: {PYTHON}")
    print("=" * 80, flush=True)

    results = {}
    total_start = time.time()

    for lang_code, script_name, lang_title in LANGS:
        print(f"\n>>>>>>>> STARTING LANGUAGE: {lang_title} ({lang_code.upper()}) <<<<<<<<")
        script_path = WORK / script_name
        if not script_path.exists():
            print(f"ERROR: Script not found: {script_path}", file=sys.stderr)
            sys.exit(1)

        t_lang_start = time.time()
        env = os.environ.copy()
        env["AE_EP"] = "15"
        env["AE_LANG"] = lang_code
        env["AE_AUDIO_DIR"] = "audio_s_higgs"

        cmd = [PYTHON, str(script_path)]
        print(f"Executing: {' '.join(cmd)}", flush=True)
        res = subprocess.run(cmd, env=env)
        elapsed = time.time() - t_lang_start

        if res.returncode != 0:
            print(f"\n❌ FAILED: {lang_title} ({lang_code}) returned exit code {res.returncode}", file=sys.stderr)
            sys.exit(res.returncode)

        results[lang_code] = {
            "title": lang_title,
            "elapsed": elapsed,
            "status": "SUCCESS"
        }
        print(f"\n✅ COMPLETED: {lang_title} ({lang_code.upper()}) in {elapsed/60:.2f} minutes!", flush=True)

    total_elapsed = time.time() - total_start
    print("\n" + "=" * 80)
    print("🎉 ALL 3 LANGUAGES COMPLETED SUCCESSFULLY FOR EPISODE 15!")
    print(f"Total Time: {total_elapsed/60:.2f} minutes")
    for code, info in results.items():
        print(f"  - {info['title']} ({code.upper()}): {info['elapsed']/60:.2f} min [{info['status']}]")
    print("=" * 80, flush=True)

if __name__ == "__main__":
    main()
