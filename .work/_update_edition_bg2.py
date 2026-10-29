import sys
from pathlib import Path

path = Path(".work/edition.py")
text = path.read_text(encoding="utf-8")

old_str = '''        "acting": WORK / "acting_tap05.json",
        "sfx_sheet": WORK / "sfx_tap05.json",
        "act1_cue": "1.15", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: "bgm_cello_sad.mp3", 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 4: "bgm_ambient_deep.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {},
        "flag_hold_shots": (),'''

new_str = '''        "acting": WORK / "acting_tap05.json",
        "sfx_sheet": WORK / "sfx_tap05.json",
        "act1_cue": "1.15", "silence_cue": "1.11", "click_cues": ("1.08",),
        "bed": {1: "bgm_cello_sad.mp3", 2: ("bgm_piano_minimal.mp3", "bgm_piano_minimal_v2.mp3"),
                3: ("bgm_cello_sad.mp3", "bgm_sub_drone.mp3"), 4: "bgm_ambient_deep.mp3", 5: "bgm_piano_warm.mp3"},
        "sfx_cues": [],
        "combo": {}, "inset": {}, "bg2": {"2-06": "t5_park_trashcan_drop", "2-10": "t5_church_council_altar"},
        "flag_hold_shots": (),'''

norm_text = text.replace("\r\n", "\n")
norm_old = old_str.replace("\r\n", "\n")
norm_new = new_str.replace("\r\n", "\n")

if norm_old not in norm_text:
    print("ERROR: old_str not found in edition.py!")
    sys.exit(1)

norm_text = norm_text.replace(norm_old, norm_new, 1)
path.write_text(norm_text, encoding="utf-8")
print("SUCCESS: Updated edition.py for Episode 05!")
