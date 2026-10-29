import json
import sys

sys.stdout.reconfigure(encoding="utf-8")

with open(".work/script_tap09.json", encoding="utf-8") as f:
    data = json.load(f)

turns = [t for t in data if t.get("kind") == "LOI"]
total_s = sum(len(t.get("sentences", [])) for t in turns)
print(f"Total turns: {len(turns)}, Total sentences: {total_s}")
for t in turns:
    sents = t.get("sentences", [])
    s_ids = f"{sents[0]['id']}..{sents[-1]['id']}" if sents else ""
    first_txt = sents[0]["text"][:40] if sents else ""
    print(f"Hoi {t.get('act')} | Turn {t.get('id'):<5} | Role {t.get('role')} | {len(sents):>2} c | {s_ids:<14} | {first_txt}...")
