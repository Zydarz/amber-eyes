import json
import numpy as np
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
BG = ROOT / "assets" / "bg"
jobs = json.load(open(ROOT / ".work" / "bg_jobs_tap06.json", encoding="utf-8"))

stats = []
for j in jobs:
    name = j["name"]
    p = BG / f"{name}.png"
    if not p.exists():
        stats.append({"name": name, "exists": False})
        continue
    im = Image.open(p)
    w, h = im.size
    arr = np.asarray(im.convert("L"), np.float32)
    mean_val = float(arr.mean())
    std_val = float(arr.std())
    p_size_mb = p.stat().st_size / (1024 * 1024)
    stats.append({
        "name": name,
        "exists": True,
        "size": (w, h),
        "mb": round(p_size_mb, 2),
        "mean_brightness": round(mean_val, 1),
        "std_contrast": round(std_val, 1),
    })

print(f"Total checked: {len(stats)}")
print("Dimensions check:", all(s["size"] == (2112, 1188) for s in stats if s["exists"]))
print("Total size MB:", round(sum(s["mb"] for s in stats if s["exists"]), 1))

# Highlight top brightest and darkest images
brightest = sorted(stats, key=lambda x: x["mean_brightness"], reverse=True)[:3]
darkest = sorted(stats, key=lambda x: x["mean_brightness"])[:3]
highest_contrast = sorted(stats, key=lambda x: x["std_contrast"], reverse=True)[:3]

print("\nBrightest scenes (e.g. dawn, daylight, snow exterior, lecture):")
for b in brightest:
    print(f"  {b['name']}: brightness {b['mean_brightness']}/255, contrast {b['std_contrast']}")

print("\nDarkest scenes (e.g. crawl space, night highway, basement):")
for d in darkest:
    print(f"  {d['name']}: brightness {d['mean_brightness']}/255, contrast {d['std_contrast']}")

print("\nHighest contrast (chiaroscuro):")
for c in highest_contrast:
    print(f"  {c['name']}: contrast std {c['std_contrast']}, brightness {c['mean_brightness']}")
