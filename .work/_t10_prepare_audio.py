# -*- coding: utf-8 -*-
"""Prepare audio masters (48kHz stereo WAV) and character stems (16kHz mono WAV) for Tap 10.
Solves the issue of missing stems which caused flat/static badge audio visualizers.
"""
import json
import subprocess
import sys
import wave
from pathlib import Path
import numpy as np

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"

CONFIGS = [
    {
        "lang": "vi",
        "mp3": ROOT / "02_SAN_XUAT" / "Tap10" / "xuat_ban" / "Tap10_master.mp3",
        "wav": WORK / "audio_master_t10.wav",
        "tl": WORK / "timeline_s_t10.json",
        "stems_dir": WORK / "stems_t10",
    },
    {
        "lang": "en",
        "mp3": ROOT / "02_SAN_XUAT" / "Tap10_EN" / "xuat_ban" / "Tap10_EN_master.mp3",
        "wav": WORK / "audio_master_EN_t10.wav",
        "tl": WORK / "timeline_s_EN_t10.json",
        "stems_dir": WORK / "stems_EN_t10",
    },
    {
        "lang": "ja",
        "mp3": ROOT / "02_SAN_XUAT" / "Tap10_JA" / "xuat_ban" / "Tap10_JA_master.mp3",
        "wav": WORK / "audio_master_JA_t10.wav",
        "tl": WORK / "timeline_s_JA_t10.json",
        "stems_dir": WORK / "stems_JA_t10",
    },
]

ROLES = ("H", "D", "C", "N1", "N2")
N_ELEMENT = {"1.07": "N1", "4.05": "N2"}
SR_STEMS = 16000

for cfg in CONFIGS:
    lang = cfg["lang"].upper()
    print(f"\n==========================================")
    print(f"[{lang}] Preparing master audio & stems...")
    print(f"==========================================")
    
    mp3 = cfg["mp3"]
    wav = cfg["wav"]
    tl_p = cfg["tl"]
    stems_dir = cfg["stems_dir"]
    stems_dir.mkdir(parents=True, exist_ok=True)
    
    if not mp3.exists():
        raise FileNotFoundError(f"Master MP3 not found: {mp3}")
    
    # 1. Convert MP3 to 48kHz stereo WAV if not exists or size is 0
    if not wav.exists() or wav.stat().st_size == 0:
        print(f"[{lang}] Converting {mp3.name} -> {wav.name} (48kHz stereo)...")
        cmd = [
            str(FF), "-y", "-v", "error",
            "-i", str(mp3),
            "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le",
            str(wav)
        ]
        subprocess.run(cmd, check=True)
        print(f"[{lang}] Created {wav.name} ({wav.stat().st_size / 1024 / 1024:.1f} MB)")
    else:
        print(f"[{lang}] Reusing existing {wav.name}")
        
    # 2. Extract stems per role
    tl = json.loads(tl_p.read_text(encoding="utf-8"))
    total_dur = float(tl["total"])
    items = tl["items"]
    print(f"[{lang}] Timeline duration: {total_dur:.2f} s, items: {len(items)}")
    
    # Decode audio master to 16kHz mono float32 for stems
    raw = subprocess.run([
        str(FF), "-v", "error", "-i", str(mp3),
        "-f", "f32le", "-ac", "1", "-ar", str(SR_STEMS), "-"
    ], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    print(f"[{lang}] Decoded {len(x)} samples at {SR_STEMS}Hz = {len(x)/SR_STEMS:.2f} s")
    
    N = int(total_dur * SR_STEMS) + SR_STEMS
    stems = {r: np.zeros(N, dtype=np.float32) for r in ROLES}
    
    for it in items:
        r = it.get("role")
        el = it.get("element", "")
        if r == "N":
            r = N_ELEMENT.get(el, "N1")
        elif r not in stems:
            # Check if role maps to N1 or N2
            r = N_ELEMENT.get(el, r)
            
        if r not in stems:
            print(f"  Warning: unknown role '{r}' for element {el}")
            continue
            
        a = int(round(it["start"] * SR_STEMS))
        b = int(round(it["end"] * SR_STEMS))
        seg = x[a:b]
        if len(seg) > 0:
            stems[r][a:a + len(seg)] = seg
            
    for r in ROLES:
        s = stems[r]
        peak = float(np.abs(s).max())
        rms = float(np.sqrt(np.mean(s ** 2)))
        out_int16 = (np.clip(s, -1.0, 1.0) * 32767.0).astype(np.int16)
        out_file = stems_dir / f"{r}.wav"
        with wave.open(str(out_file), "wb") as wf:
            wf.setnchannels(1)
            wf.setsampwidth(2)
            wf.setframerate(SR_STEMS)
            wf.writeframes(out_int16.tobytes())
        db_peak = 20 * np.log10(peak + 1e-12)
        db_rms = 20 * np.log10(rms + 1e-12)
        print(f"  [{lang}] Stem {r}.wav: peak={db_peak:.1f} dBFS, rms={db_rms:.1f} dBFS -> written to {out_file.name}")
        assert peak > 0.001, f"Stem {r}.wav has no signal (peak={peak})"

print("\nALL AUDIO MASTERS AND STEMS PREPARED SUCCESSFULLY!")
