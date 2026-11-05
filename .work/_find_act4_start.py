import json

recog = json.load(open(".work/speech_full_recognized_en_t02.json", encoding="utf-8"))
for r in recog[180:195]:
    print(f"[{r['index']}] {r['start']:.2f} - {r['end']:.2f}: {r['text']}")
