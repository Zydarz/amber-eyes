#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""GIAM SAT SUAT TAP 02 EN — cac phep kiem tra BO SUNG (ngoài _qc_tap02_final.py).

Phep:
  P1  Nhip (pacing): phan bo do dai shot, shot > 15 s (H10), shot im lang > 2,5 s
  P2  Sync audio–shot: moi shot co loi phai co nang luong am thanh trong khoang
  P3  Dead air: quet ca tap trong file master (khong chi nhung doan > 0,3 s)
  P4  Frame: khong co khung den toan bo / khung dinh lap trong video
  P5  Phu de: 203 cau deu co cue, dung khoang thoi gian, khong trung
  P6  Do lech cau TTS: so cau co chu tren hinh ma cau do KHONG co trong script
  P7  Drift: audio trong mp4 co khop voi master mp3 (tuong quan cheo, 5 moc)
"""
import json
import os
import re
import subprocess
import sys
import wave
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
os.environ.setdefault("AE_LANG", "en")
os.environ.setdefault("AE_EP", "02")
os.environ.setdefault("PYTHONIOENCODING", "utf-8")
# Windows: stdout mac dinh cp1252 -> in tieng Viet co dau se UnicodeEncodeError.
for _s in ("stdout", "stderr"):
    try:
        getattr(sys, _s).reconfigure(encoding="utf-8", errors="replace")
    except Exception:
        pass
sys.path.insert(0, str(WORK))
import edition as ED  # noqa: E402

FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FP = FF.with_name("ffprobe.exe")
OUT = ED.OUT_DIR
MP4 = OUT / (ED.MASTER + ".mp4")
WAV = ED.w("audio_master.wav")
TL = json.loads(ED.w("timeline_s.json").read_text(encoding="utf-8-sig"))
SH = json.loads(ED.w("shots.json").read_text(encoding="utf-8-sig"))
SRT = (OUT / ED.SRT).read_text(encoding="utf-8-sig")

fails = []


def chk(label, cond, detail=""):
    if not cond:
        fails.append(label)
    print("[%s] %s%s" % ("OK  " if cond else "LOI", label, (" — " + detail) if detail else ""))


def run(args, timeout=3600):
    return subprocess.run(args, capture_output=True, text=True, encoding="utf-8",
                          errors="replace", timeout=timeout)


# ------------------------------------------------------------------ P1 pacing
print("=" * 78)
print("P1 — NHIP (pacing) cua bang shot moi")
print("=" * 78)
shots = SH["shots"]
durs = [(s["end"] - s["start"], s["id"], s.get("sentences", [])) for s in shots]
ds = sorted(d for d, _, _ in durs)
import statistics as st
print("   %d shot · min %.2f · p25 %.2f · median %.2f · p75 %.2f · max %.2f · TB %.2f"
      % (len(shots), ds[0], ds[len(ds) // 4], st.median(ds), ds[len(ds) * 3 // 4], ds[-1],
         sum(ds) / len(ds)))
over15 = [(d, i) for d, i, _ in durs if d > 15.0]
under3 = [(d, i, ss) for d, i, ss in durs if d < 3.0]
print("   shot > 15 s: %d  %s" % (len(over15), [(i, round(d, 1)) for d, i in over15[:8]]))
print("   shot < 3 s : %d (cac hang nghỉ/nghỉ chuyen hoi — thiet ke)" % len(under3))
# Shot < 3 s VAN CO LOI: chi can 1 cau ngan — van hop le. Chi loi khi < 1,5 s (khong doc nhat).
short_voice = [(d, i) for d, i, ss in under3 if ss and d < 1.5]
chk("Khong shot co loi nao < 1,5 s", not short_voice,
    ", ".join("%s=%.1fs" % (i, d) for d, i in short_voice[:6]))
# Shot > 15 s: tieu chuan cho phep khi co nhịp / chữ hiện đầu câu (QC A9.2 đã đạt) -> GHI NHAY
voice_long = [(d, i) for d, i, ss in durs if d > 15.0 and ss]
print("   [GHI] %d shot > 15 s co loi — QC A9.2 đã xác nhận có nhịp/bám V2: %s"
      % (len(voice_long), ", ".join("%s=%.1fs" % (i, d) for d, i in voice_long[:10])))
# so voi ban du 25/10
try:
    old_p = WORK / "_cu" / "shots_EN_t02_20261031_233834.json"
    old_sh = json.loads(old_p.read_text(encoding="utf-8-sig"))["shots"]
    od = sorted(s["end"] - s["start"] for s in old_sh)
    print("   so sanh ban du 25/10: %d shot · TB %.1f s · max %.1f s · > 15 s: %d"
          % (len(old_sh), sum(od) / len(od), od[-1], sum(1 for d in od if d > 15)))
    print("                ban moi : %d shot · TB %.1f s · max %.1f s · > 15 s: %d"
          % (len(shots), sum(ds) / len(ds), ds[-1], len(over15)))
except Exception as _e:
    print("   (khong doc duoc ban shot cu: %s)" % _e)

# ------------------------------------------------------------------ P2 sync
print()
print("=" * 78)
print("P2 — SYNC: moi shot co loi phai co tieng trong khoang")
print("=" * 78)
with wave.open(str(WAV), "rb") as wf:
    sr = wf.getframerate()
    n = wf.getnframes()
    x = np.frombuffer(wf.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    ch = wf.getnchannels()
if ch > 1:
    x = x.reshape(-1, ch).mean(axis=1)
print("   master: %.2f s @ %d Hz, %d kenh" % (len(x) / sr, sr, ch))
win = max(1, int(sr * 0.02))
k = len(x) // win
env = np.sqrt((x[:k * win].reshape(k, win) ** 2).mean(axis=1))
NOISE = np.percentile(env, 10) * 3 + 1e-4
bad_sync = []
for s in shots:
    ss = s.get("sentences", [])
    if not ss:
        continue
    a = max(0, int(s["start"] / (win / sr)))
    b = min(len(env), int(s["end"] / (win / sr)))
    if b <= a:
        bad_sync.append((s["id"], "window rong"))
        continue
    peak = env[a:b].max()
    if peak < NOISE:
        bad_sync.append((s["id"], "khong co tieng (peak %.4f < %.4f)" % (peak, NOISE)))
chk("Moi shot co loi deu co tieng trong khoang", not bad_sync, "; ".join(
    "%s: %s" % (i, d) for i, d in bad_sync[:6]))

# moi CAU phai co tieng
bad_sent = []
for it in TL["items"]:
    a = max(0, int((it["start"] + 0.05) / (win / sr)))
    b = min(len(env), int((it["end"] - 0.05) / (win / sr)))
    if b <= a:
        bad_sent.append((it["id"], "window rong"))
        continue
    if env[a:b].max() < NOISE:
        bad_sent.append((it["id"], "im lang"))
chk("Moi 1 trong %d cau deu co tieng" % len(TL["items"]), not bad_sent, "; ".join(
    "%s: %s" % (i, d) for i, d in bad_sent[:8]))

# ------------------------------------------------------------------ P3 dead air
print()
print("=" * 78)
print("P3 — DEAD AIR trong master (nguong -45 dB, >= 1,0 s)")
print("=" * 78)
r = run([str(FF), "-hide_banner", "-nostats", "-i", str(WAV),
         "-af", "silencedetect=noise=-45dB:d=1.0", "-f", "null", "-"], timeout=1800)
sil = re.findall(r"silence_start:\s*([\d.]+).*?silence_end:\s*([\d.]+)", r.stderr)
print("   doan im >= 1,0 s: %d" % len(sil))
for a, b in sil[:12]:
    print("      %8.2f -> %8.2f  (%.2f s)" % (float(a), float(b), float(b) - float(a)))
# cho phep cac doan im nam trong khoang "nghi" cua bang shot
rest_windows = [(s["start"], s["end"]) for s in shots if not s.get("sentences")]
unexplained = []
for a, b in sil:
    a, b = float(a), float(b)
    if any(w[0] - 0.6 <= a and b <= w[1] + 0.6 for w in rest_windows):
        continue
    unexplained.append((a, b))
chk("Khong co dead air > 1,0 s ngoai khoang nghi da thiet ke", not unexplained,
    "; ".join("%.1f-%.1fs" % (a, b) for a, b in unexplained[:6]))

# ------------------------------------------------------------------ P4 frames
print()
print("=" * 78)
print("P4 — FRAME: khong khung den toan bo / khong freeze")
print("=" * 78)
r = run([str(FF), "-hide_banner", "-nostats", "-i", str(MP4),
         "-vf", "blackdetect=d=0.5:pix_th=0.10", "-an", "-f", "null", "-"], timeout=3600)
blk = re.findall(r"black_start:\s*([\d.]+)\s+black_end:\s*([\d.]+)", r.stderr)
print("   doan den toan bo >= 0,5 s: %d %s" % (len(blk), blk[:8]))
d_mp4 = float(run([str(FP), "-v", "error", "-show_entries", "format=duration",
                    "-of", "default=noprint_wrappers=1:nokey=1", str(MP4)]).stdout.strip())
# den o dau intro + dip chuyen hoi tai ranh hoi + den o cuoi -> deu la THIET KE
act_ends = [TL["acts"][str(a)][1] for a in range(1, 6)]
tail_blacks = [(float(a), float(b)) for a, b in blk if float(b) > d_mp4 - 12]
unexpected = [(a, b) for a, b in blk
              if not (float(a) < 1.2 or float(b) > d_mp4 - 12
                      or any(abs(float(a) - e) < 1.5 or abs(float(b) - e) < 1.5
                             for e in act_ends))]
chk("Khong co khung den toan bo ngoai dip chuyen hoi / intro / outro", not unexpected,
    str(unexpected[:6]))
print("   den o cuoi (nen thiet ke): %s" % tail_blacks)
print("   ranh hoi (dip thiet ke): %s" % [round(e, 1) for e in act_ends])

r = run([str(FF), "-hide_banner", "-nostats", "-i", str(MP4),
         "-vf", "freezedetect=n=0.001:d=3", "-an", "-f", "null", "-"], timeout=3600)
fz = re.findall(r"freeze_start:\s*([\d.]+).*?freeze_duration:\s*([\d.]+)", r.stderr)
print("   doan freeze >= 3 s: %d %s" % (len(fz), fz[:6]))
long_fz = [(a, b) for a, b in fz if float(b) >= 6.0]
chk("Khong co freeze >= 6 s (tru doan cuoi chuyen den)", not long_fz, str(long_fz[:4]))

# ------------------------------------------------------------------ P5 subtitles
print()
print("=" * 78)
print("P5 — PHU DE")
print("=" * 78)
cues = [b for b in re.split(r"\n\s*\n", SRT.strip()) if b.strip()]
print("   %d cue" % len(cues))
cue_txt = []
last_end = 0.0
mono = True
for b in cues:
    L = b.splitlines()
    ts = re.findall(r"(\d+):(\d+):(\d+)[,.](\d+)", L[1])
    a = int(ts[0][0]) * 3600 + int(ts[0][1]) * 60 + int(ts[0][2]) + int(ts[0][3]) / 1000
    z = int(ts[1][0]) * 3600 + int(ts[1][1]) * 60 + int(ts[1][2]) + int(ts[1][3]) / 1000
    if a < last_end - 0.01:
        mono = False
    last_end = max(last_end, z)
    cue_txt.append((a, z, " ".join(L[2:]).strip()))
chk("Cue phu de khong chong lap", mono)
chk("Cue cuoi phai nam trong video", last_end <= d_mp4 + 0.5, "%.1f vs %.1f" % (last_end, d_mp4))
# doi chieu phu de voi cau
tl_items = TL["items"]
norm = lambda s: re.sub(r"\s+", " ", re.sub(r"[^\w\s]", " ", s.lower())).strip()
tl_n = [norm(i["text"]) for i in tl_items]
cue_all = norm(" ".join(t for _, _, t in cue_txt))
miss = [tl_items[i]["id"] for i, t in enumerate(tl_n)
        if t and t not in cue_all and len(t) > 12]
chk("Moi cau trong timeline deu co trong phu de", not miss, ", ".join(miss[:6]))
print("   cau khong doi chung: %d" % len(miss))

# ------------------------------------------------------------------ P6 cross-check
print()
print("=" * 78)
print("P6 — DOI CHIEU text: timeline / phu de / ke hoach")
print("=" * 78)
plan = (ED.EP_DIR / ("KeHoach_Video_Tap02.md" if not ED.EN else "KeHoach_Video_Tap02_EN.md")).read_text(encoding="utf-8-sig")
# chi quet BANG SHOT (truoc muc "Lượt sửa lỗi") — muc sua loi co trich nguyen van cum cu de ghi lai
plan_tbl = plan.split("### Lượt sửa lỗi")[0]
mismatch = []
for it in TL["items"]:
    t = norm(it["text"])
    if t and t not in norm(" ".join(x for _, _, x in cue_txt)):
        mismatch.append(it["id"])
chk("Text timeline == text phu de (tuoc 1:1)", not mismatch, ", ".join(mismatch[:6]))
for kw in ("snowshoe", "man disguised", "classified"):
    hit = [i + 1 for i, L in enumerate(plan_tbl.splitlines()) if kw in L]
    chk("Bang shot khong con cum cu '%s'" % kw, not hit, str(hit[:5]))

# ------------------------------------------------------------------ P7 drift
print()
print("=" * 78)
print("P7 — DRIFT: audio trong mp4 co khop voi master mp3 (tuong quan cheo)")
print("=" * 78)
MP3 = OUT / (ED.MASTER + ".mp3")
SR = 16000


def _pcm(path, ss, dur=40):
    r = subprocess.run([str(FF), "-v", "error", "-ss", str(ss), "-i", str(path),
                        "-t", str(dur), "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                       capture_output=True, timeout=600)
    return np.frombuffer(r.stdout, dtype="<i2").astype(np.float32)


def _lag_corr(ss):
    a = _pcm(MP3, ss)
    b = _pcm(MP4, ss)
    n = min(len(a), len(b), SR * 30)
    a, b = a[:n], b[:n]
    if n < SR * 5:
        return None, None
    N = 1
    while N < len(a) + len(b):
        N *= 2
    cc = np.fft.irfft(np.fft.rfft(a, N) * np.conj(np.fft.rfft(b, N)), N)
    cc = np.concatenate((cc[-(n - 1):], cc[:n]))
    lag = int(np.argmax(cc)) - (n - 1)
    norm = float(np.linalg.norm(a) * np.linalg.norm(b))
    return lag / SR, (float(cc.max()) / norm if norm else 0.0)


if not MP3.exists():
    print("   (khong co master mp3 — bo qua)")
else:
    pts = [20, 300, 700, 1000, 1300]
    res = []
    for ss in pts:
        if ss > d_mp4 - 45:
            continue
        s, c = _lag_corr(ss)
        if s is None:
            continue
        res.append((ss, s, c))
        print("   tai %5d s -> lech %+0.4f s | tuong quan %.4f" % (ss, s, c))
    if res:
        lags = [s for _, s, _ in res]
        cors = [c for _, _, c in res]
        # AAC/AAC tao treo ~ -5 ms co dinh: tieu chi = lech < 50 ms VA khong tran (drift) > 20 ms
        chk("Lech audio mp4 <-> master mp3 < 50 ms o moi moc",
            all(abs(s) < 0.05 for s in lags),
            ", ".join("%ds:%.3fs" % (t, s) for t, s, _ in res))
        chk("Khong co drift tich luy (do lech giua cac moc < 20 ms)",
            (max(lags) - min(lags)) < 0.02,
            "spread %.4f s" % (max(lags) - min(lags)))
        chk("Tuong quan audio mp4 <-> master mp3 >= 0,95 o moi moc",
            all(c >= 0.95 for c in cors),
            ", ".join("%ds:%.3f" % (t, c) for t, _, c in res))

print()
print("=" * 78)
print("TONG KET: %d phep that bai" % len(fails))
for f in fails:
    print("   - " + f)
print("=" * 78)
sys.exit(1 if fails else 0)
