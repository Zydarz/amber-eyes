import json

recog = json.load(open(".work/speech_full_recognized_en_t02.json", encoding="utf-8"))
for r in recog:
    if "Sunday" in r["text"] or "February" in r["text"] or "Ottawa" in r["text"] or "Smyth" in r["text"] or "Smythe" in r["text"]:
        print(f"[{r['index']}] {r['start']:.2f} - {r['end']:.2f}: {r['text']}")
