import json, pathlib, collections
w = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
t = json.loads((w/"timeline_s_t03.json").read_text(encoding="utf-8-sig"))
it = t["items"]
print("total:", t["total"], "intro:", t["intro"], "items:", len(it))
print("item0 keys:", list(it[0].keys()))
print("item0:", json.dumps(it[0], ensure_ascii=False)[:500])
print("itemLast:", json.dumps(it[-1], ensure_ascii=False)[:500])
print("markers:", json.dumps(t["markers"], ensure_ascii=False)[:400])
print("acts:", json.dumps(t["acts"], ensure_ascii=False)[:400])
roles = collections.Counter(i.get("role") for i in it)
print("roles:", roles)
