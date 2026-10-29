#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_sfx2.py — bộ SFX bổ sung (22/10/2026): chuyển cảnh, nhấn chữ, đạo cụ, không khí.

Cùng nguyên tắc với make_sfx.py: tự tổng hợp bằng DSP, không mẫu ngoài, không bản quyền,
tái lập 100% (mọi nhiễu đều có seed). Chỉ GHI CÁC FILE MỚI, không đụng 11 file cũ.

Chạy:  py -3 .work/make_sfx2.py      ->  assets/sfx/*.wav (44,1 kHz mono 16-bit)
"""
import sys
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from make_sfx import SR, band, fade, modal, noise, normalize, write_wav  # noqa: E402


def t_(n):
    return np.arange(n) / SR


def onepole_sweep(x, f_start, f_peak, f_end, peak_at=0.5):
    """Low-pass một cực, tần số cắt quét theo thời gian (tạo cảm giác lướt qua)."""
    n = len(x)
    k = np.linspace(0, 1, n)
    f = np.where(k < peak_at, f_start + (f_peak - f_start) * (k / peak_at),
                 f_peak + (f_end - f_peak) * ((k - peak_at) / (1 - peak_at)))
    a = np.exp(-2 * np.pi * f / SR)
    y = np.zeros(n, np.float32)
    s = 0.0
    for i in range(n):
        s = (1 - a[i]) * x[i] + a[i] * s
        y[i] = s
    return y


def room(x, taps=((0.031, 0.32), (0.057, 0.22), (0.089, 0.14), (0.131, 0.08), (0.19, 0.05))):
    y = x.copy()
    for d, g in taps:
        i = int(d * SR)
        y[i:] += g * x[:len(x) - i]
    return y


def pad_to(x, dur):
    n = int(dur * SR)
    return np.pad(x, (0, max(0, n - len(x))))[:n].astype(np.float32)


# --------------------------------------------------------------- chuyển cảnh
def whoosh():
    """Lướt gió nhẹ — chuyển cảnh, chữ lớn bay vào."""
    n = int(0.9 * SR)
    x = noise(n, 301)
    x = onepole_sweep(x, 250, 3200, 500, peak_at=0.55)
    env = np.sin(np.pi * np.linspace(0, 1, n)) ** 1.6
    return fade((x * env).astype(np.float32), 0.01, 0.15)


def riser():
    """Dâng căng thẳng 2,4 s trước thẻ chuyển hồi."""
    n = int(2.4 * SR)
    t = t_(n)
    f = 110 * 2 ** (2.0 * t / t[-1])                       # 2 quãng tám
    ph = 2 * np.pi * np.cumsum(f) / SR
    tone = 0.5 * np.sin(ph) + 0.25 * np.sin(2 * ph) + 0.12 * np.sin(3.01 * ph)
    nz = onepole_sweep(noise(n, 302), 300, 6000, 7000, peak_at=0.98)
    env = (np.linspace(0, 1, n) ** 2.2).astype(np.float32)
    x = (tone * 0.6 + nz * 0.8) * env
    return fade(x.astype(np.float32), 0.05, 0.03)


def reverse_swell():
    """Tiếng ngược dâng lên (bóng nhập vào nhau, cửa sáng)."""
    n = int(1.8 * SR)
    t = t_(n)
    body = np.exp(-t / 0.5) * (np.sin(2 * np.pi * 220 * t) + 0.5 * np.sin(2 * np.pi * 331 * t)
                                + 0.3 * np.sin(2 * np.pi * 440 * t))
    nz = band(noise(n, 303), 500, 6000) * np.exp(-t / 0.35)
    x = room((0.6 * body + 0.5 * nz).astype(np.float32))
    return fade(x[::-1].copy(), 0.05, 0.02)


# --------------------------------------------------------------- nhấn chữ
def impact():
    """Cú nện trầm điện ảnh — tiết lộ lớn."""
    n = int(2.2 * SR)
    t = t_(n)
    f = 38 + 32 * np.exp(-t / 0.08)
    sub = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.55)
    knock = band(noise(n, 304), 80, 900) * np.exp(-t / 0.05)
    crack = band(noise(n, 305), 1500, 7000) * np.exp(-t / 0.012)
    x = room((1.0 * sub + 0.55 * knock + 0.25 * crack).astype(np.float32),
             ((0.05, 0.3), (0.11, 0.2), (0.19, 0.12), (0.3, 0.07)))
    return fade(x, 0.001, 0.6)


def hit_soft():
    """Nhấn nhẹ cho tiêu đề — thân gỗ trầm + đuôi ngắn."""
    n = int(1.2 * SR)
    t = t_(n)
    x = (np.sin(2 * np.pi * (60 + 30 * np.exp(-t / 0.05)) * t) * np.exp(-t / 0.25)
         + 0.35 * band(noise(n, 306), 120, 1600) * np.exp(-t / 0.04))
    return fade(room(x.astype(np.float32)), 0.001, 0.4)


def ding():
    """Chuông nhỏ trong trẻo — đánh dấu mục/cờ."""
    n = int(1.6 * SR)
    x = modal(n, [(1318, 0.9, 1.0), (2637, 0.45, 0.35), (3952, 0.25, 0.18), (5280, 0.15, 0.08)], seed=31)
    return fade(x, 0.001, 0.4)


def chime_warm():
    """Chuông hoà âm trưởng ấm — lời chào kết."""
    n = int(3.0 * SR)
    x = np.zeros(n, np.float32)
    for k, f in enumerate((523.25, 659.25, 783.99, 1046.5)):
        i = int(k * 0.11 * SR)
        y = modal(n - i, [(f, 1.4, 1.0), (2 * f, 0.6, 0.3), (3 * f, 0.3, 0.12)], seed=40 + k)
        x[i:] += 0.6 * y
    return fade(x, 0.002, 0.8)


def shimmer():
    """Lấp lánh thuỷ tinh — hào quang 'thánh nhân', búp bê sứ, thuật ngữ."""
    n = int(2.2 * SR)
    t = t_(n)
    x = np.zeros(n, np.float32)
    notes = (1760, 2217, 2637, 3520, 2960, 4186)
    for k, f in enumerate(notes):
        i = int(k * 0.12 * SR)
        L = n - i
        tt = t_(L)
        y = np.sin(2 * np.pi * f * tt) * np.exp(-tt / 0.6) * (0.75 + 0.25 * np.sin(2 * np.pi * 6 * tt))
        x[i:] += (0.5 * y).astype(np.float32)
    x += (0.08 * band(noise(n, 307), 6000, 12000) * np.sin(np.pi * t / t[-1])).astype(np.float32)
    return fade(x, 0.01, 0.6)


def pop():
    """Bong bóng 'póp' thân thiện — biểu tượng hiện lên."""
    n = int(0.18 * SR)
    t = t_(n)
    f = 420 + 900 * np.exp(-t / 0.02)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.035)
    return fade(x.astype(np.float32), 0.001, 0.05)


def pulse():
    """Nhịp 'dopamine' — hai cú bass mềm."""
    n = int(1.4 * SR)
    x = np.zeros(n, np.float32)
    for st, g in ((0.0, 1.0), (0.42, 0.8)):
        i = int(st * SR)
        L = int(0.6 * SR)
        tt = t_(L)
        y = np.sin(2 * np.pi * (70 + 60 * np.exp(-tt / 0.04)) * tt) * np.exp(-tt / 0.18)
        x[i:i + L] += (g * y).astype(np.float32)
    return fade(x, 0.002, 0.3)


# --------------------------------------------------------------- đạo cụ
def typewriter():
    """Máy chữ gõ 11 phím — ngày tháng hiện từng ký tự."""
    n = int(1.7 * SR)
    x = np.zeros(n, np.float32)
    rnd = np.random.default_rng(308)
    tt = 0.0
    for k in range(11):
        i = int(tt * SR)
        L = int(0.06 * SR)
        y = modal(L, [(2900, 0.012, 0.6), (4100, 0.008, 0.4)], jitter=0.1, seed=80 + k)
        y += band(noise(L, 400 + k), 1500, 8000) * np.exp(-np.linspace(0, 9, L))
        y += 0.5 * np.sin(2 * np.pi * 180 * t_(L)) * np.exp(-t_(L) / 0.01)
        x[i:i + L] += (rnd.uniform(0.7, 1.0) * y).astype(np.float32)
        tt += float(rnd.uniform(0.09, 0.15))
    return fade(band(x, 120, 11000), 0.001, 0.1)


def notif_ping():
    """Thông báo mạng xã hội — 2 nốt ngắn, mềm."""
    n = int(0.9 * SR)
    x = np.zeros(n, np.float32)
    for st, f in ((0.0, 1046.5), (0.12, 1568.0)):
        i = int(st * SR)
        y = modal(n - i, [(f, 0.35, 1.0), (2 * f, 0.12, 0.2)], seed=int(f))
        x[i:] += 0.6 * y
    return fade(x, 0.001, 0.3)


def stamp_thud():
    """Dấu mộc cao su đóng xuống giấy — 'Bộp'."""
    n = int(0.6 * SR)
    t = t_(n)
    x = (np.sin(2 * np.pi * (95 + 60 * np.exp(-t / 0.015)) * t) * np.exp(-t / 0.07)
         + 0.7 * band(noise(n, 309), 400, 3500) * np.exp(-t / 0.025))
    return fade(room(x.astype(np.float32), ((0.02, 0.2), (0.045, 0.1))), 0.001, 0.15)


def pin_tap():
    """Ghim bấm cắm vào bảng bần."""
    n = int(0.25 * SR)
    t = t_(n)
    x = (0.8 * band(noise(n, 310), 1500, 6000) * np.exp(-t / 0.006)
         + 0.6 * np.sin(2 * np.pi * 240 * t) * np.exp(-t / 0.03))
    return fade(x.astype(np.float32), 0.001, 0.05)


def string_pluck():
    """Gảy dây đỏ (Karplus–Strong) — sợi chỉ nối manh mối."""
    n = int(1.6 * SR)
    p = int(SR / 196)
    buf = noise(p, 311) * 0.8
    x = np.zeros(n, np.float32)
    for i in range(n):
        x[i] = buf[i % p]
        buf[i % p] = 0.996 * 0.5 * (buf[i % p] + buf[(i + 1) % p])
    return fade(band(x, 80, 6000), 0.001, 0.3)


def card_flip():
    """Lật thẻ giấy nhanh — mốc thời gian."""
    n = int(0.22 * SR)
    t = t_(n)
    x = band(noise(n, 312), 1800, 9000) * (np.exp(-t / 0.03) + 0.4 * np.exp(-((t - 0.08) / 0.015) ** 2))
    return fade(x.astype(np.float32), 0.001, 0.05)


def pen_strike():
    """Gạch bút qua giấy — 'xoẹt'."""
    n = int(0.45 * SR)
    x = onepole_sweep(band(noise(n, 313), 1200, 9000), 2000, 7000, 2500, peak_at=0.4)
    env = np.sin(np.pi * np.linspace(0, 1, n)) ** 0.8
    return fade((x * env).astype(np.float32), 0.005, 0.05)


def coin_clink():
    """Đồng xu leng keng — 3 đồng rơi."""
    n = int(1.2 * SR)
    x = np.zeros(n, np.float32)
    for k, st in enumerate((0.0, 0.14, 0.31)):
        i = int(st * SR)
        y = modal(n - i, [(3100, 0.25, 1.0), (4680, 0.18, 0.6), (6900, 0.1, 0.35), (8400, 0.06, 0.2)],
                  jitter=0.08, seed=90 + k)
        x[i:] += (0.8 - 0.2 * k) * y
    return fade(x, 0.001, 0.3)


def switch_on():
    """Công tắc đèn rọi 'cạch' + tiếng ù dâng nhẹ."""
    n = int(1.4 * SR)
    t = t_(n)
    clk = band(noise(n, 314), 1200, 7000) * np.exp(-t / 0.005)
    hum = (np.sin(2 * np.pi * 120 * t) + 0.4 * np.sin(2 * np.pi * 240 * t)) * (1 - np.exp(-t / 0.2)) * np.exp(-t / 0.8)
    return fade((clk + 0.15 * hum).astype(np.float32), 0.001, 0.4)


def door_creak():
    """Bản lề cửa kẽo kẹt (stick–slip) — cửa lồng, cửa nhà hồng."""
    n = int(1.5 * SR)
    t = t_(n)
    f = 260 + 140 * np.sin(np.pi * t / t[-1]) + 20 * np.sin(2 * np.pi * 3.3 * t)
    ph = 2 * np.pi * np.cumsum(f) / SR
    saw = 2 * ((ph / (2 * np.pi)) % 1.0) - 1
    rnd = np.random.default_rng(315)
    grit = np.repeat(rnd.uniform(0.3, 1.0, int(n / 900) + 1), 900)[:n]
    x = band(saw * grit, 300, 4000) * np.sin(np.pi * np.linspace(0, 1, n)) ** 0.5
    return fade(room(x.astype(np.float32)), 0.02, 0.2)


def footsteps():
    """Ba bước chân chậm trên sàn — 'cô ấy tự bước vào'."""
    n = int(1.9 * SR)
    x = np.zeros(n, np.float32)
    for k, st in enumerate((0.0, 0.6, 1.2)):
        i = int(st * SR)
        L = int(0.35 * SR)
        tt = t_(L)
        y = np.sin(2 * np.pi * (85 + 10 * k) * tt) * np.exp(-tt / 0.05)
        y += 0.5 * band(noise(L, 316 + k), 300, 3000) * np.exp(-tt / 0.02)
        x[i:i + L] += (0.9 - 0.1 * k) * y.astype(np.float32)
    return fade(room(x, ((0.03, 0.2), (0.07, 0.1))), 0.001, 0.2)


def tv_off():
    """Màn hình máy tính tắt — 'tít' cao rơi xuống + cạch."""
    n = int(0.8 * SR)
    t = t_(n)
    f = 7800 * np.exp(-t / 0.12) + 200
    x = 0.4 * np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t / 0.25)
    x += 0.6 * band(noise(n, 318), 800, 5000) * np.exp(-t / 0.01)
    return fade(x.astype(np.float32), 0.001, 0.2)


# --------------------------------------------------------------- không khí
def rain_loop():
    """Mưa đêm 12 s (lặp được) — nền Hồi 1 quanh ngôi nhà."""
    n = int(12.0 * SR)
    x = 0.5 * band(noise(n, 319), 400, 9000)
    x += 0.25 * band(noise(n, 320), 80, 400)
    rnd = np.random.default_rng(321)
    for _ in range(900):
        i = int(rnd.uniform(0, n - 400))
        L = int(rnd.uniform(80, 300))
        x[i:i + L] += (rnd.uniform(0.2, 0.9) * band(noise(L, int(rnd.integers(1e6))), 2000, 10000)
                       * np.exp(-np.linspace(0, 7, L))).astype(np.float32)
    k = int(0.5 * SR)                                        # nối vòng không vấp
    x[:k] = x[:k] * np.linspace(0, 1, k) + x[-k:] * np.linspace(1, 0, k)
    return x[:-k].astype(np.float32)


def clock_tick():
    """Đồng hồ tích tắc 5 s — đếm năm tháng."""
    n = int(5.0 * SR)
    x = np.zeros(n, np.float32)
    for k in range(10):
        i = int((0.05 + k * 0.5) * SR)
        f = 2400 if k % 2 == 0 else 1900
        L = int(0.05 * SR)
        y = modal(L, [(f, 0.01, 1.0), (f * 1.6, 0.006, 0.4)], seed=120 + k)
        x[i:i + L] += y
    return fade(x, 0.001, 0.1)


def birds():
    """Chim sớm — bình minh (FM chirp)."""
    n = int(4.0 * SR)
    x = np.zeros(n, np.float32)
    rnd = np.random.default_rng(322)
    for k in range(9):
        i = int(rnd.uniform(0, 3.4) * SR)
        L = int(rnd.uniform(0.08, 0.22) * SR)
        tt = t_(L)
        f0 = rnd.uniform(2800, 4200)
        f = f0 + rnd.uniform(-1200, 1200) * tt / tt[-1] + 300 * np.sin(2 * np.pi * rnd.uniform(18, 35) * tt)
        y = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.sin(np.pi * tt / tt[-1])
        x[i:i + L] += (rnd.uniform(0.4, 1.0) * y).astype(np.float32)
    return fade(room(x), 0.01, 0.3)


BUILDERS = [
    ("whoosh.wav", whoosh), ("riser.wav", riser), ("reverse_swell.wav", reverse_swell),
    ("impact.wav", impact), ("hit_soft.wav", hit_soft), ("ding.wav", ding), ("chime_warm.wav", chime_warm),
    ("shimmer.wav", shimmer), ("pop.wav", pop), ("pulse.wav", pulse),
    ("typewriter.wav", typewriter), ("notif_ping.wav", notif_ping), ("stamp_thud.wav", stamp_thud),
    ("pin_tap.wav", pin_tap), ("string_pluck.wav", string_pluck), ("card_flip.wav", card_flip),
    ("pen_strike.wav", pen_strike), ("coin_clink.wav", coin_clink), ("switch_on.wav", switch_on),
    ("door_creak.wav", door_creak), ("footsteps.wav", footsteps), ("tv_off.wav", tv_off),
    ("rain_loop.wav", rain_loop), ("clock_tick.wav", clock_tick), ("birds.wav", birds),
]


def main():
    for name, fn in BUILDERS:
        x = normalize(fn())
        path, dur = write_wav(name, x)
        print(f"  {name:<20} {dur:5.2f}s  rms={float(np.sqrt((x ** 2).mean())):.4f}")


if __name__ == "__main__":
    main()
