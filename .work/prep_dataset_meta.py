"""Lam moi dataset-metadata.json cua dataset Kaggle (mo ta + danh sach resource
theo clip tham chieu that co trong thu muc).

Chay truoc moi lan `kaggle datasets version`.
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent        # .work/
DS = HERE / "kaggle_higgs" / "dataset_voxcpm2"
META_P = DS / "dataset-metadata.json"

meta = json.loads(META_P.read_text(encoding="utf-8-sig"))

CLIPS = {
    "H.wav": "Host - nam 40 tuoi, tram am - 22.5s, F0 108 Hz",
    "D.wav": "Dieu tra vien - nam 50+, gia va khan - 22.3s, F0 128 Hz",
    "C.wav": "Chuyen gia tam ly - nu 50 tuoi - 23.5s, F0 209 Hz",
    "W1.wav": "Nguoi binh thuong W1 - nu tre 20 tuoi - 23.5s, F0 250 Hz",
    "W2.wav": "Nguoi binh thuong W2 - nu 50 tuoi - 26.7s, F0 200 Hz",
    "W3.wav": "Nguoi binh thuong W3 - nam 25 tuoi - 24.6s, F0 161 Hz",
    "W4.wav": "Nguoi binh thuong W4 - nam 50 tuoi - 26.2s, F0 137 Hz",
    "M_LOW.wav": "G9 moi - vai H - nam 40, rat tram (very low) - 19.3s, F0 96 Hz",
    "M_HIGH.wav": "G9 moi - vai D - nam 50+, cao (higher tenor) - 16.9s, F0 192 Hz",
    "W6_LOW.wav": "G9 moi - vai N1 - nu thap (low alto) - 28.1s, F0 179 Hz",
    "W5_HIGH.wav": "G9 moi - vai N2 - nu cao (soprano) - 19.1s, F0 289 Hz",
    "W6_LOW_S20.wav": "G9 - bien the hao -2.0 nua cung cua W6_LOW - 27.3s, F0 160 Hz",
    "W6_LOW_S25.wav": "G9 - bien the hao -2.5 nua cung cua W6_LOW - 27.3s, F0 158 Hz",
    "W6_LOW_S30.wav": "G9 - bien the hao -3.0 nua cung cua W6_LOW - 27.3s, F0 155 Hz",
    "W6_LOW_S35.wav": "G9 - bien the hao -3.5 nua cung cua W6_LOW - 27.3s, F0 150 Hz",
    "W6_LOW_S40.wav": "G9 - bien the hao -4.0 nua cung cua W6_LOW - 27.3s, F0 145 Hz",
}
EXTRA = {
    "refs.json": "Metadata tung clip: control_instruction, target_text, F0 do that, giay, license",
    "pilot_spec_v6.json": "Spec pilot v6: 13 o x 6 cau x 2 ban (do F0 clone that cho G9)",
    "pilot_payload_v6.json": "Payload pilot v6 (items: id -> text/emotion/ref_wav)",
    "prod_spec.json": "Spec san xuat Tap 02: 203 cau x 2 ban theo §7",
    "higgs_payload_t02.json": "Payload san xuat Tap 02 (203 cau, the co emotion)",
}

meta["subtitle"] = ("16 clip tham chieu tieng Viet cho Higgs v3 (7 goc + 4 moi G9 + 5 bien the)")
assert 20 <= len(meta["subtitle"]) <= 80, len(meta["subtitle"])
meta["description"] = (
    "Bo clip tham chieu tieng Viet cho kenh Amber Eyes, lam ref_audio cho Higgs Audio v3 "
    "zero-shot voice cloning.\n\n"
    "NGUON: openbmb/VoxCPM2 che do Voice Design (O Reference Audio) -> giay phep Apache-2.0, "
    "KHONG can ghi cong.\n\n"
    "7 clip goc (vai H D C W1-W4) + 4 clip MOI cho G9 (M_LOW, M_HIGH, W6_LOW, W5_HIGH) + "
    "5 bien the hao cao do cua W6_LOW (S20/S25/S30/S35/S40) de tach vai N1 khoi C va N2.\n"
    "Bien the S20-S40: phase vocoder (time-stretch + resample) tren chinh W6_LOW, giu nguyen "
    "thoi luong, ghi ro trong refs.json.\n\n"
    "Ky thuat: WAV PCM 16-bit mono 24.000 Hz, -18 LUFS, True Peak <= -1,5 dBFS, 16-28 s tieng.\n\n"
    "Sinh tu du an Amber Eyes (00_TIEU_CHUAN/QUY_TAC_GIONG_MAU_VOXCPM2.md). CHI DUNG NOI BO."
)

resources = []
for name in sorted(CLIPS):
    p = DS / name
    if not p.exists():
        continue
    resources.append({"path": name, "description": CLIPS[name]})
    txt = name.replace(".wav", ".txt")
    if (DS / txt).exists():
        resources.append({"path": txt, "description": "ref_text cua %s (trung chinh)" % name})
for name, desc in EXTRA.items():
    if (DS / name).exists():
        resources.append({"path": name, "description": desc})
meta["resources"] = resources

META_P.write_text(json.dumps(meta, ensure_ascii=False, indent=2), encoding="utf-8")
print("resources:", len(resources))
for r in resources:
    print("  %-24s %s" % (r["path"], r["description"][:70]))
print("\n->", META_P)
