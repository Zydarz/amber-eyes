"""Package VoxCPM2 voice-design samples into Higgs reference files.

VoxCPM2 (Voice Design) sinh gioc mau tu mo ta van ban, khong can audio tham chieu.
Tau lieu: 00_TIEU_CHUAN/TAO_GIONG_MAU_VOXCPM2.md
Quy tac file tham chieu: 00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md §4

INPUT
  .work/voxcpm_raw/<role>/*.mp3          audio tai ve tu web (moi vai 3-5 ban)
  .work/voxcpm_refs_manifest.json        { "<role>": { "take": "<file>.mp3",
                                        "control": "...", "text": "..." } }

OUTPUT
  assets/voice_ref_voxcpm2/<role>.wav     WAV mono 24 kHz, -18 LUFS
  assets/voice_ref_voxcpm2/<role>.txt     ref_text chep dung tung chu
  assets/voice_ref_voxcpm2/refs.json     vai / control / text / nguon / F0 / giay

KHONG ghi de assets/voice_ref_higgs/ (bo mau MiniMax) - so sanh A/B truoc khi thay.

Usage:
  py -3 .work/higgs_make_refs_voxcpm.py
  py -3 .work/higgs_make_refs_voxcpm.py --manifest <path> --raw <dir> --out <dir>
"""
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
RAW = ROOT / ".work" / "voxcpm_raw"
MANIFEST = ROOT / ".work" / "voxcpm_refs_manifest.json"
OUT = ROOT / "assets" / "voice_ref_voxcpm2"
BIN = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin"
FF, FP = str(BIN / "ffmpeg.exe"), str(BIN / "ffprobe.exe")

LO, HI = 8.0, 15.0          # QUY_TAC §4: 8-15 s
TARGET_LUFS = -18.0         # QUY_TAC §4: -20 ... -16 LUFS

# F0 muc tieu do chot o TAO_GIONG_MAU_VOXCPM2.md muc 3
F0_TARGET = {
    "H": (100, 106), "D": (138, 148), "C": (202, 212),
    "W1": (228, 242), "W2": (180, 192), "W3": (162, 175), "W4": (120, 128),
}

# Chuoi ffmpeg giong het higgs_make_refs.py:73-76, them duoi cat khoang lang cuoi
FLT = ("aresample=24000:resampler=soxr,"
       "loudnorm=I=-18:TP=-1.5:LRA=11,"
       "silenceremove=start_periods=1:start_threshold=-50dB,"
       "areverse,silenceremove=start_periods=1:start_threshold=-50dB,areverse")


def dur(p):
    r = subprocess.run([FP, "-v", "error", "-show_entries", "format=duration",
                        "-of", "csv=p=0", str(p)], capture_output=True, text=True)
    return float(r.stdout.strip())


def f0_median(path):
    """F0 trung vị (autocorrelation) - dung ham co san cua project neu import duoc."""
    sys.path.insert(0, str(ROOT / ".work"))
    try:
        from voice_audition import pcm, f0_median as _f0   # noqa: E402
        x, sr = pcm(path, 16000)
        return _f0(x, sr)
    except Exception as exc:                                   # fallback: tu tinh
        import numpy as np
        x, sr = pcm_local(path, 16000)
        win, hop, out = int(0.04 * sr), int(0.01 * sr), []
        for s in range(0, len(x) - win, hop):
            f = x[s:s + win]
            if np.sqrt((f ** 2).mean()) < 0.02:
                continue
            f = f - f.mean()
            ac = np.correlate(f, f, "full")[win - 1:]
            lo, hi = int(sr / 400), int(sr / 70)
            k = lo + int(np.argmax(ac[lo:hi]))
            if ac[k] > 0.3 * ac[0]:
                out.append(sr / k)
        return float(np.median(out)) if out else 0.0


def pcm_local(path, sr=16000):
    import numpy as np
    r = subprocess.run([FF, "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(sr),
                        "-f", "s16le", "-"], capture_output=True)
    return np.frombuffer(r.stdout, np.int16).astype(np.float32) / 32768, sr


def find_take(role, take):
    """Tim file mp3: uu tien .work/voxcpm_raw/<role>/<take>, sau do .work/voxcpm_raw/<take>."""
    for cand in (RAW / role / take, RAW / take, RAW / role):
        if cand.is_file():
            return cand
        if cand.is_dir():
            hits = sorted(cand.glob("*.mp3"))
            if hits:
                return hits[0]
    return None


def main():
    global RAW, MANIFEST, OUT
    args = sys.argv[1:]
    for i, a in enumerate(args):
        if a == "--raw" and i + 1 < len(args):
            RAW = Path(args[i + 1])
        elif a == "--manifest" and i + 1 < len(args):
            MANIFEST = Path(args[i + 1])
        elif a == "--out" and i + 1 < len(args):
            OUT = Path(args[i + 1])

    if not MANIFEST.exists():
        raise SystemExit(
            "Thieu manifest: %s\n"
            "  Tao file voi du:\n"
            '  { "H": { "take": "H_take01.mp3", "control": "...", "text": "..." } }' % MANIFEST)
    # utf-8-sig: manifest do nguoi dung sua bang Notepad / PowerShell hay them BOM
    man = json.loads(MANIFEST.read_text(encoding="utf-8-sig"))
    OUT.mkdir(parents=True, exist_ok=True)
    report, problems = {}, []

    for role in sorted(man):
        item = man[role]
        take = item.get("take")
        text = (item.get("text") or "").strip()
        src = find_take(role, take) if take else None
        if src is None:
            problems.append(f"{role}: khong tim thay audio (take={take!r})")
            continue
        if not text:
            problems.append(f"{role}: thieu 'text' (ref_text) trong manifest")
            continue

        wav = OUT / f"{role}.wav"
        subprocess.run([FF, "-y", "-v", "error", "-i", str(src),
                        "-af", FLT, "-ac", "1", "-ar", "24000", "-c:a", "pcm_s16le", str(wav)],
                       check=True)
        (OUT / f"{role}.txt").write_text(text, encoding="utf-8")

        seconds = dur(wav)
        f0 = f0_median(wav)
        lo_hi = F0_TARGET.get(role)
        notes = []
        if not (LO <= seconds <= HI):
            notes.append(f"THOI LUONG {seconds:.1f}s ngoai [{LO}-{HI}]s")
        if lo_hi and f0:
            if not (lo_hi[0] * 0.88 <= f0 <= lo_hi[1] * 1.12):
                notes.append(f"F0 {f0:.0f}Hz ngoai dai muc tieu {lo_hi[0]}-{lo_hi[1]}Hz")

        report[role] = {
            "voice_source": "VoxCPM2 (OpenBMB) - Voice Design",
            "control_instruction": item.get("control", ""),
            "target_text": text,
            "source_file": src.as_posix(),
            "seconds": round(seconds, 2),
            "f0_median_hz": round(f0, 1),
            "f0_target_hz": list(lo_hi) if lo_hi else None,
            "sample_rate": 24000,
            "channels": 1,
            "lufs_target": TARGET_LUFS,
            "model": "openbmb/VoxCPM2",
            "license": "Apache-2.0",
            "attribution_required": False,
            "notes": notes,
        }
        flag = ("  !! " + "; ".join(notes)) if notes else ""
        print(f"{role}: {src.name} -> {seconds:.1f}s  F0 {f0:.0f}Hz{flag}")
        if notes:
            problems.append(f"{role}: " + "; ".join(notes))

    (OUT / "refs.json").write_text(json.dumps(report, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"\nDa ghi {len(report)} vai vao {OUT}")
    if problems:
        print("\nCAN SUA:")
        for p in problems:
            print("  - " + p)
        sys.exit(1)


if __name__ == "__main__":
    main()
