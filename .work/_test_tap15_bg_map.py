#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tap 15 — Generate KeHoach_Video_Tap15.md across 3 languages (VN, EN, JA).
Conforms to Amber Eyes Production Plan Standards (A2c, V1-V9, H6, H10, H17, T2, T4, T8, T10).
"""
import json
import re
from pathlib import Path

ROOT = Path("D:/TEST/Gax/amber-eyes")
WORK = ROOT / ".work"

sc_vi = json.load(open(WORK / "script_tap15.json", encoding="utf-8"))
sc_en = json.load(open(WORK / "script_tap15_EN.json", encoding="utf-8"))
sc_ja = json.load(open(WORK / "script_tap15_JA.json", encoding="utf-8"))

tl_vi = json.load(open(WORK / "timeline_s_t15.json", encoding="utf-8"))
tl_en = json.load(open(WORK / "timeline_s_EN_t15.json", encoding="utf-8"))
tl_ja = json.load(open(WORK / "timeline_s_JA_t15.json", encoding="utf-8"))

bg_jobs = json.load(open(WORK / "bg_jobs_tap15.json", encoding="utf-8"))

# Group bg_jobs by Act
bgs_by_act = {}
for j in bg_jobs:
    act = j["act"]
    bgs_by_act.setdefault(act, []).append(j["name"])

# Specific key backgrounds for specific elements/sents
SPECIFIC_BG = {
    # Act 1
    "1.07#3": "t15_cancun_plane_tickets_unopened_mail",
    "1.07#4": "t15_cancun_plane_tickets_unopened_mail",
    "1.07#5": "t15_slashed_car_tires_curbside",
    "1.07#6": "t15_slashed_car_tires_curbside",
    "1.07#7": "t15_slashed_car_tires_curbside",
    "1.08#1": "t15_bystander_guilt_whispers_livingroom",
    "1.08#2": "t15_bystander_guilt_whispers_livingroom",
    "1.14#4": "t15_washing_machine_running_dark_utility",
    "1.14#5": "t15_washing_machine_running_dark_utility",
    "1.14#6": "t15_washing_machine_running_dark_utility",
    "1.17#1": "t15_washing_machine_running_dark_utility",
    "1.17#2": "t15_jodi_arias_a1_11_camera",
    "1.17#3": "t15_jodi_arias_a1_11_camera",
    "1.17#4": "t15_jodi_arias_a1_12_gascan",
    "1.17#5": "t15_jodi_arias_a1_12_gascan",
    "1.17#6": "t15_jodi_arias_a1_12_gascan",
    "1.18#1": "t15_jodi_arias_a1_11_camera",
    "1.18#2": "t15_jodi_arias_a1_11_camera",
    "1.18#3": "t15_jodi_arias_a1_09_arizona",
    # Act 2
    "2.05#4": "t15_darryl_brewer_garage_gas_cans",
    "2.05#5": "t15_darryl_brewer_garage_gas_cans",
    "2.07#3": "t15_interstate_highway_gas_stop_midnight",
    "2.07#4": "t15_interstate_highway_gas_stop_midnight",
    "2.08#7": "t15_salt_lake_city_suburban_doorstep",
    "2.08#8": "t15_salt_lake_city_suburban_doorstep",
    "2.08#9": "t15_investigative_timeline_wall_map",
    "2.08#10": "t15_darryl_brewer_garage_gas_cans",
    "2.08#11": "t15_salt_lake_city_suburban_doorstep",
    # Act 3
    "3.05#4": "t15_borderline_splitting_black_white_bust",
    "3.05#5": "t15_borderline_splitting_black_white_bust",
    "3.08#4": "t15_theory_of_mind_deficit_chess",
    "3.08#5": "t15_theory_of_mind_deficit_chess",
    "3.08#6": "t15_theory_of_mind_deficit_chess",
    "3.08#7": "t15_cognitive_dissonance_scriptures_bedside",
    "3.08#8": "t15_trauma_bonding_push_pull_tangle",
    "3.08#9": "t15_trauma_bonding_push_pull_tangle",
    # Act 4
    "4.02#3": "t15_jodi_arias_a4_01_desert",
    "4.02#4": "t15_jodi_arias_a4_02_camera",
    "4.06#1": "t15_jodi_arias_a4_08_mirror",
    "4.06#2": "t15_jodi_arias_a4_08_mirror",
    "4.06#3": "t15_jodi_arias_a4_09_interrogation",
    "4.08#5": "t15_prosecutor_timeline_whiteboard_clash",
    "4.08#6": "t15_prosecutor_timeline_whiteboard_clash",
    "4.09#1": "t15_media_circus_cameras_satellite_trucks",
    "4.09#2": "t15_media_circus_cameras_satellite_trucks",
    "4.10#5": "t15_pathological_self_pity_tissue",
    "4.10#6": "t15_pathological_self_pity_tissue",
    "4.12#2": "t15_two_guilt_polarities_scales",
    "4.12#3": "t15_two_guilt_polarities_scales",
    # Act 5
    "5.04#7": "t15_travis_foundation_scholarship_plaque",
    "5.04#8": "t15_travis_foundation_scholarship_plaque",
    "5.05#1": "t15_four_redflags_overview_banner",
    "5.06#1": "t15_redflag1_unstable_intense_relationships",
    "5.07#1": "t15_redflag2_frantic_efforts_avoid_abandonment",
    "5.08#1": "t15_redflag3_identity_disturbance_mirror",
    "5.09#1": "t15_redflag4_inappropriate_intense_anger",
    "5.10#1": "t15_personal_boundary_stone_wall_garden",
    "5.10#2": "t15_personal_boundary_stone_wall_garden",
    "5.10#5": "t15_quiet_sanctuary_porch_morning_light",
    "5.10#6": "t15_quiet_sanctuary_porch_morning_light",
    "5.12#1": "t15_desert_monument_dawn_freedom",
    "5.12#2": "t15_truth_shines_desert_highway_horizon",
    "5.12#3": "t15_truth_shines_desert_highway_horizon",
    "5.12#4": "t15_truth_shines_desert_highway_horizon",
}

# Build full sid -> bg mapping
sids_all = [s["id"] for e in sc_vi if "sentences" in e for s in e["sentences"]]
sent_to_bg = {}

# Distribute backgrounds per act
for act in range(1, 6):
    act_sents = [s["id"] for e in sc_vi if e.get("act") == act and "sentences" in e for s in e["sentences"]]
    act_bgs = bgs_by_act[act]
    bg_idx = 0
    consec_count = 0
    last_bg = None
    
    for sid in act_sents:
        if sid in SPECIFIC_BG:
            bg = SPECIFIC_BG[sid]
        else:
            # Pick from pool, avoiding >3 repeats
            bg = act_bgs[bg_idx % len(act_bgs)]
            if bg == last_bg and consec_count >= 3:
                bg_idx += 1
                bg = act_bgs[bg_idx % len(act_bgs)]
                consec_count = 1
            elif bg == last_bg:
                consec_count += 1
            else:
                consec_count = 1
            last_bg = bg
            bg_idx += 1
        sent_to_bg[sid] = bg

# Verify Rule H10 (no bg repeats > 4 consecutive shots)
max_consec = 0
cur_consec = 0
prev_b = None
for sid in sids_all:
    b = sent_to_bg[sid]
    if b == prev_b:
        cur_consec += 1
    else:
        cur_consec = 1
        prev_b = b
    if cur_consec > max_consec:
        max_consec = cur_consec
print(f"Max consecutive background repeats: {max_consec} (Rule H10 <= 4: {'PASS' if max_consec <= 4 else 'FAIL'})")

json.dump(sent_to_bg, open(WORK / "_tap15_sent_to_bg.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("Saved sentence-to-background mapping!")
