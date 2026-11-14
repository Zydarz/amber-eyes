# -*- coding: utf-8 -*-
"""Update Episode 20 scripts across VN, EN, JA, KO to 241 sentences with deep psychology."""

import sys
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban as PK

VN_ADD = {
    '1.02': [
        "Tại những giảng đường danh giá như Đại học Mercer, cộng đồng sinh viên thường sống trong một niềm tin mặc định về sự an toàn tuyệt đối của môi trường học thuật.",
        "Chính ảo tưởng an toàn ấy đã vô tình làm tê liệt phản xạ cảnh giác tự nhiên của những người trẻ tuổi trước các mối đe dọa ngầm."
    ],
    '1.07': [
        "Chỉ vài ngày trước khi biến mất, Lauren từng tâm sự với chúng tôi về một cảm giác bất an mơ hồ khi ở trong căn hộ của mình.",
        "Chúng tôi cứ tự dằn vặt mãi rằng tại sao lúc đó mình không tin vào linh cảm của bạn mình, để rồi Lauren phải đối mặt một mình với sự đe dọa vô hình ấy."
    ],
    '1.10': [
        "Khoảnh khắc nghi phạm ngồi sụp xuống lề đường chính là sự sụp đổ đầu tiên của một ảo tưởng ái kỷ khi kế hoạch tưởng như hoàn hảo bị thực tế đánh tan tành."
    ],
    '2.02': [
        "Sự bất động tuyệt đối của McDaniel giữa căn phòng hỏi cung không đơn thuần là sự lì lợm, mà là biểu hiện của một hệ thần kinh đang căng thẳng tột độ để duy trì sự kiểm soát.",
        "Hắn đã chọn cách đóng băng toàn bộ cơ thể như một nỗ lực tuyệt vọng nhằm ngăn cản bất kỳ vi biểu cảm nào để lộ tâm lý tội lỗi."
    ],
    '2.06': [
        "Chiếc chìa khóa vạn năng tìm thấy trong phòng McDaniel đã bóc trần sự cẩu thả nghiêm trọng của ban quản lý tòa nhà khi cất giữ chìa khóa bảo trì một cách hớ hênh.",
        "Lỗ hổng an ninh ấy đã gián tiếp trao vào tay kẻ rình rập một đặc quyền nguy hiểm: tự do bước vào không gian riêng tư của nạn nhân mà không cần phải cạy phá cửa."
    ],
    '2.10': [
        "Hàng trăm tệp dữ liệu được phục hồi từ máy tính của McDaniel cho thấy một tiến trình tự thôi miên và leo thang ám ảnh kéo dài nhiều tháng trời.",
        "Kẻ săn mồi đã liên tục nâng ngưỡng kích thích, biến sự xâm phạm đời tư của người khác thành một cơn nghiện quyền lực bệnh hoạn."
    ],
    '3.03': [
        "Dưới góc độ tâm thần học pháp y, Stephen McDaniel mang đặc trưng điển hình của sự khuyết tật nghiêm trọng về Thuyết Tâm Trí.",
        "Hắn hoàn toàn không có khả năng thấu cảm để đặt mình vào vị trí của người khác, xem những người xung quanh chỉ như những công cụ phục vụ cho cái tôi ái kỷ của mình."
    ],
    '3.05': [
        "Khi nhìn thấy những chiếc hộp đóng gói đồ đạc của Lauren, bộ não ái kỷ của McDaniel phải đối mặt với một cơn sang chấn mang tên Tổn Thương Ái Kỷ Cấp Tính.",
        "Nỗi hoảng sợ trước sự sụp đổ của ảo tưởng kiểm soát đã thúc đẩy hắn đi đến một kết luận bệnh lý: thà hủy diệt mục tiêu còn hơn là chấp nhận để đối tượng thoát khỏi tầm tay."
    ],
    '3.07': [
        "Hiện tượng bất động như tượng đá trong phòng hỏi cung của McDaniel thực chất là sự mô phỏng có ý thức của phản xạ Bất Động Sinh Học.",
        "Trong tự nhiên, khi kẻ săn mồi nhận ra không thể trốn chạy hay chống cự, cơ thể nó sẽ giả chết như một nỗ lực cuối cùng để vô hiệu hóa sự chú ý của đối phương."
    ],
    '4.02': [
        "Ba năm bị giam giữ trong bốn bức tường bê tông đã bóc trần toàn bộ sự kiêu ngạo giả tạo của cựu sinh viên trường luật.",
        "Ảo tưởng về một trí tuệ siêu việt có thể đánh lừa công lý đã hoàn toàn sụp đổ trước kho chứng cứ khoa học không thể lay chuyển."
    ],
    '4.06': [
        "Bản thỏa thuận nhận tội mà McDaniel ký kết vào phút chót không hề xuất phát từ một sự thức tỉnh lương tri hay ăn năn sám hối.",
        "Đó thuần túy là sự toan tính sinh tồn hèn nhát của một kẻ hiểu rằng phiên tòa xét xử công khai sẽ đưa hắn thẳng tới bản án tử hình."
    ],
    '4.10': [
        "Sau vụ án, những người từng cẩu thả trong quy trình bảo an của tòa nhà đã phải gánh chịu một chấn thương đạo đức dai dẳng khi nhận ra sự lơ là của mình đã mở đường cho tội ác."
    ],
    '4.11': [
        "Khoa học tâm lý học tội phạm phân biệt rạch ròi giữa Sự Ăn Năn Chân Thực và Sự Tự Thương Hại Bệnh Lý.",
        "Những giọt nước mắt hiếm hoi của McDaniel chỉ là sự xót thương cho cái tôi ái kỷ đã tan tành của chính hắn, chứ không hề có một tia thấu cảm nào cho sinh mạng của người khác."
    ],
    '5.02': [
        "Nỗi bàng hoàng của cộng đồng sinh viên Mercer đã nhanh chóng chuyển hóa thành một phong trào đại cải cách thể chế mạnh mẽ trên khắp nước Mỹ.",
        "Sự an toàn của người học không còn được phó mặc cho những giả định lỏng lẻo, mà được bảo chứng bằng những quy chuẩn quản trị minh bạch và chặt chẽ."
    ],
    '5.03': [
        "Bài học đắt giá nhất là tuyệt đối không bao giờ được phép xem nhẹ các lỗ hổng cơ sở vật chất, bởi một chiếc chìa khóa bị bỏ quên cũng có thể trở thành công cụ tiếp tay cho tội ác."
    ],
    '5.04': [
        "Chân lý sinh tồn lớn nhất là trực giác sợ hãi không phải là sự hoang tưởng, mà là tín hiệu tiến hóa báo trước mối nguy hiểm cận kề.",
        "Hãy can đảm tin vào trực giác ấy và dứt khoát thiết lập ranh giới phòng vệ thay vì cố gắng tỏ ra lịch sự để làm hài lòng người khác."
    ]
}

EN_ADD = {
    '1.02': [
        "Within prestigious academic halls like Mercer University, the student community often lived under a default assumption of absolute safety.",
        "That very illusion of academic security inadvertently paralyzed the natural vigilance of young intellectuals stepping into independent life."
    ],
    '1.07': [
        "Just days before she vanished, Lauren had shared with us an ambiguous feeling of dread inside her own apartment.",
        "We tormented ourselves with guilt, wondering why we failed to trust our friend's intuition, leaving Lauren to face that invisible threat entirely alone."
    ],
    '1.10': [
        "The moment the suspect collapsed onto the curb was the first visible breakdown of a narcissistic delusion when his supposedly perfect plan was shattered by reality."
    ],
    '2.02': [
        "McDaniel’s absolute immobility inside the interrogation room was not mere stubbornness, but the manifestation of a nervous system strained to its extreme limit to maintain control.",
        "He chose to freeze his entire body in a desperate bid to prevent any micro-expression from betraying his guilty mind."
    ],
    '2.06': [
        "The master key found inside McDaniel’s room exposed severe negligence by property management in carelessly storing maintenance keys.",
        "That systemic security loophole inadvertently handed the stalker a deadly privilege: unhindered access to the victim’s private sanctuary without forced entry."
    ],
    '2.10': [
        "Hundreds of files recovered from McDaniel’s computer revealed a months-long process of progressive self-hypnosis and escalating obsession.",
        "The predator continuously escalated his stimulation threshold, turning the violation of another's privacy into a pathological addiction to control."
    ],
    '3.03': [
        "From a forensic psychiatric perspective, Stephen McDaniel exhibited a profound deficit in Theory of Mind.",
        "He possessed no capacity for emotional empathy to see others as sovereign individuals, viewing surrounding people merely as instruments to gratify his narcissistic ego."
    ],
    '3.05': [
        "Seeing Lauren's packed moving boxes confronted McDaniel's narcissistic brain with an agonizing trauma known as Acute Narcissistic Injury.",
        "The terror of losing his delusional omnipotence drove him to a pathological conclusion: better to destroy the target than allow her to escape his control."
    ],
    '3.07': [
        "McDaniel’s stone-like immobility in the interrogation room was a conscious simulation of the biological reflex known as Tonic Immobility.",
        "In nature, when an organism realizes fight or flight is impossible, it feigns death as an ultimate biological effort to neutralize the opponent's focus."
    ],
    '4.02': [
        "Three years of confinement within concrete walls stripped away every shred of the former law student's arrogant pretense.",
        "The delusion of an intellectual mastermind capable of outsmarting justice collapsed completely before the unassailable mountain of forensic evidence."
    ],
    '4.06': [
        "The plea agreement McDaniel signed at the final hour was never an awakening of conscience or genuine repentance.",
        "It was purely cowardly survival calculus from someone who understood a public jury trial would lead directly to death row."
    ],
    '4.10': [
        "Following the case, those who had been careless with building security suffered enduring moral injury upon realizing their negligence paved the path for evil."
    ],
    '4.11': [
        "Criminal psychology draws a sharp boundary between Authentic Remorse and Pathological Self-Pity.",
        "McDaniel’s rare tears were shed solely for his shattered narcissistic ego, completely devoid of affective empathy for another human life."
    ],
    '5.02': [
        "The shock felt by the Mercer student community swiftly transformed into a powerful institutional reform movement across the United States.",
        "Student safety was no longer entrusted to loose assumptions, but safeguarded by transparent, rigorous governance standards."
    ],
    '5.03': [
        "The costliest lesson is that structural physical security loopholes must never be trivialized, for a neglected key can become an inadvertent accomplice to crime."
    ],
    '5.04': [
        "The greatest survival truth is that intuitive fear is not paranoia, but an evolutionary signal warning of imminent danger.",
        "Courageously trust that intuition and decisively establish defensive boundaries rather than compromising safety for the sake of social politeness."
    ]
}

JA_ADD = {
    '1.02': [
        "マーサー大学のような名門ロースクールのキャンパスにおいて、学生たちは学究環境の絶対的な安全性という思い込みの中で暮らしていました。",
        "まさにその安全性幻想が、自立した生活を始めたばかりの若者たちの自然な警戒心を鈍らせてしまったのです。"
    ],
    '1.07': [
        "失踪するわずか数日前、ローレンは自室で感じる漠然とした不穏な予感について、私たちに不安を漏らしていました。",
        "なぜあの時友人の直感を信じてあげられなかったのか、ローレンを見えない脅威の前に一人置き去りにしてしまったのかと、私たちは激しい自責に苛まれ続けました。"
    ],
    '1.10': [
        "容疑者が歩道に崩れ落ちた瞬間は、完璧と思われた計画が捜査の現実に打ち砕かれ、自己愛の妄想が崩壊し始めた決定的な証拠でした。"
    ],
    '2.02': [
        "取調べ室におけるマクダニエルの完全な静止は、単なる強情さではなく、制御を維持しようと極度の緊張に達した神経系の現れでした。",
        "彼は有罪の心理を露呈させる微表情を一切封じ込めようと、絶望的な試みとして全身を凍結させる道を選んだのです。"
    ],
    '2.06': [
        "マクダニエルの部屋から発見されたマスターキーは、管理鍵を無造作に放置していたアパート管理側の重大な過失を白日の下に晒しました。",
        "その組織的な保安の欠陥が、ドアをこじ開けることなく犠牲者の私的空間へ侵入できる危険な特権を、ストーカーの手に間接的に与えてしまったのです。"
    ],
    '2.10': [
        "マクダニエルのパソコンから復元された数百件のデータは、数か月にわたる自己催眠と執着のエスカレーションの軌跡を示していました。",
        "この捕食者は刺激の閾値を絶え間なく引き上げ、他者のプライバシーの侵害を支配への病的な依存へと変貌させていたのです。"
    ],
    '3.03': [
        "司法精神医学の観点から見れば、スティーブン・マクダニエルは心の理論における深刻な欠陥という典型的な特徴を示していました。",
        "彼は他者の立場に立って共感する能力を完全に欠いており、周囲の人間を自らの自己愛を満たすための道具としてしか認識していなかったのです。"
    ],
    '3.05': [
        "ローレンの荷造りされた段ボール箱を目にしたとき、マクダニエルの自己愛的な脳は急性自己愛損傷という激しい打撃に直面しました。",
        "支配という妄想の崩壊に対する恐怖が、対象が自分の手から永遠に離れるのを許すくらいなら完全に破壊してしまう方がましだという病理的結論へと彼を駆り立てたのです。"
    ],
    '3.07': [
        "取調べ室におけるマクダニエルの石像のような不動は、強直性不動と呼ばれる生物学的反射を意識的に模倣したものでした。",
        "自然界において、闘争も逃走も不可能だと悟った生物は、敵の注意を無力化するための最終的な生存戦略として擬死状態に陥るのです。"
    ],
    '4.02': [
        "コンクリートの壁に囲まれた3年間の勾留生活は、元法学生の傲慢な虚勢を根底から剥ぎ取りました。",
        "正義を欺くことができるという知能犯の妄想は、動かしがたい科学的証拠の前に完全に瓦解したのです。"
    ],
    '4.06': [
        "マクダニエルが土壇場で署名した司法取引は、良心の目覚めや真摯な懺悔から出たものでは決してありませんでした。",
        "それは、公開裁判に進めば陪審員によって死刑判決が下されると察した、卑怯な生存の損得計算に過ぎなかったのです。"
    ],
    '4.10': [
        "事件後、建物の保安管理を軽視していた関係者たちは、自らの怠慢が凶行への道を開いてしまったと悟り、消えることのない道徳的トラウマを背負い続けることとなりました。"
    ],
    '4.11': [
        "犯罪心理学は、真の悔悟と病理的自己憐憫の間に明確な境界線を引いています。",
        "マクダニエルが流した稀な涙は、打ち砕かれた自らの自己愛に対する哀れみに過ぎず、他者の尊い命への共感は微塵も含まれていませんでした。"
    ],
    '5.02': [
        "マーサー大学の学生コミュニティが受けた衝撃は、全米の大学における強力な制度改革運動へと急速に昇華していきました。",
        "学生たちの安全はもはや安易な前提に委ねられることなく、透明で厳格な管理基準によって保護されるようになったのです。"
    ],
    '5.03': [
        "最も重い教訓は、施設管理上の隙を決して軽視してはならないということであり、放置された一本の鍵が犯罪を幇助する道具になり得るのです。"
    ],
    '5.04': [
        "最大の生存の真理は、直感的な恐怖は妄想などではなく、迫り来る危険を警告する進化の知恵であるということです。",
        "礼儀正しさを保つために安全を犠牲にするのではなく、直感を信じて断固たる防衛境界線を引く勇気を持つことが何よりも重要なのです。"
    ]
}

KO_ADD = {
    '1.02': [
        "머서 대학교와 같은 명문 로스쿨 캠퍼스에서 학생들은 학문적 환경의 절대적인 안전성에 대한 맹목적인 믿음 속에 살아가고 있었습니다.",
        "바로 그 안전성에 대한 환상이 독립된 생활을 시작한 젊은이들의 자연스러운 경계심을 무디게 만들었던 것입니다."
    ],
    '1.07': [
        "실종되기 불과 며칠 전, 로렌은 자신의 아파트에서 느껴지는 막연한 불안감에 대해 우리에게 털어놓은 적이 있었습니다.",
        "우리는 왜 그때 친구의 직감을 진지하게 믿어주지 못했는지, 로렌을 보이지 않는 위협 앞에 홀로 남겨두었는지 끝없는 자책에 시달렸습니다."
    ],
    '1.10': [
        "용의자가 보도에 주저앉은 순간은 완벽하다고 믿었던 계획이 수사의 현실에 산산조각 나며 나르시시즘적 망상이 무너지기 시작한 결정적 순간이었습니다."
    ],
    '2.02': [
        "취조실에서 맥대니얼의 완전한 부동자세는 단순한 고집이 아니라, 통제력을 유지하기 위해 극도의 긴장에 도달한 신경계의 발현이었습니다.",
        "그는 죄책감을 드러내는 어떠한 미세 표정도 차단하기 위해 절박한 시도로서 온몸을 동결시키는 방식을 택했던 것입니다."
    ],
    '2.06': [
        "맥대니얼의 방에서 발견된 마스터키는 관리실 열쇠를 허술하게 방치했던 건물 관리 측의 심각한 과실을 명백히 드러냈습니다.",
        "그러한 구조적인 보안 허점이 문을 강제로 부수지 않고도 피해자의 사적 공간에 자유롭게 들어갈 수 있는 위험한 특권을 스토커의 손에 쥐여주었던 것입니다."
    ],
    '2.10': [
        "맥대니얼의 컴퓨터에서 복구된 수백 개의 데이터는 수개월에 걸친 자기 최면과 집착의 단계적 에스컬레이션 과정을 여실히 보여주었습니다.",
        "이 포식자는 자극의 한계점을 끊임없이 끌어올리며, 타인의 사생활 침해를 지배력에 대한 병적인 중독으로 변질시켰던 것입니다."
    ],
    '3.03': [
        "사법정신의학의 관점에서 볼 때, 스티븐 맥대니얼은 마음 이론에 있어서 심각한 결함을 지닌 전형적인 특성을 보였습니다.",
        "그는 타인의 입장에서 공감하는 능력을 완전히 결여하고 있었으며, 주변 사람들을 자신의 나르시시즘을 충족시키기 위한 도구로만 바라보았습니다."
    ],
    '3.05': [
        "로렌의 이삿짐 상자들을 목격했을 때, 맥대니얼의 나르시시즘적 뇌는 급성 나르시시즘적 상처라는 치명적인 타격에 직면했습니다.",
        "통제라는 망상이 무너지는 것에 대한 공포는 대상을 자신의 손에서 영원히 벗어나게 두느니 차라리 파괴해 버리겠다는 병리적인 결론으로 그를 몰아갔습니다."
    ],
    '3.07': [
        "취조실에서 맥대니얼의 석상 같은 부동자세는 긴장성 부동이라 불리는 생물학적 반사를 의식적으로 모방한 것이었습니다.",
        "자연계에서 투쟁도 도주도 불가능함을 깨달은 생명체는 상대방의 주의를 무력화하기 위한 최후의 생존 전략으로 가사 상태에 빠지는 법입니다."
    ],
    '4.02': [
        "콘크리트 벽에 갇힌 3년간의 구금 생활은 전직 로스쿨생의 오만한 허세를 밑바닥까지 벗겨냈습니다.",
        "사법 정의를 속일 수 있다는 지능적 우월감의 망상은 흔들리지 않는 과학적 증거 앞에서 완전히 무너져 내렸습니다."
    ],
    '4.06': [
        "맥대니얼이 막판에 서명한 유죄 인정 합의는 결코 양심의 각성이나 진정한 참회에서 나온 것이 아니었습니다.",
        "그것은 공개 재판으로 갈 경우 배심원단에 의해 사형 판결이 내려질 것을 직감한 비겁한 생존 계산에 불과했습니다."
    ],
    '4.10': [
        "사건 이후, 건물의 보안 관리를 소홀히 했던 관계자들은 자신들의 부주의가 범행으로 가는 길을 열어주었다는 사실을 깨닫고 지울 수 없는 도덕적 상처를 짊어지게 되었습니다."
    ],
    '4.11': [
        "범죄심리학은 진정한 참회와 병리적인 자기연민 사이에 명확한 경계선을 긋습니다.",
        "맥대니얼이 흘린 드문 눈물은 산산조각 난 자신의 나르시시즘에 대한 연민이었을 뿐, 타인의 소중한 생명에 대한 공감은 결코 존재하지 않았습니다."
    ],
    '5.02': [
        "머서 대학교 학생 사회가 받은 충격은 미국 전역의 대학가에서 강력한 제도 개혁 운동으로 빠르게 승화되었습니다.",
        "학생들의 안전은 더 이상 안이한 전제에 방치되지 않고, 투명하고 엄격한 관리 기준에 의해 보장받게 되었습니다."
    ],
    '5.03': [
        "가장 값비싼 교훈은 시설 관리상의 허점을 결코 가볍게 여겨서는 안 된다는 점이며, 방치된 열쇠 하나가 범죄를 돕는 도구가 될 수 있다는 사실입니다."
    ],
    '5.04': [
        "생존을 위한 가장 위대한 진리는 직감적인 두려움이 결코 망상이 아니라 임박한 위험을 경고하는 진화의 신호라는 점입니다.",
        "사회적 예의를 차리느라 안전을 양보하는 대신, 그 직감을 용기 있게 믿고 단호한 방어 경계선을 설정하는 것이 무엇보다 중요합니다."
    ]
}

def apply_expansions_to_script(src_path, dst_path, add_map, lang):
    p = PK.parse_file(str(src_path))
    content = src_path.read_text(encoding="utf-8")
    
    # We update the header if needed (212 -> 241)
    if "212" in content:
        content = content.replace("212 câu thoại", "241 câu thoại")
        content = content.replace("212 câu", "241 câu")
        content = content.replace("212文", "241文")
        content = content.replace("212 sentences", "241 sentences")
        content = content.replace("212개 문장", "241개 문장")
        content = content.replace("212", "241")
        # Fix table roles if necessary
        if lang == "VN":
            content = re.sub(r"\|\s*\*\*H\*\*\s*\|\s*\*\*Dẫn chuyện \(Host\)\*\*\s*\|.*?\|\s*.*?\|\s*\*\*122\*\*\s*\|",
                             "| **H** | **Dẫn chuyện (Host)** | Amber Eyes Voice | Trầm ấm, lôi cuốn, sắc sảo, dẫn dắt thấu đáo | **132** |", content)
            content = re.sub(r"\|\s*\*\*D\*\*\s*\|\s*\*\*Điều tra viên\*\*\s*\|.*?\|\s*.*?\|\s*\*\*37\*\*\s*\|",
                             "| **D** | **Điều tra viên** | Điều tra viên (nhân vật minh hoạ) | Nam trung niên, dày dạn kinh nghiệm, điềm tĩnh, đanh thép | **43** |", content)
            content = re.sub(r"\|\s*\*\*C\*\*\s*\|\s*\*\*Chuyên gia Tâm lý\*\*\s*\|.*?\|\s*.*?\|\s*\*\*36\*\*\s*\|",
                             "| **C** | **Chuyên gia Tâm lý** | Chuyên gia Tâm lý học Pháp y | Điềm đạm, khách quan, giàu hàm lượng khoa học hành vi | **42** |", content)
            content = re.sub(r"\|\s*\*\*N1\*\*\s*\|\s*\*\*Người trong cuộc 1\*\*\s*\|.*?\|\s*.*?\|\s*\*\*8\*\*\s*\|",
                             "| **N1** | **Người trong cuộc 1** | Bạn học Trường Luật Mercer (Hồi 1) | Nữ thanh niên, bàng hoàng, chân thực, rùng mình | **10** |", content)
            content = re.sub(r"\|\s*\*\*TỔNG\*\*\s*\|\s*\*\*Toàn bộ kịch bản\*\*\s*\|.*?\|\s*.*?\|\s*\*\*.*?\*\*\s*\|",
                             "| **TỔNG** | **Toàn bộ kịch bản** | **5 Hồi chuẩn A2** | **Cân bằng hoàn hảo theo Golden Benchmark (>200 câu)** | **241** |", content)
        elif lang == "EN":
            content = re.sub(r"\|\s*\*\*H\*\*\s*\|\s*\*\*Narrator \(Host\)\*\*\s*\|.*?\|\s*.*?\|\s*\*\*122\*\*\s*\|",
                             "| **H** | **Narrator (Host)** | Amber Eyes Voice | Deep, engaging, insightful storytelling | **132** |", content)
            content = re.sub(r"\|\s*\*\*D\*\*\s*\|\s*\*\*Lead Detective\*\*\s*\|.*?\|\s*.*?\|\s*\*\*37\*\*\s*\|",
                             "| **D** | **Lead Detective** | Forensic Investigator | Experienced, steady, cold procedural clarity | **43** |", content)
            content = re.sub(r"\|\s*\*\*C\*\*\s*\|\s*\*\*Psychologist\*\*\s*\|.*?\|\s*.*?\|\s*\*\*36\*\*\s*\|",
                             "| **C** | **Psychologist** | Forensic Behavioral Expert | Calm, academic, rigorous behavioral insights | **42** |", content)
            content = re.sub(r"\|\s*\*\*N1\*\*\s*\|\s*\*\*Person Involved 1\*\*\s*\|.*?\|\s*.*?\|\s*\*\*8\*\*\s*\|",
                             "| **N1** | **Person Involved 1** | Mercer Law Classmate (Act 1) | Young female, shaken, authentic, chilled | **10** |", content)
            content = re.sub(r"\|\s*\*\*TOTAL\*\*\s*\|\s*\*\*Complete Script\*\*\s*\|.*?\|\s*.*?\|\s*\*\*.*?\*\*\s*\|",
                             "| **TOTAL** | **Complete Script** | **5 Acts Standard A2** | **Perfect 4-Language Parity Benchmark** | **241** |", content)
        elif lang == "JA":
            content = re.sub(r"\|\s*\*\*H\*\*\s*\|\s*\*\*ホスト \(Host\)\*\*\s*\|.*?\|\s*.*?\|\s*\*\*122\*\*\s*\|",
                             "| **H** | **ホスト (Host)** | Amber Eyes Voice | 落ち着き、深み、説得力に富んだ物語の語り手 | **132** |", content)
            content = re.sub(r"\|\s*\*\*D\*\*\s*\|\s*\*\*捜査官\*\*\s*\|.*?\|\s*.*?\|\s*\*\*37\*\*\s*\|",
                             "| **D** | **捜査官** | 殺人課刑事（モデル人物） | 熟練、冷徹、客観的、科学捜査の確証 | **43** |", content)
            content = re.sub(r"\|\s*\*\*C\*\*\s*\|\s*\*\*心理学者\*\*\s*\|.*?\|\s*.*?\|\s*\*\*36\*\*\s*\|",
                             "| **C** | **心理学者** | 司法精神医学・行動科学専門家 | 知的、沈着、臨床的で深い行動洞察 | **42** |", content)
            content = re.sub(r"\|\s*\*\*N1\*\*\s*\|\s*\*\*一般人 1\*\*\s*\|.*?\|\s*.*?\|\s*\*\*8\*\*\s*\|",
                             "| **N1** | **一般人 1** | マーサー大学ロースクール同期生（第1幕） | 若い女性、動揺、真実味、戦慄 | **10** |", content)
            content = re.sub(r"\|\s*\*\*合計\*\*\s*\|\s*\*\*全編\*\*\s*\|.*?\|\s*.*?\|\s*\*\*.*?\*\*\s*\|",
                             "| **合計** | **全編** | **5幕構成 標準A2** | **4言語完全一致 パリティ基準（241文）** | **241** |", content)
        elif lang == "KO":
            content = re.sub(r"\|\s*\*\*H\*\*\s*\|\s*\*\*진행자 \(Host\)\*\*\s*\|.*?\|\s*.*?\|\s*\*\*122\*\*\s*\|",
                             "| **H** | **진행자 (Host)** | Amber Eyes Voice | 차분하고 깊이 있는 통찰의 내레이터 | **132** |", content)
            content = re.sub(r"\|\s*\*\*D\*\*\s*\|\s*\*\*수사관\*\*\s*\|.*?\|\s*.*?\|\s*\*\*37\*\*\s*\|",
                             "| **D** | **수사관** | 강력계 형사 (재구성 인물) | 노련하고 냉철하며 객관적인 과학수사 | **43** |", content)
            content = re.sub(r"\|\s*\*\*C\*\*\s*\|\s*\*\*프로파일러\*\*\s*\|.*?\|\s*.*?\|\s*\*\*36\*\*\s*\|",
                             "| **C** | **프로파일러** | 사법정신의학·행동과학 전문가 | 지적이고 침착하며 깊이 있는 행동 분석 | **42** |", content)
            content = re.sub(r"\|\s*\*\*N1\*\*\s*\|\s*\*\*일반인 1\*\*\s*\|.*?\|\s*.*?\|\s*\*\*8\*\*\s*\|",
                             "| **N1** | **일반인 1** | 머서 로스쿨 동기 (1막) | 젊은 여성, 충격, 생생함, 전율 | **10** |", content)
            content = re.sub(r"\|\s*\*\*총합\*\*\s*\|\s*\*\*전체 대본\*\*\s*\|.*?\|\s*.*?\|\s*\*\*.*?\*\*\s*\|",
                             "| **총합** | **전체 대본** | **5막 구성 표준 A2** | **4개 언어 완벽 일치 기준 (241문장)** | **241** |", content)

    # For each element with additions, locate the last sentence of that element and append additions after it
    for elem_id, new_sents in add_map.items():
        # find the element in p
        target_elem = next((e for e in p if e["id"] == elem_id), None)
        if not target_elem or target_elem["kind"] != "LOI":
            print(f"Error: element {elem_id} not found in {lang}")
            continue
        last_sent = target_elem["sentences"][-1]["text"]
        
        # We append the new sentences right after last_sent in the text
        addition_text = "\n" + "\n".join(new_sents)
        if last_sent in content:
            content = content.replace(last_sent, last_sent + addition_text, 1)
        else:
            print(f"Warning: could not find exact last_sent for {elem_id} in {lang}: {last_sent[:30]}")

    dst_path.parent.mkdir(parents=True, exist_ok=True)
    dst_path.write_text(content, encoding="utf-8", newline="\n")
    print(f"Updated {lang} -> {dst_path.relative_to(ROOT)}")

def main():
    targets = [
        ("VN", ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_23102026.md", ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_23102026.md", VN_ADD),
        ("EN1", ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_EN.md", ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_EN.md", EN_ADD),
        ("EN2", ROOT / "01_KICH_BAN" / "Tap20_EN" / "kichban_tap20_EN.md", ROOT / "01_KICH_BAN" / "Tap20_EN" / "kichban_tap20_EN.md", EN_ADD),
        ("JA1", ROOT / "01_KICH_BAN" / "Tap20_JA" / "kichban_tap20_JA.md", ROOT / "01_KICH_BAN" / "Tap20_JA" / "kichban_tap20_JA.md", JA_ADD),
        ("JA2", ROOT / "01_KICH_BAN" / "Tap20_JA" / "kichban_tap20_JA.md", ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_JA.md", JA_ADD),
        ("KO", ROOT / "01_KICH_BAN" / "Tap20_KO" / "kichban_tap20_KO.md", ROOT / "01_KICH_BAN" / "Tap20_KO" / "kichban_tap20_KO.md", KO_ADD),
    ]

    for label, src, dst, add_map in targets:
        apply_expansions_to_script(src, dst, add_map, label[:2])

if __name__ == "__main__":
    main()
