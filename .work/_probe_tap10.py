import json

d = json.load(open(".work/script_tap10.json", encoding="utf-8"))

with open(".work/_tap10_all_sentences.txt", "w", encoding="utf-8") as f:
    for act_idx in range(1, 6):
        f.write(f"\n==================== ACT {act_idx} ====================\n")
        for el in d:
            if el.get("act") == act_idx and el.get("kind") == "LOI":
                f.write(f"\n[{el['id']}] {el['role']} (dir: {el.get('direction', '')}):\n")
                for s in el.get("sentences", []):
                    f.write(f"  {s['id']}: {s['text']}\n")
