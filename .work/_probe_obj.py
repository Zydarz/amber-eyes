import json, sys
sys.stdout.reconfigure(encoding="utf-8")
keys = {"VN": ["vật hóa", "đạo cụ sống", "ái kỷ"], "EN": ["objectif", "living props", "narcissis"],
        "JA": ["対象化", "生きた小道具", "自己愛"], "KO": ["사물화", "살아있는 소품", "자기애"]}
for tag, ks in keys.items():
    els = json.load(open(rf"D:/TEST/Gax/amber-eyes/.work/script_tap02_{tag}.json", encoding="utf-8"))
    print(f"=== {tag}")
    for e in els:
        if e.get("kind") != "LOI": continue
        for s in e["sentences"]:
            low = s["text"].lower()
            for k in ks:
                if k.lower() in low:
                    print(f"   {s['id']} [{k}] {s['text'][:110]}")
                    break
