# -*- coding: utf-8 -*-
"""Dữ liệu Hồi 5 Kịch bản Tập 11 (4 ngôn ngữ: VN, EN, JA, KO)."""

ACT5_ELEMENTS = [
    {
        "id": "5.01",
        "kind": "BGM",
        "desc_vn": "Tiếng búa tòa án gõ vang vọng trong không gian phòng xử án trang nghiêm, tiếp sau là tiếng đàn Piano trầm lắng, sâu sắc và đầy tính thức tỉnh.",
        "desc_en": "Solemn courtroom gavel echoing through the hall, followed by deep, resonant reflective piano chords.",
        "desc_ja": "法廷の木槌の音が厳粛に鳴り響き、それに続いて深く澄んだ内省的なピアノの重低音が広がる。",
        "desc_ko": "엄숙한 법정에 울려 퍼지는 법봉 소리에 이어, 깊고 울림 있는 사색적인 피아노 화음이 흐른다."
    },
    {
        "id": "5.02",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "đĩnh đạc, đanh thép công bố phán quyết tư pháp",
        "direction_en": "authoritative, solemn, delivering the judicial verdicts",
        "direction_ja": "重厚かつ厳格な口調で、下された司法判断を告げる",
        "direction_ko": "위엄 있고 단호한 어조로 최종적인 사법 판결을 낭독하며",
        "sents_vn": [
            "Ngày 1 tháng 9 năm 1995, tại Tòa án Cấp cao Ontario, sau một phiên tòa kéo dài rúng động dư luận quốc tế.",
            "Bồi thẩm đoàn chính thức tuyên Paul Bernardo phạm tội Giết người cấp độ một đối với Leslie Mahaffy và Kristen French, cùng hàng loạt tội danh bắt cóc và tấn công nghiêm trọng.",
            "Thẩm phán tuyên phạt Paul Bernardo mức án tù chung thân không ân xá trong ít nhất 25 năm.",
            "Đặc biệt, tòa án đã gắn cho hắn nhãn 'Tội phạm Nguy hiểm' — một chỉ định pháp lý nghiêm khắc bậc nhất của luật hình sự Canada.",
            "Chỉ định này đồng nghĩa với việc hắn sẽ bị giam giữ vô thời hạn trong các trại giam an ninh tối đa như Kingston và Millhaven cho đến ngày qua đời.",
            "Hắn bị tước bỏ mọi cơ hội tái hòa nhập cộng đồng và vĩnh viễn sống sau bức tường thép dày đặc.",
            "Thế nhưng đối với người đàn bà đã đồng lõa tước đoạt sinh mạng của những đứa trẻ, cánh cửa tự do lại hé mở sau đúng một thập kỷ."
        ],
        "sents_en": [
            "On September 1, 1995, inside the Ontario Court of Justice, an exhausting trial that transfixed international observers reached its climax.",
            "The jury officially found Paul Bernardo guilty of first-degree murder in the deaths of Leslie Mahaffy and Kristen French, alongside kidnapping and aggravated assault convictions.",
            "The presiding judge sentenced Bernardo to life imprisonment with no eligibility for parole for a minimum of 25 years.",
            "Crucially, the court designated him a Dangerous Offender — the most stringent judicial classification in Canadian criminal law.",
            "This statutory classification mandated indefinite detention inside maximum-security institutions like Kingston and Millhaven for the remainder of his life.",
            "He was stripped of all future prospects of societal reintegration, doomed to exist permanently behind impenetrable prison walls.",
            "Yet for the woman who actively facilitated the extinguishing of innocent lives, the gates of freedom swung open after merely a single decade."
        ],
        "sents_ja": [
            "1995年9月1日、オンタリオ州上級裁判所において、国際社会を震撼させた長期にわたる裁判が結審を迎えました。",
            "陪審員団は、Leslie MahaffyとKristen Frenchに対する第1級殺人罪、ならびに多数の加重暴行罪においてPaul Bernardoに有罪評決を下しました。",
            "裁判長はBernardoに対し、少なくとも25年間は仮釈放の申請すら認められない無期懲役の判決を言い渡しました。",
            "何より決定的なのは、裁判所が彼をカナダ刑法で最も過酷な指定である『危険犯』に認定したことでした。",
            "この法的指定は、キングストンやミルヘイブンなどの最高警備刑務所において、彼が息を引き取る日まで無期限に拘禁され続けることを意味します。",
            "彼は社会復帰のあらゆる道を完全に断たれ、冷酷な鉄格子の向こう側で生涯を過ごすことが決定づけられました。",
            "しかし、無垢な命を奪うことに進んで手を貸したあの女には、わずか10年余りで自由への扉が開かれようとしていたのです。"
        ],
        "sents_ko": [
            "1995년 9월 1일, 전 세계의 이목이 집중된 가운데 Ontario 주 고등법원에서 열린 치열한 공판이 마침내 종착역에 닿았습니다.",
            "배심원단은 Leslie Mahaffy와 Kristen French에 대한 1급 살인 혐의를 비롯하여 다수의 납치 및 특수폭행 혐의로 Paul Bernardo에게 만장일치 유죄 평결을 내렸습니다.",
            "재판장은 Bernardo에게 최소 25년 동안 가석방 신청 자격조차 주어지지 않는 종신형을 선고했습니다.",
            "가장 결정적인 조치는 법원이 그를 캐나다 형법상 가장 엄격한 법적 분류인 ‘위험한 범죄자’로 지정한 것이었습니다.",
            "이 특별 지정은 그가 Kingston과 Millhaven 같은 최고 등급 보안 교도소에서 생을 마감하는 날까지 무기한 수감되어야 함을 뜻합니다.",
            "그는 사회 복귀의 모든 가능성을 영구히 박탈당한 채 차가운 쇠창살 뒤에 영원히 격리되는 운명을 맞이했습니다.",
            "하지만 어린 생명들을 앗아가는 데 적극적으로 앞장섰던 그 여인에게는, 고작 십여 년 만에 자유의 문이 열리고 있었습니다."
        ]
    },
    {
        "id": "5.03",
        "kind": "NGHI",
        "sec": 1.5,
        "desc_vn": "khoảng lặng kịch tính"
    },
    {
        "id": "5.04",
        "kind": "LOI",
        "role": "ĐIỀU TRA VIÊN",
        "direction_vn": "lạnh lùng, điểm lại di chứng tự do của Karla và cải cách tư pháp lịch sử",
        "direction_en": "clinical, recounting Karla's release and the sweeping institutional reforms",
        "direction_ja": "冷徹にKarlaの釈放後の実態と歴史的司法改革の経緯を総括する",
        "direction_ko": "냉철한 어조로 Karla의 출소 이후와 역사적인 사법 개혁의 성과를 짚으며",
        "sents_vn": [
            "Ngày 4 tháng 7 năm 2005, sau khi chấp hành trọn vẹn 12 năm tù giam, Karla Homolka chính thức bước qua cánh cổng nhà tù ở tuổi 35.",
            "Sự kiện này đã thổi bùng một cơn bão biểu tình và sự phẫn nộ dữ dội trên khắp các đường phố Canada.",
            "Các bậc phụ huynh và gia đình nạn nhân mang theo di ảnh của Leslie Mahaffy và Kristen French, giăng biểu ngữ phản đối sự bất công của thỏa thuận tư pháp.",
            "Để có thể tồn tại, Karla Homolka phải đổi tên thành Leanne Bordelais, trốn chạy sang vùng biển Caribbean rồi quay về một thị trấn nhỏ ở tỉnh Quebec.",
            "Nhưng bất cứ nơi nào dấu vết của cô ta bị phát hiện, làn sóng tẩy chay và phẫn nộ của cộng đồng lại bùng phát mạnh mẽ.",
            "Về mặt pháp lý, vụ án này đã thúc đẩy chính quyền tỉnh Ontario tiến hành hai cuộc điều tra độc lập mang tính lịch sử.",
            "Báo cáo của cựu Thẩm phán Patrick Galligan đã mổ xẻ toàn diện quy trình công tố và những thiếu sót chí mạng trong việc ký kết thỏa thuận nhận tội.",
            "Trong khi đó, Báo cáo mang tính bước ngoặt của Thẩm phán Archie Campbell đã chỉ ra sự tắc nghẽn thông tin giữa các sở cảnh sát, dẫn tới cuộc đại cải tổ hệ thống phân tích liên kết tội phạm bạo lực ViCLAS trên toàn quốc.",
            "Đó là những cải cách tư pháp đắt giá được đánh đổi bằng nỗi đau tột cùng của các gia đình nạn nhân."
        ],
        "sents_en": [
            "On July 4, 2005, having served her complete 12-year sentence, Karla Homolka walked out of federal prison at the age of 35.",
            "Her release ignited a ferocious firestorm of civic protests and public disgust across Canadian streets.",
            "Grieving families and citizens marched holding portraits of Leslie Mahaffy and Kristen French, carrying banners protesting the injustice of the plea bargain.",
            "To survive, Homolka legally adopted the alias Leanne Bordelais, fleeing temporarily to the Caribbean before retreating to a small town in Quebec.",
            "Yet wherever her presence was uncovered, fierce communal boycotts and collective indignation erupted instantly.",
            "Legally, the catastrophic handling of this case prompted the Ontario government to commission two historic independent judicial reviews.",
            "The exhaustive review by former Justice Patrick Galligan analyzed prosecutorial decisions, identifying critical vulnerabilities in executing plea bargains.",
            "Simultaneously, the landmark Campbell Inquiry exposed systemic communication breakdowns among policing agencies, catalyzing a total overhaul of the nationwide ViCLAS violent crime linkage system.",
            "These sweeping institutional reforms were dearly bought through the unbearable agony of devastated families."
        ],
        "sents_ja": [
            "2005年7月4日、12年の刑期を満期で終えたKarla Homolkaは、35歳で連邦刑務所の正門を後にしました。",
            "彼女の釈放は、カナダ全土の路上で猛烈な抗議デモと世論の激しい怒りを瞬く間に燃え上がらせました。",
            "悲嘆に暮れる遺族や市民たちはLeslie MahaffyとKristen Frenchの遺影を掲げ、不公正な司法取引を糾弾する横断幕を掲げて行進しました。",
            "生活を成り立たせるため、HomolkaはLeanne Bordelaisと改名し、カリブ海へ一時逃亡した後にケベック州の小さな町へと身を潜めました。",
            "しかし彼女の正体が発覚するや否や、地域社会からの激しいボイコットと公憤が即座に巻き起こりました。",
            "法制度の観点において、この事件の破綻はオンタリオ州政府に二つの歴史的独立調査委員会の設置を強く促しました。",
            "元判事Patrick Galliganによる調査報告書は検察の意思決定プロセスを徹底検証し、司法取引締結における致命的な脆弱性を浮き彫りにしました。",
            "同時に、Archie Campbell判事による画期的な報告書は警察組織間の情報共有不全を暴き、全国的な凶悪犯罪連携システムViCLASの全面刷新へと繋がりました。",
            "これらの抜本的な制度改革は、被害者遺族たちの耐え難い苦痛と引き換えに得られた極めて重い教訓だったのです。"
        ],
        "sents_ko": [
            "2005년 7월 4일, 12년의 형기를 온전히 채운 Karla Homolka는 35세의 나이에 연방 교도소 정문을 걸어 나왔습니다.",
            "그녀의 출소는 캐나다 전역의 거리에 거센 항의 시위와 대중의 극심한 분노를 다시 한번 폭발시켰습니다.",
            "슬픔에 잠긴 유가족과 시민들은 Leslie Mahaffy와 Kristen French의 영정 사진을 품에 안고, 불공정한 사법 거래를 규탄하는 현수막을 들었습니다.",
            "생존을 위해 Homolka는 Leanne Bordelais라는 가명으로 개명하고 카리브해로 도피했다가 Quebec 주의 외딴 소도시에 정착했습니다.",
            "그러나 그녀의 은신처가 밝혀질 때마다 지역 사회의 격렬한 보이콧과 공공의 분노가 불길처럼 번져나갔습니다.",
            "제도적 관점에서 이 사건의 참담한 실패는 Ontario 주 정부로 하여금 두 차례의 역사적인 독립 사법 조사를 단행하게 만들었습니다.",
            "Patrick Galligan 전 판사의 보고서는 검찰의 기소 및 협상 과정을 전면 해부하며 형량 거래 제도의 치명적 허점을 명백히 지적했습니다.",
            "동시에 Archie Campbell 판사의 기념비적인 조사 보고서는 경찰 기관 간의 정보 단절 문제를 적나라하게 고발하며, 전국 연쇄 강력범죄 분석 시스템인 ViCLAS의 대대적인 혁신을 이끌어냈습니다.",
            "이러한 뼈아픈 제도 개혁은 참혹하게 희생된 유가족들의 형언할 수 없는 고통을 대가로 치르고서야 얻어진 것이었습니다."
        ]
    },
    {
        "id": "5.05",
        "kind": "SFX",
        "desc_vn": "Tiếng lật trang sách báo cáo và tiếng thở dài nặng nề.",
        "desc_en": "Rustle of turning thick official report pages, followed by a heavy, thoughtful sigh.",
        "desc_ja": "分厚い公的報告書の頁がめくられる重い音、続いて深く重々しい思索の溜息。",
        "desc_ko": "두터운 공식 조사 보고서 책장이 넘어가는 무거운 소리, 이어 깊은 탄식의 한숨 소리."
    },
    {
        "id": "5.06",
        "kind": "LOI",
        "role": "CHUYÊN GIA TÂM LÝ",
        "direction_vn": "giọng học thuật sâu sắc, đối chiếu sự sụp đổ cái tôi và mặt nạ nạn nhân",
        "direction_en": "profoundly academic, contrasting narcissistic collapse with deceptive victimhood",
        "direction_ja": "深く学術的な語り口で、自己愛の崩壊と偽りの被害者像を対比する",
        "direction_ko": "깊이 있는 학술적 어조로 자기애적 붕괴와 기만적인 피해자 가면을 대조하며",
        "sents_vn": [
            "Xét trên bình diện tâm lý học, bản án thể xác 12 năm của Karla Homolka có thể đã kết thúc, nhưng bản án tâm lý xã hội thì vĩnh viễn không bao giờ xóa bỏ.",
            "Karla không hề biểu lộ sự ăn năn hối cải chân chính; thái độ của cô ta chỉ là sự tự thương hại bệnh lý và nỗ lực bảo vệ quyền lợi cá nhân đến cùng.",
            "Trong khi đó, Paul Bernardo trong trại giam Millhaven liên tục nộp đơn xin ân xá trong vô vọng, đổ lỗi cho người khác trong một trạng thái sụp đổ cái tôi ái kỷ kéo dài.",
            "Vụ án này để lại một bài học kinh điển cho nhân loại về việc cảnh giác trước những chiếc mặt nạ đạo đức giả.",
            "Chúng ta phải học cách phân định rạch ròi giữa một nạn nhân thực sự chịu tổn thương và một kẻ săn mồi khoác áo nạn nhân để trốn tránh trách nhiệm.",
            "Sự tàn bạo lộ liễu của Paul Bernardo rất dễ nhận diện, nhưng sự nguy hiểm ngụy trang dưới vỏ bọc mong manh của Karla Homolka mới là thứ đánh lừa được cả hệ thống tư pháp tinh vi nhất.",
            "Lòng trắc ẩn là phẩm giá cao quý của con người, nhưng lòng trắc ẩn thiếu sự tỉnh táo sẽ trở thành mảnh đất màu mỡ cho tội ác thao túng.",
            "Kẻ thủ ác luôn biết cách biến chính lòng tốt của cộng đồng thành tấm khiên che chở cho tội lỗi của chúng.",
            "Để bảo vệ bản thân và những người thân yêu, việc nhận diện các tín hiệu cảnh báo đỏ sinh tồn là vô cùng cấp thiết."
        ],
        "sents_en": [
            "From a behavioral perspective, while Homolka's 12-year physical sentence reached its conclusion, her societal psychological verdict is permanent.",
            "Karla never demonstrated authentic moral contrition; her demeanor remained steeped in pathological self-pity and relentless self-interest.",
            "Meanwhile, inside Millhaven Institution, Bernardo files futile parole applications, externalizing blame in a state of protracted narcissistic collapse.",
            "This dark case bequeaths a timeless masterclass in recognizing counterfeit innocence.",
            "We must learn to rigorously differentiate between genuine trauma victims and calculating predators donning the cloak of victimhood to evade justice.",
            "Bernardo's overt aggression was easily identifiable, yet Karla's camouflaged malice behind fragile blonde femininity deceived even supreme judicial minds.",
            "Human empathy is a noble virtue, yet empathy unmoored from discernment becomes fertile soil for psychopathic manipulation.",
            "Predators instinctively weaponize community compassion as an impenetrable shield for their atrocities.",
            "To safeguard ourselves and our loved ones, internalizing pragmatic survival red flags is an urgent necessity."
        ],
        "sents_ja": [
            "行動心理学の視座に立てば、Homolkaの12年の肉体的刑期は終了したものの、社会的な心理的判決は決して消滅しません。",
            "Karlaは真摯な道徳的悔悟を示したことは一度もなく、その態度は病的な自己憐憫と執拗な自己保身に終始していました。",
            "一方、ミルヘイブン刑務所内のBernardoは無駄な仮釈放申請を繰り返し、他者に責任を転嫁しながら長期の自己愛崩壊状態を彷徨っています。",
            "この事件は、偽りの無垢を見抜くための永遠の教訓を人類に残しました。",
            "私たちは、真のトラウマ被害者と、法の裁きから逃れるために被害者の衣を纏う狡猾な捕食者とを冷徹に見分ける術を学ばねばなりません。",
            "Bernardoの露骨な凶暴性は容易に識別できましたが、Karlaの脆く美しい外見の裏に潜む悪意こそが最高位の司法頭脳さえ欺いたのです。",
            "共感は人間の気高い美徳ですが、知性を伴わない共感はサイコパスによる心理操作の格好の温床となってしまいます。",
            "捕食者たちは、地域社会の善意そのものを自らの悪行を隠す無敵の盾として本能的に悪用するのです。",
            "自らと愛する人々を守り抜くため、生存のためのレッドフラッグを体得することは焦眉の課題です。"
        ],
        "sents_ko": [
            "행동심리학적 관점에서 볼 때, Karla Homolka의 12년 수감 생활은 끝났을지 몰라도 사회적인 심리적 단죄는 영원히 지워지지 않습니다.",
            "Karla는 진정한 도덕적 참회의 눈물을 흘린 적이 없으며, 그녀의 모든 태도는 병적인 자기연민과 집요한 이기심으로 점철되어 있었습니다.",
            "한편 Millhaven 교도소의 Paul Bernardo는 부질없는 가석방 신청을 거듭하며 남 탓만 일삼는 만성적인 자기애적 붕괴 상태에 갇혀 있습니다.",
            "이 참혹한 사건은 날조된 순진함을 가려내기 위한 영원한 교훈을 우리에게 남겼습니다.",
            "우리는 고통받는 진짜 피해자와, 사법적 책임을 피하고자 피해자의 탈을 쓴 교활한 포식자를 명확히 구별해 낼 줄 알아야 합니다.",
            "Paul Bernardo의 노골적인 흉포함은 식별하기 쉬웠지만, Karla Homolka의 가련한 금발 외모 뒤에 감춰진 악의야말로 일류 사법 두뇌들까지 감쪽같이 속였습니다.",
            "인간의 연민은 숭고한 미덕이지만, 분별력이 결여된 맹목적인 연민은 사이코패스의 심리 조작을 위한 가장 비옥한 토양이 됩니다.",
            "포식자들은 공동체의 선의 자체를 자신의 만행을 가리는 난공불락의 방패로 본능적으로 무기화합니다.",
            "스스로와 소중한 사람들을 지켜내기 위해, 실천적인 생존의 적신호들을 마음 깊이 새기는 것은 더없이 시급한 과제입니다."
        ]
    },
    {
        "id": "5.07",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "đĩnh đạc, phân tích 4 cảnh báo đỏ sinh tồn The Gift of Fear",
        "direction_en": "authoritative, delivering the 4 pragmatic survival red flags",
        "direction_ja": "重厚かつ説得力に満ちた口調で、生存のための4つのレッドフラッグを説く",
        "direction_ko": "차분하고 설득력 있는 어조로 생존을 위한 4가지 적신호를 제시하며",
        "sents_vn": [
            "Để giúp quý vị khán giả có thêm những công cụ bảo vệ thực tế, kênh Amber Eyes xin đúc kết 4 tín hiệu cảnh báo đỏ sinh tồn từ hồ sơ lịch sử này.",
            "* Cảnh báo đỏ thứ nhất: Cảnh giác trước kẻ lạm dụng sự tổn thương cá nhân.",
            "Những kẻ thao túng luôn nhắc về những vết thương hay bất hạnh trong quá khứ để biện minh cho hành vi sai trái ở hiện tại; người thực sự có lương tri sẽ nhận trách nhiệm và xót thương nạn nhân, thay vì chỉ chăm chăm đóng vai người bị hại.",
            "* Cảnh báo đỏ thứ hai: Sự bất nhất giữa lời nói đạo đức và hành vi sau lưng.",
            "Hãy luôn đánh giá một con người dựa trên chuỗi hành động thực tế, không dựa vào vẻ bề ngoài xinh đẹp hay những lời nói hoa mỹ trước đám đông.",
            "* Cảnh báo đỏ thứ ba: Cảnh giác trước sự tiếp cận của những người có vẻ ngoài vô hại.",
            "Karla Homolka đã trực tiếp dùng nụ cười thân thiện để hỏi đường và dụ dỗ nạn nhân vào bẫy; sự cảnh giác không được phép lơ là trước bất kỳ ai ở nơi công cộng.",
            "* Và cảnh báo đỏ thứ tư: Nhận diện những mối quan hệ cộng sinh độc hại.",
            "Một tình cảm chân chính không bao giờ đòi hỏi bạn phải xâm phạm ranh giới đạo đức hay làm hại người khác để chứng minh sự gắn kết.",
            "Khi ai đó yêu cầu bạn bước qua lằn ranh lương tâm nhân danh lòng trung thành, đó không phải là tình yêu mà là chiếc thòng lọng dẫn xuống vực thẳm.",
            "Hãy luôn lắng nghe trực giác bất an bên trong bạn, bởi trực giác chính là chiếc chuông báo động sớm nhạy bén nhất.",
            "Đừng bao giờ hợp lý hóa hay bỏ qua những bước lấn ranh giới nhỏ nhặt ban đầu."
        ],
        "sents_en": [
            "To equip our audience with pragmatic protective insights, Amber Eyes distills 4 critical survival red flags from this historical file.",
            "* Red Flag One: Beware those who weaponize personal trauma.",
            "Manipulators incessantly cite past grievances to justify present misconduct; genuine conscience embraces accountability and grieves for victims rather than fixating on performing victimhood.",
            "* Red Flag Two: The stark dissonance between moral rhetoric and private behavior.",
            "Consistently evaluate individuals based on their objective patterns of conduct rather than charming aesthetics or eloquent public pronouncements.",
            "* Red Flag Three: Exercise caution when approached by seemingly harmless figures.",
            "Karla Homolka utilized an innocent, friendly smile to ask for directions and lure unsuspecting victims; vigilance must never falter before disarming personas in public spaces.",
            "* And Red Flag Four: Recognize toxic codependent alliances.",
            "True love never demands the violation of moral boundaries or inflicting harm upon others as proof of devotion.",
            "When someone urges you to compromise conscience in the name of loyalty, that is not love — it is a psychological noose dragging you into the abyss.",
            "Always honor your intuitive discomfort, for intuition remains our most acute early-warning survival system.",
            "Never rationalize or dismiss seemingly minor early boundary transgressions."
        ],
        "sents_ja": [
            "視聴者の皆様に実践的な自衛の知見をお届けするため、Amber Eyesはこの歴史的事件から4つの決定的な『4つの赤い警告』を抽出します。",
            "* 第1の赤い警告：過去の傷を武器にする者に警戒せよ。",
            "心理操作者は過去の不遇を執拗に持ち出して現在の不正を正当化しますが、本物の良心を持つ者は責任を引き受け被害者を悼むものであり、被害者面を演じることに固執はしません。",
            "* 第2の赤い警告：道徳的言説と陰の行動との乖離。",
            "美しい外見や大衆の前での耳触りの良い弁舌ではなく、一貫した客観的な行動の軌跡によって人物を評価してください。",
            "* 第3の赤い警告：無害に見える人物の接近に油断するな。",
            "Karla Homolkaは道を聞くふりをして親しみやすい笑顔を浮かべ警戒を解いた被害者を罠へと誘い込みましたから、公共の場において無垢に見える人物の前でも警戒心を解いてはなりません。",
            "* そして第4の赤い警告：有害な共依存同盟を見抜け。",
            "真の愛情が、絆の証明として倫理の境界を侵犯することや他者を傷つけることを要求することは決してありません。",
            "誰かが忠誠の名の下に良心の妥協を迫るとき、それは愛ではなく、あなたを破滅の深淵へと引きずり込む首絞めの縄なのです。",
            "自らの内なる直感的な違和感を常に尊重してください、直感こそが最も鋭敏な早期生存警報システムなのですから。",
            "一見些細に見える初期の境界侵害を決して正当化したり見過ごしたりしてはなりません。"
        ],
        "sents_ko": [
            "시청자 여러분께 실질적인 자기보호의 통찰을 전해드리고자, Amber Eyes는 이 역사적 파일에서 4가지 결정적인 생존 적신호를 도출합니다.",
            "* 첫 번째 적신호: 개인적 상처를 무기화하는 자를 경계하라.",
            "조작자들은 끊임없이 과거의 불행을 들먹이며 현재의 잘못을 정당화하지만, 참된 양심을 지닌 자는 책임을 인정하고 피해자를 애도할 뿐 피해자 행세에 매달리지 않습니다.",
            "* 두 번째 적신호: 도덕적 수사와 이면 행동 간의 극심한 괴리.",
            "화려한 외모나 대중 앞에서의 번지르르한 말솜씨가 아니라, 오직 지속적이고 객관적인 행동의 패턴으로 상대를 평가하십시오.",
            "* 세 번째 적신호: 무해해 보이는 사람의 접근을 결코 방심하지 마라.",
            "Karla Homolka는 길을 묻는 친절한 미소로 접근하여 방심한 피해자들을 덫으로 유인했으니, 공공장소에서 겉보기에 무해해 보이는 인물 앞에서도 직관적 경계를 늦추어서는 안 됩니다.",
            "* 그리고 네 번째 적신호: 유해한 공생적 결속을 경계하라.",
            "진실한 사랑은 결코 애정의 증거로서 윤리적 금기를 위반하거나 타인에게 해를 끼칠 것을 요구하지 않습니다.",
            "누군가가 충성이라는 미명 아래 양심의 타협을 강요할 때, 그것은 사랑이 아니라 당신을 파멸의 심연으로 끌고 들어가는 올가미입니다.",
            "내면에서 울리는 불길한 직관의 목소리에 항상 귀를 기울이십시오, 직관이야말로 우리 내면의 가장 예리한 조기 생존 경보 시스템입니다.",
            "사소해 보이는 초기 경계 침해 행위를 결코 대수롭지 않게 넘기거나 합리화하지 마십시오."
        ]
    },
    {
        "id": "5.08",
        "kind": "NGHI",
        "sec": 1.5,
        "desc_vn": "khoảng lặng kịch tính"
    },
    {
        "id": "5.09",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "trầm ấm, truyền cảm, khép lại tập podcast với thông điệp nhân văn",
        "direction_en": "warm, resonant, closing the podcast with philosophical closure",
        "direction_ja": "温かく深い余韻を湛えた声で、人道的メッセージと共に番組を締めくくる",
        "direction_ko": "따뜻하고 깊은 울림을 담아, 인간적인 메시지와 함께 프로그램을 마무리하며",
        "sents_vn": [
            "Hồ sơ Paul Bernardo và Karla Homolka khép lại như một hồi chuông cảnh tỉnh lạnh lùng về những góc khuất khôn lường của tâm trí con người.",
            "Chiếc mặt nạ búp bê 'Ken và Barbie' lộng lẫy đã vỡ vụn, để lại bài học đau xót về cái giá của sự ngộ nhận và lòng trắc ẩn bị đặt sai chỗ.",
            "Dù thỏa thuận tư pháp có những giới hạn của thời đại, nhưng ánh sáng của lương tri lịch sử đã trả lại phẩm giá cho các nạn nhân vô tội và vạch trần chân tướng của tội ác.",
            "Xin hãy luôn nhớ rằng: sự an toàn của chúng ta bắt đầu từ việc biết tôn trọng trực giác và dũng cảm bảo vệ những ranh giới đạo đức sống còn.",
            "Cảm ơn các khách mời chuyên gia đã đồng hành cùng Amber Eyes trong ca phẫu thuật tâm lý học đầy kịch tính hôm nay.",
            "Cảm ơn quý vị khán giả đã lắng nghe và chia sẻ thông điệp thức tỉnh này.",
            "Hãy bấm đăng ký kênh và để lại góc nhìn của bạn ở phần bình luận bên dưới.",
            "Xin chào và hẹn gặp lại quý vị trong những tập hồ sơ tiếp theo.",
            "Chúc quý vị luôn giữ được sự an yên và sáng suốt trong cuộc sống."
        ],
        "sents_en": [
            "The file of Paul Bernardo and Karla Homolka closes as an unsparing reminder of the unfathomable abysses within human psychology.",
            "The dazzling Ken and Barbie doll facade has shattered irrevocably, leaving a harrowing lesson on the perils of delusion and misplaced empathy.",
            "Though flawed legal bargains reflected the limitations of an era, the clarity of historical conscience restored dignity to innocent victims and exposed predatory truth.",
            "Please always remember: our survival begins with honoring our instincts and bravely defending our vital ethical boundaries.",
            "We extend our gratitude to our esteemed expert guests for navigating this intense behavioral exploration alongside Amber Eyes today.",
            "Thank you to our viewers for listening closely and reflecting upon this essential message.",
            "Please subscribe to the channel and share your perspectives in the comments section below.",
            "Until our next investigation, we bid you farewell.",
            "May you always remain safe, vigilant, and at peace."
        ],
        "sents_ja": [
            "Paul BernardoとKarla Homolkaの記録は、人間の深層心理に横たわる測り知れない暗黒についての容赦なき警鐘として幕を閉じます。",
            "絢爛たる『ケンとバービー』人形の仮面は無残に粉砕され、盲信と見誤った同情がもたらす悲痛な代償を私たちに残しました。",
            "不完全な司法取引が一時代の限界を露呈したとしても、歴史の確かな良識は無辜の被害者たちに尊厳を取り戻し、捕食者の実態を白日の下に晒しました。",
            "どうか心に留めておいてください、私たちの安全は直感を尊重し生命線の倫理的境界を勇敢に守ることから始まるのだということを。",
            "本日Amber Eyesと共にこの濃密な深層心理の解剖に立ち会ってくださった専門家ゲストの皆様に心より感謝申し上げます。",
            "この切実な覚醒のメッセージに耳を傾け、思索を共にしてくださった視聴者の皆様、誠にありがとうございました。",
            "ぜひチャンネル登録の上、下のコメント欄で皆様のご意見や考察をお聞かせください。",
            "次回のプロファイルでお会いする日まで、しばしのお別れです。",
            "皆様が常に安全で、警戒を怠らず、平穏な日々を過ごされることを心より願っております。"
        ],
        "sents_ko": [
            "Paul Bernardo와 Karla Homolka의 파일은 인간 내면의 헤아릴 수 없는 어둠에 관한 냉철한 경종을 울리며 막을 내립니다.",
            "화려했던 ‘켄과 바비’ 인형의 가면은 산산조각 났으며, 맹목적인 믿음과 잘못 놓인 연민이 치러야 했던 뼈아픈 대가를 우리에게 남겼습니다.",
            "비록 불완전한 사법 거래가 한 시대의 한계를 드러냈을지라도, 역사의 명철한 양심은 무고한 피해자들의 존엄을 온전히 회복시키고 포식자의 실체를 단죄했습니다.",
            "부디 기억해 주십시오, 우리의 안전은 자신의 직관을 신뢰하고 생존의 윤리적 경계선을 용기 있게 지켜내는 것에서 시작된다는 사실을 말입니다.",
            "오늘 Amber Eyes와 함께 이 치열한 심리 부검의 여정에 동행해 주신 전문가 패널 여러분께 깊은 감사를 드립니다.",
            "이 엄중한 각성의 메시지에 귀 기울여 주시고 함께 고민해 주신 시청자 여러분께 진심으로 감사드립니다.",
            "채널 구독 버튼을 눌러주시고, 아래 댓글을 통해 여러분의 소중한 견해를 들려주시기 바랍니다.",
            "다음 프로파일 분석 파일에서 다시 인사드릴 때까지 안녕히 계십시오.",
            "늘 안전하고 평온한 일상이 함께하시기를 진심으로 기원합니다."
        ]
    },
    {
        "id": "5.10",
        "kind": "SFX",
        "desc_vn": "Tiếng đóng tập hồ sơ vụ án vang lên tiếng cạch dứt khoát, theo sau là tiếng tắt máy ghi âm.",
        "desc_en": "Decisive latch of a heavy case binder clicking shut, followed by the soft click of an audio recorder powering off.",
        "desc_ja": "重厚な事件記録ファイルが断固として閉じられる乾いた音、続いて録音機の電源が切れる微かなクリック音。",
        "desc_ko": "묵직한 수사 서류철이 단호하게 닫히는 경쾌한 소리, 이어 녹음기 전원이 꺼지는 나직한 딸깍 소리."
    },
    {
        "id": "5.11",
        "kind": "BGM",
        "desc_vn": "Nhạc Piano trầm buồn ngân vang 5 giây rồi từ từ nhỏ dần và tắt hẳn.",
        "desc_en": "Melancholic piano chords resonating for 5 seconds before gently fading out completely.",
        "desc_ja": "哀愁を帯びたピアノの和音が5秒間響き渡り、やがて緩やかにフェードアウトして消え去る。",
        "desc_ko": "애수 어린 피아노 화음이 5초 동안 은은하게 울려 퍼진 뒤 서서히 페이드아웃되며 완전히 잦아든다."
    }
]
