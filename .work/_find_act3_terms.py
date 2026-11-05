import json

recog = json.load(open(".work/speech_full_recognized_en_t02_novad.json", encoding="utf-8"))
for r in recog:
    t = r["text"].lower()
    if any(k in t for k in ["fantasy", "tolerance", "escalate", "trigger", "astound", "compartment"]):
        print(f"[{r['index']}] {r['start']:.2f} - {r['end']:.2f}: {r['text']}")
