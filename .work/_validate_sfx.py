import json
from pathlib import Path

man = json.loads(Path(".work/tts_manifest_t04.json").read_text(encoding="utf-8"))
valid_ids = {m["id"] for m in man}
script = json.loads(Path(".work/script_tap04.json").read_text(encoding="utf-8"))
valid_elem_ids = {e["id"] for e in script}

sfx = json.loads(Path(".work/sfx_tap04.json").read_text(encoding="utf-8"))

print("Checking ambience:")
for a, b, f, db in sfx.get("ambience", []):
    if a not in valid_ids:
        print(f"  INVALID ambience start: {a}")
    if b not in valid_ids:
        print(f"  INVALID ambience end: {b}")

print("Checking cues:")
for ref, where, off, f, db in sfx.get("cues", []):
    if ref not in valid_ids and ref not in valid_elem_ids:
        print(f"  INVALID cue ref: {ref}")

print("Checking music_drop ranges:")
for a, b in sfx.get("music_drop", {}).get("ranges", []):
    if a not in valid_ids:
        print(f"  INVALID music_drop start: {a}")
    if b not in valid_ids:
        print(f"  INVALID music_drop end: {b}")
