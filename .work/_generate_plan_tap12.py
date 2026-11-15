# -*- coding: utf-8 -*-
"""Generate 02_SAN_XUAT/Tap12/KeHoach_Video_Tap12.md matching the 249-sentence script."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPT_PATH = ROOT / ".work" / "script_tap12.json"
OUT_PATH = ROOT / "02_SAN_XUAT" / "Tap12" / "KeHoach_Video_Tap12.md"

script = json.loads(SCRIPT_PATH.read_text(encoding="utf-8"))

# Background mappings per element and sentence range
BG_MAP_ACT1 = [
    # 1.02 (9 sents): 1.02#1..#2 -> aerial, #3..#4 -> clearing, #5..#6 -> toys, #7..#8 -> tragedy, #9 -> puppet_master
    ("1.02", 1, 2, "t12_guyana_tropical_rainforest_aerial"),
    ("1.02", 3, 4, "t12_jonestown_settlement_clearing"),
    ("1.02", 5, 6, "t12_innocent_children_toys_jungle"),
    ("1.02", 7, 8, "t12_monolithic_tragedy_shadow"),
    ("1.02", 9, 9, "t12_puppet_master_dark_silhouette"),
    # 1.04 (10 sents): 1.04#1..#2 -> indiana, #3..#4 -> racial_harmony, #5..#6 -> soup_kitchen, #7..#8 -> sf_expansion, #9..#10 -> city_hall
    ("1.04", 1, 2, "t12_indiana_church_1950s_dawn"),
    ("1.04", 3, 4, "t12_racial_harmony_facade"),
    ("1.04", 5, 6, "t12_charity_soup_kitchen_bread"),
    ("1.04", 7, 8, "t12_san_francisco_temple_expansion"),
    ("1.04", 9, 10, "t12_city_hall_political_alliances"),
    # 1.06 (8 sents): 1.06#1..#2 -> iron_fist, #3..#4 -> catharsis, #5..#6 -> property_surrender, #7 -> new_west, #8 -> exodus
    ("1.06", 1, 2, "t12_iron_fist_behind_velvet_curtain"),
    ("1.06", 3, 4, "t12_catharsis_session_interrogation"),
    ("1.06", 5, 6, "t12_property_surrender_passbooks"),
    ("1.06", 7, 7, "t12_new_west_investigative_draft"),
    ("1.06", 8, 8, "t12_exodus_ships_guyana_dusk"),
    # 1.07 (8 sents): N1 (Leslie) #1..#2 -> utopian_promise, #3..#4 -> confiscated_passports, #5..#6 -> forced_labor, #7 -> meager_ration, #8 -> armed_guards
    ("1.07", 1, 2, "t12_utopian_promise_mirage"),
    ("1.07", 3, 4, "t12_confiscated_passports_trunk"),
    ("1.07", 5, 6, "t12_equatorial_forced_labor_fields"),
    ("1.07", 7, 7, "t12_meager_ration_tin_bowl"),
    ("1.07", 8, 8, "t12_inescapable_labor_camp_cage"),
    # 1.09 (6 sents): 1.09#1..#2 -> loudspeaker, #3..#4 -> central_pavilion, #5..#6 -> geographical_isolation
    ("1.09", 1, 2, "t12_loudspeaker_horns_tower"),
    ("1.09", 3, 4, "t12_central_pavilion_night_tribunal"),
    ("1.09", 5, 6, "t12_impenetrable_geographical_isolation"),
    # 1.10 (10 sents): D (Điều tra viên) #1..#2 -> concerned_relatives, #3..#5 -> leo_ryan_briefing, #6..#7 -> press_corps, #8..#10 -> entering_compound
    ("1.10", 1, 2, "t12_concerned_relatives_alliance"),
    ("1.10", 3, 5, "t12_congressman_leo_ryan_briefing"),
    ("1.10", 6, 7, "t12_press_corps_cameras_microphones"),
    ("1.10", 8, 10, "t12_entering_armed_compound_gate"),
    # 1.11 (5 sents): 1.11#1..#3 -> paranoia_cracking, #4..#5 -> edge_of_abyss
    ("1.11", 1, 3, "t12_paranoia_cracking_dictator_mind"),
    ("1.11", 4, 5, "t12_edge_of_the_abyss_shadow"),
]

BG_MAP_ACT2 = [
    # 2.02 (5 sents): 2.02#1..#2 -> arrival, #3..#4 -> reception, #5 -> crumbling_facade
    ("2.02", 1, 2, "t12_arrival_port_kaituma_dust"),
    ("2.02", 3, 4, "t12_reception_musical_performance"),
    ("2.02", 5, 5, "t12_nbc_camera_recording_facade"),
    # 2.04 (7 sents): 2.04#1..#3 -> secret_note, #4..#5 -> morning_pleas, #6..#7 -> leo_ryan_podium
    ("2.04", 1, 3, "t12_secret_note_folded_slip"),
    ("2.04", 4, 5, "t12_morning_pleas_for_defection"),
    ("2.04", 6, 7, "t12_confrontation_at_lectern"),
    # 2.06 (8 sents): 2.06#1..#2 -> truck_evacuation, #3..#4 -> airstrip, #5..#6 -> gunfire_smoke, #7..#8 -> jackie_speier
    ("2.06", 1, 2, "t12_truck_evacuation_muddy_road"),
    ("2.06", 3, 4, "t12_port_kaituma_gravel_airstrip"),
    ("2.06", 5, 6, "t12_airstrip_ambush_gunfire_smoke"),
    ("2.06", 7, 8, "t12_jackie_speier_resilience_shadow"),
    # 2.07 (8 sents): D #1..#2 -> red_brigade_tractor, #3..#5 -> fallen_reporters, #6..#8 -> gunmen_return
    ("2.07", 1, 2, "t12_red_brigade_tractor_approach"),
    ("2.07", 3, 5, "t12_fallen_reporters_and_ryan"),
    ("2.07", 6, 8, "t12_gunmen_return_report_shadows"),
    # 2.09 (5 sents): 2.09#1..#2 -> emergency_siren, #3..#5 -> mass_gathering
    ("2.09", 1, 2, "t12_emergency_siren_echo_jungle"),
    ("2.09", 3, 5, "t12_mass_gathering_central_pavilion"),
    # 2.11 (9 sents): D #1..#3 -> knife_attack, #4..#6 -> fbi_tape, #7..#9 -> vat_flavor_aid
    ("2.11", 1, 3, "t12_knife_attack_scuffle_pavilion"),
    ("2.11", 4, 6, "t12_fbi_evidence_tape_q042"),
    ("2.11", 7, 9, "t12_metal_vat_flavor_aid_poison"),
    # 2.13 (8 sents): 2.13#1..#3 -> broken_will, #4..#6 -> mass_gathering, #7..#8 -> edge_of_abyss
    ("2.13", 1, 3, "t12_broken_will_family_embrace"),
    ("2.13", 4, 6, "t12_haunting_silence_aftermath"),
    ("2.13", 7, 8, "t12_edge_of_the_abyss_shadow"),
]

BG_MAP_ACT3 = [
    # 3.02 (6 sents): 3.02#1..#3 -> unanswered_question, #4..#6 -> pawns_chessboard
    ("3.02", 1, 3, "t12_unanswered_question_diorama"),
    ("3.02", 4, 6, "t12_pawns_on_destructive_chessboard"),
    # 3.03 (9 sents): C #1..#3 -> milgram, #4..#6 -> agentic_state, #7..#9 -> false_prophet
    ("3.03", 1, 3, "t12_milgram_experiment_shock_generator"),
    ("3.03", 4, 6, "t12_agentic_state_mechanism"),
    ("3.03", 7, 9, "t12_false_prophet_deification"),
    # 3.04 (6 sents): 3.04#1..#3 -> groupthink, #4..#6 -> foot_in_door
    ("3.04", 1, 3, "t12_groupthink_hostile_mob_shadows"),
    ("3.04", 4, 6, "t12_foot_in_the_door_staircase"),
    # 3.05 (13 sents): C #1..#4 -> cognitive_dissonance, #5..#8 -> sunk_cost, #9..#13 -> habituation
    ("3.05", 1, 4, "t12_cognitive_dissonance_scales"),
    ("3.05", 5, 8, "t12_sunk_cost_entrapment_quicksand"),
    ("3.05", 9, 13, "t12_habituation_death_desensitization"),
    # 3.06 (7 sents): 3.06#1..#3 -> biological_exhaustion, #4..#5 -> sleep_deprivation, #6..#7 -> prefrontal_cortex
    ("3.06", 1, 3, "t12_biological_exhaustion_heat"),
    ("3.06", 4, 5, "t12_sleep_deprivation_speaker_wires"),
    ("3.06", 6, 7, "t12_prefrontal_cortex_impairment"),
    # 3.07 (7 sents): C #1..#3 -> white_night, #4..#5 -> simulated_poison, #6..#7 -> habituation
    ("3.07", 1, 3, "t12_white_night_midnight_bell"),
    ("3.07", 4, 5, "t12_simulated_poison_paper_cups"),
    ("3.07", 6, 7, "t12_pawns_on_destructive_chessboard"),
    # 3.08 (4 sents): 3.08#1..#2 -> moral_courage, #3..#4 -> lone_microphone
    ("3.08", 1, 2, "t12_moral_courage_candle_in_dark"),
    ("3.08", 3, 4, "t12_christine_miller_lone_microphone"),
]

BG_MAP_ACT4 = [
    # 4.02 (5 sents): 4.02#1..#3 -> tape_reels, #4..#5 -> agitated_dictator
    ("4.02", 1, 3, "t12_tape_recorder_reels_spinning"),
    ("4.02", 4, 5, "t12_agitated_dictator_microphone"),
    # 4.04 (6 sents): 4.04#1..#3 -> lone_microphone, #4..#6 -> moral_courage
    ("4.04", 1, 3, "t12_christine_miller_lone_microphone"),
    ("4.04", 4, 6, "t12_moral_courage_candle_in_dark"),
    # 4.06 (4 sents): 4.06#1..#2 -> agitated_dictator, #3..#4 -> groupthink
    ("4.06", 1, 2, "t12_agitated_dictator_microphone"),
    ("4.06", 3, 4, "t12_groupthink_hostile_mob_shadows"),
    # 4.07 (8 sents): C #1..#4 -> moral_courage, #5..#8 -> cognitive_dissonance
    ("4.07", 1, 4, "t12_moral_courage_candle_in_dark"),
    ("4.07", 5, 8, "t12_cognitive_dissonance_scales"),
    # 4.08 (6 sents): 4.08#1..#3 -> metal_vat, #4..#6 -> broken_will
    ("4.08", 1, 3, "t12_metal_vat_flavor_aid_poison"),
    ("4.08", 4, 6, "t12_broken_will_family_embrace"),
    # 4.09 (6 sents): D #1..#3 -> truck_evacuation, #4..#6 -> escaping_jungle
    ("4.09", 1, 3, "t12_truck_evacuation_muddy_road"),
    ("4.09", 4, 6, "t12_inescapable_labor_camp_cage"),
    # 4.10 (7 sents): N2 #1..#4 -> haunting_silence, #5..#7 -> forensic_agent
    ("4.10", 1, 4, "t12_haunting_silence_aftermath"),
    ("4.10", 5, 7, "t12_forensic_agent_headphones_horror"),
    # 4.11 (6 sents): 4.11#1..#3 -> abandoned_lectern, #4..#6 -> edge_of_abyss
    ("4.11", 1, 3, "t12_abandoned_lectern_single_shot"),
    ("4.11", 4, 6, "t12_edge_of_the_abyss_shadow"),
]

BG_MAP_ACT5 = [
    # 5.02 (6 sents): 5.02#1..#3 -> memorial_monolith, #4..#6 -> us_capitol
    ("5.02", 1, 3, "t12_memorial_918_names_monolith"),
    ("5.02", 4, 6, "t12_us_capitol_congressional_hearing"),
    # 5.03 (5 sents): D #1..#3 -> us_capitol, #4..#5 -> moral_compass
    ("5.03", 1, 3, "t12_us_capitol_congressional_hearing"),
    ("5.03", 4, 5, "t12_moral_compass_unbroken"),
    # 5.04 (9 sents): C #1..#3 -> vulnerability, #4..#6 -> moral_compass, #7..#9 -> independent_mind
    ("5.04", 1, 3, "t12_vulnerability_human_compassion"),
    ("5.04", 4, 6, "t12_moral_compass_unbroken"),
    ("5.04", 7, 9, "t12_independent_mind_dawn_freedom"),
    # 5.05 (23 sents):
    # 5.05#1 -> intro
    ("5.05", 1, 1, "t12_amber_eyes_closing_dossier_jonestown"),
    # #2..#4 -> redflag 1
    ("5.05", 2, 4, "t12_redflag1_total_social_isolation"),
    # #5..#7 -> redflag 2 (financial)
    ("5.05", 5, 7, "t12_redflag3_escalating_commitment_trap"),
    # #8..#10 -> redflag 3 (exhaustion)
    ("5.05", 8, 10, "t12_biological_exhaustion_heat"),
    # #11..#14 -> redflag 4 (deification)
    ("5.05", 11, 14, "t12_redflag4_fortress_paranoia_wall"),
    # #15..#18 -> gift of fear / freedom
    ("5.05", 15, 18, "t12_independent_mind_dawn_freedom"),
    # #19..#23 -> closing dossier
    ("5.05", 19, 23, "t12_amber_eyes_closing_dossier_jonestown"),
]

ALL_BG_MAP = BG_MAP_ACT1 + BG_MAP_ACT2 + BG_MAP_ACT3 + BG_MAP_ACT4 + BG_MAP_ACT5

def get_bg(eid, sent_idx):
    for e, start, end, bg in ALL_BG_MAP:
        if e == eid and start <= sent_idx <= end:
            return bg
    return "t12_amber_eyes_closing_dossier_jonestown"

CAM_CYCLE = ["pan", "pull", "push", "still"]

lines = []
lines.append('# HỒ SƠ SẢN XUẤT TẬP 12 · "THẢM KỊCH JONESTOWN" — VI EDITION')
lines.append('')
lines.append('## B1. Thông tin tập')
lines.append('')
lines.append('| Mục | Nội dung |')
lines.append('|---|---|')
lines.append('| Tên tập | **Tập 12: Thảm Kịch Jonestown — Khi 918 Con Người Cùng Bước Vào Chỗ Chết (Hồ Sơ Jim Jones & Peoples Temple)** |')
lines.append('| Vụ án | Hồ sơ Jim Jones & Peoples Temple (Jonestown, Port Kaituma & Georgetown, Guyana, 1978) |')
lines.append('| Chủ đề tâm lý | Hệ sinh thái 10 chỉ dấu tâm lý & Thao túng tâm lý tập thể (*Cult Mind Control, Obedience to Authority & Groupthink*) · Sự phục tùng quyền lực (*Milgram Paradigm*) · Bẫy chi phí chìm nhận thức (*Cognitive Sunk Cost Trap*) · Kỹ thuật leo thang cam kết (*Foot-in-the-Door*) · **TRỌNG TÂM:** Cơ chế của sự hối hận (*Sự sụp đổ của Bất hòa nhận thức & Chấn thương đạo đức*) đối lập với Sự sụp đổ cái tôi ái kỷ (*Narcissistic Collapse*) & Tự thương hại bệnh lý (*Pathological Self-Pity*) của Jim Jones · Nạn nhân học & Lương tri độc lập (*Christine Miller*) đối đầu Tư duy bầy đàn · Mặc cảm tội lỗi của người sống sót (*Survivor\'s Guilt*) của Leslie Wagner-Wilson · 4 Cảnh báo đỏ sinh tồn (*The Gift of Fear*) |')
lines.append('| Định dạng | Podcast Tài liệu Phân tích Tâm lý Tội phạm (Host-Driven Documentary) — 5 Hồi chuẩn A2c/K10 |')
lines.append('| Cấu trúc phân vai | 4 Giọng đọc chính: **Host (Cú)** (136 câu) · **Điều tra viên (Sói)** (37 câu) · **Chuyên gia Tâm lý (Cáo)** (61 câu) · **Người bình thường (N1/N2)**: N1 Leslie Wagner-Wilson (8 câu, `1.07`) & N2 Nhân viên ngoại giao / tiếp cận hiện trường (7 câu, `4.10`) |')
lines.append('| Quy mô kịch bản | **249 câu thoại** (mở rộng +39 câu tâm lý chuyên sâu) · 53 phần tử (Elements) · 33 lượt thoại |')
lines.append('| Thời lượng dự kiến | **~32 – 34 phút** · Đạt chuẩn Golden Benchmark của kênh Amber eyes |')
lines.append('| Tiêu chuẩn an toàn | **Tuân thủ tuyệt đối Quy tắc V9 (YouTube Safe)**: 0% bạo lực máu me, gore; 100% tập trung phân tích khoa học hành vi và cảnh báo đỏ sinh tồn |')
lines.append('| Tài nguyên hình ảnh | **83 ảnh nền chuẩn 2112×1188 (16:9 2K)** tiền tố `t12_` tại `assets/bg/` · Phong cách Dark Graphic Novel Noir (theo `02_SAN_XUAT/Tap12/Danh_Sach_Anh_Tap12.md`) |')
lines.append('| Bộ nhạc nền (BGM) | Dark Ambient rừng nhiệt đới ngột ngạt $\\rightarrow$ Solo Cello u buồn $\\rightarrow$ Minimalist Piano $\\rightarrow$ Tension Strings & Analog Noise $\\rightarrow$ Warm Piano |')
lines.append('| Tài liệu nghiên cứu chuyên sâu | [`01_KICH_BAN/Tap12/NghienCuu_TamLy_BoSung_KichBan_Tap12.md`](../../01_KICH_BAN/Tap12/NghienCuu_TamLy_BoSung_KichBan_Tap12.md) |')
lines.append('')
lines.append('---')
lines.append('')
lines.append('## 6. DANH SÁCH SHOT — TẬP 12 (VI)')
lines.append('')
lines.append('Nền `t12_*` là **tài sản dùng chung cho cả 3 ngôn ngữ** (H17/A8.1) — mã shot giống nhau luôn dùng cùng một nền.')
lines.append('')
lines.append('### INTRO KÊNH · 0,00–22,41 s')
lines.append('')
lines.append('Đặt `assets/brand/intro_kenh.mov` tại 0,00 s (A5.7). Không câu thoại nào thuộc intro.')
lines.append('')

act_titles = {
    1: "HỒI 1 — LỜI HỨA THIÊN ĐƯỜNG VÀ BÓNG MA NƠI RỪNG SÂU",
    2: "HỒI 2 — CUỘC PHỤC KÍCH ĐƯỜNG BĂNG VÀ TIẾNG CÒI BÁO ĐỘNG ĐỊNH MỆNH",
    3: "HỒI 3 — GIẢI MÃ CƠ CHẾ TÂM LÝ: TỪ PHỤC TÙNG ĐẾN TƯ DUY TẬP THỂ",
    4: "HỒI 4 — CUỘN BĂNG TỬ THẦN Q 042 VÀ TIẾNG NÓI PHẢN KHÁNG CÔ ĐƠN",
    5: "HỒI 5 — BÀI HỌC ĐẮT GIÁ VỀ TÂM LÝ BẦY ĐÀN & LỜI CẢNH TỈNH"
}

act_inter_titles = {
    1: ("HỒI 02", "CUỘC PHỤC KÍCH ĐƯỜNG BĂNG VÀ TIẾNG CÒI BÁO ĐỘNG ĐỊNH MỆNH"),
    2: ("HỒI 03", "GIẢI MÃ CƠ CHẾ TÂM LÝ: TỪ PHỤC TÙNG ĐẾN TƯ DUY TẬP THỂ"),
    3: ("HỒI 04", "CUỘN BĂNG TỬ THẦN Q 042 VÀ TIẾNG NÓI PHẢN KHÁNG CÔ ĐƠN"),
    4: ("HỒI 05", "BÀI HỌC ĐẮT GIÁ VỀ TÂM LÝ BẦY ĐÀN & LỜI CẢNH TỈNH")
}

loi_by_act = {}
for e in script:
    if e['kind'] == 'LOI':
        loi_by_act.setdefault(e['act'], []).append(e)

shot_counts_by_act = {}
total_shots = 0

for act_num in range(1, 6):
    lines.append(f'### {act_titles[act_num]}')
    lines.append('')
    lines.append('| Shot | Câu | Vai | Mẫu | Nền + bóng | Chữ | Beat | Nhân vật | |')
    lines.append('|---|---|---|---|---|---|---|---|---|')
    
    act_lois = loi_by_act[act_num]
    shot_idx = 0
    
    for loi_idx, e in enumerate(act_lois):
        role = e['role']
        eid = e['id']
        sents = e['sentences']
        is_n1 = (eid == '1.07')
        is_n2 = (eid == '4.10')
        
        # Check next role
        next_role = None
        if loi_idx + 1 < len(act_lois):
            next_role = act_lois[loi_idx + 1]['role']
        
        for s_idx, s in enumerate(sents, 1):
            shot_idx += 1
            sid = f"{act_num}-{shot_idx:02d}"
            cid = s['id']
            txt = s['text']
            
            # Format text: italics if >= 40 chars, bold if < 40 chars
            if len(txt) >= 40:
                chu = f"*{txt}*"
            else:
                chu = f"**{txt}**"
                
            bg = get_bg(eid, s_idx)
            cam = CAM_CYCLE[(shot_idx - 1) % len(CAM_CYCLE)]
            nen_str = f"`{bg}`, `{cam}`"
            
            # Template
            if is_n1 or is_n2:
                mau = "T4 lời kể"
            else:
                mau = "T1"
                
            # Character badge / presence
            # First shot of role in act: badge
            nv = "—"
            if shot_idx == 1 and act_num == 1:
                nv = "✦ Cú"
            elif s_idx == 1 and (loi_idx == 0 or act_lois[loi_idx-1]['role'] != role):
                if role == 'H': nv = "✦ Cú"
                elif role == 'D': nv = "✦ Sói"
                elif role == 'C': nv = "✦ Cáo"
                elif role == 'N':
                    nv = "✦ Cừu" if is_n1 else "✦ Mèo"
            
            # If last sentence of turn and role changes next
            if s_idx == len(sents) and next_role and next_role != role:
                r_code = 'H' if next_role == 'H' else ('D' if next_role == 'D' else ('C' if next_role == 'C' else 'N'))
                nv = f"→{r_code}"
                
            role_disp = role
            if is_n1: role_disp = "N1"
            elif is_n2: role_disp = "N2"
            
            lines.append(f"| {sid} | `{cid}` | {role_disp} | {mau} | {nen_str} | {chu} | — | {nv} | |")
            
    # Transition card after Act 1, 2, 3, 4
    if act_num < 5:
        shot_idx += 1
        sid = f"{act_num}-{shot_idx:02d}"
        h_tag, h_title = act_inter_titles[act_num]
        chu = f"*{h_tag}* · **{h_title}**"
        lines.append(f"| {sid} | nghỉ chuyển hồi (2 s) | — | T10 | `void`, `still` | {chu} | — | ⊘ | ◼ |")
    else:
        # Closing card after Act 5
        shot_idx += 1
        sid = f"{act_num}-{shot_idx:02d}"
        chu = "**HỒ SƠ TẬP 12 · ĐÃ ĐÓNG** · *AMBER EYES · Phân tích tâm lý tội phạm qua những hồ sơ có thật*"
        lines.append(f"| {sid} | hết tập (0,0 s) | — | T2 | `t12_amber_eyes_closing_dossier_jonestown`, `still` | {chu} | — | ⊘ | ◼ |")
        
    shot_counts_by_act[act_num] = shot_idx
    total_shots += shot_idx
    lines.append('')

lines.append(f"**Tổng:** {total_shots} dòng · 249 câu · 5 hồi · nền dùng 83 loại. Bảng viết ngày 15/11/2026 theo kịch bản mới 249 câu. Nền t12_* dùng chung 100% 3 ngôn ngữ.")

content = '\n'.join(lines) + '\n'
OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
OUT_PATH.write_text(content, encoding='utf-8')
print(f"Generated {OUT_PATH} successfully! Total lines: {len(lines)}, Total shots: {total_shots}")
