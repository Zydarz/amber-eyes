import json, pathlib, re
W = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")
ROOT = pathlib.Path(r"D:\TEST\Gax\amber-eyes")
shots = json.loads((W / "shots_EN_t03.json").read_text(encoding="utf-8"))["shots"]
bgs = sorted({s.get("bg") for s in shots if s.get("bg")})
print("nen dung trong 110 shot:", len(bgs))
missing = [b for b in bgs if not (ROOT / "assets" / "bg" / f"{b}.png").exists()]
print("nen THIEU file:", missing or "khong co")
prov = (ROOT / "provenance.json").read_text(encoding="utf-8")
nopro = [b for b in bgs if f'"{b}"' not in prov and b not in prov]
print("nen KHONG co dong trong provenance.json:", nopro or "khong co")
print("tong dong 't3_' trong provenance:", len(re.findall(r"t3_[a-z0-9_]+", prov)))
