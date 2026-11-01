"""Ten file / thu muc / dataset cua chuoi Higgs theo TAP + NGON NGU (mot cho duy nhat).

  AE_EP=03            -> Tap 03 tieng Viet
  AE_EP=02 AE_LANG=en -> Tap 02 tieng Anh (moi file mang them "_EN")
  AE_EP=02 AE_LANG=ja -> Tap 02 tieng Nhat (moi file mang them "_JA")
  AE_ACT=3            -> chi hoi 3 (hau to "_a3")

Tieng Viet giu NGUYEN ten cu (Tap 02 khong hau to; tap khac "_tXX") — kiem hoi quy L9.
Giong mau VN va EN TACH RIENG hoan toan (QUY_TAC_AUDIO_HIGGS.md §4.4): thu muc dataset,
dataset Kaggle, bang gan vai khac nhau; clip EN bat buoc duoi "_EN".
"""
import os
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent          # .work/
KH = HERE / "kaggle_higgs"

LANG = os.environ.get("AE_LANG", "vi").strip().lower()
EN = LANG == "en"
JA = LANG == "ja"
FOREIGN = LANG != "vi"                                   # EN/JA: bo giong mau rieng, ten file "_XX"
if LANG not in ("vi", "en", "ja"):
    raise SystemExit("Higgs chi ho tro AE_LANG=vi|en|ja (dang la %r)" % LANG)
EPN = os.environ.get("AE_EP", "02").strip().zfill(2)
ACT = os.environ.get("AE_ACT", "").strip()

LS = "_" + LANG.upper() if FOREIGN else ""                                 # hau to ngon ngu
_A = "_a" + ACT if ACT else ""
# SFX: spec / out / cache / kernel. VN Tap 02 ca tap = "" (ten cu).
SFX = "" if (EPN == "02" and not ACT and not FOREIGN) else "%s_t%s%s" % (LS, EPN, _A)
# SFX khong tinh hoi (file gop ca tap: exclude, merge, finish...)
SFX_EP = "" if (EPN == "02" and not FOREIGN) else "%s_t%s" % (LS, EPN)
TAG = "%st%s%s" % (LANG.upper() + "_" if FOREIGN else "", EPN, _A)          # "t02" | "t03_a3" | "EN_t02"
EP_TAG = "%st%s" % (LANG.upper() + "_" if FOREIGN else "", EPN)            # "t02" | "EN_t02"

PAYLOAD_SRC = KH / ("higgs_payload%s_t%s.json" % (LS, EPN))           # nguon (export_higgs_payload)
PAYLOAD_NAME = "higgs_payload%s_t%s%s.json" % (LS, EPN, _A)            # trong dataset
DS = KH / ("dataset_voxcpm2_" + LANG if FOREIGN else "dataset_voxcpm2")
DATASET = "chiduong2026/amber-eyes-voice-ref-voxcpm2" + ("-" + LANG if FOREIGN else "")
REF_DIR = "/kaggle/input/" + DATASET.split("/")[1]
ROLE_MAP = HERE / ("g9_role_map%s.json" % LS)
SCRIPT = HERE / ("script_tap%s%s.json" % (EPN, LS))
TTS_MANIFEST = HERE / ("tts_manifest%s_t%s.json" % (LS, EPN))
PROD = KH / ("out_higgs_prod" + SFX)                                     # thu muc tai ve
PROD_EP = KH / ("out_higgs_prod" + SFX_EP)
R2 = KH / ("out_higgs_r2" + SFX_EP)
F0_JSON = HERE / ("_f0_%s.json" % EP_TAG)
EXCLUDE = HERE / ("higgs_exclude_f0_%s.json" % EP_TAG)
CER_ROWS = HERE / ("higgs_cer_rows_%s.json" % TAG)
CER_ROWS_EP = HERE / ("higgs_cer_rows_%s.json" % EP_TAG)
SELECTION = HERE / ("higgs_selection_%s.json" % EP_TAG)
AUDIO_OUT = HERE / ("audio_s_higgs%s_t%s" % (LS, EPN))                 # = edition.w("audio_s_higgs")
MASTER_DIR = HERE.parent / "02_SAN_XUAT" / ("Tap%s%s" % (EPN, LS)) / "xuat_ban"
MASTER_MP3 = MASTER_DIR / ("Tap%s%s_master.mp3" % (EPN, LS))


def check_ref_lang(clip):
    """Chan tron giong mau giua cac ngon ngu (§4.4): clip ban XX bat buoc duoi "_XX"."""
    stem = pathlib.Path(clip).stem
    tag = re.search(r"_(EN|JA|KO)$", stem)
    if FOREIGN and stem[-3:] != LS:
        raise SystemExit("AE_LANG=%s nhung clip %r khong co duoi %s (§4.4)" % (LANG, clip, LS))
    if not FOREIGN and tag:
        raise SystemExit("ban tieng Viet nhung clip %r la giong %s (§4.4)" % (clip, tag.group(1)))
