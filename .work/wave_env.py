# -*- coding: utf-8 -*-
"""Chuẩn hoá envelope sóng giọng trên badge vai (AGENTS H24) — dùng chung cho
build_video3.py (vẽ) và qc_wave_gate.py (đo), để cổng đo ĐÚNG công thức vẽ.

Trước 16/11/2026 renderer chia cho hằng 0.12 (chỉnh theo MiniMax). Giọng Higgs to
hơn ⇒ Tập 10 có 44–62 % khung đang nói kịch trần ⇒ sóng thành dải ngang.
Nay mặc định "auto": phân vị 95 của khung ĐANG NÓI trong chính stem đó ↦ 0,9.
Tập muốn giữ y bản đã xuất thì ghim số cố định ở EPISODES[xx]["wave_norm"].
"""
import wave

import numpy as np

FPS = 30
VOICED_RMS = 0.01      # RMS khung > ngưỡng này = đang nói
TARGET_P95 = 0.9       # phân vị 95 khung đang nói sau chuẩn hoá
LEGACY = 0.12          # hằng cũ (MiniMax) — dùng khi stem quá ít lời để đo


def rms_frames(stem_path, fps=FPS, chunk=1 << 20):
    """RMS thô mỗi khung video của stem (int16 mono), đọc theo khối."""
    with wave.open(str(stem_path)) as wf:
        sr = wf.getframerate()
        hop = sr // fps
        n = wf.getnframes() // hop
        e = np.zeros(n, dtype=np.float32)
        rows = max(1, chunk // hop)
        done = 0
        while done < n:
            k = min(rows, n - done)
            a = np.frombuffer(wf.readframes(k * hop), np.int16)
            if a.size < k * hop:
                k = a.size // hop
                if k <= 0:
                    break
                a = a[: k * hop]
            blk = a.astype(np.float32) / 32768
            e[done:done + k] = np.sqrt((blk.reshape(k, hop) ** 2).mean(axis=1))
            done += k
    return e


def scale_for(e, mode=None):
    """Hệ số chia. mode = số ⇒ cố định (ghim tập cũ); None/"auto" ⇒ tự đo."""
    if isinstance(mode, (int, float)) and not isinstance(mode, bool):
        return float(mode)
    v = e[e > VOICED_RMS]
    if v.size < FPS:                       # < 1 s lời: không đủ để đo
        return LEGACY
    return max(float(np.percentile(v, 95)) / TARGET_P95, 1e-6)


def normalize(e, mode=None):
    return np.clip(e / scale_for(e, mode), 0, 1).astype(np.float32)
