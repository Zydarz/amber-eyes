import json
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"

jobs = [
    # =========================================================================
    # HỒI 1: ĐÊM ĐEN TRÊN ĐỒI BEVERLY VÀ DẤU CHẤM HẾT CỦA MÙA HÈ TÌNH YÊU (00:00 – 05:00)
    # =========================================================================
    {
        "name": "t9_summer_of_love_hippie_la",
        "act": 1,
        "sentences": "1.02#1–#2",
        "desc": "Hoàng hôn Los Angeles cuối thập niên 1960, bóng những thanh niên Hippie cài hoa trên tóc bên chiếc xe van retro ngập nắng vàng hoài niệm chiaroscuro.",
        "prompt": "Cinematic wide shot of a California coastal highway near Los Angeles during the late 1960s Summer of Love, golden hour sunset bathing silhouetted young hippies with wildflowers in their hair leaning on a vintage psychedelic camper van, dark graphic novel noir style, heavy ink contours, deep chiaroscuro, nostalgic warm amber and slate palette, fine film grain."
    },
    {
        "name": "t9_acoustic_guitar_flower_crown",
        "act": 1,
        "sentences": "1.02#3",
        "desc": "Tĩnh vật cây guitar acoustic mộc mạc dựa bên chiếc vương miện hoa dại đã khô héo trên sàn gỗ mộc, ánh sáng xiên u buồn.",
        "prompt": "Forensic still life of a battered vintage acoustic guitar leaning against a dark rustic wooden wall, a faded dried wildflower crown resting on its strings, single harsh diagonal shaft of golden dust-filled light across dark textured floorboards, poignant tragic beauty, graphic novel noir illustration."
    },
    {
        "name": "t9_los_angeles_skyline_1969",
        "act": 1,
        "sentences": "1.02#4–#5",
        "desc": "Bầu trời Los Angeles hoàng hôn 1969 nhìn từ đỉnh đồi, những rặng cây cọ đen thẫm in trên nền trời hoàng hôn rực lửa chuyển dần sang màn đêm buốt giá.",
        "prompt": "Dramatic establishing view of the 1969 Los Angeles basin from a lonely Hollywood hilltop, silhouette of iconic tall fan palm trees cutting into an ominous bruised-purple and crimson sunset horizon, deep ink shadows swallowing the foothills below, dark graphic noir aesthetic."
    },
    {
        "name": "t9_cielo_drive_estate_night",
        "act": 1,
        "sentences": "1.04#1–#2",
        "desc": "Ngôi biệt thự phong cách điền trang tại 10050 Đại lộ Cielo Drive ẩn mình giữa những rặng thông đen u tịch trên đỉnh đồi Benedict Canyon trong đêm định mệnh.",
        "prompt": "Low-angle nocturnal shot of the secluded luxury ranch-style estate at 10050 Cielo Drive tucked beneath tall towering dark pine trees on a Beverly Hills hillside, midnight fog swirling across the private gravel cul-de-sac, pale moonlight cutting through darkness, chilling quiet dread, chiaroscuro noir."
    },
    {
        "name": "t9_beverly_hills_gate_road",
        "act": 1,
        "sentences": "1.06#1",
        "desc": "Cổng sắt hoa văn mở he hé và con đường sỏi uốn lượn dẫn vào biệt thự đồi cao, ánh trăng bạc rọi xuống rặng cây đen kịt.",
        "prompt": "Heavy ornate black wrought-iron security gate standing slightly ajar at the foot of an upscale private estate driveway, winding gravel pathway disappearing into dense nocturnal foliage, stark high-contrast chiaroscuro, graphic novel ink shading, ominous isolation."
    },
    {
        "name": "t9_cielo_drive_living_room_somber",
        "act": 1,
        "sentences": "1.06#2–#4",
        "desc": "Gian phòng khách biệt thự sang trọng chìm trong tĩnh lặng u uất, ánh đèn bàn hắt bóng dài, những đồ vật vương vãi, không khí nghẹt thở bi kịch (không máu me, V9).",
        "prompt": "Atmospheric interior of a mid-century Hollywood luxury living room in deep night, warm table lamp casting dramatic long shadows across exposed wood beams, scattered vintage records and overturned furniture, solemn dignified forensic silence, strictly no blood, no gore, graphic novel noir."
    },
    {
        "name": "t9_waverly_drive_residence_night",
        "act": 1,
        "sentences": "1.06#5–#6",
        "desc": "Ngôi nhà một tầng phong cách suburban thập niên 60 tại 3311 Waverly Drive khu Los Feliz, cửa sổ tối om, hàng rào thấp, một bóng đen lẻ loi trong đêm.",
        "prompt": "Exterior of a modest 1960s suburban one-story residential home at 3311 Waverly Drive in Los Feliz at 2 AM, darkened windows, neat trimmed lawn bordered by low dark hedge, lone streetlamp casting long eerie yellow light cone, chilling stillness, graphic noir."
    },
    {
        "name": "t9_retro_radio_broadcast_table",
        "act": 1,
        "sentences": "1.07#1–#2",
        "desc": "Chiếc đài bán dẫn radio cổ điển thập niên 60 đang phát sóng trên bàn gỗ, tách cà phê nguội, ánh sáng ban mai chiếu qua rèm cửa khép kín.",
        "prompt": "Close-up of a vintage 1960s wooden transistor radio sitting on a kitchen table beside an untouched ceramic coffee mug, morning light filtering through closed Venetian blinds, stark linear shadow patterns across the surface, tense news broadcast atmosphere, graphic novel ink."
    },
    {
        "name": "t9_gun_shop_empty_shelves",
        "act": 1,
        "sentences": "1.07#3–#4",
        "desc": "Tủ kính cửa hàng khóa và súng ở Hollywood với các kệ hàng trống trơn, biển báo đóng cửa, ánh đèn neon phản chiếu trên vỉa hè vắng tanh.",
        "prompt": "Shopfront window of a Hollywood hardware and locksmith store at dusk, empty display shelves, padlocks and deadbolts sold out, neon sign casting red glow onto slick dark pavement, silhouetted pedestrian passing hurriedly, widespread panic, noir styling."
    },
    {
        "name": "t9_intact_valuables_diorama",
        "act": 1,
        "sentences": "1.07#5–#6",
        "desc": "Hộp trang sức và đồng hồ đắt tiền còn nguyên trên bàn trang điểm gỗ gụ, lớp bụi mỏng phủ lên trong bóng tối chiaroscuro.",
        "prompt": "Forensic still life of an open velvet jewelry box with untouched pearls and expensive wristwatch sitting undisturbed on a dark mahogany dressing table, raking spotlight highlighting the absence of theft, proof of senseless cruelty, deep shadows, graphic novel art."
    },
    {
        "name": "t9_withered_flower_on_asphalt",
        "act": 1,
        "sentences": "1.07#7–#8",
        "desc": "Một bông hoa dại khô héo bị giẫm nát trên nền nhựa đường lạnh ngắt, biểu tượng cho sự chấm dứt của kỷ nguyên ngây thơ Hippie.",
        "prompt": "Macro shot of a crushed wilted sunflower lying solitary on wet black cracked asphalt, tire tread marks nearby, cold pale morning light, powerful metaphor for the death of innocence and the end of the Summer of Love, high contrast noir linework."
    },
    {
        "name": "t9_bloody_letters_forensic_wall",
        "act": 1,
        "sentences": "1.09#1–#3",
        "desc": "Bức tường trắng loang lổ bóng tối với các chữ cái hình sự được khoanh vùng phân tích, ánh đèn pin pháp y chiếu rọi, góc chụp noir góc hẹp.",
        "prompt": "Forensic investigative view of an interior wall under harsh circular flashlight beam, abstract geometric police evidence markers and chalk grids outlining cryptic scrawled markings, dark chiaroscuro room, tense investigative documentary tone, no graphic violence."
    },
    {
        "name": "t9_lapd_investigation_room",
        "act": 1,
        "sentences": "1.10#1–#2",
        "desc": "Bàn làm việc ban chuyên án Sở Cảnh sát Los Angeles ngổn ngang sơ đồ hiện trường, điện thoại bàn quay số và cốc cà phê giấy, ánh đèn chùm mờ ảo.",
        "prompt": "Atmospheric 1969 LAPD detective bureau squad room late at night, messy oak desk covered in black-and-white crime scene photos, rotary desk telephone, cigarette smoke haze hanging in the cone of an overhead green banker lamp, baffled investigators, graphic noir."
    },
    {
        "name": "t9_los_angeles_county_crime_map",
        "act": 1,
        "sentences": "1.10#3–#4",
        "desc": "Bản đồ quy hoạch đô thị Los Angeles nối các đường chỉ đỏ giữa Benedict Canyon (Beverly Hills) và Los Feliz, ghim định vị hiện trường.",
        "prompt": "Forensic pinboard showing a vintage map of Los Angeles County, red string linking pushpins at Benedict Canyon and Los Feliz miles apart, typed forensic index cards pinned to corkboard, stark directional side lighting, investigative procedural aesthetics."
    },
    {
        "name": "t9_invisible_puppet_master_shadow",
        "act": 1,
        "sentences": "1.10#5–#6",
        "desc": "Bóng đen mờ ảo của một bàn tay điều khiển những sợi dây con rối vô hình trong bóng tối chiaroscuro nghệ thuật noir.",
        "prompt": "Abstract psychological noir illustration of a towering silhouetted hand in shadows above dangling marionette strings receding into darkness, subtle atmospheric haze, metaphor for fanatical invisible mental control and puppet manipulation."
    },
    {
        "name": "t9_newspaper_headline_helter_skelter",
        "act": 1,
        "sentences": "1.11#1–#3",
        "desc": "Tờ nhật báo Los Angeles Times tháng 8/1969 với hàng tít đen in đậm về thảm kịch đồi Beverly, chụp tĩnh vật trên bàn làm việc tối.",
        "prompt": "Vintage 1969 broadsheet newspaper folded on a dark desk, bold black headline reading in stylized retro print, cup of coffee with steam wisps, reading glasses resting on the paper, grim historical investigative tone, chiaroscuro lighting."
    },

    # =========================================================================
    # HỒI 2: ẢO ẢNH HELTER SKELTER TẠI TRANG TRẠI SPAHN RANCH (05:00 – 10:00)
    # =========================================================================
    {
        "name": "t9_spahn_ranch_western_facade",
        "act": 2,
        "sentences": "2.02#1–#3",
        "desc": "Cảnh toàn trang trại Spahn Ranch tiêu điều dưới chân núi đá thung lũng Santa Susana, những dãy nhà gỗ kiểu phim trường cao bồi bỏ hoang, cỏ gai khô lăn trong gió sa mạc.",
        "prompt": "Wide desolate landscape of Spahn Movie Ranch in the Santa Susana Mountains outside Chatsworth, dilapidated rustic western movie set wooden false facades weathering under scorching California sun, tumbleweeds on dusty dirt road, craggy dry sandstone hills, graphic novel noir."
    },
    {
        "name": "t9_spahn_ranch_dilapidated_porch",
        "act": 2,
        "sentences": "2.04#1–#2",
        "desc": "Hiên nhà gỗ mục nát của Spahn Ranch với những chiếc yên ngựa cũ, thùng gỗ và bóng dáng lờ mờ của những chiếc xe bán tải rỉ sét.",
        "prompt": "Low-angle view of a creaky weathered wooden boardwalk porch at Spahn Ranch, aged leather horse saddles hung on timber rails, rusted 1950s pickup truck parked in background heat shimmer, oppressive isolation, stark ink shadow line art."
    },
    {
        "name": "t9_prison_cell_bars_shadow",
        "act": 2,
        "sentences": "2.05#1–#2",
        "desc": "Song sắt nhà tù liên bang đổ bóng dài trên sàn bê tông lạnh buốt, một tập hồ sơ tiền án dày cộp đặt dưới ánh sáng le lói.",
        "prompt": "Grim perspective looking through heavy steel prison cell bars casting parallel diagonal shadows across cold cracked concrete, thick institutional criminal record dossier lying on metal bunk, gritty institutional penal history, dark noir chiaroscuro."
    },
    {
        "name": "t9_haight_ashbury_psychedelic_street",
        "act": 2,
        "sentences": "2.05#3–#5",
        "desc": "Ngã tư Haight và Ashbury ở San Francisco trong sương mù, các poster ảo giác psychedelic mờ nhạt trên tường gạch, những bóng người lang thang.",
        "prompt": "Street corner of Haight and Ashbury in San Francisco shrouded in cold coastal fog, faded psychedelic concert posters peeling on brick walls, Victorian storefronts in silhouette, drifting young wanderers, melancholy counterculture noir illustration."
    },
    {
        "name": "t9_dark_triad_psychological_symbol",
        "act": 2,
        "sentences": "2.06#1–#3",
        "desc": "Biểu tượng phân tích tâm lý học tam giác bóng tối, ba đỉnh giao nhau với ánh sáng lạnh, phản ánh sự thao túng và thiếu vắng lương tri.",
        "prompt": "Conceptual psychological illustration of the Dark Triad personality construct, geometric tripartite obsidian triangle glowing with cold phosphorescent edge light in pitch darkness, sharp intersecting facets representing narcissism, psychopathy, and Machiavellianism."
    },
    {
        "name": "t9_runaway_teenager_bus_stop",
        "act": 2,
        "sentences": "2.06#4–#5",
        "desc": "Trạm xe buýt ven đường đêm hoang vắng, chiếc ba lô cũ đặt dưới chân ghế, bóng người thanh thiếu niên cô độc nhìn về phía xa xăm.",
        "prompt": "A solitary runaway youth in silhouette sitting alone on a wooden bench at a deserted rural bus stop at midnight, beat-up canvas rucksack on the ground, single sodium-vapor streetlamp casting harsh yellow oval, vulnerability and identity crisis, graphic novel art."
    },
    {
        "name": "t9_confiscated_clocks_broken_mirror",
        "act": 2,
        "sentences": "2.07#1–#2",
        "desc": "Chiếc gương nứt vỡ nằm cạnh những chiếc đồng hồ đeo tay và lịch treo tường bị vứt bỏ trong góc tối, biểu tượng tước đoạt nhận thức thời gian.",
        "prompt": "Still-life symbolic shot of shattered mirror shards lying beside a pile of abandoned wristwatches and torn paper calendar pages in a dark barn corner, raking beam of light revealing cracked glass reflections, destruction of time and personal reflection."
    },
    {
        "name": "t9_manson_shadow_campfire_desert",
        "act": 2,
        "sentences": "2.07#3–#4",
        "desc": "Bóng đen của Charles Manson đứng trước đống lửa trại rực rỡ giữa sa mạc đêm, xung quanh là những chiếc bóng người ngồi nghe mê muội.",
        "prompt": "Nighttime desert scene with a crackling campfire casting flickering amber light and long dancing ink shadows, silhouette of a charismatic speaker standing gesturing before a circle of enraptured silhouetted listeners seated on rocks, eerie cult aura, chiaroscuro noir."
    },
    {
        "name": "t9_vinyl_record_white_album",
        "act": 2,
        "sentences": "2.08#1–#2",
        "desc": "Đĩa than vinyl màu trắng đang quay trên máy hát cổ điển, rãnh đĩa đen bóng dưới ánh đèn vàng mờ, vỏ đĩa trắng tối giản.",
        "prompt": "Macro shot of a vintage turntable needle playing a spinning black vinyl record beside an austere plain white album sleeve, amber spotlight highlighting spiral grooves, subtle audio waveform lines vibrating in dark air, distorted musical obsession."
    },
    {
        "name": "t9_apocalyptic_desert_hideout",
        "act": 2,
        "sentences": "2.08#3–#5",
        "desc": "Hang đá và thung lũng sa mạc cằn cỗi Death Valley, bầu trời tím thẫm đe dọa, cảm giác cô lập tận thế hoang tưởng.",
        "prompt": "Bleak barren vista of jagged rocky canyon walls in Death Valley at twilight, deep purple and charcoal storm clouds gathering above parched cracked earth, entrance to a subterranean desert cavern hideout in shadow, apocalyptic delusion metaphor, graphic novel noir."
    },
    {
        "name": "t9_recording_studio_rejected_demo",
        "act": 2,
        "sentences": "2.09#1–#2",
        "desc": "Băng cối thu âm âm nhạc reel-to-reel bị bỏ quên trên bàn trộn âm thanh phòng thu, bản nhạc viết tay bị vò nát.",
        "prompt": "Still life in a dimly lit 1960s Hollywood sound recording booth, reel-to-reel magnetic tape machine sitting silent, crumpled handwritten sheet music scattered across audio mixing console, harsh shadow, wounded narcissistic pride, noir cinematography."
    },
    {
        "name": "t9_cielo_drive_road_sign_shadow",
        "act": 2,
        "sentences": "2.09#3–#4",
        "desc": "Biển báo đường Cielo Drive trong đêm tối, đèn pha xe hơi rọi qua bóng cây cọ cao vút, không khí định mệnh.",
        "prompt": "Vintage green enamel Los Angeles street signpost reading in retro typography under sweep of car headlights, dark towering eucalyptus and palm tree branches swaying in night wind, chilling sense of impending doom, graphic novel noir style."
    },
    {
        "name": "t9_midnight_convoy_old_ford",
        "act": 2,
        "sentences": "2.10#1–#3",
        "desc": "Chiếc xe Ford 1959 cũ kỹ màu vàng nhạt lăn bánh trong đêm trên con đường vắng lặng tiến về phía đồi Hollywood.",
        "prompt": "A weathered vintage 1959 Ford sedan driving silently along a winding empty two-lane canyon road at midnight, dim yellow headlamps cutting through darkness, silhouetted occupants inside, heavy ink linework, sinister nocturnal journey."
    },
    {
        "name": "t9_broken_porcelain_doll_desert",
        "act": 2,
        "sentences": "2.11#1–#2",
        "desc": "Một con búp bê sứ trẻ thơ bị vỡ nửa gương mặt nằm nửa chìm trong cát sa mạc Spahn Ranch, ẩn dụ sự tha hóa tâm hồn.",
        "prompt": "Poignant macro shot of an antique vintage porcelain doll with a cracked face lying partially buried in coarse desert sand beside dry sagebrush, harsh raking morning sun casting stark shadows, visual metaphor for corrupted innocence, graphic novel ink."
    },

    # =========================================================================
    # HỒI 3: NGHỆ THUẬT XÓA BỎ BẢN NGÃ (CƠ CHẾ TẨY NÃO 3 GIAI ĐOẠN) (10:00 – 15:00)
    # =========================================================================
    {
        "name": "t9_yearbook_photos_shadow",
        "act": 3,
        "sentences": "3.02#1–#4",
        "desc": "Bốn khung ảnh kỷ yếu trung học vintage mờ nhạt trên bàn gỗ, các gương mặt bị bóng tối che khuất (V5), tương phản giữa vẻ hiền lành quá khứ và tội ác.",
        "prompt": "Forensic display of four vintage 1960s high school yearbook portrait frames lined up on a dark oak desk, the faces completely veiled in deep cast shadows according to strict V5 guidelines, neat graduation caps and church choir gowns visible in silhouette, tragic contrast."
    },
    {
        "name": "t9_shadow_devil_dialogue_noir",
        "act": 3,
        "sentences": "3.02#5–#6",
        "desc": "Bóng đen dài in trên bức tường bê tông trắng, hai bàn tay buông thõng, ánh sáng đối lập chiaroscuro tột cùng.",
        "prompt": "Dramatic chiaroscuro composition of an ominous human silhouette cast large against a bare textured white wall, arms hanging limp, razor-sharp edge contrast between pitch ink black and stark pale wall, cold chilling psychological menace, graphic novel noir."
    },
    {
        "name": "t9_kurt_lewin_three_stages_diagram",
        "act": 3,
        "sentences": "3.03#1–#2",
        "desc": "Sơ đồ kỹ thuật ba giai đoạn (Unfreezing -> Changing -> Refreezing) vẽ bằng phấn trắng trên nền bảng đen điều tra.",
        "prompt": "Forensic conceptual blackboard illustration depicting Kurt Lewin's three-stage social psychology model (Unfreezing, Changing, Refreezing), stylized geometric arrows and molecular breaking bonds chalked in crisp white lines, dim overhead spotlight, academic noir analysis."
    },
    {
        "name": "t9_unfreezing_love_bombing_circle",
        "act": 3,
        "sentences": "3.04#1–#4",
        "desc": "Vòng tròn các bóng người quây quần trong ánh sáng ấm áp giả tạo, cánh tay ôm vai an ủi, chiếc bẫy cảm xúc ban đầu.",
        "prompt": "Intimate circle of silhouetted youths huddled together in a cozy amber-lit room, embracing shoulders in an overwhelming show of manufactured affection, long soft shadows extending outward into surrounding pitch-black darkness, emotional entrapment metaphor."
    },
    {
        "name": "t9_burning_id_cards_ashes",
        "act": 3,
        "sentences": "3.05#1–#3",
        "desc": "Chiếc ví rỗng, chứng minh thư và hộ chiếu đang cháy dở thành tro trong chiếc chảo kim loại, làn khói mảnh bốc lên.",
        "prompt": "Macro still life of vintage paper driver's licenses, personal social security cards, and leather wallets burning down to gray curling ashes inside an old cast-iron skillet, glowing orange embers, thin wisps of smoke rising into darkness, deliberate identity stripping."
    },
    {
        "name": "t9_lsd_hallucinogen_distorted_reality",
        "act": 3,
        "sentences": "3.05#4–#5",
        "desc": "Không gian sa mạc ảo giác u uất với các đường xoắn ốc psychedelic đen trắng mờ ảo, cảm giác mất phương hướng và thực tại méo mó.",
        "prompt": "Abstract psychological noir scene of a desert landscape bending into disorienting warped geometric contours, swirling black-and-white optical lines distorting horizon and night sky, dissolution of ego and reality under hallucinogenic influence, graphic novel art."
    },
    {
        "name": "t9_changing_night_desert_sermon",
        "act": 3,
        "sentences": "3.06#1–#4",
        "desc": "Đống than hồng rực lửa giữa thung lũng đá đêm, bóng kẻ thuyết giáo đứng cao sừng sững, xung quanh là đám đông quỳ phục.",
        "prompt": "Nocturnal desert rock amphitheater lit only by a bed of glowing red embers, towering dark silhouette of an authoritarian preacher with outstretched arms casting enormous shadow across sandstone cliffs, subservient listener silhouettes below, powerful manipulation."
    },
    {
        "name": "t9_inverted_cross_moral_confusion",
        "act": 3,
        "sentences": "3.07#1–#3",
        "desc": "Bức tượng gỗ nhỏ hoặc biểu tượng chữ thập mờ ảo ngả nghiêng trong bóng tối, ranh giới thiện ác bị xóa nhòa.",
        "prompt": "Still life of a small carved wooden cross leaning at an oblique inverted angle on an ancient stone altar, harsh cross-lighting creating conflicting double shadows, eerie philosophical subversion, graphic novel noir contrast."
    },
    {
        "name": "t9_blind_devotion_extinguished_candle",
        "act": 3,
        "sentences": "3.07#4–#5",
        "desc": "Ngọn nến bị chụp tắt bởi chiếc chuông kim loại, khói trắng bay lên, biểu tượng cho ánh sáng lý trí bị dập tắt.",
        "prompt": "Forensic close-up of a brass candle snuffer being lowered over a flickering white candle flame, sudden wisp of white smoke trailing upward into darkness, extinguishment of critical reason and human conscience, somber noir illustration."
    },
    {
        "name": "t9_interlocking_bloody_knots_rope",
        "act": 3,
        "sentences": "3.08#1–#2",
        "desc": "Đoạn dây thừng thắt nút phức tạp đặt trên phiến đá đen, biểu tượng của sự trói buộc không lối thoát.",
        "prompt": "Still life forensic shot of a thick hemp rope tied into a complex interlocking noose knot resting on a dark wet slate slab, harsh side raking spotlight, heavy texture and graphic noir ink shadows, irrevocable criminal entanglement metaphor."
    },
    {
        "name": "t9_trauma_bonding_group_shadows",
        "act": 3,
        "sentences": "3.09#1–#4",
        "desc": "Hàng bóng đen đứng xếp liền kề nhau như một khối thống nhất không thể tách rời dưới ánh đèn đêm nghiệt ngã.",
        "prompt": "Row of solid black human silhouettes standing shoulder to shoulder in absolute geometric uniformity, their cast shadows merging into one single impenetrable dark mass across a cracked concrete floor, trauma bonding and collective moral surrender."
    },
    {
        "name": "t9_gate_of_spahn_ranch_departure",
        "act": 3,
        "sentences": "3.10#1–#2",
        "desc": "Cánh cổng gỗ Spahn Ranch mở toang trong đêm tối, vệt bánh xe hằn sâu trên cát dẫn vào bóng đêm vô tận.",
        "prompt": "Looking outward from within Spahn Ranch through a wide-open rustic timber gate into the pitch-black abyss of night, deep parallel tire tracks grooved into dry dirt roadway, lone red taillight glow fading in the far distance, threshold of no return."
    },

    # =========================================================================
    # HỒI 4: LỜI KHAI TRƯỚC TÒA VÀ CÁI BẪY QUYỀN LỰC CỦA KẺ KHÔNG CHẠM TAY (15:00 – 20:00)
    # =========================================================================
    {
        "name": "t9_death_valley_barker_ranch_raid",
        "act": 4,
        "sentences": "4.02#1–#2",
        "desc": "Căn nhà gỗ hoang sơ Barker Ranch giữa lòng chảo thung lũng Death Valley cằn cỗi, xe tuần tra bao vây trong ánh bình minh đỏ quạch.",
        "prompt": "Dawn raid at the remote stone and wood cabin of Barker Ranch nestled in a desolate rocky ravine of Death Valley, California Highway Patrol and sheriff vehicles forming a defensive perimeter, dust plumes glowing in the harsh early morning desert sun."
    },
    {
        "name": "t9_sybil_brand_jail_corridor",
        "act": 4,
        "sentences": "4.03#1–#3",
        "desc": "Hành lang nhà tù nữ Sybil Brand Institute lát gạch sáng loáng dưới đèn tuýp trắng lạnh lẽo, những cánh cửa thép có ô kính nhỏ.",
        "prompt": "Clinical one-point perspective down the polished institutional corridor of Sybil Brand Institute for Women, cold overhead fluorescent tubes reflecting off slick green linoleum floors, heavy painted steel cell doors with observation slits, grim echo of confinement."
    },
    {
        "name": "t9_linda_kasabian_witness_dossier",
        "act": 4,
        "sentences": "4.04#1–#2",
        "desc": "Hồ sơ nhân chứng được bảo vệ đặc biệt của Văn phòng Công tố, tấm ảnh mờ và bản thỏa thuận miễn trừ truy tố.",
        "prompt": "Official legal dossier folder stamped STATE'S EVIDENCE - IMMUNITY AGREEMENT resting on a wooden legal conference table, fountain pen with dried blue ink beside legal transcript pages, dramatic banker lamp illumination, high-stakes judicial turning point."
    },
    {
        "name": "t9_cielo_drive_front_gate_fog",
        "act": 4,
        "sentences": "4.05#1–#3",
        "desc": "Cánh cổng sắt lớn của biệt thự Cielo Drive nhìn từ ngoài đường lúc nửa đêm, sương mù dày đặc, ánh đèn pha mờ ảo.",
        "prompt": "View from the roadside looking toward the closed entrance gate of 10050 Cielo Drive at midnight, heavy coastal mist swirling through pine branches, distant blurred taillights, tense breathless silence of a lookout witness."
    },
    {
        "name": "t9_vacant_eyes_doll_shadow",
        "act": 4,
        "sentences": "4.05#4–#6",
        "desc": "Bóng người đứng sững trong đêm tối, ánh trăng chiếu xiên qua khung cửa, biểu tượng cho ánh mắt vô hồn đánh mất bản ngã.",
        "prompt": "Haunting psychological noir illustration of human silhouettes with vacant unseeing profiles, sharp moonlight outlining mechanical marionette-like postures, emotional detachment and the terrifying loss of personal soul, deep ink chiaroscuro."
    },
    {
        "name": "t9_kasabian_escape_night_highway",
        "act": 4,
        "sentences": "4.05#7–#9",
        "desc": "Tuyến đường cao tốc đêm vắng lặng nhìn qua kính chắn gió ô tô trong cơn mưa phùn, ánh đèn hậu đỏ nhạt xa dần.",
        "prompt": "View through a rainy car windshield driving down a dark empty California highway at night, wipers smearing streaks across wet glass, distant glowing red taillights vanishing into darkness, desperate escape from psychological enslavement."
    },
    {
        "name": "t9_los_angeles_hall_of_justice",
        "act": 4,
        "sentences": "4.07#1–#4",
        "desc": "Mặt tiền đồ sộ của Tòa thị chính và Tòa án Los Angeles (Hall of Justice), bậc thang đá rộng lớn nơi báo chí và đám đông chen chúc.",
        "prompt": "Monumental low-angle shot of the granite neoclassical facade of the Los Angeles Hall of Justice, imposing limestone columns under a gray overcast California sky, sea of press camera tripods and silhouettes gathered at the wide entrance steps."
    },
    {
        "name": "t9_prosecutor_desk_evidence_files",
        "act": 4,
        "sentences": "4.08#1–#4",
        "desc": "Bàn công tố viên chất đầy các hộp hồ sơ án, bản sao dấu vân tay và hình vẽ hiện trường, chiếc cặp da cũ kỹ.",
        "prompt": "Forensic close-up of Prosecutor Vincent Bugliosi's courtroom desk, towering stacks of trial binders, cardboard evidence boxes, yellow legal pads filled with meticulous handwritten cross-examination notes, warm incandescent reading light."
    },
    {
        "name": "t9_mastermind_conspiracy_law_book",
        "act": 4,
        "sentences": "4.09#1–#3",
        "desc": "Cuốn sách luật hình sự California mở trên bàn, ngòi bút máy kim loại trỏ vào điều khoản về tội danh đồng phạm chủ mưu.",
        "prompt": "An open leather-bound California Penal Code volume resting under a brass table lamp, fountain pen pointing toward legal sections on Conspiracy to Commit Murder and Mastermind Liability, profound historic judicial landmark."
    },
    {
        "name": "t9_carved_x_symbol_forehead",
        "act": 4,
        "sentences": "4.10#1–#3",
        "desc": "Tác phẩm đồ họa noir cận cảnh vết chữ X khắc gạch thô ráp trên nền đá xám tối tăm, biểu tượng sự từ chối chuẩn mực xã hội loài người.",
        "prompt": "Abstract graphic novel noir still life of a rough-hewn letter 'X' carved deeply into a cracked slate surface, raking harsh side lighting highlighting chipped edges and deep ink shadows, symbolic rejection of civilized human society."
    },
    {
        "name": "t9_collective_hysteria_three_shaved_heads",
        "act": 4,
        "sentences": "4.10#4–#6",
        "desc": "Ba bóng người phụ nữ cạo trọc đầu nắm tay nhau bước đi trong ánh đèn flash báo chí, nụ cười méo mó kỳ quái trong bóng tối.",
        "prompt": "Silhouetted profiles of three young women with shaven heads walking hand-in-hand down a courthouse hallway, blinding paparazzi flashbulbs bursting in background creating stark high-contrast chiaroscuro, disturbing collective hysteria and denial."
    },
    {
        "name": "t9_courtroom_gavel_bench",
        "act": 4,
        "sentences": "4.11#1–#2",
        "desc": "Bục thẩm phán trang nghiêm bằng gỗ sồi sẫm màu, chiếc búa gỗ nằm im lìm trên đĩa gõ, ánh sáng cửa sổ rọi xuống tĩnh lặng.",
        "prompt": "Dignified low-angle shot of Judge Charles Older's elevated oak bench in a 1970 Los Angeles courtroom, dark wood grain, solid wooden gavel resting beside brass sound block, high arched courtroom window casting authoritative beams of daylight."
    },

    # =========================================================================
    # HỒI 5: PHÁN QUYẾT LỊCH SỬ & BÀI HỌC VỀ SỰ TỰ CHỦ TINH THẦN (20:00 – 26:00)
    # =========================================================================
    {
        "name": "t9_courtroom_jury_verdict_dossier",
        "act": 5,
        "sentences": "5.02#1–#2",
        "desc": "Bản phán quyết của bồi thẩm đoàn có chữ ký các thành viên, con dấu đỏ tư pháp bang California, ánh sáng trang trọng.",
        "prompt": "Official certified jury verdict document resting on a polished courtroom desk, red embossed seal of the Superior Court of California, signed jury foreperson lines, solemn dignified justice, graphic novel noir linework."
    },
    {
        "name": "t9_california_supreme_court_columns",
        "act": 5,
        "sentences": "5.02#3–#4",
        "desc": "Hàng cột đá cẩm thạch uy nghiêm của Tòa án Tối cao California tại San Francisco, biểu tượng cho sự thay đổi lịch sử pháp luật.",
        "prompt": "Stately architectural view of the classical granite pillars and pediment of the California Supreme Court building in San Francisco, dramatic raking dawn sunlight, long stately shadows, landmark jurisprudence in People v. Anderson."
    },
    {
        "name": "t9_corcoran_state_prison_watchtower",
        "act": 5,
        "sentences": "5.02#5–#6",
        "desc": "Tháp canh và hàng rào kẽm gai của Nhà tù Tiểu bang Corcoran dưới ánh chiều tà hoang vắng, bóng chim bay cô độc.",
        "prompt": "Exterior perimeter of California State Prison Corcoran at desolate sunset, tall steel guard tower with searchlights silhouetted against an amber-orange horizon, multiple rows of razor wire fencing stretching into distance, solitary flight of a hawk."
    },
    {
        "name": "t9_scales_of_justice_broken_chains",
        "act": 5,
        "sentences": "5.03#1–#3",
        "desc": "Cán cân công lý bằng đồng sáng rực trên nền xích sắt bị đứt gãy, biểu tượng công lý chiến thắng sự thao túng tà giáo.",
        "prompt": "Symbolic composition of polished brass scales of justice balanced perfectly on a black marble pedestal, shattered heavy iron chain links lying broken below, dramatic raking spotlight, triumph of rule of law over mental coercion."
    },
    {
        "name": "t9_two_faced_benevolent_mask",
        "act": 5,
        "sentences": "5.04#1–#3",
        "desc": "Chiếc mặt nạ mỉm cười hiền từ bằng sứ nứt đôi, để lộ một góc tối tăm u ám phía sau, ẩn dụ cho sự thấu hiểu giả tạo.",
        "prompt": "Conceptual surreal still life of a porcelain theatrical smiling mask cracked down the center, one side radiating warm comforting benevolence while the other side is swallowed in sinister obsidian shadows, psychological warning of predatory charm."
    },
    {
        "name": "t9_redflag1_love_bombing_trap",
        "act": 5,
        "sentences": "5.05#2–#4",
        "desc": "Red Flag 1 (Dội bom tình cảm): Chiếc hộp quà phủ ruy băng nhung lộng lẫy đặt mở hé trong bóng tối, bên trong ẩn chứa chiếc bẫy thép gai vô hình.",
        "prompt": "Red Flag 1 - Love Bombing: An ornate velvet gift box tied with shimmering satin ribbon sitting slightly open in dark shadow, inside revealing cold sharp thorny brambles gleaming in a sliver of light, perilous emotional dependency metaphor."
    },
    {
        "name": "t9_redflag2_severed_family_photos",
        "act": 5,
        "sentences": "5.05#5–#7",
        "desc": "Red Flag 2 (Tước đoạt danh tính & cô lập): Bức ảnh gia đình chụp kỷ niệm bị rạch đôi, một nửa bị kéo ra xa trong góc tối, chiếc kéo kim loại sắc lạnh bên cạnh.",
        "prompt": "Red Flag 2 - Identity Stripping: A cherished vintage family photograph cleanly severed in two on a wooden surface, one half pushed into deep darkness, sharp stainless steel shears resting beside it, psychological isolation warning."
    },
    {
        "name": "t9_redflag3_fortress_paranoia_wall",
        "act": 5,
        "sentences": "5.05#8–#10",
        "desc": "Red Flag 3 (Tư duy phân cực Chúng ta vs Thế giới): Bức tường bê tông cao ngất ngăn cách hai thế giới, một bên u tối khép kín, một bên là chân trời rộng mở.",
        "prompt": "Red Flag 3 - Us vs Them Polarization: A monolithic imposing brutalist concrete wall dividing the frame, left side shrouded in paranoid pitch darkness and barbed wire, right side looking toward an open horizon with rising dawn light."
    },
    {
        "name": "t9_redflag4_sacred_conscience_compass",
        "act": 5,
        "sentences": "5.05#11–#13",
        "desc": "Red Flag 4 (Lương tri bất khả xâm phạm): Chiếc la bàn lương tri bằng vàng phản chiếu ánh sáng kiên định giữa cơn lốc cát bụi sa mạc tối tăm.",
        "prompt": "Red Flag 4 - Inviolable Conscience: A glowing antique brass navigational compass held steady on a dark stone pedestal, magnetic needle pointing true north despite swirling dark desert dust around it, moral compass and integrity."
    },
    {
        "name": "t9_open_birdcage_dawn_horizon",
        "act": 5,
        "sentences": "5.05#14–#15",
        "desc": "Chiếc lồng chim kim loại cửa mở toang, một chú chim vỗ cánh bay vút lên bầu trời bình minh rực rỡ, ánh sáng vàng ấm áp xua tan đêm dài.",
        "prompt": "Poetic wide shot of an ornate antique iron birdcage sitting with its door swung wide open on a high promontory, a bird in flight soaring toward a luminous golden sunrise over the ocean horizon, true mental freedom and personal agency."
    },
    {
        "name": "t9_amber_eyes_closing_dossier",
        "act": 5,
        "sentences": "5.05#16–#18",
        "desc": "Hồ sơ vụ án đóng lại trên bàn gỗ sồi, chiếc kính lúp và ngòi bút mực amber vàng kim, biểu trưng cho sự thật và tri thức nhân văn.",
        "prompt": "Official closing case dossier labeled AMBER EYES DOSSIER 09 neatly closed on a dark polished oak desk, brass magnifying glass and gold fountain pen beside it, warm amber ambient light, dignified documentary finale, graphic novel noir."
    }
]

# Write bg_jobs_tap09.json
bg_jobs_path = WORK / "bg_jobs_tap09.json"
bg_jobs_path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Created {bg_jobs_path} with {len(jobs)} background jobs!")

# Write gemini_image_prompts_tap09.json
gemini_prompts = []
STYLE_PREFIX = ("Cinematic 16:9 wide shot, dark graphic novel noir illustration, bold black ink linework, "
                "deep chiaroscuro lighting, subtle mist and film grain, desaturated muted palette, ominous quiet tension, highly detailed. ")
NEG_SUFFIX = (" Strictly no text, no letters, no words, no numbers, no signs, no labels, no logos, "
              "no watermark, no frame, no letterbox bars, full-bleed image.")

for j in jobs:
    gemini_prompts.append({
        "name": j["name"],
        "target_file": f"assets/bg/{j['name']}.png",
        "aspect_ratio": "16:9",
        "prompt": f"{STYLE_PREFIX}{j['prompt']}{NEG_SUFFIX}"
    })

gemini_path = WORK / "gemini_image_prompts_tap09.json"
gemini_path.write_text(json.dumps(gemini_prompts, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Created {gemini_path} with {len(gemini_prompts)} Gemini/Imagen prompts!")
