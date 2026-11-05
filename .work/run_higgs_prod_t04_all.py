#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Master Runner for Episode 04 Multilingual (VI, EN, JA) Audio Production.
Tuân thủ đầy đủ QUY_TAC_HIGGS_MAC.md, QUY_TAC_AUDIO_HIGGS.md và AGENTS.md:
- Chạy tuần tự từng ngôn ngữ (VI -> EN -> JA) để đảm bảo không tranh chấp RAM 16GB trên Mac Apple Silicon.
- Đầy đủ giám sát Whisper CER, F0 & G9 pitch separation, và UTMOSv2 MOS naturalness.
- Xuất Audio Master MP3 & WAV, kiểm định EBUR128 cho từng ngôn ngữ.
"""
import os
import sys
import time
import subprocess
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
VENV_PYTHON = pathlib.Path("/Users/duonganhhai/ai/.venv/bin/python")
PYTHON = str(VENV_PYTHON) if VENV_PYTHON.exists() else sys.executable

SCRIPTS = [
    ("Vietnamese (VI)", HERE / "generate_higgs_prod_t04vi.py", "vi"),
    ("English (EN)", HERE / "generate_higgs_prod_t04en.py", "en"),
    ("Japanese (JA)", HERE / "generate_higgs_prod_t04ja.py", "ja"),
]

def main():
    print("=" * 80)
    print("MASTER PRODUCTION RUNNER: TAP 04 HIGGS MULTILINGUAL (VI, EN, JA)")
    print("=" * 80, flush=True)

    target_lang = sys.argv[1].lower() if len(sys.argv) > 1 else "all"

    for name, script_path, lang in SCRIPTS:
        if target_lang not in ("all", lang):
            continue

        print("\n" + "#" * 80)
        print(f"### STARTING PRODUCTION: {name}")
        print("#" * 80, flush=True)

        t_start = time.time()
        env = os.environ.copy()
        env["AE_EP"] = "04"
        env["AE_LANG"] = lang
        env["AE_AUDIO_DIR"] = "audio_s_higgs"

        ret = subprocess.run([PYTHON, str(script_path)], env=env)
        dur = time.time() - t_start

        if ret.returncode != 0:
            print(f"\n❌ ERROR: Production for {name} failed with exit code {ret.returncode} after {dur/60:.1f} minutes!")
            sys.exit(ret.returncode)

        print(f"\n✅ COMPLETED: {name} in {dur/60:.1f} minutes ({dur:.1f}s)", flush=True)
        time.sleep(5)  # Rest to let OS memory manager settle

    print("\n" + "=" * 80)
    print("🎉 ALL REQUESTED PRODUCTIONS COMPLETED SUCCESSFULLY FOR TAP 04!")
    print("=" * 80, flush=True)

if __name__ == "__main__":
    main()
