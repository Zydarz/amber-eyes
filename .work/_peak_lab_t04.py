"""Do thi nghiem: cau hinh limiter + encoder nao cho true peak <= -1,5 dBFS tren file cuoi.

Vung do: 840-900 s (vung co dinh 0 dBFS tai ~869,5 s trong file cuoi hien tai).
Moi cau hinh: WAV -> [filter] -> AAC 192k -> do max_volume (mau) + ebur128 true peak.
"""
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
FF = ROOT / ".work" / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
WAV = ROOT / ".work" / "audio_master_t04.wav"
TMP = ROOT / ".work" / "_peak_lab"
TMP.mkdir(exist_ok=True)
SS, T = 840, 60

CONFIGS = [
    ("A. khong filter", []),
    ("B. alimiter -2.0 dBFS attack 5 (hien tai)", ["-af", "alimiter=limit=0.7943:attack=5:release=50:level=disabled"]),
    ("C. alimiter -2.0 dBFS attack 0.5", ["-af", "alimiter=limit=0.7943:attack=0.5:release=50:level=disabled"]),
    ("D. alimiter -3.0 dBFS attack 1", ["-af", "alimiter=limit=0.7079:attack=1:release=50:level=disabled"]),
    ("E. alimiter -4.0 dBFS attack 1", ["-af", "alimiter=limit=0.6310:attack=1:release=50:level=disabled"]),
    ("F. alimiter -2.0 attack 0.5 + latency", ["-af", "alimiter=limit=0.7943:attack=0.5:release=50:level=disabled:latency=1"]),
    ("G. aresample 48k + alimiter -3.0 attack 1", ["-af", "aresample=48000,alimiter=limit=0.7079:attack=1:release=50:level=disabled"]),
]


def measure(path):
    r = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(path), "-af",
                        "volumedetect", "-f", "null", "-"], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    mv = re.search(r"max_volume:\s*(-?[\d.]+) dB", r.stderr)
    r2 = subprocess.run([str(FF), "-hide_banner", "-nostats", "-i", str(path), "-af",
                         "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True,
                        encoding="utf-8", errors="replace")
    lufs = re.findall(r"I:\s*(-?[\d.]+) LUFS", r2.stderr)
    pk = re.findall(r"Peak:\s*(-?[\d.]+) dBFS", r2.stderr)
    return (float(mv.group(1)) if mv else None,
            float(lufs[-1]) if lufs else None,
            float(pk[-1]) if pk else None)


for label, extra in CONFIGS:
    out = TMP / ("t_%s.m4a" % abs(hash(label)))
    cmd = [str(FF), "-y", "-v", "error", "-ss", str(SS), "-t", str(T), "-i", str(WAV),
           *extra, "-c:a", "aac", "-b:a", "192k", str(out)]
    r = subprocess.run(cmd, capture_output=True, text=True)
    if r.returncode != 0:
        print("%-42s LOI: %s" % (label, r.stderr[:120]))
        continue
    mv, lu, pk = measure(out)
    verdict = "DAT" if (pk is not None and pk <= -1.5) else "VUOT"
    print("%-42s sample %6s | LUFS %6s | truePeak %6s dBFS  => %s" % (
        label, ("%.1f" % mv) if mv is not None else "?", ("%.1f" % lu) if lu is not None else "?",
        ("%.1f" % pk) if pk is not None else "?", verdict))
    out.unlink()
