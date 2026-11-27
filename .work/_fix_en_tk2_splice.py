#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vá EN TK2 TikTok Tap 04: chen 2 cau bi thieu vao master audio.

Tinh huong: Tap04_EN/TK2_master_audio.mp3 chi co 9/11 cau. Loi dung dung o
56.14s ("...serial killers in history."), 2 slot sau (TK2.01#10 vai C va
TK2.01#11 CTA vai H) chi co BGM.

Cach sua:
  1. Giai ma master thanh stereo 48k.
  2. Do nen BGM tu vung sau loi (khong co tieng) va do muc giong noi hien co
     (vung co loi) => uoc luong muc giong de 2 cau moi co cung do lon.
  3. Chen WAV moi (Higgs Kaggle) dung vi tri: sau moi cau gap 0.7s.
  4. Neu vuot duoi file, noi them nen BGM (khong cat loi).
  5. Loudnorm 2 luot I=-16 TP=-1.5 LRA=11 (A7), giong cac master khac.

Dung: py -3 .work/_fix_en_tk2_splice.py <wav_cau10> <wav_cau11>
"""
import glob
import json
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:/TEST/Gax/amber-eyes")
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
SR = 48000

D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN"
MASTER = D / "TK2_master_audio.mp3"
SPEC = D / "SPEC_AUDIO_CLIP_TAP04.json"

# moc thoi gian do duoc tu ASR (timeline_tk2.json) + spec
SPEECH_END = 56.14      # het cau TK2.01#9
PAUSE_AFTER = {10: 0.7, 11: 0.7}   # pause sau #9 (=0.7) va sau #10 (=0.7)
TAIL_MIN = 58.0         # vung chi BGM (do nen)
SPEECH_WIN = (48.0, 56.0)  # vung co loi (do giong)


def decode(path, ch=2, sr=SR):
    cmd = [FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", str(ch), "-f", "f32le", "-"]
    raw = subprocess.run(cmd, capture_output=True, check=True).stdout
    a = np.frombuffer(raw, dtype=np.float32)
    if ch == 1:
        return a
    return a.reshape(-1, ch)


def rms(x):
    x = np.asarray(x, dtype=np.float64)
    return float(np.sqrt(np.mean(x * x) + 1e-20))


def db(v):
    return 20 * np.log10(max(v, 1e-12))


def main():
    w10, w11 = sys.argv[1], sys.argv[2]
    spec = json.loads(SPEC.read_text(encoding="utf-8-sig"))
    lines = {l["clip_line_id"]: l for l in spec["clips"]["TK2"]["lines"]}
    est10 = lines["TK2.01#10"]["est_dur_s"]
    est11 = lines["TK2.01#11"]["est_dur_s"]

    mst = decode(MASTER, ch=2)
    n = len(mst)
    print("master: %.2f s  (%d mau)" % (n / SR, n))

    # --- do nen BGM (vung khong loi) va uoc luong muc giong noi ---
    i_tail = int(TAIL_MIN * SR)
    tail = mst[i_tail:]
    bgm_rms = rms(tail)
    i_sp = int(SPEECH_WIN[0] * SR)
    j_sp = int(SPEECH_WIN[1] * SR)
    sp_total = rms(mst[i_sp:j_sp])
    voice_rms = float(np.sqrt(max(sp_total ** 2 - bgm_rms ** 2, 1e-12)))
    print("BGM rms %.1f dBFS | doan loi rms %.1f dBFS | uoc luong giong %.1f dBFS"
          % (db(bgm_rms), db(sp_total), db(voice_rms)))

    # --- 2 cau moi ---
    a10 = decode(w10, ch=1)
    a11 = decode(w11, ch=1)
    d10, d11 = len(a10) / SR, len(a11) / SR
    print("cau moi: #10 %.2f s (est %.2f) · #11 %.2f s (est %.2f)" % (d10, est10, d11, est11))

    def fit(a):
        r = rms(a)
        if r <= 0:
            return a
        g = voice_rms / r
        # tran 12 dB: khong cho vuot qua muc giong chuan
        g = min(g, 10 ** (12 / 20))
        print("   gain %.2f dB" % (20 * np.log10(g)))
        return a * g

    a10 = fit(a10)
    a11 = fit(a11)

    # --- vi tri chen ---
    t10 = SPEECH_END + PAUSE_AFTER[10]
    t11 = t10 + d10 + PAUSE_AFTER[11]
    end_need = t11 + d11
    total_need = end_need + 0.3
    print("chen #10 tai %.2f s · #11 tai %.2f s · can toi %.2f s (master %.2f s)"
          % (t10, t11, total_need, n / SR))

    # --- noi them nen BGM neu can ---
    if total_need > n / SR:
        extra = int((total_need - n / SR) * SR) + SR
        # lay nen BGM tu vang tail va noi lap
        bg = mst[i_tail:]
        reps = int(np.ceil(extra / len(bg))) + 1
        bg = np.tile(bg, (reps, 1))
        # fade vao noi lai cho tu nhien
        mst = np.concatenate([mst, bg[:extra]], axis=0)
        print("noi them %.2f s nen BGM" % (extra / SR))
    else:
        mst = mst[:int(total_need * SR)]

    # --- mix 2 cau moi vao ---
    def mix(dst, sig, t0):
        i0 = int(t0 * SR)
        k = min(len(sig), len(dst) - i0)
        if k <= 0:
            return
        s = sig[:k]
        if k < len(sig):  # cat phan truot qua het file -> fade out
            f = int(SR * 0.05)
            if k > f:
                s[-f:] *= np.linspace(1, 0, f)
        dst[i0:i0 + k] += s[:, None] if dst.ndim == 2 else s

    mix(mst, a10, t10)
    mix(mst, a11, t11)
    peak = float(np.max(np.abs(mst)))
    print("peak sau mix: %.2f dBFS" % db(peak))

    out_wav = D / "TK2_master_audio_fixed.wav"
    np.stack([mst[:, 0], mst[:, 1]], axis=1).astype(np.float32).tofile  # placeholder
    # ghi stereo float32 ra file wav bang python wave
    import wave
    pcm = np.clip(mst, -1.0, 1.0)
    pcm = (pcm * 32767.0).astype(np.int16)
    with wave.open(str(out_wav), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())
    print("wav:", out_wav, "%.2f s" % (len(pcm) / SR / 2))

    # --- loudnorm 2 luot ---
    tmp = ROOT / ".work" / "_tk2_fixed_pre.wav"
    r1 = subprocess.run([FF, "-hide_banner", "-i", str(out_wav), "-af",
                         "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json", "-f", "null", "-"],
                        capture_output=True, text=True, errors="replace")
    import re
    j = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r1.stderr, re.S)
    vals = json.loads(j.group(0)) if j else {}
    print("loudnorm pass1:", {k: vals.get(k) for k in ("input_i", "input_tp", "input_lra", "input_thresh")})
    meas = (f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={vals.get('input_i')}"
            f":measured_TP={vals.get('input_tp')}:measured_LRA={vals.get('input_lra')}"
            f":measured_thresh={vals.get('input_thresh')}:linear=true")
    out_mp3 = D / "TK2_master_audio.mp3"
    subprocess.run([FF, "-y", "-v", "error", "-i", str(out_wav), "-af", meas,
                    "-ar", "48000", "-ac", "2", "-b:a", "192k", str(out_mp3)], check=True)
    subprocess.run([FF, "-y", "-v", "error", "-i", str(out_mp3), "-ar", "48000", "-ac", "2",
                    str(out_mp3.with_suffix(".wav"))], check=True)
    print("master moi:", out_mp3)

    # --- do lai LUFS cua cac master EN khac de doi chieu ---
    for cid in ("TK1", "TK3", "TK4", "TK5"):
        p = D / f"{cid}_master_audio.mp3"
        if not p.exists():
            continue
        r = subprocess.run([FF, "-hide_banner", "-i", str(p), "-af", "ebur128=peak=true",
                            "-f", "null", "-"], capture_output=True, text=True, errors="replace")
        m = re.findall(r"I:\s*(-?[\d.]+)\s*LUFS", r.stderr)
        pk = re.findall(r"Peak:\s*(-?[\d.]+)", r.stderr)
        print("  %s: %s LUFS, peak %s" % (cid, m[-1] if m else "?", pk[-1] if pk else "?"))


if __name__ == "__main__":
    main()
