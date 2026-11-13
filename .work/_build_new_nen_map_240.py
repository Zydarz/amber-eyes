import json
import re
from pathlib import Path

ROOT = Path('.')
WORK = ROOT / '.work'

# Đọc kịch bản 240 câu tiếng Việt
script_p = WORK / 'script_tap10.json'
script = json.loads(script_p.read_text(encoding='utf-8'))

# Danh sách tất cả sentence ID theo đúng thứ tự kịch bản mới 240 câu
all_sids = []
for el in script:
    if el.get('kind') == 'LOI':
        eid = el['id']
        for idx in range(len(el.get('sentences', []))):
            all_sids.append(f"{eid}#{idx+1}")

print(f"Total sentences in script: {len(all_sids)}")

# Đọc bảng cũ nen_map_t10.json làm gốc tham khảo
old_map = json.loads((WORK / '_t10/nen_map_t10.json').read_text(encoding='utf-8'))

# Xây dựng bảng map mới 240 câu
new_map = {}

# Đọc danh sách 71 background jobs để kiểm tra
bg_jobs = json.loads((WORK / '_t10/bg_jobs_t10.json').read_text(encoding='utf-8'))
valid_bgs = {j['name'] for j in bg_jobs}
print(f"Total valid backgrounds: {len(valid_bgs)}")

# Ánh xạ theo từng element:
# 1.02 (12 câu):
new_map['1.02#1'] = 't10_hitchhiking_highway_1977'
new_map['1.02#2'] = 't10_hitchhiking_highway_1977'
new_map['1.02#3'] = 't10_hitchhiking_highway_1977'
new_map['1.02#4'] = 't10_traveler_backpack_worn_map'
new_map['1.02#5'] = 't10_traveler_backpack_worn_map'
new_map['1.02#6'] = 't10_golden_innocence_road_illusion'
new_map['1.02#7'] = 't10_red_bluff_pine_forest_road'       # Red Bluff miền Tây yên bình
new_map['1.02#8'] = 't10_red_bluff_pine_forest_road'       # Rừng thông ngút ngàn
new_map['1.02#9'] = 't10_hooker_community_mask'           # Người hàng xóm bên kia hàng rào
new_map['1.02#10'] = 't10_golden_innocence_road_illusion'  # Điểm mù mất cảnh giác tập thể
new_map['1.02#11'] = 't10_hitchhiking_highway_1977'        # Dải xa lộ thênh thang (câu cũ 1.02#7)
new_map['1.02#12'] = 't10_golden_innocence_road_illusion'  # Vụ bắt cóc kỳ lạ (câu cũ 1.02#8)

# 1.04 (6 câu) - giữ nguyên từ old_map (1.04#1..#6)
for k in range(1, 7):
    new_map[f'1.04#{k}'] = old_map[f'1.04#{k}']

# 1.06 (6 câu) - giữ nguyên
for k in range(1, 7):
    new_map[f'1.06#{k}'] = old_map[f'1.06#{k}']

# 1.07 (5 câu N1) - giữ nguyên
for k in range(1, 6):
    new_map[f'1.07#{k}'] = old_map[f'1.07#{k}']

# 1.09 (5 câu) - giữ nguyên
for k in range(1, 6):
    new_map[f'1.09#{k}'] = old_map[f'1.09#{k}']

# 1.10 (7 câu) - giữ nguyên
for k in range(1, 8):
    new_map[f'1.10#{k}'] = old_map[f'1.10#{k}']

# 1.11 (5 câu) - giữ nguyên
for k in range(1, 6):
    new_map[f'1.11#{k}'] = old_map[f'1.11#{k}']

# 2.02 (6 câu) - giữ nguyên
for k in range(1, 7):
    new_map[f'2.02#{k}'] = old_map[f'2.02#{k}']

# 2.04 (10 câu - thêm 4 câu về Janice và đệm nước):
new_map['2.04#1'] = 't10_heavy_iron_latches_padlock'       # Chiếc hộp gỗ do Cameron tự tay đóng
new_map['2.04#2'] = 't10_waterbed_crushing_weight'         # Giấu dưới giường đệm nước cồng kềnh
new_map['2.04#3'] = 't10_waterbed_crushing_weight'         # Trọng lượng khổng lồ đệm nước
new_map['2.04#4'] = 't10_heavy_iron_latches_padlock'       # Cơ chế kiểm soát tuyệt đối
new_map['2.04#5'] = 't10_janice_hooker_moral_turmoil'      # Kẻ bị giam cầm không chỉ có một mình Colleen
new_map['2.04#6'] = 't10_janice_hooker_moral_turmoil'      # Phía trên nắp hộp, Janice sống trong lồng giam tâm lý
new_map['2.04#7'] = 't10_janice_hooker_moral_turmoil'      # Từng là nạn nhân bị bạo hành, ngắt kết nối lương tri
new_map['2.04#8'] = 't10_waterbed_crushing_weight'         # Tiếng cựa mình từ dưới sàn mỗi đêm
new_map['2.04#9'] = 't10_one_hour_chores_silhouette'       # Thủ đoạn MO kiểm soát (cũ 2.04#5)
new_map['2.04#10'] = 't10_heavy_iron_latches_padlock'      # Sự im lặng đồng lõa của Janice (cũ 2.04#6)

# 2.05 (5 câu) - giữ nguyên
for k in range(1, 6):
    new_map[f'2.05#{k}'] = old_map[f'2.05#{k}']

# 2.06 (12 câu - thêm 4 câu về Phân ly tâm trí Colleen):
new_map['2.06#1'] = 't10_sensory_deprivation_clock_melt'   # Hội chứng suy giảm giác quan
new_map['2.06#2'] = 't10_sensory_deprivation_clock_melt'   # Ranh giới ngày đêm xóa nhòa
new_map['2.06#3'] = 't10_sensory_deprivation_clock_melt'   # Tâm trí rơi vào trạng thái ảo giác
new_map['2.06#4'] = 't10_sensory_deprivation_clock_melt'   # Sự ngưng đọng thời gian
new_map['2.06#5'] = 't10_childhood_poems_faint_echo'       # Cơ chế Phân ly tâm trí Dissociation
new_map['2.06#6'] = 't10_childhood_poems_faint_echo'       # Neo giữ tâm trí vào vần thơ ấu, cha mẹ
new_map['2.06#7'] = 't10_childhood_poems_faint_echo'       # Trí tưởng tượng có định hướng là pháo đài
new_map['2.06#8'] = 't10_childhood_poems_faint_echo'       # Nạn nhân học hiện đại gọi đây là sinh tồn tinh thần
new_map['2.06#9'] = 't10_sensory_deprivation_clock_melt'   # Hộp sọ gỗ đội đầu (cũ 2.06#5)
new_map['2.06#10'] = 't10_childhood_poems_faint_echo'      # Tiếng thì thầm yếu ớt (cũ 2.06#6)
new_map['2.06#11'] = 't10_sensory_deprivation_clock_melt'  # Ký ức về bầu trời xanh (cũ 2.06#7)
new_map['2.06#12'] = 't10_childhood_poems_faint_echo'      # Ngọn nến hy sinh (cũ 2.06#8)

# 2.07 (4 câu) - giữ nguyên
for k in range(1, 5):
    new_map[f'2.07#{k}'] = old_map[f'2.07#{k}']

# 2.08 (7 câu) - giữ nguyên
for k in range(1, 8):
    new_map[f'2.08#{k}'] = old_map[f'2.08#{k}']

# 2.09 (4 câu) - giữ nguyên
for k in range(1, 5):
    new_map[f'2.09#{k}'] = old_map[f'2.09#{k}']

# 2.10 (6 câu) - giữ nguyên
for k in range(1, 7):
    new_map[f'2.10#{k}'] = old_map[f'2.10#{k}']

# 2.11 (3 câu) - giữ nguyên
for k in range(1, 4):
    new_map[f'2.11#{k}'] = old_map[f'2.11#{k}']

# 3.02 (4 câu) - giữ nguyên
for k in range(1, 5):
    new_map[f'3.02#{k}'] = old_map[f'3.02#{k}']

# 3.04 (4 câu) - giữ nguyên
for k in range(1, 5):
    new_map[f'3.04#{k}'] = old_map[f'3.04#{k}']

# 3.05 (7 câu) - giữ nguyên
for k in range(1, 8):
    new_map[f'3.05#{k}'] = old_map[f'3.05#{k}']

# 3.06 (4 câu) - giữ nguyên
for k in range(1, 5):
    new_map[f'3.06#{k}'] = old_map[f'3.06#{k}']

# 3.07 (11 câu - thêm 3 câu về điểm mù nhẹ nhõm gia đình):
new_map['3.07#1'] = 't10_martin_seligman_learned_helplessness'
new_map['3.07#2'] = 't10_martin_seligman_learned_helplessness'
new_map['3.07#3'] = 't10_open_cage_motionless_silhouette'
new_map['3.07#4'] = 't10_open_cage_motionless_silhouette'
new_map['3.07#5'] = 't10_martin_seligman_learned_helplessness'
new_map['3.07#6'] = 't10_father_concerned_inquiry'         # Điểm mù nhẹ nhõm gia đình
new_map['3.07#7'] = 't10_tense_family_dinner_shadows'       # Bàn ăn gia đình gượng gạo
new_map['3.07#8'] = 't10_father_concerned_inquiry'         # Khao khát tin con gái bình yên
new_map['3.07#9'] = 't10_the_company_shadow_syndicate'     # Đặc vụ ngầm The Company (cũ 3.07#6)
new_map['3.07#10'] = 't10_window_sniper_paranoia_shadow'   # Tay súng bắn tỉa (cũ 3.07#7)
new_map['3.07#11'] = 't10_wooden_box_under_bed_shadow'     # Tự quay lại chiếc hộp gỗ (cũ 3.07#8)

# 3.08 (8 câu - thêm 3 câu về chiếc hộp như vỏ ốc an toàn nghịch lý):
new_map['3.08#1'] = 't10_window_sniper_paranoia_shadow'
new_map['3.08#2'] = 't10_window_sniper_paranoia_shadow'
new_map['3.08#3'] = 't10_window_sniper_paranoia_shadow'
new_map['3.08#4'] = 't10_window_sniper_paranoia_shadow'
new_map['3.08#5'] = 't10_darkness_as_false_shelter'        # Vỏ ốc an toàn nghịch lý
new_map['3.08#6'] = 't10_darkness_as_false_shelter'        # Chiếc hộp gỗ thành nơi không bị phán xét
new_map['3.08#7'] = 't10_darkness_as_false_shelter'        # Ranh giới nguy hiểm và chốn ẩn náu
new_map['3.08#8'] = 't10_trauma_bonding_bread_and_whip'    # Bánh mì và roi vọt gắn kết sang chấn (cũ 3.08#5)

# 3.09 (8 câu) - giữ nguyên
for k in range(1, 9):
    new_map[f'3.09#{k}'] = old_map[f'3.09#{k}']

# 3.10 (3 câu) - giữ nguyên
for k in range(1, 4):
    new_map[f'3.10#{k}'] = old_map[f'3.10#{k}']

# 4.02 (5 câu) - giữ nguyên
for k in range(1, 6):
    new_map[f'4.02#{k}'] = old_map[f'4.02#{k}']

# 4.03 (9 câu - thêm 3 câu về nguy cơ đứa con gái nhỏ):
new_map['4.03#1'] = 't10_janice_hooker_moral_turmoil'
new_map['4.03#2'] = 't10_janice_hooker_moral_turmoil'
new_map['4.03#3'] = 't10_janice_hooker_moral_turmoil'
new_map['4.03#4'] = 't10_second_victim_shadow_threat'      # Bắt cóc cô gái thứ hai
new_map['4.03#5'] = 't10_seventh_year_toddler_toys_shadow' # Bản năng bảo vệ con cái
new_map['4.03#6'] = 't10_seventh_year_toddler_toys_shadow' # Bảo vệ tương lai hai đứa con gái nhỏ
new_map['4.03#7'] = 't10_janice_hooker_moral_turmoil'      # Janice đứng trước lựa chọn sinh tử (cũ 4.03#4)
new_map['4.03#8'] = 't10_second_victim_shadow_threat'      # Bóng ma tội ác không dừng lại (cũ 4.03#5)
new_map['4.03#9'] = 't10_church_pastor_confession_shadow'  # Tìm đến vị mục sư (cũ 4.03#6)

# 4.04 (5 câu - thêm 1 câu về mỏ neo mục sư):
new_map['4.04#1'] = 't10_second_victim_shadow_threat'
new_map['4.04#2'] = 't10_church_pastor_confession_shadow'  # Mỏ neo đạo đức ngoại vi từ mục sư
new_map['4.04#3'] = 't10_second_victim_shadow_threat'      # Tương lai của hai đứa trẻ (cũ 4.04#2)
new_map['4.04#4'] = 't10_church_pastor_confession_shadow'  # Lời khuyên phá vỡ sự im lặng (cũ 4.04#3)
new_map['4.04#5'] = 't10_church_pastor_confession_shadow'  # Quyết định hành động dũng cảm (cũ 4.04#4)

# 4.05 (8 câu N2 - thêm 3 câu tự thú của Janice):
new_map['4.05#1'] = 't10_church_pastor_confession_shadow'
new_map['4.05#2'] = 't10_church_pastor_confession_shadow'
new_map['4.05#3'] = 't10_wooden_box_under_bed_shadow'
new_map['4.05#4'] = 't10_church_pastor_confession_shadow'
new_map['4.05#5'] = 't10_church_pastor_confession_shadow'
new_map['4.05#6'] = 't10_janice_hooker_moral_turmoil'      # Tự lừa dối rằng im lặng gia đình sẽ bình yên
new_map['4.05#7'] = 't10_seventh_year_toddler_toys_shadow' # Con gái lớn lên bên chiếc hộp gỗ
new_map['4.05#8'] = 't10_church_pastor_confession_shadow'  # Lời mục sư đánh thức lương tri

# 4.07 (6 câu) - giữ nguyên
for k in range(1, 7):
    new_map[f'4.07#{k}'] = old_map[f'4.07#{k}']

# 4.08 (4 câu) - giữ nguyên
for k in range(1, 5):
    new_map[f'4.08#{k}'] = old_map[f'4.08#{k}']

# 4.09 (9 câu - thêm 3 câu về Tính lưỡng phân của Janice: Lương tâm vs Pháp lý):
new_map['4.09#1'] = 't10_tehama_superior_court_columns'
new_map['4.09#2'] = 't10_tehama_superior_court_columns'
new_map['4.09#3'] = 't10_immunity_agreement_document'     # Lưỡng phân: giải cứu Colleen
new_map['4.09#4'] = 't10_immunity_agreement_document'     # Bản hợp đồng miễn trừ truy tố toan tính
new_map['4.09#5'] = 't10_tehama_superior_court_columns'    # Ranh giới hối cải và thoát tội tranh cãi
new_map['4.09#6'] = 't10_frank_ochberg_psychiatric_testimony' # Lời khai tâm thần bác sĩ (cũ 4.09#3)
new_map['4.09#7'] = 't10_unmasking_predator_broken_facade'    # Vỏ bọc bị bóc trần (cũ 4.09#4)
new_map['4.09#8'] = 't10_tehama_superior_court_columns'       # Bồi thẩm đoàn công lý (cũ 4.09#5)
new_map['4.09#9'] = 't10_unmasking_predator_broken_facade'    # Bản chất kẻ săn mồi (cũ 4.09#6)

# 4.10 (6 câu - thêm 1 câu về bản án ái kỷ Cameron):
new_map['4.10#1'] = 't10_104_years_sentence_gavel'
new_map['4.10#2'] = 't10_104_years_sentence_gavel'
new_map['4.10#3'] = 't10_104_years_sentence_gavel'
new_map['4.10#4'] = 't10_california_state_prison_bars_closing'
new_map['4.10#5'] = 't10_california_state_prison_bars_closing' # Kẻ nhốt người khác bị giam trong nhà ngục ích kỷ
new_map['4.10#6'] = 't10_104_years_sentence_gavel'             # Bản án thế kỷ giáng xuống (cũ 4.10#5)

# 5.02 (8 câu) - giữ nguyên
for k in range(1, 9):
    new_map[f'5.02#{k}'] = old_map[f'5.02#{k}']

# 5.03 (7 câu - thêm 1 câu về PTG tha thứ quá khứ):
new_map['5.03#1'] = 't10_post_traumatic_growth_sprout_stone'
new_map['5.03#2'] = 't10_post_traumatic_growth_sprout_stone'
new_map['5.03#3'] = 't10_post_traumatic_growth_sprout_stone'
new_map['5.03#4'] = 't10_healing_journey_morning_light'        # Học cách tha thứ cho sự bất lực quá khứ
new_map['5.03#5'] = 't10_post_traumatic_growth_sprout_stone'  # Biểu tượng phục hồi (cũ 5.03#4)
new_map['5.03#6'] = 't10_healing_journey_morning_light'        # Sống hòa bình với vết sẹo (cũ 5.03#5)
new_map['5.03#7'] = 't10_simple_gifts_of_life_memoir'          # Cuốn sách Simple Gifts of Life (cũ 5.03#6)

# 5.04 (6 câu - thêm 2 câu về trách nhiệm cộng đồng và sự thờ ơ):
new_map['5.04#1'] = 't10_fbi_academy_profiling_archive'
new_map['5.04#2'] = 't10_fbi_academy_profiling_archive'
new_map['5.04#3'] = 't10_invisible_timber_prison_mind'
new_map['5.04#4'] = 't10_tehama_superior_court_columns'        # Giá của sự thờ ơ đằng sau riêng tư
new_map['5.04#5'] = 't10_invisible_timber_prison_mind'         # Ánh nhìn bàng quan cộng đồng
new_map['5.04#6'] = 't10_tehama_superior_court_columns'        # Các phiên ân xá bị bác bỏ (cũ 5.04#4)

# 5.05 (15 câu) - giữ nguyên 15 câu cảnh báo đỏ & kết thúc
for k in range(1, 16):
    new_map[f'5.05#{k}'] = old_map[f'5.05#{k}']

# KIỂM TRA ĐỘ PHỦ 100%:
missing = [sid for sid in all_sids if sid not in new_map]
extra = [sid for sid in new_map if sid not in all_sids]
invalid_bgs_used = [bg for bg in new_map.values() if bg not in valid_bgs]

print(f"Total mapped: {len(new_map)} / {len(all_sids)}")
print(f"Missing sentences: {len(missing)} {missing}")
print(f"Extra sentences: {len(extra)} {extra}")
print(f"Invalid backgrounds: {len(invalid_bgs_used)} {invalid_bgs_used}")

used_bgs = set(new_map.values())
unused_bgs = valid_bgs - used_bgs
print(f"Backgrounds used: {len(used_bgs)} / {len(valid_bgs)}")
print(f"Unused backgrounds: {len(unused_bgs)} {unused_bgs}")

# Ghi file nen_map_t10.json
out_p = WORK / '_t10/nen_map_t10.json'
out_p.write_text(json.dumps(new_map, ensure_ascii=False, indent=2), encoding='utf-8')
print(f"Successfully written to {out_p}")
