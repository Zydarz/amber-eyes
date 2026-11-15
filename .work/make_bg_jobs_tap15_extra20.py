"""Định nghĩa 20 ảnh nền bổ sung cho Tập 15 (Hồ sơ Travis Alexander & Jodi Arias)
Đưa tổng số ảnh nền từ 63 lên 83 ảnh (trung bình ~2.65 câu/ảnh, đạt chuẩn H10 và giải quyết triệt để vấn đề lặp nền).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

new_20_jobs = [
    # -------------------------------------------------------------
    # HỒI 1: Bổ sung 4 ảnh (12 -> 16 ảnh)
    # Tập trung vào: Nỗi dằn vặt của bạn bè, lốp xe bị rạch, Cancun, buồng tắm
    # -------------------------------------------------------------
    {
        "name": "t15_slashed_car_tires_curbside",
        "act": 1,
        "sentences": "1.07#5–#7",
        "desc": "Chiếc lốp xe bị rạch nát nằm sát lề đường trong đêm tối dưới ánh đèn đường vàng vọt, minh chứng cho hành vi phá hoại tài sản và đe dọa sinh tử của kẻ bám đuôi.",
        "prompt": "Grim forensic close-up of a slashed car tire on a parked sedan along a dark suburban curb at night, deep knife gashes in rubber, pale amber streetlight reflections on wet asphalt, eerie psychological dread noir."
    },
    {
        "name": "t15_bystander_guilt_whispers_livingroom",
        "act": 1,
        "sentences": "1.08#1–#3",
        "desc": "Góc phòng khách với hai bóng người ngồi lặng lẽ bên tách cà phê nguội ngắt, nỗi dằn vặt khôn nguôi và cảm giác tội lỗi của người ngoài cuộc khi bỏ lỡ điềm báo tử.",
        "prompt": "Moody interior view of a dimly lit living room at night, two silhouetted friends sitting in somber silence with cold mugs on a wooden coffee table, long melancholic shadows stretching across floor, heavy psychological guilt noir."
    },
    {
        "name": "t15_cancun_plane_tickets_unopened_mail",
        "act": 1,
        "sentences": "1.07#3–#4",
        "desc": "Phong bì vé máy bay đi Cancun và tập tài liệu hội thảo chưa mở nằm trên quầy bếp, chuyến đi định mệnh bị hủy bỏ trước linh cảm chẳng lành.",
        "prompt": "Forensic still life of an unopened airline envelope labeled Cancun Flight beside a leather passport holder on a dark granite kitchen island, single overhead pendant light casting dramatic chiaroscuro cone."
    },
    {
        "name": "t15_washing_machine_running_dark_utility",
        "act": 1,
        "sentences": "1.14#4–#6",
        "desc": "Căn phòng giặt là tối mờ với lồng máy giặt đang xoay tít trong nước, nơi chiếc máy ảnh kỹ thuật số Sony Cyber-shot bị giấu phi tang trong tuyệt vọng.",
        "prompt": "Chilling low-angle view of a front-loading washing machine operating in a dark cramped laundry room, water churning through glass door, metallic reflections and deep obsidian ink shadows, clinical crime scene noir."
    },

    # -------------------------------------------------------------
    # HỒI 2: Bổ sung 4 ảnh (11 -> 15 ảnh)
    # Tập trung vào: Darryl Brewer mượn can xăng, Ryan Burns ở Utah, bản đồ hành trình
    # -------------------------------------------------------------
    {
        "name": "t15_darryl_brewer_garage_gas_cans",
        "act": 2,
        "sentences": "2.05#6–#8",
        "desc": "Góc gara của người bạn trai cũ Darryl Brewer với hai can xăng nhựa màu đỏ để cạnh hộp dụng cụ, sự thao túng biến người thân thành kẻ hỗ trợ vô thức.",
        "prompt": "Cluttered 2000s residential garage interior, two vintage red plastic five-gallon fuel containers resting on oil-stained concrete beside mechanic toolboxes, harsh tungsten bulb casting high-contrast silhouettes."
    },
    {
        "name": "t15_interstate_highway_gas_stop_midnight",
        "act": 2,
        "sentences": "2.05#9–#11",
        "desc": "Trạm dừng nghỉ hoang vắng giữa sa mạc lúc nửa đêm, chiếc xe thuê màu trắng tắt đèn dưới bóng tối, hành trình ngụy tạo ngoại phạm và xóa dấu vết.",
        "prompt": "Desolate desert highway roadside stop at 2 AM, white rental sedan idling in complete shadows away from neon pump lights, vast starry Arizona desert sky, stealthy premeditation tension, heavy ink chiaroscuro."
    },
    {
        "name": "t15_salt_lake_city_suburban_doorstep",
        "act": 2,
        "sentences": "2.05#12–#14",
        "desc": "Bậc thềm nhà ngoại ô thanh bình tại Thành phố Salt Lake bang Utah trong nắng sớm, nơi hung thủ gặp gỡ người tình mới với nụ cười ngây thơ giả tạo.",
        "prompt": "Quiet early morning suburban doorstep in Salt Lake City Utah, manicured green lawn and clean concrete porch steps under crisp pale sunlight, deceptive facade of innocence masking violent crime."
    },
    {
        "name": "t15_investigative_timeline_wall_map",
        "act": 2,
        "sentences": "2.07#1–#4",
        "desc": "Bản đồ điều tra hành trình di chuyển từ California qua Arizona tới Utah gắn đinh ghim và dây chỉ đỏ trên bảng dạ, vạch trần mưu tính ngoại phạm.",
        "prompt": "High-contrast investigative wall map pinned with red yarn tracing interstate highway route from California through Arizona to Utah, timestamps and evidence polaroids pinned alongside, methodical police deduction noir."
    },

    # -------------------------------------------------------------
    # HỒI 3: Bổ sung 4 ảnh (11 -> 15 ảnh)
    # Tập trung vào: Xung đột nhận thức Travis, Trauma Bonding, Push-Pull, Ái kỷ sụp đổ
    # -------------------------------------------------------------
    {
        "name": "t15_cognitive_dissonance_scriptures_bedside",
        "act": 3,
        "sentences": "3.05#4–#6",
        "desc": "Cuốn kinh thánh tôn giáo và chiếc điện thoại di động nhấp nháy tin nhắn cám dỗ đặt trên bàn đầu giường, xung đột nhận thức tột cùng giữa chuẩn mực đạo đức và nhục cảm.",
        "prompt": "Forensic still life on a dark oak nightstand: open hardcover holy scriptures resting beside a glowing slider cellphone showing incoming text alert, harsh diagonal spotlight splitting scene into light and deep shadow, moral conflict noir."
    },
    {
        "name": "t15_trauma_bonding_push_pull_tangle",
        "act": 3,
        "sentences": "3.08#4–#7",
        "desc": "Hình ảnh ẩn dụ: Hai sợi dây thừng một đen một trắng xoắn chặt vào nhau rồi bị giằng xé dữ dội, biểu trưng cho chu kỳ kéo - đẩy và gắn kết chấn thương độc hại.",
        "prompt": "Conceptual dark graphic art: two intertwined nautical ropes one pure white and one pitch black caught in violent opposing tension, fibers fraying and snapping under strain, deep chiaroscuro background, psychological trauma bonding."
    },
    {
        "name": "t15_narcissistic_optimism_bias_shadow",
        "act": 3,
        "sentences": "3.08#10–#13",
        "desc": "Bóng người đàn ông đứng trên bục giảng diễn thuyết tự tin nhưng bóng đổ phía sau là vực thẳm, điểm mù lạc quan của người truyền cảm hứng khi đánh giá thấp hiểm họa.",
        "prompt": "High-contrast graphic novel silhouette: a confident speaker standing at a podium bathed in bright spotlight, but his long shadow stretching behind him dissolves into a dark gaping abyss, tragic blindness of optimism bias."
    },
    {
        "name": "t15_theory_of_mind_deficit_chess",
        "act": 3,
        "sentences": "3.08#14–#16",
        "desc": "Bàn cờ vua bằng đá cẩm thạch với quân cờ vua bị đập vỡ vụn, minh họa sự vật hóa con người và khiếm khuyết lòng trắc ẩn của nhân cách ái kỷ ác tính.",
        "prompt": "Macro tabletop shot of an ornate marble chessboard, a white king piece violently toppled and shattered across squares, deep pitch-black background, ruthless objectification and lack of empathy concept."
    },

    # -------------------------------------------------------------
    # HỒI 4: Bổ sung 4 ảnh (12 -> 16 ảnh)
    # Tập trung vào: Tự thương hại bệnh lý, Nước mắt giả tạo, Rạp xiếc truyền thông
    # -------------------------------------------------------------
    {
        "name": "t15_pathological_self_pity_tissue",
        "act": 4,
        "sentences": "4.11#6–#8",
        "desc": "Chiếc khăn giấy nhàu nát trên bàn và ly nước thủy tinh trơ trọi tại bục nhân chứng, nước mắt tự thương hại bệnh lý khi chiếc mặt nạ toàn năng bị xé toạc.",
        "prompt": "Forensic close-up on witness stand ledge: crumpled paper tissue beside an untouched clear glass of water, harsh courtroom overhead downlight casting sharp circular beam, hollow theatrical self-pity noir."
    },
    {
        "name": "t15_media_circus_cameras_satellite_trucks",
        "act": 4,
        "sentences": "4.10#1–#3",
        "desc": "Bên ngoài tòa án Maricopa với hàng chục xe truyền hình vệ tinh vươn ăng-ten lên trời và đám đông phóng viên chen lấn, hiện tượng rạp xiếc truyền thông toàn cầu.",
        "prompt": "Dramatic wide shot outside Maricopa County Courthouse at dusk, fleet of television broadcast trucks with towering microwave dishes silhouetted against twilight sky, flashing media camera lights, chaotic voyeurism."
    },
    {
        "name": "t15_prosecutor_timeline_whiteboard_clash",
        "act": 4,
        "sentences": "4.08#4–#7",
        "desc": "Bảng đối chất mâu thuẫn lời khai với những dòng chữ gạch chéo màu đỏ đậm, cuộc đấu trí pháp lý đanh thép của công tố viên Juan Martinez.",
        "prompt": "Stark courtroom presentation board marked with bold handwritten timelines and aggressive red cross-examination markers, forensic exhibit tags, clinical destruction of suspect falsehoods, graphic noir realism."
    },
    {
        "name": "t15_two_guilt_polarities_scales",
        "act": 4,
        "sentences": "4.12#1–#3",
        "desc": "Hình tượng chiếc cân công lý cổ xưa: một bên trĩu nặng giọt lệ lương tâm chân thực của bạn bè, một bên là sự trống rỗng hoàn toàn của kẻ thủ ác vô cảm.",
        "prompt": "Conceptual noir visual: antique brass scales of justice suspended in darkness, one pan bearing a heavy glowing teardrop of genuine remorse while the opposing pan remains hollow and desolate, philosophical polarity."
    },

    # -------------------------------------------------------------
    # HỒI 5: Bổ sung 4 ảnh (17 -> 21 ảnh)
    # Tập trung vào: Quỹ tưởng niệm Travis, Bài học ranh giới, Ngôi nhà bình yên, Hoàng hôn tự do
    # -------------------------------------------------------------
    {
        "name": "t15_travis_foundation_scholarship_plaque",
        "act": 5,
        "sentences": "5.04#7–#9",
        "desc": "Tấm kỷ niệm chương bằng đồng sáng bóng của quỹ học bổng mang tên Travis Alexander, di sản thiện nguyện và tình yêu thương của bạn bè để lại cuộc đời.",
        "prompt": "Solemn still life of an engraved bronze memorial plaque honoring Travis Alexander beside a small vase of white carnations on polished mahogany, warm amber side lighting, dignified legal legacy noir."
    },
    {
        "name": "t15_personal_boundary_stone_wall_garden",
        "act": 5,
        "sentences": "5.10#1–#4",
        "desc": "Bức tường đá kiên cố ngăn cách giữa khu vườn xanh tươi và sa mạc cằn cỗi, biểu tượng của việc thiết lập ranh giới cá nhân lành mạnh để bảo vệ sinh mạng.",
        "prompt": "Poetic wide shot of a sturdy dry stone boundary wall separating a serene verdant garden from rugged arid desert rocks, clear morning sky, empowering psychological boundary metaphor in graphic noir ink."
    },
    {
        "name": "t15_quiet_sanctuary_porch_morning_light",
        "act": 5,
        "sentences": "5.10#5–#8",
        "desc": "Hiên nhà thanh bình đón ánh ban mai ấm áp, chiếc ghế tựa gỗ thư thái bên ly trà thơm, sự bình yên và tự do quý giá khi vượt qua bóng tối độc hại.",
        "prompt": "Atmospheric wide perspective of a tranquil wooden porch overlooking peaceful mountain hills at sunrise, warm golden sunlight washing over a simple rocking chair, deep peaceful sanctuary transcending fear."
    },
    {
        "name": "t15_truth_shines_desert_highway_horizon",
        "act": 5,
        "sentences": "5.12#1–#4",
        "desc": "Con đường cao tốc thênh thang trải dài về phía chân trời rực rỡ nắng mai của Arizona, chiến thắng tối hậu của sự thật và công lý trước dối trá.",
        "prompt": "Inspiring panoramic view down a long straight desert highway vanishing into a brilliant golden dawn horizon, red rock mesas glowing under clear skies, ultimate triumph of truth and closure, bold ink linework."
    }
]

# Đọc danh sách 63 jobs hiện tại
with open(WORK / "bg_jobs_tap15.json", "r", encoding="utf-8") as f:
    old_jobs = json.load(f)

# Gộp và sắp xếp theo Hồi
all_jobs = old_jobs + new_20_jobs
all_jobs.sort(key=lambda x: x.get("act", 1))

# Lưu file hoàn chỉnh 83 jobs
out_83 = WORK / "bg_jobs_tap15_83.json"
with open(out_83, "w", encoding="utf-8") as f:
    json.dump(all_jobs, f, ensure_ascii=False, indent=2)

print(f"Đã tạo file {out_83.name} thành công với tổng cộng {len(all_jobs)} jobs!")
for act in range(1, 6):
    count = len([j for j in all_jobs if j.get("act") == act])
    print(f" - Hồi {act}: {count} ảnh")
