# -*- coding: utf-8 -*-
"""Bảng shot Tập 08 — HỒI 1.

Mỗi dòng: (id, câu, vai, mẫu, nền, chữ VN, chữ EN, chữ JA, beat, nhân vật, chuyển cảnh)

Quy ước:
- cột "Mẫu" giữ NGUYÊN tiếng Việt ở cả 3 bản (parse_shots.py dò "cờ"/"lời kể"/"ngày"/
  "so sánh" để suy ra variant) — chỉ tiêu đề mục 6 và cột "Chữ" mới dịch.
- số trên hình phải có trong câu đọc (A9.2): câu đọc viết số bằng chữ ⇒ hình cũng
  viết bằng chữ (VN "thứ nhất" ⇒ "Nấc thứ nhất", không phải "Nấc 1").
"""

ACT1 = [
    ("1-00", "`1.01`–`1.02` (20,5 s → lời đầu ≈ 23,0 s)", "—", "T1",
     "`t8_tokyo_dawn_fog` hiện dần từ đen",
     "*HỒI 01 · BUỔI SÁNG ĐỊNH MỆNH DƯỚI LÒNG ĐẤT TOKYO*",
     "*ACT 01 · A FATEFUL MORNING BENEATH THE STREETS OF TOKYO*",
     "*第1幕 · 東京の地下に訪れた運命の朝*",
     "—", "⊘", ""),

    ("1-01", "`1.02#1`–`#2`", "H", "T1", "`t8_tokyo_dawn_fog`, `pull`",
     "*Sáng thứ Hai, ngày 20 tháng 3 năm 1995, thủ đô Tokyo thức dậy trong nhịp sống hối hả thường nhật. Hàng triệu người dân đổ dồn về hệ thống tàu điện ngầm dưới lòng đất.*",
     "*On the morning of Monday, March 20, 1995, Tokyo awakened to its usual brisk rhythm of life. Millions of commuters crowded into the subterranean labyrinth of the subway network.*",
     "*1995年3月20日、月曜日の朝、東京は普段と変わらぬ慌ただしい生活のリズムの中で目覚めました。数百万人が地下鉄の巨大な網の中へ足早に吸い込まれていきました。*",
     "—", "✦ Cú", ""),

    ("1-02", "`1.02#3`", "H", "T1", "`t8_commuter_crowd_station`, `still`",
     "*Đúng tám giờ sáng — giờ cao điểm đông đúc nhất trong ngày.*",
     "*It was precisely eight o'clock in the morning, the peak rush hour of the entire day.*",
     "*午前8時ちょうど。一日の中で最も混雑する朝の通勤ラッシュアワー。*",
     "—", "—", ""),

    ("1-03", "`1.02#4`", "H", "T1", "`t8_subway_tracks_perspective`, `pull`",
     "*Năm chuyến tàu điện ngầm trên ba tuyến huyết mạch Chiyoda, Marunouchi và Hibiya đang cùng lao vun vút về phía nhà ga Kasumigaseki.*",
     "*Five subway trains across three vital artery lines — Chiyoda, Marunouchi and Hibiya — hurtled toward Kasumigaseki Station.*",
     "*千代田線、丸ノ内線、日比谷線の3つの大動脈を走る5本の列車が、霞ケ関駅へと向かって同時に疾走していました。*",
     "—", "—", ""),

    ("1-04", "`1.02#5`–`#6`", "H", "T1", "`t8_kasumigaseki_facade`, `pan`",
     "*Nơi đây đặt trụ sở của các Bộ ngành trọng yếu và Cơ quan Cảnh sát Quốc gia. Nhật Bản khi ấy vẫn tự hào với “huyền thoại an toàn” — một xã hội có tỷ lệ tội phạm thấp bậc nhất thế giới.*",
     "*Home to the nation's key ministries and the National Police Agency. Japan still took immense pride in its “myth of public safety” — one of the lowest violent crime rates in the world.*",
     "*ここは国の重要省庁と警察庁が集中する、まさに日本における政治と行政の中枢です。当時の日本は世界で最も治安が良い国の一つである「安全神話」を誇りにしていました。*",
     "—", "—", ""),

    ("1-05", "`1.04#1`", "H", "T1", "`t8_chemical_structure_sarin`, `still`",
     "*Thế nhưng, trên mỗi chuyến tàu ấy, có những người đàn ông mang theo một thứ chất độc thần kinh có sức tàn phá khủng khiếp.*",
     "*Yet on each of those trains, men boarded carrying a neurotoxic chemical capable of catastrophic devastation.*",
     "*しかし、その列車の各車両には、恐るべき破壊力を秘めた神経毒を持ち込んだ男たちが乗っていました。*",
     "—", "—", ""),

    ("1-06", "`1.04#2`", "H", "T1", "`t8_umbrella_puncture_action`, `pull`",
     "*Họ dùng đầu ô đã mài nhọn đâm thủng các túi ni-lông chứa chất lỏng chết người ngay trên sàn toa xe.*",
     "*Using umbrellas ground to razor-sharp tips, they punctured plastic bags filled with lethal liquid directly onto train floors.*",
     "*彼らは研ぎ澄ました傘の先端を使い、猛毒の液体が入ったビニール袋を車内の床の上で突き刺したのです。*",
     "—", "—", ""),

    ("1-07", "`1.04#3`", "H", "T1", "`t8_train_doors_closing`, `pan`",
     "*Khi cửa tàu vừa mở tại các nhà ga đông đúc, những kẻ này nhanh chóng bước ra ngoài, để lại luồng hơi độc bốc lên âm thầm giữa đám đông.*",
     "*As train doors opened at bustling stations, these perpetrators slipped quietly into the morning crowds, leaving toxic vapors to rise silently among the passengers.*",
     "*混雑する駅で電車のドアが開いた瞬間、犯行者たちは素早く車外へ抜け出し、車内には目に見えぬ有毒ガスが静かに立ち込めました。*",
     "—", "—", ""),

    ("1-08", "`1.04#4`", "H", "T4 trích dẫn", "`t8_newspaper_wrapped_package`, `still`",
     "*Một cuộc tấn công phối hợp tàn bạo nhắm thẳng vào các công dân vô tội.*",
     "*A calculated, coordinated chemical strike aimed directly at innocent citizens.*",
     "*罪なき一般市民を真正面から標的にした、綿密に計画された同時多発化学テロでした。*",
     "—", "—", ""),

    ("1-09", "`1.06#1`–`#2`", "H", "T1", "`t8_subway_car_mist_vapor`, `pull`",
     "*Chỉ trong vài phút ngắn ngủi, một cơn ác mộng chưa từng có trong lịch sử Nhật Bản thời hậu chiến đã bùng nổ dưới lòng đất Tokyo. Hãy hình dung điều một hành khách khi ấy phải trải qua.*",
     "*Within mere minutes, a nightmare unprecedented in Japan's postwar history erupted beneath the streets of Tokyo. Imagine what an ordinary passenger on board experienced that fateful morning.*",
     "*わずか数分の間に、日本の戦後史上前例のない悪夢が東京の地下深くで炸裂しました。その運命の朝、車内に居合わせた一人の乗客が何を経験したのか、想像してみてください。*",
     "—", "→N1", ""),

    ("1-10", "`1.07#1`–`#2`", "N1", "T4 lời kể", "`t8_subway_platform_tunnel_dark`, `still`",
     "*Tôi đang đứng đọc sách trên tàu thì ngửi thấy một mùi hắc nhẹ rất lạ, giống như mùi dung môi pha sơn. Đột nhiên, mắt tôi cay xè và mọi thứ xung quanh tối sầm lại.*",
     "*I was standing reading a book on the train when I caught a strange, faint odor, almost like paint thinner. Suddenly my eyes began burning and everything around me went pitch black.*",
     "*車内で本を読んでいたとき、シンナーのような微かな異臭が鼻をつきました。突如として目が激しく痛み始め、まるで誰かに照明を一斉に消されたかのように周囲の視界が真っ暗になりました。*",
     "—", "✦ Cừu", ""),

    ("1-11", "`1.07#3`", "N1", "T1", "`t8_dropped_novel_glasses`, `pull`",
     "*Tôi thấy ngực mình nghẹt thở, và mọi người xung quanh bắt đầu ho dữ dội rồi hoảng loạn tìm lối thoát.*",
     "*My chest tightened into suffocation, and people around me began coughing uncontrollably before rushing blindly toward the exits.*",
     "*胸が締め付けられて息ができなくなり、周りの人々が激しく咳き込みながら出口を求めてパニックになりました。*",
     "—", "—", ""),

    ("1-12", "`1.07#4`–`#5`", "N1", "T1", "`t8_subway_stairs_escape`, `pan`",
     "*Không ai hiểu chuyện gì đang xảy ra, và sự kinh hoàng bao trùm khắp sân ga. Cảm giác ấy cứ như ngày tận thế vừa ập xuống đầu chúng tôi giữa ban ngày.*",
     "*No one understood what was happening, and raw terror instantly consumed the entire platform. It truly felt as though the end of the world had descended upon us in broad daylight.*",
     "*何が起きているのか誰にも分からず、ホーム全体が生々しい恐怖に包まれました。あの瞬間、まるで白昼堂々と世界の終わりが突然降りかかってきたかのようでした。*",
     "—", "—", ""),

    ("1-13", "`1.09#1`", "H", "T1", "`t8_ambulances_tokyo_street`, `still`",
     "*Vụ tấn công hóa học đã cướp đi sinh mạng của mười bốn thường dân vô tội và làm tổn hại sức khỏe của hơn năm nghìn tám trăm người khác.*",
     "*The chemical strike claimed the lives of fourteen innocent people and severely injured over five thousand eight hundred commuters.*",
     "*この化学兵器攻撃により、14名の尊い命が奪われ、5800人以上が健康被害を受けました。*",
     "—", "→H", ""),

    ("1-14", "`1.09#2`", "H", "T1", "`t8_hospital_triage_corridor`, `pull`",
     "*Hai nhân viên đường sắt quả cảm, ông Kazumasa Takahashi và ông Tsuneo Hishinuma, đã dũng cảm dùng tay không di chuyển các túi chất độc ra khỏi toa xe để bảo vệ hành khách và anh dũng hy sinh.*",
     "*Two courageous subway station workers, Kazumasa Takahashi and Tsuneo Hishinuma, heroically removed the toxic bags with their bare hands to protect passengers and made the ultimate sacrifice.*",
     "*勇敢な駅員であった高橋一正助役と菱沼恒夫駅員は、乗客を守るため素手で毒液袋を車外へ運び出し、尊い犠牲となりました。*",
     "—", "—", ""),

    ("1-15", "`1.09#3`–`#4`", "H", "T1", "`t8_subway_platform_tunnel_dark`, `still`",
     "*Hàng nghìn người phải chịu đựng những di chứng tâm lý nặng nề và nỗi sợ hãi kéo dài suốt phần đời còn lại. Cơn hoang tưởng tập thể bùng phát khắp thủ đô: người dân Tokyo nín thở khi bước xuống ga ngầm.*",
     "*Thousands of survivors were left grappling with severe long-term psychological trauma. Collective paranoia gripped the metropolis: commuters held their breath descending subway stairs and inspected under every seat.*",
     "*何千人もの被害者が重い心的外傷後ストレス障害と長期にわたる後遺症を背負いました。集団的偏執病が首都全域を襲い、市民は地下鉄の階段を降りるたびに息を詰めました。*",
     "—", "—", ""),

    ("1-16", "`1.09#5`", "H", "T1", "`t8_subway_exit_sunlight`, `pull`",
     "*Toàn bộ hệ thống giao thông và y tế của siêu đô thị rơi vào tình trạng tê liệt khẩn cấp.*",
     "*The entire transportation and emergency medical infrastructure of the world's largest metropolis fell into an unprecedented state of paralysis.*",
     "*世界最大級のメガロポリスの交通機関と救急医療体制は、かつてない麻痺状態へと陥りました。*",
     "—", "—", ""),

    ("1-17", "`1.11#1`", "D", "T1", "`t8_tokyo_police_hq`, `pan`",
     "*Ngay sau khi tiếp nhận thông tin về vụ rải khí độc tại ga Kasumigaseki, Cơ quan Cảnh sát Quốc gia Nhật Bản đã xác định đây là một cuộc tấn công khủng bố phối hợp quy mô lớn.*",
     "*Immediately following reports of toxic gas releases at Kasumigaseki Station, the National Police Agency recognized this as a coordinated, large-scale terrorist attack.*",
     "*霞ケ関駅周辺での毒ガステロ発生の報を受け、日本の警察庁はこれが大規模な組織的同時多発テロであると直ちに断定しました。*",
     "—", "✦ Sói", ""),

    ("1-18", "`1.11#2`", "D", "T1", "`t8_incident_board_map`, `still`",
     "*Mục tiêu của chúng là nhắm thẳng vào các tuyến tàu đi qua khu vực cơ quan đầu não của chính phủ nhằm làm tê liệt bộ máy điều hành đất nước.*",
     "*The perpetrators intentionally targeted transit lines converging on central government ministries to paralyze the nation's governing apparatus.*",
     "*犯行の狙いは、国の統治機能を麻痺させるため、中央省庁街へ乗り込む路線を正面から攻撃することにありました。*",
     "—", "—", ""),

    ("1-19", "`1.11#3`–`#4`", "D", "T1", "`t8_chemical_structure_sarin`, `pull`",
     "*Phương thức gây án được tính toán tinh vi với năm kẻ tấn công đồng loạt ra tay vào đúng khung giờ cao điểm. Hóa chất được sử dụng là sarin, một loại khí độc thần kinh nhân tạo cực kỳ nguy hiểm và phức tạp trong tổng hợp.*",
     "*The operational scheme was meticulously calculated, deploying five synchronized attackers at the exact peak of commuter congestion. The substance was sarin, an artificial nerve agent extraordinarily hazardous and complex to synthesize.*",
     "*朝の通勤ラッシュの頂点を狙い、5名の実行犯が一斉に毒物を散布するという極めて冷酷な手口でした。使用された化学物質はサリンであり、高度な有機合成技術を要する極めて危険な猛毒神経ガスでした。*",
     "—", "—", ""),

    ("1-20", "`1.11#5`", "D", "T2 thẻ hồ sơ", "`t8_aum_shinrikyo_emblem_shadow`, `still`",
     "*Mọi dấu vết tại hiện trường đều nhanh chóng chỉ về một tổ chức tôn giáo bí ẩn mang tên Giáo phái Aum Shinrikyo.*",
     "*Every operational footprint at the scene pointed swiftly toward an enigmatic religious organization known as Aum Shinrikyo.*",
     "*現場に残されたあらゆる物証と痕跡は、急速にある謎めいた宗教組織、オウム真理教へと収斂していきました。*",
     "—", "—", ""),

    ("1-21", "`1.12#1`–`#3`", "H", "T1", "`t8_dossier_elite_scientists`, `pull`",
     "*Điều khiến toàn bộ thế giới bàng hoàng không chỉ dừng lại ở sự tàn độc của vụ tấn công. Kẻ thực hiện không phải là một tổ chức quân sự ngoại quốc hay những tên tội phạm đường phố liều lĩnh.*",
     "*Yet what stunned Japan and the world went far beyond the sheer cruelty of the strike itself. The perpetrators were neither a foreign military unit nor hardened street criminals operating on society's margins.*",
     "*しかし、日本と世界に最大の衝撃を与えたのは、単なる攻撃の残忍さだけではありませんでした。実行犯たちは外国の軍事組織でも、社会の底辺で生きる凶悪な犯罪集団でもありませんでした。*",
     "—", "→C", ""),

    ("1-22", "`1.12#4`–`#5`", "H", "T1", "`t8_kasumigaseki_facade`, `pan`",
     "*Đứng sau thảm kịch ấy là những nhà khoa học, bác sĩ và trí thức tinh hoa của chính đất nước Nhật Bản. Chính vị thế học thức đỉnh cao ấy đã tạo nên một “Hiệu ứng Hào quang” chết người, che mắt toàn bộ xã hội và cơ quan an ninh suốt nhiều năm dài.*",
     "*Behind this devastating assault stood top-tier scientists, medical doctors, and intellectual elites educated at Japan's most prestigious universities. Their immaculate academic credentials had created a lethal “Halo Effect”, blinding society and law enforcement for years.*",
     "*この未曾有の惨劇の背後にいたのは、日本の名門大学で高度な教育を受けた一握りの科学者、医師、そしてエリート知識人たちでした。彼らの卓越した知性と華々しい学歴こそが致命的な「ハロー効果」を生み、社会と捜査当局の目を長年にわたり曇らせました。*",
     "—", "—", ""),

    ("1-23", "nghỉ chuyển hồi (2 s)", "—", "T10", "`void`",
     "*HỒI 02* · **KHU CĂN CỨ DƯỚI CHÂN NÚI PHÚ SĨ**",
     "*ACT 02* · **THE BASE AT THE FOOT OF MOUNT FUJI**",
     "*第2幕* · **富士山の麓の巨大拠点**",
     "—", "⊘", "◼"),
]
