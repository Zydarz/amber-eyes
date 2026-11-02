import json
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
old = json.loads((W/"_cu"/"shots_t03.json.bak_20261102_104741").read_text(encoding="utf-8-sig"))
print("old shots:", len(old["shots"]), "old total:", old.get("total"))
for s in old["shots"]:
    if s["id"].startswith("2-1") or s["id"].startswith("5-0"):
        print(f'  {s["id"]}  {s["start"]}-{s["end"]}  sents={s["sentences"]}  bg={s["bg"]}')
