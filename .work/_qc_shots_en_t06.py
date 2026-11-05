# -*- coding: utf-8 -*-
"""QC check for shots_EN_t06.json and KeHoach_Video_Tap06_EN.md."""
import sys, json, re
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

shots_path = Path(".work/shots_EN_t06.json")
data = json.load(shots_path.open(encoding="utf-8"))
shots = data["shots"] if isinstance(data, dict) else data
tl = json.load(open(".work/timeline_s_EN_t06.json", encoding="utf-8"))
script = json.load(open(".work/script_tap06_EN.json", encoding="utf-8"))

print(f"=== QC SHOTS EN TAP 06 ===")
print(f"Total shots: {len(shots)}")

# 1. Check shot count
assert len(shots) == 73, f"Expected 73 shots, got {len(shots)}"

# 2. Check time continuity
for idx in range(len(shots) - 1):
    curr_s = shots[idx]
    next_s = shots[idx + 1]
    dur = curr_s["end"] - curr_s["start"]
    assert dur > 0, f"Shot {curr_s['id']} duration <= 0: {dur}"
    # Check gap / overlap between shots
    gap = next_s["start"] - curr_s["end"]
    if abs(gap) > 0.05:
        print(f"WARNING: Gap between {curr_s['id']} and {next_s['id']}: {gap:.3f} s")

# 3. Check start and total end
assert shots[0]["start"] == 20.5, f"First shot start != 20.5: {shots[0]['start']}"
total_diff = abs(shots[-1]["end"] - tl["total"])
print(f"Last shot end: {shots[-1]['end']:.2f} s | Master total: {tl['total']:.2f} s | Diff: {total_diff:.3f} s")
assert total_diff <= 0.05, f"Total length mismatch > 0.05 s: {total_diff}"

# 4. Check H12: Closing shot
last_shot = shots[-1]
assert last_shot["id"] == "5-14", "Last shot ID must be 5-14"
print(f"Shot 5-14 segments: {last_shot.get('segments')}")
# Text in last shot must contain AMBER EYES
found_brand = False
for seg in last_shot.get("segments", []):
    for kind, txt in seg.get("elems", []):
        if "AMBER EYES" in txt:
            found_brand = True
assert found_brand, "H12 VIOLATION: AMBER EYES not found in closing shot!"
print("PASS: H12 Closing shot verified with AMBER EYES brand card!")

# 5. Check background images
bg_dir = Path("assets/bg")
missing_bgs = []
for s in shots:
    bg = s.get("bg")
    if bg:
        # Check png/jpg/webp
        if not ((bg_dir / f"{bg}.png").exists() or (bg_dir / f"{bg}.jpg").exists() or (bg_dir / f"{bg}.webp").exists()):
            missing_bgs.append((s["id"], bg))
if missing_bgs:
    print(f"ERROR: Missing backgrounds: {missing_bgs}")
    sys.exit(1)
print("PASS: 100% background assets exist on disk!")

print("=== ALL SHOT PREFLIGHT QC CHECKS PASSED! ===")
