import json
import wave
import subprocess
import sys
from pathlib import Path
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"
FF = WORK / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
AUDIO_MASTER = ROOT / "02_SAN_XUAT/Tap02_EN/xuat_ban/Tap02_EN_master.mp3"
TL_PATH = WORK / "timeline_s_EN_t02.json"
OUT_DIR = WORK / "stems_EN_t02"
SR = 16000

if not TL_PATH.exists():
    print(f"Timeline {TL_PATH} does not exist yet.")
    sys.exit(1)

tl = json.loads(TL_PATH.read_text(encoding="utf-8"))
total = float(tl["total"])
items = tl["items"]
print(f"Master: {AUDIO_MASTER.name} | Total duration: {total:.2f}s | Sentences: {len(items)}")

# Decode audio master to 16kHz mono float32
raw = subprocess.run([
    str(FF), "-v", "error", "-i", str(AUDIO_MASTER),
    "-f", "f32le", "-ac", "1", "-ar", str(SR), "-"
], capture_output=True, check=True).stdout

x = np.frombuffer(raw, dtype=np.float32)
print(f"Decoded {len(x)} samples = {len(x)/SR:.2f}s")

OUT_DIR.mkdir(parents=True, exist_ok=True)
N = int(total * SR) + SR
roles = ("H", "D", "C", "N1", "N2")
stems = {r: np.zeros(N, dtype=np.float32) for r in roles}

for it in items:
    r = it.get("role")
    if r not in stems:
        print(f"Warning: unknown role {r} in {it['id']}")
        continue
    a = int(round(it["start"] * SR))
    b = int(round(it["end"] * SR))
    seg = x[a:b]
    if len(seg) > 0:
        stems[r][a:a + len(seg)] = seg

for r in roles:
    s = stems[r]
    s_clamped = np.clip(s, -1.0, 1.0)
    s_int16 = (s_clamped * 32767.0).astype(np.int16)
    out_file = OUT_DIR / f"{r}.wav"
    with wave.open(str(out_file), "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SR)
        wf.writeframes(s_int16.tobytes())
    print(f"Wrote stem: {out_file} ({len(s_int16)} samples)")

print(f"All 5 stems built successfully in {OUT_DIR}")
