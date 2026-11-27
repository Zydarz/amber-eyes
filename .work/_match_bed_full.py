#!/ coding: utf-8 -*-
"""Tim BGM that 14 clip dang dung: tuong quan envelope CUA CA BED (nhung lien tuc).

Y tuong: BGM duoc tile lap lien tuc roi duck theo giong. Trong cac khoang nghi,
tieng giong = 0 => envelope cua clip = envelope cua BGM (nhung, co gain).
=> So sanh envelope cua CA DOAN GIOI HANH voi tung file BGM da tile, dung toan bo
khung thoi gian (khong chi 1 doan) => tinh hieu chinh xac cao.
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


def decode(path, sr=16000):
    raw = subprocess.run([FF, "-v", "error", "-i", str(path), "-ar", str(sr), "-ac", "1",
                          "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def env_db(a, sr=16000, win=0.20):
    n = int(win * sr)
    out = []
    for i in range(0, len(a) - n + 1, n):
        seg = a[i:i + n]
        r = float(np.sqrt(np.mean(seg ** 2)))
        out.append(20 * np.log10(max(r, 1e-9)))
    return np.array(out)


def tile_env(env, total_len):
    reps = int(np.ceil(total_len / len(env))) + 1
    return np.tile(env, reps)[:total_len]


def corr_on_mask(x, y, mask):
    m = mask & np.isfinite(x) & np.isfinite(y)
    if m.sum() < 10:
        return 0.0, 0
    xa, ya = x[m], y[m]
    xa = xa - xa.mean()
    ya = ya - ya.mean()
    if np.std(xa) < 1e-9 or np.std(ya) < 1e-9:
        return 0.0, int(m.sum())
    return float(np.corrcoef(xa, ya)[0, 1]), int(m.sum())


def main():
    bgms = sorted((ROOT / "assets" / "bgm").glob("*.mp3"))
    bgm_env = {b.name: env_db(decode(b)) for b in bgms}

    for ld in ["Tap04", "Tap04_EN", "Tap04_JA"]:
        for n in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
            d = ROOT / "02_SAN_XUAT" / "TIKTOK" / ld
            mp3 = d / f"{n}_master_audio.mp3"
            tl = json.loads((d / f"timeline_{n.lower()}.json").read_text(encoding="utf-8"))
            e = env_db(decode(mp3))
            # mask = khung khong co giong (nhin theo khoang nghi giua cac cau)
            mask = np.zeros(len(e), dtype=bool)
            for i in range(len(tl) - 1):
                g0, g1 = tl[i]["end"], tl[i + 1]["start"]
                a = int(g0 / 0.20)
                b = int(g1 / 0.20)
                if b > a:
                    mask[a:min(b, len(e))] = True
            # them 0.4s dau/cuoi file
            mask[:2] = True
            mask[-2:] = True
            if mask.sum() < 10:
                print(f"{ld:9} {n}: khong du khung nghi ({mask.sum()})")
                continue
            scores = []
            for k, be in bgm_env.items():
                t = tile_env(be, len(e))
                c, cnt = corr_on_mask(e, t, mask)
                scores.append((c, k))
            scores.sort(reverse=True)
            top = ", ".join(f"{k}={c:+.3f}" for c, k in scores[:3])
            print(f"{ld:9} {n}: {mask.sum():3} khung nghi | {top}")


if __name__ == "__main__":
    main()
