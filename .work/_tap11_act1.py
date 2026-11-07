# -*- coding: utf-8 -*-
"""Dữ liệu Hồi 1 Kịch bản Tập 11 (4 ngôn ngữ: VN, EN, JA, KO)."""

ACT1_ELEMENTS = [
    {
        "id": "1.01",
        "kind": "BGM",
        "desc_vn": "Tiếng đàn Cello u buồn cất lên chậm rãi giữa không gian tĩnh lặng, hòa cùng tiếng gió rít hiu hắt bên bờ hồ Ontario.",
        "desc_en": "A somber cello melody rises slowly in the silence, blending with the howling winter wind across Lake Ontario.",
        "desc_ja": "静寂の中に哀愁を帯びたチェロの旋律がゆっくりと響き、オンタリオ湖畔の冷たい風の音と重なり合う。",
        "desc_ko": "적막한 어둠 속에서 구슬픈 첼로 선율이 낮게 울려 퍼지고, 온타리오 호수를 스치는 쓸쓸한 바람 소리와 뒤섞인다."
    },
    {
        "id": "1.02",
        "kind": "SFX",
        "desc_vn": "Tiếng ly rượu chạm nhau lách cách, tiếng nhạc khiêu vũ rộn rã trong một đám cưới ngoài trời.",
        "desc_en": "Glasses clinking cheerfully, upbeat wedding dance music echoing at an outdoor reception.",
        "desc_ja": "乾杯のグラスが触れ合う軽快な音、野外の結婚祝宴で陽気に流れるダンス音楽の響き。",
        "desc_ko": "유리잔이 쨍하고 부딪히는 경쾌한 소리, 야외 결혼식장에서 울려 퍼지는 흥겨운 음악 소리."
    },
    {
        "id": "1.03",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "chậm rãi, giọng trầm ấm gợi mở không gian hoài niệm",
        "direction_en": "slow, deep, evoking a nostalgic yet uneasy atmosphere",
        "direction_ja": "ゆっくりと低く、郷愁と不穏さを呼び起こすトーン",
        "direction_ko": "느리고 깊은 어조로, 아련하면서도 불길한 분위기를 풍기며",
        "sents_vn": [
            "Vào đầu thập niên 1990, tại thị trấn ven hồ thơ mộng Port Dalhousie thuộc tỉnh Ontario, có một ngôi nhà màu hồng nổi bật tọa lạc tại số 57 Đại lộ Bayview Drive.",
            "Đó là tổ ấm của một cặp vợ chồng trẻ khiến bất kỳ ai đi qua cũng phải ngoái nhìn với ánh mắt ngưỡng mộ.",
            "Người chồng là Paul Bernardo, một thanh niên bảnh bao làm việc trong ngành tài chính kế toán, luôn xuất hiện trong những bộ vest hàng hiệu và lái chiếc xe thể thao mui trần cá tính.",
            "Người vợ là Karla Homolka, kém hắn sáu tuổi, cô gái tóc vàng xinh đẹp với nụ cười rạng rỡ như thiên thần, đang làm việc tại một phòng khám thú y địa phương.",
            "Trong mắt cộng đồng dân cư xung quanh, họ chính là hiện thân hoàn mỹ của cặp búp bê 'Ken và Barbie' bước ra đời thực.",
            "Họ tổ chức một đám cưới lộng lẫy như truyện cổ tích vào tháng 6 năm 1991 bằng cỗ xe ngựa kéo tại thị trấn cổ kính Niagara-on-the-Lake."
        ],
        "sents_en": [
            "In the early 1990s, in the picturesque lakeside community of Port Dalhousie in Ontario, an eye-catching pink house stood at 57 Bayview Drive.",
            "It was the cherished home of a glamorous young couple that drew admiring glances from everyone passing by.",
            "The husband was Paul Bernardo, a handsome young professional in financial accounting who always wore designer suits and drove a sleek convertible sports car.",
            "The wife was Karla Homolka, six years his junior, a striking blonde with an angelic smile who worked at a local veterinary clinic.",
            "To their suburban neighbors, they appeared to be the living embodiment of 'Ken and Barbie' dolls come to life.",
            "In June 1991, they celebrated a fairytale wedding in a romantic horse-drawn carriage in historic Niagara-on-the-Lake."
        ],
        "sents_ja": [
            "1990年代初頭、オンタリオ州の風光明媚な湖畔の町ポート・ダルハウジーのBayview Drive 57番地に、ひときわ目を引くピンク色の家が佇んでいました。",
            "そこは、通りかかる誰もが羨望の眼差しで見つめる若い新婚夫婦の温かな家庭でした。",
            "夫のPaul Bernardoは、高級スーツを着こなし洗練されたスポーツカーを乗り回す、会計業界勤務のハンサムな青年でした。",
            "6歳年下の妻Karla Homolkaは、地元の動物病院に勤務する、天使のような輝く笑顔を持つ美しい金髪の女性でした。",
            "近隣住民の目には、二人は現実世界に現れた完璧な『ケンとバービー』人形そのものに映っていました。",
            "1991年6月、歴史あるナイアガラ・オン・ザ・レイクの町で、二人は馬車に揺られながらまるでおとぎ話のような華やかな結婚式を挙げました。"
        ],
        "sents_ko": [
            "1990년대 초반, Ontario 주 그림 같은 호숫가 마을 Port Dalhousie의 Bayview Drive 57번지에는 눈에 띄는 분홍빛 주택 한 채가 자리 잡고 있었습니다.",
            "그곳은 지나가는 사람 누구나 부러움의 눈길로 쳐다보게 만들던 매력적인 신혼부부의 따스한 보금자리였습니다.",
            "남편인 Paul Bernardo는 고급 정장을 차려입고 날렵한 컨버터블 스포츠카를 몰던, 금융 회계 분야의 말끔한 청년이었습니다.",
            "여섯 살 연하의 아내 Karla Homolka는 지역 동물병원에서 근무하던, 천사처럼 눈부신 미소를 지닌 금발의 미인이었습니다.",
            "이웃 주민들의 눈에 두 사람은 동화 속에서 방금 걸어 나온 듯한 ‘켄과 바비’ 인형의 완벽한 실사판처럼 보였습니다.",
            "1991년 6월, 유서 깊은 Niagara-on-the-Lake 마을에서 두 사람은 마차를 타고 마치 동화 같은 화려한 결혼식을 올렸습니다."
        ]
    },
    {
        "id": "1.04",
        "kind": "NGHI",
        "sec": 1.5,
        "desc_vn": "khoảng lặng kịch tính"
    },
    {
        "id": "1.05",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "chuyển giọng u tối, báo hiệu tai ương",
        "direction_en": "shifting to a darker tone, foreshadowing tragedy",
        "direction_ja": "暗いトーンへと移行し、不吉な影を予告する",
        "direction_ko": "어둡고 불길한 어조로 전환하며 비극을 예고하듯",
        "sents_vn": [
            "Đôi vợ chồng trẻ xuất hiện như những thần tượng của giới trung lưu, luôn quấn quýt bên nhau trong mọi sự kiện xã hội.",
            "Karla say đắm Paul đến mức tôn sùng hắn như một vị hoàng tử hoàn mỹ, sẵn sàng phục tùng mọi yêu sách kỳ quặc để duy trì ảo ảnh hạnh phúc.",
            "Chính vị thế xã hội và vỏ bọc kiểu mẫu ấy đã tạo nên một 'Hiệu ứng Hào quang' chết người — một tấm khiên tàng hình ru ngủ hoàn toàn trực giác cảnh giác của cộng đồng suốt nhiều năm ròng.",
            "Người ta chỉ thấy một cặp trai tài gái sắc yêu thương động vật và chăm chút tổ ấm, mà không hề mảy may nghi ngờ bóng tối bên trong.",
            "Để hiểu chiếc mặt nạ ấy hoàn hảo đến mức nào, hãy hình dung cảm nhận của những người từng sống bên cạnh ngôi nhà màu hồng."
        ],
        "sents_en": [
            "The young couple presented themselves as idols of middle-class success, inseparable at every community gathering.",
            "Karla was so utterly captivated by Paul that she worshipped him as a flawless prince, willingly yielding to his bizarre demands to sustain their fairytale illusion.",
            "That very status and immaculate facade created a fatal 'Halo Effect' — an invisible psychological shield that completely lulled the community's instincts for years.",
            "Neighbors saw only a radiant pair who loved animals and cared for their home, never suspecting the sinister abyss lurking behind closed doors.",
            "To understand just how impenetrable that mask truly was, imagine the perspective of those living right next to that pink house."
        ],
        "sents_ja": [
            "若い夫婦は中産階級の成功の象徴として周囲から見なされ、あらゆる社交の場で常に寄り添い合っていました。",
            "KarlaはPaulに夢中になり、彼を完璧な王子として崇拝し、幸福の幻想を維持するためならどのような理不尽な要求にも従う姿勢を見せていました。",
            "まさにその社会的地位と非の打ちどころのない外見こそが、致命的な『ハロー効果』――長年にわたり地域社会の警戒心を麻痺させた不可視の盾――を生み出していたのです。",
            "周囲の人々は動物を愛し家庭を慈しむ美しい男女の姿だけを目にし、その背後に潜む暗黒の深淵を疑う余地など微塵もありませんでした。",
            "その仮面がいかに完璧であったかを理解するために、あのピンクの家の隣で暮らしていた人々の視点を思い浮かべてみてください。"
        ],
        "sents_ko": [
            "이 젊은 부부는 중산층 성공의 이상적인 표상으로 비치며, 모든 사교 모임마다 한시도 떨어지지 않고 함께했습니다.",
            "Karla는 Paul에게 깊이 매료되어 그를 완벽한 왕자처럼 숭배했고, 행복의 환상을 지키기 위해 기이한 요구에도 기꺼이 순종했습니다.",
            "바로 그 사회적 위상과 흠잡을 데 없는 외양이 치명적인 ‘후광 효과’를 형성하여, 수년 동안 지역 사회의 본능적 경계심을 완전히 잠재웠습니다.",
            "주민들은 동물을 사랑하고 가정을 정성껏 가꾸는 선남선녀의 모습만을 보았을 뿐, 그 이면에 웅크린 어둠의 심연은 결코 눈치채지 못했습니다.",
            "그 가면이 얼마나 완벽했는지를 체감하기 위해, 당시 분홍빛 주택 바로 옆에 살았던 이웃 주민의 심정을 상상해 보십시오."
        ]
    },
    {
        "id": "1.06",
        "kind": "LOI",
        "role": "NGƯỜI BÌNH THƯỜNG",
        "direction_vn": "N1: Người hàng xóm tại Port Dalhousie, giọng nữ trẻ bàng hoàng, nghẹn ngào",
        "direction_en": "N1: Port Dalhousie neighbor, young female, shocked and emotional",
        "direction_ja": "N1：ポート・ダルハウジーの近隣住民、若い女性、動揺と震える声",
        "direction_ko": "N1: Port Dalhousie 이웃 주민, 젊은 여성, 충격과 떨리는 목소리",
        "sents_vn": [
            "Trong mắt tất cả chúng tôi tại khu phố ven hồ, Paul và Karla từng là một cặp đôi vàng mẫu mực.",
            "Họ luôn mỉm cười chào hỏi mọi người, chăm chút cho khu vườn nhỏ và dắt chó đi dạo mỗi buổi chiều tà.",
            "Nếu vào thời điểm ấy có ai nói rằng phía sau những khung cửa sổ sơn hồng là một địa ngục kinh hoàng nhất Bắc Mỹ, chắc chắn không một ai tin.",
            "Chiếc mặt nạ thánh thiện của họ đã khiến cả một khu phố hoàn toàn mù quáng."
        ],
        "sents_en": [
            "To all of us in that quiet lakeside neighborhood, Paul and Karla seemed like the textbook definition of a golden couple.",
            "They were always smiling, greeting everyone warmly, tending their garden, and walking their dog every evening.",
            "If anyone had told us back then that behind those pink window frames lay one of the darkest horrors in North American history, no one would have believed it.",
            "Their angelic mask completely blinded our entire neighborhood."
        ],
        "sents_ja": [
            "静かな湖畔の町に住む私たち全員の目には、PaulとKarlaはまさに理想的な模範のカップルそのものでした。",
            "二人はいつも笑顔で近所の人々に挨拶し、小さな庭を手入れし、夕暮れ時には愛犬を連れて散歩を楽しんでいました。",
            "もしあの当時、ピンク色の窓枠の向こう側で北米史上最もおぞましい悪夢が繰り広げられていたと言われたとしても、誰も信じなかったはずです。",
            "彼らのあまりにも純真無垢な仮面が、町全体の人々の目を完全に曇らせていたのです。"
        ],
        "sents_ko": [
            "한적한 호숫가 동네에 살던 저희 모두의 눈에 Paul과 Karla는 그야말로 교과서적인 모범 커플이었습니다.",
            "두 사람은 언제나 밝은 미소로 인사를 건넸고, 정원을 정성스레 가꾸었으며, 해질녘이면 반려견을 데리고 다정하게 산책을 했습니다.",
            "만약 그 당시 누군가가 저 분홍빛 창문 뒤에서 북미 역사상 가장 끔찍한 악몽이 벌어지고 있다고 말했다면, 아무도 믿지 않았을 것입니다.",
            "그들의 천사 같은 가면은 온 동네 사람들의 눈을 완전히 멀게 만들었습니다."
        ]
    },
    {
        "id": "1.07",
        "kind": "SFX",
        "desc_vn": "Tiếng còi xe cảnh sát rít xé màn đêm, tiếng lật giở hồ sơ điều tra dồn dập.",
        "desc_en": "Distant police sirens piercing the dark night, rapid rustling of case files being flipped.",
        "desc_ja": "夜の帳を切り裂く遠いパトカーのサイレン音、緊迫感漂う捜査記録をめくる激しい音。",
        "desc_ko": "밤의 정적을 찢는 사이렌 소리, 다급하게 넘겨지는 수사 기록 서류철 소리."
    },
    {
        "id": "1.08",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "trầm giọng, nhấn mạnh sự tương phản rùng mình",
        "direction_en": "deep tone, highlighting the chilling contrast",
        "direction_ja": "低く抑えた声で、戦慄すべきコントラストを際立たせる",
        "direction_ko": "낮게 가라앉은 목소리로, 오싹한 대비를 강조하며",
        "sents_vn": [
            "Thế nhưng, đằng sau cánh cửa đóng kín của căn nhà số 57 Bayview Drive là một thực tại tăm tối vượt xa mọi giới hạn tưởng tượng của con người.",
            "Cùng thời điểm cặp đôi Ken và Barbie đang tận hưởng cuộc sống nhung lụa, một bóng ma kinh hoàng đang bao trùm khắp miền Nam tỉnh Ontario.",
            "Từ năm 1987 đến năm 1990, khu vực ngoại ô Scarborough của thành phố Toronto bị rung chuyển bởi một kẻ gây án hàng loạt mang biệt danh 'Scarborough Rapist'.",
            "Hắn rình rập phụ nữ trẻ đi một mình trong đêm tối, tấn công chớp nhoáng rồi biến mất không để lại dấu vết.",
            "Cơn hoang tưởng xã hội và chấn thương tập thể bao trùm khắp các trạm xe buýt và khu dân cư khi màn đêm buông xuống."
        ],
        "sents_en": [
            "Yet, behind the locked doors of 57 Bayview Drive lay a sinister reality far beyond ordinary human comprehension.",
            "During the exact years when Ken and Barbie were reveling in their idyllic life, a horrifying shadow was terrorizing Southern Ontario.",
            "Between 1987 and 1990, the Toronto suburb of Scarborough was shaken to its core by a serial predator known as the 'Scarborough Rapist'.",
            "He stalked young women walking alone in the dark, striking swiftly before vanishing without a trace.",
            "Widespread public paranoia and collective trauma gripped bus stops and suburban neighborhoods whenever night fell."
        ],
        "sents_ja": [
            "しかし、Bayview Drive 57番地の固く閉ざされた扉の奥には、一般人の想像を遥かに超える暗黒の現実が横たわっていました。",
            "ケンとバービーが華やかな暮らしを満喫していたまさにその時期、オンタリオ州南部は得体の知れない恐怖の影に怯えていました。",
            "1987年から1990年にかけて、トロント郊外のスカーバロー地区は『Scarborough Rapist』と呼ばれる正体不明のプレデターによって震撼させられていたのです。",
            "彼は夜道を一人で歩く若い女性を執拗につけ狙い、電撃的に襲撃しては何の痕跡も残さず闇へと姿を消しました。",
            "日が沈むたびに、バス停や住宅街には集団的偏執病と拭い去れないトラウマが重くのしかかっていました。"
        ],
        "sents_ko": [
            "그러나 Bayview Drive 57번지의 굳게 닫힌 문 뒤에는 일반인의 상상을 아득히 뛰어넘는 음산한 현실이 똬리를 틀고 있었습니다.",
            "켄과 바비가 풍요로운 일상을 만끽하던 바로 그 시절, 남부 Ontario 전역에는 소름 끼치는 공포의 그림자가 짙게 드리워져 있었습니다.",
            "1987년부터 1990년 사이, Toronto 외곽 Scarborough 지역은 ‘Scarborough Rapist’로 불리는 미지의 연쇄 습격범에 의해 공포의 도가니에 빠졌습니다.",
            "그는 야심한 시각 홀로 귀가하는 젊은 여성들을 어둠 속에서 은밀히 미행하여 기습한 뒤, 아무런 흔적도 남기지 않고 연기처럼 사라졌습니다.",
            "해가 저물 때마다 버스 정류장과 주택가 골목길에는 집단적 공포와 불안감이 무겁게 엄습했습니다."
        ]
    },
    {
        "id": "1.09",
        "kind": "NGHI",
        "sec": 1.5,
        "desc_vn": "khoảng lặng kịch tính"
    },
    {
        "id": "1.10",
        "kind": "LOI",
        "role": "ĐIỀU TRA VIÊN",
        "direction_vn": "giọng nam sắc bén, tái hiện hồ sơ hiện trường nghiệp vụ",
        "direction_en": "sharp, clinical tone, reconstructing investigative records",
        "direction_ja": "冷徹かつ鋭いトーンで、捜査現場の記録を再現する",
        "direction_ko": "예리하고 단호한 어조로, 현장 수사 기록을 복기하며",
        "sents_vn": [
            "Cảnh sát Toronto đã lập một nhóm đặc nhiệm quy mô lớn chưa từng có để truy tìm kẻ thủ ác vùng Scarborough, thu thập hàng trăm mẫu dấu vết nhưng hắn vẫn lẩn khuất ngoài vòng pháp luật.",
            "Nỗi khiếp đảm thực sự bùng nổ khi hành vi phạm tội vượt qua lằn ranh tấn công đơn thuần để bước sang quỹ đạo tước đoạt sinh mạng.",
            "Tháng 6 năm 1991, nữ sinh 14 tuổi Leslie Mahaffy đột ngột biến mất tại thành phố Burlington sau khi vô tình bị khóa ngoài cửa nhà trong đêm.",
            "Hai tuần sau, tin tức xác nhận cô bé đã không còn sống làm chấn động toàn bộ dư luận Canada.",
            "Chưa đầy một năm sau, vào tháng 4 năm 1992, nữ sinh 15 tuổi Kristen French tiếp tục bị bắt cóc giữa ban ngày ngay tại bãi đỗ xe của một nhà thờ ở thành phố Saint Catharines khi đang trên đường đi học về.",
            "Hai vụ án chấn động xảy ra ngay trong vùng Niagara, cách ngôi nhà màu hồng của Paul và Karla chỉ vài dặm đường."
        ],
        "sents_en": [
            "Toronto Police formed an unprecedented task force to track the Scarborough predator, compiling hundreds of leads while he remained elusive.",
            "The terror reached a boiling point when the criminal trajectory escalated from ambushes into taking human lives.",
            "In June 1991, 14-year-old Leslie Mahaffy vanished in Burlington after accidentally being locked out of her home late at night.",
            "Two weeks later, the confirmation that she was no longer alive sent shockwaves across Canada.",
            "Less than a year later, in April 1992, 15-year-old Kristen French was abducted in broad daylight from a church parking lot in Saint Catharines while walking home from school.",
            "Both high-profile tragedies unfolded right within the Niagara Region, just a few short miles from Paul and Karla's pink home."
        ],
        "sents_ja": [
            "トロント市警察は前例のない特別捜査本部を立ち上げスカーバローの犯人を追跡し、膨大な手がかりを収集したものの、犯人は依然として包囲網をすり抜けていました。",
            "そして犯罪の軌道が単なる路上襲撃から命を奪う凶行へと跳ね上がったとき、恐怖は頂点に達しました。",
            "1991年6月、バーリントンで深夜に自宅を締め出されてしまった14歳の女子生徒Leslie Mahaffyが突如として姿を消しました。",
            "2週間後、彼女がもはや生きていないことが確認され、カナダ全土に強烈な激震が走りました。",
            "それから1年も経たない1992年4月、セントキャサリンズで下校途中だった15歳の女子生徒Kristen Frenchが、教会の駐車場から白昼堂々連れ去られました。",
            "これら二つの震撼すべき悲劇は、PaulとKarlaが住むピンクの家からわずか数マイルしか離れていないナイアガラ地域で発生していたのです。"
        ],
        "sents_ko": [
            "Toronto 경찰국은 Scarborough의 포식자를 잡기 위해 전례 없는 대규모 전담 수사본부를 꾸리고 수백 건의 단서를 수집했지만, 범인은 법망을 유유히 피해 갔습니다.",
            "그리고 범행의 궤적이 단순한 기습 공격을 넘어 소중한 생명을 앗아가는 단계로 급격히 치달았을 때 공포는 극에 달했습니다.",
            "1991년 6월, Burlington에서 야간에 현관문이 잠겨 집 밖에서 곤란을 겪던 14세 여중생 Leslie Mahaffy가 흔적도 없이 사라졌습니다.",
            "2주 후, 아이가 더 이상 살아있지 않다는 참담한 소식이 전해지며 Canada 전역이 커다란 충격에 휩싸였습니다.",
            "채 1년도 지나지 않은 1992년 4월, Saint Catharines의 교회 주차장에서 하교 중이던 15세 여학생 Kristen French가 대낮에 납치되는 사건이 연이어 발생했습니다.",
            "온 나라를 뒤흔든 두 건의 비극적인 사건은, Paul과 Karla의 분홍빛 보금자리에서 불과 몇 마일 떨어지지 않은 Niagara 관내에서 일어났습니다."
        ]
    },
    {
        "id": "1.11",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "giọng trăn trở, nêu bật chấn động dư luận",
        "direction_en": "reflective, underscoring public outrage and dread",
        "direction_ja": "思索的で、世論の衝撃と恐怖を強調する語り口",
        "direction_ko": "고뇌에 찬 목소리로, 사회적 충격과 두려움을 드러내며",
        "sents_vn": [
            "Cả đất nước Canada rơi vào trạng thái hoảng loạn và phẫn nộ tột cùng trước sự tàn độc của kẻ săn mồi giấu mặt.",
            "Phụ nữ không dám bước ra đường một mình, các bậc phụ huynh nơm nớp lo sợ và đưa đón con cái từng bước chân.",
            "Ai là kẻ thủ ác đang gieo rắc nỗi kinh hoàng cho những thiếu nữ ngây thơ?",
            "Và làm thế nào một cặp đôi trẻ có vẻ ngoài đẹp như tranh vẽ lại trở thành tâm điểm của một liên minh tội ác kỳ dị nhất lịch sử tư pháp?",
            "Sự thật phía sau chiếc mặt nạ 'Ken và Barbie' là một bài học đắt giá về điểm mù xã hội khi con người bị mê hoặc bởi vẻ bề ngoài.",
            "Chúng ta hãy cùng lắng nghe phân tích chuyên môn về cách thức tội ác đã âm thầm hình thành."
        ],
        "sents_en": [
            "The entire nation of Canada plunged into profound panic and indignation at the cruelty of this faceless predator.",
            "Women feared walking alone outside, while anxious parents guarded their children's every step to and from school.",
            "Who was the monster casting this suffocating reign of terror over innocent young girls?",
            "And how could a picture-perfect young couple possibly be at the center of the most bizarre criminal partnership in modern judicial history?",
            "The reality behind that Ken and Barbie facade stands as a stark lesson in collective blindspots caused by superficial appearances.",
            "Let us now examine the specialized behavioral analysis of how this sinister trajectory quietly took root."
        ],
        "sents_ja": [
            "カナダ全土が、姿を見せぬ捕食者の非道さに対して計り知れないパニックと激しい憤りに包まれました。",
            "女性たちは一人で街を歩くことを恐れ、不安に駆られた親たちは通学路の子供たちの足取りを一歩一歩見守るようになりました。",
            "無垢な少女たちに底知れぬ恐怖を撒き散らしている怪物は一体何者だったのでしょうか。",
            "そして絵に描いたように完璧な若きカップルが、いかにして司法史上最も異様な犯罪連盟の中心となっていったのでしょうか。",
            "ケンとバービーの仮面の裏に隠された真実は、外見の美しさに惑わされた社会の集団的盲点に関する極めて重い教訓を突きつけています。",
            "この恐るべき犯罪がどのように水面下で醸成されていったのか、専門的な行動科学の分析に耳を傾けてみましょう。"
        ],
        "sents_ko": [
            "얼굴 없는 포식자의 잔혹함 앞에 Canada 전역은 걷잡을 수 없는 공황과 끓어오르는 분노에 휩싸였습니다.",
            "여성들은 밤거리를 혼자 걷는 것을 극도로 두려워했고, 불안에 짓눌린 부모들은 등하굣길 자녀들의 발걸음을 일일이 동행했습니다.",
            "순진무구한 소녀들에게 이토록 참혹한 공포를 몰고 온 장본인은 도대체 누구였을까요?",
            "그리고 그림처럼 완벽해 보이던 신혼부부가 어떻게 사법 역사상 가장 기괴한 범죄 파트너십의 중심에 설 수 있었을까요?",
            "‘켄과 바비’ 가면 뒤에 숨겨진 진실은, 화려한 외양에 현혹된 사회의 집단적 맹점에 관한 뼈아픈 교훈을 던져줍니다.",
            "이 음습한 범죄가 보이지 않는 수면 아래서 어떻게 싹텄는지, 전문적인 행동과학 분석을 통해 짚어보겠습니다."
        ]
    },
    {
        "id": "1.12",
        "kind": "SFX",
        "desc_vn": "Tiếng đóng cửa sắt nặng nề vang lên dứt khoát.",
        "desc_en": "Heavy iron door slamming shut with finality.",
        "desc_ja": "重厚な鉄の扉が断固として閉まる重い音。",
        "desc_ko": "묵직한 철문이 쾅 하고 닫히는 단호한 소리."
    },
    {
        "id": "1.13",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "đĩnh đạc, dẫn nhập chủ đề hồ sơ chuyên sâu",
        "direction_en": "authoritative, introducing the documentary brief and thesis",
        "direction_ja": "重厚で落ち着いた口調、詳細な事件記録への導入",
        "direction_ko": "차분하고 당당한 어조로, 심층 분석 주제를 소개하며",
        "sents_vn": [
            "Chào mừng quý vị đến với kênh Amber Eyes và hồ sơ phân tích tâm lý học tội phạm hôm nay.",
            "Chúng ta sẽ cùng mở khóa một trong những vụ án gây chấn động và tranh cãi sâu sắc nhất: Hồ sơ Paul Bernardo và Karla Homolka.",
            "Tập phim này sẽ giải mã hiện tượng 'Điên cuồng đôi', cơ chế đóng vai nạn nhân thao túng lòng trắc ẩn, và bản hợp đồng tư pháp cay đắng mang tên 'Thỏa thuận với Quỷ dữ'.",
            "Đồng thời, chúng tôi sẽ phân tích sâu sắc Hệ sinh thái 10 chỉ dấu tâm lý và hành vi để giúp nhận diện những mối quan hệ độc hại trong cuộc sống.",
            "Đây không chỉ là câu chuyện về một vụ án trong quá khứ, mà là lời cảnh tỉnh sâu sắc cho sự an toàn của mỗi chúng ta hôm nay.",
            "Xin mời quý vị cùng chúng tôi bước vào Hồi thứ hai để giải mã quỹ đạo leo thang của tội ác."
        ],
        "sents_en": [
            "Welcome to Amber Eyes and today's criminal psychology profile.",
            "Together, we will unlock one of the most shocking and contentious cases in legal history: the file of Paul Bernardo and Karla Homolka.",
            "This episode dissects the phenomenon of 'Folie à Deux', the manipulative art of playing the victim, and the bitter legal compromise remembered as the 'Deal with the Devil'.",
            "Furthermore, we will delve deeply into the 10 Psychological Markers framework to help recognize toxic relationship dynamics in everyday life.",
            "This is not merely a chronicle of past horrors, but an urgent wake-up call for our personal safety and vigilance today.",
            "Join us as we step into Act Two to unravel the dark trajectory of behavioral escalation."
        ],
        "sents_ja": [
            "犯罪心理学プロファイルをお届けするAmber Eyesへようこそ。",
            "本日は、司法史上最も衝撃的で激しい議論を巻き起こした事件、Paul BernardoとKarla Homolkaの記録を解き明かしていきます。",
            "今回のエピソードでは、『共有妄想（フォリー・ドゥ）』の病理、同情を搾取する被害者面のメカニズム、そして『悪魔との取引』と刻まれた苦い司法の妥協を解剖します。",
            "さらに、日常に潜む有害な関係性を見抜く手掛かりとして、10の心理的・行動的指標の体系を深く掘り下げていきます。",
            "これは単なる過去の凄惨な事件簿ではなく、現代を生きる私たちの身を守るための切実な警鐘でもあるのです。",
            "それでは、犯罪行動がいかにして危険なエスカレーションを辿ったのか、第2幕で解き明かしていきましょう。"
        ],
        "sents_ko": [
            "범죄심리 프로파일을 전해드리는 Amber Eyes에 오신 것을 환영합니다.",
            "오늘 우리는 사법 역사상 가장 큰 충격과 논란을 남긴 사건, 바로 Paul Bernardo와 Karla Homolka의 파일을 함께 열어보고자 합니다.",
            "이번 편에서는 ‘폴리 아 되’로 불리는 감응성 정신병의 실체, 동정심을 조작하는 피해자 코스프레의 수법, 그리고 ‘악마와의 거래’로 회자되는 뼈아픈 사법적 타협을 해부합니다.",
            "아울러 우리 주변의 유해한 관계를 식별하는 데 도움을 주고자, 10대 심리 및 행동 지표의 생태계를 심도 있게 조명할 것입니다.",
            "이것은 단순한 과거의 참극을 회고하는 것이 아니라, 오늘날 우리 모두의 안전과 생존을 일깨우는 엄중한 경고입니다.",
            "범죄의 궤적이 어떻게 파멸적인 에스컬레이션을 겪었는지, 제2막을 통해 그 내막을 본격적으로 파헤쳐 보겠습니다."
        ]
    }
]
