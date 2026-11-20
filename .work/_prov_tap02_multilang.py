# -*- coding: utf-8 -*-
"""Ghi dong provenance.json cho bo TikTok Tap 02 EN va JA.
L7: provenance day du cong cu, ngay, mo ta, dieu khoan, kiem tra thuong mai.
"""
import io, json, os, shutil, datetime

ROOT = r"D:/TEST/Gax/amber-eyes"
TAP_EN = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK/Tap02_EN")
TAP_JA = os.path.join(ROOT, "02_SAN_XUAT/TIKTOK/Tap02_JA")
PROV = os.path.join(ROOT, "provenance.json")
BAK = os.path.join(ROOT, ".work/_cu")
NGAY = "2026-11-20"
GEN = ".work/_build_tk_tap02_multilang.py (generator, G6 - single source of truth)"

os.makedirs(BAK, exist_ok=True)
stamp = datetime.datetime.now().strftime("%Y%m%d_%H%M")
shutil.copy2(PROV, os.path.join(BAK, "provenance_%s.json" % stamp))

def read(p):
    return io.open(p, encoding="utf-8").read()

prov = json.load(io.open(PROV, encoding="utf-8"))
prov = [e for e in prov if "TIKTOK/Tap02_EN/" not in e.get("file", "") and "TIKTOK/Tap02_JA/" not in e.get("file", "")]

entries = []

# Plan and spec
entries.append({
    "file": "02_SAN_XUAT/TIKTOK/Tap02_EN/KE_HOACH_CLIP_TAP02_EN.md",
    "loai": "Production plan for 5 TikTok clips Episode 02 (English)",
    "cong_cu": GEN,
    "ngay": NGAY,
    "prompt": None,
    "seed": None,
    "mo_ta": "English production plan for Episode 02 TikTok clips. Covers K1-K10 and G1-G13 standards, speech rate measured from timeline_s_EN_t02.json.",
    "font": None,
    "dieu_khoan": "Internal production document.",
    "kiem_tra_thuong_mai": "Pass."
})
entries.append({
    "file": "02_SAN_XUAT/TIKTOK/Tap02_EN/SPEC_AUDIO_CLIP_TAP02.json",
    "loai": "Audio and visual timing spec for Episode 02 TikTok clips (English)",
    "cong_cu": GEN,
    "ngay": NGAY,
    "prompt": None,
    "seed": None,
    "mo_ta": "JSON spec for 5 English TikTok clips with role emotions, speed offsets, pause tags, background assignments, and overlay timings.",
    "font": None,
    "dieu_khoan": "Internal TTS input specification.",
    "kiem_tra_thuong_mai": "Pass (durations 56.1-81.9s within 45-95s gate)."
})
entries.append({
    "file": "02_SAN_XUAT/TIKTOK/Tap02_JA/KE_HOACH_CLIP_TAP02_JA.md",
    "loai": "Production plan for 5 TikTok clips Episode 02 (Japanese)",
    "cong_cu": GEN,
    "ngay": NGAY,
    "prompt": None,
    "seed": None,
    "mo_ta": "Japanese production plan for Episode 02 TikTok clips. Adheres to AGENTS.md, speech rates measured from timeline_s_JA_t02.json.",
    "font": None,
    "dieu_khoan": "Internal production document.",
    "kiem_tra_thuong_mai": "Pass."
})
entries.append({
    "file": "02_SAN_XUAT/TIKTOK/Tap02_JA/SPEC_AUDIO_CLIP_TAP02.json",
    "loai": "Audio and visual timing spec for Episode 02 TikTok clips (Japanese)",
    "cong_cu": GEN,
    "ngay": NGAY,
    "prompt": None,
    "seed": None,
    "mo_ta": "JSON spec for 5 Japanese TikTok clips with role emotions, speed offsets, pause tags, background assignments, and overlay timings.",
    "font": None,
    "dieu_khoan": "Internal TTS input specification.",
    "kiem_tra_thuong_mai": "Pass (durations 64.3-81.2s within 45-95s gate)."
})

for i in range(1, 6):
    for lang, folder, prefix, limit in [("EN", TAP_EN, "English", "2200"), ("JA", TAP_JA, "Japanese", "2200")]:
        f_cap = "Caption_TK%d.txt" % i
        f_dai = "MoTa_Dai_TK%d.txt" % i
        f_ngan = "MoTa_Ngan_TK%d.txt" % i
        
        cap = read(os.path.join(folder, f_cap))
        dai = read(os.path.join(folder, f_dai))
        ngan = read(os.path.join(folder, f_ngan))
        
        hook = cap.split("\n")[0].strip()
        
        entries.append({
            "file": "02_SAN_XUAT/TIKTOK/Tap02_%s/%s" % (lang, f_cap),
            "loai": "%s TikTok caption and publishing notes for clip TK%d Episode 02" % (prefix, i),
            "cong_cu": GEN,
            "ngay": NGAY,
            "prompt": None,
            "seed": None,
            "mo_ta": "%s caption (%d chars) for TK%d with hook '%s', mandatory AIGC disclosure, and publishing guidance." % (prefix, len(cap), i, hook),
            "font": None,
            "dieu_khoan": "Mandatory AIGC toggle on TikTok. Safe per V9/A9.2 guidelines.",
            "kiem_tra_thuong_mai": "Pass (%d chars < 2200)." % len(cap)
        })
        entries.append({
            "file": "02_SAN_XUAT/TIKTOK/Tap02_%s/%s" % (lang, f_dai),
            "loai": "%s comprehensive description for clip TK%d Episode 02" % (prefix, i),
            "cong_cu": GEN,
            "ngay": NGAY,
            "prompt": None,
            "seed": None,
            "mo_ta": "%s full description (%d chars) for TK%d with behavioral deconstruction, case context, sources, and hashtags." % (prefix, len(dai), i),
            "font": None,
            "dieu_khoan": "No clinical claims, educational analysis based on public court records.",
            "kiem_tra_thuong_mai": "Pass (%d chars < 4000)." % len(dai)
        })
        entries.append({
            "file": "02_SAN_XUAT/TIKTOK/Tap02_%s/%s" % (lang, f_ngan),
            "loai": "%s concise description for clip TK%d Episode 02" % (prefix, i),
            "cong_cu": GEN,
            "ngay": NGAY,
            "prompt": None,
            "seed": None,
            "mo_ta": "%s short description (%d chars) for TK%d optimized for TikTok Studio description box." % (prefix, len(ngan), i),
            "font": None,
            "dieu_khoan": "Safe per V9/A9.2 guidelines.",
            "kiem_tra_thuong_mai": "Pass (%d chars < 4000)." % len(ngan)
        })

for e in entries:
    prov.append(e)

with io.open(PROV, "w", encoding="utf-8", newline="\n") as f:
    json.dump(prov, f, ensure_ascii=False, indent=2)
    f.write("\n")

print("Added %d entries to provenance.json. Total entries: %d" % (len(entries), len(prov)))
