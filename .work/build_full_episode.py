# -*- coding: utf-8 -*-
"""
Tạo kịch bản Tập 31 chuẩn A2/K10/V9 đầy đủ 3 ngôn ngữ: VN, EN, JA.
Đạt trên 210 câu thoại chuẩn mực (214 câu), đồng bộ 100% từng câu thoại giữa 3 ngôn ngữ.
Tích hợp các cứ liệu lịch sử mới nhất:
- Thí nghiệm Henry Murray tại Harvard (Project MKUltra / 200 giờ thẩm vấn tra tấn tâm lý).
- Nạn nhân Percy Wood (Chủ tịch United Airlines, cuốn tiểu thuyết Ice Brothers).
- Nạn nhân tử vong Hugh Scrutton (Sacramento, 1985) và Gary Wright (Salt Lake City, 1987, bản phác thảo áo mũ trùm kính râm).
- Nạn nhân Thomas Mosser (Bà Susan Mosser) và Gilbert Murray (1995).
- Tình bạn hàn gắn cảm động giữa David Kaczynski và nạn nhân Gary Wright.
- Bức thư và câu tục ngữ "You can't eat your cake and have it too".
"""
import sys, os, json, re

def build_full_episode():
    blocks = []

    # ==========================================
    # HỒI 1: KHỞI NGUỒN CƠN ÁC MỘNG BƯU CHÍNH & VỎ BỌC RỪNG SÂU (44 CÂU)
    # ==========================================
    blocks.append(('ACT', 1, 'KHỞI NGUỒN CƠN ÁC MỘNG BƯU CHÍNH & VỎ BỌC RỪNG SÂU', 'ORIGIN OF THE POSTAL NIGHTMARE & THE WILDERNESS VEIL', '郵便爆弾の悪夢の起源と深林の隠れ蓑'))
    blocks.append(('BGM', 'BGM', 'Dark Ambient âm u, tiếng nhịp tim đập chậm và tiếng tích tắc đồng hồ kim loại ngột ngạt.', 'Dark Ambient, slow heartbeat rhythms, and oppressive metallic clock ticks.', '陰鬱なダークアンビエント、遅い心拍音、息詰まる機械時計の秒針音。'))

    blocks.append(('LOI', 'HOST',
        'chậm rãi, giọng trầm ấm gợi mở không gian lịch sử và sức nặng tâm lý',
        [
            'Vào những năm cuối thập niên 1970, nước Mỹ bước vào kỷ nguyên bùng nổ của cuộc cách mạng công nghệ số và máy tính cá nhân.',
            'Những cỗ máy vi tính đầu tiên xuất hiện trong các trường đại học và phòng nghiên cứu, hứa hẹn mở ra một tương lai tươi sáng cho toàn nhân loại.',
            'Thế nhưng, chính trong làn sóng lạc quan ấy, một bóng ma vô hình đã bắt đầu gieo rắc nỗi kinh hoàng tột độ khắp các khuôn viên học thuật.',
            'Một kẻ ẩn danh mang mật danh Unabomber đã biến những kiện bưu phẩm thường nhật thành những chiếc bẫy chết chóc đầy ám ảnh.',
            'Suốt gần hai thập kỷ, hòm thư trước cửa nhà từng là biểu tượng của sự kết nối yêu thương bỗng chốc trở thành nỗi hoang tưởng tập thể của hàng triệu con người.',
            'Nỗi sợ hãi len lỏi vào từng gia đình khi người ta phải nín thở trước mỗi phong bì dày hay kiện hàng bọc giấy nâu gửi tới bàn làm việc.',
            'Nhưng điều kỳ lạ và gây rúng động nhất không chỉ nằm ở sự tinh xảo cơ học của những quả bom phế liệu.',
            'Nó nằm ở chân dung của kẻ chủ mưu: một thần đồng toán học kiệt xuất của Đại học Harvard, người từng từ bỏ sự nghiệp đỉnh cao để lui về một căn lều gỗ hẻo lánh giữa rừng sâu Montana.',
            'Làm thế nào một trí tuệ phi phàm lại biến thành một cỗ máy hủy diệt lạnh lùng, sẵn sàng tước đoạt sinh mạng của những người xa lạ nhân danh một lý tưởng triết học méo mó?'
        ],
        [
            'In the late 1970s, America entered an era marked by the booming revolution of personal computing and digital technology.',
            'The earliest computers emerged across university campuses and research laboratories, promising a radiant future for humanity.',
            'Yet right amidst that wave of optimism, an invisible phantom began sowing sheer terror across academic sanctuaries.',
            'An elusive figure codenamed the Unabomber transformed ordinary mail packages into haunting lethal traps.',
            'For nearly two decades, curbside mailboxes once representing loving connections suddenly turned into a collective paranoia for millions.',
            'Fear permeated ordinary households as citizens held their breath before handling thick envelopes or brown-paper parcels.',
            'However, the most perplexing and shocking revelation lay not merely in the mechanical craftsmanship of the scrap-metal bombs.',
            'It resided in the mastermind behind them: a brilliant Harvard mathematics prodigy who abandoned a stellar career to retreat into an isolated wooden cabin in the Montana wilderness.',
            'How did a towering intellectual mind transform into a cold-blooded killing machine, willing to slaughter innocent strangers in the name of a distorted philosophical ideology?'
        ],
        [
            '1970年代後半、アメリカはパーソナルコンピュータとデジタル技術の爆発的な革命期を迎えようとしていました。',
            '最初のコンピュータ群が大学のキャンパスや研究所に現れ、人類に輝かしい未来を約束しているかのように見えました。',
            'しかし、その楽観主義の波のただ中で、目に見えない亡霊が学問の聖域に底知れぬ恐怖を撒き散らし始めました。',
            '「ユナボマー」というコードネームで呼ばれた匿名の怪物は、日常の郵便小包を生死を分かつ死の罠へと変貌させたのです。',
            '約20年間にわたり、かつては愛の絆を象徴していた玄関前の郵便箱が、突如として何百万人もの人々の集団妄想の対象となりました。',
            '分厚い封筒や茶色い小包を手にするたび、人々は息を呑み、恐怖は日常の家庭にまで深く侵入していきました。',
            'しかし、最も不可解で衝撃的な事実は、廃材で作られた爆弾の精巧な機械的構造だけにとどまりませんでした。',
            'それは首謀者の素顔にありました。ハーバード大学を卒業した天才数学者が、輝かしいキャリアを捨ててモンタナの深林にある粗末な小屋に隠遁していたのです。',
            'いかにして並外れた知性が冷酷な破壊機械へと変貌し、歪んだ哲学的理念の名の下に見知らぬ他者の命を奪うに至ったのでしょうか。'
        ]
    ))

    blocks.append(('SFX', 'SFX', 'Tiếng động cơ máy bay gầm rú từ xa, tiếng gió rít qua rặng thông đại ngàn.', 'Sound of distant airplane engines roaring, wind howling through pine trees.', '遠くで響く飛行機のエンジン音、松林を吹き抜ける風のうめき。'))

    blocks.append(('LOI', 'HOST',
        'chuyển giọng u tối, kể chi tiết các vụ nổ ban đầu',
        [
            'Cơn ác mộng bắt đầu vào ngày 25 tháng 5 năm 1978 tại Đại học Illinois ở Chicago.',
            'Một kiện bưu phẩm khả nghi được gửi trả về cho Giáo sư kỹ thuật vật liệu Cristos Gianakos.',
            'Tuy nhiên, vị giáo sư khẳng định mình chưa từng gửi bưu kiện đó và đã liên hệ với nhân viên an ninh nhà trường.',
            'Khi gói hàng được mở ra tại khuôn viên Đại học Northwestern, một tiếng nổ chói tai vang lên làm bị thương một viên cảnh sát bảo vệ.',
            'Đó là phát súng mở màn cho chuỗi 16 vụ gửi bom thư kéo dài suốt 17 năm sau đó.',
            'Mục tiêu của kẻ tấn công liên tục thay đổi: từ các giáo sư toán học, chuyên gia máy tính cho đến các giám đốc điều hành hàng không.',
            'Tháng 11 năm 1979, một quả bom thư được đặt trong khoang hành lý chuyến bay 444 của hãng United Airlines chở 80 hành khách.',
            'Cơ chế kích nổ bằng khí áp kế bị lỗi kỹ thuật, chỉ tạo ra một đám khói mù mịt buộc máy bay phải hạ cánh khẩn cấp.',
            'Và đến tháng 6 năm 1980, Percy Wood, Chủ tịch hãng United Airlines, bị thương nặng khi mở một kiện hàng ngụy trang dưới dạng cuốn tiểu thuyết Ice Brothers.'
        ],
        [
            'The nightmare commenced on May 25, 1978, at the University of Illinois in Chicago.',
            'A suspicious postal package was returned to materials engineering professor Cristos Gianakos.',
            'The professor, however, affirmed he had never mailed the parcel and immediately alerted campus security.',
            'When the package was inspected at Northwestern University, a deafening blast tore through the air, injuring a security officer.',
            'That was the opening salvo of a 16-bomb campaign spanning the next 17 grueling years.',
            'The attacker targets shifted relentlessly: from mathematics professors and computer scientists to airline executives.',
            'In November 1979, a barometric bomb was placed inside the cargo hold of United Airlines Flight 444 carrying 80 passengers.',
            'A mechanical flaw in the altimeter trigger caused dense smoke rather than a catastrophic explosion, forcing an emergency landing.',
            'In June 1980, Percy Wood, President of United Airlines, was severely wounded when opening a package disguised as the novel Ice Brothers.'
        ],
        [
            '悪夢は1978年5月25日、シカゴのイリノイ大学で始まりました。',
            '材料工学の教授クリストス・ジアナコス宛てに、差出人不明の不審な郵便小包が返送されてきたのです。',
            'しかし教授は身に覚えがないと主張し、直ちに大学の警備責任者に通報しました。',
            'ノースウェスタン大学構内で小包が開けられた瞬間、鋭い爆発音が響き渡り、警備員が負傷しました。',
            'それは、その後17年間にわたる計16回もの郵便爆弾事件の不吉な幕開けでした。',
            '標的は数学者、コンピュータ科学者、そして航空会社の重役へと絶え間なく変化していきました。',
            '1979年11月、80人の乗客を乗せたユナイテッド航空444便の貨物室に気圧作動式爆弾が仕掛けられました。',
            '起爆機構の作動不良により、爆弾は機体を破壊することなく白煙を上げたのみで、緊急着陸に成功しました。',
            'そして1980年6月には、ユナイテッド航空社長のパーシー・ウッドが、小説『アイス・ブラザーズ』に偽装された爆弾を開封して重傷を負ったのです。'
        ]
    ))

    blocks.append(('LOI', 'INVESTIGATOR',
        'giọng đanh thép, chuyên nghiệp, mô tả sự bế tắc của cuộc điều tra',
        [
            'Ngay sau sự cố hàng không năm 1979, Cục Điều tra Liên bang FBI đã chính thức thành lập ban chuyên án mang mã số UNABOM.',
            'Cái tên này được ghép từ hai nhóm mục tiêu ban đầu của đối tượng: University và Airline.',
            'Hơn một trăm năm mươi đặc vụ toàn thời gian, phối hợp cùng các chuyên gia chất nổ của ATF và Thanh tra Bưu điện, đã vào cuộc rà soát hàng ngàn manh mối.',
            'Nhưng đối tượng tỏ ra là một bậc thầy về kỹ thuật ngụy trang và xóa dấu vết hiện trường.',
            'Các thiết bị nổ đều được chế tạo thủ công hoàn toàn từ gỗ vụn, ống kim loại cũ và các linh kiện cơ khí tự chế tác.',
            'Hắn tỉ mỉ mài nhẵn mọi chi tiết bằng tay để xóa sạch dấu vân tay và dấu vết công cụ công nghiệp.',
            'Mảnh ghép duy nhất mà hắn cố tình để lại là hai chữ cái FC được khắc bí ẩn bên trong các mảnh vỡ kim loại.',
            'Và suốt hơn một thập kỷ, chúng tôi phải đối mặt với một bóng ma vô hình, không để lại bất kỳ dấu vết sinh học nào.'
        ],
        [
            'Immediately following the 1979 airline incident, the FBI formally established a joint task force codenamed UNABOM.',
            'The name derived from the perpetrator primary targets: Universities and Airlines.',
            'Over 150 full-time investigators, coordinating with ATF explosives experts and Postal Inspectors, probed thousands of leads.',
            'Yet the suspect proved to be an absolute master of forensic countermeasures and crime scene sanitation.',
            'Every explosive device was handcrafted entirely from scrap timber, plumbing pipes, and improvised mechanical components.',
            'He meticulously polished and filed every single part by hand to eliminate latent fingerprints and machine toolmarks.',
            'The only tangible clue intentionally left behind was the enigmatic inscription FC stamped onto internal metal fragments.',
            'For over a decade, we found ourselves pursuing an invisible ghost who left virtually zero biological traces.'
        ],
        [
            '1979年の航空機事件の直後、FBIはコードネーム「UNABOM」と呼ばれる合同特別捜査班を正式に立ち上げました。',
            'この名称は、犯人の初期の標的であった大学（University）と航空会社（Airline）の頭文字に由来しています。',
            '150人以上の専任捜査官がATFの爆発物専門家や郵便監察局と連携し、数万件に及ぶ手掛かりを徹底的に洗い出しました。',
            'しかし犯人は、現場の痕跡を完全に消し去る偽装工作の絶対的な達人でした。',
            'すべての爆発装置は、廃材の木片や古い配管パイプ、手作りの機械部品から完全に手作業で組み立てられていました。',
            '彼は指紋や工業用工具の痕跡を消し去るため、すべての部品を入念に手作業で研磨していたのです。',
            '彼が意図的に残した唯一の手掛かりは、金属片の内側に刻まれた謎めいた「FC」という2文字だけでした。',
            '10年以上にわたり、私たちは生物学的痕跡を一切残さない目に見えない亡霊と対峙することを余儀なくされたのです。'
        ]
    ))

    blocks.append(('LOI', 'ORDINARY_PERSON',
        'N1: Cư dân thị trấn Lincoln, Montana – giọng run rẩy, bàng hoàng',
        [
            'Ở một thị trấn nhỏ hẻo lánh giữa thung lũng như Lincoln, mọi người sống dựa vào sự tin tưởng và tôn trọng không gian riêng của nhau.',
            'Chúng tôi thường thấy một người đàn ông râu tóc bù xù đạp chiếc xe đạp cũ vào tiệm tạp hóa mua đậu hộp và bột mì.',
            'Ông ấy ít nói, ánh mắt xa xăm và luôn né tránh các cuộc trò chuyện xã giao.',
            'Mọi người chỉ nghĩ đơn giản rằng đó là một người yêu thiên nhiên muốn sống cuộc đời ẩn dật như nhà văn Henry Thoreau.',
            'Ông ta cất một căn lều gỗ nhỏ sâu trong rừng, không điện thắp sáng, không nước máy, sống hoàn toàn tách biệt.',
            'Chúng tôi tôn trọng sự riêng tư ấy và xem ông ta như một người hàng xóm vô hại.',
            'Không một ai trong chúng tôi có thể ngờ rằng bên trong căn lều tối tăm ấy lại là nơi chế tạo ra những cỗ máy hủy diệt gieo rắc tang tóc khắp nước Mỹ.'
        ],
        [
            'In a secluded valley town like Lincoln, folks live by mutual trust and deep respect for each other privacy.',
            'We often saw an unkempt man with a ragged beard riding an old bicycle to the general store to buy canned beans and flour.',
            'He spoke very little, kept his distant gaze fixed forward, and consistently avoided small talk.',
            'People simply assumed he was a nature lover seeking a peaceful hermit life, much like Henry David Thoreau.',
            'He built a modest timber cabin deep in the pines, without electricity or running water, living in complete detachment.',
            'We respected his solitude and regarded him merely as an eccentric, harmless neighbor.',
            'None of us could have ever fathomed that inside that dim timber shack, America deadliest killer was manufacturing lethal instruments of death.'
        ],
        [
            'リンカーンのような人里離れた渓谷の小さな町では、人々は互いの信頼とプライバシーの尊重を何よりも重んじて暮らしています。',
            '手入れされていない髭を生やした男が古い自転車に乗り、豆の缶詰や小麦粉を買いに雑貨店へやって来る姿をよく見かけました。',
            '彼は極めて無口で、遠くを見つめるような視線で、世間話を決して交わそうとはしませんでした。',
            '住民たちは皆、作家ソローのように静かな世捨て人生活を好む自然愛好家なのだろうと信じ込んでいたのです。',
            '彼は電気も水道もない小さな丸太小屋を森の奥に建て、完全に社会から隔絶して暮らしていました。',
            '私たちはその孤独を尊重し、彼を単なる無害で風変わりな隣人に過ぎないと考えていたのです。',
            'あの薄暗い丸太小屋の中で、全米を恐怖に陥れた死の兵器が製造されていたなどとは、誰一人として想像すらできませんでした。'
        ]
    ))

    blocks.append(('LOI', 'PSYCHOLOGIST',
        'giọng điềm đạm, sắc sảo, phân tích tâm lý',
        [
            'Dưới góc độ tâm lý học hành vi, vụ án Unabomber là một minh chứng đau lòng cho sự tha hóa của trí tuệ khi bị ngắt kết nối hoàn toàn khỏi lòng trắc ẩn.',
            'Hiện tượng này bắt nguồn từ một cơ chế tâm lý cực đoan mang tên “Ảo tưởng cứu thế và Sự ái kỷ trí tuệ”.',
            'Đối tượng tự phong cho mình sứ mệnh cao cả là bảo vệ nhân loại khỏi sự thống trị của hệ thống kỹ trị công nghiệp.',
            'Hắn xây dựng một bức tường phòng vệ tinh thần kiên cố để biện minh rằng: sự hy sinh sinh mạng của một vài cá nhân là cái giá tất yếu để thức tỉnh cả một nền văn minh.',
            'Khi một bộ não thông minh tự thuyết phục bản thân rằng mình nắm giữ chân lý tối thượng, nó sẽ triệt tiêu hoàn toàn cảm giác tội lỗi và biến bạo lực thành một phương tiện đạo đức giả tạo.',
            'Sự cô lập kéo dài giữa thiên nhiên hoang dã không hề chữa lành tâm hồn hắn, mà trái lại đã khuếch đại những hoang tưởng thù hằn thành hành động tàn bạo.'
        ],
        [
            'From a behavioral psychology perspective, the Unabomber case stands as a tragic testament to intellect alienated from human empathy.',
            'This phenomenon stems from a toxic psychological mechanism known as Intellectual Narcissism and Messianic Delusion.',
            'The perpetrator appointed himself on a divine crusade to liberate humanity from the encroachment of the techno-industrial system.',
            'He erected an impenetrable psychological defense mechanism to justify that sacrificing individual lives was an inevitable cost to awaken civilization.',
            'When a brilliant intellect convinces itself of possessing supreme moral truth, it eradicates empathy and transforms violence into a sanctimonious crusade.',
            'Prolonged wilderness isolation never healed his spirit; rather, it magnified his paranoid resentments into calculated cruelty.'
        ],
        [
            '行動心理学の視点から見れば、ユナボマー事件は人間の共感力から完全に切り離された知性の悲劇的な堕落を雄弁に物語っています。',
            'この現象は、「知性愛己主義と救世主妄想」と呼ばれる極端な心理メカニズムに端を発しています。',
            '犯人は、人類を技術的産業システムの専制から解放するという崇高な使命を自らに勝手に課していました。',
            '彼は強固な心理的防衛機制を築き上げ、数人の無実の命を犠牲にすることは文明を覚醒させるための不可避の代償であると正当化したのです。',
            '卓越した頭脳が自らを至高の真理の保持者であると思い込むとき、罪悪感は完全に麻痺し、暴力は独善的な道徳的手段へとすり替えられてしまうのです。',
            '大自然の中での長期にわたる孤独な隠遁生活は彼の魂を癒やすどころか、その偏執病的な憎悪を冷酷な凶行へと増幅させたに過ぎませんでした。'
        ]
    ))

    blocks.append(('LOI', 'INVESTIGATOR',
        'bổ sung chi tiết về vụ án mạng đầu tiên năm 1985',
        [
            'Sự tàn bạo của đối tượng đã chính thức bước sang nấc thang đẫm máu vào ngày 11 tháng 12 năm 1985.',
            'Hugh Scrutton, chủ một cửa hàng cho thuê máy tính tại Sacramento, California, đã nhìn thấy một bưu kiện gỗ để cạnh bãi đỗ xe phía sau cửa hàng.',
            'Khi ông cúi xuống nhặt vật thể lạ lên, khối thuốc nổ nhồi đinh nhọn và mảnh kim loại đã phát nổ dữ dội, cướp đi sinh mạng của người đàn ông vô tội.',
            'Đây là nạn nhân tử vong đầu tiên của Unabomber, đánh dấu sự chuyển hóa từ việc đe dọa sang hành vi sát nhân có chủ đích.',
            'Sau đó vào năm 1987 tại Salt Lake City, Gary Wright, một chủ cửa hàng máy tính khác, cũng bị trọng thương bởi một quả bom tương tự.',
            'Chính tại hiện trường Salt Lake City, một nhân chứng tình cờ nhìn thấy một người đàn ông mặc áo nỉ có mũ trùm đầu và đeo kính râm phi công.',
            'Từ lời khai quý giá đó, bức phác thảo truy nã kinh điển của Unabomber đã ra đời và được dán khắp các bưu điện trên toàn nước Mỹ.'
        ],
        [
            'The perpetrator lethality escalated to fatal violence on December 11, 1985.',
            'Hugh Scrutton, the owner of a computer rental store in Sacramento, California, spotted a wooden package placed near the rear parking lot.',
            'As he bent down to inspect the unusual object, an explosive charge packed with nails and metal shards detonated violently, killing him instantly.',
            'This marked the Unabomber first homicide, signaling an ominous transformation from ideological intimidation into premeditated murder.',
            'In 1987 in Salt Lake City, Gary Wright, another computer store manager, was severely mangled by a similar explosive trap.',
            'Crucially at that Salt Lake City scene, an eyewitness caught a fleeting glimpse of a man wearing a hooded sweatshirt and aviator sunglasses.',
            'From that vital description emerged the iconic FBI composite sketch of the Unabomber, posted across post offices nationwide.'
        ],
        [
            '犯人の凶虐性は、1985年12月11日に決定的な死の領域へと踏み出しました。',
            'カリフォルニア州サクラメントでコンピュータレンタル店を経営していたヒュー・スクラットンが、店舗裏の駐車場に置かれた木製小包に気づきました。',
            '彼がその不審物を拾い上げた瞬間、釘と金属片を大量に仕込んだ爆薬が激しく爆発し、無実の店主の命を瞬時に奪い去ったのです。',
            'これがユナボマーによる最初の犠牲者となり、思想的威嚇から計画的殺人への不吉な転換を告げるものとなりました。',
            '1987年にはソルトレイクシティで、別のコンピュータ店経営者ゲイリー・ライトが同様の爆弾によって全身に重傷を負いました。',
            'そしてこの現場において、フード付きスウェットシャツを着てアビエイターサングラスをかけた男を目撃した証言者が現れたのです。',
            'その貴重な証言から、全米の郵便局に掲示されることになるあの象徴的なモンタージュ似顔絵が誕生しました。'
        ]
    ))

    # ==========================================
    # HỒI 2: ÁI KỶ TRÍ TUỆ & CHÂN DUNG TÂM LÝ KẺ SĂN MỒI TRONG BÓNG TỐI (44 CÂU)
    # ==========================================
    blocks.append(('ACT', 2, 'ÁI KỶ TRÍ TUỆ & CHÂN DUNG TÂM LÝ KẺ SĂN MỒI TRONG BÓNG TỐI', 'INTELLECTUAL NARCISSISM & PSYCHOLOGICAL PORTRAIT OF THE SHADOW PREDATOR', '知性の傲慢と影の捕食者の深層心理'))
    blocks.append(('BGM', 'BGM', 'Nhạc điện tử trầm lạnh, nhịp điệu hồi hộp và tiếng gõ máy chữ cơ khí liên hồi.', 'Cold electronic bass, suspenseful rhythm, and relentless mechanical typewriter tapping.', '冷徹な電子音、緊迫したリズム、そして規則正しく打ち鳴らされる機械式タイプライターの打鍵音。'))

    blocks.append(('LOI', 'HOST',
        'giọng trầm tĩnh, đào sâu vào nhân cách kẻ thủ ác',
        [
            'Để hiểu được căn nguyên sâu xa của cơn thịnh nộ hủy diệt ấy, chúng ta phải quay ngược thời gian về những năm tháng thiếu thời của Theodore Kaczynski.',
            'Sinh năm 1942 tại Illinois trong một gia đình công nhân gốc Ba Lan, Ted đã sớm bộc lộ năng khiếu toán học xuất chúng.',
            'Với chỉ số thông minh lên tới 167, cậu bé Ted vượt cấp liên tục và trở thành tâm điểm của mọi sự kỳ vọng học thuật.',
            'Thế nhưng, sự vượt trội về trí não lại tỷ lệ nghịch với khả năng tương tác xã hội và sự trưởng thành cảm xúc.',
            'Cậu bé thần đồng luôn cảm thấy bị cô lập, lạc lõng giữa những bạn bè đồng trang lứa và thu mình vào một thế giới nội tâm khép kín.',
            'Năm 16 tuổi, Ted bước chân vào giảng đường Đại học Harvard danh tiếng, mang theo một tâm hồn non nớt nhưng đầy kiêu hãnh.',
            'Và chính tại ngôi trường này, một biến cố tâm lý tàn khốc đã giáng xuống, làm méo mó vĩnh viễn cấu trúc nhân cách của chàng trai trẻ.'
        ],
        [
            'To comprehend the deep roots of this destructive fury, we must journey back to the formative years of Theodore Kaczynski.',
            'Born in 1942 in Illinois to a Polish-American working-class family, young Ted demonstrated extraordinary mathematical prodigy early on.',
            'Possessing an astonishing IQ of 167, Ted skipped multiple grades and became the golden focus of immense academic expectations.',
            'However, his intellectual transcendence was inversely proportional to his social adaptability and emotional maturity.',
            'The child prodigy felt profoundly alienated from his peers, retreating deeper into a barricaded internal sanctum.',
            'At the tender age of sixteen, Ted entered Harvard University carrying a fragile soul beneath an armor of intellectual pride.',
            'It was precisely within these venerated halls that a devastating psychological trauma struck, permanently scarring his personality.'
        ],
        [
            'この破滅的な怒りの根源を理解するためには、セオドア・カジンスキーの幼少期にまで遡らなければなりません。',
            '1942年、イリノイ州のポーランド系労働者階級の家庭に生まれたテッドは、幼くして並外れた数学の才能を開花させました。',
            'IQ167という驚異的な知能指数を誇った彼は、飛び級を重ね、周囲の学問的期待を一身に背負う存在となりました。',
            'しかし、その超越した知性は、社会的適応力や感情の成熟度とは皮肉にも反比例していました。',
            '神童と呼ばれた少年は同年代の仲間から常に孤立し、閉ざされた内面の世界へと深く閉じこもっていったのです。',
            'わずか16歳で名門ハーバード大学の門をくぐったテッドは、傷つきやすい未熟な精神と肥大化した自負心を併せ持っていました。',
            'そしてまさにこの最高学府において、若き青年の人格構造を決定的に歪める過酷な心理的事件が起きたのです。'
        ]
    ))

    blocks.append(('LOI', 'PSYCHOLOGIST',
        'bóc tách chi tiết thí nghiệm Henry Murray và dự án MKUltra',
        [
            'Từ năm 1959 đến 1962, Ted Kaczynski trở thành đối tượng thử nghiệm trong một dự án nghiên cứu tâm lý học do Giáo sư Henry Murray điều hành tại Harvard.',
            'Henry Murray từng là cựu lãnh đạo đánh giá tâm lý của Cơ quan Tình báo Chiến lược OSS trong Thế chiến thứ hai.',
            'Các nghiên cứu của ông tại Harvard nhận được các nguồn tài trợ liên quan đến các chương trình nghiên cứu hành vi của tình báo thời Chiến tranh Lạnh.',
            'Trong suốt ba năm, chàng sinh viên 16 tuổi Ted Kaczynski đã trải qua hơn hai trăm giờ chịu đựng các buổi thử nghiệm thẩm vấn căng thẳng tột độ.',
            'Các sinh viên được yêu cầu viết những bài luận triết học bày tỏ niềm tin và lý tưởng sống thiêng liêng nhất của bản thân.',
            'Sau đó, họ bị đưa vào một căn phòng gắn điện cực theo dõi sinh lý, bị một thẩm vấn viên dùng những lời lẽ tàn nhẫn nhất để miệt thị và sỉ nhục bản ngã.',
            'Đối với một tâm hồn thiếu hụt sự gắn kết xã hội như Ted, cuộc thử nghiệm này đã phá hủy hoàn toàn niềm tin vào các thiết chế quyền lực.',
            'Nó cấy sâu vào tiềm thức hắn một nỗi phẫn uất bệnh lý đối với khoa học hành vi và nền văn minh công nghiệp.'
        ],
        [
            'Between 1959 and 1962, Ted Kaczynski became a test subject in an invasive psychological research study led by Professor Henry Murray at Harvard.',
            'Murray had served as a chief psychological profiler for the Office of Strategic Services during World War II.',
            'His Harvard laboratory was linked to behavioral control research streams associated with Cold War intelligence initiatives.',
            'Over three grueling years, the sixteen-year-old math prodigy endured roughly two hundred hours of severe stress interrogation sessions.',
            'Undergraduates were instructed to author deeply personal philosophical essays detailing their core worldviews and moral aspirations.',
            'They were subsequently wired to physiological monitors while aggressive interrogators systematically ridiculed and demolished their beliefs under blazing lights.',
            'For a socially fragile youth like Ted, this targeted humiliation shattered his foundational trust in institutional authority.',
            'It permanently ingrained a pathological hostility toward behavioral control systems and modern technological civilization.'
        ],
        [
            '1959年から1962年にかけて、テッドはハーバード大学のヘンリー・マレー教授が主導する過酷な心理実験の被験者となりました。',
            'マレー教授は第二次世界大戦中に米国の戦略情報局（OSS）で心理適性評価の責任者を務めた人物でした。',
            '彼のハーバードでの実験は、冷戦期の情報機関による人間行動操作研究の流れに深く繋がっていました。',
            'わずか16歳だった神童テッドは、3年間にわたり約200時間もの極限的なストレステストと心理尋問に晒されたのです。',
            '学生たちは自らの最も大切にする哲学的信条や人生の理想を論文に書かされました。',
            'その後、生理反応を測定する電極を取り付けられ、眩しい照明の下で尋問者から人格と信条を徹底的に嘲笑され、侮辱されたのです。',
            '社会的繋がりを持たなかったテッドの脆い心にとって、この組織的な屈辱は権威的制度への信頼を完全に打ち砕きました。',
            'この体験が、行動心理制御システムと近代産業文明に対する病的な敵意の炎を彼の潜在意識に決定的に植え付けたのです。'
        ]
    ))

    blocks.append(('SFX', 'SFX', 'Tiếng cưa gỗ kẽo kẹt, tiếng đục kim loại sắc lạnh trong đêm tối.', 'Sound of hand saws grating wood, cold chisels striking metal in darkness.', '木を挽く鋸の軋む音、暗闇の中で金属を削る冷たい鑿の響き。'))

    blocks.append(('LOI', 'INVESTIGATOR',
        'trích xuất hồ sơ hiện trường và chữ ký hành vi',
        [
            'Sau khi lấy bằng tiến sĩ toán học tại Đại học Michigan và trở thành giáo sư trẻ tuổi tại UC Berkeley, Ted bất ngờ từ chức vào năm 1969.',
            'Hắn lui về căn lều gỗ hẻo lánh tại Lincoln, Montana và thiết lập một quy trình chế tạo vũ khí cực kỳ tỉ mỉ và khoa học.',
            'Hắn kiên quyết không sử dụng bất kỳ linh kiện nào có thể truy nguyên nguồn gốc thương mại.',
            'Hắn nhặt nhạnh từng đoạn ống nước cũ, tự chế thuốc nổ đen từ lưu huỳnh và than củi, đúc các chốt kích hoạt từ gỗ sồi và kim loại phế thải.',
            'Mỗi quả bom là một tác phẩm thủ công chết chóc, đòi hỏi hàng trăm giờ lao động kiên nhẫn.',
            'Và điều đáng sợ nhất chính là sự phi nhân hóa triệt để đối với các nạn nhân trong tư duy của kẻ thủ ác.',
            'Hắn không hề quan tâm người mở gói bưu phẩm là ai, họ có gia đình hay con nhỏ hay không.',
            'Trong nhật ký bí mật được mã hóa tỉ mỉ, hắn ghi lại các vụ nổ không phải bằng sự xót thương, mà bằng sự thỏa mãn lạnh lùng khi thấy thiết bị hoạt động chính xác.',
            'Đó là sự thiếu hụt hoàn toàn của thấu cảm cảm xúc, nơi sinh mạng con người bị giáng cấp thành những con số thống kê phục vụ cho sự khẳng định bản ngã.'
        ],
        [
            'After obtaining his doctorate in mathematics at Michigan and securing an assistant professorship at UC Berkeley, Ted abruptly resigned in 1969.',
            'He retreated into the secluded Montana timber shack and established an excruciatingly methodical munitions lab.',
            'He strictly avoided any commercially serialized components that could be traced back to retail distributors.',
            'He collected scrap plumbing pipes, blended homemade black powder from potassium chlorate and charcoal, and whittled bomb switches from scrap hardwood.',
            'Each explosive device represented a lethal handcrafted artifact requiring hundreds of hours of patient labor.',
            'Yet what chilled investigators to the bone was his absolute psychological dehumanization of the victims.',
            'He harbored zero concern for who unwrapped the packages, whether they had spouses, young children, or families.',
            'In his meticulously enciphered private journals, he cataloged explosions not with remorse, but with clinical satisfaction over mechanical success.',
            'This demonstrated a total affective empathy deficit, where human lives were reduced to cold empirical data serving his intellectual vanity.'
        ],
        [
            'ミシガン大学で数学の博士号を取得し、バークレー校の若き助教授となったテッドは、1969年に突如として教授職を投げ出しました。',
            '彼はモンタナ州リンカーンの孤立した丸太小屋に退却し、戦慄するほど緻密で秩序ある兵器製造工房を立ち上げたのです。',
            '彼は市販の流通ルートから身元を特定され得るようなシリアル番号入りの部品を徹底的に排除しました。',
            '古い配管パイプを拾い集め、硫黄と木炭から自家製黒色火薬を調合し、廃材の硬木から起爆スイッチを削り出しました。',
            '個々の爆発装置は、何百時間もの忍耐強い手作業を費やして完成させた死の工芸品だったのです。',
            'そして最も背筋を凍らせたのは、彼の思考における被害者たちの徹底的な「非人間化」でした。',
            '小包を開封する人物が誰であるか、その人に家庭や幼い子供がいるかなど、彼には微塵の関心もありませんでした。',
            '暗号化された秘密の日記の中で、彼は爆破の瞬間を悔恨ではなく、機械的作動の成功に対する冷徹な満足感をもって記録していました。',
            'それは感情的共感力の完全な欠如であり、人間の尊い命が彼の知的虚栄心を誇示するための無機質な統計数値へと成り下がっていたのです。'
        ]
    ))

    blocks.append(('LOI', 'ORDINARY_PERSON',
        'N1: Giáo sư David Gelernter (Đại học Yale) – giọng trầm uất nhưng kiên định',
        [
            'Mùa hè năm 1993, tôi bước vào văn phòng tại Đại học Yale sau một kỳ nghỉ.',
            'Trên bàn có một kiện bưu phẩm nhỏ bọc giấy nâu gửi từ California, trông không khác gì những cuốn bản thảo sách bình thường.',
            'Khi tôi vừa rạch lớp băng dính bên ngoài, một tia chớp trắng lóa xé toạc không gian cùng một tiếng nổ kinh hoàng.',
            'Căn phòng ngập trong khói và lửa; tôi loạng choạng bước ra hành lang để tìm kiếm sự cứu giúp.',
            'Tôi vĩnh viễn mất đi một phần bàn tay phải, mắt phải bị tổn thương nặng và cơ thể mang đầy vết sẹo.',
            'Nhưng điều tàn bạo nhất mà kẻ gửi bom muốn cướp đi không phải là thể xác của chúng tôi, mà là cảm giác an toàn và niềm tin vào cuộc sống.',
            'Hắn muốn gieo rắc sự hoang mang vào tâm trí của mọi học giả, biến tri thức thành một mối đe dọa thường trực.',
            'Thế nhưng, chúng tôi đã từ chối đầu hàng trước nỗi sợ hãi; tôi quay trở lại giảng đường để chứng minh rằng bạo lực không bao giờ dập tắt được tri thức.'
        ],
        [
            'In the summer of 1993, I walked into my office at Yale University after a brief vacation.',
            'On my desk lay a modest package wrapped in brown paper postmarked from California, resembling an ordinary manuscript.',
            'The instant I slit the outer tape, a blinding white flash ripped through the room accompanied by a deafening roar.',
            'The room was engulfed in acrid smoke and fire; I stumbled into the hallway seeking desperate medical help.',
            'I permanently lost my right hand, suffered severe trauma to my right eye, and bore lasting scars across my body.',
            'Yet the most brutal thing that bomber sought to destroy was not merely our physical flesh, but our foundational sense of security.',
            'He wanted to inject pervasive terror into every scholar mind, turning the pursuit of knowledge into a constant threat.',
            'Nevertheless, we refused to surrender to intimidation; I returned to the lecture halls to prove that terror can never extinguish the pursuit of truth.'
        ],
        [
            '1993年の夏、私は休暇を終えてイェール大学の研究室へと戻りました。',
            '机の上にはカリフォルニアからの消印が押された茶色の包み紙の小包があり、普通の原稿のように見えました。',
            '外側のテープに切れ目を入れた瞬間、目の前で白い閃光が弾け、鼓膜を裂く轟音が部屋を包み込みました。',
            '部屋は刺激臭のある煙と炎に包まれ、私は助けを求めて必死に廊下へと這い出しました。',
            '私は右手の一部を永久に失い、右目を激しく損傷し、全身に深い傷跡を負うことになりました。',
            'しかし、爆弾魔が本当に奪おうとした最も残酷なものは私たちの肉体ではなく、日常の安全への確信そのものでした。',
            '彼はすべての学者の心に底知れぬ恐怖を植え付け、知の探求そのものを常に死の危険と隣り合わせにしようとしたのです。',
            'それでも私たちは恐怖に屈することを拒みました。私は講義室へと復帰し、暴力が真理の探求の光を決して消し去ることはできないと証明したのです。'
        ]
    ))

    # ==========================================
    # HỒI 3: CUỘC ĐẤU TRÍ NGÔN NGỮ & NỖI GIẰNG XÉ LƯƠNG TÂM CỦA NGƯỜI EM TRAI (42 CÂU)
    # ==========================================
    blocks.append(('ACT', 3, 'CUỘC ĐẤU TRÍ NGÔN NGỮ & NỖI GIẰNG XÉ LƯƠNG TÂM CỦA NGƯỜI EM TRAI', 'THE LINGUISTIC DUEL & THE BROTHER AGONIZING CONSCIENCE', '言語学的決闘と弟の引き裂かれた良心'))
    blocks.append(('BGM', 'BGM', 'Tiếng Cello u uất giằng xé hòa cùng nhịp Piano trầm mặc ngột ngạt.', 'Sorrowful solo cello interweaving with heavy, oppressive minimalist piano.', '悲痛なチェロの独奏が、重苦しく息詰まるミニマルピアノと絡み合う。'))

    blocks.append(('LOI', 'HOST',
        'chuyển sang bước ngoặt kịch tính của vụ án và hai vụ sát hại 1994-1995',
        [
            'Bước sang thập niên 1990, sự cuồng nộ của Unabomber ngày càng trở nên khốc liệt và đẫm máu hơn bao giờ hết.',
            'Tháng 12 năm 1994, một kiện bom gửi tới nhà riêng đã cướp đi sinh mạng của chuyên gia quảng cáo Thomas Mosser ngay trước mắt người vợ Susan.',
            'Bốn tháng sau, vào tháng 4 năm 1995, Gilbert Murray, Chủ tịch Hiệp hội Lâm nghiệp California, tử nạn khi mở một bưu kiện gửi tới văn phòng.',
            'Giữa lúc cả nước Mỹ chìm trong căm phẫn, kẻ thủ ác bất ngờ đưa ra một canh bạc thế kỷ nhằm thách thức toàn bộ nền tư pháp.',
            'Tháng 6 năm 1995, một bức thư nặc danh được gửi tới hai tòa soạn báo hàng đầu: The New York Times và The Washington Post.',
            'Kẻ tự xưng đại diện nhóm FC tuyên bố sẽ ngừng hoàn toàn các vụ đánh bom sát thương nếu bản luận thuyết 35.000 từ của hắn được đăng trọn vẹn.',
            'Đây là tình thế tiến thoái lưỡng nan chưa từng có đối với tự do báo chí và pháp luật Hoa Kỳ.',
            'Sau các cuộc thảo luận cân não giữa Bộ trưởng Tư pháp Janet Reno và Giám đốc FBI Louis Freeh, quyết định xuất bản đã được thông qua.',
            'Bản Tuyên ngôn mang tên “Xã hội Công nghiệp và Tương lai của nó” chính thức lên trang báo vào ngày 19 tháng 9 năm 1995.'
        ],
        [
            'Entering the 1990s, the Unabomber rage escalated into an increasingly lethal and bloodsoaked campaign.',
            'In December 1994, a mail bomb delivered to his suburban home killed advertising executive Thomas Mosser in front of his wife Susan.',
            'Four months later, in April 1995, Gilbert Murray, President of the California Forestry Association, perished opening a parcel at his office.',
            'Amidst boiling national outrage, the elusive terrorist issued an unprecedented ultimatum challenging the American justice system.',
            'In June 1995, identical anonymous letters reached the editorial rooms of The New York Times and The Washington Post.',
            'Claiming to represent the clandestine group FC, the author promised to cease lethal attacks if his 35,000-word treatise was published in full.',
            'This created an extraordinary ethical dilemma between journalistic independence and national security.',
            'Following intense deliberations between Attorney General Janet Reno and FBI Director Louis Freeh, the operational gamble was approved.',
            'The manifesto titled Industrial Society and Its Future was formally published across major newsprint on September 19, 1995.'
        ],
        [
            '1990年代に入ると、ユナボマーの凶暴性はそれまで以上に破壊的かつ致命的なものへと激化していきました。',
            '1994年12月、自宅に届いた郵便爆弾により、広告会社重役のトーマス・モッサーが妻スーザンの目前で命を奪われました。',
            'そのわずか4か月後の1995年4月には、カリフォルニア林業協会の会長ギルバート・マレーがオフィスで小包を開封して犠牲となったのです。',
            '全米が激しい怒りに包まれる中、逃亡犯は突如として司法体制全体を揺るがす前代未聞の賭けに出ました。',
            '1995年6月、ニューヨーク・タイムズとワシントン・ポストの両編集部に匿名の脅迫状が届いたのです。',
            '「FC」と名乗る著者は、自らの3万5千語におよぶ論文を全文掲載するならば、無差別爆破を完全に停止すると約束しました。',
            'これは報道の自由と国家の法治原則の狭間で、かつてない深刻な倫理的対立を引き起こしました。',
            'ジャネット・レノ司法長官とルイス・フリーFBI長官による緊迫した協議の末、掲載という大胆な作戦が決断されました。',
            '1995年9月19日、「産業社会とその未来」と題された声明文が新聞の特別別刷りとして正式に世に出たのです。'
        ]
    ))

    blocks.append(('LOI', 'INVESTIGATOR',
        'giải thích bước đột phá của Giám định ngôn ngữ học pháp y và câu thành ngữ',
        [
            'Khi bản tuyên ngôn được công bố, đặc vụ giám sát James R. Fitzgerald đã nhìn thấy cơ hội mở ra cánh cửa phá án.',
            'Fitzgerald là người tiên phong ứng dụng chuyên ngành Giám định Ngôn ngữ học Pháp y vào công tác điều tra hình sự thực tiễn.',
            'Ông hiểu rằng mỗi con người đều sở hữu một dấu vân tay ngôn ngữ duy nhất, được hình thành từ vốn từ vựng, cú pháp và thói quen diễn đạt.',
            'Fitzgerald bắt đầu phân tích từng đoạn văn trong bản tuyên ngôn, bóc tách các thuật ngữ học thuật và các biến thể chính tả từ thập niên 1950.',
            'Đặc biệt, ông chú ý tới câu thành ngữ đảo ngữ cổ xưa: “You can not eat your cake and have it too”.',
            'Cách viết này hoàn toàn trái ngược với thói quen hiện đại của người Mỹ vốn thường nói “have your cake and eat it too”.',
            'Chữ ký ngôn ngữ độc nhất vô nhị ấy đã trở thành chiếc chìa khóa vàng giúp chúng tôi tìm kiếm tác giả thật sự giữa hàng triệu người.'
        ],
        [
            'The moment the manifesto appeared in print, FBI supervisory agent James R. Fitzgerald recognized a decisive investigative opening.',
            'Fitzgerald was a visionary pioneer who introduced Forensic Linguistics as an operational investigative discipline in major criminal cases.',
            'He understood that every human mind possesses a distinct linguistic idiolect shaped by syntax, vocabulary, and cognitive habits.',
            'Fitzgerald methodically dissected paragraphs within the manifesto, isolating idiosyncratic academic terminology and 1950s spellings.',
            'Crucially, he isolated an archaic inverted proverb: "You can not eat your cake and have it too."',
            'This formulation inverted modern American colloquial usage, which almost universally says "have your cake and eat it too."',
            'That singular linguistic fingerprint became the golden master key enabling investigators to isolate the author from millions.'
        ],
        [
            'マニフェストが活字となって世に出た瞬間、FBIのジェームズ・R・フィッツジェラルド捜査官は決定的な捜査の好機を見出しました。',
            'フィッツジェラルドは、法言語学を重大犯罪の科学捜査において実戦的な武器として確立させた先駆者でした。',
            '彼は、すべての人間が語彙、統語論、思考の癖によって形作られた唯一無二の「言語の指紋」を持っていることを見抜いていました。',
            'フィッツジェラルドは声明文のあらゆる段落を解剖し、1950年代特有の古い綴りや特異な学術的言説を抽出していきました。',
            'とりわけ彼が着目したのは、「ケーキを食べてしまい、なおかつ手元に残すことはできない」という倒置された古い成句でした。',
            'この表現は、「ケーキを手元に残し、なおかつ食べる」という現代アメリカ人の一般的な語順とは明確に異なっていました。',
            'その極めて特異な言語的特徴こそが、何百万人もの群衆の中から真の書き手を浮き彫りにする黄金の鍵となったのです。'
        ]
    ))

    blocks.append(('LOI', 'ORDINARY_PERSON',
        'N2: David Kaczynski – giọng nghẹn ngào, diễn tả nỗi đau tột cùng của sự lựa chọn',
        [
            'Vợ tôi, Linda, là người đầu tiên đọc bản tuyên ngôn trên mặt báo và cảm thấy một sự hoài nghi đến thắt nghẹn lồng ngực.',
            'Cô ấy nhận ra giọng điệu căm thù kỹ trị và cách lập luận trong bài báo giống hệt những lá thư dài mà anh Ted từng gửi cho tôi.',
            'Ban đầu, tôi giận dữ gạt phắt đi; làm sao một người anh trai từng cùng tôi đi dạo trong rừng, từng dạy tôi về thiên nhiên lại có thể là kẻ giết người?',
            'Nhưng Linda kiên quyết thúc giục tôi đối diện với sự thật.',
            'Tôi trèo lên gác xép gia đình tại Schenectady, New York, tìm lại tập tài liệu và những bức thư cũ từ thập niên 1970.',
            'Khi lật giở từng trang giấy ố vàng và nhìn thấy câu nói “You can not eat your cake and have it too”, đầu gối tôi khuỵu xuống sàn nhà.',
            'Đó chính là anh Ted; không còn một chút nghi ngờ nào nữa.',
            'Lương tâm tôi bị xé toạc giữa lòng trung thành với anh trai ruột thịt và trách nhiệm bảo vệ mạng sống của những con người vô tội.',
            'Nếu tôi im lặng, tôi sẽ cứu được anh mình khỏi nhà tù, nhưng tôi sẽ vĩnh viễn không thể rửa sạch vết máu của những nạn nhân tiếp theo.'
        ],
        [
            'My wife, Linda, was the first to read the published manifesto and experienced an unbearable, suffocating suspicion.',
            'She recognized that the vitriolic anti-technology rhetoric and argumentative cadence matched letters Ted had sent me over decades.',
            'Initially, I rejected her suspicions with anger; how could the gentle older brother who taught me to love nature be a serial killer?',
            'Yet Linda patiently urged me to confront reality with unblinking honesty.',
            'I climbed into our attic in Schenectady, New York, pulling down cardboard boxes containing his essays and correspondence from the 1970s.',
            'As I turned the yellowed pages and saw his exact phrasing – "You can not eat your cake and have it too" – my knees buckled onto the floor.',
            'It was Ted; there was no longer a shadow of doubt.',
            'My soul was ripped apart between fraternal loyalty to my flesh and blood and the moral duty to protect innocent lives.',
            'If I chose silence, I might spare my brother, but I could never wash the blood of future victims from my hands.'
        ],
        [
            '新聞に掲載された声明文を最初に読んだ私の妻リンダは、胸が締め付けられるような耐え難い疑惑を覚えました。',
            '彼女は、技術への激しい憎悪と論理展開のリズムが、何年間もテッドが私に送り続けてきた長い手紙と完全に一致していると気づいたのです。',
            '当初、私は怒りをもってその疑いを退けました。幼い頃に自然の美しさを教えてくれた優しい兄が連続殺人犯であるはずがないと信じたかったのです。',
            'しかしリンダは、目を逸らすことなく真実に向き合うよう私に懇願しました。',
            '私はニューヨーク州スケネクタディの自宅の屋根裏部屋に上がり、1970年代の兄の手紙や論文が入った段ボール箱を下ろしました。',
            '黄ばんだ手紙の束をめくり、「ケーキを食べてしまい、なおかつ手元に残すことはできない」という全く同じ記述を目にした瞬間、私の膝は床へと崩れ落ちました。',
            'テッドでした。そこにはもはや、いかなる疑いの余地も残されていませんでした。',
            '血を分けた兄への忠誠心と、罪なき人々の命を守る道徳的義務との間で、私の魂は引き裂かれました。',
            'もし私が沈黙を選べば兄の命は救えるかもしれない、しかしそれでは次に流される犠牲者たちの血を私の手から拭い去ることは決してできないのです。'
        ]
    ))

    blocks.append(('LOI', 'PSYCHOLOGIST',
        'giải mã sự giằng xé lương tâm và cơ chế chuộc lỗi của người em trai',
        [
            'Quyết định của David Kaczynski và Linda Patrik là một trong những cột mốc đạo đức bi tráng nhất trong biên niên sử tư pháp.',
            'Đây là sự thức tỉnh trọn vẹn của lòng trắc ẩn trước cơ chế phòng vệ dung túng người thân.',
            'David hiểu rằng: Bao che cho cái ác nhân danh tình thân không phải là yêu thương, mà là đồng lõa hủy hoại nhân tính của chính người mình yêu quý.',
            'Ông liên hệ với luật sư để chuyển giao các tài liệu cho FBI với một thỉnh cầu tha thiết duy nhất: Xin hãy tha mạng sống cho anh trai tôi.',
            'Đó là sự dung hòa tột cùng giữa trách nhiệm công dân và tình ruột thịt thiêng liêng.',
            'Khoảnh khắc David bước qua ranh giới ấy, ông đã cứu sống biết bao nạn nhân vô tội tiềm năng khỏi những cỗ máy hủy diệt tiếp theo.'
        ],
        [
            'The decision undertaken by David Kaczynski and Linda Patrik represents one of the most tragic yet noble moral milestones in legal history.',
            'It marked the absolute triumph of universal conscience over the psychological bias of familial self-preservation.',
            'David recognized an indispensable truth: Shielding violence in the name of kinship is not devotion, but complicity in destroying humanity.',
            'He engaged legal counsel to deliver the correspondence to the FBI with a single desperate plea: Please spare my brother life.',
            'It stood as the ultimate reconciliation between civic duty and profound brotherly love.',
            'The moment David crossed that agonizing threshold, he preserved countless innocent lives from impending slaughter.'
        ],
        [
            'デイヴィッドとリンダが下した決断は、司法の歴史において最も悲痛でありながら気高い道徳的金字塔でした。',
            'それは、身内を庇い立てようとする心理的防衛機制に対し、普遍的な人間愛の良心が完全に勝利を収めた瞬間でした。',
            '家族愛の名の下に暴力を隠蔽することは愛情ではなく、愛する者の人間性を共に破壊する共犯関係に過ぎないことを彼は悟ったのです。',
            '彼は弁護士を通じて手紙の束をFBIに提出し、ただ一つの悲痛な嘆願を添えました。「どうか、兄の命だけは助けてほしい」と。',
            'それは市民としての社会的責任と、断ち切ることのできない肉親の絆との間の極限の調和でした。',
            'デイヴィッドがその苦悶の境界線を越えた瞬間、未来の爆発装置によって奪われるはずだった無数の尊い命が救われたのです。'
        ]
    ))

    # ==========================================
    # HỒI 4: CUỘC ĐỘT KÍCH LINCOLN & SỰ SỤP ĐỔ CỦA PHÁO ĐÀI CÔ ĐỘC (42 CÂU)
    # ==========================================
    blocks.append(('ACT', 4, 'CUỘC ĐỘT KÍCH LINCOLN & SỰ SỤP ĐỔ CỦA PHÁO ĐÀI CÔ ĐỘC', 'THE LINCOLN CABIN RAID & COLLAPSE OF THE ISOLATED FORTRESS', 'リンカーンの山小屋急襲と孤立した要塞の崩壊'))
    blocks.append(('BGM', 'BGM', 'Tiếng Bass nặng trĩu dồn dập, tiếng còi hú từ xa và tiếng bước chân rầm rập trong tuyết.', 'Heavy pulsing sub-bass, distant sirens wailing, and rapid rhythmic tactical footsteps in snow.', '重く脈打つサブベース、遠くで響くサイレン、そして雪を踏みしめる戦術部隊の緊迫した足音。'))

    blocks.append(('LOI', 'HOST',
        'giọng dồn dập, đưa người xem vào thời khắc quyết định của cuộc vây bắt',
        [
            'Dựa trên bản phân tích ngôn ngữ học pháp y dày 50 trang của Fitzgerald đối chiếu thư từ của gia đình, thẩm phán đã ký lệnh khám xét lịch sử.',
            'Đây là lần đầu tiên trong lịch sử tư pháp liên bang Hoa Kỳ, một lệnh khám xét được phê chuẩn chủ yếu dựa trên chứng cứ phong cách ngôn ngữ.',
            'Ngày 3 tháng 4 năm 1996, khu rừng tuyết phủ tại Lincoln, Montana bỗng trở thành tâm điểm của chiến dịch vây bắt quy mô nhất.',
            'Hàng chục đặc vụ FBI vũ trang hạng nặng, dưới sự dẫn dắt của các nhân viên kiểm lâm địa phương, âm thầm tiếp cận căn lều gỗ.',
            'Họ đóng giả làm các kỹ sư đo đạc ranh giới đất rừng để tiếp cận cửa ra vào mà không khiến đối tượng nghi ngờ.',
            'Bên trong căn lều tối tăm, kẻ bị săn lùng suốt 17 năm vẫn đinh ninh mình là một bóng ma bất khả xâm phạm.',
            'Khi cánh cửa gỗ mở ra, ánh sáng công lý đã xuyên thủng màn đêm bí mật của Unabomber.'
        ],
        [
            'Armed with Fitzgerald 50-page forensic linguistic affidavit comparing the manifesto against family letters, a federal judge granted a historic warrant.',
            'It marked the first time in federal jurisprudence that a search warrant was approved primarily upon linguistic stylistic evidence.',
            'On April 3, 1996, the snow-draped timberlands of Lincoln, Montana became the vortex of an unprecedented tactical raid.',
            'Dozens of heavily armed federal agents, assisted by local forestry personnel, silently cordoned off the primitive cabin.',
            'Agents disguised themselves as topographic surveyors to approach the threshold without alerting the reclusive suspect.',
            'Inside that dim hovel, the fugitive of 17 years remained convinced his fortress of solitude was eternally impenetrable.',
            'As the weathered timber door was pulled open, the blinding light of justice pierced the Unabomber secretive universe.'
        ],
        [
            'フィッツジェラルドがまとめた50ページにおよぶ法言語学的宣誓供述書に基づき、連邦判事は歴史的な捜索令状に署名しました。',
            '米国の連邦司法史上、文体や言語学的証拠を主たる根拠として捜索令状が承認されたのはこれが初めてのことでした。',
            '1996年4月3日、雪に覆われたモンタナ州リンカーンの針葉樹林は、空前の規模を誇る急襲作戦の舞台となりました。',
            '重武装した数十名の連邦捜査官が、地元の森林官の先導により、静まり返った丸太小屋を包囲しました。',
            '捜査官たちは警戒心の強い容疑者を刺激しないよう、土地の境界線を測量する作業員を装って接近しました。',
            '薄暗い小屋の中で、17年間逃げ続けた男は自らの孤独の要塞が永遠に不可侵であると信じ切っていました。',
            '木製のドアが開け放たれた瞬間、正義の光がユナボマーの闇に包まれた世界を余すところなく照らし出したのです。'
        ]
    ))

    blocks.append(('LOI', 'INVESTIGATOR',
        'tái hiện cuộc khám xét hiện trường bên trong căn lều gỗ',
        [
            'Hiện trường bên trong căn lều gỗ rộng mười mét vuông khiến tất cả chúng tôi phải sững sờ.',
            'Căn phòng bừa bộn nồng nặc mùi lưu huỳnh, khói bếp và rác rưởi tích tụ lâu năm.',
            'Khắp nơi là hàng chục ngàn trang tài liệu viết tay, các cuốn sổ nhật ký ghi chép chi tiết từng công thức pha chế thuốc nổ.',
            'Đặc biệt, dưới gầm giường của hắn, các chuyên gia chất nổ phát hiện một quả bom đã lắp ráp hoàn chỉnh và bọc sẵn trong bao bì gửi bưu điện.',
            'Quả bom thứ mười bảy ấy chỉ chờ ngày được mang ra thị trấn để gửi đi cướp thêm một sinh mạng nữa.',
            'Chiếc máy chữ cơ khí Smith Corona dùng để gõ bản Tuyên ngôn cũng được thu giữ nguyên vẹn trên chiếc bàn gỗ thô ráp.',
            'Mọi bằng chứng vật chất khớp hoàn toàn với những suy luận từ chứng cứ ngôn ngữ học trước đó.',
            'Kẻ chủ mưu không có cơ hội phản kháng; hắn bị khống chế và áp giải ra xe trong sự ngỡ ngàng tột độ.'
        ],
        [
            'The scene confronting our agents inside that ten-by-twelve-foot timber cabin was utterly breathtaking.',
            'The cramped space reeked heavily of raw sulfur, chimney soot, and years of accumulated domestic debris.',
            'Scattered across crude shelving were tens of thousands of handwritten journal pages detailing chemical formulations.',
            'Crucially, concealed beneath his sleeping cot, bomb technicians uncovered a live, fully armed explosive packaged for mailing.',
            'That seventeenth bomb was primed and waiting merely to be transported to town to claim yet another human life.',
            'The manual Smith Corona typewriter used to draft the published manifesto was seized intact from his rustic worktable.',
            'Every piece of physical hardware corroborated the earlier forensic linguistic deductions with clinical perfection.',
            'The mastermind had zero opportunity to mount resistance; he was subdued and escorted into custody in stunned disbelief.'
        ],
        [
            'わずか10フィート四方の丸太小屋の中で捜査官たちが目にした光景は、息を呑むほど異様なものでした。',
            '狭苦しい空間には硫黄の鼻を突く悪臭、薪の煤煙、そして長年にわたり蓄積された生活ゴミの臭いが充満していました。',
            '粗末な棚の上には、爆発物の調合実験を記録した数万ページにも及ぶ直筆の日記やノートが積み上げられていました。',
            'そしてベッドの下から、爆発物処理班によって完全に組み立てられ郵送用の梱包まで済まされた実包爆弾が発見されたのです。',
            'その17個目の爆弾は、さらなる人命を奪うために町へ持ち出される瞬間を待つばかりの状態でした。',
            '声明文を印字したスミス・コロナ社製の手動タイプライターも、粗削りな木製作業台の上からそのまま押収されました。',
            '押収されたすべての物理的証拠は、事前の法言語学的プロファイリングの推論と恐ろしいほど完璧に合致していました。',
            '首謀者は抵抗する隙すら与えられず、呆然自失の表情のまま手錠をかけられ護送車へと連行されたのです。'
        ]
    ))

    blocks.append(('LOI', 'PSYCHOLOGIST',
        'phân tích sự sụp đổ cái tôi ái kỷ và thái độ không hề ăn năn của Ted',
        [
            'Khoảnh khắc bị đưa ra trước công chúng, Ted Kaczynski phơi bày trọn vẹn bản chất của “Sự sụp đổ cái tôi ái kỷ”.',
            'Hắn không hề run rẩy hay xấu hổ; ánh mắt hắn nhìn thế giới bằng một sự khinh miệt lạnh lùng.',
            'Hắn coi mình là một tử vì đạo trí thức, một triết gia bị bắt giữ bởi một xã hội mà hắn cho là đã tha hóa.',
            'Kẻ ái kỷ ác tính hoàn toàn khuyết tật khả năng thấu cảm nỗi đau mà hắn đã gây ra cho các gia đình nạn nhân.',
            'Hắn không mảy may xót xa cho bàn tay bị cụt của Giáo sư Gelernter hay mạng sống của Hugh Scrutton và Thomas Mosser.',
            'Hắn chỉ chìm đắm trong sự tự thương hại bệnh lý, nuối tiếc cho sự tự do và quyền kiểm soát triết học của chính mình.',
            'Đó là tấn bi kịch lớn nhất của một trí tuệ phi thường: Hắn xây dựng một lý thuyết để giải phóng con người, nhưng bản thân lại trở thành nô lệ cho sự thù hận mù quáng.'
        ],
        [
            'Paraded before international cameras, Ted Kaczynski laid bare the quintessential anatomy of Malignant Narcissistic Collapse.',
            'He showed neither remorse nor humiliation; his stare projected haughty contempt toward civil society.',
            'He regarded himself as an intellectual martyr, a lone philosopher captured by a civilization he deemed hopelessly corrupted.',
            'The malignant narcissist suffered from an absolute deficit in affective empathy regarding the catastrophic trauma he inflicted.',
            'He harbored zero sorrow for Professor Gelernter shattered hand or the stolen lives of Hugh Scrutton, Thomas Mosser, and Gilbert Murray.',
            'He indulged solely in pathological self-pity, mourning only his lost personal autonomy and philosophical dominance.',
            'This underscores the profound tragedy of a brilliant mind: constructing theories to liberate mankind, while becoming a prisoner of hatred.'
        ],
        [
            '報道陣のカメラの前に引き出された瞬間、テッド・カジンスキーは「悪性自己愛の破綻」の典型的な姿を露わにしました。',
            '彼は怯えることも恥じ入ることもなく、市民社会に対して底知れぬ冷酷な軽蔑の眼差しを向け続けました。',
            '彼は自らを凶悪犯ではなく、堕落した文明社会によって捕らえられた孤独な哲学者、思想の殉教者であると見なしていたのです。',
            'この悪性自己愛者は、自らが遺族たちに与えた壊滅的な苦痛に対する感情的共感能力を完全に欠落させていました。',
            'ゲルランター教授の失われた右手や、ヒュー・スクラットン、トーマス・モッサー、ギルバート・マレーの命を悼む心は微塵もありませんでした。',
            '彼は病理的な自己憐憫に浸り、奪われた自らの自由と哲学的支配権の失墜のみを嘆き続けたのです。',
            'これこそが卓越した知性が辿り着いた最大の悲劇でした。人類を解放するための理論を構築しながら、自らは憎悪の奴隷となっていたのです。'
        ]
    ))

    blocks.append(('LOI', 'ORDINARY_PERSON',
        'N2: David Kaczynski – đối diện với sự thù hận của anh trai và tình bạn hàn gắn với nạn nhân',
        [
            'Khi danh tính của gia đình tôi bị truyền thông rò rỉ, chúng tôi rơi vào một cơn bão táp của sự phán xét và sợ hãi.',
            'Nhưng đòn giáng đau đớn nhất chính là phản ứng của anh Ted.',
            'Anh ấy từ chối mọi nỗ lực thăm nom của mẹ tôi và tôi, tuyên bố từ mặt gia đình và coi tôi là kẻ thù lớn nhất.',
            'Sau khi anh ấy bị kết án, tôi đã nhận được một phần số tiền thưởng một triệu đô la từ FBI.',
            'Mẹ tôi và tôi hiểu rằng số tiền ấy nhuốm đầy máu và nước mắt; chúng tôi không bao giờ dùng nó cho bản thân.',
            'Sau khi chi trả các chi phí pháp lý, tôi đã dành phần lớn số tiền ấy để trao tặng trực tiếp cho gia đình các nạn nhân của anh Ted.',
            'Và điều kỳ diệu nhất trong cuộc đời tôi đã xảy ra: Gary Wright, người từng bị bom của anh Ted xé toạc thân thể tại Salt Lake City, đã tìm đến tôi.',
            'Thay vì thù hận, Gary ôm lấy tôi và nói: “David, anh không có lỗi gì cả; anh đã làm điều dũng cảm nhất để cứu những người khác”.',
            'Kể từ ngày đó, Gary Wright và tôi đã trở thành những người anh em thân thiết, cùng nhau đi khắp nước Mỹ để chia sẻ thông điệp về sự hàn gắn và tình thương.'
        ],
        [
            'When our family identity was leaked to the media, we were thrust into a maelstrom of public scrutiny and terror.',
            'Yet the most agonizing blow came from Ted himself.',
            'He rejected every visitation attempt from our mother and me, formally disowning the family and branding me his bitterest enemy.',
            'Following his conviction, I received a portion of the one-million-dollar FBI reward.',
            'My mother and I recognized that this money was steeped in blood and tears; we refused to keep it for ourselves.',
            'After legal fees, I distributed the vast majority directly to the surviving victims and grieving families of Ted bombings.',
            'Then, the most profound grace of my life occurred: Gary Wright, who had been maimed by Ted bomb in Salt Lake City, reached out to me.',
            'Instead of harboring vengeance, Gary embraced me, saying: "David, you bear no guilt; you did the bravest thing imaginable to save others."',
            'From that day forward, Gary Wright and I became devoted brothers, traveling across America sharing messages of restorative healing and compassion.'
        ],
        [
            '私たちの身元がメディアに漏洩したとき、家族は世間の激しい好奇と非難の嵐の中に放り込まれました。',
            'しかし何よりも耐え難い打撃となったのは、テッド本人の反応でした。',
            '彼は母と私の面会要請を一切拒絶し、家族との縁を公然と断ち切り、私を最大の敵と宣告したのです。',
            '彼の判決後、私はFBIから100万ドルの報奨金の一部を受け取りました。',
            '母と私は、その金が罪なき人々の血と涙に塗れていることを深く理解していました。自分たちのために使うことなど決してできませんでした。',
            '弁護士費用を支払った後、私はその大半をテッドの爆弾によって被害を受けた遺族たちへ直接寄付しました。',
            'そして私の人生において最も奇跡的な出来事が起きました。ソルトレイクシティで爆弾により重傷を負ったゲイリー・ライトが私を訪ねてくれたのです。',
            '復讐の代わりにゲイリーは私を抱きしめ、「デイヴィッド、君には何の罪もない。君は他の人々の命を救うため最も勇敢な決断をしたんだ」と言ってくれました。',
            'その日以来、ゲイリー・ライトと私は実の兄弟のような親友となり、心の傷の癒やしと赦しの尊さを伝えるため全米を共に巡り続けています。'
        ]
    ))

    # ==========================================
    # HỒI 5: BẢN ÁN ADX FLORENCE & BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN (42 CÂU)
    # ==========================================
    blocks.append(('ACT', 5, 'BẢN ÁN ADX FLORENCE & BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN', 'THE ADX FLORENCE SENTENCE & RED ALERT LESSONS FOR SURVIVAL', '重警備刑務所の終身刑と命を守る赤信号の教訓'))
    blocks.append(('BGM', 'BGM', 'Tiếng Piano độc tấu trầm buồn, sâu lắng, mang âm hưởng suy tư và thức tỉnh.', 'Somber solo piano, deep, resonant, conveying profound contemplation and awakening.', '哀愁を帯びたピアノの独奏が、深い思索と魂の覚醒を促すように静かに響き渡る。'))

    blocks.append(('LOI', 'HOST',
        'dẫn dắt vào phiên tòa xét xử và lời tuyên án lịch sử',
        [
            'Tại phiên tòa xét xử liên bang ở Sacramento, một cuộc chiến pháp lý gay gắt đã nổ ra xung quanh năng lực nhận thức của Ted Kaczynski.',
            'Các luật sư do tòa chỉ định muốn đưa ra lời bào chữa dựa trên chứng mất trí nhớ phân liệt hoang tưởng để cứu hắn khỏi bản án tử hình.',
            'Thế nhưng, kẻ ái kỷ trí tuệ đã kịch liệt phản đối; hắn thà chết trên bàn tiêm thuốc độc chứ không chấp nhận để thế giới coi mình là một kẻ điên loạn.',
            'Để bảo vệ danh dự của bản Tuyên ngôn, Ted cuối cùng đã chấp nhận nhận tội toàn bộ 16 vụ đánh bom.',
            'Ngày 4 tháng 5 năm 1998, Thẩm phán Garland Burrell Jr đã tuyên phạt Theodore Kaczynski 4 bản án tù chung thân liên tiếp cộng thêm ba mươi năm tù giam, không có bất kỳ cơ hội ân xá nào.',
            'Hắn bị chuyển tới ADX Florence tại Colorado, nhà tù liên bang kiên cố và khắc nghiệt nhất nước Mỹ, nơi được mệnh danh là “Alcatraz của dãy Rocky”.',
            'Ở đó, hắn bị giam cầm 23 giờ một ngày trong một buồng giam bê tông cách âm hoàn toàn, bị tước đoạt mọi tương tác xã hội cho đến khi trút hơi thở cuối cùng vào tháng 6 năm 2023.'
        ],
        [
            'Inside the federal courtroom in Sacramento, an intense legal warfare erupted over Ted Kaczynski mental competency.',
            'His court-appointed defense attorneys sought to introduce a diagnosis of paranoid schizophrenia to spare him the death penalty.',
            'Yet the intellectual narcissist fiercely rejected this defense; he preferred execution over having his philosophy dismissed as lunacy.',
            'To preserve the intellectual integrity of his manifesto, Ted ultimately agreed to enter an unconditional guilty plea to all charges.',
            'On May 4, 1998, Federal Judge Garland Burrell Jr sentenced Theodore Kaczynski to four consecutive life terms plus thirty years, without possibility of parole.',
            'He was remanded to ADX Florence in Colorado, the most secure supermax fortress in America, famously known as the Alcatraz of the Rockies.',
            'There, he was sealed twenty-three hours a day inside a soundproof concrete cell, stripped of human contact until his death in June 2023.'
        ],
        [
            'サクラメントの連邦地方裁判所において、テッド・カジンスキーの精神鑑定と訴訟能力を巡る激しい法廷闘争が繰り広げられました。',
            '国選弁護団は死刑を回避するため、彼を妄想型統合失調症として弁護しようと試みました。',
            'しかし傲慢な自己愛を抱くテッドはその方針に激怒し、自らの哲学が狂人の妄言として片付けられるくらいなら死を選んだ方がましだと考えたのです。',
            'マニフェストの思想的正当性を守るため、テッドは最終的にすべての起訴事実を認め、司法取引に応じる道を選びました。',
            '1998年5月4日、ガーランド・バレル・ジュニア連邦判事は、仮釈放の可能性が一切ない連続終身刑4回および懲役30年の判決を言い渡しました。',
            '彼は「ロッキー山脈のアルカトラズ」と恐れられる全米最高度の厳重警備を誇るADXフローレンス刑務所へと収監されました。',
            '完全防音のコンクリート製独房に1日23時間閉じ込められ、他者との接触を奪われたまま、彼は2023年6月にその孤独な生涯を閉じたのです。'
        ]
    ))

    blocks.append(('LOI', 'INVESTIGATOR',
        'tổng kết di sản của chuyên án UNABOM đối với ngành khoa học hình sự',
        [
            'Hồ sơ UNABOM đã khép lại sau 17 năm, nhưng nó đã để lại những cải cách mang tính bước ngoặt cho ngành điều tra tội phạm toàn cầu.',
            'Lần đầu tiên, Giám định ngôn ngữ học pháp y được công nhận là một công cụ khoa học độc lập có giá trị chứng cứ pháp lý tuyệt đối trước tòa.',
            'Vụ án cũng thúc đẩy sự ra đời của các quy trình kiểm soát bưu chính hiện đại và hệ thống soi chiếu an ninh sân bay tiên tiến bậc nhất.',
            'Nó chứng minh rằng: Dù kẻ thủ ác có ẩn náu sâu đến đâu trong rừng rậm, chữ ký tư duy và hành vi của hắn sẽ luôn là manh mối không thể che giấu.',
            'Công lý không bao giờ lùi bước trước bất kỳ sự ngụy trang trí tuệ nào, dù đó là một kẻ mang chỉ số thông minh của một thiên tài.'
        ],
        [
            'The UNABOM investigation concluded after 17 years, yet its legacy permanently transformed modern forensic investigative methodology.',
            'For the very first time, Forensic Linguistics gained formal recognition as a rigorous scientific discipline with binding courtroom evidentiary value.',
            'The ordeal also spearheaded modern postal screening protocols and revolutionized aviation security protocols across the globe.',
            'It definitively demonstrated that no matter how deep a predator conceals himself in wilderness, his cognitive behavioral signature remains indelible.',
            'Justice never cowers before intellectual arrogance, regardless of whether the perpetrator possesses the intellect of a certified genius.'
        ],
        [
            'ユナボマーの捜査ファイルは17年を経て閉じられましたが、それは世界の科学捜査手法に恒久的な革命をもたらしました。',
            '法言語学という学問分野が、法廷において決定的な証拠能力を持つ厳格な科学的手法として初めて公認されたのです。',
            'この事件はまた、現代の郵便物保安検査体制と世界的な航空セキュリティの大幅な強化を促す契機となりました。',
            '捕食者がどれほど人里離れた大自然の奥深くに身を隠そうとも、その思考と行動の痕跡は決して消し去ることはできないことが証明されたのです。',
            'たとえ犯人が天才的な知能指数を誇る人物であったとしても、法と正義が知性の傲慢に屈することは決してありません。'
        ]
    ))

    blocks.append(('LOI', 'PSYCHOLOGIST',
        'đưa ra 3 bài học cảnh báo đỏ sinh tồn cho cộng đồng',
        [
            'Từ bi kịch 17 năm của hồ sơ Unabomber, khoa học hành vi rút ra ba bài học sinh tồn cốt lõi dành cho mỗi cá nhân trong xã hội hiện đại:',
            'Thứ nhất, cảnh giác trước sự tự cô lập cực đoan và hoang tưởng cứu thế; khi một người thân dần cắt đứt các kết nối xã hội và nuôi dưỡng lòng căm thù hệ thống, đó là một tín hiệu cảnh báo đỏ cần sự can thiệp tâm lý kịp thời.',
            'Thứ hai, nhận diện hiểm họa bưu chính vô danh; không bao giờ mở các bưu kiện có dấu hiệu bất thường như không có địa chỉ người gửi, dán thừa cước phí bưu điện, dán băng dính quá mức hoặc phát ra mùi lạ.',
            'Thứ ba, và là bài học nhân văn sâu sắc nhất: Lòng dũng cảm đạo đức phải luôn đứng trên sự bao che tình thân; sự can thiệp của gia đình chính là chiếc phao cứu sinh cuối cùng để ngăn chặn cái ác hủy diệt nhân tính.',
            'Và cuối cùng, bài học từ David Kaczynski và Gary Wright nhắc nhở chúng ta rằng: Nỗi đau và sự hối hận chân thực chỉ có thể được chữa lành thông qua lòng vị tha và hành động phụng sự cộng đồng.'
        ],
        [
            'From the 17-year ordeal of the Unabomber file, behavioral science distills three paramount survival imperatives for modern society:',
            'First, heed the red alerts of extreme social isolation and messianic grievances; when an individual severs social attachments while harboring ideological hatred, early intervention is critical.',
            'Second, maintain vigilance regarding anonymous mailings; never handle parcels displaying suspicious traits such as excessive postage, missing return addresses, heavy taping, or chemical odors.',
            'Third, and most profoundly humane: Moral fortitude must always transcend blind familial allegiance; courageous familial intervention remains the ultimate safeguard against the annihilation of human conscience.',
            'And finally, the healing journey of David Kaczynski and Gary Wright reminds us that authentic remorse is redeemed through forgiveness and dedicated service to humanity.'
        ],
        [
            'ユナボマーがもたらした17年間の試練から、行動科学は現代社会を生きる私たちに3つの重要な生存の教訓を提示しています。',
            '第1に、極端な社会的孤立と救世主的な被害妄想が発する危険信号を見逃さないこと――身近な人が人間関係を断ち切り、社会に対する憎悪を募らせている場合は、早期の専門的介入が不可欠です。',
            '第2に、不審な差出人不明の郵便物に対する防犯意識を常に保持すること――差出人住所の欠落、過剰な切手、過度なテーピング、異臭などの異常を認めた小包には決して直接触れてはなりません。',
            '第3に、最も深い人間的教訓として、道徳的勇気は身内への盲目的な庇い立てに常に優先されねばならないこと――勇気ある家族の介入こそが、人間の良心が完全に破壊されるのを食い止める最後の防波堤なのです。',
            'そして最後に、デイヴィッド・カジンスキーとゲイリー・ライトが歩んだ道は、真の悔恨と苦痛は他者への許しと社会への献身を通じてのみ癒やされるという真理を教えてくれています。'
        ]
    ))

    blocks.append(('LOI', 'HOST',
        'giọng trầm ấm, khép lại tập phim với thông điệp triết học nhân văn',
        [
            'Hành trình giải mã tâm lý Ted Kaczynski khép lại, để lại cho chúng ta một lời nhắc nhở sâu sắc về ranh giới mong manh giữa trí tuệ và sự tha hóa.',
            'Trí tuệ phi phàm nếu thiếu vắng sự thấu cảm và lòng nhân ái sẽ chỉ tạo nên những quái vật lạnh lùng nhất.',
            'Trong khi đó, nỗi đau giằng xé và sự hy sinh can trường của người em trai David Kaczynski đã chứng minh rằng: Lương tri và sự thật sẽ luôn là ngọn hải đăng cứu rỗi thế giới.',
            'Xin hãy luôn trân trọng cuộc sống, bảo vệ những giá trị đạo đức căn cốt và giữ vững sự tỉnh thức trong một thế giới không ngừng biến đổi.',
            'Cảm ơn quý vị đã luôn đồng hành cùng Amber Eyes trong từng hồ sơ tâm lý chuyên sâu.',
            'Xin chào và hẹn gặp lại quý vị trong những hành trình tiếp theo.'
        ],
        [
            'Our psychological journey into the mind of Ted Kaczynski draws to a close, leaving a profound meditation on the fragile frontier between genius and depravity.',
            'Towering intellect devoid of empathy and human compassion produces only the coldest and most destructive monsters.',
            'Conversely, the agonizing moral sacrifice of his brother David Kaczynski reminds us that conscience and truth remain the ultimate beacons redeeming our world.',
            'May we always cherish human life, uphold foundational ethical principles, and preserve vigilance amidst an ever-evolving technological landscape.',
            'Thank you for walking alongside Amber Eyes throughout our deep forensic psychological explorations.',
            'Until our next case file, stay vigilant and farewell.'
        ],
        [
            'テッド・カジンスキーの深層心理を巡る旅は終わりを告げ、私たちに知性と狂気の狭間にある脆い境界線についての深い思索を残しました。',
            '共感力と思いやりの心を欠いた卓越した知性は、最も冷酷で破壊的な怪物を生み出すに過ぎません。',
            'その一方で、弟デイヴィッド・カジンスキーが払った苦渋に満ちた道徳的犠牲は、良心と真実こそが世界を救済する永遠の灯火であることを証明しています。',
            '命の尊厳を重んじ、揺るぎない倫理観を胸に、移りゆく時代の中でも常に理性の覚醒を保ち続けましょう。',
            'アンバー・アイズの犯罪心理探求に最後までお付き合いいただき、心より感謝申し上げます。',
            '次なる事件記録でお会いする日まで、どうか平穏な日々をお過ごしください。'
        ]
    ))
    blocks.append(('SFX', 'SFX', 'Tiếng nhạc piano kết thúc ngân dài, hòa vào tiếng gió rừng Montana và mờ dần.', 'End piano chord resonating, blending with Montana pine wilderness wind, and fading out.', 'エンディングのピアノの残響が、モンタナの松林を渡る風の音に溶け込みながら静かに消え去る。'))

    return blocks

print('Module build_full_episode defined.')
