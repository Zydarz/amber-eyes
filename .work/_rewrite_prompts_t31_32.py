#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Viết lại prompt rủi ro chữ cho Tập 31 + Tập 32 (27/11/2026).

Áp dụng đúng bài học T37–39 (26/11/2026) cho FLUX.1-schnell:
  1. GỠ mọi từ kích hoạt chữ (sign/shop/notice/map/calendar/screen/ledger...)
  2. Thay bằng VẬT THỂ cụ thể + bề mặt TRƠN ("blank", "unmarked", "plain",
     "bare", "featureless")
  3. ĐƯA VẬT MANG CHỮ ra khỏi khung (đổi góc máy, crop, tight framing)
  4. BỎ negation trong core prompt (không hiệu quả với FLUX, còn kích hoạt chữ)
     -> phần "no text, no letters..." trong STYLE_SUFFIX của flux_client vẫn giữ
        nguyên (đó là hằng số chung, đã được kiểm chứng ở T39 135/135).

Dùng: py -3 .work/_rewrite_prompts_t31_32.py
Tự sao lưu file cũ vào .work/_cu/ trước khi ghi (L5).
"""
import json
import shutil
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

# ---------------------------------------------------------------- TẬP 31
T31 = {
    "t31_a1_02b_arrest_order_dark_desk":
        "Close-up of a closed plain kraft folder lying flat on a stark wooden desk in a dim room, "
        "a single cold overhead tungsten bulb above, deep shadow, solemn legal gravity, "
        "graphic novel noir, cinematic still",

    "t31_a1_03_ten_month_calendar_shadow":
        "Dimly lit Vietnamese home study at night, ten completely blank unmarked white sheets fanned out "
        "across a bare desk, the silhouette of a middle-aged man in a neat collared shirt seen from behind, "
        "cold blue window light on his shoulders, no visible face, cinematic still",

    "t31_a1_05_daylight_office_night_phone":
        "Split noir composition: on the left a sunlit tidy government desk with a plain closed folder, "
        "on the right a dark empty room lit only by a cold blue glow rising from below, "
        "a silhouetted hand resting palm-up, cinematic still",

    "t31_a1_06_official_case_folder_desk":
        "Investigator wooden desk under a warm banker lamp, a closed plain kraft case file and a fountain pen, "
        "deep shadows around the edges, graphic novel noir aesthetic, cinematic still",

    "t31_a1_07_market_management_building_exterior":
        "Exterior wide shot of a modest two-story Vietnamese provincial office building with iron gates "
        "and an empty concrete courtyard under an overcast winter sky, framing tight on the gate and courtyard "
        "so the upper facade stays out of picture, graphic novel noir, cinematic still",

    "t31_a1_10_four_seasons_clock_silence":
        "Close-up of a minimalist round wall clock with a completely blank unmarked face on a pale office wall, "
        "long slanting afternoon shadows across an empty hallway, quiet passage of time, "
        "noir illustration, cinematic still",

    "t31_a1_12_shocked_town_street_dusk":
        "Small northern Vietnamese town street at dusk, distant silhouetted neighbors standing quietly "
        "beside shuttered doorways under dim streetlamps, framing tight on the figures and the empty road, "
        "tense hushed atmosphere, no faces, cinematic still",

    "t31_a1_19_dark_smartphone_glow_night":
        "A dark smartphone lying face down on a wooden table in a pitch-black room, cold blue glow spilling "
        "from beneath it onto the surrounding shadows, minimalist noir composition, cinematic still",

    "t31_a1_21_hidden_chat_glow_shadows":
        "Dark desk washed by a pale cold glow, a thick stack of completely blank unmarked white pages bound "
        "with a metal clip, a keyboard blurred at the edge of frame, graphic novel noir mood, cinematic still",

    "t31_a1_21b_eighty_eight_page_stack":
        "Close-up of a thick bound stack of completely blank unmarked white pages on a dark desk under "
        "a cold blue lamp glow, deep shadow, cinematic still",

    "t31_a1_22_viral_screens_dark_room":
        "Overhead view of a dark crowd of silhouettes, dozens of dim phone screens seen as abstract pale rectangles "
        "lighting cupped hands at night, no visible faces, cinematic still",

    "t31_a1_23_police_cyber_desk_warning":
        "Late-night police command room in Vietnam, silhouetted officers at desks with monitors reduced to "
        "abstract radar-like rings of light, warm desk lamps, serious disciplined noir atmosphere, cinematic still",

    "t31_a1_23b_malware_link_shield_warning":
        "A dark smartphone lying flat on a table, its screen a plain abstract amber glow with a single simple "
        "geometric triangle shape, shadowed room, cybersecurity caution, graphic novel noir, cinematic still",

    "t31_a1_25_scattered_blank_papers_wind":
        "Completely blank unmarked white sheets of paper swirling in the night wind down an empty misty alley "
        "under a streetlamp, graphic novel noir aesthetic, cinematic still",

    "t31_a1_26_magnifying_glass_calm_desk":
        "Close-up of a brass magnifying glass resting on a closed plain smooth leather notebook "
        "on a dark wooden desk, warm amber reading lamp glow, calm analytical mood, cinematic still",

    "t31_a2_01_five_year_timeline_thread":
        "Top-down view of a completely blank unmarked textured paper map on a dark table, "
        "a single thin red thread connecting two plain metal pins, dramatic side lighting, cinematic still",

    "t31_a2_04_hung_yen_empty_bus_stop":
        "Empty rural roadside shelter in northern Vietnam countryside at early misty dawn, "
        "a single abandoned wooden bench under a plain corrugated roof, a road fading into fog, "
        "melancholic noir, cinematic still",

    "t31_a2_05_late_night_keyboard_glow":
        "Silhouetted hands typing on a keyboard in a dark room at 2 AM, cold blue light from a lamp out of frame "
        "casting sharp shadows on a bare wall, no visible face, cinematic still",

    "t31_a2_06_anonymous_screen_five_years":
        "Still life in noir lighting: a dark glass hourglass on a shadowed table beside a plain switched-off phone, "
        "dust drifting in a thin amber beam, five years passing silently, cinematic still",

    "t31_a2_10_power_asymmetry_chess_board":
        "Close-up of a wooden chessboard in dramatic low-key lighting, a tall dark king piece casting a long "
        "looming shadow over a lone smaller pawn, plain undecorated pieces, noir metaphor for power asymmetry, "
        "cinematic still",

    "t31_a2_11_calendar_pages_2020_to_2025":
        "Five worn completely blank unmarked wall sheets stacked beside a dim desk lamp in a quiet shadowed room, "
        "dust motes in the amber beam, noir style, cinematic still",

    "t31_a2_13_fading_screen_fantasy_starvation":
        "Silhouette of a solitary man sitting motionless before a monitor reduced to a flat pale glow, "
        "tight framing on the back of his head and shoulders, dark room, heavy shadows, "
        "psychological emptiness, cinematic still",

    "t31_a2_17_phone_call_dark_office_window":
        "Back silhouette of a man standing by a tall office window at dusk, one hand raised to his ear, "
        "overlooking an empty courtyard below, no visible face, cinematic still",

    "t31_a2_19b_facade_uniform_coat_hanger":
        "Neat collared work jacket hanging cleanly on a wooden coat rack inside a quiet dim office, "
        "symbol of preserving public respectability, noir style, cinematic still",

    "t31_a2_22_cracked_mask_phone_reflection":
        "A smooth featureless white mask on a dark desk beside a phone lying face down, "
        "a thin hairline crack running down the mask, noir psychological tension, cinematic still",

    "t31_a2_22b_fatal_crack_glass_screen":
        "Macro noir view of a cracked dark phone screen lying face up, a thin illuminated fracture "
        "running diagonally across the glass, tense atmosphere, cinematic still",

    "t31_a3_05_severed_empathy_light_circuit":
        "Minimalist noir still life of a warm glowing filament bulb separated from an unlit dark bulb "
        "by an open brass switch mounted on a plain dark panel, metaphor for empathy disconnect, cinematic still",

    "t31_a3_09_office_meeting_table_calm_facade":
        "Neat Vietnamese government meeting room with a long wooden table, small porcelain teacups "
        "and neatly aligned chairs, morning light through curtains, calm respectable surface, cinematic still",

    "t31_a3_13_normal_family_dinner_shield":
        "Warmly lit Vietnamese home dining table with bowls and chopsticks, a plain dark phone lying face down "
        "near the edge, peaceful surface hiding dark secrets, noir style, cinematic still",

    "t31_a3_19_distorted_chat_reflection":
        "Curved distorting glass lens held up in front of a flat cold blue glow in a dark room, "
        "bending the light unnaturally, noir style, cinematic still",

    "t31_a3_25b_social_media_scroll_probe":
        "Close-up silhouette of a thumb resting on a dimly lit phone lying on a table in a quiet room at night, "
        "watchful probing mood, cinematic still",

    "t31_a4_03_police_hq_night_lights":
        "Exterior of a modern Vietnamese office building at night, tight framing on the upper-floor windows "
        "brightly lit against dark misty hills, the lower facade out of picture, resolute noir mood, cinematic still",

    "t31_a4_03b_urgent_report_red_phone":
        "Command desk in a provincial police office at night with a dark landline telephone and a warm lamp, "
        "a plain closed folder lying on the desk, urgent decisive mood, cinematic still",

    "t31_a4_04_task_force_briefing_table":
        "Briefing room table with warm overhead lamps, plain closed manila folders, plain metal pins and "
        "lengths of string laid across the tabletop, coffee cups, disciplined investigative atmosphere, "
        "noir style, cinematic still",

    "t31_a4_05_digital_forensics_cross_check":
        "Back silhouette of an investigator in a dim forensic office looking at abstract glowing waveform "
        "and timeline shapes on a monitor, screen reduced to pure bands of light, focused noir mood, cinematic still",

    "t31_a4_09_official_stamp_warrant_desk":
        "Close-up of stainless steel handcuffs beside a closed plain leather folder on a dark wooden desk, "
        "warm lamp glow, sharp side light, noir style, cinematic still",

    "t31_a4_16b_shattered_trophy_self_pity":
        "Toppled tarnished metallic award object lying on a shadowed floor in a dim room, "
        "its plain surface scuffed and unmarked, symbolic of pathological self-pity, noir style, cinematic still",

    "t31_a4_18b_heavy_rain_public_square":
        "Empty paved public square in cold winter rain, wet stone reflecting cold streetlight, "
        "framing low on the empty ground, gloomy noir, cinematic still",

    "t31_a4_20_expanding_investigation_files":
        "Neatly arranged stack of plain closed case folders, sealed plain evidence bags and a fountain pen "
        "on an investigator desk under warm light, thorough legal rigor, noir style, cinematic still",

    "t31_a4_21b_calm_memorial_light_screen":
        "Warm amber desk lamp glowing steadily beside a powered-off black monitor on a dark desk, "
        "quiet dignity and order, graphic novel noir, cinematic still",

    "t31_a5_06_responsible_citizen_phone_down":
        "Close-up of a hand gently placing a dark switched-off phone face down on a warm wooden table "
        "beside a cup of tea, calm responsible choice, noir style, cinematic still",

    "t31_a5_15_digital_hygiene_locked_shield":
        "Solid brass padlock resting on a clean dark desk beside a closed dark laptop under warm light, "
        "symbol of digital responsibility and safety, noir style, cinematic still",

    "t31_a5_16_courthouse_dawn_justice_light":
        "Stone steps and tall columns of a courthouse at dawn bathed in clear golden sunrise light after a storm, "
        "framing tight on the steps so the upper facade stays out of picture, calm faith in rule of law, "
        "cinematic still",

    "t31_a5_20_amber_eyes_study_closing":
        "Cozy noir narrator study desk with a closed plain dark case folder, a warm amber desk lamp glowing softly, "
        "bookshelf silhouettes in background, cinematic still",
}

# ---------------------------------------------------------------- TẬP 32
T32 = {
    "t32_a1_01_hong_kong_harbour_skyline_1990s":
        "Cinematic wide opening shot of Victoria Harbour and the Hong Kong island skyline at night in the 1990s, "
        "glittering high-rises reflected on dark water, junk boats in the foreground, "
        "distant lights softened into abstract bokeh, cinematic still",

    "t32_a1_02_shadow_man_over_neon_city":
        "A lone black silhouette of a man standing on a Kowloon rooftop at night overlooking a vast field of "
        "abstract coloured light, every light source reduced to soft bokeh circles, face completely lost in shadow, "
        "seen from behind, Hong Kong 1990s, cinematic still",

    "t32_a1_05_herbal_tea_shop_yau_ma_tei":
        "Interior of a small old-fashioned herbal tea shop on a Yau Ma Tei street in Hong Kong, 1960s, "
        "wooden shelves of plain ceramic jars, a bare wooden counter, warm dim lamplight, "
        "framing tight on the shelves so the street front stays out of picture, no people, cinematic still",

    "t32_a1_08_law_books_study_lamp":
        "Desk lit by a single desk lamp, a stack of thick law books with completely blank unmarked plain covers, "
        "tight framing on the book edges, Hong Kong apartment at night, no people, cinematic still",

    "t32_a1_09_loose_blank_pages_and_lamp":
        "Close-up of loose sheets that are completely blank and unmarked scattered under a brass desk lamp, "
        "a plain pen resting beside them, dark room, Hong Kong, cinematic still",

    "t32_a1_14_empty_luxury_watch_shop":
        "Interior of an upscale Hong Kong watch boutique in 1990 after closing, empty glass counter cases "
        "with plain blank velvet trays, one overturned stool, dim emergency lighting, no people, cinematic still",

    "t32_a1_15_kai_tak_airport_tarmac_noon":
        "Wide shot of an empty airport tarmac in Hong Kong at harsh midday in July 1991, "
        "a distant plain armored van with completely blank unmarked bodywork parked far away, "
        "heat haze, cinematic still",

    "t32_a1_16_duffel_bags_of_plain_cash_bundles":
        "Several open duffel bags overflowing with plain bundles of paper wrapped in completely blank unmarked bands, "
        "on the floor of a dim bare room, a single hanging bulb, cinematic still",

    "t32_a1_17_airport_perimeter_police_dawn":
        "Hong Kong police cars with flashing lights at an airport perimeter fence at dawn in 1991, "
        "the empty grey sea beyond the runway, distant officer silhouettes, tight framing on the fence line, "
        "cinematic still",

    "t32_a1_18_armored_truck_cab_windshield_view":
        "View from inside the driver's cab of an armored truck through the windshield onto a bright empty "
        "airport apron, steering wheel and dashboard in dark foreground, Hong Kong 1991, cinematic still",

    "t32_a1_19_masked_silhouettes_far_on_apron":
        "Distant tight formation of dark silhouettes moving in unison across a sunlit airport apron, "
        "framing tight on the figures so no vehicle is in picture, heat haze, Hong Kong 1991, "
        "faces unreadable, cinematic still",

    "t32_a1_20_abandoned_armored_van_doors_open":
        "An armored cash van left on an airport tarmac with its rear doors open and completely empty, "
        "plain unmarked bodywork, flashing blue-red police lights washing across the concrete, "
        "long shadows, no people, cinematic still",

    "t32_a1_26_lawyers_conference_room_blank_files":
        "Expensive law firm conference room in Hong Kong in 1994, a polished long table with stacks of closed "
        "folders whose covers are completely blank and unmarked, tight framing on the tabletop, "
        "silhouettes of suited figures around it, cinematic still",

    "t32_a1_28_appeal_court_blank_easel":
        "Hong Kong Court of Appeal in 1995, silhouettes of lawyers beside a large completely blank unmarked "
        "white board on an easel, judges' bench in the dim background, warm lamp light, cinematic still",

    "t32_a1_29_courtroom_doors_swing_open":
        "Heavy wooden courtroom double doors swinging open onto bright daylight, a crowd of dark silhouettes "
        "gathered on the steps, framing tight on the doorway and the steps, Hong Kong 1995, "
        "dramatic backlight, cinematic still",

    "t32_a1_33_giant_hand_over_toy_courthouse":
        "Symbolic noir image of a huge shadowy hand hovering over a miniature toy-like model of a plain stone "
        "building with tiny scales and small figures, tight framing on the model so no wall lettering appears, "
        "dramatic lamp light, cinematic still",

    "t32_a2_04_hand_drawn_route_map_blank":
        "Close-up of a completely blank unmarked sheet of textured paper on a dim table with thin string and "
        "two plain pins laid across it, small lamp light, cinematic still",

    "t32_a2_05_shouson_hill_winding_road_1996":
        "Quiet winding road bend through green slopes in Hong Kong, late afternoon in May 1996, "
        "one plain unmarked sedan in the middle distance and two dark vans approaching far behind, "
        "tight framing on the road surface, stillness, cinematic still",

    "t32_a2_07_two_vans_leaving_under_trees":
        "Two dark vans driving away along a tree-lined hillside road in Hong Kong at dusk, tail lights fading, "
        "an empty quiet bend in the foreground, framing low on the road, no people, cinematic still",

    "t32_a2_11_empty_guard_booth_at_gate":
        "Empty security booth with plain unmarked walls beside an open iron mansion gate in Hong Kong at dawn, "
        "a lone parked limousine on the driveway, tight framing on the bare booth interior, "
        "no guards, quiet mist, cinematic still",

    "t32_a2_12_fixed_daily_route_road_aerial":
        "High angle view of a winding Hong Kong hillside road lit by early morning sun, a single plain unmarked "
        "car on it, faint worn tracks, calm wake-up-call mood, no people, cinematic still",

    "t32_a2_20_tea_table_negotiation_blank_papers":
        "Low lacquered tea table with two plain teacups and a few completely blank unmarked sheets between two "
        "armchairs occupied by dark silhouettes, soft lamp light, Hong Kong mansion in 1996, cinematic still",

    "t32_a2_21_red_lucky_knot_beside_vault_door":
        "Massive steel home vault door standing ajar in a dim room, a small plain red knotted cord ornament "
        "hanging in the foreground, golden light spilling from the vault, no people, cinematic still",

    "t32_a2_22_lucky_red_lanterns_quiet_street":
        "Strings of plain red paper lanterns glowing over a quiet Hong Kong street at night, "
        "wet pavement reflecting red light, framing tight on the lanterns so no storefront is in picture, "
        "no people, auspicious but uneasy mood, cinematic still",

    "t32_a2_24_delivery_trucks_convoy_dawn":
        "Convoy of plain unmarked delivery trucks with completely blank bodywork driving through quiet "
        "Hong Kong streets at dawn in 1996, grey light, wet road, silhouette of tall buildings, cinematic still",

    "t32_a2_25_house_lights_on_at_dawn":
        "Large Hong Kong family home at first light with one downstairs window glowing warmly, "
        "a plain unmarked car driving away down the empty lane, long pale shadows, quiet stillness, "
        "no people, cinematic still",

    "t32_a2_26_empty_ledger_desk_quiet_decision":
        "Wooden study desk with a telephone and a stack of completely blank unmarked sheets of paper, "
        "a closed door behind, morning light through blinds, no people, decision of silence mood, cinematic still",

    "t32_a3_01_supercars_in_lit_garage":
        "Row of expensive sports cars in a polished underground garage lit by cold spotlights in Hong Kong "
        "in 1996, tight framing on the bodywork with completely blank unmarked panels, reflective floor, "
        "no people, cinematic still",

    "t32_a3_04_spinning_roulette_light_streaks":
        "Close-up of a spinning roulette wheel blurred into pure streaks of golden light, a small ball caught "
        "mid-bounce, deep shadows around, noir casino atmosphere, cinematic still",

    "t32_a2_28_roulette_wheel_in_shadow_warning":
        "A lone roulette wheel reduced to a dark circle of blurred golden light in an empty casino room, "
        "a silhouette of a man standing beside it with his back turned, a faint warm light above, "
        "symbolic warning mood, Macau, cinematic still",

    "t32_a3_29_roulette_at_dawn_silhouette":
        "Silhouette of a man leaning at a casino table reduced to a blur of golden light, an almost empty room "
        "at dawn, grey daylight leaking through curtains, scattered plain chips, face hidden, "
        "weary mood, cinematic still",

    "t32_a3_13_corporate_headquarters_tower_dusk":
        "Tall glass corporate tower of a property conglomerate in Hong Kong at dusk in 1997, lit offices, "
        "empty plaza below, framing tight on the upper floors so the entrance stays out of picture, cinematic still",

    "t32_a3_16_sedan_on_flyover_dusk_1997":
        "A plain unmarked luxury sedan driving alone along a concrete flyover in Hong Kong at dusk in "
        "September 1997, two dark vans looming in the distance behind it, orange sunset sky, cinematic still",

    "t32_a3_20_road_map_single_route_red_thread":
        "Large completely blank unmarked wall panel with one route stretched in red thread between plain pins, "
        "dim lamp, a silhouette standing close with back turned, cinematic still",

    "t32_a4_03_spider_web_on_border_fence":
        "Dew-covered spider web stretched across a steel border fence at dawn, hazy plain rooftops in the "
        "background, soft cold light, symbolic net closing in, cinematic still",

    "t32_a4_06_guangdong_back_road_night_truck":
        "Remote dark country road in Guangdong province at night in late 1997, a parked plain unmarked truck "
        "with its lights off and two silhouettes beside it, tight framing on the road surface, thin fog, "
        "covert mood, cinematic still",

    "t32_a4_09_command_room_wall_map_red_alert":
        "Police command room in 1998 with a large completely blank unmarked wall panel, red alert lamps glowing, "
        "silhouettes of officers standing at the table, tense mood, cinematic still",

    "t32_a4_11_stakeout_car_night_lone_officer":
        "Silhouette of a lone detective sitting in a parked car at night on a dark Guangdong street, "
        "tight framing from inside the car on the windshield and his hands, glow of distant lights, "
        "face hidden, stakeout mood, cinematic still",

    "t32_a4_12_briefing_hall_rows_of_detectives":
        "Large briefing hall in Guangdong, 1998, rows of silhouettes of detectives seated facing a dim stage "
        "with a completely blank unmarked projection screen, smoky air, cinematic still",

    "t32_a4_13_blank_id_card_in_gloved_hand":
        "Close-up of a gloved hand holding a plain card with a completely smooth featureless surface, "
        "dark background, a thin beam of light across it, cinematic still",

    "t32_a4_14_highway_interchange_night_watchers":
        "Multi-level highway interchange in Shenzhen at night in 1998, streaks of car headlights, "
        "a few plain unmarked cars parked in the shadows, abstract light haze, cinematic still",

    "t32_a4_16_toll_plaza_dawn_car_approaching":
        "Empty highway toll plaza on an expressway at dawn in January 1998, plain unmarked booths in a row, "
        "a single dark car approaching in the distance, cold mist, cinematic still",

    "t32_a4_17_toll_plaza_special_police_flashing_lights":
        "Many police vehicles with flashing red and blue lights surrounding an empty highway toll plaza at dawn, "
        "plain unmarked bodywork, distant dark silhouettes of officers, swirling mist, wide shot, cinematic still",

    "t32_a4_20_wall_of_static_tv_screens":
        "Wall of old television screens in a dark newsroom all showing only featureless grey static, "
        "silhouettes of people standing in front, flickering light, Hong Kong 1998, cinematic still",

    "t32_a4_24_two_courthouses_split_composition":
        "Split composition of two plain stone and concrete court buildings side by side under dusk light, "
        "a thin river between them, framing tight on the upper architecture, no people, cinematic still",

    "t32_a5_02_courtroom_lawyers_tables_wide":
        "Wide view of a courtroom in 1998, rows of tables with silhouettes of lawyers and prosecutors, "
        "a judges' bench with silhouettes beneath a high ceiling, blank plaster walls, cold light, cinematic still",

    "t32_a5_04_press_photographers_courthouse_steps":
        "Large crowd of press photographers as dark silhouettes on wide stone steps with flashing camera lights, "
        "framing tight on heads and shoulders, Guangzhou in 1998, hazy morning, faces unreadable, cinematic still",

    "t32_a5_06_gavel_on_bench_dramatic_light":
        "Judge's wooden gavel poised over a dark bench in a courtroom, a single dramatic ray of light from a "
        "high window, blank plaster walls, a distant dark silhouette behind the bench, cinematic still",

    "t32_a5_07_court_corridor_long_hall_documents":
        "Long corridor of a court building with tall doors, silhouettes of officials carrying plain closed "
        "folders walking away, cold daylight from a far window, 1998, cinematic still",

    "t32_a5_08_appeal_bench_closed_folders_scales":
        "An appeal bench with closed plain folders and brass scales of justice on a dark polished surface, "
        "tight framing on the tabletop, dim chamber light, cinematic still",

    "t32_a5_15_psychologist_office_blank_notebook":
        "Quiet psychologist's office at night with an armchair, a lamp casting amber light, and an open notebook "
        "whose pages are completely blank and unmarked, no people, cinematic still",

    "t32_a5_17_black_sedans_convoy_changing_route":
        "Convoy of black plain unmarked armored sedans driving along a winding Hong Kong hillside road at dusk, "
        "one car taking a different branch of the road, dark silhouettes in the windows, cinematic still",

    "t32_a5_18_courthouse_columns_dusk_scales_statue":
        "Stone columns of a courthouse at dusk with a large statue of the scales of justice silhouetted against "
        "an orange sky, long shadows on the steps, framing tight on the columns, no people, cinematic still",

    "t32_a5_21_armored_limousines_garage_column":
        "Plain unmarked black armored limousines parked in a concrete garage at night, a single column of light "
        "between them, tight framing on the bodywork, no people, cinematic still",

    "t32_a5_25_closing_amber_eyes_over_closed_folder":
        "Pair of glowing amber tiger eyes in pitch darkness above a closed plain dark case folder, "
        "noir closing image, cinematic still",
}


def apply(ep, mapping):
    path = WORK / f"bg_jobs_tap{ep}.json"
    stamp = time.strftime("%Y%m%d_%H%M")
    bak = WORK / "_cu" / f"bg_jobs_tap{ep}_{stamp}_before_rewrite.json"
    bak.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(path, bak)

    jobs = json.loads(path.read_text(encoding="utf-8"))
    names = {j["name"] for j in jobs}
    missing = set(mapping) - names
    n = 0
    for j in jobs:
        if j["name"] in mapping:
            j["prompt"] = mapping[j["name"]]
            n += 1
    path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"t{ep}: ghi {n}/{len(mapping)} prompt -> {bak.name}")
    if missing:
        print(f"  !! khong khop (khong ton tai trong file): {sorted(missing)}")
    return n


def main():
    total = apply(31, T31) + apply(32, T32)
    print(f"TONG: {total} prompt viet lai (T31 {len(T31)} + T32 {len(T32)})")


if __name__ == "__main__":
    main()
