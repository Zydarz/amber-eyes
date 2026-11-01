import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
s = json.loads(pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\script_tap04.json")
               .read_text(encoding="utf-8-sig"))
ids = {el["id"]: el.get("kind") for el in s}
for m in ["1.06", "4.05", "1.15", "1.11", "1.01", "1.02", "5.09"]:
    print("  ", m, "->", ids.get(m, "KHONG CO"))
print("   tong element:", len(ids))
