import json, glob, os
p = r"D:\TEST\Gax\Audi\provenance.json"
d = json.load(open(p, encoding="utf-8"))
have = {e.get("file","").split("/")[-1] for e in d if e.get("file","").startswith("assets/bg/t3_")}
disk = {os.path.basename(f) for f in glob.glob(r"D:\TEST\Gax\Audi\assets\bg\t3_*.png")}
print("trong provenance nhung khong tren dia:", sorted(have - disk))
print("tren dia NHUNG chua co provenance:", sorted(disk - have))
