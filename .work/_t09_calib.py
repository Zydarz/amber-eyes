import io, json, os, re, sys
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

KB = {
    "t08": {"vi": "01_KICH_BAN/Tap08/kichban_tap08_23102026.md",
            "en": "01_KICH_BAN/Tap08_EN/kichban_tap08_EN.md",
            "ja": "01_KICH_BAN/Tap08_JA/kichban_tap08_JA.md"},
    "t09": {"vi": "01_KICH_BAN/Tap09/kichban_tap09_23102026.md",
            "en": "01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md",
            "ja": "01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md"},
}
TL = {("t08","vi"): "timeline_s_t08.json", ("t08","en"): "timeline_s_EN_t08.json", ("t08","ja"): "timeline_s_JA_t08.json",
      ("t09","vi"): "timeline_s_t09.json"}

def chars(rel):
    els = parse_file(str(ROOT/rel))
    d = {}
    for e in els:
        if e["kind"] != "LOI": continue
        for i, s in enumerate(e["sentences"], 1):
            d[f"{e['id']}#{i}"] = s["text"]
    return d

print("=== TẬP 08: đo THỰC từ timeline đã đo (master mp3 thật) ===")
cal = {}
for lang in ("vi","en","ja"):
    tl = json.loads((ROOT/".work"/TL[("t08",lang)]).read_text(encoding="utf-8"))
    ch = chars(KB["t08"][lang])
    speech = sum(i["end"]-i["start"] for i in tl["items"])
    n_ch = sum(len(v) for v in ch.values())
    sil = tl["total"] - speech
    cal[lang] = (n_ch, speech, sil, tl["total"])
    print(f"  {lang}: chars={n_ch} speech={speech:.2f}s silence={sil:.2f}s total={tl['total']:.2f}s "
          f"· rate={n_ch/speech:.3f} ch/s")

vi_ch, vi_sp, vi_sil, vi_tot = cal["vi"]
print()
print("=== HỆ SỐ SUY RA TỪ TẬP 08 (dùng để dựng Tập 09) ===")
for lang in ("en","ja"):
    ch, sp, sil, tot = cal[lang]
    print(f"  {lang}/vi: speech={sp/vi_sp:.4f}  chars={ch/vi_ch:.4f}  "
          f"=> rate_ratio(vn/en)={ (ch/sp) / (vi_ch/vi_sp):.4f} ch/s ratio")
    print(f"       silence={sil:.2f} vs vn silence={vi_sil:.2f}")

print()
print("=== TẬP 09: ký tự theo ngôn ngữ ===")
ch9 = {}
for lang in ("vi","en","ja"):
    ch9[lang] = chars(KB["t09"][lang])
    print(f"  {lang}: chars={sum(len(v) for v in ch9[lang].values())} n={len(ch9[lang])}")

print()
print("=== TẬP 09 VN: đo thực để neo ===")
tl9 = json.loads((ROOT/".work/timeline_s_t09.json").read_text(encoding="utf-8"))
sp9 = sum(i["end"]-i["start"] for i in tl9["items"])
sil9 = tl9["total"] - sp9
print(f"  speech={sp9:.2f}s silence={sil9:.2f}s total={tl9['total']:.2f}s "
      f"rate={sum(len(v) for v in ch9['vi'].values())/sp9:.3f} ch/s")

print()
print("=== DỰ ĐOÁN TẬP 09 EN/JA (dùng hệ số Tập 08) ===")
for lang in ("en","ja"):
    r_ch, r_sp, r_sil, _ = cal[lang]
    ratio = (r_ch/r_sp) / (vi_ch/vi_sp)          # ch/s của lang so với VN
    pred_speech = sp9 / ratio
    pred_silence = sil9                          # giữ nguyên cấu trúc nghỉ (pause_after giống nhau)
    print(f"  {lang}: rate_ratio={ratio:.4f} → speech≈{pred_speech:.1f}s  silence={pred_silence:.1f}s "
          f"→ total≈{pred_speech+pred_silence+22.41+9.0:.1f}s")
