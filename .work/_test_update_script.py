import json
import re

m = json.load(open(".work/tts_manifest_EN_t02.json", encoding="utf-8"))
script = json.load(open(".work/script_tap02_EN.json", encoding="utf-8"))

# Group manifest items by element ID
by_elem = {}
for item in m:
    eid, idx = item["id"].split("#")
    if eid not in by_elem:
        by_elem[eid] = []
    # clean SSML pauses from text for script and display
    clean_text = re.sub(r"<#[^#]+#>", "", item["text"]).strip()
    clean_text = re.sub(r"\s+", " ", clean_text)
    words = len(clean_text.split())
    by_elem[eid].append({
        "id": item["id"],
        "text": clean_text,
        "words": words,
        "role": item.get("role")
    })

print(f"Grouped into {len(by_elem)} LOI elements, total sentences: {sum(len(v) for v in by_elem.values())}")

# Update script elements
for e in script:
    eid = e["id"]
    if eid in by_elem:
        e["sentences"] = by_elem[eid]
        # full text is combination of sentences
        e["text"] = " ".join(s["text"] for s in by_elem[eid])

# Check total sentences in updated script
tot = sum(len(e.get("sentences", [])) for e in script)
print(f"Updated script has {len(script)} elements and {tot} sentences.")
