#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Vòng 3: viết lại prompt 37 ảnh còn chữ (26/11/2026).

Nguyên tắc vòng 3 (sau khi vòng 2 crop sát vẫn còn chữ):
  - BỎ HẲN mọi từ kích hoạt chữ: sign, signage, shop, storefront-with-board,
    diner, pawn, motel, hotel, dance hall, nightclub, market stall board,
    notice, poster, form, receipt, map, label, plate, cash/banknote print,
    ambulance markings, court facade, tablet/screen text.
  - Thay bằng VẬT THỂ cụ thể + bề mặt trơn ("blank", "unmarked", "plain", "bare").
  - BỎ negation ("no text, no lettering...") — đã chứng minh không hiệu quả với
    FLUX.1-schnell và còn kích hoạt chữ.
  - Giữ chủ thể của shot để khớp kịch bản.
"""
import json
import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

PROMPTS = {
    # ---------------- T37 ----------------
    "t37_a2_05_ho_nai_beer_eatery_plastic_stools_night":
        "Empty red and blue plastic stools on wet asphalt at night, warm amber light spilling from an unseen doorway, "
        "rain-slick ground reflections, closed dark shutters behind, shallow depth of field, cinematic still, "
        "muted teal and amber palette, dramatic shadow",
    "t37_a2_22_backpack_flashlight_gloves_on_bed":
        "A worn canvas backpack resting on a bare bed sheet, a metal flashlight and a pair of work gloves laid beside it, "
        "plain undecorated plaster wall behind, single warm lamp from the side, cinematic still, desaturated palette, film grain",
    "t37_a3_25_ambulance_misty_lane_rear_open_lights":
        "Rear of a plain white van with red warning lamps glowing in heavy morning mist on a narrow wet lane, "
        "completely plain bodywork, bare trees fading into fog, cold blue-grey light, cinematic still, film grain",
    "t37_a4_09_trembling_hands_pen_blank_form":
        "Extreme close-up of two trembling hands holding a pen above a completely blank unmarked sheet of paper "
        "on a scratched wooden desk, hands filling the frame, plain dark wall behind, single hard side light, cinematic still",
    "t37_a4_14_blank_forms_pen_barred_window_desk":
        "A bare wooden desk by a barred window, a blank unmarked sheet of paper and a pen lying on it, cold grey daylight "
        "through the bars, empty bare room, cinematic still, desaturated teal palette, film grain",
    "t37_a4_19_courthouse_exterior_morning_crowd_steps":
        "Crowd of people in dark coats climbing wide stone steps in morning haze, tight framing on steps and shoulders only, "
        "upper facade cropped out of picture, cold overcast light, cinematic still, film grain",
    "t37_a5_05_crowd_outside_courthouse_dusk_relief":
        "Dense crowd of people gathered outside a plain stone building at dusk, tight framing on heads and shoulders, "
        "featureless stone wall behind, shaft of light between them, cinematic still, film grain",

    # ---------------- T38 ----------------
    "t38_a1_02_roadside_diner_night_empty_stools":
        "Empty counter with round chrome stools and a bare countertop at night, warm orange light from an unseen window, "
        "wet highway asphalt outside, tight framing on the counter edge, cinematic still, film grain",
    "t38_a1_10_electronics_repair_shop_clearwater_bench":
        "A cluttered electronics repair bench with an oscilloscope, soldering iron and scattered components, "
        "plain pegboard wall behind, cool fluorescent light, cinematic still, film grain",
    "t38_a1_13_detectives_map_table_pins_dim_office":
        "Close-up of a bare tabletop with a few plain push pins and lengths of string, dim lamp overhead, dark empty office around, "
        "faces not visible, cinematic still, film grain",
    "t38_a3_08_detective_before_board_blank_witness_notes":
        "A detective seen from behind facing a large blank wall board, tight framing on shoulders and head, "
        "board surface completely empty, dim office, cinematic still, film grain",
    "t38_a3_10_empty_chair_desk_lamp_over_map":
        "An empty wooden chair at a desk with a gooseneck lamp switched on, a plain blank sheet spread on the desk, "
        "dark room, tight framing, cinematic still, film grain",
    "t38_a3_13_pawn_shops_row_windows_night_unmarked":
        "Row of dark shuttered shopfronts with blank boarded windows and reflective glass at night, wet street reflections, "
        "narrow framing, cinematic still, film grain",
    "t38_a3_14_pawn_counter_glass_case_camera_fishing_rod":
        "Close-up of a glass display case on a wooden counter holding an old camera and a fishing rod, "
        "plain undecorated shelf behind, warm dim light, cinematic still, film grain",
    "t38_a3_15_blank_receipt_pad_pen_on_counter":
        "Close-up of a plain pad of blank paper and a pen lying on a worn counter surface, blank glass display case blurred behind, "
        "dim interior, cinematic still, film grain",
    "t38_a3_21_silhouette_at_curtain_anxious_motel_window":
        "Silhouette of a person standing behind a plain curtain at a window at night, curtain fabric filling the frame, "
        "blurred city glow beyond, cinematic still, film grain",
    "t38_a3_31_roadside_biker_bar_exterior_motorcycles":
        "Two parked motorcycles seen from behind on a gravel lot beside a dark plain wall, taillights off, dusk, "
        "tight framing on rear wheels, cinematic still, film grain",
    "t38_a3_33_two_officers_silhouettes_doorway_calm":
        "Two uniformed figures standing in a doorway seen as silhouettes from inside a dark corridor, plain door frame, "
        "calm quiet mood, cinematic still, film grain",

    # ---------------- T39 ----------------
    "t39_a1_19_imported_motorcycle_night_street":
        "Close-up of the front wheel and engine of a parked motorcycle at night, blurred warm street bokeh behind, "
        "wet asphalt, cinematic still, film grain",
    "t39_a1_20_lavish_spending_night_market":
        "Overhead close-up of a stall counter with piled fruit and coins, hands exchanging small paper notes, "
        "blurred warm lights behind, cinematic still, film grain",
    "t39_a1_22_family_table_empty_chair":
        "A plain wooden family table with one empty chair, a bare white bowl and folded cloth on the table, "
        "plain wall and window behind, cold daylight, cinematic still, film grain",
    "t39_a1_26_greed_dim_stairwell_corners":
        "Dim corner of a concrete stairwell, worn steps and a metal handrail, damp wall, single weak bulb glow, "
        "cinematic still, film grain",
    "t39_a2_02_nightclub_entrance_hostess_silhouette":
        "Silhouette of a woman in a long coat standing in a doorway of a plain building at night, blank door behind her, "
        "blurred street lights, tight framing, cinematic still, film grain",
    "t39_a2_08_wenzhou_alley_autumn_1997":
        "Narrow alley between plain concrete walls, dry autumn leaves on the ground, bare branches overhead, "
        "grey overcast light, cinematic still, film grain",
    "t39_a2_12_hefei_dance_hall_july_1999":
        "Tall arched windows of an old brick building glowing warm amber at night, completely blank undecorated facade, "
        "framed tight on the windows alone, faint bare branches at the edge, cinematic still, film grain",
    "t39_a2_14_market_lane_carpenter_toolbox":
        "Close-up of a carpenter's wooden toolbox and handsaw on a cart, plain cloth awning blurred behind, "
        "warm dusty daylight, cinematic still, film grain",
    "t39_a2_20_police_at_rental_house_door":
        "A uniformed officer and a civilian standing at a plain wooden door of a bare corridor, tight framing on backs "
        "and shoulders, bare plaster wall, dim corridor light, cinematic still, film grain",
    "t39_a2_23_two_toolkits_dark_table":
        "Two metal toolkits open on a dark table, sockets and pliers laid inside, plain dark wall behind, "
        "single hard light, cinematic still, film grain",
    "t39_a3_04_workplaces_cosmetics_eatery_bar":
        "A cluttered counter of cosmetic bottles and jars in a dim shop interior, plain shelves behind, warm low light, "
        "tight framing, cinematic still, film grain",
    "t39_a3_13_cloud_sword_police_command_room":
        "A bare command room desk with a dark switched-off monitor and a radio unit, blinds casting shadows, empty chairs, "
        "cinematic still, film grain",
    "t39_a4_01_nanchang_courthouse_exterior_dec_2020":
        "Stone steps and tall bare columns of a monumental government building on a winter afternoon, framed tight on the steps "
        "and columns with the upper facade cropped out, pale grey light, cinematic still, film grain",
    "t39_a4_03_courtroom_witness_stand_empty":
        "An empty wooden witness stand inside a courtroom, tight framing on the rail and microphone, blank plaster walls, "
        "cool daylight from high windows, cinematic still, film grain",
    "t39_a4_15_lone_woman_crowded_station_escape_chance":
        "A woman seen from behind in a crowd inside a station concourse, tight framing on her shoulders and surrounding heads, "
        "blurred light haze, cinematic still, film grain",
    "t39_a4_16_rental_flat_cash_split_table":
        "Close-up of plain unmarked banknotes and coins spread on a scratched table, a hand reaching in, dim bare room, "
        "cinematic still, film grain",
    "t39_a4_17_hardware_shelf_rope_iron_bars_evening":
        "A hardware shelf stacked with coils of rope and iron bars, plain walls, dim evening light through a bare window, "
        "tight framing on the goods, cinematic still, film grain",
    "t39_a5_03_jiangxi_high_court_winter_exterior":
        "Stone steps and columns of a monumental courthouse in winter fog, framed tight on the steps so the facade is out of picture, "
        "pale grey light, cinematic still, film grain",
    "t39_a5_10_nightlife_street_one_figure_turns_away":
        "One figure stopping and turning away on a night street, background reduced to large abstract circles of coloured light, "
        "cinematic still, film grain",
}


def load_jobs(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    if isinstance(data, dict):
        for key in ("jobs", "items", "shots"):
            if key in data:
                return data[key]
        raise ValueError(f"Không tìm thấy list job trong {path}")
    return data


def main():
    stamp = time.strftime("%Y%m%d_%H%M")
    total = 0
    for ep in (37, 38, 39):
        path = WORK / f"bg_jobs_tap{ep}.json"
        if not path.exists():
            continue
        bak = WORK / "_cu" / f"bg_jobs_tap{ep}_{stamp}_r3.json"
        bak.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(path, bak)

        jobs = load_jobs(path)
        n = 0
        for j in jobs:
            name = j.get("name", "")
            if name in PROMPTS:
                j["prompt"] = PROMPTS[name]
                n += 1
        path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
        print(f"t{ep}: cập nhật {n} prompt -> {bak.name}")
        total += n

    print(f"TONG: {total} prompt vòng 3")
    missing = set(PROMPTS) - set()
    if total != len(PROMPTS):
        print(f"!! CẢNH BÁO: định nghĩa {len(PROMPTS)} mà chỉ ghi {total} (lệch {len(PROMPTS) - total})")


if __name__ == "__main__":
    main()
