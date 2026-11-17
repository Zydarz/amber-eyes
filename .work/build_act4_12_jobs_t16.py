import json

meta_12 = [
    ("t16_a4_c01_yellowed_mugshot_challenge", "Bức ảnh chân dung đen trắng mờ ố vàng năm 1971 của John List nằm trên bàn làm việc của đài truyền hình FOX, thách thức nhận dạng sau 18 năm.", "single yellowed vintage 1971 passport photo of John List resting on a messy television production desk beside broadcast microphones, heavy shadows"),
    ("t16_a4_c02_frank_bender_sculpting_studio", "Xưởng điêu khắc pháp y của Frank Bender ngổn ngang đất sét, dụng cụ tạo hình giải phẫu và các bản đo hộp sọ người.", "forensic artist studio filled with gray sculpting clay, anatomy calipers, human skull models, solitary intense desk lamp in dark room"),
    ("t16_a4_c03_richard_walter_profiler_notes", "Bản ghi chép tâm lý học hành vi của chuyên gia Richard Walter phân tích sự thoái hóa cơ mặt và thói quen bảo thủ của người mang hội chứng OCPD.", "handwritten criminal psychology profiling notes and facial muscle aging sketches under green banker lamp, analytical forensic atmosphere"),
    ("t16_a4_c04_clay_bust_aging_features_glasses", "Bức tượng bán thân bằng đất sét hoàn thiện của John List khi 64 tuổi với vầng trán hói, bọng mắt chảy xệ và cặp kính gọng đồi mồi cổ điển.", "completed hyper-realistic clay bust sculpture of an aging man with sagging jowls and vintage horn-rimmed glasses, dramatic chiaroscuro spotlight"),
    ("t16_a4_c05_americas_most_wanted_broadcast_screen", "Màn hình tivi CRT thập niên 1980 phát sóng chương trình America's Most Wanted với hình ảnh bức tượng Frank Bender trong phòng khách tối.", "glow of an old 1980s cathode-ray tube television screen in a darkened living room, broadcasting the ominous forensic clay bust sculpture"),
    ("t16_a4_c06_wanda_flannery_watching_tv_shock", "Bóng người phụ nữ ngồi chết lặng trên ghế bành trước tivi lúc nửa đêm, nhận ra người hàng xóm cũ Bob Clark giống hệt bức tượng.", "silhouette of an elderly woman freezing in terror on living room armchair, television light illuminating her wide eyes in pitch-black room"),
    ("t16_a4_c07_suburban_richmond_quiet_culdesac", "Khu phố ngoại ô Richmond Virginia thanh bình dưới bóng cây phong, nơi John List dưới thân phận Bob Clark lẩn trốn cùng người vợ mới Delores.", "quiet suburban Richmond Virginia cul-de-sac at twilight, neat lawns and colonial houses, eerie silence concealing a fugitive"),
    ("t16_a4_c08_newspaper_clipping_glance_suspicion", "Mảnh báo cắt bài viết về vụ án John List trên bàn trà phòng khách mà người hàng xóm từng tình cờ nhìn thấy, sự nghi ngờ âm ỉ.", "creased newspaper clipping about the Westfield murders resting on an antique coffee table next to a cup of black coffee"),
    ("t16_a4_c09_telephone_call_hotline_tip", "Bàn tay nhấc ống nghe điện thoại quay số cổ điển trong đêm gọi đến đường dây nóng FBI, cuộc điện thoại định mệnh kết thúc 18 năm.", "hand firmly lifting the receiver of a black rotary wall telephone in a dim kitchen, dramatic tension, tipping off the authorities"),
    ("t16_a4_c10_fbi_arrest_accounting_office", "Hai đặc vụ FBI mặc vest tối màu ập vào văn phòng kế toán Richmond, còng tay người đàn ông trung niên mang kính đang ngồi làm sổ sách.", "two sharp-dressed FBI agents entering a small quiet accounting office, handcuffing a rigid bespectacled man behind his desk, solemn arrest"),
    ("t16_a4_c11_fingerprint_card_matching_records", "Tờ thẻ lăn tay đối chiếu dấu vân tay của Bob Clark khớp hoàn toàn với hồ sơ quân ngũ năm 1944 của John List, danh tính lộ diện.", "forensic fingerprint comparison card under magnifying glass, black ink ridges matching perfectly, official RED MATCH stamp"),
    ("t16_a4_c12_courthouse_steps_westfield_return", "Bóng John List bị áp giải bước lên bậc thềm đá tòa án Hạt Union bang New Jersey, sự trở lại sau hai thập kỷ đối mặt công lý.", "handcuffed silhouette of John List flanked by US Marshals ascending grand granite steps of New Jersey courthouse under heavy gray skies")
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
        "act": 4,
        "desc": desc_vi,
        "prompt": full_prompt
    })

with open('.work/bg_jobs_tap16_act4_12.json', 'w', encoding='utf-8') as f:
    json.dump(jobs_12, f, ensure_ascii=False, indent=2)

print("Saved 12 jobs for Tap 16 Act 4 to .work/bg_jobs_tap16_act4_12.json successfully!")
