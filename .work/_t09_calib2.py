import io, json, os, re, sys
from pathlib import Path
ROOT = Path(r"D:/TEST/Gax/amber-eyes")
sys.path.insert(0, str(ROOT/".work"))
from parse_kichban import parse_file

KB = {
 "t08": {"vi":"01_KICH_BAN/Tap08/kichban_tap08_23102026.md","en":"01_KICH_BAN/Tap08_EN/kichban_tap08_EN.md","ja":"01_KICH_BAN/Tap08_JA/kichban_tap08_JA.md"},
 "t09": {"vi":"01_KICH_BAN/Tap09/kichban_tap09_23102026.md","en":"01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md","ja":"01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md"},
}
TLF = {("t08","vi"):"timeline_s_t08.json",("t08","en"):"timeline_s_EN_t08.json",("t08","ja"):"timeline_s_JA_t08.json",
       ("t09","vi"):"timeline_s_t09.json"}

def chars(rel):
    els = parse_file(str(ROOT/rel)); d={}
    for e in els:
        if e["kind"]!="LOI": continue
        for i,s in enumerate(e["sentences"],1): d[f"{e['id']}#{i}"]=s["text"]
    return d

def stats(tlname):
    tl = json.loads((ROOT/".work"/tlname).read_text(encoding="utf-8"))
    speech = sum(i["end"]-i["start"] for i in tl["items"])
    return tl, speech

print("=== KIỂM CHỨNG CÔNG THỨC TRÊN TẬP 08 (dùng timeline ĐÃ ĐO THẬT) ===")
ch8 = {l: chars(KB["t08"][l]) for l in ("vi","en","ja")}
tl8 = {}; sp8 = {}
for l in ("vi","en","ja"):
    tl8[l], sp8[l] = stats(TLF[("t08",l)])
r_vi = sum(len(v) for v in ch8["vi"].values()) / sp8["vi"]
print(f"  r_vi = {r_vi:.4f} ch/s")
for l in ("en","ja"):
    r_l = sum(len(v) for v in ch8[l].values()) / sp8[l]
    K = r_vi / r_l
    pred = sum(len(ch8[l][k]) for k in ch8[l]) / r_l
    print(f"  {l}: r={r_l:.4f} ch/s  K=r_vi/r_l={K:.4f}  speech_pred={pred:.2f}s  ACTUAL={sp8[l]:.2f}s  "
          f"err={100*(pred-sp8[l])/sp8[l]:+.2f}%")

print()
print("=== ÁP DỤNG CHO TẬP 09 (dự đoán EN/JA) ===")
ch9 = {l: chars(KB["t09"][l]) for l in ("vi","en","ja")}
tl9v, sp9 = stats(TLF[("t09","vi")])
r9_vi = sum(len(v) for v in ch9["vi"].values()) / sp9
print(f"  r_vi(t09) = {r9_vi:.4f} ch/s   speech_vn={sp9:.2f}s")
pred = {}
for l in ("en","ja"):
    r_l = r_vi * (1.0 if l=="en" else (sp8["vi"]/sp8["ja"]) * 0)  # placeholder
    # dùng đúng K đo được ở Tập 08
    K = {"en": r_vi/ (sum(len(v) for v in ch8['en'].values())/sp8['en']),
         "ja": r_vi/ (sum(len(v) for v in ch8['ja'].values())/sp8['ja'])}[l]
    r_l = r_vi / K
    p = sum(len(v) for v in ch9[l].values()) / r_l
    pred[l] = p
    print(f"  {l}: K={K:.4f} r={r_l:.4f} ch/s → speech_pred={p:.2f}s")

print()
print("=== per-sentence scaling: dur_lang = dur_vn * (ch_lang/ch_vi) * K ===")
for l in ("en","ja"):
    K = {"en": r_vi/ (sum(len(v) for v in ch8['en'].values())/sp8['en']),
         "ja": r_vi/ (sum(len(v) for v in ch8['ja'].values())/sp8['ja'])}[l]
    durs = []
    for it in tl9v["items"]:
        sid = it["id"]
        d = (it["end"]-it["start"]) * (len(ch9[l][sid])/len(ch9["vi"][sid])) * K
        durs.append(d)
    ds = sorted(durs)
    print(f"  {l}: n={len(durs)} min={ds[0]:.2f} p25={ds[len(ds)//4]:.2f} med={ds[len(ds)//2]:.2f} "
          f"p75={ds[3*len(ds)//4]:.2f} max={ds[-1]:.2f} SUM={sum(durs):.2f}s (pred {pred[l]:.2f}s)")
    out = [(it["id"], round(d,2)) for it,d in zip(tl9v["items"], durs) if d<3.0 or d>15.0]
    print(f"     ngoài [3,15]: {len(out)} -> {out[:12]}")
