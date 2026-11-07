# -*- coding: utf-8 -*-
"""Dữ liệu Hồi 3 Kịch bản Tập 11 (4 ngôn ngữ: VN, EN, JA, KO)."""

ACT3_ELEMENTS = [
    {
        "id": "3.01",
        "kind": "BGM",
        "desc_vn": "Tiếng đàn Cello rải những nốt trầm ai oán, hòa cùng tiếng Sub-bass rền rĩ, tạo không gian u tối mang tính chất một ca phẫu thuật tâm lý học.",
        "desc_en": "Mournful cello notes mingling with deep sub-bass resonance, establishing an austere forensic surgical atmosphere.",
        "desc_ja": "チェロの沈痛な低音がうごめくサブベースと交じり合い、深層心理の解剖室のような重苦しい空間を演出する。",
        "desc_ko": "구슬픈 첼로 저음이 묵직한 서브베이스의 울림과 얽혀 들며, 심리 부검실 같은 냉엄하고 어두운 공간을 조성한다."
    },
    {
        "id": "3.02",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "đặt vấn đề sâu sắc, mở ra ca phẫu thuật tâm lý học",
        "direction_en": "profound, framing the psychological autopsy with philosophical weight",
        "direction_ja": "思索的で深みのある語り口、心理的解剖への問いかけを提示する",
        "direction_ko": "깊이 있는 질문을 던지며 심리학적 부검의 문을 여는 어조로",
        "sents_vn": [
            "Đứng trước hồ sơ của Paul Bernardo và Karla Homolka, bất kỳ ai trong chúng ta cũng phải đối mặt với một câu hỏi nhức nhối:",
            "Động lực tâm lý nào đã biến một cặp vợ chồng trẻ trung, có học thức thành những kẻ săn mồi tàn bạo nhất lịch sử Canada?",
            "Liệu Karla Homolka chỉ đơn thuần là một nạn nhân bị bạo hành và cưỡng ép như những gì cô ta từng trình bày trước tòa?",
            "Hay cô ta chính là một phần không thể tách rời của một cấu trúc tội ác cộng sinh nguy hiểm?",
            "Chúng ta cần lưu ý rằng, các phân tích tâm lý dưới đây dựa trên các khung lý thuyết khoa học hành vi và hồ sơ xét xử công khai, không phải là sự quy chụp tùy tiện.",
            "Xin mời Chuyên gia tâm lý giải mã hiện tượng tâm lý học đặc biệt này."
        ],
        "sents_en": [
            "Confronting the files of Paul Bernardo and Karla Homolka, every observer is faced with a haunting inquiry:",
            "What psychological catalyst transformed an educated, youthful couple into Canada's most notorious predatory union?",
            "Was Karla Homolka merely a battered, coerced victim as she so passionately argued before legal authorities?",
            "Or did she constitute an indispensable pillar within a lethal symbiotic criminal structure?",
            "It must be clarified that the following analysis draws upon behavioral science frameworks and verified public court records rather than arbitrary conjecture.",
            "We invite the Psychologist to decipher the architecture of this extraordinary dynamic."
        ],
        "sents_ja": [
            "Paul BernardoとKarla Homolkaの記録を前にしたとき、私たちは誰もが痛切な問いに直面せざるを得ません。",
            "教養ある若き夫婦を、いかなる心理的火種がカナダ史上最も悪名高き捕食ペアへと変貌させたのでしょうか。",
            "Karla Homolkaは、法廷で涙ながらに訴えたように、単なる暴力被害者であり強要された立場に過ぎなかったのでしょうか。",
            "それとも彼女自身が、この危険極まりない共生的な犯罪構造に不可欠な一部だったのでしょうか。",
            "ここで提示される心理分析は、恣意的な憶測ではなく、行動科学の理論的枠組みと公の裁判記録に基づくものであることを明記しておきます。",
            "心理専門家に、この極めて特異な心理現象の構造を読み解いてもらいましょう。"
        ],
        "sents_ko": [
            "Paul Bernardo와 Karla Homolka의 파일을 마주할 때, 우리는 모두 뼈아픈 질문 앞에 서게 됩니다.",
            "교육 수준이 높고 젊은 부부를 캐나다 역사상 가장 악명 높은 포식자 쌍으로 변모시킨 심리적 동력은 무엇이었을까요?",
            "Karla Homolka는 법정에서 주장했던 것처럼, 정말로 폭력에 짓눌려 강요당한 무력한 피해자에 불과했을까요?",
            "아니면 그녀 자신이 이 치명적인 공생적 범죄 구조의 떼려야 뗄 수 없는 핵심 축이었을까요?",
            "이하의 심리 분석은 자의적인 추측이 아니며, 행동과학의 학술적 틀과 공개된 재판 기록에 기반한 것임을 분명히 밝혀둡니다.",
            "심리학자의 전문적인 시선을 통해 이 기괴한 심리적 역동의 구조를 정밀하게 해부해 보겠습니다."
        ]
    },
    {
        "id": "3.03",
        "kind": "NGHI",
        "sec": 1.5,
        "desc_vn": "khoảng lặng kịch tính"
    },
    {
        "id": "3.04",
        "kind": "LOI",
        "role": "CHUYÊN GIA TÂM LÝ",
        "direction_vn": "giọng học thuật, khúc chiết, giải phẫu hiện tượng Điên cuồng đôi",
        "direction_en": "clinical, incisive, dissecting the Folie a Deux pathology",
        "direction_ja": "学術的かつ明晰な論理で、感応精神病の病理を解体する",
        "direction_ko": "명석하고 학술적인 어조로 감응성 정신병의 병리를 해부하며",
        "sents_vn": [
            "Khung lý thuyết kinh điển giúp giải thích trường hợp này là hiện tượng 'Điên cuồng đôi', hay còn gọi là Hội chứng Folie à Deux.",
            "Đây là một hiện tượng hiếm gặp khi hai cá nhân có cấu trúc tâm lý lệch lạc gặp gỡ và kết hợp với nhau, tạo ra một buồng cộng hưởng tội ác.",
            "Trong mối quan hệ này, Paul Bernardo đóng vai trò là kẻ khởi xướng mang tính ái kỷ ác tính và thái nhân cách chống đối xã hội.",
            "Hắn khao khát quyền lực thống trị tuyệt đối, xem phụ nữ như những công cụ phục vụ cho sự thỏa mãn bản ngã vĩ cuồng của mình.",
            "Ở chiều ngược lại, Karla Homolka không hề là một người bình thường bị cuốn vào vòng xoáy một cách thụ động.",
            "Các nhà phân tích hành vi chỉ ra rằng Karla sở hữu sự khiếm khuyết thấu cảm cảm xúc và nỗi sợ hãi bệnh lý bị người tình bỏ rơi.",
            "Thay vì sợ hãi rút lui khi chứng kiến xu hướng bạo lực của Paul, Karla lại tìm thấy ở hắn một cảm giác kích thích quyền lực và sự lệ thuộc mù quáng.",
            "Khi hai cấu trúc tâm lý đó hòa quyện, mọi rào cản đạo đức thông thường đã bị xóa bỏ hoàn toàn."
        ],
        "sents_en": [
            "The classic behavioral framework that best illuminates this dynamic is 'Folie à Deux', or Shared Psychotic Disorder.",
            "This rare psychological condition manifests when two disturbed individuals converge, creating an amplifying echo chamber of deviance.",
            "Within this toxic bond, Paul Bernardo functioned as the dominant instigator characterized by malignant narcissism and psychopathy.",
            "He harbored an insatiable hunger for total dominion, viewing women strictly as utilitarian instruments to feed his megalomaniacal ego.",
            "Conversely, Karla Homolka was never a conventional bystander passively swept along by circumstance.",
            "Behavioral profilers highlight that Karla exhibited profound affective empathy deficits combined with a pathological terror of romantic abandonment.",
            "Rather than fleeing Bernardo's early sadistic tendencies, she experienced a perverse thrill of shared power coupled with obsessive dependency.",
            "Once their deviant psychological systems locked together, conventional moral boundaries were entirely incinerated."
        ],
        "sents_ja": [
            "この力学を説明する最も古典的な行動科学の枠組みは、『共有妄想（フォリー・ドゥ）』という現象です。",
            "これは歪んだ心理構造を持つ二人が巡り合い結びつくことで、悪性を増幅させる強烈な共鳴室が形成される極めて稀な病態です。",
            "この有害な関係において、Paul Bernardoは悪性自己愛と反社会的人格を特徴とする主導者として機能しました。",
            "彼は絶対的な支配を渇望し、自らの誇大妄想的な自我を満たすための道具としてしか女性を見ていませんでした。",
            "対照的に、Karla Homolkaも決して状況に受動的に流されただけの一般的な無辜の人間ではありませんでした。",
            "行動分析家たちは、Karlaが他者の苦痛に対する深刻な感情的共感の欠如と、パートナーからの見捨てられ不安を病的に抱えていたと指摘します。",
            "Bernardoの暴力傾向を目撃して恐怖から逃げ出すどころか、彼女は共有された支配の快感と盲目的な依存に引き込まれていきました。",
            "二つの逸脱したシステムが噛み合った瞬間、人間社会の通常の倫理的防壁は完全に溶解してしまったのです。"
        ],
        "sents_ko": [
            "이 역동을 설명하는 가장 고전적인 행동과학적 분석 틀은 바로 ‘폴리 아 되’, 즉 감응성 정신병 현상입니다.",
            "이는 왜곡된 심리 구조를 지닌 두 개인이 만나 결합함으로써, 악성을 증폭시키는 치명적인 공명실을 형성하는 희귀한 병리입니다.",
            "이 유해한 관계 속에서 Paul Bernardo는 악성 자기애와 반사회적 성격을 특징으로 하는 주동자 역할을 수행했습니다.",
            "그는 절대적인 지배욕에 사로잡혀 있었으며, 여성들을 자신의 과대망상적 자아를 충족시키기 위한 도구로만 여겼습니다.",
            "반면 Karla Homolka 역시 상황에 수동적으로 휩쓸려 들어간 평범한 방관자가 결코 아니었습니다.",
            "행동 프로파일러들은 Karla가 타인의 고통에 대한 극단적인 정서적 공감 결여와 연인에게 버림받을지 모른다는 병적 공포를 동시에 지니고 있었다고 분석합니다.",
            "Bernardo의 폭력성을 목격하고 공포에 질려 도망치기는커녕, 그녀는 비정상적인 권력욕의 자극과 맹목적인 의존성을 공유했습니다.",
            "두 사람의 일탈적 심리 체계가 완벽히 맞물린 순간, 통상적인 도덕적 방어선은 흔적도 없이 사라져 버렸습니다."
        ]
    },
    {
        "id": "3.05",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "trầm tư, đào sâu vào cơ chế vật hóa nạn nhân",
        "direction_en": "reflective, probing deeper into victim objectification",
        "direction_ja": "思索的で、被害者の客体化のメカニズムを深く掘り下げる",
        "direction_ko": "깊은 생각에 잠긴 어조로 피해자 객체화의 실체를 파고들며",
        "sents_vn": [
            "Sự cộng sinh độc hại này đã dẫn tới một hiện tượng tâm lý cực kỳ tàn nhẫn: Sự 'vật hóa' nạn nhân.",
            "Trong mắt của cả Paul và Karla, những thiếu nữ ngây thơ kia bị nhìn nhận như thế nào, thưa chuyên gia?",
            "Tại sao Karla có thể nhẫn tâm đưa chính người em gái ruột thịt của mình vào chiếc bẫy oan nghiệt?",
            "Đó là câu hỏi khiến hàng triệu người dân Canada đau đớn và phẫn nộ suốt nhiều thập kỷ qua.",
            "Xin mời chuyên gia phân tích cơ chế nhận thức đen tối này."
        ],
        "sents_en": [
            "This toxic symbiosis yielded an utterly ruthless behavioral phenomenon: the total objectification of their victims.",
            "Through the warped lenses of Paul and Karla, how were these innocent young girls actually perceived?",
            "How could Karla cold-bloodedly deliver her own biological sister into such a devastating trap?",
            "That question has haunted and enraged millions of Canadians across multiple decades.",
            "We invite the Psychologist to dissect this dark cognitive architecture."
        ],
        "sents_ja": [
            "この有害な共生関係は、極めて無慈悲な行動現象、すなわち被害者の完全な『客体化』をもたらしました。",
            "PaulとKarlaの歪んだ視座において、無垢な少女たちは実際どのように知覚されていたのでしょうか。",
            "Karlaはなぜ、自らの実の妹をこれほど残酷な罠へと突き落とすことができたのでしょうか。",
            "それこそが、何十年にもわたり無数のカナダ国民を苦悩させ憤慨させてきた疑問でした。",
            "心理専門家に、この暗黒の認知構造を解剖してもらいましょう。"
        ],
        "sents_ko": [
            "이러한 유해한 공생 관계는 지극히 무자비한 행동 양식, 즉 피해자에 대한 완전한 ‘객체화’를 낳았습니다.",
            "Paul과 Karla의 왜곡된 시선 속에서 그 순결한 소녀들은 과연 어떤 존재로 인식되었던 것일까요?",
            "어떻게 Karla는 피를 나눈 친동생을 그토록 참담한 덫으로 스스로 밀어 넣을 수 있었을까요?",
            "그것이야말로 수십 년 동안 수많은 캐나다 시민들을 비탄과 분노에 잠기게 만든 핵심적인 질문이었습니다.",
            "심리학자의 시각을 통해 이 음습한 인지 구조의 작동 방식을 명쾌하게 짚어보겠습니다."
        ]
    },
    {
        "id": "3.06",
        "kind": "LOI",
        "role": "CHUYÊN GIA TÂM LÝ",
        "direction_vn": "sắc bén, bóc trần sự vật hóa, chia ngăn và tự bào chữa",
        "direction_en": "sharp, exposing objectification, compartmentalization, and neutralization",
        "direction_ja": "鋭利な論理で、客体化、精神の分断、自己正当化の機制を暴く",
        "direction_ko": "명확하고 예리한 어조로 객체화, 심리적 구획화, 자기 정당화의 실체를 폭로하며",
        "sents_vn": [
            "Khái niệm cốt lõi ở đây chính là 'vật hóa' và 'phi nhân hóa' nạn nhân.",
            "Paul Bernardo xem các nạn nhân như những món đồ chơi dùng một lần để thỏa mãn cơn nghiện quyền lực và ảo tưởng tình dục.",
            "Còn đối với Karla Homolka, bi kịch nằm ở chỗ cô ta giáng cấp chính em gái mình thành một 'vật hiến tế' để củng cố mối liên kết tình cảm với Paul.",
            "Karla hoàn toàn thiếu hụt 'Thuyết tâm trí' đối với nỗi đau của người khác; tiếng khóc van xin không kích hoạt lòng trắc ẩn mà bị xem như trở ngại cần loại bỏ.",
            "Để duy trì cuộc sống thường nhật, Karla áp dụng triệt để cơ chế 'Chia ngăn nhận thức'.",
            "Cô ta khóa chặt thế giới người vợ hiền yêu thương động vật ở một ngăn, và thế giới đồng lõa săn mồi ở một ngăn hoàn toàn biệt lập.",
            "Cuộc hôn nhân màu hồng và đám cưới cổ tích chính là 'Lá chắn bình thường hóa' giúp cô ta tự huyễn hoặc về phẩm giá của bản thân.",
            "Cô ta sử dụng các kỹ thuật 'Trung hòa đạo đức' để ru ngủ lương tri: tự nhủ rằng mình chỉ làm để làm vui lòng chồng và giữ gìn gia đình."
        ],
        "sents_en": [
            "The pivotal concept here is absolute psychological 'Objectification' and Dehumanization.",
            "Paul Bernardo treated victims as disposable instruments manufactured solely to satiate his addiction to dominance and sexual conquest.",
            "For Karla Homolka, the horror lay in degrading her own sister into a 'sacrificial offering' designed to secure her romantic bond with Paul.",
            "Karla possessed a crippled 'Theory of Mind' regarding others' suffering; pleas for mercy triggered no empathy, perceived merely as obstacles to be suppressed.",
            "To sustain everyday functioning, Karla relied heavily upon psychological 'Compartmentalization'.",
            "She walled off the persona of an animal-loving homemaker in one mental drawer, while keeping her predatory complicity locked in another.",
            "Their idyllic home and fairytale nuptials served as a 'Shield of Normalcy' allowing her to manufacture an unblemished self-image.",
            "She deployed 'Techniques of Neutralization' to silence guilt: whispering to herself that she acted purely to please her partner and safeguard her marriage."
        ],
        "sents_ja": [
            "ここで中核となる概念こそが、心理学における完全な『客体化』と『非人間化』です。",
            "Paul Bernardoは被害者たちを、自らの支配中毒と性的征服欲を満たすためだけに製造された使い捨ての道具として扱いました。",
            "そしてKarla Homolkaにとっての惨劇は、Paulとの絆を繋ぎ止めるための『生贄の供物』として実の妹を差し出したことにありました。",
            "Karlaは他者の苦痛を慮る『心の理論』を致命的に欠いており、命乞いの声も共感を呼ぶことはなく、単に排除すべき障害としか映りませんでした。",
            "日常を平然と送るため、Karlaは『精神の分断』という防衛機制を徹底的に運用していました。",
            "彼女は動物を愛する良妻という表向きの人格を一つの引き出しにしまい込み、冷酷な捕食者の共犯者という人格を別の引き出しに隔離していたのです。",
            "ピンクの邸宅やおとぎ話のような挙式は、自らの無謬性を思い込ませるための強固な『正常性の防壁』として機能しました。",
            "彼女は『中和の技術』を駆使して罪悪感を封殺し、すべては夫を喜ばせ家庭を守るためだったと言い聞かせて良心を麻痺させていたのです。"
        ],
        "sents_ko": [
            "여기서 가장 본질적인 개념은 바로 절대적인 심리적 ‘객체화’와 ‘탈인간화’입니다.",
            "Paul Bernardo에게 피해자들은 오직 자신의 지배욕과 성적 정복욕을 채우기 위해 소비되는 일회성 도구에 불과했습니다.",
            "그리고 Karla Homolka에게 있어 가장 끔찍한 비극은, Paul과의 애정적 결속을 공고히 하기 위한 ‘제물’로서 친동생을 전락시켰다는 점입니다.",
            "Karla는 타인의 고통을 인지하는 ‘마음의 이론’이 결핍되어 있었기에, 피해자의 애원은 연민을 부르지 못하고 단지 통제해야 할 성가신 방해물로 인식되었습니다.",
            "일상생활을 지탱하기 위해 Karla는 고도의 ‘심리적 구획화’ 기제를 적극적으로 활용했습니다.",
            "그녀는 동물을 아끼는 자상한 아내라는 서랍과, 냉혹한 범죄 공범자라는 서랍을 철저히 분리하여 서로 섞이지 않도록 가두었습니다.",
            "분홍빛 보금자리와 동화 같은 결혼식은 스스로를 품위 있는 존재로 착각하게 만드는 견고한 ‘정상성의 방패’ 역할을 했습니다.",
            "그녀는 ‘중화 기술’을 동원해 남편의 비위를 맞추고 가정을 지키기 위한 불가피한 선택이었다며 양심의 가책을 스스로 잠재웠습니다."
        ]
    },
    {
        "id": "3.07",
        "kind": "SFX",
        "desc_vn": "Tiếng gương kính vỡ vụn và tiếng kim loại va chạm khô khốc.",
        "desc_en": "Glass shattering violently, dry metallic impact reverberating in the quiet.",
        "desc_ja": "ガラスが激しく粉々に砕け散る音、不気味に響く乾いた金属の衝撃音。",
        "desc_ko": "유리창이 산산조각 나며 깨지는 소리, 적막 속에 울리는 건조한 금속 충격음."
    },
    {
        "id": "3.08",
        "kind": "LOI",
        "role": "ĐIỀU TRA VIÊN",
        "direction_vn": "lạnh lùng, tái hiện điểm gãy tâm lý và bước ngoặt điều tra",
        "direction_en": "clinical, reconstructing the precipitating tipping point and investigative breakthrough",
        "direction_ja": "冷徹に心理的崩壊の引き金と捜査上の転換点を再現する",
        "direction_ko": "냉철하게 심리적 한계점과 수사상의 결정적 전환점을 복기하며",
        "sents_vn": [
            "Tuy nhiên, liên minh nào rồi cũng sẽ phải đối mặt với điểm gãy nội tại.",
            "Và điểm gãy tâm lý của cặp đôi Ken và Barbie xuất hiện vào tháng 1 năm 1993, sau những chuỗi ngày căng thẳng leo thang.",
            "Paul Bernardo bắt đầu bộc lộ sự hung hãn trực tiếp lên chính Karla, ngược đãi cô ta bằng một chiếc đèn pin lớn khiến cô ta phải nhập viện cấp cứu.",
            "Trận đòn kinh hoàng đó đã phá vỡ chiếc mặt nạ tình yêu cổ tích, kích hoạt nỗi sợ hãi sinh tồn tột cùng bên trong Karla.",
            "Nhận thấy người bạn đời đã trở thành mối đe dọa trực tiếp đến tính mạng của mình, Karla quyết định rời bỏ căn nhà số 57 Bayview Drive.",
            "Và chỉ một tháng sau đó, vào ngày 17 tháng 2 năm 1993, cảnh sát ập vào bắt giữ Paul Bernardo.",
            "Kết quả giám định ADN tồn đọng từ nhiều năm trước của Cảnh sát Toronto cuối cùng đã xác nhận Paul Bernardo chính là kẻ gây án hàng loạt vùng Scarborough.",
            "Nhận thấy con thuyền tội ác sắp chìm nghỉm, Karla Homolka lập tức kích hoạt chiến lược sinh tồn tinh vi nhất cuộc đời mình."
        ],
        "sents_en": [
            "Yet even the most insidious alliances inevitably encounter an internal breaking point.",
            "The psychological breaking point for Ken and Barbie ruptured in January 1993 following weeks of escalating domestic volatility.",
            "Paul Bernardo turned his sadistic aggression directly against Karla, severely battering her with a heavy flashlight and sending her to the emergency room.",
            "That brutal assault shattered the fairytale illusion, activating raw survival panic inside Karla.",
            "Recognizing that her partner now posed an immediate existential threat to her own survival, Karla fled 57 Bayview Drive.",
            "Barely a month later, on February 17, 1993, police moved in and arrested Paul Bernardo.",
            "Backlogged DNA testing from years earlier finally confirmed Bernardo as the long-sought Scarborough serial predator.",
            "Sensing that their criminal ship was sinking irreparably, Karla Homolka initiated the most sophisticated survival scheme of her life."
        ],
        "sents_ja": [
            "しかし、どれほど強固に見える犯罪同盟であっても、必然的に内部からの崩壊点に直面します。",
            "ケンとバービーの心理的臨界点は、家庭内の暴力性が極限まで高まった1993年1月に訪れました。",
            "Paul Bernardoはサディスティックな攻撃性をKarla自身へと向け、大型の懐中電灯で激しく殴打して救急病院へと送り込みました。",
            "その凄惨な暴力はおとぎ話の幻想を粉々に打ち砕き、Karlaの深層に眠る剥き出しの生存本能を刺激しました。",
            "パートナーが今や自らの生命に対する直接の脅威となったことを察知したKarlaは、Bayview Drive 57番地を去る決断を下しました。",
            "それからわずか1ヶ月後の1993年2月17日、警察は踏み込みPaul Bernardoを逮捕しました。",
            "長年未処理だったDNA鑑定の結果が遂に一致し、Bernardoこそがスカーバローの連続捕食者であることが特定されたのです。",
            "共犯の泥舟が完全に沈没しようとしていることを悟ったKarla Homolkaは、人生で最も周到な自己保身戦略を直ちに始動させました。"
        ],
        "sents_ko": [
            "그러나 아무리 견고해 보이던 악의 연대라 할지라도, 반드시 내부로부터의 파열점에 직면하기 마련입니다.",
            "켄과 바비의 심리적 임계점은 가정 내 폭력성이 극에 달했던 1993년 1월에 마침내 터져 나왔습니다.",
            "Paul Bernardo는 가학적인 공격성을 아내인 Karla에게 직접 쏟아부었고, 대형 손전등으로 잔혹하게 폭행하여 그녀를 응급실에 입원시켰습니다.",
            "그 끔찍한 폭행은 동화 같은 사랑의 가면을 산산조각 내며, Karla 내면의 원초적인 생존 본능을 뒤흔들어 깨웠습니다.",
            "반려자가 이제 자신의 목숨을 위협하는 치명적인 칼날이 되었음을 직감한 Karla는 Bayview Drive 57번지 자택을 빠져나왔습니다.",
            "그리고 채 한 달이 지나지 않은 1993년 2월 17일, 경찰은 전격적으로 Paul Bernardo를 체포했습니다.",
            "수년간 밀려 있던 Toronto 경찰의 DNA 감식 결과가 마침내 일치하며, Bernardo가 악명 높던 Scarborough의 연쇄 포식자임이 확정된 것입니다.",
            "범죄의 배가 침몰하고 있음을 직감한 Karla Homolka는, 인생에서 가장 정교하고 치밀한 생존 전략을 전격 가동했습니다."
        ]
    },
    {
        "id": "3.09",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "hồi hộp, chuẩn bị cho bước ngoặt phòng thẩm vấn và thỏa thuận",
        "direction_en": "suspenseful, setting the stage for the interrogation and legal deal",
        "direction_ja": "緊張感を高め、司法取引と取調室の転換点へと導く",
        "direction_ko": "긴장감을 고조시키며 취조실과 사법 거래의 전환점으로 이끌듯",
        "sents_vn": [
            "Khi người chồng bị tra tay vào còng số tám, người đàn bà trong ngôi nhà màu hồng không hề lựa chọn việc thú tội chân thành.",
            "Cô ta chọn cách đóng vai một nạn nhân yếu đuối, bị bạo hành và bị giam cầm trong sự sợ hãi suốt nhiều năm.",
            "Một vở kịch thao túng lòng trắc ẩn hoàn hảo bắt đầu được dàn dựng trước mắt các điều tra viên và công tố viên hàng đầu.",
            "Và vở kịch ấy đã dẫn tới một quyết định pháp lý gây chấn động bậc nhất thế kỷ 20.",
            "Chúng ta hãy cùng bước vào Hồi thứ tư để chứng kiến sự sụp đổ của một ảo tưởng tư pháp."
        ],
        "sents_en": [
            "With her husband placed in handcuffs, the woman from the pink house chose anything but genuine confession.",
            "She elected instead to stage the role of a frail, traumatized victim subjugated by relentless domestic terror.",
            "A masterclass in empathy manipulation unfolded before the seasoned eyes of detectives and senior prosecutors.",
            "That calculated performance yielded one of the most controversial legal compromises of the twentieth century.",
            "Join us as we enter Act Four to witness the catastrophic collapse of a judicial illusion."
        ],
        "sents_ja": [
            "夫の手に手錠が嵌められたとき、ピンクの家にいた女は誠実な自白など毛頭選ぶつもりはありませんでした。",
            "彼女が選んだのは、長年にわたる家庭内暴力の恐怖に屈服させられていた哀れな被害者を演じることでした。",
            "同情心を巧みに操る完璧な舞台劇が、歴戦の捜査官と主任検事たちの目前で演じられ始めました。",
            "そしてその計算高い演技こそが、20世紀最大の議論を呼ぶ司法判断を引き起こすことになります。",
            "司法の幻想がいかにして音を立てて崩壊していったのか、第4幕で見届けていきましょう。"
        ],
        "sents_ko": [
            "남편의 손목에 차가운 수갑이 채워졌을 때, 분홍빛 주택의 여인은 결코 진실한 자백의 길을 택하지 않았습니다.",
            "그녀가 선택한 것은 수년간 잔혹한 가정폭력의 공포에 짓눌려 살아온 가련한 피해자의 역할을 연기하는 것이었습니다.",
            "베테랑 수사관들과 고위 검사들의 눈앞에서, 동정심을 교묘히 농락하는 완벽한 심리 연극이 펼쳐지기 시작했습니다.",
            "그리고 그 치밀한 계산은 20세기 사법 역사상 가장 큰 충격을 던져준 사법적 타협으로 이어지게 됩니다.",
            "사법 체계의 환상이 어떻게 참담하게 무너져 내렸는지, 제4막을 통해 그 진실을 목격해 보시겠습니다."
        ]
    },
    {
        "id": "3.10",
        "kind": "BGM",
        "desc_vn": "Một nốt piano trầm buồn ngân vang rồi tắt lịm giữa không gian im ắng.",
        "desc_en": "A solitary sad piano note lingering before decaying into the silence.",
        "desc_ja": "孤独で物悲しいピアノの単音が長く余韻を残し、深い静寂の中へと消え入る。",
        "desc_ko": "외롭고 구슬픈 피아노 외마디 음이 길게 여운을 끌다가 적막 속으로 사라진다."
    },
    {
        "id": "3.11",
        "kind": "LOI",
        "role": "CHUYÊN GIA TÂM LÝ",
        "direction_vn": "đúc kết ngắn gọn, bóc tách tính toan tính trong tâm lý phản bội",
        "direction_en": "succinct, summarizing the cold calculation in criminal betrayal",
        "direction_ja": "簡潔に締めくくり、裏切りの深層に潜む冷徹な計算高さを要約する",
        "direction_ko": "간결하게 매듭지으며 배신 이면에 숨겨진 서늘한 계산성을 요약하듯",
        "sents_vn": [
            "Về mặt hành vi, sự phản bội này không xuất phát từ việc hồi tỉnh lương tri, mà hoàn toàn là một nước cờ bảo toàn bản thân.",
            "Khi buồng cộng hưởng Folie à Deux bị phá vỡ bởi xung đột lợi ích sinh tử, kẻ tiếp sức sẽ không ngần ngại bán đứng kẻ khởi xướng.",
            "Karla Homolka hiểu rằng ai lên tiếng trước với cơ quan công quyền sẽ là người nắm giữ quyền định đoạt số phận.",
            "Đó là bài học cay đắng nhất về bản chất của những kẻ thái nhân cách khi đối diện với sự trừng phạt."
        ],
        "sents_en": [
            "Behaviorally, this betrayal sprang not from a moral awakening, but strictly from ruthless self-preservation.",
            "Once the Folie à Deux echo chamber fractures under mortal self-interest, the secondary partner unhesitatingly sacrifices the instigator.",
            "Karla Homolka understood instinctively that whoever traded information first would control their own legal destiny.",
            "This stands as the ultimate lesson regarding the true nature of psychopathic loyalties when consequences loom."
        ],
        "sents_ja": [
            "行動科学的に見て、この裏切りは良心の目覚めによるものではなく、冷徹な自己保身の計算に過ぎませんでした。",
            "死活問題となる利害の衝突によって感応精神病の共鳴が破綻したとき、従属的パートナーは躊躇なく主導者を売り渡します。",
            "Karla Homolkaは、当局に対して先に情報を差し出した側が自らの法的運命を掌握できることを本能的に理解していました。",
            "これこそが、処罰の危機に直面したサイコパス的連帯の冷徹な本質を示す何よりの教訓なのです。"
        ],
        "sents_ko": [
            "행동과학적 관점에서 볼 때, 이러한 배신은 양심의 각성이 아니라 철저히 계산된 냉혹한 자기보호 본능의 발로였습니다.",
            "생사가 걸린 이해관계의 충돌로 감응성 정신병의 공명실에 균열이 가자, 종속적 파트너는 주동자를 주저 없이 내던졌습니다.",
            "Karla Homolka는 수사 당국에 먼저 입을 여는 쪽이 자신의 법적 운명을 쥐락펴락할 수 있음을 본능적으로 간파했습니다.",
            "이것이야말로 처벌의 위기 앞에서 사이코패스적 연대가 보여주는 서늘한 본질에 대한 가장 뼈아픈 교훈입니다."
        ]
    }
]
