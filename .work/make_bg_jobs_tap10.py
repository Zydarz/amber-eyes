import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

jobs = [
    # =========================================================================
    # HỒI 1: CHUYẾN XE ĐỊNH MỆNH VÀ CHIẾC HỘP ĐEN DƯỚI GẦM GIƯỜNG (00:00 – 05:30)
    # =========================================================================
    {
        "name": "t10_hitchhiking_highway_1977",
        "act": 1,
        "sentences": "1.02#1–#3",
        "desc": "Xa lộ ven biển Bờ Tây ngập nắng vàng hoài niệm năm 1977, bóng thanh niên mang ba lô vẫy xe xin quá giang trên lề đường trải dài, phong cách graphic noir cổ điển.",
        "prompt": "Cinematic 16:9 wide shot of a sun-drenched Pacific West Coast interstate highway in late 1970s America, golden hour light casting long dramatic silhouettes of young hitchhikers with backpacks standing on gravel roadside, vintage camper vans and classic sedans passing by, nostalgic warm amber and dusky slate tones, dark graphic novel noir style, fine film grain."
    },
    {
        "name": "t10_traveler_backpack_worn_map",
        "act": 1,
        "sentences": "1.02#4–#5",
        "desc": "Tĩnh vật ba lô vải sờn, vài cuốn sách giấy ố vàng và tấm bản đồ đường bộ California gập nếp đặt trên mỏm đá ven đường, ánh nắng chiều tà ấm áp.",
        "prompt": "Atmospheric still life of a weathered 1970s canvas traveler backpack, several vintage paperback books, and a creased unfolded road map resting on sun-baked roadside rocks, golden dust motes dancing in warm side-light, poignant innocent youth aesthetic, heavy ink linework, dark chiaroscuro."
    },
    {
        "name": "t10_golden_innocence_road_illusion",
        "act": 1,
        "sentences": "1.02#6",
        "desc": "Cung đường cao tốc thẳng tắp chạy về chân trời hoàng hôn rực lửa, nhưng phía xa bầu trời chuyển dần sang màu tím thẫm đe dọa, báo hiệu cạm bẫy định mệnh.",
        "prompt": "Dramatic establishing shot of an endless two-lane highway stretching straight toward an ominous bruised-crimson horizon, radiant golden sunset giving way to deep obsidian storm clouds in the far distance, stark chiaroscuro noir, sense of impending unseen trap."
    },
    {
        "name": "t10_route99_eugene_roadside",
        "act": 1,
        "sentences": "1.04#1–#2",
        "desc": "Biển báo mốc Quốc lộ 99 trong làn sương sớm tại Eugene bang Oregon, bóng một cô gái trẻ mang ba lô giơ ngón tay cái bên rặng linh sam u tịch.",
        "prompt": "Moody early morning roadside scene along historic Route 99 near Eugene, Oregon, towering Douglas fir tree silhouettes shrouded in cool blue mist, silhouetted young woman with backpack raising her thumb for a ride, solitary figure, high-contrast graphic novel noir."
    },
    {
        "name": "t10_birthday_invitation_youth",
        "act": 1,
        "sentences": "1.04#3–#4",
        "desc": "Thiệp mời sinh nhật viết tay phong cách thập niên 70 trên mặt bàn gỗ bên tách trà nguội, ánh sáng xiên rọi qua cửa sổ mộc mạc.",
        "prompt": "Forensic still life of a handwritten 1977 birthday party invitation card lying next to a small brass key and an unlit birthday candle on rustic wooden table, soft diagonal shaft of amber morning light cutting across dark wood planks, nostalgic hopeful tone, noir linework."
    },
    {
        "name": "t10_blue_dodge_van_approaching",
        "act": 1,
        "sentences": "1.06#1–#3",
        "desc": "Chiếc xe tải nhỏ Dodge màu xanh lam cổ điển đang từ từ giảm tốc tấp vào lề sỏi, bụi đường bay lơ lửng trong ráng chiều vàng cam.",
        "prompt": "Exterior cinematic shot of a vintage 1970s blue Dodge van slowing down on the gravel shoulder of a lonely rural highway, dust swirling in the golden amber afternoon backlight, long shadow stretching toward the viewer, deceptive domestic appearance, graphic noir."
    },
    {
        "name": "t10_innocent_family_facade",
        "act": 1,
        "sentences": "1.06#4–#5",
        "desc": "Góc nhìn từ ngoài vào cabin xe qua kính chắn gió mờ ảo: bóng cặp vợ chồng trẻ bế đứa trẻ sơ sinh, bức bình phong gia đình hoàn hảo che đậy ác quỷ.",
        "prompt": "Intriguing interior-exterior composite looking through the windshield of a vintage van, shadowy silhouettes of a young mother holding an infant baby in the passenger seat and a driver in profile, deceptive facade of pure domestic warmth, heavy chiaroscuro ink contours."
    },
    {
        "name": "t10_stepping_into_abyss_trap",
        "act": 1,
        "sentences": "1.06#6",
        "desc": "Bàn chân bước lên bậc thang cửa trượt của chiếc xe van, bóng tối sâu thẳm bên trong cabin nuốt chửng ánh sáng ban ngày.",
        "prompt": "Tense low-angle macro shot of a traveler sneaker stepping onto the running board of an open van sliding door, deep pitch-black interior yawning like an abyss, harsh sunlight cutting across the doorframe, chilling sense of no return, dark graphic novel illustration."
    },
    {
        "name": "t10_empty_birthday_table",
        "act": 1,
        "sentences": "1.07#1–#3",
        "desc": "Gian phòng tiệc sinh nhật về đêm với những chiếc ghế trống trơn, chiếc bánh sinh nhật chưa thắp nến nằm cô độc trên khăn trải bàn sẫm màu.",
        "prompt": "Interior of a dimly lit 1970s suburban living room at midnight, untouched birthday cake with twenty unlit candles sitting on an empty festive table, deflated balloons lying on floorboards, solemn silence and rising dread, noir chiaroscuro lighting."
    },
    {
        "name": "t10_missing_flyer_gas_station",
        "act": 1,
        "sentences": "1.07#4–#7",
        "desc": "Hàng loạt tờ rơi tìm người mất tích dán trên cột bơm xăng và bảng tin ven Quốc lộ 99, gió đêm lay nhẹ mép giấy trong ánh đèn huỳnh quang nhấp nháy.",
        "prompt": "Atmospheric nighttime shot of a lonely rural Route 99 gas station under flickering cold neon light, black-and-white missing person posters pinned to a weathered wooden board, telephone booth in background, wind-blown dust, somber investigative documentary aesthetic."
    },
    {
        "name": "t10_red_bluff_pine_forest_road",
        "act": 1,
        "sentences": "1.09#1–#2",
        "desc": "Con đường mòn đất gồ ghề rẽ sâu vào rừng thông Red Bluff California hoang vu, những thân cây thông cổ thụ cao vút chặn đứng ánh hoàng hôn.",
        "prompt": "Eerie low-angle establishing shot of a secluded dirt logging trail veering off into dense pine forests near Red Bluff, California, towering pine trunks forming a suffocating natural barricade, dying dusk light filtering through needles, sinister isolation, noir style."
    },
    {
        "name": "t10_sawmill_lumber_yard_dusk",
        "act": 1,
        "sentences": "1.10#1",
        "desc": "Xưởng cưa gỗ địa phương Red Bluff trong buổi chạng vạng, đống gỗ thông xẻ chồng chất cao, lưỡi cưa tròn khổng lồ in bóng đen trên vách tôn rỉ sét.",
        "prompt": "Industrial noir landscape of a small-town California sawmill lumber yard at twilight, massive stacks of rough-cut timber planks, silhouette of giant industrial circular saw blades against a bruised evening sky, sawdust floating in air, ominous working-class setting."
    },
    {
        "name": "t10_knife_shadow_ambush",
        "act": 1,
        "sentences": "1.10#2",
        "desc": "Bóng đen kẻ săn mồi vung lưỡi dao găm trong không gian chật hẹp của cabin xe, ánh kim loại lóe sáng tương phản cao trên nền đen mực, tuyệt đối không máu me.",
        "prompt": "Stark high-contrast chiaroscuro silhouette composition inside a darkened vehicle cabin, sharp cold glint of a hunting knife edge silhouetted against moonlit window, rope coils on seat, strictly no gore, no blood, pure psychological menace, graphic novel noir."
    },
    {
        "name": "t10_soundproof_headbox_forensic",
        "act": 1,
        "sentences": "1.10#3–#6",
        "desc": "Tĩnh vật pháp y chiếc hộp gỗ cách âm đội đầu nặng 10kg đóng bằng ván ép dày, lót mút xốp đen và các lỗ thông khí nhỏ xíu, ánh đèn bàn kỹ thuật rọi xiên.",
        "prompt": "Forensic still life of the notorious handmade wooden headbox, constructed of heavy reinforced plywood lined with dark acoustic foam, small precision ventilation holes drilled along the side, resting on an evidence table under harsh circular spotlight, graphic noir ink art."
    },
    {
        "name": "t10_isolated_red_bluff_cabin",
        "act": 1,
        "sentences": "1.10#7–1.11#1",
        "desc": "Căn nhà gỗ biệt lập ẩn sâu trong rừng thông Red Bluff giữa màn đêm u tối, một đốm sáng le lói từ cửa sổ tầng hầm, sương mù lơ lửng mặt đất.",
        "prompt": "Nocturnal establishing view of a secluded single-story timber cabin in the dense woods of Red Bluff, California at 3 AM, single faint yellow light glowing from a low crawlspace window, pale moonlight filtering through thick pine boughs, chilling quiet dread."
    },
    {
        "name": "t10_wooden_box_under_bed_shadow",
        "act": 1,
        "sentences": "1.11#2–#3",
        "desc": "Gian phòng ngủ chìm trong bóng tối, dưới gầm giường đệm nước cồng kềnh là chiếc hộp gỗ đóng kín bằng then sắt, cánh cửa địa ngục 7 năm mở ra.",
        "prompt": "Dark chiaroscuro interior of a bedroom floor in deep shadow, heavy frame of a large bulky waterbed looming overhead, beneath it a narrow coffin-like wooden box with heavy iron sliding latch firmly shut, pitch-black abyss, poignant psychological horror."
    },

    # =========================================================================
    # HỒI 2: BẢY NĂM TRONG BÓNG TỐI VÀ SỰ BIẾN MẤT CỦA THỜI GIAN (05:30 – 11:00)
    # =========================================================================
    {
        "name": "t10_coffin_box_claustrophobia",
        "act": 2,
        "sentences": "2.02#1–#2",
        "desc": "Góc nhìn ngột ngạt từ bên trong chiếc hộp gỗ hẹp dài chưa đầy 2m, bóng tối đặc quánh, một vệt sáng mỏng như sợi chỉ lọt qua khe ván ép.",
        "prompt": "Intensely claustrophobic subjective view from inside a pitch-black wooden box measuring under two meters in length, absolute sensory darkness broken only by a microscopic hairline slit of cold light along the wooden seam, dust floating in void, dark graphic noir."
    },
    {
        "name": "t10_stiff_hands_wooden_slats",
        "act": 2,
        "sentences": "2.02#3–#4",
        "desc": "Bóng dáng đôi bàn tay co quắp chạm vào những thớ gỗ ván ép thô ráp không thể trở mình trong chiếc hộp kín, ánh sáng tối giản chiaroscuro.",
        "prompt": "Macro chiaroscuro composition of silhouetted fingers pressing against rough splintered unvarnished plywood texture in extreme confinement, inability to stretch limbs, profound physical torment and psychological isolation, graphic novel ink drawing."
    },
    {
        "name": "t10_heavy_iron_latches_padlock",
        "act": 2,
        "sentences": "2.04#1, #4",
        "desc": "Then cài sắt kiên cố và ổ khóa công nghiệp hoen gỉ chốt chặt bên ngoài thành hộp gỗ dày dặn, ngăn chặn mọi nỗ lực thoát thân.",
        "prompt": "Forensic close-up of heavy industrial iron sliding hasps and a thick steel padlock bolted securely onto heavy plywood planks, scratched wood surface, harsh raking light revealing mechanical coldness and absolute captivity, noir style."
    },
    {
        "name": "t10_waterbed_crushing_weight",
        "act": 2,
        "sentences": "2.04#2–#3",
        "desc": "Góc nhìn từ mặt sàn hướng lên sức nặng đè nén ngột ngạt của khung giường đệm nước cồng kềnh ép chặt chiếc hộp bên dưới, bóng tối bóp nghẹt không gian.",
        "prompt": "Low-angle dramatic shot showing the oppressive massive wooden frame of a 1970s waterbed looming directly over the wooden box on the carpeted floor, visual metaphor of insurmountable crushing weight, deep ink black shadows, somber palette."
    },
    {
        "name": "t10_one_hour_chores_silhouette",
        "act": 2,
        "sentences": "2.04#5",
        "desc": "Bóng một người phụ nữ cúi mình lau sàn nhà gỗ trong căn bếp heo hút dưới bóng đổ dài của kẻ canh giữ, ánh đèn treo lơ lửng trên trần.",
        "prompt": "Subdued interior shot of a shadowy domestic kitchen, silhouette of a woman on her knees scrubbing dark floorboards under harsh single overhead bare lightbulb, menacing tall shadow of captor cast across doorway, grim daily routine, graphic noir."
    },
    {
        "name": "t10_hooker_community_mask",
        "act": 2,
        "sentences": "2.05#1–#3",
        "desc": "Khu dân cư ngoại ô thanh bình ngập nắng, bóng người đàn ông mỉm cười trò chuyện với hàng xóm bên hàng rào gỗ trắng, vỏ bọc công dân mẫu mực.",
        "prompt": "Sunny suburban street in Red Bluff California during the late 70s, silhouette of an apparently respectable polite family man chatting over a white picket fence with neighbors, church spire in distance, stark irony of deceptive social facade, graphic noir."
    },
    {
        "name": "t10_dark_dominance_psychopathy",
        "act": 2,
        "sentences": "2.05#4–#5",
        "desc": "Gian xưởng mộc tối tăm với các dụng cụ cưa đục sắc lạnh treo trên tường, bóng một kẻ đứng trầm ngâm toan tính quyền lực thống trị cực đoan.",
        "prompt": "Dark woodworking workshop interior, silhouette of a brooding man surrounded by sharp hand saws, chisels, and heavy steel clamps hanging on wall pegs, single spotlight carving deep facial shadows, psychological portrait of extreme narcissism."
    },
    {
        "name": "t10_sensory_deprivation_clock_melt",
        "act": 2,
        "sentences": "2.06#1–#4",
        "desc": "Biểu tượng siêu thực noir về hội chứng tước đoạt cảm giác: chiếc đồng hồ quả quýt không có kim lơ lửng tan biến giữa bóng tối vô tận.",
        "prompt": "Surreal psychological noir representation of sensory deprivation syndrome: a vintage pocket watch floating in absolute black void with its hour and minute hands completely erased, cracked glass, melting into darkness, collapse of temporal reality."
    },
    {
        "name": "t10_childhood_poems_faint_echo",
        "act": 2,
        "sentences": "2.06#5–#6",
        "desc": "Thành trì tinh thần nội tâm: những trang kinh thánh vintage mở và câu thơ tuổi thơ phát sáng mờ ảo giữa khoảng không tăm tối, ngọn lửa hy vọng mong manh.",
        "prompt": "Poignant conceptual noir art of an open weathered Bible and faint glowing handwritten childhood verse scripts suspended in dark mist, a tiny ember of inner light resisting suffocating surrounding blackness, resilience of the human mind."
    },
    {
        "name": "t10_the_company_shadow_syndicate",
        "act": 2,
        "sentences": "2.08#1–#3",
        "desc": "Bóng ma tổ chức tội phạm ngầm The Company: hàng loạt bóng đen mặc áo măng tô và mũ fedora đứng dưới ánh đèn đường mờ ảo, mạng lưới vô hình rình rập.",
        "prompt": "Ominous cinematic noir visualization of the fabricated syndicate 'The Company': an eerie row of shadowy figures in trench coats and fedoras lurking under misty streetlights, interconnected web of surveillance lines, psychological paranoia construct."
    },
    {
        "name": "t10_family_home_under_surveillance",
        "act": 2,
        "sentences": "2.08#4",
        "desc": "Ngôi nhà của cha mẹ nạn nhân trong đêm nhìn qua tâm ngắm ống nhòm gián điệp, lời đe dọa sát hại giả tưởng trói buộc ý chí người con gái.",
        "prompt": "Chilling nocturnal view of a peaceful suburban house viewed through a circular sniper lens or surveillance binocular crosshair from a parked car across the dark street, fabricated threat of ruthless retaliation, graphic novel noir."
    },
    {
        "name": "t10_written_slave_contract_quill",
        "act": 2,
        "sentences": "2.09#1–#4",
        "desc": "Bản hợp đồng nô lệ quái dị được đánh máy trên giấy ố vàng với con dấu sáp đỏ và chữ ký ép buộc đặt trên bàn gỗ mun, chiếc cùm xích tinh thần.",
        "prompt": "Forensic close-up of the typed 'slave contract' document resting on a dark desk, archaic legalistic clauses, dark red wax seal impression, vintage typewriter ribbon in background, stark high-contrast chiaroscuro, symbolic death of human rights."
    },
    {
        "name": "t10_darkness_as_false_shelter",
        "act": 2,
        "sentences": "2.10#1–#3",
        "desc": "Bóng dáng người ngồi co ro bên trong chiếc hộp hé nắp, nhìn ra thế giới bên ngoài đầy cạm bẫy tưởng tượng, chiếc hộp trở thành nơi trú ẩn méo mó.",
        "prompt": "Deep psychological silhouette view looking out from inside the wooden box toward a cracked open door, outside world rendered as threatening shadowy silhouettes, twisted cognition where captivity feels like false sanctuary to protect loved ones, noir art."
    },
    {
        "name": "t10_clock_hands_seven_years",
        "act": 2,
        "sentences": "2.11#1–#2",
        "desc": "Mặt đồng hồ cổ điển với những vệt kim quay mờ ảo trên vách gỗ mục nát, 2.660 ngày trôi qua trong câm lặng trước khi biến cố xảy ra.",
        "prompt": "Metaphorical time-lapse composition of an antique wooden pendulum wall clock, blurred motion trails of spinning clock hands, marks carved into dark timber, silent passage of seven long years, dramatic side lighting, fine grain noir."
    },

    # =========================================================================
    # HỒI 3: NGHỊCH LÝ NGÀY VỀ VÀ SỰ BẤT LỰC TẬP NHIỄM (11:00 – 16:30)
    # =========================================================================
    {
        "name": "t10_riverside_california_bungalow",
        "act": 3,
        "sentences": "3.02#1–#2",
        "desc": "Con phố ngoại ô thành phố Riverside bang California rực rỡ nắng ấm tháng 3 năm 1981, ngôi nhà cũ của cha mẹ nạn nhân với hàng rào hoa giấy.",
        "prompt": "Exterior daylight view of a sunny tree-lined residential avenue in Riverside, California in March 1981, modest single-story stucco family home with neat lawn and driveway, deceptive suburban tranquility, contrast of warmth and hidden trauma, noir styling."
    },
    {
        "name": "t10_front_door_unbelievable_return",
        "act": 3,
        "sentences": "3.04#1–#2",
        "desc": "Cánh cửa chính ngôi nhà cũ mở toang, người mẹ đứng sững sờ nghẹn ngào khi thấy người con gái mất tích 4 năm xuất hiện bằng xương bằng thịt trước hiên.",
        "prompt": "Emotional high-contrast threshold shot from inside an open front doorway, silhouette of a weeping mother seeing her long-lost daughter standing on the sunlit porch after four years, trembling embrace on the brink, poignant chiaroscuro linework."
    },
    {
        "name": "t10_polite_boyfriend_facade",
        "act": 3,
        "sentences": "3.04#3–#5",
        "desc": "Phòng khách gia đình ấm cúng, kẻ bắt cóc ngồi trên ghế bành lịch thiệp nhấp tách trà, đóng vai người bạn trai chu đáo hoàn hảo trước mặt cha mẹ.",
        "prompt": "Interior living room drama, silhouette of Cameron Hooker sitting politely in an armchair sipping coffee, crisp collared shirt, smiling charming facade, family tea set on coffee table, chilling undertone of calculated deception, graphic novel noir."
    },
    {
        "name": "t10_tense_family_dinner_shadows",
        "act": 3,
        "sentences": "3.04#6",
        "desc": "Bàn ăn gia đình với đĩa sứ và hoa tươi, mọi người ngồi quây quần nhưng những bóng đen dài trên tường đan xen đầy ngột ngạt và căng thẳng ngầm.",
        "prompt": "Atmospheric wide shot of a family dinner table laden with warm food, overhead dining pendant lamp casting long sinister intersecting shadows across the wallpaper, unspoken tension hanging thick in the air, psychological crime documentary art."
    },
    {
        "name": "t10_bathroom_mirror_downcast_eyes",
        "act": 3,
        "sentences": "3.05#1–#3",
        "desc": "Khoảnh khắc đứng một mình trước gương phòng tắm, vòi nước chảy róc rách, ánh mắt cúi gằm đượm buồn không dám cất tiếng cầu cứu vì sợ hãi.",
        "prompt": "Solemn interior shot of a vintage bathroom, running water in a porcelain sink, silhouette of a young woman leaning on counter with downcast sorrowful eyes staring at her reflection, trapped in invisible psychic bonds, deep charcoal shadows."
    },
    {
        "name": "t10_father_concerned_inquiry",
        "act": 3,
        "sentences": "3.05#4–#5",
        "desc": "Bóng người cha nắm lấy tay con gái gặng hỏi đầy âu lo, nhưng bóng đen vô hình của tổ chức ngầm bóp nghẹt lời đáp khiến cô chỉ biết cúi đầu.",
        "prompt": "Intimate chiaroscuro frame of an elderly father leaning forward, tenderly holding his daughter's trembling hands, shadowy silhouette behind her metaphorically silencing her lips, heartbreaking conflict between love and terror, noir ink style."
    },
    {
        "name": "t10_packed_suitcase_return_car",
        "act": 3,
        "sentences": "3.05#6",
        "desc": "Chiếc vali nhỏ đặt lại vào cốp xe bên lề đường, cô gái ngoan ngoãn bước lên xe quay về căn nhà gỗ Red Bluff, nghịch lý gây chấn động.",
        "prompt": "Melancholic street shot at twilight, small leather suitcase being closed into a car trunk, figure voluntarily stepping into the passenger seat to return to her captor's cabin, quiet tragic surrender, long headlights sweeping the empty asphalt."
    },
    {
        "name": "t10_open_door_paradox_dilemma",
        "act": 3,
        "sentences": "3.06#1–#3",
        "desc": "Hình tượng ẩn dụ về nghịch lý tự do: cánh cửa lớn mở toang hướng ra cánh đồng ngập nắng, nhưng chiếc bóng đứng bất động không bước qua ngưỡng cửa.",
        "prompt": "Powerful philosophical metaphor of an open heavy timber door leading out to an expanse of sunlit golden fields, yet a solitary human silhouette remains immobilized inside the dark threshold, questioning the psychological mechanism of confinement."
    },
    {
        "name": "t10_martin_seligman_learned_helplessness",
        "act": 3,
        "sentences": "3.07#1–#2",
        "desc": "Sơ đồ tâm lý học nghiên cứu của Giáo sư Martin Seligman về Sự bất lực tập nhiễm (Learned Helplessness), các đồ thị thực nghiệm trên bảng đen học thuật.",
        "prompt": "Academic noir illustration of psychological research laboratory diagrams, blackboard chalk drawings depicting Martin Seligman's theory of Learned Helplessness, neural pathways of surrender, clean stark linework, amber chalk accents."
    },
    {
        "name": "t10_open_cage_motionless_silhouette",
        "act": 3,
        "sentences": "3.07#3",
        "desc": "Chiếc lồng chim bằng sắt mở toang cánh cửa nhưng bóng chú chim vẫn đậu yên bất động trên thanh gỗ mục, sự tê liệt ý chí phản kháng.",
        "prompt": "Poignant visual allegory of an ornate iron birdcage with its door swung wide open, inside a small bird silhouette sits motionless on its perch having unlearned the will to fly, raking spotlight on empty bars, dark graphic novel art."
    },
    {
        "name": "t10_window_sniper_paranoia_shadow",
        "act": 3,
        "sentences": "3.08#1–#4",
        "desc": "Khung cửa sổ phòng khách nhìn ra màn đêm, ảo ảnh những tay súng bắn tỉa của The Company đang rình rập, nỗi sợ hãi gia đình bị hại trói chặt đôi chân.",
        "prompt": "Psychological terror view through lace curtains toward dark nocturnal trees, phantom shadows of unseen snipers aiming at the house, invisible chains forged of protective love for parents holding the captive captive, chiaroscuro noir."
    },
    {
        "name": "t10_trauma_bonding_bread_and_whip",
        "act": 3,
        "sentences": "3.09#1–#4",
        "desc": "Cơ chế gắn kết chấn thương (Trauma Bonding): bàn tay trao mẩu bánh mì ân huệ nhỏ giọt bên cạnh chiếc roi sắt trừng phạt, chiếc bẫy phụ thuộc cảm xúc.",
        "prompt": "Symbolic chiaroscuro still life representing Trauma Bonding: a single hand offering a small crust of bread and a sip of water bathed in gentle amber light, directly juxtaposed against iron shackles in deep shadow, predatory intermittent reinforcement."
    },
    {
        "name": "t10_captor_as_sole_savior_complex",
        "act": 3,
        "sentences": "3.09#5–#6",
        "desc": "Hình bóng khổng lồ của kẻ thao túng đứng trên cao đưa tay xuống vực sâu tối đen, nạn nhân bám víu như chiếc phao cứu sinh duy nhất để tồn tại.",
        "prompt": "Psychological silhouette composition of a giant dark figure towering over a deep shadowy trench, offering a single hand to an isolated figure below, disturbing Stockholm syndrome dependency where the abuser becomes the sole perceived protector."
    },
    {
        "name": "t10_invisible_timber_prison_mind",
        "act": 3,
        "sentences": "3.10#1–#2",
        "desc": "Nhà tù vô hình trong tâm trí kiên cố hơn ngàn lần ván ép: bóng dáng con người bị bao bọc bởi những tấm vách gỗ ảo giác và xiềng xích vô hình.",
        "prompt": "Abstract psychological noir illustration of a human mind enclosed within towering metaphysical wooden planks and interlocking invisible iron chains, a tiny spark of distant starlight piercing the gloom from above, question of redemption."
    },

    # =========================================================================
    # HỒI 4: SỰ RẠN NỨT CỦA LỒNG GIAM VÀ CUỘC GIẢI CỨU NGẦM (16:30 – 21:30)
    # =========================================================================
    {
        "name": "t10_seventh_year_toddler_toys_shadow",
        "act": 4,
        "sentences": "4.02#1–#3",
        "desc": "Năm thứ 7 của sự giam cầm (1984): sàn nhà với đồ chơi trẻ em bằng gỗ và thú bông, vết nứt đầu tiên xuất hiện trong căn nhà kẻ bắt cóc.",
        "prompt": "Interior of the Red Bluff cabin living room in 1984, vintage wooden rocking horse and scattered toddler toys on the rug, sunlight creeping under the heavy bedroom door, impending collapse of a seven-year domestic fortress, graphic noir."
    },
    {
        "name": "t10_janice_hooker_moral_turmoil",
        "act": 4,
        "sentences": "4.03#1–#4",
        "desc": "Bóng dáng người vợ Janice Hooker đứng bên bồn rửa chén trong đêm, nhìn hai đứa con nhỏ đang ngủ say, sự giằng xé lương tâm và nỗi sợ hãi tột cùng.",
        "prompt": "Haunting nocturnal interior, silhouette of Janice Hooker standing by the kitchen window clutching her temples, through open doorway two sleeping children in cribs are visible, crushing moral torment and breaking point of an accomplice, noir ink style."
    },
    {
        "name": "t10_second_victim_shadow_threat",
        "act": 4,
        "sentences": "4.04#1–#2",
        "desc": "Chiếc móc áo trống thứ hai trên hành lang tối tăm, kế hoạch điên loạn của kẻ săn mồi muốn bắt thêm nạn nhân mới làm giọt nước tràn ly.",
        "prompt": "Foreboding hallway shot in high contrast, two empty wire coat hangers hanging against a cracked wooden wall, single harsh bulb swinging slightly, visual metaphor for the horrifying demand to capture a second victim, triggering rebellion."
    },
    {
        "name": "t10_church_pastor_confession_shadow",
        "act": 4,
        "sentences": "4.05#1–#5",
        "desc": "Gian nhà thờ gỗ Red Bluff vắng lặng, ánh sáng từ ô cửa kính màu chiếu xuống bóng người phụ nữ quỳ thú nhận tội lỗi trước vị mục sư nhân hậu.",
        "prompt": "Solemn interior of a modest rural church, colorful shafts of muted sunlight streaming through stained-glass windows onto a weeping woman kneeling in prayer before a compassionate silhouetted pastor, moral awakening and decision to save a life."
    },
    {
        "name": "t10_august_escape_car_morning_dust",
        "act": 4,
        "sentences": "4.05#6",
        "desc": "Buổi sáng ngày 9 tháng 8 năm 1984, chiếc xe hơi vội vã lao đi trên đường sỏi rời khỏi thị trấn Red Bluff trong khi kẻ thủ ác đang ở xưởng cưa.",
        "prompt": "Cinematic chase establishing shot on the morning of August 9, 1984, vintage station wagon speeding down a rural gravel road kicking up billows of amber dust, leaving the dark pine timber mill behind in the rearview mirror, urgent flight to freedom."
    },
    {
        "name": "t10_truth_revealed_shattered_phantom",
        "act": 4,
        "sentences": "4.05#7–#8",
        "desc": "Tấm gương nứt vỡ phản chiếu dòng chữ 'THE COMPANY' vỡ vụn thành ngàn mảnh, sự thật được hé lộ làm tan biến bóng ma 7 năm, nước mắt òa khóc.",
        "prompt": "Powerful surreal visual of a cracked hand mirror shattering into pieces, revealing the phantom name 'THE COMPANY' dissolving into smoke, realization of the grand lie, tears breaking through a captive's trance, graphic novel noir."
    },
    {
        "name": "t10_red_bluff_bus_depot_departure",
        "act": 4,
        "sentences": "4.07#1–#3",
        "desc": "Bến xe buýt Red Bluff trong ánh nắng ban mai, cánh cửa xe buýt mở ra, Colleen bước lên chuyến xe đầu tiên không cùm xích sau 2.660 ngày tăm tối.",
        "prompt": "Atmospheric wide shot of the Red Bluff Greyhound bus depot, morning light breaking over the terminal roof, silhouetted young woman stepping up onto the bus stairs without chains or headbox, exhaust fumes catching the dawn rays, profound liberation."
    },
    {
        "name": "t10_tehama_county_sheriff_station",
        "act": 4,
        "sentences": "4.08#1",
        "desc": "Trụ sở Sở Cảnh sát Hạt Tehama tại Red Bluff vào đêm tháng 11 năm 1984, xe tuần tra cảnh sát đậu trước hàng cột đèn đường mờ sương.",
        "prompt": "Exterior nocturnal shot of the Tehama County Sheriff's Department building in Red Bluff, California, November 1984, patrol cruisers parked outside under yellow streetlamps, cold autumn rain slicking the pavement, turning point of justice."
    },
    {
        "name": "t10_immunity_agreement_document",
        "act": 4,
        "sentences": "4.08#2",
        "desc": "Văn bản thỏa thuận miễn trừ truy tố có con dấu đỏ của Công tố bang California trên bàn làm việc điều tra, chiếc bút máy đặt ngay ngắn bên lời khai.",
        "prompt": "Forensic close-up of legal documents on a dark oak desk: State of California Immunity Agreement with official embossed red seal and notarized witness statements, brass fountain pen resting on margins, solemn judicial procedure."
    },
    {
        "name": "t10_forensic_search_evidence_seizure",
        "act": 4,
        "sentences": "4.08#3–#4",
        "desc": "Các điều tra viên với đèn pin pháp y khám xét phòng ngủ căn nhà gỗ, lôi chiếc hộp gỗ và chiếc hộp đội đầu từ dưới gầm giường đệm nước ra ánh sáng.",
        "prompt": "Tense forensic investigation scene inside the dim bedroom, police detectives in trench coats shining circular flashlight beams beneath the dismantled waterbed frame, pulling the heavy plywood box and acoustic headbox into the light."
    },
    {
        "name": "t10_tehama_superior_court_columns",
        "act": 4,
        "sentences": "4.09#1–#2",
        "desc": "Phòng xử án Tòa án Thượng thẩm Hạt Tehama năm 1985, hàng cột gỗ sồi uy nghiêm, bàn bị cáo nơi kẻ thủ ác ngoan cố không nhận tội.",
        "prompt": "Classical American courtroom interior in 1985, heavy polished dark mahogany judge bench and jury box, silhouetted defendant sitting rigidly at defense table maintaining stubborn arrogance, high-contrast judicial chiaroscuro."
    },
    {
        "name": "t10_frank_ochberg_psychiatric_testimony",
        "act": 4,
        "sentences": "4.09#3",
        "desc": "Bục nhân chứng chuyên gia: Bác sĩ Frank Ochberg với tập tài liệu phân tích Hội chứng Stockholm và cơ chế tê liệt tâm lý trước bồi thẩm đoàn.",
        "prompt": "Forensic courtroom still life of an open psychiatric evaluation binder and microphone on the witness stand, clinical diagrams explaining Stockholm Syndrome and coercive control, raking spotlight on authoritative medical charts."
    },
    {
        "name": "t10_unmasking_predator_broken_facade",
        "act": 4,
        "sentences": "4.09#4",
        "desc": "Chiếc mặt nạ sứ trắng của kẻ săn mồi vỡ toang thành từng mảnh trên sàn đá hoa cương phòng xử án, bộc lộ bản chất méo mó bệnh hoạn trước công lý.",
        "prompt": "Metaphorical noir art of a smooth white porcelain smiling mask shattering into jagged shards on a cold courthouse floor, unmasking the narcissistic predator behind the respectable family facade, bold ink linework."
    },
    {
        "name": "t10_104_years_sentence_gavel",
        "act": 4,
        "sentences": "4.10#1–#3",
        "desc": "Chiếc búa gỗ thẩm phán gõ đanh thép xuống đế gỗ, bản án 104 năm tù giam đóng dấu đỏ khép lại chuỗi ngày tội ác thế kỷ.",
        "prompt": "Dramatic close-up of a dark oak judicial gavel striking down onto a polished sounding block, motion blur, official legal judgment document with red California State seal reading '104 Years Imprisonment', definitive justice rendered."
    },
    {
        "name": "t10_california_state_prison_bars_closing",
        "act": 4,
        "sentences": "4.10#4",
        "desc": "Hành lang nhà tù bang California thăm thẳm với hàng song sắt dày đặc đóng sầm vĩnh viễn, tước đoạt ánh sáng mặt trời của kẻ thủ ác suốt phần đời còn lại.",
        "prompt": "Stark penal noir shot looking down an endless concrete prison corridor in a California state penitentiary, heavy vertical steel cell bars casting stark parallel shadows across the floor, permanent exclusion from freedom."
    },

    # =========================================================================
    # HỒI 5: ÁNH SÁNG SAU BẢY NĂM ĐỊA NGỤC & SỰ HỒI SINH KỲ DIỆU (21:30 – 26:30)
    # =========================================================================
    {
        "name": "t10_healing_journey_morning_light",
        "act": 5,
        "sentences": "5.02#1–#3",
        "desc": "Bình minh trên bờ biển Thái Bình Dương, bóng người phụ nữ bước đi dọc bờ cát mịn, sóng biển xóa nhòa những dấu chân trong quá khứ đau thương.",
        "prompt": "Poetic dawn seascape along the northern California coastline, gentle rolling waves washing over wet sand, silhouetted woman walking toward the rising sun, soft warm golden and sea-mist palette, quiet spiritual healing."
    },
    {
        "name": "t10_accounting_degree_diploma",
        "act": 5,
        "sentences": "5.02#4–#6",
        "desc": "Bằng tốt nghiệp đại học ngành kế toán đóng khung trang trọng trên bàn làm việc gỗ sáng bên máy tính bàn cổ điển và những chồng sổ sách ngay ngắn.",
        "prompt": "Inspiring still life of a framed university bachelor's degree diploma in Accounting resting on an organized oak study desk next to accounting ledgers and a vintage calculator, warm sunlight streaming through sheer curtains."
    },
    {
        "name": "t10_simple_gifts_of_life_memoir",
        "act": 5,
        "sentences": "5.02#7",
        "desc": "Cuốn hồi ký Những món quà giản dị của cuộc sống đặt bên tách cà phê sáng bốc khói nghi ngút và làn gió mát thổi qua ô cửa sổ mở toang.",
        "prompt": "Warm domestic still life of an open published hardcover memoir book lying beside a steaming white ceramic coffee mug, morning breeze gently lifting the pages, golden sunlight illuminating the wood grain, celebrating simple daily freedom."
    },
    {
        "name": "t10_warm_family_breakfast_table",
        "act": 5,
        "sentences": "5.02#8–#9",
        "desc": "Bàn ăn sáng gia đình ngập tràn ánh nắng và tình yêu thương, hoa tươi trong bình gốm, điểm tựa tái sinh sau 7 năm tăm tối.",
        "prompt": "Sunny morning kitchen scene, wooden table laid with fresh bread, fruit bowl, and wild daisies in a clay vase, warm amber light filling every corner, visual celebration of family love and spiritual rebirth."
    },
    {
        "name": "t10_post_traumatic_growth_sprout_stone",
        "act": 5,
        "sentences": "5.03#1–#3",
        "desc": "Ẩn dụ tâm lý học Tăng trưởng sau sang chấn (Post-Traumatic Growth): một mầm cây xanh kiên cường vươn lên qua khe nứt của tảng đá hoa cương xám đen.",
        "prompt": "Inspiring metaphorical artwork representing Post-Traumatic Growth: a delicate yet resilient vibrant green sprout pushing through a deep crack in solid gray granite rock, bathed in radiant morning light, triumph of life over adversity."
    },
    {
        "name": "t10_fbi_academy_profiling_archive",
        "act": 5,
        "sentences": "5.04#1–#2",
        "desc": "Kệ lưu trữ tài liệu Học viện FBI Quantico, tập hồ sơ giảng dạy chuyên án Stan Dossier - Coercive Control & Trauma Bonding, bài học cảnh tỉnh xã hội.",
        "prompt": "Authoritative archive view of the FBI Academy Quantico behavioral science library, dark green file boxes on steel shelves, official study binder marked 'Stan Case Study: Psychological Coercion & Captivity Resilience', somber documentary noir."
    },
    {
        "name": "t10_redflag1_trojan_innocence_trap",
        "act": 5,
        "sentences": "5.05#1–#4",
        "desc": "Dấu hiệu cảnh báo 1: Chiếc xe gia đình và đồ chơi gấu bông vô hại đổ bóng thành hàm nanh sói trên nền đất, cạm bẫy niềm tin ngụy tạo.",
        "prompt": "Conceptual noir graphic of Red Flag 1: A harmless vintage family van and a child's teddy bear casting a long menacing shadow of a stalking predator onto cracked asphalt, warning against false innocent facades."
    },
    {
        "name": "t10_redflag2_spatial_isolation_grid",
        "act": 5,
        "sentences": "5.05#5–#7",
        "desc": "Dấu hiệu cảnh báo 2: Đường dây điện thoại bị cắt đứt và cây cầu gãy ngăn cách ngôi nhà đơn độc với đất liền, thủ thuật cô lập không gian.",
        "prompt": "Graphic noir allegory of Red Flag 2: A severed telephone line sparking faintly in darkness, a solitary cabin separated from the distant city lights by broken bridges, visual representation of psychological and informational isolation."
    },
    {
        "name": "t10_redflag3_phantom_enemy_mirror",
        "act": 5,
        "sentences": "5.05#8–#10",
        "desc": "Dấu hiệu cảnh báo 3: Tấm gương phóng đại chiếu ra bóng quái vật tưởng tượng ngoài cửa sổ, thủ thuật gieo rắc nỗi sợ hãi về kẻ thù không có thật.",
        "prompt": "Surreal conceptual noir art of Red Flag 3: A distorting curved lens projecting giant menacing phantom silhouettes against the wall, smoke and mirrors manufactured by a manipulator to enforce obedience through terror."
    },
    {
        "name": "t10_redflag4_breaking_helplessness_sparks",
        "act": 5,
        "sentences": "5.05#11–#13",
        "desc": "Dấu hiệu cảnh báo 4: Những mắt xích sắt gỉ bị bẻ gãy bởi ngọn lửa ý chí kiên định bên trong, phá vỡ sự bất lực tập nhiễm trong suy nghĩ.",
        "prompt": "Dramatic symbolic art of Red Flag 4: Heavy cast-iron shackle links fracturing and shattering under intense golden inner sparks, breaking the mental conditioning of learned helplessness, fiery determination."
    },
    {
        "name": "t10_breaking_invisible_chains_dawn",
        "act": 5,
        "sentences": "5.05#14",
        "desc": "Đôi bàn tay giải phóng những mảnh ván gỗ chiếc hộp vụn nát bay về phía chân trời bình minh rộng mở, tự do đích thực trong tâm trí con người.",
        "prompt": "Panoramic cinematic shot of silhouetted open hands releasing splintered wooden box planks into the wind, soaring across an immense golden sunrise sky, absolute spiritual freedom, high-contrast emotional climax."
    },
    {
        "name": "t10_amber_eyes_closing_dossier_colleen",
        "act": 5,
        "sentences": "5.05#15–#17",
        "desc": "Tập hồ sơ da Amber Eyes khép lại trang nghiêm trên bàn gỗ sồi, biểu tượng mắt cú hổ phách mạ vàng bừng sáng, lời chào tạm biệt tập 10.",
        "prompt": "Close-up still life of the dark leather Amber Eyes investigative dossier closing solemnly on an antique oak desk, embossed golden owl eye logo gleaming in warm amber lamplight, dignified closing frame, graphic novel noir perfection."
    }
]

def main():
    print(f"Tổng số ảnh nền thiết kế cho Tập 10: {len(jobs)} ảnh.")
    
    # Ghi file bg_jobs_tap10.json
    bg_jobs_path = WORK / "bg_jobs_tap10.json"
    bg_jobs_path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo: {bg_jobs_path}")

    # Ghi file gemini_image_prompts_tap10.json
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
    gemini_path = WORK / "gemini_image_prompts_tap10.json"
    gemini_path.write_text(json.dumps(gemini_prompts, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo: {gemini_path}")

if __name__ == "__main__":
    main()
