import json, subprocess
from pathlib import Path
W = Path(__file__).resolve().parents[1] / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffmpeg.exe"
man = json.loads((W / "tts_manifest_t02.json").read_text(encoding="utf-8"))
it = next(m for m in man if m["id"] == "2.05#11")
print("manifest 2.05#11:", {k: it[k] for k in ("role", "emotion", "speed", "text")})
def dur(p):
    r = subprocess.run([str(FF), "-i", str(p)], capture_output=True, text=True, encoding="utf-8", errors="replace")
    for ln in r.stderr.splitlines():
        if "Duration" in ln:
            return ln.strip()
    return "?"
print("\nTHOI LUONG:")
print("  production (Korean_ColdYoungMan):", dur(W / "audio_s_t02" / "s2_05_11.mp3"))
for vid in ("English_Diligent_Man", "English_DecentYoungMan", "male-qn-qingse", "Korean_CockyGuy"):
    fs = sorted((W / "cer_xac_minh_giong_nam").glob(f"p2_*_{vid}_2_05-11*.mp3"))
    for f in fs:
        print(f"  {vid:26s}: {dur(f)}  ({f.stat().st_size} bytes)")
