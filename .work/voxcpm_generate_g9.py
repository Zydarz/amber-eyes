#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sinh 3 clip tham chieu VoxCPM2 MOI cho G9 (Tập 02, Higgs Audio v3).

VIET: chay tren Mac mini (MPS). KHONG chay tren Windows — VoxCPM2 can MPS/Apple Silicon.

Lý do: bo clip hien tai KHONG tach duoc 2 vai nam:
  vai H (clone 130 Hz) vs vai D (clone 121 Hz) = 0.23 nua cung, can >= 4.
  Higgs KHONG giu F0 cua clip tham chieu (H +20%, D -8%) => 2 vai tro ve cung mot vung.
  Vai N1 (clone 245 Hz) vs vai C (clone 205 Hz) = 3.07 nua cung, can >= 4.

Script nay sinh 3 bo 3 clip:
  M_HIGH  nam cao  (F0 168-182 Hz) -> du phong cho vai D
  M_LOW   nam rat tram (F0 80-92 Hz) -> du phong cho vai H
  W5_HIGH nu cao   (F0 258-276 Hz) -> cho vai N1

Moi bo sinh toi da 5 take, dung khi co take nao F0 nam trong dai muc tieu.
Sau do TU CHON take co F0 sat giua dai nhat va copy ra thu muc de doi giong.

CHAY:
    /Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py

Xuat:
    .work/voxcpm_raw/<ROLE>/<ROLE>_takeNN.wav   (48 kHz, ban goc)
    .work/voxcpm_raw/<ROLE>/takes.json
    assets/voice_ref_voxcpm2_g9_raw/<ROLE>.wav  (take duoc chon, 48 kHz — de ta dong goi)
"""
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
OUT_PICK = ROOT / "assets" / "voice_ref_voxcpm2_g9_raw"
OUT_REF = ROOT / "assets" / "voice_ref_voxcpm2_g9"

# Cung chuoi ffmpeg giong het higgs_make_refs_voxcpm.py:48-52 (24 kHz mono, -18 LUFS, TP=-2.0)
FLT = ("aresample=24000,"
       "loudnorm=I=-18:TP=-2.0:LRA=11,"
       "silenceremove=start_periods=1:start_threshold=-50dB,"
       "areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse")

TAKE_CONFIGS = [
    {"cfg": 2.0, "seed": 42},
    {"cfg": 2.0, "seed": 101},
    {"cfg": 2.0, "seed": 2024},
    {"cfg": 2.5, "seed": 777},
    {"cfg": 2.5, "seed": 999},
]
MAX_TAKES = 5


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


def main():
    if not MANIFEST.exists():
        sys.exit(f"Thieu manifest: {MANIFEST}")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
    RAW.mkdir(parents=True, exist_ok=True)

    print("=" * 72)
    print("VOXCPM2 VOICE DESIGN — SINH CLIP MOI CHO G9 (Tập 02 / Higgs v3)")
    print("=" * 72)

    print("\n[1/2] Nap model VoxCPM2 tren MPS...")
    t0 = time.time()
    model = VoxCPM.from_pretrained("openbmb/VoxCPM2", optimize=False, device="mps",
                                   local_files_only=True)
    print(f"    xong trong {time.time() - t0:.1f}s")
    sample_rate = getattr(model.tts_model, "sample_rate", 48000)

    print("\n[2/2] Sinh take cho tung vai...")
    packaged = []
    for role, data in manifest.items():
        lo_f0, hi_f0 = data.get("f0_target", [0, 0])
        control = re.sub(r"[()（）]", "", (data.get("control") or "").strip()).strip()
        text = (data.get("text") or "").strip()
        final_text = f"({control}){text}"

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
        print(f"    control: {control[:110]}...")

        for idx, cfg_info in enumerate(TAKE_CONFIGS[:MAX_TAKES]):
            seed, cfg = cfg_info["seed"], cfg_info["cfg"]
            take_num = idx + 1
            fname = f"{role}_take{take_num:02d}.wav"
            out_p = role_dir / fname
            print(f"  > {fname} (seed={seed}, cfg={cfg})...", end="", flush=True)
            t_start = time.time()
            try:
                torch.manual_seed(seed)
                if torch.backends.mps.is_available():
                    torch.mps.manual_seed(seed)
                audio = model.generate(text=final_text, cfg_value=cfg,
                                       inference_timesteps=10, normalize=False)
            except Exception as exc:                       # noqa: BLE001
                print(f" LOI: {exc}")
                continue
            dur = len(audio) / sample_rate
            sf.write(str(out_p), audio, sample_rate)
            f0 = f0_median(audio, sample_rate)
            in_range = (lo_f0 * 0.94 <= f0 <= hi_f0 * 1.06)
            print(f" {time.time()-t_start:.1f}s | {dur:.2f}s | F0 {f0:.1f} Hz "
                  f"{'[TRONG DAI]' if in_range else '[LECH]'}")

            records.append({
                "take": fname, "role": role, "file": str(out_p.relative_to(ROOT)),
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
                break

        if not records:
            print(f"  !! {role}: khong sinh duoc take nao")
            continue
        best = min(records, key=lambda r: abs(r["f0_hz"] - (lo_f0 + hi_f0) / 2))
        OUT_PICK.mkdir(parents=True, exist_ok=True)
        src = ROOT / best["file"]
        shutil.copy2(src, OUT_PICK / f"{role}.wav")
        (OUT_PICK / f"{role}.txt").write_text(text, encoding="utf-8")
        print(f"  => CHON: {best['take']} (F0 {best['f0_hz']} Hz) -> "
              f"{OUT_PICK.relative_to(ROOT)}/{role}.wav")

        # --- dong goi thanh clip tham chieu 24 kHz (giong het higgs_make_refs_voxcpm.py) ---
        OUT_REF.mkdir(parents=True, exist_ok=True)
        ff = shutil.which("ffmpeg") or "ffmpeg"
        ref_wav = OUT_REF / f"{role}.wav"
        try:
            subprocess.run([ff, "-y", "-v", "error", "-i", str(src), "-af", FLT,
                            "-ac", "1", "-ar", "24000", "-c:a", "pcm_s16le", str(ref_wav)],
                           check=True)
            (OUT_REF / f"{role}.txt").write_text(text, encoding="utf-8")
            ref_f0 = f0_median(sf.read(str(ref_wav), dtype="float32")[0], 24000)
            print(f"  => DONG GOI: {ref_wav.relative_to(ROOT)} "
                  f"(24 kHz mono, F0 {ref_f0:.1f} Hz)")
            packaged.append({
                "role": role, "source_file": src.as_posix(),
                "reference_file": ref_wav.as_posix(),
                "f0_hz": round(ref_f0, 1), "f0_target_hz": [lo_f0, hi_f0],
                "sample_rate": 24000, "channels": 1, "lufs_target": -18.0,
                "model": "openbmb/VoxCPM2", "license": "Apache-2.0",
                "attribution_required": False,
                "voice_source": "VoxCPM2 (OpenBMB) - Voice Design",
                "control_instruction": control, "target_text": text,
                "why": data.get("why", ""),
            })
        except Exception as exc:                           # noqa: BLE001
            print(f"  !! LOI dong goi ffmpeg: {exc}")

    if packaged:
        (OUT_REF / "refs.json").write_text(
            json.dumps({p["role"]: p for p in packaged}, ensure_ascii=False, indent=1),
            encoding="utf-8")

    print("\n" + "=" * 72)
    print("XONG. File da chon:")
    for role in manifest:
        p = OUT_REF / f"{role}.wav"
        print(f"  {role:9} {'OK' if p.exists() else 'THIEU'}  {p}")
    print("\nBuoc tiep theo ( tren may nay ):")
    print("  git add assets/voice_ref_voxcpm2_g9")
    print("  git commit -m 'feat(audio): them 3 clip tham chieu VoxCPM2 cho G9 (Tap 02)'")
    print("  git push")
    print("=" * 72)


if __name__ == "__main__":
    main()
