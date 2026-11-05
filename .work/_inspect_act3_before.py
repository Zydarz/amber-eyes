import json

recog = json.load(open(".work/speech_full_recognized_en_t02_novad.json", encoding="utf-8"))
for r in recog[90:106]:
    print(f"[{r['index']}] {r['start']:.2f} - {r['end']:.2f}: {r['text']}")
