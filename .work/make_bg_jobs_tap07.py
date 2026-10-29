import json
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"

jobs = [
    # HỒI 1: BUỔI SÁNG ĐỊNH MỆNH TẠI BÃI ĐỖ XE KMART (00:00 – 05:00)
    {
        "name": "t7_digital_coercion_screen",
        "act": 1,
        "sentences": "1.02#1–#3",
        "desc": "Cận cảnh màn hình điện thoại trong bóng tối, ánh sáng xanh lạnh buốt hắt lên mặt bàn gỗ tối tăm, các dòng tin nhắn nhấp nháy, không khí căng thẳng lạnh gáy.",
        "prompt": "Extreme close-up of a vintage smartphone resting on a dark rustic wooden table in a pitch-black room, cold blue electronic screen glow casting sharp directional shadows, subtle atmospheric dust particles floating in the light cone, dark graphic novel noir aesthetic, high contrast chiaroscuro, desaturated cold tones, film grain."
    },
    {
        "name": "t7_highway_50km_isolation",
        "act": 1,
        "sentences": "1.02#4–#6",
        "desc": "Tuyến đường cao tốc ban đêm vắng lặng nối hai thị trấn ven biển Massachusetts mờ ảo dưới mưa đêm, đèn pha xe hơi xa xa, cảm giác cô lập và khoảng cách.",
        "prompt": "An empty, desolate coastal Massachusetts highway cutting through dark pine forests at midnight under a driving cold rain, asphalt reflecting distant sodium streetlights and red taillight streaks in the far distance, moody atmospheric fog, dark graphic novel noir art style, heavy ink shadows, solitude."
    },
    {
        "name": "t7_kmart_parking_lot_morning",
        "act": 1,
        "sentences": "1.04#1–#2",
        "desc": "Bãi đỗ xe siêu thị Kmart rộng lớn hoang vắng dưới nắng hè gay gắt, một góc khuất xa xa có chiếc xe bán tải màu đen đỗ cô độc bên hàng rào cỏ dại.",
        "prompt": "Wide angle view of a vast, nearly empty suburban department store asphalt parking lot under a harsh, bleached summer midday sun, cracked pavement with patches of overgrown weeds near a chainlink fence border, lonely atmosphere, noir contrast with deep stark shadows."
    },
    {
        "name": "t7_ford_f250_black_truck",
        "act": 1,
        "sentences": "1.04#3",
        "desc": "Chiếc xe bán tải Ford F-250 màu đen đỗ im lìm dưới ánh nắng chói chang, cửa kính đóng kín phản chiếu bầu trời mùa hè ảm đạm, góc máy thấp trang nghiêm.",
        "prompt": "Low-angle cinematic shot of a heavy-duty black pickup truck parked quietly in an isolated corner of an empty parking lot, dark tinted windows reflecting an overcast pale sky, sun flares cutting across the black metal hood, somber graphic novel noir linework."
    },
    {
        "name": "t7_water_pump_equipment",
        "act": 1,
        "sentences": "1.06#1–#2",
        "desc": "Tĩnh vật máy bơm nước cơ khí nhỏ đặt ở thùng xe sau, ống dẫn kim loại phủ bụi, ánh sáng chiaroscuro tương phản mạnh mẽ, góc nhìn hình sự khách quan.",
        "prompt": "Forensic still-life composition of a small gasoline-powered water pump resting in the corrugated bed of a pickup truck, coiled rubber hoses and metal fittings, harsh directional sunlight casting deep black linear shadows, gritty industrial texture, graphic novel noir illustration."
    },
    {
        "name": "t7_tugboat_harbor_fog",
        "act": 1,
        "sentences": "1.06#3–#5",
        "desc": "Bến cảng tàu kéo Fairhaven mờ sương sớm, những con tàu kéo neo đậu bên cầu tàu gỗ cũ kỹ, mặt nước tĩnh lặng, gợi nhắc ước mơ nghề nghiệp thuyền trưởng của Conrad.",
        "prompt": "A quiet New England maritime harbor at early dawn, sturdy commercial tugboats moored alongside weathered wooden piers, thick coastal sea fog swirling across dark calm water, industrial cranes and docks in deep silhouette, evocative noir ink linework."
    },
    {
        "name": "t7_tugboat_captain_license",
        "act": 1,
        "sentences": "1.06#6–#7",
        "desc": "Bằng chứng nhận thuyền trưởng tàu kéo lồng trong khung kính trên bàn làm việc, ánh sáng mờ ảo từ cửa sổ chiếu vào, tĩnh vật trang nghiêm.",
        "prompt": "A framed maritime master captain's license certificate resting on an aged oak study desk, morning window light casting angled Venetian blind shadows across the glass frame, antique brass compass and nautical charts beside it, poignant chiaroscuro atmosphere."
    },
    {
        "name": "t7_mothers_empty_kitchen_phone",
        "act": 1,
        "sentences": "1.07#1–#3",
        "desc": "Bàn ăn trong gian bếp gia đình buổi sáng, chiếc điện thoại nhấp nháy cuộc gọi không người nhấc máy, tách cà phê nguội, ánh sáng xiên qua rèm cửa u buồn.",
        "prompt": "A quiet suburban family kitchen bathed in somber morning light, a smartphone lying face-up on the wooden dining table with a blinking missed-call indicator, an untouched cup of black coffee casting a long shadow, empty chairs, poignant silence, graphic novel noir."
    },
    {
        "name": "t7_kmart_police_perimeter",
        "act": 1,
        "sentences": "1.07#4–#6",
        "desc": "Bãi đỗ xe Kmart bị phong tỏa bởi dây vàng cảnh sát, xe tuần tra nhấp nháy đèn xa xa trong ánh nắng gay gắt, không lộ mặt người.",
        "prompt": "Yellow police crime scene barrier tape fluttering in the wind across the foreground of a sun-bleached parking lot, blurred silhouette of emergency patrol cruisers in the deep background with emergency flashers reflecting on asphalt, solemn investigative atmosphere, noir ink."
    },
    {
        "name": "t7_forensic_evidence_phone",
        "act": 1,
        "sentences": "1.09#1–#3",
        "desc": "Chiếc điện thoại thông minh cũ của nạn nhân đặt trong túi zip đựng vật chứng trong suốt trên bàn kim loại phòng giám định, ánh sáng lạnh kỹ thuật số.",
        "prompt": "A clear plastic forensic evidence bag containing a dark touchscreen mobile phone, laid flat on a brushed stainless steel examination table, forensic metric ruler placed beside it, stark clinical top-down spotlight, high contrast chiaroscuro noir."
    },
    {
        "name": "t7_digital_forensic_extraction",
        "act": 1,
        "sentences": "1.10#1–#4",
        "desc": "Màn hình máy tính điều tra viên hiển thị sơ đồ trích xuất dữ liệu pháp y điện thoại, các biểu đồ tần suất tin nhắn và nhật ký cuộc gọi dày đặc, ánh sáng xanh ma mị.",
        "prompt": "Dark forensic computer laboratory, an illuminated desktop monitor displaying complex digital communication network graphs, message frequency heatmaps, and forensic file extraction progress bars, blue ambient glow reflecting across dark keyboards and desk, detective noir."
    },
    {
        "name": "t7_psychological_trap_metaphor",
        "act": 1,
        "sentences": "1.11#1–#2",
        "desc": "Ẩn dụ thị giác: Một chiếc mê cung vô hình bằng những sợi dây phát sáng kỹ thuật số thắt chặt quanh một chiếc ghế trống, bóng tối chiaroscuro đè nặng.",
        "prompt": "Conceptual visual metaphor of psychological coercion: an empty wooden chair isolated in absolute blackness, surrounded by an intricate web of faintly glowing neon threads and invisible digital strings converging inwards, dramatic chiaroscuro noir, suffocating mood."
    },
    {
        "name": "t7_clinical_depression_shadow",
        "act": 1,
        "sentences": "1.12#1–#3",
        "desc": "Một bóng người đơn độc ngồi cúi đầu trên bờ vực đá hướng ra biển đen mù sương trong đêm tối, chiếc phao cứu sinh rách nát trôi dạt trên bãi cát, ánh sáng lạnh buốt.",
        "prompt": "A dark human silhouette seated alone with head lowered on a craggy coastal cliff overlooking a stormy, churning midnight ocean, thick mist and rain, a weathered tattered lifebuoy half-buried in wet dark sand below, somber desaturated cold palette, graphic novel noir."
    },
    {
        "name": "t7_dossier_carter_case_07",
        "act": 1,
        "sentences": "1.13#1–#2",
        "desc": "Bìa hồ sơ điều tra vụ án Tập 07 Amber Eyes đặt trên bàn gỗ sẫm màu bên cạnh chiếc điện thoại vật chứng và kính lúp hình sự.",
        "prompt": "A thick manila criminal case file folder tied with red string resting on an antique mahogany detective desk, forensic magnifying glass, ink pen, and evidence tags lying beside it, focused warm overhead desk lamp pool of light cutting through heavy surrounding darkness."
    },

    # HỒI 2: MÊ CUNG HAI MƯƠI NGHÌN DÒNG TIN NHẮN (05:00 – 10:00)
    {
        "name": "t7_florida_beach_encounter_2012",
        "act": 2,
        "sentences": "2.02#1–#3",
        "desc": "Bờ biển Florida rực rỡ nhưng nhìn qua lăng kính noir hoài niệm, bóng hai thiếu niên đạp xe trên lối đi ven biển lúc hoàng hôn mờ ảo, không lộ mặt.",
        "prompt": "Nostalgic retro flashback: distant silhouettes of two teenagers riding cruiser bicycles along a sandy Florida coastal boardwalk at dusk, palm trees silhouetted against a desaturated amber and charcoal twilight sky, bittersweet graphic novel noir linework."
    },
    {
        "name": "t7_massachusetts_route_map",
        "act": 2,
        "sentences": "2.03#1–#2",
        "desc": "Bản đồ vệ tinh địa hình bang Massachusetts kết nối hai điểm Plainville và Fairhaven bằng một đường đứt nét phát sáng kỹ thuật số, xuyên qua các khu rừng và thị trấn.",
        "prompt": "A top-down stylized geographic map of southeastern Massachusetts under dim investigative lighting, a glowing digital dashed vector line connecting two distinct suburban towns thirty-five miles apart, contour lines and road grids drawn in precise graphic novel ink."
    },
    {
        "name": "t7_late_night_bedroom_phone",
        "act": 2,
        "sentences": "2.03#3–#4",
        "desc": "Góc phòng ngủ thiếu niên lúc 3 giờ sáng, ánh sáng màn hình điện thoại rọi một góc gối và chăn, đồng hồ báo thức điện tử hiển thị nửa đêm, sự cô lập tột cùng.",
        "prompt": "A dark teenage bedroom at 3 AM, a single smartphone glowing intensely on a bed pillow, casting a stark cold bluish light across rumpled blankets and a bedroom wall, deep cavernous shadows throughout the room, eerie digital isolation, noir aesthetic."
    },
    {
        "name": "t7_plainville_suburban_house",
        "act": 2,
        "sentences": "2.04#1–#3",
        "desc": "Căn nhà hai tầng ngoại ô thị trấn Plainville Massachusetts trong ánh hoàng hôn u ám, rèm cửa sổ phòng ngủ khép kín, nơi phát đi hàng nghìn dòng tin nhắn.",
        "prompt": "Exterior of an affluent quiet New England two-story suburban home at twilight, manicured lawn, dark overcast sky, a single upper bedroom window softly illuminated behind drawn sheer curtains, an aura of quiet unease, dark graphic novel noir."
    },
    {
        "name": "t7_two_phone_screens_contrast",
        "act": 2,
        "sentences": "2.04#4–#6",
        "desc": "Hai chiếc điện thoại thông minh đặt đối diện nhau trên nền kính đen nứt vỡ, một màn hình màu xanh hy vọng mờ nhạt, màn hình kia chuyển sang màu đỏ tối tăm.",
        "prompt": "Two smartphones resting on a dark reflective glass surface with spiderweb hairline cracks, one screen glowing with a faint cool blue pulse while the other emanates a sinister deep amber glow, dramatic chiaroscuro, visual metaphor for toxic psychological divergence."
    },
    {
        "name": "t7_sms_transcript_forensic_binder",
        "act": 2,
        "sentences": "2.06#1–#3",
        "desc": "Tập hồ sơ in rời hàng trăm trang bản trích xuất tin nhắn điện thoại với các đoạn bôi vàng làm nổi bật, kẹp sắt hồ sơ tòa án, ánh đèn neon văn phòng rọi xuống.",
        "prompt": "A thick three-ring evidentiary binder open to pages of densely printed forensic chat logs, specific lines highlighted in translucent amber marker, heavy metal binding rings catching harsh desk light, solemn investigative documentary noir."
    },
    {
        "name": "t7_ticking_clock_deadlines",
        "act": 2,
        "sentences": "2.06#4–#6",
        "desc": "Chiếc đồng hồ treo tường cổ điển kim giây đang nhích dần về phía nửa đêm, bóng đổ kéo dài trên tường vôi, không khí áp bức đếm ngược thời gian.",
        "prompt": "Close-up of a minimalist analog wall clock hanging on a textured dark wall, stark hands pointing near midnight, a sharp beam of raking light accentuating the ticking second hand, long diagonal shadows, intense sense of impending deadline, noir graphic novel."
    },
    {
        "name": "t7_family_photo_frame_shadow",
        "act": 2,
        "sentences": "2.07#1–#4",
        "desc": "Khung ảnh gia đình chụp ba mẹ con trên lò sưởi bị bóng tối chiaroscuro che khuất một nửa, chiếc điện thoại di động rung nhẹ bên cạnh khung ảnh.",
        "prompt": "A silver-framed family portrait resting on a wooden fireplace mantelpiece, heavy chiaroscuro shadow slicing diagonally across the smiling faces, a modern mobile phone resting face-down beside the frame in sharp focus, poignant tension, noir ink art."
    },
    {
        "name": "t7_psychological_coercion_chess",
        "act": 2,
        "sentences": "2.08#1–#4",
        "desc": "Bàn cờ vua bằng đá thạch anh trong bóng tối, một quân tốt trắng bị bao vây bởi vô số bóng đen vô hình trên các ô cờ, biểu tượng của sự bế tắc và thao túng tinh thần.",
        "prompt": "A stone chessboard set against deep blackness, a solitary white pawn surrounded and cornered by elongated predatory dark shadows representing psychological entrapment, dramatic raking spotlight, artistic graphic novel noir."
    },
    {
        "name": "t7_kmart_lot_midnight_darkness",
        "act": 2,
        "sentences": "2.09#1–#3",
        "desc": "Bãi đỗ xe Kmart lúc nửa đêm vắng lặng tuyệt đối, cột đèn cao áp nhấp nháy mờ ảo, chiếc xe tải đen đỗ lẻ loi giữa khoảng sân nhựa đường ướt sương đêm.",
        "prompt": "Desolate suburban Kmart parking lot at midnight, a single tall sodium vapor lamp flickering weakly above, casting a wide hazy orange pool on damp dark asphalt, solitary silhouette of a black pickup truck parked at the far periphery, noir mood."
    },
    {
        "name": "t7_open_truck_door_fresh_air",
        "act": 2,
        "sentences": "2.09#4–#6",
        "desc": "Cánh cửa xe tải hé mở, bậc bước chân dính vài giọt sương, một luồng ánh sáng từ cabin hắt ra nền nhựa đường, biểu tượng cho khoảnh khắc người thanh niên bước ra chọn sự sống.",
        "prompt": "An open driver-side door of a dark pickup truck, interior cabin dome light spilling a beam of warm yellow light onto the wet asphalt ground outside, footsteps on damp pavement, night breeze stirring fallen leaves, symbol of reaching for life, graphic novel noir."
    },
    {
        "name": "t7_night_sky_breath_of_life",
        "act": 2,
        "sentences": "2.09#7–#8",
        "desc": "Bầu trời đêm sâu thẳm đầy sao phía trên bãi đỗ xe ven biển, làn gió đêm lay động hàng cây phong, không gian mở thoáng đãng tương phản với cabin ngột ngạt.",
        "prompt": "A wide upward shot gazing at a deep indigo night sky dotted with faint distant stars, tree silhouettes framing the upper edges, clean crisp night air blowing through lush branches, a momentary sense of freedom and open space, noir watercolor wash."
    },
    {
        "name": "t7_incoming_call_timer_40min",
        "act": 2,
        "sentences": "2.10#1–#2",
        "desc": "Chiếc điện thoại hiển thị giao diện cuộc gọi đang diễn ra hơn 40 phút, nằm trên nắp capô xe hơi trong bóng đêm, ánh sáng màn hình phản chiếu lạnh tanh.",
        "prompt": "A smartphone resting on the curved metallic hood of a dark vehicle under moonlight, the screen illuminated with an active call timer showing extensive elapsed duration, digital soundwave graphic glowing faintly, cold noir chiaroscuro composition."
    },
    {
        "name": "t7_closed_car_window_fog",
        "act": 2,
        "sentences": "2.10#3",
        "desc": "Kính cửa sổ cabin xe tải đóng kín hoàn toàn từ bên trong, sương mù và hơi nước bắt đầu đọng thành giọt trên mặt kính, bóng đêm bao trùm vĩnh viễn.",
        "prompt": "Close-up of a pickup truck side window tightly closed from within, heavy condensation and moisture beads dripping slowly down the dark tinted glass, exterior reflection of dim distant streetlights, ominous suffocation, graphic novel noir."
    },

    # HỒI 3: VỞ KỊCH CÔ BẠN GÁI ĐAU KHỔ & BỘ NÃO ÁI KỶ KỊCH TÍNH (10:00 – 15:00)
    {
        "name": "t7_empty_theater_spotlight",
        "act": 3,
        "sentences": "3.02#1–#2",
        "desc": "Một sân khấu kịch bằng gỗ trống không, chỉ có một chiếc đèn rọi duy nhất rọi xuống một chiếc ghế gãy, không gian xung quanh đen kịt.",
        "prompt": "An empty wooden theatrical stage plunged in complete darkness except for a single harsh conical white spotlight shining down on the center floorboards, heavy velvet curtains draped in shadow at the wings, dramatic noir staging of histrionic narcissism."
    },
    {
        "name": "t7_drama_masks_digital_glitch",
        "act": 3,
        "sentences": "3.03#1–#3",
        "desc": "Hai chiếc mặt nạ kịch nghệ (bi kịch và hài kịch) treo trên tường bê tông nứt nẻ, bị nhiễu sóng kỹ thuật số, chiaroscuro sắc nét.",
        "prompt": "Two classic theatrical drama masks (tragedy and comedy) carved from white porcelain hanging on a dark textured cracked concrete wall, fractured with subtle digital glitch scanlines and glowing data artifacts, sharp chiaroscuro lighting."
    },
    {
        "name": "t7_highschool_empty_lockers",
        "act": 3,
        "sentences": "3.04#1–#3",
        "desc": "Hành lang trường trung học King Philip hoang vắng lúc hoàng hôn, những dãy tủ sắt locker màu xám kéo dài hun hút, bóng râm tĩnh mịch của sự cô lập học đường.",
        "prompt": "A deserted suburban high school hallway after hours, rows of metal lockers stretching down a polished linoleum corridor, dim amber dusk light filtering through high windows casting long geometric shadows, eerie silence and social isolation."
    },
    {
        "name": "t7_vintage_tv_glee_glow",
        "act": 3,
        "sentences": "3.05#1–#2",
        "desc": "Màn hình tivi trong phòng tối đang phát một tập phim truyền hình ca nhạc thanh thiếu niên, ánh sáng xanh lục huỳnh quang hắt lên bàn học chất đầy tạp chí tuổi teen.",
        "prompt": "A modern flat-screen television glowing in a dark teenage bedroom, displaying blurred colorful musical performance imagery, casting vibrant cyan and magenta light across a desk cluttered with teen entertainment magazines, graphic novel noir."
    },
    {
        "name": "t7_copied_script_lines_notebook",
        "act": 3,
        "sentences": "3.05#3–#4",
        "desc": "Cuốn sổ tay mở trên bàn học với những dòng chữ ghi chép cẩn thận các câu thoại phim kịch nghệ, bên cạnh là chiếc máy tính xách tay phát sáng.",
        "prompt": "A spiral-bound lined notebook open on a study desk, neat handwritten verbatim quotes and theatrical dialogue copied with blue fountain pen ink, a lit laptop keyboard in the soft background, noir chiaroscuro desk setting."
    },
    {
        "name": "t7_staged_tragedy_mirror",
        "act": 3,
        "sentences": "3.06#1–#3",
        "desc": "Một chiếc gương trang điểm trong phòng ngủ phản chiếu bộ trang phục tang lễ màu đen treo trên mắc áo, ánh sáng chiaroscuro tương phản ma mị.",
        "prompt": "A bedroom vanity mirror reflecting a dark tailored mourning dress hanging on a wooden coat rack, makeup brushes and perfume atomizers arranged neatly on the glass vanity top, dramatic theatrical shadows, graphic novel noir art."
    },
    {
        "name": "t7_suburban_living_room_tv",
        "act": 3,
        "sentences": "3.06#4–#6",
        "desc": "Phòng khách gia đình ấm cúng với tivi đang bật, chiếc ghế sofa êm ái nơi chàng trai trẻ đang ngồi bình yên bên người thân trước khi chiếc bẫy tinh thần khép lại.",
        "prompt": "A warm, comforting suburban living room at evening time, soft incandescent lamp light, a cozy sofa facing a glowing television set, peaceful domestic tranquility contrasting sharply with external psychological manipulation, cinematic noir."
    },
    {
        "name": "t7_puppet_strings_metaphor",
        "act": 3,
        "sentences": "3.07#1–#3",
        "desc": "Ẩn dụ thị giác: Những sợi dây rối vô hình buông xuống từ trần nhà tăm tối, gắn vào một màn hình điện thoại phát sáng, bố cục noir kịch tính đầy ẩn ý.",
        "prompt": "Dark symbolic graphic illustration: marionette wooden crossbars and delicate glowing strings descending from an unseen ceiling, attached to an illuminated smartphone floating in mid-air, psychological puppetry, deep obsidian shadows."
    },
    {
        "name": "t7_social_media_notifications_flood",
        "act": 3,
        "sentences": "3.08#1–#3",
        "desc": "Biểu tượng thông báo lượt thích, lượt chia sẻ và bình luận an ủi trên màn hình kỹ thuật số mờ ảo, hàng trăm ánh đèn nhỏ lấp lánh như đom đóm trong đêm đen ảo vọng.",
        "prompt": "Abstract digital noir visualization of social media validation: countless floating holographic notification badges, heart icons, and message bubbles glowing softly in an endless dark cyber void, seductive yet hollow atmosphere."
    },
    {
        "name": "t7_baseball_field_charity_empty",
        "act": 3,
        "sentences": "3.08#4–#6",
        "desc": "Sân bóng chày ngoại ô vắng lặng lúc chạng vạng, chiếc găng tay bóng chày và quả bóng cũ nằm trên băng ghế gỗ, tấm băng rôn từ thiện Homers for Conrad bay nhẹ.",
        "prompt": "A quiet suburban community baseball diamond at sunset, wooden dugout bench with a worn leather baseball glove and ball left behind, a faded charity banner tied to the chain-link backstop fluttering in the evening breeze, noir palette."
    },
    {
        "name": "t7_cracked_porcelain_mask",
        "act": 3,
        "sentences": "3.08#7",
        "desc": "Chiếc mặt nạ thiên thần bằng sứ trắng tinh khôi bị rạn nứt một đường chéo sắc lẹm, để lộ bóng tối vô tận phía sau, chuyển hồi sang Hồi 4.",
        "prompt": "A pristine white porcelain angelic face mask fractured cleanly down the middle by a jagged dark crack, stark directional light highlighting the smooth surface while pitch blackness gapes behind the split, dramatic chiaroscuro noir."
    },

    # HỒI 4: DÒNG TIN NHẮN ĐẦY TỘI LỖI VÀ BẢN ÁN LỊCH SỬ (15:00 – 20:00)
    {
        "name": "t7_confession_text_timestamp",
        "act": 4,
        "sentences": "4.02#1–#3",
        "desc": "Màn hình điện thoại hiển thị ngày September 15 2014 với dòng tin nhắn văn bản màu xám bạc trôi trên nền đen tuyền, góc chụp cận cảnh nghệ thuật chiaroscuro.",
        "prompt": "Macro close-up of a mobile messaging interface displaying a formal timestamp of mid-September 2014, glowing dialogue bubbles stacked neatly, clean crisp typography style with noir lighting and subtle glass reflections."
    },
    {
        "name": "t7_witness_trembling_phone",
        "act": 4,
        "sentences": "4.03#1–#4",
        "desc": "Cận cảnh bàn tay thiếu nữ nắm chặt chiếc điện thoại đang phát sáng trong quán cà phê vắng, ngón tay run rẩy bên tách cà phê đá, ánh sáng xiên qua cửa kính mờ mưa.",
        "prompt": "Close-up on hands trembling slightly while holding an illuminated phone beside a glass of iced coffee in a dim rainy cafe booth, raindrops streaking down the glass window in background, intense shock and moral horror captured in noir linework."
    },
    {
        "name": "t7_confession_message_turn",
        "act": 4,
        "sentences": "4.03#5–#8",
        "desc": "Tập tài liệu in lời khai nhân chứng Samantha Boardman được đóng dấu tiếp nhận của Cơ quan Điều tra Cảnh sát Fairhaven.",
        "prompt": "Formal printed witness interview statement document resting on a police detective's desk, blue ink signature at the bottom alongside a red rubber ink stamp from Fairhaven Police Department, serious investigative documentary noir."
    },
    {
        "name": "t7_bristol_county_indictment_stamp",
        "act": 4,
        "sentences": "4.05#1–#3",
        "desc": "Văn bản cáo trạng của Tòa án Hạt Bristol với con dấu mực đỏ tươi INDICTMENT INVOLUNTARY MANSLAUGHTER đóng dứt khoát trên trang giấy công văn.",
        "prompt": "Legal indictment papers with embossed state seal, a prominent red stamped seal reading 'COMMONWEALTH INDICTMENT', heavy linen paper texture, antique wooden desk surface, authoritative judicial noir."
    },
    {
        "name": "t7_taunton_courthouse_exterior",
        "act": 4,
        "sentences": "4.05#4–#5",
        "desc": "Mặt tiền Tòa án Hạt Bristol tại Taunton Massachusetts bằng đá hoa cương uy nghiêm, những bậc thang đá cổ kính và hàng cột La Mã sừng sững dưới bầu trời xám xịt.",
        "prompt": "Grand neoclassical exterior of the Bristol County Juvenile Courthouse in Taunton Massachusetts, imposing granite columns, wide stone stairs, overcast stormy sky, dramatic low angle, solemn legal drama noir."
    },
    {
        "name": "t7_empty_courtroom_bench_trial",
        "act": 4,
        "sentences": "4.05#6",
        "desc": "Góc nhìn bên trong phòng xử án trang nghiêm, dãy ghế bồi thẩm đoàn hoàn toàn trống rỗng, ánh sáng tập trung vào chiếc bục gỗ của Thẩm phán duy nhất.",
        "prompt": "Interior of an empty formal courtroom during a bench trial, polished mahogany jury box noticeably vacant with rows of empty wooden armchairs, solitary light beam illuminating the high elevated judge's bench, majestic quiet."
    },
    {
        "name": "t7_courtroom_projection_screen",
        "act": 4,
        "sentences": "4.06#1–#2",
        "desc": "Màn hình máy chiếu lớn trong phòng xử án hiển thị hàng chục dòng tin nhắn phóng to với các mốc thời gian rõ ràng, các luật sư và công tố viên chìm trong bóng lưng.",
        "prompt": "A large digital courtroom evidence projection screen illuminating a dark courtroom, displaying thousands of lines of parsed SMS text messages in high contrast, silhouettes of courtroom spectators and attorneys seated in solemn attention."
    },
    {
        "name": "t7_us_constitution_amendment1",
        "act": 4,
        "sentences": "4.06#3–#4",
        "desc": "Quyển sách luật Hiến pháp Hoa Kỳ mở tại trang Tu chính án thứ nhất bên cạnh chiếc búa gỗ của thẩm phán, cuộc xung đột giữa tự do ngôn luận và trách nhiệm hình sự.",
        "prompt": "A heavy leather-bound volume of United States Constitutional Law open to the First Amendment, an antique brass scale of justice balancing in the soft background, deep judicial chiaroscuro shadows."
    },
    {
        "name": "t7_prescription_pill_bottle_celexa",
        "act": 4,
        "sentences": "4.07#1–#4",
        "desc": "Lọ thuốc chống trầm cảm theo toa bằng nhựa màu hổ phách đặt trên mặt bàn kính bên cạnh tập tài liệu giám định tâm thần pháp y, viên thuốc rơi nhẹ trên bàn.",
        "prompt": "An amber translucent prescription pill bottle with clinical label resting beside a forensic psychiatric evaluation binder on a reflective glass desk, a single pill lying near the cap, stark clinical chiaroscuro noir."
    },
    {
        "name": "t7_judge_moniz_bench_gavel",
        "act": 4,
        "sentences": "4.08#1–#4",
        "desc": "Bục xét xử của Thẩm phán Lawrence Moniz với chiếc búa gỗ tư pháp đặt trang trọng trên đệm da, tập phán quyết dày mở sẵn dưới ánh đèn vàng ấm áp.",
        "prompt": "Elevated wooden judicial bench of Judge Lawrence Moniz, a polished dark hardwood gavel resting on its striking block, thick typed legal findings of fact documents open, dignified golden overhead court lighting."
    },
    {
        "name": "t7_courtroom_breathless_silence",
        "act": 4,
        "sentences": "4.08#5–#7",
        "desc": "Toàn cảnh phòng xử án chìm trong sự im lặng căng thẳng tuyệt đối, các hàng ghế khán giả tối màu, ánh sáng chiaroscuro rọi thẳng vào trung tâm bục công lý.",
        "prompt": "Wide atmospheric view of a crowded Massachusetts courtroom held in breathless silence, gallery benches in deep chiaroscuro silhouette, shafts of afternoon window light slicing across polished oak railings, historic verdict moment."
    },
    {
        "name": "t7_court_verdict_document_guilty",
        "act": 4,
        "sentences": "4.10#1–#2",
        "desc": "Bản án chính thức của Tòa án Tối cao Massachusetts có chữ ký và dấu mộc xác nhận tội danh GUILTY OF INVOLUNTARY MANSLAUGHTER.",
        "prompt": "The official signed judicial verdict document of Massachusetts Commonwealth Court, bold black lettering 'GUILTY - INVOLUNTARY MANSLAUGHTER', judicial embossed gold foil seal, dark rich noir lighting."
    },
    {
        "name": "t7_bristol_county_jail_bars",
        "act": 4,
        "sentences": "4.10#3",
        "desc": "Song sắt nhà giam Hạt Bristol đổ bóng dài xuống hành lang bê tông xám lạnh lẽo, biểu trưng cho sự trừng phạt nghiêm minh của pháp luật.",
        "prompt": "Heavy vertical steel prison cell bars casting long parallel geometric shadows down an empty polished concrete correctional corridor, cold fluorescent institutional light, solemn conclusion of justice, graphic novel noir."
    },

    # HỒI 5: ĐẠO ĐỨC KHÔNG GIAN SỐ & ĐẠO LUẬT CONRAD (20:00 – 26:00)
    {
        "name": "t7_massachusetts_state_house_dome",
        "act": 5,
        "sentences": "5.02#1–#3",
        "desc": "Mái vòm mạ vàng của Tòa nhà Nghị viện Bang Massachusetts tại Boston vươn cao trên nền trời xanh thẫm, biểu tượng của sự lập pháp và công lý.",
        "prompt": "The iconic gleaming golden dome of the Massachusetts State House in Boston standing proud against a dramatic stormy twilight sky, historic brick facade, majestic architectural graphic novel noir linework."
    },
    {
        "name": "t7_conrads_law_legislative_bill",
        "act": 5,
        "sentences": "5.02#4–#6",
        "desc": "Dự thảo văn bản Conrad's Law An Act Preventing Coerced Suicide được đệ trình lên nghị viện, chiếc bút máy đặt bên cạnh chữ ký bảo trợ của các nhà lập pháp.",
        "prompt": "An official legislative bill document titled 'CONRAD\\'S LAW - AN ACT PREVENTING COERCED SUICIDE' laid neatly on a mahogany legislative committee desk, a classic fountain pen resting across the sponsor signature line, warm judicial light."
    },
    {
        "name": "t7_digital_cage_smartphone_glow",
        "act": 5,
        "sentences": "5.03#1–#3",
        "desc": "Ẩn dụ thị giác: Một chiếc lồng chim bằng thanh kim loại mỏng bao bọc một chiếc điện thoại đang phát sáng trong đêm tối, biểu trưng cho chiếc lồng giam tâm lý.",
        "prompt": "Surreal symbolic noir artwork: an ornate vintage birdcage forged from dark iron bars enclosing an illuminated glowing smartphone inside, surrounded by deep obsidian darkness, metaphor for toxic digital isolation."
    },
    {
        "name": "t7_redflag1_isolated_virtual_bubble",
        "act": 5,
        "sentences": "5.04#1–#4",
        "desc": "Cảnh báo đỏ 1: Một quả cầu thủy tinh phát sáng cô lập giữa rừng cây tăm tối, bên trong là hai bóng đen ảo trao đổi tín hiệu số, biểu tượng mối quan hệ mạng khép kín.",
        "prompt": "Conceptual visual warning: an ethereal glowing glass sphere isolated in the middle of a dense dark forest, tiny digital fiber-optic pulses circulating inside, dark graphic novel noir style, moody desaturated blue tones."
    },
    {
        "name": "t7_redflag2_manipulative_text_provocation",
        "act": 5,
        "sentences": "5.04#5–#7",
        "desc": "Cảnh báo đỏ 2: Cận cảnh những dòng tin nhắn mỉa mai khiêu khích hiện lên trên màn hình điện thoại nứt vỡ, chiếc bóng săn mồi lướt qua phía sau.",
        "prompt": "Dramatic close-up of a shattered phone screen glowing aggressively in the dark, harsh fragmented shadows cast on a table, predatory dark silhouette towering in background shadow, noir graphic novel tension."
    },
    {
        "name": "t7_redflag3_performative_grief_stage",
        "act": 5,
        "sentences": "5.04#8–#11",
        "desc": "Cảnh báo đỏ 3: Một chiếc bục phát biểu vây quanh bởi hàng chục micrô và ống kính máy ảnh, trên bục là chiếc khăn tang màu đen rỗng không.",
        "prompt": "A press conference podium surrounded by a thick cluster of microphones and flashing media camera lenses in the dark, on the podium rests an empty black mourning ribbon, theatrical chiaroscuro critique of performative grief."
    },
    {
        "name": "t7_redflag4_disconnect_phone_dawn",
        "act": 5,
        "sentences": "5.04#12–#15",
        "desc": "Cảnh báo đỏ 4: Chiếc điện thoại thông minh bị đặt úp mặt xuống chiếc bàn gỗ bên cửa sổ mở toang, ánh bình minh ấm áp tràn vào phòng xua tan bóng tối.",
        "prompt": "A smartphone turned face down decisively on a rustic wooden windowsill, an open window looking out at a gentle golden sunrise over the ocean, fresh morning breeze fluttering linen curtains, symbol of choosing real life over digital darkness."
    },
    {
        "name": "t7_digital_lighthouse_beacon",
        "act": 5,
        "sentences": "5.04#16–#17",
        "desc": "Ngọn hải đăng ven biển Fairhaven quét luồng sáng vàng rực rỡ xuyên qua màn đêm mù sương trên mặt biển, ngụ ý ánh sáng tri thức và sự tỉnh táo dẫn đường.",
        "prompt": "A coastal stone lighthouse on a rocky New England bluff sweeping a powerful, brilliant beam of golden light through dense ocean fog and dark churning waves, beacon of truth, hope, and clarity, stunning graphic novel noir."
    },
    {
        "name": "t7_closing_dossier_white_rose",
        "act": 5,
        "sentences": "5.04#18",
        "desc": "Bìa hồ sơ vụ án Tập 07 khép lại trang nghiêm trên bàn gỗ sồi, đặt bên cạnh một cành hoa hồng trắng tươi và ngọn nến lung linh dưới ánh bình minh hé rạng.",
        "prompt": "The closed confidential case dossier of Episode 07 tied neatly with a crimson ribbon on a warm oak desk, a fresh single white rose and a softly burning candle placed beside it, golden morning sun rays breaking across the scene, peaceful closure."
    }
]

out_file = WORK / "bg_jobs_tap07.json"
out_file.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Da tao {out_file} voi {len(jobs)} jobs anh!")
