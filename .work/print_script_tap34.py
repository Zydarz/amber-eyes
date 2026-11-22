import json

script = json.load(open(".work/script_tap34.json", encoding="utf-8"))
for item in script:
    if "sentences" in item:
        print(f"\n--- Element {item['id']} ({len(item['sentences'])} sentences) ---")
        for s in item['sentences']:
            print(f"[{s['id']}] {s['text']}")
