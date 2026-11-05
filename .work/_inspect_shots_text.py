import json
d = json.load(open(".work/shots_text_tap02_EN.json", encoding="utf-8"))
for k in ["1-05", "1-06", "1-07", "1-08", "1-09", "1-10"]:
    print(k, ":", d.get(k))
