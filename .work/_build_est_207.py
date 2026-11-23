#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate initial estimated timeline (207 sentences) for VI, EN, JA.
Used as 'est' for _t09_align4.py and _t09_timeline_from_asr.py.
"""
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
W = ROOT / ".work"
FF = W / "ffmpeg" / "ffmpeg-n9.0-latest-win64-lgpl-shared-9.0" / "bin" / "ffprobe.exe"

FILES = {
    "vi": {
        "script": W / "script_tap09.json",
        "mp3": ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap09" / "xuat_ban" / "Tap09_master.mp3",
        "out": W / "_t09" / "_t09_est_vi.json",
    },
    "en": {
        "script": W / "script_tap09_EN.json",
        "mp3": ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap09_EN" / "xuat_ban" / "Tap09_EN_master.mp3",
        "out": W / "_t09" / "_t09_est_en.json",
    },
    "ja": {
        "script": W / "script_tap09_JA.json",
        "mp3": ROOT / "02_SAN_XUAT" / "Ho_So_Toi_Pham" / "Tap09_JA" / "xuat_ban" / "Tap09_JA_master.mp3",
        "out": W / "_t09" / "_t09_est_ja.json",
    },
}

def get_dur(p):
    r = subprocess.run([str(FF), "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True, check=True)
    return float(r.stdout.strip())

for lang, cfg in FILES.items():
    total = round(get_dur(cfg["mp3"]), 2)
    script = json.loads(cfg["script"].read_text(encoding="utf-8"))
    
    # Collect sentences
    all_sentences = []
    total_chars = 0
    for el in script:
        if el["kind"] == "LOI":
            role = el.get("role") or "H"
            if el["id"] == "1.07":
                role = "N1"
            elif el["id"] == "4.05":
                role = "N2"
            act = int(el["id"].split(".")[0])
            for i, s in enumerate(el.get("sentences", []), 1):
                sid = f"{el['id']}#{i}"
                txt = s["text"].strip()
                all_sentences.append({
                    "id": sid,
                    "element": el["id"],
                    "act": act,
                    "role": role,
                    "text": txt,
                    "chars": len(txt)
                })
                total_chars += len(txt)
                
    print(f"[{lang}] {len(all_sentences)} sentences, {total_chars} chars, total={total}s")
    assert len(all_sentences) == 207, f"Expected 207 sentences, got {len(all_sentences)}"
    
    # Proportional time distribution between 23.0s and total - 7.0s
    t_start = 23.0
    t_end = total - 7.0
    avail_time = t_end - t_start
    
    # Baseline pause after sentence
    pause_per_sentence = 0.45
    total_pause = len(all_sentences) * pause_per_sentence
    speech_time = max(avail_time - total_pause, avail_time * 0.7)
    
    curr_t = t_start
    items = []
    for s in all_sentences:
        dur = max(1.2, (s["chars"] / total_chars) * speech_time)
        s_start = round(curr_t, 2)
        s_end = round(curr_t + dur, 2)
        items.append({
            "id": s["id"],
            "element": s["element"],
            "act": s["act"],
            "role": s["role"],
            "start": s_start,
            "end": s_end,
            "text": s["text"]
        })
        curr_t = s_end + pause_per_sentence
        
    # Scale exactly to t_end
    actual_span = items[-1]["end"] - items[0]["start"]
    target_span = t_end - t_start
    scale = target_span / actual_span
    for it in items:
        s_rel = (it["start"] - t_start) * scale
        e_rel = (it["end"] - t_start) * scale
        it["start"] = round(t_start + s_rel, 2)
        it["end"] = round(t_start + e_rel, 2)
        if it["end"] <= it["start"]:
            it["end"] = it["start"] + 0.4
            
    # Markers
    markers = [{"type": "INTRO", "start": 0.0, "end": 22.41}]
    # Add BGM, SFX, NGHI, ACT from script
    for el in script:
        if el["kind"] == "BGM":
            # find closest sentence start
            act = int(el["id"].split(".")[0])
            first_s = next((it for it in items if it["element"] == el["id"]), None)
            if first_s is None:
                # find first sentence in this act or adjacent
                first_s = next((it for it in items if it["act"] == act), None)
            at_t = first_s["start"] if first_s else 23.0
            markers.append({"type": "BGM", "id": el["id"], "at": at_t, "desc": el.get("desc", "")})
        elif el["kind"] == "SFX":
            markers.append({"type": "SFX", "id": el["id"], "at": 0.0, "desc": el.get("desc", "")})
        elif el["kind"] == "NGHI":
            markers.append({"type": "NGHI", "id": el["id"], "start": 0.0, "end": 0.0, "desc": el.get("desc", "")})
            
    # Acts boundaries
    acts = {}
    for a in range(1, 6):
        a_items = [it for it in items if it["act"] == a]
        if a_items:
            acts[str(a)] = [a_items[0]["start"], a_items[-1]["end"]]
            if a > 1:
                markers.append({"type": "ACT", "act": a, "start": a_items[0]["start"] - 2.0, "end": a_items[0]["start"]})
                
    out_data = {
        "total": total,
        "intro": 22.41,
        "items": items,
        "markers": markers,
        "acts": acts
    }
    cfg["out"].parent.mkdir(parents=True, exist_ok=True)
    cfg["out"].write_text(json.dumps(out_data, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"[{lang}] Wrote {cfg['out'].name} successfully!")
