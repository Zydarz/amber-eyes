import json,sys
a=int(sys.argv[1])
tl=json.load(open(".work/timeline_s_t14.json",encoding="utf-8"))["items"]
d=json.load(open(".work/_t14_bg_desc.json",encoding="utf-8"))
print("== SENTENCES")
for i,it in enumerate([x for x in tl if x["act"]==a]): print(i,it["id"],it["text"][:105])
print("== IMAGES")
for n,v in d.items():
    if v[0]==a and "closing_dossier" not in n: print(n[4:],"|",v[1][:75])
