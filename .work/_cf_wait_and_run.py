#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chờ Cloudflare mở lại hạn mức rồi tự sinh nốt ảnh Tập 37/38/39.

Lặp: thử chạy gen_images_cf_resume.py (dùng cả 6 account, tự failover).
  - Nếu script sinh được ≥1 ảnh => quota đã mở => tiếp tục chạy tới hết, rồi thoát.
  - Nếu vẫn 429 (hết quota) => ngủ 180s rồi thử lại.
Request 429 không tốn neuron nên vòng lặp này gần như miễn phí.

Dùng: py -3 .work/_cf_wait_and_run.py [phut_toi_da]
"""
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
RESUME = WORK / "gen_images_cf_resume.py"

budget_min = float(sys.argv[1]) if len(sys.argv) > 1 else 55.0
deadline = time.time() + budget_min * 60
attempt = 0

print(f"Chờ quota Cloudflare tối đa {budget_min:.0f} phút...", flush=True)

while time.time() < deadline:
    attempt += 1
    stamp = time.strftime("%H:%M:%S")
    print(f"\n===== Lần thử {attempt} @ {stamp} =====", flush=True)
    p = subprocess.run([sys.executable, str(RESUME), "37", "38", "39"],
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (p.stdout or "") + (p.stderr or "")
    print(out[-4000:], flush=True)

    done = any(k in out for k in ("XONG", "thành công"))
    quota_dead = ("hết hạn mức" in out) or ("429" in out)
    if done:
        print(f"\n>>> ĐÃ SINH ĐƯỢC ẢNH — quota đã mở, tiếp tục chạy tới hết.", flush=True)
        # chạy nốt cho chắc (script đã chạy hết 3 tập ở trên)
        break
    if not quota_dead:
        print("\n>>> Lỗi khác quota — dừng vòng lặp, xem log.", flush=True)
        break
    wait = min(180, max(30, deadline - time.time()))
    print(f">>> Vẫn hết quota. Ngủ {wait:.0f}s rồi thử lại.", flush=True)
    time.sleep(wait)

print("\nKết thúc vòng chờ.", flush=True)
