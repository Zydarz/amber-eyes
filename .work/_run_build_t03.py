#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chay build_video3.py va ghi log UTF-8 (PowerShell > tao file UTF-16LE)."""
import os
import subprocess
import sys
from pathlib import Path

W = Path(r"D:\TEST\Gax\amber-eyes\.work")
LOG = W / "_build_pic_t03.log"
BUILD = W / "build_video3.py"

env = dict(os.environ)
env["AE_EP"] = "03"
env["PYTHONIOENCODING"] = "utf-8"

with open(LOG, "w", encoding="utf-8", newline="\n") as log:
    p = subprocess.Popen([sys.executable, str(BUILD), "--workers", sys.argv[1] if len(sys.argv) > 1 else "6"],
                         stdout=subprocess.PIPE, stderr=subprocess.STDOUT, env=env,
                         cwd=str(W.parent), text=True, encoding="utf-8", errors="replace",
                         bufsize=1)
    for line in p.stdout:
        log.write(line)
        log.flush()
    rc = p.wait()
print("build exit=", rc)
sys.exit(rc)
