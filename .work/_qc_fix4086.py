#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem chat luong 3 take moi cua 4.08#6 (Higgs, fix 'snow boot impression').

- ASR 2 vong/ban (bo qua the) -> CER so voi cau dich
- do dai, dinh (peak), im lang dau/duoi
- F0 trung binh -> so voi take CU (cung vai D) de kiem tra giong
- chon ban tot nhat va CAI DAT vao audio_s_higgs_EN_t02/s4_08_6.wav
"""
import json
import pathlib
import re
import shutil
import subprocess
import sys
import time
import unicodedata
import wave

import numpy as np

HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
KG = HERE / "kaggle_higgs"
SRC = KG / "out_higgs_fix4086" / "out_higgs_fix4086"
INSTALL = HERE / "audio_s_higgs_EN_t02" / "s4_08_06.wav"
CACHE = KG / "_asr_cache_fix4086"
CACHE.mkdir(parents=True, exist_ok=True)
FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

EXPECT = ("Then Smyth laid down photographs of the snow boot impression from the crime scene "
          "beside Williams’s own boots, stating plainly: “They are identical.”")
OLD_TAKE = HERE / "audio_s_higgs_EN_t02" / "s4_08_06.wav"

sys.stdout.reconfigure(encoding="utf-8", errors="replace")


def norm(t):
    t = unicodedata.normalize("NFC", t.lower())
    t = re.sub(r"[^\w\s]", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def cer(ref, hyp):
    a, b = norm(ref), norm(hyp)
    d = list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        prev, d[0] = d[0], i
        for j in range(1, len(b) + 1):
            cur = d[j]
            d[j] = min(d[j] + 1, d[j - 1] + 1, prev + (a[i - 1] != b[j - 1]))
            prev = cur
    return d[-1] / max(1, len(a))


def mcode(args, timeout=600):
    r = subprocess.run(["cmd", "/c", "mcode-tools"] + args, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    if r.returncode != 0:
        raise RuntimeError((r.stderr or r.stdout or "")[:400])
    return json.loads(r.stdout)


def asr(path, rnd):
    cf = CACHE / f"{path.stem}__r{rnd}.json"
    if cf.exists():
        try:
            return json.loads(cf.read_text(encoding="utf-8"))
        except Exception:
            pass
    up = mcode(["upload-temp-url", str(path), "--mime-type", "audio/wav"])
    url = up.get("temp_url")
    if not url:
        return {"transcription": "", "code": -1, "error": "upload fail"}
    af = CACHE / f"{path.stem}__r{rnd}.args.json"
    af.write_text(json.dumps({"audio_info": {
        "url": url, "mime_type": "audio/wav",
        "prompt": "Transcribe verbatim in English, do not add or omit anything."}},
        ensure_ascii=False), encoding="utf-8")
    res = mcode(["connector", "call", "connector__matrix__listen_audio", "--args-file", str(af)])
    try:
        cf.write_text(json.dumps(res, ensure_ascii=False), encoding="utf-8")
    except Exception:
        pass
    return res


def wav_info(p):
    with wave.open(str(p), "rb") as wf:
        sr = wf.getframerate()
        n = wf.getnframes()
        x = np.frombuffer(wf.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    if wf.getnchannels() > 1:
        x = x.reshape(-1, wf.getnchannels()).mean(axis=1)
    return sr, x


def envelope(x, sr):
    win = max(1, int(sr * 0.02))
    k = len(x) // win
    return np.abs(x[:k * win]).reshape(k, win).max(axis=1)


def sil(x, sr, thr_db=-45.0, win_s=0.02):
    e = envelope(x, sr)
    thr = 10 ** (thr_db / 20)
    idx = np.where(e > thr)[0]
    if len(idx) == 0:
        return None, None, 0.0
    lead = idx[0] * win_s
    tail = (len(e) - idx[-1] - 1) * win_s
    return lead, tail, len(e) * win_s - lead - tail


def f0(x, sr):
    """F0 trung binh (autocorrelation) 70-260 Hz."""
    win = int(sr * 0.04)
    hop = int(sr * 0.02)
    vals = []
    for s in range(0, len(x) - win, hop):
        seg = x[s:s + win]
        if np.sqrt((seg ** 2).mean()) < 0.02:
            continue
        seg = seg - seg.mean()
        ac = np.correlate(seg, seg, "full")[win - 1:]
        lo, hi = int(sr / 260), int(sr / 70)
        if hi >= len(ac):
            continue
        k = int(np.argmax(ac[lo:hi])) + lo
        if ac[k] > 0.3 * ac[0]:
            vals.append(sr / k)
    return float(np.median(vals)) if vals else 0.0


def peak_db(p):
    r = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(p),
                        "-af", "volumedetect", "-f", "null", "-"],
                       capture_output=True, text=True, errors="replace")
    m = re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr)
    return float(m.group(1)) if m else 0.0


# ------------------------------------------------------------------ doi chieu take CU
print("=" * 78)
print("TAKE CU (audio dang cai dat) — baseline")
print("=" * 78)
sr_o, x_o = wav_info(OLD_TAKE)
lead_o, tail_o, speech_o = sil(x_o, sr_o)
old_f0 = f0(x_o, sr_o)
print("  dur %.2fs | speech %.2fs | lead %.2f | tail %.2f | peak %.2f dBFS | F0 %.1f Hz"
      % (len(x_o) / sr_o, speech_o, lead_o, tail_o, peak_db(OLD_TAKE), old_f0))

results = []
for p in sorted(SRC.glob("4_08_6_D_D_EN_t0.8_s*.wav")):
    sr, x = wav_info(p)
    lead, tail, speech = sil(x, sr)
    cers = []
    hyps = []
    for rnd in (1, 2):
        res = asr(p, rnd)
        hyp = res.get("transcription") or res.get("text") or ""
        hyps.append(hyp)
        cers.append(cer(EXPECT, hyp))
    pdb = peak_db(p)
    f = f0(x, sr)
    results.append({"file": p.name, "dur": len(x) / sr, "speech": speech, "lead": lead,
                    "tail": tail, "peak": pdb, "f0": f, "cer": cers, "hyp": hyps})
    print("\n" + "=" * 78)
    print("%s" % p.name)
    print("=" * 78)
    print("  dur %.2fs | speech %.2fs | lead %.2f | tail %.2f | peak %.2f dBFS | F0 %.1f Hz (cu %.1f, lech %.1f Hz)"
          % (len(x) / sr, speech, lead, tail, pdb, f, old_f0, f - old_f0))
    for i, (c, h) in enumerate(zip(cers, hyps), 1):
        print("  ASR r%d  CER %.2f%%" % (i, c * 100))
        print("       %r" % h)

print("\n" + "=" * 78)
print("BANG CHON")
print("=" * 78)
print("%-34s %8s %8s %8s %8s %8s" % ("file", "dur", "CER%", "peak", "tail", "F0"))
for r in results:
    print("%-34s %8.2f %8.2f %8.2f %8.2f %8.1f"
          % (r["file"], r["dur"], min(r["cer"]) * 100, r["peak"], r["tail"], r["f0"]))

# chon: CER thap nhat; peak <= -1.0 dBFS; tail < 1.5s
ok = [r for r in results if min(r["cer"]) <= 0.02 and r["peak"] <= -1.0 and r["tail"] < 1.5]
if not ok:
    print("\n!! KHONG co ban nao dat du dieu kien (CER<=2%, peak<=-1dB, tail<1.5s) — can review thu cong")
    raise SystemExit(2)
best = min(ok, key=lambda r: (min(r["cer"]), abs(r["f0"] - old_f0)))
print("\nCHON:", best["file"])

bak = HERE / "_cu" / ("s4_08_6_snowshoe_cu_%s.wav" % time.strftime("%Y%m%d_%H%M%S"))
shutil.copy2(OLD_TAKE, bak)
shutil.copy2(SRC / best["file"], OLD_TAKE)
print("BACKUP take cu ->", bak.name)
print("CAI DAT       ->", OLD_TAKE, OLD_TAKE.stat().st_size, "bytes")
sr_n, x_n = wav_info(OLD_TAKE)
print("dur moi %.2fs (cu %.2fs) | F0 moi %.1f Hz (cu %.1f)"
      % (len(x_n) / sr_n, len(x_o) / sr_o, f0(x_n, sr_n), old_f0))
