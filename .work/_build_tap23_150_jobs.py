#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate exactly 150 prompt definitions for Episode 23.
Following H21 (Kaggle FLUX Deep Noir Architecture) & H25 (Per-shot distribution).
Strict compliance with V5 (No real faces, silhouette only) and V9 (No gore, no text).
"""
import json
from pathlib import Path

# Act 1: 52 sentences -> 32 backgrounds (1.62 sents/bg)
# Act 2: 47 sentences -> 30 backgrounds (1.56 sents/bg)
# Act 3: 52 sentences -> 32 backgrounds (1.62 sents/bg)
# Act 4: 56 sentences -> 34 backgrounds (1.64 sents/bg)
# Act 5: 38 sentences -> 22 backgrounds (1.72 sents/bg)
# Total: 150 backgrounds

BG_SPECS = [
    # ==========================================
    # HỒI 1 (32 ảnh: t23_a1_01 đến t23_a1_32)
    # ==========================================
    {
        "name": "t23_a1_01_los_angeles_heatwave_skyline",
        "act": 1,
        "sentences": "1.02#1",
        "desc": "Bầu trời Los Angeles mùa hè 1985 ngột ngạt dưới làn sóng nhiệt gay gắt và u ám.",
        "prompt": "Panoramic establishing shot of 1980s Los Angeles skyline shrouded in thick oppressive smog and eerie heatwave haze, bleak retro architecture under pale gloomy grey sky, dark desaturated noir atmosphere."
    },
    {
        "name": "t23_a1_02_suburban_locked_window_blinds",
        "act": 1,
        "sentences": "1.02#2",
        "desc": "Cửa sổ nhà dân vùng ngoại ô đóng kín then cài trong nỗi hoang mang tột độ.",
        "prompt": "Close-up cinematic shot of suburban home window with tightly drawn metal blinds, heavy metal lock bolted shut, shadows of trembling leaves cast against pale stucco wall in unsettling silence."
    },
    {
        "name": "t23_a1_03_shadowy_figure_prowling_alley",
        "act": 1,
        "sentences": "1.02#3",
        "desc": "Bóng đen bí ẩn rình rập trong con hẻm tối giữa đêm khuya.",
        "prompt": "Mysterious solitary dark silhouette of an intruder lurking in a narrow dimly lit Los Angeles alleyway at midnight, wet asphalt reflecting faint moonlight, deep pitch-black shadows."
    },
    {
        "name": "t23_a1_04_darkened_suburban_neighborhood_night",
        "act": 1,
        "sentences": "1.02#4",
        "desc": "Khu dân cư ngoại ô chìm trong bóng tối dày đặc và không khí rình rập.",
        "prompt": "Eerie night view of a quiet 1980s Californian suburban street, dark houses with turned off lights, overgrown palm trees swaying in cold midnight wind, creeping dread."
    },
    {
        "name": "t23_a1_05_paranoia_empty_living_room_shadows",
        "act": 1,
        "sentences": "1.02#5",
        "desc": "Phòng khách gia đình tối tăm, ánh trăng xuyên qua rèm tạo thành chiếc bẫy âu lo.",
        "prompt": "Interior of a dark 1980s American living room, pale moonlight slanting through window blinds onto empty vintage sofa, dead silence, suffocating atmosphere of urban paranoia."
    },
    {
        "name": "t23_a1_06_newspaper_headline_night_stalker",
        "act": 1,
        "sentences": "1.02#6",
        "desc": "Trang báo lưu trữ về nỗi khiếp sợ mang tên Night Stalker (hoàn toàn không chữ).",
        "prompt": "Vintage 1980s crime newsprint sheets scattered on a wooden investigator desk, completely blank and unmarked with no writing or text at all, high contrast chiaroscuro lighting."
    },
    {
        "name": "t23_a1_07_massive_police_investigation_map",
        "act": 1,
        "sentences": "1.02#7",
        "desc": "Bản đồ điều tra quy mô lớn của cảnh sát với các vị trí đánh dấu.",
        "prompt": "Tactical police investigation wall map of Los Angeles county with pushpins and connected red strings, dark dossier room lit by a single overhead desk lamp, dramatic noir shadows."
    },
    {
        "name": "t23_a1_08_chaotic_crime_scene_flashlight",
        "act": 1,
        "sentences": "1.04#1",
        "desc": "Hiện trường đột nhập ban đêm với luồng đèn pin cảnh sát soi rọi.",
        "prompt": "Dark crime scene perimeter outside a single-story California home, narrow beam of an investigative flashlight cutting through heavy night mist, stark contrast, ominous quiet."
    },
    {
        "name": "t23_a1_09_predatory_gaze_backyard_fence",
        "act": 1,
        "sentences": "1.04#2",
        "desc": "Góc nhìn rình rập từ sau hàng rào gỗ hướng vào cửa sổ phòng ngủ.",
        "prompt": "Point of view shot through weathered wooden backyard fence slats, looking toward a dark suburban house bedroom window, creeping cold dread, deep black shadows."
    },
    {
        "name": "t23_a1_10_open_screen_window_unlatched",
        "act": 1,
        "sentences": "1.04#3",
        "desc": "Ô cửa sổ mở hé ban đêm với tấm lưới chống muỗi bị rạch thủng.",
        "prompt": "Detailed shot of an unlatched suburban sliding window slightly ajar at night, torn mesh screen gently fluttering in night draft, eerie chiaroscuro lighting, forensic documentary tone."
    },
    {
        "name": "t23_a1_11_hardware_store_gun_security_frenzy",
        "act": 1,
        "sentences": "1.04#4",
        "desc": "Cửa hàng bán khóa cửa và thiết bị an ninh cháy hàng trong cơn sốt bảo vệ gia đình.",
        "prompt": "Empty hardware store counter in 1985 with display racks of heavy iron deadbolts, padlocks and chains, dimly lit shop interior, cold desaturated tones, completely blank labels."
    },
    {
        "name": "t23_a1_12_detectives_carrillo_salerno_dossier",
        "act": 1,
        "sentences": "1.04#5",
        "desc": "Bàn làm việc của các điều tra viên kỳ cựu với hồ sơ vụ án xếp chồng.",
        "prompt": "Forensic detectives desk at Los Angeles Sheriff Department, thick paper case folders tied with string, vintage rotary telephone, cold overhead fluorescent lighting casting heavy shadows."
    },
    {
        "name": "t23_a1_13_abandoned_toyota_station_wagon",
        "act": 1,
        "sentences": "1.04#6",
        "desc": "Chiếc xe Toyota station wagon cũ bị bỏ lại trong bãi đất trống bụi bặm.",
        "prompt": "Dusty vintage 1970s Toyota station wagon parked in an abandoned suburban lot under dim orange sodium vapor streetlight, dusty rearview mirror, sinister desolate atmosphere."
    },
    {
        "name": "t23_a1_14_latent_fingerprint_dusting_macro",
        "act": 1,
        "sentences": "1.04#7",
        "desc": "Bụi bột pháp y nổi rõ dấu vân tay trên mặt gương chiếu hậu.",
        "prompt": "Forensic macro shot of black graphite fingerprint powder brushed onto glossy metallic car surface revealing clear ridge patterns, technical forensic lighting, stark contrast."
    },
    {
        "name": "t23_a1_15_afis_computer_terminal_1985",
        "act": 1,
        "sentences": "1.04#8",
        "desc": "Màn hình hệ thống máy tính AFIS đầu tiên của thập niên 1980 với đồ họa vân tay xanh lục.",
        "prompt": "Vintage 1980s mainframe computer terminal in dark police server room, monochrome green CRT screen displaying glowing fingerprint vector grids without any text, retro technological breakthrough."
    },
    {
        "name": "t23_a1_16_morning_newsstand_front_pages",
        "act": 1,
        "sentences": "1.06#1",
        "desc": "Sạp báo sáng ngày 31 tháng 8 năm 1985 tràn ngập hình truy nã kẻ sát nhân.",
        "prompt": "Metal outdoor newsstand rack on Los Angeles street at early grey dawn, stacked newspapers showing a dark high-contrast criminal silhouette mugshot, no text or words on papers."
    },
    {
        "name": "t23_a1_17_greyhound_bus_terminal_exhaust",
        "act": 1,
        "sentences": "1.06#2",
        "desc": "Bến xe buýt liên bang đầy khói xả và không khí ngột ngạt.",
        "prompt": "Desolate Greyhound bus station depot in downtown Los Angeles, heavy diesel exhaust smoke rising around vintage interstate bus, solitary silhouette walking on dirty platform pavement."
    },
    {
        "name": "t23_a1_18_convenience_store_shock_discovery",
        "act": 1,
        "sentences": "1.06#3",
        "desc": "Bên trong tiệm tạp hóa nhỏ, khoảnh khắc kẻ sát nhân đối diện bức ảnh truy nã chính mình.",
        "prompt": "Inside a gritty 1980s East LA neighborhood grocery store, rows of canned goods on metal shelves, newspaper rack by the counter, tense psychological chiaroscuro atmosphere."
    },
    {
        "name": "t23_a1_19_fleeing_suspect_running_street",
        "act": 1,
        "sentences": "1.06#4",
        "desc": "Bóng kẻ thủ ác tháo chạy thục mạng qua giao lộ đường phố.",
        "prompt": "Long shadow of a tall gaunt running figure cast across hot asphalt intersection, dramatic low-angle perspective, oppressive midday heat shimmering above pavement, noir dread."
    },
    {
        "name": "t23_a1_20_east_la_neighborhood_residents_unite",
        "act": 1,
        "sentences": "1.06#5–1.06#6",
        "desc": "Người dân khu phố Hubbard đồng lòng đổ ra đường chặn đứng kẻ ác.",
        "prompt": "Sunlit gritty East Los Angeles residential street with chain link fences and modest houses, group of determined community men emerging together onto street, high drama chiaroscuro."
    },
    {
        "name": "t23_a1_21_neighbor_witness_alert_moment",
        "act": 1,
        "sentences": "1.06#7–1.07#1",
        "desc": "Nhân chứng đứng bên hiên nhà kinh ngạc nhận diện kẻ bị truy nã.",
        "prompt": "Suburban porch steps of an East LA house, view looking out toward the sunny dusty street, unsettling realization, tense investigative realism, deep shadows under porch awning."
    },
    {
        "name": "t23_a1_22_carjacking_attempt_struggle",
        "act": 1,
        "sentences": "1.07#2–1.07#3",
        "desc": "Kẻ thủ ác cố giật cửa xe ô tô của phụ nữ trong cơn tuyệt vọng trốn chạy.",
        "prompt": "Vintage 1980s American sedan stopped on residential street, silhouette attempting to wrench open car door handle, panic and dynamic motion captured in graphic novel ink linework."
    },
    {
        "name": "t23_a1_23_community_mob_chase_hubbard",
        "act": 1,
        "sentences": "1.07#4–1.07#5",
        "desc": "Đám đông cư dân dũng cảm bao vây và rượt đuổi kẻ sát nhân trên đường phố.",
        "prompt": "Dramatic pursuit down an East LA alleyway, shadowy fleeing figure chased by determined crowd of neighborhood residents, intense dust and harsh California sunlight, noir contrast."
    },
    {
        "name": "t23_a1_24_subdued_on_concrete_sidewalk",
        "act": 1,
        "sentences": "1.07#6–1.07#7",
        "desc": "Kẻ ác bị người dân khống chế chặt chẽ trên vỉa hè bê tông.",
        "prompt": "Ground-level shot of cracked concrete sidewalk where an intruder is held down by strong hands, harsh sunlight cast against pavement, gritty forensic realism, stark ink shadows."
    },
    {
        "name": "t23_a1_25_police_cruisers_approaching_sirens",
        "act": 1,
        "sentences": "1.07#8–1.07#10",
        "desc": "Đoàn xe cảnh sát Los Angeles hối hả lao tới với đèn chớp nhấp nháy.",
        "prompt": "Flock of 1980s black-and-white police cruisers speeding down urban avenue, flashing emergency roof lights reflecting off dusty windshields, dramatic wide perspective."
    },
    {
        "name": "t23_a1_26_police_cordon_crowd_protection",
        "act": 1,
        "sentences": "1.09#1–1.09#3",
        "desc": "Lực lượng cảnh sát lập hàng rào che chắn áp giải nghi phạm giữa đám đông phẫn nộ.",
        "prompt": "Uniformed police officers shielding a handcuffed suspect silhouette from an agitated street crowd, bright sunlight contrasting with deep black uniform silhouettes, intense news atmosphere."
    },
    {
        "name": "t23_a1_27_police_station_back_entrance_escort",
        "act": 1,
        "sentences": "1.09#4–1.09#5",
        "desc": "Áp giải kẻ sát nhân qua cửa sau kiên cố của trụ sở cảnh sát.",
        "prompt": "Heavy reinforced steel security door at rear entrance of Los Angeles police precinct, officers ushering a handcuffed figure inside, gloomy industrial concrete walls."
    },
    {
        "name": "t23_a1_28_distorted_personality_dossier",
        "act": 1,
        "sentences": "1.09#6–1.09#7",
        "desc": "Hồ sơ phân tích sự méo mó trong cấu trúc nhân cách của kẻ phạm tội.",
        "prompt": "Investigative psychology file folder lying open on metal desk, clinical behavioral observation notes with blank lines, harsh overhead lamp, cold clinical tone."
    },
    {
        "name": "t23_a1_29_grieving_family_el_paso_shadows",
        "act": 1,
        "sentences": "1.09#8–1.09#9",
        "desc": "Gia đình tại El Paso bàng hoàng đau đớn trong căn nhà xơ xác.",
        "prompt": "Humble dimly lit kitchen in El Paso Texas, silhouette of an elderly person sitting with head in hands at worn wooden table, tragic sorrow, muted sepia and slate tones."
    },
    {
        "name": "t23_a1_30_interrogation_room_steel_chair",
        "act": 1,
        "sentences": "1.10#1–1.10#2",
        "desc": "Ghế sắt và bàn kim loại trong phòng hỏi cung lạnh lẽo đối diện điều tra viên.",
        "prompt": "Cold concrete interrogation room with bare light bulb hanging from wire, single metal table and bolted steel chairs, oppressive psychological standoff atmosphere."
    },
    {
        "name": "t23_a1_31_occult_symbolism_pentagram_dossier",
        "act": 1,
        "sentences": "1.10#3–1.10#5",
        "desc": "Bản báo cáo điều tra về các biểu tượng tà giáo và cơ chế ngắt kết nối đạo đức.",
        "prompt": "Evidence photograph folder documenting an inverted pentagram chalk sketch on dark wall, strictly no text or writing, forensic scale ruler, stark dark chiaroscuro lighting."
    },
    {
        "name": "t23_a1_32_hybristophilia_phenomenon_court_facade",
        "act": 1,
        "sentences": "1.10#6–1.11#4",
        "desc": "Mặt tiền Tòa Thượng thẩm Los Angeles nơi hiện tượng say mê tội phạm bùng nổ.",
        "prompt": "Massive granite facade and neoclassical pillars of Los Angeles Superior Courthouse under overcast slate grey sky, dark shadows falling across wide stone steps, unsettling historic tension."
    },

    # ==========================================
    # HỒI 2 (30 ảnh: t23_a2_01 đến t23_a2_30)
    # ==========================================
    {
        "name": "t23_a2_01_packed_courtroom_chaotic_atmosphere",
        "act": 2,
        "sentences": "2.02#1–2.02#2",
        "desc": "Phòng xử án đông nghẹt người dự khán trong không khí căng thẳng nghẹt thở.",
        "prompt": "Crowded 1980s courtroom gallery with wooden benches filled with spectator silhouettes, high vaulted ceiling, tall windows letting in pale diffused daylight, heavy tense atmosphere."
    },
    {
        "name": "t23_a2_02_women_in_black_groupies_gallery",
        "act": 2,
        "sentences": "2.02#3–2.02#5",
        "desc": "Nhóm phụ nữ trẻ mặc đồ đen trong phòng xử án dõi theo bị cáo say mê.",
        "prompt": "Group of young women in dark 1980s retro attire sitting in courtroom gallery benches, looking toward the defense table with whispering fascination, chiaroscuro shadow play."
    },
    {
        "name": "t23_a2_03_rockstar_aura_sunglasses_defense_table",
        "act": 2,
        "sentences": "2.04#1–2.04#3",
        "desc": "Chiếc kính râm đen đặt trên bàn luật sư bào chữa biểu thị thái độ ngạo mạn.",
        "prompt": "Dark aviator sunglasses resting on legal yellow notepads on polished mahogany defense table, harsh reflection in tinted lenses, cynical defiance, deep noir shadows."
    },
    {
        "name": "t23_a2_04_mailbags_filled_with_love_letters",
        "act": 2,
        "sentences": "2.04#4–2.04#5",
        "desc": "Các bao tải thư tình và bưu phẩm ái mộ gửi tới trại giam chất đống.",
        "prompt": "Heavy canvas postal mailbags overflowing with stacks of paper envelopes tied with pink ribbons in prison mail room, completely blank envelopes with no text, dim moody lighting."
    },
    {
        "name": "t23_a2_05_reverse_halo_effect_mirror_reflection",
        "act": 2,
        "sentences": "2.04#6",
        "desc": "Chiếc gương vỡ phản chiếu sự méo mó của hiệu ứng hào quang ngược.",
        "prompt": "Cracked vintage vanity mirror showing fractured reflections in dark room, symbolic representation of cognitive distortion and dangerous romanticization, muted amber tones."
    },
    {
        "name": "t23_a2_06_victims_families_agony_courtroom",
        "act": 2,
        "sentences": "2.04#7–2.04#8",
        "desc": "Thân nhân nạn nhân ngồi ở hàng ghế dự tòa trong nỗi đau đớn tột cùng.",
        "prompt": "Mournful silhouettes of family members seated in courtroom row, bowed heads, tightly clutched handkerchiefs, somber dignified grief under harsh judicial lighting."
    },
    {
        "name": "t23_a2_07_cruel_moral_paradox_bench",
        "act": 2,
        "sentences": "2.04#9–2.04#10",
        "desc": "Sự tương phản tàn nhẫn giữa đám đông hiếu kỳ và nỗi đau thân nhân nạn nhân.",
        "prompt": "Symbolic composition of courtroom aisle dividing two worlds: cold somber shadows of victims families on one side and blurred excited spectators on the other, deep noir."
    },
    {
        "name": "t23_a2_08_investigators_righteous_indignation",
        "act": 2,
        "sentences": "2.06#1–2.06#2",
        "desc": "Vẻ mặt nghiêm nghị phẫn nộ của các điều tra viên trước sự tôn sùng lệch lạc.",
        "prompt": "Back view of a sturdy detective in vintage suit standing at courtroom rail, looking toward defense bench with resolute stern posture, dramatic side chiaroscuro rim light."
    },
    {
        "name": "t23_a2_09_cowardly_predator_nocturnal_shadows",
        "act": 2,
        "sentences": "2.06#3–2.06#5",
        "desc": "Hình tượng kẻ săn mồi hèn nhát rình rập người yếu thế trong đêm.",
        "prompt": "Menacing shadowy figure creeping along an exterior dark brick wall under moonlight, predatory posture, strictly a distant silhouette, unsettling psychological dread."
    },
    {
        "name": "t23_a2_10_survivor_witness_stand_testimony",
        "act": 2,
        "sentences": "2.06#6–2.06#8",
        "desc": "Nhân chứng sống sót kiên cường bước lên bục khai báo vạch trần tội ác.",
        "prompt": "Empty wooden witness stand with microphone under dramatic beam of light, symbolizing heroic truth and dignity confronting criminal arrogance, solemn legal noir."
    },
    {
        "name": "t23_a2_11_dignity_restored_courtroom_gavel",
        "act": 2,
        "sentences": "2.06#9",
        "desc": "Búa công lý và hồ sơ vạch trần tội ác, phục hồi phẩm giá nạn nhân.",
        "prompt": "Solid dark wooden gavel resting on leather sound block on judge's elevated mahogany bench, legal dossiers, dignified solemn composition, deep rich shadows."
    },
    {
        "name": "t23_a2_12_doreen_lioy_writing_letters_desk",
        "act": 2,
        "sentences": "2.08#1–2.08#3",
        "desc": "Chiếc bàn làm việc của người phụ nữ viết hàng chục lá thư gửi vào buồng tử tù.",
        "prompt": "Vintage 1980s apartment desk with fountain pen, open blank parchment sheets, lit desk lamp casting warm circular pool of light against deep gloomy room shadows."
    },
    {
        "name": "t23_a2_13_san_quentin_prison_visiting_room_wedding",
        "act": 2,
        "sentences": "2.08#4",
        "desc": "Phòng thăm nuôi nhà tù San Quentin nơi diễn ra đám cưới kỳ dị năm 1996.",
        "prompt": "Cold institutional visiting room in maximum security prison, reinforced mesh divider, bare fluorescent tubes, institutional green painted walls, sterile unsettling atmosphere."
    },
    {
        "name": "t23_a2_14_gold_wedding_band_behind_glass",
        "act": 2,
        "sentences": "2.08#5",
        "desc": "Chiếc nhẫn cưới bằng vàng nằm cạnh vách ngăn kính nhà tù.",
        "prompt": "Single gold wedding band resting on steel counter next to thick scratched prison partition glass, stark symbolic contrast of naive romanticism and cold imprisonment."
    },
    {
        "name": "t23_a2_15_savior_complex_cognitive_trap",
        "act": 2,
        "sentences": "2.08#6–2.08#7",
        "desc": "Ảo tưởng người giải cứu như chiếc lồng kính giam hãm lý trí.",
        "prompt": "Metaphorical hourglass with dark sand running through, surrounded by scattered blank legal documents and fading memories, dark psychological chiaroscuro aesthetic."
    },
    {
        "name": "t23_a2_16_prosecution_forensic_evidence_exhibit",
        "act": 2,
        "sentences": "2.09#1–2.09#2",
        "desc": "Bàn trưng bày vật chứng pháp y đanh thép của cơ quan công tố.",
        "prompt": "Prosecution evidence table covered with sealed brown evidence bags, forensic fingerprint cards with blank labels, measuring rulers, solemn investigative rigor."
    },
    {
        "name": "t23_a2_17_avia_shoe_print_plaster_cast",
        "act": 2,
        "sentences": "2.09#2",
        "desc": "Bản thạch cao đúc khuôn dấu giày thể thao Avia cỡ 11.5 đặc trưng.",
        "prompt": "Forensic plaster cast of geometric athletic shoe sole tread pattern lying on lab black velvet tray, raking cross-lighting emphasizing tread ridges, high detail."
    },
    {
        "name": "t23_a2_18_modus_operandi_cut_telephone_wire",
        "act": 2,
        "sentences": "2.09#3",
        "desc": "Thủ đoạn MO: Đường dây điện thoại bên ngoài nhà bị cắt đứt trong đêm.",
        "prompt": "Exterior weathered stucco house corner showing a cleanly snipped black telephone wire dangling against wall, moonlight reflecting on cut copper ends, chilling calculated malice."
    },
    {
        "name": "t23_a2_19_psychological_signature_pentagram_wall",
        "act": 2,
        "sentences": "2.09#4–2.09#5",
        "desc": "Chữ ký tâm lý Signature: Biểu tượng ngôi sao năm cánh thô bạo trên tường.",
        "prompt": "Crime scene evidence photo of an ominous crude inverted pentagram drawn on cracked interior wallpaper, harsh forensic flashlight beam, stark black-and-white noir linework."
    },
    {
        "name": "t23_a2_20_jury_deliberation_closed_door",
        "act": 2,
        "sentences": "2.09#6",
        "desc": "Cánh cửa phòng nghị án của bồi thẩm đoàn đóng kín trong nhiều ngày.",
        "prompt": "Heavy oak jury room door firmly closed, frosted glass panel softly backlit from inside, brass doorknob, tense solemn silence in empty courthouse hallway."
    },
    {
        "name": "t23_a2_21_judge_michael_tynan_verdict_podium",
        "act": 2,
        "sentences": "2.10#1–2.10#2",
        "desc": "Bục thẩm phán tuyên đọc bản án tử hình cho 43 tội danh nghiêm trọng.",
        "prompt": "Elevated wooden judicial podium beneath California state seal silhouette, open sentencing order documents, solemn authority of law piercing through crime darkness."
    },
    {
        "name": "t23_a2_22_defiant_sneer_handcuffs_microphone",
        "act": 2,
        "sentences": "2.10#3",
        "desc": "Còng tay kim loại nặng và micro truyền thông ghi nhận lời ngông cuồng.",
        "prompt": "Heavy steel handcuffs resting on table in front of a battery of press microphones, harsh news flash reflections, capturing the cynical defiance of the convict."
    },
    {
        "name": "t23_a2_23_pathological_self_pity_collapse",
        "act": 2,
        "sentences": "2.10#4",
        "desc": "Sự sụp đổ thảm hại của cái tôi ái kỷ sau lớp vỏ bọc thách thức.",
        "prompt": "A crumbling stone statue head in deep pitch-black darkness, high contrast chiaroscuro cracks, symbolic of pathological narcissistic collapse beneath reality."
    },
    {
        "name": "t23_a2_24_san_quentin_death_row_cell_door",
        "act": 2,
        "sentences": "2.10#5",
        "desc": "Cánh cửa buồng biệt giam tử tù San Quentin đóng chặt bằng khóa sắt nặng.",
        "prompt": "Solid steel cell door with narrow viewing slit and heavy sliding food tray slot on maximum security Death Row corridor, cold green peeling paint, deep shadows."
    },
    {
        "name": "t23_a2_25_unanswered_psychological_questions",
        "act": 2,
        "sentences": "2.10#6–2.10#7",
        "desc": "Tập hồ sơ mở hé với những câu hỏi nhức nhối về sự lệch chuẩn tâm lý.",
        "prompt": "Open investigative dossier on dark wood desk with glowing lamp, blank case notes, magnifying glass resting on pages, deep contemplative investigative mood."
    },
    {
        "name": "t23_a2_26_defeated_predator_in_shadows",
        "act": 2,
        "sentences": "2.10#8–2.10#9",
        "desc": "Kẻ săn mồi bóng đêm hoàn toàn bất lực và chiến bại trước công lý.",
        "prompt": "Distant shadowy figure trapped behind heavy iron vertical bars, hands clutching bars in defeat, pool of cold moonlight on stone prison floor, stark noir."
    },
    {
        "name": "t23_a2_27_psychologists_dissecting_childhood",
        "act": 2,
        "sentences": "2.10#10",
        "desc": "Bàn làm việc của chuyên gia tâm lý học bắt tay vào giải phẫu quá khứ thủ ác.",
        "prompt": "Psychological researcher desk with vintage textbooks on abnormal psychology, medical journals, desk lamp casting warm beam across analytical charts, quiet scholarly tension."
    },
    {
        "name": "t23_a2_28_court_transcript_stacked_archives",
        "act": 2,
        "sentences": "2.10#10",
        "desc": "Các thùng lưu trữ hàng vạn trang biên bản phiên tòa kéo dài lịch sử.",
        "prompt": "Warehouse archive shelving lined with cardboard evidence boxes and numbered court transcript volumes, dim perspective vanishing into darkness, solemn justice."
    },
    {
        "name": "t23_a2_29_media_circus_cameras_scattered",
        "act": 2,
        "sentences": "2.02#5",
        "desc": "Chân máy ảnh và dây cáp truyền hình ngổn ngang sau cơn cuồng loạn đưa tin.",
        "prompt": "Empty courthouse steps after media frenzy, tangled electrical broadcast cables on stone steps, discarded coffee cups, desolate evening dusk over city."
    },
    {
        "name": "t23_a2_30_scales_of_justice_in_dim_light",
        "act": 2,
        "sentences": "2.09#1",
        "desc": "Cán cân công lý bằng đồng vững vàng trong ánh sáng trang nghiêm của phòng xử.",
        "prompt": "Classic bronze scales of justice standing balanced on dark wood podium, illuminated by single soft ray of pale light from high cathedral courthouse window."
    },

    # ==========================================
    # HỒI 3 (32 ảnh: t23_a3_01 đến t23_a3_32)
    # ==========================================
    {
        "name": "t23_a3_01_el_paso_desert_railroad_tracks",
        "act": 3,
        "sentences": "3.02#1–3.02#3",
        "desc": "Đường ray xe lửa hoang vắng cắt qua sa mạc El Paso Texas thập niên 1960.",
        "prompt": "Desolate dusty railroad tracks stretching toward arid horizon in El Paso Texas at bleak sunset, rusted rails, tumbleweeds, gloomy overcast sky, harsh retro tones."
    },
    {
        "name": "t23_a3_02_three_pillars_toxic_criminology",
        "act": 3,
        "sentences": "3.02#4–3.02#6",
        "desc": "Ba yếu tố độc hại: Chấn thương thực thể, bạo hành gia đình và bình thường hóa tội ác.",
        "prompt": "Conceptual noir composition of three dark geometric monoliths standing on cracked barren desert ground, stormy ominous thunderclouds overhead, symbolic Chiaroscuro."
    },
    {
        "name": "t23_a3_03_childhood_head_trauma_dresser",
        "act": 3,
        "sentences": "3.03#1–3.03#2",
        "desc": "Chiếc tủ gỗ nặng đổ sập và tai nạn thời thơ ấu gây chấn thương não bộ.",
        "prompt": "Vintage 1960s wooden bedroom dresser overturned on dusty floorboards, scattered vintage children toys, harsh beam of light through doorway, dramatic ink contrast."
    },
    {
        "name": "t23_a3_04_brain_ct_scan_frontal_temporal_lobe",
        "act": 3,
        "sentences": "3.03#3–3.03#4",
        "desc": "Phim chụp cộng hưởng từ / cắt lớp sọ não với vùng thùy trán bị tổn thương.",
        "prompt": "Medical lightboard displaying vintage neurological cranial X-ray films showing frontal lobe structure, clinical dark examination room, cold monochrome glow."
    },
    {
        "name": "t23_a3_05_railroad_worker_heavy_leather_belt",
        "act": 3,
        "sentences": "3.03#5",
        "desc": "Chiếc thắt lưng da nặng của người cha tượng trưng cho bạo hành gia đình.",
        "prompt": "Heavy cracked leather workman belt coiled on a rough wooden bench beside iron railroad spikes, dim single overhead light bulb, grim domestic abuse symbolism."
    },
    {
        "name": "t23_a3_06_cemetery_tombstones_sleeping_hiding",
        "act": 3,
        "sentences": "3.03#6",
        "desc": "Khu nghĩa trang El Paso nơi cậu bé trốn ngủ qua đêm để tránh đòn roi.",
        "prompt": "Gloomy overgrown desert cemetery at midnight, weathered stone tombstones casting long eerie shadows under pale moon, thorny desert brush, unsettling isolation."
    },
    {
        "name": "t23_a3_07_cousin_war_photos_normalization",
        "act": 3,
        "sentences": "3.03#7–3.03#8",
        "desc": "Các bức ảnh tư liệu cũ thời chiến của người anh họ Miguel bình thường hóa bạo lực.",
        "prompt": "Scattered vintage polaroid photographs lying on stained wooden table, showing blurred military jungle foliage silhouettes, completely blank borders, grim history."
    },
    {
        "name": "t23_a3_08_shattered_domestic_shooting_trauma",
        "act": 3,
        "sentences": "3.03#9–3.03#10",
        "desc": "Kỷ vật vỡ nát biểu thị sang chấn tâm lý năm 13 tuổi chứng kiến bạo lực cực đoan.",
        "prompt": "Shattered ceramic coffee mug spilled on linoleum kitchen floor, bullet hole in weathered wooden wall casting thin ray of blinding light, intense psychological trauma."
    },
    {
        "name": "t23_a3_09_empathy_deficit_frozen_mask",
        "act": 3,
        "sentences": "3.03#11–3.03#12",
        "desc": "Sự khuyết tật thấu cảm cảm xúc: Mặt nạ đá lạnh lẽo vô cảm trước nỗi đau.",
        "prompt": "Chiseled stone mask half buried in black desert sand, cold emotionless gaze, raking sidelight creating pitch-black shadow on one half, psychological deficit metaphor."
    },
    {
        "name": "t23_a3_10_skid_row_los_angeles_hotel_corridor",
        "act": 3,
        "sentences": "3.04#1–3.04#2",
        "desc": "Hành lang khách sạn rẻ tiền khu Skid Row nơi Ramirez sống lang thang nghiện ngập.",
        "prompt": "Dimly lit decaying hotel hallway in 1980s downtown LA Skid Row, flickering yellowish incandescent bulb, peeling floral wallpaper, cracked linoleum floor, desolate dread."
    },
    {
        "name": "t23_a3_11_moral_disengagement_pentagram_sketch",
        "act": 3,
        "sentences": "3.04#3",
        "desc": "Bản phác họa tà giáo như một cơ chế ngắt kết nối lương tri để tự bào chữa.",
        "prompt": "Charcoal sketch of an esoteric pentagram drawn on rough brown cardboard paper, burning candle casting wavering noir shadows, psychological rationalization theme."
    },
    {
        "name": "t23_a3_12_hybristophilia_concept_ancient_greek_roots",
        "act": 3,
        "sentences": "3.04#4–3.05#1",
        "desc": "Khái niệm Hybristophilia: Nguồn gốc cổ xưa và sự lệch lạc cảm xúc.",
        "prompt": "Ancient weathered classical parchment scroll unrolled on scholar desk under candle light, ink bottle and quill, academic criminology and psychiatric history atmosphere."
    },
    {
        "name": "t23_a3_13_two_subtypes_active_passive_scales",
        "act": 3,
        "sentences": "3.05#2–3.05#3",
        "desc": "Phân chia hai phân nhóm: Thể hung hăng chủ động và Thể thụ động cứu chuộc.",
        "prompt": "Abstract psychological diagram on chalkboard: two contrasting silhouettes facing away from each other, clean chalk lines without any written text, intellectual noir."
    },
    {
        "name": "t23_a3_14_bonnie_and_clyde_car_bullet_holes",
        "act": 3,
        "sentences": "3.05#4",
        "desc": "Chiếc xe hơi thời Bonnie & Clyde biểu thị thể hung hăng đồng lõa chủ động.",
        "prompt": "Vintage 1930s Ford V8 coupe silhouette parked by dusty country road, bullet holes in steel bodywork, retro sepia and black ink linework, historic criminal folklore."
    },
    {
        "name": "t23_a3_15_passive_savior_longing_window",
        "act": 3,
        "sentences": "3.05#5–3.05#6",
        "desc": "Thể thụ động cứu chuộc: Người phụ nữ đứng bên cửa sổ chìm trong ảo tưởng cảm hóa.",
        "prompt": "Back view of a solitary woman standing at rain-streaked apartment window, looking out into dark urban night, silhouette clutching a letter, melancholic longing."
    },
    {
        "name": "t23_a3_16_dangerous_fantasy_cage_rescue",
        "act": 3,
        "sentences": "3.05#7–3.05#8",
        "desc": "Niềm tin ngây thơ rằng tình yêu của mình sẽ biến con mãnh thú thành cừu non.",
        "prompt": "Metaphorical ornate iron cage with door slightly ajar, empty inside except for a single withered white rose resting on iron floor, dark chiaroscuro symbolism."
    },
    {
        "name": "t23_a3_17_cognitive_dissonance_split_portrait",
        "act": 3,
        "sentences": "3.05#9–3.05#10",
        "desc": "Cơ chế bất hòa nhận thức: Bức chân dung bị xé làm đôi giữa thực tại và ảo ảnh.",
        "prompt": "A monochrome photograph torn down the center, one half showing dark crime scene tape and the other half a soft blurred romantic silhouette, deep psychological split."
    },
    {
        "name": "t23_a3_18_compartmentalization_mental_island",
        "act": 3,
        "sentences": "3.05#11–3.05#12",
        "desc": "Chia ngăn nhận thức: Ốc đảo tâm lý cô lập để trốn tránh sự thật tàn nhẫn.",
        "prompt": "A tiny solitary barren rock island surrounded by dark turbulent churning ocean waves under a pitch-black night sky, symbolic of extreme psychological denial."
    },
    {
        "name": "t23_a3_19_surrogate_narcissistic_satisfaction",
        "act": 3,
        "sentences": "3.06#1–3.06#2",
        "desc": "Thỏa mãn ái kỷ thay thế: Cảm giác đặc biệt khi gắn kết với kẻ sát nhân nổi tiếng.",
        "prompt": "A lone velvet theatre chair illuminated by a single harsh spotlight in an empty auditorium, dramatic high-contrast noir lighting, theme of illusory importance."
    },
    {
        "name": "t23_a3_20_media_spotlight_borrowed_identity",
        "act": 3,
        "sentences": "3.06#3–3.06#4",
        "desc": "Danh tính vay mượn từ ánh đèn flash truyền thông để khỏa lấp tự ti.",
        "prompt": "Silhouette of a person walking along a red velvet rope cordon, blinded by dazzling camera flash bulbs bursting in darkness, hollow fleeting fame."
    },
    {
        "name": "t23_a3_21_safe_romance_behind_prison_bars",
        "act": 3,
        "sentences": "3.07#1–3.07#2",
        "desc": "Nghịch lý an toàn: Yêu kẻ bị giam cầm vĩnh viễn mang lại sự kiểm soát không rủi ro.",
        "prompt": "Rows of heavy steel prison bars bathed in cool moonlight, clean and uncluttered space beyond, paradox of safety through total physical confinement."
    },
    {
        "name": "t23_a3_22_controlled_letters_supervised_visits",
        "act": 3,
        "sentences": "3.07#3–3.07#4",
        "desc": "Mối quan hệ được kiểm soát một chiều qua thư từ và giờ thăm nuôi giám sát.",
        "prompt": "Neat stack of sealed paper letters tied with string beside a vintage prison acoustic visiting telephone handset resting on steel shelf, quiet order."
    },
    {
        "name": "t23_a3_23_pop_culture_glorification_bad_boy",
        "act": 3,
        "sentences": "3.07#5",
        "desc": "Văn hóa đại chúng tiếp tay lãng mạn hóa kẻ bất hảo thành hình tượng nổi loạn.",
        "prompt": "Retro 1980s television set glowing in dark living room, distorted monochrome broadcast signal screen, flickering light casting long shadows on wall."
    },
    {
        "name": "t23_a3_24_grave_insult_to_victims_memory",
        "act": 3,
        "sentences": "3.07#6–3.07#7",
        "desc": "Sự thần tượng hóa tội ác là nỗi xúc phạm nghiêm trọng đối với vong linh nạn nhân.",
        "prompt": "Dignified marble memorial stone plaque surrounded by solemn autumn leaves, soft respectful sidelight, quiet reverence, moral gravity."
    },
    {
        "name": "t23_a3_25_dissecting_toxic_seeds_wake_up_call",
        "act": 3,
        "sentences": "3.07#8–3.08#1",
        "desc": "Tiếng chuông cảnh tỉnh giải phẫu mầm mống tâm lý trước khi di căn thành nguy hiểm.",
        "prompt": "Ancient bronze alarm bell hanging in clock tower silhouette against stormy twilight sky, striking hammer poised, symbolic wake-up call to society."
    },
    {
        "name": "t23_a3_26_crime_as_toxic_social_virus",
        "act": 3,
        "sentences": "3.08#2–3.08#3",
        "desc": "Tội ác lây lan như thứ virus độc hại xâm nhập vào nhận thức cộng đồng.",
        "prompt": "Forensic laboratory microscope slide glowing under ultraviolet light, abstract crystalline virus-like patterns forming in darkness, clinical noir."
    },
    {
        "name": "t23_a3_27_peeling_away_false_mythology",
        "act": 3,
        "sentences": "3.08#4–3.08#5",
        "desc": "Thời gian bóc trần lớp vỏ bọc huyền thoại giả tạo của quỷ vương bóng đêm.",
        "prompt": "Weathered poster tearing off a decaying brick wall, revealing cracked crumbling concrete beneath, temporal decay, peeling away illusions."
    },
    {
        "name": "t23_a3_28_childhood_backyard_dusty_swing",
        "act": 3,
        "sentences": "3.03#2",
        "desc": "Chiếc xích đu kim loại cũ rỉ sét đung đưa trong gió sa mạc El Paso.",
        "prompt": "Empty rusted iron chain playground swing swaying in dry desert wind in overgrown backyard, harsh sun-bleached ground, eerie childhood memory."
    },
    {
        "name": "t23_a3_29_neurological_impulse_control_aberration",
        "act": 3,
        "sentences": "3.03#4",
        "desc": "Biểu đồ xung động thần kinh bị rối loạn biểu hiện qua nét vẽ noir.",
        "prompt": "Vintage EEG brainwave polygraph paper scroll unfurling on forensic table, jagged black ink spike lines showing epileptic discharge, scientific documentary realism."
    },
    {
        "name": "t23_a3_30_psychological_bookshelf_archives",
        "act": 3,
        "sentences": "3.08#1",
        "desc": "Kệ sách chuyên ngành tâm thần học và phân tích hành vi tội phạm.",
        "prompt": "Tall dark mahogany bookshelf filled with thick leather-bound psychiatric case studies and DSM reference volumes, library ladder in shadows."
    },
    {
        "name": "t23_a3_31_symbolic_crossroads_moral_choice",
        "act": 3,
        "sentences": "3.08#3",
        "desc": "Ngã ba đường trong đêm biểu thị ranh giới đạo đức của cộng đồng.",
        "prompt": "Lonely asphalt crossroads in the desert under starless midnight sky, cracked road surface, distant telephone pole silhouettes, existential moral boundary."
    },
    {
        "name": "t23_a3_32_san_quentin_aerial_fortress_dusk",
        "act": 3,
        "sentences": "3.08#5",
        "desc": "Pháo đài San Quentin sừng sững bên vịnh biển khi hoàng hôn buông xuống.",
        "prompt": "Wide exterior view of San Quentin State Prison fortress towers perched on rocky promontory over dark churning ocean water at desolate dusk, heavy grey mist."
    },

    # ==========================================
    # HỒI 4 (34 ảnh: t23_a4_01 đến t23_a4_34)
    # ==========================================
    {
        "name": "t23_a4_01_san_quentin_death_row_exterior_wall",
        "act": 4,
        "sentences": "4.02#1–4.02#2",
        "desc": "Bức tường đá kiên cố của nhà tù San Quentin giam giữ tử tù suốt 24 năm.",
        "prompt": "Massive granite exterior prison wall with barbed wire fencing along the parapet, guard tower silhouette against pale grey sky, stark fortress noir."
    },
    {
        "name": "t23_a4_02_endless_letters_fan_mail_cell",
        "act": 4,
        "sentences": "4.02#3–4.02#4",
        "desc": "Những bức thư ái mộ chất đầy góc buồng giam nuôi dưỡng cái tôi ái kỷ.",
        "prompt": "Interior corner of narrow concrete prison cell, piles of paper envelopes sitting on metal shelf beside steel bunk bed, dim light bulb casting harsh shadows."
    },
    {
        "name": "t23_a4_03_relentless_march_of_time_bars",
        "act": 4,
        "sentences": "4.02#5–4.02#6",
        "desc": "Sự lạnh lùng của thời gian và song sắt bóc trần sự thật về tuổi trẻ qua đi.",
        "prompt": "Close-up of heavy rusted iron prison bars with peeling dark paint, shaft of cold dust-mote filled light angling through narrow window slit, passage of decades."
    },
    {
        "name": "t23_a4_04_frail_decaying_inmate_cot",
        "act": 4,
        "sentences": "4.02#7",
        "desc": "Chiếc giường sắt buồng giam với kẻ sát nhân suy kiệt vì bệnh tật.",
        "prompt": "Thin institutional mattress on bolted iron bed frame in narrow cell, rough wool blanket, desolate silence of an aging terminal inmate, grim reality."
    },
    {
        "name": "t23_a4_05_doreen_lioy_marriage_collapse_rings",
        "act": 4,
        "sentences": "4.04#1",
        "desc": "Sự tan vỡ trong im lặng của cuộc hôn nhân tù tội từng tốn nhiều giấy mực.",
        "prompt": "A discarded gold ring lying abandoned on cold cracked linoleum floor, harsh raking light, end of an obsessive illusion, somber noir aesthetic."
    },
    {
        "name": "t23_a4_06_dna_technology_breakthrough_2009",
        "act": 4,
        "sentences": "4.04#2–4.04#3",
        "desc": "Bước ngoặt công nghệ ADN năm 2009 liên kết trực tiếp với vụ án mạng 1984.",
        "prompt": "Modern forensic laboratory illuminated by cool blue and white lights, automated genetic sequencer carousel with sample test tubes, objective scientific truth."
    },
    {
        "name": "t23_a4_07_irrefutable_evidence_child_victim",
        "act": 4,
        "sentences": "4.04#4",
        "desc": "Chứng cứ không thể chối cãi làm sụp đổ hoàn toàn ảo tưởng cảm hóa.",
        "prompt": "Forensic lab evidence binder resting open under bright desk light, DNA autoradiogram strip showing matching band lines, undeniable cold reality."
    },
    {
        "name": "t23_a4_08_silent_departure_severed_ties",
        "act": 4,
        "sentences": "4.04#5–4.04#6",
        "desc": "Sự rút lui trong im lặng tuyệt đối của người phụ nữ từng thề yêu trọn đời.",
        "prompt": "Silhouetted figure of a woman walking away down long empty prison corridor toward exit doors, long lonely shadow stretching behind on shiny floor."
    },
    {
        "name": "t23_a4_09_moral_trauma_self_disgust_shattered",
        "act": 4,
        "sentences": "4.04#7–4.04#8",
        "desc": "Cơn sang chấn đạo đức dữ dội và cảm giác tự ghê tởm vì đã dung dưỡng kẻ thủ ác.",
        "prompt": "Dramatic symbolic shot of a delicate porcelain cup shattered into jagged fragments on black granite, stark chiaroscuro lighting, moral collapse."
    },
    {
        "name": "t23_a4_10_removed_wedding_ring_bitter_penance",
        "act": 4,
        "sentences": "4.04#9",
        "desc": "Chiếc nhẫn cưới bị tháo bỏ, sự dằn vặt và hối hận muộn màng trước dư luận.",
        "prompt": "Empty pale hand resting on wooden table showing faint pale indentation mark where a wedding band used to be, solemn quiet regret, moody lighting."
    },
    {
        "name": "t23_a4_11_detectives_stern_reflection_decades_later",
        "act": 4,
        "sentences": "4.06#1–4.06#2",
        "desc": "Điều tra viên kỳ cựu nhìn lại hồ sơ vụ án sau nhiều thập kỷ với ánh mắt cương trực.",
        "prompt": "Elderly detective silhouette standing before tall office window overlooking contemporary city skyline, hands clasped behind back, unwavering dedication."
    },
    {
        "name": "t23_a4_12_unmasking_cowardly_opportunist",
        "act": 4,
        "sentences": "4.06#3–4.06#5",
        "desc": "Lột bỏ mặt nạ: Bản chất thật sự chỉ là một kẻ hèn hạ rình rập người yếu thế.",
        "prompt": "A grotesque theatrical mask lying broken on damp pavement under streetlamp, unmasking criminal cowardice, raw graphic novel linework."
    },
    {
        "name": "t23_a4_13_insult_to_justice_and_victims",
        "act": 4,
        "sentences": "4.06#6–4.06#8",
        "desc": "Thông điệp đanh thép: Thần tượng hóa tội ác là sự sỉ nhục vong linh nạn nhân.",
        "prompt": "Courthouse interior marble memorial wall engraved with solemn wreath silhouette, dignified quiet reverence, sharp chiaroscuro contrast."
    },
    {
        "name": "t23_a4_14_marin_general_hospital_exterior_dawn",
        "act": 4,
        "sentences": "4.08#1",
        "desc": "Bệnh viện Đa khoa Marin trong buổi sáng ngày 7 tháng 6 năm 2013.",
        "prompt": "Exterior view of Marin General Hospital building at chilly overcast grey dawn, emergency bay signs dimly glowing, wet pavement, somber finality."
    },
    {
        "name": "t23_a4_15_terminal_illness_hospital_room_monitor",
        "act": 4,
        "sentences": "4.08#2–4.08#3",
        "desc": "Căn phòng bệnh viện có lính canh, màn hình y tế đo nhịp tim phẳng lặng.",
        "prompt": "Hospital secure wing room with barred window, medical heart monitor screen showing flat baseline line, empty beside guarded bed, sterile cold atmosphere."
    },
    {
        "name": "t23_a4_16_nature_and_oblivion_final_judgment",
        "act": 4,
        "sentences": "4.08#4–4.08#5",
        "desc": "Bản án của tự nhiên và sự lãng quên của xã hội định đoạt kết cục.",
        "prompt": "Desolate cemetery grounds with swirling dry autumn leaves sweeping across empty grass paths, stark bare trees against bleak overcast sky."
    },
    {
        "name": "t23_a4_17_solitary_unclaimed_remains_cremation",
        "act": 4,
        "sentences": "4.08#6–4.08#7",
        "desc": "Hũ tro cốt không người thân nhận lãnh, kết cục thảm hại của kẻ từng được tung hô.",
        "prompt": "Simple plain metallic urn sitting on stainless steel shelf in county morgue storage vault, cold clinical lighting, absolute abandonment and oblivion."
    },
    {
        "name": "t23_a4_18_court_reporter_retrospective_desk",
        "act": 4,
        "sentences": "4.09#1–4.09#2",
        "desc": "Nhà báo theo dõi phiên tòa năm xưa ngồi bên chiếc máy đánh chữ cũ hồi tưởng.",
        "prompt": "Vintage manual typewriter on dark oak journalist desk, rolled typing paper, scattered press passes, warm desk lamp casting circular beam, nostalgic solemnity."
    },
    {
        "name": "t23_a4_19_superficial_dark_glamour_fading",
        "act": 4,
        "sentences": "4.09#3–4.09#4",
        "desc": "Vẻ hào nhoáng bóng tối bề ngoài chỉ là chiếc mặt nạ che đậy nhân cách lệch lạc.",
        "prompt": "Fading black-and-white tabloid newspaper clipping yellowing under cracked glass frame, superficial criminal glamour dissolving into dust."
    },
    {
        "name": "t23_a4_20_moral_blindspot_mass_psychosis",
        "act": 4,
        "sentences": "4.09#5–4.09#6",
        "desc": "Điểm mù nhận thức và sự hoang tưởng tập thể của những người mê muội.",
        "prompt": "Abstract artistic depiction of silhouettes standing blindly in dense fog, reaching toward a dim flickering lamp, psychological blindness metaphor."
    },
    {
        "name": "t23_a4_21_enduring_courage_community_unity",
        "act": 4,
        "sentences": "4.09#7–4.09#9",
        "desc": "Sức mạnh trường tồn thuộc về lòng quả cảm của nạn nhân và sự đoàn kết khu phố.",
        "prompt": "Warm low-angle view of suburban neighborhood front porches with lit porch lamps, tree-lined quiet street, peaceful restored community harmony."
    },
    {
        "name": "t23_a4_22_media_sensation_dissolving_into_air",
        "act": 4,
        "sentences": "4.09#10–4.09#11",
        "desc": "Cơn sốt truyền thông giật gân tan biến, chỉ còn lại bài học cảnh tỉnh sâu sắc.",
        "prompt": "Scattered loose pages of old newsprint blowing away down an empty windy street at twilight, vanishing into shadows, moral documentary conclusion."
    },
    {
        "name": "t23_a4_23_dark_chapter_officially_closed",
        "act": 4,
        "sentences": "4.10#1–4.10#2",
        "desc": "Cái chết của Richard Ramirez chính thức khép lại chương đen tối trong lịch sử điều tra.",
        "prompt": "Thick heavy leather-bound criminal case ledger closing firmly on wooden desk, puff of dust rising into shaft of light, definitive judicial closure."
    },
    {
        "name": "t23_a4_24_criminology_casebook_permanent_dossier",
        "act": 4,
        "sentences": "4.10#3–4.10#4",
        "desc": "Hồ sơ được lưu trữ vĩnh viễn trong giáo trình tội phạm học như một nghiên cứu điển hình.",
        "prompt": "FBI behavioral science case study volume shelved alongside institutional forensic textbooks, dark academic research office, quiet solemn scholarship."
    },
    {
        "name": "t23_a4_25_vigilance_and_community_solidarity",
        "act": 4,
        "sentences": "4.10#5–4.10#6",
        "desc": "Cảnh giác và sự đoàn kết xóm giềng là vũ khí mạnh nhất đẩy lùi bóng tối.",
        "prompt": "Solid interlocking iron chain links resting on heavy oak police precinct table, symbol of neighborhood solidarity and collective vigilance, high contrast."
    },
    {
        "name": "t23_a4_26_hybristophilia_psychiatry_dsm_manual",
        "act": 4,
        "sentences": "4.11#1–4.11#2",
        "desc": "Cẩm nang chẩn đoán tâm thần học DSM phân tích về lệch lạc cảm xúc say mê tội ác.",
        "prompt": "Open diagnostic manual of mental disorders on clinical desk, glasses resting on open page, clinical examination room in soft monochrome lighting."
    },
    {
        "name": "t23_a4_27_romanticizing_evil_toxic_culture",
        "act": 4,
        "sentences": "4.11#3",
        "desc": "Văn hóa độc hại lãng mạn hóa cái ác dẫn dắt con người vào những cái bẫy cảm xúc.",
        "prompt": "A poisoned apple resting on a silver platter in deep chiaroscuro shadows, symbolic of alluring toxic romantic illusions, rich noir contrast."
    },
    {
        "name": "t23_a4_28_moral_resilience_compassionate_clarity",
        "act": 4,
        "sentences": "4.11#4–4.11#5",
        "desc": "Bảo vệ sự tỉnh táo nhận thức và xây dựng hệ thống miễn dịch tâm lý cộng đồng.",
        "prompt": "A sturdy lighthouse beam slicing cleanly through pitch-black stormy ocean fog, illuminating safe rocky coast, metaphor for moral clarity."
    },
    {
        "name": "t23_a4_29_summer_1985_fading_into_history",
        "act": 4,
        "sentences": "4.12#1",
        "desc": "Mùa hè 1985 đã lùi xa vào dĩ vãng nhưng những bài học vẫn còn nguyên giá trị.",
        "prompt": "Faded vintage sepia postcard of Los Angeles highway in 1985 resting on modern dark mahogany desk, transition of time, quiet historical reflection."
    },
    {
        "name": "t23_a4_30_psychological_mirror_human_nature",
        "act": 4,
        "sentences": "4.12#2–4.12#3",
        "desc": "Hồ sơ vụ án là tấm gương phản chiếu những góc khuất bất an trong bản tính con người.",
        "prompt": "Antique oval mirror in ornate dark frame reflecting a shadowy silhouette contemplating their own reflection, psychological depth and introspection."
    },
    {
        "name": "t23_a4_31_san_quentin_empty_corridor_night",
        "act": 4,
        "sentences": "4.02#6",
        "desc": "Hành lang tử tù vắng lặng lúc nửa đêm với ánh đèn vàng hiu hắt.",
        "prompt": "Empty maximum security prison corridor at night, long perspective vanishing toward barred gates, wet mop reflections on concrete floor."
    },
    {
        "name": "t23_a4_32_dna_evidence_box_archive_vault",
        "act": 4,
        "sentences": "4.04#3",
        "desc": "Hộp lưu trữ mẫu bằng chứng sinh học trong kho lưu trữ niêm phong.",
        "prompt": "Metal cold-storage specimen lockbox in police evidence depository, frost forming along steel edges, forensic chain of custody tags."
    },
    {
        "name": "t23_a4_33_empty_courtroom_bench_silence",
        "act": 4,
        "sentences": "4.06#7",
        "desc": "Ghế gỗ phòng xử án trống trải trong tĩnh lặng sau khi phiên tòa kết thúc.",
        "prompt": "Rows of polished empty oak courtroom benches viewed from above, late afternoon sunlight fading through high windows, profound quiet."
    },
    {
        "name": "t23_a4_34_amber_eyes_dossier_seal_closing",
        "act": 4,
        "sentences": "4.12#3",
        "desc": "Dấu niêm phong sáp đỏ của hồ sơ Amber Eyes sẵn sàng chuyển sang phần đúc kết.",
        "prompt": "Thick manila dossier binder stamped with dark red wax seal and black ink insignia, lying on antique wooden desk beside brass desk lamp."
    },

    # ==========================================
    # HỒI 5 (22 ảnh: t23_a5_01 đến t23_a5_22)
    # ==========================================
    {
        "name": "t23_a5_01_psychological_anatomy_overview",
        "act": 5,
        "sentences": "5.02#1–5.02#3",
        "desc": "Giải phẫu tâm lý học tội phạm: Bài học cảnh tỉnh về sự tôn nghiêm của công lý.",
        "prompt": "High-angle view of an investigator's analytical desk, case notes, analytical psychological diagram, brass calipers, dignified intellectual atmosphere."
    },
    {
        "name": "t23_a5_02_debunking_false_glamour_truth",
        "act": 5,
        "sentences": "5.02#4–5.02#7",
        "desc": "Bóc trần sự thật: Cái ác không bao giờ là biểu tượng quyến rũ.",
        "prompt": "A stage spotlight shining onto bare dusty wooden floorboards where an ornate mask has shattered, unvarnished truth, dramatic chiaroscuro."
    },
    {
        "name": "t23_a5_03_investigators_safety_security_message",
        "act": 5,
        "sentences": "5.03#1–5.03#2",
        "desc": "Thông điệp an toàn điều tra: Kiểm soát hệ thống an ninh gia đình vững chắc.",
        "prompt": "Sturdy solid brass front door lock mechanism shown from interior, reinforced deadbolt securely engaged, warm and safe home interior."
    },
    {
        "name": "t23_a5_04_neighborhood_vigilance_mutual_support",
        "act": 5,
        "sentences": "5.03#3–5.03#4",
        "desc": "Sự cảnh giác và tương trợ xóm giềng là lá chắn an toàn tối thượng.",
        "prompt": "Suburban street at night with lit porch lights glowing reassuringly from house to house, calm peaceful neighborhood solidarity, soft noir."
    },
    {
        "name": "t23_a5_05_psychological_roots_inner_emptiness",
        "act": 5,
        "sentences": "5.04#1–5.04#3",
        "desc": "Căn nguyên say mê độc hại xuất phát từ sự thiếu hụt giá trị tự thân.",
        "prompt": "Conceptual shot of a solitary silhouette sitting before an empty picture frame in a shadowed room, longing for identity, moody slate palette."
    },
    {
        "name": "t23_a5_06_emotional_boundaries_self_respect",
        "act": 5,
        "sentences": "5.04#4–5.04#6",
        "desc": "Thiết lập ranh giới cảm xúc lành mạnh và trân trọng giá trị tự thân.",
        "prompt": "A sturdy clean stone boundary marker standing in green meadow under clear morning light, metaphor for emotional self-protection and healthy boundaries."
    },
    {
        "name": "t23_a5_07_complicity_vs_redemption_warning",
        "act": 5,
        "sentences": "5.04#7",
        "desc": "Bao che cho cái ác không phải là cứu rỗi mà là sự đồng lõa tự hủy hoại.",
        "prompt": "Hands letting go of a heavy black iron anchor slipping into deep dark waters, symbolic release from toxic complicity, dramatic chiaroscuro."
    },
    {
        "name": "t23_a5_08_four_redflags_survival_guide_intro",
        "act": 5,
        "sentences": "5.05#1",
        "desc": "Giới thiệu 4 cảnh báo đỏ nhận diện hội chứng say mê độc hại.",
        "prompt": "Forensic survival dossier opened on desk, four distinct red wax seals placed neatly in a row on parchment, dignified documentary design."
    },
    {
        "name": "t23_a5_09_redflag1_attraction_to_aggression",
        "act": 5,
        "sentences": "5.05#2–5.05#3",
        "desc": "Cảnh báo đỏ 1: Bị thu hút bởi sự hung hăng, ngạo mạn hoặc quá khứ bất hảo.",
        "prompt": "Dramatic symbolic scene: a jagged rusty combat blade reflecting menacing red sidelight against pitch-black shadows, danger sign, high tension."
    },
    {
        "name": "t23_a5_10_redflag1_brutality_vs_masculinity",
        "act": 5,
        "sentences": "5.05#4–5.05#5",
        "desc": "Đừng nhầm lẫn sự thô bạo với bản lĩnh hay sự cuốn hút bí ẩn.",
        "prompt": "A cracking mirror reflecting a distorted aggressive silhouette, contrasting with a calm steady hand holding an umbrella in rain, noir allegory."
    },
    {
        "name": "t23_a5_11_redflag2_savior_complex_fantasy",
        "act": 5,
        "sentences": "5.05#6–5.05#7",
        "desc": "Cảnh báo đỏ 2: Ảo tưởng người giải cứu, tin tình yêu có thể cảm hóa kẻ ác.",
        "prompt": "A delicate paper origami boat floating toward dangerous dark whirlpool rapids, symbolic of naive romantic rescue fantasies, dramatic water reflections."
    },
    {
        "name": "t23_a5_12_redflag2_companion_not_savior",
        "act": 5,
        "sentences": "5.05#8–5.05#9",
        "desc": "Bạn là người đồng hành tìm sẻ chia, chứ không phải vị cứu tinh nhân cách.",
        "prompt": "Two solid wooden armchairs facing each other by a fireplace in quiet respectful equality, warm amber glow against dark walls, healthy relationship."
    },
    {
        "name": "t23_a5_13_redflag3_justifying_bad_behavior",
        "act": 5,
        "sentences": "5.05#10–5.05#11",
        "desc": "Cảnh báo đỏ 3: Thói quen biện minh, bao che cho hành vi sai trái của đối phương.",
        "prompt": "A hand attempting to smooth over cracked jagged dry earth, unable to hide deep fissures, metaphor for futile excuses for toxic abuse."
    },
    {
        "name": "t23_a5_14_redflag3_misplaced_forgiveness_complicity",
        "act": 5,
        "sentences": "5.05#12–5.05#13",
        "desc": "Lòng vị tha đặt nhầm chỗ là sự dung dưỡng cho cái xấu leo thang.",
        "prompt": "Scales of justice severely tilted by dark heavy stone on one plate, casting stark black shadow on judicial bench, compromise of moral boundaries."
    },
    {
        "name": "t23_a5_15_redflag4_isolation_from_loved_ones",
        "act": 5,
        "sentences": "5.05#14–5.05#15",
        "desc": "Cảnh báo đỏ 4: Tự cô lập bản thân khỏi gia đình, bạn bè để bảo vệ mối quan hệ lệch lạc.",
        "prompt": "Solitary withered telephone pole standing in barren fog with severed lines dangling, surrounded by deep silence, tragic psychological isolation."
    },
    {
        "name": "t23_a5_16_redflag4_manipulator_severing_support",
        "act": 5,
        "sentences": "5.05#16",
        "desc": "Kẻ thao túng tìm cách tước bỏ mạng lưới hỗ trợ xã hội của nạn nhân.",
        "prompt": "Shadow of a marionette puppeteer's hand controlling thin tangled strings over a dark empty tabletop, ominous manipulative control, noir linework."
    },
    {
        "name": "t23_a5_17_healthy_relationship_connection_peace",
        "act": 5,
        "sentences": "5.05#17",
        "desc": "Mối quan hệ lành mạnh luôn mang lại sự an tâm và mở rộng kết nối với gia đình.",
        "prompt": "Open French doors leading out to a peaceful sunlit garden patio with green vines and flowering trees, calm reassuring domestic serenity."
    },
    {
        "name": "t23_a5_18_amber_eyes_gratitude_closing",
        "act": 5,
        "sentences": "5.05#18",
        "desc": "Lời cảm ơn khán giả đã đồng hành cùng tập hồ sơ tâm lý học Amber Eyes.",
        "prompt": "A warm studio recording microphone glowing in soft amber light on dark walnut desk, acoustic foam panels in background, cozy investigative atmosphere."
    },
    {
        "name": "t23_a5_19_subscribe_bell_community_callout",
        "act": 5,
        "sentences": "5.05#19",
        "desc": "Lời kêu gọi đăng ký kênh, chia sẻ video để lan tỏa sự tỉnh táo.",
        "prompt": "Antique brass hand bell resting beside open leather notebook and fountain pen on study desk, warm diffused sidelight, community engagement aesthetic."
    },
    {
        "name": "t23_a5_20_farewell_until_next_dossier",
        "act": 5,
        "sentences": "5.05#20",
        "desc": "Lời chào tạm biệt và hẹn gặp lại trong những tập hồ sơ tiếp theo.",
        "prompt": "Closed heavy leather dossier portfolio tied with dark ribbon resting on library study table, soft dust motes floating in warm amber desk lamp beam."
    },
    {
        "name": "t23_a5_21_san_gabriel_mountains_sunrise_hope",
        "act": 5,
        "sentences": "5.05#20",
        "desc": "Bình minh hy vọng vươn lên trên dãy núi San Gabriel sau đêm dài ác mộng.",
        "prompt": "Majestic silhouette of San Gabriel mountain peaks illuminated by first rays of pale golden dawn, dispersing night mists over Los Angeles valley, peace restored."
    },
    {
        "name": "t23_a5_22_amber_eyes_closing_dossier_card",
        "act": 5,
        "sentences": "Thẻ kết",
        "desc": "Khung hình kết thúc tập 23 mang biểu tượng hồ sơ kênh Amber Eyes.",
        "prompt": "Minimalist dark slate background with subtle film grain and vignette, faint graphic novel owl feather silhouette in the corner, elegant noir finish."
    }
]

def main():
    print(f"Tổng số ảnh định nghĩa: {len(BG_SPECS)}")
    out_file = Path('.work/bg_jobs_tap23.json')
    out_file.write_text(json.dumps(BG_SPECS, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã ghi 150 prompt chuẩn Deep Noir vào {out_file}")

if __name__ == '__main__':
    main()
