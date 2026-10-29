import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"

jobs = [
    # =========================================================================
    # HỒI 1: VỎ BỌC 'CON NHÀ NGƯỜI TA' VÀ TÒA THÁP DỐI LỪA MƯỜI NĂM (00:00 – 05:30)
    # =========================================================================
    {
        "name": "t13_markham_suburb_residential_dusk",
        "act": 1,
        "sentences": "1.02#1",
        "desc": "Khu dân cư Markham thanh bình, tuyết nhẹ, những ngôi nhà gạch ngoại ô ấm áp dưới ánh hoàng hôn mùa đông Ontario.",
        "prompt": "Cinematic 16:9 establishing shot of a quiet suburban neighborhood in Markham, Ontario, dusted with light evening snow, tidy brick houses under a moody bruised amber twilight sky, warm glowing porch lamps, dark graphic novel noir style, fine film grain."
    },
    {
        "name": "t13_immigrant_dream_trophy_cars",
        "act": 1,
        "sentences": "1.02#2–#3",
        "desc": "Căn nhà hai tầng khang trang tại đại lộ Helen với hai chiếc xe đắt tiền trong gara, biểu tượng của giấc mơ thành đạt người nhập cư.",
        "prompt": "Atmospheric wide shot of a prosperous two-story brick suburban house with a paved driveway, two luxury sedans parked neatly in the double garage, symbol of the hardworking immigrant American dream, brooding evening chiaroscuro, heavy ink contours."
    },
    {
        "name": "t13_golden_child_portrait_silhouette",
        "act": 1,
        "sentences": "1.02#4",
        "desc": "Bóng chân dung người con gái trong khung ảnh mạ vàng trên lò sưởi, tâm điểm kỳ vọng của cả gia đình.",
        "prompt": "Forensic still life of an ornate gilded photo frame resting on a dark wood fireplace mantle, silhouette portrait of a young Asian girl with classical poise, warm low spotlight illuminating the golden frame against deep shadow, subtle noir tension."
    },
    {
        "name": "t13_figure_skates_and_grand_piano",
        "act": 1,
        "sentences": "1.02#5–#6",
        "desc": "Cây đàn dương cầm bóng loáng bên đôi giày trượt băng nghệ thuật mài sắc và chồng sách vở điểm A, biểu tượng kỷ luật khắt khe.",
        "prompt": "Chiaroscuro still life of a gleaming polished black grand piano, sharpened competitive figure ice skates resting on the bench, and neat stacks of classical sheet music with academic binders, oppressive discipline aesthetic, dark ink linework."
    },
    {
        "name": "t13_perfect_daughter_facade",
        "act": 1,
        "sentences": "1.04#1–#2",
        "desc": "Chiếc áo len thanh lịch, nụ cười lễ phép và chồng giấy khen điểm A được đóng khung lấp lánh trên tường gỗ.",
        "prompt": "Composition showing framed straight-A academic achievement certificates hanging on a wood-paneled wall, soft warm amber interior lighting, facade of the flawless obedient golden child, vintage graphic novel aesthetic, sharp contrast."
    },
    {
        "name": "t13_tiger_parent_looming_shadow",
        "act": 1,
        "sentences": "1.04#3–#4",
        "desc": "Bóng đen người cha uy nghiêm đổ dài từ ngưỡng cửa thư phòng, áp lực kiểm soát độc đoán như chiếc lồng vô hình.",
        "prompt": "Dramatic interior shot of an imposing patriarchal shadow cast across a polished hardwood hallway floor from an open doorway, towering authoritative presence of tiger parenting, suffocating quiet tension, deep obsidian blacks."
    },
    {
        "name": "t13_locked_bedroom_desk_clock",
        "act": 1,
        "sentences": "1.04#5–#6",
        "desc": "Chiếc bàn học đơn độc dưới ánh đèn bàn gay gắt, đồng hồ báo thức tích tắc và cửa sổ đóng kín cách ly với thế giới bên ngoài.",
        "prompt": "Nocturnal view of a teenage study desk illuminated solely by a harsh brass desk lamp, ticking analog clock, closed textbook and closed curtains sealing the room off from adolescent social life, oppressive isolation noir."
    },
    {
        "name": "t13_failing_calculus_exam_dread",
        "act": 1,
        "sentences": "1.06#1–#2",
        "desc": "Trang bài thi Giải tích gạch đỏ mực phê điểm F, bóng bàn tay run rẩy gục đầu trong bóng tối phòng ngủ.",
        "prompt": "Grim macro still life of a high school Calculus examination paper marked with red ink corrections and a failing grade, silhouetted trembling hands clutching the edge of the desk in dark despair, stark noir chiaroscuro."
    },
    {
        "name": "t13_forgery_scissors_glue_photocopy",
        "act": 1,
        "sentences": "1.06#3–#4",
        "desc": "Kéo bấm, keo dán, lưỡi dao cạo giấy và ánh sáng quét màu xanh từ máy photocopy lúc nửa đêm, giây phút chế tạo học bạ giả đầu tiên.",
        "prompt": "Tense nighttime forensic still life of craft scissors, glue stick, razor blade, and cut-out report card grades illuminated by the eerie cyan glow of a home photocopier glass bed, first fatal act of document forgery."
    },
    {
        "name": "t13_house_of_cards_first_lie",
        "act": 1,
        "sentences": "1.06#5–#6",
        "desc": "Tòa tháp quân bài mỏng manh xếp cao trên mặt kính phản chiếu, biểu tượng lời nói dối đầu tiên châm ngòi cho 10 năm lừa dối.",
        "prompt": "Surreal symbolic noir visual of a precarious multi-tiered house of playing cards trembling on a black reflective glass tabletop, deep ominous shadows, symbol of a decade-long tower of lies ready to collapse."
    },
    {
        "name": "t13_school_piano_recital_hall",
        "act": 1,
        "sentences": "1.07#1–#2",
        "desc": "Cây đàn piano trong hội trường trường học Mary Ward, nơi cô nữ sinh tỏa sáng giữa bạn bè nhưng nội tâm chìm trong âu lo.",
        "prompt": "Atmospheric view of a school auditorium stage with a single grand piano under a solitary stage spotlight, rows of empty wooden seats receding into shadow, nostalgic high school memory, subtle melancholy noir."
    },
    {
        "name": "t13_rushing_home_school_curfew",
        "act": 1,
        "sentences": "1.07#3–#4",
        "desc": "Bóng cô gái đeo ba lô vội vã chạy qua con đường tuyết lạnh khi hoàng hôn vừa tắt, nỗi sợ trễ giờ giới nghiêm của cha.",
        "prompt": "Dynamic silhouette of a young student with a heavy backpack rushing down a suburban sidewalk at winter dusk, streetlamps flickering on against icy slush, palpable dread of violating strict parental curfews, cold slate tones."
    },
    {
        "name": "t13_unseen_suffocating_pressure",
        "act": 1,
        "sentences": "1.07#5–#7",
        "desc": "Bức rèm phòng ngủ rủ xuống, đôi vai nhỏ bé oằn mình trước cái bóng khổng lồ của kỳ vọng, sự cô độc cùng cực.",
        "prompt": "Emotional graphic composition of a young woman's slumped silhouette seated on a window sill behind drawn heavy drapes, clutching her knees against a brooding night skyline, invisible crushing emotional burden."
    },
    {
        "name": "t13_fake_university_acceptance_letter",
        "act": 1,
        "sentences": "1.09#1–#2",
        "desc": "Tờ giấy báo trúng tuyển Đại học Ryerson và Dược khoa U of T được làm giả tinh vi, con dấu đỏ ngụy tạo trên bàn kính.",
        "prompt": "Forensic macro still life of a forged university acceptance letter with an embossed emblem and counterfeit admissions seal, resting beside an official academic brochure, deceptive academic achievement facade."
    },
    {
        "name": "t13_morning_bus_stop_winter_mist",
        "act": 1,
        "sentences": "1.09#3",
        "desc": "Trạm dừng xe buýt ngoại ô mù sương buổi sáng, bóng cô gái xách cặp giả vờ bước lên xe đi học đại học.",
        "prompt": "Chilly early morning suburban bus shelter shrouded in cold gray fog, lone silhouetted figure holding a commuter satchel waiting for the bus, phantom daily routine of a fake university student, muted blue-gray noir palette."
    },
    {
        "name": "t13_public_library_reading_hours",
        "act": 1,
        "sentences": "1.09#4",
        "desc": "Dãy bàn gỗ tĩnh lặng của thư viện công cộng Toronto, nơi cô gái ngồi đọc tiểu thuyết hàng giờ giết thời gian trốn tránh gia đình.",
        "prompt": "Quiet cavernous interior of a downtown public library, long oak tables beneath green banker lamps, a solitary figure reading to kill four years of phantom college lectures, quiet sorrow and drifting alienation."
    },
    {
        "name": "t13_illicit_romance_daniel_wong",
        "act": 1,
        "sentences": "1.09#5",
        "desc": "Căn hộ chung cư tối đèn nơi ngoại ô, bóng hai người bên làn khói mờ ảo, tình yêu bị cấm đoán với Daniel Wong.",
        "prompt": "Moody interior of a dimly lit suburban apartment living room, faint city glow through horizontal blinds, two silhouetted figures seated on a worn sofa in quiet conversation, forbidden romance in the shadows."
    },
    {
        "name": "t13_counterfeit_pharmacy_degree_sickkids",
        "act": 1,
        "sentences": "1.09#6",
        "desc": "Tấm bằng cử nhân Dược khoa giả đóng khung bên ống nghe y tế và tài liệu ngụy tạo về Bệnh viện Nhi SickKids.",
        "prompt": "Forensic still life of an ornate fake University of Toronto Bachelor of Science in Pharmacy diploma, a medical stethoscope, and fabricated hospital badge lanyard, the pinnacle of an elaborate decade-long deception."
    },
    {
        "name": "t13_father_growing_suspicion",
        "act": 1,
        "sentences": "1.10#1–#2",
        "desc": "Người cha đứng nơi góc phòng khách, ánh mắt hoài nghi nhìn vào chiếc túi xách không hề có thẻ nhân viên bệnh viện hay đồng phục y tế.",
        "prompt": "Subtle domestic psychological thriller shot: a stern father's silhouette standing in a hallway archway, eyeing an unzipped commuter handbag on the hall table devoid of hospital ID or scrubs, seeds of suspicion taking root."
    },
    {
        "name": "t13_trailing_car_cold_toronto_streets",
        "act": 1,
        "sentences": "1.10#3–#4",
        "desc": "Chiếc xe hơi âm thầm bám theo bóng con gái trên đường phố Toronto mùa đông xám xịt, sự thật chuẩn bị phơi bày.",
        "prompt": "Cinematic noir street scene from inside a surveillance vehicle, windshield wipers sweeping cold rain, following a solitary pedestrian through gray downtown Toronto streets, relentless paternal pursuit of truth."
    },
    {
        "name": "t13_empty_hospital_roster_shock",
        "act": 1,
        "sentences": "1.10#5",
        "desc": "Sảnh lễ tân bệnh viện SickKids hiện đại vắng bóng con gái, danh sách nhân viên y tế trống trơn, khoảnh khắc người cha bàng hoàng chết lặng.",
        "prompt": "Cold institutional shot of a sterile hospital reception atrium, empty informational desk counter under fluorescent strip lights, an elderly father figure standing frozen in devastating realization of total fabrication."
    },
    {
        "name": "t13_twenty_years_pride_shattered",
        "act": 1,
        "sentences": "1.11#1–#2",
        "desc": "Khung ảnh gia đình và những tấm bằng khen bị rơi vỡ trên sàn nhà, hai mươi năm danh dự vỡ vụn thành tro tàn.",
        "prompt": "Dramatic close-up of a shattered glass photo frame lying face up on polished floorboards, splintered web of cracks across a pristine family portrait, twenty years of immigrant pride pulverized in an instant."
    },
    {
        "name": "t13_desperate_wrath_father_confrontation",
        "act": 1,
        "sentences": "1.11#3–#4",
        "desc": "Phòng khách đêm buốt giá, bóng người cha giận dữ chỉ tay ra lệnh trừng phạt, lằn ranh đưa đẩy cô con gái cưng vào vực thẳm.",
        "prompt": "High-contrast confrontation in a shadowy living room, father's accusatory silhouetted arm outstretched in boiling fury, a daughter cowering against the banister, fateful domestic rupture crossing the point of no return."
    },

    # =========================================================================
    # HỒI 2: ĐÊM KINH HOÀNG TẠI ĐẠI LỘ HELEN VÀ CUỘC GỌI 911 (05:30 – 11:00)
    # =========================================================================
    {
        "name": "t13_helen_avenue_domestic_prison",
        "act": 2,
        "sentences": "2.02#1",
        "desc": "Ngôi nhà số 238 Helen Avenue nhìn từ ngoài vào ban đêm, các rèm cửa kéo kín, biến thành nhà tù gia đình lạnh lẽo.",
        "prompt": "Nocturnal exterior of 238 Helen Avenue in Markham, drawn black blinds in every window, cold streetlamp casting harsh barred shadows across the brick facade, residential home turned into a gilded domestic prison."
    },
    {
        "name": "t13_confiscated_laptop_cellphone",
        "act": 2,
        "sentences": "2.02#2–#3",
        "desc": "Chiếc laptop và điện thoại của Jennifer bị tịch thu, niêm phong trên bàn làm việc của người cha dưới sự giám sát 24/7.",
        "prompt": "Forensic still life of a confiscated silver laptop with its power cord removed and a switched-off mobile phone placed on a strict father's study desk under lock and key, total digital quarantine."
    },
    {
        "name": "t13_house_arrest_twenty_four_years_old",
        "act": 2,
        "sentences": "2.02#4–#5",
        "desc": "Cô gái 24 tuổi ngồi cô độc bên góc giường, bị đối xử như đứa trẻ bị quản thúc nghiêm ngặt, rèm cửa khép kín.",
        "prompt": "Melancholic bedroom interior showing a 24-year-old woman sitting curled on the edge of a twin bed in dark shadow, barred window blinds casting cage-like stripes, regression into infantile house arrest."
    },
    {
        "name": "t13_simmering_resentment_dark_room",
        "act": 2,
        "sentences": "2.04#1–#2",
        "desc": "Căn phòng tối với ánh trăng lạnh chiếu nghiêng, ngọn lửa hận thù âm ỉ thay thế nỗi xấu hổ trong tâm trí bị dồn ép.",
        "prompt": "Moody psychological noir close-up of a face in deep shadow with only cold moonlight catching narrowed determined eyes, shame transmuting into icy calculating resentment, ominous crimson and deep indigo tones."
    },
    {
        "name": "t13_secret_burner_phone_messages",
        "act": 2,
        "sentences": "2.04#3–#4",
        "desc": "Ánh sáng xanh le lói từ màn hình chiếc điện thoại bí mật trong bóng tối, những dòng tin nhắn trao đổi âm mưu với Daniel Wong.",
        "prompt": "Close-up of hands typing in darkness on an old hidden burner flip phone, glowing blue screen illuminating tense fingertips, conspiratorial text messages sent beneath bed covers, noir aesthetic."
    },
    {
        "name": "t13_murder_for_hire_conspiracy_shadows",
        "act": 2,
        "sentences": "2.04#5",
        "desc": "Ba bóng đen sát thủ gặp gỡ trong bãi đậu xe tối tăm, bản phác thảo căn nhà 238 Helen Avenue trên nắp capô.",
        "prompt": "Gritty crime noir scene of three heavy silhouetted figures leaning over the hood of an idling car in a dark suburban strip mall parking lot, street map of Markham spread under a flickering yellow sodium lamp."
    },
    {
        "name": "t13_five_hundred_thousand_insurance_policy",
        "act": 2,
        "sentences": "2.04#6–#7",
        "desc": "Bản hợp đồng bảo hiểm nhân thọ và giấy thừa kế 500.000 đô la đặt cạnh chìa khóa nhà, mồi nhử lòng tham và sự giải thoát mù quáng.",
        "prompt": "Forensic still life of official Canadian life insurance policy documents displaying five-hundred-thousand dollar payout figures, beside a brass house key on a polished mahogany surface, deadly incentive of patricide."
    },
    {
        "name": "t13_unlocked_front_door_night",
        "act": 2,
        "sentences": "2.06#1",
        "desc": "Then cài cánh cửa chính số 238 Helen Avenue được xoay mở khẽ khàng lúc 22h05 đêm ngày 8/11/2010.",
        "prompt": "Macro shot of a heavy brass deadbolt on a residential front door silently slipping unlocked from the inside, sliver of cold November night air entering the dimly lit foyer, fateful moment of betrayal."
    },
    {
        "name": "t13_three_intruders_stealth_entry",
        "act": 2,
        "sentences": "2.06#2–#3",
        "desc": "Ba bóng đen mang súng ngắn lặng lẽ bước qua bậc thềm phòng khách mờ tối, không hề có dấu vết cạy phá.",
        "prompt": "Ominous noir wide shot of three hooded armed silhouettes stepping silently through an open front door into a dark suburban hallway, drawn handguns held low, eerie absence of forced entry."
    },
    {
        "name": "t13_parents_subdued_in_bedroom",
        "act": 2,
        "sentences": "2.06#4",
        "desc": "Người cha và người mẹ giật mình thức giấc trong phòng ngủ, bị ba họng súng đen ngòm khống chế trong im lặng rợn người.",
        "prompt": "Tense cinematic bedroom scene in semi-darkness, an elderly couple startled awake by menacing shadows standing over their bed, silent gun barrels glinting in the faint streetlight, sheer terror."
    },
    {
        "name": "t13_loosely_tied_staircase_banister",
        "act": 2,
        "sentences": "2.06#5",
        "desc": "Chiếc dây thừng buộc hờ hững quanh tay Jennifer vào tay vịn cầu thang gỗ tầng hai, hiện trường dàn dựng giả tạo.",
        "prompt": "Forensic observation shot of a white nylon cord tied in loose, slack loops around a woman's wrists to a carved wooden staircase banister, blatantly staged restraint with ample slack, suspicious crime scene detail."
    },
    {
        "name": "t13_ransacked_drawers_staged_robbery",
        "act": 2,
        "sentences": "2.08#1",
        "desc": "Ngăn kéo tủ phòng khách bị kéo tung, tài liệu vương vãi tạo hiện trường cướp của giả, trong khi tài sản giá trị vẫn nguyên vẹn.",
        "prompt": "Crime scene still life of halfway opened dresser drawers with neatly folded clothes tossed on the rug, staged amateur ransacking while expensive electronics remain untouched on the sideboard, dark chiaroscuro."
    },
    {
        "name": "t13_basement_stairs_descent_terror",
        "act": 2,
        "sentences": "2.08#2",
        "desc": "Cầu thang gỗ dẫn xuống tầng hầm tối tăm, bóng ba sát thủ dẫn hai người lớn tuổi đi xuống điểm định mệnh.",
        "prompt": "High-angle view down steep unfinished basement stairs into murky subterranean darkness, elongated shadows descending into the cellar, suffocating dread, heavy black ink rendering."
    },
    {
        "name": "t13_tragic_demise_gentle_mother",
        "act": 2,
        "sentences": "2.08#3",
        "desc": "Tĩnh vật chiếc khăn len và chuỗi hạt của người mẹ rơi trên sàn tầng hầm tĩnh lặng, sự hy sinh oan khuất của người phụ nữ hiền lành.",
        "prompt": "Solemn forensic still life adhering strictly to documentary standards: a gentle mother's hand-knitted woolen scarf and prayer bead necklace lying on cold basement floorboards in quiet spotlight, poignant tragic quietude, no gore."
    },
    {
        "name": "t13_father_gravely_wounded_miracle",
        "act": 2,
        "sentences": "2.08#4",
        "desc": "Bóng người cha gục ngã bên chân cầu thang tầng hầm, ngọn lửa sinh mệnh thoi thóp nhưng ý chí sinh tồn kiên cường.",
        "prompt": "Solemn silhouette of a fallen figure at the base of basement steps in heavy shadows, faint pool of low amber light catching a trembling hand reaching forward, unbroken miraculous spark of life, documentary respectful tone."
    },
    {
        "name": "t13_fleeing_hitmen_suburban_night",
        "act": 2,
        "sentences": "2.08#5",
        "desc": "Ba bóng đen sát thủ vội vã lao ra khỏi cửa sau, biến mất vào màn đêm ngoại ô Markham cùng số tiền lẻ từ chiếc ví.",
        "prompt": "Wide dynamic noir view of three shadowy figures bolting across a frost-covered suburban backyard lawn into the dense tree line, car taillights disappearing around a distant corner."
    },
    {
        "name": "t13_panicked_911_call_transcript",
        "act": 2,
        "sentences": "2.10#1–#2",
        "desc": "Bàn điều phối tổng đài 911 với sóng âm thanh nhấp nhô ghi lại tiếng gào khóc kích động của Jennifer lúc 22h35.",
        "prompt": "Emergency dispatch console illuminated by computer monitors displaying glowing green audio waveforms of the frantic 911 recording, digital clock reading 22:35, professional dispatch headset resting on desk."
    },
    {
        "name": "t13_tied_hands_phone_contradiction",
        "act": 2,
        "sentences": "2.10#3–#4",
        "desc": "Góc quay cận cảnh sợi dây thừng lỏng lẻo bên lan can cầu thang và chiếc điện thoại bấm số chính xác, mâu thuẫn vật lý đầu tiên.",
        "prompt": "Forensic close-up illustrating critical physical contradiction: a mobile phone held deftly in unhindered fingers right beside limp slack loops of rope hanging free from the stair rail, glaring logistical impossibility."
    },
    {
        "name": "t13_theatrical_performance_unmasked",
        "act": 2,
        "sentences": "2.10#5–#6",
        "desc": "Chiếc mặt nạ kịch nghệ nứt vỡ bên đường dây điện thoại, sự hoảng loạn giả tạo bị bóc trần dưới góc nhìn điều tra sắc bén.",
        "prompt": "Symbolic noir composition of a cracked theatrical tragedy mask resting beside a twisted landline telephone cord, melodramatic hysterical scream exposed as rehearsed theater, cold chiaroscuro lighting."
    },
    {
        "name": "t13_emergency_responders_flashing_lights",
        "act": 2,
        "sentences": "2.11#1–#2",
        "desc": "Ánh đèn nhấp nháy đỏ xanh của xe cảnh sát và cứu thương phản chiếu trên tuyết lạnh trước căn nhà số 238 Helen Avenue.",
        "prompt": "Dramatic outdoor night shot of 238 Helen Avenue swarmed by York Regional Police cruisers and paramedic ambulances, strobing red and blue emergency beacons casting surreal reflections on fresh suburban snow."
    },
    {
        "name": "t13_unforeseen_variable_destiny",
        "act": 2,
        "sentences": "2.11#3–#4",
        "desc": "Cửa xe cấp cứu đóng lại đưa người cha vào bệnh viện trong cơn hôn mê, biến số định mệnh nằm ngoài kịch bản của kẻ thủ ác.",
        "prompt": "Ambulance rear doors slamming shut in the night, interior amber light illuminating emergency medical equipment rushing the comatose father to Markham Stouffville Hospital, the miraculous variable that unraveled the murder plot."
    },

    # =========================================================================
    # HỒI 3: GIẢI MÃ TÂM LÝ: TỪ 'CHA MẸ HỔ' ĐẾN HỘI CHỨNG NÓI DỐI BỆNH LÝ (11:00 – 16:30)
    # =========================================================================
    {
        "name": "t13_psychological_tragedy_unfolds",
        "act": 3,
        "sentences": "3.02#1–#2",
        "desc": "Bức tranh gia đình ấm cúng bị xé rách làm đôi, để lộ bóng tối sâu thẳm của bi kịch tâm lý học tội phạm hiện đại.",
        "prompt": "Conceptual noir visual of a traditional Asian family portrait cleanly torn down the center, edges curling back to reveal an abyss of deep black void beneath, profound domestic psychological tragedy."
    },
    {
        "name": "t13_crossroads_mythomania_and_pressure",
        "act": 3,
        "sentences": "3.02#3–#4",
        "desc": "Chiếc la bàn tâm lý rạn nứt tại điểm giao nhau giữa hội chứng nói dối bệnh lý và áp lực giáo dục cực đoan.",
        "prompt": "Symbolic split-toned conceptual scene: an antique brass compass with cracked glass face spinning erratically between two opposing magnetic poles labeled Tiger Parenting and Mythomania, glowing amber backlight."
    },
    {
        "name": "t13_tiger_parenting_immigrant_anxiety",
        "act": 3,
        "sentences": "3.03#1–#2",
        "desc": "Chiếc cặp da cũ kỹ và những cuốn sổ làm thêm ca đêm của người nhập cư, nỗi bất an địa vị xã hội dồn lên vai con cái.",
        "prompt": "Still life of a worn factory worker punch card, thermos, and overtime logs beside a stack of prestigious university prep books, deep immigrant existential anxiety channeled into extreme academic expectations."
    },
    {
        "name": "t13_conditional_love_bargain",
        "act": 3,
        "sentences": "3.03#3–#4",
        "desc": "Chiếc cân tâm lý đặt tấm bằng điểm số hoàn hảo một bên và trái tim người mẹ một bên, tình yêu có điều kiện bóp nghẹt tâm hồn.",
        "prompt": "Surreal chiaroscuro metaphor of an antique balance scale: heavy brass weights of perfect grades tipping the balance while an origami paper heart hangs fragile and neglected in the air, conditional love."
    },
    {
        "name": "t13_fear_of_failure_abyss",
        "act": 3,
        "sentences": "3.03#5–#6",
        "desc": "Hố sâu thăm thẳm ngăn cách đứa trẻ với ngưỡng cửa gia đình, nỗi sợ bị ruồng bỏ lớn hơn cả nỗi sợ vi phạm pháp luật.",
        "prompt": "Dramatic architectural metaphor of a tiny silhouetted figure standing on the edge of a deep chasm separating her from a grand welcoming front door, terror of abandonment far outweighing moral boundaries."
    },
    {
        "name": "t13_mythomania_pathological_lying_trap",
        "act": 3,
        "sentences": "3.04#1–#2",
        "desc": "Chiếc gương phản chiếu nhiều khuôn mặt dối trá méo mó, cơ chế tự vệ hoang tưởng Mythomania của cái tôi tổn thương.",
        "prompt": "Psychological noir hall of mirrors with distorted fractured reflections of a faceless silhouette, labyrinth of illusions reflecting endless lies, protective pathology of wounded narcissism and mythomania."
    },
    {
        "name": "t13_sunk_cost_web_of_lies",
        "act": 3,
        "sentences": "3.05#1–#3",
        "desc": "Mạng nhện cơ khí phức tạp kéo căng từng lời dối trá, bẫy chi phí chìm khiến kẻ nói dối không thể quay đầu.",
        "prompt": "Intricate conceptual illustration of a mechanical spiderweb woven from typewriter ribbons, forged signatures, and calendar pages, entrapping a central silhouetted figure in the sunk cost trap of escalating deceit."
    },
    {
        "name": "t13_forgery_factory_blurring_reality",
        "act": 3,
        "sentences": "3.05#4–#5",
        "desc": "Bàn làm việc ngổn ngang con dấu, bằng cấp giả và giấy tờ ngụy tạo, ranh giới giữa hư cấu và thực tại bị xóa nhòa.",
        "prompt": "Atmospheric workspace strewn with official stamp impressions, fake transcripts, pharmacy textbooks, and coffee cups under a harsh green banker lamp, the boundary between reality and fantasy dissolving."
    },
    {
        "name": "t13_cognitive_fragmentation_cage",
        "act": 3,
        "sentences": "3.05#6–#7",
        "desc": "Bức chân dung chia đôi: một nửa là nữ sinh Dược khoa ưu tú rạng rỡ, một nửa là cái bóng cô đơn quằn quại trong lồng giam tinh thần.",
        "prompt": "Striking split portrait in graphic novel noir: right side depicting a brilliant smiling pharmacy graduate in cap and gown, left side showing a weeping trapped shadow behind iron cage bars, cognitive fragmentation."
    },
    {
        "name": "t13_hostile_projection_jailers",
        "act": 3,
        "sentences": "3.06#1–#3",
        "desc": "Ngôi nhà ấm cúng biến dạng thành pháo đài ngục tù sắt thép, cha mẹ biến thành những cai ngục tàn nhẫn trong tâm trí bị tha hóa.",
        "prompt": "Expressionist noir distorted view of a suburban brick house transforming into a foreboding stone penitentiary with watchtower searchlights, parents re-imagined as merciless wardens in a poisoned mind."
    },
    {
        "name": "t13_psychological_rupture_narcissism",
        "act": 3,
        "sentences": "3.07#1–#3",
        "desc": "Tấm gương ái kỷ vỡ vụn thành trăm mảnh sắc nhọn, phản ứng đứt gãy tâm lý phá hủy nguồn cội của sự phán xét.",
        "prompt": "Explosive abstract chiaroscuro of a mirror shattering into flying dagger-like shards under a single bright spotlight, psychological rupture of a cornered vulnerable narcissist annihilating the source of judgment."
    },
    {
        "name": "t13_toxic_inheritance_illusion",
        "act": 3,
        "sentences": "3.07#4–#6",
        "desc": "Ảo ảnh về tự do và quyền thừa kế giàu sang tan biến thành đám mây khói độc, đỉnh cao của sự tha hóa nhân cách.",
        "prompt": "Surreal noir diorama of golden banknotes and sports car silhouettes dissolving into poisonous purple and sulfuric smoke, the grotesque moral corruption of murdering parents for illusory wealth and freedom."
    },
    {
        "name": "t13_truth_seeking_light_ray",
        "act": 3,
        "sentences": "3.08#1–#3",
        "desc": "Tia sáng chân lý xuyên qua những lớp rèm dày đặc và màn sương đen tối, lời nói dối không thể ngăn công lý lộ diện.",
        "prompt": "Powerful cinematic beam of pristine white dawn light cutting through dense murky courtroom curtains, dispelling dark swirling smoke, symbol of unstoppable forensic truth piercing the labyrinth of lies."
    },

    # =========================================================================
    # HỒI 4: ĐẤU TRÍ PHÒNG THẨM VẤN & SỰ THỨC TỈNH CỦA NGƯỜI CHA (16:30 – 21:30)
    # =========================================================================
    {
        "name": "t13_interrogation_room_innocent_act",
        "act": 4,
        "sentences": "4.02#1–#2",
        "desc": "Phòng thẩm vấn hình sự với bức tường xám lạnh, Jennifer ngồi khép nép diễn vai nạn nhân yếu đuối may mắn sống sót.",
        "prompt": "York Regional Police interrogation room, bare utilitarian gray walls, small round laminate table, a diminutive young woman seated meekly with tissue in hand acting the grief-stricken surviving victim."
    },
    {
        "name": "t13_detective_bill_goetz_gaze",
        "act": 4,
        "sentences": "4.02#3–#4",
        "desc": "Ánh mắt sắc lạnh đầy kinh nghiệm của Thám tử William Goetz đối diện nghi phạm qua chiếc bàn kim loại nhẵn bóng.",
        "prompt": "Intense over-the-shoulder shot from behind a seasoned homicide detective in dark suit, piercing analytical gaze fixed across the table, one-way mirror reflecting the quiet duel of wits."
    },
    {
        "name": "t13_unforced_entry_crime_scene_log",
        "act": 4,
        "sentences": "4.03#1–#3",
        "desc": "Sơ đồ hiện trường ngôi nhà với cánh cửa nguyên vẹn và chiếc laptop đắt tiền bỏ quên trên bàn, mâu thuẫn nghiệp vụ rõ rệt.",
        "prompt": "Forensic case binder open on a steel desk, crime scene sketch diagrams of 238 Helen Avenue with unforced entryway stamps, photographs of expensive untouched electronics circled in yellow pencil."
    },
    {
        "name": "t13_sole_survivor_paradox",
        "act": 4,
        "sentences": "4.03#4–#5",
        "desc": "Hai bia dấu đạn dưới tầng hầm đối lập với chiếc ghế nguyên vẹn trên tầng hai, nghịch lý nhân chứng duy nhất còn sống sót.",
        "prompt": "Split forensic diagram contrasting yellow evidence placards of fired bullet casings in the basement against the completely untouched second-floor landing, the chilling anomaly of the spared witness."
    },
    {
        "name": "t13_hospital_icu_miraculous_awakening",
        "act": 4,
        "sentences": "4.05#1–#3",
        "desc": "Màn hình đo nhịp tim ICU nhấp nhô ánh sáng xanh, người cha tỉnh dậy sau hôn mê, ánh mắt sáng tỏ ký ức định mệnh.",
        "prompt": "Hospital intensive care unit in subdued blue lighting, glowing vital signs monitor tracing steady heartbeats, an elderly patient's hand stirring on white sheets, miraculous return from the brink of death."
    },
    {
        "name": "t13_father_memory_unmasked_daughter",
        "act": 4,
        "sentences": "4.06#1–#3",
        "desc": "Ký ức người cha bên giường bệnh: cô con gái đứng thì thầm bình thản với sát thủ giữa phòng khách, không một chút sợ hãi.",
        "prompt": "Eerie memory flash rendered in sepia and dark ink: a daughter standing casually in the hallway murmuring with armed masked intruders without fear, calm complicity that shattered a father's heart."
    },
    {
        "name": "t13_unbound_hands_broken_heart",
        "act": 4,
        "sentences": "4.06#4–#6",
        "desc": "Bàn tay tự do không hề bị trói của cô con gái dẫn lối kẻ thủ ác, nỗi đau vỡ vụn cõi lòng của người cha bị phản bội.",
        "prompt": "Haunting vision of unrestrained bare hands gesturing freely through the house while parents are marched down the stairs, immense emotional anguish of a father realizing his beloved daughter betrayed them to monsters."
    },
    {
        "name": "t13_third_interrogation_november_22",
        "act": 4,
        "sentences": "4.08#1–#2",
        "desc": "Ngày 22/11/2010, căn phòng thẩm vấn bước vào phiên đối đầu quyết định, kỹ thuật thẩm vấn từng bước của Thám tử Goetz.",
        "prompt": "Wide cinematic shot of the climactic third interrogation on November 22, 2010, Detective Bill Goetz leaning forward empathetically, methodically setting the psychological trap with calm surgical precision."
    },
    {
        "name": "t13_forensic_cellphone_text_evidence",
        "act": 4,
        "sentences": "4.08#3–#5",
        "desc": "Tập hồ sơ dày trích xuất dữ liệu viễn thông: hàng trăm tin nhắn chỉ điểm sát thủ của Jennifer và Daniel Wong đặt lên bàn.",
        "prompt": "Forensic close-up of a thick telecommunication audit report slapped onto the table, highlighted text logs documenting exact timestamps between Jennifer and Daniel Wong as the mother walked through the front door."
    },
    {
        "name": "t13_crumbling_mask_confession",
        "act": 4,
        "sentences": "4.08#6–#7",
        "desc": "Khuôn mặt cúi gục trong hai bàn tay run rẩy, giọt nước mắt muộn màng khi Jennifer Pan buộc phải thừa nhận dàn dựng vụ tấn công.",
        "prompt": "High-contrast chiaroscuro portrait of total emotional collapse: a woman's silhouette slumped forward with face buried in trembling hands, the flawless porcelain mask of innocence permanently shattered."
    },
    {
        "name": "t13_deception_body_language_analysis",
        "act": 4,
        "sentences": "4.09#1–#3",
        "desc": "Phân tích cử chỉ dối trá trên màn hình camera giám sát: vuốt tóc, chỉnh áo, đảo mắt và nhịp thở dồn dập của nghi phạm.",
        "prompt": "Split video monitor screen analyzing interrogation body language: timestamped freeze-frames showing rapid eye movement, nervous hair-stroking, collar adjusting, unconscious behavioral cues of cognitive deception overload."
    },
    {
        "name": "t13_final_fabrication_suicide_excuse",
        "act": 4,
        "sentences": "4.09#4–#6",
        "desc": "Lời nói dối cuối cùng về mưu toan tự sát bốc khói trên mặt bàn thẩm vấn, thói quen bóp méo thực tại không bao giờ dứt.",
        "prompt": "Conceptual noir visual of a handwritten suicide note curling into black ash under an interrogator's spotlight, the final desperate fabrication of suicide-for-hire evaporating into cold legal reality."
    },
    {
        "name": "t13_handcuffs_iron_bars_closed",
        "act": 4,
        "sentences": "4.10#1–#3",
        "desc": "Đôi còng số tám khóa chặt trên bàn thẩm vấn kim loại, cánh cửa sắt trại giam đóng sập lại, kết thúc 10 năm kịch nghệ.",
        "prompt": "Definitive justice shot: heavy steel handcuffs clicked shut on a metal table, heavy reinforced jail door closing behind vertical shadow bars, the ten-year masquerade ending in cold penal custody."
    },

    # =========================================================================
    # HỒI 5: BẢN ÁN LƯƠNG TÂM & LỜI CẢNH TỈNH (21:30 – 26:30)
    # =========================================================================
    {
        "name": "t13_supreme_court_ontario_verdict",
        "act": 5,
        "sentences": "5.02#1–#2",
        "desc": "Phòng xử án Tòa Thượng thẩm Ontario uy nghiêm, búa thẩm phán gõ xuống phán quyết tù chung thân 25 năm không ân xá.",
        "prompt": "Solemn interior of the Ontario Superior Court of Justice in Newmarket, carved wooden judge's bench with polished gavel, silhouetted jury box delivering the verdict of First-Degree Murder and Life Imprisonment."
    },
    {
        "name": "t13_court_appeals_conscience_sentence",
        "act": 5,
        "sentences": "5.02#3–#4",
        "desc": "Chồng hồ sơ kháng cáo 2025–2026 bên cạnh chiếc đồng hồ cát thời gian, bản án lương tâm ngàn đời không thể xóa bỏ.",
        "prompt": "Still life of bound appellate legal briefs labeled Supreme Court of Canada 2025-2026 beside a dark hourglass with trickling sand, inescapable eternal life sentence of human conscience."
    },
    {
        "name": "t13_detective_dossier_lasting_trauma",
        "act": 5,
        "sentences": "5.03#1–#3",
        "desc": "Tập hồ sơ khép lại trên bàn làm việc của cơ quan điều tra, vết sẹo tinh thần và thể xác không tiền tài nào bù đắp nổi.",
        "prompt": "Somber police investigator's desk at twilight, closed manila case file stamped CLOSED, reflections on the tragic vanity of insurance payouts that can never heal the lifelong physical and emotional wounds of a father."
    },
    {
        "name": "t13_dialogue_breakdown_family_ruin",
        "act": 5,
        "sentences": "5.04#1–#4",
        "desc": "Chiếc bàn ăn gia đình trống trải, chiếc ghế cách xa nhau trong bóng tối, hậu quả của sự im lặng và thiếu vắng đối thoại.",
        "prompt": "Haunting architectural view of an empty suburban dining table set for dinner, chairs pulled apart in cold shadows, poignant visual of the destruction of empathy and the lethal silence of authoritarian parenting."
    },
    {
        "name": "t13_four_redflags_overview_banner",
        "act": 5,
        "sentences": "5.05#1",
        "desc": "Tấm bảng cảnh báo 4 Dấu hiệu cảnh báo đỏ (Red Flags) phòng ngừa áp lực độc hại gia đình bừng sáng trên nền noir.",
        "prompt": "Graphic noir informational display board presenting four distinct glowing crimson caution emblems, educational behavioral psychology forensic framework for identifying toxic family pressures."
    },
    {
        "name": "t13_redflag1_conditional_love_punishment",
        "act": 5,
        "sentences": "5.05#2–#4",
        "desc": "Cảnh báo đỏ 1: Chiếc cân vàng đong đếm điểm số và tình yêu thương, bên cạnh chiếc roi kỷ luật khắc nghiệt.",
        "prompt": "Conceptual noir warning visual: golden scales demanding perfection beside a broken pencil and strict disciplinary rod, crimson alert hue, Red Flag 1 Conditional Love and Extreme Punishment of Failure."
    },
    {
        "name": "t13_redflag2_escalating_web_of_lies",
        "act": 5,
        "sentences": "5.05#5–#7",
        "desc": "Cảnh báo đỏ 2: Chiếc mạng nhện dối trá bọc kín những văn bằng giấy tờ giả, lời dối trá nhỏ leo thang thành thảm họa.",
        "prompt": "Conceptual noir warning visual: delicate cobweb spinning outwards from a single forged report card to encompass forged diplomas and false lifestyles, Red Flag 2 Escalating Web of Pathological Deceit."
    },
    {
        "name": "t13_redflag3_total_control_autonomy_loss",
        "act": 5,
        "sentences": "5.05#8–#10",
        "desc": "Cảnh báo đỏ 3: Chiếc lồng chim sắt giam cầm đôi cánh tự do bên những chiếc khóa phong tỏa phương tiện liên lạc.",
        "prompt": "Conceptual noir warning visual: an open iron birdcage tangled with severed telephone wires and padlocked journals, crimson glow, Red Flag 3 Total Authoritarian Control and Stripping of Personal Autonomy."
    },
    {
        "name": "t13_redflag4_emotional_disconnect_rupture",
        "act": 5,
        "sentences": "5.05#11–#13",
        "desc": "Cảnh báo đỏ 4: Bức tường gạch ngăn cách hai bàn tay trong bóng tối, sự mất kết nối cảm xúc dẫn tới đứt gãy nhân tính.",
        "prompt": "Conceptual noir warning visual: an impenetrable cold stone wall separating two silhouetted hands reaching toward each other in darkness, Red Flag 4 Complete Emotional Disconnection and Psychological Rupture."
    },
    {
        "name": "t13_authentic_soul_open_window_dawn",
        "act": 5,
        "sentences": "5.05#14",
        "desc": "Cửa sổ phòng ngủ mở rộng đón ánh bình minh ấm áp, cuốn sách mở trang trắng, biểu tượng tâm hồn tự do và trung thực.",
        "prompt": "Inspiring serene wide shot of an open bedroom window overlooking a gentle golden sunrise, curtains billowing softly in fresh morning air, blank open journal on the sill, sovereign freedom of an honest life."
    },
    {
        "name": "t13_amber_eyes_closing_dossier_jennifer",
        "act": 5,
        "sentences": "5.05#15–#17",
        "desc": "Tập hồ sơ Amber Eyes khép lại trang nghiêm, đôi mắt cú hổ phách tỏa ánh sáng trí tuệ trên nền nhung đen.",
        "prompt": "Signature Amber Eyes closing scene, dark leather-bound case file folder closing solemnly on a dark mahogany desk, glowing golden amber owl eye circular emblem illuminating the cover, elegant noir insignia."
    }
]

def main():
    WORK.mkdir(parents=True, exist_ok=True)
    
    bg_jobs_path = WORK / "bg_jobs_tap13.json"
    bg_jobs_path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo {bg_jobs_path} ({len(jobs)} jobs) thành công!")

    # Tạo gemini_image_prompts_tap13.json
    gemini_prompts = []
    for j in jobs:
        gemini_prompts.append({
            "name": j["name"],
            "act": j["act"],
            "sentences": j["sentences"],
            "desc": j["desc"],
            "aspect_ratio": "16:9",
            "resolution": "2K (2112x1188)",
            "style": "Dark Graphic Novel Noir with Chiaroscuro",
            "prompt": j["prompt"]
        })

    gemini_prompts_path = WORK / "gemini_image_prompts_tap13.json"
    gemini_prompts_path.write_text(json.dumps(gemini_prompts, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo {gemini_prompts_path} ({len(gemini_prompts)} prompts) thành công!")

if __name__ == "__main__":
    main()
