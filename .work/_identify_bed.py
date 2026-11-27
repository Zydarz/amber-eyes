#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Xac dinh bed nhac nen cua 14 clip da co tren dia:
 1) tach doan "giua hai cau" (khoang nghi) cua tung clip
 2) tuong quan envelope voi 11 file BGM trong assets/bgm/ => file nao khop
 3) do muc bed (RMS) va muc giong (speech) de biet ty le tron cua clip chuan

Dich khi: file nao THAT su duoc dung cho clip nao.
"""
import glob
import json
import pathlib
import subprocess
import sys

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parent.parent
FF = glob.glob(str(ROOT / ".work" / "ffmpeg" / "*" / "bin" / "ffmpeg.exe"))[0]
BGMDIR = ROOT / "assets" / "bgm"


def decode(path, sr=16000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def env_rms(a, sr=16000, win=0.10):
    n = int(win * sr)
    out = []
    for i in range(0, len(a) - n + 1, n):
        seg = a[i:i + n]
        out.append(float(np.sqrt(np.mean(seg ** 2))))
    return np.array(out)


def corr(x, y):
    if len(x) < 5 or len(y) < 5:
        return 0.0
    m = min(len(x), len(y))
    x, y = x[:m], y[:m]
    x = x - x.mean()
    y = y - y.mean()
    if np.std(x) < 1e-9 or np.std(y) < 1e-9:
        return 0.0
    return float(np.corrcoef(x, y)[0, 1])


def main():
    bgms = sorted(BGMDIR.glob("*.mp3"))
    bgm_env = {}
    for b in bgms:
        bgm_env[b.name] = env_rms(decode(b))
    print("=== ung vien BGM tren dia ===")
    for k, v in bgm_env.items():
        print(f"   {k:34} dur_env={len(v)*0.1:6.1f}s")

    spec_bg = {
        ("Tap04", "TK1"): "bgm_ambient_tension.mp3", ("Tap04", "TK2"): "bgm_jazz_noir.mp3",
        ("Tap04", "TK3"): "bgm_sub_drone.mp3", ("Tap04", "TK4"): "bgm_ambient_deep.mp3",
        ("Tap04", "TK5"): "bgm_piano_warm.mp3",
    }
    for ld in ["Tap04", "Tap04_EN", "Tap04_JA"]:
        for n in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
            d = ROOT / "02_SAN_XUAT" / "TIKTOK" / ld
            mp3 = d / f"{n}_master_audio.mp3"
            tl = json.loads((d / f"timeline_{n.lower()}.json").read_text(encoding="utf-8"))
            a = decode(mp3)
            # khoang nghi: giua dong i va i+1, lay o giua
            gaps = []
            for i in range(len(tl) - 1):
                g0, g1 = tl[i]["end"], tl[i + 1]["start"]
                if g1 - g0 > 0.25:
                    gaps.append((g0, g1))
            want = spec_bg.get((ld, n), spec_bg.get(("Tap04", n)))
            # lay 1 khoang nghi dai nhat, cat 0.3s moi dau de tranh loai nhac
            if not gaps:
                print(f"{ld:9} {n}: khong co khoang nghi >0,25s")
                continue
            g0, g1 = max(gaps, key=lambda x: x[1] - x[0])
            a0 = int((g0 + 0.15) * 16000)
            a1 = int(min(g1 - 0.10, g0 + 4.0) * 16000)
            seg = a[a0:a1]
            if len(seg) < 1600:
                print(f"{ld:9} {n}: khoang nghi qua ngan")
                continue
            e = env_rms(seg)
            rms_db = 20 * np.log10(max(float(np.sqrt(np.mean(seg ** 2))), 1e-12))
            # muc giong: trong 1 dong
            l0 = tl[0]["start"]
            l1 = tl[0]["end"]
            sp = a[int(l0 * 16000):int(l1 * 16000)]
            sp_db = 20 * np.log10(max(float(np.sqrt(np.mean(sp ** 2))), 1e-12))
            scores = sorted(((corr(e, bgm_env[k]), k) for k in bgm_env), reverse=True)
            best = ", ".join(f"{k}={c:+.2f}" for c, k in scores[:3])
            print(f"{ld:9} {n}: spec={want:28} bed_rms={rms_db:6.1f} dB  speech_rms={sp_db:6.1f} dB"
                  f"  | top: {best}")


if __name__ == "__main__":
    main()
