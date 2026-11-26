import hashlib, json, sys
from pathlib import Path
from PIL import Image
import numpy as np
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
BG = ROOT/"assets"/"bg"
jobs = json.load(open(ROOT/".work"/"bg_jobs_tap36.json", encoding="utf-8"))
names = [j["name"] for j in jobs]
files = [BG/f"{n}.png" for n in names]
missing = [f.name for f in files if not f.exists()]
small  = [f.name for f in files if f.exists() and f.stat().st_size < 100_000]
dims, means, mds5 = {}, [], {}
for f in files:
    if not f.exists(): continue
    im = Image.open(f); dims[im.size] = dims.get(im.size,0)+1
    a = np.asarray(im.convert("L"), dtype=np.float32)
    means.append(a.mean())
    mds5.setdefault(hashlib.md5(f.read_bytes()).hexdigest(), []).append(f.name)
dup = {k:v for k,v in mds5.items() if len(v)>1}
print("Tong job:", len(jobs), "| thieu file:", len(missing), "| file <100KB:", len(small))
print("Kich thuoc:", dims)
print(f"Do sang trung binh: min {min(means):.1f} · max {max(means):.1f} · tb {sum(means)/len(means):.1f}")
print("Anh trung byte-identical:", len(dup))
for k,v in list(dup.items())[:5]: print("  ", v)
print("Tong dung luong:", round(sum(f.stat().st_size for f in files if f.exists())/1048576,1), "MB")
prov = json.load(open(ROOT/"provenance.json", encoding="utf-8"))
p36 = [r for r in prov if r["file"].startswith("assets/bg/t36_")]
print("provenance.json ban ghi t36:", len(p36))
print("Tat ca co kich thuoc goc 2112x1188:", all(r.get("kich_thuoc_goc")==[2112,1188] for r in p36))
