import json
import re

# Load chunks
tl = json.load(open('.work/timeline_s_t14.json', encoding='utf-8'))['items']
tl_map = {x['id']: x for x in tl}
jobs_77 = json.load(open('.work/bg_jobs_tap14.json', encoding='utf-8'))
assigned = set()
for j in jobs_77:
    s = j['sentences']
    if '–' in s:
        parts = s.split('–')
        elem = parts[0].split('#')[0]
        s_idx = int(parts[0].split('#')[1])
        e_idx = int(parts[1].replace('#',''))
        for i in range(s_idx, e_idx + 1):
            assigned.add(f'{elem}#{i}')
    else:
        assigned.add(s)

uncovered = [x for x in tl if x['id'] not in assigned]

chunks = []
cur_chunk = []
for item in uncovered:
    if cur_chunk and cur_chunk[0]['act'] != item['act']:
        chunks.append(cur_chunk)
        cur_chunk = [item]
    elif len(cur_chunk) >= 2:
        chunks.append(cur_chunk)
        cur_chunk = [item]
    elif cur_chunk and (cur_chunk[0]['end'] - cur_chunk[0]['start']) + (item['end'] - item['start']) > 24.0:
        chunks.append(cur_chunk)
        cur_chunk = [item]
    else:
        cur_chunk.append(item)
if cur_chunk:
    chunks.append(cur_chunk)

idx = 0
while len(chunks) < 68 and idx < len(chunks):
    if len(chunks[idx]) == 2:
        item1 = [chunks[idx][0]]
        item2 = [chunks[idx][1]]
        chunks.pop(idx)
        chunks.insert(idx, item2)
        chunks.insert(idx, item1)
        idx += 2
    else:
        idx += 1

# Define 68 specific contexts, scene codes, and visual descriptions
meta = [
    # Hồi 1 (11 chunks)
    ("t14_c01_dan_linda_wedding_portrait", "Chân dung đóng khung của Dan Broderick và vợ mới Linda Kolkena trong bóng tối, biểu tượng khởi đầu bi kịch.", "framed wedding portrait of Dan Broderick and his new young wife in high society mansion shadows, cold dramatic spotlight"),
    ("t14_c02_betty_suburban_house_exterior", "Ngôi nhà ngoại ô San Diego trong sương mù lạnh lẽo, nơi Betty một mình đối diện sự cô lập.", "gloomy exterior of a quiet suburban San Diego house at dusk, dense fog rolling on lawn, dark windows"),
    ("t14_c03_young_dan_med_books_studying", "Bàn học ngổn ngang sách giải phẫu y khoa và giáo trình luật của Dan thời sinh viên, Betty làm việc bên cạnh.", "vintage wooden desk covered with medical textbook anatomy sketches and legal treatises, dim desk lamp, exhausted student life"),
    ("t14_c04_betty_teaching_kindergarten_classroom", "Lớp học mẫu giáo vắng lặng cuối chiều, chiếc bảng phấn cũ, Betty chắt chiu từng đồng lương phụ giáo viên.", "empty vintage 1970s kindergarten classroom with small wooden desks and chalkboard, dusty afternoon light"),
    ("t14_c05_dan_law_firm_partnership_celebration", "Góc phòng hội nghị công ty luật với rượu vang và bóng lưng các luật sư bắt tay nhau.", "dimly lit prestigious law firm conference room, crystal glasses and shadowy silhouettes of wealthy attorneys celebrating"),
    ("t14_c06_dan_appointment_young_secretary_linda", "Bóng lưng cô thư ký trẻ 21 tuổi bước vào văn phòng luật sư, sự khởi đầu của vết nứt gia đình.", "silhouette of a young female receptionist walking into a grand law office, heavy blinds casting venetian shadow bars"),
    ("t14_c07_betty_whispering_anxiety_bedroom", "Betty ngồi bên mép giường trong đêm, ánh trăng chiếu qua rèm cửa, nỗi bất an về sự thay đổi của chồng.", "solitary silhouette of a distressed woman sitting on the edge of an empty bed, moonlit venetian blinds"),
    ("t14_c08_dan_dismissive_gaslighting_gesture", "Bóng Dan quay lưng xua tay đầy lạnh lùng, bác bỏ những câu hỏi của Betty trong phòng khách tối.", "silhouette of a sharp-dressed man coldly turning his back and making a dismissive hand wave, stark chiaroscuro"),
    ("t14_c09_betty_burning_dan_custom_suits", "Đống tro tàn của những bộ âu phục đắt tiền bị đốt ngoài sân trong cơn phẫn uất tột cùng.", "pile of expensive tailored mens suits burning in a backyard bonfire, dark embers, thick drifting black smoke, night"),
    ("t14_c10_dan_buying_coral_way_luxury_estate", "Cánh cổng sắt biệt thự sang trọng trên đường Coral Way, biểu tượng quyền lực mới của Dan.", "tall ornate black iron estate gate locked tight, sprawling luxury mansion looming in heavy mist behind"),
    ("t14_c11_dan_locking_out_betty_restraining", "Lệnh cấm tiếp cận dán trên cửa kính và ổ khóa mới được thay, Betty bị chặn bên ngoài.", "brass deadbolt lock and official court restraining order legal notice taped onto a polished wooden front door"),

    # Hồi 2 (16 chunks)
    ("t14_c12_california_no_fault_divorce_court", "Phòng xử án ly hôn California với dãy bàn luật sư đối địch và ánh sáng xám xịt từ cửa sổ cao.", "grand California divorce courtroom, empty judge bench, cold shafts of grey daylight cut through towering windows"),
    ("t14_c13_legal_asymmetry_paperwork_avalanche", "Chồng hồ sơ kiện tụng dày cộp đè bẹp giấy tờ viết tay nguệch ngoạc của người vợ tự bào chữa.", "mountain of thick bound legal motions and court files towering over a single crumpled handwritten letter, harsh desk lamp"),
    ("t14_c14_dan_calculating_child_support_ledger", "Sổ kế toán liệt kê các khoản trừ tiền phạt vô lý mà Dan áp đặt lên tiền trợ cấp của Betty.", "vintage financial ledger with handwritten deductions, dollar calculations, red ink penalties, cold calculating bureaucracy"),
    ("t14_c15_betty_ramming_car_into_front_door", "Chiếc xe hơi đâm sầm vào cửa chính biệt thự, gạch vỡ và khung cảnh đổ nát trong cơn thịnh nộ.", "front bumper of a car smashed through an elegant suburban front door, shattered glass, debris scattered in dark hall"),
    ("t14_c16_betty_handcuffed_mental_hold_cell", "Cửa sắt nhà tạm giữ giam giữ Betty 72 giờ giám định tâm thần, sự nhục nhã tột cùng.", "heavy steel holding cell bars, dim institutional fluorescent light, solitary shadow cast on stained concrete floor"),
    ("t14_c17_spray_painted_curtains_bizarre_retaliation", "Bức tường phòng khách bị xịt sơn đen loang lổ, phản ứng bộc phát mất kiểm soát của Betty.", "luxurious living room wallpaper and cream curtains defaced with aggressive black paint splatters, chaotic ruined elegance"),
    ("t14_c18_dan_recording_answering_machine_traps", "Cuộn băng cối ghi âm quay chậm trong góc phòng tối, Dan chuẩn bị bẫy ghi âm Betty chửi bới.", "vintage tape recorder with spinning reels in a dark room, red recording indicator light glowing ominously"),
    ("t14_c19_answering_machine_red_light_blinking", "Đèn đỏ máy nhắn tin nhấp nháy liên tục trong đêm, chứa hàng chục tin nhắn đe dọa điên cuồng.", "close-up of an answering machine tape counter and blinking amber alert LED in a dark suburban hallway"),
    ("t14_c20_court_fine_deduction_check_zero", "Tấm séc trợ cấp bị khấu trừ đến mức số tiền thực nhận là 0 đô la, đẩy Betty vào bước đường cùng.", "official bank check showing zero balance after endless court sanctions, stamped with red official seal"),
    ("t14_c21_dan_linda_extravagant_wedding_lawn", "Bãi cỏ biệt thự nơi Dan và Linda tổ chức đám cưới xa hoa với dàn vệ sĩ mặc vest đứng gác.", "lavish white outdoor wedding tent at twilight, armed bodyguards in dark suits standing watch in shadows"),
    ("t14_c22_bodyguards_surrounding_wedding_venue", "Hai vệ sĩ đeo tai nghe bộ đàm đứng cảnh giới trước cổng hoa, Dan lo sợ Betty tấn công.", "two imposing security guards with radio earpieces standing rigid in front of a wealthy estate entrance"),
    ("t14_c23_betty_in_rented_apartment_isolation", "Căn hộ chung cư thuê lạnh lẽo của Betty, đối lập hoàn toàn với cuộc sống thượng lưu ngày trước.", "sparse rented apartment with cardboard boxes, bare lightbulb hanging, solitary silhouette gazing out dark window"),
    ("t14_c24_betty_browsing_gun_store_revolver", "Tủ kính cửa hàng súng với khẩu súng lục ổ quay 38 Smith & Wesson nằm lạnh lẽo trên nhung đỏ.", "vintage gun shop display case, a .38 caliber snub-nose revolver resting on worn black velvet, cold metallic glint"),
    ("t14_c25_box_of_bullets_on_dressing_table", "Hộp đạn bằng đồng mở nắp đặt cạnh lọ nước hoa trên bàn trang điểm, sự chuyển biến nguy hiểm.", "small cardboard box of brass revolver cartridges next to an antique vanity mirror and pearl necklace"),
    ("t14_c26_stolen_house_key_glinting_dawn", "Chùm chìa khóa nhà Dan bị lấy trộm đặt trên ghế xe hơi trong bóng tối rạng sáng.", "brass house key lying on the dark leather seat of a car, dim dashboard glow, predawn eerie darkness"),
    ("t14_c27_car_idling_outside_coral_way_predawn", "Chiếc xe hơi tắt đèn đỗ im lìm dưới rặng cây trước biệt thự Coral Way rạng sáng ngày định mệnh.", "car parked quietly under towering weeping willow trees at predawn, headlights off, looming dark mansion ahead"),

    # Hồi 3 (13 chunks)
    ("t14_c28_psychological_profiling_gaslighting_concept", "Hình ảnh ẩn dụ chiếc đèn gas chập chờn chiếu vào tấm gương nứt vỡ, thao túng thực tại.", "conceptual dark art, an antique flickering gas lamp casting distorted eerie shadows across a cracked ornate mirror"),
    ("t14_c29_shattered_sense_of_reality_maze", "Mê cung bê tông tăm tối với những lối rẽ không lối thoát, sự hoang mang tột độ của nạn nhân.", "gloomy infinite concrete labyrinth viewed from above, claustrophobic fog creeping through narrow damp corridors"),
    ("t14_c30_narcissistic_entitlement_pedestal", "Bức tượng đá cẩm thạch kiêu ngạo đứng trên bệ cao nứt toác, ảo tưởng quyền lực của kẻ ái kỷ.", "cracked marble classical bust statue standing arrogantly on a crumbling pedestal, dramatic theatrical side lighting"),
    ("t14_c31_coercive_control_invisible_puppet_strings", "Đôi bàn tay vô hình điều khiển những sợi dây rối chằng chịt trong bóng đêm, sự kìm kẹp vô hình.", "shadowy hands manipulating tangled marionette strings fading into complete darkness, psychological thriller style"),
    ("t14_c32_victim_reactive_abuse_explosion", "Núi lửa âm ỉ phun trào tro bụi đen kịt, phép ẩn dụ cho phản ứng bạo liệt sau nhiều năm bị áp bức.", "dark brooding conceptual art, violent burst of black volcanic ash and sparks piercing a suffocating night sky"),
    ("t14_c33_darvo_mechanism_spinning_mirrors", "Hệ thống gương phản chiếu làm méo mó sự thật, biến thủ phạm thành nạn nhân.", "endless hall of distorting funhouse mirrors reflecting inverted fragmented silhouettes in deep gloom"),
    ("t14_c34_children_caught_in_crossfire_shadows", "Hai chiếc cặp sách học sinh bỏ quên trên cầu thang lạnh lẽo, những đứa con bị giằng xé.", "two small vintage school backpacks left on a gloomy wooden staircase landing, heavy oppressive atmosphere"),
    ("t14_c35_institutional_blindspot_legal_balance", "Cán cân công lý bị lệch về một bên vì túi tiền và quan hệ chính trị, tòa án San Diego.", "ancient bronze scales of justice tilted heavily to one side under a stack of money envelopes, dark courtroom bench"),
    ("t14_c36_moral_disengagement_mask_of_sanity", "Mặt nạ sứ trắng tinh xảo vỡ đôi làm lộ ra bóng tối mục ruỗng bên trong.", "cracked porcelain theatrical mask split in half revealing pitch-black void inside, chiaroscuro lighting"),
    ("t14_c37_weaponized_intimacy_betrayal", "Bức thư tình cũ ngả vàng bị rạch nát bởi lưỡi dao mổ sắc bén, sự phản bội cay đắng.", "yellowed vintage handwritten love letter sliced diagonally by a sharp surgical scalpel, dark wooden desk"),
    ("t14_c38_point_of_no_return_threshold", "Cánh cửa phòng ngủ mở hé một nửa vào bóng tối sâu thẳm, ranh giới giữa lý trí và tội ác.", "heavy panel door slightly ajar into an utterly black bedroom, narrow blade of cold light cutting across carpet"),
    ("t14_c39_boiling_rage_furnace_darkness", "Lò than âm ỉ cháy đỏ trong tầng hầm tối tăm, ẩn dụ cho cơn thịnh nộ tích tụ hai thập kỷ.", "dark basement boiler furnace glowing with deep crimson embers behind iron grate, suffocating heat in darkness"),
    ("t14_c40_shattered_ego_ideal_ruins", "Tòa lâu đài cát nguy nga bị sóng biển đen ngòm cuốn trôi chỉ còn lại đống đổ nát.", "ruins of an elaborate sandcastle being consumed by violent black nocturnal waves under a stormy sky"),

    # Hồi 4 (15 chunks)
    ("t14_c41_coral_way_mansion_sleeping_predawn", "Biệt thự Coral Way chìm trong giấc ngủ tĩnh lặng lúc 5 giờ sáng, không hề biết hiểm họa sắp tới.", "luxurious two-story San Diego mansion asleep in deep predawn blue shadows, all windows dark and silent"),
    ("t14_c42_unlocked_front_door_swinging_open", "Cánh cửa chính mở hé không phát ra tiếng động, bóng đen lướt vào tiền sảnh.", "front entryway door cracked open silently, darkness inside, faint silhouette stepping across threshold"),
    ("t14_c43_slow_steps_up_carpeted_staircase", "Góc nhìn từ chân cầu thang trải thảm nhung hướng lên tầng 2 tối om, tiếng bước chân rón rén.", "creepy perspective looking up a wide carpeted curved staircase into pitch-black upper hallway, noir dread"),
    ("t14_c44_bedroom_door_creaking_open_shadow", "Cánh cửa phòng ngủ master mở ra, hai bóng người đang ngủ say trên chiếc giường lớn.", "bedroom door slowly pushing open, faint moonlight revealing silhouette of a massive king-size bed"),
    ("t14_c45_muzzle_flashes_in_darkened_room", "Ánh chớp lửa đầu nòng xé toạc bóng đêm phòng ngủ, năm phát đạn định mệnh xé toạc không gian.", "sudden violent bright orange muzzle flash illuminating a dark bedroom in high contrast noir style"),
    ("t14_c46_severed_telephone_cord_nightstand", "Dây điện thoại bàn đầu giường bị giật đứt lìa rơi xuống sàn thảm cạnh vết đạn.", "close-up of a ripped telephone cord hanging limply from a vintage bedside phone, receiver dangling"),
    ("t14_c47_dan_final_words_floor_shadows", "Bóng đen ngã quỵ trên thảm cạnh giường, chiếc gối lụa rơi xuống, những lời nói cuối cùng.", "dramatic crime scene shadows on hardwood floor, crumpled bedsheet trailing off mattress, solemn silence"),
    ("t14_c48_betty_fleeing_in_car_morning_fog", "Chiếc xe hơi lao đi trong màn sương mù dày đặc buổi sáng San Diego sau khi tiếng súng dứt.", "vintage station wagon speeding away down a misty coastal road at dawn, taillights fading into gloom"),
    ("t14_c49_turning_herself_in_police_station", "Bóng Betty đứng lặng trước quầy trực ban đồn cảnh sát La Jolla lúc bình minh để đầu thú.", "silhouette of a woman standing motionless in front of a cold brick police station lobby desk at dawn"),
    ("t14_c50_sensational_newspapers_headline_stands", "Kệ bán báo ven đường ngập tràn tiêu đề chấn động về vụ luật sư bị vợ cũ bắn chết.", "vintage newspaper kiosk overflowing with black-and-white tabloids and sensational murder headlines"),
    ("t14_c51_media_circus_outside_courthouse", "Đám đông phóng viên và máy quay phim chen chúc trước bậc thềm tòa án San Diego.", "swarming crowd of vintage 1990 photojournalists and news cameras outside towering courthouse steps"),
    ("t14_c52_betty_in_blue_dress_defense_bench", "Betty mặc váy xanh chỉnh tề ngồi cạnh luật sư bào chữa Jack Early, nét mặt chai sạn.", "somber courtroom scene, woman in conservative dress sitting beside defense attorney, dramatic chiaroscuro"),
    ("t14_c53_hung_jury_first_trial_deadlock", "Phòng nghị án bỏ hoang với 12 chiếc ghế trống và tập phiếu bầu bế tắc 10-2, phiên tòa đầu tiên.", "empty jury deliberation room, scattered ballot papers and half-empty coffee cups on large table, deadlock"),
    ("t14_c54_second_trial_second_degree_verdict", "Thẩm phán gõ búa tuyên án 32 năm tù đến chung thân, bản án khép lại bi kịch.", "wooden judge gavel resting on courtroom bench next to official sentencing document, cold finality"),
    ("t14_c55_california_institution_for_women_gates", "Cổng sắt hàng rào thép gai của Trại giam Phụ nữ Frontera California đóng sập lại.", "monolithic barbed wire prison security gates slamming shut, gloomy California desert mountains in distance"),

    # Hồi 5 (13 chunks)
    ("t14_c56_frontera_prison_cell_aging_betty", "Bóng người phụ nữ lớn tuổi ngồi sau song sắt nhìn qua ô cửa sổ nhỏ, năm tháng trôi qua.", "solitary silhouette of an aging woman seated inside a stark prison cell, narrow beam of dusty sunlight"),
    ("t14_c57_parole_board_denial_stamped_file", "Hồ sơ xin ân xá bị đóng dấu đỏ từ chối (DENIED) trên bàn hội đồng ân xá.", "official prison parole board dossier stamped in bold red ink DENIED, solemn bureaucratic rejection"),
    ("t14_c58_battered_wife_vs_scorned_killer_dichotomy", "Bức tranh hai mặt đối lập: một bên là người vợ bị bạo hành, một bên là kẻ sát nhân lạnh lùng.", "symbolic dual portrait silhouette, one side crying in shadow, other side hardened in stone, psychological study"),
    ("t14_c59_the_gift_of_fear_warning_signs", "Trang sách mở ra với những dòng gạch chân về cảnh báo trực giác và sự leo thang bạo lực.", "open vintage psychology book on wooden lectern, prominent underlined sentences in dark ink, moody lighting"),
    ("t14_c60_financial_asymmetry_red_flag_vault", "Két sắt ngân hàng mở toang nhưng trống rỗng, biểu tượng của sự bóp nghẹt tài chính có chủ đích.", "massive steel bank vault door open slightly, empty safe deposit boxes inside, metaphor of financial control"),
    ("t14_c61_systematic_denial_shattered_compass", "Chiếc la bàn cổ bị vỡ mặt kính, kim chỉ xoay vô định, biểu tượng mất phương hướng thực tại.", "antique brass pocket compass with cracked glass face, needle spinning wildly, resting on weathered sea map"),
    ("t14_c62_legal_scorched_earth_barren_field", "Cánh đồng cháy rụi chỉ còn tro tàn và hàng rào đổ nát, phép ẩn dụ cho chiến dịch tiêu diệt đối phương.", "bleak scorched earth field under bruised purple twilight sky, smoking charred fence posts, total devastation"),
    ("t14_c63_loss_of_proportionality_cliff_edge", "Bóng người đứng trên bờ vực chênh vênh trước cơn bão biển dữ dội, mất hết sự cân nhắc hậu quả.", "solitary silhouette standing precariously on a jagged sea cliff edge facing violent oceanic tempest, vertigo"),
    ("t14_c64_the_trap_of_reactive_violence", "Chiếc bẫy thép săn thú giương sẵn phủ đầy lá mục trong rừng tối, lời cảnh tỉnh cho nạn nhân.", "heavy rusted iron bear trap lying in wait among dark rotting autumn leaves on foggy forest floor"),
    ("t14_c65_walking_away_to_survive_path", "Lối đi mòn rẽ sang hướng khác băng qua đồi cỏ mùa thu lúc bình minh, lựa chọn buông bỏ để sống.", "narrow footpath leading away from dark forest towards misty dawn horizon, quiet solemn redemption"),
    ("t14_c66_healing_and_rebuilding_safe_haven", "Ngọn đèn bão nhỏ ấm áp thắp sáng góc hiên nhà gỗ mộc mạc, sự bình yên tìm lại sau đổ vỡ.", "dim kerosene lantern hanging outside a weathered coastal wooden cabin, quiet safe shelter from rain"),
    ("t14_c67_amber_eyes_investigation_dossier_seal", "Bìa hồ sơ lưu trữ Amber Eyes đóng dấu sáp màu hổ phách, khép lại vụ án Betty Broderick.", "closed vintage crime dossier file tied with black string and sealed with amber wax stamp, desk lamp glow"),
    ("t14_c68_final_closing_words_calm_ocean", "Mặt biển La Jolla mênh mông lúc rạng đông với những gợn sóng tĩnh lặng, lời cảnh tỉnh muôn đời.", "vast calm Pacific ocean horizon at pale dawn, gentle mist rolling over slate water, profound quiet reflection")
]

STYLE_PREFIX = "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
MOOD_CORE = "gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
NEGATIVE_SUFFIX = "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, full-bleed 16:9."

final_68_jobs = []
for i in range(68):
    ch = chunks[i]
    name, desc_vi, prompt_core = meta[i]
    act = ch[0]['act']
    sent_str = ch[0]['id'] if len(ch) == 1 else f"{ch[0]['id']}–#{ch[-1]['id'].split('#')[1]}"
    
    full_prompt = f"{STYLE_PREFIX}{prompt_core}, {MOOD_CORE}{NEGATIVE_SUFFIX}"
    
    final_68_jobs.append({
        "stt": i + 1,
        "name": name,
        "act": act,
        "sentences": sent_str,
        "desc": desc_vi,
        "prompt": full_prompt
    })

# Save to .work/bg_jobs_tap14_extra68.json
with open('.work/bg_jobs_tap14_extra68.json', 'w', encoding='utf-8') as f:
    json.dump(final_68_jobs, f, ensure_ascii=False, indent=2)

print("Saved 68 jobs to .work/bg_jobs_tap14_extra68.json successfully!")
