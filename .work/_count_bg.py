import json
import re
from pathlib import Path

BG = Path(r"D:/TEST/Gax/amber-eyes/assets/bg")
files = list(BG.glob("*.png"))
print("PNG goc assets/bg:", len(files))
print("PNG trong _raw:", len(list((BG / "_raw").glob("*.png"))))

eps = {}
for p in files:
    m = re.match(r"^t(\d+)_", p.name)
    if m:
        eps[int(m.group(1))] = eps.get(int(m.group(1)), 0) + 1
print("tap co anh (tien to tNN_):", sorted(eps))
print("tong anh theo tien to:", sum(eps.values()))

for t in ("26", "40"):
    jobs = json.loads(Path(f"D:/TEST/Gax/amber-eyes/.work/bg_jobs_tap{t}.json").read_text(encoding="utf-8"))
    have = sum(1 for j in jobs if (BG / (j["name"] + ".png")).exists())
    print(f"tap {t}: {have}/{len(jobs)} job co file")
