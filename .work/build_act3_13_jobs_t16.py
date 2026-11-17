import json

meta_13 = [
    ("t16_a3_c01_family_annihilator_shadowy_hall", "Bóng đen người đàn ông đứng ở ngã ba hành lang tối tăm, ẩn dụ cho khái niệm kẻ hủy diệt gia đình (Family Annihilator).", "monumental dark graphic novel noir scene, solitary silhouette of a family patriarch standing at the intersection of empty decaying corridors, chilling psychological dread"),
    ("t16_a3_c02_ocpd_versus_ocd_distorted_mirror", "Tấm gương nứt đôi phản chiếu hai khuôn mặt: một bên dằn vặt hoảng loạn (OCD), một bên lạnh lùng tự mãn cứng nhắc (OCP-D).", "cracked antique mirror reflecting a split psychological duality, one side distorted in panic, other side rigid stone-cold narcissistic perfection, chiaroscuro lighting"),
    ("t16_a3_c03_strict_puritanical_childhood_bible", "Căn phòng ngủ thời thơ ấu khắc khổ với chiếc bàn học gỗ mộc, cây thước kẻ thẳng tắp và cuốn kinh thánh cũ dưới kỷ luật hà khắc.", "stark austere 1930s childhood bedroom with wooden ruler placed mathematically parallel to an ancient Bible under harsh direct light"),
    ("t16_a3_c04_chasm_between_perfection_ruin", "Một vết nứt địa chấn chia đôi sàn nhà đá cẩm thạch sang trọng, tượng trưng cho khoảng cách giữa chiếc mặt nạ danh dự và bờ vực phá sản.", "deep jagged fault line splitting a luxurious marble floor in half, darkness yawning beneath the polished surface, high contrast noir"),
    ("t16_a3_c05_desperate_embezzlement_mother_fund", "Bàn tay đeo găng mở trộm phong bì tiền tiết kiệm của người mẹ già trong ngăn kéo tủ thờ, sự suy đồi đạo đức lén lút.", "close-up of a gloved hand quietly sliding cash out of an elderly mother envelope in a dark mahogany drawer, faint amber candlelight"),
    ("t16_a3_c06_helen_bedridden_medicine_bottles", "Phòng ngủ người vợ Helen với rèm cửa buông kín và hàng loạt lọ thuốc an thần rải rác trên bàn cạnh giường, biểu hiện suy sụp.", "dimly lit sickroom with drawn heavy drapes, silhouette of a bed in deep shadow, bedside table cluttered with vintage medicine bottles"),
    ("t16_a3_c07_moral_disengagement_scales_sin", "Cán cân đạo đức bị bóp méo, nơi cái chết của người thân bị ngụy biện thành hành động cứu rỗi linh hồn vào thiên đàng.", "conceptual dark art, symbolic bronze scales weighing a cold revolver against angelic white wings in heavy creeping mist, chilling delusion"),
    ("t16_a3_c08_selfish_preservation_masked_piety", "Bóng John List quỳ gối cầu nguyện trước bàn thờ nhưng mắt liếc nhìn chiếc va li tiền và vé xe buýt chuẩn bị đào tẩu.", "silhouette kneeling before a wooden altar, side glance toward a packed leather travel suitcase and bus ticket in shadow, hypocrisy"),
    ("t16_a3_c09_cognitive_compartmentalization_cabinet", "Chiếc tủ chia ngăn bí mật với những hộc tủ khóa kín độc lập, ẩn dụ cơ chế chia ngăn tâm lý cắt đứt quá khứ tội ác.", "massive antique wooden apothecary cabinet with dozens of small locked drawers, key in one lock, metaphor for mental compartmentalization"),
    ("t16_a3_c10_cross_country_bus_rainy_window", "Góc nhìn qua ô cửa kính xe buýt mờ nước mưa ban đêm băng qua những thị trấn miền Tây hoang vắng, John List xóa dấu vết.", "view from inside a vintage 1970s Greyhound bus, rain streaming down window pane, passing desolate neon motel signs into dark wilderness"),
    ("t16_a3_c11_denver_church_choir_hymn_books", "Hàng ghế nhà thờ Lutheran ở Denver với những cuốn sách thánh ca mở sẵn, nơi John List xây dựng vỏ bọc tín đồ ngoan đạo mới mang tên Bob Clark.", "empty pews of a quiet Denver Lutheran church, rows of worn hymn books, pale shafts of sunlight cutting through dusty stained glass"),
    ("t16_a3_c12_suburban_denver_modest_house", "Ngôi nhà gỗ ngoại ô giản dị tại Denver dưới rặng cây phong mùa thu, cuộc sống gia đình thứ hai bình thản đến rợn người.", "modest 1980s suburban Denver ranch-style house at dusk, yellow porch light, serene peaceful exterior concealing dark past"),
    ("t16_a3_c13_hand_of_justice_approaching_clock", "Chiếc đồng hồ cát cổ với những hạt cát cuối cùng đang rơi xuống, thời khắc đền tội sau 18 năm cận kề.", "vintage ornate brass hourglass with dark sand running out, ominous shadowy silhouette of justice approaching from background")
]

STYLE_PREFIX = "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
MOOD_CORE = "gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
NEGATIVE_SUFFIX = "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, full-bleed 16:9."

jobs_13 = []
for i, item in enumerate(meta_13, 1):
    name, desc_vi, prompt_core = item
    full_prompt = f"{STYLE_PREFIX}{prompt_core}, {MOOD_CORE}{NEGATIVE_SUFFIX}"
    jobs_13.append({
        "stt": i,
        "name": name,
        "act": 3,
        "desc": desc_vi,
        "prompt": full_prompt
    })

with open('.work/bg_jobs_tap16_act3_13.json', 'w', encoding='utf-8') as f:
    json.dump(jobs_13, f, ensure_ascii=False, indent=2)

print("Saved 13 jobs for Tap 16 Act 3 to .work/bg_jobs_tap16_act3_13.json successfully!")
