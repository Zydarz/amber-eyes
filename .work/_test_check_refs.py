import pathlib

ROOT = pathlib.Path(".")

ROLE_MAPS = {
    "vi": {
        "H": (ROOT / "assets/voice_ref_voxcpm2/H.wav", ROOT / "assets/voice_ref_voxcpm2/H.txt"),
        "D": (ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav", ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.txt"),
        "C": (ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav", ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.txt"),
        "N2": (ROOT / "assets/voice_ref_voxcpm2_g9/W5_HIGH.wav", ROOT / "assets/voice_ref_voxcpm2_g9/W5_HIGH.txt")
    },
    "en": {
        "H": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/H_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/H_EN.txt"),
        "D": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/D_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/D_EN.txt"),
        "C": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/C_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/C_EN.txt"),
        "N2": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/N2_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/N2_EN.txt")
    },
    "ja": {
        "H": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/H_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/H_JA.txt"),
        "D": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/D_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/D_JA.txt"),
        "C": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/C_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/C_JA.txt"),
        "N2": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/N2_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/N2_JA.txt")
    }
}

all_ok = True
for lang, rmap in ROLE_MAPS.items():
    print(f"--- Checking {lang} ---")
    for r, (w, t) in rmap.items():
        w_ok = w.exists()
        t_ok = t.exists()
        print(f"  [{r}] wav={w_ok} ({w}) | txt={t_ok} ({t})")
        if not (w_ok and t_ok):
            all_ok = False

if all_ok:
    print("ALL REFERENCE FILES EXIST!")
else:
    print("SOME REFERENCE FILES MISSING!")
