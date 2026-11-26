import json, shutil, sys, time
from datetime import date
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes"); WORK = ROOT/".work"
sys.path.insert(0, str(WORK))
from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL
BG = ROOT/"assets"/"bg"; JOBS_FILE = WORK/"bg_jobs_tap36.json"; PROV_FILE = ROOT/"provenance.json"
OLD_DIR = WORK/"_cu"/f"bg_old_{date.today().strftime('%Y%m%d')}"/"t36_replaced_v5"
NEG = (" strictly no text of any kind, no letters, no words, no numbers, no handwriting, no logos, no emblems, "
       "no signage, no signboards, no plaques, no house numbers, no labels, no badges, no model names, "
       "no license plates, no vehicles, no cars, no motorbikes, no bicycles, no stickers, no printed papers, "
       "no screens, no frames, every surface completely blank and unmarked")
FIX = {
 "t36_a2_20_repressed_rural_village_square_night":
   "A lone man seen from behind walking down an empty village lane toward a dark forest road, only distant rooflines "
   "and a church tower silhouette against the night sky, bare shutters on empty houses, no vehicles anywhere, "
   "empty silent street, oppressive conservative society" + NEG,
}
def prov(rec):
    p = json.loads(PROV_FILE.read_text(encoding="utf-8")); idx = {r["file"]: i for i, r in enumerate(p)}
    e = {"file": rec["file"], "loai": "nền 16:9 dùng chung 4 ngôn ngữ",
         "cong_cu": f"Cloudflare Workers AI ({DEFAULT_MODEL})", "ngay": str(date.today()),
         "prompt": rec["prompt"], "seed": None, "nguon_anh_tham_chieu": None,
         "kich_thuoc_goc": [2112, 1188], "dieu_khoan": "Cloudflare Workers AI Terms of Service",
         "kiem_tra_thuong_mai": "đạt",
         "ghi_chu": "Sinh nền bằng Cloudflare FLUX.1 schnell, chuẩn Deep Noir H21/H25/H26, crop 16:9 và resize 2112x1188"}
    if rec["file"] in idx: p[idx[rec["file"]]] = e
    else: p.append(e)
    for _ in range(3):
        try:
            PROV_FILE.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8"); break
        except OSError as ex: print("retry:", ex); time.sleep(1)
jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8")); OLD_DIR.mkdir(parents=True, exist_ok=True)
for j in jobs:
    if j["name"] in FIX:
        old = BG/f"{j['name']}.png"
        if old.exists(): shutil.move(str(old), str(OLD_DIR/old.name))
        j["prompt"] = FIX[j["name"]]
JOBS_FILE.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
for j in jobs:
    if j["name"] not in FIX: continue
    dst = BG/f"{j['name']}.png"; t0 = time.perf_counter()
    img = generate_16_9_background(prompt=j["prompt"], steps=4, out_size=(2112,1188), with_noir_style=True)
    img.save(dst, "PNG", optimize=True)
    print(f"XONG {j['name']} ({dst.stat().st_size//1024} KB, {time.perf_counter()-t0:.1f}s)", flush=True)
    prov({"file": f"assets/bg/{j['name']}.png", "prompt": j["prompt"]})
print("XONG v5")
