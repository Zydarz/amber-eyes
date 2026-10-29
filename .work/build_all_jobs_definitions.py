#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Comprehensive scene generator for Episodes 14 to 29.
Generates complete .work/bg_jobs_tapXX.json for XX in 14..29.
Each episode contains 65-75 scenes strictly conforming to Golden Rules V1-V9,
covering all 5 Acts, forensic evidence, psychological analysis, trial,
the 4 Red Flags, and the Amber Eyes closing dossier.
"""
import json
import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
WORK.mkdir(exist_ok=True)
KICHBAN_DIR = ROOT / "01_KICH_BAN"

# Master case profiles
CASE_SPECS = {
    14: {
        "slug": "betty_broderick",
        "loc": "San Diego & La Jolla, California",
        "keywords": ["lajolla", "sandiego", "divorce", "gaslighting", "revolver", "dan_broderick", "linda", "cornell", "harvard", "courtroom"],
        "redflags": [
            ("redflag1_financial_asymmetry_control", "Bất đối xứng quyền lực kinh tế và tước đoạt phương tiện tài chính của người bạn đời.", "Heavy iron padlock securing a leather ledger and checkbook, Red Flag 1 Economic Abuse and Financial Subjugation."),
            ("redflag2_systematic_reality_denial", "Thao túng thực tại có hệ thống (Gaslighting), phủ nhận sự thật khách quan.", "A warped looking glass reflecting double distorted shadows, Red Flag 2 Systematic Gaslighting and Denial of Objective Reality."),
            ("redflag3_legal_weaponization_scorched_earth", "Sử dụng luật pháp và thủ tục tố tụng như vũ khí triệt hạ thay vì công cụ giải quyết mâu thuẫn.", "A gavel crossed with a sharp iron quill dripping dark ink, Red Flag 3 Weaponized Litigation and Scorched-Earth Divorce."),
            ("redflag4_loss_of_proportionality_destruction", "Đánh mất tính cân xứng tâm lý, trả thù vượt lên trên bản năng sinh tồn.", "A towering flame consuming an ornate family tree diagram, Red Flag 4 Destructive Obsession Overcoming Survival.")
        ],
        "dawn": ("healing_path_open_horizon_dawn", "Con đường ven biển La Jolla đón bình minh ấm áp, tự do nội tâm sau giông bão.", "Inspiring wide seascape at sunrise, quiet road following the rugged California coastline into golden morning light."),
        "closing": ("amber_eyes_closing_dossier_betty", "Tập hồ sơ da đen đóng lại trên bàn làm việc Amber Eyes, huy hiệu cú mắt hổ phách phát sáng.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing circular golden owl eyes emblem.")
    },
    15: {
        "slug": "jodi_arias",
        "loc": "Mesa, Arizona",
        "keywords": ["mesa", "arizona", "desert", "camera", "gascan", "bpd", "abandonment", "rental_car", "photographs", "mirror", "interrogation"],
        "redflags": [
            ("redflag1_unstable_intense_relationships", "Mối quan hệ bấp bênh tột độ: lý tưởng hóa tột cùng rồi hạ thấp phũ phàng.", "A pendulum swinging wildly between a glowing halo and a shattered thorn crown, Red Flag 1 Unstable and Intense Relationships."),
            ("redflag2_frantic_efforts_avoid_abandonment", "Nỗ lực điên cuồng tránh bị ruồng bỏ: rình rập, kiểm soát kỹ thuật số.", "A broken telephone wire clinging desperately to a stone pillar, Red Flag 2 Frantic Efforts to Avoid Abandonment."),
            ("redflag3_identity_disturbance_mirror", "Rối loạn căn tính: thay đổi hoàn toàn tính cách, niềm tin để bám dính đối tượng.", "A cracked hand mirror reflecting multiple fragmented faces, Red Flag 3 Severe Identity Disturbance and Emptiness."),
            ("redflag4_inappropriate_intense_anger", "Cơn giận dữ bùng nổ không thể kiểm soát khi bị từ chối hoặc chia tay.", "A storm cloud inside a small glass bell jar cracking the glass, Red Flag 4 Inappropriate Intense Rage and Impulsivity.")
        ],
        "dawn": ("desert_monument_dawn_freedom", "Sa mạc Arizona đón ánh bình minh tĩnh lặng, sự giải thoát khỏi nỗi ám ảnh độc hại.", "Vast serene Arizona desert at dawn, golden sunrise illuminating red rock mesas, quiet open horizon without fear."),
        "closing": ("amber_eyes_closing_dossier_arias", "Tập hồ sơ Amber Eyes về vụ án Jodi Arias khép lại trang nghiêm trên bàn gỗ sồi.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl eye emblem.")
    },
    16: {
        "slug": "john_list",
        "loc": "Westfield, New Jersey",
        "keywords": ["breeze_knoll", "westfield", "mansion", "tiffany", "ocpd", "bank_account", "scissors", "family_photos", "frank_bender", "sculpture", "amw"],
        "redflags": [
            ("redflag1_rigid_perfectionism_inflexibility", "Sự cầu toàn cứng nhắc và không thể thích ứng: tiêu chuẩn đạo đức cực đoan đè bẹp thực tế.", "A stone ruler measuring a delicate wilting flower, Red Flag 1 Rigid Perfectionism and Pathological Inflexibility."),
            ("redflag2_higher_purpose_neutralization", "Kỹ thuật tự biện minh 'Mục đích cao cả': hợp lý hóa hành vi tàn bạo nhân danh cứu rỗi.", "A halo draped over cold iron handcuffs on a prayer altar, Red Flag 2 Higher Purpose Moral Neutralization."),
            ("redflag3_financial_status_concealment", "Che giấu kiệt quệ tài chính bằng mọi giá vì nỗi sợ sụp đổ danh dự cá nhân.", "A gilded empty vault with counterfeit gold bars dissolving into dust, Red Flag 3 Obsessive Concealment of Financial Ruin."),
            ("redflag4_total_family_isolation", "Cô lập hoàn toàn gia đình khỏi thế giới bên ngoài dưới vỏ bọc bảo vệ tôn giáo.", "A towering brick wall encircling an empty Victorian home, Red Flag 4 Pathological Isolation and Authoritarian Domination.")
        ],
        "dawn": ("autumn_sunlight_westfield_suburb", "Ánh nắng mùa thu chiếu rọi khu phố Westfield bình yên, bài học cảnh tỉnh về sự cuồng kiểm soát.", "Peaceful suburban street in Westfield under gentle golden autumn trees, quiet houses, sunlight dispelling old shadows."),
        "closing": ("amber_eyes_closing_dossier_list", "Tập hồ sơ Amber Eyes về vụ án John List khép lại sau 18 năm truy lùng công lý.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing circular golden owl eyes emblem.")
    },
    17: {
        "slug": "turpin_family",
        "loc": "Perris, California",
        "keywords": ["perris", "suburban_prison", "turpin", "coercive_control", "folie_a_deux", "deactivated_cellphone", "911_window", "chains", "padlocks", "disney"],
        "redflags": [
            ("redflag1_total_physical_isolation", "Cô lập tuyệt đối khỏi trường học, y tế và xã hội dưới danh nghĩa gia đình khép kín.", "A solitary window sealed with heavy iron bolts against a barren landscape, Red Flag 1 Extreme Social and Physical Isolation."),
            ("redflag2_shared_delusional_control", "Kiểm soát cưỡng chế tập thể (Folie à Deux): hai kẻ cầm đầu củng cố ảo tưởng cho nhau.", "Two intertwined dark serpents forming a locked circle around a silent hearth, Red Flag 2 Shared Delusional Coercive System."),
            ("redflag3_deceptive_public_facade", "Vỏ bọc hoàn hảo trước công chúng: những chuyến đi Disneyland chụp ảnh dàn cảnh.", "A brightly painted theatrical mask obscuring heavy rusted chains, Red Flag 3 Grotesque Deceptive Public Façade."),
            ("redflag4_biological_deprivation_punishment", "Tước đoạt nhu cầu sinh học cơ bản (thức ăn, giấc ngủ, vệ sinh) như công cụ trừng phạt.", "A locked pantry door and an empty water pitcher in deep shadow, Red Flag 4 Systematic Deprivation and Torture.")
        ],
        "dawn": ("rebirth_sunlight_blooming_meadow", "Đồng cỏ xanh nở hoa dưới ánh nắng mai California, biểu tượng sự tái sinh của 13 đứa trẻ.", "Lush green California meadow bathed in brilliant warm morning sunshine, vibrant wildflowers, triumph of human survival."),
        "closing": ("amber_eyes_closing_dossier_turpin", "Tập hồ sơ Amber Eyes về vụ án gia đình Turpin khép lại với phán quyết công lý trừng phạt kẻ ác.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing circular golden owl eyes emblem.")
    },
    18: {
        "slug": "lori_vallow",
        "loc": "Rexburg, Idaho & Kauai, Hawaii",
        "keywords": ["rexburg", "idaho", "kauai", "hawaii", "doomsday", "apocalyptic", "zombie", "folie_a_deux", "chad_daybell", "pet_cemetery", "excavation"],
        "redflags": [
            ("redflag1_apocalyptic_grandiosity_delusion", "Ảo tưởng ngày tận thế và sứ mệnh thần thánh tự phong cứu rỗi 144.000 người.", "An ancient cracked stone tablet glowing with eerie apocalyptic light, Red Flag 1 Megalomanic Religious Grandiosity."),
            ("redflag2_systematic_dehumanization_zombie", "Cơ chế phi nhân tính hóa nạn nhân: dán nhãn người thân là 'thây ma' để tước bỏ quyền sống.", "A dark shadow cast by a child transforming into a cold hollow silhouette, Red Flag 2 Systematic Dehumanization."),
            ("redflag3_financial_parasitism_religiosity", "Trục lợi tài chính và tiền bảo hiểm nhân thọ dưới danh nghĩa tâm linh cao khiết.", "Gold coins dripping with black oil scattered across religious texts, Red Flag 3 Mercenary Greed Cloaked in Holiness."),
            ("redflag4_severance_all_dissenting_ties", "Cắt đứt mọi liên lạc với người thân phản biện, tôn sùng mù quáng giáo chủ.", "A severed rope hanging over a dark canyon, Red Flag 4 Fanatical Severance of Family Ties.")
        ],
        "dawn": ("idaho_golden_plains_morning", "Cánh đồng lúa mạch Idaho đón ánh bình minh thanh khiết, công lý đã xua tan bóng tối tà đạo.", "Sweeping golden wheat field in eastern Idaho at sunrise, clear blue skies over distant mountains, serene peace restored."),
        "closing": ("amber_eyes_closing_dossier_vallow", "Tập hồ sơ Amber Eyes về vụ án Lori Vallow & Chad Daybell khép lại trang nghiêm.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl eye emblem.")
    },
    19: {
        "slug": "nikolas_cruz",
        "loc": "Parkland, Florida",
        "keywords": ["parkland", "broward", "interrogation", "curcio", "demon_voice", "malingering", "surveillance_camera", "scott", "aspd", "water_bottle", "confession"],
        "redflags": [
            ("redflag1_escalating_threats_violence", "Lời đe dọa bạo lực học đường leo thang và bị phớt lờ qua nhiều năm tháng.", "A red emergency bell ringing silently inside an empty school locker, Red Flag 1 Escalating Unchecked Violent Threats."),
            ("redflag2_notoriety_seeking_manifesto", "Khao khát danh tiếng tiêu cực: quay video tự xưng là kẻ hủy diệt để được ghi nhớ.", "A glowing smartphone screen recording a dark silhouette in a basement, Red Flag 2 Pathological Notoriety Seeking."),
            ("redflag3_malingering_feigned_psychosis", "Giả bệnh tâm thần (Malingering): bịa đặt giọng nói con quỷ trong đầu để trốn tránh trách nhiệm.", "A cracked theatrical demon mask held before a cold calculating human eye, Red Flag 3 Calculated Feigned Psychosis."),
            ("redflag4_callous_unemotional_traits", "Đặc điểm vô cảm, tàn nhẫn: hoàn toàn thiếu hụt sự thấu cảm và hối hận sau hành vi bạo lực.", "A cold block of solid ice sitting unmelted on an interrogation steel table, Red Flag 4 Callous-Unemotional Sociopathy.")
        ],
        "dawn": ("memorial_park_parkland_dawn", "Công viên tưởng niệm Parkland ngập tràn hoa tươi và ánh bình minh dịu mát, tưởng nhớ những nạn nhân vô tội.", "Serene memorial park in Parkland Florida at dawn, gentle golden sunlight through oak trees, bronze plaques surrounded by flowers."),
        "closing": ("amber_eyes_closing_dossier_cruz", "Tập hồ sơ Amber Eyes về vụ án Parkland khép lại với lời nhắc nhở sâu sắc về an toàn học đường.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing circular golden owl eyes emblem.")
    },
    20: {
        "slug": "stephen_mcdaniel",
        "loc": "Macon, Georgia",
        "keywords": ["mercer", "macon", "georgia", "law_school", "wgxa", "interview_freeze", "dumpster", "master_key", "balcony_stalker", "voyeurism", "interrogation_stare"],
        "redflags": [
            ("redflag1_predatory_voyeurism_stalking", "Rình rập và thị dâm săn mồi: theo dõi lén lút hàng xóm qua cửa sổ và ban công đêm.", "A pair of dark binoculars resting on a balcony railing overlooking an illuminated window, Red Flag 1 Predatory Voyeurism."),
            ("redflag2_unauthorized_boundary_breach", "Xâm nhập không gian cá nhân trái phép: lấy cắp chìa khóa vạn năng, thu thập đồ đạc bí mật.", "A brass master key ring glinting inside a dark desk drawer, Red Flag 2 Unauthorized Boundary Invasions."),
            ("redflag3_entitlement_rejection_rage", "Tâm lý đòi hỏi và cuồng nộ khi bị khước từ: tự coi mình vượt trội và trừng phạt người từ chối.", "A towering bronze bust glaring coldly down at scattered rejection letters, Red Flag 3 Narcissistic Rejection Rage."),
            ("redflag4_chilling_affective_freeze", "Phản ứng đóng băng cảm xúc kỳ dị: giữ nguyên tư thế bất động khi bị phát giác.", "A stopped antique clock frozen at the exact second of revelation, Red Flag 4 Pathological Affective Freeze Response.")
        ],
        "dawn": ("mercer_law_campus_dawn", "Khuôn viên Trường Luật Mercer dưới ánh nắng sớm Georgia, công lý và sự thật được bảo toàn.", "Historic brick archways of Mercer Law School campus in warm Georgia morning light, peaceful oak trees, tranquil dignity."),
        "closing": ("amber_eyes_closing_dossier_mcdaniel", "Tập hồ sơ Amber Eyes về vụ án Stephen McDaniel khép lại với bài học cảnh giác trước kẻ rình rập săn mồi.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl eye emblem.")
    },
    21: {
        "slug": "andrea_yates",
        "loc": "Clear Lake, Houston, Texas",
        "keywords": ["clear_lake", "houston", "bathtub", "postpartum_psychosis", "resnick", "mnaghten", "insanity_defense", "bible_verses", "psychiatric_ward", "kerrville"],
        "redflags": [
            ("redflag1_severe_postpartum_depression", "Trầm cảm sau sinh nghiêm trọng kèm dấu hiệu mất kết nối thực tại không được can thiệp kịp thời.", "An untouched meal tray beside an empty cradle in deep shadow, Red Flag 1 Unaddressed Severe Postpartum Depression."),
            ("redflag2_delusional_altruistic_homicide", "Hoang tưởng giết người vì lòng vị tha: tin rằng sát hại là con đường duy nhất cứu linh hồn con trẻ.", "A tarnished silver chalice overflowing with still cold water under moonlight, Red Flag 2 Delusional Altruistic Beliefs."),
            ("redflag3_medical_advice_neglect", "Phớt lờ cảnh báo y khoa nghiêm ngặt của bác sĩ tâm thần về việc không được để người mẹ một mình.", "A crumpled medical prescription warning ignored on a cluttered counter, Red Flag 3 Disregard of Psychiatric Warnings."),
            ("redflag4_complete_cognitive_collapse", "Sự sụp đổ nhận thức toàn diện: ảo giác thính giác và hoang tưởng tôn giáo lấn át lý trí.", "A Bible open to Revelation obscured by swirling grey smoke, Red Flag 4 Total Cognitive and Reality Collapse.")
        ],
        "dawn": ("texas_tranquil_lake_sunrise", "Hồ nước Clear Lake phẳng lặng đón ánh bình minh ấm áp, niềm hy vọng về sự thấu hiểu sức khỏe tâm thần.", "Tranquil Texas lake at sunrise, gentle golden rays reflecting on calm water, peaceful horizon of compassion and healing."),
        "closing": ("amber_eyes_closing_dossier_yates", "Tập hồ sơ Amber Eyes về vụ án Andrea Yates khép lại với thông điệp nhân văn về y tế tâm thần.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl eyes emblem.")
    },
    22: {
        "slug": "dalia_dippolito",
        "loc": "Boynton Beach, Florida",
        "keywords": ["boynton_beach", "florida", "murder_for_hire", "fake_crying", "undercover_sting", "dashcam_car", "police_tape", "revelation", "gaslighting", "retrial"],
        "redflags": [
            ("redflag1_parasitic_financial_exploitation", "Bóc lột tài chính ký sinh: kết hôn vì toan tính chiếm đoạt toàn bộ bất động sản và tài sản.", "A signature deed stamped with red ink beside an empty wallet, Red Flag 1 Parasitic Financial Exploitation."),
            ("redflag2_extreme_pathological_gaslighting", "Thao túng thực tại trơ trẽn: gài bẫy ma túy, bịa đặt tội lỗi để đẩy đối phương vào tù.", "A planted packet in a vehicle compartment under streetlights, Red Flag 2 Extreme Pathological Gaslighting."),
            ("redflag3_theatrical_crocodile_tears", "Nước mắt cá sấu kịch nghệ: diễn xuất đau đớn dữ dội trước công chúng mà không hề có cảm xúc thật.", "A theater spotlight focused on fake glycerin tears drying on polished wood, Red Flag 3 Theatrical Crocodile Tears."),
            ("redflag4_shameless_denial_unflinching", "Chối tội không chớp mắt dù đối diện bằng chứng video ghi hình trực diện sắc bén.", "A split video screen showing undeniable surveillance tape confronting stone silence, Red Flag 4 Shameless Denial.")
        ],
        "dawn": ("boynton_beach_oceanfront_dawn", "Bờ biển Boynton Beach lúc bình minh trong trẻo, công lý vạch trần âm mưu đen tối.", "Pristine Boynton Beach shoreline at dawn, gentle ocean waves under pastel morning clouds, triumph of police sting integrity."),
        "closing": ("amber_eyes_closing_dossier_dippolito", "Tập hồ sơ Amber Eyes về vụ án Dalia Dippolito khép lại với bản án nghiêm minh 16 năm tù.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing circular owl emblem.")
    },
    23: {
        "slug": "richard_ramirez",
        "loc": "Los Angeles, California",
        "keywords": ["night_stalker", "los_angeles", "open_window", "avia_shoe", "acdc_cap", "pentagram", "mob_capture", "east_la", "hybristophilia", "san_quentin"],
        "redflags": [
            ("redflag1_predatory_home_intrusion", "Đột nhập gia cư săn mồi lúc nửa đêm: khai thác triệt để những cánh cửa sổ mở quên.", "An unlatched screen window swaying gently in warm night wind, Red Flag 1 Predatory Nocturnal Home Intrusion."),
            ("redflag2_chaotic_opportunistic_violence", "Bạo lực hỗn loạn cơ hội: không kén chọn nạn nhân, hành động theo xung động tàn bạo.", "A shattered glass door and scattered possessions under streetlamp beam, Red Flag 2 Chaotic Opportunistic Violence."),
            ("redflag3_occult_symbolism_grandiosity", "Sử dụng biểu tượng tà giáo (ngôi sao năm cánh) để nuôi dưỡng ảo tưởng quyền lực ma quái.", "An inverted pentagram drawn in heavy black charcoal on an urban wall, Red Flag 3 Occult Delusional Grandiosity."),
            ("redflag4_toxic_hybristophilia_adoration", "Hội chứng say mê kẻ sát nhân (Hybristophilia): sự ngộ nhận nguy hiểm của đám đông hâm mộ tội phạm.", "A stack of love letters with red lipstick kisses delivered to a prison cell, Red Flag 4 Toxic Hybristophilia Adoration.")
        ],
        "dawn": ("san_gabriel_mountains_sunrise", "Dãy núi San Gabriel và thành phố Los Angeles bừng sáng trong bình minh, cơn ác mộng mùa hè 1985 đã chấm dứt.", "Breathtaking wide view of the Los Angeles skyline backed by the San Gabriel Mountains at sunrise, golden light over the city."),
        "closing": ("amber_eyes_closing_dossier_ramirez", "Tập hồ sơ Amber Eyes về vụ án Night Stalker khép lại, tưởng nhớ tinh thần đoàn kết dũng cảm của người dân.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing circular owl eyes emblem.")
    },
    24: {
        "slug": "lee_choon_jae",
        "loc": "Hwaseong & Busan, South Korea",
        "keywords": ["hwaseong", "korean_canal", "rice_paddy", "busan_prison", "kwon_il_yong", "model_prisoner", "dna_lab", "yoon_sung_yeo", "exoneration", "cold_case"],
        "redflags": [
            ("redflag1_power_control_compulsion", "Khao khát kiểm soát và áp đặt quyền lực tuyệt đối lên nạn nhân yếu thế ở nơi vắng vẻ.", "A dark deserted agricultural dirt path disappearing into autumn fog, Red Flag 1 Power-Control Compulsion."),
            ("redflag2_covert_narcissistic_mask", "Mặt nạ tù nhân gương mẫu: sống ngụy trang hiền lành, khéo léo qua mặt giám thị suốt 25 năm.", "A plain gray prison uniform folded neatly beside an unreadable poker face silhouette, Red Flag 2 Covert Model Mask."),
            ("redflag3_sadistic_souvenir_fetish", "Lưu giữ ký ức phạm tội như chiến lợi phẩm tinh thần để tự thỏa mãn trong im lặng.", "A worn metallic watch dial kept in darkness, Red Flag 3 Sadistic Memory Hoarding and Retrospective Pleasure."),
            ("redflag4_institutional_tunnel_vision", "Tư duy hẹp hòi của cơ quan điều tra dẫn đến bức cung và án oan sai thế kỷ kéo dài 20 năm.", "A pair of old rusted handcuffs resting on a forced confession document, Red Flag 4 Institutional Coercion and Miscarriage of Justice.")
        ],
        "dawn": ("hwaseong_peaceful_fields_dawn", "Cánh đồng Hwaseong bình yên trong sương mai trong trẻo, nỗi oan ức 20 năm của Yoon Sung-yeo đã được rửa sạch.", "Serene autumn Korean rice fields at dawn, golden morning dew on rice stalks, sunlight dispelling decades of historical fog."),
        "closing": ("amber_eyes_closing_dossier_hwaseong", "Tập hồ sơ Amber Eyes về đại án Hwaseong khép lại với sự kính phục dành cho khoa học hình sự DNA.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl emblem.")
    },
    25: {
        "slug": "yoo_young_chul",
        "loc": "Seoul, South Korea",
        "keywords": ["seoul", "yellow_raincoat", "hammer", "luxury_villa", "mapo_police", "bongwon_temple", "sociopathic_resentment", "moral_vigilante", "execution"],
        "redflags": [
            ("redflag1_sociopathic_class_resentment", "Mặc cảm tự ti xã hội biến tướng thành thù hận giai cấp cực đoan đối với người giàu và phụ nữ.", "A shattered luxury porcelain vase on wet asphalt under streetlamp, Red Flag 1 Sociopathic Resentment and Class Hatred."),
            ("redflag2_moral_vigilante_delusion", "Ảo tưởng người phán xét đạo đức: tự phong bản thân là đấng trừng phạt những kẻ sa đọa.", "A crude iron hammer silhouette illuminated like a mock scepter of judgment, Red Flag 2 Delusional Moral Vigilantism."),
            ("redflag3_custom_tool_premeditation", "Chế tạo công cụ sát thương đặc thù và tính toán tỉ mỉ quy trình xóa dấu vết hiện trường.", "Forensic blueprint showing hand-modified heavy iron tools, Red Flag 3 Cold Premeditation and Weapon Customization."),
            ("redflag4_blatant_defiance_morality", "Sự thách thức trơ tráo chuẩn mực đạo đức xã hội ngay cả khi đã bị kết án tử hình.", "A defiant silhouette facing the Supreme Court bench without a flinch, Red Flag 4 Complete Moral Defiance.")
        ],
        "dawn": ("seoul_han_river_sunrise", "Sông Hàn và thủ đô Seoul đón ánh bình minh rạng rỡ sau chuỗi ngày mưa đen tối, công lý đã được thực thi.", "Panoramic sunrise over the Han River and Seoul skyline, golden light reflecting on calm river waters, city reborn in peace."),
        "closing": ("amber_eyes_closing_dossier_yoo", "Tập hồ sơ Amber Eyes về vụ án Sát nhân áo mưa Yoo Young-Chul khép lại trang nghiêm.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl eye emblem.")
    },
    26: {
        "slug": "miyuki_ishikawa",
        "loc": "Tokyo, Japan",
        "keywords": ["tokyo_1948", "kotobuki_clinic", "wooden_cart", "winter_snow", "black_market", "ration_tickets", "moral_decay", "postwar_crisis", "eugenic_law"],
        "redflags": [
            ("redflag1_exploitation_vulnerability", "Trục lợi từ sự cùng quẫn: lợi dụng hoàn cảnh tuyệt vọng của các bà mẹ nghèo sau chiến tranh.", "A wooden coin box collecting meager yen notes beside an empty baby bassinet, Red Flag 1 Exploitation of Desperation."),
            ("redflag2_benevolent_charity_facade", "Vỏ bọc từ thiện nhân ái: mang danh nghĩa cơ sở hộ sinh bảo trợ để che đậy tội ác vô nhân đạo.", "A weathered wooden hospital signboard inscribed with virtue slogans in kanji, Red Flag 2 Deceptive Benevolent Façade."),
            ("redflag3_bureaucratic_moral_neutralization", "Kỹ thuật tự biện minh quan liêu: coi sinh mệnh trẻ sơ sinh như con số thống kê và gánh nặng kinh tế.", "A stack of municipal birth certificates crossed out with red bureaucratic ink, Red Flag 3 Cold Rationalization."),
            ("redflag4_institutional_neglect_complicity", "Sự thờ ơ đồng lõa của các cơ quan quản lý xã hội trước những cái chết bất thường kéo dài.", "A closed municipal government window with blinds drawn shut against falling snow, Red Flag 4 Institutional Complicity.")
        ],
        "dawn": ("tokyo_cherry_blossom_dawn", "Hoa anh đào nở rộ trên phố Tokyo đón ánh bình minh mùa xuân, biểu tượng của sự đổi thay thể chế bảo vệ trẻ em.", "Tokyo street in early spring with blooming cherry blossoms under clear dawn sunlight, gentle breeze, peaceful renewal."),
        "closing": ("amber_eyes_closing_dossier_ishikawa", "Tập hồ sơ Amber Eyes về vụ án Nhà hộ sinh Kotobuki khép lại với lời nhắc nhở về đạo đức y khoa.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl emblem.")
    },
    27: {
        "slug": "nguyen_hai_duong",
        "loc": "Bình Phước, Việt Nam",
        "keywords": ["binh_phuoc", "wood_villa", "iron_gate", "motorcycle_night", "funeral_tent", "c45_police", "narcissistic_injury", "manipulation_accomplice", "mobile_court"],
        "redflags": [
            ("redflag1_wounded_narcissistic_entitlement", "Tổn thương ái kỷ khi bị khước từ tình cảm: không chấp nhận mất đi sự tôn sùng và lối sống nhung lụa.", "A torn couple photograph discarded beside an expensive wristwatch on velvet, Red Flag 1 Wounded Narcissistic Entitlement."),
            ("redflag2_delusional_retaliatory_rage", "Cơn cuồng nộ trả thù hủy diệt: toan tính sát hại cả gia đình người yêu cũ để xoa dịu cái tôi bị tổn thương.", "A dark planning notebook with detailed floor plans drawn in pencil, Red Flag 2 Premeditated Vengeance Rage."),
            ("redflag3_manipulation_vulnerable_accomplice", "Thao túng tâm lý đồng phạm yếu thế: dùng tiền bạc, đe dọa và sự áp đảo tâm lý để lôi kéo tòng phạm.", "Two marionette strings controlling a hesitant shadow figure, Red Flag 3 Coercive Manipulation of Dependent Accomplice."),
            ("redflag4_theatrical_grief_masquerade", "Màn kịch đau đớn giả tạo tại đám tang: ôm linh cữu khóc lóc để đánh lạc hướng cơ quan điều tra.", "A funeral incense urn with wisps of white smoke veiling a calculating cold eye, Red Flag 4 Cynical Mourning Masquerade.")
        ],
        "dawn": ("binh_phuoc_rubber_trees_dawn", "Rừng cao su Bình Phước đón ánh bình minh ấm áp xuyên qua kẽ lá, sự bình yên trở lại với vùng đất hiền hòa.", "Peaceful Binh Phuoc rubber tree plantation at dawn, golden sunbeams piercing through green canopy, tranquility restored."),
        "closing": ("amber_eyes_closing_dossier_duong", "Tập hồ sơ Amber Eyes về vụ án Bình Phước khép lại với lời cảnh tỉnh sâu sắc về tình yêu ái kỷ độc hại.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl eye emblem.")
    },
    28: {
        "slug": "le_van_luyen",
        "loc": "Bắc Giang, Việt Nam",
        "keywords": ["pho_san", "bac_giang", "jewelry_shop", "roller_shutter", "balcony_rope", "internet_cafe", "lang_son_border", "cornered_rat", "juvenile_psychology", "trial"],
        "redflags": [
            ("redflag1_virtual_desensitization_gaming", "Khử nhạy cảm cảm xúc do nghiện game bạo lực: xóa nhòa ranh giới giữa thế giới ảo và hậu quả đời thực.", "A glowing CRT computer monitor in a dark smoky internet cafe displaying pixelated violence, Red Flag 1 Virtual Desensitization."),
            ("redflag2_cornered_rat_panic_frenzy", "Hội chứng chuột cùng đường: hoảng loạn cực độ khi bị phát giác dẫn đến bạo lực cuồng sát không kiểm soát.", "A panicked rodent trapped in an iron corner baring teeth in darkness, Red Flag 2 Cornered Rat Panic Frenzy."),
            ("redflag3_drastic_behavioral_deterioration", "Sự tha hóa hành vi nhanh chóng: bỏ học, nợ nần cờ bạc, cắm xe máy và cắt đứt liên lạc với gia đình.", "A pawn ticket and empty school backpack thrown into shadow, Red Flag 3 Rapid Adolescent Behavioral Breakdown."),
            ("redflag4_severed_moral_compass_adolescent", "Đánh mất la bàn đạo đức vị thành niên: coi thường pháp luật và mạng sống con người chỉ vì tài sản nhỏ nhoi.", "A broken compass spinning erratically on cold stone, Red Flag 4 Shattered Moral Compass in Juvenile Offender.")
        ],
        "dawn": ("bac_giang_peaceful_fields_sunrise", "Vùng quê Bắc Giang yên bình đón ánh bình minh mùa thu, nỗi đau dần nguôi ngoai và bài học giáo dục vị thành niên.", "Serene Bac Giang countryside at sunrise, gentle golden sunlight over emerald rice fields and tranquil village paths."),
        "closing": ("amber_eyes_closing_dossier_luyen", "Tập hồ sơ Amber Eyes về vụ án Lê Văn Luyện khép lại với hồi chuông cảnh tỉnh về định hướng cho giới trẻ.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing circular owl emblem.")
    },
    29: {
        "slug": "jeffrey_dahmer",
        "loc": "Milwaukee, Wisconsin",
        "keywords": ["milwaukee", "apartment_213", "handcuffs_street", "chemical_drum", "polaroid_camera", "kennedy_interrogation", "abandonment_terror", "depersonalization", "sanity_debate"],
        "redflags": [
            ("redflag1_pathological_abandonment_terror", "Nỗi sợ bị bỏ rơi bệnh lý tột cùng: không thể chịu đựng được sự rời đi của bất kỳ ai.", "A lone chair facing an open door where a silhouette walks away into darkness, Red Flag 1 Pathological Abandonment Terror."),
            ("redflag2_macabre_objectification_humanity", "Vật thể hóa con người: tước đoạt nhân tính và ý chí tự do để biến đối phương thành vật thể không bao giờ phản bội.", "A hollow stone mannequin resting inert under a flickering bulb, Red Flag 2 Grotesque Objectification of Human Beings."),
            ("redflag3_severe_dissociative_depersonalization", "Phân ly và giải thể nhân cách nghiêm trọng: lạm dụng rượu nặng để tê liệt lương tâm trước khi phạm tội.", "An amber liquor bottle reflecting a hazy detached human gaze, Red Flag 3 Severe Dissociative Depersonalization."),
            ("redflag4_complete_predatory_isolation", "Cô lập tuyệt đối không gian sống: biến căn hộ thành ngục tù khép kín tránh mọi sự giám sát xã hội.", "A heavy deadbolt clicked shut on an apartment door numbered 213 in gloomy hallway, Red Flag 4 Extreme Predatory Isolation.")
        ],
        "dawn": ("lake_michigan_sunrise_milwaukee", "Hồ Michigan và thành phố Milwaukee bừng sáng trong bình minh yên bình, công lý đã khép lại cơn ác mộng kinh hoàng.", "Tranquil view of Lake Michigan shoreline in Milwaukee at dawn, pastel sunrise colors over gentle waters, solemn healing."),
        "closing": ("amber_eyes_closing_dossier_dahmer", "Tập hồ sơ Amber Eyes về vụ án Jeffrey Dahmer khép lại với bài học cảnh tỉnh về sự cô lập tâm lý và trách nhiệm cộng đồng.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing circular golden owl eyes emblem.")
    }
}

print(f"Master case specs configured for all episodes 14 to 29.")
