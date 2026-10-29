import json, os
jobs = json.load(open(r"D:\TEST\Gax\Audi\.work\bg_jobs_tap03.json", encoding="utf-8"))
names = [j["name"] for j in jobs]
bg = r"D:\TEST\Gax\Audi\assets\bg"
png = {f[:-4] for f in os.listdir(bg) if f.startswith("t3_") and f.endswith(".png")}
print("prompts:", len(names), "| png:", len(png))
print("MISSING png :", [n for n in names if n not in png])
print("EXTRA png   :", [n for n in sorted(png) if n not in names])
