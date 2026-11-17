import json

meta_12 = [
    ("t16_a1_c01_breeze_knoll_victorian_facade", "Dinh thự phong cách Victoria 19 phòng Breeze Knoll sừng sững trong sương mù lạnh lẽo của mùa đông 1971, các cửa sổ đóng kín đen kịt.", "sprawling 19-room dark Victorian gothic mansion Breeze Knoll at twilight, towering turrets, dense cold winter fog rolling across barren lawn, windows dark and dead"),
    ("t16_a1_c02_john_list_conservative_suit_silhouette", "Bóng John List trong bộ vest bảo thủ kiểu thập niên 1970 và cặp kính gọng sừng, đứng nghiêm nghị trong phòng khách tối tăm.", "silhouette of a stern rigid man in a conservative dark suit and retro thick-rimmed glasses, standing motionless in a dimly lit Victorian parlor, intense chiaroscuro"),
    ("t16_a1_c03_breeze_knoll_grand_hall_shadows", "Đại sảnh biệt thự với cầu thang gỗ sồi đồ sộ và những bức chân dung tổ tiên u ám nhìn xuống, vẻ hào nhoáng che đậy sự khánh kiệt.", "cavernous grand entrance hall of an old wealthy estate, massive dark oak staircase curving upwards into shadow, dusty chandelier, oppressive silence"),
    ("t16_a1_c04_unemployment_bank_deficit_letters", "Bàn làm việc với những lá thư sa thải từ ngân hàng và thông báo thấu chi tài chính bị giấu kín dưới ngăn kéo khóa chặt.", "vintage mahogany desk drawer slightly pulled out revealing bank termination notice and overdue debt statements under a dim brass lamp"),
    ("t16_a1_c05_john_pretending_train_commute", "Bóng John List cầm cặp táp da ngồi cô độc trên ghế băng ga tàu điện ngầm New York, giả vờ đi làm mỗi ngày suốt nhiều tháng.", "solitary silhouette of an accountant with a leather briefcase sitting on an empty cold commuter train platform in early morning winter gloom"),
    ("t16_a1_c06_patricia_theater_script_bedroom", "Phòng ngủ cô con gái lớn Patricia với tập kịch bản sân khấu và ánh đèn bàn học nhỏ, ước mơ tự do bị bóp nghẹt bởi người cha bảo thủ.", "moody teenage bedroom with theater script and drama playbooks on desk, solitary warm lamp struggling against suffocating room shadows"),
    ("t16_a1_c07_snow_covered_porch_unread_mail", "Bậc thềm hiên nhà Breeze Knoll phủ đầy tuyết trắng với hàng chục tờ báo và thư từ bị bỏ mặc không ai lấy suốt gần một tháng.", "snow-covered front porch of Breeze Knoll mansion, large pile of unread yellowing newspapers and frozen mail stacked against the heavy locked front door"),
    ("t16_a1_c08_police_flashlight_entering_window", "Ánh đèn pin tuần tra của cảnh sát xé toạc bóng đêm chiếu qua ô cửa sổ kính tầng trệt bị cạy mở rạng sáng ngày 7 tháng 12.", "dramatic sharp beam of a police flashlight cutting through a broken ground-floor window into a pitch-black dusty abandoned hallway"),
    ("t16_a1_c09_freezing_corridor_silent_mansion", "Hành lang dài băng giá bên trong biệt thự với hệ thống sưởi bị tắt có chủ đích, hơi lạnh bốc lên mờ ảo trong ánh đèn rọi.", "long freezing grand corridor of an empty mansion, breath mist visible in flashlight beam, peeling wallpaper, eerie stillness, cold forensic atmosphere"),
    ("t16_a1_c10_ballroom_sleeping_bags_tiffany_skylight", "Căn phòng khiêu vũ nguy nga rộng lớn với trần kính màu Tiffany đắt giá, nơi bốn thi thể nằm xếp ngay ngắn trong túi ngủ trên sàn gỗ.", "vast cavernous dark ballroom with an exquisite stained-glass Tiffany skylight dome above, shadowy crime scene markers on polished floor, haunting dread"),
    ("t16_a1_c11_confession_letter_five_pages_pastor", "Lá thư thú tội 5 trang viết tay đặt cạnh chiếc gạt tàn và khẩu súng đã cạn đạn trên bàn ăn, John gửi mục sư giải thích hành vi sát hại.", "close-up of a neat five-page handwritten confession letter lying beside a cold vintage revolver and empty shell casings on a polished dining table"),
    ("t16_a1_c12_chevrolet_impala_abandoned_airport", "Chiếc xe Chevrolet Impala màu xanh phủ đầy tuyết trắng nằm im lìm trong bãi đỗ xe sân bay JFK, hung thủ đã biến mất không dấu vết.", "vintage 1960s Chevrolet sedan covered in thick snow, parked abandoned in a dark airport parking lot at night, blizzard howling")
]

STYLE_PREFIX = "A masterpiece graphic novel noir illustration, dark investigative crime dossier aesthetic, bold black ink linework, high contrast psychological chiaroscuro lighting, deep pitch-black shadows, "
MOOD_CORE = "gloomy overcast suffocating pale grey sky, cold mist floating over the ground, unsettling silence, creeping psychological dread, hidden crime scene atmosphere, faded eerie retro colors, decayed autumn tones, fine 35mm film grain, David Fincher meets vintage crime comic style, "
NEGATIVE_SUFFIX = "Strictly no vibrant colors, no cheerful sunlight, no bright blue sky, no warm golden glow, no 3D render, no CGI, no photorealism, strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, no watermark, full-bleed 16:9."

jobs_12 = []
for i, item in enumerate(meta_12, 1):
    name, desc_vi, prompt_core = item
    full_prompt = f"{STYLE_PREFIX}{prompt_core}, {MOOD_CORE}{NEGATIVE_SUFFIX}"
    jobs_12.append({
        "stt": i,
        "name": name,
        "act": 1,
        "desc": desc_vi,
        "prompt": full_prompt
    })

with open('.work/bg_jobs_tap16_act1_12.json', 'w', encoding='utf-8') as f:
    json.dump(jobs_12, f, ensure_ascii=False, indent=2)

print("Saved 12 jobs for Tap 16 Act 1 to .work/bg_jobs_tap16_act1_12.json successfully!")
