# -*- coding: utf-8 -*-
"""
Builder script for Tap 42 multilingual scripts:
- kichban_tap42_19112026.md (Vietnamese)
- kichban_tap42_EN.md (English)
- kichban_tap42_JA.md (Japanese)

Structured strictly following Tap 10 format:
- 5 Acts
- 36 Speaker blocks
- ~240 lines each
- Matching 1-to-1 parity between VN, EN, JA
"""

import sys

def get_script_data():
    # We will define the 36 blocks with (role_vn, role_en, role_ja, text_vn_lines, text_en_lines, text_ja_lines, note_vn, note_en, note_ja)
    blocks = []
    
    # ------------------ ACT 1: 7 BLOCKS (46 lines) ------------------
    # Block 1: HOST (12 lines)
    blocks.append({
        'act': 1,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(chậm rãi, giọng trầm ấm gợi mở không gian lịch sử và bối cảnh xã hội)',
        'note_en': '(slowly, with a warm and deep voice evoking historical context and social weight)',
        'note_ja': '（落ち着いた低音の温かな語り口で、歴史的背景と社会的重みを示唆する）',
        'bgm_vn': '**[BGM]:** Tiếng đàn Cello u buồn cất lên chậm rãi giữa không gian tĩnh lặng, hòa cùng tiếng gió rít hiu hắt của thị trấn công nghiệp Marcinelle, tạo cảm giác ngột ngạt và bất an.',
        'bgm_en': '**[BGM]:** A somber cello melody rises slowly through the silence, blending with the bleak whistling wind of industrial Marcinelle, creating a suffocating and ominous atmosphere.',
        'bgm_ja': '**[BGM]:** 静寂の中に哀愁を帯びたチェロの旋律が重く響き、工業都市マルシネルの冷たい風の音と混ざり合い、息苦しい不穏さを醸し出す。',
        'vn': [
            "Vào giữa thập niên 1990, vương quốc Bỉ trải qua một giai đoạn thanh bình dường như không thể lay chuyển giữa lòng châu Âu phát triển.",
            "Những thị trấn cổ kính ven sông Sambre và các vùng ngoại ô công nghiệp yên ả từng là biểu tượng cho cuộc sống an lành và thịnh vượng.",
            "Người dân nơi đây sống trong niềm tin mặc định rằng hiểm họa bạo lực chỉ thuộc về những đô thị xa xôi hoặc những trang tiểu thuyết kinh dị.",
            "Thế nhưng, chính trong sự êm đềm và mất cảnh giác tập thể ấy, một cơn ác mộng đen tối bậc nhất lịch sử hiện đại đã âm thầm bén rễ.",
            "Tại thị trấn Marcinelle thuộc thành phố Charleroi, một ngôi nhà gạch đỏ bình thường với những ô cửa sổ sáng đèn hàng đêm đã trở thành chiếc bẫy tử thần.",
            "Phía sau vẻ ngoài cũ kỹ và có phần lộn xộn của một người thợ điện địa phương là một mật thất ngầm được xây dựng tinh vi.",
            "Một căn hầm bê tông cách âm chật hẹp, nằm khuất sau những kệ gỗ nặng trĩu, đã được chuẩn bị như một nhà tù vĩnh viễn.",
            "Đây không đơn thuần là một vụ bắt cóc tống tiền thông thường, mà là sự hiện thực hóa một ảo tưởng bệnh lý về quyền lực và sự kiểm soát tuyệt đối.",
            "Những dải đường làng hiền hòa và các cung đường đi học của trẻ thơ đã vô tình trở thành ngư trường săn mồi của một kẻ thủ ác tàn nhẫn.",
            "Khi những chiếc xe đạp bị bỏ lại bên vệ đường và những tiếng cười thơ ngây bỗng chốc tắt lịm, một đám mây u ám bắt đầu bao phủ toàn bộ đất nước.",
            "Dư chấn của hồ sơ Marc Dutroux sau này không chỉ làm sụp đổ một mạng lưới tội ác, mà còn làm rung chuyển tận gốc rễ niềm tin vào hệ thống thực thi pháp luật.",
            "Một cuộc khủng hoảng lương tri chưa từng có đã bắt đầu từ chính những vết nứt vô hình trong lòng xã hội."
        ],
        'en': [
            "In the mid-1990s, the Kingdom of Belgium enjoyed a seemingly unshakable era of peace at the very heart of developed Europe.",
            "The picturesque towns along the Sambre River and quiet industrial suburbs stood as symbols of serene and prosperous living.",
            "Local residents lived under the default assumption that violent horrors belonged only to distant metropolises or crime novels.",
            "Yet, within that peaceful collective innocence, one of the darkest nightmares in modern history was quietly taking root.",
            "In the town of Marcinelle near Charleroi, an unassuming red-brick house with softly lit windows became a deadly trap.",
            "Behind the weathered, cluttered facade of a local electrician lay a meticulously engineered subterranean secret chamber.",
            "A cramped, soundproof concrete dungeon, concealed behind heavy shelving, had been prepared as a permanent prison.",
            "This was not merely a conventional kidnapping for ransom, but the physical manifestation of a pathological obsession with absolute power and control.",
            "Peaceful country roads and daily school routes inadvertently turned into hunting grounds for a merciless predator.",
            "When abandoned bicycles were found by roadsides and innocent laughter suddenly vanished, a dark shadow descended across the nation.",
            "The shockwaves of the Marc Dutroux case would later not only dismantle a criminal conspiracy, but shake institutional trust to its core.",
            "An unprecedented crisis of public conscience began within these invisible fissures of modern society."
        ],
        'ja': [
            "1990年代半ば、ベルギー王国は発展したヨーロッパの中心で、揺るぎない平和と平穏を享受していました。",
            "サンブル川沿いの歴史ある町並みや静かな工業地帯の郊外は、穏やかで豊かな生活の象徴と見なされていました。",
            "住民たちは、凶悪な暴力の悲劇など遠い大都市やサスペンス小説の中だけの出来事だと信じ切っていたのです。",
            "しかし、その平穏な集合的無防備さの陰で、近代史上最も暗い悪夢が密かに根を下ろしていました。",
            "シャルルロワ近郊の町マルシネルにおいて、夜ごとに灯りがともるありふれた赤レンガ造りの民家が、死の罠へと変貌を遂げていました。",
            "地元の電気工という古びた散らかった生活の裏側に、緻密に設計された地下の秘密部屋が潜んでいたのです。",
            "重い棚の奥深くに隠された狭く防音されたコンクリートの地下室は、永遠の牢獄として用意されていました。",
            "これは単なる身代金目的の誘拐ではなく、絶対的な権力と支配に対する病的な妄想の具現化でした。",
            "のどかな田舎道や子どもたちの通学路は、無慈悲な捕食者が張り巡らせた獲物の狩り場と化していたのです。",
            "放置された自転車が道端に転がり、幼い笑い声が唐突に途絶えたとき、暗雲が国全体を覆い始めました。",
            "後にマルク・デュトルー事件と呼ばれるこの衝撃は、犯罪組織を解体しただけでなく、法執行機関への信頼を根底から揺るがしました。",
            "社会の見えない亀裂の中から、かつてない前代未闻の良心の危機が幕を開けたのです。"
        ]
    })

    # Block 2: HOST (6 lines)
    blocks.append({
        'act': 1,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(chuyển giọng u tối, báo hiệu tai ương và chuỗi mất tích bí ẩn)',
        'note_en': '(shifting to a somber tone, signaling disaster and the mysterious disappearances)',
        'note_ja': '（トーンを落とし、忍び寄る惨劇と連続失踪の不穏さを告げる）',
        'sfx_vn': '**[SFX]:** Tiếng lốp xe rít nhẹ trên mặt đường ẩm ướt, tiếng động cơ xe van nổ trầm đục trong màn sương mờ.',
        'sfx_en': '**[SFX]:** Tires screeching softly on wet asphalt, the muffled rumble of a van engine idling through the fog.',
        'sfx_ja': '**[SFX]:** 濡れたアスファルトに軋むタイヤの摩擦音、霧の中に響くバンの鈍いアイドリング音。',
        'vn': [
            "Mùa hè năm 1995 bắt đầu với một sự biến mất kỳ lạ làm bàng hoàng thị trấn Grâce-Hollogne gần thành phố Liège.",
            "Hai cô bé tám tuổi là Julie Lejeune và Mélissa Russo bỗng nhiên mất tích không một dấu vết khi đang chơi đùa gần một cây cầu vượt.",
            "Không một nhân chứng trực tiếp, không một cuộc gọi đòi tiền chuộc, các em dường như đã tan biến vào không khí giữa ban ngày.",
            "Chỉ vài tháng sau đó, đến lượt hai thiếu nữ trẻ An Marchal và Eefje Lambrecks biến mất bí ẩn sau một buổi dạo chơi tại bờ biển Blankenberge.",
            "Nỗi hoang mang bắt đầu lan tỏa như một dịch bệnh tâm lý vô hình, len lỏi vào từng bữa cơm của mọi gia đình trên khắp nước Bỉ.",
            "Cha mẹ các nạn nhân ôm những tấm ảnh con đi khắp các ngõ ngách, nhưng câu trả lời nhận lại chỉ là sự im lặng đáng sợ của màn đêm."
        ],
        'en': [
            "The summer of 1995 began with a chilling disappearance that stunned the town of Grâce-Hollogne near Liège.",
            "Two eight-year-old girls, Julie Lejeune and Mélissa Russo, vanished without a trace while playing near a highway overpass.",
            "With no direct witnesses and no ransom calls, the children seemed to have evaporated into thin air in broad daylight.",
            "Only a few months later, two teenage girls, An Marchal and Eefje Lambrecks, mysteriously disappeared after an outing in Blankenberge.",
            "Dread spread like an invisible psychological contagion, creeping into family dinner tables across Belgium.",
            "Desperate parents carried photographs of their children through every street corner, met only by the terrifying silence of the dark."
        ],
        'ja': [
            "1995年の夏、リエージュ近郊の町グラス＝オローニュを震撼させる戦慄の失踪劇からすべてが始まりました。",
            "8歳の少女ジュリー・ルジューヌとメリッサ・ルッソが、高架橋の近くで遊んでいた最中に忽然と姿を消したのです。",
            "直接の目撃者もおらず、身代金の要求電話もなく、子どもたちは白昼堂々、煙のように消え去ったかのようでした。",
            "それからわずか数か月後、10代の少女アン・マルシャルとエーフイェ・ランブレックスが海辺の町ブランケンベルヘから謎の失踪を遂げます。",
            "目に見えない心理的伝染病のように恐怖が広がり、ベルギー中のあらゆる家庭の食卓へと忍び寄っていきました。",
            "我が子の写真を抱えた親たちが街の隅々を彷徨い歩きましたが、返ってきたのは夜の冷酷な沈黙だけでした。"
        ]
    })

    # Block 3: HOST (6 lines)
    blocks.append({
        'act': 1,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(tiếp tục mạch tự sự nghẹt thở, khắc họa bẫy ngụy trang)',
        'note_en': '(continuing the breathless narrative, depicting the deceptive predatory trap)',
        'note_ja': '（息詰まる語りを継続し、巧妙に偽装された捕食者の罠を描写する）',
        'sfx_vn': '**[SFX]:** Tiếng cánh cửa trượt kim loại xe van đóng sầm dứt khoát, tiếng gió rít dồn dập.',
        'sfx_en': '**[SFX]:** The sharp metallic slam of a van sliding door, followed by rapid howling wind.',
        'sfx_ja': '**[SFX]:** スライドドアが激しく閉まる乾いた金属音、吹きすさぶ風の唸り。',
        'vn': [
            "Thủ đoạn của kẻ săn mồi Marc Dutroux dựa trên một chiếc xe van màu trắng và sự tính toán lạnh lùng về thời điểm ra tay.",
            "Hắn thường theo dõi quy luật sinh hoạt của các nạn nhân, nhắm vào những cung đường vắng vẻ nơi trẻ em thường đi học một mình.",
            "Một cú tấp xe bất ngờ, cánh cửa trượt mở ra trong tích tắc và con mồi bị lôi vào khoang xe tối tăm trước khi kịp cất tiếng kêu cứu.",
            "Chiếc xe hòa vào dòng phương tiện lưu thông trên quốc lộ như hàng vạn chiếc xe chuyên chở hàng hóa bình thường khác.",
            "Không ai có thể ngờ rằng phía sau thùng xe kín mít ấy là sự khởi đầu của một hành trình tước đoạt toàn bộ nhân phẩm con người.",
            "Kẻ thủ ác đã khai thác triệt để 'Điểm mù xã hội' — nơi mọi người tin rằng người qua đường sẽ lên tiếng nếu có điều gì bất thường xảy ra."
        ],
        'en': [
            "The modus operandi of predator Marc Dutroux relied on a white utility van and cold, calculated timing.",
            "He methodically shadowed his victims' routines, targeting isolated spots where children walked alone to school or home.",
            "A sudden curb pull, a sliding door opening in an instant, and the target was hauled into the dark interior before an alarm could sound.",
            "The vehicle seamlessly melted into highway traffic, indistinguishable from thousands of everyday commercial delivery vans.",
            "No observer could imagine that behind those windowless metal panels lay the onset of systematic human degradation.",
            "The perpetrator ruthlessly exploited the 'Social Blindspot' — where bystanders mistakenly assume someone else will speak up if danger lurks."
        ],
        'ja': [
            "捕食者マルク・デュトルーの手口は、白い作業用バンと冷徹に計算された犯行の瞬間に基づいていました。",
            "彼は標的の行動パターンを入念に監視し、子どもたちが一人で通学する人通りの少ない死角を狙い定めていたのです。",
            "不意に路肩へと車を寄せ、一瞬のうちにスライドドアを開け放ち、悲鳴を上げる間もなく暗闇へと引きずり込みました。",
            "その車は何事もなかったかのように高速道路の車列に紛れ込み、街を行き交う無数の商業車両と何ら変わりませんでした。",
            "窓のない金属パネルの向こう側で、人間の尊厳を完全に剥奪する儀式が始まっているとは、誰も想像し得なかったのです。",
            "犯人は「社会的死角」を冷酷に悪用しました。異常があれば誰かが必ず声を上げるはずだという、周囲の根拠なき思い込みを突いたのです。"
        ]
    })

    # Block 4: ORDINARY PERSON (5 lines)
    blocks.append({
        'act': 1,
        'role_vn': 'NGƯỜI BÌNH THƯỜNG',
        'role_en': 'ORDINARY PERSON',
        'role_ja': '一般人',
        'note_vn': '(N1: Người dân thị trấn Marcinelle, giọng run rẩy, bàng hoàng tột độ)',
        'note_en': '(N1: Marcinelle Town Resident, voice trembling with immense shock)',
        'note_ja': '（N1：マルシネルの住民、震える声で極限の衝撃を語る）',
        'vn': [
            "Hãy hình dung cảm giác của chúng tôi khi sống ngay cạnh một người hàng xóm mà ai cũng nghĩ chỉ là một tay thợ điện lập dị.",
            "Ông ta hàng ngày vẫn lái chiếc xe van màu trắng ra vào con hẻm, đôi khi chào hỏi vài câu bâng quơ với những người xung quanh.",
            "Ngôi nhà lúc nào cũng bừa bộn rác rưởi cơ khí, nuôi vài con chó dữ sủa inh ỏi sau hàng rào gỗ.",
            "Chúng tôi chỉ phàn nàn về tiếng ồn và sự nhếch nhác, chứ làm sao có thể tưởng tượng nổi chuyện kinh hoàng đang diễn ra dưới lòng đất?",
            "Nghĩ lại những buổi chiều con cái chúng tôi chơi đùa ngoài vỉa hè chỉ cách căn hầm ấy vài bước chân, đến tận bây giờ tôi vẫn rùng mình ớn lạnh."
        ],
        'en': [
            "Imagine our shock living right next door to a neighbor everyone dismissed as merely an eccentric local handyman.",
            "Every day he drove that white van in and out of the alley, occasionally tossing casual greetings to people passing by.",
            "The house was constantly cluttered with mechanical junk, keeping fierce dogs barking loudly behind a wooden fence.",
            "We complained only about the noise and the unsightly mess; how could anyone fathom the horror unfolding beneath our feet?",
            "Remembering our own children playing on the sidewalk just yards away from that cellar, a chill still runs down my spine today."
        ],
        'ja': [
            "誰もがただの変わり者の電気工だと思い込んでいた男の、すぐ隣で暮らしていた私たちの衝撃を想像してみてください。",
            "彼は毎日あの白いバンを路地に出し入れし、通りがかる人々に時折当たり障りのない挨拶を交わしていました。",
            "家には機械の残骸が散らかり放題で、木製フェンスの裏では獰猛な数匹の犬がけたたましく吠え立てていました。",
            "私たちは騒音や不潔さに不満を漏らしていただけで、まさか足元でそんな恐ろしい惨劇が進行していようとは夢にも思いませんでした。",
            "あのかび臭い地下室からほんの数メートルの歩道で、私たちの子どもたちが夕暮れまで遊んでいたことを思い出すと、今でも戦慄を覚えます。"
        ]
    })

    # Block 5: HOST (5 lines)
    blocks.append({
        'act': 1,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(trầm giọng, nhấn mạnh sự sụp đổ của các rào cản cảnh giác)',
        'note_en': '(lowering voice, emphasizing the complete collapse of societal vigilance)',
        'note_ja': '（声を落とし、社会的警戒網の完全な崩壊を強調する）',
        'sfx_vn': '**[SFX]:** Tiếng còi cảnh sát vang vọng xa xăm, tiếng lật giấy tờ hồ sơ vội vã.',
        'sfx_en': '**[SFX]:** Distant police siren echoing, followed by the hurried rustling of case files.',
        'sfx_ja': '**[SFX]:** 遠くで鳴り響く警察のサイレン、慌ただしく捜査資料をめくる紙の音。',
        'vn': [
            "Vỏ bọc của một gã đàn ông luộm thuộm, có gia đình và công việc lặt vặt đã tạo ra một bức màn ngụy trang hoàn hảo.",
            "Người ta có xu hướng đề phòng những bóng ma trong bóng tối nhưng lại hoàn toàn mất cảnh giác trước những kẻ quen mặt trong khu phố.",
            "Marc Dutroux hiểu rất rõ tâm lý bài trừ nghi ngờ của cộng đồng xung quanh mình.",
            "Hắn tận dụng chính sự nhẫn nại và thói quen ngại can thiệp vào chuyện nhà người khác của các cư dân láng giềng.",
            "Và thế là, cánh cửa dẫn xuống căn hầm số 128 phố Philippeville vẫn đóng kín suốt nhiều tháng trời mà không một ai hay biết."
        ],
        'en': [
            "The facade of a scruffy family man doing odd handyman jobs formed an impenetrable cloak of deception.",
            "Society tends to brace against lurking shadows while letting its guard completely down before familiar neighborhood faces.",
            "Marc Dutroux astutely recognized and manipulated this collective reluctance to suspect ordinary acquaintances.",
            "He weaponized neighbors' polite tolerance and their instinct to avoid meddling in other households' private affairs.",
            "And thus, the cellar door at number 128 Rue de Philippeville remained sealed for months without raising an alarm."
        ],
        'ja': [
            "雑多な修理仕事で食いつなぐ、だらしない家庭持ちの男という外見が、完璧な偽装の盾となっていました。",
            "人間は暗闇に潜む見知らぬ脅威には警戒を強める一方で、見慣れた近隣住人の前では警戒心を完全に解いてしまうものです。",
            "マルク・デュトルーは、周囲のコミュニティが抱くこの無意識の油断と不信拒絶の心理を熟知していました。",
            "他人の家庭事情に過度に干渉することを避けるという、隣人たちの控えめな配慮そのものが凶器へと転化されたのです。",
            "こうして、フィリップヴィル通り128番地の地下へと通じる扉は、何ヶ月もの間、誰にも悟られることなく閉ざされ続けました。"
        ]
    })

    # Block 6: INVESTIGATOR (7 lines)
    blocks.append({
        'act': 1,
        'role_vn': 'ĐIỀU TRA VIÊN',
        'role_en': 'INVESTIGATOR',
        'role_ja': '捜査官',
        'note_vn': '(giọng đanh thép, chuyên nghiệp, phân tích phương thức gây án MO và chữ ký Signature)',
        'note_en': '(steely, precise, professional, analyzing Modus Operandi and Psychological Signature)',
        'note_ja': '（冷徹かつ的確なプロの語り口で、犯行手口MOと心理的シグネチャーを分析する）',
        'vn': [
            "Khi phân tích phương thức gây án trong hồ sơ này, lực lượng điều tra nhận thấy một sự mâu thuẫn đầy nghịch lý.",
            "Về thủ đoạn phạm tội hay Modus Operandi, các vụ bắt cóc được thực hiện rất nhanh gọn, chớp nhoáng bên lề đường bằng xe van.",
            "Thế nhưng chữ ký tâm lý hay Signature của Marc Dutroux lại bộc lộ rõ nhu cầu kiểm soát dài hạn mang tính chiếm đoạt cực đoan.",
            "Hắn không phi tang nạn nhân ngay sau khi xâm hại, mà dành nhiều tuần để đào đất, trát vữa và lắp đặt hệ thống cửa bí mật.",
            "Căn hầm Marcinelle chỉ có diện tích vỏn vẹn gần ba mét vuông, cao chưa đầy hai mét, được giấu kín sau một tủ đồ cơ khí.",
            "Một hệ thống thông gió thô sơ và chuông báo động tự chế được lắp đặt để ngăn chặn mọi nỗ lực đào tẩu.",
            "Điều này chứng tỏ đối tượng đã lên kế hoạch biến các nạn nhân thành tài sản sở hữu độc quyền vĩnh viễn trong thế giới ngầm của riêng mình."
        ],
        'en': [
            "Examining the behavioral patterns across these files reveals a striking psychological paradox.",
            "Regarding Modus Operandi, the abductions were executed swiftly along public roadways using an ordinary utility van.",
            "However, Dutroux's psychological Signature displayed a fixation on long-term domination and absolute possession.",
            "Rather than disposing of victims immediately, he spent weeks excavating dirt, pouring mortar, and fitting concealed doors.",
            "The Marcinelle cellar measured barely three square meters and under two meters high, tucked behind a heavy tool cupboard.",
            "A crude ventilation pipe and a homemade electronic alarm wire were rigged to extinguish any escape attempt.",
            "This confirms the perpetrator premeditated transforming victims into permanently subjugated possessions within his underworld."
        ],
        'ja': [
            "事件記録全体に見られる行動パターンを精査すると、極めて際立った心理的パラドックスが浮き彫りになります。",
            "犯行手口であるモダス・オペランディに関して言えば、路上での誘拐は白いバンを用いて電光石火の早業で行われました。",
            "しかし、マルク・デュトルーの心理的シグネチャーは、長期的な支配と極端な私物化への病的な執着を示していました。",
            "彼は犯行後すぐに痕跡を隠滅するのではなく、何週間もかけて土を掘り、モルタルを塗り、隠し扉を設置していたのです。",
            "マルシネルの地下室はわずか3平方メートル足らず、天井高は2メートルにも満たず、重い道具棚の背後に隠されていました。",
            "粗雑な換気パイプと手製の電子警報装置が取り付けられ、脱出の試みを徹底的に封じ込める構造になっていました。",
            "これは、自らの閉ざされた地下王国において、被害者を恒久的に服従させる私的所有物へと変造する計画的犯行を証明しています。"
        ]
    })

    # Block 7: HOST (5 lines)
    blocks.append({
        'act': 1,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(kết Hồi 1, chuyển nhịp tâm lý sang phân tích thế giới nội tâm bệnh hoạn)',
        'note_en': '(concluding Act 1, bridging the psychological transition into the distorted inner world)',
        'note_ja': '（第1幕を結び、歪んだ深層心理の解明へと移行する）',
        'vn': [
            "Cái bẫy đã sập xuống, chôn vùi tương lai của những sinh linh thơ ngây dưới lớp đất đá lạnh lẽo.",
            "Nhưng điều gì đã biến một con người từng có tiền án trở thành một kẻ săn mồi ngạo mạn bất chấp mọi giới hạn xã hội?",
            "Làm thế nào một kẻ từng bị kết án tù hơn mười ba năm lại có thể ung dung bước ra ngoài và tiếp tục mở rộng quy mô tội ác?",
            "Và phía sau cánh cửa căn hầm Marcinelle, mối quan hệ đồng lõa giữa hắn và người vợ Michelle Martin đã vận hành như thế nào?",
            "Chúng ta hãy cùng bước vào Hồi hai để giải phẫu cấu trúc nhân cách ái kỷ và cơ chế chia ngăn nhận thức của kẻ thủ ác."
        ],
        'en': [
            "The trap snapped shut, burying the futures of innocent lives beneath cold subterranean concrete.",
            "Yet what drove a previously convicted criminal to evolve into a brazen predator defying every societal boundary?",
            "How could an offender sentenced to thirteen years in prison walk free early and methodically expand his reign of terror?",
            "And behind the walls of that Marcinelle residence, how did the toxic complicity with his wife Michelle Martin truly function?",
            "Let us step into Act Two to dissect the narcissistic personality structure and mental compartmentalization of this predator."
        ],
        'ja': [
            "冷酷な罠は閉じられ、罪なき命の未来は地下の冷たいコンクリートの底へと埋め殺されました。",
            "しかし、前科のあった一人の男を、社会のあらゆる規範をあざ笑う傲慢な捕食者へと変貌させたものは何だったのでしょうか？",
            "かつて禁錮13年以上の実刑判決を受けた男が、なぜ早期釈放され、凶行の規模を拡大し続けることができたのか？",
            "そしてマルシネルの家屋の壁の裏で、妻ミシェル・マルタンとの共犯関係は一体どのように機能していたのでしょうか？",
            "第2幕において、捕食者の自己愛性人格構造と、精神の認知的区画化メカニズムを解剖していきましょう。"
        ]
    })

    # ------------------ ACT 2: 9 BLOCKS (57 lines) ------------------
    # Block 8: HOST (6 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(giọng trầm tĩnh, đào sâu vào vỏ bọc xã hội và cơ chế chia ngăn)',
        'note_en': '(reflective tone, delving into the social camouflage and mental compartmentalization)',
        'note_ja': '（静かなトーンで、社会的偽装と認知的区画化のメカニズムを掘り下げる）',
        'bgm_vn': '**[BGM]:** Tiếng drone điện tử rùng rợn hòa cùng tiếng gõ đồng hồ tích tắc ngột ngạt, tạo không khí u ám của sự che giấu bệnh lý.',
        'bgm_en': '**[BGM]:** Chilling electronic drone blending with the suffocating ticking of a metal clock, evoking pathological secrecy.',
        'bgm_ja': '**[BGM]:** 戦慄の電子ドローンと息苦しい金属時計の針の音が重なり、病的な隠蔽の不穏な空気を醸し出す。',
        'vn': [
            "Một trong những đặc điểm nổi bật nhất của Marc Dutroux chính là khả năng phân chia nhận thức hay Compartmentalization ở mức độ cực đoan.",
            "Ban ngày, hắn duy trì hình ảnh của một người đàn ông bình thường: lui tới các gara ô tô, mặc cả từng món đồ cũ và chuyện trò cùng hàng xóm.",
            "Thế nhưng khi màn đêm buông xuống, hắn biến thành một bạo chúa toàn năng điều hành một nhà tù ngầm do chính tay mình thiết kế.",
            "Sự chia ngăn này cho phép đối tượng khóa chặt mọi cảm xúc tội lỗi vào một góc khuất riêng biệt của tâm trí.",
            "Hắn không nhìn thấy ở những đứa trẻ bị giam cầm nỗi đau đớn hay sự sợ hãi của một con người.",
            "Trong mắt hắn, các nạn nhân đã bị tước đoạt hoàn toàn phẩm giá, chỉ còn là những món đồ chơi phục vụ cho ảo tưởng thống trị."
        ],
        'en': [
            "Among the most defining traits of Marc Dutroux was his capacity for extreme psychological Compartmentalization.",
            "By daylight, he maintained the routine of an ordinary working man: visiting garages, bargaining over scrap parts, chatting with neighbors.",
            "Yet as night fell, he transformed into an omnipotent tyrant ruling a custom-built underground dungeon.",
            "This cognitive split allowed the offender to seal away all moral guilt into a completely isolated mental vault.",
            "He was incapable of perceiving the terror or agonizing human suffering of the captive children.",
            "In his distorted mind, the victims were wholly dehumanized, reduced to inanimate instruments serving his domination fantasies."
        ],
        'ja': [
            "マルク・デュトルーの最も顕著な特徴の一つは、極限まで発達した認知的区画化、すなわちコンパートメンタリゼーションでした。",
            "昼間、彼は自動車整備工場を出入りし、廃品の部品代を値切り、近隣住人と世間話に興じる平凡な男を演じていました。",
            "しかし夜の帳が下りると、自ら設計した地下牢獄を冷酷に支配する全能の暴君へと豹変したのです。",
            "この精神の分離構造により、彼は罪悪感のすべてを心の隔離された金庫の中へと封じ込めることができました。",
            "彼は囚われの少女たちが流す涙や、人間としての耐え難い苦痛を認識することが全くできませんでした。",
            "その歪んだ内面において、被害者たちは完全に非人間化され、自らの支配妄想を満たす道具に成り下がっていたのです。"
        ]
    })

    # Block 9: INVESTIGATOR (10 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'ĐIỀU TRA VIÊN',
        'role_en': 'INVESTIGATOR',
        'role_ja': '捜査官',
        'note_vn': '(trích xuất dữ liệu điều tra, vạch trần lỗ hổng kiểm soát tư pháp)',
        'note_en': '(extracting investigative data, exposing catastrophic systemic parole failures)',
        'note_ja': '（捜査資料を引用し、壊滅的な司法監視体制の破綻を暴き出す）',
        'sfx_vn': '**[SFX]:** Tiếng lật trang tài liệu tòa án sột soạt, tiếng gõ bút dứt khoát trên bàn.',
        'sfx_en': '**[SFX]:** Rustling of court docket pages, followed by the decisive tapping of a pen on a wooden desk.',
        'sfx_ja': '**[SFX]:** 裁判記録のページが擦れ合う乾いた紙音、机に叩きつけられるペンの硬い音。',
        'vn': [
            "Hồ sơ lưu trữ của cơ quan tư pháp cho thấy Marc Dutroux từng bị kết án mười ba năm rưỡi tù giam vào năm 1989 vì tội bắt cóc và cưỡng hại các bé gái.",
            "Thế nhưng chỉ sau hơn ba năm thụ án, vào tháng Tư năm 1992, hắn đã được ân xá có điều kiện nhờ sự can thiệp của các báo cáo tâm lý hành vi bề mặt.",
            "Các chuyên viên cải tạo thời điểm đó đánh giá hắn là một tù nhân gương mẫu, biết phục tùng và không còn nguy cơ tái phạm.",
            "Đây chính là một trong những thất bại thể chế đau đớn nhất của hệ thống tư pháp Bỉ thập niên 1990.",
            "Việc được thả tự do trước hạn không hề làm đối tượng thức tỉnh, mà ngược lại củng cố thêm niềm tin rằng bộ máy công quyền quá ngây thơ và dễ bị dắt mũi.",
            "Ngay sau khi bước ra khỏi trại giam, Dutroux lập tức mua căn nhà ở Marcinelle và bắt tay vào việc mua vật liệu xây dựng hầm ngầm.",
            "Hắn tham gia vào các đường dây trộm cắp xe hơi để có tiền trang trải cho những dự án đen tối của mình.",
            "Mọi cảnh báo từ các sĩ quan thực địa về dấu hiệu bất thường của hắn đều bị trôi dạt giữa sự bất đồng và cạnh tranh nghiệp vụ giữa lực lượng Hiến binh và Cảnh sát Tư pháp.",
            "Sự thiếu đồng bộ trong chia sẻ thông tin tình báo đã vô tình tạo ra một hành lang an toàn cho kẻ thủ ác hoạt động suốt nhiều năm.",
            "Chúng tôi gọi đó là sự tê liệt của mạng lưới kiểm soát trước một kẻ ái kỷ có kỹ năng thao túng bậc thầy."
        ],
        'en': [
            "Official judicial archives reveal Marc Dutroux was sentenced to thirteen and a half years in prison in 1989 for child abduction and abuse.",
            "Yet after serving barely three years, in April 1992, he was granted early conditional parole based on superficial behavioral assessments.",
            "Correctional evaluators at the time mistakenly deemed him a compliant, model inmate posing minimal recidivism risk.",
            "This stands as one of the most tragic institutional oversights in modern Belgian judicial history.",
            "Early release did not rehabilitate the offender; instead, it solidified his conviction that state authorities were naive and easily duped.",
            "Immediately upon release, Dutroux purchased the Marcinelle property and procured raw materials to construct his underground vault.",
            "He embedded himself in illicit car-theft rings to finance his predatory subterranean engineering projects.",
            "Field officers' warnings regarding his suspicious activities vanished into bureaucratic rivalries between the Gendarmerie and Judicial Police.",
            "A catastrophic lack of intelligence coordination inadvertently gifted this predator an unmonitored operational corridor for years.",
            "We classify this as systemic surveillance paralysis in the face of a master manipulative narcissist."
        ],
        'ja': [
            "公式な司法記録によれば、マルク・デュトルーは1989年、少女たちの誘拐および暴行罪で禁錮13年半の判決を受けていました。",
            "しかし服役からわずか3年余りの1992年4月、表面的な行動評価報告書に基づき、条件付き早期仮釈放が認められてしまったのです。",
            "当時の更生指導担当官たちは、彼を従順な模範囚であり、再犯の恐れは極めて低いと誤って判断しました。",
            "これこそが、1990年代のベルギー司法制度における最も痛恨の制度的失態の一つでした。",
            "早期釈放は更生をもたらすどころか、国家機関など世間知らずで容易に操れるという彼の傲慢な確信を強固にしただけでした。",
            "刑務所の門を出るやいなや、デュトルーはマルシネルの物件を買い取り、地下秘密部屋の建設資材を調達し始めたのです。",
            "彼は地下の暗黒プロジェクトの資金を稼ぎ出すため、組織的な自動車盗難グループに関与しました。",
            "彼の不審行動を警告した現場警察官たちの声は、憲兵隊と司法警察の間の縄張り争いと官僚主義の壁に阻まれて消え去りました。",
            "情報共有の致命的な欠落が、この凶悪な捕食者に対して何年もの間、野放しの安全回廊を与えてしまったのです。",
            "私たちはこれを、人心掌握に長けた病的ナルシシストの前に屈した、監視システムの麻痺状態と呼んでいます。"
        ]
    })

    # Block 10: HOST (5 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(trầm ngâm, dẫn dắt vào mối quan hệ cộng sinh độc hại)',
        'note_en': '(contemplative, introducing the toxic symbiotic relationship)',
        'note_ja': '（物思いに沈むように、有害な共生関係の分析へと導く）',
        'vn': [
            "Một kẻ bạo chúa không thể duy trì vương quốc tội ác của mình nếu không có một người hỗ trợ trong bóng tối.",
            "Và tại ngôi nhà số 128 phố Philippeville, người đồng hành ấy không ai khác chính là vợ hắn, Michelle Martin.",
            "Từng là một nữ giáo viên tiểu học có học thức, điều gì đã đẩy một người phụ nữ vào vị thế kẻ đồng lõa tàn nhẫn?",
            "Làm thế nào một người mẹ đang nuôi dưỡng những đứa con nhỏ lại có thể thản nhiên bước đi trên sàn nhà mà bên dưới là tiếng khóc than của những đứa trẻ vô tội?",
            "Câu trả lời nằm ở một cấu trúc tâm lý phụ thuộc độc hại và sự tha hóa đạo đức diễn ra từng ngày."
        ],
        'en': [
            "A tyrant cannot sustain his underworld kingdom without an enabler standing in the shadows.",
            "And at number 128 Rue de Philippeville, that enabler was none other than his wife, Michelle Martin.",
            "Once an educated elementary school teacher, what compelled a woman to descend into the role of a heartless accomplice?",
            "How could a mother caring for her own young children walk casually across floorboards beneath which innocent captives wept?",
            "The explanation resides within a toxic dependency dynamic and gradual moral erosion unfolding day by day."
        ],
        'ja': [
            "いかなる暴君も、影に立つ従順な協力者の存在なくして自らの暗黒王国を維持することはできません。",
            "そしてフィリップヴィル通り128番地において、その協力者こそ他ならぬ妻ミシェル・マルタンだったのです。",
            "かつて教養ある小学校教師であった女性が、なぜ無慈悲な共犯者の立場へと堕落してしまったのでしょうか？",
            "自らも幼い我が子を育てる一人の母親が、足元から罪なき子らの泣き声が漏れる床の上を、どうして平然と歩くことができたのか？",
            "その答えは、病的な依存心理と、日々進行する道徳的腐食のダイナミクスの中に隠されていました。"
        ]
    })

    # Block 11: PSYCHOLOGIST (12 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'CHUYÊN GIA TÂM LÝ',
        'role_en': 'PSYCHOLOGIST',
        'role_ja': '心理学者',
        'note_vn': '(giọng học thuật sắc sảo, bóc tách mối quan hệ kiểm soát cưỡng ép Coercive Control và Hội chứng phụ nữ bị bạo hành)',
        'note_en': '(incisive clinical insight, dissecting Coercive Control and Battered Woman dynamics)',
        'note_ja': '（鋭い臨床的知見で、強圧的支配Coercive Controlと被虐待女性症候群の病理を解体する）',
        'vn': [
            "Dưới lăng kính tâm lý học tội phạm, mối quan hệ giữa Marc Dutroux và Michelle Martin là một ví dụ điển hình của hiện tượng Kiểm soát Cưỡng ép hay Coercive Control.",
            "Martin gặp Dutroux khi còn rất trẻ và nhanh chóng bị cuốn vào một mạng lưới thao túng tâm lý khép kín.",
            "Dutroux sử dụng sự kết hợp tàn nhẫn giữa bạo lực thể xác, cô lập xã hội và những lời đe dọa thường trực để triệt tiêu hoàn toàn ý chí độc lập của vợ.",
            "Theo học thuyết Hội chứng Phụ nữ bị bạo hành của tiến sĩ Lenore Walker, nạn nhân lâu năm thường phát triển cơ chế phục tùng tuyệt đối như một chiến lược sinh tồn.",
            "Họ tin rằng cách duy nhất để tránh bị đòn roi trút lên đầu mình là làm hài lòng kẻ thống trị bằng mọi giá.",
            "Tuy nhiên, chúng ta không thể đơn thuần coi Michelle Martin là một nạn nhân thụ động vô tội.",
            "Ở đây đã diễn ra một quá trình Ngắt kết nối đạo đức hay Moral Disengagement theo lý thuyết của Albert Bandura.",
            "Martin đã sử dụng cơ chế 'Khuếch tán trách nhiệm' để tự trấn an rằng: 'Mọi chuyện đều do Marc quyết định, tôi chỉ là người hầu hạ bất lực'.",
            "Bà ta bình thường hóa sự hiện diện của căn hầm ngục tối, biến một tội ác kinh hoàng thành một phần thói quen sinh hoạt trong gia đình.",
            "Sự thờ ơ này đạt đến đỉnh điểm khi lòng trắc ẩn bị thay thế hoàn toàn bởi nỗi sợ hãi vị kỷ đối với người chồng bạo ngược.",
            "Khi ranh giới đạo đức đầu tiên bị phá vỡ, sự thỏa hiệp tiếp theo sẽ diễn ra một cách tự nhiên và trơn tru đến đáng sợ.",
            "Đó là con đường trượt dài từ một nạn nhân bị kiểm soát trở thành kẻ tiếp tay cho cái ác diệt chủng nhân tính."
        ],
        'en': [
            "Through a criminological lens, the dynamic between Marc Dutroux and Michelle Martin represents a textbook case of Coercive Control.",
            "Martin met Dutroux at a young, impressionable age and was swiftly ensnared in an airtight matrix of psychological manipulation.",
            "Dutroux employed a brutal cycle of physical violence, social isolation, and chronic terror to extinguish her autonomous will.",
            "Under Lenore Walker's Battered Woman Syndrome framework, chronic domestic victims often adopt absolute compliance as a survival mechanism.",
            "They internalize the belief that their only protection against severe retribution is placating the abuser at any cost.",
            "However, forensic science cannot categorize Michelle Martin merely as a passive, blameless victim.",
            "What occurred was profound Moral Disengagement as formulated by psychologist Albert Bandura.",
            "Martin weaponized 'Diffusion of Responsibility' to soothe her conscience: 'Marc controls everything; I am just a helpless subordinate.'",
            "She routinized the dungeon's horrific reality, integrating it into domestic daily life as though it were normal household maintenance.",
            "This callousness peaked when basic human empathy was entirely eclipsed by self-centered dread of her abusive spouse.",
            "Once the foundational moral boundary is compromised, subsequent complicity unfolds with terrifying ease and fluidity.",
            "This marks the fatal descent from a coerced partner into an active facilitator of absolute dehumanization."
        ],
        'ja': [
            "犯罪心理学の視点から見れば、マルク・デュトルーとミシェル・マルタンの関係性は「強圧的支配（コエルシブ・コントロール）」の典型例です。",
            "マルタンは極めて若い多感な時期にデュトルーと出会い、瞬く間に心理的操作の強固な網の目へと絡め取られました。",
            "デュトルーは身体的暴力、社会的孤立、そして絶え間ない脅迫を組み合わせ、妻の自律的な意志を完全に粉砕していきました。",
            "レノア・ウォーカー博士の「被虐待女性症候群」理論が示すように、長期的な被害者は生き残るための防衛策として絶対服従を身につけます。",
            "暴力の矛先が自分に向くのを防ぐ唯一の方法は、いかなる代償を払ってでも支配者を満足させることだと思い込むのです。",
            "しかしながら、法医学的見地からミシェル・マルタンを単なる受動的で無実な被害者と見なすことは到底できません。",
            "そこにはアルバート・バンデューラが提唱した「道徳的脱関与（モラル・ディスエンゲージメント）」の深いプロセスが介在していました。",
            "マルタンは「責任の拡散」を都合よく利用し、『すべては夫の命令であり、自分は無力な従属者に過ぎない』と自らに言い聞かせたのです。",
            "彼女は地下牢獄の凄惨な現実を日常化し、家庭の雑務の一部であるかのように慣れ親しんでいきました。",
            "この無神経さは、人間としての根源的な共感能力が、暴君への保身の恐怖によって完全に上書きされたときに頂点に達しました。",
            "最初の道徳的境界線が一度破綻してしまえば、その後の共謀は戦慄を覚えるほど滑らかに、自然に連鎖していくものです。",
            "これこそが、被虐待者から人間性を破壊する共犯者への、致命的な転落の軌跡だったのです。"
        ]
    })

    # Block 12: HOST (4 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(trầm giọng, hé lộ điểm tối lương tri mùa đông 1995-1996)',
        'note_en': '(darkening tone, revealing the nadir of moral conscience in winter 1995–1996)',
        'note_ja': '（声を沈め、1995年から1996年の冬における良心の最暗部を明かす）',
        'vn': [
            "Và rồi, phép thử tàn nhẫn nhất đối với lương tâm của Michelle Martin đã xảy ra vào mùa đông năm 1995.",
            "Marc Dutroux bất ngờ bị cảnh sát bắt giữ và tống giam trong hơn ba tháng vì liên quan đến một vụ trộm cắp xe tải.",
            "Trong suốt thời gian người chồng vắng nhà, chỉ có duy nhất Michelle Martin nắm giữ chìa khóa và sự sống còn của những đứa trẻ bên dưới.",
            "Một khoảnh khắc định mệnh mở ra cơ hội để một con người lựa chọn giữa sự hèn nhát tội lỗi và sự cứu chuộc sinh mạng."
        ],
        'en': [
            "Then, the ultimate, merciless test of Michelle Martin's conscience arrived during the winter of 1995.",
            "Marc Dutroux was abruptly arrested and detained for over three months in connection with a stolen truck investigation.",
            "Throughout her husband's imprisonment, Michelle Martin alone held the keys and the power of life and death over the children below.",
            "A defining crossroads emerged where a human being had to choose between cowardly complicity and saving innocent lives."
        ],
        'ja': [
            "そして1995年の冬、ミシェル・マルタンの良心に対する最も残酷な試練が訪れました。",
            "マルク・デュトルーが盗難トラック事件に関連して警察に身柄を拘束され、3か月以上収監されたのです。",
            "夫が不在の間、地下に閉じ込められた少女たちの鍵と生死の全権を握っていたのは、ミシェル・マルタンただ一人でした。",
            "臆病な共犯関係にしがみつくのか、それとも罪なき命を救い出すのか、人間としての決定的な分かれ道が訪れたのです。"
        ]
    })

    # Block 13: INVESTIGATOR (7 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'ĐIỀU TRA VIÊN',
        'role_en': 'INVESTIGATOR',
        'role_ja': '捜査官',
        'note_vn': '(giọng đanh thép, nêu chi tiết nghịch lý tàn nhẫn)',
        'note_en': '(steely tone, detailing the chillingly cruel contradiction)',
        'note_ja': '（冷徹な声で、戦慄すべき残酷な矛盾の事実を詳述する）',
        'vn': [
            "Biên bản thẩm vấn sau này ghi nhận một sự thật khiến bất kỳ ai có lương tri cũng phải căm phẫn đến tột cùng.",
            "Trong hơn chín mươi ngày Dutroux ở trong trại giam, Michelle Martin đều đặn lái xe đến ngôi nhà ở Marcinelle.",
            "Bà ta mang thức ăn và nước uống đến để chăm sóc chu đáo cho bầy chó cưng của chồng nuôi trong sân.",
            "Thế nhưng bà ta tuyệt nhiên không một lần mở cánh cửa hầm ngầm để mang dù chỉ là một mẩu bánh mì hay một ngụm nước cho hai bé gái Julie và Mélissa.",
            "Khi bị các điều tra viên chất vấn gay gắt tại sao không cứu các nạn nhân, Martin chỉ run rẩy đưa ra một lời bào chữa lạnh lùng:",
            "'Tôi sợ Marc phát hiện sẽ giết tôi khi anh ấy ra tù, và tôi sợ phải đối mặt với bóng tối dưới căn hầm ấy'.",
            "Sự bỏ mặc có tính toán này đã trực tiếp dẫn đến cái chết thương tâm vì kiệt sức và đói khát của hai sinh linh tám tuổi ngay dưới sàn nhà."
        ],
        'en': [
            "Subsequent interrogation transcripts record a reality that evokes profound outrage in anyone with a conscience.",
            "During the ninety-plus days Dutroux was locked away, Michelle Martin drove regularly to the Marcinelle property.",
            "She brought bowls of food and fresh water to meticulously care for her husband's pet dogs kept in the yard.",
            "Yet she never once opened the cellar door to offer so much as a crust of bread or a drop of water to eight-year-olds Julie and Mélissa.",
            "When investigators confronted her sharply on why she never intervened, Martin offered only a trembling, icy rationalization:",
            "'I feared Marc would kill me upon his release, and I was terrified of facing the darkness down in that cellar.'",
            "This deliberate abandonment directly caused the tragic demise by starvation and exhaustion of two eight-year-old children beneath the floor."
        ],
        'ja': [
            "後の尋問調書には、良識ある人間であれば誰もが激しい怒りを禁じ得ない戦慄の事実が克明に記録されています。",
            "デュトルーが収監されていた90日以上の間、ミシェル・マルタンは定期的にマルシネルの家へと車を走らせていました。",
            "彼女は夫が庭で飼っていた愛犬たちを甲斐甲斐しく世話するため、十分な餌と新鮮な水を与えていたのです。",
            "しかし、地下室の扉を開け、8歳のジュリーとメリッサにひとかけらのパンや一口のの水を与えることは一度もありませんでした。",
            "捜査官たちがなぜ子どもたちを救わなかったのか厳しく問い詰めた際、マルタンはただ震えながら冷淡な弁明を口にしました。",
            "『釈放されたらマルクに殺されると恐れていたし、あの地下室の暗闇に足を踏み入れるのが怖かったのです』と。",
            "この計算された完全な放置が、床下で飢えと衰弱により8歳の幼い2人の命が失われるという痛ましい悲劇を直接引き起こしたのです。"
        ]
    })

    # Block 14: HOST (4 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(trầm giọng đầy phẫn uất, nhấn mạnh sự tha hóa)',
        'note_en': '(solemn indignation, highlighting the absolute moral collapse)',
        'note_ja': '（静かな憤りを込め、道徳的崩壊の深淵を浮き彫りにする）',
        'vn': [
            "Cho chó ăn nhưng để hai đứa trẻ chết đói ngay bên dưới — đó là bản cáo trạng đanh thép nhất về sự tha hóa của một con người.",
            "Mọi lý lẽ về sự sợ hãi hay bị thao túng tâm lý đều hoàn toàn sụp đổ trước hành vi tàn nhẫn này.",
            "Khi bản năng tự bảo vệ của bản thân vượt lên trên tính mạng của đồng loại, ranh giới giữa người bị hại và kẻ thủ ác đã hoàn toàn bị xóa nhòa.",
            "Đó không còn là sự yếu đuối, đó là sự đồng lõa chủ động bằng hành vi bất hành động."
        ],
        'en': [
            "Feeding the dogs while allowing two captive children to starve directly below — that remains the ultimate indictment of human depravity.",
            "All psychological defenses of spousal coercion collapse entirely before the weight of this unspeakable neglect.",
            "When self-preservation eclipses the fundamental duty to human life, the line between victim and perpetrator is obliterated.",
            "This was no longer helplessness; this was active complicity through conscious inaction."
        ],
        'ja': [
            "犬に餌を与えながら、その真下で囚われの子どもたちを餓死させたという事実 — これこそが人間性の退廃を告発する最も重い罪状です。",
            "配偶者からの強圧や恐怖といういかなる心理的弁解も、この冷酷な不作為の前には完全に崩壊します。",
            "自らの保身が他者の生存という至高の倫理を踏み躙った瞬間、被害者と加害者の境界線は完全に消滅しました。",
            "それはもはや弱さなどではなく、意識的な沈黙と放置を通じた能動的な共犯関係に他ならなかったのです。"
        ]
    })

    # Block 15: PSYCHOLOGIST (6 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'CHUYÊN GIA TÂM LÝ',
        'role_en': 'PSYCHOLOGIST',
        'role_ja': '心理学者',
        'note_vn': '(phân tích cơ chế tê liệt cảm xúc và sự rạn nứt nhân cách)',
        'note_en': '(analyzing emotional blunting and cognitive dissonance collapse)',
        'note_ja': '（感情麻痺と認知的葛藤の崩壊メカニズムを分析する）',
        'vn': [
            "Hiện tượng Michelle Martin cho chúng ta thấy mặt tối đáng sợ của sự Tê liệt Cảm xúc hay Emotional Blunting.",
            "Để có thể tiếp tục sống và đối diện với bản thân, bộ não của bà ta buộc phải dựng lên cơ chế chối bỏ thực tại cực đoan.",
            "Bà ta coi những đứa trẻ như những thực thể không tồn tại trong tâm trí, một bí mật kinh hoàng mà tốt nhất là vờ như không có.",
            "Nhưng sự trốn tránh nhận thức ấy không thể xóa bỏ được vết nhơ trong tiềm thức.",
            "Nó tích tụ lại thành một Chấn thương Đạo đức hay Moral Injury âm ỉ, chuẩn bị cho sự sụp đổ tâm lý hoàn toàn khi bị phơi bày trước ánh sáng công lý.",
            "Và đó chính là mầm mống cho sự hối hận mang tính phòng vệ mà chúng ta sẽ phân tích ở Hồi bốn."
        ],
        'en': [
            "The phenomenon of Michelle Martin demonstrates the terrifying reality of pathological Emotional Blunting.",
            "To function and preserve a shred of self-image, her mind erected an extreme fortress of psychological denial.",
            "She treated the captives as non-existent entities, a dark anomaly best handled by pretending it did not exist.",
            "Yet cognitive avoidance can never scrub clean the deep stains left upon the human subconscious.",
            "It festered into a latent Moral Injury, priming her psyche for total collapse once exposed to the light of justice.",
            "This laid the psychological groundwork for the defensive remorse we will scrutinize in Act Four."
        ],
        'ja': [
            "ミシェル・マルタンに見られる現象は、病的な「感情麻痺（エモーショナル・ブランティング）」の戦慄すべき結末を示しています。",
            "日常を維持し、最低限の自己像を保つため、彼女の精神は極端な現実否認の城壁を築き上げざるを得ませんでした。",
            "彼女は囚われの少女たちを心の中に存在しないものとして扱い、見ないふりをすることで恐怖から逃避しようとしたのです。",
            "しかし、そうした認知的逃避も、人間の潜在意識に刻まれた深い道徳的汚濁を消し去ることは決してできません。",
            "それは燻る「道徳的負傷（モラル・インジャリー）」となって蓄積し、公の司法の光に晒された際の完全な精神崩壊を準備していきました。",
            "これこそが、第4幕で詳細に検証することになる、防衛的悔悟の心理的土台となったのです。"
        ]
    })

    # Block 16: HOST (3 lines)
    blocks.append({
        'act': 2,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(kết Hồi 2, chuyển tiếp kịch tính sang cuộc giam cầm và ý chí sinh tồn)',
        'note_en': '(concluding Act 2, transitioning to the harrowing captivity and survival struggle)',
        'note_ja': '（第2幕を結び、過酷な監禁生活と生存への闘争へと物語を繋ぐ）',
        'vn': [
            "Khi chiếc hộp tử thần Marcinelle khép lại trên số phận của những nạn nhân xấu số, một bi kịch khác lại tiếp tục tiếp diễn.",
            "Mùa hè năm 1996, hai nạn nhân tiếp theo là Sabine Dardenne và Laetitia Delhez bị bắt cóc và đưa vào chính căn hầm ấy.",
            "Nhưng lần này, cuộc đối đầu giữa kẻ săn mồi bệnh hoạn và một ý chí sinh tồn kiên cường phi thường đã tạo nên bước ngoặt lịch sử."
        ],
        'en': [
            "As that tomb in Marcinelle sealed the fate of those innocent souls, another harrowing chapter was already unfolding.",
            "In the summer of 1996, two more young victims, Sabine Dardenne and Laetitia Delhez, were abducted into that very dungeon.",
            "Yet this time, the clash between a sadistic captor and an astonishingly resilient will to survive forged a historic turning point."
        ],
        'ja': [
            "マルシネルの死の棺が幼き魂たちの運命を呑み込んだ後も、恐るべき悲劇の連鎖は止まりませんでした。",
            "1996年の夏、さらなる2人の被害者、サビーヌ・ダルデンヌとレティシア・デルヘズが拉致され、まさにその地下室へと幽閉されたのです。",
            "しかしこの時、サディスティックな捕食者と、驚異的な生存の意志との衝突が、歴史的な転換点をもたらすことになります。"
        ]
    })

    # ------------------ ACT 3: 8 BLOCKS (49 lines) ------------------
    # Block 17: HOST (4 lines)
    blocks.append({
        'act': 3,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(chuyển sang bối cảnh giam cầm ngột ngạt và sự kiên cường)',
        'note_en': '(evoking the suffocating confinement and extraordinary resilience)',
        'note_ja': '（息苦しい監禁の空間と、驚異的な精神的強靭さを描き出す）',
        'bgm_vn': '**[BGM]:** Tiếng Cello độc tấu u uất hòa cùng nhịp Bass nặng trĩu, tái hiện không gian ngột ngạt của hầm ngục và sự căng thẳng tột độ.',
        'bgm_en': '**[BGM]:** Somber solo cello blended with a heavy, pulsing bass, recreating the suffocating dungeon atmosphere and extreme tension.',
        'bgm_ja': '**[BGM]:** 陰鬱なチェロ・ソロと重く脈打つベースが重なり、地下牢獄の息苦しい閉塞感と極度の緊張感を再現する。',
        'vn': [
            "Ngày 28 tháng 5 năm 1996, cô bé mười hai tuổi Sabine Dardenne đang trên đường đạp xe tới trường tại thành phố Kain.",
            "Một chiếc xe van màu trắng bất ngờ chặn lối, và trong nháy mắt, tuổi thơ trong sáng của cô bé bị chôn vùi dưới căn hầm Marcinelle.",
            "Suốt tám mươi ngày đêm ròng rã sống trong bóng tối ẩm thấp, thiếu thốn ánh sáng mặt trời và bị đe dọa sinh mệnh liên tục.",
            "Thế nhưng, chính trong nghịch cảnh tột cùng ấy, một bản lĩnh sinh tồn phi thường đã tỏa sáng để chống lại sự tẩy não của kẻ thủ ác."
        ],
        'en': [
            "On May 28, 1996, twelve-year-old Sabine Dardenne was riding her bicycle to school in the town of Kain.",
            "A white utility van cut off her path, and within seconds, her innocent youth was swallowed into the Marcinelle cellar.",
            "For eighty agonizing days and nights in damp subterranean darkness, deprived of daylight and facing continuous mortal peril.",
            "Yet in the depths of that extreme adversity, an extraordinary psychological resilience shone forth to defy her captor's brainwashing."
        ],
        'ja': [
            "1996年5月28日、12歳の少女サビーヌ・ダルデンヌはカインの町で学校へ向かって自転車を走らせていました。",
            "突如現れた白いバンが行く手を遮り、瞬く間に彼女の無垢な青春はマルシネルの地下室の闇へと呑み込まれました。",
            "湿気と暗闇に閉ざされた地下で、日光を奪われ、絶え間ない生命の危機に脅かされ続けた過酷な80日と80夜。",
            "しかし、その極限の逆境の中で、捕食者の洗脳工作に抗う驚異的な精神の強靭さが光を放ち始めました。"
        ]
    })

    # Block 18: HOST (4 lines)
    blocks.append({
        'act': 3,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(bóc tách chiến thuật tẩy não The Savior Delusion)',
        'note_en': '(dissecting the brainwashing tactics of The Savior Delusion)',
        'note_ja': '（『救済者妄想』を用いた洗脳の手口を解剖する）',
        'vn': [
            "Marc Dutroux không chỉ tra tấn thể xác, mà còn áp dụng một chiến lược thao túng nhận thức vô cùng xảo quyệt.",
            "Hắn liên tục gieo rắc vào tâm trí Sabine rằng cha mẹ cô bé không hề yêu thương cô, rằng họ từ chối trả tiền chuộc để đón cô về.",
            "Hắn tự vẽ nên hình ảnh của những kẻ bắt cóc tàn độc bên ngoài và tự xưng mình là 'người bảo vệ' duy nhất bảo đảm sự an toàn cho cô bé.",
            "Đó là mưu đồ hủy hoại hoàn toàn điểm tựa tinh thần, buộc nạn nhân phải trao trọn niềm tin và sự phục tùng tuyệt đối cho chính kẻ giam cầm mình."
        ],
        'en': [
            "Marc Dutroux did not rely solely on physical coercion; he deployed insidious cognitive manipulation.",
            "He persistently poisoned Sabine's thoughts, claiming her parents did not love her and refused to pay ransom for her return.",
            "He fabricated a sinister fictional syndicate outside, posing as her benevolent 'savior' shielding her from worse violence.",
            "His objective was to sever her psychological anchors, forcing the child to invest total trust and submission in her captor."
        ],
        'ja': [
            "マルク・デュトルーは単なる身体的威圧にとどまらず、極めて狡猾な認知的操作戦術を展開しました。",
            "彼はサビーヌの両親が彼女を愛しておらず、身代金の支払いを拒絶したという嘘を執拗に吹き込み続けたのです。",
            "外部に凶暴な架空の犯罪組織が存在すると信じ込ませ、自分こそが彼女を守る唯一の『保護者』であると偽装しました。",
            "それは精神的拠り所を完全に破壊し、自らを幽閉している張本人に対して全幅の信頼と服従を捧げさせるための企みでした。"
        ]
    })

    # Block 19: INVESTIGATOR (7 lines)
    blocks.append({
        'act': 3,
        'role_vn': 'ĐIỀU TRA VIÊN',
        'role_en': 'INVESTIGATOR',
        'role_ja': '捜査官',
        'note_vn': '(phân tích tài liệu chứng cứ, các bức thư viết tay của nạn nhân)',
        'note_en': '(analyzing physical evidence and handwritten victim correspondence)',
        'note_ja': '（物的証拠と被害者の直筆の手紙を分析する）',
        'sfx_vn': '**[SFX]:** Tiếng sột soạt của giấy viết thư cũ, tiếng bút mực cọ xát trên mặt giấy thô ráp.',
        'sfx_en': '**[SFX]:** Fragile rustle of old letter paper, the soft scratching of a pen on coarse parchment.',
        'sfx_ja': '**[SFX]:** 古びた便箋が擦れ合う微かな紙音、粗末な紙の上を走るペンの筆跡音。',
        'vn': [
            "Khi khám xét căn nhà Marcinelle sau này, chúng tôi đã thu giữ được những bức thư viết tay của Sabine gửi cho mẹ.",
            "Dutroux từng hứa với cô bé rằng sẽ mang những bức thư này gửi qua bưu điện, nhưng thực chất hắn cất giấu toàn bộ vào ngăn kéo cá nhân.",
            "Mỗi dòng chữ đều thể hiện một sự tỉnh táo đáng kinh ngạc của một đứa trẻ mười hai tuổi bị giam cầm.",
            "Cô bé viết về tình yêu gia đình, dặn dò mẹ giữ gìn sức khỏe và luôn khẳng định một niềm tin son sắt rằng công lý sẽ tìm đến.",
            "Sabine không bao giờ tin vào câu chuyện bịa đặt rằng gia đình đã bỏ rơi mình.",
            "Cô bé duy trì ý thức về thời gian bằng cách đếm từng ngày, ghi nhớ từng âm thanh sinh hoạt và từng tiếng động phát ra từ phía trên trần hầm.",
            "Những tài liệu này là bằng chứng vô giá chứng minh ý chí kháng cự không thể bị khuất phục của nạn nhân trước sự kiểm soát độc hại."
        ],
        'en': [
            "During the subsequent search of the Marcinelle house, we recovered Sabine's handwritten letters to her mother.",
            "Dutroux repeatedly promised the child he would mail these letters, but instead hoarded them in his personal drawer.",
            "Every sentence reflected the breathtaking, lucid clarity of an imprisoned twelve-year-old girl.",
            "She wrote of unwavering family love, urged her mother to stay strong, and clung to a fierce conviction that rescue would come.",
            "Sabine never surrendered to the captor's deceit that her parents had abandoned her.",
            "She maintained temporal awareness by counting days, tracking subtle environmental noises, and memorizing sounds overhead.",
            "These documents provide priceless forensic proof of an unbreakable human spirit resisting coercive subjugation."
        ],
        'ja': [
            "後のマルシネル家屋の家宅捜索において、私たちはサビーヌが母親に宛てて書いた直筆の手紙の数々を押収しました。",
            "デュトルーは手紙を郵便で届けると少女に約束しながら、実際には自らの引き出しの奥深くに隠し持っていたのです。",
            "記された一行一行には、監禁された12歳の少女とは思えない驚異的で明晰な理性が宿っていました。",
            "彼女は家族への不変の愛を綴り、母の健康を気遣い、必ず救出の手が届くという確固たる信念を貫き通していました。",
            "サビーヌは、両親に見捨てられたという犯人の卑劣な虚言を決して受け入れることはありませんでした。",
            "彼女は日数を数え、環境の微細な変化を記録し、天井から響く物音を記憶することで時間感覚を維持し続けたのです。",
            "これらの手紙は、強圧的支配の前に屈することを拒絶した、人間の不屈の抵抗精神を示すかけがえのない証拠です。"
        ]
    })

    # Block 20: HOST (4 lines)
    blocks.append({
        'act': 3,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(trầm ngâm, đặt câu hỏi về hiện tượng tâm lý)',
        'note_en': '(contemplative, questioning conventional psychological assumptions)',
        'note_ja': '（深思に耽り、従来の心理学的通念に疑問を投げかける）',
        'vn': [
            "Nhiều người khi nghe lại câu chuyện này thường tự hỏi: Tại sao Sabine không bị rơi vào Hội chứng Stockholm?",
            "Làm thế nào một cô bé mới lớn có thể phân biệt được ranh giới giữa việc phục tùng để sống sót và việc bị đồng hóa tâm lý?",
            "Đây là một câu hỏi then chốt đòi hỏi góc nhìn chuyên sâu từ khoa học hành vi và tâm lý học chấn thương.",
            "Hãy lắng nghe chuyên gia tâm lý giải mã cơ chế Kháng cự Tỉnh táo của cô bé."
        ],
        'en': [
            "Reviewing this ordeal, many instinctively wonder: Why did Sabine not succumb to Stockholm syndrome?",
            "How could a young adolescent cleanly distinguish between tactical survival compliance and genuine emotional bonding?",
            "This critical question demands deep behavioral analysis through the lens of modern trauma psychology.",
            "Let us hear our criminal psychologist decode the mechanics of Lucid Resistance."
        ],
        'ja': [
            "この過酷な体験を振り返るとき、多くの人々は自問します。なぜサビーヌはストックホルム症候群に陥らなかったのか？",
            "思春期の少女が、生き延びるための戦術的従属と、犯人への心理的同一化の境界線をいかにして見極め得たのか？",
            "この極めて重要な問いは、現代のトラウマ心理学の知見を通じた深い行動分析を要求しています。",
            "犯罪心理学の専門家に、「明晰な抵抗（ルシッド・レジスタンス）」のメカニズムを解説してもらいましょう。"
        ]
    })

    # Block 21: PSYCHOLOGIST (11 lines)
    blocks.append({
        'act': 3,
        'role_vn': 'CHUYÊN GIA TÂM LÝ',
        'role_en': 'PSYCHOLOGIST',
        'role_ja': '心理学者',
        'note_vn': '(phân tích khoa học hành vi, giải mã Lucid Resistance và phân biệt với Stockholm syndrome)',
        'note_en': '(clinical expertise, breaking down Lucid Resistance vs Stockholm syndrome)',
        'note_ja': '（専門的見地から、明晰な抵抗とストックホルム症候群の違いを理論的に解明する）',
        'vn': [
            "Hội chứng Stockholm là một thuật ngữ thường bị truyền thông lạm dụng một cách đơn giản hóa quá mức.",
            "Để Stockholm syndrome hình thành, nạn nhân phải trải qua quá trình đồng hóa nhận thức, coi mục tiêu của kẻ bắt cóc là mục tiêu của chính mình.",
            "Nhưng trong trường hợp của Sabine Dardenne, chúng ta chứng kiến một cơ chế hoàn toàn khác: đó là 'Sự Kháng cự Tỉnh táo' hay Lucid Resistance.",
            "Sabine nhận thức rất rõ rằng Dutroux là một con quỷ dữ và cô bé đang ở trong một tình thế nguy hiểm chết người.",
            "Hành vi ngoan ngoãn nghe lời hay bảo gì nghe nấy không phải là sự đồng cảm, mà là một 'Chiến lược Nhẫn nhịn có Ý thức' để tự bảo toàn mạng sống.",
            "Cô bé hiểu rằng nếu phản kháng bằng vũ lực trong một không gian chật hẹp, cô sẽ bị tiêu diệt ngay lập tức.",
            "Do đó, Sabine chấp nhận đóng vai một người phục tùng trên bề mặt, nhưng trong nội tâm, bức tường bản ngã được giữ gìn nguyên vẹn.",
            "Những bức thư gửi mẹ chính là 'Mỏ neo tâm lý' vững chắc giúp cô kết nối với thế giới thực tại và bác bỏ mọi luận điệu thao túng của kẻ bắt cóc.",
            "Theo công trình nghiên cứu về Sức bật Tâm lý của Boris Cyrulnik, khả năng duy trì câu chuyện nội tâm độc lập chính là chìa khóa giúp nạn nhân vượt qua sang chấn.",
            "Sabine không bao giờ để kẻ thủ ác xâm chiếm tâm hồn mình.",
            "Đó là chiến thắng vang dội của lý trí và bản lĩnh con người trước bóng tối bạo tàn."
        ],
        'en': [
            "Stockholm syndrome is a concept frequently oversimplified and sensationalized across popular media.",
            "For genuine identification to occur, a captive must internalize the abductor's worldview and adopt their goals.",
            "Yet in Sabine Dardenne's testimony, we witness an entirely different paradigm: 'Lucid Resistance.'",
            "Sabine harbored zero illusions regarding Dutroux's monstrous nature and the mortal peril surrounding her.",
            "Her outward compliance was never emotional affection; it was a 'Conscious Appeasement Strategy' calibrated purely for survival.",
            "She intuitively recognized that physical confrontation within confined quarters would invite immediate lethal retaliation.",
            "Thus, Sabine adopted external obedience while fiercely preserving an intact, untouched psychological core inside.",
            "Her letters to her mother operated as an unyielding 'Psychological Anchor,' anchoring her to reality and repelling his manipulation.",
            "As Boris Cyrulnik's research on psychological resilience demonstrates, guarding an autonomous inner narrative is vital to surviving trauma.",
            "Sabine never surrendered the sovereign territory of her soul to her captor.",
            "This stands as a profound triumph of human dignity and intellect over brutal authoritarian darkness."
        ],
        'ja': [
            "ストックホルム症候群という概念は、メディアによってしばしば過度に単純化され、誤解されがちです。",
            "真の心理的同一化が成立するためには、被害者が犯人の世界観を内面化し、その目的を共有しなければなりません。",
            "しかしサビーヌ・ダルデンヌの事例において目撃されるのは、全く異なるパラダイム、すなわち「明晰な抵抗」です。",
            "サビーヌはデュトルーが冷酷な捕食者であり、自らが致死的な危機にあることを一瞬たりとも見誤りませんでした。",
            "彼女の従順な態度は好意などではなく、生き延びるためだけに計算された「意識的融和戦略（アピースメント）」だったのです。",
            "狭小な地下室で暴力的な直接対決を試みれば、即座に破滅を招くことを彼女は直感的に理解していました。",
            "それゆえに彼女は外面的には従順を演じつつ、内面の不可侵な自己領域を頑として守り抜いたのです。",
            "母親宛ての手紙は、現実世界との繋がりを保ち、犯人の洗脳工作を跳ね返す強固な「心理的アンカー」として機能しました。",
            "ボリス・シリュルニクのレジリエンス研究が示す通り、自律的な内なる物語を死守することこそがトラウマを生き抜く鍵となります。",
            "サビーヌは、自らの魂の主権領域を一寸たりとも捕食者に明け渡すことはありませんでした。",
            "これこそが、残虐な暗黒支配に対する人間の知性と尊厳の、決定的な勝利だったのです。"
        ]
    })

    # Block 22: HOST (8 lines)
    blocks.append({
        'act': 3,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(chuyển sang bước ngoặt vụ bắt cóc Laetitia Delhez và sự thức tỉnh của nhân chứng)',
        'note_en': '(shifting to the turning point of Laetitia Delhez abduction and alert witness)',
        'note_ja': '（レティシア・デルヘズ拉致事件の転換点と、目撃者の機転へと場面を移す）',
        'sfx_vn': '**[SFX]:** Tiếng bút ghi vội trên mẩu giấy nhỏ, tiếng còi xe cảnh sát rền vang từ xa.',
        'sfx_en': '**[SFX]:** Scribbling of a pencil on a small notepad, sirens screaming in the distance.',
        'sfx_ja': '**[SFX]:** 小さなメモ用紙に鉛筆を走らせる音、遠くから迫り来るパトカーのサイレン。',
        'vn': [
            "Cuộc đấu tranh sinh tồn trong hầm ngục Marcinelle bước vào một bước ngoặt quyết định vào đầu tháng Tám năm 1996.",
            "Ngày 9 tháng Tám, cô bé mười bốn tuổi Laetitia Delhez bị bắt cóc tại thị trấn Bertrix sau khi rời một hồ bơi công cộng.",
            "Dutroux cùng tên đồng phạm Michel Lelièvre đã đưa Laetitia về nhốt chung vào căn hầm cùng với Sabine.",
            "Thế nhưng, kẻ săn mồi tự mãn không hề hay biết rằng lần này, chiếc bẫy hoàn hảo của hắn đã để lại một lỗ hổng chí mạng.",
            "Một thiếu niên địa phương tình cờ đứng gần đó đã nhận thấy hành vi tấp xe bất thường của chiếc xe van màu trắng.",
            "Bằng một phản xạ cảnh giác tuyệt vời, người nhân chứng trẻ tuổi này đã kịp thời ghi lại một phần biển số xe khả nghi vào một mẩu giấy nhỏ.",
            "Một mẩu giấy tưởng chừng như bình thường đã trở thành chiếc chìa khóa vàng phá vỡ màn sương mù bế tắc suốt hơn một năm ròng rã.",
            "Lực lượng cảnh sát lập tức lần theo manh mối biển số và chiếc xe van trắng nhanh chóng đưa họ quay trở lại cái tên quen thuộc: Marc Dutroux."
        ],
        'en': [
            "The subterranean survival struggle reached its decisive tipping point in early August 1996.",
            "On August 9, fourteen-year-old Laetitia Delhez was abducted in Bertrix upon leaving a local swimming pool.",
            "Dutroux and his accomplice Michel Lelièvre transported Laetitia straight to the Marcinelle cellar alongside Sabine.",
            "Yet the arrogant predator was entirely blind to the fatal flaw his reckless confidence had left behind.",
            "A local teenage bystander nearby noticed the white van's suspicious movements and abrupt departure.",
            "Exercising remarkable vigilance, this young witness swiftly jotted down a partial license plate number on a scrap of paper.",
            "That modest paper scrap became the golden key shattering over a year of baffling investigative paralysis.",
            "Police immediately traced the registration data, and the white utility van pointed straight back to a familiar name: Marc Dutroux."
        ],
        'ja': [
            "マルシネルの地下で繰り広げられた生存の闘争は、1996年8月初旬、決定的な転換点を迎えます。",
            "8月9日、14歳の少女レティシア・デルヘズがベルトルの町で公営プールから出た直後に拉致されました。",
            "デュトルーと共犯者のミシェル・ルリエーヴルは、レティシアをマルシネルの地下室へと連行し、サビーヌと共に閉じ込めました。",
            "しかし、傲慢な捕食者は、自らの過信が残した致命的な破綻に全く気づいていませんでした。",
            "付近に居合わせた地元の若者が、白いバンの不審な動きと突如としての急発進を見逃さなかったのです。",
            "驚くべき機転と警戒心を発揮したその目撃者は、破れたメモ用紙に不審な車のナンバーの一部を素早く書き留めました。",
            "そのささやかな紙切れが、1年以上にわたって停滞していた捜査の深い混迷を打ち破る黄金の鍵となったのです。",
            "警察は直ちに車両登録データを追跡し、その白いバンは聞き覚えのある一つの名前へと一直線に繋がりました。マルク・デュトルーです。"
        ]
    })

    # Block 23: PSYCHOLOGIST (8 lines)
    blocks.append({
        'act': 3,
        'role_vn': 'CHUYÊN GIA TÂM LÝ',
        'role_en': 'PSYCHOLOGIST',
        'role_ja': '心理学者',
        'note_vn': '(phân tích tâm lý học nhân chứng và ý thức cộng đồng)',
        'note_en': '(analyzing witness psychology and communal vigilance)',
        'note_ja': '（目撃者心理とコミュニティの警戒意識の重要性を分析する）',
        'vn': [
            "Hành động của người nhân chứng ghi lại biển số xe là một minh chứng xuất sắc cho khái niệm 'Cảnh giác Sinh tồn Cộng đồng'.",
            "Thông thường, hiệu ứng Bàng quan hay Bystander Effect khiến mọi người chờ đợi người khác hành động.",
            "Người ta hay tự nhủ: 'Chắc chỉ là một chiếc xe đỗ nhầm, không có gì to tát'.",
            "Nhưng khi một cá nhân dám tin vào linh cảm bất an và chủ động ghi lại chi tiết thực tế, chuỗi domino của cái ác lập tức bị chặn đứng.",
            "Trong tâm lý học xã hội, đây chính là sự phá vỡ điểm mù tập thể.",
            "Một cử chỉ quan sát có trách nhiệm đã cứu sống hai mạng người và kéo toàn bộ tội ác ra trước ánh sáng.",
            "Đó là bài học đắt giá về việc mỗi công dân đều có thể trở thành một lá chắn bảo vệ an toàn cho xã hội.",
            "Sự thật không chỉ đến từ phòng thí nghiệm hình sự, mà bắt đầu từ chính sự tỉnh thức của những con người bình thường."
        ],
        'en': [
            "The witness who recorded the license plate provides a textbook model of proactive 'Communal Protective Vigilance.'",
            "Under the classic Bystander Effect, individuals routinely assume someone else will intervene or investigate.",
            "People comfort themselves with passive rationalizations: 'It's probably just a lost delivery driver, nothing alarming.'",
            "Yet when a single individual trusts their unease and records concrete objective data, the predator's domino chain halts.",
            "In social psychology, this represents the decisive puncture of collective denial.",
            "A solitary act of responsible observation directly saved two young lives and exposed an entire criminal underworld.",
            "This offers an enduring lesson: every conscious citizen serves as an indispensable frontline guardian of civil safety.",
            "Justice does not originate solely in high-tech forensic laboratories; it begins with the alertness of everyday observers."
        ],
        'ja': [
            "ナンバープレートを書き留めた目撃者の行動は、能動的な「コミュニティ防衛警戒心」の模範的な事例です。",
            "古典的な「傍観者効果」のもとでは、多くの人々が他人が介入してくれるだろうと責任を先送りにしてしまいます。",
            "人々は『道を間違えた配達車だろう、大したことではない』と自らに言い聞かせ、受動的に安心しようとするのです。",
            "しかし、一人の個人が自らの直感的不安を信じ、客観的な事実データを記録した瞬間、捕食者の悪のドミノは阻止されました。",
            "社会心理学において、これこそが集合的否認の壁を打破する決定的な一撃でした。",
            "責任ある観察というひとつの行動が、2つの若き命を直接救い、暗黒の全貌を白日の下に晒したのです。",
            "すべての良識ある市民が社会安全の最前線に立つ防波堤となり得るという、計り知れない教訓がここにあります。",
            "正義は高度な科学捜査研究所の中だけで生まれるのではなく、市井の人々の覚醒した眼差しから始まるのです。"
        ]
    })

    # Block 24: HOST (3 lines)
    blocks.append({
        'act': 3,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(kết Hồi 3, dẫn vào cuộc đột kích giải cứu nghẹt thở)',
        'note_en': '(concluding Act 3, leading into the breathless rescue raid)',
        'note_ja': '（第3幕を結び、緊迫した救出突入劇へと物語を導く）',
        'vn': [
            "Vòng vây nghiệp vụ đã nhanh chóng khép chặt xung quanh ngôi nhà số 128 phố Philippeville.",
            "Ngày 13 tháng Tám năm 1996, Marc Dutroux và Michelle Martin chính thức bị bắt giữ trong sự bàng hoàng của dư luận.",
            "Và hai ngày sau đó, cánh cửa hầm ngục Marcinelle cuối cùng đã bị phá vỡ để đưa những sinh linh sống sót trở về với ánh sáng."
        ],
        'en': [
            "The investigative dragnet rapidly tightened around number 128 Rue de Philippeville.",
            "On August 13, 1996, Marc Dutroux and Michelle Martin were arrested, sending tremors through public awareness.",
            "Two days later, the subterranean concrete dungeon in Marcinelle was finally breached, returning surviving captives to the light."
        ],
        'ja': [
            "捜査の包囲網は、フィリップヴィル通り128番地の家屋へと急速に狭められていきました。",
            "1996年8月13日、マルク・デュトルーとミシェル・マルタンが身柄を拘束され、世間に激震が走りました。",
            "そしてその2日後、ついにマルシネルの地下牢獄の分厚い扉が破られ、生き残った少女たちが光の中へと救出されたのです。"
        ]
    })

    # ------------------ ACT 4: 8 BLOCKS (52 lines) ------------------
    # Block 25: HOST (5 lines)
    blocks.append({
        'act': 4,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(trọng tâm biến chuyển tâm lý, cuộc xưng tội và cuộc giải cứu ngày 15/8/1996)',
        'note_en': '(psychological turning point, confessions and the historic August 15, 1996 rescue)',
        'note_ja': '（心理的転換点、供述の変遷と1996年8月15日の歴史的救出劇を描く）',
        'bgm_vn': '**[BGM]:** Tiếng đàn Dương cầm tối giản kết hợp tiếng vĩ cầm giằng xé phòng xử án, tạo không khí bi tráng và ngột ngạt của sự thật phơi bày.',
        'bgm_en': '**[BGM]:** Minimalist piano paired with harrowing courtroom violin, creating an intensely tragic atmosphere of truth unveiled.',
        'bgm_ja': '**[BGM]:** ミニマル・ピアノと緊迫した法廷バイオリンが交錯し、暴かれた真実の悲壮で重苦しい空気を醸し出す。',
        'vn': [
            "Ngày 15 tháng Tám năm 1996 đã đi vào lịch sử nước Bỉ như một ngày của những cảm xúc tột cùng đan xen giữa vỡ òa và đau đớn.",
            "Dưới áp lực thẩm vấn đanh thép và các bằng chứng không thể chối cãi, Marc Dutroux buộc phải thừa nhận nơi cất giấu các nạn nhân.",
            "Lực lượng cảnh sát phá tung kệ gỗ chứa đồ cơ khí dưới tầng hầm, để lộ một tấm cửa sắt nặng trĩu dẫn vào hốc tường bê tông.",
            "Khi ánh đèn pin đầu tiên quét qua bóng tối ẩm thấp, hình ảnh Sabine Dardenne và Laetitia Delhez bước ra còn sống đã làm rung động hàng triệu trái tim.",
            "Thế nhưng niềm vui cứu sống hai thiếu nữ nhanh chóng bị phủ bóng đen bởi những phát hiện kinh hoàng ngay sau đó."
        ],
        'en': [
            "August 15, 1996, etched itself permanently into Belgian history as a day of overwhelming relief torn by profound tragedy.",
            "Confronted by relentless interrogation and irrefutable evidence, Marc Dutroux was forced to yield the location of his captives.",
            "Officers dismantled the heavy workshop shelving in the cellar, uncovering a reinforced hatch leading into a hidden vault.",
            "When flashlight beams pierced the damp dark, the miraculous emergence of Sabine Dardenne and Laetitia Delhez alive shook millions.",
            "Yet that moment of deliverance was instantly shadowed by sickening discoveries unearthed in the days that followed."
        ],
        'ja': [
            "1996年8月15日は、胸を突く安堵と底知れぬ痛哭が交錯する日として、ベルギーの歴史に永遠に刻まれました。",
            "執拗な尋問と反論の余地のない証拠の前に追い詰められたマルク・デュトルーは、ついに隠し場所の自白を余儀なくされたのです。",
            "捜査官たちが地下室の重い作業棚を解体すると、コンクリートの壁の奥へと通じる頑丈な鉄扉が現れました。",
            "湿った暗闇を懐中電灯の光が貫いた瞬間、サビーヌとレティシアが生きて歩み出てきた光景は、数百万の人々の心を激しく揺さぶりました。",
            "しかし、2人の少女が生還した奇跡の歓喜は、直後に暴かれた戦慄の事実によって一瞬にして暗雲へと呑み込まれました。"
        ]
    })

    # Block 26: INVESTIGATOR (9 lines)
    blocks.append({
        'act': 4,
        'role_vn': 'ĐIỀU TRA VIÊN',
        'role_en': 'INVESTIGATOR',
        'role_ja': '捜査官',
        'note_vn': '(giọng đanh thép, đau đớn tột cùng khi công bố việc khai quật thi thể)',
        'note_en': '(steely, gripped by solemn pain, announcing the tragic recovery of remains)',
        'note_ja': '（冷徹さの奥に深い悲痛を滲ませ、遺体発掘の痛ましい調査結果を告げる）',
        'vn': [
            "Niềm hy vọng mong manh tìm thấy những đứa trẻ mất tích từ năm 1995 đã vỡ vụn tại khu vườn ở Sars-la-Buissière.",
            "Chỉ hai ngày sau cuộc giải cứu, cơ quan chức năng đã khai quật được thi thể của hai bé gái Julie Lejeune và Mélissa Russo.",
            "Các kết quả giám định pháp y khẳng định hai em đã qua đời vì kiệt sức và đói khát trong chính căn hầm Marcinelle vào đầu năm 1996.",
            "Tiếp đó, thi thể của hai thiếu nữ An Marchal và Eefje Lambrecks cũng được tìm thấy tại một khu đất khác thuộc sở hữu của đối tượng.",
            "Toàn bộ quy mô của một chuỗi tội ác bệnh lý kéo dài nhiều năm đã hoàn toàn bị phơi bày trần trụi.",
            "Trước những bằng chứng vật chất sắt đá, thái độ của Marc Dutroux chỉ là sự chối bỏ ái kỷ và tìm cách đổ tội cho đồng bọn.",
            "Hắn tuyên bố mình chỉ là một mắt xích phục vụ cho một mạng lưới ngầm quyền lực bên ngoài hòng tự giảm nhẹ tội danh.",
            "Trong khi đó, Michelle Martin bắt đầu tung ra những giọt nước mắt sám hối, tự nhận mình là nạn nhân bị bạo hành cưỡng bức.",
            "Một cuộc đấu tranh cân não mới lại bắt đầu ngay trong phòng thẩm vấn giữa các chuyên gia và kẻ đồng lõa."
        ],
        'en': [
            "Frail hopes of recovering the children missing since 1995 dissolved tragically in a backyard garden at Sars-la-Buissière.",
            "Barely two days after the rescue, authorities exhumed the tragic remains of eight-year-olds Julie Lejeune and Mélissa Russo.",
            "Forensic pathology confirmed both children had perished from sheer starvation and neglect inside the Marcinelle vault in early 1996.",
            "Shortly thereafter, the bodies of teenagers An Marchal and Eefje Lambrecks were uncovered at another property tied to Dutroux.",
            "The terrifying scope of a multi-year systematic criminal spree was laid completely bare.",
            "Faced with unassailable forensic evidence, Marc Dutroux defaulted to classic narcissistic denial, blaming accomplices.",
            "He spun fabricated tales of serving an omnipotent elite syndicate in a desperate gambit to deflect primary accountability.",
            "Simultaneously, Michelle Martin wept torrents of remorse, styling herself purely as a terrorized victim of spousal violence.",
            "A grueling psychological chess match commenced within interrogation chambers to dismantle this accomplice's narrative."
        ],
        'ja': [
            "1995年から失踪していた子どもたちが無事であるという一縷の望みは、サール＝ラ＝ビュイシエールの庭で残酷にも砕け散りました。",
            "救出劇からわずか2日後、当局は8歳の少女ジュリーとメリッサの痛ましい遺体を掘り起こしました。",
            "法医学鑑定の結果、2人の幼い命は1996年初頭、まさにあのマルシネルの地下室で飢餓と衰弱により絶命したことが確認されました。",
            "続いて、10代のアン・マルシャルとエーフイェ・ランブレックスの遺体も、デュトルーに関連する別の土地で発見されました。",
            "長年にわたる病的な連続犯罪の全貌が、完全に白日の下に晒されたのです。",
            "動かぬ法医学的証拠を突きつけられても、マルク・デュトルーは自己愛的な否認に終始し、共犯者たちへ責任を擦り付けようとしました。",
            "彼は自らの主犯責任を軽減するため、自らは外部の強大なエリート地下組織の単なる手先に過ぎないと虚構を並べ立てたのです。",
            "その一方で、ミシェル・マルタンは涙ながらの悔悟を演じ、自らは夫の暴力に怯える一方的な被害者であったと主張し始めました。",
            "取調室において、捜査陣とこの狡猾な共犯者との間で、息詰まる心理戦の火蓋が切って落とされたのです。"
        ]
    })

    # Block 27: HOST (5 lines)
    blocks.append({
        'act': 4,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(đào sâu vào câu hỏi trọng tâm: Tại sao lại hối hận? Cơ chế tâm lý gì ở đây?)',
        'note_en': '(probing the core question: Why remorse? What psychological mechanism is at work?)',
        'note_ja': '（中核的命題へと迫る：なぜ悔悟したのか？そこにどのような心理的メカニズムが働いていたのか？）',
        'vn': [
            "Và đây chính là điểm nút tâm lý phức tạp và nhân bản nhất của toàn bộ hồ sơ:",
            "Tại sao Michelle Martin lại hối hận? Cơ chế tâm lý gì thực sự vận hành đằng sau sự ăn năn muộn màng của bà ta?",
            "Đó là sự thức tỉnh chân chính của một lương tri từng bị đóng băng, hay chỉ là một chiếc mặt nạ phòng vệ để tìm kiếm sự khoan hồng của pháp luật?",
            "Để trả lời câu hỏi nhức nhối này, chúng ta cần lắng nghe chính lời khai đầy giằng xé của người trong cuộc;",
            "trước khi chuyên gia tâm lý bóc tách từng tầng nhận thức sâu kín nhất của bản ngã con người."
        ],
        'en': [
            "This leads us to the most complex, profoundly human psychological crossroad of the entire case:",
            "Why did Michelle Martin express remorse? What cognitive mechanisms truly operated behind her belated repentance?",
            "Did this signify the genuine awakening of a frozen conscience, or was it a defensive mask calculated to secure institutional mercy?",
            "To answer this agonizing question, we must first hear the conflicted testimony of the accomplice herself;",
            "before our criminal psychologist dissects the deepest subconscious strata of this fragmented self."
        ],
        'ja': [
            "そしてこれこそが、事件全体の中で最も複雑で人間的な心理の交差点です。",
            "なぜミシェル・マルタンは後悔したのか？その遅すぎた悔悟の裏で、実際にどのような心理メカニズムが機能していたのか？",
            "それは凍りついていた良心の真の覚醒だったのか、それとも減刑を勝ち取るための計算された防衛の仮面に過ぎなかったのか？",
            "この痛切な問いに答えるため、私たちはまず当事者自身の葛藤に満ちた証言に耳を傾けなければなりません。",
            "その上で、犯罪心理学者がこの分裂した自我の最も深奥にある無意識の層を解剖していきます。"
        ]
    })

    # Block 28: ORDINARY PERSON (8 lines)
    blocks.append({
        'act': 4,
        'role_vn': 'NGƯỜI BÌNH THƯỜNG',
        'role_en': 'ORDINARY PERSON',
        'role_ja': '一般人',
        'note_vn': '(N2: Lời tự sự tái hiện của Michelle Martin, giọng nghẹn ngào, sợ hãi đan xen tội lỗi tột cùng)',
        'note_en': '(N2: Reconstruction of Michelle Martin voice, choked with dread and overwhelming guilt)',
        'note_ja': '（N2：ミシェル・マルタンの独白の再現、恐怖と極度の罪悪感に喘ぐ声）',
        'vn': [
            "Những ngày tháng đó, tôi sống trong một địa ngục của sự sợ hãi và mù quáng tột cùng.",
            "Marc là một cái bóng khổng lồ bao trùm lấy mọi suy nghĩ, mọi hành động và từng hơi thở của tôi.",
            "Mỗi lần nhìn vào cánh cửa hầm, tôi nghe thấy tiếng nói yếu ớt vọng lên nhưng đôi chân tôi hoàn toàn đông cứng.",
            "Tôi tự nhủ rằng nếu tôi hé lộ ra ngoài, Marc sẽ giết chết cả tôi lẫn hai đứa con gái nhỏ của chúng tôi.",
            "Tôi đem thức ăn cho chó để tự đánh lừa bản thân rằng mình vẫn đang làm tròn bổn phận bình thường trong gia đình.",
            "Nhưng khi nhìn thấy những cỗ quan tài trắng nhỏ bé được đưa lên từ lòng đất, tôi hiểu rằng không một lý lẽ nào trên đời có thể rửa sạch vết nhơ này.",
            "Tôi ghê tởm chính bản thân mình, ghê tởm sự hèn nhát đã biến tôi thành một kẻ đồng lõa tàn nhẫn.",
            "Tôi xin lỗi những người làm cha, làm mẹ; dù tôi biết hàng ngàn lời xin lỗi cũng vĩnh viễn là không bao giờ đủ."
        ],
        'en': [
            "During those dark months, I existed in an absolute purgatory of terror and total psychological blindness.",
            "Marc was a towering monstrous shadow suffocating every thought, every step, and every breath I took.",
            "Every time I glanced toward that cellar door, faint sounds filtered up, yet my limbs froze in absolute terror.",
            "I convinced myself that if I whispered a word, Marc would slaughter both me and our two young daughters.",
            "I fed the dogs to deceive myself into believing I was merely maintaining an ordinary household routine.",
            "Yet seeing those tiny white caskets exhumed from the soil, I knew no excuse on earth could ever cleanse my stain.",
            "I felt sickened by my very existence, utterly revulsed by the cowardice that transformed me into a ruthless accomplice.",
            "I beg the forgiveness of those grieving parents; though I know millions of apologies can never suffice."
        ],
        'ja': [
            "あの暗黒の日々、私は恐怖と完全な盲目という名の地獄の中で生きていました。",
            "マルクは私のあらゆる思考、あらゆる行動、そして呼吸のすべてを圧殺する巨大な影だったのです。",
            "あの地下室の扉に視線を向けるたび、微かな声が聞こえてくるようでしたが、私の足は恐怖で完全に硬直していました。",
            "もし口を割れば、マルクは私だけでなく、2人の幼い娘たちまでも惨殺するに違いないと思い込んでいたのです。",
            "犬に餌を与えたのは、自分が平凡な家庭の務めを果たしているのだと自らを欺くための悲惨な言い訳でした。",
            "しかし、土の中から掘り起こされた小さな白い棺を目にしたとき、地上のいかなる弁解も自らの罪の汚れを洗い流せないことを悟りました。",
            "私は自分自身に激しい吐き気を覚えました。私を冷酷な共犯者へと仕立て上げた己の臆病さに、心の底から絶望したのです。",
            "遺族である親御さんたちに心からお詫び申し上げます。何千、何万の謝罪の言葉を重ねようとも、決して許されるはずがないと知りながら。"
        ]
    })

    # Block 29: HOST (6 lines)
    blocks.append({
        'act': 4,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(trầm ngâm, đặt vấn đề phân tích khoa học hành vi)',
        'note_en': '(reflective, transitioning to behavioral scientific breakdown)',
        'note_ja': '（沈思黙考し、行動科学による客観的分析へとバトンを渡す）',
        'vn': [
            "Lời tự thú đầy giằng xé của Michelle Martin phản ánh đúng trạng thái chao đảo của một bản ngã bị nghiền nát giữa tội lỗi và sự tự vệ.",
            "Xã hội Bỉ thời điểm đó hoàn toàn không chấp nhận những giọt nước mắt này, coi đó là sự đạo đức giả trơ trẽn của một kẻ sát nhân gián tiếp.",
            "Thế nhưng, dưới góc nhìn khoa học hành vi, sự ăn năn của con người luôn là một cấu trúc đa tầng vô cùng phức tạp.",
            "Tại sao sự hối hận ấy chỉ thực sự bộc phát khi đối tượng đã bị tách rời khỏi người chồng bạo ngược và đối diện với bức tường nhà giam?",
            "Cơ chế nào đã kích hoạt nỗi dằn vặt này và đâu là ranh giới giữa lương tâm chân chính và toan tính sinh tồn?",
            "Chuyên gia tâm lý học tội phạm sẽ bóc tách bốn cơ chế kích hoạt sự hối hận trong hồ sơ này."
        ],
        'en': [
            "Michelle Martin's agonizing confession captures a fractured psyche caught between unbearable guilt and self-preservation.",
            "Belgian society at large overwhelmingly rejected her tears, dismissing them as the shameless theatrics of an indirect killer.",
            "Yet through behavioral science, human remorse is understood as an intensely layered, contradictory architecture.",
            "Why did this contrition manifest only after she was physically severed from her abuser and facing cold prison bars?",
            "What psychological catalyst unlocked this torment, and where lies the divide between authentic conscience and survival calculus?",
            "Our criminal psychologist will now dissect the four cognitive catalysts governing remorse in this case."
        ],
        'ja': [
            "ミシェル・マルタンの葛藤に満ちた告白は、耐え難い罪悪感と自己保身の狭間で粉々に砕けた自我の動揺を捉えています。",
            "当時のベルギー社会は彼女の涙を一切受け入れず、間接的殺人者の厚顔無恥な欺瞞劇として激しく糾弾しました。",
            "しかし行動科学の視座から見れば、人間の悔悟の心理とは極めて重層的で矛盾に満ちた構造を持っています。",
            "なぜその反省は、暴君である夫から物理的に隔離され、冷たい監獄の鉄格子と向き合って初めて噴出したのか？",
            "何がこの激しい苦悩を引き金を引いたのか、そして真の良心と生き残るための計算の境界線はどこにあるのか？",
            "犯罪心理学者が、この事件における悔悟を司る4つの認知的メカニズムを解剖します。"
        ]
    })

    # Block 30: INVESTIGATOR (4 lines)
    blocks.append({
        'act': 4,
        'role_vn': 'ĐIỀU TRA VIÊN',
        'role_en': 'INVESTIGATOR',
        'role_ja': '捜査官',
        'note_vn': '(nhận định nghiệp vụ về tính xác thực của lời khai)',
        'note_en': '(forensic operational assessment of confession credibility)',
        'note_ja': '（供述の信憑性に関する捜査実務上の冷静な見解を述べる）',
        'vn': [
            "Trong quá trình lấy lời khai, chúng tôi luôn phải tỉnh táo trước hiện tượng 'Hối hận Phòng vệ' hay Defensive Remorse.",
            "Khi đối mặt với mức án ba mươi năm tù hoặc tù chung thân, bản năng sinh tồn tự nhiên thúc đẩy nghi phạm tìm kiếm sự đồng cảm.",
            "Martin cố gắng khắc họa mình như một nạn nhân bị kiểm soát để tránh khung hình phạt cao nhất dành cho kẻ đồng mưu.",
            "Tuy nhiên, sự day dứt về cái chết của hai đứa trẻ là một thực tế tâm lý không thể phủ nhận hoàn toàn."
        ],
        'en': [
            "Throughout forensic interrogations, investigators must remain rigorously vigilant against 'Defensive Remorse.'",
            "Facing thirty years or life imprisonment, raw survival instinct compels suspects to engineer judicial sympathy.",
            "Martin deliberately amplified her victim status under coercive control to evade the maximum penalties reserved for co-conspirators.",
            "Nevertheless, her psychological torment over the children's demise constituted a tangible clinical reality."
        ],
        'ja': [
            "司法尋問の実務において、捜査陣は常に「防衛的悔悟（ディフェンシブ・リモース）」の罠を厳格に警戒しなければなりません。",
            "30年の禁錮刑や終身刑という過酷な現実を前にした時、原始的な生存本能が容疑者に同情を誘う言動を取らせるのです。",
            "マルタンは強圧的支配の被害者という立場をことさらに強調し、共謀主犯としての最高刑を免れようと画策しました。",
            "それにもかかわらず、幼い子どもたちの死に対する彼女の心理的苦悶が、紛れもない臨床的現実であったこともまた事実です。"
        ]
    })

    # Block 31: PSYCHOLOGIST (9 lines)
    blocks.append({
        'act': 4,
        'role_vn': 'CHUYÊN GIA TÂM LÝ',
        'role_en': 'PSYCHOLOGIST',
        'role_ja': '心理学者',
        'note_vn': '(giải phẫu chuyên sâu 4 cơ chế kích hoạt sự hối hận)',
        'note_en': '(deep clinical dissection of four cognitive catalysts of remorse)',
        'note_ja': '（悔悟の情を活性化させた4つの認知的メカニズムを臨床的に解剖する）',
        'vn': [
            "Để giải mã câu hỏi 'Tại sao lại hối hận?', chúng ta cần bóc tách bốn cơ chế tâm lý kích hoạt sự chuyển biến ở Michelle Martin.",
            "Thứ nhất là Sự sụp đổ của Bất hòa Nhận thức hay Cognitive Dissonance Breakdown.",
            "Khi Dutroux còn ở bên cạnh, Martin bám vào chiếc phao cứu sinh 'mình làm thế vì sợ hãi'.",
            "Nhưng khi hai cỗ quan tài trắng xuất hiện, bức tường tự lừa dối sụp đổ hoàn toàn; cái chết của hai đứa trẻ là một thực tế tàn khốc mà không cơ chế phòng vệ nào có thể biện minh nổi.",
            "Thứ hai là Chấn thương Đạo đức hay Moral Injury — trạng thái một cá nhân bị sang chấn tâm lý sâu sắc vì chính hành vi phi nhân tính do mình gây ra.",
            "Thứ ba là Sự giải phóng khỏi Trường Lực Kiểm soát Cưỡng ép: việc Dutroux bị bắt giam đã phá vỡ chiếc lồng kiểm soát tinh thần, cho phép lý trí của Martin hoạt động trở lại sau nhiều năm bị tê liệt.",
            "Và thứ tư là Tính Lưỡng phân giữa Lương tâm và Sinh tồn: sự hối hận của bà ta vừa là nỗi đau lương tri chân thực, vừa là nỗ lực vô thức nhằm cứu chuộc một phần bản ngã đã nát vụn.",
            "Việc sau này Martin xin vào sống tại Tu viện Clarisse năm 2012 chính là biểu hiện cuối cùng của nỗ lực tìm kiếm sự thanh tẩy tâm hồn trước sự chối bỏ vĩnh viễn của xã hội.",
            "Sự hối hận ấy có thể không chuộc được tội ác, nhưng nó là minh chứng cho thấy ngọn lửa lương tri dù bị vùi dập đến đâu vẫn có thể bùng cháy để thiêu đốt kẻ phạm tội."
        ],
        'en': [
            "To resolve 'Why remorse?', we must dissect four interlocking psychological catalysts governing Michelle Martin's shift.",
            "First is Cognitive Dissonance Breakdown.",
            "While beside Dutroux, Martin leaned on the fragile rationalization of absolute fear to shield her ego.",
            "Yet when those tiny caskets surfaced, self-delusion disintegrated; dead children are an absolute horror no defense mechanism can soften.",
            "Second is profound Moral Injury — a state of acute internal trauma inflicted by violating one's core ethical boundaries.",
            "Third is Liberation from the Coercive Field: Dutroux's arrest shattered the psychological cage, allowing dormant cognitive agency to restart.",
            "Fourth is the Ambivalent Duality between Conscience and Survival: her repentance fused genuine ethical agony with an unconscious drive to salvage a shattered ego.",
            "Her eventual retreat into the Clarisse Convent in 2012 represents the final manifestation of this quest for spiritual atonement amid universal social banishment.",
            "Such remorse cannot resurrect lost lives, yet it proves that even a suppressed conscience eventually ignites to scorch the transgressor from within."
        ],
        'ja': [
            "『なぜ悔悟したのか？』という問いを解くため、ミシェル・マルタンの変容を促した4つの連動する心理メカニズムを解剖しなければなりません。",
            "第1に、「認知的不協和の完全な崩壊」です。",
            "夫の支配下にある間、彼女は恐怖という脆い防衛にすがりつき、自我の体面を保っていました。",
            "しかし小さな棺の出現により、自己欺瞞の城壁は粉砕されました。命を奪われた子らの現実は、いかなる心理的防衛も正当化し得ない絶対的破滅だったのです。",
            "第2に、自らの非人間的加害行為によって自己の倫理的根幹を自ら破壊してしまった「道徳的負傷（モラル・インジャリー）」の激痛です。",
            "第3に、「強圧的支配の磁場からの物理的解放」です。デュトルーの逮捕によって精神的檻が打破され、麻痺していた批判的認知機能が再起動したのです。",
            "そして第4に、「良心と生存本能の葛藤に満ちた二重性」です。彼女の悔悟は、純粋な倫理的苦痛と、崩壊した自我を救済しようとする無意識の防衛が複雑に癒着したものでした。",
            "後に2012年、マルタンがクラリス修道院へと身を寄せた事実は、社会から永遠に拒絶された魂が求めた霊的浄化の最終的な発露でした。",
            "その悔悟が失われた命を買い戻すことはできませんが、抑圧された良心がいかに遅くとも、最後には加害者自身を焼き尽くす炎となって蘇ることを証明しています。"
        ]
    })

    # Block 32: HOST (6 lines)
    blocks.append({
        'act': 4,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(kết Hồi 4, mở ra làn sóng phẫn nộ và cuộc diễu hành Bạch hành)',
        'note_en': '(concluding Act 4, bridging to public fury and the historic White March)',
        'note_ja': '（第4幕を結び、民衆の怒りと歴史的白の行進へと架け橋を渡す）',
        'vn': [
            "Bi kịch Marcinelle không chỉ là câu chuyện nội tâm giữa những kẻ thủ ác và các nạn nhân dưới lòng đất.",
            "Khi sự thật về sự tắc trách của cảnh sát và những cơ hội cứu sống các em bị bỏ lỡ được phơi bày, một cơn thịnh nộ tập thể chưa từng có đã quét qua toàn vương quốc Bỉ.",
            "Đỉnh điểm của sự phẫn nộ bùng phát khi vị thẩm phán điều tra Jean-Marc Connerotte bị tước quyền thụ lý vụ án chỉ vì tham dự một bữa tối từ thiện của gia đình nạn nhân.",
            "Giọt nước đã tràn ly, đánh sập hoàn toàn niềm tin mong manh của người dân vào bộ máy tư pháp.",
            "Và từ trong sự tuyệt vọng cùng cực, lương tri của một dân tộc đã thức tỉnh để tạo nên một cuộc xuống đường lịch sử.",
            "Đó là cuộc diễu hành Bạch hành — biểu tượng của sự phản kháng bất bạo động vĩ đại nhất châu Âu thế kỷ hai mươi."
        ],
        'en': [
            "The tragedy of Marcinelle was never confined to the dark dynamic between captors and subterranean victims.",
            "As systemic police bungling and missed opportunities to save dying children emerged, an unprecedented collective fury swept Belgium.",
            "Outrage erupted into a national firestorm when popular investigating magistrate Jean-Marc Connerotte was removed from the bench over a minor procedural pretext.",
            "This final insult shattered the public's lingering trust in state judicial integrity.",
            "Out of utter despair, the collective conscience of an entire nation awakened to forge an unforgettable historic uprising.",
            "This gave birth to the White March — the most magnificent manifestation of non-violent civic solidarity in twentieth-century Europe."
        ],
        'ja': [
            "マルシネルの惨劇は、地下に蠢く捕食者と被害者たちの密室劇にとどまるものではありませんでした。",
            "警察の制度的失態と、瀕死の子どもたちを救出する機会が見逃されていた事実が露呈するにつれ、前代未聞の怒りがベルギー全土を席巻しました。",
            "人望の厚かったジャン＝マルク・コンロット予審判事が、遺族支援の夕食会に出席したという些細な口実で担当を解任されたとき、怒りは頂点に達しました。",
            "この決定は、国家の司法制度に対する国民のわずかな信頼の残滓を完全に打ち砕いたのです。",
            "極限の絶望の中から、一国の集合的良心が覚醒し、歴史に刻まれる平和的蜂起が巻き起こりました。",
            "それこそが「白の行進（ラ・マルシェ・ブランシュ）」 — 20世紀ヨーロッパにおける最も崇高な非暴力市民連帯の象徴でした。"
        ]
    })

    # ------------------ ACT 5: 4 BLOCKS (36 lines) ------------------
    # Block 33: HOST (8 lines)
    blocks.append({
        'act': 5,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(giọng trầm hùng, tái hiện cuộc diễu hành Bạch hành ngày 20/10/1996 và phiên tòa Arlon 2004)',
        'note_en': '(solemn and powerful, evoking the October 20, 1996 White March and 2004 Arlon trial)',
        'note_ja': '（荘厳かつ力強い口調で、1996年10月20日の白の行進と2004年のアルロン公判を回顧する）',
        'bgm_vn': '**[BGM]:** Tiếng Piano ấm áp trang nghiêm (Warm Piano) cất lên chậm rãi, hòa cùng nhịp vĩ cầm sâu lắng mang âm hưởng thức tỉnh và tái thiết niềm tin.',
        'bgm_en': '**[BGM]:** Warm solemn piano rising slowly, blending with deeply reflective violin evoking civic awakening and rebuilding trust.',
        'bgm_ja': '**[BGM]:** 温かく荘厳なピアノの調べが静かに立ち上がり、覚醒と信頼回復の響きを湛えた深いバイオリンと調和する。',
        'vn': [
            "Ngày 20 tháng Mười năm 1996, đường phố thủ đô Brussels chứng kiến một biển người ba trăm ngàn người cùng nhau diễu hành trong sự im lặng tuyệt đối.",
            "Chiếm hơn ba phần trăm dân số của cả nước, người dân thuộc mọi tầng lớp, sắc tộc và quan điểm chính trị đã bước đi bên nhau.",
            "Không có biểu ngữ bạo lực, không có những tiếng la hét đập phá; chỉ có những bộ trang phục màu trắng, những bông hoa trắng và những quả bóng bay trắng bay lên bầu trời.",
            "Màu trắng đại diện cho sự trong trắng của những sinh linh vô tội đã khuất và khát vọng thanh tẩy một nền tư pháp bị vấy bẩn bởi sự quan liêu.",
            "Cuộc diễu hành Bạch hành hay La Marche Blanche đã trở thành một bước ngoặt thế kỷ, buộc chính phủ Bỉ phải tiến hành một cuộc đại cải tổ toàn diện.",
            "Hệ thống cảnh sát phân mảnh bị giải thể để hợp nhất thành lực lượng Cảnh sát Liên bang duy nhất, đường dây nóng và tổ chức bảo vệ trẻ em Child Focus ra đời.",
            "Tám năm sau, vào năm 2004, phiên tòa thế kỷ tại thành phố Arlon đã tuyên mức án chung thân không ân xá cho Marc Dutroux và ba mươi năm tù cho Michelle Martin.",
            "Công lý đã được thực thi bằng pháp luật, nhưng chiến thắng thực sự thuộc về sức mạnh của sự đoàn kết và lương tri xã hội."
        ],
        'en': [
            "On October 20, 1996, the streets of Brussels bore witness to a silent ocean of over three hundred thousand citizens marching together.",
            "Representing over three percent of the nation's entire populace, people of every class, background, and belief walked shoulder to shoulder.",
            "There were no destructive banners, no violent riots; only white garments, white flowers, and white balloons floating into the autumn sky.",
            "White symbolized the radiant innocence of the lost children and an unyielding demand to cleanse a justice system tainted by bureaucratic stagnation.",
            "The White March marked an epochal turning point, compelling the Belgian state to execute the most sweeping structural reforms in its history.",
            "Fragmented police forces were abolished to form a unified Federal Police service, while nationwide hotlines and Child Focus were established.",
            "Eight years later, in 2004, the trial of the century in Arlon sentenced Marc Dutroux to life imprisonment and Michelle Martin to thirty years.",
            "Legal justice was formally rendered, yet the true victory belonged to civic solidarity and the indomitable power of collective conscience."
        ],
        'ja': [
            "1996年10月20日、首都ブリュッセルの街路は、完全な沈黙の中で行進する30万人以上の市民の白き大海を目撃しました。",
            "総人口の3パーセントを超える人々が、階層や民族、政治的立場の相違を超えて肩を並べて歩調を合わせました。",
            "破壊的なスローガンも暴力的な暴動もなく、ただ白い衣服、白い花、そして秋の空へと放たれる白い風船だけが街を埋め尽くしました。",
            "白は失われた幼き魂たちの汚れなき無垢と、官僚主義にまみれた司法制度の抜本的浄化を求める誓いを象徴していました。",
            "この「白の行進」は歴史的転換点となり、ベルギー政府にかつてない全面的な国家機構改革の断行を余儀なくさせました。",
            "分断されていた警察機構は解体・統合されて単一の連邦警察となり、全国通報網や国際的な児童保護組織チャイルド・フォーカスが設立されました。",
            "8年後の2004年、アルロンの法廷はマルク・デュトルーに終身刑を、ミシェル・マルタンに禁錮30年の実刑判決を下しました。",
            "法的正義は執行されましたが、真の勝利は市民社会の連帯と、集合的良心の不屈の力にこそ捧げられたのです。"
        ]
    })

    # Block 34: PSYCHOLOGIST (7 lines)
    blocks.append({
        'act': 5,
        'role_vn': 'CHUYÊN GIA TÂM LÝ',
        'role_en': 'PSYCHOLOGIST',
        'role_ja': '心理学者',
        'note_vn': '(phân tích Tăng trưởng sau sang chấn Post-Traumatic Growth và bài học hành vi)',
        'note_en': '(analyzing Post-Traumatic Growth and behavioral survival principles)',
        'note_ja': '（外傷後成長Post-Traumatic Growth理論と行動的生存原則を提示する）',
        'vn': [
            "Nhìn lại toàn bộ thảm kịch, chúng ta thấy rõ sức mạnh kỳ diệu của hiện tượng Tăng trưởng Sau Sang chấn hay Post-Traumatic Growth.",
            "Nạn nhân sinh tồn Sabine Dardenne đã không để bóng tối giam cầm phần đời còn lại của mình.",
            "Năm 2004, cô bước vào phòng xử án Arlon ở tuổi hai mươi, nhìn thẳng vào mắt kẻ bắt cóc và dõng dạc đòi lại phẩm giá cho bản thân và các bạn.",
            "Cuốn tự truyện của cô không phải là tiếng khóc than, mà là một bản tuyên ngôn kiên cường về quyền làm chủ số phận.",
            "Từ góc độ bảo vệ bản thân, tâm lý học hành vi đúc kết ba bài học cảnh báo đỏ sinh tồn cốt lõi:",
            "Một là luôn lắng nghe và hành động ngay theo trực giác bất an; không bao giờ thương lượng với những kẻ có dấu hiệu kiểm soát hay đe dọa.",
            "Hai là xây dựng mạng lưới an toàn cộng đồng; sự quan sát nhạy bén của một người láng giềng hay một nhân chứng có thể thay đổi vận mệnh của nhiều sinh mạng."
        ],
        'en': [
            "Reflecting upon this tragedy, we observe the profound reality of Post-Traumatic Growth as articulated by clinical science.",
            "Surviving victim Sabine Dardenne refused to permit that cellar's shadows to dictate the remainder of her life.",
            "In 2004, entering the Arlon courtroom at age twenty, she stared directly into her abductor's eyes, reclaiming dignity for herself and her peers.",
            "Her subsequent memoir was no lamentation of victimhood, but an uncompromising manifesto of personal agency and resilience.",
            "From a behavioral defense perspective, forensic psychology crystalizes three foundational red-flag survival principles:",
            "First, instantly trust and act upon defensive intuition; never negotiate or normalize covert coercive and controlling behaviors.",
            "Second, cultivate proactive community vigilance; the sharp observation of a single observant neighbor can alter human destinies forever."
        ],
        'ja': [
            "惨劇の全貌を振り返る時、私たちは臨床心理学が説く「外傷後成長（ポスト・トラウマティック・グロース）」の崇高な現実を目撃します。",
            "生還したサビーヌ・ダルデンヌは、あの地下室の暗黒の影に自らの残りの人生を支配されることを断固として拒絶しました。",
            "2004年、20歳でアルロンの法廷に立った彼女は、捕食者の瞳を正面から見据え、自らと亡き友たちの尊厳を堂々と奪還しました。",
            "彼女の自叙伝は受動的な被害者の嘆きではなく、自らの運命の主権を取り戻した人間の不屈の宣言書となったのです。",
            "自己防衛の観点から、行動心理学は3つの決定的なレッドフラッグ生存原則を導き出します。",
            "第1に、防衛的直感を無条件に信じ、即座に行動すること。潜在的な強圧や支配の兆候を決して見逃したり交渉したりしてはなりません。",
            "第2に、コミュニティの能動的警戒網を構築すること。一人の隣人の鋭敏な観察眼が、無数の生命の行方を永遠に変える力を持つのです。"
        ]
    })

    # Block 35: INVESTIGATOR (6 lines)
    blocks.append({
        'act': 5,
        'role_vn': 'ĐIỀU TRA VIÊN',
        'role_en': 'INVESTIGATOR',
        'role_ja': '捜査官',
        'note_vn': '(tổng kết bài học nghiệp vụ, lời cam kết của lực lượng thực thi pháp luật)',
        'note_en': '(operational summary, solemn commitment of professional law enforcement)',
        'note_ja': '（捜査実務の総括と、法執行機関が胸に刻むべき厳粛な教訓を述べる）',
        'vn': [
            "Đối với lực lượng điều tra và thực thi pháp luật, hồ sơ Marc Dutroux mãi là một bài học xương máu không bao giờ được phép lãng quên.",
            "Không có sự tắc trách nào là vô hại; mỗi sự cạnh tranh nghiệp vụ vô nghĩa hay một báo cáo bị bỏ qua đều có thể phải trả giá bằng mạng sống con người.",
            "Hệ thống tư pháp chỉ thực sự xứng đáng với niềm tin của nhân dân khi biết đặt tính mạng của những người yếu thế lên trên hết.",
            "Sự ra đời của lực lượng cảnh sát cải tổ và các quy trình phối hợp khẩn cấp ngày nay là sự chuộc lỗi muộn màng nhưng kiên quyết.",
            "Chúng tôi cam kết sẽ không bao giờ để những tiếng kêu cứu trong bóng tối bị chìm vào sự thờ ơ của bộ máy công quyền thêm một lần nào nữa.",
            "Ánh sáng của công lý phải luôn là ngọn hải đăng bảo vệ cho từng ngôi nhà và từng đứa trẻ."
        ],
        'en': [
            "For investigative and forensic professionals, the Marc Dutroux dossier remains a permanent testament written in blood.",
            "No institutional negligence is harmless; every petty bureaucratic rivalry or ignored field report can cost human lives.",
            "A justice system commands public legitimacy only when it fiercely prioritizes the survival of the vulnerable above all else.",
            "The birth of unified policing and modern emergency response protocols stands as an enduring, resolute restitution.",
            "We vow that faint cries from subterranean shadows will never again be swallowed by bureaucratic indifference.",
            "The light of justice must stand as an uncompromising beacon safeguarding every household and every child."
        ],
        'ja': [
            "捜査および法執行の実務に携わる者にとって、マルク・デュトルー事件は血をもって刻まれた永遠の教訓であり続けます。",
            "いかなる制度的怠慢も無害ではあり得ません。不毛な縄張り争いや無視された現場の報告書が、人間の生命という代償を要求するのです。",
            "司法制度は、最も脆弱な立場にある人々の生存を至高の価値として守り抜いて初めて、国民の信頼に値するものとなります。",
            "統合された近代警察の誕生と迅速な緊急初動プロトコルは、遅すぎたとはいえ、決して後退してはならない誓いの結晶です。",
            "私たちは、暗闇から漏れ聞こえる微かな救求めの叫びが、二度と官僚主義の冷淡さに呑み込まれぬよう誓わねばなりません。",
            "正義の光は、すべての家庭とすべての子どもたちを守護する、妥協なき灯台であり続けなければならないのです。"
        ]
    })

    # Block 36: HOST (15 lines)
    blocks.append({
        'act': 5,
        'role_vn': 'HOST',
        'role_en': 'HOST',
        'role_ja': 'ホスト',
        'note_vn': '(giọng trầm ấm, xúc động sâu sắc, đúc kết thông điệp nhân văn và chào kết thúc tập)',
        'note_en': '(warm, deeply emotional, summarizing the humanist message and bidding farewell)',
        'note_ja': '（深みのある温かな口調で心揺さぶる人道的メッセージを総括し、番組を締めくくる）',
        'vn': [
            "Hành trình giải mã hồ sơ Marc Dutroux khép lại, để lại trong lòng mỗi chúng ta những khoảng lặng sâu sắc về bản chất con người.",
            "Chúng ta đã nhìn thấy những góc tối tăm ghê rợn nhất của sự tha hóa ái kỷ và sự đồng lõa hèn nhát.",
            "Nhưng vượt lên trên tất cả nỗi đau, chúng ta cũng đã chứng kiến ý chí sinh tồn kiên cường không thể bị dập tắt của những nạn nhân dũng cảm.",
            "Chúng ta đã thấy sự thức tỉnh vĩ đại của lương tri xã hội khi hàng trăm ngàn con người cùng nắm tay nhau trong sắc trắng tinh khôi.",
            "Cái ác có thể ngụy trang dưới những vỏ bọc bình thường nhất, có thể đào những căn hầm sâu nhất để che giấu tội lỗi.",
            "Thế nhưng, chừng nào con người còn biết lắng nghe sự thật, chừng nào cộng đồng còn biết đoàn kết và bảo vệ lẫn nhau;",
            "Bóng tối sẽ không bao giờ có thể chiến thắng được ánh sáng của công lý.",
            "Mong rằng những bài học từ thảm kịch Marcinelle sẽ là hồi chuông cảnh tỉnh vĩnh cửu cho sự an toàn của con em chúng ta.",
            "Hãy luôn quan sát, luôn chở che và không bao giờ im lặng trước những bất công quanh mình.",
            "Cảm ơn quý vị khán giả đã luôn đồng hành cùng Amber Eyes trong những hành trình khám phá chiều sâu tâm lý học tội phạm.",
            "Sự theo dõi và chia sẻ của quý vị chính là nguồn động lực to lớn để chúng tôi tiếp tục lan tỏa những giá trị tỉnh thức nhân văn.",
            "Xin hãy nhấn nút đăng ký và bật chuông thông báo để không bỏ lỡ những hồ sơ chuyên sâu tiếp theo.",
            "Chúc quý vị và gia đình luôn an yên và giữ vững sự tỉnh giác trước mọi biến chuyển của cuộc sống.",
            "Xin chào tạm biệt và hẹn gặp lại quý vị trong những tập hồ sơ tiếp theo.",
            "Amber Eyes — Soi sáng sự thật từ những góc tối tâm lý con người."
        ],
        'en': [
            "Our journey through the Marc Dutroux dossier concludes, leaving profound reflections within each of us regarding the human condition.",
            "We have gazed into the absolute darkest abysses of narcissistic depravity and cowardly complicity.",
            "Yet rising far above the agony, we have witnessed the indomitable resilience of courageous survivors.",
            "We have seen the awakening of societal conscience as hundreds of thousands walked united in radiant white.",
            "Evil may cloak itself behind ordinary facades, digging the deepest subterranean vaults to hide its transgressions.",
            "Yet so long as humanity champions truth, so long as communities unite to shield one another fiercely;",
            "Shadows will never extinguish the resilient dawn of justice.",
            "May the enduring lessons of Marcinelle stand as an eternal guardian for the safety of our children.",
            "Stay vigilant, cherish those around you, and never retreat into silence before injustice.",
            "Thank you for accompanying Amber Eyes through this forensic journey into the depths of criminal psychology.",
            "Your engagement and shared reflections empower us to continually illuminate profound human truths.",
            "Please subscribe and ring the bell to stay connected with our forthcoming investigative dossiers.",
            "Wishing you and your loved ones peace, safety, and unwavering awareness in everyday life.",
            "Until our next journey into the archives of justice, farewell.",
            "Amber Eyes — Illuminating truth from the deepest corridors of the human mind."
        ],
        'ja': [
            "マルク・デュトルー事件の心理学的解剖の旅を終えるにあたり、私たちの胸には人間の本質をめぐる深い思索が去来します。",
            "私たちは自己愛的な堕落と臆病な共犯関係が作り出した、人間の最も暗い深淵を見つめました。",
            "しかし激しい痛哭の彼方に、勇敢な生存者たちが示した決して屈することのない不屈のレジリエンスを目撃しました。",
            "純白の光の中で手を取り合った数十万の市民が見せた、社会の良心の崇高な覚醒を目撃したのです。",
            "悪は最も平凡な日常の仮面を被り、自らの罪を隠蔽するために最も深い地下室を穿つかもしれません。",
            "しかし、人間が真実を直視し続け、コミュニティが互いを守るために連帯し続ける限りにおいて、光は決して消え去りません。",
            "いかなる暗黒も、正義の黎明の光を永久に呑み込むことはできないのです。",
            "マルシネルの惨劇が遺した教訓が、私たちの子どもたちの安全を守護する永遠の警鐘となることを切に願います。",
            "常に周囲に目を配り、愛する者を慈しみ、不正の前に沈黙してはなりません。",
            "犯罪心理学の深奥を探求するアンバー・アイズの旅に最後までお付き合いいただき、心より感謝申し上げます。",
            "皆様の温かいご支援と共有こそが、私たちが深遠な人間的真実を照らし続けるための最大の原動力です。",
            "チャンネル登録と通知ベルの設定をぜひよろしくお願いいたします。",
            "皆様とご家族の平穏と安全、そして日常における確かな覚醒を心より祈念いたします。",
            "次なる正義の記録の旅でお会いできるその日まで、さようなら。",
            "アンバー・アイズ — 人間の深層心理の暗闇から、真実の光を照らし出す。"
        ]
    })

    return blocks

def format_script(blocks, lang):
    output = []
    
    # Headers
    if lang == 'VN':
        output.append("# KỊCH BẢN CHI TIẾT TẬP 42: HỒ SƠ MARC DUTROUX — NGÔI NHÀ NỖI SỢ MARCINELLE & SỰ PHẢN KHÁNG CỦA LƯƠNG TRI XÃ HỘI")
        output.append("")
        output.append("* **Đề tài:** Vụ án chấn động nước Bỉ dẫn tới cuộc diễu hành Bạch hành của 300.000 người dân.")
        output.append("* **Chủ đề tâm lý:** Mối quan hệ kiểm soát độc hại vợ chồng, Cơ chế hối hận của đồng phạm, Sự thức tỉnh của lương tri xã hội trước lỗ hổng tư pháp.")
        output.append("* **Thời lượng dự kiến:** 28 – 32 phút")
        output.append("* **Định dạng:** Chuẩn A2c/K10 — Cấu trúc 5 Hồi chuẩn mực theo Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c) và Luật K10")
        output.append("* **Tiêu chuẩn An toàn YouTube (Rule V9):** 100% YouTube Safe, không mô tả trực diện thương tổn thể xác hay chi tiết rùng rợn; tập trung 100% vào phân tích tâm lý học tội phạm, vi biểu cảm, chiến thuật hỏi cung và bài học phòng ngừa tội phạm.")
        output.append("")
        output.append("---")
        output.append("")
        output.append("## BẢNG PHÂN VAI VÀ CẤU TRÚC GIỌNG ĐỌC")
        output.append("")
        output.append("| Ký hiệu | Vai trò | Tên nhân vật thể hiện | Đặc điểm giọng đọc |")
        output.append("| :--- | :--- | :--- | :--- |")
        output.append("| **H** | **Dẫn chuyện (Host)** | Cú (Host Amber Eyes) | Trầm ấm, lôi cuốn, sắc sảo, dẫn dắt thấu đáo (~48% thời lượng) |")
        output.append("| **D** | **Điều tra viên** | Sói (Điều tra viên) | Nam trung niên, dày dạn kinh nghiệm, điềm tĩnh, đanh thép (~24% thời lượng) |")
        output.append("| **C** | **Chuyên gia Tâm lý** | Cáo (Chuyên gia tâm lý) | Nữ sắc sảo, điềm đạm, khách quan, giàu hàm lượng khoa học hành vi (~22% thời lượng) |")
        output.append("| **N** | **Người trong cuộc** | Nhân chứng / Nạn nhân / Người đồng lõa | Chân thực, hồi hộp, phản ánh góc nhìn đời thực (~6% thời lượng) |")
        output.append("")
        output.append("---")
    elif lang == 'EN':
        output.append("# CRIMINAL PSYCHOLOGY AUDIO / PODCAST SCRIPT: EPISODE 42")
        output.append("**Theme:** The 10 Psychological Indicators & Coercive Control, The Mechanics of Remorse & The White March – The Marc Dutroux Case and The Marcinelle House of Horror.")
        output.append("**Edition:** Standard A2c/K10 — Criminal Psychological Ecology & Safety Rule V9 (November 2026).")
        output.append("")
        output.append("---")
        output.append("")
        output.append("## PRODUCTION BRIEF & NARRATIVE STRUCTURE")
        output.append("")
        output.append("| Category | Standard Setup for Audio Episode (Host-Driven Documentary) |")
        output.append("| :--- | :--- |")
        output.append("| **Episode Title** | Episode 42: The Marcinelle House of Horror — Coercive Control, The Mechanics of Remorse & The White March (The Marc Dutroux Case) |")
        output.append("| **Format** | Investigative Documentary Podcast (Narrator-led Documentary) – The **Host** maintains the narrative backbone, connecting historical data, regulating emotional pacing, and bringing in specialized perspectives (Investigator, Psychologist, Ordinary Person) at precise dramatic beats according to the 10 Psychological Indicators. |")
        output.append("| **Estimated Total Duration** | 28 – 32 minutes (5 narrative acts + dramatic audio transitions) |")
        output.append("| **Suggested Background Music (BGM)** | Suffocating Dark Ambient, Somber Solo Cello, Minimalist Piano blended with chilling Electronic Drone, Harrowing Courtroom Violin, and Warm Piano for solemn reflection. Volume: -26dB under narration, rising to -14dB at scene transitions. |")
        output.append("| **Voice Allocation Mechanism** | - **Host (~48% duration):** Warm, deep, reflective male voice, guiding the narrative with a humanistic lens, social aftermath, halo effect, and survival lessons.<br>- **Investigator (~24%):** Steely, precise, authoritative male voice representing investigative records, physical evidence, Modus Operandi vs Signature.<br>- **Criminal Psychologist (~22%):** Insightful, composed, academic female voice dissecting Coercive Control, Moral Disengagement, Lucid Resistance, and Remorse mechanics.<br>- **Ordinary Person (~6%):** N1 (Town Resident - Act 1) shocked voice; N2 (Michelle Martin - Act 4) trembling voice choked with guilt. |")
        output.append("")
        output.append("---")
    elif lang == 'JA':
        output.append("# 犯罪心理学オーディオ／ポッドキャスト台本：第42話")
        output.append("**テーマ：** 10大心理指標生態系＆強圧的支配（Coercive Control）、共犯者の悔悟メカニズムと白の行進 — マルク・デュトルー事件とマルシネル恐怖の館。")
        output.append("**バージョン：** 標準A2c/K10 — 犯罪心理生態系＆安全基準V9（2026年11月）。")
        output.append("")
        output.append("---")
        output.append("")
        output.append("## 制作仕様とナレーション構成（PRODUCTION BRIEF）")
        output.append("")
        output.append("| 項目 | 音声エピソード標準設定（Host-Driven Documentary） |")
        output.append("| :--- | :--- |")
        output.append("| **エピソード名** | 第42話：マルシネル恐怖の館 — 強圧的支配、共犯者の悔悟メカニズムと白の行進（マルク・デュトルー事件） |")
        output.append("| **フォーマット** | 調査ドキュメンタリー・ポッドキャスト（Narrator-led Documentary） – **ホスト**が物語の根幹を担い、歴史的資料を繋ぎ、感情の起伏を調和させ、10大心理指標に基づいて専門的視点（捜査官、心理学者、一般人）を的確な劇的転換点へと招き入れます。 |")
        output.append("| **予定総時間** | 28 – 32分（5幕構成＋緊迫した音響の間） |")
        output.append("| **推奨BGM** | 息苦しいダーク・アンビエント、陰鬱なチェロ・ソロ、戦慄する電子ドローンを融合させたミニマル・ピアノ、緊迫した法廷のバイオリン、そして厳粛な回顧を告げる温かなピアノ。音量：ナレーション下 -26dB、場面転換点 -14dB。 |")
        output.append("| **キャスト構成** | - **ホスト（全体の約48%）：** 深みと温かみのある男性の声。人道的な視点、社会的余波、ハロー効果、生存への教訓を通じて物語を導きます。<br>- **捜査官（約24%）：** 冷徹で鋭敏、正確無比な男性の声。実地捜査記録、物的証拠、シグネチャー対MOを代弁します。<br>- **心理学者（約22%）：** 穏やかで深い学術性を備えた女性の声。強圧的支配、道徳的脱関与、明晰な抵抗、悔悟のメカニズムを解剖します。<br>- **一般人（約6%）：** N1（マルシネルの住民 - 第1幕）衝撃に震える声；N2（ミシェル・マルタン - 第4幕）罪悪感に苛まれ震える声。 |")
        output.append("")
        output.append("---")

    cur_act = 0
    act_titles_vn = [
        "",
        "## HỒI 1: KHỞI NGUỒN CƠN ÁC MỘNG & TIẾNG CHUÔNG BÁO ĐỘNG",
        "## HỒI 2: VỎ BỌC NGUỴ TRANG & DẤU VẾT HÀNH VI NGẦM",
        "## HỒI 3: CUỘC ĐẤU TRÍ TRONG PHÒNG THẨM VẤN & BẢN NGÃ VỠ VỤN",
        "## HỒI 4: KHOA HỌC HÌNH SỰ LẬT MỞ BÍ ẨN & ÁNH SÁNG CÔNG LÝ",
        "## HỒI 5: BẢN ÁN CUỐI CÙNG & BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN"
    ]
    act_titles_en = [
        "",
        "## ACT 1: THE GENESIS OF THE NIGHTMARE & THE ALARM BELLS",
        "## ACT 2: CAMOUFLAGE & SUBTERRANEAN BEHAVIORAL PATTERNS",
        "## ACT 3: COGNITIVE CHESS IN CONFINEMENT & CRACKED EGOS",
        "## ACT 4: FORENSIC TRUTH UNVEILED & THE LIGHT OF JUSTICE",
        "## ACT 5: THE FINAL VERDICT & RED-FLAG SURVIVAL LESSONS"
    ]
    act_titles_ja = [
        "",
        "## 第1幕：悪夢の胎動と警鐘の響き",
        "## 第2幕：偽装の仮面と地下の行動痕跡",
        "## 第3幕：閉ざされた空間での認知的チェスと自我の亀裂",
        "## 第4幕：法科学が暴く深淵と正義の光",
        "## 第5幕：最終判決と生命のレッドフラッグ教訓"
    ]

    for b in blocks:
        if b['act'] != cur_act:
            cur_act = b['act']
            output.append("")
            output.append("---")
            output.append("")
            if lang == 'VN':
                output.append(act_titles_vn[cur_act])
            elif lang == 'EN':
                output.append(act_titles_en[cur_act])
            elif lang == 'JA':
                output.append(act_titles_ja[cur_act])
            output.append("")

        # BGM if present
        if 'bgm_vn' in b:
            if lang == 'VN':
                output.append(b['bgm_vn'])
            elif lang == 'EN':
                output.append(b['bgm_en'])
            elif lang == 'JA':
                output.append(b['bgm_ja'])
            output.append("")

        # SFX if present
        if 'sfx_vn' in b:
            if lang == 'VN':
                output.append(b['sfx_vn'])
            elif lang == 'EN':
                output.append(b['sfx_en'])
            elif lang == 'JA':
                output.append(b['sfx_ja'])
            output.append("")

        # Character block
        if lang == 'VN':
            role = b['role_vn']
            note = b['note_vn']
            lines = b['vn']
        elif lang == 'EN':
            role = b['role_en']
            note = b['note_en']
            lines = b['en']
        elif lang == 'JA':
            role = b['role_ja']
            note = b['note_ja']
            lines = b['ja']

        output.append(f"**{role}** *{note}*:")
        for line in lines:
            output.append(line)
        output.append("")

    return "\n".join(output)

if __name__ == '__main__':
    blocks = get_script_data()
    print(f"Total blocks generated: {len(blocks)}")
    total_vn = sum(len(b['vn']) for b in blocks)
    total_en = sum(len(b['en']) for b in blocks)
    total_ja = sum(len(b['ja']) for b in blocks)
    print(f"Total lines: VN={total_vn}, EN={total_en}, JA={total_ja}")

    vn_text = format_script(blocks, 'VN')
    en_text = format_script(blocks, 'EN')
    ja_text = format_script(blocks, 'JA')

    with open('01_KICH_BAN/Tap42/kichban_tap42_19112026.md', 'w', encoding='utf-8') as f:
        f.write(vn_text)
    print("Wrote Vietnamese script to 01_KICH_BAN/Tap42/kichban_tap42_19112026.md")

    with open('01_KICH_BAN/Tap42_EN/kichban_tap42_EN.md', 'w', encoding='utf-8') as f:
        f.write(en_text)
    print("Wrote English script to 01_KICH_BAN/Tap42_EN/kichban_tap42_EN.md")

    with open('01_KICH_BAN/Tap42_JA/kichban_tap42_JA.md', 'w', encoding='utf-8') as f:
        f.write(ja_text)
    print("Wrote Japanese script to 01_KICH_BAN/Tap42_JA/kichban_tap42_JA.md")
