import shutil
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
CU = ROOT / ".work" / "_cu" / "t06_truoc_dung_lai_20261103"
CU.mkdir(parents=True, exist_ok=True)
SRC = ROOT / "02_SAN_XUAT" / "Tap06" / "xuat_ban"
FILES = ["Tap06_master.mp4", "Tap06_master.mp3", "Tap06.srt", "thumbnail.png"]
for n in FILES:
    s = SRC / n
    if s.exists():
        shutil.copy2(s, CU / n)
        print(f"backup  {n}  {(CU / n).stat().st_size:,} B")
for n in ["shots_t06.json", "timeline_s_t06.json", "script_tap06.json",
          "higgs_selection_t06.json", "tts_manifest_t06.json", "acting_tap06.json"]:
    s = ROOT / ".work" / n
    if s.exists():
        shutil.copy2(s, CU / n)
        print(f"backup  .work/{n}")
print("=>", CU)
