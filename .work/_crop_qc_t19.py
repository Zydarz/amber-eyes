import json
from pathlib import Path
from PIL import Image

ROOT = Path(r"D:/TEST/Gax/amber-eyes")
CROP_DIR = ROOT / ".work/qc_crops_t19"
CROP_DIR.mkdir(parents=True, exist_ok=True)

# Danh sách một số cảnh có vật thể giấy/bìa/màn hình để soi zoom 100%
check_list = [
    ("t19_b1_curcio_steely_gaze_dossier_folder", (600, 400, 1500, 1000)),
    ("t19_b1_clinical_malingering_forensic_manual", (700, 400, 1500, 1000)),
    ("t19_b1_abandoned_valentines_card_corridor", (800, 400, 1400, 900)),
    ("t19_b2_cctv_split_screen_observation_console", (500, 300, 1600, 1000)),
    ("t19_b3_school_expulsion_letter_desk_shadows", (600, 400, 1500, 900)),
    ("t19_b4_florida_legal_statute_volume_pages", (700, 400, 1500, 1000)),
    ("t19_b5_memorial_bronze_plaque_candlelight", (600, 300, 1500, 900)),
    ("t19_b5_redflag1_dark_envelope_threat_leakage", (700, 400, 1400, 900)),
]

for name, box in check_list:
    img_path = ROOT / f"assets/bg/{name}.png"
    if img_path.exists():
        with Image.open(img_path) as im:
            crop = im.crop(box)
            crop.save(CROP_DIR / f"crop_{name}.png")
            print(f"Đã trích xuất crop: crop_{name}.png")
