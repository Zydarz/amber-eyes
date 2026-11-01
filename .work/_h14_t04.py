import json, pathlib
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
tl = json.loads((HERE / "timeline_s_t04.json").read_text(encoding="utf-8-sig"))
sh = json.loads((HERE / "shots_t04.json").read_text(encoding="utf-8-sig"))
print("timeline total = %.3f | shots total = %.3f | lech = %.4f s" % (tl["total"], sh["total"], abs(tl["total"]-sh["total"])))
s = sh["shots"]
print("shot cuoi: %s %.2f-%.2f (timeline total %.2f)" % (s[-1]["id"], s[-1]["start"], s[-1]["end"], tl["total"]))
# dem doan trong timeline
print("items:", len(tl["items"]), "| dau:", tl["items"][0]["id"], tl["items"][0]["start"], "| cuoi:", tl["items"][-1]["id"], tl["items"][-1]["end"])
