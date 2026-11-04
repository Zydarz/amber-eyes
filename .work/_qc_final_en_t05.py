#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QC CUOI Tap05 EN — kiem mp4 xuat ban truoc khi giao.

Cong: thoi luong · so khung · A/V sync · the ket · giai ma · loudness/peak.
Chay: py -3 .work/_qc_final_en_t05.py
"""
import hashlib
import json
import os
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
os.environ.setdefault("AE_EP", "05")
os.environ.setdefault("AE_LANG", "en")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"
MP4 = ROOT / "02_SAN_XUAT" / "Tap05_EN" / "xuat_ban" / "Tap05_EN_master.mp4"
MP3 = ROOT / "02_SAN_XUAT" / "Tap05_EN" / "xuat_ban" / "Tap05_EN_master.mp3"
PICTURE = WORK / "video3_EN_t05" / "picture.mp4"
TL = json.loads((WORK / "timeline_s_EN_t05.json").read_text(encoding="utf-8"))
TOT = TL["total"]
FPS = 30
SR = 8000
OK, FAIL = [], []


def ok(m):
    OK.append(m)


def bad(m):
    FAIL.append(m)


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", **kw)


def probe(path):
    p = sh([str(FP), "-v", "error", "-show_streams", "-show_format", "-of", "json", str(path)])
    return json.loads(p.stdout)


def grab(src, t0, dur):
    p = subprocess.run([str(FF), "-v", "error", "-ss", f"{t0}", "-t", f"{dur}", "-i", str(src),
                        "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"], capture_output=True)
    if p.returncode != 0 or not p.stdout:
        raise SystemExit(f"khong doc duoc audio {src}: {p.stderr.decode('utf-8','replace')[:300]}")
    return np.frombuffer(p.stdout, dtype="<i2").astype(np.float32) / 32768.0


def xcorr_full(x, y):
    L = len(x) + len(y) - 1
    N = 1
    while N < L:
        N *= 2
    c = np.fft.irfft(np.fft.rfft(x, N) * np.conj(np.fft.rfft(y, N)), N)
    return np.concatenate([c[N - len(y) + 1:], c[:len(x)]])


def xcorr_lag(x, y, maxlag):
    c = xcorr_full(x, y)
    mid = len(y) - 1
    seg = c[mid - maxlag: mid + maxlag + 1]
    lags = np.arange(-maxlag, maxlag + 1)
    b = int(np.argmax(seg))
    return int(lags[b]), float(seg[b])


def self_test():
    rng = np.random.default_rng(7)
    sig = rng.standard_normal(2048).astype(np.float32)

    def shift(a, k):
        o = np.zeros_like(a)
        o[k:] = a[:-k]
        return o

    c1 = xcorr_full(sig, shift(sig, 37))
    c2 = np.correlate(sig, shift(sig, 37), mode="full")
    same = c1.shape == c2.shape and np.allclose(c1, c2, atol=1e-3)
    l1, _ = xcorr_lag(sig, shift(sig, 37), 200)
    l2, _ = xcorr_lag(shift(sig, 37), sig, 200)
    if not (same and l1 == -37 and l2 == 37):
        raise SystemExit("self-test that bai: FFT/lag sai")
    print("  self-test xcorr: OK (FFT == np.correlate, dau lag dung)")


print("===== QC CUOI Tap05 EN =====")
print(f"  mp4 : {MP4}")
print(f"  mp3 : {MP3}")
print(f"  timeline.total = {TOT} s")
print()

# ---------- 0. file ton tai + hash
if not MP4.exists():
    raise SystemExit("KHONG CO MP4")
h = hashlib.sha256(MP4.read_bytes()).hexdigest()[:12]
print(f"  sha256(mp4) = {h} · size = {MP4.stat().st_size:,} bytes")

info = probe(MP4)
v = next(s for s in info["streams"] if s["codec_type"] == "video")
a = next(s for s in info["streams"] if s["codec_type"] == "audio")
dur = float(info["format"]["duration"])

# ---------- 1. thoi luong
if abs(dur - TOT) > 0.05:
    bad(f"1) Thoi luong mp4 = {dur:.3f} s, timeline.total = {TOT} s — LECH > 0,05 s")
else:
    ok(f"1) Thoi luong mp4 = {dur:.3f} s == timeline.total ({TOT} s), lech {dur - TOT:+.3f} s")

# ---------- 2. so khung
nf = int(round(float(v["nb_frames"]))) if v.get("nb_frames") not in (None, "N/A") else None
if nf is None:
    p = sh([str(FP), "-v", "error", "-count_frames", "-select_streams", "v:0",
            "-show_entries", "stream=nb_read_frames", "-of", "csv=p=0", str(MP4)])
    nf = int(p.stdout.strip().split(",")[0])
exp = int(TOT * FPS)
if nf != exp:
    bad(f"2) So khung = {nf}, ky vong {exp} (int(total*30))")
else:
    ok(f"2) So khung = {nf} == int({TOT} * {FPS}) = {exp}")

# ---------- 3. co goc / khung hinh / fps
if v["width"] != 1920 or v["height"] != 1080:
    bad(f"3) Khung hinh {v['width']}x{v['height']}, ky vong 1920x1080")
else:
    ok(f"3) Khung hinh 1920x1080 · fps = {v.get('r_frame_rate')} · codec = {v['codec_name']}")
if a["codec_name"] != "aac":
    bad(f"3) Audio codec = {a['codec_name']}, ky vong aac")
else:
    ok(f"3) Audio: aac {a.get('bit_rate')} · {a.get('sample_rate')} Hz · {a.get('channels')} kenh")

# ---------- 4. A/V sync (mp4 vs mp3 master) bang tuong quan cheo FFT
self_test()
print()
worst, rows = 0.0, []
windows = [(30.0, 60.0), (300.0, 330.0), (640.0, 670.0), (950.0, 980.0), (1200.0, 1230.0)]
for t0, t1 in windows:
    x = grab(MP4, t0, t1 - t0)
    y = grab(MP3, t0, t1 - t0)
    n = min(len(x), len(y))
    x, y = x[:n], y[:n]
    x = x - x.mean()
    y = y - y.mean()
    x /= (np.linalg.norm(x) + 1e-9)
    y /= (np.linalg.norm(y) + 1e-9)
    lag, r = xcorr_lag(x, y, int(0.3 * SR))
    ms = lag / SR * 1000
    worst = max(worst, abs(ms))
    rows.append((t0, lag, ms, r))
    print(f"  {t0:7.0f}-{t1:7.0f} s · lag {lag:+5d} mau = {ms:+7.1f} ms · r = {r:.4f}")
print()
if worst > 20:
    bad(f"4) Lech A/V lon nhat {worst:.1f} ms (> 20 ms)")
else:
    ok(f"4) Lech A/V lon nhat {worst:.1f} ms (<= 20 ms) so voi mp3 master tai 5 moc")

# ---------- 5. the ket o cuoi
# Luu y (A11 #55): the ket FADE OUT ve den ~2 s cuoi (dong thoi 0,11) — khu vuc do
# khong phai de so sanh anh. Phai lay khung luc the con sang.
from PIL import Image
sh = json.loads((WORK / "shots_EN_t05.json").read_text(encoding="utf-8"))
last = sh["shots"][-1]
card_start = last["end"] - (last["end"] - last["start"])   # bat dau the 5-15
still = np.asarray(Image.open(WORK / "video3_EN_t05" / "stills" / "shot_5-15.png").convert("RGB"),
                   dtype=np.float32)
for label, t in (("card_visible", card_start + 1.8), ("card_mid", card_start + 4.0)):
    out = WORK / f"_qc_endcard_en_t05_{label}.png"
    subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{t:.3f}", "-i", str(MP4),
                    "-frames:v", "1", str(out)], check=True)
    im = np.asarray(Image.open(out).convert("RGB"), dtype=np.float32)
    mae = float(np.abs(im - still).mean())
    bright = float(im.mean())
    if bright < 40:
        bad(f"5) Khung '{label}' (t={t:.1f} s) toi den (TB {bright:.1f}) — the ket khong hien")
    elif mae > 30:
        bad(f"5) Khung '{label}' (t={t:.1f} s) khac anh tinh shot 5-15 (MAE {mae:.1f} > 30)")
    else:
        ok(f"5) The ket hien dung tai t={t:.1f} s · do sang TB {bright:.1f} · MAE anh tinh {mae:.1f}")
# duoi video phai fade den (dong thoi voi VN Tap05 va EN Tap04)
out = WORK / "_qc_endcard_en_t05_tail.png"
subprocess.run([str(FF), "-y", "-v", "error", "-ss", f"{dur - 1.0:.3f}", "-i", str(MP4),
                "-frames:v", "1", str(out)], check=True)
im = np.asarray(Image.open(out).convert("RGB"), dtype=np.float32)
if float(im.mean()) > 2.0:
    bad(f"5) Duoi video khong fade den (TB {im.mean():.2f})")
else:
    ok(f"5) Duoi video fade den dung nhu VN Tap05 / EN Tap04 (TB {im.mean():.2f})")

# ---------- 6. giai ma toan bo: 0 loi
p = subprocess.run([str(FF), "-v", "error", "-i", str(MP4), "-f", "null", "-"],
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
errs = [l for l in p.stderr.splitlines() if l.strip()]
if p.returncode != 0 or errs:
    bad(f"6) Giai ma co loi ({len(errs)} dong): {errs[:5]}")
else:
    ok("6) Giai ma toan bo video: 0 loi")

# ---------- 7. loudness + true peak tren chinh mp4
e = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(MP4), "-af", "ebur128=peak=true",
                    "-f", "null", "-"], capture_output=True, text=True, encoding="utf-8",
                   errors="replace").stderr
import re
i_l = re.findall(r"I:\s+(-?[\d.]+) LUFS", e)
tp = re.findall(r"Peak:\s+(-?[\d.]+) dBFS", e)
lra = re.findall(r"LRA:\s+(-?[\d.]+) LU", e)
if i_l:
    print(f"  Integrated loudness (mp4) = {i_l[-1]} LUFS · LRA = {lra[-1] if lra else '?'} · "
          f"true peak = {tp[-1] if tp else '?'} dBFS")
    if abs(float(i_l[-1]) + 16) > 1.0:
        bad(f"7) Loudness {i_l[-1]} LUFS lech > 1 LU so voi chuan -16")
    else:
        ok(f"7) Loudness {i_l[-1]} LUFS (chuan -16 ± 1)")
    if tp and float(tp[-1]) > -1.5:
        bad(f"7) True peak {tp[-1]} dBFS > -1,5 dBFS")
    else:
        ok(f"7) True peak {tp[-1] if tp else '?'} dBFS (<= -1,5)")
else:
    bad("7) Khong doc duoc loudness tu mp4")

print()
for x in OK:
    print(f"  [OK]   {x}")
for x in FAIL:
    print(f"  [FAIL] {x}")
print(f"\n  => {len(OK)} OK · {len(FAIL)} loi")
(WORK / "_qc_final_en_t05_result.json").write_text(
    json.dumps({"ok": OK, "fail": FAIL, "sha256": h, "duration": dur, "frames": nf},
               ensure_ascii=False, indent=1), encoding="utf-8")
sys.exit(1 if FAIL else 0)
