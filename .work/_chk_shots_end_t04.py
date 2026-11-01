import json, pathlib
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
sh = json.loads((HERE / "shots_t04.json").read_text(encoding="utf-8-sig"))
by = {s["id"]: s for s in sh["shots"]}
s = by["5-18"]
print("5-18:", s["start"], "-", s["end"], "| template:", s["template"], "| variant:", s["variant"], "| bg:", s["bg"])
print("segments:")
for seg in s["segments"]:
    print("   at_sentence:", seg["at_sentence"], "|", [(e[0], e[1]) for e in seg["elems"]])
print()
print("8 shot co scrim — kiem tra segments co chu bi chim (nen sang):")
for sid in ("1-06","1-10","1-15","1-17","2-08","4-03","4-07","4-13"):
    x = by.get(sid)
    if not x: print("   %s: THIEU" % sid); continue
    txt = " ".join(e[1] for seg in x["segments"] for e in seg["elems"])
    print("   %-6s template=%-4s variant=%-9s | %s" % (sid, x["template"], x["variant"], txt[:70]))
