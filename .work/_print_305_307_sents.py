import json
s = json.load(open(".work/script_tap02_EN.json", encoding="utf-8"))
for e in s:
    if e["id"] in ("3.05", "3.07"):
        print(f"=== Element {e['id']} ({len(e.get('sentences',[]))} sents) ===")
        for sent in e.get("sentences", []):
            print(f"  {sent['id']}: {sent['text']}")
