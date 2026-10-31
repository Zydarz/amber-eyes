#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phep thu VoxCPM2 CHE DO CLONE (Mac mini, MPS) — so cong bang voi Higgs.

Doc .work/voxcpm_clone_spec.json (sinh boi build_voxcpm_clone_spec.py tren Windows):
72 file = 3 vai (H / D3_SH / C2_AB03) x 12 cau that Tap 02 x 2 ban.

  --check   nap model, in chu ky model.generate, tim tham so clone, sinh THU 1 cau roi thoat
  (khong)   sinh ca 72 file; checkpoint tung file (chay lai se bo qua file da co)

Xuat: assets/pilot_voxcpm_clone/<file>.wav (24 kHz mono PCM16, KHONG chuan hoa loudness — nhu Higgs)
      assets/pilot_voxcpm_clone/manifest.json (cung truong voi higgs_manifest.json)

CHAY:
    /Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_clone_pilot.py --check
    /Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_clone_pilot.py
"""
import argparse
import datetime
import inspect
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
SPEC = ROOT / ".work" / "voxcpm_clone_spec.json"
OUT = ROOT / "assets" / "pilot_voxcpm_clone"
RAW = ROOT / ".work" / "voxcpm_raw" / "clone_pilot"
MAN = OUT / "manifest.json"
FF = shutil.which("ffmpeg") or "ffmpeg"

# Ten tham so clone co the gap (theo thu tu uu tien: co ca loi mau > chi audio mau)
WAV_KEYS = ["prompt_wav_path", "reference_wav_path", "ref_wav_path", "prompt_audio_path"]
TXT_KEYS = ["prompt_text", "reference_text", "ref_text"]

ap = argparse.ArgumentParser()
ap.add_argument("--check", action="store_true")
args = ap.parse_args()

print("=" * 74)
print("VOXCPM2 CLONE PILOT —", datetime.datetime.now().isoformat(timespec="seconds"))
print("=" * 74)
t0 = time.time()
model = VoxCPM.from_pretrained("openbmb/VoxCPM2", optimize=False, device="mps", local_files_only=True)
SR = getattr(model.tts_model, "sample_rate", 48000)
print(f"nap model {time.time() - t0:.0f}s | sample_rate {SR}")

params = inspect.signature(model.generate).parameters
print("CHU KY model.generate:", ", ".join(params))
wav_key = next((k for k in WAV_KEYS if k in params), None)
txt_key = next((k for k in TXT_KEYS if k in params), None)
print(f"tham so clone: audio={wav_key}  loi_mau={txt_key}")
if wav_key is None:
    sys.exit("!! DUNG: khong tim thay tham so clone trong model.generate — bao lai nguyen van dong CHU KY o tren")
MODE = f"{wav_key}+{txt_key}" if txt_key else wav_key

spec = json.loads(SPEC.read_text(encoding="utf-8"))["items"]
OUT.mkdir(parents=True, exist_ok=True)
RAW.mkdir(parents=True, exist_ok=True)
manifest = json.loads(MAN.read_text(encoding="utf-8")) if MAN.exists() else []
done = {r["key"] for r in manifest if r.get("ok")}


def gen(it):
    torch.manual_seed(it["seed"])
    if torch.backends.mps.is_available():
        torch.mps.manual_seed(it["seed"])
    kw = {"text": it["text"], "cfg_value": 2.0, "inference_timesteps": 10, "normalize": False,
          wav_key: str(ROOT / it["ref_wav"])}
    if txt_key:
        kw[txt_key] = (ROOT / it["ref_txt"]).read_text(encoding="utf-8").strip()
    if "denoise" in params:
        kw["denoise"] = False          # clip mau da sach; tranh nap them model khu on
    return model.generate(**kw)


todo = [it for it in spec if it["key"] not in done]
if args.check:
    todo = todo[:1]
print(f"\ncan sinh: {len(todo)} / {len(spec)} file | che do clone: {MODE}\n")

t_all = time.time()
for n, it in enumerate(todo, 1):
    t1 = time.time()
    rec = {k: it[k] for k in ("key", "id", "role", "emotion", "variant", "seed", "file")}
    rec.update({"ref_wav": it["ref_name"] + ".wav", "text_sent": it["text"], "text_plain": it["text_plain"],
                "engine": "VoxCPM2 clone", "clone_mode": MODE})
    try:
        audio = np.asarray(gen(it), dtype=np.float32).squeeze()
        raw = RAW / it["file"]
        sf.write(str(raw), audio, SR)
        subprocess.run([FF, "-y", "-v", "error", "-i", str(raw), "-ac", "1", "-ar", "24000",
                        "-c:a", "pcm_s16le", str(OUT / it["file"])], check=True)
        dur = len(audio) / SR
        dt = time.time() - t1
        rec.update({"ok": True, "duration_s": round(dur, 2), "gen_s": round(dt, 1),
                    "rtf": round(dt / dur, 2) if dur else None,
                    "peak_dbfs": round(20 * np.log10(float(np.max(np.abs(audio))) + 1e-12), 2)})
        print(f"OK  [{n}/{len(todo)}] {it['file']:40} {dur:5.1f}s  gen {dt:5.1f}s", flush=True)
    except Exception as e:                                   # noqa: BLE001
        rec.update({"ok": False, "error": f"{type(e).__name__}: {str(e)[:300]}"})
        print(f"LOI [{n}/{len(todo)}] {it['file']}: {rec['error']}", flush=True)
    manifest = [r for r in manifest if r["key"] != it["key"]] + [rec]
    MAN.write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")

ok = sum(1 for r in manifest if r.get("ok"))
print("\n" + "=" * 74)
print(f"XONG: {ok}/{len(spec)} file OK | lan nay {len(todo)} file trong {(time.time() - t_all) / 60:.1f} phut")
print(f"che do clone: {MODE}")
fails = [r for r in manifest if not r.get("ok")]
for r in fails:
    print("  LOI:", r["file"], r["error"])
print("=" * 74)
sys.exit(0 if not fails else 3)
