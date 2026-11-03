#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Production Audio Generator for Episode 03 Japanese using Higgs Audio v3 on MLX.
Tuân thủ đầy đủ QUY_TAC_HIGGS_MAC.md, QUY_TAC_AUDIO_HIGGS.md và AGENTS.md:
- Pre-encodes 5 VoxCPM2 reference voices once (H, D, C, N1, N2) — Rule M1.
- Tách biệt TTS và QC (Rule M2).
- Tự động cắt đuôi câm > 0.8s @ -45 dBFS (Rule M3).
- CẤM mọi thẻ <|emotion:...|> (Rule M4).
- Đo F0 trung vị và kiểm tra G9 (ngưỡng >= 4 nửa cung).
- Chạy Whisper ASR (Japanese) và tính CER với ja_cer (ngưỡng 2%).
- Sinh bản thay thế (variant 1) cho các câu CER > 2%.
- Tính timeline chính xác, xuất srt và báo cáo CanNghe.
"""
import os
import sys

os.environ["AE_EP"] = "03"
os.environ["AE_LANG"] = "ja"
os.environ["AE_AUDIO_DIR"] = "audio_s_higgs"

import json
import time
import wave
import hashlib
import pathlib
import subprocess
import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))
import ja_cer
import edition as ED

from mlx_audio.tts.utils import load as load_higgs
from mlx_audio.audio_io import write as audio_write
from transformers import pipeline

PAYLOAD_PATH = HERE / "kaggle_higgs" / "higgs_payload_JA_t03.json"
DS_DIR = HERE / "kaggle_higgs" / "dataset_voxcpm2_ja"
AUDIO_OUT = HERE / "audio_s_higgs_JA_t03"
AUDIO_OUT.mkdir(parents=True, exist_ok=True)
RAW_OUT = HERE / "kaggle_higgs" / "out_higgs_prod_JA_t03"
RAW_OUT.mkdir(parents=True, exist_ok=True)

ROLE_REF_MAP = {
    "H": ("H_JA.wav", "H_JA.txt"),
    "D": ("D_JA.wav", "D_JA.txt"),
    "C": ("C_JA.wav", "C_JA.txt"),
    "N1": ("N1_JA.wav", "N1_JA.txt"),
    "N2": ("N2_JA.wav", "N2_JA.txt"),
}

def fname(sid):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return f"s{a}_{b}_{int(k):02d}.wav"

def raw_fname(sid, role, ref, var):
    ma, k = sid.split("#")
    a, b = ma.split(".")
    stem = pathlib.Path(ref).stem
    return f"{a}_{b}_{k}_{role}_{stem}_t0.8_s{var}.wav"

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
    """Quy tắc M3: cắt đuôi câm < -45 dB dài > 0.8s, giữ lại 0.3s + 30ms fade."""
    with wave.open(str(wav_path), "rb") as wf:
        sr = wf.getframerate()
        frames = wf.readframes(wf.getnframes())
        data = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
    
    total_dur = len(data) / sr
    hop = int(sr * 0.02)
    thresh = 10.0 ** (threshold_db / 20.0)
    
    # scan from tail backwards
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
            # 30 ms fade out
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

def main():
    print("=" * 80)
    print("PRODUCTION PIPELINE: HIGGS AUDIO V3 — TAP 03 JA (JAPANESE)")
    print("=" * 80, flush=True)

    payload = json.loads(PAYLOAD_PATH.read_text(encoding="utf-8"))
    items = payload["items"]
    print(f"Total sentences: {len(items)}", flush=True)

    print("\n[Step 1/5] Loading Higgs Audio v3 Model on Apple Silicon...", flush=True)
    t0 = time.time()
    model = load_higgs("bosonai/higgs-audio-v3-tts-4b")
    print(f"Model loaded in {time.time()-t0:.2f}s", flush=True)

    print("\n[Step 2/5] Pre-encoding 5 VoxCPM2 Reference Voices (Rule M1)...", flush=True)
    ref_cache = {}
    for role, (wname, tname) in ROLE_REF_MAP.items():
        wpath = DS_DIR / wname
        tpath = DS_DIR / tname
        t_ref = tpath.read_text(encoding="utf-8").strip()
        t_enc = time.time()
        codes = model.encode_reference_audio(str(wpath))
        ref_cache[role] = (codes, t_ref, wname)
        print(f"  Role {role:2s} -> {wname} encoded in {time.time()-t_enc:.2f}s", flush=True)

    print("\n[Step 3/5] Generating Sentence Audio (Variant 0)...", flush=True)
    man_path = AUDIO_OUT / "higgs_manifest.json"
    man = json.loads(man_path.read_text(encoding="utf-8")) if man_path.exists() else {}

    for idx, it in enumerate(items):
        sid = it["id"]
        role = it["role"]
        text = it["text"]
        out_name = fname(sid)
        dst_wav = AUDIO_OUT / out_name
        codes, ref_text, ref_name = ref_cache[role]
        raw_name = raw_fname(sid, role, ref_name, 0)
        raw_wav = RAW_OUT / raw_name

        if dst_wav.exists() and dst_wav.stat().st_size > 4000 and sid in man:
            print(f"  [{idx+1:03d}/{len(items)}] {sid} ({role}) -> ALREADY EXISTS: {out_name}", flush=True)
            continue

        seed = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|0".encode()).hexdigest()[:8], 16)
        print(f"  [{idx+1:03d}/{len(items)}] {sid} ({role}) [seed={seed}]: '{text[:50]}...'", flush=True)
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
        gen_time = time.time() - t_start

        # Save to both production audio folder and raw output folder
        audio_write(str(dst_wav), res[0].audio, res[0].sample_rate)
        audio_write(str(raw_wav), res[0].audio, res[0].sample_rate)
        trim_silence_tail(dst_wav)
        trim_silence_tail(raw_wav)

        f0 = estimate_f0(dst_wav)
        dur = getattr(res[0], "audio_duration", "N/A")
        print(f"      -> {out_name} (dur: {dur}, F0: {f0:.1f}Hz, gen: {gen_time:.1f}s)", flush=True)

        man[sid] = {
            "id": sid,
            "role": role,
            "ref_wav": ref_name,
            "text": text,
            "file": out_name,
            "seed": seed,
            "variant": 0,
            "f0": f0,
            "gen_time": gen_time
        }
        man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")

    print("\n[Step 4/5] Transcribing with Whisper & Measuring Quality (CER)...", flush=True)
    asr_pipe = pipeline("automatic-speech-recognition", model="openai/whisper-base")
    high_cer = []
    cer_rows = []

    for idx, it in enumerate(items):
        sid = it["id"]
        role = it["role"]
        orig_text = it["text"]
        wav_path = AUDIO_OUT / fname(sid)
        asr_res = asr_pipe(str(wav_path), return_timestamps=True, generate_kwargs={"language": "japanese"})["text"].strip()
        c = ja_cer.cer_pair(orig_text, asr_res)
        f0 = man.get(sid, {}).get("f0", 0.0)

        cer_rows.append({
            "id": sid,
            "role": role,
            "file": fname(sid),
            "text": orig_text,
            "asr": asr_res,
            "cer": c,
            "f0": f0
        })

        if c > 0.02:
            high_cer.append((sid, role, c, orig_text, asr_res))
            print(f"  [WARN > 2%] {sid} ({role}): CER={c*100:.2f}% | '{orig_text[:40]}' -> '{asr_res[:40]}'", flush=True)

    (HERE / "higgs_cer_rows_JA_t03.json").write_text(
        json.dumps(cer_rows, ensure_ascii=False, indent=1), encoding="utf-8")

    # Generate round 2 (variant 1) for sentences with CER > 2%
    if high_cer:
        print(f"\n[Step 4b] Re-generating {len(high_cer)} sentences with CER > 2% (Variant 1)...", flush=True)
        for sid, role, old_cer, orig_text, _ in high_cer:
            codes, ref_text, ref_name = ref_cache[role]
            seed1 = int(hashlib.sha256(f"{sid}|{role}|{ref_name}|0.8|1".encode()).hexdigest()[:8], 16)
            dst_wav = AUDIO_OUT / fname(sid)
            raw_v1 = RAW_OUT / raw_fname(sid, role, ref_name, 1)

            res = list(model.generate(
                text=orig_text,
                ref_audio_codes=codes,
                ref_text=ref_text,
                temperature=0.8,
                top_p=0.95,
                seed=seed1,
                fade_in_ms=30.0,
                fade_out_ms=15.0
            ))
            audio_write(str(raw_v1), res[0].audio, res[0].sample_rate)
            trim_silence_tail(raw_v1)
            asr1 = asr_pipe(str(raw_v1), return_timestamps=True, generate_kwargs={"language": "japanese"})["text"].strip()
            c1 = ja_cer.cer_pair(orig_text, asr1)
            print(f"  {sid} ({role}): Take 0 CER={old_cer*100:.2f}% vs Take 1 CER={c1*100:.2f}%", flush=True)
            if c1 < old_cer:
                audio_write(str(dst_wav), res[0].audio, res[0].sample_rate)
                trim_silence_tail(dst_wav)
                print(f"      -> Chose Take 1 (CER improved to {c1*100:.2f}%)", flush=True)
                man[sid]["seed"] = seed1
                man[sid]["variant"] = 1
                man[sid]["f0"] = estimate_f0(dst_wav)
                # update cer_rows
                for r in cer_rows:
                    if r["id"] == sid:
                        r["cer"] = c1
                        r["asr"] = asr1
                        r["f0"] = man[sid]["f0"]
                        break

        man_path.write_text(json.dumps(man, ensure_ascii=False, indent=1), encoding="utf-8")
        (HERE / "higgs_cer_rows_JA_t03.json").write_text(
            json.dumps(cer_rows, ensure_ascii=False, indent=1), encoding="utf-8")

    # Measure F0 and G9 semitones
    print("\n[Step 4c] Evaluating Pitch Separation (G9 Rule)...", flush=True)
    role_f0 = {}
    for r in cer_rows:
        role = r["role"]
        f0 = r["f0"]
        if f0 > 0:
            role_f0.setdefault(role, []).append(f0)
    
    medians = {role: float(np.median(vals)) for role, vals in role_f0.items()}
    for role, med in sorted(medians.items(), key=lambda x: x[1]):
        print(f"  Role {role:2s}: median F0 = {med:.1f} Hz (n={len(role_f0[role])})")
    
    if "D" in medians and "H" in medians:
        dh_semitones = 12.0 * np.log2(medians["H"] / medians["D"])
        print(f"  Delta D -> H: {dh_semitones:.2f} semitones (Target >= 4.0 nc) {'✅' if dh_semitones >= 4.0 else '⚠ TRƯỢT'}")
    if "H" in medians and "C" in medians:
        hc_semitones = 12.0 * np.log2(medians["C"] / medians["H"])
        print(f"  Delta H -> C: {hc_semitones:.2f} semitones (Target >= 4.0 nc) {'✅' if hc_semitones >= 4.0 else '⚠ TRƯỢT'}")

    print("\n[Step 5/5] Computing Episode Timeline & Generating Deliverables...", flush=True)
    SR = 44100
    FIRST_VOICE = 23.0
    GAP_ACT = 2.0
    GAP_SPEAKER = 0.65
    GAP_SENT = 0.40
    GAP_Q = 0.60
    MAX_PAUSE = 3.0

    act_data = json.loads(ED.EP["acting"].read_text(encoding="utf-8"))
    PAUSE_AFTER = act_data.get("_pause_after", {})

    script = json.loads(ED.EP["script"].read_text(encoding="utf-8"))

    def get_dur(p):
        with wave.open(str(p), "rb") as w:
            return w.getnframes() / w.getframerate()

    durs = {sid: get_dur(AUDIO_OUT / fname(sid)) for sid in man}

    t = FIRST_VOICE
    items_tl, markers = [], [{"type": "INTRO", "start": 0.0, "end": 22.41}]
    acts = {}
    cur_act = None
    pending = None

    for e in script:
        act = e["act"]
        if cur_act is not None and act != cur_act:
            markers.append({"type": "ACT", "act": act, "start": round(t, 3), "end": round(t + GAP_ACT, 3)})
            t += GAP_ACT
            pending = None
        if act not in acts:
            acts[act] = [t, t]
        cur_act = act
        if e["kind"] == "NGHI":
            sec = min(e["sec"], MAX_PAUSE)
            markers.append({"type": "NGHI", "id": e["id"], "start": round(t, 3), "end": round(t + sec, 3), "desc": e.get("desc", "")})
            t += sec
            pending = None
        elif e["kind"] in ("SFX", "BGM"):
            markers.append({"type": e["kind"], "id": e["id"], "at": round(t, 3), "desc": e.get("desc", "")})
        else:
            role = man[e["sentences"][0]["id"]]["role"]
            if pending:
                g = GAP_SPEAKER if pending[0] != role else GAP_SENT
                if pending[1].rstrip("”\" ").endswith("?"):
                    g = max(g, GAP_Q)
                t += g
            for k, s in enumerate(e["sentences"]):
                d = durs[s["id"]]
                disp = s["text"]
                items_tl.append({"id": s["id"], "element": e["id"], "act": act, "role": role,
                                 "start": round(t, 3), "end": round(t + d, 3), "text": disp})
                t += d
                t += PAUSE_AFTER.get(s["id"], 0.0)
                if k < len(e["sentences"]) - 1:
                    t += GAP_Q if s["text"].rstrip("”\" ").endswith("?") else GAP_SENT
            pending = (role, e["sentences"][-1]["text"])
        acts[act][1] = t

    end_voice = t
    total = end_voice + 1.0 + 5.0 + 3.0

    timeline_out = {
        "total": round(total, 3),
        "intro": 22.41,
        "items": items_tl,
        "markers": markers,
        "acts": {str(k): [round(a, 3), round(b, 3)] for k, (a, b) in acts.items()}
    }
    ED.w("timeline_s.json").write_text(json.dumps(timeline_out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Saved timeline to {ED.w('timeline_s.json')} (total={total:.1f}s)", flush=True)

    # Subtitles
    import subtitles
    subtitles.main()
    print("Generated subtitles via subtitles.py", flush=True)

    # CanNghe report
    can_nghe_lines = [
        "# Câu cần nghe — Tập 03 JA (Higgs) — 02/11/2026\n",
        f"Dự kiến Master: `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp3` · {total:.1f} s (~{total/60:.1f} min) · {len(items_tl)} câu · lời đầu {items_tl[0]['start']} s · lời cuối {end_voice:.1f} s\n",
        "| Mốc | Câu | Vai | CER | Câu gốc | ASR nghe được | Ghi chú |",
        "|---|---|---|---:|---|---|---|"
    ]
    time_map = {it["id"]: it["start"] for it in items_tl}
    for sid in sorted(time_map.keys(), key=lambda x: time_map[x]):
        r = next((row for row in cer_rows if row["id"] == sid), None)
        if not r:
            continue
        c = r["cer"]
        if c > 0.02:
            start_s = time_map[sid]
            m = int(start_s // 60)
            s = start_s % 60
            time_str = f"{m}:{s:05.2f}"
            orig = r["text"].replace("|", r"\|")
            asr = r["asr"].replace("|", r"\|")
            can_nghe_lines.append(f"| {time_str} | {sid} | {r['role']} | {c*100:.1f}% | {orig} | {asr} | Nghe xác nhận |")

    can_nghe_p = ROOT / "02_SAN_XUAT" / "Tap03_JA" / "xuat_ban" / "CanNghe_Tap03_JA_higgs.md"
    can_nghe_p.write_text("\n".join(can_nghe_lines) + "\n", encoding="utf-8")
    print(f"Wrote CanNghe report to {can_nghe_p}", flush=True)

    print("\n🎉 DONE! ALL STEPS COMPLETED FOR TAP 03 JA!", flush=True)

if __name__ == "__main__":
    main()
