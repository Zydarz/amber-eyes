#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""TRON LAI master EN TK2 Tap 04 (nguoi dung da cho phep).

Vao:  TK2_master_audio.mp3 moi (27/11, 72,34 s, 11/11 cau, NHANH DOC THUAN - khong BGM)
Ra:   TK2_master_audio_new.mp3 + .wav (BGM + ambience, TP <= -1,5 dBFS, 0 khoang cam > 0,3 s)

Cong thuc giong build_tiktok_master_audio_tk03.py (Tập 03):
  1. voice track tu master hien tai
  2. BGM tile lap + DUCKING -24 dB khi noi / -16 dB khi nghi (smooth 0,2 s)
  3. ambience phong kin (nhieu lam tron) -42 dB  => A1/V4: 0 khoang cam > 0,3 s
  4. fade cuoi 0,8 s (chi BGM + ambience; giong giu nguyen de khong mat cau cuoi)
  5. loudnorm 2 lượt I=-16, TP=-1,5, LRA=11  (+ limiter latency=1 theo A11 #38)

BAO HIEM KEEP HEADROOM (sai so da gap):
  - Master nguon da bi CLIP: 312 mau > 0 dBFS, peak +1,25 dBFS.
  - Ghi WAV 16-bit se clip cung them => loudnorm do sai TP => ket qua sai.
  => Ha voice ve peak -6 dBFS TRUOC khi tron (chu cho BGM), roi chuan hoa raw mix
     ve peak -3 dBFS truoc khi ghi WAV. KHONG sua noi dung giong noi.
"""
import json
import pathlib
import shutil
import subprocess
import sys
from datetime import datetime

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = sorted(str(p) for p in (ROOT / ".work" / "ffmpeg").glob("*/bin/ffmpeg.exe"))[0]
D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN"
SR = 48000

# SPEC Tap04 TK2 yeu cau bgm_jazz_noir.mp3 - FILE NAY KHONG CON tren dia (da xoa o dot don media).
# Chon bgm_ambient_deep.mp3: co tren dia + co dong provenance day du (MiniMax) + la bed ma
# clip TK2 cua Tap 03 cung dung (tien le trong du an) + ton noir phu hop Act 1.
BGM_FILE = ROOT / "assets" / "bgm" / "bgm_ambient_deep.mp3"

BG_GAIN_SPEAK_DB = -24.0
BG_GAIN_PAUSE_DB = -16.0
AMBIENCE_DB = -42.0
FADE_S = 0.8
LOUD_I, LOUD_TP, LOUD_LRA = -16.0, -1.5, 11.0
VOICE_PEAK_DB = -6.0     # chua cho BGM + ambience
RAW_PEAK_DB = -3.0       # headroom cho WAV 16-bit


def db(x):
    return 20 * np.log10(max(float(np.max(np.abs(x))), 1e-12))


def read_audio(path, sr=SR):
    p = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                       "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(p.stdout, dtype=np.float32).copy()


def write_wav(path, samples, sr=SR):
    import wave
    ints = (np.clip(samples, -1.0, 1.0) * 32767.0).astype(np.int16)
    with wave.open(str(path), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(ints.tobytes())


def generate_subtle_ambience(n, level_db=-42.0):
    np.random.seed(42)
    noise = np.random.normal(0, 1, n).astype(np.float32)
    b = np.ones(50) / 50.0
    smooth = np.convolve(noise, b, mode="same")
    peak = np.max(np.abs(smooth)) + 1e-9
    return (smooth / peak) * (10.0 ** (level_db / 20.0))


def measure(path):
    a = read_audio(path, sr=SR)
    pk = float(np.max(np.abs(a)))
    n_over = int((np.abs(a) > 1.0).sum())
    n = int(0.05 * SR)
    sil = 0.0
    for i in range(0, len(a) - n + 1, n):
        if float(np.max(np.abs(a[i:i + n]))) < 1e-4:
            sil += 0.05
    r = subprocess.run([FF, "-hide_banner", "-i", str(path), "-af",
                        f"loudnorm=I={LOUD_I}:TP={LOUD_TP}:LRA={LOUD_LRA}:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True)
    st = json.loads(r.stderr[r.stderr.rfind("{"):r.stderr.rfind("}") + 1])
    return dict(dur=len(a) / SR, peak=db(a), n_over=n_over, sil=sil,
                I=float(st["input_i"]), TP=float(st["input_tp"]))


def main():
    src = D / "TK2_master_audio.mp3"
    stem = D / "TK2_voice_stem.mp3"
    bakdir = ROOT / ".work" / "_cu" / f"entk2_master_premix_{datetime.now():%Y%m%d_%H%M}"
    bakdir.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, bakdir / src.name)
    if (D / "TK2_master_audio.wav").exists():
        shutil.copy2(D / "TK2_master_audio.wav", bakdir / "TK2_master_audio.wav")
    print("backup ->", bakdir)

    # IDEMPOTENT: doc voice tu stem neu da co (khong doc lai master da tron => khong tron 2 lan)
    voice_src = stem if stem.exists() else src
    print(f"nguon giong: {voice_src.name}")
    voice = read_audio(voice_src)
    N = len(voice)
    print(f"voice: {N/SR:.2f}s  peak={db(voice):+.2f} dBFS  mau>0dBFS={int((np.abs(voice)>1.0).sum())}")

    # luu voice stem de ASR chay tren file KHONG co BGM (BGM lam ASR nhieu manh - A11 #201)
    if not stem.exists():
        subprocess.run([FF, "-y", "-v", "error", "-i", str(voice_src), "-ar", str(SR), "-ac", "1",
                        str(stem)], check=True)
        print("da luu voice stem ->", stem.name)

    # --- 1. ha voice ve peak muc tieu (chu headroom cho BGM + ambience) ---
    vp = float(np.max(np.abs(voice)))
    target = 10 ** (VOICE_PEAK_DB / 20.0)
    vg = target / vp
    voice = voice * vg
    print(f"voice gain: {20*np.log10(vg):+.2f} dB  => peak {db(voice):+.2f} dBFS")

    # --- 2. BGM tile + ducking ---
    bgm = read_audio(BGM_FILE)
    reps = int(np.ceil(N / len(bgm))) + 1
    bgm = np.tile(bgm, reps)[:N].copy()
    voice_env = np.abs(voice)
    hop = int(0.05 * SR)
    for i in range(0, len(voice_env), hop):
        voice_env[i:i + hop] = np.mean(voice_env[i:i + hop])
    speaking = voice_env > 0.015
    gain = np.where(speaking, 10.0 ** (-BG_GAIN_SPEAK_DB / 20.0),
                    10.0 ** (-BG_GAIN_PAUSE_DB / 20.0)).astype(np.float32)
    smooth_w = int(0.2 * SR)
    gain = np.convolve(gain, np.ones(smooth_w) / smooth_w, mode="same")[:N]
    ducked = bgm * gain

    # --- 3. ambience phong kin ---
    amb = generate_subtle_ambience(N, AMBIENCE_DB)[:N]

    # --- 4. fade cuoi (chi BGM + ambience) ---
    fl = int(FADE_S * SR)
    fade = np.linspace(1.0, 0.05, fl)
    ducked[-fl:] *= fade
    amb[-fl:] *= fade

    raw = voice + ducked * 0.9 + amb
    rp = float(np.max(np.abs(raw)))
    if rp > 10 ** (RAW_PEAK_DB / 20.0):
        raw = raw * ((10 ** (RAW_PEAK_DB / 20.0)) / rp)
    raw_wav = bakdir / "TK2_mix_raw.wav"
    write_wav(raw_wav, raw)
    print(f"raw mix: peak {db(rp):+.2f} -> {db(raw):+.2f} dBFS (ghi WAV 16-bit, khong clip)")

    # --- 5. loudnorm 2 pass ---
    p1 = subprocess.run([FF, "-y", "-i", str(raw_wav), "-af",
                         f"loudnorm=I={LOUD_I}:TP={LOUD_TP}:LRA={LOUD_LRA}:print_format=json",
                         "-f", "null", "-"], capture_output=True, text=True, check=True)
    stats = json.loads(p1.stderr[p1.stderr.rfind("{"):p1.stderr.rfind("}") + 1])
    print("pass1:", {k: stats[k] for k in ("input_i", "input_tp", "input_lra", "target_offset")})
    filt = (f"loudnorm=I={LOUD_I}:TP={LOUD_TP}:LRA={LOUD_LRA}:"
            f"measured_I={stats['input_i']}:measured_TP={stats['input_tp']}:"
            f"measured_LRA={stats['input_lra']}:measured_thresh={stats['input_thresh']}:"
            f"offset={stats['target_offset']}:linear=true")

    new_wav = D / "TK2_master_audio_new.wav"
    new_mp3 = D / "TK2_master_audio_new.mp3"
    subprocess.run([FF, "-y", "-v", "error", "-i", str(raw_wav), "-af", filt,
                    "-ar", str(SR), "-ac", "2", str(new_wav)], check=True)
    subprocess.run([FF, "-y", "-v", "error", "-i", str(new_wav),
                    "-codec:a", "libmp3lame", "-b:a", "256k", str(new_mp3)], check=True)

    print()
    for label, p in [("CU ", src), ("MOI", new_mp3)]:
        m = measure(p)
        print(f"{label} {p.name}: {m['dur']:.2f}s  peak={m['peak']:+.2f} dBFS  mau>0dBFS={m['n_over']}  "
              f"im_lang_tuyet_doi={m['sil']:.2f}s  I={m['I']:.1f} LUFS  TP={m['TP']:.2f} dBFS")

    # kiem tra khoang cam > 0,3 s theo chuan QC (silencedetect -60 dB, d=0.3)
    r = subprocess.run([FF, "-hide_banner", "-i", str(new_mp3), "-af",
                        "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"],
                       capture_output=True, text=True)
    sils = [l for l in r.stderr.splitlines() if "silence_start" in l]
    print(f"khoang cam >0,3 s @ -60 dB: {len(sils)}")
    for s in sils:
        print("   ", s.strip())


if __name__ == "__main__":
    main()
