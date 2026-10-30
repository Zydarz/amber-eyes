import json
import re
import sys
from pathlib import Path

try:
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    sys.stderr.reconfigure(encoding="utf-8", errors="replace")
except Exception:
    pass

ROOT = Path(__file__).resolve().parents[1]
shots = json.loads((ROOT / ".work" / "shots_t04.json").read_text(encoding="utf-8"))["shots"]
tl = json.loads((ROOT / ".work" / "timeline_s_t04.json").read_text(encoding="utf-8"))
script = json.loads((ROOT / ".work" / "script_tap04.json").read_text(encoding="utf-8"))

items = {it["id"]: it for it in tl["items"]}
sents_dict = {}
for e in script:
    if e["kind"] == "LOI":
        for s in e["sentences"]:
            sents_dict[s["id"]] = s["text"]

print("=" * 100)
print(f"{'SHOT':<6} | {'TIME (s)':<17} | {'DUR':<5} | {'NỀN (BG)':<24} | {'CHỮ TRÊN HÌNH (SEGMENTS)':<35} | {'NỘI DUNG LỜI THOẠI':<40}")
print("=" * 100)

long_shots = []
suspicious_bgs = []

for s in shots:
    sid = s["id"]
    st = s["start"]
    et = s["end"]
    dur = et - st
    bg = s.get("bg", "")
    s_sents = s.get("sentences", [])
    segs = s.get("segments", [])
    
    seg_txts = []
    for sg in segs:
        for k, v in sg.get("elems", []):
            seg_txts.append(v)
    seg_str = " / ".join(seg_txts)
    if len(seg_str) > 35:
        seg_str = seg_str[:32] + "..."
        
    if s_sents:
        sent_txt = " ".join(sents_dict.get(k, "") for k in s_sents)
        sent_brief = sent_txt[:40] + "..." if len(sent_txt) > 40 else sent_txt
        time_str = f"{st:6.1f} -> {et:6.1f}"
    else:
        sent_brief = f"[KHÔNG LỜI: {s.get('beat_text', '')[:30]}]"
        time_str = f"{st:6.1f} -> {et:6.1f}"

    if dur > 20.0 and s_sents:
        long_shots.append((sid, dur, bg, s_sents, seg_str))

    print(f"{sid:<6} | {time_str:<17} | {dur:4.1f}s | {bg:<24} | {seg_str:<35} | {sent_brief}")

print("\n" + "=" * 100)
print("DANH SÁCH CÁC SHOT CÓ THỜI LƯỢNG DÀI (> 20s) CẦN XEM XÉT CHẺ SHOT HOẶC KIỂM TRA ĐỔI NỀN:")
for sid, dur, bg, s_sents, segs in long_shots:
    print(f"  • Shot {sid}: {dur:.1f}s | Nền: {bg} | Câu: {s_sents}")
    for sid_c in s_sents:
        print(f"      - {sid_c} ({items[sid_c]['start']:.1f} -> {items[sid_c]['end']:.1f}s): \"{sents_dict.get(sid_c, '')}\"")
