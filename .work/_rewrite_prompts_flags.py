#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Viết lại PROMPT cho 45 ảnh lỗi QC (AI vẽ chữ / lệch nghĩa) của Tập 37/38/39.

Nguyên tắc: không thêm câu cấm chữ (FLUX vẫn vẽ), mà BỎ HẲN cơ hội để vẽ chữ —
  · cửa hệ/đèn neon   -> plain blank facade, closed shutters, no signboard
  · chữ Hán tự        -> paper lanterns / cloth awnings, plain unmarked walls
  · biển số xe        -> blank unnumbered plate
  · giấy tờ / bảng    -> completely blank unmarked surface
  · thẻ khoản tiền    -> plain notes with no printing

Có backup .work/_cu/bg_jobs_tapXX_<timestamp>.json trước khi sửa.
"""
import json
import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
BK = WORK / "_cu"
BK.mkdir(parents=True, exist_ok=True)
STAMP = time.strftime("%Y%m%d_%H%M")

NEW_PROMPTS = {
    # ---------------- TẬP 37 ----------------
    "t37_a1_19_psychologist_silhouette_frosted_glass_desk":
        "A psychologist's silhouette standing behind a frosted glass desk in a dim consulting room, a closed hardcover book and an open notebook whose pages are completely blank, a desk lamp glow, an empty chair on the other side, bare walls, no documents, no writing, no text.",
    "t37_a2_05_ho_nai_beer_eatery_plastic_stools_night":
        "A late-night roadside beer eatery seen from a dark alley corner: low plastic stools and a bare table under one bulb, closed corrugated shutters and plain dark walls behind, no signboard, no neon lettering, no menu, no text.",
    "t37_a2_07_head_down_on_table_overturned_chair":
        "A young man slumped forward with his head down on a dim table in a quiet room, an overturned chair beside him, a plain ashtray and an empty glass, bare stained walls, no papers, no labels, no text.",
    "t37_a2_22_backpack_flashlight_gloves_on_bed":
        "A backpack, a flashlight and folded gloves laid on a plain metal bed in a bare rented room, a bare wall and a closed shutter behind, a plain cloth bag with no print, no poster, no label, no text.",
    "t37_a2_25_motorbike_parked_far_silhouette_enters_alley":
        "A motorbike parked far down a narrow alley at night and a lone silhouette entering the alley from the foreground seen from behind, wet concrete, bare walls, the rear plate a completely blank unreadable rectangle, no characters, no numbers, no text.",
    "t37_a3_25_ambulance_misty_lane_rear_open_lights":
        "An ambulance with its rear doors open and lights on, parked in a misty village lane at dawn, a plain unmarked white body, no lettering, no symbols, no cross, no numbers, no text, villagers watching from a distance.",
    "t37_a4_09_trembling_hands_pen_blank_form":
        "Trembling hands holding a pen over a completely blank sheet of paper on a dark desk, a simple wooden chair, bare walls, the paper surface empty with no printed lines, no writing, no text.",
    "t37_a4_14_blank_forms_pen_barred_window_desk":
        "A bare desk by a barred window with a pen and a stack of completely blank unmarked sheets, a plain chair, cold daylight, no documents printed, no text, no numbers.",
    "t37_a4_19_courthouse_exterior_morning_crowd_steps":
        "A plain neoclassical courthouse exterior seen from the base of its steps in the morning, a blank unadorned stone facade, wide steps with a small crowd of dark silhouettes, bare trees, no pediment inscription, no plaque, no characters, no lettering, no text.",
    "t37_a5_05_crowd_outside_courthouse_dusk_relief":
        "A crowd of dark silhouettes standing outside a plain courthouse at dusk, a blank unadorned facade and a blank arched doorway with no name board, no lettering, no characters, no text.",

    # ---------------- TẬP 38 ----------------
    "t38_a1_02_roadside_diner_night_empty_stools":
        "A roadside diner at night seen from the empty counter side: empty stools, a bare counter, warm window light, plain dark walls and a window with no lettering, no sign, no menu, no text.",
    "t38_a1_05_sheriff_office_bulletin_board_blank":
        "A sheriff's office interior with a bare desk, a lamp and a wall of empty plain notice frames whose surfaces are completely blank and unmarked, a detective silhouette studying them, no papers printed, no text, no numbers.",
    "t38_a1_08_driver_silhouette_car_shoulder_headlights":
        "A lone driver silhouette standing beside a car on a highway shoulder at night with headlights on, seen from behind, the rear license plate a plain blank rectangle with no characters, no numbers, no text.",
    "t38_a1_10_electronics_repair_shop_clearwater_bench":
        "An electronics repair bench seen from inside a dark workshop: a workbench with a soldering iron, tangled cables, a radio chassis with its back open, plain bare walls and a blank doorway behind, no storefront sign, no lettering, no text.",
    "t38_a1_13_detectives_map_table_pins_dim_office":
        "Two detective silhouettes over a dim table with a completely blank folded map carrying no labels, push pins scattered, a bare lamp, blank walls, no portrait, no writing, no text.",
    "t38_a2_10_balcony_two_silhouettes_facing_apart":
        "Two woman silhouettes standing apart on a balcony at dusk, a plain railing and blank wall behind, an open door spilling warm light, no sign, no lettering, no characters, no text.",
    "t38_a2_22_task_force_case_map_wall_silhouettes":
        "A dim task force room with a bare table and several plain empty document frames on the wall whose surfaces are completely blank and unmarked, silhouettes standing in shadow, no writing, no text, no numbers.",
    "t38_a2_33_door_closing_silhouette_leaving_dusk":
        "A silhouette stepping out of a closing door at dusk beside a plain roadside building with a blank wall and no signboard, wet asphalt, bare power poles, no lettering, no characters, no text.",
    "t38_a2_36_two_silhouettes_embrace_doorway_dusk":
        "Two silhouettes embracing in a lit doorway at dusk in a plain building wall with no signboard and no lettering, warm interior light, wet road, no characters, no text.",
    "t38_a3_08_detective_before_board_blank_witness_notes":
        "A detective silhouette standing before a wall of completely blank unmarked notice frames, a bare wooden floor, a single lamp, the frames empty with no writing at all, no text, no numbers.",
    "t38_a3_10_empty_chair_desk_lamp_over_map":
        "An empty wooden chair at a desk lit by a single lamp, a completely blank folded map with no labels or markings on the table, bare walls, no writing, no text.",
    "t38_a3_13_pawn_shops_row_windows_night_unmarked":
        "A row of plain closed shopfronts at night seen from across an empty street, dark unadorned windows and plain shutters, no signboards, no lettering, no characters, no text, one dim streetlamp.",
    "t38_a3_14_pawn_counter_glass_case_camera_fishing_rod":
        "Inside a dim shop, a plain glass counter with a camera, a fishing rod and small unlabelled items, blank bare walls behind, no signboard, no lettering, no price tags, no text.",
    "t38_a3_15_blank_receipt_pad_pen_on_counter":
        "A plain shop counter with a completely blank receipt pad, a pen and a bare scale, blank walls, no signboard, no lettering, the paper totally empty with no writing, no text, no numbers.",
    "t38_a3_21_silhouette_at_curtain_anxious_motel_window":
        "A lone silhouette standing at a curtained window at night in a plain corridor, plain wall and curtain, an empty parking lot visible outside, no sign, no lettering, no characters, no text.",
    "t38_a3_31_roadside_biker_bar_exterior_motorcycles":
        "Motorcycles parked outside a closed roadside bar at dusk, a plain unmarked facade and a blank doorway, no signboard, no lettering, no characters, no text.",
    "t38_a3_33_two_officers_silhouettes_doorway_calm":
        "Two plain-clothes officer silhouettes standing in a quiet doorway of a bare building, blank walls and steps, no signboard, no lettering, no characters, no text.",

    # ---------------- TẬP 39 ----------------
    "t39_a1_12_child_desks_chalk_dust_light":
        "Empty wooden school desks in a classroom with chalk dust floating in a shaft of light, plain blank chalkboard with no writing, plain walls, no notebooks, no papers, no text.",
    "t39_a1_19_imported_motorcycle_night_street":
        "A large imported motorcycle parked under a street lamp on a wet night street in a 1990s Chinese city, plain blank shuttered walls and closed dark shopfronts with no boards, two faint silhouettes in the distance, no lettering, no characters, no text.",
    "t39_a1_20_lavish_spending_night_market":
        "A busy 1990s night market with plain round paper lanterns that carry no writing, stalls covered by unmarked plain cloth, a silhouette of a man handing over money, crowd as dark shapes, no signboards, no characters, no text.",
    "t39_a1_22_family_table_empty_chair":
        "A wooden family table in a plain home with one empty chair pushed back and no one seated, cold daylight through a bare window, plain walls, a single bowl on the table, no family, no people, no text.",
    "t39_a1_26_greed_dim_stairwell_corners":
        "A narrow dim stairwell of an old building with peeling plaster, a single weak bulb, deep corners and a blank wall, no signboard, no plaque, no characters, no text.",
    "t39_a2_02_nightclub_entrance_hostess_silhouette":
        "A 1990s Chinese nightclub entrance: a plain doorway with colored light spilling onto wet pavement, round paper lanterns without writing, a slender woman silhouette at the door with her face in shadow, plain unmarked walls, no signboard, no characters, no lettering, no text.",
    "t39_a2_08_wenzhou_alley_autumn_1997":
        "A narrow alley in Wenzhou in autumn 1997, wet cobbles, closed shutters and plain blank walls, a dim rental house window with plain curtains, no shopfront boards, no characters, no lettering, no text.",
    "t39_a2_12_hefei_dance_hall_july_1999":
        "A large dance hall exterior at night in July 1999 seen from the side of the street: a plain blank facade with tall glowing windows, parked cars, crowd as faint shadows, no signboard, no characters, no lettering, no text.",
    "t39_a2_14_market_lane_carpenter_toolbox":
        "An early-morning market lane with a carpenter's wooden toolbox and handsaw on a cart, plain cloth awnings, empty wet lane, steam from a distant stall, no signboards, no characters, no lettering, no text.",
    "t39_a2_20_police_at_rental_house_door":
        "Plain-clothed police silhouettes in front of a worn rental house door, a plain unmarked door with no number plate and no characters, flashlight beams into the dark hall, grey dusk, no lettering, no text.",
    "t39_a2_23_two_toolkits_dark_table":
        "Two open toolkits with practical metal tools on a dark table, split lighting with one hard lamp and one soft window light, plain bare walls, no mask, no prop, no text.",
    "t39_a3_04_workplaces_cosmetics_eatery_bar":
        "A small cosmetics counter, a cramped eatery and a dim bar in a southern Chinese city seen in one composition, workers as silhouettes, plain blank walls and plain unmarked containers, no signboards, no characters, no lettering, no text.",
    "t39_a3_13_cloud_sword_police_command_room":
        "A dark police command room with rows of dark monitors showing only a blank faint glow, officer silhouettes at consoles, blank plain walls, no interface, no glyphs, no characters, no text.",
    "t39_a4_01_nanchang_courthouse_exterior_dec_2020":
        "Exterior of a Chinese intermediate court building in Nanchang in December 2020, grey winter sky, crowd silhouettes at the steps, a plain blank stone facade, no name board, no characters, no lettering, no text.",
    "t39_a4_03_courtroom_witness_stand_empty":
        "An empty witness stand in the middle of a Chinese courtroom, cold light from tall windows, rows of empty benches, plain blank walls, no emblem, no plaque, no characters, no text.",
    "t39_a4_15_lone_woman_crowded_station_escape_chance":
        "A crowded bus station concourse with a lone woman silhouette standing among blurred moving commuters, plain blank pillars and a blank glass doorway, nothing legible, no sign, no characters, no text.",
    "t39_a4_16_rental_flat_cash_split_table":
        "A modest rental flat table lit by a bare bulb with two equal stacks of banknotes divided down the middle, empty chairs, plain bare walls, the notes plain with no printing, no writing, no text.",
    "t39_a4_17_hardware_shelf_rope_iron_bars_evening":
        "Inside a hardware store: shelves with coils of rope and metal bars, plain bare walls and blank shelf edges, a silhouette of a shopper leaving through the door, no signboard, no lettering, no text.",
    "t39_a5_03_jiangxi_high_court_winter_exterior":
        "Exterior of a provincial high court building in Jiangxi on a grey winter day, a plain unadorned stone facade, empty steps, bare trees, no name board, no characters, no lettering, no text.",
    "t39_a5_10_nightlife_street_one_figure_turns_away":
        "A busy nightlife street seen as abstract blurred neon color without any lettering, plain glowing shapes, silhouettes of passersby, one figure stopping and turning away, no signboards, no characters, no text.",
}


def main():
    by_ep = {}
    for name in NEW_PROMPTS:
        ep = name[1:3]
        by_ep.setdefault(ep, []).append(name)

    for ep, names in sorted(by_ep.items()):
        path = WORK / f"bg_jobs_tap{ep}.json"
        if not path.exists():
            print(f"Tập {ep}: không có {path}")
            continue
        shutil.copy2(path, BK / f"bg_jobs_tap{ep}_{STAMP}.json")
        jobs = json.loads(path.read_text(encoding="utf-8"))
        changed = 0
        for j in jobs:
            if j["name"] in NEW_PROMPTS:
                j["prompt"] = NEW_PROMPTS[j["name"]]
                changed += 1
        path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Tập {ep}: đã viết lại prompt {changed}/{len(names)} ảnh lỗi (backup: {BK.name}/bg_jobs_tap{ep}_{STAMP}.json)")


if __name__ == "__main__":
    main()
