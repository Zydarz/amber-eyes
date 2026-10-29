import json, re
p = r"D:\TEST\Gax\Audi\.work\tap03_review\parsed_final.json"
els = json.load(open(p, encoding="utf-8"))
LATIN = re.compile(r"[A-Za-z]{3,}")
for e in els:
    if e["kind"] != "LOI":
        continue
    for s in e["sentences"]:
        for q in re.findall(r"\u201c([^\u201d]+)\u201d", s["text"]):
            latin = " ".join(LATIN.findall(q))
            ratio = len(latin) / max(len(q), 1)
            flag = "ENGLISH" if ratio > 0.45 else "ok"
            print(f'{s["id"]:<10} [{flag}] {q[:110]}')
