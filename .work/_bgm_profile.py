# -*- coding: utf-8 -*-
"""Do dac tinh chat cua 11 file BGM de chon bed phu hop cho TK2 (spec: jazz noir / Act 1).

Tieu chi: nhip do, tam trung, do no, co phai co tinh tiet khong.
"""
import glob
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = sorted(str(p) for p in (ROOT / ".work" / "ffmpeg").glob("*/bin/ffmpeg.exe"))[0]


def decode(path, sr=16000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def analyze(path):
    a = decode(path)
    sr = 16000
    dur = len(a) / sr
    rms = float(np.sqrt(np.mean(a ** 2)))
    peak = float(np.max(np.abs(a)))
    # nhip do qua zero-crossing
    zc = np.mean(np.abs(np.diff(np.sign(a))) > 0)
    bpm = zc * sr / 2.0
    # centroid tam trung (Hz)
    sp = np.abs(np.fft.rfft(a[:min(len(a), sr * 20)])) ** 2
    fr = np.fft.rfftfreq(min(len(a), sr * 20), 1 / sr)
    centroid = float((sp * fr).sum() / max(sp.sum(), 1e-12))
    # flatness (tieng on nhieu vs am thanh)
    psd = np.abs(np.fft.rfft(a[:min(len(a), sr * 20)])) ** 2 + 1e-12
    flat = float(np.exp(np.mean(np.log(psd))) / np.mean(psd))
    return dur, 20 * np.log10(max(rms, 1e-12)), 20 * np.log10(max(peak, 1e-12)), bpm, centroid, flat


print(f"{'file':30}{'dur':>7}{'rms dB':>9}{'peak dB':>9}{'bpm':>7}{'centroid Hz':>13}{'flatness':>10}")
for b in sorted((ROOT / "assets" / "bgm").glob("*.mp3")):
    d, rms, pk, bpm, cen, flat = analyze(b)
    print(f"{b.name:30}{d:7.1f}{rms:9.1f}{pk:9.1f}{bpm:7.0f}{cen:13.0f}{flat:10.4f}")
