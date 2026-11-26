#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""ROUND 2 — 37 ảnh vẫn còn chữ sau vòng 1.

Bài học từ vòng 1: chỉ thêm câu cấm chữ KHÔNG đủ. FLUX vẽ chữ Hán tự khi nghe
thấy "shop/market/diner/courthouse/motel/bar" trong prompt. Cách sửa vòng 2:
  · ĐỔI BỐI CẢNH: crop sát vào vật chủ đạo, mặt tiền cửa hệ/địa ốc BỊ CẮT KHỎI KHUNG
  · BỎ các từ kích hoạt biển: shop/diner/courthouse/market/bar → diễn đạt trung tính
  · "background reduced to soft unrecognizable blur", "smooth blank concrete"
  · "no writing of any kind, no lettering, no characters, no numbers, no logos"

Script này: (1) ghi prompt mới vào bg_jobs_tapXX.json (có backup)
            (2) rút danh sách flags còn lại vào _qc_flags_t37_39.json
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

P = {
    # ---------------- TẬP 37 ----------------
    "t37_a2_05_ho_nai_beer_eatery_plastic_stools_night":
        "Tight framing on low plastic stools and a bare table under a single bulb at night in a roadside eatery; the frame is filled by the table and the stools, the background reduced to dark blurred shapes with no readable surface, a closed shutter, no signboard, no lettering, no characters, no numbers, no logos, no writing of any kind.",
    "t37_a2_22_backpack_flashlight_gloves_on_bed":
        "Close crop on a backpack, a flashlight and folded gloves laid on a plain metal bed; the wall behind is smooth bare plaster with nothing on it, no poster, no sign, no sticker, no label, no text, no characters, no numbers.",
    "t37_a3_25_ambulance_misty_lane_rear_open_lights":
        "Rear of a plain white emergency van with its doors open and lights on in a misty village lane at dawn; the vehicle body is completely unadorned with no cross, no symbol, no emblem, no letters, no numbers, no characters, no text; villagers as faint silhouettes far away.",
    "t37_a4_09_trembling_hands_pen_blank_form":
        "Extreme close-up of trembling hands holding a pen above a completely blank unmarked sheet of paper on a dark desk; the paper surface is pure empty white with no printed lines, no signature, no writing, no text, no numbers, no characters; the background is a soft dark blur.",
    "t37_a4_14_blank_forms_pen_barred_window_desk":
        "Tight crop on a desk by a barred window with a pen and a stack of completely blank unmarked sheets; the paper surfaces are pure empty white with no printed lines, no writing, no text, no numbers, no characters; only a plain chair and soft daylight.",
    "t37_a4_19_courthouse_exterior_morning_crowd_steps":
        "Viewed from the very bottom of wide stone steps of a grey institutional building in the morning; only the steps, the lower columns and a crowd of small dark silhouettes are in frame, the upper facade is cropped out entirely, the stone is smooth and unadorned with no plaque, no emblem, no characters, no lettering, no text.",
    "t37_a5_05_crowd_outside_courthouse_dusk_relief":
        "A crowd of dark silhouettes gathered on wide stone steps at dusk, seen from below so that only the steps, the lower columns and the crowd are in frame; the upper facade is cropped out of the picture, smooth unadorned stone, no name board, no plaque, no characters, no lettering, no text.",

    # ---------------- TẬP 38 ----------------
    "t38_a1_02_roadside_diner_night_empty_stools":
        "Tight framing on the empty counter of a roadside eatery at night: empty stools, a bare counter, warm light, the window frame and a plain dark wall fill the background as soft blur, no signboard, no menu, no lettering, no characters, no numbers, no writing of any kind.",
    "t38_a1_10_electronics_repair_shop_clearwater_bench":
        "Tight crop on an electronics repair bench: a soldering iron, tangled cables and an open radio chassis, a plain smooth concrete wall behind with nothing pinned on it, no poster, no note, no label, no lettering, no characters, no numbers, no text.",
    "t38_a1_13_detectives_map_table_pins_dim_office":
        "Extreme close-up of a dim table with push pins stuck into a completely blank plain sheet of paper, no map lines, no labels, no legend, no writing, no text, no characters, no numbers; only bare hands and the edge of a lamp in frame.",
    "t38_a3_08_detective_before_board_blank_witness_notes":
        "Tight crop on a wall of empty plain notice frames whose surfaces are completely blank smooth off-white, a detective silhouette passing in front, a bare floor, no printed sheets, no writing, no text, no characters, no numbers.",
    "t38_a3_10_empty_chair_desk_lamp_over_map":
        "Tight crop on an empty wooden chair and a desk lamp, a completely blank plain sheet of paper on the desk with no map lines, no labels, no writing, no text, no characters, no numbers; a plain bare wall.",
    "t38_a3_13_pawn_shops_row_windows_night_unmarked":
        "A row of closed corrugated metal shutters along a wet empty street at night, seen straight on at ground level so that only the shutters, the kerb and one dim streetlamp are in frame; no windows, no signboards, no lettering, no characters, no numbers, no text.",
    "t38_a3_14_pawn_counter_glass_case_camera_fishing_rod":
        "Tight crop inside a dim shop on a plain glass counter holding a camera, a fishing rod and small unlabelled items; a plain smooth wall behind with nothing on it, no signboard, no price tags, no labels, no lettering, no characters, no numbers, no text.",
    "t38_a3_15_blank_receipt_pad_pen_on_counter":
        "Extreme close-up of a bare shop counter with a completely blank empty receipt pad, a pen and a simple scale; the paper surface is pure empty white with no printed lines, no writing, no text, no characters, no numbers; a plain blank wall behind.",
    "t38_a3_21_silhouette_at_curtain_anxious_motel_window":
        "Tight framing on a silhouette standing at a curtained window at night, the window frame and the curtain fill the picture, the glass is dark and empty with no lettering and no reflections of signs, no sign, no characters, no numbers, no text.",
    "t38_a3_31_roadside_biker_bar_exterior_motorcycles":
        "Tight crop on motorcycles parked on a plain unmarked concrete forecourt at dusk, a low angle so that only the bikes, wet ground and a blank wall are in frame, no building facade, no signboard, no lettering, no characters, no numbers, no text, the plates are blank.",
    "t38_a3_33_two_officers_silhouettes_doorway_calm":
        "Tight crop on two plain-clothes officer silhouettes standing in a plain doorway, only the doorway, the step and a blank wall are in frame, no signboard, no plaque, no lettering, no characters, no numbers, no text.",

    # ---------------- TẬP 39 ----------------
    "t39_a1_19_imported_motorcycle_night_street":
        "Tight crop on a large imported motorcycle parked under a street lamp on a wet night street; only the bike, the lamp post and blurred dark shapes are in frame, the rear plate is a plain blank rectangle, no storefronts, no signboards, no lettering, no characters, no numbers, no text.",
    "t39_a1_20_lavish_spending_night_market":
        "Tight framing on a silhouette of a man handing over money inside a dim stall lit by plain round paper lanterns with no writing, the background is a soft blur of dark shapes and unlit cloth awnings, no signboards, no characters, no lettering, no numbers, no text.",
    "t39_a1_22_family_table_empty_chair":
        "Tight crop on a wooden table with one empty chair pushed back and a single bowl, a plain bare wall behind with nothing on it, the window is out of frame, no family, no people, no lettering, no characters, no numbers, no text.",
    "t39_a1_26_greed_dim_stairwell_corners":
        "Extreme close-up of a peeling plaster stairwell wall with a single weak bulb at the edge of the frame, deep shadow corners, the wall completely bare with no sign, no plaque, no frame, no characters, no numbers, no text.",
    "t39_a2_02_nightclub_entrance_hostess_silhouette":
        "Tight framing on a narrow doorway glowing with colored light onto wet pavement, a slender woman silhouette at the door with her face in shadow, plain round paper lanterns without writing; everything above the door is cropped out of frame, no signboard, no characters, no lettering, no numbers, no text.",
    "t39_a2_08_wenzhou_alley_autumn_1997":
        "A narrow alley between two plain concrete walls in autumn 1997, wet cobbles, one dim window with plain curtains on the left and closed plain shutters on the right, nothing hanging on any wall, no storefronts, no signboards, no characters, no lettering, no numbers, no text.",
    "t39_a2_12_hefei_dance_hall_july_1999":
        "Tight framing on the tall glowing windows of a dance hall seen from the side of the street, the facade above and below the windows is cropped out of the picture, parked cars and blurred shadows at the bottom edge, no signboard, no characters, no lettering, no numbers, no text.",
    "t39_a2_14_market_lane_carpenter_toolbox":
        "Tight crop on a carpenter's wooden toolbox and handsaw resting on a cart, a plain cloth awning blurred behind, nothing hanging or posted anywhere, no signboards, no characters, no lettering, no numbers, no text.",
    "t39_a2_20_police_at_rental_house_door":
        "Tight crop on a plain unmarked door with a flashlight beam hitting it, two plain-clothes silhouettes seen from behind, no number plate, no sticker, no sign, no characters, no lettering, no numbers, no text.",
    "t39_a2_23_two_toolkits_dark_table":
        "Tight crop on two open toolkits of metal tools on a dark table, a plain smooth wall behind with nothing on it, no mask, no prop, no lettering, no characters, no numbers, no text.",
    "t39_a3_04_workplaces_cosmetics_eatery_bar":
        "Tight framing on a small cosmetics counter with plain unmarked jars and bottles, a worker silhouette behind, a plain smooth wall filling the background, no shelves of labels, no signboards, no characters, no lettering, no numbers, no text.",
    "t39_a3_13_cloud_sword_police_command_room":
        "Tight crop on a row of dark monitors in a dim command room, each screen showing nothing but a blank faint glow with no interface graphics, no glyphs, no characters, no numbers, no text; a plain dark wall.",
    "t39_a4_01_nanchang_courthouse_exterior_dec_2020":
        "Viewed from the very bottom of the wide stone steps of a grey institutional building in December 2020, crowd silhouettes on the steps, the upper facade cropped out of frame entirely, smooth unadorned stone, no name board, no emblem, no characters, no lettering, no text.",
    "t39_a4_03_courtroom_witness_stand_empty":
        "Tight crop on an empty wooden witness stand, plain bench rows in soft focus behind, bare walls, no emblem, no plaque, no banner, no characters, no lettering, no numbers, no text.",
    "t39_a4_15_lone_woman_crowded_station_escape_chance":
        "Tight crop on a lone woman silhouette among blurred commuters in a station concourse, plain concrete columns and a soft blurred background, nothing legible, no sign, no characters, no lettering, no numbers, no text.",
    "t39_a4_16_rental_flat_cash_split_table":
        "Extreme close-up of two equal stacks of plain unmarked banknotes on a bare table under a bare bulb, the notes show no printing, no portraits, no numbers, no characters; empty chairs blurred behind, no writing, no text.",
    "t39_a4_17_hardware_shelf_rope_iron_bars_evening":
        "Tight crop on shelves of coiled rope and metal bars inside a plain store, a plain smooth wall behind with nothing on it, a silhouette leaving through the door in soft focus, no signboard, no labels, no lettering, no characters, no numbers, no text.",
    "t39_a5_03_jiangxi_high_court_winter_exterior":
        "Viewed from the very bottom of the wide stone steps of a grey institutional building on a winter day, bare trees at the edges, the upper facade cropped out of the picture entirely, smooth unadorned stone, no name board, no emblem, no characters, no lettering, no text.",
    "t39_a5_10_nightlife_street_one_figure_turns_away":
        "Tight framing on one figure stopping and turning away on a night street, the background reduced to large abstract blurred circles of coloured light with no letter shapes, no signboards, no characters, no lettering, no numbers, no text.",
}

REASON = {
    "t37_a2_05_ho_nai_beer_eatery_plastic_stools_night": "v1 còn biển chữ",
    "t37_a2_22_backpack_flashlight_gloves_on_bed": "v1 còn thẻ dán trên tường",
    "t37_a3_25_ambulance_misty_lane_rear_open_lights": "v1 còn ký hiệu/char trên xe",
    "t37_a4_09_trembling_hands_pen_blank_form": "v1 biên bản còn chữ",
    "t37_a4_14_blank_forms_pen_barred_window_desk": "v1 giấy còn chữ",
    "t37_a4_19_courthouse_exterior_morning_crowd_steps": "v1 còn huy hiệu chữ trên thành",
    "t37_a5_05_crowd_outside_courthouse_dusk_relief": "v1 còn chữ Hán trên vòm",
    "t38_a1_02_roadside_diner_night_empty_stools": "v1 còn biển dọc",
    "t38_a1_10_electronics_repair_shop_clearwater_bench": "v1 còn giấy dán tường",
    "t38_a1_13_detectives_map_table_pins_dim_office": "v1 bản đồ còn nhãn",
    "t38_a3_08_detective_before_board_blank_witness_notes": "v1 khung tranh còn giấy chữ",
    "t38_a3_10_empty_chair_desk_lamp_over_map": "v1 bản đồ + biển tường còn chữ",
    "t38_a3_13_pawn_shops_row_windows_night_unmarked": "v1 còn biển Hán",
    "t38_a3_14_pawn_counter_glass_case_camera_fishing_rod": "v1 còn biển dọc",
    "t38_a3_15_blank_receipt_pad_pen_on_counter": "v1 còn biển lớn + giấy chữ",
    "t38_a3_21_silhouette_at_curtain_anxious_motel_window": "v1 còn chữ trên kính",
    "t38_a3_31_roadside_biker_bar_exterior_motorcycles": "v1 còn biển + biển số",
    "t38_a3_33_two_officers_silhouettes_doorway_calm": "v1 còn biển Hán",
    "t39_a1_19_imported_motorcycle_night_street": "v1 biển số có ký tự",
    "t39_a1_20_lavish_spending_night_market": "v1 còn biển Hán",
    "t39_a1_22_family_table_empty_chair": "v1 còn chữ trên kính",
    "t39_a1_26_greed_dim_stairwell_corners": "v1 còn bảng số",
    "t39_a2_02_nightclub_entrance_hostess_silhouette": "v1 còn biển Hán lớn",
    "t39_a2_08_wenzhou_alley_autumn_1997": "v1 còn biển Hán",
    "t39_a2_12_hefei_dance_hall_july_1999": "v1 còn biển Hán + ANGEL",
    "t39_a2_14_market_lane_carpenter_toolbox": "v1 còn biển Hán dọc",
    "t39_a2_20_police_at_rental_house_door": "v1 còn giấy dán cửa",
    "t39_a2_23_two_toolkits_dark_table": "v1 còn ký tự trên nắp hộp",
    "t39_a3_04_workplaces_cosmetics_eatery_bar": "v1 còn nhiều biển Hán",
    "t39_a3_13_cloud_sword_police_command_room": "v1 màn hình còn chữ",
    "t39_a4_01_nanchang_courthouse_exterior_dec_2020": "v1 còn chữ Hán trên tòa",
    "t39_a4_03_courtroom_witness_stand_empty": "v1 còn chữ trên tường tòa",
    "t39_a4_15_lone_woman_crowded_station_escape_chance": "v1 còn biển Hán",
    "t39_a4_16_rental_flat_cash_split_table": "v1 tiền còn in chữ",
    "t39_a4_17_hardware_shelf_rope_iron_bars_evening": "v1 còn biển Hán",
    "t39_a5_03_jiangxi_high_court_winter_exterior": "v1 còn chữ Hán trên tòa",
    "t39_a5_10_nightlife_street_one_figure_turns_away": "v1 còn nhiều biển neon chữ",
}


def main():
    by_ep = {}
    for name in P:
        by_ep.setdefault(name[1:3], []).append(name)

    for ep, names in sorted(by_ep.items()):
        path = WORK / f"bg_jobs_tap{ep}.json"
        shutil.copy2(path, BK / f"bg_jobs_tap{ep}_{STAMP}_r2.json")
        jobs = json.loads(path.read_text(encoding="utf-8"))
        n = 0
        for j in jobs:
            if j["name"] in P:
                j["prompt"] = P[j["name"]]
                n += 1
        path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"Tập {ep}: viết lại {n} prompt (round 2), backup _cu/bg_jobs_tap{ep}_{STAMP}_r2.json")

    flags = {
        "note": "Round 2 (26/11/2026): 37 ảnh vẫn còn chữ AI sau vòng 1. Nguyên tắc: đổi bối cảnh/crop sát + bỏ từ kích hoạt biển.",
        "extra_negative": "no writing of any kind, no lettering, no characters, no numbers, no logos, no signage, background reduced to soft unrecognizable blur",
        "flags": [
            {"ep": int(name[1:3]), "name": name, "reason": REASON.get(name, "")}
            for name in P
        ],
    }
    (WORK / "_qc_flags_t37_39.json").write_text(json.dumps(flags, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Danh sách flags round 2: {len(flags['flags'])} ảnh")


if __name__ == "__main__":
    main()
