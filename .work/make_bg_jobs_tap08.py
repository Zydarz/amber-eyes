import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

jobs = [
    # =========================================================================
    # HỒI 1: BUỔI SÁNG ĐỊNH MỆNH DƯỚI LÒNG ĐẤT TOKYO (00:00 – 05:00)
    # =========================================================================
    {
        "name": "t8_tokyo_dawn_fog",
        "act": 1,
        "sentences": "1.02#1",
        "desc": "Bầu trời Tokyo sáng sớm ngày 20/03/1995 mờ sương lạnh lẽo, những tòa nhà cao tầng chìm trong bóng tối chiaroscuro.",
        "prompt": "Cinematic wide shot of Tokyo skyline on a cold overcast morning in March 1995, misty pre-dawn fog swirling between brutalist office towers and distant telecommunication antennas, dark graphic novel noir aesthetic, deep chiaroscuro contrast, desaturated slate-blue and charcoal palette, atmospheric film grain, solitude."
    },
    {
        "name": "t8_commuter_crowd_station",
        "act": 1,
        "sentences": "1.02#2–#3",
        "desc": "Dòng người hối hả giờ cao điểm đổ dồn xuống cửa ga tàu điện ngầm Tokyo, bóng người đen dài trên nền gạch lát sáng loáng.",
        "prompt": "Low-angle dynamic shot of commuter silhouettes flowing down tiled stairs into a Tokyo subway station entrance, long dark cast shadows on wet polished tiles, overhead fluorescent signs casting stark linear light pools, vintage 1990s Japanese commuters with coats and umbrellas, graphic novel noir linework."
    },
    {
        "name": "t8_subway_tracks_perspective",
        "act": 1,
        "sentences": "1.02#4",
        "desc": "Phối cảnh sâu hun hút vào đường hầm ngầm của 3 tuyến tàu Chiyoda, Marunouchi và Hibiya, đường ray thép lấp loáng dưới đèn báo hiệu.",
        "prompt": "Deep one-point perspective looking into a dark Tokyo underground subway tunnel, twin polished steel rails gleaming under distant signal lanterns, arched concrete tunnel walls with heavy conduits and electrical cabling, eerie quiet tension, cold teal and yellow signal lights piercing pitch darkness."
    },
    {
        "name": "t8_kasumigaseki_facade",
        "act": 1,
        "sentences": "1.02#5–#6",
        "desc": "Mặt tiền uy nghiêm của khu phức hợp các Bộ ngành chính phủ tại Kasumigaseki trong ánh ban mai xám xịt.",
        "prompt": "Imposing low-angle shot of the massive stone facade of the Kasumigaseki government ministry headquarters in central Tokyo, stark granite pillars and monolithic institutional architecture under an ominous pale gray morning sky, empty asphalt plaza, deep chiaroscuro shadow."
    },
    {
        "name": "t8_newspaper_wrapped_package",
        "act": 1,
        "sentences": "1.04#1–#2",
        "desc": "Tĩnh vật bọc giấy báo chứa túi nylon bí mật đặt cạnh chân ghế toa tàu, góc chụp thấp noir căng thẳng.",
        "prompt": "Forensic close-up still life of an inconspicuous bundle wrapped in Japanese newspaper sitting quietly beneath an olive-green vinyl subway carriage seat, clear plastic lining peeking out from torn newsprint, directional beam of fluorescent light, cold noir atmosphere, high detail."
    },
    {
        "name": "t8_chemical_structure_sarin",
        "act": 1,
        "sentences": "1.04#3",
        "desc": "Bản vẽ cấu trúc phân tử chất độc Sarin mờ ảo trên nền bảng đen kỹ thuật hình sự, ánh sáng xanh lạnh ma mị.",
        "prompt": "Forensic technical diagram of the chemical molecular structure of Sarin nerve agent drawn in faint white chalk on a dark laboratory blackboard, phosphorescent cold cyan backlighting, scientific formulas and molecular bonds glowing in darkness, somber investigative noir illustration."
    },
    {
        "name": "t8_umbrella_puncture_action",
        "act": 1,
        "sentences": "1.04#4–#5",
        "desc": "Cận cảnh đầu nhọn chiếc ô kim loại đâm thủng lớp màng bọc nylon, giọt chất lỏng trong suốt rỉ ra sàn tàu.",
        "prompt": "Macro shot of a sharpened metallic black umbrella tip piercing a translucent plastic bag on a ribbed linoleum train carriage floor, a clear droplet of chemical liquid beading on the edge, dramatic raking spotlight, tense noir graphic storytelling, no gore."
    },
    {
        "name": "t8_train_doors_closing",
        "act": 1,
        "sentences": "1.04#6",
        "desc": "Cửa toa tàu điện ngầm đóng sập lại, bóng phản chiếu mờ ảo trên kính toa xe khi đoàn tàu lao vào hầm tối.",
        "prompt": "Subway carriage sliding stainless steel doors slamming shut, blurred distorted reflections in the glass windows as the metallic train accelerates into the dark tunnel, yellow warning stripes on platform edge, motion blur, heavy ink shadows, noir cinematography."
    },
    {
        "name": "t8_subway_car_mist_vapor",
        "act": 1,
        "sentences": "1.06#1–#2",
        "desc": "Toa tàu đông đúc với làn hơi độc vô hình bay là là trên sàn, ánh đèn neon nhấp nháy tạo bầu không khí ngột ngạt nghẹt thở.",
        "prompt": "Interior perspective of an empty retro Tokyo metro car with rows of green bench seats and metal handrails, faint atmospheric hazy vapor creeping across the ribbed floor tiles, flickering overhead fluorescent tubes, eerie green-tinted chiaroscuro, claustrophobic dread."
    },
    {
        "name": "t8_subway_platform_tunnel_dark",
        "act": 1,
        "sentences": "1.07#1–#2",
        "desc": "Sân ga ngầm u tối nhìn sâu vào lòng hầm hun hút, ánh đèn vàng mờ nhạt, cảm giác ngột ngạt và mù lòa của nạn nhân.",
        "prompt": "A subterranean subway station platform shrouded in thick darkness, station lights suddenly cutting to dim amber emergency strips, deep receding blackness swallowing the platform columns, graphic novel noir art style, oppressive sensory deprivation, solitary atmosphere."
    },
    {
        "name": "t8_dropped_novel_glasses",
        "act": 1,
        "sentences": "1.07#3–#4",
        "desc": "Cuốn tiểu thuyết bỏ dở và chiếc kính mắt gọng kim loại vỡ nứt rơi trên sàn gạch sân ga, tĩnh lặng lạnh gáy.",
        "prompt": "Still-life forensic shot of an abandoned paperback Japanese novel and a pair of broken wire-rimmed reading glasses lying on cold white station floor tiles, harsh directional light casting razor-sharp shadows, profound poignant tragedy, graphic novel noir ink."
    },
    {
        "name": "t8_subway_stairs_escape",
        "act": 1,
        "sentences": "1.07#5–#6",
        "desc": "Cầu thang gạch men dẫn từ ga ngầm lên mặt đất, các bóng đen hoảng loạn bò tìm lối thoát trong ánh sáng yếu ớt.",
        "prompt": "Steep tiled pedestrian stairway leading upward from subway depths toward street level, stark silhouetted forms scrambling toward daylight, harsh side-lighting accentuating steps and handrails, dramatic black ink chiaroscuro, desperate escape metaphor."
    },
    {
        "name": "t8_subway_exit_sunlight",
        "act": 1,
        "sentences": "1.07#7–#8",
        "desc": "Góc nhìn từ chân lối thoát ga ngầm hướng lên ánh sáng chói lòa của buổi sáng Tokyo, biểu tượng của sự sống sót và bàng hoàng.",
        "prompt": "Looking straight up from the dark bottom of a subway stairwell exit toward a blinding pale morning sky, stark geometric silhouette of the concrete opening framing the outside city, dust particles floating in the light shaft, stark contrast of light and darkness."
    },
    {
        "name": "t8_ambulances_tokyo_street",
        "act": 1,
        "sentences": "1.09#1–#2",
        "desc": "Đèn cứu thương đỏ rực nhấp nháy trên đường phố Tokyo xám xịt trong buổi sáng thảm họa, hàng dài xe khẩn cấp.",
        "prompt": "Long shot of a broad Tokyo boulevard lined with emergency response vehicles, red flashing beacon lights reflecting in wet morning asphalt, yellow barricade cones, silhouetted medical personnel in distance, somber rain-slicked noir atmosphere, dignified restraint."
    },
    {
        "name": "t8_hospital_triage_corridor",
        "act": 1,
        "sentences": "1.09#3–#4",
        "desc": "Hành lang cấp cứu bệnh viện dã chiến với các bình dưỡng khí và cột truyền dịch xếp dài, chiaroscuro xanh lạnh.",
        "prompt": "Hospital emergency corridor in stark chiaroscuro lighting, rows of tall green steel oxygen cylinders and IV drip stands lined against white tiled walls, harsh clinical blue-gray tones, empty gurneys in deep shadows, solemn medical atmosphere."
    },
    {
        "name": "t8_tokyo_police_hq",
        "act": 1,
        "sentences": "1.10#1–#2",
        "desc": "Trụ sở Cơ quan Cảnh sát Quốc gia Nhật Bản (Keishicho) uy nghiêm trong đêm điều tra khẩn cấp, xe tuần tra nhấp nháy đèn.",
        "prompt": "Exterior view of the Tokyo Metropolitan Police Department (Keishicho) headquarters building at dusk, monolithic modern fortress with lit office windows against a stormy purple-black sky, parked black-and-white patrol cruisers with dim lights, serious investigative weight."
    },
    {
        "name": "t8_incident_board_map",
        "act": 1,
        "sentences": "1.10#3–#4",
        "desc": "Bản đồ mạng lưới tàu điện ngầm Tokyo trong phòng tác chiến cảnh sát với các mốc đỏ đánh dấu các ga bị tấn công.",
        "prompt": "A sprawling tactical police wall map of the Tokyo metropolitan subway grid, intricate colored transit lines crisscrossing a dark grid, red circular markers highlighting Kasumigaseki, Tsukiji, and Kamiyacho stations, forensic notes pinned beside it, dim briefing room lighting."
    },
    {
        "name": "t8_aum_shinrikyo_emblem_shadow",
        "act": 1,
        "sentences": "1.11#1–#2",
        "desc": "Biểu tượng chữ Phạn bí truyền của giáo phái Aum Shinrikyo chìm trong bóng tối bí ẩn, ánh sáng chiaroscuro đe dọa.",
        "prompt": "An embossed brass esoteric Sanskrit emblem of the Aum cult emerging from deep velvet darkness, a single razor-thin beam of amber light skimming across its intricate geometric curves, ominous religious mystery, dark graphic novel noir linework."
    },
    {
        "name": "t8_dossier_elite_scientists",
        "act": 1,
        "sentences": "1.11#3–#4",
        "desc": "Bìa hồ sơ điều tra chuyên án bí mật của cảnh sát Tokyo với danh sách các nhà khoa học tinh hoa bị nghi vấn.",
        "prompt": "Police investigative case dossier folder labeled with Japanese kanji stamped CONFIDENTIAL, sitting on a dark oak desk surrounded by university graduation registries and chemistry research journals, warm banker lamp casting dramatic circle of light."
    },

    # =========================================================================
    # HỒI 2: KHU CĂN CỨ DƯỚI CHÂN NÚI PHÚ SĨ VÀ PHÒNG THÍ NGHIỆM TỬ THẦN (05:00 – 10:00)
    # =========================================================================
    {
        "name": "t8_mount_fuji_dawn_somber",
        "act": 2,
        "sentences": "2.02#1–#2",
        "desc": "Núi Phú Sĩ sừng sững trong sương sớm u ám lạnh lẽo, những rặng thông đen bao quanh chân núi cô lập.",
        "prompt": "Majestic yet somber view of Mount Fuji towering in the distance, crowned with snow under a heavy overcast slate sky, sprawling dense dark pine forests of Kamikuishiki village shrouded in morning mist, evocative Japanese noir landscape painting, cold muted colors."
    },
    {
        "name": "t8_police_convoy_kamikuishiki",
        "act": 2,
        "sentences": "2.02#3",
        "desc": "Đoàn xe cảnh sát và đặc nhiệm phòng hóa rầm rộ nối đuôi nhau trên con đường làng Kamikuishiki vắng lặng.",
        "prompt": "A long convoy of dark police riot buses and specialized Hazmat vehicles snaking along a narrow winding rural road beneath Mount Fuji at dawn, bare winter trees flanking the asphalt, flashing silent blue beacons, determined law enforcement mobilization."
    },
    {
        "name": "t8_hazmat_officers_formation",
        "act": 2,
        "sentences": "2.02#4–#5",
        "desc": "Đội hình đặc nhiệm cảnh sát trong trang phục phòng chống vũ khí hóa học và mặt nạ dưỡng khí tiến vào căn cứ.",
        "prompt": "Silhouetted formation of tactical police officers in full chemical Hazmat suits and respiratory gas masks advancing in tight discipline, reflective visors mirroring the gray morning light, heavy boots on gravel, graphic novel noir illustration."
    },
    {
        "name": "t8_satyam_compound_aerial",
        "act": 2,
        "sentences": "2.04#1–#2",
        "desc": "Quần thể Satyam gồm những khối nhà bê tông thô ráp xám xịt, hàng rào thép gai và tháp quan sát canh phòng cẩn mật.",
        "prompt": "Atmospheric wide establishing view of the sprawling Satyam compound, multiple utilitarian gray concrete warehouse blocks encircled by high chain-link fences and barbed wire, surveillance cameras mounted on steel poles, bleak oppressive compound under overcast sky."
    },
    {
        "name": "t8_satyam_7_exterior",
        "act": 2,
        "sentences": "2.04#3–#4",
        "desc": "Mặt ngoài tòa nhà Satyam số 7 không cửa sổ, các ống thông gió công nghiệp khổng lồ chạy ngoằn ngoèo trên tường.",
        "prompt": "Brutalist windowless exterior of Satyam Building No. 7, massive cylindrical industrial ventilation ducts and steel scrubbers snaking up the raw concrete facade, armored steel entry doors, heavy industrial secret factory vibe, dark chiaroscuro."
    },
    {
        "name": "t8_chemical_plant_reactor",
        "act": 2,
        "sentences": "2.05#1–#2",
        "desc": "Dàn tháp phản ứng và máy móc tổng hợp hóa chất hữu cơ bằng thép không gỉ sáng bóng bên trong Satyam số 7.",
        "prompt": "Interior of a covert industrial chemical manufacturing facility, multi-story stainless steel distillation towers, cylindrical reaction kettles, complex maze of polished pipes, pressure gauges and control consoles gleaming under cold sodium lighting, high detail noir."
    },
    {
        "name": "t8_chemical_precursor_drums",
        "act": 2,
        "sentences": "2.05#3–#4",
        "desc": "Hàng trăm thùng phi chứa hóa chất tiền chất độc hại xếp chồng trên pallet gỗ trong kho ngầm, ánh đèn neon lạnh.",
        "prompt": "Rows upon rows of 55-gallon industrial steel chemical drums stacked on wooden pallets inside a cavernous concrete underground warehouse, diamond hazmat warning symbols, puddle of condensate reflecting fluorescent tubes, forensic investigative atmosphere."
    },
    {
        "name": "t8_sarin_synthesis_laboratory",
        "act": 2,
        "sentences": "2.06#1",
        "desc": "Phòng thí nghiệm chưng cất hóa chất với bình cầu thủy tinh, ống sinh hàn và đồng hồ đo áp suất tinh vi.",
        "prompt": "Close-up of clandestine chemical synthesis apparatus: borosilicate round-bottom flasks with bubbling condensation tubes, coiled spiral glass condensers, digital temperature readouts in cold red LEDs, amber reagent bottles, dark scientific noir lighting."
    },
    {
        "name": "t8_bio_incubator_pathogens",
        "act": 2,
        "sentences": "2.06#2",
        "desc": "Tủ ủ vô trùng nuôi cấy vi sinh vật ngầm dán nhãn vi khuẩn bệnh Than và Botulinum trong ánh đèn tím khử trùng.",
        "prompt": "Underground biological containment laboratory, stainless steel incubator cabinets with glass inspection doors illuminated by eerie ultraviolet germicidal lamps, sealed Petri dishes, biohazard warning placards, sterile clinical horror."
    },
    {
        "name": "t8_mi17_helicopter_hangar",
        "act": 2,
        "sentences": "2.06#3–#4",
        "desc": "Chiếc trực thăng quân sự Mi-17 xám bạc đậu im lìm trong hangar tối om, cánh quạt khổng lồ rủ bóng nặng nề.",
        "prompt": "A massive Soviet-built Mi-17 military transport helicopter parked silently inside a dark corrugated metal hangar, heavy five-blade rotor casting long linear shadows across the concrete floor, single overhead bulb illuminating the nose and cockpit windows."
    },
    {
        "name": "t8_matsumoto_night_1994",
        "act": 2,
        "sentences": "2.07#1–#2",
        "desc": "Con phố dân cư tĩnh mịch tại Matsumoto đêm mùa hè 1994, sương mờ bao phủ chiếc xe tải cải tiến bí ẩn.",
        "prompt": "A quiet residential street in Matsumoto Nagano on a moonlit summer night in 1994, traditional Japanese tiled-roof houses behind low garden walls, faint ground fog rolling along asphalt, silhouette of an anonymous customized refrigerated delivery van, eerie stillness."
    },
    {
        "name": "t8_matsumoto_court_dossier",
        "act": 2,
        "sentences": "2.07#3",
        "desc": "Hồ sơ tài liệu vụ kiện đất đai của giáo phái tại Tòa án Matsumoto nằm dưới ánh đèn bàn làm việc ban đêm.",
        "prompt": "Legal judicial case files tied with ribbon, Japanese court seals stamped on aged Manila folders labeled Matsumoto Land Dispute, resting on a dark walnut judge's bench under an emerald green banker's lamp, dramatic chiaroscuro."
    },
    {
        "name": "t8_sakamoto_lawyer_desk",
        "act": 2,
        "sentences": "2.08#1–#2",
        "desc": "Bàn làm việc vắng bóng người của Luật sư Sakamoto tại văn phòng Yokohama, tập tài liệu bảo vệ nạn nhân và điện thoại rơi.",
        "prompt": "An empty vintage wooden desk in a Yokohama legal aid office, client case files scattered across the surface, an analog rotary telephone off the hook, a warm desk lamp casting an amber glow on empty chairs, poignant silence, dignified sacrifice."
    },
    {
        "name": "t8_mountain_grave_memorial",
        "act": 2,
        "sentences": "2.08#3",
        "desc": "Khung cảnh rừng thông miền núi Gunma mù sương nơi hài cốt gia đình luật sư dũng cảm được tìm thấy, trang nghiêm đượm buồn.",
        "prompt": "A remote misty mountain ridge in Gunma prefecture, towering Japanese cedar trees shrouded in dense mountain fog, a simple wooden memorial marker placed respectfully in the mossy clearing, cold somber daylight filtering through the forest canopy."
    },
    {
        "name": "t8_weapons_of_mass_destruction",
        "act": 2,
        "sentences": "2.09#1–#2",
        "desc": "Tĩnh vật hình sự: Bình chứa khí nén kim loại, ống nghiệm vi sinh và tài liệu mật của giáo phái dưới đèn spotlight.",
        "prompt": "Forensic still life composition: Heavy steel gas cylinders, glass culture tubes, military aerial dispersal nozzles, and bound leather esoteric doctrine books arranged on an evidence collection table, clinical noir lighting, investigative gravity."
    },

    # =========================================================================
    # HỒI 3: NGHỊCH LÝ CỦA CÁC THIÊN TÀI KHOA HỌC (10:00 – 15:00)
    # =========================================================================
    {
        "name": "t8_asahara_shadow_profile",
        "act": 3,
        "sentences": "3.02#1–#3",
        "desc": "Bóng lưng và góc nghiêng của giáo chủ Shoko Asahara với mái tóc dài và râu rậm ngồi thiền trong bóng tối, không lộ mặt.",
        "prompt": "Silhouette of a bearded cult leader with long tangled hair sitting in full lotus meditation posture against deep velvet shadows, face completely obscured in darkness, only the outline backlit by a dim amber candle, psychological noir character portrait, rule V5 compliant."
    },
    {
        "name": "t8_todai_red_gate_shadow",
        "act": 3,
        "sentences": "3.02#4–#5",
        "desc": "Cổng Đỏ (Akamon) của Đại học Tokyo trong mưa chiều mùa đông u tối, biểu tượng cho cánh cửa học thuật đã khép lại với kẻ thất bại.",
        "prompt": "The iconic Akamon Red Gate of the University of Tokyo standing under a driving cold winter rain, aged crimson wooden pillars and tiled eaves glistening in twilight, bare elm branches, rejection and bitter academic ambition metaphor, noir atmosphere."
    },
    {
        "name": "t8_chinese_herbal_apothecary",
        "act": 3,
        "sentences": "3.02#6–#8",
        "desc": "Tủ thuốc bắc cổ kính bằng gỗ tối màu với các lọ thủy tinh đựng rễ cây và dược liệu đông y, quá khứ bán thuốc giả của giáo chủ.",
        "prompt": "Interior of an old traditional Chinese medicine and acupuncture shop, dusty dark wooden herb drawers with calligraphy labels, amber glass apothecary jars filled with dried roots and herbs, small brass balancing scale, moody nostalgic chiaroscuro."
    },
    {
        "name": "t8_devotion_altar_kneeling",
        "act": 3,
        "sentences": "3.03#1–#2",
        "desc": "Bóng những tín đồ thanh niên mặc áo choàng trắng quỳ rạp trước đài sen cao trong đại sảnh nghi lễ mờ khói nhang.",
        "prompt": "Spacious ritual meditation hall, deep shadows with rows of kneeling silhouettes in flowing white robes prostrating before an elevated lotus platform, curling trails of incense smoke catching golden light beams, complete surrender of intellect."
    },
    {
        "name": "t8_tsukuba_chemistry_lab",
        "act": 3,
        "sentences": "3.03#3",
        "desc": "Phòng thí nghiệm hóa hữu cơ Đại học Tsukuba với bảng đen chi chít công thức hóa học hữu cơ phân tử, ghế xoay trống vắng.",
        "prompt": "An elite university organic chemistry laboratory, blackboards covered with meticulous hand-drawn hydrocarbon rings and polymer synthesis equations, glassware and analytical balances on clean slate benches, empty leather chair, academic excellence."
    },
    {
        "name": "t8_cosmic_physics_observatory",
        "act": 3,
        "sentences": "3.03#4",
        "desc": "Đài thiên văn vật lý với kính viễn vọng lớn hướng lên bầu trời đêm đầy sao, biểu trưng cho sự nghiệp của nhà vật lý Hideo Murai.",
        "prompt": "Inside a majestic astronomical observatory dome, large optical telescope pointing up through the open slit toward a brilliant starry cosmos, chalkboard filled with cosmic ray and astrophysics equations, deep indigo and starlight tones."
    },
    {
        "name": "t8_virology_electron_microscope",
        "act": 3,
        "sentences": "3.03#5",
        "desc": "Kính hiển vi điện tử trong phòng nghiên cứu vi sinh của Đại học Y Kyoto, màn hình huỳnh quang xanh lục hiển thị cấu trúc virus.",
        "prompt": "High-tech medical virology laboratory, a transmission electron microscope unit with its phosphor green circular display showing intricate viral capsid structures, cold metallic surfaces, dim room lighting, clinical detachment."
    },
    {
        "name": "t8_cardiac_surgery_theatre",
        "act": 3,
        "sentences": "3.03#6–#7",
        "desc": "Phòng mổ tim mạch vô trùng hiện đại với dàn đèn phẫu thuật cực sáng chiếu xuống bàn mổ inox, sự nghiệp đỉnh cao của Bác sĩ Hayashi.",
        "prompt": "State-of-the-art cardiovascular operating theater, overhead surgical shadowless lamps casting brilliant circular pool of pure white light onto a pristine stainless steel operating table, heart-lung bypass machine in background, sterile noble vocation."
    },
    {
        "name": "t8_stethoscope_abandoned_drain",
        "act": 3,
        "sentences": "3.04#1–#2",
        "desc": "Chiếc ống nghe y tế của bác sĩ nằm vắt qua đường ống cống bê tông xám xịt trong căn cứ ngầm, sự tha hóa tột cùng.",
        "prompt": "Forensic visual metaphor: A gleaming medical stethoscope and white doctor's coat draped over a dirty rusted industrial pipe in a grime-stained concrete sewer vault, tragic fall from grace, intense chiaroscuro noir contrast."
    },
    {
        "name": "t8_tokyo_stock_crash_1990",
        "act": 3,
        "sentences": "3.05#1–#3",
        "desc": "Ẩn dụ kinh tế bong bóng sụp đổ: Các bảng điện tử chỉ số chứng khoán lao dốc phản chiếu trên mặt vũng nước mưa phố Tokyo.",
        "prompt": "Visual metaphor of Japan's 1990 bubble economy collapse: Tokyo financial district skyscrapers looming in darkness, digital stock ticker displays with plunging red arrows reflected in cold rain puddles on cracked sidewalk, existential disillusionment."
    },
    {
        "name": "t8_corporate_salaryman_cogs",
        "act": 3,
        "sentences": "3.05#4–#5",
        "desc": "Không gian văn phòng công ty Nhật Bản những năm 90 với hàng dãy bàn làm việc giống hệt nhau, áp lực đè nặng bánh răng cỗ máy xã hội.",
        "prompt": "Vast monochrome Tokyo corporate office floor at 10 PM, endless rows of identical gray cubicles under harsh fluorescent tubes, small silhouetted office workers hunched over mountains of paperwork, alienation and existential vacuum."
    },
    {
        "name": "t8_yoga_meditation_incense",
        "act": 3,
        "sentences": "3.06#1–#4",
        "desc": "Phòng tập yoga và thiền Aum Shinsen no Kai thời kỳ đầu với thảm trắng, khói trầm hương lượn lờ và sơ đồ vật lý lượng tử treo tường.",
        "prompt": "Early yoga and spiritual retreat studio, rows of neat tatami mats on hardwood floor, wisps of white incense smoke curling in soft morning window light, wall posters blending Buddhist chakras with quantum physics diagrams, deceptive pseudo-scientific allure."
    },
    {
        "name": "t8_intellectual_hubris_chess",
        "act": 3,
        "sentences": "3.07#1–#3",
        "desc": "Quân vua cờ bằng ngà voi đứng cô độc trên bàn cờ đá cẩm thạch đen, đổ bóng dài méo mó thành hình chiếc bóng tà ác, ẩn dụ cái tôi trí tuệ.",
        "prompt": "Visual metaphor of intellectual pride: A polished ivory chess king standing proud on a dark reflective marble board, its elongated shadow warping into a monstrous distorted horned silhouette, high contrast chiaroscuro noir symbolism."
    },
    {
        "name": "t8_moral_rationalization_books",
        "act": 3,
        "sentences": "3.07#4–#6",
        "desc": "Những cuốn sách giáo trình khoa học đỉnh cao xếp xen lẫn kinh sách tận thế dưới ánh nến leo lét trong thư viện tối.",
        "prompt": "Still life of heavy academic organic chemistry and physics textbooks stacked beside esoteric occult apocalyptic scrolls, a single melting wax candle illuminating handwritten notes justifying violence through logic, chilling noir mood."
    },
    {
        "name": "t8_iron_gate_closing",
        "act": 3,
        "sentences": "3.08#1–#2",
        "desc": "Cánh cổng sắt bọc thép gai của khu căn cứ Kamikuishiki đóng chặt lại bằng ổ khóa lớn, biểu tượng của sự bẫy kín và cắt đứt thế giới.",
        "prompt": "Heavy rusted iron gate of a remote mountain compound slamming shut, heavy industrial chain with a brass padlock snapping locked, barbed wire coils along the top, misty pine woods beyond, visual symbol of psychological entrapment."
    },

    # =========================================================================
    # HỒI 4: MA THUẬT TẨY NÃO & KHÁI NIỆM "POA" ĐẪM MÁU (15:00 – 20:00)
    # =========================================================================
    {
        "name": "t8_concrete_cell_isolation",
        "act": 4,
        "sentences": "4.02#1–#3",
        "desc": "Phòng biệt giam bê tông trần xám xịt với ô cửa sổ sắt nhỏ trên cao, một tấm chăn mỏng rách rưới trên sàn đá lạnh buốt.",
        "prompt": "A tiny bare concrete isolation cell inside a cult compound, raw damp walls, a small high window with heavy iron bars admitting a sliver of pale moonlight, a single tattered blanket on the cold stone floor, extreme isolation and claustrophobia."
    },
    {
        "name": "t8_malnutrition_solitary_bowl",
        "act": 4,
        "sentences": "4.03#1–#2",
        "desc": "Chiếc bát sứ sứt mẻ đựng chút cơm nguội và vài cọng rau luộc đặt lẻ loi trên bậc thềm đá, biểu tượng của sự bỏ đói thể xác.",
        "prompt": "A chipped ceramic bowl containing a meager ration of plain white rice and a single boiled green leaf, sitting on a cold concrete floor beside a tin cup of water, dramatic top-down spotlight, poignant physical deprivation, graphic novel noir."
    },
    {
        "name": "t8_frontal_lobe_brain_scan",
        "act": 4,
        "sentences": "4.03#3–#6",
        "desc": "Hình ảnh chụp cộng hưởng từ / PET scan lát cắt não bộ con người trên màn hình y khoa, vùng thùy trán bị bóng tối bao phủ.",
        "prompt": "Neurological diagnostic PET scan of a human brain displayed on a dark medical monitor, the prefrontal cortex region glowing in cold inactive indigo and fading into black, clinical diagram of executive function collapse, scientific noir."
    },
    {
        "name": "t8_psi_headgear_electrodes",
        "act": 4,
        "sentences": "4.04#1–#3",
        "desc": "Cận cảnh chiếc mũ điện cực PSI (Perfect Salvation Initiation) với mớ dây điện chằng chịt và các đầu hút kim loại phát sáng ma quái.",
        "prompt": "Detailed forensic view of the notorious PSI (Perfect Salvation Initiation) helmet: A black skullcap bristling with multi-colored insulated electrical wires, metallic suction cup electrodes, and pulsating red and blue indicator lights on a mannequin head, eerie mind control device."
    },
    {
        "name": "t8_hallucinogen_ritual_hall",
        "act": 4,
        "sentences": "4.04#4–#5",
        "desc": "Sảnh nghi lễ chìm trong ánh sáng tím huyền bí và khói mờ ảo giác, các chai thuốc hướng thần và ống nghiệm trên bàn tế.",
        "prompt": "Dark subterranean ritual hall bathed in disorienting violet and amber haze, glass vials of chemical hallucinogens and syringes resting on a ritual altar beside burning candles, distorted shadows on rough cavern walls, psychological manipulation."
    },
    {
        "name": "t8_buddhist_mandala_distortion",
        "act": 4,
        "sentences": "4.05#1–#3",
        "desc": "Bức tranh cát Mandala Phật giáo Tây Tạng thiêng liêng bị xáo trộn và biến dạng thành những đường nét sắc nhọn đen tối, biểu tượng bóp méo giáo lý.",
        "prompt": "A traditional intricate Buddhist sacred sand mandala on a dark stone floor, but its sacred sacred circular geometry is warping and fracturing into aggressive jagged black ink dagger shapes, symbolic perversion of spiritual doctrine, chiaroscuro."
    },
    {
        "name": "t8_apocalypse_prophecy_scroll",
        "act": 4,
        "sentences": "4.06#1–#3",
        "desc": "Bản thảo thư pháp viết tay về ngày tận thế và chiến tranh hủy diệt Armageddon đặt cạnh những mô hình tên lửa và đám mây hình nấm.",
        "prompt": "Handwritten Japanese prophetic manuscript scroll covered in bold black calligraphy depicting apocalyptic Armageddon, nuclear mushroom cloud sketches drawn in red ink, brass navigational compass and magnifying glass, grim cult obsession."
    },
    {
        "name": "t8_poa_twisted_doctrine",
        "act": 4,
        "sentences": "4.06#4–#6",
        "desc": "Ẩn dụ thị giác: Bông sen trắng tinh khiết bị dìm vào vũng mực đen kịt, cành sen gãy đôi, biểu tượng cho khái niệm 'Poa' đẫm máu.",
        "prompt": "Visual metaphor of the distorted 'Poa' doctrine: A pristine pure white lotus flower snapped at the stem, slowly drowning in an ominous pool of thick black printer's ink, high-contrast black-and-white noir symbolism, tragic loss of purity."
    },
    {
        "name": "t8_dr_hayashi_umbrella_subway",
        "act": 4,
        "sentences": "4.07#1–#2",
        "desc": "Bóng người đàn ông trung niên trong áo khoác dài cầm chiếc ô đen đứng lẻ loi trên sân ga đông đúc, bóng tối nội tâm đè nặng.",
        "prompt": "Silhouette of a middle-aged man in a dark trench coat holding a long black umbrella, standing motionless amidst the blurred rush of commuters on a subway platform, head bowed, heavy tragic shadow stretching across platform tiles, Rule V5 compliant."
    },
    {
        "name": "t8_tokyo_court_witness_stand",
        "act": 4,
        "sentences": "4.08#1–#4",
        "desc": "Bục nhân chứng bằng gỗ tại Tòa án Tokyo, chiếc micro kim loại đơn độc dưới ánh đèn rọi thẳng từ trần nhà, không khí trang nghiêm nghẹn ngào.",
        "prompt": "The solitary wooden witness dock in the Tokyo District Court, a gooseneck chrome microphone poised under a single stark overhead beam of light, dark courtroom gallery in deep shadow, solemn atmosphere of reckoning and grief."
    },
    {
        "name": "t8_broken_hippocratic_oath",
        "act": 4,
        "sentences": "4.08#5–#7",
        "desc": "Bản Lời thề Hippocrates bằng giấy da bị rách một đường dài, chiếc dao mổ phẫu thuật bằng thép sáng loáng nằm bên cạnh trong bóng tối.",
        "prompt": "Forensic still life: An ancient parchment scroll of the Hippocratic Oath torn down the center, a gleaming surgical stainless steel scalpel lying across the tear, harsh raking light casting razor-sharp shadows, profound medical betrayal."
    },
    {
        "name": "t8_tokyo_court_gavel_strike",
        "act": 4,
        "sentences": "4.08#7-SFX",
        "desc": "Chiếc búa gỗ thẩm phán đập dứt khoát xuống đế gỗ tròn trong phòng xử án, khẳng định công lý hình sự.",
        "prompt": "A solid dark mahogany judicial gavel striking down onto a polished circular wooden sounding block, dramatic side-lighting catching dust motes in the air, authoritative symbol of justice and judicial finality, rich chiaroscuro."
    },
    {
        "name": "t8_murai_assassination_cameras",
        "act": 4,
        "sentences": "4.10#1–#3",
        "desc": "Ống kính máy quay truyền hình và đèn flash máy ảnh rọi sáng hỗn loạn trong đêm tối bên ngoài văn phòng Aum ở Minami-Aoyama.",
        "prompt": "Media circus chaos outside a Tokyo building at night: Blinding camera flashes bursting in darkness, silhouettes of television news camera rigs, boom microphones, police barricade tape fluttering in the night wind, chaotic noir frenzy."
    },
    {
        "name": "t8_hidden_ceiling_hideout",
        "act": 4,
        "sentences": "4.10#4–#7",
        "desc": "Khoang hầm bí mật chật hẹp giữa trần nhà Satyam số 6, bọc tiền yen và những thỏi vàng nằm lăn lóc trên thanh xà gỗ phủ bụi.",
        "prompt": "A cramped, dusty crawlspace between rough wooden ceiling joists and plasterboard, flashlight beam illuminating bundles of Japanese yen currency notes in a canvas duffel bag and gleaming gold bullion bars, pathetic collapse of a false savior."
    },

    # =========================================================================
    # HỒI 5: PHÁN QUYẾT LỊCH SỬ & BÀI HỌC VỀ SỰ TỰ DO TƯ TƯỞNG (20:00 – 26:00)
    # =========================================================================
    {
        "name": "t8_grand_courtroom_proceedings",
        "act": 5,
        "sentences": "5.02#1–#3",
        "desc": "Toàn cảnh đại phòng xử án Tòa án Quận Tokyo với bục ba vị thẩm phán uy nghiêm, dãy bàn luật sư và không gian xử án đồ sộ.",
        "prompt": "Wide angle view of the monumental main courtroom of the Tokyo District Court, three judges' elevated bench with dark wood paneling, massive Chrysanthemum seal on wall, long defense and prosecution tables, dignified judicial majesty."
    },
    {
        "name": "t8_asahara_empty_dock",
        "act": 5,
        "sentences": "5.02#4–#6",
        "desc": "Vành móng ngựa gỗ sau tấm kính chắn trong suốt, một chiếc ghế trống dưới ánh đèn rọi duy nhất, chấm dứt cơn cuồng vọng.",
        "prompt": "The defendant's dock enclosed behind thick ballistic glass in a Japanese courtroom, a single empty wooden chair under a vertical spotlight beam, surrounding room in deep chiaroscuro shadow, the curtain falling on megalomania."
    },
    {
        "name": "t8_thirteen_death_verdicts",
        "act": 5,
        "sentences": "5.02#7–#11",
        "desc": "Mười ba tập hồ sơ bản án bìa đen mang con dấu đỏ của Tòa án Tối cao Tokyo xếp ngay ngắn trên bàn gỗ sẫm màu.",
        "prompt": "Thirteen identical black leather-bound judicial verdict binders arranged in a formal row on a dark polished oak table, each stamped with an official red seal, solemn gravity of capital sentences, stark contrast lighting."
    },
    {
        "name": "t8_tokyo_detention_house_dawn",
        "act": 5,
        "sentences": "5.02#11–#12",
        "desc": "Trại tạm giam Tokyo tại Kosuge sừng sững trong ánh bình minh tháng 7 năm 2018, những bức tường bê tông cao vút và dây thép gai.",
        "prompt": "Imposing silhouette of the Tokyo Detention House at Kosuge at early dawn in July 2018, massive geometric concrete towers, perimeter walls crowned with razor wire, pale peach and gold horizon glow breaking through dark clouds, justice served."
    },
    {
        "name": "t8_murakami_underground_book",
        "act": 5,
        "sentences": "5.02#13–#03#1",
        "desc": "Cuốn sách 'Underground' (Ngầm) của Haruki Murakami đặt trên bàn gỗ bên cạnh tách trà xanh nguội và bản đồ ga tàu Tokyo.",
        "prompt": "Still life: A vintage edition of Haruki Murakami's book 'Underground' resting on a rustic wooden table beside a ceramic teacup of green tea and a folded 1995 Tokyo metro subway map, soft nostalgic chiaroscuro light."
    },
    {
        "name": "t8_fragile_boundary_mirror",
        "act": 5,
        "sentences": "5.03#2–#3",
        "desc": "Tấm gương phẳng phản chiếu khung cảnh thành phố bình yên bị một vết nứt sâu chạy ngang, ẩn dụ về ranh giới mong manh của tâm trí.",
        "prompt": "Visual philosophical metaphor: A clean plate glass mirror reflecting a peaceful Tokyo city skyline, fractured right across the middle by a sharp jagged diagonal crack, reflecting darkness behind the glass, fragile boundary between normalcy and fanaticism."
    },
    {
        "name": "t8_redflag1_social_isolation",
        "act": 5,
        "sentences": "5.04#1–#4",
        "desc": "Dấu hiệu 1 (Cô lập): Sợi dây điện thoại bàn bị cắt đứt trên mặt bàn làm việc, cánh cửa gỗ khóa chặt trong bóng tối.",
        "prompt": "Red Flag 1 - Social Isolation: A vintage desk telephone with its coiled handset cord cleanly severed, a heavy locked wooden door with deadbolt in background, isolated room in deep shadow, visual warning graphic."
    },
    {
        "name": "t8_redflag2_physical_exhaustion",
        "act": 5,
        "sentences": "5.04#5–#8",
        "desc": "Dấu hiệu 2 (Kiệt quệ): Chiếc đồng hồ bấm giờ cổ điển, chiếc giường sắt chăn gối xộc xệch, bóng đèn trần leo lét, biểu tượng suy kiệt.",
        "prompt": "Red Flag 2 - Physical Exhaustion: An antique mechanical stopwatch ticking on an unmade metal cot with tangled blankets, a single bare swinging electric bulb casting harsh rhythmic shadows, sleeplessness and mental depletion."
    },
    {
        "name": "t8_redflag3_cult_of_personality",
        "act": 5,
        "sentences": "5.04#9–#13",
        "desc": "Dấu hiệu 3 (Sùng bái): Bức tượng bán thân bằng đá khổng lồ trên bệ cao trong bóng tối, tất cả luồng sáng đều hướng lên một người.",
        "prompt": "Red Flag 3 - Cult of Personality: A monumental faceless stone bust on a towering pedestal in cavernous darkness, multiple harsh spotlights all converging upward upon it, tiny subservient shadows at the base, authoritarian psychological warning."
    },
    {
        "name": "t8_redflag4_moral_inversion",
        "act": 5,
        "sentences": "5.04#14–#18",
        "desc": "Dấu hiệu 4 (Ngụy biện đạo đức): Thanh kiếm sắc bén phản chiếu cành ô liu hòa bình bị bẻ gãy, biểu tượng sự tha hóa đạo đức.",
        "prompt": "Red Flag 4 - Moral Inversion: A polished double-edged samurai sword blade reflecting a broken olive branch resting on black stone, dangerous philosophical deceit, sharp chiaroscuro edge lighting."
    },
    {
        "name": "t8_tokyo_dawn_restored_peace",
        "act": 5,
        "sentences": "5.04#19",
        "desc": "Toàn cảnh đường chân trời Tokyo lúc bình minh rạng rỡ, ánh sáng vàng hổ phách xua tan sương mù, biểu tượng của sự hồi sinh và bình yên.",
        "prompt": "Breathtaking panoramic sunrise over Tokyo, warm amber and golden sunlight sweeping across skyscrapers and peaceful river waterways, mist dissolving into crystal morning air, serene hopeful atmosphere, healing and restored reason."
    }
]

# Write bg_jobs_tap08.json
bg_jobs_path = WORK / "bg_jobs_tap08.json"
bg_jobs_path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Created {bg_jobs_path} with {len(jobs)} background jobs!")

# Write gemini_image_prompts_tap08.json
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

gemini_path = WORK / "gemini_image_prompts_tap08.json"
gemini_path.write_text(json.dumps(gemini_prompts, ensure_ascii=False, indent=2), encoding="utf-8")
print(f"Created {gemini_path} with {len(gemini_prompts)} Gemini/Imagen prompts!")
