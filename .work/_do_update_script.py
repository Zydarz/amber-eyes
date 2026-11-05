import json
import re
from pathlib import Path

ROOT = Path("D:/TEST/Gax/amber-eyes")
m = json.loads((ROOT / ".work/tts_manifest_EN_t02.json").read_text(encoding="utf-8"))
script_path = ROOT / ".work/script_tap02_EN.json"
script = json.loads(script_path.read_text(encoding="utf-8"))

by_elem = {}
for item in m:
    eid, idx = item["id"].split("#")
    if eid not in by_elem:
        by_elem[eid] = []
    clean_text = re.sub(r"<#[^#]+#>", "", item["text"]).strip()
    clean_text = re.sub(r"\s+", " ", clean_text)
    words = len(clean_text.split())
    by_elem[eid].append({
        "id": item["id"],
        "text": clean_text,
        "words": words
    })

for e in script:
    eid = e["id"]
    if eid in by_elem:
        e["sentences"] = by_elem[eid]
        e["text"] = " ".join(s["text"] for s in by_elem[eid])

script_path.write_text(json.dumps(script, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Updated {script_path} with {len(script)} elements, {sum(len(e.get('sentences',[])) for e in script)} sentences.")
