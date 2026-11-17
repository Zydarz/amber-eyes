import json

meta_15 = [
    ("t16_a2_c01_detectives_dusting_empty_frames", "Các thám tử rọi đèn pin và phủ bột tìm dấu vân tay trên những khung ảnh trống rỗng tại hiện trường Breeze Knoll.", "two 1970s detectives in trench coats using flashlights and fingerprint powder on empty vintage picture frames on wall, dark moody crime scene"),
    ("t16_a2_c02_family_album_cutout_faces", "Quyển album ảnh gia đình bìa da cũ mở ra trên bàn, toàn bộ khuôn mặt của John List đã bị cắt đục lỗ kỳ quái.", "vintage leather-bound family photo album open on wooden table, eerie oval silhouette holes where the father face was meticulously cut out"),
    ("t16_a2_c03_sharp_scissors_cut_photos_floor", "Chiếc kéo sắc nhọn đặt cạnh những mảnh giấy ảnh vụn vương vãi trên sàn nhà phủ bụi, sự toan tính xóa bỏ nhân dạng.", "pair of sharp metal tailor scissors lying beside small oval cut-out photo scraps scattered on dusty floorboards, intense chiaroscuro"),
    ("t16_a2_c04_shredded_birth_certificates_records", "Giấy khai sinh và hồ sơ nghĩa vụ quân sự cũ bị xé vụn trong lò sưởi, John List chủ động khai tử thân phận cũ.", "charred fragments of paper identity documents and military records in cold brick fireplace, ashes and dark embers"),
    ("t16_a2_c05_erasing_past_identity_metaphor", "Bóng người đàn ông đứng trước tấm gương phủ đầy hơi sương dùng khăn lau mờ khuôn mặt mình, sự biến mất có tính toán.", "metaphorical noir scene, silhouette of a middle-aged man wiping steam from a mirror completely blurring his own facial reflection"),
    ("t16_a2_c06_vintage_radio_humming_hymns", "Chiếc đài radio cổ điển phát ra những bản thánh ca tôn giáo trầm buồn giữa căn phòng trống vắng không một bóng người.", "vintage 1970s wooden table radio glowing softly with faint amber tuner light in an empty dark dining room, eerie religious ambiance"),
    ("t16_a2_c07_thermostat_cranked_freezing_cold", "Bộ điều nhiệt lò sưởi trên tường được vặn xuống mức nhiệt độ thấp nhất, hơi băng giá bao phủ biệt thự bảo quản hiện trường.", "close-up of an old wall thermostat dial turned down to freezing cold, thin layer of frost creeping on dial edge in darkness"),
    ("t16_a2_c08_fbi_wanted_poster_hundreds_stamps", "Tấm áp phích truy nã toàn liên bang FBI dán trên bảng thông báo bưu điện với dấu mộc truy tìm hung thủ John List.", "vintage FBI wanted poster featuring black and white composite sketch of John List, pinned on weathered cork bulletin board in dark post office"),
    ("t16_a2_c09_mysterious_fire_breeze_knoll_ruins", "Ngọn lửa bí ẩn thiêu rụi dinh thự Breeze Knoll vào tháng 8 năm 1972, tàn tro và những cột gỗ cháy đen trong đêm.", "massive dark gothic Victorian mansion engulfed in raging midnight fire, black smoke billowing into stormy clouds, tragic ruins"),
    ("t16_a2_c10_cold_case_dossier_growing_dust", "Tập hồ sơ chuyên án án mạng Breeze Knoll nằm im lìm trên kệ lưu trữ của sở cảnh sát, lớp bụi dày theo năm tháng.", "thick manila cold case police archive file labeled WESTFIELD 1971 gathering heavy dust on metal shelving unit in dim records room"),
    ("t16_a2_c11_detectives_studying_ocpd_profile", "Hai điều tra viên lớn tuổi soi kính lúp nghiên cứu hồ sơ tính cách bảo thủ và thói quen ám ảnh của nghi phạm.", "two seasoned detectives under green banker desk lamp studying psychological profile documents and old handwritten accounting logs"),
    ("t16_a2_c12_accountant_ledger_red_ink_cracking", "Cuốn sổ cái kế toán ngập tràn các dòng số ghi bằng mực đỏ thâm hụt, gánh nặng tài chính đè bẹp sự tôn nghiêm gia trưởng.", "close-up of an old financial accounting ledger filled with red ink deficit figures and stressed pencil calculations in fading light"),
    ("t16_a2_c13_cognitive_dissonance_moral_trap", "Chiếc cân đồng thau cân bằng giữa cuốn kinh thánh và chiếc chìa khóa két sắt rỗng, sự mâu thuẫn đạo đức cực đoan.", "ancient brass balance scale weighing a worn leather Bible against an empty safe deposit key, dramatic psychological symbolism"),
    ("t16_a2_c14_psychological_mechanism_rigid_gears", "Bánh răng đồng thau khổng lồ của chiếc đồng hồ cơ khí quay cứng nhắc trong bóng tối, ẩn dụ cho sự rập khuôn của hội chứng OCPD.", "monumental dark clockwork brass gears interlocked tightly, motionless and rigid in atmospheric gloom, metaphor for obsessive compulsion"),
    ("t16_a2_c15_psychologist_opening_dossier_threshold", "Bàn làm việc của Chuyên gia tâm lý với ngọn đèn bàn ấm áp và tập hồ sơ hé mở, chuẩn bị giải phẫu góc khuất tâm lý hung thủ.", "psychologist polished mahogany desk with warm amber lamp, open confidential psychological assessment dossier, analytical focus")
]

STYLE_PREFIX = "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
MOOD_CORE = "gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
NEGATIVE_SUFFIX = "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, full-bleed 16:9."

jobs_15 = []
for i, item in enumerate(meta_15, 1):
    name, desc_vi, prompt_core = item
    full_prompt = f"{STYLE_PREFIX}{prompt_core}, {MOOD_CORE}{NEGATIVE_SUFFIX}"
    jobs_15.append({
        "stt": i,
        "name": name,
        "act": 2,
        "desc": desc_vi,
        "prompt": full_prompt
    })

with open('.work/bg_jobs_tap16_act2_15.json', 'w', encoding='utf-8') as f:
    json.dump(jobs_15, f, ensure_ascii=False, indent=2)

print("Saved 15 jobs for Tap 16 Act 2 to .work/bg_jobs_tap16_act2_15.json successfully!")
