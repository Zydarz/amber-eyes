import json, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

print("=== 3. KIỂM TRA SFX_TAP05.JSON & FILE ÂM THANH ===")
sfx_sheet_path = Path(".work/sfx_tap05.json")
assert sfx_sheet_path.exists(), "sfx_tap05.json không tồn tại!"

sheet = json.loads(sfx_sheet_path.read_text(encoding='utf-8'))
SFX = Path("assets/sfx")

# 1. Check ambience files
amb_miss = []
for a, b, name, rel in sheet.get("ambience", []):
    fp = SFX / name
    fp_t2 = SFX / "t2" / name
    if fp.exists():
        status = "OK"
    elif fp_t2.exists():
        status = "OK (t2)"
    else:
        status = "MISSING!"
        amb_miss.append(name)
    print(f"Ambience [{a} -> {b}]: {name:<30} ({rel} dB) -> {status}")

# 2. Check cues files
cue_miss = []
for ref, where, off, name, rel in sheet.get("cues", []):
    fp = SFX / name
    fp_t2 = SFX / "t2" / name
    if fp.exists():
        status = "OK"
    elif fp_t2.exists():
        status = "OK (t2)"
    else:
        status = "MISSING!"
        cue_miss.append(name)
    print(f"Cue [{ref} @ {where} {off:+.1f}s]: {name:<30} ({rel} dB) -> {status}")

# 3. Check music drop
drop_ranges = sheet.get("music_drop", {}).get("ranges", [])
print(f"Tổng số đoạn drop nhạc: {len(drop_ranges)}")
for a, b in drop_ranges:
    print(f"  Drop nhạc: {a} -> {b}")

print(f"\nTổng kết SFX: Ambience missing={len(amb_miss)} | Cues missing={len(cue_miss)}")
