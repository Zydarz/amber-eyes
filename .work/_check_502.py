import json
r = json.load(open(".work/speech_full_recognized_en_t02.json", encoding="utf-8"))
for x in r:
    if 1110 <= x["start"] <= 1140:
        print(f"[{x['index']}] {x['start']:.2f} - {x['end']:.2f}: {x['text']}")
