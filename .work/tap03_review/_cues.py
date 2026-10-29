import json

p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_tap03.json"
els = json.load(open(p, encoding="utf-8"))
for e in els:
    if e["kind"] != "LOI":
        d = (e.get("desc") or "")[:78]
        extra = f' sec={e["sec"]}' if e["kind"] == "NGHI" else ""
        print(f'{e["id"]:>6} {e["kind"]:<4}{extra:<12} {d}')
print()
print("--- LOI first-sentence ids (for need/summary/cue anchors) ---")
for e in els:
    if e["kind"] == "LOI":
        s = e["sentences"][0]
        print(f'{e["id"]:>6} {e["role"]:<3} first={s["id"]:<10} | {s["text"][:64]}')
