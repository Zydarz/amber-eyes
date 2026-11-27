# -*- coding: utf-8 -*-
"""Debug tien trinh tron: gia tri cua voice / bgm / gain / ducked / ambience."""
import glob
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = sorted(str(p) for p in (ROOT / ".work" / "ffmpeg").glob("*/bin/ffmpeg.exe"))[0]
SR = 48000


def read_audio(path, sr=SR):
    p = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                       "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(p.stdout, dtype=np.float32).copy()


def db(x):
    return 20 * np.log10(max(float(np.max(np.abs(x))), 1e-12))


D = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap04_EN"
voice = read_audio(D / "TK2_master_audio.mp3")
N = len(voice)
bgm = read_audio(ROOT / "assets" / "bgm" / "bgm_ambient_deep.mp3")
print(f"voice: len={N} ({N/SR:.2f}s) peak={db(voice):+.2f} dBFS  n>1.0={int((np.abs(voice)>1).sum())}")
print(f"bgm:   len={len(bgm)} ({len(bgm)/SR:.2f}s) peak={db(bgm):+.2f} dBFS")

reps = int(np.ceil(N / len(bgm))) + 1
bgm_t = np.tile(bgm, reps)[:N].copy()
print(f"bgm tiled: len={len(bgm_t)} peak={db(bgm_t):+.2f} dBFS")

voice_env = np.abs(voice)
hop = int(0.05 * SR)
for i in range(0, len(voice_env), hop):
    voice_env[i:i + hop] = np.mean(voice_env[i:i + hop])
speaking = voice_env > 0.015
print(f"speaking frames: {speaking.sum()}/{len(speaking)} ({speaking.mean():.0%})")

g_speak = 10.0 ** (-24.0 / 20.0)
g_pause = 10.0 ** (-16.0 / 20.0)
gain = np.where(speaking, g_speak, g_pause).astype(np.float32)
print(f"gain: min={gain.min():.4f} max={gain.max():.4f} mean={gain.mean():.4f}")
smooth_w = int(0.2 * SR)
g2 = np.convolve(gain, np.ones(smooth_w) / smooth_w, mode="same")[:N]
print(f"gain sau smooth: min={g2.min():.4f} max={g2.max():.4f} mean={g2.mean():.4f} "
      f"(smooth_w={smooth_w})")
ducked = bgm_t * g2
print(f"ducked: peak={db(ducked):+.2f} dBFS")

np.random.seed(42)
noise = np.random.normal(0, 1, N).astype(np.float32)
b = np.ones(50) / 50.0
smooth = np.convolve(noise, b, mode="same")
peak = np.max(np.abs(smooth)) + 1e-9
amb = (smooth / peak) * (10.0 ** (-42.0 / 20.0))
print(f"amb: peak={db(amb):+.2f} dBFS")

raw = voice * 1.0 + ducked * 0.9 + amb
print(f"raw: peak={db(raw):+.2f} dBFS  min={raw.min():.3f} max={raw.max():.3f}")
