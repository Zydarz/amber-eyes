import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

jobs = [
    # =========================================================================
    # HỒI 1: LỜI HỨA THIÊN ĐƯỜNG VÀ BÓNG MA NƠI RỪNG SÂU (00:00 – 05:30)
    # =========================================================================
    {
        "name": "t12_guyana_tropical_rainforest_aerial",
        "act": 1,
        "sentences": "1.02#1",
        "desc": "Rừng già nhiệt đới Guyana bạt ngàn trong làn sương mù ẩm ướt rùng rợn, dòng sông uốn khúc tối màu dưới ánh hoàng hôn u tịch, phong cách graphic novel noir.",
        "prompt": "Cinematic 16:9 aerial establishing shot of the vast remote tropical rainforest canopy of Guyana, dense humid mist rising from tangled jungle trees, dark muddy river snaking through the endless wilderness, ominous bruised purple and muted amber twilight sky, high-contrast dark graphic novel noir style, fine film grain."
    },
    {
        "name": "t12_jonestown_settlement_clearing",
        "act": 1,
        "sentences": "1.02#2",
        "desc": "Khu khai hoang nông nghiệp Jonestown giữa rừng già xích đạo, các dãy lán trại gỗ lợp mái tôn trải dài tĩnh mịch trước hoàng hôn.",
        "prompt": "Atmospheric wide shot of the isolated Jonestown agricultural settlement carved out of dense jungle clearing, corrugated tin-roof wooden communal pavilions, solitary pathways of red clay mud, dusk shadows lengthening across the compound, brooding quiet tension, heavy ink chiaroscuro."
    },
    {
        "name": "t12_innocent_children_toys_jungle",
        "act": 1,
        "sentences": "1.02#3",
        "desc": "Tĩnh vật những con búp bê vải sờn và đôi dép trẻ em nằm trơ trọi trên thềm gỗ ẩm mốc ven rừng, ánh sáng rọi xiên u buồn.",
        "prompt": "Forensic still life of worn 1970s rag dolls, handcrafted wooden toys, and a pair of small children sandals lying abandoned on weathered wooden porch planks, warm low-angle diagonal light beam piercing through jungle foliage, haunting innocent silence, dark graphic noir linework."
    },
    {
        "name": "t12_monolithic_tragedy_shadow",
        "act": 1,
        "sentences": "1.02#4",
        "desc": "Quần thể khu lán trung tâm Jonestown chìm trong bóng tối khổng lồ của tán rừng, không một bóng quân đội xâm lược, sự im lặng rợn người.",
        "prompt": "Dramatic panoramic view of the vast central pavilion of Jonestown engulfed by towering shadows of ancient tropical trees, complete absence of external armed forces, suffocating eerie stillness, deep obsidian blacks and somber indigo tones, stark chiaroscuro noir."
    },
    {
        "name": "t12_puppet_master_dark_silhouette",
        "act": 1,
        "sentences": "1.02#5",
        "desc": "Bóng đen kẻ độc tài Jim Jones với cặp kính râm đặc trưng đứng trên cao, bóng đổ dài nuốt chửng hàng trăm sinh mệnh vô hình.",
        "prompt": "Chilling silhouette in profile of a charismatic cult leader wearing dark aviator sunglasses and pastoral collar, standing on an elevated wooden rostrum, casting an immense monstrous shadow across the ground, faceless silhouette adhering strictly to documentary standards, heavy black ink contours."
    },
    {
        "name": "t12_indiana_church_1950s_dawn",
        "act": 1,
        "sentences": "1.04#1",
        "desc": "Ngôi nhà thờ mộc mạc thập niên 1950 tại bang Indiana dưới ánh bình minh hoài niệm, nơi khởi nguồn của Đền thờ Nhân dân Peoples Temple.",
        "prompt": "Nostalgic exterior shot of a humble 1950s Midwestern brick church in rural Indiana, soft pale amber morning light filtering through autumn mist, vintage American automobiles parked quietly along the curb, deceptive peaceful origins, vintage graphic novel aesthetic."
    },
    {
        "name": "t12_racial_harmony_facade",
        "act": 1,
        "sentences": "1.04#2",
        "desc": "Cảnh sinh hoạt hội trường với bóng đen những bàn tay đa chủng tộc nắm chặt nhau, biểu tượng tiến bộ xã hội ban đầu của Peoples Temple.",
        "prompt": "Powerful graphic composition showing diverse silhouettes of men, women, and elderly people holding hands together in unity inside a dimly lit meeting hall, warm golden spotlight illuminating raised clasped hands, symbolic racial equality facade, bold ink shading."
    },
    {
        "name": "t12_charity_soup_kitchen_bread",
        "act": 1,
        "sentences": "1.04#3",
        "desc": "Tĩnh vật khay súp từ thiện nóng hổi, bánh mì cắt lát và tờ bướm cứu trợ người nghèo trên bàn gỗ sờn, ánh đèn vàng ấm áp.",
        "prompt": "Warm still life of a steaming metal soup kettle, sliced bread on a worn cutting board, and printed community charity flyers on a rustic communal kitchen table, soft amber hanging bulb lighting, nostalgic humanitarian benevolence facade, dark linework."
    },
    {
        "name": "t12_san_francisco_temple_expansion",
        "act": 1,
        "sentences": "1.04#4",
        "desc": "Trụ sở Peoples Temple tại San Francisco đầu thập niên 1970, dòng người đông đúc xếp hàng trong làn sương mù Bờ Tây đặc trưng.",
        "prompt": "Cinematic street scene outside the Peoples Temple headquarters on Geary Boulevard in San Francisco circa 1972, dense Pacific fog rolling down Victorian streetlamps, long queue of hopeful citizens waiting under vintage neon marquee, noir atmosphere."
    },
    {
        "name": "t12_city_hall_political_alliances",
        "act": 1,
        "sentences": "1.04#5",
        "desc": "Bậc thềm Tòa thị chính San Francisco với bóng các chính khách bắt tay, chứng nhận bổ nhiệm Chủ tịch Ủy ban Nhà ở thành phố.",
        "prompt": "Interior architectural shot of the grand neoclassical rotunda of San Francisco City Hall, silhouetted municipal politicians shaking hands under towering limestone columns, framed official commission certificate on mahogany desk, high-contrast political noir."
    },
    {
        "name": "t12_iron_fist_behind_velvet_curtain",
        "act": 1,
        "sentences": "1.06#1",
        "desc": "Bức rèm nhung đỏ sang trọng hé mở lộ ra xiềng xích và bóng chiếc roi da trong góc tối của hội thánh, đế chế độc tài ẩn giấu.",
        "prompt": "Symbolic chiaroscuro still life of an opulent red velvet stage curtain pulled slightly aside to reveal heavy iron chains and a coiled leather whip resting in pitch-black shadow, stark contrast between righteous charity facade and brutal authoritarian reality."
    },
    {
        "name": "t12_catharsis_session_interrogation",
        "act": 1,
        "sentences": "1.06#2–#3",
        "desc": "Buổi 'Thanh lọc tâm trí' ngột ngạt dưới bóng đèn treo đơn độc, một bóng người quỳ gối giữa vòng vây chỉ trích và sỉ nhục của tập thể.",
        "prompt": "Tense theatrical interior of a secret nighttime catharsis session, single harsh bare bulb illuminating a lone kneeling silhouette in the center of a wooden stage, surrounded by menacing shadowy figures pointing accusatory fingers, psychological humiliation noir."
    },
    {
        "name": "t12_property_surrender_passbooks",
        "act": 1,
        "sentences": "1.06#4",
        "desc": "Chồng sổ tiết kiệm ngân hàng, khế ước chuyển nhượng nhà đất và những phong bì trợ cấp xã hội bị tịch thu trên bàn gỗ đen.",
        "prompt": "Forensic still life of stacked 1970s bank savings passbooks, stamped real estate property deeds, and Social Security check envelopes piled on a dark mahogany desk, harsh raking desk lamp light, systemic financial dispossession aesthetic."
    },
    {
        "name": "t12_new_west_investigative_draft",
        "act": 1,
        "sentences": "1.06#5",
        "desc": "Bản thảo phóng sự điều tra của tạp chí New West cùng ống kính máy ảnh và xấp ảnh tư liệu bí mật trên bàn làm việc đêm.",
        "prompt": "Journalistic investigative desktop at midnight, vintage typewriter beside typed galleys marked New West Magazine, magnifying glass, rolls of 35mm film negatives, and classified interview notes, urgent investigative tension, moody slate and amber noir."
    },
    {
        "name": "t12_exodus_ships_guyana_dusk",
        "act": 1,
        "sentences": "1.06#6",
        "desc": "Con tàu chở hàng chở gần một ngàn tín đồ rời cảng trong màn đêm mù mịt, hướng về bờ biển hoang vu Nam Mỹ.",
        "prompt": "Dramatic seaport scene of a vintage cargo ship departing an industrial harbor at twilight, heavy ocean fog swallowing the dark hull, faint silhouettes of hundreds of passengers on deck staring into the endless sea toward South America, brooding noir journey."
    },
    {
        "name": "t12_utopian_promise_mirage",
        "act": 1,
        "sentences": "1.07#1–#2",
        "desc": "Ảo ảnh về miền đất hứa rực rỡ với đồng cỏ và hoa trái, mờ ảo như bức tranh vẽ đối lập với rừng rậm u uất.",
        "prompt": "Surreal split-toned composition showing an ethereal painted poster of a tropical paradise with blooming orchards and golden sunlight, peeling and curling at the edges to reveal rotting dark jungle timber beneath, tragic illusion of promised utopia."
    },
    {
        "name": "t12_confiscated_passports_trunk",
        "act": 1,
        "sentences": "1.07#3–#4",
        "desc": "Chiếc rương sắt cũ kỹ khóa chặt, bên trong chứa hàng trăm cuốn hộ chiếu Mỹ và ví tiền của các tín đồ bị tước đoạt.",
        "prompt": "Forensic macro still life of an open heavy green military footlocker filled with confiscated blue US passports, leather wallets, and identity papers, heavy brass padlock resting on the rim, symbol of total loss of civic identity, dark chiaroscuro."
    },
    {
        "name": "t12_equatorial_forced_labor_fields",
        "act": 1,
        "sentences": "1.07#5",
        "desc": "Bóng những tín đồ cúi gập lưng vung cuốc trên bãi đất đỏ bazan dưới ánh nắng xích đạo gay gắt đến cháy da.",
        "prompt": "Scorching daytime landscape in the Guyana clearing, silhouetted field laborers bent double wielding hoes and machetes in harsh midday tropical sun, shimmering heat waves rising from scorched clay soil, exhausting agricultural servitude, gritty noir."
    },
    {
        "name": "t12_meager_ration_tin_bowl",
        "act": 1,
        "sentences": "1.07#6",
        "desc": "Bát sắt đựng phần cơm trắng lõng bõng chan nước sốt loãng, chiếc thìa nhôm trầy xước cạnh vũng bùn đất.",
        "prompt": "Poignant macro still life of a dented tin bowl containing plain white rice covered in thin watery gravy, resting on a rough timber bench beside a scratched aluminum spoon, harsh side-light emphasizing starvation and biological exhaustion."
    },
    {
        "name": "t12_armed_guards_crossbow_perimeter",
        "act": 1,
        "sentences": "1.07#7",
        "desc": "Bóng tay lính gác cầm súng trường và nỏ tự chế đứng sau rặng cây dương xỉ rậm rạp ngăn chặn lối ra rừng.",
        "prompt": "Ominous jungle perimeter view, deep shadowy fern fronds framing the silhouette of an armed sentry holding a rifle and homemade hunting crossbow, watching the jungle edge, sense of trapped claustrophobia in open air, dark graphic noir."
    },
    {
        "name": "t12_inescapable_labor_camp_cage",
        "act": 1,
        "sentences": "1.07#8",
        "desc": "Con đường mòn bùn lầy dẫn vào rừng sâu bị giăng kín dây kẽm gai và cành cây gai góc, lồng giam lao dịch không lối thoát.",
        "prompt": "Haunting perspective looking down a narrow muddy trail disappearing into suffocating black rainforest, jagged barbed wire strands stretched between rotting fence posts, psychological cage without walls, deep vignette and film grain."
    },
    {
        "name": "t12_loudspeaker_horns_tower",
        "act": 1,
        "sentences": "1.09#1–#2",
        "desc": "Cột gỗ cao vút gắn chùm loa phóng thanh kim loại chĩa về bốn phía lán trại, rung lên giữa bầu trời xám xịt.",
        "prompt": "Low-angle dramatic shot of a tall weathered wooden pole mounted with multiple metallic public-address horn loudspeakers, wires dangling against an overcast bruised sky, sound waves visually implied through ink hatching, constant surveillance and brainwashing."
    },
    {
        "name": "t12_central_pavilion_night_tribunal",
        "act": 1,
        "sentences": "1.09#3",
        "desc": "Lán trung tâm Jonestown sáng rực ánh đèn măng-sông trong đêm, nơi diễn ra các phiên trừng phạt thể xác người hoài nghi.",
        "prompt": "Interior night scene of the Jonestown open-air wooden pavilion, blinding white glare from kerosene pressure lanterns casting intense jagged shadows of seated crowd, disciplinary trial atmosphere, fear and psychological intimidation."
    },
    {
        "name": "t12_impenetrable_geographical_isolation",
        "act": 1,
        "sentences": "1.09#4",
        "desc": "Bản đồ không gian địa lý thể hiện Jonestown như một chấm nhỏ cô độc lọt thỏm giữa hàng trăm dặm rừng già nhiệt đới.",
        "prompt": "Cartographic forensic diagram of northwestern Guyana, antique topographer map overlaid with ink hatching showing hundreds of miles of roadless dense jungle surrounding a tiny isolated red circle marked Jonestown, total geographic isolation."
    },
    {
        "name": "t12_concerned_relatives_alliance",
        "act": 1,
        "sentences": "1.10#1–#2",
        "desc": "Hồ sơ của Nhóm Thân nhân Quan ngại với những bức thư khẩn thiết, ảnh chụp gia đình bị kẹt lại tại Guyana.",
        "prompt": "Forensic evidence dossier marked Concerned Relatives, black-and-white family portraits pinned to corkboard, urgent telegrams addressed to the US State Department, desperate appeals for government intervention, somber documentary noir."
    },
    {
        "name": "t12_congressman_leo_ryan_briefing",
        "act": 1,
        "sentences": "1.10#3",
        "desc": "Bàn làm việc tại Washington với bản đồ hành trình Guyana, thẻ đại biểu Quốc hội của Nghị sĩ Leo Ryan và vé máy bay.",
        "prompt": "Official congressional briefing desk, official US House of Representatives pass badge belonging to Congressman Leo Ryan, flight tickets to Georgetown Guyana, stamped diplomatic passport, resolute moral duty tone, crisp chiaroscuro."
    },
    {
        "name": "t12_press_corps_cameras_microphones",
        "act": 1,
        "sentences": "1.10#4",
        "desc": "Máy quay phim 16mm của đài NBC, máy ảnh phóng viên và micro thu âm sẵn sàng cho chuyến công tác thực địa nguy hiểm.",
        "prompt": "Journalistic field equipment still life, heavy 16mm NBC television news film camera, 35mm rangefinder cameras with telephoto lenses, directional microphone, reporter notebooks, ready for hostile environment fact-finding mission."
    },
    {
        "name": "t12_entering_armed_compound_gate",
        "act": 1,
        "sentences": "1.10#5",
        "desc": "Cánh cổng gỗ mộc mạc mang biển hiệu Peoples Temple ẩn hiện sau làn sương rừng, báo hiệu hang ổ đầy cạm bẫy.",
        "prompt": "Cinematic shot of the rustic wooden archway entrance to Peoples Temple Agricultural Project, peeling hand-painted sign half-shrouded in morning mist, muddy tire tracks leading into dense suffocating jungle foliage, ominous frontier threshold."
    },
    {
        "name": "t12_paranoia_cracking_dictator_mind",
        "act": 1,
        "sentences": "1.11#1–#2",
        "desc": "Jim Jones trong căn phòng kín tại Jonestown, gương mặt ẩn sau kính đen, hai bàn tay run rẩy bấu chặt mép bàn vì hoang tưởng.",
        "prompt": "Psychological noir portrait of the cult leader in a dark claustrophobic wooden cabin, face obscured by heavy shadows and dark sunglasses, trembling white-knuckled hands gripping the table edge, pill bottles scattered across papers, spiraling paranoia."
    },
    {
        "name": "t12_edge_of_the_abyss_shadow",
        "act": 1,
        "sentences": "1.11#3",
        "desc": "Bóng đen kẻ thủ ác đứng trên mỏm dốc nhìn xuống khu lán trại đang ngủ yên, toan tính kéo tất cả xuống vực thẳm.",
        "prompt": "Dramatic silhouette of a solitary domineering figure standing on an earthen ridge overlooking the quiet sleeping pavilions of Jonestown below, stormy purple sky bruised by distant lightning, chilling resolve to drag innocent souls into catastrophe."
    },

    # =========================================================================
    # HỒI 2: CUỘC PHỤC KÍCH ĐƯỜNG BĂNG VÀ TIẾNG CÒI BÁO ĐỘNG ĐỊNH MỆNH (05:30 – 11:00)
    # =========================================================================
    {
        "name": "t12_arrival_port_kaituma_dust",
        "act": 2,
        "sentences": "2.02#1–#2",
        "desc": "Chiếc xe tải chở phái đoàn Quốc hội chạy dọc con đường đất đỏ gồ ghề tiến vào khu định cư Jonestown dưới ráng chiều.",
        "prompt": "Cinematic shot of a vintage flatbed dump truck carrying the congressional delegation arriving along a bumpy red clay road, dust swirling in deep amber sunset light, entering the Jonestown clearing under intense wary stares, documentary noir."
    },
    {
        "name": "t12_reception_musical_performance",
        "act": 2,
        "sentences": "2.04#1–#2",
        "desc": "Sân khấu lán trung tâm với cây đàn guitar thùng, dàn hợp xướng tín đồ đang biểu diễn với nụ cười gượng gạo trong ánh đèn.",
        "prompt": "Lively yet uncanny musical performance inside the large open wooden pavilion, acoustic guitars and vocal microphones on stage, smiling choir members singing under hanging bulb arrays, rehearsed staged enthusiasm masking deep exhaustion."
    },
    {
        "name": "t12_nbc_camera_recording_facade",
        "act": 2,
        "sentences": "2.04#3",
        "desc": "Ống kính máy quay NBC hướng về các gia đình ngồi quây quần, ghi lại khung cảnh hòa bình giả tạo kiểu mẫu.",
        "prompt": "Shoulder-mounted 16mm NBC news camera in silhouette pointing toward smiling multigenerational families seated at communal picnic tables, red recording tally light glowing, fragile illusion of peace captured on celluloid."
    },
    {
        "name": "t12_leo_ryan_podium_applause",
        "act": 2,
        "sentences": "2.04#4",
        "desc": "Bóng Dân biểu Leo Ryan đứng phát biểu trước micro, hội trường bùng nổ tràng vỗ tay được dàn dựng công phu.",
        "prompt": "Silhouetted figure of Congressman Leo Ryan standing at a wooden microphone stand addressing a packed audience under timber rafters, enthusiastic clapping hands raised across the hall, dramatic warm spotlighting, fateful optimism."
    },
    {
        "name": "t12_secret_note_folded_slip",
        "act": 2,
        "sentences": "2.06#1–#3",
        "desc": "Cận cảnh bàn tay run rẩy lén chuyển mẩu giấy gấp tư nhàu nát ghi dòng chữ cầu cứu tuyệt vọng trong bóng tối.",
        "prompt": "Tense forensic macro shot of two hands brushing secretly in shadowy darkness, passing a tiny creased paper slip, visible handwritten desperate plea reading 'Help us get out of Jonestown', high-contrast ink chiaroscuro, pulse of danger."
    },
    {
        "name": "t12_morning_pleas_for_defection",
        "act": 2,
        "sentences": "2.06#4",
        "desc": "Từng nhóm tín đồ lén lút tiếp cận các thành viên phái đoàn bên góc lán trại lúc tảng sáng xin được hồi hương.",
        "prompt": "Subtle early morning scene in misty jungle dawn, small groups of shadowy figures quietly approaching delegation members behind wooden storage sheds, whispered urgent conversations, courage battling terror, cool blue and slate tones."
    },
    {
        "name": "t12_crumbling_facade_tension",
        "act": 2,
        "sentences": "2.06#5",
        "desc": "Không khí căng thẳng đặc quánh bao trùm khu lán trại khi bức màn tự nguyện hoàn toàn rách nát.",
        "prompt": "Atmospheric wide shot of the compound in heavy equatorial heat, armed guards gathering on porch steps, nervous glances exchanged between workers, total fracture of the staged utopian narrative, suffocating impending doom."
    },
    {
        "name": "t12_confrontation_at_lectern",
        "act": 2,
        "sentences": "2.07#1–#3",
        "desc": "Cuộc đối thoại nảy lửa tại bục gỗ giữa Nghị sĩ Ryan cương trực và Jim Jones với vẻ mặt thất thần hoảng loạn.",
        "prompt": "Stark confrontation scene at the pavilion rostrum, resolute silhouette of the US Congressman facing the agitated cult leader in dark sunglasses, defensive pleading postures, heavy timber posts framing intense psychological breakdown."
    },
    {
        "name": "t12_knife_attack_scuffle_pavilion",
        "act": 2,
        "sentences": "2.07#4–#5",
        "desc": "Bóng kẻ cuồng tín cầm dao lao tới bị các luật sư và nhân chứng ôm chặt ngăn cản giữa lán trung tâm.",
        "prompt": "Sudden violent scuffle in dramatic silhouette, raised arm clutching a glinting hunting knife intercepted by grappling figures in front of the wooden stage, overturned benches, flash of adrenaline and terror, graphic noir linework."
    },
    {
        "name": "t12_truck_evacuation_muddy_road",
        "act": 2,
        "sentences": "2.07#6",
        "desc": "Chiếc xe tải chở phái đoàn và 15 tín đồ đào thoát vội vã lao qua con đường đất bùn lầy hướng về sân bay.",
        "prompt": "Exterior shot of a mud-splattered flatbed truck speeding down a rutted jungle road away from the compound, passengers holding tight to wooden rails in anxious silence, spray of red mud, frantic race toward evacuation."
    },
    {
        "name": "t12_port_kaituma_gravel_airstrip",
        "act": 2,
        "sentences": "2.09#1–#2",
        "desc": "Đường băng sỏi đá Port Kaituma hoang vắng giữa rừng già với bóng hai chiếc phi cơ cánh quạt nhỏ Cessna và Otter.",
        "prompt": "Desolate wide shot of the remote Port Kaituma jungle airstrip, red gravel runway surrounded by impenetrable wall of tall rainforest trees, two small propeller airplanes waiting quietly under darkening afternoon clouds, tense silence."
    },
    {
        "name": "t12_red_brigade_tractor_approach",
        "act": 2,
        "sentences": "2.11#1",
        "desc": "Chiếc máy kéo màu đỏ kéo theo rơ-moóc chở các tay súng cận vệ lao nhanh về phía đường băng trong làn bụi mờ.",
        "prompt": "Menacing ground-level view of a rumbling red farm tractor towing an open trailer, armed cult enforcers silhouettes standing with raised shotguns and rifles, churning up dust as it speeds directly onto the runway apron, brutal ambush."
    },
    {
        "name": "t12_airstrip_ambush_gunfire_smoke",
        "act": 2,
        "sentences": "2.11#2",
        "desc": "Khói súng bốc lên mịt mù trên nền đường băng, vỏ đạn rơi rải rác bên cánh máy bay bị bắn thủng lỗ chỗ.",
        "prompt": "Graphic noir depiction of sudden ambush, clouds of gunsmoke drifting across gravel airstrip, spent rifle cartridge casings scattered in mud near airplane landing gear tires, bullet holes puncturing aluminum wing skin, stark chiaroscuro."
    },
    {
        "name": "t12_fallen_reporters_and_ryan",
        "act": 2,
        "sentences": "2.11#3–#4",
        "desc": "Máy quay phim NBC đổ nghiêng trên bãi sỏi cạnh cuốn sổ tay nhà báo và huy hiệu Quốc hội vương vết bụi đường.",
        "prompt": "Solemn forensic still life, dented NBC news camera lying on the gravel shoulder, cracked lens reflecting overcast sky, reporter press card, and fallen congressional lapel pin in red dust, solemn historical tragedy, respectful documentary angle."
    },
    {
        "name": "t12_jackie_speier_resilience_shadow",
        "act": 2,
        "sentences": "2.11#5–#6",
        "desc": "Bóng người phụ nữ trẻ gục bên bánh xe máy bay nhưng bàn tay vẫn kiên cường bám chặt mặt đất sinh tồn.",
        "prompt": "Moving artistic silhouette of a wounded young female congressional aide sheltering beneath the shadow of an aircraft wheel, hand gripping the gravel firmly in fierce determination to survive, solitary ray of amber light cutting across the dark ground."
    },
    {
        "name": "t12_gunmen_return_report_shadows",
        "act": 2,
        "sentences": "2.13#1–#2",
        "desc": "Chiếc máy kéo phóng bạt mạng trở lại cổng Jonestown trong bóng chiều tà, bóng các tay súng bước vào lán báo tin.",
        "prompt": "Dark silhouette of the tractor returning through the wooden gates of Jonestown in deep dusk, shadowy figures dismounting and running toward the central pavilion, grim news delivered in panicked whispers, fateful threshold."
    },
    {
        "name": "t12_emergency_siren_echo_jungle",
        "act": 2,
        "sentences": "2.13#3–#4",
        "desc": "Chiếc còi báo động khẩn cấp bằng kim loại rú lên xé toạc không gian yên tĩnh của cánh rừng nhiệt đới.",
        "prompt": "Low-angle shot of a metal emergency siren horn vibrating atop a wooden pole, jarring shockwaves visually rendered through jagged ink hatching, flocks of jungle birds scattering into dark stormy twilight, herald of destruction."
    },
    {
        "name": "t12_mass_gathering_central_pavilion",
        "act": 2,
        "sentences": "2.13#4",
        "desc": "Hàng trăm bóng người từ các lán trại lũ lượt bước về phía lán trung tâm dưới ánh hoàng hôn đỏ quạch u ám.",
        "prompt": "Eerie mass migration of hundreds of silhouetted men, women, and children streaming along muddy paths toward the glowing central pavilion, bruised crimson and charcoal dusk sky, somber collective momentum toward tragedy."
    },

    # =========================================================================
    # HỒI 3: GIẢI MÃ CƠ CHẾ TÂM LÝ: TỪ PHỤC TÙNG ĐẾN TƯ DUY TẬP THỂ (11:00 – 16:30)
    # =========================================================================
    {
        "name": "t12_unanswered_question_diorama",
        "act": 3,
        "sentences": "3.02#1–#4",
        "desc": "Khung cảnh trừu tượng với bức tường đen và hàng trăm con rối gỗ bị cắt đứt dây, gợi mở câu hỏi nhức nhối của nhân loại.",
        "prompt": "Philosophical conceptual art of an immense black stone wall inscribed with subtle hairline fractures, row of antique wooden marionettes with severed strings lying motionless on reflective floorboards, haunting inquiry into human obedience, dark chiaroscuro."
    },
    {
        "name": "t12_milgram_experiment_shock_generator",
        "act": 3,
        "sentences": "3.03#1–#3",
        "desc": "Bảng điều khiển máy sốc điện trong thí nghiệm tâm lý Stanley Milgram với các công tắc vạch điện áp tăng dần.",
        "prompt": "Forensic close-up of Stanley Milgram's classic 1960s experimental shock generator console, vintage toggle switches labeled with escalating voltage ratings up to 450 Volts XXX, harsh raking laboratory light, psychological obedience paradigm."
    },
    {
        "name": "t12_agentic_state_mechanism",
        "act": 3,
        "sentences": "3.03#4–#5",
        "desc": "Sơ đồ giải phẫu tâm lý học biểu diễn sự chuyển đổi từ chủ thể tự do sang 'Trạng thái Công cụ' vô thức phục tùng.",
        "prompt": "Conceptual diagram of human consciousness transitioning into an 'Agentic State', human silhouette transforming into interlocking mechanical brass cogwheels under a domineering authority apex, clean technical ink linework on dark slate."
    },
    {
        "name": "t12_false_prophet_deification",
        "act": 3,
        "sentences": "3.03#6",
        "desc": "Bục giảng Jonestown với bóng đen Jim Jones phóng to khổng lồ phủ bóng lên những chiếc ghế gỗ nhỏ bé phía dưới.",
        "prompt": "Theatrical chiaroscuro shot looking up at a towering wooden pulpit, immense shadow of the cult leader cast onto high timber rafters, dwarfing rows of empty rustic pews below, visual metaphor for absolute moral abdication."
    },
    {
        "name": "t12_foot_in_the_door_staircase",
        "act": 3,
        "sentences": "3.04#1–#3",
        "desc": "Cầu thang gỗ dẫn dắt tâm lý với từng bậc thang nhỏ dần lún sâu vào bóng tối, minh họa cho sự leo thang cam kết.",
        "prompt": "Metaphorical architectural rendering of a steep spiral wooden staircase descending gradually from sunlight into an impenetrable pitch-black abyss, representing the subtle 'Foot-in-the-Door' escalation of commitment, dark graphic noir."
    },
    {
        "name": "t12_cognitive_dissonance_scales",
        "act": 3,
        "sentences": "3.05#1–#5",
        "desc": "Chiếc cân tâm lý học Leon Festinger mất thăng bằng giữa một bên là sự thật thực tế và một bên là chi phí đã đầu tư.",
        "prompt": "Surreal still life of antique brass balance scales tipped violently to one side under the crushing weight of sacrifice and sunken pride, while truth and rational doubt float weightless, warm amber highlight on metal pan, Leon Festinger theory."
    },
    {
        "name": "t12_sunk_cost_entrapment_quicksand",
        "act": 3,
        "sentences": "3.05#6–#8",
        "desc": "Hình ảnh ẩn dụ bàn tay chìm dần trong bãi cát lún của niềm tin mù quáng và sự tự biện minh nhận thức.",
        "prompt": "Poignant conceptual graphic illustration of an outstretched hand grasping an illusory shining golden medallion while sinking inexorably into dark quicksand of collective delusion and self-justification, high-contrast ink crosshatching."
    },
    {
        "name": "t12_biological_exhaustion_heat",
        "act": 3,
        "sentences": "3.06#1–#2",
        "desc": "Ánh mặt trời xích đạo chói chang thiêu đốt cánh đồng cỏ khô khốc, bóng người gục ngã vì kiệt sức sinh học.",
        "prompt": "Harsh monochromatic landscape of an equatorial clearing under an unforgiving blazing white-hot sun, lone silhouette collapsed over a wooden plow in cracked dirt, visible heat shimmer, biological depletion and cognitive breakdown."
    },
    {
        "name": "t12_sleep_deprivation_speaker_wires",
        "act": 3,
        "sentences": "3.06#3",
        "desc": "Đường dây điện chằng chịt nối các loa phóng thanh phát ra âm thanh xuyên màn đêm, cướp đi giấc ngủ con người.",
        "prompt": "Tangled black electrical wires silhouetted against a restless midnight sky, connecting humming horn speakers mounted to cabin rafters, cold blue moonlight, sleepless night of relentless psychological auditory siege."
    },
    {
        "name": "t12_prefrontal_cortex_impairment",
        "act": 3,
        "sentences": "3.06#4–#5",
        "desc": "Sơ đồ y khoa phác thảo não bộ với vùng thùy trán bị bóng tối bao phủ do thiếu ngủ và suy kiệt dinh dưỡng.",
        "prompt": "Forensic neurobiology diagram displaying a human profile brain map, prefrontal cortex area dimmed and engulfed in fractured ink shadows, illustrating the scientific failure of executive function under chronic starvation and sleep deprivation."
    },
    {
        "name": "t12_white_night_midnight_bell",
        "act": 3,
        "sentences": "3.07#1–#3",
        "desc": "Chiếc chuông đồng treo giữa quảng trường Jonestown đung đưa trong đêm phát ra những hồi chuông báo động giả định.",
        "prompt": "Heavy bronze alarm bell swinging on a rustic wooden gallows in the center of Jonestown at midnight, cold crescent moon overhead, sound reverberating through empty dark paths, simulated crisis drill."
    },
    {
        "name": "t12_simulated_poison_paper_cups",
        "act": 3,
        "sentences": "3.07#4–#5",
        "desc": "Những chiếc cốc giấy nhỏ đựng nước màu đỏ xếp thành hàng dài trên bàn gỗ trong các buổi tập dượt lòng trung thành.",
        "prompt": "Forensic still life of dozens of small paper drinking cups filled with red liquid neatly aligned on rough wooden plank tables, dim overhead kerosene lantern light, chilling loyalty test rehearsal, desensitizing reflex."
    },
    {
        "name": "t12_habituation_death_desensitization",
        "act": 3,
        "sentences": "3.07#6–#7",
        "desc": "Biểu đồ tâm lý học thể hiện đường cong đáp ứng sợ hãi phẳng dần theo thời gian qua các cuộc diễn tập lặp lại.",
        "prompt": "Scientific psychological chart etched on vintage blackboard, downward curve of human fear response flattening toward baseline over successive trials, habituation and psychological erosion of survival instinct, chalkboard noir."
    },
    {
        "name": "t12_pawns_on_destructive_chessboard",
        "act": 3,
        "sentences": "3.08#1–#3",
        "desc": "Bàn cờ vua đen với hàng trăm quân cờ tốt bằng gỗ đứng bất động trước bóng bàn tay kẻ thao túng.",
        "prompt": "Allegorical still life of an enormous dark wooden chessboard stretching to the horizon, hundreds of identical carved wooden pawn pieces standing in rigid ranks before the towering shadow of an invisible player hand, fate sealed."
    },

    # =========================================================================
    # HỒI 4: CUỘN BĂNG TỬ THẦN Q 042 VÀ TIẾNG NÓI PHẢN KHÁNG CÔ ĐƠN (16:30 – 21:30)
    # =========================================================================
    {
        "name": "t12_fbi_evidence_tape_q042",
        "act": 4,
        "sentences": "4.02#1–#3",
        "desc": "Cuộn băng cassette cổ điển dán nhãn bằng chứng FBI Record Q 042 đặt trong túi nylon pháp y cạnh chiếc máy thu âm cũ.",
        "prompt": "Forensic still life of an authentic 1970s compact cassette tape inside a sealed FBI evidence plastic bag, typed label marked 'RYMUR FBI Record Q 042', resting on stainless steel examination table beside forensic ruler, stark clinical noir."
    },
    {
        "name": "t12_tape_recorder_reels_spinning",
        "act": 4,
        "sentences": "4.04#1–#2",
        "desc": "Hai cuộn băng từ xoay tròn từ từ trong máy phát cassette dưới ánh đèn điều tra vàng nhạt.",
        "prompt": "Extreme macro close-up of the spinning black spools of a cassette mechanism playing behind scratched clear plastic, tiny magnetic tape threading over the playback head, warm raking lamp light, haunting audio artifact of history."
    },
    {
        "name": "t12_agitated_dictator_microphone",
        "act": 4,
        "sentences": "4.04#3–#4",
        "desc": "Chiếc micro kim loại cổ điển trên bục giảng Jonestown hứng trọn những lời gieo rắc hoảng loạn dồn dập.",
        "prompt": "Low-angle view of a vintage Shure dynamic microphone mounted on a wooden lectern, dark background of the pavilion roof trusses, single spotlight beam cutting through rising tropical humidity, acoustic crucible of mass panic."
    },
    {
        "name": "t12_christine_miller_lone_microphone",
        "act": 4,
        "sentences": "4.06#1–#2",
        "desc": "Bóng người phụ nữ 60 tuổi nhỏ bé đứng thẳng trước micro giữa lán trung tâm, ngẩng cao đầu đối chất với bạo quyền.",
        "prompt": "Historic moment of moral courage in silhouette, an elderly African-American woman standing dignified and resolute before the public microphone, facing the elevated cult leader rostrum, surrounded by seated darkness, noble defiance."
    },
    {
        "name": "t12_moral_courage_candle_in_dark",
        "act": 4,
        "sentences": "4.07#1–#5",
        "desc": "Ngọn nến đơn độc bùng cháy rực rỡ giữa vòng xoáy bóng tối, biểu tượng cho lương tri bất khuất của Christine Miller.",
        "prompt": "Poetic chiaroscuro composition of a solitary lit candle flame standing firm amidst violent swirling shadows of darkness, warm amber glow illuminating the words 'Life is worth living' in delicate Cambria script in the viewer's mind, unbroken conscience."
    },
    {
        "name": "t12_groupthink_hostile_mob_shadows",
        "act": 4,
        "sentences": "4.08#1–#4",
        "desc": "Đám đông tín đồ bao quanh hò hét, giơ tay phản đối và xua đuổi tiếng nói lý trí duy nhất, sự tàn nhẫn của Groupthink.",
        "prompt": "Oppressive psychological depiction of Irving Janis's Groupthink, menacing silhouettes of crowd members shouting and waving dismissive hands toward a solitary center figure, suffocating conformist pressure crushing independent dissent."
    },
    {
        "name": "t12_metal_vat_flavor_aid_poison",
        "act": 4,
        "sentences": "4.09#1–#3",
        "desc": "Chiếc thùng phuy kim loại lớn đặt giữa lán trung tâm bên cạnh những gói bột giải khát và ống tiêm y tế.",
        "prompt": "Forensic still life of a large galvanized metal tub standing in the pavilion center, empty Flavor Aid paper packets, glass medicine vials, and plastic oral syringes lying on a nearby examination table, grim clinical instruments of tragedy."
    },
    {
        "name": "t12_broken_will_family_embrace",
        "act": 4,
        "sentences": "4.09#4–#6",
        "desc": "Bóng cha mẹ ôm chặt con nhỏ trong sự trống rỗng cùng cực, chiếc lồng giam lính gác bao quanh bốn phía.",
        "prompt": "Heartbreaking artistic silhouette of parents holding children close in a desperate final embrace under the pavilion shadows, armed sentries silhouetted at the exits, poignant human tragedy rendered with solemn dignity, no graphic violence."
    },
    {
        "name": "t12_haunting_silence_aftermath",
        "act": 4,
        "sentences": "4.10#1–#4",
        "desc": "Khung cảnh lán Jonestown nhìn từ xa trong sương sớm tĩnh lặng đến nghẹt thở, những chiếc lán gỗ trơ trọi giữa rừng già.",
        "prompt": "Vast solemn panoramic view of the Jonestown compound at pale blue morning dawn, complete motionless silence hanging over the wooden pavilion and surrounding jungle canopy, morning mist drifting like a shroud, respectful distant perspective."
    },
    {
        "name": "t12_forensic_agent_headphones_horror",
        "act": 4,
        "sentences": "4.10#5–#8",
        "desc": "Bóng nhân viên điều tra FBI đeo tai nghe bên máy phát băng cassette, cúi đầu trước nỗi kinh hoàng của dải băng từ.",
        "prompt": "Solemn silhouette of an FBI forensic investigator wearing bulky vintage headphones beside a portable tape recorder, head bowed in profound grief, single beam of pale flashlight illuminating the tape counter, auditory witness to horror."
    },
    {
        "name": "t12_abandoned_lectern_single_shot",
        "act": 4,
        "sentences": "4.11#1–#2",
        "desc": "Chiếc bục gỗ Jonestown trống không với một vết đạn và chiếc micro ngã đổ, kết thúc một ảo tưởng cuồng vọng.",
        "prompt": "Solemn empty lectern on the wooden stage of the abandoned pavilion, knocked-over microphone, quiet breeze blowing through the deserted rafters, final silence closing the darkest chapter of twentieth-century cults."
    },

    # =========================================================================
    # HỒI 5: BÀI HỌC ĐẮT GIÁ VỀ TÂM LÝ BẦY ĐÀN & LỜI CẢNH TỈNH (21:30 – 26:30)
    # =========================================================================
    {
        "name": "t12_memorial_918_names_monolith",
        "act": 5,
        "sentences": "5.02#1–#4",
        "desc": "Bia tưởng niệm trang nghiêm khắc ghi 918 cái tên vô tội, ánh nắng ban mai rọi qua tán cây rừng nhiệt đới.",
        "prompt": "Monumental stone memorial monolith inscribed with subtle lines representing 918 lost lives, morning sunlight breaking through green leaves above, casting golden warmth on gray stone, eternal memory and historical reflection."
    },
    {
        "name": "t12_us_capitol_congressional_hearing",
        "act": 5,
        "sentences": "5.03#1–#4",
        "desc": "Phòng điều trần Quốc hội Hoa Kỳ tại Đồi Capitol với các tập tài liệu điều tra an ninh công vụ và tư pháp.",
        "prompt": "Prestigious interior of a US Capitol congressional hearing chamber, carved wooden dais, leather chairs, thick printed bound volumes of House Foreign Affairs Committee investigation reports, solemn pursuit of legal reform."
    },
    {
        "name": "t12_vulnerability_human_compassion",
        "act": 5,
        "sentences": "5.04#1–#3",
        "desc": "Bàn tay nâng niu một đóa hoa trắng tinh khôi nhưng bị bóng gai góc của sự thao túng rình rập bao quanh.",
        "prompt": "Philosophical fine art still life of gentle cupped hands holding a pure white forest lily, while spiky predatory bramble shadows creep across the marble pedestal beneath, metaphor for the vulnerability of genuine human idealism."
    },
    {
        "name": "t12_moral_compass_unbroken",
        "act": 5,
        "sentences": "5.04#4–#5",
        "desc": "Chiếc la bàn đạo đức phát ra ánh sáng hổ phách rực rỡ, biểu tượng cho ý chí tự do và lương tri không thể bị đánh đổi.",
        "prompt": "Glowing antique brass navigational compass resting on a dark slate surface, needle pointing steadily true North, radiating a warm amber luminescence that pushes back creeping pitch-black shadows, unbroken personal conscience."
    },
    {
        "name": "t12_redflag1_total_social_isolation",
        "act": 5,
        "sentences": "5.05#2–#4",
        "desc": "Dấu hiệu cảnh báo đỏ 1: Lưới nhện sắt cắt đứt các sợi dây liên kết với gia đình và xã hội bên ngoài.",
        "prompt": "Conceptual noir warning visual: severe iron spiderweb grid severing telephone lines, mail envelopes, and family photograph strings, glowing crimson alert beacon cutting across cold slate darkness, Red Flag 1 Total Social Isolation."
    },
    {
        "name": "t12_redflag2_silenced_critical_thinking",
        "act": 5,
        "sentences": "5.05#5–#7",
        "desc": "Dấu hiệu cảnh báo đỏ 2: Đầu bút máy bị bẻ gãy trên trang giấy trắng bên chiếc khóa miệng kim loại.",
        "prompt": "Conceptual noir warning visual: broken gold fountain pen nib with spilled black ink pooling across a blank journal page, beside a heavy metal muzzle padlock, glowing crimson accent, Red Flag 2 Silenced Critical Thinking."
    },
    {
        "name": "t12_redflag3_escalating_commitment_trap",
        "act": 5,
        "sentences": "5.05#8–#10",
        "desc": "Dấu hiệu cảnh báo đỏ 3: Chiếc bẫy bánh răng cơ khí quay cuồng nuốt chửng từng đồng xu và khế ước danh dự.",
        "prompt": "Conceptual noir warning visual: interlocking heavy industrial gear teeth relentlessly dragging timepieces, gold coins, and signed pledges into dark machinery, Red Flag 3 Escalating Commitment Sunk Cost Trap."
    },
    {
        "name": "t12_redflag4_fortress_paranoia_wall",
        "act": 5,
        "sentences": "5.05#11–#13",
        "desc": "Dấu hiệu cảnh báo đỏ 4: Bức tường thành gai góc vây kín với những lỗ châu mai nhìn ra thế giới trong sự hoang tưởng.",
        "prompt": "Conceptual noir warning visual: jagged stone fortress parapet lined with defensive embrasures peering out at a harmless world shrouded in paranoid shadows, glowing crimson alert hue, Red Flag 4 Us Versus The World Mentality."
    },
    {
        "name": "t12_independent_mind_dawn_freedom",
        "act": 5,
        "sentences": "5.05#14",
        "desc": "Đôi bàn tay phá vỡ xiềng xích vô hình, vươn về phía bầu trời tự do bao la ngập tràn ánh nắng bình minh.",
        "prompt": "Inspiring triumphant composition of silhouetted hands breaking apart severed iron chain links, fragments dissolving into light, radiant golden amber sunrise cresting a peaceful ocean horizon, sovereign independent mind."
    },
    {
        "name": "t12_amber_eyes_closing_dossier_jonestown",
        "act": 5,
        "sentences": "5.05#15–#17",
        "desc": "Tập hồ sơ Amber Eyes khép lại trang nghiêm với biểu tượng đôi mắt cú hổ phách bừng sáng trên nền nhung đen.",
        "prompt": "Signature Amber Eyes closing scene, dark leather-bound case file folder closing on a dark oak desk, glowing golden amber owl eye circular emblem illuminating the leather cover, elegant noir documentary insignia, fine film grain."
    }
]

def main():
    WORK.mkdir(parents=True, exist_ok=True)
    
    bg_jobs_path = WORK / "bg_jobs_tap12.json"
    bg_jobs_path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo {bg_jobs_path} ({len(jobs)} jobs) thành công!")

    # Tạo gemini_image_prompts_tap12.json
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

    gemini_prompts_path = WORK / "gemini_image_prompts_tap12.json"
    gemini_prompts_path.write_text(json.dumps(gemini_prompts, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo {gemini_prompts_path} ({len(gemini_prompts)} prompts) thành công!")

if __name__ == "__main__":
    main()
