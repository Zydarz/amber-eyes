import json

script = json.load(open(".work/script_tap34.json", encoding="utf-8"))
for item in script:
    if "sentences" in item:
        act = item.get("act")
        first_id = item["sentences"][0]["id"]
        last_id = item["sentences"][-1]["id"]
        spk = item["sentences"][0].get("speaker")
        txt = item["sentences"][0].get("text")[:50]
        print(f"Act {act} | {item['id']} ({len(item['sentences'])} sentences): {first_id} -> {last_id} [{spk}] '{txt}'")
