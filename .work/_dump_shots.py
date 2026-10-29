import json
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

script = json.loads(open(".work/script_tap04.json", encoding="utf-8").read())
shots = json.loads(open(".work/shots_t04.json", encoding="utf-8").read())["shots"]

sents = {}
for e in script:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sents[s["id"]] = s["text"]

with open(".work/shots_analysis.txt", "w", encoding="utf-8") as out:
    for s in shots:
        sid = s["id"]
        sids = s.get("sentences", [])
        txt = " // ".join(f"[{x}]: {sents.get(x, '')}" for x in sids)
        out.write(f"\n{'='*80}\n")
        out.write(f"SHOT {sid} | BG: {s.get('bg')} | TEMPLATE: {s.get('template')} | ROLE: {s.get('role')} | FLAGS: {s.get('flags')}\n")
        out.write(f"AUDIO: {txt}\n")
        for idx, sg in enumerate(s.get("segments", [])):
            out.write(f"  SEG {idx} (at={sg.get('at_sentence')}): {sg.get('elems')}\n")

print("Exported to .work/shots_analysis.txt")
