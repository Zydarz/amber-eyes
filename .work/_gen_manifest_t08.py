import json, sys
sys.path.insert(0, "D:/TEST/Gax/amber-eyes/.work")
import tts_sentences as TS, edition as ED
items = TS.plan_items()
p = ED.w("tts_manifest.json")
p.write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding="utf-8")
print(ED.EPN, ED.LANG if hasattr(ED,"LANG") else "", len(items), p.name)
