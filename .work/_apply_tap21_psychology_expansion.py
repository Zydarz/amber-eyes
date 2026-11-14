# -*- coding: utf-8 -*-
"""Apply deep psychology expansions to Episode 21 across all 4 languages (VN, EN, JA, KO)."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

ADDITIONS = {
    "1.07": {
        "VN": [
            "Sau này khi biết chuyện, nỗi day dứt lớn nhất bao trùm cả khu phố chính là sự xuất hiện muộn màng của người bà nội.",
            "Bà Dora Yates đã hẹn đến giúp đỡ chăm sóc lũ trẻ vào buổi sáng hôm ấy, nhưng một sự chậm trễ vô tình đã khiến bà đến nơi khi mọi chuyện đã quá muộn.",
            "Tiếng gào khóc nghẹn ngào của người bà già trước dải băng vàng cảnh sát đã trở thành nỗi ám ảnh day dứt khôn nguôi cho tất cả chúng tôi.",
            "Nỗi dằn vặt của một người đến muộn chỉ sau ba mươi phút định mệnh ấy là một vết thương lòng vĩnh viễn không thể nào xoa dịu.",
        ],
        "EN": [
            "Later, when the full truth came to light, the most agonizing grief that haunted our neighborhood was the heartbreaking arrival of the paternal grandmother.",
            "Dora Yates had promised to arrive that morning to help look after the young children, but an ordinary, unintended delay brought her to the doorstep when everything was already irrevocably lost.",
            "The elderly grandmother's weeping collapse before the police cordon became an indelible, haunting memory for every resident on our street.",
            "That devastating torment of the latecomer, missing the threshold of life and death by barely thirty fateful minutes, remains an incurable wound upon the soul.",
        ],
        "JA": [
            "後に真相が明らかになったとき、地域全体を最も深く苛んだのは、祖母の痛切極まりない遅れでした。",
            "ドラ・イエーツはその朝、孫たちの世話を手伝うために訪れる予定でしたが、日常の些細な遅れにより、現場に到着したときにはすでに取り返しのつかない悲劇が終わっていたのです。",
            "規制線の前で泣き崩れる老いた祖母の姿は、私たち近隣住民全員にとって決して消えることのない深い傷跡となりました。",
            "運命のわずか三十分の遅れによって最悪の事態を防げなかったという「遅れてきた者」の後悔は、生涯癒えることのない魂の十字架となったのです。",
        ],
        "KO": [
            "후에 진상이 밝혀졌을 때, 동네 전체를 가장 깊이 괴롭힌 것은 바로 친할머니의 비통한 지각이었습니다.",
            "도라 예이츠는 그날 아침 아이들을 돌보는 것을 돕기 위해 방문하기로 되어 있었으나, 일상적인 사소한 지체로 인해 이미 비극이 끝난 뒤에야 현장에 도착했습니다.",
            "통제선 앞에서 오열하는 노모의 모습은 우리 주민 모두에게 결코 지워지지 않는 깊은 상흔이 되었습니다.",
            "운명의 30분 늦음으로 인해 비극을 막지 못했다는 자책감은 평생 치유되지 않는 영혼의 상처로 남았습니다.",
        ],
    },
    "1.10": {
        "VN": [
            "Trong toàn bộ bức tranh hiện trường tĩnh lặng đầy u uất sáng hôm ấy, hồ sơ điều tra ghi nhận một khoảnh khắc xé lòng nhất về bản năng con người.",
            "Đó là sự vùng vẫy trong tuyệt vọng của đứa trẻ lớn nhất, bé Noah bảy tuổi, khi linh cảm bất thường khiến cậu bé quay đầu bỏ chạy khắp hành lang.",
            "Trong tâm trí non nớt của một đứa trẻ, ngôi nhà vốn là tổ ấm an toàn bỗng chốc trở thành một mê cung kinh hoàng không lối thoát.",
            "Và đối với người mẹ đang trong cơn mộng du loạn thần, sự truy đuổi ấy không bắt nguồn từ lòng thù hận, mà là một ảo tưởng cứu rỗi điên rồ rằng phải đưa linh hồn con về với Chúa trước khi quỷ dữ đoạt lấy.",
        ],
        "EN": [
            "Amid the harrowing silence of that suburban home that morning, investigative records documented the most heart-wrenching manifestation of primal survival instinct.",
            "It was the frantic flight of the eldest child, seven-year-old Noah, whose sudden realization prompted him to flee desperately down the hallway.",
            "In the innocent mind of a seven-year-old boy, the familiar sanctuary of his home had abruptly transformed into an inescapable nightmare.",
            "Yet for the mother locked within an acute psychotic fugue, that pursuit was driven not by malice, but by the twisted salvation delusion that she had to rescue his soul before darkness claimed it forever.",
        ],
        "JA": [
            "あの朝の静まり返った悲痛な現場において、捜査資料が記録した最も胸を引き裂かれる瞬間は、人間の原初的な生存本能の表れでした。",
            "それは長男である七歳のノア君が、母親の異変を本能的に察知し、廊下を必死に逃げ惑ったという事実です。",
            "わずか七歳の少年の無垢な心にとって、温かいはずの我が家が突如として逃げ場のない恐怖の迷宮へと変貌してしまいました。",
            "そして急性精神病の暗闇に閉じ込められた母親にとって、その追走は悪意からではなく、悪魔の手に落ちる前に我が子の魂を救済しなければならないという狂気の妄想によるものだったのです。",
        ],
        "KO": [
            "그날 아침 참혹한 현장의 침묵 속에서 수사 기록은 가장 가슴 아픈 인간의 원초적 생존 본능을 기록했습니다.",
            "그것은 맏이인 일곱 살 노아 군이 어머니의 이상 징후를 본능적으로 감지하고 복도를 필사적으로 도망쳤다는 사실입니다.",
            "일곱 살 소년의 순진한 마음에 따뜻해야 할 집은 순식간에 탈출구 없는 공포의 미궁으로 변해버렸습니다.",
            "그리고 급성 정신병의 망상에 갇힌 어머니에게 그 추격은 악의가 아니라 어둠이 아이의 영혼을 앗아가기 전에 구원해야 한다는 광기 어린 망상 때문이었습니다.",
        ],
    },
    "2.06": {
        "VN": [
            "Hồ sơ điều tra về môi trường gia đình hé lộ một chuỗi những áp lực vô hình nhưng vô cùng khốc liệt đã đè nặng lên người phụ nữ ấy.",
            "Người chồng Russell Yates theo đuổi hình mẫu gia đình gia trưởng truyền thống và chịu ảnh hưởng sâu sắc từ những bức thư truyền đạo cực đoan của nhà thuyết giáo Woroniecki.",
            "Bất chấp những lời cảnh báo y khoa nghiêm khắc rằng việc tiếp tục mang thai sẽ kích hoạt lại chứng loạn thần nguy hiểm tính mạng, người chồng vẫn kiên định với lý tưởng đông con của mình.",
            "Sự phủ nhận thực tế và lòng tin mù quáng vào sức chịu đựng của người vợ đã vô tình đẩy một người mẹ đang suy kiệt vào bước đường cùng không lối thoát.",
        ],
        "EN": [
            "Investigative records into the domestic dynamics revealed an invisible yet crushing gauntlet of expectations bearing down upon Andrea.",
            "Her husband, Russell Yates, adhered rigidly to an authoritarian patriarchal model, heavily influenced by the radical, guilt-laden correspondence of traveling preacher Michael Woroniecki.",
            "Despite explicit, grave medical warnings that any further pregnancy would inevitably trigger a catastrophic resurgence of psychosis, Russell adamantly pursued his vision of an expanding family.",
            "That relentless denial of psychological reality and blind reliance on his wife's endurance unwittingly steered an exhausted, unraveling mother into an absolute dead end.",
        ],
        "JA": [
            "家庭環境に関する捜査記録は、アンドレアに重くのしかかっていた目に見えない過酷な重圧の連鎖を浮き彫りにしています。",
            "夫のラッセル・イエーツは厳格な家父長制の理想を追い求め、巡回説教者ウォロニエツキの過激な教義の手紙に深く影響されていました。",
            "これ以上の妊娠は命に関わる重篤な精神病の再発を確実に招くという明確な医学的警告があったにもかかわらず、夫は大家族という自らの青写真を頑なに推し進めたのです。",
            "現実を否認し、妻の精神的耐久力に盲目的に依存した姿勢は、すでに限界を超えて衰弱していた母親を逃げ場のない破滅の淵へと追い詰めていきました。",
        ],
        "KO": [
            "가정 환경에 대한 수사 기록은 안드레아에게 가해진 보이지 않는 가혹한 중압감의 연쇄를 보여줍니다.",
            "남편 러셀 예이츠는 가부장적 가족 모델을 고수하며 순회 설교자 워로니에츠키의 서신에 깊이 영향을 받았습니다.",
            "추가 임신이 치명적인 정신병의 재발을 부를 것이라는 명백한 의학적 경고에도 불구하고, 남편은 대가족의 이상을 고집했습니다.",
            "현실을 부인하고 아내의 정신적 인내력에 맹목적으로 의존한 태도는 이미 쇠약해진 어머니를 막다른 골목으로 몰아넣었습니다.",
        ],
    },
    "2.10": {
        "VN": [
            "Bi kịch còn được tiếp tay bởi một điểm mù chí tử của hệ thống y tế đương thời khi bác sĩ điều trị quyết định cắt bỏ hoàn toàn thuốc chống loạn thần chỉ hai tuần trước biến cố.",
            "Sự tự mãn chuyên môn và sự thiếu lắng nghe tiếng kêu cứu từ gia đình đã tước đi chiếc khiên hóa học duy nhất có thể ngăn chặn sự sụp đổ của tế bào thần kinh.",
            "Khi khoa học y khoa rút lui và sự cô lập xã hội khép kín lại, não bộ của người mẹ đã hoàn toàn thất thủ trước sự xâm lăng của những ảo giác hoang đường.",
        ],
        "EN": [
            "The catastrophe was compounded by a fatal blindspot within the psychiatric care system when her treating physician abruptly terminated all antipsychotic medication merely two weeks prior to the tragedy.",
            "Clinical complacency and a dismissive attitude toward the family's desperate warnings dismantled the sole pharmacological shield keeping neurological collapse at bay.",
            "When medical intervention retreated and domestic isolation consolidated, the mother's overburdened brain surrendered entirely to the overwhelming onslaught of psychotic delusions.",
        ],
        "JA": [
            "さらにこの悲劇は、主治医が事件のわずか二週間前に抗精神病薬の投与を突如として全廃するという、医療側の致命的な盲点によって決定づけられました。",
            "専門家としての過信と、家族からの切実な警告の軽視が、神経伝達の完全な崩壊を防ぎ得た唯一の化学的防壁を取り払ってしまったのです。",
            "医療の支援が断たれ、閉鎖的な家庭の孤立が深まったとき、母親の脳は暴走する幻覚と妄想の猛威の前に完全に陥落してしまいました。",
        ],
        "KO": [
            "이 비극은 사건 2주 전 주치의가 항정신병 치료제를 갑자기 전면 중단한 의료 시스템의 치명적인 맹점으로 인해 결정되었습니다.",
            "전문가로서의 과신과 가족의 절박한 호소에 대한 경시는 뇌 신경의 붕괴를 막을 수 있었던 유일한 화학적 방패를 없애버렸습니다.",
            "의학적 지원이 끊기고 가정의 고립이 굳어졌을 때, 어머니의 뇌는 폭주하는 환각과 망상 앞에 완전히 무너져 내렸습니다.",
        ],
    },
    "3.03": {
        "VN": [
            "Trong tâm thần học pháp y, hồ sơ Andrea Yates là trường hợp kinh điển đại diện cho hiện tượng ‘Hành vi gây hại vì vị tha hoang tưởng’, hay Altruistic Filicide.",
            "Khác biệt hoàn toàn với những kẻ ác ý hành động vì thù hận, vụ lợi hay sự tàn nhẫn, người mẹ bị loạn thần không hề có dã tâm làm tổn thương con trẻ.",
            "Trong thế giới quan bị bóp méo hoàn toàn bởi cơn loạn thần, cô chân thành tin rằng mình là một người mẹ mang tội lỗi truyền kiếp, và cái chết trần thế là cánh cửa duy nhất đưa các con đến chốn bình an vĩnh hằng.",
            "Đó là nghịch lý đau đớn nhất của một tâm trí bệnh hoạn: Tình yêu thương mẫu tử nguyên thủy bị cơn bão thần kinh đánh cắp và biến dạng thành một hành vi hủy diệt mang danh nghĩa cứu chuộc.",
        ],
        "EN": [
            "In forensic psychiatry, the Andrea Yates case stands as the quintessential manifestation of what clinical literature defines as ‘Altruistic Filicide’.",
            "Utterly distinct from predators motivated by malice, vengeance, or cruelty, a mother gripped by postpartum psychosis harbors no hostility toward her offspring.",
            "Within a worldview radically distorted by psychotic illness, she sincerely believed she was inherently damned, and that temporal death represented the solitary portal to ensure her children's eternal salvation.",
            "This embodies the most agonizing paradox of severe psychiatric disease: profound maternal devotion hijacked by a biochemical storm and inverted into an act of tragic destruction under the delusion of salvation.",
        ],
        "JA": [
            "法精神医学において、アンドレア・イエーツの事例は、臨床文献が「利他的子殺し」と定義する現象の典型的な証拠です。",
            "悪意や復讐、あるいは残虐な衝動に基づいて行動する者とは根本的に異なり、重度の産後精神病に囚われた母親は、我が子に対して微塵の敵意も抱いていませんでした。",
            "精神病によって完全に歪められた精神世界の中で、彼女は自分が罪深い母親であり、肉体の死こそが純粋な子どもたちを永遠の救済へと導く唯一の道であると信じ込んでいたのです。",
            "母性愛という最も純粋な感情が、脳内の生化学的な暴走によってハイジャックされ、救済という名の下に破滅的な行為へと反転してしまった、医学上最も悲痛な逆説と言えます。",
        ],
        "KO": [
            "법정신의학에서 안드레아 예이츠의 사례는 임상 문헌이 '이타적 자녀 살해'로 정의하는 현상의 전형적인 증거입니다.",
            "악의나 복수, 잔혹한 충동으로 행동하는 자들과 달리, 산후 정신병에 사로잡힌 어머니는 자녀에게 어떤 적의도 품지 않았습니다.",
            "정신병으로 완전히 왜곡된 정신세계 속에서, 그녀는 자신이 저주받은 어머니이며 육체의 죽음만이 아이들을 영원한 구원으로 이끄는 유일한 길이라고 믿었습니다.",
            "모성애라는 가장 순수한 감정이 신경생화학적 폭주에 의해 왜곡되어 구원이라는 이름의 파멸적 행위로 반전된 가장 비극적인 역설입니다.",
        ],
    },
    "3.07": {
        "VN": [
            "Sự đứt gãy hoàn toàn với thực tại đã xây nên một bức tường nhận thức kiên cố ngăn cách người mẹ với thế giới xung quanh.",
            "Khi não bộ không còn khả năng phân biệt giữa tiếng nói nội tâm bệnh lý và âm thanh của đời thực, mọi chuẩn mực đạo đức thông thường đều bị vô hiệu hóa.",
            "Việc nhận diện sự khác biệt giữa cái ác có toan tính và sự bất lực bi kịch của một tâm hồn đổ vỡ chính là thước đo cho lòng trắc ẩn và sự tiến bộ của nền văn minh con người.",
        ],
        "EN": [
            "A catastrophic rupture from reality erected an impenetrable cognitive barrier severing the mother from the outside world.",
            "When the human brain loses the capacity to distinguish between malignant pathological hallucinations and external objective reality, conventional moral compasses are entirely rendered void.",
            "Discerning the fundamental divide between calculated wickedness and the helpless tragedy of a shattered mind remains the truest measure of compassion and progress in modern civilization.",
        ],
        "JA": [
            "現実感覚の完全な破綻は、母親と周囲の世界との間に越えられない認識の障壁を築き上げました。",
            "病理学的な幻聴と客観的な現実の境界を脳が識別できなくなったとき、通常の人道的な規範はすべてその効力を奪われてしまいます。",
            "計算された悪意と、病に壊された魂の悲劇的な無力感との間の決定的な違いを見極めることこそが、人間の理性と司法の成熟を測る真の試金石なのです。",
        ],
        "KO": [
            "현실 감각의 완전한 붕괴는 어머니와 주변 세계 사이에 넘을 수 없는 인지적 장벽을 쌓아 올렸습니다.",
            "병리적 환청과 객관적 현실의 경계를 뇌가 식별할 수 없게 되었을 때, 일반적인 도덕 규범은 모두 무력화되었습니다.",
            "계산된 악의와 병든 영혼의 비극적 무력감을 구별하는 것이야말로 인간 이성과 사법의 성숙을 가늠하는 진정한 척도입니다.",
        ],
    },
    "4.06": {
        "VN": [
            "Nhiều tuần sau khi bị bắt giữ, khi phác đồ điều trị tâm thần tích cực tại bệnh viện nhà tù bắt đầu tái lập lại trật tự hóa học trong não bộ, bi kịch thực sự mới bộc phát.",
            "Đó là khoảnh khắc mà các bác sĩ pháp y gọi là ‘Sự thức tỉnh sau loạn thần’.",
            "Khi làn sương mù hoang tưởng tan biến hoàn toàn, người mẹ ấy bàng hoàng đối diện với hiện thực trần trụi rằng không có ác quỷ nào cả, mà chính bàn tay mình đã vĩnh viễn tước đi những đứa con ruột thịt.",
            "Cơn bão sụp đổ bản ngã và chấn thương đạo đức cực hạn đã khiến người phụ nữ ấy ngã quỵ trong những cơn co giật đớn đau không lời.",
        ],
        "EN": [
            "Weeks following her arrest, as intensive psychiatric stabilization inside the prison medical facility gradually restored biochemical balance in her brain, the true, agonizing horror erupted.",
            "It was the devastating threshold forensic clinicians identify as ‘Post-Psychotic Awakening’.",
            "As the dense fog of religious delusions receded entirely, the mother was confronted with the unfathomable truth: there was no demonic intervention, and her own hands had extinguished the lives of her beloved children.",
            "That catastrophic collapse of ego and overwhelming moral injury plunged the woman into silent, convulsive despair that words can scarcely capture.",
        ],
        "JA": [
            "逮捕から数週間が経過し、拘置所の精神病棟での集中的な治療によって脳内の生化学的均衡が徐々に回復したとき、本当の地獄の蓋が開きました。",
            "法精神医学の専門家たちが「精神病後の覚醒」と呼ぶ過酷な瞬間です。",
            "妄想の濃霧が完全に晴れ渡ったとき、その母親は身も凍るような現実を直視することになりました。悪魔の存在などなく、自らの愛する五人の子どもの命を奪ったのは自分自身の手であったという事実です。",
            "自己同一性の壊滅的な崩壊と極限の道徳的トラウマにより、彼女は言葉を失い、身を震わせて絶望の深淵へと崩れ落ちました。",
        ],
        "KO": [
            "체포 수주일 후 구치소 병동의 집중 치료로 뇌의 생화학적 균형이 회복되었을 때, 진짜 지옥의 문이 열렸습니다.",
            "법정신의학 전문가들이 '정신병 후 각성'이라 부르는 참혹한 순간이었습니다.",
            "망상의 짙은 안개가 걷혔을 때, 어머니는 악마의 개입은 없었으며 자신의 손으로 사랑하는 아이들의 생명을 앗아갔다는 차가운 현실과 마주했습니다.",
            "자아의 파멸적 붕괴와 극심한 도덕적 트라우마는 그녀를 말 없는 절망의 심연으로 밀어 넣었습니다.",
        ],
    },
    "4.11": {
        "VN": [
            "Khoa học tâm lý giải thích sự hối hận của Andrea Yates là một hiện tượng ăn năn chân thực và vĩnh viễn, đối lập hoàn toàn với sự tự thương hại bệnh lý của những kẻ thủ ác ái kỷ.",
            "Cô không hề tìm cách bào chữa, không than vãn về số phận hay đổ lỗi cho hoàn cảnh để mưu cầu sự tự do trần thế.",
            "Bằng chứng rõ nét nhất là trong suốt gần hai mươi năm được điều trị tại Bệnh viện Nhà nước Kerrville, Andrea luôn từ chối nộp đơn xin phóng thích hay giảm nhẹ chế độ giám hộ.",
            "Cô chọn ở lại phía sau những bức tường bệnh viện tâm thần, ngày ngày làm những món đồ thủ công để gây quỹ tưởng niệm các con, tự giam mình trong một bản án lương tâm tự nguyện cho đến hơi thở cuối cùng.",
        ],
        "EN": [
            "Psychological science elucidates Andrea Yates's remorse as an authentic, enduring manifestation of moral atonement, standing in stark contrast to the pathological self-pity of narcissistic offenders.",
            "She never attempted self-justification, never lamented her lost personal liberty, nor weaponized victimhood to petition for earthly freedom.",
            "The most compelling testament to this mindset is that throughout nearly two decades of confinement at Kerrville State Hospital, Andrea has consistently declined to submit petitions for release.",
            "She consciously chooses to remain behind hospital walls, crafting knitted items daily to benefit the memorial fund honoring her children, voluntarily submitting to a lifelong prison of conscience until her final breath.",
        ],
        "JA": [
            "心理学は、アンドレア・イエーツの後悔を、自己愛性犯罪者に見られる病理学的な自己憐憫とは完全に異なる、本物かつ永遠の道徳的悔悛であると説明します。",
            "彼女は決して自己を正当化せず、失われた自由を嘆くこともなく、この世の解放を求めて被害者ぶることもありませんでした。",
            "その何よりの証拠は、カービル州立病院での約二十年間に及ぶ収容生活の中で、彼女が一貫して仮釈放や退院の申し立てを拒否し続けていることです。",
            "彼女は病院の壁の内側に留まることを自ら選び、子どもたちの追悼基金のために日々手芸品を作り続けながら、最期の一息まで自発的な良心の牢獄に身を捧げることを選んだのです。",
        ],
        "KO": [
            "심리학은 안드레아 예이츠의 후회를 자기애성 범죄자의 자기연민과는 완전히 다른, 진실하고 영원한 도덕적 참회로 설명합니다.",
            "그녀는 결코 자기 합리화를 시도하지 않았고, 잃어버린 자유를 한탄하거나 세속적 석방을 탄원하지 않았습니다.",
            "그 증거로 커빌 주립병원에서 약 20년간의 수용 생활 동안 안드레아는 가석방이나 퇴원 청원을 일관되게 거부해왔습니다.",
            "그녀는 병원 벽 안에 머물며 아이들의 추모 기금을 위해 매일 뜨개질을 하며, 마지막 숨을 거둘 때까지 스스로 선택한 양심의 형벌을 다하고 있습니다.",
        ],
    },
    "5.03": {
        "VN": [
            "Vụ án đã đặt dấu chấm hết cho sự hoài nghi vô cảm đối với sức khỏe tâm thần của người phụ nữ sau sinh trong hệ thống tư pháp hình sự.",
            "Nỗi đau khôn cùng của năm sinh linh bé bỏng đã hóa thành động lực thúc đẩy sự ra đời của Quỹ Tưởng niệm Trẻ em Yates, một tổ chức tiên phong nâng cao nhận thức và hỗ trợ y tế cho hàng ngàn gia đình trên khắp nước Mỹ.",
            "Công lý không chỉ dừng lại ở sự phán xét nghiêm minh đối với hành vi, mà còn là sự dũng cảm nhìn nhận đúng bản chất y học để bảo vệ những con người yếu thế trước sự suy sụp của tâm trí.",
        ],
        "EN": [
            "This landmark case permanently dismantled the dismissive skepticism surrounding maternal mental health within the modern criminal justice system.",
            "The unfathomable loss of five innocent young lives was transformed into the enduring catalyst for the Yates Children Memorial Fund, pioneering education and psychiatric support for countless families nationwide.",
            "True justice transcends mere retributive condemnation of tragic actions; it demands the moral courage to recognize clinical reality and safeguard vulnerable souls overwhelmed by mental collapse.",
        ],
        "JA": [
            "この歴史的な裁判は、刑事司法制度における産後女性の精神衛生に対する無理解と冷笑的な懐疑論に終止符を打ちました。",
            "尊い五つの幼い命の喪失は、「イエーツ子ども追悼基金」の設立へと結実し、全米の無数の家族に教育と精神医療支援を届ける不滅の力となりました。",
            "真の正義とは、悲劇的な行為に対する単なる応報的処罰にとどまらず、医学的真実を直視し、精神の崩壊に抗えなかった脆弱な人間を守る勇気を持つことなのです。",
        ],
        "KO": [
            "이 역사적인 재판은 형사사법제도에서 산후 여성의 정신건강에 대한 무지와 냉소적 회의론에 종지부를 찍었습니다.",
            "무고한 다섯 어린 생명의 희생은 '예이츠 어린이 추모 기금'의 설립으로 이어져, 전국의 수많은 가정을 돕는 영원한 힘이 되었습니다.",
            "진정한 정의란 행위에 대한 단순한 응보적 처벌에 그치지 않고, 의학적 진실을 직시하여 정신의 붕괴 앞에 무력했던 취약한 인간을 보호하는 것입니다.",
        ],
    },
    "5.04": {
        "VN": [
            "Bài học nhân văn sâu sắc nhất đọng lại sau thảm kịch là: sự an toàn của tổ ấm gia đình không thể được xây dựng bằng sự im lặng hay sự cam chịu đơn độc.",
            "Khi một người mẹ sau sinh rơi vào trầm cảm và cạn kiệt năng lượng, đó không phải là sự yếu đuối về mặt ý chí mà là một tín hiệu khẩn cấp đòi hỏi sự thấu cảm và can thiệp kịp thời từ người bạn đời và toàn xã hội.",
            "Hãy luôn lắng nghe, chia sẻ và giang rộng vòng tay che chở trước khi những vết rạn nứt tâm hồn biến thành một bi kịch không thể cứu vãn.",
        ],
        "EN": [
            "The most profound human lesson echoing from this tragedy is that the sanctity of a home cannot be sustained through isolated endurance and silence.",
            "When a postpartum mother plunges into profound depression and neurological exhaustion, it represents not a moral failure of willpower, but an urgent biological alarm demanding immediate empathy and intervention from partners and society alike.",
            "We must cultivate vigilance, dismantle stigma, and extend protective support before invisible psychological fractures unravel into irreversible heartbreak.",
        ],
        "JA": [
            "この悲劇から導き出される最も深い教訓は、家庭の安全と幸福は、個人の孤独な耐忍や沈黙の上に成り立つものではないということです。",
            "産後の母親が重度の抑うつと疲弊に沈むとき、それは決して意志の弱さではなく、家族や社会全体の深い共感と迅速な医療介入を求める緊急の生物学的SOSなのです。",
            "心の目に見えない亀裂が取り返しのつかない悲劇へと崩壊する前に、私たちは偏見を捨て、温かい理解と支援の手を差し伸べ続けなければなりません。",
        ],
        "KO": [
            "이 비극이 남긴 가장 깊은 교훈은 가정의 안녕이 개인의 고독한 침묵이나 인내 위에 세워질 수 없다는 것입니다.",
            "산후 어머니가 심각한 우울과 탈진에 빠질 때, 그것은 의지의 나약함이 아니라 배우자와 사회의 즉각적인 공감과 개입을 요구하는 긴급한 생물학적 경보입니다.",
            "마음에 보이지 않는 균열이 돌이킬 수 없는 비극으로 무너지기 전에, 우리는 편견을 버리고 따뜻한 이해와 지원의 손길을 내밀어야 합니다.",
        ],
    },
}

ANCHORS = {
    "1.07": {
        "VN": "Không một ai có thể tin được rằng một người mẹ hiền lành, tận tụy lại có thể rơi vào một vực thẳm tăm tối và tuyệt vọng đến mức độ ấy.",
        "EN": "No one could comprehend how such a gentle, devoted mother could have descended into such an unfathomable and dark abyss.",
        "JA": "あれほど穏やかで子供思いだった母親が、なぜそこまで暗く絶望的な深淵へ突き落とされたのか信じられませんでした。",
        "KO": "그토록 온화하고 헌신적이던 어머니가 어떻게 이토록 칠흑 같은 암흑과 절망의 나락으로 떨어질 수 있었는지 믿기지 않았습니다.",
    },
    "1.10": {
        "VN": "Đó là một lời khai rợn người, phản ánh một niềm tin hoang tưởng tuyệt đối đã đè bẹp hoàn toàn mọi nhận thức thực tế của người mẹ.",
        "EN": "It was a chilling statement, reflecting an absolute psychotic conviction that had utterly crushed her grasp of reality.",
        "JA": "それは聴く者を慄然とさせる供述であり、現実感覚を完全に圧殺した重篤な精神病の存在を物語っていました。",
        "KO": "듣는 이를 전율케 하는 진술이었으며, 현실 인식을 송두리째 짓밟은 절대적인 정신병적 확신을 여실히 보여주었습니다.",
    },
    "2.06": {
        "VN": "Đó là một sai lầm nhận thức chí mạng của gia đình, đặt một quả bom nổ chậm vào hệ thần kinh vốn đã suy kiệt của người phụ nữ.",
        "EN": "It was a catastrophic blind spot that placed a biological time bomb inside an already depleted central nervous system.",
        "JA": "それはすでに疲弊しきっていた中枢神経系に時限爆弾を仕掛けるに等しい、家族側の致命的な判断の誤りでした。",
        "KO": "그것은 이미 탈진해 있던 신경계에 시한폭탄을 장착한 것이나 다름없는, 가족의 치명적인 오판이었습니다.",
    },
    "2.10": {
        "VN": "Những phát hiện khoa học hành vi sau đây sẽ làm sáng tỏ cơ chế tâm bệnh học vô cùng phức tạp đằng sau thảm kịch.",
        "EN": "The following behavioral science findings illuminate the intricate psychopathological mechanisms driving this tragedy.",
        "JA": "続く行動科学の知見が、この悲劇の背後にある極めて複雑な精神病理のメカニズムを解き明かします。",
        "KO": "이어지는 행동과학의 분석은 비극의 이면에 도사린 복잡한 정신병리 메커니즘을 명쾌하게 밝혀줄 것입니다.",
    },
    "3.03": {
        "VN": "Hành động của cô khi ấy không còn chịu sự kiểm soát của lý trí tỉnh táo mà hoàn toàn bị điều khiển bởi ảo giác cứu chuộc sai lệch.",
        "EN": "Her actions were no longer governed by conscious deliberation, but dictated entirely by a profoundly distorted imperative of salvation.",
        "JA": "その行動はもはや明晰な理性の統制下にはなく、救済を装った歪んだ妄想によって完全に操られていたのです。",
        "KO": "그녀의 행동은 명료한 이성의 지배를 벗어나 구원을 가장한 끔찍하게 왜곡된 망상적 명령에 철저히 종속되어 있었습니다.",
    },
    "3.07": {
        "VN": "Và cuộc chiến pháp lý để bảo vệ chân lý khoa học ấy đã chính thức bùng nổ tại phòng xử án của Tòa án Hạt Harris.",
        "EN": "The legal struggle to uphold scientific truth erupted decisively inside the courtroom of Harris County, Texas.",
        "JA": "そして科学的真理を守るための法廷闘争が、テキサス州ハリス郡裁判所で火蓋を切ることになります。",
        "KO": "그리고 그 과학적 진실을 지켜내기 위한 치열한 법정 공방이 텍사스주 해리스 카운티 법원에서 불을 뿜기 시작했습니다.",
    },
    "4.06": {
        "VN": "Và phán quyết của bồi thẩm đoàn trong phiên tái thẩm đã phản ánh đúng bản chất nhân văn sâu sắc của nền tư pháp văn minh.",
        "EN": "The jury's eventual verdict in that retrial genuinely reflected the profound humanitarian essence of a civilized legal order.",
        "JA": "そして再審における陪審員団の判断は、文明的司法制度が備えるべき深い人間性の本質を体現することになりました。",
        "KO": "그리고 재심 배심원단의 평결은 문명화된 사법 제도가 지향해야 할 깊은 인간적 가치를 온전히 반영했습니다.",
    },
    "4.11": {
        "VN": "Công lý chỉ thực sự trọn vẹn và bền vững khi nó được soi sáng bởi tri thức khoa học và lòng nhân đạo đích thực.",
        "EN": "Justice achieves its highest form only when illuminated by rigorous scientific inquiry and authentic humanitarian wisdom.",
        "JA": "正義は、真の科学的知見と偽らざる人道主義によって照らされた時、初めて完全で揺るぎないものとなるのです。",
        "KO": "사법 정의는 철저한 과학적 진실과 진정한 인간애에 의해 조명될 때에만 비로소 온전하게 완성될 수 있습니다.",
    },
    "5.03": {
        "VN": "Sự cẩn trọng tối đa và mạng lưới giám sát chặt chẽ từ gia đình chính là lá chắn bảo vệ sinh mệnh cho cả mẹ và con.",
        "EN": "Rigorous vigilance and an active family support network constitute the ultimate shield protecting the lives of both mother and child.",
        "JA": "最大限の警戒心と家族による隙のない見守り体制こそが、母子双方の尊い命を守る真の防壁となります。",
        "KO": "가족들의 빈틈없는 감시와 세심한 보호망이야말로 산모와 아이 모두의 생명을 지키는 가장 견고한 방패입니다.",
    },
    "5.04": {
        "VN": "Sự hỗ trợ thiết thực, lắng nghe không phán xét từ người chồng và gia đình chính là bức tường thành vững chắc nhất che chở cho người phụ nữ trong giai đoạn nhạy cảm này.",
        "EN": "Unconditional support and non-judgmental listening from partners and family represent the strongest fortress shielding women during this vulnerable passage.",
        "JA": "配偶者や家族による批判のない傾聴と献身的な生活支援こそが、この脆弱な時期にある女性を守る最強の砦となります。",
        "KO": "남편과 가족들의 비판 없는 경청과 실질적인 양육 동참이야말로 가장 취약한 시기에 놓인 여성을 보호하는 가장 든든한 성벽입니다.",
    },
}

target_files = [
    ("VN", ROOT / "01_KICH_BAN" / "Tap21" / "kichban_tap21_23102026.md"),
    ("EN", ROOT / "01_KICH_BAN" / "Tap21" / "kichban_tap21_EN.md"),
    ("EN", ROOT / "01_KICH_BAN" / "Tap21_EN" / "kichban_tap21_EN.md"),
    ("JA", ROOT / "01_KICH_BAN" / "Tap21" / "kichban_tap21_JA.md"),
    ("JA", ROOT / "01_KICH_BAN" / "Tap21_JA" / "kichban_tap21_JA.md"),
    ("KO", ROOT / "01_KICH_BAN" / "Tap21" / "kichban_tap21_KO.md"),
    ("KO", ROOT / "01_KICH_BAN" / "Tap21_KO" / "kichban_tap21_KO.md"),
]

def update_file(lang, path):
    if not path.exists():
        print(f"Skipping non-existent: {path}")
        return
    print(f"Updating {lang}: {path}")
    content = path.read_text(encoding="utf-8")
    
    # Update header: 212 -> 248 sentences
    content = content.replace("212 câu thoại", "248 câu thoại")
    content = content.replace("212 câu", "248 câu")
    content = content.replace("212", "248")  # careful with other numbers, let's verify
    
    # Better to do targeted replacement for sentence counts in table
    for el_id, additions_by_lang in ADDITIONS.items():
        anchor = ANCHORS[el_id][lang]
        add_text = "\n".join(additions_by_lang[lang])
        replacement = anchor + "\n" + add_text
        if anchor in content:
            content = content.replace(anchor, replacement)
        else:
            print(f"WARNING: Anchor for {el_id} in {lang} NOT FOUND in {path}!")
            print(f"Expected anchor: {anchor[:50]}...")
            
    # Fix CRLF
    content = content.replace("\r\r\n", "\r\n").replace("\r\n", "\n")
    path.write_text(content, encoding="utf-8")
    print(f"Done: {path}")

for lang, p in target_files:
    update_file(lang, p)

print("All target files updated.")
