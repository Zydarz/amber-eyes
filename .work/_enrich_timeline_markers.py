# -*- coding: utf-8 -*-
"""Enrich markers in timeline_s_EN_t06.json."""
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

tl_path = ".work/timeline_s_EN_t06.json"
tl = json.load(open(tl_path, encoding="utf-8"))
items = {it["id"]: it for it in tl["items"]}

# Build comprehensive markers
markers = [
    {"type": "INTRO", "start": 0.0, "end": round(items["1.02#1"]["start"] - 0.20, 2)},
    {"type": "BGM", "id": "1.01", "at": round(items["1.02#1"]["start"] - 0.20, 2), "desc": "A somber, slow opening piano melody"},
    {"type": "SFX", "id": "1.03", "at": round(items["1.02#1"]["end"], 2), "desc": "Camera flashes and applause"},
    {"type": "NGHI", "id": "1.05", "start": round(items["1.04#2"]["end"], 2), "end": round(items["1.06#1"]["start"] - 0.20, 2), "desc": "cello melody swells"},
    {"type": "SFX", "id": "1.07", "at": round(items["1.06#6"]["end"], 2), "desc": "Car door shuts"},
    {"type": "SFX", "id": "1.10", "at": round(items["1.09#6"]["end"], 2), "desc": "Police phone rings"},
    {"type": "BGM", "id": "1.17", "at": round(items["1.16#2"]["end"], 2), "desc": "Music swells and cuts with metallic clink"},
    {"type": "ACT", "act": 2, "start": round(items["1.16#2"]["end"], 2), "end": round(items["2.02#1"]["start"] - 0.20, 2)},
    {"type": "BGM", "id": "2.01", "at": round(items["2.02#1"]["start"] - 0.20, 2), "desc": "Dark ambient pulses with tense bass"},
    {"type": "SFX", "id": "2.05", "at": round(items["2.04#2"]["end"], 2), "desc": "Rustle of case folders and footsteps"},
    {"type": "NGHI", "id": "2.12", "start": round(items["2.11#6"]["end"], 2), "end": round(items["3.02#1"]["start"] - 0.20, 2), "desc": "distant police sirens echo"},
    {"type": "ACT", "act": 3, "start": round(items["2.11#6"]["end"], 2), "end": round(items["3.02#1"]["start"] - 0.20, 2)},
    {"type": "BGM", "id": "3.01", "at": round(items["3.02#1"]["start"] - 0.20, 2), "desc": "Sub-bass drone"},
    {"type": "SFX", "id": "3.04", "at": round(items["3.03#3"]["end"], 2), "desc": "Crawlspace access hatch creaks open"},
    {"type": "SFX", "id": "3.08", "at": round(items["3.07#3"]["end"], 2), "desc": "Shovel cuts deep into wet earth"},
    {"type": "BGM", "id": "3.14", "at": round(items["3.13#3"]["end"], 2), "desc": "Low cello note lingers"},
    {"type": "ACT", "act": 4, "start": round(items["3.13#3"]["end"], 2), "end": round(items["4.02#1"]["start"] - 0.20, 2)},
    {"type": "BGM", "id": "4.01", "at": round(items["4.02#1"]["start"] - 0.20, 2), "desc": "Violin melody"},
    {"type": "SFX", "id": "4.11", "at": round(items["4.10#2"]["end"], 2), "desc": "Judge's gavel strikes"},
    {"type": "ACT", "act": 5, "start": round(items["4.10#2"]["end"], 2), "end": round(items["5.02#1"]["start"] - 0.20, 2)},
    {"type": "BGM", "id": "5.01", "at": round(items["5.02#1"]["start"] - 0.20, 2), "desc": "Introspective piano"},
    {"type": "NGHI", "id": "5.05", "start": round(items["5.04#4"]["end"], 2), "end": round(items["5.06#1"]["start"] - 0.20, 2), "desc": "quiet heavy sigh"},
    {"type": "BGM", "id": "5.07", "at": round(items["5.06#19"]["end"], 2), "desc": "Music score swells and fades out"}
]

tl["markers"] = markers
with open(tl_path, "w", encoding="utf-8") as f:
    json.dump(tl, f, ensure_ascii=False, indent=2)

print(f"Updated {tl_path} with {len(markers)} markers!")
