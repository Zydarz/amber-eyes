#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_sfx.py — tổng hợp hiệu ứng âm thanh (SFX) cho Tập 01.

Vì sao tự tổng hợp chứ không tải file mẫu bên ngoài:
  1) không vướng bản quyền — tiêu chuẩn kênh đòi hỏi provenance sạch;
  2) tái lập được 100% bằng code (đúng cách đã làm tiếng "Tách");
  3) không tốn tiền, không phụ thuộc mạng.

Kỹ thuật DSP dùng ở đây:
  - modal synthesis: cộng các mode tắt dần (f, decay, amp) cho tiếng gõ gỗ / kim loại;
  - nhiễu lọc băng kiểu FFT (zero-phase) cho tiếng giấy, bàn phím, tĩnh;
  - tích pha tần số để quét (wail) cho còi xe cảnh sát;
  - envelope nhiều nhịp cho tiếng bộ đàm rè.

Chạy:  py -3 .work/make_sfx.py
Kết quả: assets/sfx/*.wav  (44 100 Hz, mono, 16-bit PCM)
"""
import wave
from pathlib import Path

import numpy as np

ROOT = Path(r"D:\TEST\Gax\Audi")
OUT = ROOT / "assets" / "sfx"
SR = 44100


# ------------------------------------------------------------------ tiện ích
def noise(n, seed):
    return np.random.default_rng(seed).standard_normal(n).astype(np.float32)


def fade(x, fi=0.01, fo=0.08):
    """Fade vào/ra để không bị click ở đầu-cuối."""
    n = len(x)
    a = max(1, int(fi * SR))
    b = max(1, int(fo * SR))
    if a * 2 < n:
        x[:a] *= np.linspace(0, 1, a).astype(np.float32)
    if b * 2 < n:
        x[-b:] *= np.linspace(1, 0, b).astype(np.float32)
    return x


def band(x, lo, hi):
    """Lọc băng bằng FFT (zero-phase). Đệm trước/sau để tránh vòng lặp."""
    n = len(x)
    pad = n
    y = np.pad(x, pad)
    Y = np.fft.rfft(y)
    f = np.fft.rfftfreq(len(y), 1.0 / SR)
    Y[(f < lo) | (f > hi)] = 0.0
    return np.fft.irfft(Y, n=len(y))[pad:pad + n].astype(np.float32)


def modal(n, spec, jitter=0.0, seed=0):
    """Tổng các mode tắt dần. spec = [(freq, decay_s, amp), ...]."""
    t = np.arange(n) / SR
    out = np.zeros(n, np.float32)
    for k, (f, dec, a) in enumerate(spec):
        r = np.random.default_rng(seed * 100 + k)
        fj = f * (1.0 + jitter * (r.random() - 0.5))
        ph = r.uniform(0, 2 * np.pi)
        out += (a * np.exp(-t / dec) * np.sin(2 * np.pi * fj * t + ph)).astype(np.float32)
    return out


def normalize(x, peak=0.92):
    m = float(np.abs(x).max())
    if m > 0:
        x = x * (peak / m)
    return x.astype(np.float32)


def resonate(x, f, q):
    """Cộng hưởng 2 cực (mô phỏng formant của người nói)."""
    w = 2 * np.pi * f / SR
    r = float(np.exp(-w / (2 * q)))
    a1 = 2 * r * np.cos(w)
    a2 = -r * r
    g = (1 - r) * np.sqrt(1 - 2 * r * np.cos(2 * w) + r * r)
    y = np.zeros(len(x), np.float32)
    y1 = y2 = 0.0
    for i in range(len(x)):
        v = float(x[i]) + a1 * y1 + a2 * y2
        y[i] = v
        y2 = y1
        y1 = v
    return (y * g).astype(np.float32)


def write_wav(name, x):
    OUT.mkdir(parents=True, exist_ok=True)
    pcm = np.clip(x, -1.0, 1.0)
    data = (pcm * 32767.0).astype("<i2").tobytes()
    path = OUT / name
    with wave.open(str(path), "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(data)
    return path, len(pcm) / SR


# ------------------------------------------------------------------- âm thanh
def gavel():
    """Búa tòa án gõ 'Cốp' — gỗ, tiếng khô, vang vọng."""
    n = int(1.8 * SR)
    body = modal(n, [(148, 0.18, 1.0), (293, 0.13, 0.7), (437, 0.09, 0.5),
                      (655, 0.06, 0.35), (980, 0.04, 0.22), (1520, 0.025, 0.12)],
                 seed=1)
    click = band(noise(int(0.005 * SR), 11), 900, 5000)
    x = body.copy()
    x[:len(click)] += 1.1 * click
    x = band(x, 90, 6500)
    # vang vọng: vài bản sao lệch nhịp (room tail)
    for d, g in [(0.026, 0.35), (0.049, 0.24), (0.077, 0.15), (0.112, 0.09), (0.155, 0.05)]:
        i = int(d * SR)
        x[i:] += g * body[:n - i]
    return fade(x, 0.002, 0.35)


def lock_door():
    """Khóa cửa sắt 'Cạch' — kim loại, lắc nhẹ."""
    n = int(1.3 * SR)
    main = modal(n, [(2180, 0.26, 0.7), (3320, 0.19, 0.5), (4610, 0.13, 0.35),
                      (6270, 0.09, 0.22), (8100, 0.06, 0.12)], jitter=0.05, seed=2)
    cl = band(noise(int(0.006 * SR), 12), 2000, 9000)
    x = main.copy()
    x[:len(cl)] += 1.2 * cl
    d = int(0.14 * SR)
    x[d:] += 0.45 * main[:n - d]                     # lắc lần hai
    t = np.arange(n) / SR
    x += (0.5 * np.exp(-t / 0.05) * np.sin(2 * np.pi * 155 * t)).astype(np.float32)
    x = band(x, 100, 12000)
    return fade(x, 0.001, 0.30)


def chains():
    """Xiềng xích, kim loại va chạm nhẹ."""
    n = int(2.6 * SR)
    x = np.zeros(n, np.float32)
    events = [(0.00, 1.0), (0.38, 0.62), (0.63, 0.80), (1.24, 0.50),
              (1.52, 0.70), (2.02, 0.42)]
    for k, (st, g) in enumerate(events):
        i = int(st * SR)
        L = int(0.6 * SR)
        y = modal(L, [(2600, 0.10, 0.5), (3900, 0.075, 0.35), (5400, 0.05, 0.25),
                      (7100, 0.035, 0.15), (9300, 0.02, 0.08)],
                  jitter=0.12, seed=3 + k)
        tick = band(noise(int(0.003 * SR), 20 + k), 3000, 11000)
        y[:len(tick)] += 0.8 * tick
        y = band(y, 800, 13000)
        m = min(L, n - i)
        x[i:i + m] += (g * y[:m]).astype(np.float32)
    return fade(x, 0.002, 0.40)


def keyboard_night():
    """Bàn phím gõ lạch cạch trong đêm — gõ thành cụm."""
    n = int(2.6 * SR)
    x = np.zeros(n, np.float32)
    rnd = np.random.default_rng(31)
    times = []
    t = 0.0
    for _ in range(5):
        for _j in range(int(rnd.integers(3, 7))):
            times.append(t)
            t += float(rnd.uniform(0.075, 0.16))
        t += float(rnd.uniform(0.25, 0.75))
    for k, st in enumerate(times):
        i = int(st * SR)
        L = int(0.05 * SR)
        if i + L > n:
            break
        y = band(noise(L, 40 + k), 2200, 8000)
        tt = np.arange(L) / SR
        y += (0.5 * np.exp(-tt / 0.012) * np.sin(2 * np.pi * (1500 + 137 * k) * tt)).astype(np.float32)
        x[i:i + L] += ((0.55 + 0.45 * rnd.random()) * y).astype(np.float32)
    x = band(x, 600, 11000)
    return fade(x, 0.003, 0.15)


def paper_rustle():
    """Lật giấy hồ sơ sột soạt.

    Giấy thật = tiếng cào rất cao, rất nhanh, KHÔNG có thân trầm.
    Bản cũ lọc 1,5–8 kHz + sóng bao hình chậm => nghe như lắc bình thuốc.
    Bản này: nền rất nhỏ ở 2,5–9,5 kHz + 38 tiếng "tick" giấy cào rời rạc.
    """
    n = int(0.95 * SR)
    x = (0.35 * band(noise(n, 51), 2500, 9500)).astype(np.float32)
    rnd = np.random.default_rng(52)
    for k in range(38):
        i = int(rnd.uniform(0, n - 2500))
        L = int(rnd.uniform(300, 1800))
        tk = band(noise(L, 60 + k), 3500, 11000)
        e = np.exp(-np.linspace(0, 6, L)).astype(np.float32)
        x[i:i + L] += (rnd.uniform(0.5, 1.0) * tk * e).astype(np.float32)
    # 3 "phớt" giấy lớn
    for k, st in enumerate([0.05, 0.32, 0.58]):
        i = int(st * SR)
        L = int(0.10 * SR)
        fl = band(noise(L, 200 + k), 1200, 6000)
        e = np.exp(-np.linspace(0, 5, L)).astype(np.float32)
        x[i:i + L] += (0.7 * fl * e).astype(np.float32)
    return fade(x, 0.003, 0.10)


def folder_close():
    """Gấp hồ sơ giấy 'Bụp' — vỏ giấy, KHÔNG có tiếng rầm trầm (tránh nghe như sập kim loại)."""
    n = int(0.45 * SR)
    t = np.arange(n) / SR
    slap = band(noise(n, 71), 700, 3200)
    env = np.exp(-t / 0.055).astype(np.float32)
    a = int(0.004 * SR)
    env[:a] *= np.linspace(0, 1, a).astype(np.float32)
    x = (slap * env).astype(np.float32)
    # tiếng crinkle kéo dài khi gấp
    rnd = np.random.default_rng(73)
    for k in range(14):
        i = int(rnd.uniform(0, n - 1200))
        L = int(rnd.uniform(250, 900))
        tk = band(noise(L, 210 + k), 3000, 10000)
        x[i:i + L] += (0.45 * rnd.random() * tk * np.exp(-np.linspace(0, 6, L))).astype(np.float32)
    # tiếng "snap" nhẹ
    sn = band(noise(int(0.012 * SR), 72), 1800, 8000)
    x[:len(sn)] += (0.35 * sn * np.exp(-np.linspace(0, 5, len(sn)))).astype(np.float32)
    return fade(x, 0.002, 0.08)


def police_siren_distant():
    """Còi xe cảnh sát vọng rất xa — wail lên rồi xuống, nghe ù."""
    dur = 2.8
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 560 + 300 * (0.5 - 0.5 * np.cos(2 * np.pi * t / dur))
    f += 7 * np.sin(2 * np.pi * 3.1 * t)
    phase = 2 * np.pi * np.cumsum(f) / SR
    x = np.sin(phase).astype(np.float32)
    x = band(x, 200, 1500)
    x += (0.05 * band(noise(n, 81), 300, 1200)).astype(np.float32)
    env = np.ones(n, np.float32)
    a = int(0.35 * SR)
    env[:a] *= np.linspace(0, 1, a).astype(np.float32)
    b = int(0.9 * SR)
    env[-b:] *= np.linspace(1, 0, b).astype(np.float32)
    x = x * env
    return fade(x, 0.01, 0.30)


def door_knock():
    """Gõ cửa dồn dập trong đêm — xa, ù. 3 tiếng sát nhau, xong trước khi lời mở đầu."""
    n = int(1.6 * SR)
    x = np.zeros(n, np.float32)
    for k, (st, g) in enumerate([(0.0, 1.0), (0.40, 0.82), (0.80, 0.64)]):
        i = int(st * SR)
        L = int(0.55 * SR)
        t = np.arange(L) / SR
        y = (0.9 * np.exp(-t / 0.085) * np.sin(2 * np.pi * (108 + 8 * k) * t)).astype(np.float32)
        y += (0.6 * np.exp(-t / 0.05) * np.sin(2 * np.pi * (205 + 12 * k) * t)).astype(np.float32)
        y += (0.3 * np.exp(-t / 0.025) * np.sin(2 * np.pi * 340 * t)).astype(np.float32)
        ct = band(noise(int(0.012 * SR), 90 + k), 600, 2600)
        y[:len(ct)] += 0.55 * ct
        m = min(L, n - i)
        x[i:i + m] += (g * y[:m]).astype(np.float32)
    x = band(x, 70, 3000)
    return fade(x, 0.002, 0.20)


def radio_chatter():
    """Bộ đàm cảnh sát rè nhẹ, rồi chuyển sang tiếng mở cửa phòng thẩm vấn.

    "Rè" = mơ hồ, không thành lời. Để nghe ra giọng người thì cộng hưởng
    formant (600 Hz + 1300 Hz) thay vì chỉ lọc băng — nếu không chỉ là tĩnh.
    """
    dur = 3.2
    n = int(dur * SR)
    rnd = np.random.default_rng(101)
    x = (0.05 * band(noise(n, 102), 1200, 5000)).astype(np.float32)   # vỏ tĩnh
    voice = band(noise(n, 103), 300, 1900)                            # giọng mơ hồ
    voice = (0.7 * resonate(voice, 600, 5)
             + 0.5 * resonate(voice, 1300, 7)
             + 0.25 * voice).astype(np.float32)
    env = np.zeros(n, np.float32)
    tt = 0.12
    while tt < 2.5:
        dur_s = float(rnd.uniform(0.09, 0.24))
        i = int(tt * SR)
        L = int(dur_s * SR)
        e = (np.sin(np.pi * np.linspace(0, 1, L)) ** 0.7).astype(np.float32)
        env[i:i + L] = np.maximum(env[i:i + L], float(rnd.uniform(0.6, 1.0)) * e)
        tt += dur_s + float(rnd.uniform(0.02, 0.10))
    x += (1.1 * voice * env).astype(np.float32)
    # tiếng mở cửa ở cuối
    ci = int(2.5 * SR)
    L = int(0.6 * SR)
    ct = np.arange(L) / SR
    cr = band(noise(L, 104), 700, 3200)
    cr *= (0.5 + 0.5 * np.sin(2 * np.pi * 11 * ct)).astype(np.float32)
    cr *= np.exp(-ct / 0.3).astype(np.float32)
    x[ci:ci + L] += (0.45 * cr).astype(np.float32)
    lk = band(noise(int(0.008 * SR), 105), 1500, 6000)
    j = ci + int(0.5 * SR)
    x[j:j + len(lk)] += (0.6 * lk).astype(np.float32)
    sq = band(noise(int(0.05 * SR), 106), 900, 4200)                   # tạp mở mic
    x[:len(sq)] += (0.6 * sq * np.exp(-np.linspace(0, 4, len(sq)))).astype(np.float32)
    x = band(x, 250, 6000)
    return fade(x, 0.004, 0.10)


def heart_beep():
    """Máy đo nhịp tim bệnh viện kêu 'Bíp... Bíp...'."""
    n = int(6.0 * SR)
    x = np.zeros(n, np.float32)
    f = 1040.0

    def beep(start, dur=0.085, g=1.0):
        i = int(start * SR)
        L = int(dur * SR)
        t = np.arange(L) / SR
        y = np.sin(2 * np.pi * f * t) + 0.12 * np.sin(2 * np.pi * 2 * f * t)
        y *= (np.hanning(L) ** 0.35).astype(np.float32)
        x[i:i + L] += (g * y).astype(np.float32)

    for k, s in enumerate([0.0, 0.26, 1.05, 1.31, 2.15, 2.41, 3.30, 3.56, 4.45, 4.71]):
        beep(s, g=1.0 if k % 2 == 0 else 0.85)
    return fade(x, 0.002, 0.40)


def heartbeat_slow():
    """Nhịp tim đập chậm (Hồi 4) — trầm, dưới nền violin."""
    n = int(8.0 * SR)
    x = np.zeros(n, np.float32)
    for k in range(8):
        st = 0.4 + k * 1.0
        for off, g in [(0.0, 1.0), (0.33, 0.62)]:
            i = int((st + off) * SR)
            L = int(0.5 * SR)
            t = np.arange(L) / SR
            y = (np.exp(-t / 0.13) * np.sin(2 * np.pi * 52 * t)).astype(np.float32)
            y += (0.5 * np.exp(-t / 0.08) * np.sin(2 * np.pi * 78 * t)).astype(np.float32)
            y += (0.15 * band(noise(L, 120 + int(st)), 60, 180)).astype(np.float32)
            m = min(L, n - i)
            if m > 0:
                x[i:i + m] += (g * y[:m]).astype(np.float32)
    x = band(x, 30, 260)
    return fade(x, 0.05, 0.60)


# ---------------------------------------------------------------------- main
BUILDERS = [
    ("gavel.wav", gavel),
    ("lock_door.wav", lock_door),
    ("chains.wav", chains),
    ("keyboard_night.wav", keyboard_night),
    ("paper_rustle.wav", paper_rustle),
    ("folder_close.wav", folder_close),
    ("police_siren_distant.wav", police_siren_distant),
    ("door_knock.wav", door_knock),
    ("radio_chatter.wav", radio_chatter),
    ("heart_beep.wav", heart_beep),
    ("heartbeat_slow.wav", heartbeat_slow),
]


def main():
    print(f"ghi vao {OUT}")
    for name, fn in BUILDERS:
        x = normalize(fn())
        path, dur = write_wav(name, x)
        rms = float(np.sqrt((x ** 2).mean()))
        print(f"  {name:<28} {dur:>5.2f}s  peak={np.abs(x).max():.3f}  rms={rms:.4f}"
              f"  ({path.stat().st_size/1024:.0f} KB)")


if __name__ == "__main__":
    main()
