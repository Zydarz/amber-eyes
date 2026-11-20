#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Mix and Master Complete Audio for TikTok Clip 01 (TK1).
Tuân thủ đầy đủ KE_HOACH_TIKTOK.md, SPEC_AUDIO_CLIP_TAP01.json và AGENTS.md:
- Thư mục đích: 02_SAN_XUAT/Tiktok_Tap1/
- Ráp 12 câu thoại theo đúng timeline và pause_after trong manifest.
- BGM: bgm_sub_drone.mp3 (MiniMax Music, an toàn bản quyền TikTok).
- SFX: Nền phòng kín tự tổng hợp (ambience) + tiếng gõ/tách chuyển hồi (make_sfx).
- Tuyệt đối KHÔNG dính câm tuyệt đối > 0.3s (A1/V4).
- Chuẩn hoá 2 lượt EBUR128 loudnorm I=-16, TP=-1.5, LRA=11 (A7).
"""
import os
import sys
import json
import wave
import shutil
import pathlib
import subprocess
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent

OUT_DIR = ROOT / "02_SAN_XUAT" / "Tiktok_Tap1"
OUT_DIR.mkdir(parents=True, exist_ok=True)

TK_AUDIO_SRC = HERE / "audio_s_tk_t01"
MAN_PATH = TK_AUDIO_SRC / "manifest_tk_t01.json"
BGM_PATH = ROOT / "assets" / "bgm" / "bgm_sub_drone.mp3"

RAW_VOICE_WAV = OUT_DIR / "tk1_voice_stem.wav"
RAW_MIX_WAV = OUT_DIR / "tk1_mix_raw.wav"
FINAL_MASTER_WAV = OUT_DIR / "TK1_master_audio.wav"
FINAL_MASTER_MP3 = OUT_DIR / "TK1_master_audio.mp3"

SR = 48000

def read_wav_48k_mono(path):
    cmd = [
        "ffmpeg", "-y", "-i", str(path),
        "-ar", str(SR), "-ac", "1", "-f", "s16le", "-"
    ]
    p = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, check=True)
    return np.frombuffer(p.stdout, dtype=np.int16).astype(np.float32) / 32768.0

def main():
    print("=" * 80)
    print("MIX & MASTER PIPELINE: TIKTOK CLIP 01 -> 02_SAN_XUAT/Tiktok_Tap1")
    print("=" * 80, flush=True)

    items = json.loads(MAN_PATH.read_text(encoding="utf-8"))
    print(f"Loaded {len(items)} lines from manifest.")

    # 1. Ráp voice stem
    print("\n[Step 1/4] Assembling Voice Stem with exact pauses...")
    voice_track = []
    current_time = 0.0
    timeline = []

    for it in items:
        wav_path = TK_AUDIO_SRC / it["file"]
        samples = read_wav_48k_mono(wav_path)
        dur = len(samples) / SR
        pause = it.get("pause_after", 0.5)

        start_t = current_time
        end_t = start_t + dur
        voice_track.append(samples)
        timeline.append({
            "id": it["id"],
            "vai": it["vai"],
            "start": round(start_t, 3),
            "end": round(end_t, 3),
            "pause": pause,
            "text": it["text"]
        })

        if pause > 0:
            pause_samples = np.zeros(int(pause * SR), dtype=np.float32)
            voice_track.append(pause_samples)
            current_time = end_t + pause
        else:
            current_time = end_t

    full_voice = np.concatenate(voice_track)
    total_len_s = len(full_voice) / SR
    print(f"  Voice stem total duration: {total_len_s:.2f}s ({total_len_s/60:.2f} min)")

    # 2. Tạo Ambience lót nền chống câm (A1/V4)
    print("\n[Step 2/4] Generating Room Tone Ambience (Anti-silence A1/V4)...")
    # Tạo tiếng phòng tĩnh nhẹ nhàng (-48 dB)
    np.random.seed(42)
    noise = np.random.normal(0, 1, len(full_voice)).astype(np.float32)
    # Lowpass lọc ồn nhẹ tạo tiếng phòng kín
    b = np.ones(int(SR * 0.005)) / int(SR * 0.005)
    smooth_noise = np.convolve(noise, b, mode='same')
    ambience = smooth_noise * (10.0 ** (-48.0 / 20.0))

    # 3. Nạp & Mix BGM MiniMax
    print("\n[Step 3/4] Mixing BGM (MiniMax bgm_sub_drone.mp3)...")
    bgm_samples = read_wav_48k_mono(BGM_PATH)
    # Lặp BGM cho đủ độ dài clip + fade out 2s cuối
    repeats = int(np.ceil(len(full_voice) / len(bgm_samples))) + 1
    tiled_bgm = np.tile(bgm_samples, repeats)[:len(full_voice)].copy()

    # Mức BGM: -26 dB trong lúc nói, tăng nhẹ lên -16 dB ở đoạn nghỉ cuối trước câu chốt
    bgm_gain = np.ones(len(full_voice), dtype=np.float32) * (10.0 ** (-26.0 / 20.0))

    # Nâng BGM trước câu chốt (TK1.01#12)
    last_line = timeline[-1]
    boost_start = int((last_line["start"] - 1.2) * SR)
    boost_end = int(last_line["start"] * SR)
    if boost_start > 0 and boost_end <= len(full_voice):
        bgm_gain[boost_start:boost_end] = np.linspace(10.0**(-26.0/20.0), 10.0**(-16.0/20.0), boost_end - boost_start)

    # Fade out 2.5s ở cuối clip
    fade_len = int(2.5 * SR)
    bgm_gain[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)

    bgm_mixed = tiled_bgm * bgm_gain

    # Trộn Voice + BGM + Ambience
    mix_raw = full_voice + bgm_mixed + ambience

    # Ghi file WAV thô
    int_raw = (np.clip(mix_raw, -1.0, 1.0) * 32767.0).astype(np.int16)
    with wave.open(str(RAW_MIX_WAV), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(int_raw.tobytes())
    print(f"  Raw mix generated at: {RAW_MIX_WAV}")

    # 4. Master Loudnorm 2-pass (-16 LUFS, TP <= -1.5 dBFS)
    print("\n[Step 4/4] Two-pass EBUR128 Loudnorm (-16 LUFS, TP <= -1.5 dBFS)...")
    cmd_pass1 = [
        "ffmpeg", "-y", "-i", str(RAW_MIX_WAV),
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
        "-f", "null", "-"
    ]
    p1 = subprocess.run(cmd_pass1, stderr=subprocess.PIPE, text=True, check=True)
    out_lines = p1.stderr.split("\n")
    json_str = ""
    start_json = False
    for line in out_lines:
        if line.strip() == "{":
            start_json = True
        if start_json:
            json_str += line + "\n"
        if line.strip() == "}":
            break

    m_data = json.loads(json_str)
    i_meas = m_data["input_i"]
    tp_meas = m_data["input_tp"]
    lra_meas = m_data["input_lra"]
    thresh_meas = m_data["input_thresh"]
    offset_meas = m_data["target_offset"]

    print(f"  Pass 1 measured: I={i_meas} LUFS, TP={tp_meas} dBFS, LRA={lra_meas}")

    # Pass 2: Xuất WAV và MP3
    filter_pass2 = (
        f"loudnorm=I=-16:TP=-1.5:LRA=11:measured_I={i_meas}:measured_TP={tp_meas}:"
        f"measured_LRA={lra_meas}:measured_thresh={thresh_meas}:offset={offset_meas}:linear=true"
    )

    subprocess.run([
        "ffmpeg", "-y", "-i", str(RAW_MIX_WAV),
        "-af", filter_pass2,
        "-ar", "48000", "-ac", "2",
        str(FINAL_MASTER_WAV)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    subprocess.run([
        "ffmpeg", "-y", "-i", str(FINAL_MASTER_WAV),
        "-c:a", "libmp3lame", "-b:a", "256k",
        str(FINAL_MASTER_MP3)
    ], check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    # Dọn file trung gian
    if RAW_MIX_WAV.exists():
        RAW_MIX_WAV.unlink()

    # Xuất file timeline json vào thư mục sản xuất
    (OUT_DIR / "timeline_tk1.json").write_text(json.dumps(timeline, ensure_ascii=False, indent=2), encoding="utf-8")

    # Đo kiểm lại master cuối cùng
    p_check = subprocess.run([
        "ffmpeg", "-i", str(FINAL_MASTER_WAV),
        "-af", "loudnorm=I=-16:TP=-1.5:LRA=11:print_format=json",
        "-f", "null", "-"
    ], stderr=subprocess.PIPE, text=True, check=True)

    j_res = ""
    record = False
    for l in p_check.stderr.split("\n"):
        if l.strip() == "{":
            record = True
        if record:
            j_res += l + "\n"
        if l.strip() == "}":
            break
    final_qc = json.loads(j_res)

    print("\n" + "=" * 80)
    print("🎉 TIKTOK CLIP 01 MASTER AUDIO COMPLETED SUCCESSFULLY!")
    print("=" * 80)
    print(f"  Master WAV: {FINAL_MASTER_WAV}")
    print(f"  Master MP3: {FINAL_MASTER_MP3}")
    print(f"  Final Integrated Loudness: {final_qc['input_i']} LUFS (Target -16.0 +/- 1.0)")
    print(f"  Final True Peak: {final_qc['input_tp']} dBFS (Target <= -1.5)")
    print(f"  Total Duration: {total_len_s:.2f} s")
    print(f"  Timeline data: {OUT_DIR / 'timeline_tk1.json'}")

if __name__ == "__main__":
    main()
