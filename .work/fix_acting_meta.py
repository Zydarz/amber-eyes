import json
from pathlib import Path

path = Path(".work/acting_tap40.json")
data = json.loads(path.read_text(encoding="utf-8"))
data["_meta"]["episode"] = "40"
data["_meta"]["description"] = "Acting & Pause parameters for Tap 40 (227 sentences)"
path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
print("Updated _meta for acting_tap40.json")
