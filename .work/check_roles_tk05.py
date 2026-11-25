import json
from pathlib import Path

ROOT = Path(".")
role_maps = {
    "vi": {
        "H": (ROOT / "assets/voice_ref_voxcpm2/H.wav", ROOT / "assets/voice_ref_voxcpm2/H.txt"),
        "D": (ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav", ROOT / "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.txt"),
        "C": (ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav", ROOT / "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.txt"),
        "N1": (ROOT / "assets/voice_ref_voxcpm2_g9/W6_LOW.wav", ROOT / "assets/voice_ref_voxcpm2_g9/W6_LOW.txt"),
        "N2": (ROOT / "assets/voice_ref_voxcpm2_g9/W5_HIGH.wav", ROOT / "assets/voice_ref_voxcpm2_g9/W5_HIGH.txt")
    },
    "en": {
        "H": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/H_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/H_EN.txt"),
        "D": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/D_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/D_EN.txt"),
        "C": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/C_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/C_EN.txt"),
        "N1": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/N1_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/N1_EN.txt"),
        "N2": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/N2_EN.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_en/N2_EN.txt")
    },
    "ja": {
        "H": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/H_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/H_JA.txt"),
        "D": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/D_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/D_JA.txt"),
        "C": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/C_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/C_JA.txt"),
        "N1": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/N1_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/N1_JA.txt"),
        "N2": (ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/N2_JA.wav", ROOT / ".work/kaggle_higgs/dataset_voxcpm2_ja/N2_JA.txt")
    }
}

for lang, roles in role_maps.items():
    print(f"Checking {lang} voice references:")
    for r, (w, t) in roles.items():
        if not w.exists():
            print(f"  Missing WAV: {r} -> {w}")
        if not t.exists():
            print(f"  Missing TXT: {r} -> {t}")
print("Done checking voice references!")
