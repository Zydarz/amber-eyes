#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Chạy nốt toàn bộ pipeline EN Tập 02 sau khi đã nạp tiền gói TTS.

Thứ tự: TTS (18 câu còn thiếu) -> G10 -> build_audio3 -> parse_shots -> build_video3
        -> subtitles -> package -> QC A9.1/A9.3/A9.4.

Dùng:  $env:AE_LANG='en'; $env:AE_EP='02'; py -3 .work/_finish_tap02_en.py
"""
import os
import subprocess
import sys
import time
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
os.environ["AE_LANG"] = "en"
os.environ["AE_EP"] = "02"
os.environ["PYTHONIOENCODING"] = "utf-8"
PY = sys.executable


def run(script, args=(), label=None):
    label = label or script
    print(f"\n=== {label} ===", flush=True)
    t0 = time.time()
    r = subprocess.run([PY, str(W / script), *args], cwd=ROOT,
                       capture_output=True, text=True, encoding="utf-8", errors="replace")
    out = (r.stdout or "") + (r.stderr or "")
    print(out[-4000:], flush=True)
    print(f"--- {label}: exit={r.returncode} · {time.time() - t0:.0f}s", flush=True)
    if r.returncode != 0:
        raise SystemExit(f"DỪNG tại {label} (exit {r.returncode})")
    return out


# 1. đọc lại 18 câu vai D còn thiếu (script tự bỏ qua câu đã có)
run("tts_sentences.py", label="TTS 215 câu EN (chỉ đọc câu thiếu)")

# 1b. G10 là CHỐT: báo cáo phải là ĐẠT mới được dựng tiếp
run("voice_role_check.py", label="G10 — đồng nhất giọng theo vai")
rep = (ROOT / "02_SAN_XUAT" / "Tap02_EN" / "thu_giong_kiem_vai" / "report.md").read_text(encoding="utf-8")
if "KẾT LUẬN: ĐẠT" not in rep:
    print("\n!!! G10 KHÔNG ĐẠT — DỪNG, không dựng hình. Xem report.md:", flush=True)
    for line in rep.splitlines():
        if "KHÔNG ĐẠT" in line:
            print("   ", line.strip(), flush=True)
    raise SystemExit(3)
print(">>> G10 ĐẠT — tiếp tục dựng", flush=True)

# 2. âm thanh + bảng shot
run("build_audio3.py", label="Âm thanh (audio master + timeline)")
run("parse_shots.py", label="Bảng shot EN")
run("_qc_tap02_shots.py", label="QC A9.2 — bảng shot")

# 3. dựng hình (lâu nhất: ~92 phút với 6 worker)
run("build_video3.py", ["--workers", "6"], label="Dựng hình")

# 4. phụ đề + đóng gói
run("subtitles.py", label="Phụ đề SRT")
run("package.py", ["--mux"], label="Đóng gói (mux + thumbnail + mô tả)")

# 5. QC cuối
run("_qc_tap02_final.py", label="QC A9.1 / A9.3 / A9.4")
print("\nHOÀN TẤT — xem 02_SAN_XUAT/Tap02_EN/xuat_ban/")
