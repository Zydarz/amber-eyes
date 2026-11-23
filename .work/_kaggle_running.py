# -*- coding: utf-8 -*-
"""Liệt kê các kernel Kaggle đang chạy (RUNNING/QUEUED) của tài khoản."""
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

out = subprocess.run([sys.executable, "-m", "kaggle", "kernels", "list", "--mine",
                      "--page-size", "40"], capture_output=True, text=True)
lines = [l for l in out.stdout.splitlines() if l.strip()]
refs = []
for l in lines[2:]:
    p = l.split()
    if p and p[0].startswith("chiduong"):
        refs.append(p[0])

print("tong kernel:", len(refs))
running = []
for r in refs:
    s = subprocess.run([sys.executable, "-m", "kaggle", "kernels", "status", r],
                       capture_output=True, text=True).stdout.strip()
    if "RUNNING" in s or "QUEUED" in s or "STARTING" in s:
        running.append((r, s.split("has status")[-1].strip()))
        print("DANG CHAY:", r, "=>", s.split("has status")[-1].strip())
if not running:
    print("khong co kernel nao dang chay")
