"""Sinh payload Higgs nguon cho mot tap: .work/kaggle_higgs/higgs_payload_tXX.json

Dung lai tts_sentences.plan_items() (so -> chu, acting, TTS_FIX, N1/N2) nen loi doc
giong het duong MiniMax. build_spec.py doc file nay (thay clip theo g9_role_map.json,
bo the cam xuc).

  AE_EP=03 py -3 .work/export_higgs_payload.py            -> ghi payload Tap 03
  AE_EP=02 py -3 .work/export_higgs_payload.py --check    -> so voi payload hien co, khong ghi
"""
import json
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import edition as ED  # noqa: E402
import tts_sentences as TS  # noqa: E402
import higgs_paths as P  # noqa: E402  (AE_LANG=en -> higgs_payload_EN_tXX.json)

OUT = P.PAYLOAD_SRC


def wav_name(sid):
    """'1.03#1' -> '1_03_1.wav' (quy uoc payload Tap 02)."""
    ma, k = sid.split("#")
    a, b = ma.split(".")
    return "%s_%s_%d.wav" % (a, b, int(k))


# Doi chu rieng cho Higgs (dung lai tu payload Tap 02 lam tay 30/10/2026):
#   "..." -> bo (G1) · <#0.35#> -> <|prosody:pause|> · chu thich ngoai ngu trong ngoac -> bo (G7)
RE_PAREN_FOREIGN = re.compile(r"\s*\(([^()]*)\)")
VI_CHARS = re.compile(r"[ăâđêôơưáàảãạấầẩẫậắằẳẵặéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]", re.I)


def higgs_text(t):
    if P.FOREIGN:
        # Ban EN/JA: loi doc MiniMax (acting_tapXX_EN.json) gai the ngat <#x#> GIUA cau.
        # Higgs §5 / G1: chi giu ngat sau dau ":" truoc cau trich, bo moi the khac.
        t = re.sub(r":\s*<#[\d.]+#>", ": <|prosody:pause|>", t)
        t = re.sub(r"\s*<#[\d.]+#>\s*", " ", t)
        t = t.replace("...", "")
        # K7: so La Ma sau ten nguoi doc bang chu ("Elizabeth II" -> "Elizabeth the Second")
        if P.EN:
            t = re.sub(r"\b([A-Z][a-z]+) (II|III|IV)\b",
                       lambda m: "%s the %s" % (m.group(1), {"II": "Second", "III": "Third", "IV": "Fourth"}[m.group(2)]), t)
        # G11 ban JA: chu so -> so kanji (2009年 -> 二千九年), cung bo doi so voi ja_cer (Q3a)
        if P.JA:
            # G7: chu thich tieng Anh trong ngoac "(Existential Vacuum)" -> bo khoi loi doc (T08, 06/11/2026)
            t = re.sub(r"\s*[（(][A-Za-z][^()（）]*[)）]", "", t)
            import ja_cer
            t = ja_cer.ja_numbers(t)
        return re.sub(r"  +", " ", t).strip()
    t = RE_PAREN_FOREIGN.sub(lambda m: m.group(0) if VI_CHARS.search(m.group(1)) else "", t)
    t = re.sub(r"<#[\d.]+#>", "<|prosody:pause|>", t)
    t = t.replace("...", "")
    return re.sub(r"  +", " ", t).strip()


def build():
    items = []
    for it in TS.plan_items():
        items.append({
            "id": it["id"], "role": it["role"], "ref_wav": "", "ref_txt": "",
            "text_plain": higgs_text(it["text"]), "text": higgs_text(it["text"]), "emotion": it["emotion"],
            "emotion_tag": "", "speed": it["speed"], "speed_base": None,
            "file": wav_name(it["id"]), "display": it["display"],
        })
    return {"episode": ED.EPN, "lang": P.LANG, "model": "bosonai/higgs-tts-3-4b",
            "ref_dir": P.REF_DIR, "role_ref": {},
            "items": items}


if __name__ == "__main__":
    new = build()
    if "--check" in sys.argv:
        old = json.loads(OUT.read_text(encoding="utf-8-sig"))
        oi = {i["id"]: i for i in old["items"]}
        ni = {i["id"]: i for i in new["items"]}
        print("cu %d cau · moi %d cau · cung id: %s" % (len(oi), len(ni), oi.keys() == ni.keys()))
        for f in ("role", "text_plain", "emotion", "display"):
            diff = [k for k in oi if k in ni and str(oi[k][f]).strip() != str(ni[k][f]).strip()]
            print("  khac %-10s %d %s" % (f, len(diff), diff[:5]))
        sys.exit(0)
    OUT.write_text(json.dumps(new, ensure_ascii=False, indent=1), encoding="utf-8")
    print("%d cau -> %s" % (len(new["items"]), OUT))
