# -*- coding: utf-8 -*-
"""Update Tap 18 scripts to 240 sentences across VN, EN, JA (and KO) with deep psychological analysis."""
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

# 1. VN ADDITIONS
VN_ADD = {
    '1.04': [
        "Nỗi bế tắc tuyệt vọng của Charles Vallow trước khi qua đời phản ánh một bi kịch tâm lý điển hình mang tên “Hội chứng Cassandra”.",
        "Đó là trạng thái cay đắng của một người nhìn thấu trước hiểm họa diệt vong của gia đình mình, nhưng mọi lời cầu cứu đều bị hệ thống hành pháp phớt lờ như một vụ tranh chấp ly hôn tầm thường.",
        "Cùng lúc đó, tại những cộng đồng tôn giáo khép kín như Rexburg, người ta thường mắc phải “Ảo tưởng An toàn Sùng đạo”.",
        "Niềm tin mặc định rằng những người năng nổ đi nhà thờ và viết sách về đức tin không thể làm điều ác đã vô tình dệt nên một bức màn che giấu hoàn hảo cho sự tha hóa nhân tính."
    ],
    '2.06': [
        "Đối với Alex Cox, hồ sơ điều tra tâm lý cho thấy hắn hoàn toàn bị thao túng bởi cơ chế “Gắn kết Ký sinh Bệnh lý” đối với người chị ruột.",
        "Hắn mù quáng tin rằng mình là một chiến binh ánh sáng của Chúa, sẵn sàng bóp cò súng và đào đất để phục vụ ảo tưởng của Lori mà không hề đòi hỏi lợi ích vật chất.",
        "Thế nhưng, vào những ngày cuối đời tại Arizona sau khi thi thể Tammy bị khai quật, Alex đã rơi vào cơn hoảng loạn tột cùng khi cay đắng nhận ra mình chỉ là một con tốt thí bị vứt bỏ.",
        "Trong khi đó, thiếu nữ mười sáu tuổi Tylee Ryan đã thể hiện bản lĩnh kiên cường phi thường khi nỗ lực che chở cho em trai tự kỷ cho đến hơi thở cuối cùng."
    ],
    '3.08': [
        "Về phía Chad Daybell, sự cuồng vĩ của hắn bắt nguồn từ một cơ chế “Ái kỷ Bù trừ” sâu sắc của một người đàn ông cả đời mờ nhạt làm nghề đào huyệt.",
        "Khi được Lori tôn sùng như một sứ giả bất tử, cái tôi tự ti bấy lâu đã bùng nổ thành một ảo tưởng cứu thế điên cuồng, biến việc sát hại người thân thành một sứ mệnh thiêng liêng.",
        "Còn đối với người con trai cả Colby Ryan, bi kịch này đã gây ra một cơn sang chấn mang tên “Sự Sụp Đổ Bản Sắc Mẫu Tử”.",
        "Nỗi đau đớn tột cùng khi nhận ra người mẹ hiền từ nuôi nấng mình thực chất là một kẻ thủ ác lạnh lùng đã để lại vết thương lương tâm vĩnh viễn không thể chữa lành."
    ],
    '4.09': [
        "Khoảnh khắc khiến cả phòng xử án lặng người là khi cuộn băng ghi âm cuộc gọi của nhân chứng Melanie Gibb được phát lên trước tòa.",
        "Đó là tiếng nói giằng xé của một người phụ nữ từng bị mê hoặc nhưng đã kịp thức tỉnh lương tri để quay đầu tố giác tội ác.",
        "Lời đối chất run rẩy nhưng quả quyết ấy đã xé toạc tấm màn thánh thiện giả tạo, phơi bày trần trụi động cơ tàn bạo của những kẻ cuồng tín."
    ],
    '4.10': [
        "Dưới góc độ nghiệp vụ điều tra, sự hợp tác của Melanie Gibb đánh dấu bước ngoặt quyết định chuyển hóa từ nghi vấn sang chứng cứ pháp lý xác thực.",
        "Hành vi hối hận của bà mang tính nhị nguyên rõ rệt giữa sự cắn rứt lương tâm đạo đức và bản năng tự vệ pháp lý để tránh bị truy tố tội tòng phạm.",
        "Bà hiểu rằng việc khai man với FBI về tung tích một đứa trẻ mất tích sẽ dẫn thẳng tới bản án tù chung thân.",
        "Cuộc gọi ghi âm ngày 8 tháng 12 năm 2019 chính là bằng chứng vàng đập tan toàn bộ các kịch bản ngoại phạm mà cặp đôi đã chuẩn bị kỹ lưỡng."
    ],
    '4.11': [
        "Khoa học tâm lý giải thích sự hối hận của Melanie Gibb là kết quả của một “Cú Sốc Thực Tế” đánh sập hoàn toàn cơ chế bất hòa nhận thức.",
        "Vào ngày 26 tháng 11 năm 2019, khi Lori yêu cầu bà nói dối cảnh sát rằng bé JJ đang đi xem phim ở Arizona, ranh giới giữa đức tin và tội ác hình sự đã sụp đổ.",
        "Melanie nhận ra mình không còn ở trong một sứ mệnh cứu thế, mà đang bị kéo vào vũng lầy của một vụ bắt cóc và mưu sát trẻ thơ.",
        "Chấn thương đạo đức dữ dội kết hợp với bản năng mẫu tính đã thức tỉnh, thôi thúc bà phải hành động để giải thoát cho lương tâm.",
        "Sự ăn năn chân thành của người ngoài cuộc đã đối lập gay gắt với sự chai sạn vô cảm của hai kẻ thủ ác.",
        "Đó là sự khác biệt căn bản giữa một tâm hồn lầm lỡ biết quay đầu và những nhân cách ái kỷ ác tính vĩnh viễn không thể cứu chuộc."
    ],
    '4.12': [
        "Kẻ tự phong mình là đấng cứu thế giờ đây chỉ còn lại nỗi cay đắng cô độc trong xà lim tử tù đối diện với án phạt tối hậu.",
        "Sự sụp đổ hoàn toàn của thế giới quan hoang tưởng đã phơi bày chân tướng của những kẻ săn mồi đội lốt đức tin.",
        "Bản án công lý trần thế đã khép lại, nhưng nỗi ám ảnh về sự biến chuyển tâm lý giữa điều thiện và điều ác vẫn còn vang vọng mãi."
    ],
    '5.03': [
        "Quy tắc vàng được đúc kết từ bi kịch này là: tính mạng và sự an toàn của trẻ thơ phải luôn được đặt lên trên sự e dè về quyền riêng tư hay tự do tín ngưỡng.",
        "Không một rào cản hành chính nào được phép làm chậm trễ bước chân của công lý khi một sinh mệnh ngây thơ đang đứng trước bờ vực hiểm nguy."
    ],
    '5.04': [
        "Về mặt tâm lý học cộng đồng, thảm kịch để lại một vết thương lương tâm tập thể dai dẳng, nhắc nhở chúng ta về cái giá của sự thỏa hiệp và thờ ơ trước những dấu hiệu bất thường.",
        "Chỉ khi mỗi cá nhân dám dũng cảm lên tiếng trước sự bất công, chúng ta mới có thể ngăn chặn những mầm mống cuồng tín tước đoạt tương lai của con trẻ."
    ]
}

# 2. EN ADDITIONS
EN_ADD = {
    '1.04': [
        "Charles Vallow’s desperate helplessness before his death reflects a classic psychological tragedy known as the “Cassandra Syndrome.”",
        "It is the agonizing state of someone who clearly foresees the catastrophic destruction of his family, yet every desperate plea is dismissed by law enforcement as trivial domestic strife.",
        "At the same time, in tight-knit religious communities like Rexburg, people often fell prey to the “Devout Safety Illusion.”",
        "The default assumption that active churchgoers who author religious books could never commit evil inadvertently wove a flawless veil that concealed monstrous human depravity."
    ],
    '2.06': [
        "Regarding Alex Cox, psychological investigative profiles reveal he was entirely manipulated through a mechanism of “Pathological Enmeshment” with his sister.",
        "He blindly believed he was God’s holy warrior of light, ready to pull the trigger and dig graves to serve Lori’s delusions without demanding financial rewards.",
        "Yet, during his final days in Arizona after Tammy’s body was exhumed, Alex spiraled into absolute panic upon bitterly realizing he was merely an expendable pawn.",
        "Meanwhile, sixteen-year-old Tylee Ryan displayed extraordinary resilience, fiercely attempting to protect her autistic little brother until her very last breath."
    ],
    '3.08': [
        "On Chad Daybell’s side, his megalomania stemmed from deep “Compensatory Narcissism” developed by an obscure cemetery sexton who felt insignificant all his life.",
        "When revered by Lori as an immortal prophet, his long-repressed inferiority exploded into a destructive messiah complex, reframing familial murder into a sacred calling.",
        "Meanwhile, for the surviving eldest son Colby Ryan, this horror triggered a catastrophic trauma known as “Maternal Identity Collapse.”",
        "The agonizing realization that the devoted mother who raised him was actually a cold-blooded killer left a permanent psychological scar that time can never heal."
    ],
    '4.09': [
        "The moment that silenced the entire courtroom was when the recorded confrontation call by witness Melanie Gibb was played before the jury.",
        "It was the agonizing voice of a woman once seduced by the cult who awakened her conscience just in time to expose the monstrous truth.",
        "Her trembling yet resolute confrontation tore away the holy facade, ruthlessly exposing the brutal depravity of these fanatic narcissists."
    ],
    '4.10': [
        "From an investigative perspective, Melanie Gibb’s cooperation marked the pivotal turning point transforming mere suspicion into concrete judicial evidence.",
        "Her remorse demonstrated a distinct duality between genuine moral guilt and legal self-preservation to avoid indictment as a co-conspirator.",
        "She recognized that lying to the FBI regarding the whereabouts of a missing child would inevitably result in a devastating prison sentence.",
        "The recorded call from December 8, 2019 served as the golden evidence that pulverized every prefabricated alibi constructed by the couple."
    ],
    '4.11': [
        "Psychological science explains Melanie Gibb’s remorse as the result of a violent “Reality Shock” that utterly shattered her cognitive dissonance.",
        "On November 26, 2019, when Lori demanded she lie to police that little JJ was watching movies in Arizona, the boundary between faith and felony dissolved.",
        "Melanie realized with sickening horror that she was no longer part of a divine calling, but was being ensnared in child abduction and murder.",
        "Profound moral injury coupled with awakened maternal instincts compelled her to take decisive action to rescue her tormented conscience.",
        "The authentic repentance of this awakened follower stood in razor-sharp contrast to the frozen apathy of the two ringleaders.",
        "It illustrates the fundamental chasm between a misguided soul capable of redemption and malignant narcissistic personalities that are forever beyond salvation."
    ],
    '4.12': [
        "The self-proclaimed messiah now languishes in bitter isolation on death row, awaiting his ultimate punishment.",
        "The total collapse of their delusional worldview laid bare the true monstrous faces of predators disguised in religious sanctity.",
        "While the verdict of earthly justice is sealed, the chilling haunting lesson regarding the fragile boundary between good and evil will echo forever."
    ],
    '5.03': [
        "The golden rule forged from this tragedy is that a child's life and safety must always transcend deference to religious freedom or parental privacy.",
        "No bureaucratic barrier should ever impede the urgent intervention of justice when an innocent young life hangs perilously in the balance."
    ],
    '5.04': [
        "In terms of community psychology, this tragedy leaves an enduring collective moral scar, reminding us of the devastating price of indifference toward abnormal warning signs.",
        "Only when individuals muster the courage to speak out against injustice can society truly prevent extremist cults from stealing the future of our children."
    ]
}

# 3. JA ADDITIONS
JA_ADD = {
    '1.04': [
        "チャールズ・ヴァローが命を落とす前に抱いていた絶望的な無力感は、「カッサンドラ症候群」と呼ばれる典型的な心理的悲劇を浮き彫りにしています。",
        "それは、自らの家族に迫る破滅的な危機を正確に予見していながら、法執行機関によって単なる離婚トラブルとして一蹴されてしまう痛切な葛藤です。",
        "同時に、レクスバーグのような閉鎖的な宗教コミュニティでは、人々は「敬虔な安全性幻想」に囚われていました。",
        "熱心に教会へ通い宗教書を執筆する人間が悪行に手を染めるはずがないという思い込みが、人間性の残酷な堕落を覆い隠す完璧な隠れ蓑となってしまったのです。"
    ],
    '2.06': [
        "アレックス・コックスに関して言えば、捜査心理プロファイルは彼が実の姉に対する「病理的共依存」のメカニズムによって完全に操られていたことを示しています。",
        "彼は自らを神の光の戦士と盲信し、金銭的見返りを求めることもなく、ローリの妄想に奉仕するために引き金を引き、土を掘り返しました。",
        "しかし、タミーの遺体が発掘された後のアリゾナでの最期の日々、アレックスは自らが単なる使い捨ての捨て駒に過ぎなかったと悟り、激しい恐慌に陥りました。",
        "その一方で、16歳の少女タイリー・ライアンは、息を引き取る最後の瞬間まで自閉症の弟を守ろうと、並外れた強靭な勇気を示していたのです。"
    ],
    '3.08': [
        "チャド・デイベルに関して言えば、彼の誇大妄想は墓堀人として生涯うだつの上がらなかった男の根深い「補償的自己愛」に起因しています。",
        "ローリから不滅の預言者として崇拝されたとき、長年抑圧されてきた劣等感は狂信的な救世主妄想へと爆発し、家族の殺害を神聖な使命へとすり替えました。",
        "一方、生き残った長男コルビー・ライアンにとって、この悲劇は「母性アイデンティティの崩壊」という壊滅的なトラウマをもたらしました。",
        "自らを慈しみ育ててくれた母親が冷酷な殺人鬼であったという痛烈な事実は、決して癒えることのない魂の傷跡を残したのです。"
    ],
    '4.09': [
        "法廷全体を息をのむ静寂に包み込んだ瞬間は、証人メラニー・ギブによる通話録音テープが陪審員の前で再生されたときでした。",
        "それは、かつてカルトに魅了されながらも、間一髪で良心を取り戻し恐ろしい真実を告発した女性の苦悩に満ちた声でした。",
        "震えながらも毅然とした彼女の追及は、偽りの聖なる仮面を引き裂き、狂信的な自己愛者たちの残酷な本性を容赦なく暴き出したのです。"
    ],
    '4.10': [
        "捜査の実務的観点から見れば、メラニー・ギブの協力は単なる疑念を確固たる司法的証拠へと昇華させた決定的な転換点でした。",
        "彼女の後悔は、道徳的良心の呵責と、共犯者としての起訴を免れるための法的自己防衛本能という明確な二面性を示していました。",
        "彼女は、行方不明の子どもの所在についてFBIに偽証すれば、壊滅的な刑罰が自らに降りかかることを熟知していたのです。",
        "2019年12月8日の録音通話は、夫婦が入念に用意していたアリバイ工作のすべてを粉砕する決定的な黄金の証拠となりました。"
    ],
    '4.11': [
        "心理科学は、メラニー・ギブの悔恨を、彼女の認知的不協和を完全に打ち砕いた激しい「現実ショック」の結実として説明します。",
        "2019年11月26日、ローリがJJと一緒にアリゾナで映画を見ていると警察に嘘をつくよう要求した瞬間、信仰と重罪の境界線は消失しました。",
        "メラニーは、自分がもはや崇高な神の使命などではなく、子どもの拉致と殺害の泥沼に引きずり込まれつつあることに戦慄したのです。",
        "深い道徳的損傷と目覚めた母性本能が結びつき、苛まれる自らの良心を救い出すために彼女を決断へと突き動かしました。",
        "目覚めた追従者の真摯な悔悟は、首謀者二人の凍りついた冷酷な無感覚と極めて鮮烈な対比を成しています。",
        "それは、過ちから引き返すことができる魂と、永遠に救済不能な悪性自己愛パーソナリティとの決定的な深淵を物語っているのです。"
    ],
    '4.12': [
        "自称救世主は今や死刑囚房の苦渋に満ちた孤立の中で、最終的な刑の執行を待つ身に過ぎません。",
        "誇大妄想的な世界観の完全な崩壊は、信仰の仮面を被った捕食者たちの怪物じみた素顔を白日の下に晒しました。",
        "現世の正義の審判は下されましたが、善と悪の間の脆い境界に関する不気味な教訓は、永遠に響き渡り続けるのです。"
    ],
    '5.03': [
        "この悲劇から導き出された黄金律は、子どもの生命と安全は宗教的自由や個人のプライバシーへの配慮よりも常に優先されなければならないということです。",
        "罪のない幼い命が危機に瀕しているとき、いかなる行政的障壁も正義の迅速な介入を遅らせてはならないのです。"
    ],
    '5.04': [
        "コミュニティ心理学の観点から見れば、この悲劇は永続的な集団的倫理の傷跡を残し、異常な警告サインに対する無関心がもたらす壊滅的な代償を痛烈に思い起こさせます。",
        "一人ひとりが不正に対して声を上げる勇気を持って初めて、社会はカルトの狂信が子どもたちの未来を奪うのを真に防ぐことができるのです。"
    ]
}

# 4. KO ADDITIONS
KO_ADD = {
    '1.04': [
        "찰스 밸로우가 숨지기 전에 겪었던 절망적인 무력감은 '카산드라 증후군'이라 불리는 전형적인 심리적 비극을 반영합니다.",
        "그것은 자기 가족에게 닥쳐올 파멸적인 위기를 똑똑히 예견하면서도, 모든 구조 요청이 사법 당국에 의해 단순한 이혼 분쟁으로 묵살당하는 뼈아픈 좌절입니다.",
        "동시에 렉스버그와 같은 폐쇄적인 종교 공동체에서 사람들은 흔히 '경건한 안전성 환상'에 빠져들었습니다.",
        "교회에 열성적으로 출석하고 신앙 서적을 집필하는 인물이 악행을 저지를 리 없다는 맹목적 믿음이 인간성의 참혹한 타락을 가려주는 완벽한 장막이 된 것입니다."
    ],
    '2.06': [
        "알렉스 콕스의 경우, 수사 심리 프로파일은 그가 친누나에 대한 '병리적 공의존' 기제에 의해 완전히 조종당했음을 보여줍니다.",
        "그는 자신이 신의 빛의 전사라는 망상에 빠져 금전적 대가도 요구하지 않은 채 로리의 망상을 위해 방아쇠를 당기고 땅을 팠습니다.",
        "하지만 태미의 시신이 발굴된 후 애리조나에서의 마지막 나날들 동안, 알렉스는 자신이 한낱 버려지는 장기말에 불과했음을 깨닫고 극심한 공황에 빠졌습니다.",
        "그 와중에 열여섯 살 소녀 타일리 라이언은 마지막 숨을 거두는 순간까지 자폐를 앓는 남동생을 지키려 비범한 용기를 발휘했습니다."
    ],
    '3.08': [
        "채드 데이벨의 경우, 그의 과대망상은 평생 무덤 파는 일로 초라하게 살았던 한 남자의 깊은 '보상적 자기애'에서 비롯되었습니다.",
        "로리에게 불멸의 예언자로 숭배받게 되자 억눌렸던 열등감은 광적인 구세주 망상으로 폭발했고, 가족 살해를 성스러운 사명으로 둔갑시켰습니다.",
        "한편 살아남은 장남 콜비 라이언에게 이 비극은 '모성 정체성의 붕괴'라는 치명적인 트라우마를 안겼습니다.",
        "자신을 헌신적으로 길러준 어머니가 냉혹한 살인마였다는 처절한 진실은 결코 아물지 않는 영혼의 상흔을 남겼습니다."
    ],
    '4.09': [
        "법정 전체를 얼어붙게 만든 순간은 증인 멜라니 깁의 통화 녹음 파일이 배심원단 앞에서 재생되었을 때였습니다.",
        "그것은 한때 사이비에 매혹되었으나 가까스로 양심을 되찾고 끔찍한 진실을 고발한 한 여성의 처절한 목소리였습니다.",
        "떨리지만 단호했던 그녀의 추궁은 위선적인 성스러움의 가면을 찢어발기고 광신적 자기애자들의 잔혹한 본성을 낱낱이 드러냈습니다."
    ],
    '4.10': [
        "수사 실무의 관점에서 멜라니 깁의 협조는 단순한 의혹을 결정적인 법적 증거로 전환시킨 결정적 분수령이었습니다.",
        "그녀의 후회는 도덕적 양심의 가책과 공범 기소를 피하기 위한 법적 자기방어 본능이라는 뚜렷한 이중성을 띠고 있었습니다.",
        "그녀는 실종된 아이의 행방에 대해 FBI에 위증할 경우 종신형에 처해질 수 있음을 너무나 잘 알고 있었습니다.",
        "2019년 12월 8일의 녹음 통화는 부부가 치밀하게 준비했던 모든 알리바이를 산산조각 낸 결정적 황금 증거가 되었습니다."
    ],
    '4.11': [
        "심리과학은 멜라니 깁의 참회를 그녀의 인지부조화를 완전히 무너뜨린 폭력적인 '현실 충격'의 결과로 설명합니다.",
        "2019년 11월 26일, 로리가 JJ와 애리조나에서 영화를 보고 있다고 경찰에 거짓말하라고 요구한 순간, 신앙과 중범죄의 경계는 무너졌습니다.",
        "멜라니는 자신이 성스러운 사명에 있는 것이 아니라 아동 납치와 살해의 늪에 휘말리고 있음을 전율하며 깨달았습니다.",
        "극심한 도덕적 손상과 깨어난 모성 본능이 결합하여 괴로워하는 양심을 구하기 위해 그녀를 결단으로 이끌었습니다.",
        "깨어난 추종자의 진정한 참회는 두 주범의 얼어붙은 무감각과 극명한 대조를 이루었습니다.",
        "이는 뉘우칠 줄 아는 길 잃은 영혼과 결코 구원받을 수 없는 악성 자기애적 인격 사이의 본질적인 심연을 보여줍니다."
    ],
    '4.12': [
        "자칭 구세주는 이제 사형수 감방의 쓸쓸한 고립 속에서 최종적인 형벌의 날만을 기다리고 있을 뿐입니다.",
        "망상적 세계관의 완전한 붕괴는 종교적 성스러움의 탈을 쓴 포식자들의 괴물 같은 실체를 만천하에 드러냈습니다.",
        "지상의 사법적 판결은 내려졌지만, 선과 악 사이의 위태로운 경계에 대한 오싹한 교훈은 영원히 메아리칠 것입니다."
    ],
    '5.03': [
        "이 비극에서 도출된 황금률은 아동의 생명과 안전이 종교적 자유나 부모의 사생활에 대한 배려보다 항상 우선해야 한다는 점입니다.",
        "무고한 어린 생명이 위태로운 벼랑 끝에 서 있을 때, 그 어떤 행정적 장벽도 정의의 신속한 개입을 가로막아서는 안 됩니다."
    ],
    '5.04': [
        "공동체 심리학 관점에서 이 비극은 영구적인 집단적 윤리적 상흔을 남기며, 비정상적인 경고 신호에 대한 무관심이 치러야 할 참혹한 대가를 일깨웁니다.",
        "각 개인이 불의에 맞서 용기 있게 목소리를 낼 때에만, 사회는 광신 집단이 우리 아이들의 미래를 앗아가는 것을 진정으로 막을 수 있습니다."
    ]
}

anchors = {
    'VN': {
        '1.04': 'để thực hiện kiểm tra an sinh khẩn cấp.',
        '2.06': 'Lòng tham vật chất và sự cuồng tín đã hòa quyện thành một động cơ tội ác không thể chối cãi.',
        '3.08': 'Nỗi đau ấy để lại những vết thương tâm lý vĩnh viễn không bao giờ có thể chữa lành.',
        '4.09': 'Nhưng đó là phán quyết công bằng và cần thiết duy nhất để trả lại danh dự và sự bình yên cho linh hồn của Tammy, Tylee và bé JJ.',
        '4.10': 'Sự nghiêm minh của pháp luật đã phá tan hoàn toàn vương quốc ảo tưởng do những kẻ cuồng tín dựng nên.',
        '4.11': 'Bản án trần thế đã khép lại số phận của hai kẻ thủ ác, nhưng bản án tâm lý học sẽ còn được lưu truyền như một bài học cảnh tỉnh sâu sắc.',
        '4.12': 'Để lại cho xã hội những câu hỏi day dứt về ranh giới mong manh giữa niềm tin và sự hủy diệt.',
        '5.03': 'Công lý đã được thực thi trọn vẹn, trả lại sự thanh thản cho các nạn nhân đã khuất.',
        '5.04': 'Sự tỉnh thức lý trí và tư duy phản biện độc lập chính là chiếc khiên vững chắc nhất bảo vệ chúng ta trước những cạm bẫy cuồng tín.'
    },
    'EN': {
        '1.04': 'Recognizing immediate danger surrounding the two vulnerable children, the Woodcocks pleaded with the Rexburg Police Department in Idaho to perform an emergency welfare check.',
        '2.06': 'Material greed and spiritual megalomania had coalesced into an undeniable criminal motive.',
        '3.08': 'That profound trauma leaves enduring psychological scars that rarely heal completely.',
        '4.09': 'Yet it was the only just and necessary verdict to restore dignity and solemn peace to Tammy, Tylee, and little JJ.',
        '4.10': 'The rule of law completely obliterated the narcissistic fantasy kingdom constructed by these religious extremists.',
        '4.11': 'Earthly verdicts have resolved their legal fate, yet this case will remain a cautionary study in forensic psychology for generations.',
        '4.12': 'Leaving our society to contemplate haunting questions regarding the fragile line separating blind faith from absolute destruction.',
        '5.03': 'Justice was thoroughly served, restoring peace to the memories of those who perished.',
        '5.04': 'Rational discernment and critical thinking remain our most formidable armor against the seductive traps of toxic fanaticism.'
    },
    'JA': {
        '1.04': '二人の無力な子供たちに危険が迫っていることを悟ったウッドコック夫妻は、アイダホ州レックスバーグ警察に至急の安否確認を要請しました。',
        '2.06': '金銭的強欲と狂信が融合し、否定しがたい犯罪の動機を形成していたのです。',
        '3.08': 'その精神的トラウマは、決して容易には癒えることのない深い傷痕を残します。',
        '4.09': 'しかしそれは、タミー、タイリー、そして幼いJJの魂に尊厳と静けさを取り戻すための唯一の正当な判断でした。',
        '4.10': '法の厳格な正義は、狂信者たちが築き上げた妄想の帝国を完全に粉砕したのです。',
        '4.11': '現世の裁判は二人の運命に幕を引きましたが、この記録は深層心理の警告として後世に語り継がれるでしょう。',
        '4.12': 'そして盲目的な狂信と破滅を分かつ脆い境界線について、社会に重い問いを投げかけています。',
        '5.03': '正義は完全に執行され、尊い犠牲者たちの記憶に安らぎが取り戻されました。',
        '5.04': '論理的な思考と批判的吟味の精神こそが、狂信の罠から私たちを守る最も強固な盾なのです。'
    },
    'KO': {
        '1.04': '어린 두 아이에게 닥친 위험을 직감한 우드콕 부부는 아이다호주 렉스버그 경찰국에 긴급 복지 점검을 요청했습니다.',
        '2.06': '물질적 탐욕과 광신이 뒤엉켜 부인할 수 없는 범죄 동기를 완성하고 있었습니다.',
        '3.08': '그 심리적 외상은 결코 온전히 치유되기 힘든 영구적인 흉터를 남깁니다.',
        '4.09': '그러나 그것은 태미, 타일리, 그리고 어린 JJ의 영혼에 존엄과 평안을 돌려주기 위한 유일하고 정의로운 판단이었습니다.',
        '4.10': '엄정한 법의 지배는 광신자들이 세워 올린 기괴한 망상의 왕국을 완전히 짓밟아 무너뜨렸습니다.',
        '4.11': '세속의 판결은 두 사람의 운명을 봉인했지만, 이 기록은 깊은 경고를 담은 범죄심리학의 교훈으로 오래도록 기억될 것입니다.',
        '4.12': '그리고 맹목적인 믿음과 파멸 사이를 가르는 위태로운 경계선에 대해 우리 사회에 묵직한 물음을 던지고 있습니다.',
        '5.03': '정의는 온전히 구현되었으며, 억울하게 희생된 이들의 영혼 앞에 평안이 되돌려졌습니다.',
        '5.04': '합리적인 분별력과 비판적 사고야말로 광신의 덫으로부터 우리 자신을 지켜내는 가장 강력한 방패입니다.'
    }
}

def update_script(file_path, additions, lang_code):
    print(f"\nProcessing {lang_code}: {file_path}")
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()
    
    updated_text = text
    # Update header version and sentence count
    updated_text = re.sub(r'208\s*(câu thoại|sentences|文|개 대사)', '240 \\1', updated_text, flags=re.I)
    updated_text = re.sub(r'28\s*–\s*31\s*(phút|minutes|分|분)', '29 – 32 \\1', updated_text, flags=re.I)
    
    for eid, anchor in anchors[lang_code].items():
        if anchor not in updated_text:
            print(f"ERROR: Anchor not found for {eid} in {lang_code}: {anchor}")
            sys.exit(1)
        added_block = '\n' + '\n'.join(additions[eid])
        updated_text = updated_text.replace(anchor, anchor + added_block, 1)
        print(f"  Injected {len(additions[eid])} sentences after anchor {eid}")
        
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(updated_text)
    print(f"SUCCESS: Updated {file_path}")

# Run update for all files
update_script('01_KICH_BAN/Tap18/kichban_tap18_23102026.md', VN_ADD, 'VN')
update_script('01_KICH_BAN/Tap18_EN/kichban_tap18_EN.md', EN_ADD, 'EN')
update_script('01_KICH_BAN/Tap18_JA/kichban_tap18_JA.md', JA_ADD, 'JA')
update_script('01_KICH_BAN/Tap18_KO/kichban_tap18_KO.md', KO_ADD, 'KO')

if os.path.exists('01_KICH_BAN/Tap18/kichban_tap18_EN.md'):
    update_script('01_KICH_BAN/Tap18/kichban_tap18_EN.md', EN_ADD, 'EN')
