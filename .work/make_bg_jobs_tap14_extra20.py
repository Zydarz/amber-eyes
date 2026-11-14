"""Định nghĩa 20 ảnh bổ sung cho Tập 14 (Hồ sơ Betty Broderick)
Đưa tổng số ảnh nền từ 57 lên 77 ảnh (trung bình ~2.7 shot/ảnh, đạt chuẩn H10 và giải quyết triệt để vấn đề lặp nền).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

new_20_jobs = [
    # -------------------------------------------------------------
    # HỒI 1 (Bổ sung 4 ảnh: 12 -> 16 ảnh)
    # -------------------------------------------------------------
    {
        "name": "t14_tupperware_avon_sales_struggle",
        "act": 1,
        "sentences": "1.04#3–#4",
        "desc": "Các thùng hàng mỹ phẩm Avon và đồ gia dụng Tupperware xếp chồng trong góc phòng khách nhỏ hẹp, minh chứng những năm tháng Betty bươn chải nuôi chồng ăn học.",
        "prompt": "Grim intimate interior of a modest 1970s apartment living room, cardboard boxes of Tupperware containers and vintage cosmetic sales catalogs stacked beside a worn vinyl armchair, pale tungsten lighting cutting through heavy shadow, quiet exhausting domestic struggle, graphic novel noir linework."
    },
    {
        "name": "t14_san_diego_bar_association_gala",
        "act": 1,
        "sentences": "1.06#1–#2",
        "desc": "Bữa tiệc dạ hội xa hoa của Đoàn Luật sư San Diego, bóng các luật sư danh giá nâng ly chúc tụng trong ánh đèn chùm rực rỡ, vẻ hào nhoáng của địa vị thượng lưu.",
        "prompt": "Atmospheric wide shot of an opulent 1980s San Diego legal society ballroom gala, towering crystal chandeliers casting golden ambient glare, silhouetted wealthy lawyers in tuxedos and evening gowns raising champagne flutes, deceptive luxury facade, sharp chiaroscuro ink contrast."
    },
    {
        "name": "t14_gaslighting_whispers_corridor",
        "act": 1,
        "sentences": "1.07#4–#5",
        "desc": "Hành lang vắng lặng với bóng người thì thầm to nhỏ, sự cô lập thông tin và ánh mắt nghi kỵ của xã hội thượng lưu khiến người vợ cảm thấy hoang mang tột độ.",
        "prompt": "Moody interior view of an empty dimly lit executive office hallway, long sinister shadows stretching along polished marble floor, two whispering silhouettes half-concealed behind frosted glass doors, psychological alienation aesthetic, heavy noir blacks."
    },
    {
        "name": "t14_shattered_trust_wedding_ring",
        "act": 1,
        "sentences": "1.10#4–#5",
        "desc": "Chiếc nhẫn cưới bằng vàng nằm trơ trọi trên mặt bàn gỗ sồi tối màu bên cạnh hóa đơn bữa trưa nhà hàng sang trọng bị vò nát, niềm tin hôn nhân sụp đổ hoàn toàn.",
        "prompt": "Forensic still life macro shot of a plain gold wedding band resting on dark polished mahogany desk beside a crumpled credit card receipt and faint lipstick smudge, harsh single spotlight from side casting long dramatic shadow, tragic betrayal noir."
    },

    # -------------------------------------------------------------
    # HỒI 2 (Bổ sung 4 ảnh: 12 -> 16 ảnh)
    # -------------------------------------------------------------
    {
        "name": "t14_courtroom_bench_power_imbalance",
        "act": 2,
        "sentences": "2.02#5–#7",
        "desc": "Phòng xử án tòa gia đình với một bên là dàn luật sư danh tiếng vây quanh người chồng, đối diện là chiếc ghế đơn độc của người vợ tự bào chữa.",
        "prompt": "High-contrast courtroom composition showing stark power asymmetry: on one side a polished legal team in tailored suits flanking a confident attorney, facing a lone silhouetted woman sitting before a solitary microphone, oppressive institution chiaroscuro, heavy ink contours."
    },
    {
        "name": "t14_crested_stationery_threatening_letters",
        "act": 2,
        "sentences": "2.06#2–#4",
        "desc": "Những lá thư pháp lý in tiêu đề mạ vàng của văn phòng luật sư Daniel Broderick xếp chồng trên bàn trà, vũ khí hóa thủ tục tố tụng để bóp nghẹt tài chính người vợ cũ.",
        "prompt": "Dramatic close-up of formal legal warning letters stamped with ornate attorney letterhead resting under a desk lamp, stark typewritten threats of contempt of court and fine deductions, cold calculated judicial aggression noir."
    },
    {
        "name": "t14_gun_store_revolver_purchase",
        "act": 2,
        "sentences": "2.09#1–#3",
        "desc": "Tủ kính trưng bày vũ khí trong cửa hàng súng địa phương mờ tối, bàn tay người phụ nữ chỉ vào khẩu súng lục ổ quay nòng ngắn, bước ngoặt định mệnh trước thảm kịch.",
        "prompt": "Tense interior of an old-fashioned gun store in San Diego, dusty glass counter displaying revolvers and ammo boxes under yellow overhead neon, silhouetted female hand pointing toward a .38 caliber revolver, chilling fatal turning point noir."
    },
    {
        "name": "t14_night_drive_headlights_coral_way",
        "act": 2,
        "sentences": "2.10#5–#7",
        "desc": "Chiếc xe ô tô di chuyển trong đêm tối trên con đường ngoại ô vắng lặng, ánh đèn pha rọi xuyên qua làn sương mỏng hướng về khu biệt thự Marston Hills.",
        "prompt": "Cinematic low-angle tracking shot of a 1980s sedan driving through the pitch-black quiet streets of San Diego at 5 AM, dual headlight beams cutting through coastal mist, brooding darkness swallowing the road, unstoppable tragic momentum noir."
    },

    # -------------------------------------------------------------
    # HỒI 3 (Bổ sung 4 ảnh: 10 -> 14 ảnh)
    # -------------------------------------------------------------
    {
        "name": "t14_darvo_defense_mirror_labyrinth",
        "act": 3,
        "sentences": "3.03#6–#8",
        "desc": "Cơ chế phòng vệ tâm lý DARVO: đảo ngược vai trò nạn nhân và kẻ tấn công, trực quan hóa bằng những tấm gương phản chiếu méo mó giữa bóng tối sâu thẳm.",
        "prompt": "Surreal psychological graphic novel illustration: warped funhouse mirrors reflecting distorted silhouettes, conceptual visualization of DARVO defense mechanism reversing offender and victim, deep pitch-black shadows, haunting ink chiaroscuro."
    },
    {
        "name": "t14_children_pawns_chess_board",
        "act": 3,
        "sentences": "3.06#3–#5",
        "desc": "Bàn cờ vua bằng đá cẩm thạch với những quân tốt trẻ thơ bị xô đẩy giữa hai quân hậu quyền lực, ẩn dụ việc con cái bị biến thành công cụ trả đũa hôn nhân.",
        "prompt": "Symbolic conceptual noir still life: an ornate marble chessboard where small wooden child figurines are trapped as helpless pawns between an aggressive black king and white queen, cold dramatic lighting, heartbreaking generational collateral damage."
    },
    {
        "name": "t14_parental_alienation_doorstep",
        "act": 3,
        "sentences": "3.07#3–#5",
        "desc": "Bóng những đứa trẻ đứng ngơ ngác trước bậc thềm cửa nhà giữa đêm tối, vali nhỏ nằm bên cạnh, bi kịch của sự chia ngăn nhận thức và bỏ rơi cảm xúc.",
        "prompt": "Heartrending nocturnal composition: small silhouettes of young children with tiny suitcases standing outside a grand locked mansion door in the cold night, harsh porch light casting long frightened shadows, cruelty of parental alienation noir."
    },
    {
        "name": "t14_moral_disengagement_scales",
        "act": 3,
        "sentences": "3.07#6–#7",
        "desc": "Cơ chế trung hòa đạo đức: cuốn sách luật pháp bị xé rách đè lên cán cân công lý méo mó, sự tự hợp lý hóa hành vi tội ác dưới vỏ bọc đòi lại công bằng.",
        "prompt": "Abstract psychological noir conceptual art: a torn legal codex and broken scales of justice enveloped in dark curling smoke, stark black ink linework showing the mental decay of moral disengagement, ominous and disturbing silence."
    },

    # -------------------------------------------------------------
    # HỒI 4 (Bổ sung 4 ảnh: 13 -> 17 ảnh)
    # -------------------------------------------------------------
    {
        "name": "t14_bedroom_broken_window_smoke",
        "act": 4,
        "sentences": "4.04#3–#5",
        "desc": "Khói súng bảng lảng trong phòng ngủ lớn sau 5 phát đạn rạng sáng, rèm cửa trắng bay phần phật bên khung cửa sổ mở, khoảnh khắc tĩnh lặng sau tội ác hủy diệt.",
        "prompt": "Grim crime scene atmospheric view of a luxury master bedroom just after dawn, wisps of acrid gunsmoke drifting through chilly morning breeze, billowing white sheer curtains, cold slate and bruised amber light through the window, eerie aftermath silence noir."
    },
    {
        "name": "t14_telephone_cord_severed_closeup",
        "act": 4,
        "sentences": "4.06#4–#6",
        "desc": "Cận cảnh hiện trường đầu dây điện thoại bị giật đứt lìa khỏi ổ cắm tường, bằng chứng đanh thép chứng minh toan tính tước đoạt cơ hội sống của nạn nhân.",
        "prompt": "Forensic macro still life of a beige telephone wire violently ripped from its wall jack, copper wires exposed on plush carpet beside an off-the-hook handset, stark cold crime scene investigator flashlight beam, signature evidence of malice noir."
    },
    {
        "name": "t14_defense_attorney_closing_argument",
        "act": 4,
        "sentences": "4.10#1–#3",
        "desc": "Bục tranh tụng phòng xử án với bóng luật sư bào chữa chỉ tay về phía bồi thẩm đoàn, cuộc tranh luận nảy lửa giữa hội chứng phụ nữ bị bạo hành và sát hại có toan tính.",
        "prompt": "Dramatic high-contrast courtroom perspective: silhouetted defense counsel in mid-gesture before the jury box, large courtroom clock high on the wood-paneled wall, tense battle of forensic arguments, classic graphic novel courtroom drama."
    },
    {
        "name": "t14_prison_visiting_room_glass",
        "act": 4,
        "sentences": "4.12#1–#3",
        "desc": "Phòng thăm nuôi trại giam với vách kính ngăn cách dày cộp và chiếc ống nghe điện thoại sắt, sự cô độc vĩnh viễn của thủ phạm sau bản án 32 năm tù.",
        "prompt": "Desolate interior shot of a correctional facility visitation room, scratched acrylic partition separating empty metal stools, heavy black coiled telephone receiver resting on metal shelf, crushing weight of lifelong incarceration, stark monochrome noir."
    },

    # -------------------------------------------------------------
    # HỒI 5 (Bổ sung 4 ảnh: 10 -> 14 ảnh)
    # -------------------------------------------------------------
    {
        "name": "t14_gift_of_fear_book_desk",
        "act": 5,
        "sentences": "5.05#1–#3",
        "desc": "Cuốn sách kinh điển 'The Gift of Fear' nằm trên bàn làm việc bên cạnh ngọn nến thơm và tách trà ấm, thông điệp về sự thức tỉnh của bản năng và trực giác sinh tồn.",
        "prompt": "Inspiring contemplative still life of a hardcover psychology book titled 'The Gift of Fear' resting on a warm dark wooden study desk beside an unlit brass candleholder, soft golden morning light streaming through blinds, philosophical reflection noir."
    },
    {
        "name": "t14_toxic_ties_severed_chain",
        "act": 5,
        "sentences": "5.05#8–#11",
        "desc": "Sợi xích sắt nặng nề bị cắt đứt làm đôi rơi xuống đất, biểu tượng của sự dũng cảm buông bỏ các mối quan hệ độc hại để tự giải phóng bản thân.",
        "prompt": "Powerful symbolic graphic art: a heavy rusted iron chain cleanly severed in mid-air, links scattering across dark cobblestones, bright ray of dawn light illuminating the broken link, profound liberation from toxic entanglement, bold ink art."
    },
    {
        "name": "t14_ash_heap_phoenix_rebuilding",
        "act": 5,
        "sentences": "5.05#14–#16",
        "desc": "Bóng người phụ nữ độc lập bước đi tự tin về phía chân trời rạng rỡ, để lại sau lưng đống tro tàn của quá khứ đổ vỡ, thông điệp về sự hồi sinh kiên cường.",
        "prompt": "Uplifting graphic novel silhouette composition: a solitary dignified woman walking away from shadowy ruins toward a vast glowing golden horizon, leaving behind the dark ashes of past betrayal, inspiring triumph of personal dignity and survival."
    },
    {
        "name": "t14_peace_of_mind_calm_waters",
        "act": 5,
        "sentences": "5.05#19–#22",
        "desc": "Mặt biển La Jolla phẳng lặng phản chiếu ánh nắng ban mai tinh khôi, sự bình yên đích thực trong tâm hồn của những người biết buông bỏ hận thù.",
        "prompt": "Serene wide panoramic view of calm Pacific ocean waters at full sunrise, gentle ripples catching golden amber light, rugged sea cliff silhouettes in the distance, tranquil atmospheric closure, pure inner peace transcending tragedy."
    }
]

# Đọc danh sách cũ
with open(WORK / "bg_jobs_tap14.json", "r", encoding="utf-8") as f:
    old_jobs = json.load(f)

# Gộp và sắp xếp theo Hồi
all_jobs = old_jobs + new_20_jobs
# Sắp xếp theo act
all_jobs.sort(key=lambda x: x.get("act", 1))

# Lưu file hoàn chỉnh 77 jobs
with open(WORK / "bg_jobs_tap14_77.json", "w", encoding="utf-8") as f:
    json.dump(all_jobs, f, ensure_ascii=False, indent=2)

print(f"Đã tạo file bg_jobs_tap14_77.json thành công với tổng cộng {len(all_jobs)} jobs!")
for act in range(1, 6):
    count = len([j for j in all_jobs if j.get("act") == act])
    print(f" - Hồi {act}: {count} ảnh")
