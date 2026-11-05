import json
r = json.load(open(".work/speech_full_recognized_en_t02_novad.json", encoding="utf-8"))
for seg in r[126:132]:
    print(f"[{seg['index']}] {seg['start']:.2f} - {seg['end']:.2f}: {seg['text']}")
