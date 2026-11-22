import subprocess
import pathlib
import json

ROOT = pathlib.Path(".")
dirs = [
    ROOT / "02_SAN_XUAT/TIKTOK/Tap02",
    ROOT / "02_SAN_XUAT/TIKTOK/Tap02_EN",
    ROOT / "02_SAN_XUAT/TIKTOK/Tap02_JA"
]

results = []
for d in dirs:
    for cid in ["TK1", "TK2", "TK3", "TK4", "TK5"]:
        wav = d / f"{cid}_master_audio.wav"
        if not wav.exists():
            continue
        cmd = [
            "ffmpeg", "-i", str(wav),
            "-af", "silencedetect=noise=-60dB:d=0.3",
            "-f", "null", "-"
        ]
        p = subprocess.run(cmd, stderr=subprocess.PIPE, text=True)
        silences = []
        for line in p.stderr.splitlines():
            if "silence_start:" in line:
                silences.append(line)
        results.append({
            "file": str(wav),
            "silence_count": len(silences),
            "pass": len(silences) == 0
        })

print(json.dumps(results, indent=2))
