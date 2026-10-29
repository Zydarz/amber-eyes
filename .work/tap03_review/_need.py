import json

p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
els = json.load(open(p, encoding="utf-8"))
NEEDLES = [
    "I killed my mother",
    "Stop me",
    "coed killer",
    "giống mẹ hắn",
    "how huge this guy was",
    "Prison records listed his IQ",
    "cool and soft-spoken",
    "several lengthy interviews",
    "study me and find out",
    "Society is not ready",
    "place for me in society",
    "more like a father",
    "luôn muốn người ta ngước nhìn lên",
    "hundreds of people",
    "The Lust Murderer",
    "đồng thời",
    "tra tấn đến chết",
    "Ord Drive",
    "Aiko Koo",
    "mèo",
    "cửa bẩy",
    "thiến hoạn",
    "Overt Hostility",
    "lưới VICAP",
]
for e in els:
    if e["kind"] != "LOI":
        continue
    for s in e["sentences"]:
        for n in NEEDLES:
            if n.lower() in s["text"].lower():
                print(f'{s["id"]:<10} | {s["text"][:190]}')
                break
