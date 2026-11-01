#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh giọng mẫu tiếng Hàn vòng 5 (ko5): VAI D bằng VoxCPM2 chế độ CLONE từ D3_SH (Mac mini, MPS).

Thực hiện đề xuất trong 90_LUU_TRU/BaoCao_DoGiongMau_JA3_KO3_20261101.md:
- Giọng tham chiếu: assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav (D3_SH, F0 ~88 Hz)
- Target text: câu thoại tiếng Hàn chuẩn của vai D (5 câu, ~48 từ)
- 10 take (10 seed đa dạng)
- Xuất: assets/voice_ref_voxcpm2_ko5/D_clone_d3sh_ko5_tNN.wav + .txt + refs.json
"""
import datetime
import json
import os
import shutil
import subprocess
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf
import torch
from voxcpm import VoxCPM

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
RAW_DIR = WORK / "voxcpm_raw" / "D_ko5"
OUT_DIR = ROOT / "assets" / "voice_ref_voxcpm2_ko5"
REF_WAV = ROOT / "assets" / "voice_ref_voxcpm2_dc3" / "D_NEW_subbass-husky_t02.wav"
REF_TXT = ROOT / "assets" / "voice_ref_voxcpm2_dc3" / "D_NEW_subbass-husky_t02.txt"

TARGET_TEXT = (
    "수사 일지에는 모든 정황이 상세히 기록되어 있습니다. "
    "현장 주택에서 발견된 증거와 일치하는 진술은 단 하나도 없었습니다. "
    "질문은 여전히 남아 있고, 전체 기록은 아직 모든 것을 말해주지 않았습니다. "
    "현장은 초기부터 철저히 통제되었으며, 모든 증거물은 절차에 따라 번호가 매겨지고 봉인되었습니다. "
    "최종 결론을 내리기 전에 시간대와 이동 동선을 철저히 재검증해야 합니다."
)

SEEDS = [7, 11, 42, 99, 101, 256, 500, 777, 888, 2024]
CFG = 2.0
TIMESTEPS = 10
F0_TARGET = [78, 88]
LO_SEC, HI_SEC = 16.0, 28.0

FLT = (
    "aresample=24000,"
    "loudnorm=I=-18:TP=-2.0:LRA=11,"
    "silenceremove=start_periods=1:start_threshold=-50dB,"
    "areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse"
)


def f0_autocorr(x, sr=24000):
    """Autocorrelation F0 median (using ffmpeg pipe to 16 kHz, exact match with voxcpm_generate_g9)."""
    ff = shutil.which("ffmpeg") or "ffmpeg"
    tmp_in = f"/tmp/_f0_autocorr_{os.getpid()}.wav"
    sf.write(tmp_in, x, sr)
    r = subprocess.run([ff, "-v", "error", "-i", tmp_in, "-ac", "1", "-ar", "16000",
                        "-f", "s16le", "-"], capture_output=True)
    try:
        os.remove(tmp_in)
    except OSError:
        pass
    if r.returncode != 0 or not r.stdout:
        return 0.0
    x_16k = np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768
    sr_res = 16000
    win, hop, out = int(0.04 * sr_res), int(0.01 * sr_res), []
    for s in range(0, len(x_16k) - win, hop):
        f = x_16k[s : s + win]
        if np.sqrt((f ** 2).mean()) < 0.02:
            continue
        f = f - f.mean()
        ac = np.correlate(f, f, "full")[win - 1 :]
        lo, hi = int(sr_res / 400), int(sr_res / 70)
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.3 * ac[0]:
            out.append(sr_res / k)
    return float(np.median(out)) if out else 0.0


def f0_yin(x, sr=24000, fmin=60, fmax=400, win=0.04, hop=0.01, th=0.15):
    """YIN pitch estimation."""
    W = int(win * sr)
    H = int(hop * sr)
    tmin = int(sr / fmax)
    tmax = int(sr / fmin)
    out = []
    for s in range(0, len(x) - W - tmax, H):
        f = x[s : s + W + tmax]
        if np.sqrt((f[:W] ** 2).mean()) < 0.02:
            continue
        d = np.array([np.sum((f[:W] - f[t : t + W]) ** 2) for t in range(tmax + 1)])
        c = np.cumsum(d[1:])
        dn = np.ones_like(d)
        dn[1:] = d[1:] * np.arange(1, tmax + 1) / np.maximum(c, 1e-12)
        cand = np.where(dn[tmin:] < th)[0]
        if not len(cand):
            continue
        t = tmin + cand[0]
        while t + 1 <= tmax and dn[t + 1] < dn[t]:
            t += 1
        if 1 <= t < tmax:
            a, b, cc = dn[t - 1], dn[t], dn[t + 1]
            den = a - 2 * b + cc
            t = t + (0.5 * (a - cc) / den if den else 0)
        out.append(sr / t)
    return float(np.median(out)) if out else 0.0


def measure_loudness(wav_path):
    """Measure integrated LUFS and True Peak via ffmpeg ebur128."""
    r = subprocess.run(
        ["ffmpeg", "-i", str(wav_path), "-af", "ebur128=peak=true", "-f", "null", "-"],
        capture_output=True,
        text=True,
    )
    lufs, peak = -99.0, 0.0
    for line in r.stderr.splitlines():
        if "I:" in line and "LUFS" in line:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    lufs = float(parts[1])
                except Exception:
                    pass
        if "Peak:" in line and "dBFS" in line:
            parts = line.split()
            if len(parts) >= 2:
                try:
                    peak = float(parts[1])
                except Exception:
                    pass
    return lufs, peak


def measure_audio_props(data, sr):
    """Measure total duration, active speech duration, max pause, and noise floor."""
    dur = len(data) / float(sr)
    frame_len = int(0.02 * sr)
    rms_frames = []
    for s in range(0, len(data) - frame_len, frame_len):
        f = data[s : s + frame_len]
        rms_frames.append(np.sqrt(np.mean(f ** 2)))
    rms_arr = np.array(rms_frames)

    speech_frames = int(np.sum(rms_arr >= 0.00316))  # -50 dBFS
    speech_dur = float(speech_frames * 0.02)

    # Noise floor: 3rd percentile RMS converted to dBFS
    q03 = float(np.percentile(rms_arr, 3))
    noise_dbfs = float(20 * np.log10(max(q03, 1e-12)))

    # Max pause
    is_silent = rms_arr < 0.00316
    max_silent, cur_silent = 0, 0
    for s in is_silent:
        if s:
            cur_silent += 1
            if cur_silent > max_silent:
                max_silent = cur_silent
        else:
            cur_silent = 0
    max_pause = float(max_silent * 0.02)

    return float(dur), speech_dur, max_pause, noise_dbfs


def main():
    print("=" * 76)
    print("VOXCPM2 — TẠO GIỌNG MẪU TIẾNG HÀN VÒNG 5 (ko5): VAI D (CLONE TỪ D3_SH)")
    print("=" * 76)

    assert REF_WAV.exists(), f"Thiếu file giọng tham chiếu: {REF_WAV}"
    assert REF_TXT.exists(), f"Thiếu file lời tham chiếu: {REF_TXT}"
    prompt_text = REF_TXT.read_text(encoding="utf-8").strip()

    RAW_DIR.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    refs_json_path = OUT_DIR / "refs.json"
    records = {}
    if refs_json_path.exists():
        try:
            records = json.loads(refs_json_path.read_text(encoding="utf-8"))
        except Exception:
            records = {}

    print(f"\n[1/2] Nạp model VoxCPM2 trên MPS...")
    t0 = time.time()
    model = VoxCPM.from_pretrained("openbmb/VoxCPM2", optimize=False, device="mps", local_files_only=True)
    SR = getattr(model.tts_model, "sample_rate", 48000)
    print(f"    Nạp xong trong {time.time() - t0:.1f}s | sample_rate: {SR}")

    print(f"\n[2/2] Sinh {len(SEEDS)} take clone (cfg={CFG}, steps={TIMESTEPS})...\n")

    t_all = time.time()
    for idx, seed in enumerate(SEEDS, 1):
        name = f"D_clone_d3sh_ko5_t{idx:02d}"
        raw_wav = RAW_DIR / f"{name}.wav"
        pkg_wav = OUT_DIR / f"{name}.wav"
        pkg_txt = OUT_DIR / f"{name}.txt"

        print(f"  [{idx:02d}/{len(SEEDS):02d}] {name} (seed={seed})...", end="", flush=True)

        t_gen = time.time()
        # Nếu đã có raw và pkg hợp lệ, có thể tái sử dụng
        if not raw_wav.exists():
            torch.manual_seed(seed)
            if torch.backends.mps.is_available():
                torch.mps.manual_seed(seed)
            audio = model.generate(
                text=TARGET_TEXT,
                prompt_wav_path=str(REF_WAV),
                prompt_text=prompt_text,
                cfg_value=CFG,
                inference_timesteps=TIMESTEPS,
                normalize=False,
                denoise=False,
            )
            raw_audio = np.asarray(audio, dtype=np.float32).squeeze()
            sf.write(str(raw_wav), raw_audio, SR)
            dt_gen = time.time() - t_gen
        else:
            raw_audio, _ = sf.read(str(raw_wav), dtype="float32")
            dt_gen = 0.0

        # Packaging 24 kHz mono -18 LUFS
        subprocess.run(
            ["ffmpeg", "-y", "-v", "error", "-i", str(raw_wav), "-af", FLT,
             "-ac", "1", "-ar", "24000", "-c:a", "pcm_s16le", str(pkg_wav)],
            check=True,
        )
        pkg_txt.write_text(TARGET_TEXT, encoding="utf-8")

        # Measurements
        data, sr_read = sf.read(str(pkg_wav), dtype="float32")
        tot_dur, speech_dur, max_pause, noise_dbfs = measure_audio_props(data, sr_read)
        ac_f0 = f0_autocorr(data, sr_read)
        yin_f0 = f0_yin(data, sr_read)
        lufs, true_peak = measure_loudness(pkg_wav)

        notes = []
        if not (F0_TARGET[0] * 0.94 <= yin_f0 <= F0_TARGET[1] * 1.06):
            notes.append(f"YIN F0 {yin_f0:.1f}Hz ngoai dai {F0_TARGET[0]}-{F0_TARGET[1]}Hz")
        if not (LO_SEC <= speech_dur <= HI_SEC):
            notes.append(f"Speech dur {speech_dur:.1f}s ngoai [{LO_SEC}-{HI_SEC}]s")
        if lufs < -19.0 or lufs > -17.0:
            notes.append(f"LUFS {lufs:.1f} ngoai [-19, -17]")
        if true_peak > -1.5:
            notes.append(f"Peak {true_peak:.1f}dBFS > -1.5")
        if max_pause > 1.5:
            notes.append(f"Max pause {max_pause:.2f}s > 1.5s")

        status_str = "[TRONG DAI]" if not notes else f"!! {'; '.join(notes)}"
        print(f" {dt_gen:4.1f}s | dur {tot_dur:4.1f}s (sp {speech_dur:4.1f}s) | AC {ac_f0:4.1f} / YIN {yin_f0:4.1f} Hz | LUFS {lufs:5.1f} | {status_str}")

        records[name] = {
            "voice_source": "VoxCPM2 (OpenBMB) - Cross-lingual Voice Clone",
            "reference_audio": str(REF_WAV.relative_to(ROOT)),
            "reference_text": prompt_text,
            "target_text": TARGET_TEXT,
            "source_file": str(raw_wav.relative_to(ROOT)),
            "reference_file": str(pkg_wav.relative_to(ROOT)),
            "role": "D",
            "variant": "clone_d3sh_ko5",
            "seed": seed,
            "cfg": CFG,
            "inference_timesteps": TIMESTEPS,
            "total_seconds": float(round(tot_dur, 2)),
            "speech_seconds": float(round(speech_dur, 2)),
            "max_pause_s": float(round(max_pause, 2)),
            "noise_floor_dbfs": float(round(noise_dbfs, 1)),
            "f0_autocorr_hz": float(round(ac_f0, 1)),
            "f0_median_hz": float(round(yin_f0, 1)),  # primary F0 metric
            "f0_yin_hz": float(round(yin_f0, 1)),
            "f0_target_hz": [int(F0_TARGET[0]), int(F0_TARGET[1])],
            "lufs": float(round(lufs, 1)),
            "true_peak_dbfs": float(round(true_peak, 1)),
            "notes": notes,
            "model": "openbmb/VoxCPM2",
            "license": "Apache-2.0",
            "why": "VONG 5 KO (01/11/2026): Che do clone tu D3_SH de dat F0 muc tieu 78-88 Hz sau khi 56 take Voice Design deu >= 101 Hz.",
            "generated_at": datetime.datetime.now().isoformat(),
        }
        refs_json_path.write_text(
            json.dumps(records, ensure_ascii=False, indent=2, default=lambda o: float(o) if hasattr(o, "__float__") else str(o)),
            encoding="utf-8"
        )

    dt_total = (time.time() - t_all) / 60
    print("\n" + "=" * 76)
    print(f"HOÀN TẤT: {len(records)} take trong {OUT_DIR} (tổng thời gian {dt_total:.1f} phút)")
    print("=" * 76)


if __name__ == "__main__":
    main()
