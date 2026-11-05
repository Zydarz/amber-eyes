#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Pipeline dựng ẢNH TĨNH Tập 02 cho một ngôn ngữ (EN / JA / KO) — KHÔNG build video.

Bước: parse_shots -> QC -> render ảnh tĩnh -> contact sheet.

Dùng:  py -3 .work/_pipeline_stills_t02.py ja
"""
import os
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"


def run(desc, cmd, env):
    t0 = time.time()
    print(f"=== {desc} ===", flush=True)
    r = subprocess.run(cmd, cwd=ROOT, env=env, capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    out = (r.stdout or "") + (r.stderr or "")
    for line in out.strip().splitlines()[-40:]:
        print("   " + line)
    print(f"--- rc={r.returncode} · {time.time()-t0:.1f}s\n", flush=True)
    return r.returncode


def main():
    lang = sys.argv[1].lower() if len(sys.argv) > 1 else "vi"
    env = dict(os.environ)
    env["AE_LANG"] = lang
    env["AE_EP"] = "02"
    env["PYTHONIOENCODING"] = "utf-8"

    ok = True
    ok &= run("1. parse_shots", [sys.executable, str(W / "parse_shots.py")], env) == 0
    ok &= run("2. QC bang shot", [sys.executable, str(W / "_qc_tap02_langs.py")], env) == 0
    ok &= run("3. Render anh tinh", [sys.executable, str(W / "build_video3.py"), "--stills", "all"], env) == 0
    ok &= run("4. Contact sheet", [sys.executable, str(W / "_mk_contact_langs.py")], env) == 0
    print("HOAN TAT" if ok else "CO BUOC LOI")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
