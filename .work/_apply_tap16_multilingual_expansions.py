# -*- coding: utf-8 -*-
"""Apply in-depth psychological expansions to Tap 16 across VN, EN, JA, and KO with exact target matching."""
import io, sys, re
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

insertions = {
    'VN': [
        (
            "Khi những sự bất thường bắt đầu lộ diện, thành kiến bình thường hóa đã khiến xã hội lờ đi những tín hiệu báo động đỏ sớm nhất.",
            "\nTại những cộng đồng thượng lưu danh giá như thị trấn Westfield, người ta thường tự ru ngủ mình bằng ảo tưởng rằng danh vọng và sự giàu sang có thể miễn trừ cho con người trước cái ác.\n"
            "Vẻ ngoài đạo mạo của những bộ âu phục chỉnh tề và nếp sống sùng đạo đã dệt nên một tấm màn nhung êm ái, nhưng vô tình làm tê liệt hoàn toàn phản xạ cảnh giác tự nhiên của xã hội.\n"
            "Suốt gần một tháng trời căn biệt thự rực sáng đèn giữa đêm đông và báo chí chất đống trước hiên, hàng xóm xung quanh chỉ nhìn rồi bước qua trong sự im lặng giữ kẽ.\n"
            "Chính sự thờ ơ tập thể đội lốt tôn trọng quyền riêng tư ấy đã tạo nên một khoảng chân không an toàn cho tội ác đóng băng hiện trường."
        ),
        (
            "Suốt nhiều năm tháng về sau, câu nói kêu cứu của cô học trò nhỏ vẫn ám ảnh tâm trí tôi như một nỗi day dứt không bao giờ nguôi ngoai.",
            "\nMỗi khi nhớ lại ánh mắt thảng thốt của Patricia trong căn phòng tập kịch chiều hôm ấy, tim tôi như bị bóp nghẹt bởi sự bất lực và nỗi ân hận khôn nguôi.\n"
            "Con bé đã cảm nhận được hơi thở lạnh lẽo của hiểm họa đang siết chặt quanh cổ mình, em đã dũng cảm cất lên tiếng kêu cứu với người lớn duy nhất mà em tin tưởng.\n"
            "Nhưng lúc ấy, tôi đã tự trấn an rằng đó chỉ là những áp lực tâm lý tuổi dậy thì trong một gia đình quá đỗi khắt khe, rằng một người cha mẫu mực như ông List sẽ không bao giờ làm hại con cái.\n"
            "Sự ngây thơ và do dự của chính tôi đã tước đi cơ hội sống sót cuối cùng của một tâm hồn trẻ thơ vô tội."
        ),
        (
            "Đó là một bài toán hóc búa vượt quá giới hạn của các kỹ thuật truy nã truyền thống ở thời kỳ đó.",
            "\nĐể có thể tồn tại suốt mười tám năm ròng rã mà không bị những bóng ma quá khứ quật ngã, bộ não của John List đã vận hành một cơ chế phòng vệ cực hạn mang tên “Sự Chia ngăn Nhận thức”.\n"
            "Hắn đã thành công trong việc đóng băng và niêm phong toàn bộ ký ức về ngày 9 tháng 11 năm 1971 vào một chiếc két sắt tâm lý kiên cố, hoàn toàn cô lập khỏi cuộc sống đời thường.\n"
            "Dưới cái tên Robert Clark, hắn thản nhiên bước vào một cuộc hôn nhân mới, ăn ngon ngủ yên mỗi đêm và tiếp tục duy trì thói quen đi lễ nhà thờ mỗi chủ nhật như một quý ông mẫu mực.\n"
            "Hắn không hề gặp ác mộng, bởi vì trong thế giới quan méo mó của một kẻ mắc OCPD, bi kịch Breeze Knoll không phải là tội ác tước đoạt mạng sống, mà chỉ là một thủ tục phá sản đau đớn mà hắn đã hoàn tất và đóng sổ sách lại phía sau lưng."
        ),
        (
            "Hắn phải sống sót để tiếp tục làm việc, xưng tội trước lúc lâm chung, với ảo tưởng rằng sau này vẫn sẽ được đoàn tụ cùng những người thân yêu trên Thiên quốc.",
            "\nMột câu hỏi lớn luôn khiến công chúng đau đáu: Tại sao một người sùng đạo như John List lại không bao giờ biểu lộ một tia ân hận thực sự sau khi tước đoạt sinh mạng của cả gia đình?\n"
            "Câu trả lời nằm ở sự khiếm khuyết hoàn toàn về năng lực thấu cảm cảm xúc, kết hợp cùng kỹ thuật trung hòa đạo đức mang tên “Kêu gọi lòng trung thành cao hơn”.\n"
            "Bức thư dài năm trang gửi vị mục sư không phải là sự ăn năn, mà là một bản giao dịch tâm lý đầy toan tính: hắn tự thuyết phục mình rằng việc tiễn đưa người thân khi họ còn giữ được đức tin là hành động bác ái để bảo đảm linh hồn họ bước vào Thiên đàng.\n"
            "Đối với bản ngã ái kỷ bệnh lý, thừa nhận tội lỗi đồng nghĩa với việc chiếc mặt nạ hoàn hảo bị phá hủy hoàn toàn; do đó, tâm trí hắn lựa chọn bám víu vào sự tự huyễn hoặc tôn giáo để vĩnh viễn trốn chạy trách nhiệm lương tâm."
        ),
        (
            "Cơ chế này cho phép một con người có thể sống cuộc đời của một công dân lương thiện ngay trên đống tro tàn của quá khứ.",
            "\nKhi đứng trước vành móng ngựa hai mươi năm sau đó, những giọt nước mắt hiếm hoi mà John List rơi xuống hoàn toàn không dành cho năm người thân đã khuất dưới mái vòm Breeze Knoll.\n"
            "Đó là hiện tượng “Sự sụp đổ cái tôi ái kỷ” và “Tự thương hại bệnh lý” kinh điển trong tội phạm học.\n"
            "Hắn chỉ khóc cho chính mình: khóc vì danh dự bị vùi dập, khóc vì sự tự do bị tước đoạt, và tiếc nuối cho cuộc đời giả tạo dưới cái tên Robert Clark vừa tan thành mây khói.\n"
            "Đến tận những ngày cuối đời sau song sắt, hắn vẫn trơ trẽn khẳng định mình là một người cha yêu thương con cái, phơi bày một linh hồn lạnh lẽo không bao giờ có thể cứu rỗi."
        ),
        (
            "Sự thật sau đó đã chứng minh rằng cái ác tinh vi nhất luôn biết cách khoác lên mình chiếc áo choàng của sự bình thường và tử tế.",
            "\nThú thật rằng suốt nhiều năm trước đó, tôi đã liên tục dập tắt những mối nghi ngờ le lói trong lòng mình vì sợ bị coi là kẻ hoang tưởng tọc mạch.\n"
            "Khi tình cờ đọc được bài báo cũ và nhận thấy vẻ ngoài của Bob Clark giống hệt kẻ đào tẩu John List, tôi đã nửa đùa nửa thật chia sẻ với Delores, nhưng rồi cả hai chúng tôi đều cười xòa bỏ qua vì không muốn phá vỡ cuộc sống bình yên của nhau.\n"
            "Thế nhưng đêm chủ nhật hôm ấy, khi bức tượng đất sét của Frank Bender xuất hiện trên màn hình truyền hình trước hai mươi hai triệu người, một luồng điện lạnh buốt chạy dọc sống lưng tôi.\n"
            "Tôi nhận ra rằng sự do dự lúc này không còn là sự lịch thiệp, mà là sự đồng lõa hèn nhát với tội ác đang lẩn trốn.\n"
            "Lương tâm và trách nhiệm công dân đã thôi thúc tôi nhấc máy gọi cho đường dây nóng, bởi vì một xã hội im lặng trước cái ác là một xã hội đang tự đầu hàng."
        ),
        (
            "Cặp kính gọng sừng cổ điển trên gương mặt kẻ đào tẩu chính là chiếc chìa khóa định mệnh mở toang cánh cửa dẫn hắn vào trại giam.",
            "\nHành động dũng cảm của người hàng xóm Wanda Flannery đã kéo sập bức màn dối trá, nhưng đồng thời giáng một đòn chí mạng vào tâm trí người vợ thứ hai là Delores Miller.\n"
            "Delores hoàn toàn vô tội về mặt pháp lý, nhưng lại phải gánh chịu một chấn thương tâm lý tàn khốc mang tên “Sự sụp đổ bản ngã do phản bội niềm tin”.\n"
            "Bà bàng hoàng nhận ra người đàn ông mà mình đầu ấp tay gối, cùng cầu nguyện và chia sẻ từng bữa ăn suốt nhiều năm qua lại chính là kẻ đã tước đoạt sinh mạng của cả mẹ ruột, vợ và ba người con.\n"
            "Cảm giác ghê tởm, tội lỗi vì đã vô tình trở thành lá chắn bình thường hóa cho kẻ ác đã đẩy bà vào một cuộc khủng hoảng tinh thần sâu sắc; đó là cái giá quá đắt của sự ngây thơ khi đối diện với chiếc mặt nạ hoàn hảo của tội phạm OCPD."
        ),
        (
            "Nó chứng minh rằng không một bức tường dối trá nào có thể tồn tại vĩnh viễn trước ánh sáng của sự thật và khoa học pháp y hiện đại.",
            "\nVụ án John List khép lại nhưng để lại lời cảnh tỉnh trường tồn cho công tác điều tra hình sự và an ninh gia đình hiện đại.\n"
            "Không một chiếc mặt nạ đạo mạo, không một địa vị xã hội danh giá nào có thể là bảo chứng tuyệt đối cho sự an toàn nếu thiếu vắng sự nhạy cảm và trách nhiệm can thiệp của những người xung quanh.\n"
            "Sự an bình thực sự của một cộng đồng không được xây nên từ những cánh cổng đóng kín hay sự giữ kẽ vô cảm, mà phải được gìn giữ bằng lòng dũng cảm bảo vệ những sinh mệnh dễ bị tổn thương nhất.\n"
            "Đó là di sản nhân văn đắt giá nhất được đánh đổi bằng nỗi đau và nước mắt của năm sinh mạng vô tội tại dinh thự Breeze Knoll."
        ),
        (
            "Tôn giáo và đạo đức không bao giờ là tấm bình phong để biện minh cho sự ích kỷ, sự hèn nhát và hành vi tước đoạt mạng sống của đồng loại.",
            "\nNhìn lại thảm kịch Breeze Knoll sau hơn nửa thế kỷ, vết thương dai dẳng nhất không chỉ thuộc về các phòng xử án, mà nằm trong tâm trí của những người từng có cơ hội ngăn chặn cái ác nhưng đã bỏ lỡ.\n"
            "Hiện tượng “Chấn thương Đạo đức của Nhân chứng” thể hiện rõ nét qua nỗi day dứt suốt đời của cô giáo Jean Phillips và những người từng tiếp xúc với gia đình List.\n"
            "Sự im lặng của xã hội thường không bắt nguồn từ sự tàn nhẫn, mà sinh ra từ nỗi e ngại bị phán xét, sự sợ hãi va chạm và thói quen xem nhẹ linh cảm bất an của những người yếu thế.\n"
            "Khi một đứa trẻ cất tiếng kêu cứu về sự ngột ngạt trong chính ngôi nhà của mình, đó không bao giờ là câu chuyện riêng tư cần giữ kín, mà là một mệnh lệnh khẩn cấp đòi hỏi cộng đồng phải dũng cảm phá vỡ sự im lặng để hành động."
        )
    ],
    'EN': [
        (
            "When early warning signs quietly surfaced, collective normalcy bias led society to discount the most critical red flags.",
            "\nIn prestigious, affluent communities like the town of Westfield, people often lull themselves into the illusion that social status and wealth grant immunity from human malice.\n"
            "The respectable facade of tailored suits and devout churchgoing wove a comfortable velvet curtain that inadvertently paralyzed society's natural instinct for vigilance.\n"
            "For nearly an entire month, while the mansion blazed with lights through winter nights and mail piled high upon the porch, neighbors simply watched and walked past in polite detachment.\n"
            "It was that collective indifference, masquerading as respect for family privacy, which provided the perfect vacuum for horror to freeze undisturbed in time."
        ),
        (
            "For decades afterward, that desperate cry from my young student haunted me like an agonizing grief that could never find peace.",
            "\nWhenever I recall the frantic terror in Patricia's eyes inside that rehearsal room that afternoon, my heart constricts with sheer helplessness and unending regret.\n"
            "That poor child had already sensed the icy grip of impending doom tightening around her throat; she had bravely cried out to the only adult she trusted.\n"
            "Yet at that moment, I rationalized her words away as teenage melodrama under the weight of an overly strict household, telling myself that an upstanding father like Mr. List could never harm his own children.\n"
            "My own naive hesitation stripped that innocent young soul of her very last chance at survival."
        ),
        (
            "It represented a complex forensic riddle extending far beyond the capabilities of conventional law enforcement techniques at the time.",
            "\nTo survive eighteen long years without being crushed by the ghosts of his past, John List's psyche relied on an extreme defense mechanism known as 'Cognitive Compartmentalization'.\n"
            "He succeeded in freezing and locking away every memory of November 9, 1971, inside a fortified psychological vault, completely insulated from daily consciousness.\n"
            "Under the alias Robert Clark, he effortlessly entered a new marriage, slept peacefully every night, and faithfully attended church every Sunday as an exemplary gentleman.\n"
            "He suffered no nightmares, because within the distorted worldview of a rigid OCPD mind, the tragedy at Breeze Knoll was not murder; it was merely a painful bankruptcy procedure that he had resolved and permanently closed on the ledger."
        ),
        (
            "He resolved to survive, work, and secure last-minute repentance on his deathbed, cherishing the grotesque fantasy of a celestial family reunion.",
            "\nA profound question has haunted the public for decades: Why did a devout man like John List never express a single shred of genuine remorse after obliterating his entire family?\n"
            "The answer lies in a complete deficit of affective empathy, paired with the neutralization technique known as 'Appeal to Higher Loyalties'.\n"
            "His five-page confession letter to his pastor was not an act of contrition, but a calculated theological transaction: he convinced himself that sending his loved ones to death while their faith remained intact was an act of mercy ensuring their passage to Heaven.\n"
            "For a pathological narcissist, acknowledging guilt would utterly shatter his idealized self-image; thus, his mind clung desperately to religious rationalization to evade moral accountability forever."
        ),
        (
            "This mechanism allowed him to live seamlessly as an upright, peaceful citizen right atop the incinerated ashes of his past.",
            "\nWhen standing in the prisoner's dock two decades later, the rare tears John List shed were never for the five souls who perished beneath the Tiffany stained glass of Breeze Knoll.\n"
            "They were textbook manifestations of 'Narcissistic Collapse' and 'Pathological Self-Pity'.\n"
            "He wept exclusively for himself: mourning his destroyed reputation, lamenting his lost freedom, and grieving the shattered facade of his comfortable life as Robert Clark.\n"
            "Even in his final days behind bars, he shamelessly insisted that he had been a loving father, exposing a frozen soul utterly incapable of redemption."
        ),
        (
            "What unfolded afterward proved that the most insidious evil frequently cloaks itself in the mundane garments of routine neighborliness.",
            "\nTo be completely honest, for years I repeatedly extinguished the quiet suspicions flickering in my heart, terrified of being dismissed as a paranoid busybody.\n"
            "When I stumbled across that old magazine article and noticed Bob Clark bore an uncanny resemblance to the fugitive John List, I mentioned it half-jokingly to Delores; but we simply laughed it off, reluctant to disturb our peaceful lives.\n"
            "Yet on that Sunday night, when Frank Bender's clay bust appeared on national television before twenty-two million viewers, an icy chill surged down my spine.\n"
            "I realized in an instant that hesitation was no longer polite discretion; it was cowardly complicity with a monster hiding in plain sight.\n"
            "My conscience and civic duty compelled me to dial that hotline, because a community that remains silent before wickedness is a community that surrenders its own humanity."
        ),
        (
            "Those vintage horn-rimmed eyeglasses perched upon his nose served as the fateful key unlocking the door to his prison cell.",
            "\nWanda Flannery's courageous act shattered the facade of deception, but simultaneously dealt a devastating blow to his second wife, Delores Miller.\n"
            "While legally blameless, Delores suffered a catastrophic psychological trauma known as 'Identity Shattering through Betrayal of Trust'.\n"
            "She was thrust into the horrifying realization that the mild-mannered man with whom she had shared a bed, prayed, and dined for years was the very predator who had eliminated his elderly mother, wife, and three children.\n"
            "The overwhelming horror and visceral guilt of having unknowingly served as a normalizing shield for a mass killer plunged her into profound psychological crisis; that is the heartbreaking cost of innocence before the flawless mask of an OCPD offender."
        ),
        (
            "It established that no labyrinth of deception can withstand the unblinking illumination of forensic truth and scientific methodology.",
            "\nThe John List dossier stands closed, yet it leaves an enduring warning for criminal investigation and contemporary domestic vigilance.\n"
            "No respectable facade, no elevated social pedigree can ever serve as a guarantee of safety without the sensitivity and proactive courage of those in the surrounding community.\n"
            "The true security of any neighborhood is never forged behind locked gates or polite indifference, but is vigilantly guarded through the collective courage to protect the most vulnerable among us.\n"
            "That remains the most profound humanitarian legacy, purchased with the pain and tears of five precious lives inside the Breeze Knoll mansion."
        ),
        (
            "Spiritual faith and moral codes must never be weaponized as shields to sanctify personal cowardice, egotism, and the destruction of human life.",
            "\nReflecting upon the Breeze Knoll tragedy over half a century later, the most enduring wounds reside not merely within courtroom archives, but inside the minds of those who held the opportunity to intervene yet hesitated.\n"
            "The phenomenon of 'Witness Moral Injury' is poignantly etched into the lifelong remorse of teacher Jean Phillips and others who crossed paths with the List family.\n"
            "Societal silence rarely stems from active malice; rather, it is bred from the fear of awkward confrontation and the tragic habit of dismissing the survival intuition of the vulnerable.\n"
            "When a young person cries out about suffocating dread inside their own home, it is never a private matter to be discreetly ignored, but an urgent moral mandate demanding that the community break its silence and act."
        )
    ],
    'JA': [
        (
            "不吉な異変が水面下に現れ始めた時にも、正常性バイアスが社会の目を眩ませ、最初期の危険な警戒信号を見過ごさせたのです。",
            "\nウェストフィールドのような格式高い高級住宅街では、社会的地位や富が人間の悪意を寄せ付けないという幻想に人々は浸りがちです。\n"
            "仕立ての良いスーツと敬虔な教会通いという立派な仮面は、平穏なベルベットのカーテンを織り上げ、社会が本来持つべき警戒心を麻痺させてしまいました。\n"
            "冬の夜に邸宅の明かりが一晩中灯り続け、ポーチに新聞が山積みにされていた一ヶ月間、隣人たちは礼儀正しい沈黙を守って通り過ぎるだけだったのです。\n"
            "家庭のプライバシー尊重という名のもとに隠されたこの集団的無関心こそが、悲劇を凍りつかせた完璧な空白地帯を生み出しました。"
        ),
        (
            "それから何十年が過ぎても、幼い教え子のあの悲痛な叫びは、消えることのない深い後悔とともに私の心を締めつけ続けています。",
            "\nあの日の放課後、演劇室で私の目を見つめたパトリシアの怯えた眼差しを思い出すたび、胸が無力感と消えない悔恨で締め付けられます。\n"
            "あの子は自分の首元に忍び寄る凍りつくような危険を察知し、信頼できる唯一の大人であった私に向かって必死に助けを求めていたのです。\n"
            "しかしその時、私は厳格すぎる家庭環境による思春期の過敏な不安に過ぎないと自分に言い聞かせ、リスト氏のような模範的な父親が子供を傷つけるはずがないと思い込んでしまいました。\n"
            "私自身の躊躇と無邪気な思い込みが、罪なき少女の生き残る最後の希望を奪ってしまったのです。"
        ),
        (
            "それは当時の伝統的な指名手配技術の限界をはるかに超越した、極めて難解な科学的難問だったのです。",
            "\n過去の亡霊に押しつぶされることなく十八年間を生き延びるため、ジョン・リストの精神は「認知的区画化」という極限の防衛機制を働かせていました。\n"
            "彼は千九百七十一年十一月九日の記憶を強固な心理的金庫の中に封印し、日々の日常意識から完全に切り離すことに成功したのです。\n"
            "ロバート・クラークという偽名のもと、彼は平然と再婚し、毎晩安らかに眠り、模範的な紳士として毎週日曜日に礼拝へ通い続けました。\n"
            "彼が悪夢にうなされることはありませんでした。OCPDの歪んだ世界観において、あの惨劇は殺人ではなく、清算を終えて帳簿を閉じた破産手続きに過ぎなかったからです。"
        ),
        (
            "彼は現世を生き延びて働き、臨終の床で神の許しを請うことで、将来天国で家族と再会できるという倒錯した幻想を抱いていたのです。",
            "\n多くの人々が抱く根源的な疑問があります。なぜジョン・リストのような敬虔な男が、家族全員の命を奪った後も真の悔悟を一切示さなかったのか。\n"
            "その答えは、情動的共感能力の完全な欠如と、「より高次な忠誠心への訴え」と呼ばれる道徳的中和技術にあります。\n"
            "牧師に宛てた五枚の手紙は懺悔ではなく、計算された神学的取引でした。家族の信仰が失われる前にその命を奪うことこそが、天国行きを保証する慈悲の業であると自分に思い込ませたのです。\n"
            "自己愛的な病理において、罪を認めることは自らの完璧な仮面を完全に破壊することを意味します。そのため彼の精神は宗教的自己正当化にしがみつき、道徳的責任から永遠に逃避したのです。"
        ),
        (
            "この機制によって、彼は自らが焼き尽くした過去の残骸の真上で、何食わぬ顔で善良な市民としての人生を歩み続けることができたのです。",
            "\n二十年後に法廷の被告席に立った際、ジョン・リストが流した稀な涙は、ブリーズ・ノールの天井の下で命を絶たれた五人の家族のためのものではありませんでした。\n"
            "それは犯罪心理学における典型的な「自己愛の崩壊」と「病理的自己憐憫」の現れに他なりませんでした。\n"
            "彼が泣いたのは自分自身のためだけでした。傷つけられたプライド、奪われた自由、そしてロバート・クラークとしての偽りの平穏が崩壊したことを嘆いていたのです。\n"
            "獄中で最期を迎えるその日まで、自分は家族を愛する良き父親だったと臆面もなく言い張り、決して救われることのない凍りついた魂を晒し続けました。"
        ),
        (
            "その後の真実は、最も狡猾な悪意こそが平凡さと親切という仮面を完璧に着こなすという事実を残酷に証明しました。",
            "\n正直に言えば、お節介で妄想癖のある人間だと思われるのを恐れ、何年もの間、胸に浮かぶ小さな疑念を自分自身で打ち消し続けていました。\n"
            "古い雑誌記事を偶然目にしてボブ・クラークが逃亡者ジョン・リストに酷似していると気づいた時も、デロリスに冗談交じりで話しただけで、互いの平穏を壊したくなくて笑い飛ばしてしまったのです。\n"
            "しかしあの夜、全国放送の画面にフランク・ベンダーの胸像が二千二百万人の視聴者の前に映し出された瞬間、背筋に氷のような戦慄が走りました。\n"
            "この期に及んで沈黙を守ることは礼儀正しさなどではなく、目の前に潜む悪への卑怯な加担だと悟ったのです。\n"
            "良心と市民としての責任感に背中を押され、私は受話器を取りました。悪に対して沈黙する社会は、自らの人間性を放棄した社会に他ならないからです。"
        ),
        (
            "逃亡犯の鼻梁に乗せられていたあのクラシックなセルフレーム眼鏡こそが、彼を刑務所の独房へと導く運命の鍵となったのでした。",
            "\n隣人ワンダ・フラナリーの勇気ある通報は偽りの帳を裂きましたが、同時に後妻であるデロリス・ミラーの精神に破壊的な打撃を与えました。\n"
            "デロリスは法的には無実でしたが、「信頼の裏切りによる自己崩壊」という過酷な心理的トラウマを背負わされることになります。\n"
            "長年同じベッドで眠り、祈りを捧げ、食卓を共にしてきた物静かな夫が、実の母、妻、そして三人の我が子を葬った殺人犯であったという悪夢のような現実に直面したのです。\n"
            "知らぬ間に凶悪犯の隠れ蓑として機能してしまっていたという激しい自己嫌悪と罪悪感は、彼女を深い精神的苦痛に突き落としました。OCPD犯罪者の完璧な仮面の前に無邪気さが支払わされた、あまりにも過酷な代償だったのです。"
        ),
        (
            "どれほど強固に築かれた欺瞞の壁であっても、真実の光と現代法科学の鋭利なメスから逃れ続けることは不可能であると示したのです。",
            "\nジョン・リスト事件の記録は閉じられましたが、現代の犯罪捜査と家庭の安全に対して永遠の警鐘を鳴らし続けています。\n"
            "周囲の人々の鋭敏な観察力と介入する勇気なくして、いかに立派な仮面や高い社会的地位であっても安全の絶対的な保証にはなり得ません。\n"
            "真の平穏は閉ざされた門や無関心な遠慮によって守られるのではなく、最も傷つきやすい命を連帯して守る勇気によってのみ維持されるのです。\n"
            "それこそが、ブリーズ・ノールの邸宅で奪われた五つの尊い命の犠牲から私たちが受け取るべき、最も重い教訓なのです。"
        ),
        (
            "いかなる信仰や倫理的教条も、自己保身と卑怯さ、そして尊い命の破壊を正当化するための防壁として利用されてはならないのです。",
            "\n半世紀以上を経てブリーズ・ノールの悲劇を振り返る時、最も消え去らない傷跡は法廷記録の中だけではなく、悪を阻止する機会を持ちながら躊躇してしまった人々の心の中に刻まれています。\n"
            "「目撃者の道徳的トラウマ」という現象は、演劇教師ジーン・フィリップスをはじめ、生前のリスト一家と関わりのあった人々の生涯にわたる悔恨に如実に表れています。\n"
            "社会的な沈黙は積極的な悪意から生じるのではなく、波風を立てることへの恐れや、社会的弱者の発する不吉な予感を軽視する習慣から生まれます。\n"
            "家庭内の息苦しいほどの恐怖について若者が声を上げた時、それは決して不可侵の私事として見過ごされるべきではなく、社会が沈黙を破って行動を起こすべき緊急の命題なのです。"
        )
    ],
    'KO': [
        (
            "불길한 이상 징후들이 서서히 드러나기 시작했을 때조차, 집단적 정상성 편향은 가장 결정적인 위험 신호들을 무시하게 만들었습니다.",
            "\n웨스트필드와 같은 명망 높은 상류층 공동체에서 사람들은 사회적 지위와 부유함이 악으로부터 면제권을 준다는 환상에 스스로를 안주시키곤 합니다.\n"
            "단정한 정장 차림과 독실한 종교 생활이라는 겉모습은 평온한 벨벳 커튼을 드리웠지만, 사회가 본래 지녀야 할 자연스러운 경계심을 완전히 마비시키고 말았습니다.\n"
            "한겨울 밤새 저택의 불빛이 환하게 켜져 있고 현관 앞에 신문이 쌓여가던 한 달 가까운 시간 동안, 이웃들은 그저 예의 바른 침묵 속에서 지나칠 뿐이었습니다.\n"
            "가정의 사생활 존중이라는 미명 아래 숨겨진 이러한 집단적 무관심이야말로, 참극이 그대로 동결될 수 있는 완벽한 진공 상태를 만들어냈습니다."
        ),
        (
            "그 후 수십 년의 세월이 흘렀지만, 제 어린 제자가 남긴 그 절박한 호소는 영원히 지워지지 않는 회한이 되어 제 영혼을 짓누르고 있습니다.",
            "\n그날 오후 연극 연습실에서 저를 바라보던 패트리샤의 공포에 질린 눈빛을 떠올릴 때마다, 제 가슴은 무력감과 끝없는 후회로 죄어옵니다.\n"
            "그 아이는 자신의 목을 조여오는 파멸의 차가운 기운을 이미 감지하고 있었으며, 자신이 신뢰하는 유일한 어른에게 용기를 내어 도움을 요청했던 것입니다.\n"
            "하지만 그 당시 저는 그것을 지나치게 엄격한 가정환경 탓에 생긴 사춘기 특유의 과민한 불안으로만 치부하며, 리스트 씨처럼 모범적인 아버지가 자식들을 해칠 리 없다고 스스로를 안심시켰습니다.\n"
            "제 자신의 순진한 망설임이 죄 없는 어린 영혼의 마지막 생존 기회를 앗아가고 만 것입니다."
        ),
        (
            "그것은 당시의 전통적인 수사 기법의 한계를 완전히 뛰어넘는 지극히 까다로운 과학적 난제였습니다.",
            "\n과거의 망령에 짓눌리지 않고 십팔 년이라는 긴 세월을 버텨내기 위해, 존 리스트의 정신은 '인지적 구획화'라는 극단적인 방어 기제를 작동시켰습니다.\n"
            "그는 천구백칠십일년 십일월 구일의 모든 기억을 견고한 심리적 금고 속에 동결하여 봉인하고, 일상적인 의식으로부터 철저히 격리하는 데 성공했습니다.\n"
            "로버트 클라크라는 가명 아래 그는 태연하게 재혼을 하고, 매일 밤 평안하게 잠을 청하며, 모범적인 신사로서 매주 일요일 예배에 참석하는 삶을 유지했습니다.\n"
            "그는 악몽을 꾸지도 않았는데, OCPD의 왜곡된 세계관 속에서 브리즈 놀의 비극은 살인이 아니라, 단지 자신이 결산하고 장부를 영구히 덮어버린 고통스러운 파산 절차에 불과했기 때문입니다."
        ),
        (
            "그는 현세에서 악착같이 살아남아 일하다가 임종 직전에 회개함으로써, 훗날 천국에서 가족들과 재회하겠다는 기괴한 망상을 품었던 것입니다.",
            "\n수십 년 동안 대중의 뇌리를 떠나지 않은 근본적인 의문이 있습니다. 왜 존 리스트처럼 독실한 신자가 온 가족의 목숨을 앗아간 후에도 진정한 뉘우침을 단 한 번도 보이지 않았을까요?\n"
            "그 답은 정서적 공감 능력의 완전한 결핍과 '더 높은 충성심에의 호소'라는 도덕적 중화 기제에 있습니다.\n"
            "목사에게 보낸 다섯 쪽짜리 편지는 참회가 아니라 치밀하게 계산된 신학적 거래였습니다. 가족의 신앙이 온전할 때 목숨을 끊어주는 것이야말로 그들의 영혼이 천국에 들어가도록 보장하는 자비의 행위라고 스스로를 설득했던 것입니다.\n"
            "병리적 자기애적 자아에게 자신의 죄를 인정하는 것은 완벽한 가면을 완전히 산산조각 내는 것을 의미합니다. 그리하여 그의 정신은 영원히 양심의 책임을 회피하기 위해 종교적 자기기만에 필사적으로 매달렸던 것입니다."
        ),
        (
            "이 방어기제는 한 인간이 자신이 파괴한 끔찍한 과거의 잿더미 바로 위에서 선량하고 평화로운 시민으로 살아갈 수 있도록 만들어주었습니다.",
            "\n이십 년 후 법정 피고인석에 섰을 때 존 리스트가 흘린 드문 눈물은 브리즈 놀의 스테인드글라스 아래에서 스러져간 다섯 영혼을 위한 것이 결코 아니었습니다.\n"
            "그것은 범죄심리학에서 말하는 전형적인 '자기애의 붕괴'와 '병리적 자기연민'의 표출이었습니다.\n"
            "그는 오직 자기 자신만을 위해 울었습니다. 짓밟힌 평판을 슬퍼하고, 박탈당한 자유를 한탄하며, 로버트 클라크로서 누리던 위선적인 삶이 산산조각 난 것에 대해 비통해했던 것입니다.\n"
            "창살 안에서 생을 마감하는 마지막 날까지도 그는 자신이 자녀들을 사랑하는 다정한 아버지였다고 뻔뻔스럽게 주장하며, 결코 구원받을 수 없는 냉혹한 영혼의 민낯을 드러냈습니다."
        ),
        (
            "그 뒤에 밝혀진 진실은 가장 지독한 악마일수록 평범함과 친절이라는 가면을 완벽하게 뒤집어쓴다는 사실을 뼈저리게 증명해 주었습니다.",
            "\n솔직히 고백하자면, 수년 동안 저는 남의 일에 참견하는 피해망상 환자 취급을 받을까 두려워 마음속에 피어오르는 작은 의구심들을 스스로 억눌러 왔습니다.\n"
            "우연히 오래된 잡지 기사를 보며 밥 클라크가 도망자 존 리스트와 판박이처럼 닮았다는 사실을 발견했을 때도, 델로리스에게 농담 반 진담 반으로 건넸을 뿐, 서로의 평화로운 삶을 깨뜨리고 싶지 않아 그냥 웃어넘기고 말았습니다.\n"
            "하지만 그 일요일 밤, 이천이백만 명의 시청자 앞에서 프랭크 벤더의 점토 흉상이 전국 방송 화면에 나타난 순간, 제 등골을 타고 얼음 같은 전율이 흘러내렸습니다.\n"
            "이제 더 이상의 망설임은 예의 바른 신중함이 아니라, 눈앞에 숨어 있는 흉악한 범죄에 비겁하게 가담하는 것임을 깨달았습니다.\n"
            "양심과 시민으로서의 책임감이 저로 하여금 핫라인으로 전화를 걸게 만들었습니다. 악 앞에서 침묵하는 사회는 스스로 인간성을 포기하는 사회이기 때문입니다."
        ),
        (
            "도망자의 코 위에 얹혀 있던 그 갈색 뿔테 안경이야말로, 그를 교도소 독방으로 이끈 운명의 열쇠였던 것입니다.",
            "\n이웃 완다 플래너리의 용기 있는 신고는 기만의 장막을 찢어버렸지만, 동시에 두 번째 아내인 델로리스 밀러의 정신에 치명적인 타격을 입혔습니다.\n"
            "델로리스는 법적으로는 아무런 죄가 없었지만, '신뢰의 배신으로 인한 자아의 붕괴'라는 끔찍한 심리적 외상을 겪어야만 했습니다.\n"
            "그녀는 여러 해 동안 한 침대에서 잠을 자고, 함께 기도하며 식사를 나누던 온순한 남편이 실은 자신의 노모와 아내, 그리고 세 자녀를 몰살한 살인마였다는 끔찍한 진실과 마주하게 되었습니다.\n"
            "자신도 모르는 사이에 흉악범의 은폐를 돕는 방패막이가 되어주었다는 깊은 자괴감과 죄책감은 그녀를 극심한 정신적 위기로 몰아넣었습니다. 이는 OCPD 범죄자의 완벽한 가면 앞에서 순진함이 치러야 했던 너무나 가혹한 대가였습니다."
        ),
        (
            "아무리 치밀하게 쌓아 올린 거짓의 장벽이라 할지라도, 과학적 진실과 현대 법의학의 빛 앞에서는 결코 영원할 수 없음을 증명해 준 것입니다.",
            "\n존 리스트 사건의 기록은 닫혔지만, 현대의 범죄 수사와 가정의 안전에 영원한 경종을 울리고 있습니다.\n"
            "주변 사람들의 예리한 관찰력과 개입하는 용기가 없다면, 아무리 훌륭한 겉모습이나 높은 사회적 지위도 결코 안전을 완벽히 보장해 주지 못합니다.\n"
            "한 공동체의 진정한 평화는 닫힌 대문이나 무관심한 조심성으로 세워지는 것이 아니라, 가장 연약한 생명들을 연대하여 보호하려는 용기를 통해 지켜지는 것입니다.\n"
            "그것이야말로 브리즈 놀 저택에서 희생된 다섯 명의 무고한 생명이 남긴 고통과 눈물로 맞바꾼 가장 값진 인도주의적 유산입니다."
        ),
        (
            "그 어떤 신앙이나 도덕적 가치도 비겁한 자기합리화와 가족의 생명을 앗아가는 폭력을 정당화하는 방패가 될 수는 없습니다.",
            "\n반세기가 넘는 시간이 흐른 지금 브리즈 놀의 비극을 되돌아볼 때, 가장 오래 남는 상처는 법정의 기록 속에만 있는 것이 아니라, 악을 막을 수 있었던 기회를 놓쳐버린 사람들의 마음속에 남아 있습니다.\n"
            "'목격자의 도덕적 외상'이라는 현상은 연극 교사 진 필립스를 비롯하여 리스트 가족과 마주쳤던 사람들의 평생에 걸친 자책감 속에 생생히 새겨져 있습니다.\n"
            "사회의 침묵은 대개 적극적인 악의에서 비롯되는 것이 아니라, 타인의 시선에 대한 두려움, 갈등에 대한 기피, 그리고 약자들이 느끼는 불길한 예감을 가볍게 넘겨버리는 습관에서 발생합니다.\n"
            "자신의 집 안에서 짓눌려 숨이 막히는 공포에 대해 어린 영혼이 도움을 외칠 때, 그것은 결코 숨겨두어야 할 사적인 문제가 아니라 온 공동체가 침묵을 깨고 행동해야 하는 절박한 도덕적 명령인 것입니다."
        )
    ]
}

def update_header(content, lang):
    if lang == 'VN':
        content = re.sub(
            r'\*\*Phiên bản:\*\* Chuẩn A2 — Bản kiểm duyệt an toàn YouTube.*',
            r'**Phiên bản:** Chuẩn A2c/K10 — Hệ sinh thái 10 chỉ dấu tâm lý học tội phạm & Bổ sung phân tích biến chuyển tâm lý đa chiều ngày 14/11/2026 (257 câu).',
            content
        )
        content = re.sub(
            r'\|\s*\*\*Tổng số câu đọc\*\*\s*\|\s*220 câu.*',
            r'| **Tổng số câu đọc** | 257 câu (chuẩn >= 200 câu) |',
            content
        )
        content = re.sub(
            r'\|\s*\*\*Tổng thời lượng dự kiến\*\*\s*\|\s*26 – 28 phút.*',
            r'| **Tổng thời lượng dự kiến** | 28 – 32 phút (5 hồi nội dung + các khoảng lặng âm thanh kịch tính) |',
            content
        )
    elif lang == 'EN':
        content = re.sub(
            r'\*\*Version:\*\* Standard A2 — YouTube Safety Compliant.*',
            r'**Version:** Standard A2c/K10 — 10 Psychological Indicators & Multidimensional Behavioral Dynamics (257 sentences).',
            content
        )
        content = re.sub(
            r'\|\s*\*\*Total Spoken Sentences\*\*\s*\|\s*220 sentences.*',
            r'| **Total Spoken Sentences** | 257 sentences (Standard >= 200) |',
            content
        )
        content = re.sub(
            r'\|\s*\*\*Estimated Duration\*\*\s*\|\s*26 – 28 minutes.*',
            r'| **Estimated Duration** | 28 – 32 minutes (5 acts + dramatic soundscapes) |',
            content
        )
    elif lang == 'JA':
        content = re.sub(
            r'\*\*バージョン:\*\* A2標準 — YouTube安全ポリシー.*',
            r'**バージョン:** A2c/K10標準 — 犯罪心理学10指標生態系＆多次元行動変容分析 (257文).',
            content
        )
        content = re.sub(
            r'\|\s*\*\*総音声センテンス数\*\*\s*\|\s*220文.*',
            r'| **総音声センテンス数** | 257文 (基準 >= 200文) |',
            content
        )
        content = re.sub(
            r'\|\s*\*\*想定総所要時間\*\*\s*\|\s*26 – 28分.*',
            r'| **想定総所要時間** | 28 – 32分 (5幕構成 + 劇的音響間欠) |',
            content
        )
    elif lang == 'KO':
        content = re.sub(
            r'\*\*버전:\*\* A2 표준 — 유튜브 안전 가이드라인.*',
            r'**버전:** A2c/K10 표준 — 범죄심리학 10대 지표 생태계 및 다차원 행동변용 분석 (257문장).',
            content
        )
        content = re.sub(
            r'\|\s*\*\*총 낭독 문장 수\*\*\s*\|\s*220문장.*',
            r'| **총 낭독 문장 수** | 257문장 (기준 >= 200문장) |',
            content
        )
        content = re.sub(
            r'\|\s*\*\*예상 총 재생 시간\*\*\s*\|\s*26 – 28분.*',
            r'| **예상 총 재생 시간** | 28 – 32분 (5막 구성 + 극적 음향 간헐) |',
            content
        )
    return content

targets = [
    ('VN', '01_KICH_BAN/Ho_So_Toi_Pham/Tap16/kichban_tap16_23102026.md'),
    ('EN', '01_KICH_BAN/Ho_So_Toi_Pham/Tap16/kichban_tap16_EN.md'),
    ('EN', '01_KICH_BAN/Ho_So_Toi_Pham/Tap16_EN/kichban_tap16_EN.md'),
    ('JA', '01_KICH_BAN/Ho_So_Toi_Pham/Tap16_JA/kichban_tap16_JA.md'),
    ('KO', '01_KICH_BAN/Ho_So_Toi_Pham/Tap16_KO/kichban_tap16_KO.md'),
]

for lang, path in targets:
    raw = open(path, encoding='utf-8').read()
    raw = update_header(raw, lang)
    
    ins_list = insertions[lang]
    for target, addition in ins_list:
        if target not in raw:
            print(f"ERROR: target not found in {path}:\n{target}")
            sys.exit(1)
        raw = raw.replace(target, target + addition, 1)
        
    with open(path, 'w', encoding='utf-8') as f:
        f.write(raw)
    print(f"Successfully updated: {path}")

print("\nAll 5 script files successfully expanded.")
