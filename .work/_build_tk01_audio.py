#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dung am thanh clip TikTok TK1: giong (master) + BGM co ducking + SFX tong hop
-> chuan hoa -16 LUFS, true peak <= -1,5 dBFS.

Nguon am thanh (chi dung nguon duoc phep cho TikTok):
  - giong  : 02_SAN_XUAT/TIKTOK/Tap01/TK1_master_audio.wav (nguoi dung tao)
  - BGM   : assets/bgm/bgm_sub_drone.mp3  (MiniMax Music - duoc phep)
  - SFX   : tu tong hop boi script nay (khong dung 211 SFX YouTube Audio Library)

Muc ke hoach: BGM -26 dB khi co loi, nang -14 dB o nghi; luon co lop nen moi truong (A1).
"""
import json
import os
import pathlib
import re
import subprocess
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
HERE = ROOT / ".work"
FF = HERE / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap01"
CLIP = os.environ.get("AE_CLIP", "TK1")      # L8: cau hinh clip nam trong SPEC
N = CLIP[2:]
_SPEC = json.loads((D / "SPEC_AUDIO_CLIP_TAP01.json").read_text(encoding="utf-8-sig"))
CLIP_SPEC = next(c for c in _SPEC["clips"] if c["id"] == CLIP)
MASTER = D / ("%s_master_audio.wav" % CLIP)
BGM = ROOT / "assets" / "bgm" / CLIP_SPEC["bgm"]
TL = D / ("timeline_tk%s.json" % N)
OUT_WAV = HERE / ("_tk%s_mix_raw.wav" % N)
OUT_NORM = HERE / ("_tk%s_mix_norm.wav" % N)
STATS = HERE / ("_tk%s_loudnorm.json" % N)

SR = 48000
TARGET_I = -16.0
TARGET_TP = -1.5
BED_REL_SPEECH = -26.0      # BGM so voi RMS giong khi co loi
BED_REL_PAUSE = -14.0       # BGM so voi RMS giong khi nghi
ROOM_REL = -38.0            # nen moi truong (room tone)
SFX_REL = -34.0             # tieng may ghi am "Tach"


def read_wav(p):
    with wave.open(str(p), "rb") as wf:
        sr = wf.getframerate()
        ch = wf.getnchannels()
        sw = wf.getsampwidth()
        raw = wf.readframes(wf.getnframes())
    x = np.frombuffer(raw, dtype=np.int16).astype(np.float32) / 32768.0
    if ch > 1:
        x = x.reshape(-1, ch).mean(axis=1)
    return x, sr


def write_wav(p, x, sr=SR, ch=2):
    st = np.stack([x, x], axis=1) if ch == 2 else x[:, None]
    pcm = (np.clip(st, -1.0, 1.0) * 32767).astype(np.int16)
    with wave.open(str(p), "wb") as wf:
        wf.setnchannels(ch)
        wf.setsampwidth(2)
        wf.setframerate(sr)
        wf.writeframes(pcm.tobytes())


def decode_to_wav(src, dst, sr=SR):
    subprocess.run([str(FF), "-y", "-v", "error", "-i", str(src), "-ac", "1", "-ar", str(sr),
                    "-f", "wav", str(dst)], check=True, capture_output=True)


def rms_db(x):
    return 20 * np.log10(max(float(np.sqrt(np.mean(x ** 2))), 1e-9))


def one_pole_smooth(g, attack, release, sr=SR):
    """Lam noi muc gain: attack/release don (s) -> tranh 'pump'."""
    a = float(np.exp(-1.0 / (attack * sr)))
    r = float(np.exp(-1.0 / (release * sr)))
    out = np.empty_like(g)
    y = g[0]
    for i in range(len(g)):
        c = a if g[i] < y else r
        y = c * y + (1 - c) * g[i]
        out[i] = y
    return out


def room_tone(n, sr, seed=7):
    """ Nen moi truong: nhiet do lam filtered (1/f) - khong tieng 'his' giong."""
    rng = np.random.default_rng(seed)
    x = rng.standard_normal(n).astype(np.float32)
    # 1/f: loc trung binh 3 lan
    k = 24
    x = np.convolve(x, np.ones(k, dtype=np.float32) / k, mode="same")
    x = np.convolve(x, np.ones(k, dtype=np.float32) / k, mode="same")
    x /= max(float(np.sqrt(np.mean(x ** 2))), 1e-9)
    return x


def recorder_click(n, sr):
    """ Tieng may ghi am 'Tach': tick + thin transient."""
    rng = np.random.default_rng(11)
    burst = rng.standard_normal(int(0.035 * sr)).astype(np.float32)
    burst *= np.exp(-np.linspace(0, 9, len(burst)))
    t = np.arange(len(burst)) / sr
    thump = 0.5 * np.sin(2 * np.pi * 180 * t) * np.exp(-np.linspace(0, 14, len(burst)))
    x = burst * 0.6 + thump * 0.4
    out = np.zeros(n, dtype=np.float32)
    out[:len(x)] = x
    out /= max(float(np.sqrt(np.mean(out ** 2))), 1e-9)
    return out


def metal_clank(n, sr, at):
    """Tieng kim loai va cham (tong hop): thanh phan khong hoa am tat dan + transient."""
    rng = np.random.default_rng(23)
    L = int(1.1 * sr)
    t = np.arange(L) / sr
    x = np.zeros(L, dtype=np.float32)
    for f, a, dk in ((820, 1.0, 7), (1330, 0.7, 9), (2170, 0.5, 11), (3410, 0.3, 14)):
        x += (a * np.sin(2 * np.pi * f * t + rng.uniform(0, 6.28)) * np.exp(-dk * t)).astype(np.float32)
    k = int(0.012 * sr)
    x[:k] += rng.standard_normal(k).astype(np.float32) * np.exp(-np.linspace(0, 7, k)) * 0.8
    out = np.zeros(n, dtype=np.float32)
    i0 = int(at * sr)
    seg = x[:max(0, min(L, n - i0))]
    out[i0:i0 + len(seg)] = seg
    out /= max(float(np.sqrt(np.mean(out ** 2))), 1e-9)
    return out


def paper_flip(n, sr, at):
    """Tieng lat giay (tong hop): nhieu xao xac ngan loc dai 2-6 kHz, bao nhanh."""
    rng = np.random.default_rng(31)
    L = int(0.9 * sr)
    x = np.zeros(L, dtype=np.float32)
    for off, dur, amp in ((0.00, 0.22, 1.0), (0.28, 0.16, 0.6), (0.52, 0.10, 0.4)):
        k = int(dur * sr)
        nz = rng.standard_normal(k).astype(np.float32)
        nz = nz - np.convolve(nz, np.ones(12, dtype=np.float32) / 12, mode="same")   # cao tan
        env = np.sin(np.linspace(0, np.pi, k)) ** 2 * np.exp(-np.linspace(0, 3, k))
        i0 = int(off * sr)
        x[i0:i0 + k] += amp * nz * env
    out = np.zeros(n, dtype=np.float32)
    i0 = int(at * sr)
    seg = x[:max(0, min(L, n - i0))]
    out[i0:i0 + len(seg)] = seg
    out /= max(float(np.sqrt(np.mean(out ** 2))), 1e-9)
    return out


def door_knock(n, sr, at):
    """Tieng go cua (tong hop): 3 cu go tram, thanh phan 90-140 Hz tat nhanh + transient go."""
    rng = np.random.default_rng(41)
    L = int(1.4 * sr)
    x = np.zeros(L, dtype=np.float32)
    for off, f0, amp in ((0.00, 118, 1.0), (0.36, 104, 0.85), (0.74, 96, 0.7)):
        k = int(0.28 * sr)
        t = np.arange(k) / sr
        body = np.sin(2 * np.pi * f0 * t) * np.exp(-t * 18) + 0.4 * np.sin(2 * np.pi * f0 * 2.3 * t) * np.exp(-t * 28)
        c = int(0.008 * sr)
        body[:c] += rng.standard_normal(c) * np.exp(-np.linspace(0, 6, c)) * 0.9
        i0 = int(off * sr)
        x[i0:i0 + k] += (amp * body).astype(np.float32)
    out = np.zeros(n, dtype=np.float32)
    i0 = int(at * sr)
    seg = x[:max(0, min(L, n - i0))]
    out[i0:i0 + len(seg)] = seg
    out /= max(float(np.sqrt(np.mean(out ** 2))), 1e-9)
    return out


def main():
    tl = json.loads(TL.read_text(encoding="utf-8-sig"))
    voice, sr = read_wav(MASTER)
    total = len(voice) / sr
    print("  giong: %.2f s @ %d Hz" % (total, sr))

    # --- BGM -> mono 48k, lap cho duot dai ---
    bgm_wav = HERE / ("_tk%s_bgm.wav" % N)
    decode_to_wav(BGM, bgm_wav)
    bgm, _ = read_wav(bgm_wav)
    n = len(voice)
    reps = int(np.ceil(n / len(bgm)))
    bed = np.tile(bgm, reps)[:n].astype(np.float32)

    voice_rms = rms_db(voice[int(0.3 * sr):int(2.0 * sr)])
    bed_rms = rms_db(bed)
    print("  RMS giong %.1f dBFS · RMS bed %.1f dBFS" % (voice_rms, bed_rms))

    # --- gain bed: pause = giong - 14 dB ; speech = giong - 26 dB ---
    target_pause = voice_rms + BED_REL_PAUSE
    g_base_db = target_pause - bed_rms
    print("  gain bed goc %.1f dB (pause) -> %.1f dB (co loi)"
          % (g_base_db, g_base_db + (BED_REL_SPEECH - BED_REL_PAUSE)))

    # --- envelope ducking theo timeline ---
    speech = np.zeros(n, dtype=np.float32)
    for l in tl:
        i0 = max(0, int(l["start"] * sr))
        i1 = min(n, int(l["end"] * sr))
        speech[i0:i1] = 1.0
    # moc chuyen duong: giong -> -12 dB, nghi -> 0 dB
    g_db = np.where(speech > 0, BED_REL_SPEECH - BED_REL_PAUSE, 0.0).astype(np.float32)
    g_db = one_pole_smooth(g_db, attack=0.12, release=0.40, sr=sr)
    gain = 10 ** ((g_base_db + g_db) / 20.0)
    bed_mix = bed * gain

    # --- nen moi truong + SFX ---
    rt = room_tone(n, sr) * (10 ** ((voice_rms + ROOM_REL) / 20.0))
    if CLIP == "TK1":
        sfx = recorder_click(n, sr) * (10 ** ((voice_rms + SFX_REL) / 20.0))
        sfx_note = "tu tong hop (room tone + tick may ghi am)"
    else:   # SFX theo SPEC: sfx_kind (clank|paper) tai dau cau sfx_at (hoac sfx_clank_at)
        kind = CLIP_SPEC.get("sfx_kind", "clank")
        at = next(l["start"] for l in tl
                  if l["id"] == (CLIP_SPEC.get("sfx_at") or CLIP_SPEC["sfx_clank_at"]))
        fn = {"paper": paper_flip, "knock": door_knock}.get(kind, metal_clank)
        sfx = fn(n, sr, at) * (10 ** ((voice_rms + SFX_REL) / 20.0))
        sfx_note = "tu tong hop (room tone + %s tai %.2f s)" % (
            {"paper": "lat giay", "knock": "go cua"}.get(kind, "kim loai va cham"), at)

    mix = voice + bed_mix + rt + sfx
    peak = float(np.max(np.abs(mix)))
    print("  truoc chuan hoa: peak %.2f dBFS" % (20 * np.log10(max(peak, 1e-9))))
    write_wav(OUT_WAV, mix, SR, 2)

    # --- loudnorm 2 pass ---
    p1 = subprocess.run([str(FF), "-hide_banner", "-i", str(OUT_WAV), "-af",
                         "loudnorm=I=%g:TP=%g:LRA=11:print_format=json" % (TARGET_I, TARGET_TP),
                         "-f", "null", "-"], capture_output=True, text=True, errors="replace")
    txt = p1.stderr
    m = re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", txt, re.S)
    if not m:
        print("  LOI: khong parse duoc loudnorm JSON\n%s" % txt[-2000:])
        return 1
    meas = json.loads(m.group(0))
    print("  loudnorm do 1 luot:", {k: meas.get(k) for k in
                                   ("input_i", "input_tp", "input_lra", "input_thresh")})
    af = ("loudnorm=I=%g:TP=%g:LRA=11:measured_I=%s:measured_TP=%s:measured_LRA=%s:"
          "measured_thresh=%s:offset=%s:linear=true:print_format=summary"
          % (TARGET_I, TARGET_TP, meas["input_i"], meas["input_tp"], meas["input_lra"],
             meas["input_thresh"], meas.get("target_offset", 0.0)))
    subprocess.run([str(FF), "-y", "-hide_banner", "-v", "error", "-i", str(OUT_WAV), "-af", af,
                    "-ar", str(SR), "-c:a", "pcm_s16le", str(OUT_NORM)], check=True,
                   capture_output=True)

    # --- do lai bang ebur128 ---
    p2 = subprocess.run([str(FF), "-hide_banner", "-i", str(OUT_NORM), "-af",
                          "ebur128=peak=true", "-f", "null", "-"], capture_output=True,
                         text=True, errors="replace")
    tail = p2.stderr[-2500:]
    i_m = re.findall(r"I:\s*(-?\d+\.?\d*) LUFS", tail)
    tp_m = re.findall(r"Peak:\s*(-?\d+\.?\d*) dBFS", tail)
    lra_m = re.findall(r"LRA:\s*(-?\d+\.?\d*) LU", tail)
    i_val = float(i_m[-1]) if i_m else None
    tp_val = float(tp_m[-1]) if tp_m else None
    print("  SAU chuan hoa: I = %s LUFS · true peak = %s dBFS · LRA = %s"
          % (i_val, tp_val, lra_m[-1] if lra_m else "?"))

    stats = {"input_i": meas.get("input_i"), "input_tp": meas.get("input_tp"),
             "final_i": i_val, "final_tp": tp_val,
             "bed_gain_base_db": round(g_base_db, 2),
             "bed_rel_speech_db": BED_REL_SPEECH, "bed_rel_pause_db": BED_REL_PAUSE,
             "room_rel_db": ROOM_REL, "sfx_rel_db": SFX_REL,
             "voice_rms_db": round(voice_rms, 2), "bed_rms_db": round(bed_rms, 2),
             "duration_s": round(total, 3),
             "sources": {"voice": "02_SAN_XUAT/TIKTOK/Tap01/%s_master_audio.wav" % CLIP,
                         "bgm": "assets/bgm/%s (MiniMax Music)" % CLIP_SPEC["bgm"],
                         "sfx": sfx_note}}
    STATS.write_text(json.dumps(stats, ensure_ascii=False, indent=2), encoding="utf-8")
    print("  -> %s" % OUT_NORM)
    print("  -> %s" % STATS)
    return 0


if __name__ == "__main__":
    sys.exit(main())
