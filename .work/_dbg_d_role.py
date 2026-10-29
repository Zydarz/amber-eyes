import json
m = json.load(open(r"D:\TEST\Gax\Audi\.work\tts_manifest_EN_t02.json", encoding="utf-8"))
ids = ["1.17#1", "1.17#5", "2.05#2", "2.05#6", "2.05#10", "2.05#14",
       "2.08#2", "2.08#6", "4.08#1", "4.08#5", "4.08#9", "4.10#4"]
d = {x["id"]: x for x in m}
for i in ids:
    x = d[i]
    print(f"{i:>9} {x['emotion']:>10} speed={x['speed']}  {x['text'][:60]}")
