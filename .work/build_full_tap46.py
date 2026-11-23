# -*- coding: utf-8 -*-
"""
Generate exact 240-sentence scripts for Tap 46 in Vietnamese, English, and Japanese.
Each element matches Tap 10 sentence-for-sentence (total 240 sentences across 36 LOI turns).
Includes deep psychological forensic profiling of Nomia Rosemary Ndlovu, hitmen Njabulo Kunene and Lakhiwe Mkhize,
victims Maurice Mabasa, Audrey, Witness Homu, Brilliant, Mayeni, Zanele, mother Maria Mushwana, sister Joyce, and Tembisa community.
"""

import os, re, json

# Data structure containing all 36 LOI turns with exactly the same sentence count as Tap 10:
# [
#   (id, act, role, direction, [VN sentences], [EN sentences], [JA sentences])
# ]

ELEMENTS_DATA = [
  # --- ACT 1 ---
  ("1.02", 1, "HOST", "chậm rãi, giọng trầm ấm gợi mở không gian lịch sử",
   [
     "Mỗi góc tối của xã hội luôn ẩn chứa những vết nứt vô hình mà mắt thường của chúng ta không thể nào nhận biết.",
     "Giữa vùng đất Tembisa sầm uất của tỉnh Gauteng, Nam Phi, một bóng ma tội ác đã âm thầm bao trùm suốt hơn sáu năm ròng rã.",
     "Người dân nơi đây vốn quen thuộc với những vất vả thường nhật và luôn tìm kiếm sự che chở từ những người khoác trên mình sắc phục bảo vệ pháp luật.",
     "Sắc phục màu xanh của lực lượng cảnh sát từ lâu đã trở thành biểu tượng của niềm tin, sự an toàn và công lý tối thượng trong tâm thức cộng đồng.",
     "Người ta tin rằng những ai đeo trên ngực chiếc huy hiệu cảnh sát đều là những người gác cổng đáng tin cậy sẵn sàng bảo vệ sinh mạng cho nhân dân.",
     "Các phương tiện truyền thông địa phương thời bấy giờ liên tục ca ngợi những chiến công trấn áp tội phạm, biến lực lượng thực thi pháp luật thành bức tường thành bảo vệ sự bình yên.",
     "Thế nhưng, chính niềm tin mặc định đầy ngây thơ ấy đã tạo nên một “Điểm mù xã hội” vô cùng nguy hiểm.",
     "Tại những khu phố nghèo ven đô như Tembisa, người dân thường sống nương tựa vào nhau bằng tình làng nghĩa xóm và niềm tin trọn vẹn vào cơ quan hành pháp.",
     "Sự giản dị chất phác của những gia đình lao động đã dệt nên một tấm rèm bình yên nhưng vô tình làm tê liệt phản xạ cảnh giác tự nhiên của con người.",
     "Ai cũng tin rằng mình biết rõ người hàng xóm bên kia hàng rào, tin rằng phía sau những bộ đồng phục nghiêm trang luôn là những tấm lòng vì dân phục vụ.",
     "Chính sự mất cảnh giác tập thể ấy đã biến vùng đất này thành một nơi ẩn náu hoàn hảo cho cái ác ngụy trang.",
     "Một trong những chuỗi án mạng trục lợi bảo hiểm chấn động nhất lịch sử tư pháp Nam Phi đã bắt đầu từ chính sự che giấu hoàn hảo của chiếc huy hiệu ấy."
   ],
   [
     "Every dark corner of society hides invisible fractures that our naked eyes often fail to detect.",
     "In the bustling township of Tembisa in Gauteng province, South Africa, a sinister shadow silently loomed for more than six long years.",
     "The local residents were accustomed to daily hardships and consistently looked for protection from those wearing the uniform of the law.",
     "The blue uniform of the police force had long been a revered symbol of trust, security, and ultimate justice in the collective consciousness.",
     "People inherently believed that anyone bearing the police badge on their chest was a reliable guardian sworn to protect civilian lives.",
     "Local media at the time regularly celebrated crime-fighting accomplishments, turning law enforcement into an unshakeable bastion of peace.",
     "Yet, that very naive and default trust ended up creating a profoundly perilous societal blind spot.",
     "In working-class townships like Tembisa, residents leaned heavily on communal bonds and complete faith in law enforcement agencies.",
     "The humble simplicity of hardworking families wove a serene curtain that inadvertently paralyzed natural survival vigilance.",
     "Everyone believed they genuinely knew their neighbors, convinced that behind every dignified uniform beat a dedicated heart serving the public.",
     "It was precisely this collective lack of suspicion that turned the community into a perfect sanctuary for camouflaged evil.",
     "One of the most shocking insurance-motivated murder sprees in South African judicial history began under the flawless cover of that very badge."
   ],
   [
     "社会のあらゆる暗がりには、肉眼では捉えきれない無形の亀裂が常に潜んでいます。",
     "南アフリカ・ハウテン州の活気ある町テンビサにおいて、ある邪悪な影が6年以上にわたり静かに立ち込めていました。",
     "この地の人々は日々の苦難に耐えながら、法の執行者を象徴する制服に深い庇護と安心を求めて生きていました。",
     "警察官が身にまとう青い制服は、人々の意識の中で長年にわたり信頼、安全、そして正義の象徴として敬われてきました。",
     "胸に警察バッジをつけた者は、市民の生命を守り抜く揺るぎない守護者であると誰もが無条件に信じていたのです。",
     "当時の地元メディアも治安維持の成果を称賛し、法執行機関を平穏を守る頼もしい砦として描いていました。",
     "しかし、その純朴で無防備な信頼こそが、極めて危険な「社会的盲点」を生み出す温床となってしまいました。",
     "テンビサのような労働者階級の町では、人々は互いの助け合いと法執行機関への全幅の信頼を命綱として暮らしています。",
     "素朴な生活の営みが生み出す平穏のベールは、皮肉にも捕食者に対する人間本来の警戒反応を麻痺させてしまいました。",
     "誰もが隣人を理解していると信じ、厳格な制服の背後には常に高潔な奉仕の精神が宿っていると信じ切っていたのです。",
     "この集団的な油断こそが、偽装された巨悪にとって最も完璧な隠れ蓑を提供することになりました。",
     "南アフリカ司法史上、最も戦慄すべき保険金連続殺人の幕開けは、まさにそのバッジの完璧な偽装の下で切られたのです。"
   ]
  ),

  ("1.04", 1, "HOST", "chuyển giọng u tối, báo hiệu tai ương",
   [
     "Vào tháng ba năm 2012, một thi thể nam giới được tìm thấy tại khu vực hẻo lánh thuộc Olifantsfontein.",
     "Nạn nhân được xác định là Madala Witness Homu, một người lao động hiền lành và là em họ của một nữ cảnh sát đang công tác tại đồn Tembisa South.",
     "Cái chết bất thường với nhiều thương tổn nghiêm trọng của người đàn ông nghèo khó ban đầu chỉ được xem như một vụ ẩu đả ngẫu nhiên nơi ngoại ô.",
     "Thế nhưng, điều kỳ lạ là ngay sau cái chết của người em họ, nữ trung sĩ Nomia Rosemary Ndlovu đã nhanh chóng xuất hiện tại hiện trường với tư cách người nhà.",
     "Bà ta tỏ ra đau buồn tột độ, chủ động hỗ trợ cơ quan chức năng hoàn tất các thủ tục pháp y và giấy tờ chứng tử.",
     "Không ai mảy may nghi ngờ rằng phía sau những giọt nước mắt xót thương ấy là một giao dịch tài chính ngầm vừa hoàn tất việc thu hoạch lợi nhuận."
   ],
   [
     "In March 2012, the body of a man was discovered in a secluded rural area of Olifantsfontein.",
     "The victim was identified as Madala Witness Homu, a gentle worker and the cousin of a policewoman stationed at Tembisa South Police Station.",
     "The abnormal death marked by severe physical trauma was initially dismissed as a random altercation in a rough suburban territory.",
     "Yet, suspiciously, immediately after the death of her cousin, Sergeant Nomia Rosemary Ndlovu swiftly arrived on the scene as a grieving family member.",
     "She displayed overwhelming sorrow, proactively assisting authorities with forensic clearances and official death documentation.",
     "No one remotely suspected that behind those grieving tears lay a covert financial harvest that had just reached fruition."
   ],
   [
     "2012年3月、オリファンツフォンテインの辺鄙な荒野で、一人の男性の遺体が発見されました。",
     "被害者はテンビサ・サウス警察署に勤務する女性警官の従兄弟であり、温厚な労働者であったマダラ・ウィットネス・ホムと特定されました。",
     "凄惨な外傷を負った貧しい男の不審死は、当初、郊外特有の偶発的な暴力事件として片付けられようとしていました。",
     "しかし不可解なことに、従兄弟の死の直後、巡査部長ノミア・ローズマリー・ンドロヴが遺族として迅速に現場へ現れたのです。",
     "彼女は深い悲嘆に暮れる素振りを見せ、法医学手続きや死亡診断書の発行を当局へ自ら進んで手助けしました。",
     "その痛ましい涙の裏側で、冷酷な金融取引の果実がすでに収穫されていたとは、当時誰も夢にも思っていませんでした。"
   ]
  ),

  ("1.06", 1, "HOST", "tiếp tục mạch tự sự nghẹt thở",
   [
     "Chỉ một thời gian ngắn sau khi nạn nhân được an táng, các công ty bảo hiểm đã chi trả một khoản tiền tang lễ khổng lồ hơn một trăm ba mươi nghìn Rand.",
     "Người đứng tên nhận trọn vẹn số tiền bồi thường ấy không ai khác chính là người chị họ cảnh sát mẫu mực Nomia Rosemary Ndlovu.",
     "Trong cộng đồng lao động nghèo, số tiền ấy là cả một gia tài mà một người bình thường phải tích lũy trong nhiều năm ròng rã.",
     "Thay vì dùng số tiền ấy để chăm lo cho gia đình người đã khuất, nữ cảnh sát lại lập tức lao vào những canh bạc thâu đêm tại các sòng bài sang trọng.",
     "Vị ngọt ngào của dòng tiền kiếm được quá dễ dàng đã đánh thức con quái vật tham lam vốn đang ngủ say trong tâm trí bà ta.",
     "Đó không phải là một sự việc bộc phát đơn lẻ, mà chính là phát súng mở màn cho một chuỗi săn lùng mạng sống của chính những người mang cùng dòng máu."
   ],
   [
     "Shortly after the victim was buried, insurance companies disbursed an immense funeral payout exceeding one hundred and thirty thousand Rand.",
     "The sole beneficiary who claimed the entirety of that financial compensation was none other than the exemplary police sergeant, Nomia Rosemary Ndlovu.",
     "Within an impoverished working-class township, that amount represented a small fortune requiring years of grueling labor to accumulate.",
     "Instead of utilizing those funds to support the grieving relatives, the policewoman promptly plunged into all-night gambling sprees at lavish casinos.",
     "The exhilarating sweetness of effortless blood money awakened a dormant monster of voracious greed within her psyche.",
     "This was not an isolated impulse, but rather the opening salvo of a calculated hunt targeting the lives of her own kin."
   ],
   [
     "被害者の埋葬が終わって間もなく、複数の保険会社から13万ランドを超える巨額の葬儀給付金が支払われました。",
     "その給付金を全額受領した唯一の受取人は、他ならぬ模範的な女性巡査部長、ノミア・ローズマリー・ンドロヴだったのです。",
     "貧しい労働者街において、その大金は通常の生活者が何年も汗水流して蓄えなければならない莫大な財産でした。",
     "遺族の支援に充てるどころか、この女性警官はその資金を握りしめ、華美なカジノでの夜を徹した賭博へと直行しました。",
     "あまりに容易に手に入った血塗られた金の味は、彼女の精神の奥底で眠っていた強欲の怪物を決定的に呼び覚ましました。",
     "それは単発の衝動的犯行などではなく、自らの血肉を分けた親族を標的とする連続狩猟の号砲だったのです。"
   ]
  ),

  ("1.07", 1, "NGƯỜI BÌNH THƯỜNG", "N1: Đồng nghiệp tại Đồn Tembisa South, giọng nữ trẻ hoang mang, bàng hoàng",
   [
     "Hãy hình dung cảm giác bàng hoàng của toàn bộ cán bộ chiến sĩ tại trạm cảnh sát Tembisa South khi sự việc bắt đầu phát lộ.",
     "Rosemary từng là một đồng đội mẫn cán, luôn nở nụ cười hòa nhã và rất nhiệt tình giúp đỡ mọi người trong ca trực.",
     "Chị ấy thường xuyên xung phong giải quyết các hồ sơ tử tuất phức tạp và luôn tỏ ra thấu hiểu nỗi đau của thân nhân người bị nạn.",
     "Mỗi khi nghe tin người thân trong gia đình chị ấy lần lượt qua đời vì những tai nạn bất ngờ, chúng tôi đều quyên góp và chia buồn sâu sắc.",
     "Chúng tôi thực sự không thể nào ngờ rằng đằng sau chiếc áo đồng phục nghiêm trang ấy lại là một tâm địa tàn độc đến mức lạnh sống lưng."
   ],
   [
     "Just imagine the utter bewilderment among all officers at Tembisa South Police Station when the truth finally surfaced.",
     "Rosemary was perceived as a dedicated colleague, consistently wearing a warm smile and eager to assist anyone during long shifts.",
     "She frequently volunteered to handle complicated deceased-estate paperwork and always appeared deeply empathetic toward grieving families.",
     "Whenever news arrived that another of her relatives had perished in unexpected tragedies, we rallied around her, raising condolences and funds.",
     "Never in our darkest nightmares could we have imagined that behind that respectable uniform lurked an unspeakable, chilling ruthlessness."
   ],
   [
     "真実が白日の下に晒されたとき、テンビサ・サウス警察署の同僚たちがどれほどの衝撃を受けたか想像してみてください。",
     "ローズマリーは常に柔らかな笑みを絶やさず、勤務中も進んで同僚を支える極めて勤勉な同僚と目されていました。",
     "彼女は複雑な変死事案や検視書類の処理を進んで引き受け、遺族の痛みに深く寄り添う姿勢を見せていたのです。",
     "彼女の親族が不慮の事故で次々と命を落としたという知らせを聞くたび、私たちは心から同情し、互いにカンパを集めて彼女を慰めました。",
     "あの誇り高い警察の制服の裏側に、背筋が凍るほど冷酷無残な怪物が潜んでいたとは、誰一人として想像すらできませんでした。"
   ]
  ),

  ("1.09", 1, "HOST", "trầm giọng",
   [
     "Sự ra đi liên tiếp của những người thân trong gia đình Ndlovu trong những năm tiếp theo đã bắt đầu để lại những vết gợn bất thường.",
     "Tháng sáu năm 2013, cô em gái ruột Audrey Ndlovu được phát hiện tử vong ngay trong phòng ngủ sau khi uống một cốc nước trà lạ.",
     "Tiếp đó, các cháu ruột là Brilliant Mashego, Mayeni Mashaba và Zanele Motha cũng lần lượt thiệt mạng vì những nguyên nhân đầy uẩn khúc.",
     "Mỗi cái chết đều kéo theo một hồ sơ yêu cầu bồi thường bảo hiểm nhân thọ và bảo hiểm tang lễ được nộp lên với tốc độ đáng kinh ngạc.",
     "Một đám mây đen chết chóc bao trùm lấy dòng họ Ndlovu, trong khi tài khoản của nữ cảnh sát liên tục nhận về những món tiền kếch xù."
   ],
   [
     "The relentless succession of deaths among Ndlovu's relatives over the subsequent years began carving ominous, suspicious ripples.",
     "In June 2013, her own biological sister, Audrey Ndlovu, was discovered dead in her bedroom shortly after consuming a peculiar cup of tea.",
     "Subsequently, her nephews Brilliant Mashego and Mayeni Mashaba, alongside niece Zanele Motha, mysteriously perished under deeply questionable circumstances.",
     "Every single demise was immediately accompanied by an insurance and funeral claim filed with astonishing, calculated speed.",
     "A dark, suffocating cloud of mortality enveloped the Ndlovu family, while the policewoman's bank accounts swelled with colossal windfalls."
   ],
   [
     "その後の数年間、ンドロヴ家の親族が相次いで命を落とす異常な事態は、不穏な疑惑の波紋を広げ始めました。",
     "2013年6月、実の妹であるオードリー・ンドロヴが、不自然なお茶を口にした直後、寝室で変死しているのが発見されました。",
     "続いて甥のブリリアント・マシェゴ、マイエニ・マシャバ、そして姪のザネレ・モタも、相次いで不可解な死を遂げたのです。",
     "いかなる死の直後にも、驚異的な手際の良さで生命保険および葬儀保険の給付金請求書が各社へ提出されていました。",
     "ンドロヴ一族の上に死の暗雲が立ち込める一方で、この女性警官の口座には巨額の現金が次々と振り込まれ続けたのです。"
   ]
  ),

  ("1.10", 1, "ĐIỀU TRA VIÊN", "giọng nam sắc bén, tái hiện không gian nghiệp vụ",
   [
     "Nghi phạm là Trung sĩ Nomia Rosemary Ndlovu, sinh năm 1978, công tác lâu năm tại lực lượng cảnh sát Nam Phi.",
     "Ngay từ những vụ việc đầu tiên, đối tượng đã bộc lộ một phương thức gây án mang tính toán kỹ lưỡng dựa trên sự am hiểu sâu sắc về lỗ hổng hành chính.",
     "Bà ta biết chính xác các hãng bảo hiểm nhân thọ thẩm định hồ sơ lỏng lẻo như thế nào đối với các gói bảo hiểm tang lễ giá trị vừa phải.",
     "Bà ta âm thầm đứng tên mua hàng chục hợp đồng bảo hiểm cho cùng một nạn nhân tại nhiều công ty tài chính khác nhau mà không thông báo cho người thân.",
     "Khi nạn nhân tử vong, với tư cách là một sĩ quan cảnh sát, bà ta dễ dàng tiếp cận hiện trường và thúc đẩy việc cấp giấy chứng tử nhanh chóng.",
     "Tổng số tiền mà đối tượng đã chiếm đoạt qua các hợp đồng bảo hiểm đẫm máu này lên tới hơn một phẩy bốn triệu Rand.",
     "Đây không phải là hành vi của một kẻ quẫn trí, mà là một cỗ máy kiếm tiền máu lạnh hoạt động dưới sự bảo kê của chính quyền lực hành pháp."
   ],
   [
     "The primary suspect was Sergeant Nomia Rosemary Ndlovu, born in 1978, a veteran officer within the South African Police Service.",
     "From the inception of her scheme, the perpetrator exhibited a meticulously calculated modus operandi exploiting administrative loopholes.",
     "She knew precisely how lax insurance underwriters were when evaluating moderate-value funeral policies across different providers.",
     "She covertly registered dozens of policies on a single relative across multiple financial institutions without the victim's knowledge.",
     "Upon a victim's demise, utilizing her official police authority, she seamlessly accessed scenes and expedited the processing of death certificates.",
     "The total sum fraudulently acquired by the suspect through these blood-drenched policies exceeded one point four million Rand.",
     "This was never the impulse of a desperate mind, but the work of a cold-blooded syndicate operating behind the shield of state authority."
   ],
   [
     "最重要容疑者は1978年生まれのベテラン警察官、ノミア・ローズマリー・ンドロヴ巡査部長でした。",
     "犯行の初期段階から、容疑者は行政や保険業界の制度的盲点を熟知した上で、綿密に計算された手口を駆使していました。",
     "彼女は、一定額以下の葬儀保険において保険各社の審査が極めて形式的かつ緩慢であることを正確に見抜いていたのです。",
     "本人の同意や認識なしに、同一の親族を対象として複数の金融会社で十数件もの保険契約を秘密裏に結んでいました。",
     "標的が死亡すると、警察官という立場を巧みに利用して現場にいち早く介入し、死亡診断書や検視書類の発行を急速に進めました。",
     "これら血塗られた保険契約を通じて彼女が不法に詐取した総額は、140万ランド以上にも達していました。",
     "これは決して困窮による凶行ではなく、公権力の盾を悪用して稼働し続けた冷酷無比な殺人事業だったのです。"
   ]
  ),

  ("1.11", 1, "HOST", "khép lại Hồi 1",
   [
     "Tấm màn nhung che đậy tội ác tưởng chừng như không thể bị xuyên thủng suốt nhiều năm ròng rã.",
     "Những lời xì xào nghi ngờ trong gia đình nhanh chóng bị dập tắt bởi uy quyền và chiếc huy hiệu cảnh sát đầy quyền lực của Rosemary.",
     "Thế nhưng, cái ác một khi đã nếm trải sự thỏa mãn vô độ thì sẽ không bao giờ biết điểm dừng.",
     "Cơn nghiện quyền lực và cờ bạc đã đẩy kẻ thủ ác bước vào một vòng xoáy leo thang ngày càng điên cuồng và tàn độc hơn.",
     "Bản năng sinh tồn của bóng tối đã chuẩn bị giăng sẵn những cạm bẫy hủy diệt tiếp theo đối với những người chung sống bên cạnh bà ta."
   ],
   [
     "The velvety curtain concealing these monstrous crimes seemed entirely impenetrable for many years.",
     "Whispers of suspicion within the family were instantly suppressed by Rosemary's overwhelming authority and her formidable police badge.",
     "Yet evil, once intoxicated by unchecked gratification, never voluntarily reaches an end.",
     "Addiction to absolute power and reckless gambling propelled the killer into an increasingly frantic and ruthless escalation.",
     "The destructive impulse of darkness was already preparing its next lethal traps for those sharing her daily life."
   ],
   [
     "この戦慄すべき犯罪を覆い隠していたベルベットの幕は、何年にもわたって決して破られないかのように見えました。",
     "親族の間でささやかれた微かな疑惑も、ローズマリーの威圧的な権力と警察バッジの威光の前に即座にかき消されました。",
     "しかし、留まることのない充足感を一度味わった悪意は、自らその歩みを止めることなど決してありません。",
     "権力への陶酔とギャンブルへの病的な依存は、この殺人鬼をより狂乱的で無慈悲なエスカレーションへと駆り立てていきました。",
     "闇の深淵は、彼女の身近で暮らす次なる犠牲者たちを捕らえるため、さらなる破滅の罠を確実に張り巡らせていたのです。"
   ]
  ),

  # --- ACT 2 ---
  ("2.02", 2, "HOST", "giọng hồi hộp dẫn dắt",
   [
     "Điều gì đã biến một nữ sĩ quan cảnh sát từng tuyên thệ bảo vệ sự bình yên của nhân dân thành một kẻ săn mồi tàn sát chính gia đình mình?",
     "Để trả lời cho câu hỏi ấy, chúng ta phải thâm nhập vào cấu trúc nhân cách đầy méo mó và phức tạp của Rosemary Ndlovu.",
     "Ở nơi làm việc, bà ta xây dựng một hình mẫu người phụ nữ độc lập, mạnh mẽ và tận tụy với công việc tuần tra.",
     "Tại khu dân cư Tembisa, bà ta xuất hiện như một trụ cột kinh tế hào phóng, sẵn sàng chi tiền cho những đám tang của dòng họ.",
     "Thế nhưng, tất cả sự tử tế ấy thực chất chỉ là một lớp hóa trang hoàn hảo được dàn dựng công phu để che giấu một thế giới nội tâm băng giá.",
     "Ẩn sâu phía sau nụ cười thân thiện là một cơ chế tâm lý cực kỳ bệnh hoạn cho phép bà ta xóa sạch mọi ranh giới của lương tri."
   ],
   [
     "What transformed a sworn police officer, pledged to uphold peace and protect citizens, into a predator exterminating her own family?",
     "To answer that haunting question, one must dissect the deeply warped and intricate personality architecture of Rosemary Ndlovu.",
     "In the workplace, she projected the persona of an independent, resilient woman profoundly committed to her patrol duties.",
     "Across the Tembisa community, she appeared as a generous financial matriarch, always willing to fund elaborate tribal funerals.",
     "Yet every display of benevolence was merely an elaborate theatrical camouflage designed to mask a frigid internal void.",
     "Lurking behind that engaging smile was a pathological psychological mechanism enabling her to completely erase moral conscience."
   ],
   [
     "市民の平穏と生命を守ると誓った警察官を、自らの肉親を間引く捕食者へと変貌させたものは何だったのでしょうか。",
     "その重い問いに答えるためには、ローズマリー・ンドロヴの歪曲し複雑を極めた人格構造を解剖しなければなりません。",
     "職場において、彼女は巡回任務に献身し、自立した強靭な女性警察官としてのパブリックイメージを確立していました。",
     "テンビサの地域社会にあっては、一族の葬儀費用を惜しみなく負担する気前の良い大黒柱として振る舞っていたのです。",
     "しかし、それらすべての善意の振る舞いは、凍りついた内面世界を隠匿するために丹念に仕組まれた偽装に過ぎませんでした。",
     "その親しみやすい笑みの深層には、良心の境界線を完全に消去してしまう極めて病的な心理メカニズムが潜んでいたのです。"
   ]
  ),

  ("2.04", 2, "ĐIỀU TRA VIÊN", "mô tả dấu vết tài chính và đời sống ngầm",
   [
     "Hồ sơ trinh sát tài chính cho thấy đối tượng Rosemary Ndlovu là một con bạc bệnh lý khét tiếng tại các sòng bài thuộc khu vực Johannesburg.",
     "Mỗi khi tan ca trực tại đồn cảnh sát, bà ta thường lái xe thẳng tới các bàn đỏ đen và nướng sạch tiền lương chỉ trong vài giờ đồng hồ.",
     "Những món nợ ngập đầu từ các tay cho vay nặng lãi đã tạo ra một áp lực tài chính nghẹt thở đè nặng lên cuộc sống của đối tượng.",
     "Để duy trì cơn nghiện cờ bạc và lối sống xa hoa giả tạo, bà ta đã nảy sinh ý định biến mạng sống của người thân thành nguồn thanh khoản tài chính.",
     "Tháng mười năm 2015, người bạn đời chung sống nhiều năm của bà ta là Maurice Mabasa đã trở thành mục tiêu tiếp theo trong tầm ngắm.",
     "Mabasa là cha của con bà ta, một người đàn ông hiền lành luôn hết lòng yêu thương và tin tưởng người bạn đời cảnh sát.",
     "Thế nhưng, sau lưng người bạn đời, Ndlovu đã bí mật mua tới mười sáu hợp đồng bảo hiểm nhân thọ khác nhau đứng tên Mabasa.",
     "Thi thể của Maurice Mabasa sau đó được tìm thấy tại một khu đất hoang ở Olifantsfontein với hơn tám mươi vết thương chí mạng trên cơ thể.",
     "Hành vi bạo tàn bất thường này cho thấy kẻ ra tay muốn đảm bảo chắc chắn rằng nạn nhân không còn bất kỳ cơ hội sống sót nào.",
     "Ngay sau vụ án mạng, Ndlovu đã ung dung đút túi hơn bốn trăm mười sáu nghìn Rand từ các yêu cầu bồi thường bảo hiểm nhân thọ của Mabasa."
   ],
   [
     "Financial intelligence records revealed that suspect Rosemary Ndlovu was a notorious pathological gambler frequenting major Johannesburg casinos.",
     "Upon concluding her police shifts, she routinely drove straight to gambling tables, squandering her official salary in mere hours.",
     "Spiraling debts owed to ruthless loan sharks generated suffocating financial pressure that heavily constrained her lifestyle.",
     "To feed her gambling compulsive disorder and maintain an illusion of wealth, she conceived the scheme of converting kin into liquid assets.",
     "In October 2015, her long-term domestic partner, Maurice Mabasa, became the next prime target on her fatal ledger.",
     "Mabasa was the father of her child, a mild-mannered man who devotedly loved and unconditionally trusted his policewoman partner.",
     "Yet entirely behind his back, Ndlovu had clandestinely acquired sixteen separate life and accident policies covering Mabasa's life.",
     "Maurice Mabasa's body was subsequently discovered abandoned in Olifantsfontein bearing more than eighty catastrophic stab wounds.",
     "This extraordinary savagery demonstrated an uncompromising intent to ensure the victim had absolute zero probability of survival.",
     "Immediately following the slaughter, Ndlovu casually collected over four hundred and sixteen thousand Rand in life insurance payouts."
   ],
   [
     "財務捜査の記録は、容疑者ローズマリー・ンドロヴがヨハネスブルグ市内の名だたるカジノに入り浸る重度の病理的ギャンブラーであった事実を突き止めました。",
     "警察署での勤務を終えるや否や、彼女は車を駆って賭博場へ直行し、正規の給与をわずか数時間で使い果たしていました。",
     "悪質な高利貸しから抱えた雪だるま式の借金は、彼女の生活に息の詰まるような重圧としてのしかかっていたのです。",
     "ギャンブルへの渇望を満たし、裕福な生活の幻想を維持するため、彼女は肉親の生命を即時換金可能な金融資産へと変質させる着想を得ました。",
     "2015年10月、長年の同居パートナーであったモーリス・マバサが、彼女の標的リストの筆頭に据えられました。",
     "マバサは彼女の子供の父親であり、警察官であるパートナーを心から愛し、全幅の信頼を寄せていた温和な男性でした。",
     "しかしその背後で、ンドロヴはマバサの名義で実に16件もの生命保険および傷害保険契約を秘密裏に結んでいたのです。",
     "その後、モーリス・マバサの遺体はオリファンツフォンテインの荒れ地で、80箇所以上もの致命的な刺傷を負った状態で発見されました。",
     "この異常なまでの残虐性は、標的が生き延びる可能性を徹底的に根絶しようとする加害者の冷徹な意志を物語っていました。",
     "惨劇の直後、ンドロヴは何食わぬ顔で41万6千ランドを超えるマバサの保険給付金を懐に収めたのです。"
   ]
  ),

  ("2.05", 2, "HOST", "phác họa chân dung kẻ thủ ác",
   [
     "Mỗi nạn nhân ngã xuống là một lần tài khoản của nữ cảnh sát lại nhảy múa những con số đẫm máu.",
     "Bà ta coi cái chết của người thân như một kỳ thu hoạch mùa màng định kỳ để trang trải cho những cơn khát đỏ đen.",
     "Sự tàn nhẫn không chỉ dừng lại ở hành động tước đoạt sinh mạng, mà còn thể hiện ở thái độ trơ trẽn đến rợn người của kẻ thủ ác sau mỗi vụ việc.",
     "Bà ta đích thân đến nhà xác để nhận dạng thi thể, giả vờ ngất xỉu trong vòng tay người thân, rồi lập tức quay sang giục giã công ty bảo hiểm chi tiền.",
     "Sự vô cảm ấy bắt nguồn từ một cơ chế tâm lý bệnh lý sâu sắc mà khoa học hành vi đã chỉ rõ."
   ],
   [
     "With every relative who fell, the policewoman's bank balance surged with blood-soaked numbers.",
     "She treated the deaths of her loved ones as seasonal financial harvests to service her insatiable gambling cravings.",
     "Her cruelty was not confined to orchestrated killings; it manifested in her chillingly theatrical behavior following every tragedy.",
     "She personally visited mortuaries to identify remains, feigned fainting in relatives' arms, then immediately badgered insurers for expedited cash.",
     "Such absolute emotional detachment stems from profound psychological pathology that behavioral forensic science illuminates."
   ],
   [
     "親族が一人また一人と命を落とすたび、この女性警官の預金口座には血塗られた数字が積み上がっていきました。",
     "彼女は身内の死を、自らのギャンブル依存を満たすための定期的な「資金収穫」として扱っていたのです。",
     "その冷酷さは単に殺害を指図した点にとどまらず、惨劇の直後に見せた身の毛のよだつほど不遜な態度にも如実に表れていました。",
     "自ら死体安置所へ遺体確認に赴いては、親族の腕の中で卒倒する演技をし、その舌の根の乾かぬうちに保険会社へ電話をかけて送金を催促しました。",
     "この徹底した無感情さは、法心理行動科学が解明している極めて深刻な精神病理メカニズムに起因するものです。"
   ]
  ),

  ("2.06", 2, "CHUYÊN GIA TÂM LÝ", "phân tích cơ chế chia ngăn tâm trí và sự vật hóa con người",
   [
     "Dưới góc độ tâm lý học tội phạm, Rosemary Ndlovu là một trường hợp điển hình của sự kết hợp giữa Ái kỷ ác tính và Thái nhân cách.",
     "Đặc điểm nổi bật nhất ở đối tượng này chính là cơ chế “Phân ngăn nhận thức bệnh lý” được vận hành ở mức độ hoàn hảo.",
     "Trong não bộ của bà ta tồn tại hai ngăn kéo hoàn toàn độc lập và không bao giờ va chạm vào nhau trong đời sống thường nhật.",
     "Ngăn kéo thứ nhất là hình ảnh một nữ trung sĩ cảnh sát gương mẫu, nghiêm túc thi hành công vụ và được đồng nghiệp quý mến.",
     "Ngăn kéo thứ hai là một kẻ tính toán lạnh lùng, sẵn sàng định giá mạng sống của từng thành viên trong gia đình như những món hàng hóa.",
     "Hiện tượng này gắn liền với khái niệm “Vật hóa và Phi nhân hóa cực đoan” trong tâm lý học xã hội.",
     "Đối với Ndlovu, người em gái, người cháu ruột hay thậm chí người bạn đời Maurice Mabasa không phải là những con người độc lập có cảm xúc.",
     "Dưới lăng kính méo mó của lòng tham, họ chỉ là những tờ hợp đồng bảo hiểm biết đi, những công cụ tài chính dùng để giải quyết các khoản nợ.",
     "Khi thấu cảm cảm xúc bị triệt tiêu hoàn toàn, nỗi đau đớn và sự sợ hãi của nạn nhân không thể kích hoạt được bất kỳ phản xạ trắc ẩn nào.",
     "Trái lại, việc nhìn thấy các kế hoạch diễn ra trơn tru còn mang lại cho bà ta một cảm giác khoái cảm quyền lực và sự hưng phấn tột độ.",
     "Bà ta tự huyễn hoặc rằng mình nắm trong tay quyền sinh quyền sát và đủ thông minh để qua mặt toàn bộ hệ thống tư pháp của đất nước.",
     "Ảo tưởng toàn năng ấy chính là chiếc bẫy tâm lý tự giăng sẵn đưa kẻ thủ ác bước dần về phía vực thẳm sụp đổ."
   ],
   [
     "From the perspective of criminal psychology, Rosemary Ndlovu represents an archetype combining Malignant Narcissism and Severe Psychopathy.",
     "Her defining trait is an impeccably maintained mechanism of pathological cognitive compartmentalization.",
     "Within her mind existed two fully distinct compartments that never interfered with each other during ordinary routines.",
     "The first compartment housed the respected police sergeant who dutifully executed patrols and earned genuine affection from colleagues.",
     "The second compartment operated as an emotionless ledger, assigning precise financial price tags to the flesh and blood of her family.",
     "This phenomenon is inextricably linked to extreme objectification and radical dehumanization in behavioral science.",
     "To Ndlovu, her sister, her nephews, and even her domestic partner Maurice Mabasa were never sentient individuals possessing intrinsic human worth.",
     "Through the distorted prism of avarice, they were merely walking policies—expendable financial instruments to liquidate debts.",
     "Because affective empathy was completely eradicated, the terror and agony of victims failed to trigger even a micro-spark of remorse.",
     "Conversely, witnessing her sinister schemes unfold smoothly rewarded her with perverse power arousal and intoxicating narcissistic elevation.",
     "She nurtured a delusion of sovereign omnipotence, believing herself brilliant enough to permanently outwit the nation's legal apparatus.",
     "That very omnipotent fantasy was the psychological snare guiding the perpetrator steadily toward inevitable catastrophic collapse."
   ],
   [
     "犯罪心理学の観点から見れば、ローズマリー・ンドロヴは悪性自己愛と重度のサイコパシーが融合した典型例です。",
     "彼女の精神において最も際立っていた特徴は、極限まで洗練された「病理的認知的区画化」のメカニズムでした。",
     "彼女の脳内には互いに完全に分離し、日常の中で決して衝突することのない2つの独立した引き出しが存在していたのです。",
     "第1の引き出しには、真摯にパトロール任務を遂行し、同僚たちから愛される模範的な女性巡査部長の姿が収められていました。",
     "そして第2の引き出しには、身内の肉親一人ひとりの生命に正確な値段をつけ、冷酷に管理する計算高い犯罪者が棲みついていました。",
     "この現象は、行動科学における極端な「対象化」および「脱人間化」の概念と深く結びついています。",
     "ンドロヴにとって、妹や甥たち、さらには同居パートナーのマバサすらも、感情や尊厳を持った生身の人間ではありませんでした。",
     "強欲という歪んだレンズを通して見れば、彼らは単なる「歩く保険証書」であり、借金返済のためにいつでも換金できる道具に過ぎなかったのです。",
     "感情的共感能力が完全に欠如しているため、被害者たちの激痛や恐怖は、彼女の心に微かな同情の反応すら呼び起こしませんでした。",
     "それどころか、緻密な殺害計画が滞りなく進行する様を見届けることは、彼女に倒錯した権力快感と全能の高揚感を与えていました。",
     "彼女は自らが国家の司法システム全体を手玉に取れるほど知能に長け、生殺与奪の権を握っているという妄想に溺れていたのです。",
     "その全能の幻想こそが、自らを破滅の断崖へと着実に追い込んでいく致命的な心理的罠となりました。"
   ]
  ),

  ("2.07", 2, "HOST", "tiếp tục mạch tự sự",
   [
     "Sự trót lọt của sáu vụ án mạng liên tiếp trong suốt sáu năm đã củng cố niềm tin mù quáng của Rosemary vào sự bất khả xâm phạm của bản thân.",
     "Không một viên thanh tra nào đặt câu hỏi tại sao vận rủi lại liên tục giáng xuống đầu một gia đình duy nhất với tần suất dày đặc đến thế.",
     "Chiếc huy hiệu cảnh sát lấp lánh trên ngực đã trở thành một tấm khiên hộ mệnh vững chắc xua tan mọi sự nghi ngờ từ phía cơ quan chức năng.",
     "Thế nhưng, khi những con mồi trong gia đình dần cạn kiệt, lòng tham của bà ta bắt đầu vươn vòi bạch tuộc tới những mục tiêu thiêng liêng nhất."
   ],
   [
     "The flawless execution of six consecutive homicides across six years cemented Rosemary's blind belief in her absolute invulnerability.",
     "Not a single local investigator had questioned why tragedy relentlessly struck a single household with such unfathomable regularity.",
     "The shining police badge pinned to her chest functioned as an impenetrable shield repelling scrutiny from official quarters.",
     "Yet as her pool of targeted relatives dwindled, her insatiable greed extended its tentacles toward the most sacred bonds of nature."
   ],
   [
     "6年間にわたり6件もの殺人が何一つ咎められずに成功した事実は、自らが不可侵の存在であるというローズマリーの盲信を決定づけました。",
     "なぜこれほど奇怪な悲劇が、特定のひとつの家庭にのみ驚くべき頻度で降りかかるのか、疑問を抱く地元捜査官は誰もいませんでした。",
     "胸に輝く警察バッジが、公的機関によるあらゆる追及や疑惑を跳ね返す難攻不落の盾として機能していたのです。",
     "しかし、手近な親族の標的が底をつき始めると、彼女の底なしの強欲は、人間の最も神聖な血の絆へとその触手を伸ばし始めました。"
   ]
  ),

  ("2.08", 2, "ĐIỀU TRA VIÊN", "giải thích diễn biến tội ác tiếp theo",
   [
     "Đầu năm 2018, đối tượng Ndlovu bắt đầu lên kế hoạch thanh trừng người mẹ đẻ của mình là bà Maria Mushwana tại Bushbuckridge.",
     "Bà Maria là một người mẹ già yếu, cả đời lam lũ nuôi nẫng các con và luôn coi Rosemary là niềm tự hào lớn nhất của dòng họ.",
     "Ndlovu đã tiếp cận một sát thủ đánh thuê tên là Lakhiwe Mkhize và trả trước cho hắn số tiền hai nghìn sáu trăm Rand để sát hại bà mẹ già.",
     "Thủ đoạn của bà ta là yêu cầu sát thủ giả làm một thầy lang đến thăm khám rồi ra tay đầu độc hoặc làm ngạt thở nạn nhân để nhận bảo hiểm.",
     "Chưa dừng lại ở đó, đối tượng tiếp tục liên hệ với một nhân vật cộm cán khác là Njabulo Vincent Kunene để bàn bạc một hợp đồng tàn khốc hơn.",
     "Mục tiêu lần này là người em gái ruột Joyce Ndlovu cùng năm đứa con nhỏ của Joyce, trong đó đứa bé nhất mới chỉ vừa tròn năm tháng tuổi.",
     "Kế hoạch ma quỷ mà nữ cảnh sát vạch ra là chuốc thuốc mê toàn bộ sáu mẹ con rồi phóng hỏa thiêu rụi ngôi nhà để ngụy tạo thành một vụ cháy ngẫu nhiên.",
     "Mức thù lao mà bà ta hứa hẹn trả cho phi vụ thảm sát man rợ này là sáu mươi lăm nghìn Rand sau khi thanh toán xong các khoản tiền bảo hiểm."
   ],
   [
     "In early 2018, suspect Ndlovu commenced orchestrating the liquidation of her own elderly mother, Maria Mushwana, in Bushbuckridge.",
     "Maria was a frail, humble matriarch who spent her lifetime raising children, considering Rosemary the crown jewel of their lineage.",
     "Ndlovu approached a hired mercenary named Lakhiwe Mkhize, paying him an advance of two thousand six hundred Rand to assassinate the elderly mother.",
     "Her instruction was for the hitman to pose as a traditional healer, gaining entrance to poison or suffocate the victim for insurance cash.",
     "Not stopping there, the perpetrator contacted another underworld figure, Njabulo Vincent Kunene, to negotiate an even more monstrous contract.",
     "This target comprised her biological sister Joyce Ndlovu and Joyce's five young children, the youngest being a five-month-old infant.",
     "The diabolical scheme concocted by the policewoman entailed drugging all six individuals, then setting the residence ablaze to mimic an accidental fire.",
     "The promised fee offered for this barbaric mass slaughter was sixty-five thousand Rand, payable once insurance payouts cleared."
   ],
   [
     "2018年初頭、容疑者ンドロヴはブッシュバックリッジに住む実の老母、マリア・ムシュワナの抹殺計画に着手しました。",
     "マリアは一生をかけて子供たちを育て上げ、ローズマリーを一族最高の誇りとして疑わなかった病弱で慎ましい母親でした。",
     "ンドロヴはラキウェ・ムキゼという雇われの殺し屋に接近し、実母を暗殺する手付金として2600ランドを支払いました。",
     "その指示内容は、伝統的な祈祷師を装って家に侵入し、毒殺または窒息によって母親の命を奪えというものでした。",
     "それにとどまらず、容疑者は裏社会の人物であるニャブロ・ヴィンセント・クネネに接触し、さらに残虐な契約を持ちかけました。",
     "標的となったのは、実妹のジョイス・ンドロヴと彼女の5人の幼い子供たちであり、末子はわずか生後5ヶ月の乳児でした。",
     "この女性警官が練り上げた計画は、母子6人全員に睡眠薬を飲ませた上で家に放火し、不慮の火災事故に偽装するというものでした。",
     "この凄惨な大量殺戮の見返りとして彼女が提示した報酬は、保険金が下りた後に支払う6万5千ランドでした。"
   ]
  ),

  ("2.09", 2, "HOST", "nhấn mạnh sự tột cùng của tội ác",
   [
     "Một người phụ nữ khoác áo cảnh sát sẵn sàng ra lệnh thiêu sống chính những đứa cháu ruột còn đang ẵm ngửa để đổi lấy vài cọc tiền giấy.",
     "Đó là sự sụp đổ toàn diện của mọi chuẩn mực đạo đức tối thiểu trong xã hội loài người.",
     "Thế nhưng, chính trong thời khắc đen tối nhất ấy, một biến cố tâm lý bất ngờ đã xảy ra làm đảo lộn hoàn toàn bàn cờ tội ác.",
     "Một tia sáng lương tri le lói đã bất ngờ bùng lên từ chính nơi mà kẻ thủ ác không bao giờ ngờ tới nhất."
   ],
   [
     "A woman cloaked in police authority was prepared to incinerate her own nursing infant nieces and nephews for stacks of paper currency.",
     "This marked the absolute collapse of the most fundamental moral baseline in human society.",
     "Yet precisely at that pitch-black juncture, an unforeseen psychological pivot shattered the entire architecture of her crimes.",
     "A flicker of human conscience unexpectedly ignited in the very quarter the killer least anticipated."
   ],
   [
     "警察官の制服をまとった女性が、紙幣の束を手に入れるため、まだ乳を飲む幼子を含む実の甥や姪を生きたまま焼き殺そうとしたのです。",
     "それは人間社会におけるあらゆる最低限の道徳規範が、完全に崩壊した瞬間でした。",
     "しかし、まさにその最も暗い岐路において、犯罪の盤面全体を根底から覆す予期せぬ心理的変容が起こりました。",
     "加害者が最も警戒していなかった場所から、微かな人間の良心の光が突如として立ち現れたのです。"
   ]
  ),

  ("2.10", 2, "CHUYÊN GIA TÂM LÝ", "đúc kết sự leo thang của ảo tưởng ái kỷ",
   [
     "Khi một kẻ thái nhân cách đạt tới đỉnh cao của ảo tưởng toàn năng, họ sẽ hoàn toàn đánh mất khả năng phán đoán giới hạn của thế giới thực.",
     "Rosemary Ndlovu tin rằng đồng tiền có thể mua chuộc được tất cả và mọi con người trên thế giới này đều mang bản chất tham lam giống như bà ta.",
     "Bà ta đánh đồng những kẻ đánh thuê ngoài xã hội với sự băng hoại nhân cách không đáy của chính mình.",
     "Đó chính là sai lầm chết người và là điểm mù nhận thức lớn nhất của một bản ngã ái kỷ bệnh hoạn.",
     "Kẻ thủ ác đã không thể hiểu được rằng, ngay cả trong thế giới ngầm tăm tối nhất, ranh giới giữa cái ác thông thường và sự phi nhân tính tột cùng vẫn luôn tồn tại.",
     "Chính sự ngộ nhận về ranh giới tâm lý ấy đã dẫn lối cho sự sụp đổ không thể cứu vãn của đối tượng."
   ],
   [
     "When a severe psychopath scales the pinnacle of omnipotent fantasy, they entirely lose the capacity to gauge reality's boundaries.",
     "Rosemary Ndlovu believed money could buy anything and that all human beings shared her bottomless, corrupt greed.",
     "She projected her own complete moral depravity onto street mercenaries, assuming they possessed no moral floor.",
     "That catastrophic miscalculation constituted the fatal cognitive blind spot of her pathological narcissism.",
     "The killer failed to grasp that even in the darkest criminal underworld, a boundary remains separating common crime from sheer monstrosity.",
     "That fundamental misunderstanding of human psychological thresholds directly catalyzed her irreparable downfall."
   ],
   [
     "重度のサイコパスが全能感の頂点に達するとき、現実世界が持つ限界を測る判断力は完全に喪失してしまいます。",
     "ローズマリー・ンドロヴは、金さえ積めばすべてが解決し、この世のすべての人間が自分と同じ底なしの強欲に染まっていると信じ込んでいました。",
     "彼女は裏社会の殺し屋たちに対しても、自らと同じ破綻した人格倫理を勝手に投影していたのです。",
     "その致命的な誤認こそが、病的な自己愛が抱える最大の認知的盲点でした。",
     "どれほど暗い裏社会であっても、通常の悪事と徹底した非人間的蛮行との間には、越えてはならない境界線が存在することを彼女は理解できませんでした。",
     "心理的境界に対するその完全な見誤りこそが、彼女を不可避の破滅へと決定的に導くことになったのです。"
   ]
  ),

  ("2.11", 2, "HOST", "thắt lại Hồi 2",
   [
     "Chiếc bẫy tội ác tưởng chừng như hoàn hảo đã bắt đầu xuất hiện những vết rạn nứt chí mạng đầu tiên từ bên trong.",
     "Con đường dẫn tới công lý chuẩn bị được khai mở bởi chính sự thức tỉnh đầy giằng xé của những con người từng đứng trong bóng tối.",
     "Những bước chân bí mật trong đêm tối sắp sửa định đoạt số phận của kẻ chủ mưu tàn độc."
   ],
   [
     "The seemingly foolproof trap of evil began exhibiting its first fatal structural fractures from within.",
     "The path toward justice was about to be blazed by the agonizing moral awakening of men who once walked in shadows.",
     "Covert footsteps in the dark were about to irrevocably decide the destiny of this ruthless mastermind."
   ],
   [
     "完璧に見えた悪の罠の内側に、最初の致命的な構造的亀裂が走り始めました。",
     "正義へと続く道は、かつて闇の中に身を置いていた男たちの苦悩に満ちた道徳的覚醒によって切り拓かれようとしていました。",
     "暗闇の中で交わされた秘密の足音が、この冷酷な首謀者の運命を決定づけようとしていたのです。"
   ]
  ),

  # --- ACT 3 ---
  ("3.02", 3, "HOST", "đặt vấn đề gây chấn động về sự chuyển hóa tâm lý",
   [
     "Tại sao một kẻ đánh thuê từng sống bằng bạo lực lại đột ngột dừng bước trước một bản hợp đồng béo bở?",
     "Điều gì đã khiến những tên tội phạm chuyên nghiệp quyết định quay đầu và phản bội lại chính người thuê mình?",
     "Cơ chế tâm lý nào đã đánh sập lòng tham và đánh thức lương tri của những con người vốn dĩ quen thuộc với bóng tối giang hồ?",
     "Đây chính là nút thắt nhân bản sâu sắc nhất và là bước ngoặt quyết định đưa toàn bộ chuỗi tội ác của Rosemary Ndlovu ra ánh sáng."
   ],
   [
     "Why would a hired gun, accustomed to violence, suddenly halt before a highly lucrative contract?",
     "What compelled hardened underworld figures to turn around and betray the very person who commissioned them?",
     "What psychological mechanism shattered raw greed and awakened conscience within men steeped in street criminality?",
     "This represents the most profound humanitarian pivot and the decisive turning point exposing Rosemary Ndlovu's crimes to light."
   ],
   [
     "暴力で生計を立ててきた裏社会の殺し屋が、なぜ巨額の報酬を前にして突如としてその足を止めたのでしょうか。",
     "何が職業的犯罪者たちを翻意させ、自らを雇った人物を裏切らせる決断へと駆り立てたのでしょうか。",
     "暗黒街の現実に慣れ親しんでいた男たちの貪欲さを打ち砕き、良心を呼び覚ました心理メカニズムとは一体何だったのか。",
     "これこそが最も深遠な人間的葛藤であり、ローズマリー・ンドロヴの全犯罪を白日の下に晒した決定的な転換点でした。"
   ]
  ),

  ("3.04", 3, "HOST", "tái hiện cuộc hội ngộ nghẹt thở",
   [
     "Hãy quay trở lại thời điểm sát thủ Lakhiwe Mkhize nhận lệnh đến căn nhà của bà mẹ già Maria Mushwana tại Bushbuckridge.",
     "Hắn mang theo vũ khí trong người, bước vào căn nhà vắng vẻ với mục đích tước đoạt sinh mạng của một người phụ nữ xa lạ để lấy tiền công.",
     "Thế nhưng, khi cánh cửa gỗ mở ra, hình ảnh hiện ra trước mắt hắn lại là một bà cụ già yếu, lưng còng với ánh mắt hiền từ và đôi bàn tay nhăn nheo lam lũ.",
     "Bà cụ không hề phòng bị, ân cần đón tiếp kẻ lạ mặt bằng sự chất phác mộc mạc của một người mẹ nơi thôn dã.",
     "Khoảnh khắc hai ánh mắt chạm nhau giữa gian phòng khách nghèo nàn đã tạo nên một cơn địa chấn tâm lý dữ dội đánh thẳng vào tiềm thức của tên sát thủ."
   ],
   [
     "Return to the moment when hitman Lakhiwe Mkhize arrived at the humble dwelling of elderly mother Maria Mushwana in Bushbuckridge.",
     "Concealing weapons, he stepped into the quiet house with the singular intent of taking a stranger's life for financial gain.",
     "Yet as the worn wooden door creaked open, he was confronted by a frail, bent grandmother with benevolent eyes and calloused hands.",
     "The elderly woman, possessing zero defense, welcomed the stranger with the genuine, unassuming warmth of a village mother.",
     "The moment their gazes locked within that modest living room unleashed a violent psychological seismic wave straight into the hitman's subconscious."
   ],
   [
     "雇われの殺し屋ラキウェ・ムキゼが、ブッシュバックリッジにある老母マリア・ムシュワナの質素な家を訪れた瞬間に立ち戻ってみましょう。",
     "彼は武器を忍ばせ、報酬と引き換えに見知らぬ女性の命を奪うという明確な目的を持って、静まり返った家に足を踏み入れました。",
     "しかし、古びた木の扉が開いたとき、彼の前に現れたのは、曲がった背中と慈愛に満ちた瞳、長年の労働を物語る皺だらけの手を持つ病弱な老女でした。",
     "老女は何の警戒心も抱かず、村の母親特有の純朴で温かなもてなしの心で、見知らぬ訪問者を迎え入れたのです。",
     "その慎ましい居間で二人の視線が交錯した瞬間、殺し屋の無意識の深層に激しい心理的衝撃波が直撃しました。"
   ]
  ),

  ("3.05", 3, "ĐIỀU TRA VIÊN", "nhấn mạnh chi tiết lời khai của sát thủ",
   [
     "Tại cơ quan điều tra và sau đó là trước vành móng ngựa, Lakhiwe Mkhize đã nghẹn ngào thuật lại khoảnh khắc quyết định ấy.",
     "Hắn khai rằng khi nhìn vào gương mặt đôn hậu của bà cụ, toàn bộ sức mạnh và ý chí giết chóc trong người hắn hoàn toàn tan biến.",
     "Bàn tay hắn run rẩy không thể rút hung khí ra khỏi túi áo như kế hoạch đã định sẵn với Rosemary.",
     "Thay vì ra tay sát hại nạn nhân, Mkhize bối rối xin bà cụ một cốc nước lọc để uống rồi vội vã rời khỏi hiện trường.",
     "Hắn chấp nhận mất số tiền thù lao còn lại và kiên quyết từ chối tiếp tục thực hiện phi vụ cho nữ cảnh sát.",
     "Đó là sự thất bại đầu tiên trong chuỗi kế hoạch ám sát tưởng như bất khả chiến bại của Rosemary Ndlovu.",
     "Ánh mắt của người mẹ nghèo khó đã vô tình trở thành tấm lá chắn kiên cố nhất bẻ gãy lưỡi dao của cái ác."
   ],
   [
     "Before detectives and subsequently on the witness stand, Lakhiwe Mkhize choked back emotion as he recounted that decisive crossroads.",
     "He testified that looking into that grandmother's gentle face, every shred of violent intent completely evaporated from his spirit.",
     "His hands trembled uncontrollably, rendering him physically incapable of drawing the weapon as planned with Rosemary.",
     "Instead of carrying out the murder, a deeply disoriented Mkhize asked the elderly woman for a cup of tap water, then fled the scene.",
     "He forfeited the remaining balance of the contract and unequivocally refused to execute further tasks for the policewoman.",
     "It marked the very first failure in Rosemary Ndlovu's seemingly invincible chain of premeditated homicides.",
     "The impoverished mother's eyes inadvertently became an impenetrable moral fortress that broke the blade of evil."
   ],
   [
     "捜査当局の聴取、そしてその後の法廷証言において、ラキウェ・ムキゼはその決定的な瞬間を涙声で振り返りました。",
     "老女の穏やかな顔を見つめた瞬間、自らの内側にあった殺意と暴力の意志が跡形もなく消え失せたと彼は証言しました。",
     "彼の両手は激しく震え、ローズマリーと事前に取り決めていた通りに武器を取り出すことが肉体的に不可能となったのです。",
     "殺害を実行する代わりに、激しく狼狽したムキゼは老女に一杯の水を求め、それを飲み干すと足早に現場を立ち去りました。",
     "彼は残りの報酬をすべて放棄し、この女性警官からの暗殺依頼を金輪際拒絶することを固く決意したのです。",
     "それは、これまで百発百中と思われたローズマリー・ンドロヴの暗殺計画において、初めて生じた決定的な綻びでした。",
     "貧しい老母の無垢な眼差しが、図らずも悪意の刃を打ち砕く最も強固な道徳的防壁となったのです。"
   ]
  ),

  ("3.06", 3, "HOST", "giọng đầy trăn trở",
   [
     "Sự chùn bước của Lakhiwe Mkhize đã cứu sống người mẹ già trong gang tấc nhưng chưa thể dập tắt cơn khát máu của Rosemary.",
     "Bà ta lập tức chuyển hướng sang Njabulo Vincent Kunene và thúc ép hắn thực hiện kế hoạch thiêu sống gia đình người em gái Joyce.",
     "Thế nhưng, một lần nữa, kẻ thủ ác lại vấp phải bức tường thành đạo đức kiên cố của bản năng con người.",
     "Cơn giằng xé nội tâm trong tâm trí những tên tội phạm đánh thuê đã tạo nên một bước ngoặt lịch sử ngoài dự liệu."
   ],
   [
     "Lakhiwe Mkhize's hesitation narrowly spared the mother's life, but it failed to quench Rosemary's murderous drive.",
     "She immediately redirected the assignment to Njabulo Vincent Kunene, pressuring him to incinerate her sister Joyce's family.",
     "Yet once again, the ruthless mastermind collided against the unyielding moral barrier of innate human instinct.",
     "The profound moral turmoil tearing through the hired criminals generated an entirely unprecedented, historic turning point."
   ],
   [
     "ラキウェ・ムキゼの躊躇は老母の生命を辛うじて救いましたが、ローズマリーの凶行への執念を鎮めることはできませんでした。",
     "彼女は標的の実行役を即座にニャブロ・ヴィンセント・クネネへと切り替え、実妹ジョイスの一家を焼き殺す計画を猛烈に急かしました。",
     "しかしここでもまた、冷酷な首謀者は人間本来の防衛的本能が持つ頑強な道徳の壁に正面から衝突することになります。",
     "雇われの犯罪者たちの内面に渦巻いた激しい道徳的葛藤が、誰も予期しなかった歴史的転換点を生み出すことになったのです。"
   ]
  ),

  ("3.07", 3, "CHUYÊN GIA TÂM LÝ", "giải phẫu cơ chế hối hận và sự sụp đổ của lòng tham",
   [
     "Dưới góc độ tâm lý học hành vi, sự chuyển hóa của Kunene và Mkhize là một minh chứng sống động cho hiện tượng “Điểm gãy nhận thức trước lằn ranh cấm kỵ phổ quát”.",
     "Trong tâm lý học đạo đức, có những quy chuẩn mang tính cấm kỵ tuyệt đối đã được mã hóa vào gen di truyền và tiến hóa xã hội của loài người qua hàng vạn năm.",
     "Một kẻ tội phạm có thể sẵn sàng trộm cắp, hành hung hoặc tiêu diệt các đối thủ tranh chấp quyền lợi trong thế giới ngầm để sinh tồn.",
     "Thế nhưng, hành vi sát hại trẻ sơ sinh và thiêu sống phụ nữ cùng con nhỏ vô tội là một lằn ranh đỏ mà tâm lý người bình thường không thể vượt qua.",
     "Khi Rosemary Ndlovu yêu cầu thiêu sống năm đứa trẻ, yêu cầu man rợ ấy đã kích hoạt một phản xạ “Ghê tởm đạo đức nguyên thủy” trong tâm trí Njabulo Kunene.",
     "Nỗi kinh hoàng trước sự độc ác phi nhân tính của người thuê đã đè bẹp hoàn toàn sức cám dỗ của số tiền sáu mươi lăm nghìn Rand.",
     "Đồng thời, sự hối hận ở đây còn được thúc đẩy bởi một cơ chế tâm lý tự vệ vô cùng sắc bén: sự nhận diện kẻ thao túng.",
     "Kunene nhận thức sâu sắc rằng một kẻ sẵn sàng tàn sát cả ruột thịt và mẹ đẻ thì tuyệt đối sẽ không bao giờ để cho những sát thủ đánh thuê được sống yên ổn.",
     "Hắn hiểu rằng việc thực hiện hợp đồng này đồng nghĩa với việc tự ký bản án tử hình cho chính bản thân mình trong tương lai.",
     "Sự kết hợp giữa lương tri trỗi dậy và bản năng sinh tồn đã thúc đẩy đối tượng đưa ra quyết định đảo chiều lịch sử.",
     "Đó là lúc bản năng bảo vệ giống loài đã chiến thắng tuyệt đối trước những toan tính vật chất tầm thường."
   ],
   [
     "Behavioral profiling indicates the transformation of Kunene and Mkhize exemplifies a cognitive rupture before universal evolutionary taboos.",
     "In moral psychology, certain absolute taboos have been encoded into human genetics and societal evolution across tens of thousands of years.",
     "A criminal may readily engage in theft, physical assaults, or the targeted elimination of underworld rivals for survival or gain.",
     "However, incinerating mothers and innocent nursing infants represents a universal red line that human psychology fundamentally rejects.",
     "When Rosemary Ndlovu demanded burning five children alive, that monstrous directive triggered profound, primitive moral revulsion inside Kunene.",
     "The visceral horror elicited by the client's absolute depravity utterly crushed the material allure of sixty-five thousand Rand.",
     "Simultaneously, this remorse was galvanized by an acute self-preservation instinct: recognizing the terminal nature of the manipulator.",
     "Kunene realized that someone willing to slaughter her own mother and siblings would never permit hired accomplices to remain alive.",
     "He understood that executing this monstrous contract was tantamount to signing his own future execution warrant.",
     "The confluence of awakened conscience and sharp survival calculations compelled the operative to execute a historic reversal.",
     "It was a defining triumph of primal species preservation over transient material temptation."
   ],
   [
     "行動心理学の見地から見れば、クネネとムキゼの心理的変容は「普遍的タブーの限界線における認知的破断」の鮮烈な実例です。",
     "道徳心理学において、人類が数万年にわたる遺伝的および社会的な進化を通じて培ってきた絶対的タブーが存在します。",
     "犯罪者は生存や利害のため、窃盗や傷害、さらには裏社会のライバルに対する排除行為には手を染めるかもしれません。",
     "しかし、無力な母親と乳幼児を生きたまま焼き殺す行為は、通常の人間心理が決して踏み越えられない一線を画しています。",
     "ローズマリーが5人の子供を生きたまま焼き殺せと命じたとき、その常軌を逸した要求はクネネの精神に「原初的な道徳的嫌悪」を激しく引き起こしました。",
     "依頼者の底知れぬ残虐性に対する本能的な恐怖が、6万5千ランドという報酬の物質的魅惑を完全に圧倒したのです。",
     "同時に、この後悔と翻意は、極めて鋭敏な自己防衛本能、すなわち「操り手の本質の見極め」によっても強く後押しされていました。",
     "実の母親や肉親すら平然と抹殺する人間が、事後に雇われの実行犯を生かしておくはずがないことをクネネは本能的に悟ったのです。",
     "この悪魔的な契約を完遂することは、自らの未来の死刑執行令状に署名することと同義であると理解したのです。",
     "呼び覚まされた良心と冷徹な生存本能の結合が、この男を歴史的な告発行動へと決定的に突き動かしました。",
     "それは、卑小な金銭的計算に対して、種を守ろうとする原初の本能が完全な勝利を収めた瞬間でした。"
   ]
  ),

  ("3.08", 3, "HOST", "bóc tách diễn biến tố giác",
   [
     "Thay vì đổ xăng đốt nhà người vô tội, Njabulo Kunene đã bí mật tìm đến một đồn cảnh sát để tố cáo toàn bộ âm mưu đen tối của Rosemary Ndlovu.",
     "Lời khai của một tay giang hồ về việc một nữ trung sĩ cảnh sát đang lên kế hoạch thiêu sống cả gia đình ban đầu nghe như một câu chuyện hoang đường.",
     "Thế nhưng, sự chân thực trong nỗi sợ hãi và những chứng cứ liên lạc mà Kunene cung cấp đã thu hút sự chú ý đặc biệt của một thám tử kỳ cựu.",
     "Đó là Thám tử Cấp cao Keshi Benneth Mabunda, người lúc bấy giờ đang âm thầm theo dõi những điểm bất thường xung quanh các vụ bảo hiểm tại Tembisa.",
     "Thám tử Mabunda ngay lập tức nhận ra đây chính là mảnh ghép còn thiếu để vén màn toàn bộ chuỗi án mạng bí ẩn suốt sáu năm qua.",
     "Một sự phối hợp chưa từng có tiền lệ giữa một sĩ quan điều tra liêm chính và một nhân chứng từng đứng trong bóng tối chính thức được thiết lập.",
     "Họ hiểu rằng chỉ một sơ suất nhỏ cũng có thể khiến tính mạng của sáu mẹ con người em gái bị hủy diệt trong gang tấc.",
     "Kế hoạch giăng lưới bắt quả tang kẻ chủ mưu bắt đầu được triển khai với độ chính xác và bảo mật tuyệt đối."
   ],
   [
     "Instead of dousing the home in gasoline, Njabulo Kunene covertly sought out police authorities to expose Rosemary Ndlovu's monstrous conspiracy.",
     "An underworld figure reporting that an active police sergeant was planning to incinerate her family initially sounded like bizarre fiction.",
     "However, the unfeigned terror in his demeanor and the detailed phone records he provided commanded the acute attention of a seasoned detective.",
     "That investigator was Senior Captain Keshi Benneth Mabunda, who had been quietly probing suspicious insurance anomalies around Tembisa.",
     "Captain Mabunda instantly recognized that this was the vital missing puzzle piece required to crack six years of inexplicable family homicides.",
     "An unprecedented alliance between an incorruptible senior investigator and an underworld whistleblower was formally forged.",
     "Both men fully understood that a single misstep would result in the immediate obliteration of the sister and her five children.",
     "An intricate sting operation designed to catch the mastermind in the act was initiated with uncompromising operational security."
   ],
   [
     "ガソリンを撒いて民家に火をつける代わりに、ニャブロ・クネネは警察当局に秘密裏に接触し、ローズマリーの邪悪な陰謀を告発しました。",
     "現職の女性巡査部長が一族を焼き殺そうとしているという裏社会の男の証言は、当初、荒唐無稽な作り話のように受け取られかねませんでした。",
     "しかし、彼の表情に滲む偽らざる恐怖と提示された詳細な通信記録は、あるベテラン捜査官の鋭敏な嗅覚を捉えました。",
     "それこそが、テンビサ周辺で起きていた不自然な保険金関連の死亡事案を秘密裏に追跡していたケシ・ベネット・マブンダ警部でした。",
     "マブンダ警部は、過去6年間にわたる親族連続変死事件の全貌を解き明かす最後の決定的なピースが手に入ったことを即座に確信しました。",
     "清廉潔白な敏腕捜査官と、かつて闇に生きた内部告発者との間で、前例のない協力関係がここに結実したのです。",
     "一瞬の判断ミスや情報漏洩が、罪なき母子6人の命を即座に奪い去るという極限の緊張感の中で作戦は進められました。",
     "冷酷な首謀者を現行犯で完全包囲するためのおとり捜査網が、極秘裏に、かつ寸分の狂いもなく敷かれ始めたのです。"
   ]
  ),

  ("3.09", 3, "CHUYÊN GIA TÂM LÝ", "bóc tách sự đối lập nhân cách giữa kẻ chủ mưu và đồng phạm",
   [
     "Ở đây chúng ta chứng kiến một sự tương phản tâm lý vô cùng sâu sắc và đầy trớ trêu giữa hai thái cực con người.",
     "Một bên là nữ cảnh sát được đào tạo bài bản, hưởng lương nhà nước, nhưng lại tha hóa đến mức coi mạng sống người thân như rác rưởi.",
     "Một bên là những kẻ ngoài lề xã hội, từng lầm đường lạc lối, nhưng vẫn giữ lại được đốm lửa lương tri tối thiểu trước sự sống của những đứa trẻ thơ.",
     "Sự hối hận chân thực không đo đếm bằng địa vị xã hội hay bộ đồng phục khoác trên mình, mà đo bằng năng lực biết dừng lại trước tội ác.",
     "Chính sự dừng lại của những kẻ đánh thuê đã trở thành nhịp cầu đưa công lý quay trở lại với vùng đất Tembisa.",
     "Đó là bài học đắt giá về việc bản chất thiện lương của con người có thể trỗi dậy từ những nơi tăm tối và hoang phế nhất.",
     "Sự phản tỉnh ấy đã cứu vớt không chỉ sáu sinh mạng vô tội, mà còn cứu vớt chính phần người còn sót lại trong tâm hồn những kẻ lầm lỡ.",
     "Một lằn ranh đạo đức rõ rệt đã được vạch ra giữa sự tha hóa nhân cách hoàn toàn và năng lực phản tỉnh của lương tri."
   ],
   [
     "Here we bear witness to a profoundly ironic and stark psychological contrast between two distinct human poles.",
     "On one side stands a trained law enforcement officer drawing state salary, yet so depraved she treated kin's lives as trash.",
     "On the opposite side stand marginalized outlaws who nevertheless safeguarded an unquenchable spark of humanity before innocent young lives.",
     "Genuine moral remorse is never determined by social rank or official uniforms, but by the innate capacity to halt before monstrosity.",
     "It was precisely the refusal of these mercenaries that served as the bridge ushering justice back to Tembisa.",
     "This delivers an invaluable behavioral lesson: human decency can awaken from the most desolate, shadowed margins of society.",
     "That crucial reflection not only rescued six innocent lives, but reclaimed the remnants of humanity within the souls of fallen men.",
     "A definitive moral boundary was permanently etched between irredeemable sociopathy and the restorative power of conscience."
   ],
   [
     "ここで私たちは、人間性の対極に位置するふたつの極点の間にある、極めて皮肉で深遠な心理的対比を目撃することになります。",
     "一方には、公的教育を受け国家の給与を得ていながら、肉親の命を塵芥のように扱えるまでに精神を腐敗させた女性警官がいます。",
     "そしてもう一方には、裏社会に生き道を誤りながらも、無力な幼子の命の前で決して消えることのない人間性の火種を守り抜いた男たちがいます。",
     "真の道徳的悔悟とは、社会的地位や身にまとう制服で決まるものではなく、蛮行の直前で踏みとどまる能力にこそ宿るものです。",
     "この雇われの実行犯たちが足を止めたことこそが、テンビサの地に再び司法の正義を呼び戻す決定的な架け橋となりました。",
     "それは、最も荒涼とした社会の暗がりからでも、人間の良心の光が力強く甦り得るという尊い行動科学の教訓です。",
     "その痛切な反省は、罪なき6人の生命を救っただけでなく、道を誤った男たちの魂に残されていた人間性の残滓をも救い出しました。",
     "救いようのない反社会的人格の崩壊と、良心の自己回復力との間に、明確で揺るぎない道徳の境界線が引かれたのです。"
   ]
  ),

  ("3.10", 3, "HOST", "khép lại Hồi 3",
   [
     "Một kế hoạch phản gián và gài bẫy ngầm đỉnh cao đã nhanh chóng được thiết lập dưới sự chỉ huy của Thám tử Mabunda.",
     "Kẻ thủ ác vẫn đinh ninh rằng đàn em đang răm rắp thi hành mệnh lệnh mà không hề hay biết rằng từng lời nói của mình đang được ghi lại từng giây từng phút.",
     "Giờ khắc đền tội của nữ cảnh sát biến chất đã chính thức điểm."
   ],
   [
     "A masterclass undercover sting operation was swiftly engineered under the tactical command of Captain Mabunda.",
     "The perpetrator remained completely convinced her subordinates were obediently following directives, unaware every syllable was being recorded second by second.",
     "The hour of reckoning for this corrupt officer had definitively struck."
   ],
   [
     "マブンダ警部の指揮の下、極めて高度なおとり捜査作戦が迅速に展開されました。",
     "自らの放った手下たちが命令に盲従していると信じ切っていた首謀者は、自らの一言一句が秒単位で記録されていることに全く気づいていませんでした。",
     "腐敗した女性警官に罪の報いが下される審判の時が、ついに告げられようとしていたのです。"
   ]
  ),

  # --- ACT 4 ---
  ("4.02", 4, "HOST", "mở đầu Hồi 4",
   [
     "Tháng ba năm 2018, một chiếc xe ô tô lăn bánh dọc theo con đường dẫn tới Bushbuckridge thuộc tỉnh Mpumalanga.",
     "Bên trong xe là Rosemary Ndlovu cùng những người mà bà ta tin rằng là những sát thủ thiện chiến được cử đi thi hành hợp đồng thiêu sống sáu mẹ con người em gái.",
     "Nữ trung sĩ ngồi ở ghế phụ, hoàn toàn thoải mái chỉ đạo từng chi tiết của vụ phóng hỏa với một sự lạnh lùng đến rợn tóc gáy.",
     "Bà ta dặn dò kỹ lưỡng cách tẩm xăng, cách chặn cửa thoát hiểm và cách rời khỏi hiện trường sao cho không để lại bất kỳ dấu vết nào.",
     "Thế nhưng, người tài xế đang lái xe thực chất là một cảnh sát chìm dày dạn kinh nghiệm, và toàn bộ khoang xe đã được lắp đặt các thiết bị ghi hình bí mật."
   ],
   [
     "In March 2018, a nondescript vehicle traveled along the rural roadway heading toward Bushbuckridge in Mpumalanga province.",
     "Inside sat Rosemary Ndlovu alongside men she believed to be ruthless hitmen dispatched to incinerate her sister and five children.",
     "The police sergeant reclined casually in the passenger seat, directing every tactical detail of the arson with chilling detachment.",
     "She gave precise instructions on applying petrol, barricading exits, and evacuating the scene to ensure zero forensic trace remained.",
     "In reality, the driver was an undercover operative, and the vehicle was thoroughly rigged with concealed audio and video surveillance."
   ],
   [
     "2018年3月、ムプマランガ州ブッシュバックリッジへと続く郊外の道路を、1台の乗用車が走行していました。",
     "車内にはローズマリー・ンドロヴと、彼女が実妹母子6人を焼き殺す契約を完遂するために雇ったと信じ込んでいる男たちが乗っていました。",
     "助手席に腰掛けたこの女性巡査部長は、背筋が凍るほどの冷淡さで、放火殺人のあらゆる戦術的詳細を事細かに指示していました。",
     "ガソリンをどう撒くか、いかに脱出口を塞ぐか、証拠を残さずにいかに逃走するかを克明に説いていたのです。",
     "しかし、ハンドルを握っていた運転手は潜入捜査官であり、車内には極小の監視カメラと集音装置が完璧に仕掛けられていました。"
   ]
  ),

  ("4.03", 4, "ĐIỀU TRA VIÊN", "thuật lại chiến dịch nghiệp vụ và bằng chứng video",
   [
     "Đoạn video nghiệp vụ ghi lại cuộc trao đổi trên xe ô tô ngày hôm đó đã trở thành bằng chứng vàng có sức nặng tuyệt đối trước tòa án.",
     "Trong thước phim được phát công khai tại phiên xét xử, công chúng bàng hoàng chứng kiến cảnh Rosemary mô tả chi tiết cách thức thiêu sống người em gái và các cháu ruột.",
     "Bà ta thậm chí còn cười nói thản nhiên và dặn dò các sát thủ không được nương tay ngay cả với đứa trẻ sơ sinh đang bú mẹ.",
     "Khi chiếc xe dừng lại tại một điểm hẹn quy định để chuẩn bị hành động, lực lượng đặc nhiệm đã bất ngờ ập tới khống chế và bắt giữ quả tang đối tượng.",
     "Tại thời điểm bị tra tay vào còng số tám, Rosemary vẫn tỏ ra vô cùng ngạo mạn và to tiếng quát tháo các đồng đội vì cho rằng họ đã bắt nhầm người.",
     "Bà ta tin chắc rằng với nghiệp vụ cảnh sát của mình, bà ta có thể dễ dàng xóa sạch mọi dấu vết và thoát tội như những lần trước.",
     "Thế nhưng, sự tự tin mù quáng ấy đã sụp đổ hoàn toàn khi toàn bộ băng ghi âm được bảo mật an toàn tại cơ quan công tố.",
     "Từng cử chỉ và lời nói của đối tượng trên chiếc xe định mệnh đã biến thành chiếc thòng lọng pháp lý siết chặt lấy số phận của bà ta.",
     "Chiến dịch vây bắt đã thành công vang dội mà không để xảy ra bất kỳ thương tổn nào cho gia đình của người em gái."
   ],
   [
     "The undercover sting footage captured inside that vehicle that afternoon became the absolute cornerstone evidence presented before the High Court.",
     "In recordings broadcast publicly during the trial, observers were horrified seeing Rosemary detail how to incinerate her sister and young kin.",
     "She laughed casually, explicitly ordering the operatives to show zero mercy even to the nursing five-month-old infant.",
     "When the vehicle pulled into the pre-arranged staging location, heavily armed tactical units instantly swarmed, arresting the suspect red-handed.",
     "As handcuffs locked around her wrists, Rosemary maintained astonishing arrogance, shouting at arresting officers that they were making a grave mistake.",
     "She remained firmly convinced her police insider knowledge would effortlessly dismantle the state's case, as she had done in the past.",
     "However, that blind narcissism disintegrated entirely as encrypted recordings were secured safely by senior prosecutors.",
     "Every chilling word and dismissive gesture inside that vehicle became the definitive legal noose sealing her judicial fate.",
     "The tactical operation achieved total success, ensuring the sister and her children remained entirely untouched and protected."
   ],
   [
     "その日の午後、車内で記録された潜入捜査の映像データは、高等裁判所で提示された最も決定的な動かぬ物証となりました。",
     "法廷で一般公開された映像の中で、ローズマリーが実妹と幼い甥たちを焼き殺す手順を楽しげに語る姿に、傍聴席は息を呑みました。",
     "彼女は何の躊躇もなく笑みを浮かべ、まだ授乳中である生後5ヶ月の乳児に対しても一切の容赦をするなと厳命していたのです。",
     "車が犯行直前の最終合流地点に停車した瞬間、待機していた特殊戦術部隊が突入し、容疑者を現行犯で完全制圧しました。",
     "手錠が手首に打ち込まれた瞬間も、ローズマリーは傲慢な態度を崩さず、重大な誤認逮捕であるとして同僚捜査官たちを一喝しました。",
     "過去の犯行と同様、自らの警察実務知識を駆使すれば、いかなる追及も容易にかわせると彼女は高を括っていたのです。",
     "しかし、その盲目的な自己愛は、暗号化された映像証拠が検察当局によって保全されたことで完全に粉砕されることになりました。",
     "運命の車内で彼女が発した戦慄の一言一句と仕草のすべてが、彼女の法的運命を決定づける強固な絞首縄となったのです。",
     "この電撃的な逮捕作戦は完全な成功を収め、妹一家の生命には指一本触れさせることなく保護が完了しました。"
   ]
  ),

  ("4.04", 4, "HOST", "tiết lộ sự kiên trì của điều tra viên",
   [
     "Thế nhưng, nữ cảnh sát đã đánh giá quá thấp sự bền bỉ của Thám tử Keshi Benneth Mabunda.",
     "Trong suốt nhiều tháng trước đó, Thám tử Mabunda đã âm thầm lật lại toàn bộ hồ sơ của sáu cái chết kỳ lạ liên quan đến Rosemary Ndlovu.",
     "Ông đã làm việc không ngừng nghỉ với hàng chục công ty bảo hiểm, các bệnh viện, nhà xác và các ngân hàng để dựng lại mạng lưới dòng tiền khổng lồ.",
     "Từng bản hợp đồng khống, từng chữ ký giả mạo và từng mốc thời gian chuyển tiền đều được kết nối lại thành một chuỗi bằng chứng đanh thép.",
     "Bản cáo trạng không chỉ nhắm vào vụ bắt quả tang tại Bushbuckridge, mà còn phơi bày trọn vẹn bức tranh thảm sát kéo dài suốt sáu năm."
   ],
   [
     "Yet the rogue policewoman critically underestimated the dogged tenacity of Senior Captain Keshi Benneth Mabunda.",
     "For countless months prior, Captain Mabunda had painstakingly reopened the files of all six suspicious deaths linked to Rosemary Ndlovu.",
     "He coordinated relentlessly across dozens of insurance corporations, mortuaries, medical facilities, and financial institutions to map the money trail.",
     "Every fabricated policy, forged endorsement signature, and timestamped bank transfer was bound into an airtight evidentiary chain.",
     "The forthcoming indictment encompassed far more than the Bushbuckridge sting, systematically laying bare six full years of calculated family slaughter."
   ],
   [
     "しかし、この腐敗した女性警官は、ケシ・ベネット・マブンダ警部が抱く執念の捜査力をあまりにも過小評価していました。",
     "現行犯逮捕に先立つ数ヶ月間、マブンダ警部はローズマリーに関連する過去6件の不審死記録をすべて地道に洗い直していました。",
     "彼は十数社に及ぶ保険会社、死体安置所、医療機関、金融機関の間を奔走し、膨大な不正資金の流れを完全に可視化しました。",
     "偽装された保険契約書、偽造された署名、給付金の送金記録が、反論の余地のない強固な証拠の連鎖として一本に結ばれたのです。",
     "起訴内容はブッシュバックリッジでの未遂事件にとどまらず、過去6年間にわたって計画的に実行された親族虐殺の全容を暴き出すものでした。"
   ]
  ),

  ("4.05", 4, "NGƯỜI BÌNH THƯỜNG", "N2: Lời tự vấn của Njabulo Kunene, giọng nam run rẩy, đầy giằng xé tội lỗi",
   [
     "Tôi từng là một kẻ sống bằng những việc làm đen tối ngoài vòng pháp luật và không bao giờ nghĩ mình sẽ hợp tác với cảnh sát.",
     "Nhưng khi người đàn bà ấy chỉ vào ngôi nhà có năm đứa trẻ đang ngủ và bảo chúng tôi hãy châm lửa thiêu rụi tất cả, tôi đã lạnh toát sống lưng.",
     "Đó không còn là chuyện phạm pháp thông thường nữa, đó là sự tàn sát một bầy trẻ vô tội không có khả năng tự vệ.",
     "Hình ảnh những đứa bé vô tội cứ ám ảnh tâm trí tôi suốt cả chặng đường đi, khiến tôi không thể nào thở nổi.",
     "Tôi biết rằng nếu tôi đồng ý làm theo lời bà ta, linh hồn tôi sẽ vĩnh viễn bị đọa đày trong tội lỗi và ngọn lửa căm hờn của nhân loại.",
     "Việc tôi bước vào đồn cảnh sát để tố cáo không phải để mong được tha thứ, mà là để chặn đứng bàn tay độc ác của một con quỷ đội lốt người.",
     "Tôi thà chấp nhận ngồi tù vì những lỗi lầm cũ của mình còn hơn là phải sống suốt đời với ký ức về tiếng khóc của những đứa trẻ trong biển lửa.",
     "Khoảnh khắc nhìn thấy các đặc nhiệm ập vào bắt giữ bà ta, gánh nặng tội lỗi đè nặng trên ngực tôi dường như mới vơi đi phần nào."
   ],
   [
     "I was an outlaw who operated in the shadows for years, and I never in my life imagined I would ever walk into a police station to cooperate.",
     "Yet when that woman pointed toward a house where five innocent children slept and instructed us to incinerate them all, my spine turned to ice.",
     "That was no longer ordinary street criminality; it was the outright slaughter of helpless, defenseless infants.",
     "The vision of those innocent children haunted my thoughts relentlessly throughout that entire journey, suffocating my breath.",
     "I knew with absolute certainty that if I obeyed her, my soul would be damned forever in guilt and the righteous fury of humanity.",
     "Walking into the police station was never about seeking personal pardon; it was about stopping the hands of a demon wearing human flesh.",
     "I would far rather face imprisonment for my past transgressions than live a single day haunted by the screams of burning babies.",
     "The moment tactical officers swarmed and secured her in handcuffs, the crushing moral weight on my chest finally began to lift."
   ],
   [
     "私は長年裏社会の闇の中で生きてきた人間であり、警察に自ら協力するなど自分の人生において夢にも思っていませんでした。",
     "しかし、あの女が5人の幼子が眠る家を指差し、全員を生きたまま焼き殺せと命じたとき、私の背筋は完全に凍りつきました。",
     "それはもはや金目当ての犯罪などではなく、何の抵抗もできない無力な子供たちに対する明白な大虐殺でした。",
     "道中ずっと、無垢な子供たちの寝顔が私の脳裏に焼き付いて離れず、息をすることすら苦しくてたまりませんでした。",
     "もしあの女の指示に従って火を放てば、自分の魂は未来永劫、耐えがたい罪悪感と人類の怒りの炎に焼かれ続けると直感しました。",
     "私が警察署の門を叩いたのは、減刑や許しを乞うためではなく、人間の皮をかぶった悪魔の凶行を絶対に阻止するためでした。",
     "炎の中で叫ぶ子供たちの声を背負って生きるくらいなら、過去の過ちを認めて刑務所に入ったほうが遥かに救われると思いました。",
     "特殊部隊が突入して彼女の両手に手錠をかけた瞬間、私の胸を押し潰していた重苦しい罪の重圧がようやく解き放たれたのです。"
   ]
  ),

  ("4.07", 4, "HOST", "tiếp tục diễn biến đối đầu trong phòng thẩm vấn",
   [
     "Khi bị đưa vào phòng thẩm vấn của Cơ quan Điều tra Độc lập, chiếc mặt nạ kiêu hãnh của nữ trung sĩ bắt đầu bộc lộ những rạn nứt nghiêm trọng.",
     "Đối diện với Thám tử Mabunda cùng hàng xấp tài liệu tài chính dày đặc đặt trên bàn, bà ta liên tục thay đổi lời khai và tìm cách chối tội.",
     "Bà ta đổ lỗi cho các thầy phù thủy truyền thống đã yểm bùa xui khiến, rồi lại quay sang khẳng định mình mua bảo hiểm chỉ vì lòng tốt muốn giúp đỡ dòng họ.",
     "Thế nhưng, khi đoạn video ghi âm ghi hình ngầm được bật lên trên màn hình lớn, căn phòng thẩm vấn bỗng chốc rơi vào sự im lặng đặc quánh.",
     "Từng câu chữ lạnh lùng do chính miệng bà ta thốt ra đã tước đoạt toàn bộ không gian biện hộ cuối cùng của kẻ thủ ác.",
     "Những lời dối trá tinh vi nhất đã hoàn toàn bị bẻ gãy trước sức mạnh không thể chối cãi của sự thật khách quan."
   ],
   [
     "Brought into the interrogation suite of the Independent Police Directorate, the sergeant's mask of arrogance suffered catastrophic fractures.",
     "Confronted by Captain Mabunda across tables overflowing with forensic banking ledgers, she frantically modified her claims, denying culpability.",
     "She deflected blame onto traditional sangomas for bewitching her, then pivoted to asserting she purchased policies purely out of familial generosity.",
     "However, when the undercover sting recordings were projected onto the large monitors, the room plummeted into dense, suffocating silence.",
     "Every chilling syllable spoken by her own lips permanently stripped away her final avenues of legal denial.",
     "Her most elaborate webs of deceit were utterly dismantled before the undeniable weight of objective scientific evidence."
   ],
   [
     "独立警察捜査局の取調室に連行されたとき、この巡査部長が誇示していた傲慢な仮面は、ついに破滅的な亀裂を見せ始めました。",
     "机を埋め尽くす膨大な金融取引記録を前にマブンダ警部と対峙した彼女は、供述を二転三転させながら必死に罪を逃れようと試みました。",
     "呪術師に呪いをかけられて操られていたと言い訳し、次の瞬間には親族への純粋な善意から保険をかけていただけだと強弁したのです。",
     "しかし、車内の潜入捜査映像が大画面モニターに再生された瞬間、取調室の空気は重苦しく凍りつきました。",
     "自らの口から吐き出された冷酷無残な肉声の一言一句が、この殺人鬼に残されていた最後の弁解の余地を完全に奪い去ったのです。",
     "どれほど巧妙に張り巡らされた虚飾の嘘も、客観的証拠が持つ圧倒的な真実の重みの前に完全に粉砕されました。"
   ]
  ),

  ("4.08", 4, "ĐIỀU TRA VIÊN", "thuật lại phản ứng ngoan cố của đối tượng",
   [
     "Thay vì cúi đầu nhận tội trước những chứng cứ khoa học không thể chối cãi, đối tượng Ndlovu lại chuyển sang thái độ giận dữ và đe dọa.",
     "Bà ta thậm chí còn tìm cách liên hệ với thế giới ngầm từ trong trại giam để thuê sát thủ ám sát chính Thám tử Mabunda và các nhân chứng quan trọng.",
     "Hành vi ngoan cố đến cùng này cho thấy mức độ nguy hiểm cực độ và sự băng hoại nhân cách không thể cứu vãn của đối tượng.",
     "Tuy nhiên, mọi toan tính bẩn thỉu của bà ta đều bị lực lượng an ninh phong tỏa và đập tan kịp thời."
   ],
   [
     "Rather than conceding guilt before irrefutable forensic evidence, suspect Ndlovu pivoted to explosive fury and overt intimidation.",
     "She even attempted reaching out to underworld contacts from within her holding facility to contract hits on Captain Mabunda and key state witnesses.",
     "This defiant trajectory underscored her exceptional dangerousness and the irredeemable degradation of her underlying personality.",
     "Nevertheless, every malicious maneuver she attempted was systematically neutralized and neutralized by security forces."
   ],
   [
     "動かしがたい科学的証拠を突きつけられてなお、容疑者ンドロヴは自らの罪を認めるどころか、激しい怒りと威嚇の態度を剥き出しにしました。",
     "彼女は拘置所の内部から裏社会の伝手を利用し、事件を暴いたマブンダ警部と重要証言者たちの暗殺を外部へ依頼することすら試みました。",
     "最後まで抵抗を続けようとするその狂気じみた執念は、彼女の人格破綻の深さと、社会に対する極度の危険性を証明していました。",
     "しかし、そうした悪あがきの企てはすべて、厳戒態勢を敷いた治安当局によって未然に察知され、完全に粉砕されました。"
   ]
  ),

  ("4.09", 4, "CHUYÊN GIA TÂM LÝ", "phân tích tâm lý của kẻ thủ ác khi bản ngã sụp đổ",
   [
     "Quan sát diễn biến hành vi của Rosemary Ndlovu trong suốt quá trình điều tra và xét xử, chúng ta thấy rõ hiện tượng “Sự sụp đổ cái tôi ái kỷ”.",
     "Khi nhận thấy quyền lực hành pháp và sự dối trá không còn khả năng thao túng được thực tại, đối tượng rơi vào trạng thái hoảng loạn sâu sắc.",
     "Tuy nhiên, ở những kẻ có nhân cách thái nhân cách nặng, sự hoảng loạn này không bao giờ chuyển hóa thành sự ăn năn chân chính.",
     "Thay vào đó, nó biến thành “Sự tự thương hại bệnh lý” kết hợp với các màn kịch tính hóa cảm xúc giả tạo.",
     "Bà ta gào khóc thảm thiết, than vãn về những cơn đau tức ngực bất ngờ và liên tục gián đoạn phiên tòa bằng các yêu cầu y tế vô căn cứ.",
     "Những giọt nước mắt ấy hoàn toàn không phải để khóc thương cho những người thân đã bị bà ta đẩy vào cõi chết.",
     "Đó chỉ là những giọt nước mắt xót xa cho sự tự do đã mất và sự căm phẫn tột cùng khi bản thân bị vạch trần trước toàn thể xã hội.",
     "Sự tương phản giữa nụ cười ngạo mạn ngoài hành lang và những tiếng khóc gào trong phòng xử án chính là bằng chứng xác thực nhất của sự giả tạo.",
     "Đó là chân dung của một nhân cách ái kỷ không bao giờ dám đối diện với sự hèn nhát và tội lỗi của chính mình."
   ],
   [
     "Observing Rosemary Ndlovu's conduct throughout the trial highlights the textbook phenomenon of Narcissistic Collapse.",
     "When official badge authority and manipulative deceptions failed to control reality, the subject experienced severe internal decompensation.",
     "Yet in severe psychopathy, this panic never transmutes into genuine, moral remorse.",
     "Instead, it morphs into pathological self-pity intertwined with melodramatic, histrionic courtroom performances.",
     "She wailed theatrically, complained of sudden chest pains, and repeatedly disrupted legal sessions with spurious medical emergencies.",
     "Those theatrical tears were never shed out of genuine sorrow for the family members she coldly consigned to the grave.",
     "They were weeping solely for her forfeited liberty and boiling resentment at being exposed before the eyes of the nation.",
     "The stark contrast between her casual smiles in corridors and theatrical sobbing on the witness stand laid bare her deception.",
     "This embodies the quintessential portrait of a malignant narcissist utterly incapable of confronting her own cowardice and guilt."
   ],
   [
     "公判を通じて示されたローズマリー・ンドロヴの行動様式は、自己愛が崩壊に瀕した際の古典的な自己愛憤怒の崩壊現象を示しています。",
     "警察バッジの威光や虚飾の言葉で現実を支配できなくなったとき、彼女の精神は激しい内的パニックへと陥りました。",
     "しかし、重度のサイコパスにおいて、このパニックが道徳的で真摯な反省へと昇華されることは決してありません。",
     "それは病理的な自己憐憫へと転じ、法廷内での大仰で芝居がかったヒステリックな演技へと姿を変えたのです。",
     "彼女は号泣して取り乱し、突発的な胸の痛みを訴え、根拠のない医療的措置を要求して公判を幾度となく中断させました。",
     "その大粒の涙は、自らの手で冷酷に墓場へと送り込んだ親族たちへの哀悼の涙などでは決してありませんでした。",
     "失われた自らの自由を嘆き、社会全体の前で化けの皮を剥がされたことに対する底知れぬ怒りと自己執着の涙に過ぎなかったのです。",
     "法廷の廊下で見せた不敵な笑みと、証言台での大仰な号泣との鮮烈な乖離こそが、彼女の底知れぬ欺瞞の動かぬ証拠でした。",
     "これこそが、自らの臆病さと犯した罪の重さに決して向き合うことのできない、悪性自己愛者の真の肖像なのです。"
   ]
  ),

  ("4.10", 4, "HOST", "khép lại Hồi 4",
   [
     "Cuộc điều tra kéo dài nhiều năm ròng rã cuối cùng đã khép lại bằng một bản cáo trạng lịch sử gồm hàng chục tội danh giết người và lừa đảo.",
     "Ánh sáng của công lý và lòng dũng cảm của các điều tra viên đã chính thức đưa kẻ thủ ác ra trước vành móng ngựa của công lý tối cao.",
     "Những bí mật đen tối từng được chôn giấu dưới đáy vực sâu giờ đây đã được phơi bày trọn vẹn dưới ánh sáng mặt trời.",
     "Một phán quyết mang tính lịch sử đang chờ đợi để khép lại một trong những chương đen tối nhất của lịch sử tư pháp Nam Phi.",
     "Bản cáo trạng đanh thép ấy là thành quả của sự phối hợp kiên cường giữa công lý chân chính và lương tri con người.",
     "Mọi ngả đường trốn chạy của tội ác đã bị chặn đứng hoàn toàn trước ngưỡng cửa của công lý."
   ],
   [
     "The exhaustive, multi-year investigation culminated in a landmark indictment encompassing dozens of counts of murder, fraud, and conspiracy.",
     "The clarity of forensic science and investigative courage finally brought this rogue officer before the highest bar of justice.",
     "Dark secrets once buried deep within the abyss were now exposed completely to the unforgiving glare of sunlight.",
     "A historic verdict awaited to close one of the bleakest chapters in South African judicial memory.",
     "That unyielding indictment stood as the monumental triumph of dedicated justice joined with awakened human conscience.",
     "Every avenue of evasion was decisively sealed shut before the threshold of absolute accountability."
   ],
   [
     "長年にわたる過酷な捜査は、多数の殺人罪、詐欺罪、殺人共謀罪を含む歴史的な起訴状の作成をもって完結しました。",
     "科学的証拠の明晰さと捜査官たちの不屈の勇気が、ついにこの腐敗した警官を正義の法廷へと引きずり出しました。",
     "深淵の底に隠蔽されていた忌まわしい秘密の数々が、白日の下に容赦なく晒されることになったのです。",
     "南アフリカ司法の記憶において最も暗い章に終止符を打つ、歴史的な判決の時が静かに迫っていました。",
     "その揺るぎない起訴状は、清廉な司法の執念と、覚醒した人間の良心とが結びついた偉大な記念碑でした。",
     "犯行を隠蔽するためのあらゆる逃走路は、絶対的な法的責任の門前で完全に封鎖されたのです。"
   ]
  ),

  # --- ACT 5 ---
  ("5.02", 5, "HOST", "giọng suy ngẫm, triết lý và đầy xúc động",
   [
     "Tháng mười một năm 2021, tại Tòa án Cấp cao Nam Phi chi nhánh Palm Ridge, phiên tòa xét xử Nomia Rosemary Ndlovu đã thu hút sự chú ý của hàng triệu người dân trên toàn thế giới.",
     "Khán phòng chật kín người tham dự, từ những thân nhân còn sống sót của các nạn nhân cho tới các sĩ quan cảnh sát và đông đảo giới truyền thông quốc tế.",
     "Đứng trước vành móng ngựa, kẻ từng một thời thét ra lửa tại đồn cảnh sát Tembisa South giờ đây phải đối diện với sự thật trần trụi về những tội ác ghê tởm của chính mình.",
     "Không còn chiếc áo đồng phục cảnh sát che chắn, không còn những lời dối trá ngọt ngào, chỉ còn lại sự cô độc của một tâm hồn đã bị lòng tham làm hoen rỉ.",
     "Ánh mắt của công lý từ hàng triệu con người đang dõi theo từng cử chỉ của kẻ đã chà đạp lên những giá trị thiêng liêng nhất của tình thân.",
     "Cả khán phòng nín thở chờ đợi từng lời tuyên án từ vị Thẩm phán chủ tọa phiên tòa.",
     "Đó là thời khắc mà sự thật và lương tri giành lại vị thế tối thượng sau nhiều năm bị bóp nghẹt dưới bóng tối của lòng tham.",
     "Một sự phán xét không chỉ dành riêng cho một cá nhân tội phạm, mà còn là lời cảnh tỉnh nghiêm khắc đối với toàn thể cộng đồng."
   ],
   [
     "In November 2021, at the South African High Court sitting in Palm Ridge, the sentencing of Nomia Rosemary Ndlovu gripped millions globally.",
     "The gallery was packed to capacity, filled with surviving family members, police officers, and international media representatives.",
     "Standing in the prisoner's dock, the woman who once exercised immense authority at Tembisa South Police Station faced the raw truth of her atrocities.",
     "Stripped of her protective police uniform and deprived of manipulative charms, she stood entirely isolated in her morally corroded shell.",
     "The eyes of justice from millions of citizens bore down upon every movement of the woman who desecrated the sacred ties of blood.",
     "The entire courtroom held its collective breath, hanging on every word uttered by the presiding Judge.",
     "This was the definitive moment where truth and conscience reclaimed supremacy after years of suffocation beneath shadows of greed.",
     "It stood as a judgment not merely against a single killer, but as a stern reckoning for societal consciousness."
   ],
   [
     "2021年11月、パーム・リッジに開かれた南アフリカ高等裁判所において、ノミア・ローズマリー・ンドロヴに対する判決言い渡しは世界中の数百万人の注目を集めました。",
     "傍聴席は超満員となり、辛うじて生き残った親族たち、警察官たち、そして世界各国の報道関係者で埋め尽くされていました。",
     "被告人席に立つその姿には、かつてテンビサ・サウス警察署で権勢を振るった威勢はなく、犯した残虐な凶行の冷厳な真実と直面していました。",
     "身を守ってくれた警察の制服も剥ぎ取られ、甘言の嘘も封じられた今、彼女の魂は強欲によって腐食された孤独な器としてそこにありました。",
     "血肉の絆という最も神聖な情愛を踏みにじった女の一挙手一投足に、数百万の市民の正義の視線が突き刺さっていました。",
     "法廷全体が息を呑み、裁判長から紡ぎ出される一語一語を静まり返って待っていました。",
     "それは、強欲の暗闇によって長年窒息させられていた真実と良心が、至高の威厳を取り戻した歴史的瞬間でした。",
     "この判決は、一人の凶悪犯に対する断罪にとどまらず、社会全体の倫理観を揺さぶる厳粛な警鐘となったのです。"
   ]
  ),

  ("5.03", 5, "CHUYÊN GIA TÂM LÝ", "đúc kết sự thức tỉnh và bài học hành vi",
   [
     "Hồ sơ Rosemary Ndlovu để lại một khoảng trống đau đớn nhưng đồng thời cung cấp những bài học vô giá cho khoa học hành vi và tâm lý học xã hội.",
     "Vụ án này phá vỡ hoàn toàn định kiến ngây thơ cho rằng phụ nữ và những người làm công tác bảo vệ pháp luật luôn miễn nhiễm với xu hướng giết người hàng loạt.",
     "Lòng tham bệnh lý kết hợp với cơn nghiện cờ bạc và sự tha hóa quyền lực có thể biến bất kỳ ai thành một con quái vật nếu thiếu đi sự kiểm soát nghiêm ngặt.",
     "Đồng thời, sự việc cũng gióng lên hồi chuông cảnh báo về mối hiểm họa của “Hiệu ứng Hào quang” trong các mối quan hệ xã hội và công việc.",
     "Chúng ta thường có xu hướng hạ thấp cảnh giác trước những người mang danh phận cao quý hoặc những người có quan hệ huyết thống ruột thịt.",
     "Thế nhưng, lịch sử tư pháp đã chứng minh rằng sự phản bội đau đớn nhất luôn xuất phát từ chính những người mà chúng ta trao gửi niềm tin trọn vẹn nhất.",
     "Việc nhận diện sớm các chỉ dấu thao túng và bóc tách chiếc mặt nạ tỉnh táo chính là vũ khí phòng vệ tối thượng của mỗi con người."
   ],
   [
     "The Rosemary Ndlovu case leaves a harrowing void, yet yields invaluable insights for behavioral science and social psychology.",
     "It permanently dismantles the naive assumption that women and sworn law officers are inherently immune to serial predatory violence.",
     "Pathological greed fused with compulsive gambling and unchecked authority can deform any individual into a monster absent rigorous oversight.",
     "Furthermore, it sounds an urgent alarm regarding the mortal perils of the Halo Effect within familial and professional networks.",
     "Human beings routinely lower psychological guards before individuals cloaked in respectable titles or tied by direct bloodlines.",
     "Yet judicial history demonstrates that the most catastrophic betrayals inevitably originate from those granted our unreserved trust.",
     "Developing early recognition of manipulative cues and dissecting the mask of sanity remains humanity's ultimate survival defense."
   ],
   [
     "ローズマリー・ンドロヴの事件記録は痛ましい爪痕を残した一方で、行動科学と社会心理学に対して計り知れない教訓をもたらしました。",
     "この事件は、女性や公権力を担う法執行官が連続的な捕食的暴力とは無縁であるという無邪気な先入観を完全に粉砕しました。",
     "病的な金銭欲、重度のギャンブル依存、そして監視を欠いた公権力の腐敗が重なれば、人間はいとも容易く怪物へと変貌し得るのです。",
     "同時にこの事件は、血縁や職務上の関係性において生じる「ハロー効果」の致命的な危険性について、痛切な警鐘を鳴らしています。",
     "人間は、高潔な職位をまとう者や血のつながった親族に対して、自らの心理的警戒防壁を無意識に下げてしまいがちです。",
     "しかし司法の歴史が証明している通り、最も破滅的な裏切りとは、全幅の信頼を寄せていた身内からこそもたらされるものなのです。",
     "巧妙な操作的手口の初期徴候を見抜き、正気の仮面を冷静に解剖する能力こそが、人間にとって究極の生存防衛手段となります。"
   ]
  ),

  ("5.04", 5, "ĐIỀU TRA VIÊN", "nhận định di sản tư pháp và bản án",
   [
     "Thẩm phán Ramarumo Monama đã tuyên phạt Nomia Rosemary Ndlovu sáu án tù chung thân liên tiếp cho sáu tội danh giết người dã man.",
     "Cộng thêm ba mươi năm tù giam cho các tội danh âm mưu giết người, lừa đảo chiếm đoạt tài sản bảo hiểm và cản trở tiến trình thực thi công lý.",
     "Trong phần tuyên án đanh thép kéo dài nhiều giờ đồng hồ, Thẩm phán nhấn mạnh rằng hành vi của bị cáo là sự sỉ nhục nghiêm trọng nhất đối với màu cờ sắc phục của lực lượng cảnh sát Nam Phi trong suốt gần chín mươi năm qua.",
     "Bản án nghiêm khắc này là lời khẳng định đanh thép rằng không một ai, dù mang trên mình bất kỳ cấp bậc hay quyền lực nào, có thể đứng trên luật pháp và sinh mạng của đồng loại.",
     "Thắng lợi của chuyên án cũng là minh chứng cho sự kiên định không khoan nhượng của lực lượng điều tra liêm chính, đại diện bởi Thám tử Mabunda.",
     "Các quy trình thẩm định bảo hiểm nhân thọ trên toàn quốc sau đó đã được siết chặt toàn diện để ngăn chặn những kẽ hở trục lợi đẫm máu tương tự."
   ],
   [
     "Judge Ramarumo Monama sentenced Nomia Rosemary Ndlovu to six consecutive life terms for six counts of premeditated murder.",
     "She received an additional thirty years' imprisonment for attempted murder, widespread insurance fraud, and defeating the ends of justice.",
     "In a rigorous sentencing address spanning several hours, the Judge emphasized that her actions represented the gravest betrayal of the police uniform in nearly ninety years.",
     "This uncompromising sentence resoundingly affirmed that no individual, regardless of rank or badge, stands above the law or human life.",
     "The triumph of this investigation stands as a testament to the unyielding integrity of principled investigators, embodied by Captain Mabunda.",
     "Subsequently, life insurance underwriting standards nationwide were overhauled to permanently close loopholes enabling such bloodshed."
   ],
   [
     "ラマルモ・モナマ裁判長は、ノミア・ローズマリー・ンドロヴに対し、6件の計画的殺人罪について6回連続の終身刑を言い渡しました。",
     "さらに、殺人未遂罪、大規模な保険金詐欺罪、司法妨害罪に対して、追加で懲役30年の刑が科されました。",
     "数時間に及ぶ峻厳な量刑理由の朗読の中で、裁判長は被告人の所業が過去90年間において警察の制服に対する最も深刻な背徳行為であると指弾しました。",
     "この厳格極まりない判決は、いかなる階級や権力を帯びた者であっても、法と生命の尊厳の上に立つことは許されないという鉄の意志を示しました。",
     "この捜査の完全な勝利は、マブンダ警部に代表される清廉な捜査官たちの不屈の正義感と粘り強さの記念碑となったのです。",
     "この事件を契機に、全国の生命保険審査基準は根本的に見直され、同様の血塗られた制度の悪用を防ぐ厳格な制度改革が進められました。"
   ]
  ),

  ("5.05", 5, "HOST", "chuyển sang phần đúc kết và bài học nhận diện",
   [
     "Khi bản án lịch sử được tuyên đọc, một sự im lặng trang nghiêm bao trùm lấy toàn bộ phòng xử án trước khi vỡ òa trong những giọt nước mắt của gia đình nạn nhân.",
     "Bà mẹ già Maria Mushwana ngồi ở hàng ghế đầu, đôi mắt ngấn lệ nhìn đứa con gái ruột đang bị áp giải rời khỏi phòng xử án trong chiếc còng sắt lạnh ngắt.",
     "Nỗi đau mất đi những đứa con, đứa cháu thân yêu sẽ là vết thương không bao giờ có thể lành lặn trong tâm khảm của người mẹ già tội nghiệp.",
     "Nhưng ít nhất, linh hồn của Maurice Mabasa, của Audrey, của Witness Homu và những đứa trẻ xấu số đã có thể tìm thấy chút thanh thản nơi suối vàng.",
     "Từ thảm kịch đẫm nước mắt của hồ sơ Rosemary Ndlovu, kênh Amber Eyes xin gửi gắm tới cộng đồng ba nguyên tắc cảnh báo đỏ sinh tồn cốt lõi để bảo vệ bản thân và gia đình.",
     "Thứ nhất, hãy luôn cảnh giác cao độ trước mọi yêu cầu cung cấp thông tin cá nhân hoặc việc đứng tên trên các hợp đồng tài chính, bảo hiểm mờ ám, ngay cả khi yêu cầu đó đến từ chính người thân ruột thịt.",
     "Thứ hai, tuyệt đối không bao giờ chủ quan hay để cho “Hiệu ứng Hào quang” của sắc phục, chức vị hay danh tiếng xã hội làm tê liệt trực giác an toàn tự nhiên của bản thân.",
     "Thứ ba, khi phát hiện các dấu hiệu bạo lực tiềm ẩn, âm mưu tội ác hoặc những bất thường đe dọa sinh mạng, hãy dũng cảm tìm kiếm sự hỗ trợ từ các cơ quan bảo vệ pháp luật độc lập thay vì im lặng thỏa hiệp.",
     "Mỗi hành trình giải mã tâm lý tội phạm cùng Amber Eyes không nhằm khơi gợi nỗi sợ hãi, mà để thắp sáng sự hiểu biết và nâng cao nhận thức bảo vệ bản thân cho mỗi chúng ta.",
     "Chiếc mặt nạ hoàn hảo của cái ác có thể đánh lừa được mắt nhìn nhất thời, nhưng lương tri và sự thật sẽ luôn là ngọn hải đăng soi rọi công lý.",
     "Xin hãy luôn trân trọng cuộc sống, bảo vệ những người thân yêu và giữ vững sự tỉnh thức trước mọi cám dỗ và nguy cơ tiềm ẩn.",
     "Lòng dũng cảm dám nhìn thẳng vào bóng tối chính là nguồn sức mạnh vĩ đại nhất giúp chúng ta bảo vệ những giá trị thiêng liêng của cuộc đời.",
     "Cảm ơn quý vị khán giả đã luôn đồng hành cùng kênh trong từng tập hồ sơ chuyên sâu.",
     "Sự ủng hộ và đồng cảm của quý vị chính là động lực to lớn để chúng tôi tiếp tục hành trình phụng sự công lý và sự thật.",
     "Xin chào và hẹn gặp lại quý vị trong những hành trình tiếp theo."
   ],
   [
     "As that historic verdict was pronounced, a solemn stillness held the courtroom before shattering into tears wept by the victims' kin.",
     "Elderly mother Maria Mushwana sat in the front row, tearful eyes watching her daughter escorted away in cold steel handcuffs.",
     "The agony of losing children and grandchildren remains an indelible wound etched forever into the heart of this grieving matriarch.",
     "Yet at long last, the souls of Maurice Mabasa, Audrey, Witness Homu, and their young kin may find peace in eternity.",
     "From the tears of the Rosemary Ndlovu tragedy, Amber Eyes presents three essential survival red flags to safeguard your family.",
     "First, maintain uncompromising vigilance regarding requests for personal identification or ambiguous financial insurance policies, even when originating from immediate kin.",
     "Second, never permit the Halo Effect of official uniforms, institutional prestige, or social status to anesthetize your innate safety instincts.",
     "Third, upon sensing covert danger, criminal plots, or existential threats, boldly seek intervention from independent authorities rather than yielding to silence.",
     "Every investigative journey with Amber Eyes seeks not to provoke dread, but to illuminate understanding and strengthen individual survival awareness.",
     "The perfect mask of evil may deceive superficial observation temporarily, but conscience and empirical truth remain eternal beacons of justice.",
     "Cherish your life, fiercely protect your loved ones, and maintain relentless vigilance against hidden perils and destructive temptations.",
     "The moral courage to confront the darkness directly remains our greatest power in preserving the sanctity of human existence.",
     "We extend our profound gratitude to our viewers for walking alongside us through every forensic case file.",
     "Your enduring support and empathetic resonance provide our greatest momentum in championing the cause of truth and justice.",
     "Farewell, and we look forward to reuniting with you in our forthcoming investigative journeys."
   ],
   [
     "歴史的な判決が言い渡された瞬間、法廷内は静まり返り、やがて被害者遺族たちの嗚咽と涙によって満たされました。",
     "最前列に座っていた老母マリア・ムシュワナは、冷たい鉄の手錠をはめられ連行されていく我が子の後ろ姿を涙の瞳で見つめていました。",
     "愛する我が子や孫たちを奪われた痛恨の悲哀は、この悲劇の母親の胸の奥底で決して癒えることのない傷痕として残るでしょう。",
     "しかし少なくとも、モーリス・マバサ、オードリー、ウィットネス・ホム、そして幼き甥たちの魂は、黄泉の国で安らかな平穏を見出すことができます。",
     "ローズマリー・ンドロヴの涙に濡れた事件記録から、アンバー・アイズは皆様とご家族の身を守るための「3つの生存レッドフラッグ原則」を提唱します。",
     "第1に、身元情報の提供要請や不透明な金融・保険契約の締結を求められた際は、たとえ血のつながった近親者であっても常に厳格な警戒を維持すること。",
     "第2に、制服や社会的地位、輝かしい肩書がもたらす「ハロー効果」によって、自らの本能的な危険察知能力を決して麻痺させないこと。",
     "第3に、潜在的な暴力の兆候、犯罪の企て、または生命の危機を察知した際は、沈黙して妥協することなく、勇気を持って独立した治安当局の支援を求めること。",
     "アンバー・アイズが届ける犯罪心理の解読は、単に恐怖を煽るためのものではなく、知性を照らし、皆様の自己防衛意識を研ぎ澄ますためのものです。",
     "悪の完璧な仮面は一時的に人の目を欺くかもしれませんが、人間の良心と客観的真実は、常に正義を照らし出す不動の灯台であり続けます。",
     "どうか自らの命をいつくしみ、愛する人々を守り抜き、あらゆる誘惑と潜在的危機に対して絶え間ない覚醒を保ち続けてください。",
     "深淵の闇を恐れずに直視する勇気こそが、私たちの命の尊厳を守り抜く最大の力となるのです。",
     "各事件の深層プロファイリングに最後までお付き合いいただき、心より感謝申し上げます。",
     "皆様の温かいご支援と共感こそが、私たちが正義と真実を探求し続けるための最大の原動力です。",
     "それでは、また次なる心理解読の旅路でお会いしましょう。"
   ]
  )
]

# Cue mappings across the 3 editions
CUES = {
  "1.01": {
    "kind": "BGM",
    "VN": "Tiếng Dark Ambient âm u cất lên chậm rãi giữa không gian ngột ngạt, hòa cùng tiếng nhịp tim đập chậm và tiếng tích tắc đồng hồ kim loại lạnh lẽo, tạo cảm giác bất an sâu sắc.",
    "EN": "Low, oppressive Dark Ambient tones resonate slowly amid a suffocating space, accompanied by slow heartbeats and the cold ticking of a metallic clock.",
    "JA": "陰鬱なダークアンビエントが重苦しい空間にゆっくりと響き渡り、鈍い鼓動と冷たい金属時計の秒針の音が深い不安感を醸成する。"
  },
  "1.03": {
    "kind": "SFX",
    "VN": "Tiếng còi xe cảnh sát từ xa, tiếng máy bộ đàm rè nhẹ, tiếng lật giấy tờ hồ sơ vội vã.",
    "EN": "Distant police sirens wailing, faint radio static crackle, rapid flipping of investigative case files.",
    "JA": "遠くで響くパトカーのサイレン、微かな無線機のノイズ、慌ただしくめくられる捜査書類の紙音。"
  },
  "1.05": {
    "kind": "SFX",
    "VN": "Tiếng còi xe cứu thương vang vọng xa xăm, tiếng máy in hóa đơn ngân hàng kêu lạch cạch.",
    "EN": "Echoing ambulance siren from afar, rhythmic mechanical clatter of a bank receipt printer.",
    "JA": "遠くでこだまする救急車のサイレン、リズミカルに印字される銀行の伝票印刷機の機械音。"
  },
  "1.08": {
    "kind": "SFX",
    "VN": "Tiếng gõ bàn phím máy tính đồn cảnh sát, tiếng còi xe tuần tra xa xăm.",
    "EN": "Clicking keyboards inside a busy police precinct, faint patrol car sirens echoing in the distance.",
    "JA": "警察署内のキーボード打鍵音、遠くを通り過ぎるパトロールカーのサイレン。"
  },
  "1.12": {
    "kind": "BGM",
    "VN": "Một nốt cello trầm đục ngân dài rồi chìm vào khoảng không im lặng đến nghẹt thở.",
    "EN": "A deep, hollow cello note lingers mournfully, gradually dissolving into suffocating silence.",
    "JA": "重く濁ったチェロの単音が長く響き渡り、やがて息詰まるような沈黙の深淵へと消え入る。"
  },
  "2.01": {
    "kind": "BGM",
    "VN": "Âm thanh Dark Ambient lạnh lẽo, tiếng kim đồng hồ tích tắc chậm rãi như đếm từng giây ngột ngạt giữa căn phòng điều tra cô đặc bóng tối.",
    "EN": "Chilling Dark Ambient atmosphere with rhythmic clock ticks, counting agonizing seconds in a shadow-drenched interrogation room.",
    "JA": "冷徹なダークアンビエントの響き。濃密な影に包まれた取調室で、息詰まる秒刻みを刻む時計の針の音。"
  },
  "2.03": {
    "kind": "SFX",
    "VN": "Tiếng xóc bài cờ bạc dồn dập, tiếng xèng kim loại rơi loảng xoảng trong sòng bài casino.",
    "EN": "Rhythmic shuffling of casino cards, metallic cascade of slot machine tokens clattering.",
    "JA": "カジノのカードをリズミカルにシャッフルする音、スロットマシンの金属メダルがジャラジャラと擦れ合う音。"
  },
  "2.12": {
    "kind": "NGHI",
    "sec": 1.5,
    "VN": "Tiếng drone u uất kéo dài rồi tan biến",
    "EN": "A somber drone stretches out and fades into nothingness",
    "JA": "陰鬱なドローン音が長く尾を引いて虚空へ消え去る"
  },
  "3.01": {
    "kind": "BGM",
    "VN": "Âm nhạc chuyển sang tiếng Dương cầm tối giản, chậm rãi, mang màu sắc triết học và đầy tính tự vấn về giới hạn tâm lý con người.",
    "EN": "Score transitions to minimalist, contemplative piano notes exploring the moral boundaries of human psychology.",
    "JA": "音楽はミニマルで哲学的なピアノ独奏へと移行し、人間の心理的限界を静かに問いかける。"
  },
  "3.03": {
    "kind": "SFX",
    "VN": "Tiếng bước chân rụt rè trong căn nhà gỗ, tiếng thở dài nặng trĩu, tiếng rót nước vào cốc thủy tinh.",
    "EN": "Hesitant footsteps across worn floorboards, a heavy sigh, water poured softly into a glass.",
    "JA": "擦り切れた床板を軋ませるためらいがちな足音、重い吐息、グラスに水が静かに注がれる音。"
  },
  "3.11": {
    "kind": "BGM",
    "VN": "Một nốt piano trầm buồn ngân vang rồi từ từ hòa quyện vào tiếng cello u uất.",
    "EN": "A melancholic piano chord rings out, slowly dissolving into a sorrowful cello line.",
    "JA": "憂いを帯びたピアノの一和音が響き、哀愁に満ちたチェロの旋律へと静かに溶け込んでいく。"
  },
  "4.01": {
    "kind": "BGM",
    "VN": "Âm thanh vĩ cầm dồn dập, giằng xé, tái hiện không khí nghẹt thở của chiến dịch nghiệp vụ bí mật và sự sụp đổ của một đế chế tội ác.",
    "EN": "Frantic, agonizing violin strings capturing the breathless tension of an undercover operation and impending collapse.",
    "JA": "切迫したヴァイオリンの旋律が激しく鳴り響き、極秘おとり捜査の息詰まる緊張感と犯罪帝国の瓦解を描き出す。"
  },
  "4.06": {
    "kind": "SFX",
    "VN": "Tiếng đóng sầm cửa xe cảnh sát, tiếng còng số tám khóa lách cách đanh thép.",
    "EN": "Police cruiser door slamming shut, sharp metallic click of handcuffs snapping tight.",
    "JA": "警察車両のドアが重く閉まる音、手錠が硬質な金属音を立てて冷酷にロックされる音。"
  },
  "4.11": {
    "kind": "BGM",
    "VN": "Một nốt nhạc u uất lắng xuống rồi tan biến vào tiếng thở dài nặng nhọc.",
    "EN": "A somber chord settles low, trailing off into a heavy, resonant sigh.",
    "JA": "沈鬱な和音が静かに沈み込み、重く深い息の音とともに虚空へと消え入る。"
  },
  "5.01": {
    "kind": "BGM",
    "VN": "Nhạc nền chuyển sang giai điệu Piano ấm áp, sâu lắng, mang âm hưởng triết lý nhân văn và thức tỉnh lương tri sâu sắc.",
    "EN": "Music shifts to warm, profound piano harmonies embodying humanitarian reflection and moral awakening.",
    "JA": "音楽は温もりと深みを帯びたピアノの調べへと変わり、人道的な内省と崇高な良心の覚醒を奏でる。"
  },
  "5.06": {
    "kind": "BGM",
    "VN": "Nhạc nền ngân vang ấm áp, trang trọng rồi từ từ nhỏ dần và kết thúc trọn vẹn trong sự thanh thản.",
    "EN": "Score swells warmly with dignified reverence, gradually fading into gentle, lasting peace.",
    "JA": "温かく荘厳なピアノの響きが穏やかに満ちわたり、清らかな静寂の中へと美しく消え入る。"
  }
}

def format_script(lang):
    lines = []
    if lang == "VN":
        lines.append("# KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM")
        lines.append("**Chủ đề:** Hệ sinh thái 10 chỉ dấu tâm lý & Sự tha hóa quyền lực hành pháp, Coi người thân là công cụ tài chính, Diễn xuất vô cảm sau tội ác – Hồ sơ Nomia Rosemary Ndlovu và Bản hợp đồng bảo hiểm đẫm máu.")
        lines.append("**Phiên bản:** Chuẩn A2c/K10 — Hệ sinh thái 10 chỉ dấu tâm lý học tội phạm & Bổ sung phân tích biến chuyển tâm lý đa chiều ngày 21/11/2026.\n")
        lines.append("---\n")
        lines.append("## THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN (PRODUCTION BRIEF)\n")
        lines.append("| Hạng mục | Thiết lập chuẩn cho tập Audio (Host-Driven Documentary) |")
        lines.append("| :--- | :--- |")
        lines.append("| **Tên tập (Episode Title)** | Tập 46: Hồ Sơ Rosemary Ndlovu — NỮ CẢNH SÁT LÒNG THAM & BẢN HỢP ĐỒNG BẢO HIỂM ĐẪM MÁU |")
        lines.append("| **Định dạng (Format)** | Podcast Tài liệu Điều tra (Narrator-led Documentary) – **Host** nắm giữ trục xương sống kể chuyện, kết nối dữ liệu lịch sử, điều phối nhịp cảm xúc và mời các góc nhìn chuyên môn (Điều tra viên, Chuyên gia tâm lý, Người bình thường) vào đúng điểm nút kịch tính theo Hệ sinh thái 10 chỉ dấu tâm lý. |")
        lines.append("| **Tổng thời lượng dự kiến** | 28 – 32 phút (5 hồi nội dung + các khoảng lặng chuyển cảnh âm thanh) |")
        lines.append("| **Nhạc nền (BGM) gợi ý** | Dark Ambient âm u, tiếng nhịp tim đập chậm, Solo Cello u uất giằng xé, Minimalist Piano lạnh lẽo hòa cùng tiếng Sub-bass rùng rợn, và Warm Piano ấm áp trang nghiêm đúc kết. Âm lượng: -26dB dưới giọng đọc, nâng lên -14dB ở các điểm chuyển cảnh. |")
        lines.append("| **Cơ chế phân bổ giọng đọc** | - **Host (~48% thời lượng):** Giọng nam trầm ấm, sâu lắng, dẫn dắt câu chuyện với góc nhìn nhân văn, dư chấn xã hội, hiệu ứng hào quang và bài học sinh tồn.<br>- **Điều tra viên (~24%):** Giọng nam đanh thép, sắc lạnh, chuẩn xác, đại diện cho hồ sơ nghiệp vụ, chứng cứ hiện trường, chữ ký Signature vs MO và chiến thuật pháp lý của Thám tử Keshi Benneth Mabunda.<br>- **Chuyên gia tâm lý (~22%):** Giọng điềm đạm, mang tính học thuật sâu sắc, bóc tách hiện tượng tha hóa quyền lực, cơ chế phân ngăn tâm trí, sự vật hóa người thân và giải mã cơ chế hối hận của đồng phạm đánh thuê.<br>- **Người bình thường (~6%):** N1 (Đồng nghiệp tại Đồn Tembisa South - Hồi 1, 5 câu) giọng nữ trẻ hoang mang, bàng hoàng; N2 (Njabulo Kunene / Sát thủ hối cải - Hồi 4, 8 câu) giọng nam run rẩy, giằng xé tội lỗi tột cùng. |")
        lines.append("| **Quy tắc trích dẫn** | Mọi trích dẫn nguyên văn trong hình phải đúng 100% so với nguồn lưu trữ. Quy ước ký hiệu: ngoặc kép “ ” = trích dẫn nguyên văn. |")
        lines.append("| **Nguồn đối chiếu chính** | Hồ sơ xét xử tại Tòa Thượng thẩm Nam Phi chi nhánh Palm Ridge (2021) do Thẩm phán Ramarumo Monama chủ tọa · Lời khai của Thám tử Cấp cao Keshi Benneth Mabunda thuộc Sở Cảnh sát Nam Phi (SAPS) · Lời khai của sát thủ Njabulo Vincent Kunene và Lakhiwe Mkhize · Loạt phim tài liệu điều tra Rosemary’s Hitlist (Showmax, Đạo diễn Valen'tino Mathibela) · Các công trình nghiên cứu về Tâm lý học Pháp y của Hiệp hội Tâm lý học Nam Phi · Thuyết Ngắt kết nối đạo đức của Albert Bandura (1991) · Học thuyết Mặt nạ tỉnh táo của Hervey Cleckley (1941) · Lý thuyết The Gift of Fear của Gavin de Becker (1997). |\n")
        lines.append("---\n")
    elif lang == "EN":
        lines.append("# FORENSIC & CRIMINAL PSYCHOLOGY AUDIO SCRIPT")
        lines.append("**Topic:** 10 Psychological Markers & Executive Power Depravity, Dehumanization of Kin as Financial Commodities, Affective Callousness – Case File: Nomia Rosemary Ndlovu and the Blood-Stained Insurance Policies.")
        lines.append("**Version:** A2c/K10 Standard — Forensic Ecosystem of 10 Psychological Behavioral Markers & Multi-Subject Trajectory Analysis.\n")
        lines.append("---\n")
        lines.append("## PRODUCTION BRIEF & NARRATIVE STRUCTURE\n")
        lines.append("| Item | Standard Configuration (Host-Driven Documentary) |")
        lines.append("| :--- | :--- |")
        lines.append("| **Episode Title** | Episode 46: Case File Rosemary Ndlovu — THE GREED OF A POLICE SERGEANT & BLOOD-STAINED INSURANCE CONTRACTS |")
        lines.append("| **Format** | Narrator-led Investigative Documentary – The **Host** leads the central narrative spine, orchestrating emotion and seamlessly introducing professional perspectives (Investigator, Psychologist, Ordinary Person) at key dramatic junctures. |")
        lines.append("| **Estimated Runtime** | 28 – 32 minutes (5 acts + atmospheric transitions) |")
        lines.append("| **Recommended BGM** | Oppressive Dark Ambient, slow heartbeat pulses, sorrowful solo cello, chilling minimalist piano over ominous sub-bass drones, concluding with warm philosophical piano. Levels: -26dB under speech, rising to -14dB at scene transitions. |")
        lines.append("| **Cast & Voice Allocation** | - **Host (~48% duration):** Deep, resonant, warm male voice guiding historical context, societal aftermath, halo effects, and survival wisdom.<br>- **Investigator (~24%):** Authoritative, clinical, sharp male voice reflecting forensic files, physical evidence, signature versus MO, and tactical brilliance of Captain Keshi Benneth Mabunda.<br>- **Psychologist (~22%):** Poised, deeply academic female voice analyzing institutional corruption, cognitive compartmentalization, objectification of loved ones, and the moral turning point of hitmen.<br>- **Ordinary Person (~6%):** N1 (Tembisa South Police Colleague - Act 1, 5 sentences) bewildered young female voice; N2 (Njabulo Kunene / Penitent Hitman - Act 4, 8 sentences) trembling male voice grappling with agonizing moral torment. |")
        lines.append("| **Quotation Standards** | All verbatim quotes must match archival transcripts 100%. Quotes marked with curly marks “ ”. |")
        lines.append("| **Primary References** | Gauteng High Court (Palm Ridge) trial proceedings (2021) presided over by Judge Ramarumo Monama · Forensic testimonies of Senior Detective Captain Keshi Benneth Mabunda (SAPS) · Testimonies of hitmen Njabulo Vincent Kunene and Lakhiwe Mkhize · Showmax docuseries Rosemary's Hitlist (IdeaCandy, Dir. Valen'tino Mathibela) · Clinical forensic papers of the Psychological Society of South Africa · Moral Disengagement Theory (Albert Bandura, 1991) · The Mask of Sanity (Hervey Cleckley, 1941) · The Gift of Fear (Gavin de Becker, 1997). |\n")
        lines.append("---\n")
    elif lang == "JA":
        lines.append("# 犯罪心理学オーディオ／ポッドキャスト台本")
        lines.append("**テーマ:** 10の心理指標と公権力の腐敗、肉親の金融商品化、冷酷な演技性――事件記録: ノミア・ローズマリー・ンドロヴと血塗られた保険金契約。")
        lines.append("**バージョン:** A2c/K10標準規格――法心理行動分析10指標体系および多主体心理変容分析版。\n")
        lines.append("---\n")
        lines.append("## 制作仕様とナレーション構成（PRODUCTION BRIEF）\n")
        lines.append("| 項目 | 標準設定（ホスト主導型ドキュメンタリー） |")
        lines.append("| :--- | :--- |")
        lines.append("| **エピソード名** | 第46話：事件記録ローズマリー・ンドロヴ――強欲の女性警官と血塗られた保険金契約 |")
        lines.append("| **形式** | 捜査ドキュメンタリーポッドキャスト――**ホスト**が物語の中心軸を担い、感情の起伏を制御しながら、節目ごとに専門家（捜査官、心理学者、一般人）の見解を招き入れます。 |")
        lines.append("| **推定所要時間** | 28～32分（本編5幕＋場面転換音響） |")
        lines.append("| **推奨BGM** | 重厚なダークアンビエント、鈍い鼓動音、哀切なチェロ独奏、サブベースドローンを伴う冷徹なミニマルピアノ、そして結びの温かな人道的ピアノ。音量設定：ナレーション下 -26dB、場面転換時 -14dB。 |")
        lines.append("| **キャスト構成** | - **ホスト（全体の約48%）：** 深みと温かみのある男性の声。人道的な視点、社会的余波、ハロー効果、生存への教訓を通じて物語を導きます。<br>- **捜査官（約24%）：** 冷徹で鋭敏、正確無比な男性の声。ケシ・ベネット・マブンダ警部の実地捜査記録、物的証拠、シグネチャー対MO、法廷戦略を代弁します。<br>- **心理学者（約22%）：** 穏やかで深い学術性を備えた女性の声。権力の腐敗、認知的区画化、親族の対象化、実行犯の良心覚醒のメカニズムを解剖します。<br>- **一般人（約6%）：** N1（テンビサ警察署の同僚 - 第1幕、5文）衝撃と困惑に震える若い女性の声；N2（ニャブロ・クネネ／翻意した殺し屋 - 第4幕、8文）罪悪感に苛まれ葛藤する男性の声。 |")
        lines.append("| **引用規定** | 原典記録の正確性100%。引用符は「 」を使用。 |")
        lines.append("| **主要参考文献** | 南アフリカ高等裁判所パーム・リッジ支部公判記録（2021年、ラマルモ・モナマ裁判長） · 南アフリカ警察（SAPS）ケシ・ベネット・マブンダ警部の法廷証言 · 殺し屋ニャブロ・ヴィンセント・クネネおよびラキウェ・ムキゼの証言 · ドキュメンタリー『Rosemary's Hitlist』（Showmax、ヴァレンティノ・マティベラ監督） · 南アフリカ心理学会の法心理学論文集 · アルバート・バンデューラの道徳的脱関与理論（1991） · ハーヴェイ・チェックリーの正気の仮面理論（1941） · ギャヴィン・ド・ベッカーの恐怖の贈り物理論（1997）。 |\n")
        lines.append("---\n")

    act_titles = {
        "VN": [
            "## HỒI 1: KHỞI NGUỒN CƠN ÁC MỘNG VÀ TIẾNG CHUÔNG BÁO ĐỘNG",
            "## HỒI 2: VỎ BỌC NGUỴ TRANG VÀ DẤU VẾT HÀNH VI NGẦM",
            "## HỒI 3: CUỘC ĐẤU TRÍ TRONG PHÒNG THẨM VẤN VÀ CƠ CHẾ HỐI HẬN CỦA ĐỒNG PHẠM",
            "## HỒI 4: KHOA HỌC HÌNH SỰ LẬT MỞ BÍ ẨN VÀ ÁNH SÁNG CÔNG LÝ",
            "## HỒI 5: BẢN ÁN CUỐI CÙNG VÀ BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN"
        ],
        "EN": [
            "## ACT 1: GENESIS OF THE NIGHTMARE & THE UNHEEDED ALARMS",
            "## ACT 2: THE VELVET CAMOUFLAGE & SUBTERRANEAN BEHAVIORAL TRAILS",
            "## ACT 3: THE CHESSBOARD OF CONSCIENCE & THE PSYCHOLOGY OF MERCENARY REMORSE",
            "## ACT 4: FORENSIC SCIENCE DISSECTS THE LABYRINTH & TRUTH PREVAILS",
            "## ACT 5: THE FINAL VERDICT & SURVIVAL RED FLAGS"
        ],
        "JA": [
            "## 第1幕：悪夢の胎動と見過ごされた警鐘",
            "## 第2幕：完璧なベルベットの偽装と水面下の行動痕跡",
            "## 第3幕：良心の盤面と雇われ殺し屋の悔悟メカニズム",
            "## 第4幕：法科学が暴く迷宮と白日の下の真実",
            "## 第5幕：歴史的断罪と生存へのレッドフラッグ教訓"
        ]
    }

    role_headers = {
        "VN": {
            "HOST": "HOST",
            "ĐIỀU TRA VIÊN": "ĐIỀU TRA VIÊN",
            "CHUYÊN GIA TÂM LÝ": "CHUYÊN GIA TÂM LÝ",
            "NGƯỜI BÌNH THƯỜNG": "NGƯỜI BÌNH THƯỜNG"
        },
        "EN": {
            "HOST": "HOST",
            "ĐIỀU TRA VIÊN": "INVESTIGATOR",
            "CHUYÊN GIA TÂM LÝ": "PSYCHOLOGIST",
            "NGƯỜI BÌNH THƯỜNG": "ORDINARY PERSON"
        },
        "JA": {
            "HOST": "ホスト",
            "ĐIỀU TRA VIÊN": "捜査官",
            "CHUYÊN GIA TÂM LÝ": "心理学者",
            "NGƯỜI BÌNH THƯỜNG": "一般人"
        }
    }

    cur_act = 0
    loi_idx = 0

    # Total 52 elements matching Tap 10 layout:
    # 1.01(BGM), 1.02(LOI H), 1.03(SFX), 1.04(LOI H), 1.05(SFX), 1.06(LOI H), 1.07(LOI N), 1.08(SFX), 1.09(LOI H), 1.10(LOI D), 1.11(LOI H), 1.12(BGM)
    # 2.01(BGM), 2.02(LOI H), 2.03(SFX), 2.04(LOI D), 2.05(LOI H), 2.06(LOI C), 2.07(LOI H), 2.08(LOI D), 2.09(LOI H), 2.10(LOI C), 2.11(LOI H), 2.12(NGHI)
    # 3.01(BGM), 3.02(LOI H), 3.03(SFX), 3.04(LOI H), 3.05(LOI D), 3.06(LOI H), 3.07(LOI C), 3.08(LOI H), 3.09(LOI C), 3.10(LOI H), 3.11(BGM)
    # 4.01(BGM), 4.02(LOI H), 4.03(LOI D), 4.04(LOI H), 4.05(LOI N), 4.06(SFX), 4.07(LOI H), 4.08(LOI D), 4.09(LOI C), 4.10(LOI H), 4.11(BGM)
    # 5.01(BGM), 5.02(LOI H), 5.03(LOI C), 5.04(LOI D), 5.05(LOI H), 5.06(BGM)

    element_plan = [
        # Act 1
        ("cue", "1.01"), ("loi", 0), ("cue", "1.03"), ("loi", 1), ("cue", "1.05"), ("loi", 2),
        ("loi", 3), ("cue", "1.08"), ("loi", 4), ("loi", 5), ("loi", 6), ("cue", "1.12"),
        # Act 2
        ("cue", "2.01"), ("loi", 7), ("cue", "2.03"), ("loi", 8), ("loi", 9), ("loi", 10),
        ("loi", 11), ("loi", 12), ("loi", 13), ("loi", 14), ("loi", 15), ("cue", "2.12"),
        # Act 3
        ("cue", "3.01"), ("loi", 16), ("cue", "3.03"), ("loi", 17), ("loi", 18), ("loi", 19),
        ("loi", 20), ("loi", 21), ("loi", 22), ("loi", 23), ("cue", "3.11"),
        # Act 4
        ("cue", "4.01"), ("loi", 24), ("loi", 25), ("loi", 26), ("loi", 27), ("cue", "4.06"),
        ("loi", 28), ("loi", 29), ("loi", 30), ("loi", 31), ("cue", "4.11"),
        # Act 5
        ("cue", "5.01"), ("loi", 32), ("loi", 33), ("loi", 34), ("loi", 35), ("cue", "5.06")
    ]

    for item_type, val in element_plan:
        if item_type == "cue":
            cid = val
            act_num = int(cid.split('.')[0])
            if act_num > cur_act:
                cur_act = act_num
                lines.append("\n---\n")
                lines.append(act_titles[lang][cur_act - 1] + "\n")
            
            cue_info = CUES[cid]
            ckind = cue_info["kind"]
            cdesc = cue_info[lang]
            if ckind in ["BGM", "SFX"]:
                lines.append(f"**[{ckind}]:** {cdesc}\n")
            elif ckind == "NGHI":
                sec = cue_info["sec"]
                if lang == "VN":
                    lines.append(f"**[Nghỉ {sec} giây – {cdesc}]**\n")
                elif lang == "EN":
                    lines.append(f"**[Pause {sec} seconds – {cdesc}]**\n")
                elif lang == "JA":
                    lines.append(f"**[休止 {sec}秒 – {cdesc}]**\n")
        elif item_type == "loi":
            data = ELEMENTS_DATA[val]
            cid, act_num, role_vn, direction_vn, sents_vn, sents_en, sents_ja = data
            if act_num > cur_act:
                cur_act = act_num
                lines.append("\n---\n")
                lines.append(act_titles[lang][cur_act - 1] + "\n")

            role_tag = role_headers[lang][role_vn]
            
            # Form direction label
            if lang == "VN":
                direction = direction_vn
                sents = sents_vn
            elif lang == "EN":
                # Translate direction
                dir_map = {
                    "chậm rãi, giọng trầm ấm gợi mở không gian lịch sử": "deliberate, warm and resonant tone evoking historical gravity",
                    "chuyển giọng u tối, báo hiệu tai ương": "shifting to dark solemnity, signaling impending tragedy",
                    "tiếp tục mạch tự sự nghẹt thở": "continuing with breathless narrative momentum",
                    "N1: Đồng nghiệp tại Đồn Tembisa South, giọng nữ trẻ hoang mang, bàng hoàng": "N1: Tembisa South Police Colleague, bewildered young female voice",
                    "trầm giọng": "solemn tone",
                    "giọng nam sắc bén, tái hiện không gian nghiệp vụ": "incisive male voice, reconstructing investigative reality",
                    "khép lại Hồi 1": "concluding Act 1",
                    "giọng hồi hộp dẫn dắt": "suspenseful, driving narration",
                    "mô tả dấu vết tài chính và đời sống ngầm": "detailing financial trails and underworld life",
                    "phác họa chân dung kẻ thủ ác": "sketching the killer's psychological anatomy",
                    "phân tích cơ chế chia ngăn tâm trí và sự vật hóa con người": "forensic analysis of compartmentalization and radical dehumanization",
                    "tiếp tục mạch tự sự": "maintaining narrative momentum",
                    "giải thích diễn biến tội ác tiếp theo": "reconstructing the escalating criminal conspiracy",
                    "nhấn mạnh sự tột cùng của tội ác": "underscoring the zenith of depravity",
                    "đúc kết sự leo thang của ảo tưởng ái kỷ": "synthesizing the escalation of narcissistic omnipotence",
                    "thắt lại Hồi 2": "concluding Act 2",
                    "đặt vấn đề gây chấn động về sự chuyển hóa tâm lý": "raising profound questions on moral transformation",
                    "tái hiện cuộc hội ngộ nghẹt thở": "reconstructing the breathless encounter",
                    "nhấn mạnh chi tiết lời khai của sát thủ": "highlighting the critical testimony of the hitman",
                    "giọng đầy trăn trở": "reflective and searching tone",
                    "giải phẫu cơ chế hối hận và sự sụp đổ của lòng tham": "anatomizing the psychology of remorse and the collapse of greed",
                    "bóc tách diễn biến tố giác": "deconstructing the whistleblowing turning point",
                    "bóc tách sự đối lập nhân cách giữa kẻ chủ mưu và đồng phạm": "contrasting the sociopathy of the mastermind with the hitmen's moral awakening",
                    "khép lại Hồi 3": "concluding Act 3",
                    "mở đầu Hồi 4": "opening Act 4",
                    "thuật lại chiến dịch nghiệp vụ và bằng chứng video": "recounting the tactical sting and definitive video evidence",
                    "tiết lộ sự kiên trì của điều tra viên": "revealing the relentless tenacity of the investigator",
                    "N2: Lời tự vấn của Njabulo Kunene, giọng nam run rẩy, đầy giằng xé tội lỗi": "N2: Reflections of Njabulo Kunene, trembling male voice wracked with guilt",
                    "tiếp tục diễn biến đối đầu trong phòng thẩm vấn": "chronicling the interrogation room confrontation",
                    "thuật lại phản ứng ngoan cố của đối tượng": "reconstructing the suspect's defiant retaliation",
                    "phân tích tâm lý của kẻ thủ ác khi bản ngã sụp đổ": "forensic profiling of narcissistic collapse and pathological self-pity",
                    "khép lại Hồi 4": "concluding Act 4",
                    "giọng suy ngẫm, triết lý và đầy xúc động": "contemplative, deeply moving philosophical tone",
                    "đúc kết sự thức tỉnh và bài học hành vi": "synthesizing behavioral awakenings and forensic lessons",
                    "nhận định di sản tư pháp và bản án": "evaluating the landmark judicial verdict and legal legacy",
                    "chuyển sang phần đúc kết và bài học nhận diện": "transitioning to survival red flags and final reflections"
                }
                direction = dir_map.get(direction_vn, direction_vn)
                sents = sents_en
            elif lang == "JA":
                dir_map_ja = {
                    "chậm rãi, giọng trầm ấm gợi mở không gian lịch sử": "深みと温かみのある落ち着いた声で、歴史的重みを呼び覚ます",
                    "chuyển giọng u tối, báo hiệu tai ương": "暗雲立ち込める声調へと転じ、忍び寄る惨劇を予告する",
                    "tiếp tục mạch tự sự nghẹt thở": "息詰まるような緊張感を保ちながら語りを進める",
                    "N1: Đồng nghiệp tại Đồn Tembisa South, giọng nữ trẻ hoang mang, bàng hoàng": "N1：テンビサ警察署の同僚、衝撃と困惑に震える若い女性の声",
                    "trầm giọng": "重々しく沈痛な声で",
                    "giọng nam sắc bén, tái hiện không gian nghiệp vụ": "鋭敏で明晰な男性の声、捜査現場の現実を再現する",
                    "khép lại Hồi 1": "第1幕を締めくくる",
                    "giọng hồi hộp dẫn dắt": "緊迫感を帯びた声で核心へと引き込む",
                    "mô tả dấu vết tài chính và đời sống ngầm": "金融捜査の軌跡と裏社会の生活実態を詳述する",
                    "phác họa chân dung kẻ thủ ác": "加害者の精神構造を浮き彫りにする",
                    "phân tích cơ chế chia ngăn tâm trí và sự vật hóa con người": "認知的区画化と極端な対象化の心理メカニズムを解剖する",
                    "tiếp tục mạch tự sự": "物語の緊迫感を維持しながら語り続ける",
                    "giải thích diễn biến tội ác tiếp theo": "狂気を増していく犯行計画の展開を解説する",
                    "nhấn mạnh sự tột cùng của tội ác": "極限に達した背徳の深淵を強調する",
                    "đúc kết sự leo thang của ảo tưởng ái kỷ": "全能感と自己愛の肥大化を総括する",
                    "thắt lại Hồi 2": "第2幕を締めくくる",
                    "đặt vấn đề gây chấn động về sự chuyển hóa tâm lý": "心理的転換点に関する根源的な問いを投げかける",
                    "tái hiện cuộc hội ngộ nghẹt thở": "息を呑む緊迫の遭遇場面を再現する",
                    "nhấn mạnh chi tiết lời khai của sát thủ": "殺し屋の生々しい証言の核心を強調する",
                    "giọng đầy trăn trở": "思索と葛藤に満ちた重厚な声で",
                    "giải phẫu cơ chế hối hận và sự sụp đổ của lòng tham": "悔悟の心理メカニズムと強欲の自壊を解剖する",
                    "bóc tách diễn biến tố giác": "内部告発への劇的な転換プロセスを解き明かす",
                    "bóc tách sự đối lập nhân cách giữa kẻ chủ mưu và đồng phạm": "首謀者の冷酷さと実行犯の良心覚醒の対比を浮き彫りにする",
                    "khép lại Hồi 3": "第3幕を締めくくる",
                    "mở đầu Hồi 4": "第4幕の幕開け",
                    "thuật lại chiến dịch nghiệp vụ và bằng chứng video": "電撃的なおとり捜査と決定的証拠映像を克明に再現する",
                    "tiết lộ sự kiên trì của điều tra viên": "捜査官の不屈の執念と捜査展開を明かす",
                    "N2: Lời tự vấn của Njabulo Kunene, giọng nam run rẩy, đầy giằng xé tội lỗi": "N2：ニャブロ・クネネの内省、罪悪感に苛まれ震える男性の声",
                    "tiếp tục diễn biến đối đầu trong phòng thẩm vấn": "取調室における緊迫の対決劇を語る",
                    "thuật lại phản ứng ngoan cố của đối tượng": "追い詰められた容疑者の悪あがきと反抗を詳述する",
                    "phân tích tâm lý của kẻ thủ ác khi bản ngã sụp đổ": "自己愛の崩壊と病理的自己憐憫の精神病理を解剖する",
                    "khép lại Hồi 4": "第4幕を締めくくる",
                    "giọng suy ngẫm, triết lý và đầy xúc động": "思索的で深い感動を湛えた哲学的な声で",
                    "đúc kết sự thức tỉnh và bài học hành vi": "行動科学的知見と道徳的覚醒の意義を総括する",
                    "nhận định di sản tư pháp và bản án": "歴史的判決の重みと法制度の遺産を評価する",
                    "chuyển sang phần đúc kết và bài học nhận diện": "生存へのレッドフラッグ教訓と結びの言葉へ移行する"
                }
                direction = dir_map_ja.get(direction_vn, direction_vn)
                sents = sents_ja

            lines.append(f"**{role_tag}** *({direction})*:\n")
            for s in sents:
                lines.append(s)
            lines.append("")

    return "\n".join(lines)

# Write VN script
vn_text = format_script("VN")
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap46/kichban_tap46_19112026.md", "w", encoding="utf-8") as f:
    f.write(vn_text)
print("Saved VN script")

# Write EN script
en_text = format_script("EN")
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap46_EN/kichban_tap46_EN.md", "w", encoding="utf-8") as f:
    f.write(en_text)
print("Saved EN script")

# Write JA script
ja_text = format_script("JA")
with open("01_KICH_BAN/Ho_So_Toi_Pham/Tap46_JA/kichban_tap46_JA.md", "w", encoding="utf-8") as f:
    f.write(ja_text)
print("Saved JA script")

