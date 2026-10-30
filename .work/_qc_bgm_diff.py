# -*- coding: utf-8 -*-
"""So master audio cũ/mới theo đúng mốc hồi của từng tập (đọc từ log build)."""
import pathlib
import re
import sys
import wave

import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"


def read(p):
    with wave.open(str(p), "rb") as w:
        n, ch, sr = w.getnframes(), w.getnchannels(), w.getframerate()
        d = np.frombuffer(w.readframes(n), dtype=np.int16).astype(np.float32) / 32768.0
    return (d.reshape(-1, ch) if ch == 2 else d), sr


def acts_from_log(log_text, label):
    """Lấy dòng 'hồi: {...}' đầu tiên SAU khối của label."""
    i = log_text.find(f"---------- {label}")
    if i == -1:
        return None
    m = re.search(r"hồi: \{(.*?)\}", log_text[i:], re.S)
    if not m:
        return None
    out = {}
    for part in m.group(1).split(","):
        k, v = part.split(":")
        k = int(k.strip())
        a, z = v.strip().strip("'").split("–")
        out[k] = (float(a), float(z))
    return out


log = (WORK / "rebuild_bgm_audio.log").read_text(encoding="utf-8")
JOBS = [
    ("T02 VN", WORK / "_cu" / "audio_master_t02.wav.bak_bgm", WORK / "audio_master_t02.wav"),
    ("T07 VN", WORK / "_cu" / "audio_master_t07.wav.bak_bgm", WORK / "audio_master_t07.wav"),
    ("T02 EN", WORK / "_cu" / "audio_master_EN_t02.wav.bak_bgm", WORK / "audio_master_EN_t02.wav"),
]
# hồi nào đã sửa bed
CHANGED = {"T02 VN": {1, 3}, "T07 VN": {3}, "T02 EN": {1, 3}}

for label, old_p, new_p in JOBS:
    if not old_p.exists() or not new_p.exists():
        print(f"--- {label}: thieu file")
        continue
    acts = acts_from_log(log, label)
    if not acts:
        print(f"--- {label}: khong lay duoc moc hoi tu log")
        continue
    a, sr = read(old_p)
    b, _ = read(new_p)
    n = min(len(a), len(b))
    print(f"\n=== {label}  sr={sr} Hz  old={len(a)/sr:.1f}s new={len(b)/sr:.1f}s ===")
    print(f"{'Hoi':<5}{'khoang':<18}{'trang thai':<10}{'tuong quan':>12}{'RMS lech':>11}{'a(gain)':>10}")
    print("-" * 70)
    for act in sorted(acts):
        s, e = acts[act]
        i, j = int(s * sr), min(int(e * sr), n)
        x, y = a[i:j], b[i:j]
        if x.size == 0:
            continue
        rms_x = float(np.sqrt((x ** 2).mean()))
        rms_d = float(np.sqrt(((y - x) ** 2).mean()))
        corr = float((x * y).sum()) / (float(np.sqrt((x * x).sum() * (y * y).sum())) or 1e-12)
        a_opt = float((x * y).sum() / max((x * x).sum(), 1e-12))
        st = "ĐÃ SỬA" if act in CHANGED.get(label, set()) else "giữ"
        print(f"H{act:<4}{f'{s:.1f}-{e:.1f}':<18}{st:<10}{corr:>12.5f}{rms_d:>11.5f}{a_opt:>10.5f}")
    i, j = 0, int(min(22.4, n / sr) * sr)
    x, y = a[i:j], b[i:j]
    corr = float((x * y).sum()) / (float(np.sqrt((x * x).sum() * (y * y).sum())) or 1e-12)
    print(f"intro 0-22.4s (KHONG doi){'':<10}{corr:>12.5f}")
