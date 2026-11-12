"""Pipeline to render picture.mp4 and mux final video for Episode 09 (VI, EN, JA).
Follows rules L1-L10, H14, A7, Step 9 and Step 10 of AGENTS.md.
"""
import os
import sys
import re
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
FF = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
FFPROBE = WORK / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

CONFIGS = {
    "vi": {
        "env_lang": None,
        "timeline": WORK / "timeline_s_t09.json",
        "video_dir": WORK / "video3_t09",
        "expected_dur": 1523.19,
        "out_dir": ROOT / "02_SAN_XUAT" / "Tap09" / "xuat_ban",
        "master_mp4": "Tap09_master.mp4",
        "alias_mp4": "Tap09.mp4",
        "audio_master": WORK / "audio_master_t09.wav",
        "srt": ROOT / "02_SAN_XUAT" / "Tap09" / "xuat_ban" / "Tap09.srt",
    },
    "en": {
        "env_lang": "en",
        "timeline": WORK / "timeline_s_EN_t09.json",
        "video_dir": WORK / "video3_EN_t09",
        "expected_dur": 1436.70,
        "out_dir": ROOT / "02_SAN_XUAT" / "Tap09_EN" / "xuat_ban",
        "master_mp4": "Tap09_EN_master.mp4",
        "alias_mp4": "Tap09_EN.mp4",
        "audio_master": WORK / "audio_master_EN_t09.wav",
        "srt": ROOT / "02_SAN_XUAT" / "Tap09_EN" / "xuat_ban" / "Tap09_EN.srt",
    },
    "ja": {
        "env_lang": "ja",
        "timeline": WORK / "timeline_s_JA_t09.json",
        "video_dir": WORK / "video3_JA_t09",
        "expected_dur": 1721.45,
        "out_dir": ROOT / "02_SAN_XUAT" / "Tap09_JA" / "xuat_ban",
        "master_mp4": "Tap09_JA_master.mp4",
        "alias_mp4": "Tap09_JA.mp4",
        "audio_master": WORK / "audio_master_JA_t09.wav",
        "srt": ROOT / "02_SAN_XUAT" / "Tap09_JA" / "xuat_ban" / "Tap09_JA.srt",
    }
}

def get_duration(fn):
    cmd = [str(FFPROBE), "-v", "error", "-show_entries", "format=duration",
           "-of", "default=noprint_wrappers=1:nokey=1", str(fn)]
    p = subprocess.run(cmd, capture_output=True, text=True, check=True)
    return float(p.stdout.strip())

def render_picture(lang, workers=6):
    cfg = CONFIGS[lang]
    v_dir = cfg["video_dir"]
    v_dir.mkdir(parents=True, exist_ok=True)
    pic = v_dir / "picture.mp4"

    # Check if picture.mp4 already exists and has correct duration
    if pic.exists():
        try:
            dur = get_duration(pic)
            if abs(dur - cfg["expected_dur"]) <= 0.05:
                print(f"[{lang.upper()}] picture.mp4 already exists with correct duration {dur:.2f} s. Skipping render.")
                return pic
        except Exception:
            pass

    print(f"\n=======================================================")
    print(f"[{lang.upper()}] STARTING RENDER picture.mp4 (workers={workers})...")
    print(f"=======================================================", flush=True)

    env = os.environ.copy()
    env["AE_EP"] = "09"
    if cfg["env_lang"]:
        env["AE_LANG"] = cfg["env_lang"]
    elif "AE_LANG" in env:
        del env["AE_LANG"]

    cmd = [sys.executable, str(WORK / "build_video3.py"), "--workers", str(workers)]
    subprocess.run(cmd, env=env, check=True)

    if not pic.exists():
        raise RuntimeError(f"[{lang.upper()}] Failed to generate {pic}")

    dur = get_duration(pic)
    print(f"[{lang.upper()}] Rendered picture.mp4 duration: {dur:.2f} s (expected: {cfg['expected_dur']:.2f} s)")
    if abs(dur - cfg["expected_dur"]) > 0.05:
        raise ValueError(f"[{lang.upper()}] Duration mismatch: {dur:.2f} s vs expected {cfg['expected_dur']:.2f} s (> 0.05 s)")
    return pic

def mux_video(lang):
    cfg = CONFIGS[lang]
    final_master = cfg["out_dir"] / cfg["master_mp4"]
    if final_master.exists():
        try:
            dur = get_duration(final_master)
            if abs(dur - cfg["expected_dur"]) <= 0.05:
                print(f"[{lang.upper()}] Final master mp4 already exists with correct duration {dur:.2f} s. Skipping mux.")
                alias = cfg["out_dir"] / cfg["alias_mp4"]
                if not alias.exists() or alias.stat().st_size != final_master.stat().st_size:
                    shutil.copy2(final_master, alias)
                return final_master
        except Exception:
            pass

    print(f"\n[{lang.upper()}] Packaging and muxing final video...")

    env = os.environ.copy()
    env["AE_EP"] = "09"
    if cfg["env_lang"]:
        env["AE_LANG"] = cfg["env_lang"]
    elif "AE_LANG" in env:
        del env["AE_LANG"]

    cmd = [sys.executable, str(WORK / "package.py"), "--mux"]
    subprocess.run(cmd, env=env, check=True)

    final_master = cfg["out_dir"] / cfg["master_mp4"]
    if not final_master.exists():
        raise RuntimeError(f"[{lang.upper()}] Expected master mp4 not found: {final_master}")

    alias = cfg["out_dir"] / cfg["alias_mp4"]
    if not alias.exists() or alias.stat().st_size != final_master.stat().st_size:
        shutil.copy2(final_master, alias)
        print(f"[{lang.upper()}] Created alias: {alias.name}")

    print(f"[{lang.upper()}] Final video muxed successfully: {final_master} ({final_master.stat().st_size / 1024 / 1024:.1f} MB)")
    return final_master

def qc_video(lang):
    cfg = CONFIGS[lang]
    final = cfg["out_dir"] / cfg["master_mp4"]
    print(f"\n[{lang.upper()}] Running QC checks on {final.name}...")

    # 1. Duration check
    v_dur = get_duration(final)
    a_dur = get_duration(cfg["audio_master"])
    print(f"  Duration: video={v_dur:.3f} s, audio={a_dur:.3f} s, delta={abs(v_dur - a_dur):.3f} s")
    assert abs(v_dur - a_dur) <= 0.05, f"Audio/Video desync: {abs(v_dur - a_dur)} s > 0.05 s"
    assert abs(v_dur - cfg["expected_dur"]) <= 0.05, f"Expected duration mismatch: {abs(v_dur - cfg['expected_dur'])} s > 0.05 s"

    # 2. Decode test
    print("  Testing video and audio decoding...")
    p = subprocess.run([str(FF), "-v", "error", "-i", str(final), "-f", "null", "-"],
                       capture_output=True, text=True)
    if p.returncode != 0 or p.stderr.strip():
        raise RuntimeError(f"Decode errors found: {p.stderr}")
    print("  Decode check: 0 errors.")

    # 3. Audio Loudnorm measurement
    print("  Measuring audio loudness on final MP4...")
    p = subprocess.run([str(FF), "-hide_banner", "-i", str(final), "-af", "loudnorm=print_format=json", "-f", "null", "-"],
                       capture_output=True, text=True)
    m = re.findall(r"\{[\s\S]*?\}", p.stderr)
    for block in reversed(m):
        if "input_i" in block:
            ln = json.loads(block)
            i_lufs = float(ln["input_i"])
            tp = float(ln["input_tp"])
            lra = float(ln["input_lra"])
            print(f"  Loudness: I={i_lufs:.2f} LUFS (req -16±1), TP={tp:.2f} dBFS (req <= -1.5), LRA={lra:.2f}")
            assert -17.0 <= i_lufs <= -15.0, f"LUFS out of range: {i_lufs}"
            assert tp <= -1.5, f"True peak exceeded: {tp} dBFS > -1.5 dBFS"
            break

    # 4. Silence check (>0.3s at -60dB)
    print("  Checking for silence > 0.3s at -60dB (Rule A1 / V4)...")
    p = subprocess.run([str(FF), "-hide_banner", "-i", str(final), "-af", "silencedetect=noise=-60dB:d=0.3", "-f", "null", "-"],
                       capture_output=True, text=True)
    sil_starts = [line for line in p.stderr.splitlines() if "silence_start" in line]
    print(f"  Silence gaps > 0.3s @ -60dB: {len(sil_starts)}")
    assert len(sil_starts) == 0, f"Found {len(sil_starts)} silent gaps > 0.3s!"

    # 5. Outro card check (frame at total - 6s)
    t_endcard = v_dur - 6.0
    endcard_img = WORK / f"_qc_endcard_{lang}.png"
    subprocess.run([str(FF), "-y", "-ss", f"{t_endcard:.2f}", "-i", str(final), "-vframes", "1", str(endcard_img)],
                   capture_output=True, check=True)
    assert endcard_img.exists() and endcard_img.stat().st_size > 50000, "Endcard frame missing or too small"
    print(f"  Outro endcard verified at t={t_endcard:.2f} s: {endcard_img.name} ({endcard_img.stat().st_size} bytes)")

    print(f"[{lang.upper()}] ALL QC CHECKS PASSED SUCCESSFULLY!\n")

def run(lang):
    render_picture(lang)
    mux_video(lang)
    qc_video(lang)

if __name__ == "__main__":
    target = sys.argv[1].lower() if len(sys.argv) > 1 else "all"
    if target in CONFIGS:
        run(target)
    elif target == "all":
        for l in ["vi", "en", "ja"]:
            run(l)
    else:
        print(f"Usage: {sys.argv[0]} [vi|en|ja|all]")
