# -*- coding: utf-8 -*-
"""Dữ liệu Hồi 2 Kịch bản Tập 11 (4 ngôn ngữ: VN, EN, JA, KO)."""

ACT2_ELEMENTS = [
    {
        "id": "2.01",
        "kind": "BGM",
        "desc_vn": "Nhạc Minimalist Piano rải những nốt lạnh lẽo, xen lẫn âm thanh gõ bàn phím máy tính chậm rãi trong đêm vắng.",
        "desc_en": "Chilly minimalist piano notes echoing in the quiet night, interspersed with deliberate keystrokes.",
        "desc_ja": "静まり返る夜に冷涼なミニマルピアノの単音が響き、不穏なキーボードの打鍵音と交錯する。",
        "desc_ko": "고요한 밤을 가르는 차가운 미니멀 피아노 선율 사이로 불길한 키보드 타건음이 나직하게 섞여든다."
    },
    {
        "id": "2.02",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "giọng đọc chậm, trầm, dẫn dắt vào giải phẫu hành vi hiện trường",
        "direction_en": "measured, somber, transitioning into behavioral crime scene analysis",
        "direction_ja": "抑制された落ち着いた語り口で、現場行動の分析へと導入する",
        "direction_ko": "침착하고 무게감 있는 어조로 현장 행동 분석을 이끌며",
        "sents_vn": [
            "Khi hai thiếu nữ vô tội liên tiếp biến mất tại khu vực Niagara, cơ quan điều tra nhận định họ không chỉ đối mặt với những vụ bắt cóc đơn lẻ.",
            "Kẻ thủ ác không xuất hiện từ hư không; hắn là một kẻ săn mồi đã tích lũy kinh nghiệm qua nhiều năm rèn giũa kỹ năng trong bóng tối.",
            "Tội ác của Paul Bernardo và Karla Homolka là kết quả của một chu kỳ ảo tưởng và dung nạp kích thích cực kỳ bệnh hoạn.",
            "Giống như một cơn nghiện độc hại, khi những hành vi ban đầu không còn đem lại sự hưng phấn quyền lực, ngưỡng thỏa mãn buộc phải đẩy lên cao hơn.",
            "Toàn bộ chuỗi hành vi của cặp đôi này vận hành qua 4 nấc thang leo thang hành vi tàn bạo kéo dài suốt 5 năm.",
            "Xin mời Điều tra viên tái hiện lại các giai đoạn phát triển tội ác trong hồ sơ nghiệp vụ."
        ],
        "sents_en": [
            "When two innocent young girls vanished in the Niagara region, investigators realized they were not dealing with isolated disappearances.",
            "The perpetrator had not materialized out of thin air; he was a methodical predator honing his predatory craft over years in the shadows.",
            "The crimes of Paul Bernardo and Karla Homolka were the grotesque culmination of a fantasy addiction and escalating psychological tolerance.",
            "Much like a chemical addiction, once earlier deviant acts failed to deliver the intoxicating rush of power, the threshold of gratification escalated drastically.",
            "Their destructive trajectory progressed systematically across 4 distinct behavioral escalation stages spanning 5 years.",
            "We invite the Investigator to reconstruct these critical phases from the official case records."
        ],
        "sents_ja": [
            "ナイアガラ地域で二人の無垢な少女が相次いで姿を消したとき、捜査当局はこれが単発の失踪事件ではないことを悟りました。",
            "犯人は突如として現れたのではなく、長年にわたり闇の中で捕食スキルを研ぎ澄ませてきた計算高いハンターだったのです。",
            "Paul BernardoとKarla Homolkaの凶行は、歪んだ妄想嗜癖と危険な刺激耐性の形成がもたらした恐るべき帰結でした。",
            "薬物中毒と同様に、初期の逸脱行為ではもはや絶対的な支配の快感が得られなくなったとき、満足を求める閾値は必然的に跳ね上がりました。",
            "彼らの破滅的な軌跡は、5年間にわたる4段階の明確な行動エスカレーションを経て体系的に進行していったのです。",
            "公式捜査記録に基づき、その決定的な段階を捜査官から再現してもらいましょう。"
        ],
        "sents_ko": [
            "Niagara 일대에서 무고한 두 소녀가 연이어 실종되었을 때, 수사관들은 이것이 단순한 개별 사건이 아님을 직감했습니다.",
            "범인은 어느 날 갑자기 허공에서 나타난 것이 아니라, 수년간 어둠 속에서 포식의 기술을 치밀하게 연마해 온 자였습니다.",
            "Paul Bernardo와 Karla Homolka의 범행은 왜곡된 망상 중독과 극단적인 자극 내성이 빚어낸 참담한 결과물이었습니다.",
            "마치 독한 약물 중독처럼, 초기의 일탈 행위가 더 이상 지배의 쾌감을 주지 못하자 만족을 위한 심리적 문턱은 급격히 높아졌습니다.",
            "두 사람의 파멸적인 행적은 5년에 걸쳐 진행된 4단계의 뚜렷한 행동적 에스컬레이션을 거치며 체계적으로 진화했습니다.",
            "공식 수사 기록에 담긴 그 결정적인 국면들을 수사관의 목소리로 복기해 보겠습니다."
        ]
    },
    {
        "id": "2.03",
        "kind": "SFX",
        "desc_vn": "Tiếng lật mở hồ sơ giấy và tiếng click chuột lách cách.",
        "desc_en": "Paper folders opening, crisp clicking of a computer mouse searching a database.",
        "desc_ja": "捜査ファイルを開く紙の擦れる音、データベースを検索するマウスの乾いたクリック音。",
        "desc_ko": "서류철을 펼치는 사각거리는 소리, 데이터베이스를 검색하는 마우스 클릭 소리."
    },
    {
        "id": "2.04",
        "kind": "LOI",
        "role": "ĐIỀU TRA VIÊN",
        "direction_vn": "giọng đanh thép, lạnh lùng, nhấn mạnh từng tình tiết chứng cứ",
        "direction_en": "firm, detached, emphasizing each forensic milestone",
        "direction_ja": "毅然とした冷静な口調で、証拠の各節目を明確に強調する",
        "direction_ko": "냉정하고 단호한 어조로, 수사 기록상의 각 단계를 명확히 짚으며",
        "sents_vn": [
            "Dựa trên dữ liệu điều tra liên ngành, chúng tôi đã tái dựng quỹ đạo tha hóa của Paul Bernardo qua 4 giai đoạn leo thang rõ rệt:",
            "* Nấc thang thứ nhất: Tấn công đơn lẻ tại ngoại ô.",
            "Từ tháng 5 năm 1987, Paul Bernardo bắt đầu rình rập và thực hiện ít nhất 14 vụ tấn công phụ nữ trẻ tại vùng Scarborough, hành động đơn độc và tẩu thoát nhanh trong đêm.",
            "* Nấc thang thứ hai: Thiết lập liên minh và xâm phạm người thân.",
            "Tháng 10 năm 1987, hắn gặp Karla Homolka; sự gắn kết lệch lạc đã thúc đẩy chúng nhắm vào chính em gái ruột của Karla là Tammy Homolka vào đêm Giáng sinh năm 1990 bằng thuốc an thần đánh cắp, dẫn đến sự ra đi đau lòng của cô bé.",
            "* Nấc thang thứ ba: Bắt cóc giam giữ dài ngày tại tư gia.",
            "Tháng 6 năm 1991, sau khi kết hôn, chúng bắt cóc Leslie Mahaffy, đưa về giam cầm và ngược đãi tại căn nhà số 57 Bayview Drive trước khi tước đoạt mạng sống của cô bé.",
            "* Và nấc thang thứ tư: Táo tợn bắt cóc công khai giữa ban ngày.",
            "Tháng 4 năm 1992, chúng phục kích bắt giữ Kristen French ngay tại bãi xe nhà thờ đông người ở Saint Catharines, chứng tỏ ảo tưởng quyền lực đã lấn át hoàn toàn nỗi sợ bị phát giác.",
            "Điểm đáng sợ nhất là sự phối hợp nhịp nhàng giữa hai kẻ thủ ác trong việc giam cầm và tiêu hủy mọi dấu vết sau mỗi vụ án.",
            "Chúng sử dụng xi măng và các công cụ cơ khí để giấu tang vật dưới lòng kênh đào Lake Gibson nhằm đánh lạc hướng cơ quan chức năng.",
            "Đó là sự biến chất từ một kẻ rình rập đơn độc thành một cặp đôi sát nhân tàn độc có tổ chức."
        ],
        "sents_en": [
            "Based on inter-agency intelligence, we mapped Paul Bernardo's descent through 4 distinct escalation stages:",
            "* Stage One: Lone suburban ambushes.",
            "Beginning in May 1987, Bernardo stalked and carried out at least 14 predatory assaults against young women in Scarborough, operating entirely alone under cover of darkness.",
            "* Stage Two: Forming the partnership and violating family.",
            "In October 1987, he met Karla Homolka; their deviant bond culminated on Christmas Eve 1990 in drugging Karla's 15-year-old sister Tammy Homolka with stolen veterinary sedatives, leading to her tragic death.",
            "* Stage Three: Residential confinement.",
            "In June 1991, right around their marriage, they abducted Leslie Mahaffy, confining and tormenting her at 57 Bayview Drive before ending her young life.",
            "* And Stage Four: Brazen daytime abductions.",
            "In April 1992, they snatched Kristen French in broad daylight from a public church parking lot in Saint Catharines, proving their delusional sense of omnipotence had entirely eclipsed any fear of detection.",
            "What proved most chilling was the calculated division of labor between both perpetrators in managing confinement and covering their tracks.",
            "They utilized concrete and industrial tools to conceal evidence in Lake Gibson, deliberately misleading forensic search efforts.",
            "This marked a terrifying evolution from a solitary prowler into an organized, lethal predatory pair."
        ],
        "sents_ja": [
            "合同捜査班のデータに基づき、私たちはPaul Bernardoの凶行を4つの明確なエスカレーション段階として整理しました。",
            "* 第1段階：郊外での単独襲撃。",
            "1987年5月以降、Bernardoはスカーバロー地域で若い女性を執拗につけ狙い、夜陰に紛れて少なくとも14件の単独路上襲撃を繰り返しました。",
            "* 第2段階：共犯関係の結成と身内への侵害。",
            "1987年10月にKarla Homolkaと出会い、歪んだ結合を深めた二人は、1990年のクリスマスイブに動物病院から盗んだ鎮静剤を用いてKarlaの実妹Tammy Homolkaを襲い、悲劇的な死をもたらしました。",
            "* 第3段階：自宅での長期監禁。",
            "結婚直後の1991年6月、二人はLeslie Mahaffyを拉致し、Bayview Drive 57番地の自宅で監禁・虐待の末にその命を奪いました。",
            "* そして第4段階：白昼堂々の大胆な拉致。",
            "1992年4月、セントキャサリンズの人通りのある教会の駐車場から白昼堂々Kristen Frenchを急襲し、全能感の妄想が発覚への恐怖を完全に凌駕していたことを示しました。",
            "最も恐るべき点は、被害者の拘束から犯行痕跡の隠滅に至るまで、二人の凶行が見事な連携で行われていたことでした。",
            "彼らはセメントや工具を駆使して証拠をレイク・ギブソンの水底に沈め、当局の科学捜査を執拗に撹乱しました。",
            "それは孤独なストーカーから、組織化された冷酷な連続殺人ペアへの決定的な変貌を意味していたのです。"
        ],
        "sents_ko": [
            "합동 수사본부의 정밀 데이터를 바탕으로, 저희는 Paul Bernardo의 범죄 행적을 4단계 에스컬레이션 궤적으로 재구성했습니다.",
            "* 1단계: 외곽 지역의 단독 기습.",
            "1987년 5월부터 Bernardo는 Scarborough 일대에서 어둠을 틈타 단독으로 행동하며 젊은 여성들을 상대로 최소 14건의 연쇄 습격을 자행했습니다.",
            "* 2단계: 공범 연대 구축과 가족에 대한 침해.",
            "1987년 10월 Karla Homolka를 만난 후 왜곡된 결속을 다진 두 사람은, 1990년 크리스마스이브에 훔친 동물 진정제를 사용해 Karla의 친동생인 15세 Tammy Homolka를 공격하여 참담한 죽음에 이르게 했습니다.",
            "* 3단계: 주거지 내 감금과 가해.",
            "결혼 직후인 1991년 6월, 두 사람은 Leslie Mahaffy를 납치해 Bayview Drive 57번지 자택에 감금하고 가혹 행위를 일삼은 끝에 소중한 목숨을 앗아갔습니다.",
            "* 그리고 4단계: 대낮 공개 장소에서의 대담한 납치.",
            "1992년 4월, Saint Catharines의 교회 주차장에서 대낮에 Kristen French를 납치하며, 전능하다는 과대망상이 발각의 두려움을 완전히 압도했음을 드러냈습니다.",
            "무엇보다 끔찍했던 사실은, 피해자 감금부터 사후 은폐 공작에 이르기까지 두 사람의 역할 분담이 소름 끼칠 만큼 유기적이었다는 점입니다.",
            "그들은 시멘트와 기계 장비를 동원해 증거를 Lake Gibson 수중에 은닉하며 수사망을 교묘히 교란했습니다.",
            "이는 외톨이 스토커가 조직적이고 냉혹한 2인조 연쇄 살인마로 진화했음을 보여주는 전형적인 궤적이었습니다."
        ]
    },
    {
        "id": "2.05",
        "kind": "NGHI",
        "sec": 1.5,
        "desc_vn": "khoảng lặng kịch tính"
    },
    {
        "id": "2.06",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "trầm tư, tôn vinh phẩm giá và lòng dũng cảm của nạn nhân",
        "direction_en": "somber, honoring the victim's dignity and courage",
        "direction_ja": "厳粛で、被害者の尊厳と勇気に敬意を表する語り口",
        "direction_ko": "숙연한 목소리로 피해자의 존엄과 용기를 기리며",
        "sents_vn": [
            "Nhìn vào danh tính của các nạn nhân, chúng ta thấy rõ sự tàn nhẫn của động lực bất đối xứng quyền lực.",
            "Tammy Homolka là một cô bé 15 tuổi ngây thơ, đặt trọn niềm tin vào người chị gái ruột thịt của mình.",
            "Leslie Mahaffy và Kristen French là những nữ sinh trung học tràn đầy ước mơ, bị tước đoạt tương lai chỉ vì lọt vào tầm ngắm của những kẻ săn mồi.",
            "Tuy nhiên, sự thật lịch sử phải tôn vinh sự kiên cường và phẩm giá bất khuất của Kristen French.",
            "Trong suốt những ngày bị giam giữ, cô bé 15 tuổi ấy đã kiên quyết không chịu khuất phục và chiến đấu dũng cảm đến hơi thở cuối cùng."
        ],
        "sents_en": [
            "Looking at the victims' profiles, the cold cruelty of predator power asymmetry becomes sickeningly evident.",
            "Tammy Homolka was an innocent 15-year-old girl who placed absolute trust in her older biological sister.",
            "Leslie Mahaffy and Kristen French were bright high school students whose futures were violently stolen simply for crossing a predator's radar.",
            "Yet historical truth demands that we honor the extraordinary dignity and resilience of Kristen French.",
            "Throughout her grueling days in captivity, that courageous 15-year-old steadfastly refused to surrender her spirit and fought bravely to the very end."
        ],
        "sents_ja": [
            "被害者たちの横顔を見つめるとき、捕食者による非対称な力関係の冷酷さが痛烈に浮かび上がってきます。",
            "Tammy Homolkaは実の姉を無条件に信頼していた無垢な15歳の少女でした。",
            "Leslie MahaffyとKristen Frenchは、捕食者の視界に入ってしまったというだけで未来を無残に奪われた、夢に溢れる女子高校生でした。",
            "しかし歴史の真実として、私たちはKristen Frenchの類まれなる気高さと不屈の勇気を決して忘れてはなりません。",
            "過酷な拘束の最中にあっても、その勇敢な15歳の少女は精神を決して屈服させることなく、最後の瞬間まで尊厳のために戦い抜いたのです。"
        ],
        "sents_ko": [
            "피해자들의 면면을 돌아볼 때, 포식자가 휘두른 비대칭적 권력 관계의 잔혹함이 소름 끼치도록 명백하게 드러납니다.",
            "Tammy Homolka는 친언니를 절대적으로 신뢰했던 순진한 15세 소녀였습니다.",
            "Leslie Mahaffy와 Kristen French는 단지 포식자의 레이더망에 포착되었다는 이유만으로 미래를 송두리째 빼앗긴 꿈 많은 여학생들이었습니다.",
            "그러나 역사적 진실은 우리가 Kristen French가 보여준 비범한 품격과 불굴의 용기를 반드시 기억할 것을 요구합니다.",
            "그 모진 감금의 순간 속에서도, 그 용감한 15세 소녀는 결코 영혼을 굴복시키지 않은 채 마지막 순간까지 당당히 맞서 싸웠습니다."
        ]
    },
    {
        "id": "2.07",
        "kind": "LOI",
        "role": "ĐIỀU TRA VIÊN",
        "direction_vn": "đanh thép, phân định rạch ròi giữa thủ đoạn và chữ ký tâm lý",
        "direction_en": "firm, demarcating Modus Operandi from behavioral Signature",
        "direction_ja": "毅然とした口調で、犯行手口と心理的署名を明確に区別する",
        "direction_ko": "단호한 목소리로 범행 수법과 심리적 시그니처를 뚜렷이 구분하며",
        "sents_vn": [
            "Kristen French đã để lại những vết cào cấu quyết liệt trên người Paul Bernardo trong lúc giằng co tự vệ.",
            "Chính tinh thần phản kháng bất khuất ấy đã giúp lưu giữ những mẫu ADN quan trọng của kẻ thủ ác.",
            "Về mặt nghiệp vụ, chúng tôi phân định rất rõ giữa hai yếu tố: 'Thủ đoạn gây án' và 'Dấu ấn tâm lý'.",
            "Thủ đoạn gây án của chúng là sử dụng công cụ đe dọa, cắt đứt liên lạc, dùng thuốc an thần động vật và che giấu chứng cứ nhằm trốn tránh pháp luật.",
            "Thủ đoạn này liên tục thay đổi và hoàn thiện sau mỗi lần gây án để đối phó với cảnh sát.",
            "Nhưng 'Dấu ấn tâm lý' — thứ không bao giờ thay đổi — chính là nhu cầu bệnh lý về việc ghi hình lại toàn bộ tội ác."
        ],
        "sents_en": [
            "Kristen French left fierce scratch marks across Paul Bernardo's body as she fought desperately in self-defense.",
            "It was her brave resistance that directly preserved critical forensic DNA evidence from her attacker.",
            "In forensic methodology, we draw an absolute distinction between 'Modus Operandi' and behavioral Signature.",
            "Their Modus Operandi involved intimidation tools, isolating victims, administering stolen tranquilizers, and concealing materials to evade capture.",
            "This functional method continually evolved and sharpened with each crime to counter law enforcement tactics.",
            "Yet their 'behavioral Signature' — the immutable psychological fingerprint — was their compulsive need to videotape the crimes."
        ],
        "sents_ja": [
            "Kristen Frenchは必死の自衛の中で、Paul Bernardoの身体に鮮烈な抵抗の爪痕を残しました。",
            "その屈しない抵抗こそが、襲撃者の極めて重要な法医学的DNA証拠を直接保持することにつながったのです。",
            "鑑識実務において、私たちは『手口』と心理的署名を厳格に区別して扱います。",
            "彼らの手口は、脅迫具を用い、被害者を孤立させ、盗んだ鎮静剤を投与し、捜査を逃れるために証拠を隠蔽することでした。",
            "この機能的手法は、警察の捜査網に対抗するために犯行を重ねるごとに学習され先鋭化していきました。",
            "しかし彼らの『心理的署名』――決して変わることのない不変の刻印――とは、犯行の全容をビデオテープに記録するという病的な欲求でした。"
        ],
        "sents_ko": [
            "Kristen French는 필사적인 자기방어 과정에서 Paul Bernardo의 몸에 격렬한 저항의 손톱자국을 남겼습니다.",
            "바로 그 꺾이지 않은 용기 덕분에 공격자의 결정적인 법의학적 DNA 증거가 고스란히 보존될 수 있었습니다.",
            "수사 기법상, 저희는 ‘범행 수법’과 ‘심리적 시그니처’를 철저하게 구별하여 분석합니다.",
            "두 사람의 범행 수법은 협박 도구를 사용하고, 연락을 차단하며, 훔친 진정제를 투여하고, 수사망을 피하기 위해 증거물을 은닉하는 행위였습니다.",
            "이러한 기능적 수법은 경찰의 추적을 따돌리기 위해 매 범행마다 끊임없이 수정되고 정교해졌습니다.",
            "그러나 결코 변하지 않는 ‘심리적 시그니처’는 바로 범행의 모든 과정을 비디오카메라에 기록하려는 병적인 욕구였습니다."
        ]
    },
    {
        "id": "2.08",
        "kind": "SFX",
        "desc_vn": "Tiếng cuộn băng cassette quay rè rè và tiếng nút bấm máy quay cơ khí.",
        "desc_en": "Mechanical camcorder tape whirring, tactile click of a recording switch.",
        "desc_ja": "家庭用ビデオカメラのテープが回転する機械音、録画ボタンが押される重いクリック音。",
        "desc_ko": "캠코더 테이프가 돌아가는 기계음, 녹화 버튼이 딸깍하고 눌리는 묵직한 소리."
    },
    {
        "id": "2.09",
        "kind": "LOI",
        "role": "CHUYÊN GIA TÂM LÝ",
        "direction_vn": "giọng học thuật, mổ xẻ chứng cứ tâm lý video",
        "direction_en": "academic, dissecting psychological mechanics behind the videotapes",
        "direction_ja": "学術的な分析トーンで、ビデオ記録の背後にある心理メカニズムを解剖する",
        "direction_ko": "학술적이고 통찰력 있는 어조로 비디오 기록 이면의 심리 메커니즘을 분석하며",
        "sents_vn": [
            "Đúng như vậy, việc dùng máy quay cầm tay để ghi lại từng thước phim giam cầm không hề phục vụ cho mục đích tẩu thoát của chúng.",
            "Đó là hành vi thuộc về 'Signature' — dấu ấn tâm lý thỏa mãn cảm giác thống trị và chiếm hữu tuyệt đối.",
            "Chúng ép buộc các nạn nhân phải gọi chúng bằng những danh xưng phục tùng, biến nỗi đau của người khác thành những thước phim chiến lợi phẩm.",
            "Đối với Paul Bernardo, các cuộn băng là liều kích thích kích hoạt lại ảo tưởng vĩ cuồng mỗi khi hắn ngồi xem lại một mình.",
            "Còn đối với Karla Homolka, việc cầm máy quay là cách cô ta thể hiện sự gắn kết chặt chẽ với người bạn đời lệch lạc.",
            "Những cuộn băng ấy chính là chiếc chìa khóa duy nhất bóc trần bản chất thật của liên minh tội ác này."
        ],
        "sents_en": [
            "Indeed, utilizing a camcorder to document the confinement served zero functional utility in evading capture.",
            "It was an unmistakable 'Signature' behavior — satisfying an insatiable craving for absolute domination and psychological possession.",
            "They forced victims to address them by subservient titles, transforming human suffering into grotesque trophies on magnetic tape.",
            "For Paul Bernardo, these recordings served as a toxic catalyst to rekindle grandiose fantasies whenever he reviewed them in solitude.",
            "For Karla Homolka, operating the camera signaled her absolute allegiance and intimate partnership with her disturbed spouse.",
            "Those hidden recordings would ultimately prove to be the single forensic key exposing the true reality of their criminal union."
        ],
        "sents_ja": [
            "まさにその通りであり、家庭用カメラで監禁の全過程を映像に記録することは逃走の役には一切立ちませんでした。",
            "それこそが明白な『Signature』行動であり、絶対的な支配と完全な心理的所有という歪んだ欲求を満たす儀式でした。",
            "彼らは被害者に屈辱的な呼称を使うよう強要し、他者の苦痛をビデオテープ上の戦利品へと貶めました。",
            "Paul Bernardoにとって、これらのテープは一人で鑑賞するたびに誇大妄想の全能感を再燃させるための刺激剤でした。",
            "そしてKarla Homolkaにとってカメラを回す行為は、破滅的な伴侶への絶対的な忠誠と連帯を示す手段だったのです。",
            "この隠蔽された記録こそが、後に二人の共犯関係の真の力学を白日の下に晒す唯一の法医学的鍵となりました。"
        ],
        "sents_ko": [
            "그렇습니다, 캠코더를 들고 감금의 전 과정을 낱낱이 영상으로 담아낸 행위는 도주나 증거 인멸에는 아무런 도움이 되지 않았습니다.",
            "그것은 오로지 절대적인 지배욕과 심리적 소유욕을 채우기 위한 명백한 ‘시그니처’ 행동이었습니다.",
            "두 사람은 피해자들에게 굴종적인 호칭을 강요하며 타인의 고통을 테이프에 담긴 엽기적인 트로피로 변질시켰습니다.",
            "Paul Bernardo에게 그 비디오들은 혼자 앉아 돌려볼 때마다 과대망상적 권력욕을 다시 점화하는 자극제 역할을 했습니다.",
            "반면 Karla Homolka에게 카메라를 쥐는 행위는 일탈한 반려자를 향한 절대적 헌신과 일체감을 확인하는 의식이었습니다.",
            "숨겨둔 그 테이프들이야말로 훗날 이 기괴한 범죄 연합의 실체를 명명백백히 밝혀낼 유일한 열쇠가 되었습니다."
        ]
    },
    {
        "id": "2.10",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "giọng trầm lắng, kết nối mạch sang phân tích hội chứng",
        "direction_en": "somber, transitioning to the clinical analysis of Folie a Deux",
        "direction_ja": "低く思索的な声で、感応精神病の臨床分析へと話を繋ぐ",
        "direction_ko": "차분하고 무게감 있는 어조로 감응성 정신병 분석으로 다리를 놓으며",
        "sents_vn": [
            "Thủ đoạn giúp chúng che giấu hành vi suốt nhiều năm ròng rã, nhưng chính dấu ấn tâm lý bệnh hoạn lại trở thành bằng chứng thép kết tội chúng.",
            "Nhưng điều gì đã khiến một cô gái trẻ xinh đẹp, có công việc ổn định lại sẵn sàng đồng lõa với những hành vi tàn nhẫn như vậy?",
            "Làm thế nào một mối quan hệ tình cảm lại có thể biến thành một buồng cộng hưởng ác tính thiêu rụi mọi ranh giới lương tri?",
            "Hãy cùng chúng tôi bước vào Hồi thứ ba để giải phẫu hiện tượng tâm lý học kỳ dị mang tên 'Điên cuồng đôi'.",
            "Xin mời Chuyên gia tâm lý làm sáng tỏ cơ chế bên trong bộ não của cặp đôi Ken và Barbie."
        ],
        "sents_en": [
            "Modus Operandi kept them hidden for years, but their obsessive behavioral Signature forged the undeniable evidence of their guilt.",
            "Yet what could drive an attractive young woman with a steady career to willingly orchestrate such cruel depravity?",
            "How could a romantic bond devolve into a malignant resonance chamber obliterating every trace of human conscience?",
            "Step with us into Act Three as we dissect the enigmatic behavioral phenomenon known as 'Folie à Deux'.",
            "We invite the Psychologist to illuminate the cognitive machinery inside the minds of Ken and Barbie."
        ],
        "sents_ja": [
            "手口は彼らを何年も捜査線から遠ざけましたが、病的なシグニチャーこそが皮肉にも動かぬ有罪の鉄証となりました。",
            "しかし、安定した職を持ち魅力的な容姿の若い女性が、なぜ進んでこれほど冷酷な凶行に手を貸したのでしょうか。",
            "いかにして親密な恋愛関係が、あらゆる道徳の境界を焼き尽くす悪性の共鳴室へと堕落していったのでしょうか。",
            "第3幕では、『共有妄想（フォリー・ドゥ）』と呼ばれる特異な心理現象を解剖していきます。",
            "心理専門家に、ケンとバービーの深層心理に潜む認知メカニズムを解明してもらいましょう。"
        ],
        "sents_ko": [
            "범행 수법은 그들을 수년간 법망 밖으로 숨겨주었지만, 집착적인 심리적 시그니처는 결국 그들의 유죄를 입증하는 결정적 증거가 되었습니다.",
            "하지만 반듯한 직업과 아름다운 외모를 지닌 젊은 여성이 왜 이토록 잔혹한 행위에 기꺼이 가담했을까요?",
            "어떻게 평범해 보이던 연인 관계가 인간으로서의 최소한의 양심마저 모조리 불태워버리는 악성 공명실로 변질될 수 있었을까요?",
            "제3막에서는 ‘폴리 아 되’로 알려진 기괴한 범죄심리학적 현상을 본격적으로 해부해 보겠습니다.",
            "심리학자의 전문적인 시각을 통해 켄과 바비의 뇌리 속에 자리 잡은 인지적 메커니즘을 밝혀내겠습니다."
        ]
    },
    {
        "id": "2.11",
        "kind": "BGM",
        "desc_vn": "Đoạn nhạc Cello u tối ngân lên một nốt trầm sâu lắng rồi chuyển dần sang tiếng Sub-bass ngột ngạt.",
        "desc_en": "Dark cello note sustaining deeply, mutating into an oppressive sub-bass drone.",
        "desc_ja": "ダークチェロの重苦しい低音が長く響き、息苦しいサブベースドローンへと変容していく。",
        "desc_ko": "어두운 첼로 저음이 깊게 여운을 남기며 점차 숨 막히는 서브베이스 드론으로 잦아든다."
    },
    {
        "id": "2.12",
        "kind": "LOI",
        "role": "ĐIỀU TRA VIÊN",
        "direction_vn": "lạnh lùng, khép lại bức tranh hiện trường và mở ra hồ sơ tâm lý",
        "direction_en": "detached, closing the crime scene brief and bridging to psychology",
        "direction_ja": "冷静沈着に現場の概要を総括し、深層心理の解明へと引き継ぐ",
        "direction_ko": "냉정하고 차분하게 현장 개요를 매듭지으며 심리 분석으로 연결하듯",
        "sents_vn": [
            "Trước khi đi vào cơ chế tâm lý, các dữ liệu khám xét tại số 57 Bayview Drive cần được nhìn nhận một cách khách quan.",
            "Ngôi nhà sơn hồng bên ngoài trông vô cùng ấm cúng, nhưng bên trong phòng ngủ và tầng hầm lại được bố trí như những căn phòng biệt lập.",
            "Hàng trăm vật dụng cá nhân của các nạn nhân đã được thu giữ và đối chiếu ADN cẩn trọng.",
            "Mỗi món đồ bị lấy đi không mang giá trị vật chất, mà mang ý nghĩa của những chiến lợi phẩm khẳng định quyền lực.",
            "Các điều tra viên nhận thấy hung thủ không hành động trong trạng thái hoảng loạn bộc phát.",
            "Mọi bước đi đều thể hiện sự toan tính lạnh lùng của những bộ óc hoàn toàn làm chủ nhận thức của mình."
        ],
        "sents_en": [
            "Before examining internal psychology, the physical search data at 57 Bayview Drive must be objectively assessed.",
            "While the exterior pink home appeared utterly welcoming, the interior bedrooms and basement were configured for strict isolation.",
            "Hundreds of personal belongings tied to victims were cataloged and rigorously cross-matched through DNA testing.",
            "Each taken memento carried zero monetary worth, serving solely as psychological trophies asserting dominance.",
            "Investigators observed unequivocally that the perpetrators never operated in spontaneous panic.",
            "Every calculated move reflected the cold deliberation of minds retaining complete cognitive lucidity."
        ],
        "sents_ja": [
            "心理メカニズムに入る前に、Bayview Drive 57番地での捜索データは客観的に精査される必要があります。",
            "外観のピンク色の家は非常に温かみがあるように見えましたが、寝室や地下室は厳格に隔離された空間として機能していました。",
            "被害者に属する無数の私物が押収され、慎重なDNA鑑定によって一件ずつ突き合わされました。",
            "奪われた物品は金銭的価値を持たず、支配力を誇示するための心理的戦利品としての意味しか持っていませんでした。",
            "捜査官たちは、犯人たちが決して突発的なパニック状態で行動していなかった点に注目しました。",
            "すべての手順は、自らの認知を完全に掌握した者たちによる冷徹な計算のもとで実行されていたのです。"
        ],
        "sents_ko": [
            "내면의 심리 메커니즘을 살피기 전에, Bayview Drive 57번지 자택에 대한 압수수색 결과는 객관적으로 분석되어야 합니다.",
            "외관상 분홍빛 주택은 지극히 아늑해 보였으나, 내부 침실과 지하실은 외부와 철저히 단절된 격리 공간으로 꾸며져 있었습니다.",
            "피해자들에게서 빼앗은 수많은 개인 소지품들이 압수되었고, 엄밀한 DNA 대조 작업을 통해 하나하나 확인되었습니다.",
            "그 물품들은 금전적 가치가 전무했으며, 오로지 지배력을 확인하기 위한 심리적 트로피의 기능만을 수행했습니다.",
            "수사관들은 범인들이 결코 우발적인 공황 상태에서 범행을 저지르지 않았다는 사실을 명확히 확인했습니다.",
            "모든 움직임은 상황을 온전히 통제하고 지각하던 자들의 서늘한 계산 아래서 치밀하게 실행되었습니다."
        ]
    }
]
