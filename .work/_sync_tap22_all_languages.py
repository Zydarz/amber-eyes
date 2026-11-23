# -*- coding: utf-8 -*-
"""Synchronize Episode 22 across all 4 languages (VN, EN, JA, KO) to exact 248 sentences.
Uses structured block-based expansion so no sentences are lost or misaligned.
"""

import sys
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# 10 Expansion blocks
ADDITIONS_ORDER = [
    (3, "1.07", 4),
    (5, "1.10", 4),
    (9, "2.06", 4),
    (12, "2.10", 4),
    (14, "3.03", 4),
    (18, "3.07", 4),
    (22, "4.06", 4),
    (26, "4.11", 4),
    (29, "5.03", 2),
    (30, "5.04", 2),
]

ADDITIONS = {
    3: {
        "VN": [
            "Sau buổi sáng định mệnh ấy, một nỗi hoang mang vô hình bao trùm khắp các dãy nhà liền kề yên tĩnh của khu phố chúng tôi.",
            "Người ta bắt đầu nhìn nhau với ánh mắt dè chừng, tự hỏi liệu phía sau những nụ cười chào hỏi lịch thiệp mỗi sớm mai là những bí mật đen tối nào đang được che giấu.",
            "Ảo tưởng về một vùng ngoại ô an toàn tuyệt đối đã hoàn toàn vỡ vụn khi chúng tôi nhận ra ranh giới giữa một tổ ấm hạnh phúc và một hiện trường án mạng đôi khi chỉ mong manh như một sợi tóc.",
            "Nỗi đau đớn lớn nhất của cộng đồng không chỉ là sự xuất hiện của tội ác, mà là sự sụp đổ cay đắng của niềm tin vào sự lương thiện của những người sống ngay cạnh mình.",
        ],
        "EN": [
            "Following that fateful morning, an insidious unease quietly settled over the peaceful townhouses of our quiet suburban neighborhood.",
            "Residents began exchanging guarded glances, silently wondering what dark, unfathomable secrets might lurk behind the polite morning smiles of those living right beside them.",
            "The comforting illusion of an impregnable suburban sanctuary was utterly shattered when we realized that the boundary between a loving home and a chilling crime scene is sometimes razor-thin.",
            "The deepest ache haunting our community was not merely the sudden intrusion of evil, but the devastating collapse of fundamental trust in the decency of our neighbors.",
        ],
        "JA": [
            "あの運命の朝を境に、私たちの平穏だった新興住宅街の家々の間に、目に見えない不穏な動揺が静かに広がっていきました。",
            "毎朝交わされる礼儀正しい挨拶や笑顔の裏に、どれほど暗く恐ろしい秘密が隠されているのだろうかと、誰もが互いを警戒の目で見つめ直すようになったのです。",
            "安全で平和な郊外生活という心地よい幻想は音を立てて崩れ去り、温かい家庭と凄惨な犯行現場の境界線がいかに紙一重であるかを思い知らされました。",
            "地域社会を最も深く苛んだのは、突如現れた悪意そのもの以上に、すぐ隣に暮らす人間の善意に対する根本的な信頼が残酷にも打ち砕かれたことでした。",
        ],
        "KO": [
            "그 운명적인 아침 이후, 우리 평화로운 타운하우스 단지 전체에 눈에 보이지 않는 불안감이 무겁게 내려앉았습니다.",
            "주민들은 아침마다 나누던 다정한 인사 뒤에 얼마나 어둡고 끔찍한 비밀이 숨겨져 있을지 서로를 경계의 눈빛으로 바라보기 시작했습니다.",
            "완벽하게 안전한 교외 지역이라는 안락한 환상은 산산이 부서졌고, 따뜻한 보금자리와 살인 사건 현장의 경계가 얼마나 종이 한 장 차이인지 뼈저리게 깨달았습니다.",
            "지역 공동체를 가장 아프게 괴롭힌 것은 악의의 침입 그 자체보다 바로 옆집에 살던 이웃의 선의에 대한 근본적인 신뢰가 무너져 내린 것이었습니다.",
        ],
    },
    5: {
        "VN": [
            "Dưới góc độ tâm lý học điều tra, màn kịch gục khóc của đối tượng tại hiện trường là một ví dụ kinh điển về nỗi đau mang tính trình diễn nhằm thao túng sự chú ý của công chúng.",
            "Ả tin rằng việc phóng đại cảm xúc và bám víu vào sự hiện diện của lực lượng chức năng sẽ tạo nên một bức tường phòng thủ tâm lý vững chắc che đậy dã tâm bên trong.",
            "Thế nhưng những cử chỉ lau mắt ráo hoảnh và sự thiếu hụt các biến đổi sinh lý thực sự như nhịp thở ngắt quãng hay sự tái nhợt của làn da đã không thể qua mặt được các điều tra viên dày dạn kinh nghiệm.",
            "Cái bẫy nghiệp vụ được giăng ra không chỉ để thu thập chứng cứ vật chất, mà còn để đối tượng tự bộc lộ trọn vẹn bản chất giả tạo của mình trước pháp luật.",
        ],
        "EN": [
            "From an investigative behavioral standpoint, the suspect's theatrical collapse at the perimeter was a textbook manifestation of performative grief designed to manipulate public perception.",
            "She genuinely believed that exaggerating her emotional display and clinging to responding officers would construct an impenetrable psychological fortress concealing her sinister intent.",
            "Yet her tearless dabbing of dry eyes and the conspicuous absence of authentic physiological distress—such as choked breathing or sudden pallor—could not deceive seasoned investigators.",
            "Our sting operation was meticulously engineered not merely to secure physical evidence, but to compel the suspect to fully expose her fraudulent nature before the eyes of justice.",
        ],
        "JA": [
            "捜査行動科学の観点から見れば、現場の規制線で見せた被疑者の過剰な泣き崩れは、周囲の視線を欺くために計算された「演じられた悲嘆」の典型例でした。",
            "彼女は感情を誇張して警戒にあたる警察官にしがみつくことで、自らの邪悪な企みを隠蔽する強固な心理的防壁を築けると信じ込んでいたのです。",
            "しかし、涙の流れていない乾いた目を拭う仕草や、過呼吸や顔面の蒼白といった本物の心理的動揺に伴う自律神経反応の欠如は、熟練の捜査官の目を決して欺くことはできませんでした。",
            "このおとり捜査は単なる物的証拠の保全にとどまらず、被疑者自らの手でその虚飾と欺瞞の仮面を剥ぎ取らせるために完璧に仕掛けられた心理的な罠だったのです。",
        ],
        "KO": [
            "수사 행동과학의 관점에서 현장 통제선에서 피의자가 보여준 오열 연기는 대중의 시선을 조작하기 위해 고안된 '연출된 슬픔'의 전형적인 사례였습니다.",
            "그녀는 감정을 극대화하고 출동한 경찰관에게 매달림으로써 자신의 흉악한 본심을 은폐할 수 있는 난공불락의 심리적 방어벽을 구축할 수 있다고 믿었습니다.",
            "그러나 눈물 한 방울 흐르지 않는 메마른 눈을 닦아내는 동작과 호흡 곤란이나 안색 창백 같은 진정한 자율신경계 반응의 결여는 베테랑 형사들의 눈을 속일 수 없었습니다.",
            "우리의 함정 수사는 단순히 물리적 증거를 확보하기 위한 것뿐만 아니라 피의자 스스로 그 위선과 거짓의 가면을 벗어던지도록 유도하기 위해 정밀하게 설계된 심리전이었습니다.",
        ],
    },
    9: {
        "VN": [
            "Khoảnh khắc ả bình thản ngồi trong xe hơi để mặc cả giá tiền tước đoạt sinh mạng của chồng đã phơi bày một sự tha hóa hoàn toàn về mặt nhân tính.",
            "Ả không chỉ đòi hỏi kết quả cuối cùng, mà còn muốn kiểm soát từng chi tiết nhỏ nhất từ góc bắn cho đến việc tạo hiện trường giả để bảo đảm bản thân không phải chịu bất kỳ rủi ro nào.",
            "Sự háo hức lộ rõ trong ánh mắt khi nói về cái chết của người đàn ông từng chung chăn gối là biểu hiện rõ nét nhất của sự thỏa mãn quyền lực ở một nhân cách chống đối xã hội.",
            "Đó là bằng chứng thép khẳng định rằng hành vi này hoàn toàn không có chỗ cho sự trắc ẩn hay bất kỳ xung đột lương tâm nào.",
        ],
        "EN": [
            "The chilling composure with which she sat inside that vehicle bargaining over the price of her husband's life laid bare an absolute moral degradation.",
            "She did not merely demand the ultimate fatal outcome, but insisted on dictating every meticulous detail—from firing angles to staging a mock burglary—to ensure she bore zero personal risk.",
            "The unmistakable gleam of anticipation in her eyes as she contemplated the demise of her lawful spouse was the quintessential hallmark of power arousal in an antisocial personality.",
            "This stood as irrefutable proof that her murderous undertaking harbored no trace of compassion, nor the slightest flicker of inner moral conflict.",
        ],
        "JA": [
            "夫の命の値段を値踏みしながら車内で平然と交渉を進める彼女の冷酷な態度は、人間性の完全な喪失を白日の下に晒していました。",
            "単に標的の排除を要求するだけでなく、自身のリスクを完全にゼロにするため、銃撃の角度から強盗偽装の細部に至るまで自ら執拗に指図しようとしたのです。",
            "かつて愛を誓った配偶者の死を目前にしてその瞳に浮かんだ露骨な高揚感は、反社会的人格特有の「支配権力の充足感」を何よりも雄弁に物語っていました。",
            "これこそが、彼女の冷血な謀略の中にいささかの良心の呵責も、人間的な慈悲の欠片も存在しなかったことを証明する動かぬ鉄証となったのです。",
        ],
        "KO": [
            "차 안에 태연하게 앉아 남편 목숨의 대가를 흥정하던 그녀의 섬뜩한 태도는 인간성의 완전한 파탄을 적나라하게 보여주었습니다.",
            "그녀는 단지 최종적인 살해 결과만을 요구한 것이 아니라, 자신의 위험을 완전히 배제하기 위해 총격 각도부터 강도 위장 수법까지 세세하게 지시하고자 했습니다.",
            "합법적인 배우자의 죽음을 이야기하며 그녀의 눈빛에 스쳐 지나간 노골적인 흥분감은 반사회적 성격장애 특유의 '통제 권력의 충족감'을 여실히 드러냈습니다.",
            "이것이야말로 그녀의 살인 모의 과정에 그 어떤 동정심이나 내면의 도덕적 갈등조차 전혀 존재하지 않았음을 증명하는 결정적 증거였습니다.",
        ],
    },
    12: {
        "VN": [
            "Khoảnh khắc Michael Dippolito lùi bước và dứt khoát từ chối cái ôm giả tạo ấy là một trong những giây phút bi kịch và chân thực nhất của bản năng con người.",
            "Trong tích tắc định mệnh đó, toàn bộ tình yêu thương, sự trân trọng và niềm tin mà anh từng gửi gắm vào cuộc hôn nhân sáu tháng đã vỡ vụn thành trăm mảnh.",
            "Nỗi đau đớn bị phản bội bởi chính người mà mình từng muốn dùng cả phần đời còn lại để che chở là một vết thương tâm lý sâu sắc không lời nào có thể diễn tả.",
            "Cái lùi bước dứt khoát ấy không chỉ là sự tự vệ thể xác, mà là lời tuyên bố đoạn tuyệt vĩnh viễn với chiếc bẫy tình cảm độc hại đã suýt chôn vùi sinh mạng của anh.",
        ],
        "EN": [
            "The moment Michael Dippolito recoiled and decisively rejected that manipulative embrace remains one of the most tragic, raw manifestations of human survival instinct.",
            "In that singular, devastating instant, all the profound devotion, cherish, and earnest faith he had poured into their six-month marriage shattered into a thousand irrecoverable pieces.",
            "The agonizing trauma of being targeted for destruction by the very soul he had pledged to protect for the rest of his days inflicted an emotional wound beyond the reach of words.",
            "That resolute backward step was not merely physical self-defense, but an absolute psychological severance from the toxic emotional snare that had nearly cost him his life.",
        ],
        "JA": [
            "マイケル・ディッポリトが身を引いてその偽りの抱擁を毅然と拒絶した瞬間は、人間の生存本能が露わになった最も痛切で劇的な光景でした。",
            "その運命の一瞬において、わずか六か月の結婚生活に注ぎ込んできた深い愛情、献身、そして純粋な信頼のすべてが無惨にも粉々に打ち砕かれたのです。",
            "残された生涯をかけて守り抜くと誓った最愛のパートナーによって自らの命が狙われていたという耐えがたい裏切りのトラウマは、言葉では到底言い尽くせない魂の深傷となりました。",
            "あの一歩後退した拒絶の動作は、単なる肉体的な自己防衛にとどまらず、自らの命を奪い去ろうとした邪悪な愛憎の罠に対する魂の完全な決別宣言だったのです。",
        ],
        "KO": [
            "마이클 디폴리토가 뒷걸음질 치며 그녀의 거짓된 포옹을 단호하게 거부한 순간은 인간의 생존 본능이 드러난 가장 비극적이고 진실한 순간이었습니다.",
            "그 짧은 순간, 6개월의 결혼 생활 동안 쏟아부었던 모든 사랑과 헌신, 순수한 신뢰가 회복할 수 없는 수천 개의 조각으로 산산이 부서졌습니다.",
            "평생을 바쳐 지키겠다고 맹세했던 배우자가 자신의 목숨을 앗아가려 했다는 참혹한 배신의 상흔은 말로 다 표현할 수 없는 영혼의 깊은 상처가 되었습니다.",
            "그 단호한 뒷걸음질은 단순한 신체적 방어를 넘어 자신의 목숨을 앗아갈 뻔했던 유독한 감정의 덫과의 완전한 결별 선언이었습니다.",
        ],
    },
    14: {
        "VN": [
            "Dưới lăng kính tâm lý học tiến hóa, hành vi của Dalia phản ánh một chiến lược ký sinh xã hội mang tính hủy diệt cao độ.",
            "Ả khéo léo biến những mặc cảm về quá khứ lầm lỡ của Michael thành một đòn bẩy tâm lý để cô lập anh khỏi các mối quan hệ hỗ trợ xung quanh.",
            "Bằng cách liên tục gieo rắc sự bất an và đòi hỏi những cam kết vật chất vội vã, ả từng bước tước đoạt quyền tự chủ tài chính của người bạn đời một cách êm ái.",
            "Khi toàn bộ quyền lợi đã được chuyển giao vào tay mình, nạn nhân lập tức mất đi giá trị sử dụng và bị đưa vào danh sách cần phải thanh lý không thương tiếc.",
        ],
        "EN": [
            "Through the lens of evolutionary psychology, Dalia's calculated maneuvers exemplified a highly destructive form of predatory social parasitism.",
            "She skillfully exploited Michael's vulnerabilities surrounding his past legal mistakes, transforming his desire for redemption into psychological leverage to isolate him from supportive networks.",
            "By systematically cultivating insecurity while relentlessly demanding premature material commitments, she progressively stripped her partner of financial autonomy without raising alarm.",
            "The moment all critical assets were successfully transferred into her legal possession, the victim instantly lost all perceived utility and was coldly slated for merciless disposal.",
        ],
        "JA": [
            "進化心理学の観点から分析すれば、ダリアの取った一連の行動は極めて破壊的な「捕食的社会寄生戦略」そのものでした。",
            "彼女はマイケルの過去の過ちに対する罪悪感や更生への渇望を巧みに利用し、彼を周囲の支援ネットワークから孤立させる心理的梃子へと変えていったのです。",
            "精神的な不安を執拗に植え付けながら性急な財産譲渡を要求し続けることで、配偶者の経済的自立権を誰にも気づかれずに段階的に奪い去っていきました。",
            "そして不動産を含むすべての権利が法的に自らの手中に収まった瞬間、被害者は利用価値を完全に失い、冷酷にも「速やかに処分すべき障害物」へと格下げされたのです。",
        ],
        "KO": [
            "진화심리학의 렌즈를 통해 분석하면 달리아의 치밀한 행태는 극도로 파괴적인 '포식적 사회 기생 전략'을 그대로 보여줍니다.",
            "그녀는 과거의 법적 과오로 인한 마이클의 죄책감과 갱생에 대한 열망을 교묘히 악용하여 그를 주변 지지망으로부터 고립시키는 심리적 지렛대로 삼았습니다.",
            "체계적으로 불안감을 조성하는 동시에 성급한 물질적 헌신을 집요하게 요구함으로써 배우자의 재정적 자율성을 아무런 의심 없이 차근차근 박탈해 나갔습니다.",
            "모든 핵심 부동산과 권리가 법적으로 자신의 손에 넘어가자마자 피해자는 이용 가치를 완전히 상실하고 무자비하게 청산되어야 할 장애물로 전락했습니다.",
        ],
    },
    18: {
        "VN": [
            "Một lát cắt tâm lý đầy trăn trở trong hồ sơ này là sự chối bỏ nhận thức mang tính phòng vệ cực đoan từ chính người mẹ của kẻ thủ ác.",
            "Đối diện với sự thật kinh hoàng về đứa con gái mình hết mực yêu thương, người mẹ đã chọn cách phong tỏa nhận thức để bảo vệ cái tôi khỏi sự sụp đổ danh dự.",
            "Bà bám víu vào những giả thuyết hoang đường về việc con mình chỉ là nạn nhân của một cái bẫy truyền thông do cảnh sát và đoàn làm phim dàn dựng.",
            "Sự chối bỏ mù quáng của tình mẫu tử tuy là một phản xạ tâm lý dễ hiểu, nhưng vô tình lại trở thành một mảnh ghép dung dưỡng cho sự trơ trẽn của kẻ phạm tội.",
        ],
        "EN": [
            "A deeply poignant psychological facet of this case lies in the extreme defensive denial exhibited by the perpetrator's own biological mother.",
            "Confronted with the horrifying reality of the daughter she had tenderly raised, the mother chose cognitive compartmentalization to shield her ego from catastrophic dishonor.",
            "She clung desperately to outlandish conspiracy theories, insisting her daughter was merely an innocent casualty framed by an aggressive reality television production and overzealous police.",
            "While such blind maternal denial is an understandable psychological defense mechanism, it inadvertently became an enabling shelter fueling the perpetrator's complete lack of remorse.",
        ],
        "JA": [
            "この事件における極めて痛切な心理的一面は、犯人の実母が見せた極限状態の「自己防衛的現実否認」にあります。",
            "丹精込めて育て上げた愛娘の恐るべき本性と犯行の動かぬ証拠を突きつけられた時、母親は名誉の崩壊から自己を守るため、現実そのものを遮断する道を選びました。",
            "娘は警察とテレビ番組の過激な演出によって仕組まれた罠の犠牲者に過ぎないという、荒唐無稽な陰謀論に必死にしがみつき続けたのです。",
            "盲目的な母性愛による現実否認は心理的な防衛反応としては理解し得るものですが、結果として犯人の破廉恥な開き直りと無反省を支える危険な温床となってしまいました。",
        ],
        "KO": [
            "이 사건에서 대단히 가슴 아픈 심리학적 단면 중 하나는 가해자의 친모가 보여준 극단적인 자기방어적 현실 부정입니다.",
            "지극정성으로 키워온 딸의 끔찍한 실체와 범행 증거를 마주했을 때 어머니는 명예의 파멸로부터 자아를 지키기 위해 현실 자체를 차단하는 길을 택했습니다.",
            "그녀는 딸이 자극적인 리얼리티 프로그램 제작진과 과열된 경찰에 의해 억울하게 덫에 걸렸다는 황당무계한 음모론에 필사적으로 매달렸습니다.",
            "맹목적인 모성애로 인한 현실 부정은 방어기제로서는 이해할 수 있으나 결과적으로 가해자의 뻔뻔한 파렴치함과 죄의식 결여를 부추기는 온상이 되고 말았습니다.",
        ],
    },
    22: {
        "VN": [
            "Bước ngoặt quyết định cứu sống Michael Dippolito bắt nguồn từ sự thức tỉnh lương tâm và cơ chế hối hận của chính người trung gian Mohamed Shihadeh.",
            "Từng có mối quan hệ tình cảm mờ ám và lắng nghe những lời than vãn của Dalia, nhưng khi đối diện với kế hoạch tước đoạt sinh mạng cụ thể, anh ta đã trải qua một cơn địa chấn đạo đức dữ dội.",
            "Sự kinh hoàng trước một dã tâm máu lạnh kết hợp với nỗi sợ hãi hiện sinh về việc trở thành đồng phạm giết người đã kích hoạt bản năng tự vệ và kéo phần lương tri còn sót lại của anh ta quay về với lề lối công lý.",
            "Quyết định dũng cảm bước vào sở cảnh sát tố giác và chấp nhận mang thiết bị ghi âm giăng bẫy chính là sự chuyển hóa từ một sai lầm trong quá khứ thành hành động cứu người chuộc lỗi mẫu mực.",
        ],
        "EN": [
            "The decisive turning point that ultimately spared Michael Dippolito's life stemmed directly from the moral awakening and authentic remorse of the intermediary, Mohamed Shihadeh.",
            "Having engaged in a clandestine affair and entertained Dalia's toxic complaints, he experienced a profound ethical shock when confronted with an explicit, premeditated assassination plot.",
            "The sheer horror of witnessing cold-blooded malice, coupled with an existential terror of facing life imprisonment as an accomplice to murder, shattered his denial and summoned his dormant conscience.",
            "His courageous decision to walk into the police department, blow the whistle, and wear a hidden wire to trap the conspirator transformed a compromising past into a life-saving act of profound redemption.",
        ],
        "JA": [
            "マイケル・ディッポリトの命を救う決定的な転換点となったのは、仲介役であったモハメド・シハデ自身の良心の覚醒と真摯な後悔のメカニズムでした。",
            "かつて不適切な関係を持ち、ダリアの不満に耳を傾けていた彼でしたが、具体的かつ冷酷な殺害計画を突きつけられた瞬間、猛烈な道徳的衝撃に襲われたのです。",
            "冷血な悪意に対する原初的な恐怖と、殺人共犯者として終身刑に直面するという実存的な危機感が彼の現実否認を打ち砕き、眠っていた人間的良心を揺り起こしました。",
            "自ら警察署へ駆け込んで真相を通報し、おとり捜査のために盗聴器を身につけて危険な接触に応じた彼の決断は、過去の過ちを人命救助という真の贖罪へと昇華させた決定的な瞬間でした。",
        ],
        "KO": [
            "마이클 디폴리토의 목숨을 구한 결정적 전환점은 바로 중개자였던 모하메드 시하데 자신의 양심의 각성과 진정한 후회의 메커니즘에서 비롯되었습니다.",
            "한때 부적절한 관계를 맺고 달리아의 불평에 귀 기울였던 그였지만 구체적인 살해 계획을 마주한 순간 극심한 도덕적 충격을 겪었습니다.",
            "냉혹한 살인 음모에 대한 원초적인 공포와 살인 공범으로서 종신형에 처해질 수 있다는 실존적 공포감이 그의 부정을 깨부수고 잠자던 양심을 흔들어 깨웠습니다.",
            "스스로 경찰서로 달려가 진실을 제보하고 도청 장치를 착용한 채 함정 수사에 응한 그의 용기 있는 결단은 과거의 잘못을 진정한 인명 구조의 속죄로 승화시킨 결정적 계기였습니다.",
        ],
    },
    26: {
        "VN": [
            "Sự đối lập giữa sự thức tỉnh của Shihadeh và sự trơ trẽn của Dalia đã làm nổi bật ranh giới căn bản giữa sự ăn năn chân chính và sự tự thương hại ái kỷ.",
            "Trong khi người trung gian biết sợ hãi trước tội ác để quay đầu cứu người, thì kẻ chủ mưu lại giam cầm tâm trí mình trong sự thù hận và đóng vai nạn nhân suốt gần một thập kỷ.",
            "Những giọt nước mắt lăn dài tại tòa án hoàn toàn là sự khóc thương cho tuổi xuân bị tước đoạt và nỗi cay đắng khi chiếc gương thần ái kỷ bị đập vỡ trước ánh sáng công lý.",
            "Đó là bản án tâm lý nghiệt ngã nhất: Người biết hối hận đã tìm lại được phẩm giá làm người, còn kẻ vô cảm sẽ vĩnh viễn sống trong ngục tù tăm tối của sự ích kỷ và dối trá.",
        ],
        "EN": [
            "This stark contrast between Shihadeh's redemption and Dalia's relentless defiance illuminates the fundamental divide between authentic moral remorse and narcissistic self-pity.",
            "While the intermediary harbored sufficient moral reverence for human life to reverse course and save a soul, the mastermind entombed herself in victimhood and bitter resentment for nearly a decade.",
            "Those bitter tears shed upon her sentencing were wept exclusively for her own lost youth, shattered entitlement, and the absolute destruction of her deceptive reflection before the court.",
            "This represents the most severe psychological retribution: the repentant soul reclaimed his humanity, while the unrepentant predator remains forever imprisoned within the dark cell of her own hollow vanity.",
        ],
        "JA": [
            "シハデの真摯な回心とダリアの不遜な居直りとの鮮烈な対比は、本物の「道徳的後悔」と自己愛的な「病理的自己憐憫」との決定的な境界線を浮き彫りにしています。",
            "仲介者が他者の命に対する畏怖の念から自らの過ちを正して人命を救ったのに対し、首謀者である彼女は十年間近く自らを被害者と位置づけ、他者への怨嗟に囚われ続けました。",
            "法廷で流された涙は、取り返しのつかない青春の喪失と、司法の光の前で自己愛の魔法の鏡が打ち砕かれたことに対する自分自身への哀惜に過ぎなかったのです。",
            "これこそが最も峻厳な心理的判決と言えます。真に悔いた者は人間としての尊厳を取り戻し、悔いることを拒絶した者は虚飾と欺瞞に満ちた魂の牢獄に永遠に幽閉され続けるのです。",
        ],
        "KO": [
            "시하데의 진정한 참회와 달리아의 뻔뻔한 오만함의 극명한 대비는 진정한 '도덕적 후회'와 자기애적 '병리적 자기연민'의 근본적인 차이를 극명하게 보여줍니다.",
            "중개자가 인간 생명에 대한 최소한의 외경심으로 발걸음을 되돌려 사람을 구한 반면 주모자인 그녀는 10년 가까이 피해자 코스프레와 타인을 향한 원망의 늪에 갇혀 있었습니다.",
            "선고 직후 법정에서 흘린 눈물은 잃어버린 자신의 젊음과 사법의 빛 앞에서 박살 난 자기애의 환영에 대한 자기 연민의 눈물에 불과했습니다.",
            "이것이야말로 가장 준엄한 심리학적 형벌입니다. 뉘우친 영혼은 인간으로서의 존엄성을 되찾았지만 참회를 거부한 포식자는 자신의 공허한 거짓의 감옥에 영원히 갇히게 되었습니다.",
        ],
    },
    29: {
        "VN": [
            "Vụ án là minh chứng đanh thép cho thấy sự dũng cảm tố giác của một cá nhân có thể thay đổi hoàn toàn cục diện giữa sự sống và cái chết của đồng loại.",
            "Kỷ cương xã hội và sự bình yên của mỗi gia đình chỉ có thể được bảo vệ vững chắc khi mỗi công dân biết từ chối thỏa hiệp với cái ác và sẵn sàng đứng về phía lẽ phải.",
        ],
        "EN": [
            "This case stands as powerful testament that the moral courage of a single individual coming forward can decisively tilt the balance between life and death.",
            "Social order and the sanctity of domestic peace can only be safeguarded when citizens refuse to normalize sinister impulses and bravely step forward to uphold the truth.",
        ],
        "JA": [
            "この事件は、一人の人間が勇気を持って真実を通報することが、他者の生死の天秤を決定的に変える力を持つことを雄弁に物語っています。",
            "社会の規律と各家庭の平穏は、市民一人ひとりが邪悪な企みとの妥協を断固として拒絶し、正義のために立ち上がる覚悟を持つことによってのみ守られるのです。",
        ],
        "KO": [
            "이 사건은 한 개인의 용기 있는 고발이 타인의 생과 사의 저울을 완전히 뒤바꿀 수 있음을 보여주는 강력한 증거입니다.",
            "사회의 법질서와 각 가정의 평온함은 시민들이 악의적인 유혹과의 타협을 단호히 거부하고 진실을 지키기 위해 일어설 때에만 굳건히 지켜질 수 있습니다.",
        ],
    },
    30: {
        "VN": [
            "Hành trình kiên cường đòi lại công lý của Michael Dippolito minh chứng cho khả năng Tăng trưởng sau sang chấn, khi nạn nhân dũng cảm đối diện với sự phản bội để tái thiết niềm tin cuộc sống.",
            "Sự thức tỉnh trước những cạm bẫy thao túng không khiến chúng ta trở nên hoài nghi khép kín, mà trang bị cho tâm hồn một bản lĩnh vững vàng để trân trọng những giá trị chân thực của tình yêu thương.",
        ],
        "EN": [
            "Michael Dippolito's resilient pursuit of justice exemplifies the profound power of Post-Traumatic Growth, where a survivor confronts devastating betrayal to rebuild genuine existential trust.",
            "Awakening from the snares of calculated manipulation should never compel us into cynical isolation, but rather fortify our souls with discernment to cherish authentic, unselfish human affection.",
        ],
        "JA": [
            "正義を求めて闘い抜いたマイケル・ディッポリトの不屈の歩みは、凄惨な裏切りを乗り越えて人生の信頼を再建する「外傷後成長」の力強い証左となりました。",
            "冷酷な操作の罠から目覚めることは私たちを頑なな不信へと追いやるのではなく、真実で無私なる愛の尊さを見極めるための揺るぎない心の強さを授けてくれるのです。",
        ],
        "KO": [
            "정의를 향해 끈질기게 싸워온 마이클 디폴리토의 불굴의 여정은 끔찍한 배신을 딛고 실존적 신뢰를 회복하는 '외상 후 성장'의 위대한 힘을 증명합니다.",
            "교묘한 통제의 덫에서 깨어나는 것은 우리를 냉소적인 불신으로 몰아넣는 것이 아니라 진실하고 사심 없는 사랑의 가치를 식별하는 단단한 내면의 힘을 길러줍니다.",
        ],
    },
}

def parse_md_into_sections(content):
    """Parses markdown into pre-dialogue content, 32 dialogue blocks, and post-dialogue content."""
    lines = content.splitlines()
    pre_lines = []
    blocks = []
    post_lines = []
    
    curr_h = None
    curr_lines = []
    in_dialogue = False
    
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("**") and not line.startswith("**["):
            in_dialogue = True
            if curr_h:
                blocks.append((curr_h, curr_lines))
            curr_h = line
            curr_lines = []
        elif not in_dialogue:
            pre_lines.append(line)
        else:
            # Check if this line is a cue like **[BGM]:** or **[SFX]:** or act header ## HỒI
            if line.startswith("**[") or line.startswith("## ") or line.startswith("---"):
                curr_lines.append(line)
            elif curr_h:
                curr_lines.append(line)
        i += 1
        
    if curr_h:
        blocks.append((curr_h, curr_lines))
        
    return pre_lines, blocks

def expand_file_block_based(lang, file_path):
    print(f"\nProcessing {lang}: {file_path}")
    content = Path(file_path).read_text(encoding="utf-8")
    lines = content.splitlines()
    
    # Extract blocks
    raw_blocks = []
    curr_speaker = None
    curr_content = []
    
    # Store lines before first speaker
    header_lines = []
    first_speaker_found = False
    
    for l in lines:
        if l.startswith("**") and not l.startswith("**["):
            first_speaker_found = True
            if curr_speaker:
                raw_blocks.append((curr_speaker, curr_content))
            curr_speaker = l
            curr_content = []
        elif not first_speaker_found:
            header_lines.append(l)
        else:
            curr_content.append(l)
    if curr_speaker:
        raw_blocks.append((curr_speaker, curr_content))
        
    print(f"  Found {len(raw_blocks)} dialogue blocks")
    if len(raw_blocks) != 32:
        print(f"  ERROR: Expected 32 blocks, got {len(raw_blocks)}!")
        return
        
    # Reconstruct blocks with additions
    new_blocks = []
    for idx, (spk, body) in enumerate(raw_blocks):
        # Filter pure speech sentences vs cue lines
        # In body, there might be cue lines at the end like **[SFX]:** or **[BGM]:** or blank lines
        speech_lines = []
        trailing_cues = []
        in_trailing = False
        
        # We can scan body backwards to separate trailing cues
        # A line is trailing cue if it starts with **[ or ## or is blank at the end
        cutoff = len(body)
        for k in range(len(body) - 1, -1, -1):
            bk = body[k].strip()
            if not bk:
                continue
            if bk.startswith("**[") or bk.startswith("##") or bk.startswith("---"):
                cutoff = k
            else:
                break
                
        speech_lines = [b for b in body[:cutoff] if b.strip()]
        trailing_cues = body[cutoff:]
        
        # If this block is in ADDITIONS and not already expanded
        if idx in ADDITIONS:
            add_lines = ADDITIONS[idx][lang]
            # Check if already added
            if not any(add_lines[0] in s for s in speech_lines):
                speech_lines.extend(add_lines)
                print(f"  [+] Block [{idx}] expanded with {len(add_lines)} sentences (now {len(speech_lines)})")
            else:
                print(f"  [.] Block [{idx}] already contains expansion (has {len(speech_lines)} sentences)")
                
        new_blocks.append((spk, speech_lines + trailing_cues))
        
    # Update header metadata
    header_text = "\n".join(header_lines)
    header_text = re.sub(r'\(212 câu thoại\)', '(248 câu thoại)', header_text)
    header_text = re.sub(r'\(212 câu\)', '(248 câu)', header_text)
    header_text = re.sub(r'212 câu thoại', '248 câu thoại', header_text)
    header_text = re.sub(r'212 câu', '248 câu', header_text)
    header_text = re.sub(r'212 sentences', '248 sentences', header_text)
    header_text = re.sub(r'212\s*台詞', '248 台詞', header_text)
    header_text = re.sub(r'212\s*문장', '248 문장', header_text)
    
    header_text = header_text.replace("| **122** |", "| **126** |")
    header_text = header_text.replace("| **37** |", "| **51** |")
    header_text = header_text.replace("| **36** |", "| **50** |")
    header_text = header_text.replace("| **8** |", "| **12** |")
    header_text = header_text.replace("| **212** |", "| **248** |")
    
    # Reassemble file
    out_lines = [header_text]
    for spk, body in new_blocks:
        out_lines.append(spk)
        for b in body:
            out_lines.append(b)
        out_lines.append("") # blank line between blocks
        
    final_content = "\n".join(out_lines)
    final_content = final_content.replace("\r\r\n", "\r\n").replace("\r\n", "\n")
    # Clean excessive blank lines
    final_content = re.sub(r'\n{3,}', '\n\n', final_content)
    
    Path(file_path).write_text(final_content, encoding="utf-8")
    print(f"  Saved {file_path}")

target_files_to_sync = [
    ("VN", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22" / "kichban_tap22_23102026.md"),
    ("EN", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22" / "kichban_tap22_EN.md"),
    ("EN", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22_EN" / "kichban_tap22_EN.md"),
    ("JA", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22" / "kichban_tap22_JA.md"),
    ("JA", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22_JA" / "kichban_tap22_JA.md"),
    ("KO", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22" / "kichban_tap22_KO.md"),
    ("KO", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22_KO" / "kichban_tap22_KO.md"),
]

def generate_json_scripts_from_markdown():
    print("\n--- Generating JSON scripts using parse_kichban ---")
    sys.path.insert(0, str(ROOT / ".work"))
    from parse_kichban import parse_lines
    
    sources = [
        ("VN", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22" / "kichban_tap22_23102026.md", ROOT / ".work" / "script_tap22.json"),
        ("EN", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22_EN" / "kichban_tap22_EN.md", ROOT / ".work" / "script_tap22_EN.json"),
        ("JA", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22_JA" / "kichban_tap22_JA.md", ROOT / ".work" / "script_tap22_JA.json"),
        ("KO", ROOT / "01_KICH_BAN" / "Ho_So_Toi_Pham" / "Tap22_KO" / "kichban_tap22_KO.md", ROOT / ".work" / "script_tap22_KO.json"),
    ]
    
    for lang, md_path, json_path in sources:
        if not md_path.exists():
            print(f"Skipping {md_path}")
            continue
        lines = md_path.read_text(encoding="utf-8").splitlines()
        els = parse_lines(lines)
        s_count = sum(len(e.get("sentences", [])) for e in els if e.get("kind") == "LOI")
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(els, f, ensure_ascii=False, indent=1)
        print(f"  Created {json_path.name}: {len(els)} elements, {s_count} LOI sentences")

if __name__ == "__main__":
    for lang, p in target_files_to_sync:
        if p.exists():
            expand_file_block_based(lang, p)
    generate_json_scripts_from_markdown()
    print("\nSync completed successfully!")
