import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path("D:/TEST/Gax/amber-eyes")
W = ROOT / ".work"
PUB = ROOT / "02_SAN_XUAT/Tap02_JA/xuat_ban"
FF = W / "ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"

# 1. Backup (Rule L5)
BK = W / "_cu/ja_t02_bak_20261105_render"
BK.mkdir(parents=True, exist_ok=True)
print(f"=== 1. SAO LUU (L5) -> {BK} ===")

files_to_backup = [
    W / "timeline_s_JA_t02.json",
    W / "shots_JA_t02.json",
    ROOT / "02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md"
]
for f in files_to_backup:
    if f.exists():
        dst = BK / f.name
        shutil.copy2(f, dst)
        print(f"  Da sao luu: {f.name}")

# 2. Restore from commit 5e9910b9
print("\n=== 2. KHOI PHUC TU COMMIT 5e9910b9 ===")
for git_rel, target_path in [
    (".work/timeline_s_JA_t02.json", W / "timeline_s_JA_t02.json"),
    (".work/shots_JA_t02.json", W / "shots_JA_t02.json"),
    ("02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md", ROOT / "02_SAN_XUAT/Tap02_JA/KeHoach_Video_Tap02_JA.md")
]:
    res = subprocess.run(["git", "show", f"5e9910b9:{git_rel}"], capture_output=True, text=True, encoding="utf-8")
    if res.returncode != 0:
        raise SystemExit(f"Khong lay duoc 5e9910b9:{git_rel}")
    target_path.write_text(res.stdout, encoding="utf-8")
    print(f"  Khoi phuc thanh cong: {target_path.name}")

# 3. Verify restored files
print("\n=== 3. KIEM TRA CAC FILE DA KHOI PHUC ===")
tl = json.loads((W / "timeline_s_JA_t02.json").read_text(encoding="utf-8-sig"))
sh = json.loads((W / "shots_JA_t02.json").read_text(encoding="utf-8-sig"))
print(f"  Timeline total: {tl.get('total')} s · items: {len(tl.get('items', []))}")
print(f"  Shots total:    {sh.get('total')} s · shots: {len(sh.get('shots', []))}")

mp3 = PUB / "Tap02_JA_master.mp3"
res_dur = subprocess.run([str(FF), "-i", str(mp3)], capture_output=True, text=True, encoding="utf-8", errors="replace")
dur_mp3 = None
for line in (res_dur.stderr or "").splitlines():
    if "Duration:" in line:
        h, m, s = line.split("Duration:")[1].split(",")[0].strip().split(":")
        dur_mp3 = int(h) * 3600 + int(m) * 60 + float(s)
print(f"  Master MP3:     {dur_mp3} s")
drift = abs(dur_mp3 - tl["total"])
print(f"  Do lech audio vs timeline: {drift:.4f} s (cho phep <= 0.05 s) -> {'PASS' if drift <= 0.05 else 'FAIL'}")

# 4. Create audio_master_JA_t02.wav
wav_p = W / "audio_master_JA_t02.wav"
print(f"\n=== 4. TAO {wav_p.name} (44.1kHz stereo PCM) ===")
subprocess.run([
    str(FF), "-y", "-i", str(mp3),
    "-ar", "44100", "-ac", "2", "-c:a", "pcm_s16le",
    str(wav_p)
], check=True, capture_output=True)
print(f"  Tao WAV thanh cong: {wav_p.stat().st_size} bytes")

# 5. Build stems
print("\n=== 5. BUILD STEMS (stems_JA_t02) ===")
r_stems = subprocess.run([sys.executable, str(W / "_build_stems_ja_t02.py")],
                         capture_output=True, text=True, encoding="utf-8", errors="replace")
print(r_stems.stdout)
if r_stems.returncode != 0:
    print(r_stems.stderr)
    raise SystemExit("Loi khi build stems!")

stems_dir = W / "stems_JA_t02"
stems = list(stems_dir.glob("*.wav"))
print(f"  Stems da tao: {[s.name for s in stems]}")
