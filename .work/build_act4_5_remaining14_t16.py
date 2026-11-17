import json

meta_14 = [
    # 2 ảnh còn lại của Hồi 4:
    ("t16_a4_c11_fingerprint_card_matching_records", 4, "4.10#2–#6", "Thẻ lăn tay đối chiếu dấu vân tay của Bob Clark khớp hoàn toàn với hồ sơ quân ngũ 1944 của John List.", "forensic fingerprint comparison card under magnifying glass, black ink ridges matching perfectly, official RED MATCH stamp"),
    ("t16_a4_c12_courthouse_steps_westfield_return", 4, "4.12#2–#4", "Bóng John List bị áp giải bước lên bậc thềm đá tòa án Hạt Union bang New Jersey đối diện công lý.", "handcuffed silhouette of John List flanked by US Marshals ascending grand granite steps of New Jersey courthouse under heavy gray skies"),

    # 12 ảnh của Hồi 5:
    ("t16_a5_c01_sentencing_five_life_terms", 5, "5.02#2", "Thẩm phán William Wertheimer gõ búa tuyên phạt 5 bản án tù chung thân liên tiếp, mức án nghiêm khắc nhất.", "heavy wooden judge gavel resting on courtroom bench next to official sentencing document reading FIVE CONSECUTIVE LIFE TERMS, solemn justice"),
    ("t16_a5_c02_unrepentant_cold_stare_defense", 5, "5.02#6", "Ánh mắt lạnh lùng không chút hối hận của John List khi bị áp giải rời phòng xử án, chiếc mặt nạ đạo đức giả.", "close-up silhouette profile of an unrepentant aging man in prison uniform, icy emotionless gaze, stark chiaroscuro lighting"),
    ("t16_a5_c03_trenton_prison_cemetery_tombstone", 5, "5.03#2–#3", "Khu nghĩa trang nhà tù bang New Jersey lạnh lẽo dưới màn mưa phùn, nơi John List trút hơi thở cuối cùng năm 2008.", "stark unmarked prison cemetery grave under gray drizzle, rusting iron fence, bleak desolate atmosphere, finality of justice"),
    ("t16_a5_c04_tyrannical_family_patriarch_throne", "5", "5.04#2–#3", "Chiếc ghế gia trưởng bọc nhung rách nát trên bục cao phủ đầy bóng tối, biểu tượng quyền kiểm soát độc hại.", "ornate antique wooden armchair on elevated platform casting long monstrous shadow on crumbling wall, psychological metaphor"),
    ("t16_a5_c05_accepting_vulnerability_open_hands", 5, "5.04#4–#5", "Đôi bàn tay mở ra hướng về ánh sáng yếu ớt lúc bình minh, biểu tượng chấp nhận sự tổn thương và thất bại để cứu vãn gia đình.", "pair of open weathered hands illuminated by gentle pale dawn light emerging from pitch darkness, solemn philosophical hope"),
    ("t16_a5_c06_redflag1_rigid_perfectionism_barracks", 5, "5.05#2–#3", "Phòng ăn gia đình rập khuôn rập rạp như doanh trại quân đội, bộ dao nĩa thẳng tắp không được xê dịch một milimet.", "dining table set with fanatical obsessive precision, silver cutlery aligned mathematically, dark suffocating domestic prison"),
    ("t16_a5_c07_redflag2_financial_deceit_vault", 5, "5.05#4–#5", "Chiếc két sắt gia đình khóa kín với những bức thư báo nợ giấu sau tranh treo tường, sự chối bỏ thực tại tài chính.", "hidden safe behind an oil painting cracked open showing eviction notices and debt warnings, dramatic investigative noir"),
    ("t16_a5_c08_transparency_and_shared_honesty", 5, "5.05#6–#7", "Bàn ăn mộc mạc nơi hai bàn tay nắm chặt nhau qua ánh đèn dầu ấm áp, sự chia sẻ và minh bạch cùng vượt qua khủng hoảng.", "two hands clasped firmly across a rustic wooden table beside a warm oil lamp, peaceful contrast to toxic secrecy"),
    ("t16_a5_c09_redflag3_religious_weaponization_altar", 5, "5.05#8–#9", "Cuốn kinh thánh bị dùng làm vũ khí thao túng, bóng cây thánh giá đổ dài đè nặng lên những bức ảnh gia đình.", "heavy dark shadow of a crucifix looming oppressively over small framed family snapshots on table, psychological control"),
    ("t16_a5_c10_healthy_faith_shield_comfort", 5, "5.05#10–#11", "Cửa sổ kính màu nhà thờ cổ chiếu rọi ánh sáng thanh khiết, đức tin chân chính chở che thay vì bóp nghẹt mạng sống.", "soft daylight filtering through ancient cathedral stained-glass window, illuminating an open peaceful doorway, quiet sanctuary"),
    ("t16_a5_c11_redflag4_toxic_isolation_locked_gate", 5, "5.05#12–#13", "Cánh cổng sắt gai quấn xích khóa chặt ngăn cách ngôi nhà với thế giới bên ngoài, dấu hiệu cô lập gia đình cực đoan.", "heavy iron estate gate chained tight with massive padlock, dry autumn leaves trapped in bars, total domestic isolation"),
    ("t16_a5_c12_listening_to_the_cries_helping_hand", 5, "5.05#14", "Một bàn tay đưa ra nắm lấy bàn tay đang chới với trong sương mù, thông điệp lắng nghe tiếng kêu cứu trước bờ vực bi kịch.", "one helping hand reaching down into dark mist to grasp a trembling hand, poignant dramatic noir lighting, redemption"),
    ("t16_a5_c13_amber_eyes_closing_dossier_list", 5, "5.05#15", "Bìa hồ sơ chuyên án Amber Eyes đóng kín, đóng dấu niêm phong màu hổ phách bên cạnh tách trà ấm, khép lại vụ án John List.", "closed vintage leather dossier file tied with black ribbon, glowing amber wax seal, desk lamp illuminating forensic notes, closure")
]

# We need exactly 2 of Act 4 + 12 of Act 5 = 14 jobs!
# Let's adjust meta to exactly 14 items
jobs_14 = []
STYLE_PREFIX = "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
MOOD_CORE = "gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
NEGATIVE_SUFFIX = "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, full-bleed 16:9."

for i, item in enumerate(meta_14[:14], 1):
    name, act, sent_str, desc_vi, prompt_core = item[0], int(item[1]), item[2], item[3], item[4]
    full_prompt = f"{STYLE_PREFIX}{prompt_core}, {MOOD_CORE}{NEGATIVE_SUFFIX}"
    jobs_14.append({
        "stt": i,
        "name": name,
        "act": act,
        "sentences": sent_str,
        "desc": desc_vi,
        "prompt": full_prompt
    })

with open('.work/bg_jobs_tap16_act4_5_remaining14.json', 'w', encoding='utf-8') as f:
    json.dump(jobs_14, f, ensure_ascii=False, indent=2)

print("Saved 14 remaining jobs for Tap 16 to .work/bg_jobs_tap16_act4_5_remaining14.json successfully!")
