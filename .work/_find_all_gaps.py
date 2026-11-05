import json

r = json.load(open(".work/speech_full_recognized_en_t02_novad.json", encoding="utf-8"))
print(f"Total segments: {len(r)}")
for i in range(len(r) - 1):
    cur_end = r[i]["end"]
    nxt_start = r[i + 1]["start"]
    gap = nxt_start - cur_end
    if gap > 3.0:
        print(f"Gap of {gap:.2f}s between [{r[i]['index']}] ({cur_end:.2f}s) and [{r[i+1]['index']}] ({nxt_start:.2f}s)")
        print(f"   Before: '{r[i]['text']}'")
        print(f"   After : '{r[i+1]['text']}'")
