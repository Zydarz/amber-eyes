#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh clip tham chieu VoxCPM2 MOI cho G9 (Tập 02, Higgs Audio v3) — CACH DO THANG.

VIET: chay tren Mac mini (MPS). KHONG chay tren Windows — VoxCPM2 can MPS/Apple Silicon.

Van de G9: vai H (clone 130 Hz) va vai D (clone 121 Hz) chi cach 0.23 nua cung, can >= 4.
Higgs KHONG giu F0 cua clip tham chieu (H 108->130 +20%, D 128->121 -8%) => 2 vai
nam tro ve cung mot vung ~125 Hz.

Cach sua: MO MOT CLIP THAM CHIEU CO F0 KHAC XA. F0 cua clip VoxCPM2 duoc dieu khien
bang TU KHOA CAO DO trong `control` (khong phai bang tham so cua script).
Bang tu khoa -> F0 thuc do duoc trong bo 7 clip hien tai:
    nam: "low-pitched"                    -> 108 Hz  (H)
         "mid-low-pitched"                -> 128 Hz  (D)
         "lower mid-pitched"              -> 137 Hz  (W4)
         "medium-pitched"                 -> 162 Hz  (W3)
    nu : "mid-pitched"                    -> 200-210 Hz (W2/C)
         "higher-pitched"                 -> 252 Hz  (W1)
=> Muon cao hon: dung "higher-pitched"/"high-pitched"/"soprano" (tu nhe len manh)
=> Muon thap hon: dung "very low-pitched"/"bass"/"sub-bass"

Script nay D0 THANG: voi moi vai, thu cac `control_variants` theo thu tu tu nhe -> manh,
sinh 1 take moi bien, do F0, DUNG NGAY khi co take nao trong dai muc tieu.
Neu het thang ma chua trong dai, sinh them take cua bien dao gan nhat.

4 VAI (muc tieu F0 cua CLIP THAM CHIEU, do bang f0_median):
    M_LOW   80-92 Hz    nam  -> vai H  (clone <= 97 Hz de cach D >= 4 nua cung)
    M_HIGH  168-182 Hz  nam  -> vai D  (clone >= 165 Hz de cach H >= 4 nua cung)
    W6_LOW  148-162 Hz  nu   -> vai N1 (clone <= 163 Hz de cach C VA N2 deu >= 4 nc)
    W5_HIGH 258-276 Hz  nu   -> phuong an doi: N1 cao, N2 thap (W6_LOW)

CHAY:
    /Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py

Xuat:
    .work/voxcpm_raw/<ROLE>/<ROLE>_takeNN.wav       (48 kHz ban goc)
    .work/voxcpm_raw/<ROLE>/takes.json
    assets/voice_ref_voxcpm2_g9/<ROLE>.wav           (24 kHz mono, -18 LUFS)
    assets/voice_ref_voxcpm2_g9/<ROLE>.txt
    assets/voice_ref_voxcpm2_g9/refs.json

CHE DO UNG VIEN (--candidates, 30/10/2026 — tao lai giong D + C):
    python3 .work/voxcpm_generate_g9.py --manifest .work/voxcpm_refs_manifest_dc.json \
        --out assets/voice_ref_voxcpm2_dc --candidates 3
    -> KHONG dung o take dau trung dai: moi bac control x N seed, DONG GOI MOI take
       thanh <ROLE>_<tag>_tNN.wav (vi cong that la F0/CER sau khi Higgs clone, do tren Kaggle).
    -> refs.json co them nhip am tiet/giay (syl_per_s) cua clip.
"""
import argparse
import datetime
import json
import os
import re
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
RAW = WORK / "voxcpm_raw"
MANIFEST = WORK / "voxcpm_refs_manifest_g9.json"
OUT_REF = ROOT / "assets" / "voice_ref_voxcpm2_g9"

# Cung chuoi ffmpeg giong het higgs_make_refs_voxcpm.py:48-52
FLT = ("aresample=24000,"
       "loudnorm=I=-18:TP=-2.0:LRA=11,"
       "silenceremove=start_periods=1:start_threshold=-50dB,"
       "areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse")

# (cfg, seed) cho moi take
TAKE_CONFIGS = [(2.0, 42), (2.0, 101), (2.0, 2024), (2.5, 777), (2.5, 999)]
EXTRA_TAKES = 3          # sinh them neu het thang ma chua co take nao trong dai

# QUY_TAC_AUDIO_HIGGS.md §4: clip tham chieu 16-28 s (tam 20 s)
LO_SEC, HI_SEC = 16.0, 28.0


def f0_median(audio_np, sr=48000):
    """F0 trung vi (autocorrelation) — cung ham voi voice_audition.f0_median."""
    ff = shutil.which("ffmpeg") or "ffmpeg"
    tmp_in = f"/tmp/_f0_g9_{os.getpid()}.wav"
    sf.write(tmp_in, audio_np, sr)
    r = subprocess.run([ff, "-v", "error", "-i", tmp_in, "-ac", "1", "-ar", "16000",
                        "-f", "s16le", "-"], capture_output=True)
    try:
        os.remove(tmp_in)
    except OSError:
        pass
    if r.returncode != 0 or not r.stdout:
        return 0.0
    x = np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768
    sr_res = 16000
    win, hop, out = int(0.04 * sr_res), int(0.01 * sr_res), []
    for s in range(0, len(x) - win, hop):
        f = x[s:s + win]
        if np.sqrt((f ** 2).mean()) < 0.02:
            continue
        f = f - f.mean()
        ac = np.correlate(f, f, "full")[win - 1:]
        lo, hi = int(sr_res / 400), int(sr_res / 70)
        k = lo + int(np.argmax(ac[lo:hi]))
        if ac[k] > 0.3 * ac[0]:
            out.append(sr_res / k)
    return float(np.median(out)) if out else 0.0


def gen_one(model, control, text, sr, seed, cfg, out_p):
    torch.manual_seed(seed)
    if torch.backends.mps.is_available():
        torch.mps.manual_seed(seed)
    final_text = f"({re.sub(r'[()（）]', '', control).strip()}){text.strip()}"
    t0 = time.time()
    audio = model.generate(text=final_text, cfg_value=cfg,
                           inference_timesteps=10, normalize=False)
    dur = len(audio) / sr
    sf.write(str(out_p), audio, sr)
    return audio, dur, time.time() - t0


def package(src, ref_wav, text, lo_f0, hi_f0):
    """Dong goi 24 kHz mono -18 LUFS; tra ve (seconds, ref_f0, notes)."""
    ff = shutil.which("ffmpeg") or "ffmpeg"
    subprocess.run([ff, "-y", "-v", "error", "-i", str(src), "-af", FLT,
                    "-ac", "1", "-ar", "24000", "-c:a", "pcm_s16le", str(ref_wav)],
                   check=True)
    ref_wav.with_suffix(".txt").write_text(text, encoding="utf-8")
    data, sr_read = sf.read(str(ref_wav), dtype="float32")
    seconds = round(len(data) / float(sr_read), 2)
    ref_f0 = f0_median(data, sr_read)
    notes = []
    if not (LO_SEC <= seconds <= HI_SEC):
        notes.append(f"THOI LUONG {seconds:.1f}s ngoai [{LO_SEC}-{HI_SEC}]s")
    if not (lo_f0 * 0.94 <= ref_f0 <= hi_f0 * 1.06):
        notes.append(f"F0 {ref_f0:.0f}Hz ngoai dai muc tieu {lo_f0}-{hi_f0}Hz")
    return seconds, ref_f0, notes


def run_candidates(model, manifest, sample_rate, n_seeds):
    """Moi bac control x n_seeds seed; dong goi MOI take (khong dung som)."""
    packaged = {}
    for role, data in manifest.items():
        lo_f0, hi_f0 = data["f0_target"]
        text = data["text"].strip()
        n_syl = len(text.split())
        role_dir = RAW / role
        role_dir.mkdir(parents=True, exist_ok=True)
        print(f"\n--- {role}  (muc tieu F0 clip {lo_f0}-{hi_f0} Hz) ---")
        # manifest co the ghim (cfg, seed) rieng cho vai: "takes": [[2.0, 7], ...]
        # (bo EN 31/10/2026 — dung lai seed cua giong VN da chot); khong co -> nhu cu
        takes = [(float(c), int(s)) for c, s in data["takes"]] if data.get("takes") else \
            [TAKE_CONFIGS[i % len(TAKE_CONFIGS)] for i in range(n_seeds)]
        for v in data["control_variants"]:
            for i, (cfg, seed) in enumerate(takes):
                name = f"{role}_{v['tag']}_t{i + 1:02d}"
                raw_p = role_dir / f"{name}.wav"
                print(f"  > {name} (seed={seed}, cfg={cfg})...", end="", flush=True)
                try:
                    _, dur, secs = gen_one(model, v["control"], text, sample_rate,
                                           seed, cfg, raw_p)
                    ref_wav = OUT_REF / f"{name}.wav"
                    seconds, ref_f0, notes = package(raw_p, ref_wav, text, lo_f0, hi_f0)
                except Exception as exc:                    # noqa: BLE001
                    print(f" LOI: {exc}")
                    continue
                syl = round(n_syl / seconds, 2) if seconds else 0.0
                print(f" {secs:.0f}s | {seconds:.1f}s | F0 {ref_f0:.1f} Hz | {syl} am/s"
                      + ("  !! " + "; ".join(notes) if notes else "  [TRONG DAI]"))
                packaged[name] = {
                    "voice_source": "VoxCPM2 (OpenBMB) - Voice Design",
                    "control_instruction": v["control"], "target_text": text,
                    "source_file": raw_p.as_posix(), "seconds": seconds,
                    "f0_median_hz": round(ref_f0, 1), "f0_target_hz": [lo_f0, hi_f0],
                    "syl_per_s": syl, "syl_target": data.get("syl_target"),
                    "sample_rate": 24000, "channels": 1, "lufs_target": -18.0,
                    "model": "openbmb/VoxCPM2", "license": "Apache-2.0",
                    "attribution_required": False, "notes": notes,
                    "role": role, "variant": v["tag"], "seed": seed, "cfg": cfg,
                    "reference_file": ref_wav.as_posix(), "why": data.get("why", ""),
                    "generated_at": datetime.datetime.now().isoformat(),
                }
                (OUT_REF / "refs.json").write_text(
                    json.dumps(packaged, ensure_ascii=False, indent=1), encoding="utf-8")
    return packaged


def main():
    global MANIFEST, OUT_REF
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", default=None)
    ap.add_argument("--out", default=None)
    ap.add_argument("--candidates", type=int, default=0,
                    help="so seed moi bac control; >0 = che do ung vien")
    ap.add_argument("--seeds", default=None,
                    help="danh sach seed cach dau phay (cfg 2.0), thay TAKE_CONFIGS; "
                         "--candidates = so seed")
    args = ap.parse_args()
    if args.seeds:
        TAKE_CONFIGS[:] = [(2.0, int(s)) for s in args.seeds.split(",")]
        args.candidates = len(TAKE_CONFIGS)
    if args.manifest:
        MANIFEST = (ROOT / args.manifest).resolve()
    if args.out:
        OUT_REF = (ROOT / args.out).resolve()
    if not MANIFEST.exists():
        sys.exit(f"Thieu manifest: {MANIFEST}")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
    if args.candidates > 0 and (OUT_REF / "refs.json").exists():
        sys.exit(f"{OUT_REF}/refs.json da ton tai — khong ghi de (L5). Doi --out hoac sao luu truoc.")
    RAW.mkdir(parents=True, exist_ok=True)
    OUT_REF.mkdir(parents=True, exist_ok=True)

    print("=" * 74)
    print("VOXCPM2 — DONG THANG TAO CLIP THAM CHIEU MOI CHO G9 (Tap 02 / Higgs v3)")
    print("=" * 74)

    print("\n[1/2] Nap model VoxCPM2 tren MPS...")
    t0 = time.time()
    model = VoxCPM.from_pretrained("openbmb/VoxCPM2", optimize=False, device="mps",
                                   local_files_only=True)
    print(f"    xong trong {time.time() - t0:.1f}s")
    sample_rate = getattr(model.tts_model, "sample_rate", 48000)

    if args.candidates > 0:
        print(f"\n[2/2] Che do ung vien: moi bac x {args.candidates} seed...")
        packaged = run_candidates(model, manifest, sample_rate, args.candidates)
        print("\n" + "=" * 74)
        print(f"XONG: {len(packaged)} ung vien trong {OUT_REF}")
        for k, p in packaged.items():
            print(f"  {k:28} F0 {p['f0_median_hz']:6.1f} Hz | {p['seconds']:5.1f}s | "
                  f"{p['syl_per_s']} am/s | {'OK' if not p['notes'] else '; '.join(p['notes'])}")
        print("=" * 74)
        return

    print("\n[2/2] Do thang tung vai...")
    packaged = []

    for role, data in manifest.items():
        lo_f0, hi_f0 = data.get("f0_target", [0, 0])
        mid = (lo_f0 + hi_f0) / 2
        text = (data.get("text") or "").strip()
        variants = data.get("control_variants") or [{"tag": "default",
                                                     "control": data.get("control", "")}]

        role_dir = RAW / role
        role_dir.mkdir(parents=True, exist_ok=True)
        takes_path = role_dir / "takes.json"
        records = []
        if takes_path.exists():
            try:
                records = json.loads(takes_path.read_text(encoding="utf-8"))
            except Exception:
                records = []

        print(f"\n--- {role}  (muc tieu F0 {lo_f0}-{hi_f0} Hz) ---")
        print(f"    {data.get('note', '')}")

        used_seed = 0
        winner = None

        # --- vong 1: do thang qua cac bien the control ---
        for v in variants:
            tag = v.get("tag", "v")
            control = v["control"]
            cfg, seed = TAKE_CONFIGS[used_seed % len(TAKE_CONFIGS)]
            used_seed += 1
            fname = f"{role}_{tag}_take01.wav"
            out_p = role_dir / fname
            print(f"  > [{tag}] {fname} (seed={seed}, cfg={cfg})...", end="", flush=True)
            try:
                audio, dur, secs = gen_one(model, control, text, sample_rate, seed, cfg, out_p)
            except Exception as exc:                        # noqa: BLE001
                print(f" LOI: {exc}")
                continue
            f0 = f0_median(audio, sample_rate)
            in_range = (lo_f0 * 0.94 <= f0 <= hi_f0 * 1.06)
            print(f" {secs:.0f}s | {dur:.1f}s | F0 {f0:.1f} Hz "
                  f"{'[TRONG DAI]' if in_range else '[LECH]'}")
            records.append({
                "take": fname, "role": role, "variant": tag, "control": control,
                "file": str(out_p.relative_to(ROOT)), "seed": seed, "cfg": cfg,
                "timesteps": 10, "normalize": False, "sample_rate": sample_rate,
                "duration_s": round(dur, 2), "f0_hz": round(f0, 1),
                "f0_target_hz": [lo_f0, hi_f0], "f0_in_range": in_range,
                "generated_at": datetime.datetime.now().isoformat(),
                "tool": "VoxCPM2 (OpenBMB, Voice Design)", "license": "Apache-2.0",
            })
            takes_path.write_text(json.dumps(records, ensure_ascii=False, indent=2),
                                  encoding="utf-8")
            if in_range and winner is None:
                winner = records[-1]
                print(f"  => DUNG trong dai, dung tai day: {fname}")
                break

        # --- vong 2: het thang, sinh them take cua bien gan nhat ---
        if winner is None and records:
            best_var = min(records, key=lambda r: abs(r["f0_hz"] - mid))
            v = next((x for x in variants if x.get("tag") == best_var.get("variant")),
                     variants[0])
            print(f"  > het thang. Sinh them take cua bien '{best_var.get('variant')}'...")
            for _ in range(EXTRA_TAKES):
                if used_seed >= len(TAKE_CONFIGS):
                    used_seed = 0
                cfg, seed = TAKE_CONFIGS[used_seed % len(TAKE_CONFIGS)]
                used_seed += 1
                fname = f"{role}_{best_var.get('variant')}_take{len(records) + 1:02d}.wav"
                out_p = role_dir / fname
                print(f"  > {fname} (seed={seed}, cfg={cfg})...", end="", flush=True)
                try:
                    audio, dur, secs = gen_one(model, v["control"], text, sample_rate,
                                               seed, cfg, out_p)
                except Exception as exc:                    # noqa: BLE001
                    print(f" LOI: {exc}")
                    continue
                f0 = f0_median(audio, sample_rate)
                in_range = (lo_f0 * 0.94 <= f0 <= hi_f0 * 1.06)
                print(f" {secs:.0f}s | {dur:.1f}s | F0 {f0:.1f} Hz "
                      f"{'[TRONG DAI]' if in_range else '[LECH]'}")
                records.append({
                    "take": fname, "role": role, "variant": best_var.get("variant"),
                    "control": v["control"], "file": str(out_p.relative_to(ROOT)),
                    "seed": seed, "cfg": cfg, "timesteps": 10, "normalize": False,
                    "sample_rate": sample_rate, "duration_s": round(dur, 2),
                    "f0_hz": round(f0, 1), "f0_target_hz": [lo_f0, hi_f0],
                    "f0_in_range": in_range,
                    "generated_at": datetime.datetime.now().isoformat(),
                    "tool": "VoxCPM2 (OpenBMB, Voice Design)", "license": "Apache-2.0",
                })
                takes_path.write_text(json.dumps(records, ensure_ascii=False, indent=2),
                                      encoding="utf-8")
                if in_range:
                    winner = records[-1]
                    break

        if not records:
            print(f"  !! {role}: khong sinh duoc take nao")
            continue
        if winner is None:
            winner = min(records, key=lambda r: abs(r["f0_hz"] - mid))
            print(f"  !! KHONG co take nao trong dai {lo_f0}-{hi_f0} Hz. "
                  f"Van lay take gan nhat: {winner['take']} (F0 {winner['f0_hz']} Hz)")

        # --- dong goi 24 kHz ---
        ff = shutil.which("ffmpeg") or "ffmpeg"
        src = ROOT / winner["file"]
        ref_wav = OUT_REF / f"{role}.wav"
        try:
            subprocess.run([ff, "-y", "-v", "error", "-i", str(src), "-af", FLT,
                            "-ac", "1", "-ar", "24000", "-c:a", "pcm_s16le", str(ref_wav)],
                           check=True)
            (OUT_REF / f"{role}.txt").write_text(text, encoding="utf-8")
            data, sr_read = sf.read(str(ref_wav), dtype="float32")
            seconds = round(len(data) / float(sr_read), 2)
            ref_f0 = f0_median(data, sr_read)

            # QUY_TAC §4: thoi luong 16-28 s, F0 trong dai muc tieu
            notes = []
            if not (LO_SEC <= seconds <= HI_SEC):
                notes.append(f"THOI LUONG {seconds:.1f}s ngoai [{LO_SEC}-{HI_SEC}]s")
            if not (lo_f0 * 0.94 <= ref_f0 <= hi_f0 * 1.06):
                notes.append(f"F0 {ref_f0:.0f}Hz ngoai dai muc tieu {lo_f0}-{hi_f0}Hz")

            print(f"  => DONG GOI {ref_wav.relative_to(ROOT)} "
                  f"(24 kHz mono, {seconds:.1f}s, F0 {ref_f0:.1f} Hz)"
                  + ("  !! " + "; ".join(notes) if notes else ""))
            # Schema refs.json phai GION schema canonical (higgs_make_refs_voxcpm.py:158-173)
            packaged.append({
                "voice_source": "VoxCPM2 (OpenBMB) - Voice Design",
                "control_instruction": winner.get("control", ""),
                "target_text": text,
                "source_file": src.as_posix(),
                "seconds": seconds,
                "f0_median_hz": round(ref_f0, 1),
                "f0_target_hz": [lo_f0, hi_f0],
                "sample_rate": 24000,
                "channels": 1,
                "lufs_target": -18.0,
                "model": "openbmb/VoxCPM2",
                "license": "Apache-2.0",
                "attribution_required": False,
                "notes": notes,
                # --- truong bo sung (giau duoc, dung cho viec truy vet) ---
                "role": role,
                "variant": winner.get("variant"),
                "reference_file": ref_wav.as_posix(),
                "why": data.get("why", ""),
            })
        except Exception as exc:                            # noqa: BLE001
            print(f"  !! LOI dong goi ffmpeg: {exc}")

    if packaged:
        (OUT_REF / "refs.json").write_text(
            json.dumps({p["role"]: p for p in packaged}, ensure_ascii=False, indent=1),
            encoding="utf-8")

    print("\n" + "=" * 74)
    print("XONG:")
    for role in manifest:
        p = OUT_REF / f"{role}.wav"
        print(f"  {role:9} {'OK' if p.exists() else 'THIEU'}  {p}")
    print("\nBuoc tiep theo ( tren may nay ):")
    print("  git add assets/voice_ref_voxcpm2_g9")
    print("  git commit -m 'feat(audio): them 3 clip tham chieu VoxCPM2 cho G9 (Tap 02)'")
    print("  git push")
    print("=" * 74)


if __name__ == "__main__":
    main()
