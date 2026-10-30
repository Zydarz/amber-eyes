#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""make_sfx3.py — bộ âm thanh Tập 02: nền môi trường + tiếng động thật hơn (22/10/2026).

Phản hồi Tập 01: SFX "nhàm chán, ít, không thấy chân thật". Đo lại Tập 01: 14 tiếng trong 19 phút
(~1 tiếng / 80 s), tất cả mono, khô, vang giả bằng 5 tiếng dội — và KHÔNG có nền môi trường, nên giữa
các câu chỉ có nhạc. Bộ này sửa ba chỗ:
  1. NỀN MÔI TRƯỜNG (amb_*): chạy liên tục dưới lời theo cảnh — gió tuyết, phòng thẩm vấn, tầng hầm…
     Đây là thứ làm người nghe "ở trong" cảnh. Dài 40 s, nối vòng được.
  2. TIẾNG ĐỘNG (fx_*): stereo, có vị trí trái/phải, nhiều lớp (thân + ma sát + cộng hưởng).
  3. VANG THẬT: tích chập với đáp ứng xung tổng hợp (phòng nhỏ / phòng vừa / sảnh lớn / ngoài trời).
Không dùng mẫu ngoài, mọi nhiễu có seed → tái lập 100%, không vướng bản quyền.

Chạy:  py -3 .work/make_sfx3.py            -> assets/sfx/t2/*.wav (44,1 kHz STEREO 16-bit)
       py -3 .work/make_sfx3.py --demo     -> thêm 02_SAN_XUAT/Tap02/thu_am/demo_sfx_tap02.mp3
"""
import json
import sys
import wave
from pathlib import Path

import numpy as np
from scipy.signal import butter, fftconvolve, sosfilt

SR = 44100
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "sfx" / "t2"
RNG = np.random.default_rng


# ------------------------------------------------------------------ nền tảng
def t_(dur):
    return np.arange(int(dur * SR)) / SR


def white(dur, seed):
    return RNG(seed).standard_normal(int(dur * SR)).astype(np.float32)


def pink(dur, seed):
    n = int(dur * SR)
    X = np.fft.rfft(RNG(seed).standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR)
    X /= np.sqrt(np.maximum(f, 20))
    x = np.fft.irfft(X, n)
    return (x / np.abs(x).max()).astype(np.float32)


def brown(dur, seed):
    x = np.cumsum(RNG(seed).standard_normal(int(dur * SR)))
    x = hp(x, 15)
    return (x / np.abs(x).max()).astype(np.float32)


def _f(x, kind, f, order=2):
    sos = butter(order, f, kind, fs=SR, output="sos")
    return sosfilt(sos, x).astype(np.float32)


def lp(x, f, o=2):
    return _f(x, "lowpass", f, o)


def hp(x, f, o=2):
    return _f(x, "highpass", f, o)


def bp(x, lo, hi, o=2):
    return _f(x, "bandpass", [lo, hi], o)


def smooth_rand(dur, rate, seed, lo=0.0, hi=1.0):
    """Đường cong ngẫu nhiên mượt (gió giật, rung nhẹ)."""
    n = int(dur * SR)
    k = max(2, int(dur * rate) + 2)
    pts = RNG(seed).uniform(lo, hi, k)
    return np.interp(np.linspace(0, k - 1, n), np.arange(k), pts).astype(np.float32)


def env_exp(dur, tau, attack=0.002):
    t = t_(dur)
    e = np.exp(-t / tau)
    a = int(attack * SR)
    if a:
        e[:a] *= np.linspace(0, 1, a)
    return e.astype(np.float32)


def pad(x, dur):
    n = int(dur * SR)
    return np.pad(x, (0, max(0, n - len(x))))[:n].astype(np.float32)


def place(dst, x, t, g=1.0):
    i = int(t * SR)
    if i >= len(dst):
        return
    j = min(len(dst), i + len(x))
    dst[i:j] += g * x[: j - i]


def norm(x, peak=0.89):
    m = np.abs(x).max()
    return (x * (peak / m)).astype(np.float32) if m > 0 else x


def pan(x, p):
    """p: -1 trái … +1 phải, công suất không đổi → stereo (n, 2)."""
    a = (p + 1) * np.pi / 4
    return np.stack([x * np.cos(a), x * np.sin(a)], 1).astype(np.float32)


def stereo_wide(dur, gen, seed):
    """Hai kênh từ hai seed khác nhau → nền rộng, tự nhiên."""
    return np.stack([gen(dur, seed), gen(dur, seed + 7)], 1).astype(np.float32)


def ir(rt, seed, bright=6000, pre=0.012):
    """Đáp ứng xung tổng hợp: tiếng dội sớm thưa + đuôi nhiễu tắt dần, sáng ở đầu, tối ở cuối."""
    n = int((rt + pre) * SR)
    out = np.zeros((n, 2), np.float32)
    for c in range(2):
        r = RNG(seed + c)
        tail = r.standard_normal(n).astype(np.float32) * np.exp(-np.arange(n) / SR * 6.9 / rt)
        tail = 0.5 * lp(tail, bright) + 0.5 * lp(tail, bright / 4)
        tail[: int(pre * SR)] = 0
        for _ in range(8):                                     # phản xạ sớm
            d = int(r.uniform(pre, pre + 0.06) * SR)
            tail[d] += r.uniform(0.3, 0.8) * (1 if r.random() > 0.5 else -1)
        out[:, c] = tail
    return out / np.abs(out).max()


ROOMS = {"small": (0.45, 3), "medium": (0.9, 5), "hall": (1.9, 11), "outdoor": (0.25, 17)}


def verb(x, room, wet):
    """x mono hoặc stereo → stereo có vang."""
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    rt, seed = ROOMS[room]
    h = ir(rt, seed, bright=3500 if room == "outdoor" else 6000)
    y = np.stack([fftconvolve(x[:, c], h[:, c])[: len(x) + len(h) - 1] for c in range(2)], 1)
    dry = np.pad(x, ((0, len(y) - len(x)), (0, 0)))
    y = y / (np.abs(y).max() + 1e-9) * np.abs(x).max()
    return ((1 - wet) * dry + wet * y).astype(np.float32)


def loopable(x, xf=2.0):
    """Đuôi hoà vào đầu → lặp không thấy mối nối."""
    n = int(xf * SR)
    a = np.linspace(0, 1, n)[:, None] if x.ndim == 2 else np.linspace(0, 1, n)
    head, tail = x[:n].copy(), x[-n:]
    x = x[:-n].copy()
    x[:n] = head * a + tail * (1 - a)
    return x


def write(name, x):
    OUT.mkdir(parents=True, exist_ok=True)
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    x = norm(x)
    pcm = (np.clip(x, -1, 1) * 32767).astype("<i2")
    with wave.open(str(OUT / name), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes(pcm.tobytes())


# ------------------------------------------------------------------ hạt (grain) dùng chung
def grains(dur, rate, seed, lo, hi, glen=(0.002, 0.009), amp=(0.3, 1.0)):
    """Mưa hạt nhiễu ngắn — nền của tiếng tuyết lạo xạo, lửa tí tách, giấy sột soạt."""
    r = RNG(seed)
    x = np.zeros(int(dur * SR), np.float32)
    for _ in range(int(dur * rate)):
        g = r.uniform(*glen)
        s = bp(white(g + 0.01, int(r.integers(1e9)))[: int(g * SR)], lo, hi) * np.hanning(int(g * SR))
        place(x, s, r.uniform(0, dur - g), r.uniform(*amp))
    return x


def modes(dur, freqs, taus, amps, seed=0):
    """Cộng hưởng kim loại / gốm / gỗ: tổng các dao động tắt dần, hơi lệch tần."""
    t = t_(dur)
    r = RNG(seed)
    x = np.zeros_like(t)
    for f, tau, a in zip(freqs, taus, amps):
        x += a * np.sin(2 * np.pi * f * r.uniform(0.995, 1.005) * t + r.uniform(0, 6.28)) * np.exp(-t / tau)
    return x.astype(np.float32)


# ================================================================== NỀN MÔI TRƯỜNG (40 s, lặp được)
AMB = 42.0


def amb_winter_wind():
    """Gió tuyết ngoài trời: nhiễu hồng lọc dải, tâm dải và biên độ trôi theo cơn giật."""
    out = []
    for c, seed in enumerate((11, 12)):
        x = pink(AMB, seed)
        gust = smooth_rand(AMB, 0.25, seed + 1, 0.15, 1.0) ** 2
        lowp = lp(x, 500) * (0.6 + 0.4 * gust)
        whistle = bp(x, 700, 1600) * gust ** 1.5 * 0.5
        hiss = hp(white(AMB, seed + 3), 5000) * 0.03
        out.append(lowp + whistle + hiss)
    return loopable(np.stack(out, 1))


def amb_airbase():
    """Căn cứ không quân đêm tuyết: gió + động cơ phản lực rất xa vọng lên rồi tắt."""
    x = amb_winter_wind() * 0.8
    n = len(x)
    jet = lp(brown(n / SR, 21), 260) * 0.0
    t = np.arange(n) / SR
    for t0 in (6.0, 26.0):
        swell = np.exp(-((t - t0 - 5) / 3.2) ** 2)
        roar = lp(brown(n / SR, int(t0)), 300) + 0.3 * bp(pink(n / SR, int(t0) + 1), 900, 2500)
        jet = jet + roar * swell
    return (x + 0.5 * np.stack([jet, jet * 0.9], 1)).astype(np.float32)


def amb_interrogation():
    """Phòng thẩm vấn: đèn huỳnh quang 120 Hz rè + máy lạnh + phòng nhỏ dội."""
    t = t_(AMB)
    hum = sum(a * np.sin(2 * np.pi * f * t) for f, a in ((120, 1), (240, 0.5), (360, 0.35), (480, 0.2), (600, 0.12)))
    buzz = np.clip(np.sin(2 * np.pi * 120 * t) * 3, -1, 1) * 0.08 * smooth_rand(AMB, 0.3, 31, 0.4, 1)
    flick = 1 - 0.15 * (smooth_rand(AMB, 4, 32, 0, 1) > 0.93)          # thỉnh thoảng chập chờn
    hvac = lp(pink(AMB, 33), 700) * 0.9
    tone = np.stack([0.25 * (hum + buzz) * flick + hvac, 0.22 * (hum + buzz) * flick + lp(pink(AMB, 34), 700) * 0.9], 1)
    return loopable(tone.astype(np.float32))


def amb_office_night():
    """Văn phòng đêm: nền phòng + đồng hồ treo tường + xe xa ngoài cửa."""
    x = np.stack([lp(pink(AMB, 41), 900) * 0.5, lp(pink(AMB, 42), 900) * 0.5], 1)
    tick = hp(white(0.02, 43), 2000) * env_exp(0.02, 0.003)
    for k in range(int(AMB)):
        place(x[:, 0], tick, k + 0.02, 0.9 if k % 2 else 0.6)
        place(x[:, 1], tick, k + 0.021, 0.7 if k % 2 else 0.5)
    for t0, p in ((8, -0.6), (23, 0.5), (34, -0.2)):                   # xe chạy qua xa
        car = lp(pink(5, int(t0)), 600) * np.hanning(int(5 * SR))
        place(x, pan(car * 0.5, p), t0)
    return loopable(x)


def amb_basement():
    """Tầng hầm: ù trầm + nước nhỏ giọt có vang."""
    base = np.stack([lp(brown(AMB, 51), 120), lp(brown(AMB, 52), 120)], 1) * 0.6
    drips = np.zeros(int(AMB * SR), np.float32)
    r = RNG(53)
    for t0 in np.cumsum(r.uniform(1.2, 3.5, 30)):
        if t0 > AMB - 1:
            break
        d = 0.06
        f = r.uniform(900, 1500)
        tt = t_(d)
        drop = np.sin(2 * np.pi * (f + 900 * tt / d) * tt) * env_exp(d, 0.012)
        place(drips, drop, t0, r.uniform(0.3, 0.7))
    return loopable(base + verb(drips, "medium", 0.6)[: len(base)] * 0.5)


def amb_courtroom():
    """Phòng xử lớn, trống: nền phòng rộng, ghế gỗ kẽo kẹt rất nhỏ."""
    x = np.stack([lp(pink(AMB, 61), 500) * 0.4, lp(pink(AMB, 62), 500) * 0.4], 1)
    creak = np.zeros(int(AMB * SR), np.float32)
    for t0 in (7.0, 19.5, 31.0):
        c = bp(white(0.5, int(t0)), 300, 900) * smooth_rand(0.5, 20, int(t0) + 1, 0, 1) * np.hanning(int(0.5 * SR))
        place(creak, c, t0, 0.5)
    return loopable(x + verb(creak, "hall", 0.7)[: len(x)] * 0.4)


def amb_fire():
    """Lửa trong thùng: gầm trầm + tí tách."""
    roar = np.stack([lp(brown(AMB, 71), 250), lp(brown(AMB, 72), 250)], 1) * 0.3 + np.stack([bp(pink(AMB, 75), 2000, 8000), bp(pink(AMB, 76), 2000, 8000)], 1) * 0.12
    crack = grains(AMB, 70, 73, 1200, 9000, (0.0008, 0.003), (0.2, 1.0))
    pops = grains(AMB, 6, 74, 600, 4000, (0.002, 0.008), (0.6, 1.0))
    return loopable(roar + pan(crack * 0.9, -0.1) + pan(pops * 1.0, 0.2))


def amb_road_night():
    """Đường quê đêm tuyết ở trạm kiểm soát: gió + đèn xe chạy qua + máy xe nổ không tải gần."""
    x = amb_winter_wind() * 0.7
    t = np.arange(len(x)) / SR
    idle = sum(a * np.sin(2 * np.pi * f * t + 0.3 * np.sin(2 * np.pi * 0.7 * t)) for f, a in ((32, 1), (64, 0.6), (96, 0.3)))
    idle = lp(idle.astype(np.float32) + 0.3 * lp(brown(len(x) / SR, 81), 200), 250) * 0.35
    return (x + pan(idle, 0.4)[: len(x)]).astype(np.float32)


# ================================================================== TIẾNG ĐỘNG
def fx_tire_snow():
    """Xe lăn bánh chậm trên tuyết, dừng lại: lạo xạo + ù máy."""
    d = 4.0
    crunch = lp(grains(d, 420, 101, 250, 2200, (0.004, 0.014), (0.15, 0.6)), 2500) * np.linspace(1, 0.15, int(d * SR))
    t = t_(d)
    eng = lp(np.sin(2 * np.pi * 38 * t) + 0.5 * np.sin(2 * np.pi * 76 * t) + 0.4 * lp(brown(d, 102), 150), 300)
    eng *= np.linspace(0.6, 1, len(t))
    return verb(pan(crunch * 0.8 + eng * 0.5, 0.3), "outdoor", 0.25)


def fx_footsteps_snow(steps=6, gap=0.62):
    d = steps * gap + 0.5
    x = np.zeros(int(d * SR), np.float32)
    for k in range(steps):
        st = lp(grains(0.22, 700, 110 + k, 300, 2600, (0.003, 0.01), (0.2, 0.7)), 3000) * np.sin(np.pi * np.linspace(0, 1, int(0.22 * SR))) ** 0.7
        thump = lp(white(0.08, 120 + k), 180) * env_exp(0.08, 0.02)
        place(x, st + pad(thump, 0.22), k * gap + RNG(k).uniform(-0.03, 0.03), 0.8 if k % 2 else 1.0)
    return verb(pan(x, -0.2), "outdoor", 0.2)


def fx_window_down():
    """Kính xe hạ xuống: mô-tơ rít + gió lùa vào."""
    d = 2.6
    t = t_(d)
    f = 140 - 15 * t / d
    motor = np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.4 * np.sin(4 * np.pi * np.cumsum(f) / SR)
    motor = bp(motor.astype(np.float32), 200, 1500) * np.r_[np.linspace(0, 1, 2000), np.ones(len(t) - 4000), np.linspace(1, 0, 2000)]
    rush = bp(pink(d, 131), 300, 2500) * np.linspace(0, 0.6, len(t))
    stop = modes(0.2, (180, 410), (0.03, 0.02), (1, 0.4), 132)
    out = lp(motor, 700) * 0.25 + rush
    place(out, stop, d - 0.25, 0.7)
    return verb(pan(out, 0.45), "small", 0.15)


def fx_flashlight():
    x = np.zeros(int(0.6 * SR), np.float32)
    for k, t0 in enumerate((0.0, 0.11)):
        c = hp(white(0.015, 140 + k), 1500) * env_exp(0.015, 0.002) + modes(0.04, (2600, 4100), (0.008, 0.005), (0.4, 0.2), 141)[:661]
        place(x, c, t0, 1.0 if k == 0 else 0.7)
    return verb(pan(x, 0.3), "outdoor", 0.15)


def fx_police_radio():
    """Bộ đàm: tiếng xẹt + giọng nói méo không nghe ra chữ + tiếng xẹt đóng."""
    d = 2.4
    sq = bp(white(0.09, 150), 900, 3500) * np.hanning(int(0.09 * SR))
    syl = (np.sin(2 * np.pi * 5.2 * t_(1.7)) > 0.1) * smooth_rand(1.7, 9, 151, 0.3, 1)
    talk = bp(white(1.7, 152) + 0.6 * np.sin(2 * np.pi * 180 * t_(1.7)), 500, 2600) * syl
    talk = np.clip(talk * 2.5, -1, 1) * 0.5
    x = np.zeros(int(d * SR), np.float32)
    place(x, sq, 0.0)
    place(x, talk, 0.12, 0.8)
    place(x, sq, 1.9, 0.9)
    return verb(pan(x, -0.5), "outdoor", 0.2)


def fx_door_metal_slam():
    """Cửa sắt đóng sầm: va đập trầm + cộng hưởng kim loại + vang hành lang."""
    d = 2.2
    thump = lp(white(0.3, 160), 140) * env_exp(0.3, 0.06) * 2
    ring = modes(d, (93, 181, 433, 721, 1120, 1640), (0.5, 0.4, 0.3, 0.2, 0.12, 0.08), (0.5, 0.6, 0.5, 0.35, 0.25, 0.15), 161)
    latch = hp(white(0.04, 162), 1800) * env_exp(0.04, 0.006)
    x = pad(thump, d) + ring * 0.5
    place(x, latch, 0.005, 1.2)
    return verb(pan(x, -0.15), "medium", 0.45)


def fx_phone_ring():
    """Điện thoại bàn cũ đổ chuông 2 hồi."""
    d = 6.2
    t = t_(d)
    tone = (np.sin(2 * np.pi * 440 * t) + np.sin(2 * np.pi * 480 * t)) * (np.sin(2 * np.pi * 20 * t) > 0)
    gate = ((t % 3.0) < 1.0) | (((t % 3.0) > 1.2) & ((t % 3.0) < 2.0))
    x = bp(tone * gate, 350, 3000).astype(np.float32) * 0.6
    return verb(pan(x, 0.25), "small", 0.3)


def fx_camera_shutter():
    x = np.zeros(int(0.5 * SR), np.float32)
    for t0, g in ((0.0, 1.0), (0.045, 0.7)):
        place(x, hp(white(0.02, int(t0 * 1000) + 170), 1200) * env_exp(0.02, 0.003), t0, g)
        place(x, modes(0.06, (1900, 3300), (0.01, 0.006), (0.3, 0.2), 171), t0, g * 0.6)
    whir = bp(white(0.25, 172), 2500, 6000) * np.hanning(int(0.25 * SR)) * 0.15
    place(x, whir, 0.08)
    return verb(pan(x, 0.1), "small", 0.2)


def fx_drawer_open():
    """Ngăn kéo gỗ kéo ra: ma sát + rung gỗ + chạm cuối."""
    d = 1.1
    rub = bp(pink(d, 180), 150, 1800) * smooth_rand(d, 30, 181, 0.4, 1) * np.r_[np.linspace(0, 1, 3000), np.ones(int(d * SR) - 6000), np.linspace(1, 0, 3000)]
    knock = modes(0.25, (140, 310, 620), (0.06, 0.04, 0.02), (1, 0.5, 0.3), 182)
    x = rub * 0.6
    place(x, knock, d - 0.27, 0.9)
    return verb(pan(x, -0.3), "small", 0.25)


def fx_hdd_spin():
    """Ổ cứng quay lên + kim đọc lách cách."""
    d = 3.0
    t = t_(d)
    f = 20 + 70 * (1 - np.exp(-t / 0.6))
    whine = np.sin(2 * np.pi * np.cumsum(f) / SR) + 0.3 * np.sin(2 * np.pi * np.cumsum(f * 7) / SR)
    whine = (whine * np.minimum(1, t / 0.3)).astype(np.float32) * 0.3
    clicks = np.zeros_like(whine)
    r = RNG(190)
    for t0 in np.sort(r.uniform(0.9, 2.8, 14)):
        place(clicks, hp(white(0.006, int(t0 * 1e4)), 2000) * env_exp(0.006, 0.0015), t0, r.uniform(0.3, 0.8))
    return verb(pan(whine + clicks, 0.2), "medium", 0.3)


def fx_chair_scrape():
    """Ghế kim loại kéo trên nền gạch: ma sát + rít cộng hưởng."""
    d = 1.3
    t = t_(d)
    rub = (bp(white(d, 200), 150, 1400) + 0.6 * lp(brown(d, 203), 200)) * smooth_rand(d, 40, 201, 0.3, 1)
    sq_f = 820 + 120 * np.sin(2 * np.pi * 1.7 * t)
    squeal = np.sin(2 * np.pi * np.cumsum(sq_f * 0.5) / SR) * smooth_rand(d, 12, 202, 0, 1) ** 4 * 0.08
    x = (rub * 0.6 + squeal) * np.hanning(len(t))
    return verb(pan(x.astype(np.float32), -0.35), "small", 0.35)


def fx_cup_down():
    """Đặt cốc sứ xuống bàn gỗ: 'Cộp'."""
    x = lp(white(0.08, 210), 400) * env_exp(0.08, 0.012) * 1.5
    x = pad(x, 0.6) + modes(0.6, (2110, 3420, 5200), (0.09, 0.06, 0.03), (0.25, 0.18, 0.08), 211)
    return verb(pan(x, 0.25), "small", 0.25)


def fx_photo_slide():
    """Trượt tấm ảnh trên mặt bàn: 'Xoẹt'."""
    d = 0.55
    x = bp(white(d, 220), 1200, 7000) * np.sin(np.pi * np.linspace(0, 1, int(d * SR))) ** 0.8 * 0.6
    tap = lp(white(0.03, 221), 600) * env_exp(0.03, 0.006)
    place(x, tap, d - 0.04, 0.6)
    return verb(pan(x, 0.15), "small", 0.2)


def fx_paper_folder():
    """Mở tập hồ sơ, lật vài trang."""
    d = 1.6
    x = grains(d, 380, 230, 900, 6000, (0.003, 0.012), (0.2, 0.8)) * smooth_rand(d, 6, 231, 0.2, 1)
    return verb(pan(x, -0.1), "small", 0.2)


def fx_pen_scribble():
    d = 1.4
    x = bp(white(d, 240), 2000, 7000) * (np.abs(np.sin(2 * np.pi * 6 * t_(d))) ** 3) * smooth_rand(d, 5, 241, 0.4, 1) * 0.5
    return verb(pan(x.astype(np.float32), 0.2), "small", 0.15)


def fx_map_unfold():
    d = 1.4
    crin = grains(d, 600, 250, 500, 5000, (0.002, 0.01), (0.2, 1.0)) * smooth_rand(d, 4, 251, 0.1, 1)
    flap = lp(white(0.15, 252), 300) * np.hanning(int(0.15 * SR))
    x = crin * 0.7
    place(x, flap, 0.9, 0.8)
    return verb(pan(x, 0), "outdoor", 0.15)


def fx_metal_snip():
    """Cắt huân chương: hai nhát kéo kim loại."""
    x = np.zeros(int(1.4 * SR), np.float32)
    for k, t0 in enumerate((0.0, 0.6)):
        shear = bp(white(0.12, 260 + k), 2500, 9000) * env_exp(0.12, 0.03) * 0.6
        clk = modes(0.3, (1870, 3010, 4420), (0.05, 0.03, 0.02), (0.6, 0.4, 0.2), 262 + k)
        place(x, shear + pad(clk, 0.12)[: len(shear)], t0)
        place(x, clk, t0 + 0.1, 0.5)
    return verb(pan(x, 0.1), "small", 0.3)


def fx_metal_crush():
    """Xe bị ép nát: ù trầm, kim loại oằn, va đập liên tiếp."""
    d = 4.5
    rumble = lp(brown(d, 270), 120) * np.r_[np.linspace(0, 1, int(1 * SR)), np.ones(int(d * SR) - int(1.5 * SR)), np.linspace(1, 0, int(0.5 * SR))]
    x = rumble * 0.8
    r = RNG(271)
    for t0 in np.sort(r.uniform(0.6, 4.0, 12)):
        hit = modes(0.9, tuple(r.uniform(60, 600, 5)), (0.35, 0.25, 0.18, 0.12, 0.08), (1, 0.7, 0.5, 0.3, 0.2), int(t0 * 100)) + pad(lp(white(0.1, int(t0 * 77)), 250) * env_exp(0.1, 0.03) * 2, 0.9)
        place(x, hit, t0, r.uniform(0.2, 0.6))
    for t0 in (0.8, 1.9, 2.9):
        groan = bp(white(1.0, int(t0 * 10)), 120, 600) * smooth_rand(1.0, 15, int(t0 * 11), 0, 1) * np.hanning(int(SR))
        place(x, groan, t0, 0.5)
    return verb(pan(x, 0), "outdoor", 0.3)


def fx_fire_whoosh():
    """Lửa bùng lên khi bén vào vải."""
    d = 2.5
    t = t_(d)
    swell = np.minimum(1, t / 0.4) * np.exp(-np.maximum(0, t - 0.5) / 1.2)
    x = (lp(brown(d, 280), 600) + 0.4 * bp(pink(d, 281), 800, 4000)) * swell
    x = x + grains(d, 30, 282, 1500, 7000, (0.001, 0.004)) * 0.3
    return verb(pan(x.astype(np.float32), 0), "small", 0.3)


def fx_gavel_triple():
    """Búa tòa 'Cốp… Cốp… Cốp' trong sảnh lớn."""
    x = np.zeros(int(3.2 * SR), np.float32)
    for k, t0 in enumerate((0.0, 0.75, 1.5)):
        h = (lp(white(0.06, 290 + k), 700) * 1.6 + np.sin(2 * np.pi * 95 * t_(0.06)) * 1.2) * env_exp(0.06, 0.012)
        h = pad(h, 0.4) + modes(0.4, (210, 470, 980), (0.025, 0.015, 0.008), (0.35, 0.2, 0.1), 293 + k)
        place(x, h, t0, 1.0 - 0.1 * k)
    return verb(x, "hall", 0.5)


# --------------------------------------------------------------- nhấn kịch tính (điện ảnh)
def fx_sub_drop():
    d = 2.6
    t = t_(d)
    f = 62 * np.exp(-t / 1.0) + 26
    x = np.tanh(1.6 * np.sin(2 * np.pi * np.cumsum(f) / SR)) * np.exp(-t / 1.1)
    return verb(x.astype(np.float32), "hall", 0.25)


def fx_stinger():
    """Hợp âm dây nghịch (quãng 2 thứ) dâng lên rồi cắt — cho khoảnh khắc hé lộ."""
    d = 2.2
    t = t_(d)
    x = np.zeros_like(t)
    for f in (146.8, 155.6, 220.0, 233.1, 293.7):
        vib = 1 + 0.004 * np.sin(2 * np.pi * 5.5 * t + f)
        ph = 2 * np.pi * np.cumsum(f * vib) / SR
        x += np.sin(ph) + 0.4 * np.sin(2 * ph) + 0.2 * np.sin(3 * ph)
    env = np.minimum(1, (t / 1.4) ** 2) * (t < 1.65) + (t >= 1.65) * np.exp(-(t - 1.65) / 0.08)
    bow = bp(white(d, 300), 1500, 5000) * 0.05
    return verb(((x / 6 + bow) * env).astype(np.float32), "hall", 0.4)


def fx_heartbeat_slow():
    d = 4.0
    x = np.zeros(int(d * SR), np.float32)
    for k in range(4):
        for off, g in ((0.0, 1.0), (0.24, 0.7)):
            b = lp(np.sin(2 * np.pi * 48 * t_(0.18)) * env_exp(0.18, 0.05), 150)
            place(x, b, k * 1.0 + off, g)
    return x


def fx_tension_tick():
    """Kim đồng hồ khô khốc, có vang phòng — dưới những câu chờ đợi."""
    d = 6.0
    x = np.zeros(int(d * SR), np.float32)
    for k in range(6):
        c = hp(white(0.015, 310 + k), 1800) * env_exp(0.015, 0.003) + modes(0.05, (3100,), (0.01,), (0.3,), 311)[: int(0.015 * SR)]
        place(x, c, k * 1.0, 1.0 if k % 2 == 0 else 0.75)
    return verb(x, "small", 0.35)


AMBIENCES = {"amb_winter_wind.wav": amb_winter_wind, "amb_airbase.wav": amb_airbase,
             "amb_interrogation.wav": amb_interrogation, "amb_office_night.wav": amb_office_night,
             "amb_basement.wav": amb_basement, "amb_courtroom.wav": amb_courtroom,
             "amb_fire.wav": amb_fire, "amb_road_night.wav": amb_road_night}
EFFECTS = {"fx_tire_snow.wav": fx_tire_snow, "fx_footsteps_snow.wav": fx_footsteps_snow,
           "fx_window_down.wav": fx_window_down, "fx_flashlight.wav": fx_flashlight,
           "fx_police_radio.wav": fx_police_radio, "fx_door_metal_slam.wav": fx_door_metal_slam,
           "fx_phone_ring.wav": fx_phone_ring, "fx_camera_shutter.wav": fx_camera_shutter,
           "fx_drawer_open.wav": fx_drawer_open, "fx_hdd_spin.wav": fx_hdd_spin,
           "fx_chair_scrape.wav": fx_chair_scrape, "fx_cup_down.wav": fx_cup_down,
           "fx_photo_slide.wav": fx_photo_slide, "fx_paper_folder.wav": fx_paper_folder,
           "fx_pen_scribble.wav": fx_pen_scribble, "fx_map_unfold.wav": fx_map_unfold,
           "fx_metal_snip.wav": fx_metal_snip, "fx_metal_crush.wav": fx_metal_crush,
           "fx_fire_whoosh.wav": fx_fire_whoosh, "fx_gavel_triple.wav": fx_gavel_triple,
           "fx_sub_drop.wav": fx_sub_drop, "fx_stinger.wav": fx_stinger,
           "fx_heartbeat_slow.wav": fx_heartbeat_slow, "fx_tension_tick.wav": fx_tension_tick}


def load(name, maxdur=None):
    """maxdur: cat nganh tieng (tieng thu thap co the dai hon nhieu giay so voi ban tong hop)."""
    with wave.open(str(OUT / name), "rb") as w:
        x = np.frombuffer(w.readframes(w.getnframes()), "<i2").astype(np.float32) / 32768
    x = x.reshape(-1, 2)
    if maxdur:
        x = x[: int(maxdur * SR)]
    return x


def demo():
    """3 cảnh × ~15 s, không lời: nghe nền + tiếng động + vang có 'ở trong cảnh' không."""
    import subprocess
    db = lambda v: 10 ** (v / 20)  # noqa: E731
    scenes = []
    # cảnh 1 — trạm kiểm soát đêm tuyết
    s = load("amb_road_night.wav")[: int(16 * SR)] * db(-16)
    for f, t0, g in (("fx_police_radio.wav", 0.8, -10), ("fx_tire_snow.wav", 3.0, -8), ("fx_window_down.wav", 7.4, -9),
                     ("fx_flashlight.wav", 10.3, -10), ("fx_footsteps_snow.wav", 11.0, -12), ("fx_stinger.wav", 13.0, -14)):
        place(s, load(f, 5.0), t0, db(g))
    scenes.append(s)
    # cảnh 2 — phòng thẩm vấn
    s = load("amb_interrogation.wav")[: int(16 * SR)] * db(-18)
    for f, t0, g in (("fx_door_metal_slam.wav", 0.3, -6), ("fx_chair_scrape.wav", 2.6, -9), ("fx_cup_down.wav", 4.3, -8),
                     ("fx_paper_folder.wav", 6.5, -12), ("fx_photo_slide.wav", 9.0, -9), ("fx_tension_tick.wav", 10.0, -16),
                     ("fx_sub_drop.wav", 13.2, -6)):
        place(s, load(f, 5.0), t0, db(g))
    scenes.append(s)
    # cảnh 3 — đốt quân phục, ép xe, búa tòa
    s = load("amb_fire.wav")[: int(16 * SR)] * db(-18)
    s[: int(5 * SR)] = load("amb_basement.wav")[: int(5 * SR)] * db(-16)
    for f, t0, g in (("fx_fire_whoosh.wav", 4.6, -6), ("fx_metal_snip.wav", 8.5, -9), ("fx_metal_crush.wav", 10.4, -9),
                     ("fx_gavel_triple.wav", 13.6, -6)):
        place(s, load(f, 5.0), t0, db(g))
    scenes.append(s)
    gap = np.zeros((int(1.2 * SR), 2), np.float32)
    mix = np.concatenate([np.concatenate([sc, gap]) for sc in scenes])
    mix = norm(mix, 0.8)
    out = ROOT / "02_SAN_XUAT" / "Tap02" / "thu_am"
    out.mkdir(parents=True, exist_ok=True)
    wav = out / "demo_sfx_tap02.wav"
    with wave.open(str(wav), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((mix * 32767).astype("<i2").tobytes())
    ff = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
    subprocess.run([str(ff), "-y", "-v", "error", "-i", str(wav), "-c:a", "libmp3lame", "-b:a", "192k",
                    str(out / "demo_sfx_tap02.mp3")], check=True)
    wav.unlink()
    print("demo:", out / "demo_sfx_tap02.mp3", f"{len(mix) / SR:.1f} s")


def protected():
    """Cac file da lay tu YouTube Audio Library -> KHONG duoc ghi de bang ban tong hop."""
    pj = ROOT / "provenance.json"
    if not pj.exists():
        return set()
    try:
        data = json.loads(pj.read_text(encoding="utf-8"))
    except Exception:
        return set()
    out = set()
    for e in data:
        f = e.get("file", "")
        if f.startswith("assets/sfx/t2/") and e.get("track_youtube"):
            out.add(Path(f).stem)
    return out


def main():
    if "--demo-only" in sys.argv:
        print("chi dung lai demo (khong sinh lai tieng tong hop)")
        demo()
        return
    keep = protected()
    for name, fn in {**AMBIENCES, **EFFECTS}.items():
        if name[:-4] in keep:
            print(f"  {name:<26} GIU NGUYEN (tieng YouTube Audio Library)")
            continue
        x = fn()
        write(name, x)
        print(f"  {name:<26} {len(x) / SR:5.1f} s")
    if "--demo" in sys.argv:
        demo()


if __name__ == "__main__":
    main()
