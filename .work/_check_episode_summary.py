# -*- coding: utf-8 -*-
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, ".work")
import parse_kichban
import edition

s = parse_kichban.parse_file("01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md")
all_sentence_ids = set()
for el in s:
    if "sentences" in el:
        for i in range(len(el["sentences"])):
            all_sentence_ids.add(f"{el['id']}#{i+1}")

print(f"Tổng số câu đọc trong kịch bản mới: {len(all_sentence_ids)}")

ep01 = edition.EPISODES["01"]
print("\n--- Kiểm tra summary ---")
print(f"Summary hiện tại: {ep01.get('summary')}")
for sid in ep01.get("summary", ()):
    print(f"  {sid} tồn tại: {sid in all_sentence_ids}")

print("\n--- Kiểm tra need ---")
print(f"Need hiện tại: {ep01.get('need')}")
for sid in ep01.get("need", []):
    print(f"  {sid} tồn tại: {sid in all_sentence_ids}")

print("\n--- Kiểm tra n_element ---")
print(f"n_element: {ep01.get('n_element')}")
el_ids = {el["id"] for el in s}
for eid in ep01.get("n_element", {}):
    print(f"  {eid} tồn tại trong element: {eid in el_ids}")

print("\n--- Kiểm tra act1_cue, silence_cue, click_cues ---")
for k in ["act1_cue", "silence_cue"]:
    v = ep01.get(k)
    print(f"  {k} ({v}) tồn tại: {v in el_ids}")

for cid in ep01.get("click_cues", ()):
    print(f"  click_cue ({cid}) tồn tại: {cid in el_ids}")
