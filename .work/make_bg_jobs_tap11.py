import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

jobs = [
    # =========================================================================
    # HỒI 1: VỎ BỌC HOÀN HẢO CỦA "CẶP ĐÔI KEN & BARBIE" (00:00 – 05:30)
    # =========================================================================
    {
        "name": "t11_pink_house_57_bayview",
        "act": 1,
        "sentences": "1.02#1",
        "desc": "Ngôi nhà màu hồng số 57 Đại lộ Bayview Drive tại thị trấn ven hồ Port Dalhousie trong nắng mai thập niên 1990.",
        "prompt": "Cinematic 16:9 wide shot of a charming suburban pink two-story house with manicured green lawn at 57 Bayview Drive in Port Dalhousie Ontario, early 1990s morning sunlight, peaceful Lake Ontario breeze in trees, dark graphic novel noir style, fine film grain, subtle ominous shadows creeping along the foundation."
    },
    {
        "name": "t11_suburban_admiration_facade",
        "act": 1,
        "sentences": "1.02#2",
        "desc": "Khu dân cư trung lưu thanh bình ven hồ Ontario với những hàng cây rợp bóng và ánh nhìn ngưỡng mộ của xóm giềng.",
        "prompt": "Atmospheric establishing shot of an affluent quiet lakeside neighborhood in Ontario, silhouetted neighbors walking dogs past white picket fences, idyllic middle-class suburban perfection, high-contrast chiaroscuro linework, muted amber and slate gray tones."
    },
    {
        "name": "t11_paul_bernardo_dashing_car",
        "act": 1,
        "sentences": "1.02#3",
        "desc": "Bóng người đàn ông lịch lãm trong bộ âu phục bên chiếc xe thể thao bóng loáng dưới ánh đèn đường ngoại ô.",
        "prompt": "Sleek dark noir composition showing the sharp silhouette of a well-dressed young man in a tailored suit leaning against a gleaming sports coupe under a warm streetlamp, shiny metallic reflections, face concealed in shadow, aura of arrogant vanity."
    },
    {
        "name": "t11_narcissistic_mirror_vanity",
        "act": 1,
        "sentences": "1.02#4",
        "desc": "Góc nhìn phòng thay đồ sang trọng, lược chải tóc mạ vàng và chiếc gương phản chiếu bóng lưng chải chuốt kiêu hãnh.",
        "prompt": "Intimate noir still life of an opulent dressing room table, ornate gold-rimmed mirror, vintage cologne bottles, gold comb, and the back silhouette of a man styling his hair, harsh dramatic raking light, graphic novel ink contours."
    },
    {
        "name": "t11_karla_veterinary_clinic",
        "act": 1,
        "sentences": "1.02#5",
        "desc": "Bóng cô gái trẻ trong chiếc áo blouse trắng tại phòng khám thú y bên khung cửa sổ ngập nắng ấm áp.",
        "prompt": "Subtle interior shot of a clean 1990s veterinary clinic, warm afternoon sunbeams streaming through blinds, silhouetted blonde young woman in a medical smock gently tending an animal kennel, facade of pure angelic innocence, heavy ink crosshatching."
    },
    {
        "name": "t11_ken_barbie_golden_illusion",
        "act": 1,
        "sentences": "1.02#6",
        "desc": "Hai con búp bê biểu tượng Ken và Barbie đặt trên bệ kính phủ rèm nhung, ánh sáng vàng óng ả nhưng bóng đổ dài ma quái.",
        "prompt": "Symbolic conceptual still life of pristine vintage blonde male and female fashion dolls standing atop a polished mahogany plinth, golden stage spotlight casting elongated twisted claw-like shadows against the velvet wall, poignant noir irony."
    },
    {
        "name": "t11_fairytale_wedding_carriage",
        "act": 1,
        "sentences": "1.04#1",
        "desc": "Cỗ xe ngựa trắng và hàng trăm đóa hoa hồng trong đám cưới mùa hè 1991, khung cảnh cổ tích huyền ảo.",
        "prompt": "Panoramic nostalgic shot of an ornate white horse-drawn wedding carriage adorned with pale roses moving down an oak-lined avenue, summer 1991 fairytale wedding aesthetic, dreamy desaturated amber glow, dark ink outlines, underlying chilling tension."
    },
    {
        "name": "t11_society_gala_inseparable_couple",
        "act": 1,
        "sentences": "1.04#2",
        "desc": "Bóng đôi vợ chồng trẻ quấn quýt bên nhau trong dạ tiệc khiêu vũ, tâm điểm của sự trầm trồ ngưỡng mộ.",
        "prompt": "Suburban social hall gala scene, golden chandelier overhead casting radiant light on the intertwined silhouettes of a glamorous young couple dancing closely, envious onlookers in shadow, dark graphic novel noir aesthetic."
    },
    {
        "name": "t11_blind_adoration_shadow",
        "act": 1,
        "sentences": "1.04#3–#4",
        "desc": "Bóng người phụ nữ cúi mình trước ngai vàng quyền lực đen tối trong phòng khách mờ ảo, sự tôn sùng mù quáng.",
        "prompt": "Psychological noir silhouette art: A young woman bowing in complete reverence toward a looming dark silhouette seated in a high-backed armchair, domestic parlor shrouded in deep chiaroscuro, themes of toxic subservience and warped adoration."
    },
    {
        "name": "t11_closed_pink_door_abyss",
        "act": 1,
        "sentences": "1.04#5–#6",
        "desc": "Cánh cửa sơn hồng đóng kín hé lộ khe tối sâu thẳm bên trong, tương phản giữa vẻ ngoài kẹo ngọt và vực thẳm tội ác.",
        "prompt": "Foreboding composition of a pastel pink painted front door with brass lion door-knocker, cracked open just a sliver into pitch-black interior void, stark contrast between cheerful exterior facade and yawning darkness within."
    },
    {
        "name": "t11_lakeside_evening_dog_walk",
        "act": 1,
        "sentences": "1.05#1–#2",
        "desc": "Bờ hồ Ontario bảng lảng chiều tà, bóng cặp đôi tay trong tay dắt hai chú chó đi dạo bên sóng nước dập dềnh.",
        "prompt": "Mellow dusk scene on the stony shore of Lake Ontario, cool slate water gently lapping the breakwater, silhouettes of a young couple holding hands walking two golden retrievers along the promenade, tranquil deceptive harmony."
    },
    {
        "name": "t11_backyard_barbecue_lawn",
        "act": 1,
        "sentences": "1.05#3–#4",
        "desc": "Bữa tiệc nướng sân sau với khói lam chiều ấm cúng, bàn ăn ngoài trời phủ hoa cỏ của khu phố kiểu mẫu.",
        "prompt": "Backyard garden scene of an idyllic suburban evening gathering, soft smoke curling from a vintage barbecue grill, wooden picnic table laden with drinks and fruit, string lanterns glowing warmly in twilight, noir graphic novel linework."
    },
    {
        "name": "t11_lace_curtain_window_illusion",
        "act": 1,
        "sentences": "1.05#5–#6",
        "desc": "Khung cửa sổ rèm hoa vintage thắt nơ tinh tế, ánh đèn ấm cúng che giấu chiếc mặt nạ lừa dối cả cộng đồng.",
        "prompt": "Close-up exterior view of a quaint sash window framed by delicate floral lace curtains tied with satin bows, warm golden incandescent light glowing from within, subtle ominous diagonal blinds shadow, fragile domestic illusion."
    },
    {
        "name": "t11_scarborough_nocturnal_shadow",
        "act": 1,
        "sentences": "1.07#1–#3",
        "desc": "Vùng ngoại ô Scarborough chìm trong màn sương đêm lạnh lẽo, bóng đen đột nhập lén lút qua rèm cửa sổ.",
        "prompt": "Dark nocturnal cityscape of Scarborough suburbs late 1980s, misty rain slicking the pavement, cold indigo and obsidian palette, menacing shadowy figure slipping between quiet residential homes, palpable suspense, graphic novel chiaroscuro."
    },
    {
        "name": "t11_scarborough_taskforce_archive",
        "act": 1,
        "sentences": "1.08#1–#2",
        "desc": "Bàn điều tra chuyên án đặc nhiệm Scarborough với bản đồ ghim cờ đỏ dán tường và hồ sơ truy tìm không dấu vân tay.",
        "prompt": "Investigation room still life: Giant wall map of Scarborough and Toronto suburbs peppered with red pushpins and red yarn, forensic case binders stacked on steel desk, desk lamp casting harsh directional light, solemn police procedural noir."
    },
    {
        "name": "t11_lake_gibson_fog_depths",
        "act": 1,
        "sentences": "1.08#3–#4",
        "desc": "Vùng hồ Lake Gibson âm u trong làn sương mù sớm, bóng mặt nước phẳng lặng che giấu đáy hồ sâu thẳm.",
        "prompt": "Eerie early dawn view of Lake Gibson shrouded in thick morning fog, cold dark waters, silhouetted weeping willows and reeds lining the bank, quiet forensic gravity, muted steel-blue and charcoal palette, fine film grain."
    },
    {
        "name": "t11_church_parking_lot_ambush",
        "act": 1,
        "sentences": "1.08#5–#7",
        "desc": "Bãi đỗ xe nhà thờ St. Catharines vắng lặng trong cơn mưa chiều tháng 4, chiếc cặp nữ sinh rơi bên lề đường.",
        "prompt": "Somatic April rain scene in an empty church parking lot in St. Catharines, gothic church steeple looming in misty gray background, solitary school backpack lying abandoned on wet asphalt puddles reflecting sullen overcast sky."
    },
    {
        "name": "t11_map_proximity_dark_crossroads",
        "act": 1,
        "sentences": "1.09#1–#5",
        "desc": "Bản đồ khu vực Niagara với vòng tròn khoanh đỏ nối ngôi nhà số 57 Bayview với các địa điểm chấn động, bóng đen bao trùm.",
        "prompt": "Overhead cartographic noir composition: Vintage Niagara Regional road map, red marker circling Port Dalhousie and Bayview Drive mere kilometers from crime scene coordinates, creeping black ink stain slowly engulfing the paper."
    },

    # =========================================================================
    # HỒI 2: CHIẾC MẶT NẠ RƠI XUỐNG VÀ THỎA THUẬN VỚI QUỶ DỮ (05:30 – 11:00)
    # =========================================================================
    {
        "name": "t11_flashlight_shattered_hallway",
        "act": 2,
        "sentences": "2.02#1–#3",
        "desc": "Chiếc đèn pin kim loại cỡ lớn rơi trên sàn gỗ hành lang giữa những mảnh vỡ đồ đạc, vết nứt đầu tiên của cặp đôi vàng.",
        "prompt": "Tense interior crime scene still life: Heavy industrial metal Maglite flashlight resting on polished oak floor among scattered glass shards and overturned hallway chair, beam of dying yellow light slicing across shadows, January 1993 domestic fracture."
    },
    {
        "name": "t11_st_catharines_hospital_night",
        "act": 2,
        "sentences": "2.04#1–#2",
        "desc": "Bệnh viện St. Catharines trong đêm mưa gió, ánh đèn cấp cứu đỏ hắt qua vũng nước loang trên mặt đường.",
        "prompt": "Exterior nocturnal shot of St. Catharines General Hospital emergency entrance in pouring rain, emergency red beacon reflecting off wet asphalt, ambulance bay canopy, somber medical sanctuary, graphic noir chiaroscuro."
    },
    {
        "name": "t11_escape_to_parents_porch",
        "act": 2,
        "sentences": "2.04#3",
        "desc": "Ngôi nhà cha mẹ đẻ trong đêm đông lạnh giá, chiếc valy vội vã để lại bậc thềm trước khi bước vào nương náu.",
        "prompt": "Cold winter night scene at a modest suburban bungalow porch, dusting of snow on wooden steps, packed leather suitcase left hastily by the glowing front door, refuge from terror, dark ink lines."
    },
    {
        "name": "t11_february_arrest_dna_match",
        "act": 2,
        "sentences": "2.04#4–#5",
        "desc": "Mẫu tinh thể DNA và kính hiển vi phòng thí nghiệm pháp y đối chiếu với hồ sơ bắt giữ Paul Bernardo ngày 17/02/1993.",
        "prompt": "High-contrast forensic laboratory table: Optical microscope illuminating an autoradiograph DNA autoradiogram membrane film, matching bands highlighted under ultraviolet glow, arrest warrant dossier dated February 17, 1993."
    },
    {
        "name": "t11_interrogation_bruised_facade",
        "act": 2,
        "sentences": "2.05#1–#3",
        "desc": "Bóng người phụ nữ gục đầu trong văn phòng luật sư với khăn tay đẫm nước mắt, tạo dựng hình ảnh nạn nhân đáng thương.",
        "prompt": "Interior interrogation room noir: Silhouette of a young woman with head bowed weeping into a white handkerchief at a long conference table, two sharp-suited defense attorneys flanking her, dramatic raking side-light carving deep shadows."
    },
    {
        "name": "t11_pleading_victim_tears",
        "act": 2,
        "sentences": "2.05#4–#6",
        "desc": "Góc nhìn cận cảnh chiếc khăn tay thấm nước mắt bên tách trà nguội trên bàn thẩm vấn, vở kịch vô tội hoàn hảo.",
        "prompt": "Still life macro shot: Crumpled linen handkerchief damp with tears beside a cold cup of tea and yellow legal notepad covered in hasty handwriting, calculated presentation of absolute innocence, heavy black ink rendering."
    },
    {
        "name": "t11_battered_woman_syndrome_file",
        "act": 2,
        "sentences": "2.06#1–#3",
        "desc": "Tập hồ sơ chẩn đoán 'Hội chứng Người phụ nữ bị Bạo hành' với bút phê của chuyên gia tâm thần học.",
        "prompt": "Forensic psychiatric evaluation folder marked with psychological assessment stamps, clinical notes on Battered Woman Syndrome and trauma coercion, brass spectacles resting on the cover, clinical sterile lighting."
    },
    {
        "name": "t11_hostage_puppet_facade",
        "act": 2,
        "sentences": "2.06#4–#5",
        "desc": "Bức tranh ẩn dụ bóng người phụ nữ bị xiềng xích vô hình, tấm lá chắn pháp lý che đậy sự đồng lõa ác tính.",
        "prompt": "Metaphorical noir graphic art: Slender female silhouette enveloped in delicate porcelain doll ribbons simulating puppet strings, shielding her from an ominous storm, deceptive construction of the helpless captive persona."
    },
    {
        "name": "t11_fragile_beauty_manipulation",
        "act": 2,
        "sentences": "2.07#1–#2",
        "desc": "Chiếc mặt nạ thạch cao thiên thần trắng muốt nứt rạn đặt trên nền bàn gỗ đen, biểu tượng sự thao túng lòng trắc ẩn.",
        "prompt": "Symbolic artwork of a pristine classical plaster angel mask with serene beautiful features, fine hairline fracture splitting down the cheek, resting on dark ebony velvet, dark chiaroscuro exploring weaponized sympathy."
    },
    {
        "name": "t11_weaponized_victim_playing",
        "act": 2,
        "sentences": "2.07#3–#5",
        "desc": "Cán cân công lý bị nghiêng lệch bởi những giọt nước mắt giả tạo, đỉnh cao của kỹ thuật thao túng đóng vai nạn nhân.",
        "prompt": "Conceptual noir visual: Antique brass scales of justice tipping dramatically under the weight of crystal tears and fragile silk ribbons, heavy steel gavel resting in deep shadow, masterclass in legal manipulation."
    },
    {
        "name": "t11_missing_evidence_dilemma",
        "act": 2,
        "sentences": "2.08#1–#2",
        "desc": "Bàn làm việc của điều tra viên với những tập hồ sơ còn thiếu bằng chứng then chốt, áp lực nghẹt thở của thời gian.",
        "prompt": "Moody overhead shot of a homicide detective desk covered in open evidence envelopes, black-and-white field photos, magnifying glass over empty fingerprint cards, desperate search for missing links in double homicide."
    },
    {
        "name": "t11_prosecution_clock_pressure",
        "act": 2,
        "sentences": "2.08#3–#5",
        "desc": "Chiếc đồng hồ cát và những dòng tít báo chí dồn dập, cơ quan công tố đánh mất sự cẩn trọng nghề nghiệp.",
        "prompt": "Tense visual metaphor: Vintage brass hourglass with sands running out rapidly against a wall of urgent newspaper headlines demanding immediate justice, ticking pressure driving flawed prosecutorial compromise."
    },
    {
        "name": "t11_deal_with_the_devil_contract",
        "act": 2,
        "sentences": "2.09#1–#3",
        "desc": "Bản thỏa thuận nhận tội tháng 05/1993 ký giữa Tổng chưởng lý và Karla Homolka, bản án 12 năm đổi lấy lời khai.",
        "prompt": "Formal legal document still life: The infamous May 1993 Ontario Ministry of the Attorney General plea agreement titled Manslaughter Plea Accord, fountain pen resting across signature line, dark ominous crimson and charcoal noir palette, Deal with the Devil."
    },

    # =========================================================================
    # HỒI 3: GIẢI MÃ HỘI CHỨNG ĐIÊN CUỒNG ĐÔI (FOLIE À DEUX) (11:00 – 16:30)
    # =========================================================================
    {
        "name": "t11_half_truth_dossier_shadow",
        "act": 3,
        "sentences": "3.02#1–#3",
        "desc": "Tập hồ sơ lời khai mở ra một nửa dưới bóng tối chiếc đèn bàn, hé lộ bức màn tâm thần học ma quái.",
        "prompt": "Intriguing chiaroscuro shot of a half-opened case file illuminated by an amber banker lamp, half the page bathed in golden light and the other half swallowed in impenetrable pitch-black shadow, duality of truth."
    },
    {
        "name": "t11_folie_a_deux_resonance",
        "act": 3,
        "sentences": "3.03#1–#2",
        "desc": "Hai chiếc bóng đối xứng giao thoa trong buồng cộng hưởng xoắn ốc ma mị, biểu tượng Hội chứng Điên cuồng đôi.",
        "prompt": "Abstract psychological noir illustration of Folie à Deux: Two human head profiles facing each other in silhouette, dark spiraling energy vortices and concentric sound waves resonating between them, mutually reinforcing madness."
    },
    {
        "name": "t11_destructive_flame_alliance",
        "act": 3,
        "sentences": "3.03#3–#5",
        "desc": "Ngọn lửa đen bùng cháy từ hai nhánh bấc quyện vào nhau, sự khuếch đại tội ác xóa bỏ mọi ranh giới lương tri.",
        "prompt": "Surreal conceptual artwork: Two braided candle wicks intertwining to produce an intense towering black-and-crimson flame, incinerating moral boundaries, dark graphic novel linework, ominous power."
    },
    {
        "name": "t11_malignant_narcissist_throne",
        "act": 3,
        "sentences": "3.04#1–#3",
        "desc": "Chiếc ngai vàng đen tối trong tâm trí kẻ ái kỷ cuồng quyền lực, bóng bàn tay muốn thống trị sinh mạng đồng loại.",
        "prompt": "Metaphorical noir piece: High-backed gothic armchair resembling an obsidian throne, towering shadow behind it stretching forward with grasping fingers, obsession with absolute control and grandiosity."
    },
    {
        "name": "t11_obedient_accomplice_strings",
        "act": 3,
        "sentences": "3.04#4",
        "desc": "Những sợi dây rối vô hình gắn kết giữa hai kẻ lệch lạc, mối quan hệ cộng sinh độc hại.",
        "prompt": "Symbolic composition of two marionette crossbars linked by tangled red cords, one puppet guiding the other in a grim dance, fatal codependency of malignant narcissist and devoted enabler."
    },
    {
        "name": "t11_covert_sociopath_profile",
        "act": 3,
        "sentences": "3.05#1–#2",
        "desc": "Sơ đồ giải phẫu tâm thần học bộc lộ chứng thái nhân cách ngầm và sự thiếu hụt hoàn toàn cảm giác tội lỗi.",
        "prompt": "Forensic psychiatric profile chart: Stylized brain anatomical diagram with cold blue zones indicating zero empathy and absence of remorse, stark graphic noir ink, clinical detachment."
    },
    {
        "name": "t11_morbid_thrill_abyss",
        "act": 3,
        "sentences": "3.05#3–#4",
        "desc": "Cửa sổ phòng ngủ nhìn ra màn đêm thăm thẳm, sự kích thích trước quyền lực tàn bạo và nỗi sợ hãi bệnh lý bị bỏ rơi.",
        "prompt": "Interior window looking out into a raging dark thunderstorm over lake waters, silhouette of a woman standing at the glass transfixed by lightning flashes, morbid fascination with danger and terror of abandonment."
    },
    {
        "name": "t11_toxic_devotion_cruelty",
        "act": 3,
        "sentences": "3.05#5–#6",
        "desc": "Chiếc nhẫn cưới bằng thép gai đặt cạnh hoa khô tàn úa, biểu tượng lòng trung thành mù quáng và tàn nhẫn.",
        "prompt": "Poignant still life: An unpolished barbed-wire band mimicking a wedding ring coiled around withered black roses on an antique lace cloth, cruelty masquerading as unconditional devotion."
    },
    {
        "name": "t11_christmas_1990_halothane_bottle",
        "act": 3,
        "sentences": "3.06#1–#3",
        "desc": "Lọ thuốc mê Halothane đánh cắp từ phòng khám thú y đặt cạnh ly rượu Giáng sinh 1990 tại tư gia Homolka.",
        "prompt": "Chilling forensic still life of Christmas Eve 1990: A vintage amber medical bottle labeled Halothane veterinary anesthetic standing beside an ornate crystal wine goblet on a festive mahogany sideboard, heavy chiaroscuro ink."
    },
    {
        "name": "t11_silent_christmas_tragedy",
        "act": 3,
        "sentences": "3.06#4",
        "desc": "Cây thông Noel mờ ảo trong phòng khách vắng lặng sau cơn bi kịch ngạt thở của cô em gái mười lăm tuổi.",
        "prompt": "Haunting quiet interior: Modest 1990 Christmas tree with faint glowing bulbs in a darkened suburban living room, gifts unopened under branches, profound somber stillness, cold midnight air."
    },
    {
        "name": "t11_chilling_polaroid_camera",
        "act": 3,
        "sentences": "3.06#5–#7",
        "desc": "Chiếc máy ảnh chụp lấy liền Polaroid nằm trên mặt bàn bên găng tay cao su, sự máu lạnh tột cùng phản bội máu mủ.",
        "prompt": "Forensic macabre still life: Vintage 1980s Polaroid instant camera resting next to white latex gloves and folded paper towels on a kitchen counter, clinical cold lighting, unconscionable moral betrayal."
    },
    {
        "name": "t11_grieving_parents_wedding_mask",
        "act": 3,
        "sentences": "3.07#1–#3",
        "desc": "Bức ảnh cưới lộng lẫy đặt cạnh di ảnh người em gái trong cùng một ngôi nhà, sự dối trá đến gai người.",
        "prompt": "Framed photo still life on a family mantelpiece: An ornate silver frame holding a lavish wedding portrait resting beside a small brass memorial urn and black ribbon, horrifying juxtaposition of celebration and complicity."
    },
    {
        "name": "t11_unholy_sacrament_altar",
        "act": 3,
        "sentences": "3.08#1–#4",
        "desc": "Bàn thờ tình yêu biến thái bị bao bọc trong bóng tối, nơi mọi lương tri bị thiêu rụi bởi thứ tôn giáo tội ác.",
        "prompt": "Atmospheric symbolic visual: Dark domestic shrine surrounded by flickering black tapers, shadows converging into a grotesque temple of shared psychosis, destruction of human conscience."
    },
    {
        "name": "t11_frozen_justice_gavel",
        "act": 3,
        "sentences": "3.09#1–#3",
        "desc": "Chiếc búa công lý bị đóng băng dưới lớp tuyết lạnh Ontario, trước khi bước ngoặt định mệnh xuất hiện.",
        "prompt": "Poignant symbolic noir: Judicial wooden gavel coated in a thick layer of frosted winter ice resting on stone court steps, snowflakes drifting through blue moonlight, impending judicial unraveling."
    },

    # =========================================================================
    # HỒI 4: SÁU CUỐN BĂNG TRÊN TRẦN NHÀ VÀ SỰ SỤP ĐỔ CỦA MỘT ẢO TƯỞNG (16:30 – 21:30)
    # =========================================================================
    {
        "name": "t11_six_8mm_tapes_bag",
        "act": 4,
        "sentences": "4.02#1–#2",
        "desc": "Chiếc túi vải chứa sáu cuộn băng video 8mm định mệnh được luật sư John Rosen bàn giao cho cảnh sát mùa thu 1994.",
        "prompt": "Forensic evidence handover still life: Brown canvas duffel bag unzipped on police evidence locker counter revealing six 8mm magnetic video cassette tapes in plastic cases, autumn 1994 turning point, stark graphic noir."
    },
    {
        "name": "t11_bathroom_ceiling_vent_hiding",
        "act": 4,
        "sentences": "4.03#1–#2",
        "desc": "Chiếc quạt thông gió trần phòng tắm hé mở, để lộ hốc bí mật nơi sáu cuộn băng bị che giấu suốt nhiều năm.",
        "prompt": "Low-angle dramatic shot looking up at a bathroom ceiling exhaust fan grille hanging open by a single screw, dark hidden hollow cavity behind sheetrock insulation, beam of inspection flashlight cutting through dust."
    },
    {
        "name": "t11_ken_murray_obstruction_charge",
        "act": 4,
        "sentences": "4.03#3–#5",
        "desc": "Bàn làm việc luật sư với ngăn kéo khóa kín cất giấu tang vật 17 tháng và cáo trạng cản trở công lý.",
        "prompt": "Legal study interior: Heavy oak desk with a locked steel drawer partially ajar, legal indictment document citing Obstruction of Justice against attorney Ken Murray, heavy solemn shadows."
    },
    {
        "name": "t11_dark_screening_room_projector",
        "act": 4,
        "sentences": "4.04#1–#3",
        "desc": "Chùm sáng từ máy chiếu 8mm cắt ngang căn phòng tối, bóng các điều tra viên ngồi chết lặng trước màn hình.",
        "prompt": "Cinematic wide shot of a pitch-black police viewing room, bright white projector beam cutting horizontally through floating cigarette smoke, dark silhouettes of detectives and Crown attorneys frozen in horrified disbelief."
    },
    {
        "name": "t11_investigator_nausea_monitor",
        "act": 4,
        "sentences": "4.05#1–#3",
        "desc": "Góc nhìn từ sau lưng nhân viên điều tra run rẩy nhìn vào màn hình CRT phát sáng trong đêm, sự thật trần trụi.",
        "prompt": "Over-the-shoulder noir shot of an investigator clutching the desk edge in revulsion, staring at a vintage CRT monitor glowing cold blue in dark room, screen reflected in trembling glasses, shattering of illusions."
    },
    {
        "name": "t11_holding_video_camera_director",
        "act": 4,
        "sentences": "4.05#4–#5",
        "desc": "Bóng bàn tay cầm chiếc máy quay phim gia đình 8mm, kẻ chỉ đạo chủ động và hào hứng trong tội ác.",
        "prompt": "Striking noir silhouette: Hands firmly operating a compact 1990s 8mm handheld camcorder with red recording LED glowing bright, positioned with authoritative poise, active director of terror."
    },
    {
        "name": "t11_triumphant_smile_deal_with_devil",
        "act": 4,
        "sentences": "4.05#6–#9",
        "desc": "Ánh sáng màn hình phản chiếu bản thỏa thuận nhận tội bị xé toạc trong tâm tưởng, nỗi cay đắng của công lý.",
        "prompt": "Metaphorical psychological visual: A torn parchment of the plea bargain agreement crumbling into ash, backlit by the eerie static glow of an interrogation monitor, bitter sting of being utterly duped by a monster."
    },
    {
        "name": "t11_equal_partner_in_cruelty",
        "act": 4,
        "sentences": "4.07#1–#3",
        "desc": "Hai chiếc ghế ngang hàng trong phòng thu bằng chứng, phơi bày quan hệ đối tác bình đẳng và khoái cảm quyền lực đen tối.",
        "prompt": "Stark symbolic set: Two identical steel interrogation chairs placed side by side under a single hanging bare bulb, equal partnership in malevolence, dismantling the battered woman myth with chilling finality."
    },
    {
        "name": "t11_mockery_of_justice_tears",
        "act": 4,
        "sentences": "4.07#4–#5",
        "desc": "Chiếc mặt nạ kịch nghệ vỡ vụn trên bục nhân chứng, những giọt nước mắt tại tòa chỉ là màn diễn xuất vị kỷ.",
        "prompt": "Courtroom witness stand empty under dramatic top light, shattered theatrical mask lying on the wood ledge beside microphone, legal process reduced to a calculated sociopathic stage play."
    },
    {
        "name": "t11_outraged_citizens_protest",
        "act": 4,
        "sentences": "4.08#1–#3",
        "desc": "Biển người biểu tình mang biểu ngữ đòi công lý cho Leslie Mahaffy và Kristen French trước tòa nhà Quốc hội Ontario.",
        "prompt": "Panoramic street protest outside Ontario Queen's Park Legislature, sea of silhouetted citizens holding placards demanding justice for young victims, autumn mist, emotional anguish and public fury, graphic novel noir."
    },
    {
        "name": "t11_constitutional_legal_deadlock",
        "act": 4,
        "sentences": "4.09#1–#3",
        "desc": "Cuốn sách luật hiến pháp và chiếc còng số tám bị khóa chặt, cái bẫy tư pháp không lối thoát bảo vệ kẻ thủ ác.",
        "prompt": "Legal still life: Heavy leatherbound Canadian Criminal Code volume with heavy padlock clamped across its binding, scales of justice trapped in an unbreakable legal gridlock, solemn institutional tragedy."
    },
    {
        "name": "t11_dangerous_offender_life_sentence",
        "act": 4,
        "sentences": "4.10#1–#2",
        "desc": "Bản án chung thân không ân xá và dấu mộc 'Dangerous Offender' giam giữ vô thời hạn Paul Bernardo tại nhà tù Kingston.",
        "prompt": "Judicial verdict document dated September 1, 1995: Bold red rubber stamp reading DANGEROUS OFFENDER - INDEFINITE DETENTION, iron prison key resting on parchment, heavy prison bars in background."
    },
    {
        "name": "t11_calendar_counting_to_freedom",
        "act": 4,
        "sentences": "4.10#3",
        "desc": "Tờ lịch nhà tù với những ô ngày bị gạch chéo, người đàn bà trong ngôi nhà màu hồng đếm ngược ngày về tự do.",
        "prompt": "Prison cell wall still life: Wall calendar with dates crossed off with red pen leading toward year 2005, shaft of barred sunlight illuminating the countdown to early freedom, profound moral contrast."
    },

    # =========================================================================
    # HỒI 5: BÀI HỌC ĐẮT GIÁ VỀ MẶT NẠ NẠN NHÂN & LỜI CẢNH TỈNH (21:30 – 26:30)
    # =========================================================================
    {
        "name": "t11_joliette_prison_gate_release",
        "act": 5,
        "sentences": "5.02#1–#3",
        "desc": "Cánh cổng sắt Trại cải tạo Nữ Joliette mở ra ngày 04/07/2005, bóng người phụ nữ bước ra giữa rừng ống kính truyền thông.",
        "prompt": "Exterior morning shot of the imposing steel gates of Joliette Institution for Women swinging open on July 4, 2005, silhouette of a woman walking out into a barrage of press telephoto lenses and flashing strobes."
    },
    {
        "name": "t11_haunted_new_identity_shadow",
        "act": 5,
        "sentences": "5.02#4–#6",
        "desc": "Hộ chiếu mang tên mới Leanne Teale đặt trên mặt bàn, nhưng bóng đen quá khứ vẫn phủ kín không thể xóa nhòa.",
        "prompt": "Still life of a new Canadian passport opened to an identity page bearing the name Leanne Teale, surrounded by permanent looming shadows of past crimes, eternal moral exile and social ostracism."
    },
    {
        "name": "t11_galligan_inquiry_report_reforms",
        "act": 5,
        "sentences": "5.03#1–#4",
        "desc": "Báo cáo thẩm tra độc lập của Thẩm phán Patrick Galligan năm 1996, cuộc cải cách triệt để quy trình thương lượng nhận tội.",
        "prompt": "Dignified study still life: Bound judicial inquiry volume titled The Galligan Inquiry Report 1996, brass judicial scales and Supreme Court seal, beacon of legal reform rising from profound tragedy."
    },
    {
        "name": "t11_victim_playing_camouflage_mirror",
        "act": 5,
        "sentences": "5.04#1–#3",
        "desc": "Tấm gương hai mặt: một bên là giọt nước mắt mong manh, một bên là móng vuốt của kẻ săn mồi đội lốt nạn nhân.",
        "prompt": "Surreal dual psychological portrait: Antique two-way mirror splitting the frame; left side shows delicate tearful reflection, right side reveals cold predator silhouette, unmasking Victim Playing."
    },
    {
        "name": "t11_disguised_predator_scales",
        "act": 5,
        "sentences": "5.04#4–#5",
        "desc": "Cán cân phân định giữa nạn nhân chân chính và kẻ săn mồi mang mặt nạ yếu đuối, sự cảnh tỉnh nghiêm khắc.",
        "prompt": "Conceptual noir artwork: Beam of truth illuminating a sharp distinction between a wounded dove and a coiled viper concealed beneath white fleece, severe psychological warning."
    },
    {
        "name": "t11_amber_eyes_redflag_intro",
        "act": 5,
        "sentences": "5.05#1",
        "desc": "Biểu tượng Amber Eyes rực sáng trên nền đen huyền bí, dẫn nhập 4 dấu hiệu cảnh báo đỏ nhận diện kẻ thao túng.",
        "prompt": "Minimalist graphic noir title card: Iconic golden Amber Eyes owl gaze piercing through atmospheric charcoal mist, brass compass and warning beacons lighting up the dark."
    },
    {
        "name": "t11_redflag1_evading_accountability",
        "act": 5,
        "sentences": "5.05#2–#4",
        "desc": "Dấu hiệu cảnh báo 1: Chiếc khiên tổn thương dùng để cản phá mọi chất vấn pháp lý và né tránh trách nhiệm.",
        "prompt": "Conceptual graphic noir art for Red Flag 1: A cracked porcelain shield inscribed with tears deflecting arrows of legitimate inquiry, evading accountability behind manufactured suffering."
    },
    {
        "name": "t11_redflag2_words_vs_actions_split",
        "act": 5,
        "sentences": "5.05#5–#7",
        "desc": "Dấu hiệu cảnh báo 2: Sự phân đôi giữa lời nói ngọt ngào trước đám đông và hành vi lạnh lùng toan tính trong bóng tối.",
        "prompt": "Striking graphic art for Red Flag 2: Split composition showing sweet honey dripping from silver lips in public light, while dark iron gears calculate ruthlessly in subterranean shadow."
    },
    {
        "name": "t11_redflag3_guilt_tripping_trap",
        "act": 5,
        "sentences": "5.05#8–#10",
        "desc": "Dấu hiệu cảnh báo 3: Chiếc bẫy cảm giác tội lỗi giăng ra để bẻ gãy mọi sự nghi ngờ chính đáng của người khác.",
        "prompt": "Dramatic symbolic noir for Red Flag 3: Delicate spiderweb woven of guilt threads ensnaring a questioning compass, turning righteous inquiry into self-blame, psychological manipulation trap."
    },
    {
        "name": "t11_redflag4_toxic_symbiosis_abyss",
        "act": 5,
        "sentences": "5.05#11–#13",
        "desc": "Dấu hiệu cảnh báo 4: Vực thẳm của mối quan hệ cộng sinh độc hại, nơi tình yêu bị đánh đổi bằng việc hủy hoại lương tri.",
        "prompt": "Emotional graphic noir art for Red Flag 4: Two figures holding hands standing on the precipice of a jagged rocky chasm, blind loyalty leading step by step into the abyss of moral destruction."
    },
    {
        "name": "t11_light_of_justice_prevails",
        "act": 5,
        "sentences": "5.05#14",
        "desc": "Ngọn đèn bão công lý bừng sáng đẩy lùi bóng tối ma quỷ, chân lý lương tri chiến thắng những giọt nước mắt cá sấu.",
        "prompt": "Triumphant chiaroscuro composition: Sturdy brass hurricane lantern blazing with warm amber light, dispelling thick black mist and crocodile tear mirages, moral clarity and truth prevailing."
    },
    {
        "name": "t11_amber_eyes_closing_dossier_bernardo",
        "act": 5,
        "sentences": "5.05#15–#17",
        "desc": "Tập hồ sơ Amber Eyes khép lại trang nghiêm trên bàn gỗ sồi, biểu tượng mắt cú hổ phách mạ vàng bừng sáng, lời chào tạm biệt Tập 11.",
        "prompt": "Close-up still life of the dark leather Amber Eyes investigative dossier closing solemnly on an antique oak desk, embossed golden owl eye logo gleaming in warm amber lamplight, dignified closing frame, graphic novel noir perfection."
    }
]

def main():
    print(f"Tổng số ảnh nền thiết kế cho Tập 11: {len(jobs)} ảnh.")
    
    # Ghi file bg_jobs_tap11.json
    bg_jobs_path = WORK / "bg_jobs_tap11.json"
    bg_jobs_path.write_text(json.dumps(jobs, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo: {bg_jobs_path}")

    # Ghi file gemini_image_prompts_tap11.json
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
    gemini_path = WORK / "gemini_image_prompts_tap11.json"
    gemini_path.write_text(json.dumps(gemini_prompts, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Đã tạo: {gemini_path}")

if __name__ == "__main__":
    main()
