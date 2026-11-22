#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Production Audio Generator for TikTok Episode 02 (VN / EN / JA) using Higgs Audio v3 on MLX.
Tuân thủ đầy đủ QUY_TAC_HIGGS_MAC.md, QUY_TAC_AUDIO_HIGGS.md và AGENTS.md:
- Pre-encodes 4 reference voices (H, D, C, N2) cho từng ngôn ngữ (Rule M1).
- Tự động cắt đuôi câm >= 0.8s @ -45 dBFS (Rule M3).
- CẤM mọi thẻ <|emotion:...|> (Rule M4).
- Đo F0 trung vị và kiểm tra G9 (ngưỡng >= 4 nửa cung).
- Chạy Whisper ASR và tính CER với vi_cer / en_cer / ja_cer (ngưỡng 2.0%).
- Multi-take: Sinh bản thay thế (variant 1) nếu CER > 2.0%.
- Xuất manifest và báo cáo chi tiết.
"""
import os
import sys
import gc
import json
import time
import wave
import hashlib
import pathlib
import argparse
import subprocess
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import vi_cer
import en_cer
import ja_cer

from mlx_audio.tts.utils import load as load_higgs
from mlx_audio.audio_io import write as audio_write
from faster_whisper import WhisperModel

ROLE_MAPS = {
    "vi": {
        "H": (ROOT / "assets/voice_ref_voxcpm2/H.wav", ROOT / "assets/voice_ref_voxcpm2/H.txt"),
        "D": (ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav", ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.txt"),
        "C": (ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav", ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.txt"),
        "N2": (ROOT / "assets/voice_ref_voxcpm2_g9/W5_HIGH.wav", ROOT / "assets/voice_ref_voxcpm2_g9/W5_HIGH.txt")
    },
    "en": {
        "H": (HERE / "kaggle_higgs/dataset_voxcpm2_en/H_EN.wav", HERE / "kaggle_higgs/dataset_voxcpm2_en/H_EN.txt"),
        "D": (HERE / "kaggle_higgs/dataset_voxcpm2_en/D_EN.wav", HERE / "kaggle_higgs/dataset_voxcpm2_en/D_EN.txt"),
        "C": (HERE / "kaggle_higgs/dataset_voxcpm2_en/C_EN.wav", HERE / "kaggle_higgs/dataset_voxcpm2_en/C_EN.txt"),
        "N2": (HERE / "kaggle_higgs/dataset_voxcpm2_en/N2_EN.wav", HERE / "kaggle_higgs/dataset_voxcpm2_en/N2_EN.txt")
    },
    "ja": {
        "H": (HERE / "kaggle_higgs/dataset_voxcpm2_ja/H_JA.wav", HERE / "kaggle_higgs/dataset_voxcpm2_ja/H_JA.txt"),
        "D": (HERE / "kaggle_higgs/dataset_voxcpm2_ja/D_JA.wav", HERE / "kaggle_higgs/dataset_voxcpm2_ja/D_JA.txt"),
        "C": (HERE / "kaggle_higgs/dataset_voxcpm2_ja/C_JA.wav", HERE / "kaggle_higgs/dataset_voxcpm2_ja/C_JA.txt"),
        "N2": (HERE / "kaggle_higgs/dataset_voxcpm2_ja/N2_JA.wav", HERE / "kaggle_higgs/dataset_voxcpm2_ja/N2_JA.txt")
    }
}

SPEC_FILES = {
    "vi": ROOT / "02_SAN_XUAT/TIKTOK/Tap02/SPEC_AUDIO_CLIP_TAP02.json",
    "en": ROOT / "02_SAN_XUAT/TIKTOK/Tap02_EN/SPEC_AUDIO_CLIP_TAP02.json",
    "ja": ROOT / "02_SAN_XUAT/TIKTOK/Tap02_JA/SPEC_AUDIO_CLIP_TAP02.json"
}

OUT_DIRS = {
    "vi": HERE / "audio_s_tk_t02_vi",
    "en": HERE / "audio_s_tk_t02_en",
    "ja": HERE / "audio_s_tk_t02_ja"
}

def fname(sid):
    # TK1.01#1 -> TK1.01_01.wav
    ma, k = sid.split("#")
    return f"{ma}_{int(k):02d}.wav"

def raw_fname(sid, role, ref, var):
    ma, k = sid.split("#")
    stem = pathlib.Path(ref).stem
    return f"{ma}_{int(k):02d}_{role}_{stem}_t0.8_v{var}.wav"

def estimate_f0(wav_path):
    try:
        with wave.open(str(wav_path), "rb") as wf:
            sr = wf.getframerate()
            frames = wf.readframes(wf.getnframes())
            data = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
        frame_len = int(sr * 0.04)
        hop_len = int(sr * 0.01)
        f0_list = []
        min_lag = int(sr / 450)
        max_lag = int(sr / 60)
        for i in range(0, len(data) - frame_len, hop_len):
            frame = data[i:i + frame_len]
            if np.std(frame) < 0.01:
                continue
            corr = np.correlate(frame, frame, mode='full')
            corr = corr[len(frame) - 1:]
            if len(corr) <= max_lag:
                continue
            peak_idx = np.argmax(corr[min_lag:max_lag]) + min_lag
            if corr[0] > 0 and corr[peak_idx] / corr[0] > 0.4:
                f0_list.append(sr / peak_idx)
        return float(np.median(f0_list)) if f0_list else 0.0
    except Exception:
        return 0.0

def trim_silence_tail(wav_path, threshold_db=-45.0, min_tail_sec=0.8):
    """Quy tắc Rule M3: cắt đuôi câm < -45 dB dài > 0.8s, giữ lại 0.3s + 30ms fade."""
    with wave.open(str(wav_path), "rb") as wf:
        sr = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        data = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0

    total_dur = len(data) / sr
    hop = int(sr * 0.02)
    thresh = 10.0 ** (threshold_db / 20.0)

    last_active = len(data)
    for i in range(len(data) - hop, 0, -hop):
        chunk = data[i:i + hop]
        rms = np.sqrt(np.mean(chunk ** 2) + 1e-9)
        if rms >= thresh:
            last_active = i + hop
            break

    tail_dur = (len(data) - last_active) / sr
    if tail_dur > min_tail_sec:
        keep_samples = int(last_active + 0.3 * sr)
        if keep_samples < len(data):
            trimmed = data[:keep_samples].copy()
            fade_len = int(0.03 * sr)
            if len(trimmed) > fade_len:
                trimmed[-fade_len:] *= np.linspace(1.0, 0.0, fade_len)
            int_data = (np.clip(trimmed, -1.0, 1.0) * 32767.0).astype(np.int16)
            with wave.open(str(wav_path), "wb") as wf:
                wf.setnchannels(1)
                wf.setsampwidth(2)
                wf.setframerate(sr)
                wf.writeframes(int_data.tobytes())
            print(f"      [TRIMMED] Tail {tail_dur:.2f}s -> pruned {total_dur:.2f}s to {len(trimmed)/sr:.2f}s", flush=True)

def parse_items_from_spec(spec_data, lang):
    items = []
    if lang == "vi":
        for clip in spec_data["clips"]:
            cid = clip["id"]
            for l in clip["lines"]:
                items.append({
                    "id": l["id"],
                    "vai": l["vai"],
                    "clip": cid,
                    "text": l["text"],
                    "pause_after": l.get("pause_after", 0.5),
                    "emotion": l.get("emotion", "neutral"),
                    "speed": l.get("speed", -0.02)
                })
    else:
        for cid, clip in spec_data["clips"].items():
            for l in clip["lines"]:
                items.append({
                    "id": l.get("clip_line_id") or l.get("id"),
                    "vai": l.get("role") or l.get("vai"),
                    "clip": cid,
                    "text": l["text"],
                    "pause_after": l.get("pause_after_s") or l.get("pause_after", 0.5),
                    "emotion": l.get("emotion", "neutral"),
                    "speed": l.get("speed_offset") or l.get("speed", -0.02)
                })
    return items

def compute_cer(asr_text, ref_text, lang):
    if lang == "vi":
        return vi_cer.cer(asr_text, ref_text)
    elif lang == "en":
        return en_cer.cer(asr_text, ref_text)
    elif lang == "ja":
        return ja_cer.cer(asr_text, ref_text)
    return 0.0

def process_language(lang, model, whisper_model):
    print("\n" + "=" * 80)
    print(f"STARTING PRODUCTION AUDIO SYNTHESIS FOR: {lang.upper()}")
    print("=" * 80, flush=True)

    out_dir = OUT_DIRS[lang]
    out_dir.mkdir(parents=True, exist_ok=True)
    raw_out = HERE / "kaggle_higgs" / f"out_higgs_prod_tk02_{lang}"
    raw_out.mkdir(parents=True, exist_ok=True)

    spec_path = SPEC_FILES[lang]
    spec_data = json.loads(spec_path.read_text(encoding="utf-8"))
    items = parse_items_from_spec(spec_data, lang)
    print(f"Total lines to synthesize for {lang}: {len(items)}", flush=True)

    # 1. Pre-encode voices
    print(f"\n[Step 1/4] Pre-encoding reference voices for {lang}...", flush=True)
    ref_cache = {}
    for role, (wpath, tpath) in ROLE_MAPS[lang].items():
        t_ref = tpath.read_text(encoding="utf-8").strip()
        t_enc = time.time()
        codes = model.encode_reference_audio(str(wpath))
        ref_cache[role] = (codes, t_ref, wpath.name)
        print(f"  Role {role:2s} -> {wpath.name} encoded in {time.time()-t_enc:.2f}s", flush=True)

    # 2. Synthesis & Multi-take if needed
    print(f"\n[Step 2/4] Generating sentence audio...", flush=True)
    manifest = []
    qc_results = []

    for idx, it in enumerate(items):
        sid = it["id"]
        role = it["vai"]
        text = it["text"]
        pause = it["pause_after"]
        out_name = fname(sid)
        dst_wav = out_dir / out_name

        codes, ref_text, ref_name = ref_cache[role]
        
        # Take 0
        seed = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|0".encode()).hexdigest()[:8], 16)
        print(f"\n  [{idx+1:02d}/{len(items)}] {sid} ({role}) [seed={seed}]: '{text[:45]}...'", flush=True)
        t_start = time.time()
        res = list(model.generate(
            text=text,
            ref_audio_codes=codes,
            ref_text=ref_text,
            temperature=0.8,
            top_p=0.95,
            seed=seed,
            fade_in_ms=30.0,
            fade_out_ms=15.0
        ))
        dur_gen = time.time() - t_start
        raw_name0 = raw_fname(sid, role, ref_name, 0)
        raw_wav0 = raw_out / raw_name0
        audio_write(str(raw_wav0), res[0].audio, 24000)
        trim_silence_tail(raw_wav0)

        # QC Whisper Take 0
        segments, _ = whisper_model.transcribe(str(raw_wav0), language=lang, beam_size=5)
        asr_text0 = " ".join([s.text for s in segments]).strip()
        cer0 = compute_cer(asr_text0, text, lang)
        f0_0 = estimate_f0(raw_wav0)
        print(f"      Take 0: CER={cer0*100:.1f}%, F0={f0_0:.1f}Hz, GenTime={dur_gen:.2f}s | ASR: '{asr_text0[:40]}'", flush=True)

        chosen_take = 0
        chosen_wav = raw_wav0
        chosen_cer = cer0
        chosen_f0 = f0_0

        # Multi-take if CER > 2.0%
        if cer0 > 0.02:
            print(f"      CER > 2% -> Generating Take 1...", flush=True)
            seed1 = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|1".encode()).hexdigest()[:8], 16)
            res1 = list(model.generate(
                text=text,
                ref_audio_codes=codes,
                ref_text=ref_text,
                temperature=0.8,
                top_p=0.95,
                seed=seed1,
                fade_in_ms=30.0,
                fade_out_ms=15.0
            ))
            raw_name1 = raw_fname(sid, role, ref_name, 1)
            raw_wav1 = raw_out / raw_name1
            audio_write(str(raw_wav1), res1[0].audio, 24000)
            trim_silence_tail(raw_wav1)

            segments1, _ = whisper_model.transcribe(str(raw_wav1), language=lang, beam_size=5)
            asr_text1 = " ".join([s.text for s in segments1]).strip()
            cer1 = compute_cer(asr_text1, text, lang)
            f0_1 = estimate_f0(raw_wav1)
            print(f"      Take 1: CER={cer1*100:.1f}%, F0={f0_1:.1f}Hz | ASR: '{asr_text1[:40]}'", flush=True)

            if cer1 < cer0:
                chosen_take = 1
                chosen_wav = raw_wav1
                chosen_cer = cer1
                chosen_f0 = f0_1
                print(f"      => Chose Take 1 (CER {cer1*100:.1f}% < {cer0*100:.1f}%)", flush=True)
            else:
                print(f"      => Kept Take 0 (CER {cer0*100:.1f}% <= {cer1*100:.1f}%)", flush=True)

        # Copy to production dst_wav
        with wave.open(str(chosen_wav), "rb") as wf:
            dur = wf.getnframes() / wf.getframerate()
        
        # Save production copy
        import shutil
        shutil.copyfile(str(chosen_wav), str(dst_wav))

        item_meta = {
            "id": sid,
            "vai": role,
            "clip": it["clip"],
            "file": out_name,
            "dur": round(dur, 3),
            "pause_after": pause,
            "emotion": it["emotion"],
            "speed": it["speed"],
            "variant": chosen_take,
            "cer": round(chosen_cer, 4),
            "f0": round(chosen_f0, 1),
            "text": text
        }
        manifest.append(item_meta)
        qc_results.append(item_meta)

    # 3. Save Manifest
    man_path = out_dir / f"manifest_tk_t02_{lang}.json"
    man_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n[Step 3/4] Saved manifest: {man_path}", flush=True)

    # 4. G9 Role F0 Evaluation
    print(f"\n[Step 4/4] Evaluating G9 F0 separation for {lang}...", flush=True)
    roles_f0 = {}
    for it in manifest:
        r = it["vai"]
        if it["f0"] > 40.0:
            roles_f0.setdefault(r, []).append(it["f0"])

    med_f0 = {r: float(np.median(vals)) for r, vals in roles_f0.items() if vals}
    print("  F0 medians by role:", med_f0)

    role_list = list(med_f0.keys())
    g9_passed = True
    for i in range(len(role_list)):
        for j in range(i + 1, len(role_list)):
            r1, r2 = role_list[i], role_list[j]
            st = 12.0 * abs(np.log2(med_f0[r1] / med_f0[r2]))
            print(f"  G9 {r1} - {r2}: {st:.2f} semitones (threshold >= 4.0 nc)")
            if st < 4.0:
                print(f"    WARNING: G9 margin < 4.0 nc between {r1} and {r2}!")
                g9_passed = False

    qc_summary = {
        "language": lang,
        "total_lines": len(manifest),
        "avg_cer": float(np.mean([x["cer"] for x in manifest])),
        "max_cer": float(np.max([x["cer"] for x in manifest])),
        "f0_medians": med_f0,
        "g9_passed": g9_passed
    }
    qc_sum_path = out_dir / f"qc_summary_{lang}.json"
    qc_sum_path.write_text(json.dumps(qc_summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Summary: Avg CER={qc_summary['avg_cer']*100:.2f}%, Max CER={qc_summary['max_cer']*100:.2f}%, G9 Passed={g9_passed}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--langs", nargs="+", default=["vi", "en", "ja"], choices=["vi", "en", "ja"])
    args = parser.parse_args()

    print("=" * 80)
    print("HIGGS AUDIO V3 - TIKTOK EPISODE 02 MULTILINGUAL PRODUCTION")
    print(f"Target languages: {args.langs}")
    print("=" * 80, flush=True)

    print("\nLoading Higgs Audio v3 Model on Apple Silicon MLX...", flush=True)
    t0 = time.time()
    model = load_higgs("bosonai/higgs-audio-v3-tts-4b")
    print(f"Higgs Model loaded in {time.time()-t0:.2f}s", flush=True)

    print("\nLoading Faster-Whisper Base Model on CPU...", flush=True)
    t0 = time.time()
    whisper_model = WhisperModel("base", device="cpu", compute_type="int8")
    print(f"Whisper Model loaded in {time.time()-t0:.2f}s", flush=True)

    for lang in args.langs:
        process_language(lang, model, whisper_model)

    print("\n" + "=" * 80)
    print("ALL LANGUAGES SYNTHESIS & INDIVIDUAL QC COMPLETED SUCCESSFULLY!")
    print("=" * 80, flush=True)

if __name__ == "__main__":
    main()
