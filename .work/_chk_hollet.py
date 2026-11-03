import json, pathlib, re
W = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
sc = json.loads((W / "script_tap03_EN.json").read_text(encoding="utf-8"))
items = sc["items"] if isinstance(sc, dict) and "items" in sc else sc
for it in items:
    t = it.get("text", "")
    if re.search(r"Hollet|Sally|59 year|52 year", t, re.I):
        print(f"[{it.get('id')}] ({it.get('role','?')}) {t}")
