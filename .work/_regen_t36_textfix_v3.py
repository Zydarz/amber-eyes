import json, shutil, sys, time
from datetime import date
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes"); WORK = ROOT/".work"
sys.path.insert(0, str(WORK))
from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL
BG = ROOT/"assets"/"bg"; JOBS_FILE = WORK/"bg_jobs_tap36.json"; PROV_FILE = ROOT/"provenance.json"
OLD_DIR = WORK/"_cu"/f"bg_old_{date.today().strftime('%Y%m%d')}"/"t36_replaced_v3"
NEG = (" strictly no text of any kind, no letters, no words, no numbers, no handwriting, no logos, "
       "no emblems, no signage, no labels, no badges, no model names, no license plates, no stickers, "
       "no printed papers, no screens, no frames, every surface completely blank and unmarked")
VEH = (" the vehicle is only a vague featureless dark shape in shadow with no badge, no model name, "
       "no plate and no readable detail anywhere on it")
FIX = {
 "t36_a1_08_parked_car_closed_windows_misted":
   "Front three-quarter view of a vintage car facing the viewer on a quiet night road, headlights glowing, "
   "windscreen fogged with condensation, no occupants visible, calm false sense of safety, moonless dark" + VEH + NEG,
 "t36_a1_13_shadow_emerging_from_thicket":
   "A pitch-black faceless silhouette standing motionless at the edge of a thick thicket, a parked car far behind "
   "him reduced to a vague dark shape in the fog" + VEH + NEG,
 "t36_a2_07_young_driver_avoiding_hill_pullouts_dusk":
   "Dusk on a Florence suburban road, a small car far down the road facing the viewer with only its headlights and "
   "a vague shape visible, one distant silhouette of a young driver glancing nervously at the darkening hills, fear spreading" + VEH + NEG,
 "t36_a2_20_repressed_rural_village_square_night":
   "Rural 1970s Italian village square at night, a stern church and a plain shuttered building with no signboard, "
   "a silhouette of a man getting into a car reduced to a vague dark shape in shadow, toward the dark forest road, "
   "oppressive conservative society" + VEH + NEG,
 "t36_a3_29_quantico_profile_1989_loner_manual_laborer_map":
   "A dim bare office in 1989, a plain corkboard covered by completely unmarked blank sheets arranged as a loose human "
   "outline, a small wooden toy car and a plain hill contour map on an otherwise empty wooden table, one cold desk lamp, "
   "heavy shadow, nothing else on the table" + NEG,
 "t36_a3_31_fbi_report_shelved_dusty_local_police_office":
   "A dusty provincial Italian police office with tall shelves of plain closed folders, one thick closed dossier, "
   "a bare empty desk, two detectives in silhouette studying a blank sheet, completely plain bare walls" + NEG,
 "t36_a4_07_police_station_summons_nervous_silhouette":
   "A small Italian police station at night, a nervous silhouette sitting alone in a hard chair across a bare desk under a "
   "swinging lamp, the officers' silhouettes frozen in surprise, completely bare walls with nothing hanging on them, "
   "nothing on the desk" + NEG,
 "t36_a4_08_alliance_of_shadows_three_silhouettes_hills":
   "Three dark silhouettes standing apart on a night hilltop in 1980s Tuscany, a parked old car behind them reduced to "
   "a vague dark shape in the mist, faces hidden entirely, sinister alliance, distant lights of Florence" + VEH + NEG,
 "t36_a4_16_haunting_cars_in_dark_lane_dream_fog":
   "Dreamlike foggy night lane with several empty old cars reduced to ghostly featureless silhouettes fading in the "
   "thick mist, no people, haunting curse concept" + VEH + NEG,
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
    PROV_FILE.write_text(json.dumps(p, ensure_ascii=False, indent=2), encoding="utf-8")
jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8")); OLD_DIR.mkdir(parents=True, exist_ok=True)
for j in jobs:
    if j["name"] in FIX:
        old = BG/f"{j['name']}.png"
        if old.exists(): shutil.move(str(old), str(OLD_DIR/old.name))
        j["prompt"] = FIX[j["name"]]
JOBS_FILE.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
print("-> da doi", len(FIX), "prompt")
ok = 0
for j in jobs:
    if j["name"] not in FIX: continue
    dst = BG/f"{j['name']}.png"; t0 = time.perf_counter()
    try:
        img = generate_16_9_background(prompt=j["prompt"], steps=4, out_size=(2112,1188), with_noir_style=True)
        img.save(dst, "PNG", optimize=True)
        print(f"XONG {j['name']} ({dst.stat().st_size//1024} KB, {time.perf_counter()-t0:.1f}s)", flush=True)
        prov({"file": f"assets/bg/{j['name']}.png", "prompt": j["prompt"]}); ok += 1
    except Exception as e:
        print(f"LOI {j['name']}: {e}", flush=True)
print(f"HOAN TAT {ok}/{len(FIX)}")
