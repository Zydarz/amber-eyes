# -*- coding: utf-8 -*-
"""
Tạo kịch bản Tập 31 chuẩn A2/K10/V9 đầy đủ 3 ngôn ngữ: VN, EN, JA.
Đồng bộ tuyệt đối: 5 Hồi, các lượt nói, số câu thoại từng lượt, các thẻ BGM/SFX.
"""
import sys, os, json, re

# Định nghĩa kịch bản qua danh sách các block:
# Mỗi block là một tuple: (kind, role/type, direction, [câu_VN], [câu_EN], [câu_JA])
# kind: 'ACT', 'BGM', 'SFX', 'LOI'

# Xây dựng dữ liệu chi tiết cho 5 Hồi
def build_episode_data():
    blocks = []
    
    # ==========================================
    # HỒI 1: KHỞI NGUỒN CƠN ÁC MỘNG BƯU CHÍNH & VỎ BỌC RỪNG SÂU
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
            'しかし、最も不可解で衝撃的な事実は、廃材で作られた爆弾の精巧な機械的構造だけにとどまりませんでした。',
            'それは首謀者の素顔にあり、ハーバード大学を卒業した天才数学者が、輝かしいキャリアを捨ててモンタナの深林にある粗末な小屋に隠遁していたのです。',
            'いかにして並外れた知性が冷酷な破壊機械へと変貌し、歪んだ哲学的理念の名の下に見知らぬ他者の命を奪うに至ったのでしょうか。'
        ]
    ))
    
    blocks.append(('SFX', 'SFX', 'Tiếng động cơ máy bay gầm rú từ xa, tiếng gió rít qua rặng thông đại ngàn.', 'Sound of distant airplane engines roaring, wind howling through pine trees.', '遠くで響く飛行機のエンジン音、松林を吹き抜ける風のうめき。'))
    
    blocks.append(('LOI', 'HOST',
        'chuyển giọng u tối, báo hiệu tai ương',
        [
            'Cơn ác mộng bắt đầu vào ngày 25 tháng 5 năm 1978 tại Đại học Illinois ở Chicago.',
            'Một kiện bưu phẩm khả nghi được gửi trả về cho Giáo sư kỹ thuật vật liệu Cristos Gianakos.',
            'Tuy nhiên, vị giáo sư khẳng định mình chưa từng gửi bưu kiện đó và đã liên hệ với nhân viên an ninh nhà trường.',
            'Khi gói hàng được mở ra tại khuôn viên Đại học Northwestern, một tiếng nổ chói tai vang lên làm bị thương một viên cảnh sát bảo vệ.',
            'Đó là phát súng mở màn cho chuỗi 16 vụ gửi bom thư kéo dài suốt 17 năm sau đó.',
            'Mục tiêu của kẻ tấn công liên tục thay đổi: từ các giáo sư toán học, chuyên gia máy tính cho đến các giám đốc điều hành hàng không.',
            'Đỉnh điểm là vụ việc vào tháng 11 năm 1979, khi một quả bom thư được đặt trong khoang hành lý chuyến bay 444 của hãng United Airlines chở 80 hành khách.',
            'May mắn thay, cơ chế kích nổ bằng khí áp kế bị lỗi kỹ thuật, chỉ tạo ra một đám khói mù mịt buộc máy bay phải hạ cánh khẩn cấp.'
        ],
        [
            'The nightmare commenced on May 25, 1978, at the University of Illinois in Chicago.',
            'A suspicious postal package was returned to materials engineering professor Cristos Gianakos.',
            'The professor, however, affirmed he had never mailed the parcel and immediately alerted campus security.',
            'When the package was inspected at Northwestern University, a deafening blast tore through the air, injuring a security officer.',
            'That was the opening salvo of a 16-bomb campaign spanning the next 17 grueling years.',
            'The attacker targets shifted relentlessly: from mathematics professors and computer scientists to airline executives.',
            'The climax arrived in November 1979, when a barometric bomb was placed inside the cargo hold of United Airlines Flight 444 carrying 80 passengers.',
            'Fortunately, a mechanical flaw in the altimeter trigger caused only dense smoke rather than a catastrophic explosion, forcing an emergency landing.'
        ],
        [
            '悪夢は1978年5月25日、シカゴのイリノイ大学で始まりました。',
            '材料工学の教授クリストス・ジアナコス宛てに、差出人不明の不審な郵便小包が返送されてきたのです。',
            'しかし教授は身に覚えがないと主張し、直ちに大学の警備責任者に通報しました。',
            'ノースウェスタン大学構内で小包が開けられた瞬間、鋭い爆発音が響き渡り、警備員が負傷しました。',
            'それは、その後17年間にわたる計16回もの郵便爆弾事件の不吉な幕開けでした。',
            '標的は数学者、コンピュータ科学者、そして航空会社の重役へと絶え間なく変化していきました。',
            '戦慄の頂点は1979年11月、80人の乗客を乗せたユナイテッド航空444便の貨物室に気圧作動式爆弾が仕掛けられた事件でした。',
            '幸運にも起爆機構の作動不良により、爆弾は機体を破壊することなく白煙を上げたのみで、緊急着陸に成功しました。'
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
            'Chúng tôi phải đối mặt với một bóng ma vô hình, không để lại bất kỳ dấu vết sinh học nào suốt hơn một thập kỷ.'
        ],
        [
            'Immediately following the 1979 airline incident, the FBI formally established a joint task force codenamed UNABOM.',
            'The name derived from the perpetrator primary targets: Universities and Airlines.',
            'Over 150 full-time investigators, coordinating with ATF explosives experts and Postal Inspectors, probed thousands of leads.',
            'Yet the suspect proved to be an absolute master of forensic countermeasures and crime scene sanitation.',
            'Every explosive device was handcrafted entirely from scrap timber, plumbing pipes, and improvised mechanical components.',
            'He meticulously polished and filed every single part by hand to eliminate latent fingerprints and machine toolmarks.',
            'The only tangible clue intentionally left behind was the enigmatic inscription FC stamped onto internal metal fragments.',
            'We found ourselves pursuing an invisible ghost who left virtually zero biological traces for over a decade.'
        ],
        [
            '1979年の航空機事件の直後、FBIはコードネーム「UNABOM」と呼ばれる合同特別捜査班を正式に立ち上げました。',
            'この名称は、犯人の初期の標的であった大学（University）と航空会社（Airline）の頭文字に由来しています。',
            '150人以上の専任捜査官がATFの爆発物専門家や郵便監察局と連携し、数万件に及ぶ手掛かりを徹底的に洗い出しました。',
            'しかし犯人は、現場の痕跡を完全に消し去る偽装工作の絶対的な達人でした。',
            'すべての爆発装置は、廃材の木片や古い配管パイプ、手作りの機械部品から完全に手作業で組み立てられていました。',
            '彼は指紋や工業用工具の痕跡を消し去るため、すべての部品を入念に手作業で研磨していたのです。',
            '彼が意図的に残した唯一の手掛かりは、金属片の内側に刻まれた謎めいた「FC」という2文字だけでした。',
            '私たちは10年以上にわたり、生物学的痕跡を一切残さない目に見えない亡霊と対峙することを余儀なくされたのです。'
        ]
    ))
    
    blocks.append(('LOI', 'ORDINARY_PERSON',
        'N1: Cư dân thị trấn Lincoln, Montana – giọng run rẩy, bàng hoàng',
        [
            'Ở một thị trấn nhỏ hẻo lánh giữa thung lũng như Lincoln, mọi người sống dựa vào sự tin tưởng và tôn trọng không gian riêng của nhau.',
            'Chúng tôi thường thấy một người đàn ông râu tóc bù xù đạp chiếc xe đạp cũ vào tiệm tạp hóa mua đậu hộp và bột mì.',
            'Ông ấy ít nói, ánh mắt xa xăm và luôn né tránh các cuộc trò chuyện xã giao.',
            'Mọi người chỉ nghĩ đơn giản rằng đó là một người yêu thiên nhiên muốn sống cuộc đời ẩn dật như nhà văn Henry Thoreau.',
            'Không một ai trong chúng tôi có thể tưởng tượng được rằng, bên trong căn lều gỗ chật chội không điện nước ấy lại là nơi chế tạo ra những cỗ máy hủy diệt tàn độc nhất.'
        ],
        [
            'In a secluded valley town like Lincoln, folks live by mutual trust and deep respect for each other privacy.',
            'We often saw an unkempt man with a ragged beard riding an old bicycle to the general store to buy canned beans and flour.',
            'He spoke very little, kept his distant gaze fixed forward, and consistently avoided small talk.',
            'People simply assumed he was a nature lover seeking a peaceful hermit life, much like Henry David Thoreau.',
            'None of us could have ever fathomed that inside that cramped cabin without electricity or plumbing, America deadliest killer was crafting lethal machines.'
        ],
        [
            'リンカーンのような人里離れた渓谷の小さな町では、人々は互いの信頼とプライバシーの尊重を何よりも重んじて暮らしています。',
            '手入れされていない髭を生やした男が古い自転車に乗り、豆の缶詰や小麦粉を買いに雑貨店へやって来る姿をよく見かけました。',
            '彼は極めて無口で、遠くを見つめるような視線で、世間話を決して交わそうとはしませんでした。',
            '住民たちは皆、作家ソローのように静かな世捨て人生活を好む自然愛好家なのだろうと信じ込んでいたのです。',
            '電気も水道もないあの狭苦しい丸太小屋の中で、全米を震撼させる凶悪な破壊装置が作られていたとは、誰一人として想像すらできませんでした。'
        ]
    ))
    
    blocks.append(('LOI', 'PSYCHOLOGIST',
        'giọng điềm đạm, sắc sảo, phân tích tâm lý',
        [
            'Dưới góc độ tâm lý học hành vi, vụ án Unabomber là một minh chứng đau lòng cho sự tha hóa của trí tuệ khi bị ngắt kết nối hoàn toàn khỏi lòng trắc ẩn.',
            'Hiện tượng này bắt nguồn từ một cơ chế tâm lý cực đoan mang tên “Ảo tưởng cứu thế và Sự ái kỷ trí tuệ”.',
            'Đối tượng tự phong cho mình sứ mệnh cao cả là bảo vệ nhân loại khỏi sự thống trị của hệ thống kỹ trị công nghiệp.',
            'Hắn xây dựng một bức tường phòng vệ tinh thần kiên cố để biện minh rằng: sự hy sinh sinh mạng của một vài cá nhân là cái giá tất yếu để thức tỉnh cả một nền văn minh.',
            'Khi một bộ não thông minh tự thuyết phục bản thân rằng mình nắm giữ chân lý tối thượng, nó sẽ triệt tiêu hoàn toàn cảm giác tội lỗi và biến bạo lực thành một phương tiện đạo đức giả tạo.'
        ],
        [
            'From a behavioral psychology perspective, the Unabomber case stands as a tragic testament to intellect alienated from human empathy.',
            'This phenomenon stems from a toxic psychological mechanism known as Intellectual Narcissism and Messianic Delusion.',
            'The perpetrator appointed himself on a divine crusade to liberate humanity from the encroachment of the techno-industrial system.',
            'He erected an impenetrable psychological defense mechanism to justify that sacrificing individual lives was an inevitable cost to awaken civilization.',
            'When a brilliant intellect convinces itself of possessing supreme moral truth, it eradicates empathy and transforms violence into a sanctimonious crusade.'
        ],
        [
            '行動心理学の視点から見れば、ユナボマー事件は人間の共感力から完全に切り離された知性の悲劇的な堕落を雄弁に物語っています。',
            'この現象は、「知性愛己主義と救世主妄想」と呼ばれる極端な心理メカニズムに端を発しています。',
            '犯人は、人類を技術的産業システムの専制から解放するという崇高な使命を自らに勝手に課していました。',
            '彼は強固な心理的防衛機制を築き上げ、数人の無実の命を犠牲にすることは文明を覚醒させるための不可避の代償であると正当化したのです。',
            '卓越した頭脳が自らを至高の真理の保持者であると思い込むとき、罪悪感は完全に麻痺し、暴力は独善的な道徳的手段へとすり替えられてしまうのです。'
        ]
    ))

    # ==========================================
    # HỒI 2: ÁI KỶ TRÍ TUỆ & CHÂN DUNG TÂM LÝ KẺ SĂN MỒI TRONG BÓNG TỐI
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
        'bóc tách thí nghiệm tâm lý Harvard và cơ chế chia ngăn',
        [
            'Từ năm 1959 đến 1962, Ted Kaczynski vô tình trở thành đối tượng nghiên cứu trong một dự án tâm lý học gây tranh cãi của Giáo sư Henry Murray.',
            'Dự án này là một phần của các cuộc thử nghiệm kiểm tra giới hạn chịu đựng tinh thần được tài trợ bí mật.',
            'Các sinh viên trẻ bị buộc phải viết những bài luận bày tỏ triết lý sống cốt lõi của mình, rồi sau đó bị một luật sư thẩm vấn công kích, làm nhục tàn nhẫn trước máy quay.',
            'Đối với một chàng trai trẻ có cái tôi ái kỷ mong manh như Ted, trải nghiệm này là một chấn thương tâm lý cực kỳ sâu sắc.',
            'Nó khắc sâu vào tâm trí hắn một nỗi uất hận không thể nguôi ngoai đối với các hệ thống kiểm soát quyền lực và khoa học hành vi.',
            'Sau khi lấy bằng tiến sĩ toán học tại Đại học Michigan và trở thành giáo sư trẻ nhất lịch sử Đại học UC Berkeley, Ted bất ngờ từ chức vào năm 1969.',
            'Hắn kích hoạt một cơ chế phòng vệ mang tên “Chia ngăn nhận thức và Sự tự cô lập cực đoan”.',
            'Hắn cắt đứt mọi liên hệ với thế giới văn minh, lui về căn lều gỗ Montana để tự giam mình trong một pháo đài cô độc.'
        ],
        [
            'Between 1959 and 1962, Ted Kaczynski became an unwitting subject in a highly controversial psychological experiment run by Professor Henry Murray.',
            'This project was tied to covertly funded research testing the limits of psychological resilience under severe stress.',
            'Young undergraduates were forced to draft essays outlining their core personal philosophies, only to be subjected to brutal verbal assaults by interrogators under bright lights.',
            'For a young man possessing a vulnerable narcissistic ego like Ted, this experience inflicted profound moral humiliation.',
            'It deeply cemented an enduring animosity toward authoritarian institutions, psychological manipulation, and technocratic power structures.',
            'After obtaining his mathematics doctorate from Michigan and becoming UC Berkeley youngest assistant professor, Ted abruptly resigned in 1969.',
            'He activated a rigid defensive mechanism: Cognitive Compartmentalization paired with Extreme Self-Isolation.',
            'Severing ties with civilized society, he retreated to his Montana timber cabin, barricading himself inside a fortress of solitude.'
        ],
        [
            '1959年から1962年にかけて、テッドはヘンリー・マレー教授が主導する極めて物議を醸す心理実験の被験者となりました。',
            'この実験は、極度のストレス下における精神的耐久力の限界を検証する秘密資金提供を受けた研究の一環でした。',
            '学生たちは自らの最も大切にする哲学的信条を論文に書かされた後、強烈な照明の下で審問官から容赦ない人格攻撃と侮辱を受けました。',
            '脆い自己愛を抱えていた若きテッドにとって、この屈辱的な体験は計り知れない心理的トラウマとなりました。',
            'この出来事が、権威的な制度、心理操作、そして技術官僚体制に対する消えることのない憎悪の炎を彼の心に植え付けたのです。',
            'ミシガン大学で数学の博士号を取得し、カリフォルニア大学バークレー校の史上最年少助教授となったテッドは、1969年に突如として職を辞しました。',
            '彼は「認知的区画化と極限の自己孤立」という強固な防衛機制を発動させたのです。',
            '文明社会とのあらゆる繋がりを断ち切った彼はモンタナの丸太小屋へと退却し、孤独の要塞の中に自らを幽閉しました。'
        ]
    ))
    
    blocks.append(('SFX', 'SFX', 'Tiếng cưa gỗ kẽo kẹt, tiếng đục kim loại sắc lạnh trong đêm tối.', 'Sound of hand saws grating wood, cold chisels striking metal in darkness.', '木を挽く鋸の軋む音、暗闇の中で金属を削る冷たい鑿の響き。'))
    
    blocks.append(('LOI', 'INVESTIGATOR',
        'trích xuất hồ sơ hiện trường và chữ ký hành vi',
        [
            'Trong căn lều rộng chỉ mười mét vuông ấy, Ted Kaczynski đã thiết lập một quy trình chế tạo vũ khí cực kỳ tỉ mỉ và khoa học.',
            'Hắn không sử dụng bất kỳ linh kiện nào có thể truy nguyên nguồn gốc thương mại.',
            'Hắn nhặt nhạnh từng đoạn ống nước cũ, tự chế thuốc nổ đen từ lưu huỳnh và than củi, đúc các chốt kích hoạt từ gỗ sồi và kim loại phế thải.',
            'Mỗi quả bom là một tác phẩm thủ công chết chóc, đòi hỏi hàng trăm giờ lao động kiên nhẫn.',
            'Và điều đáng sợ nhất chính là sự phi nhân hóa triệt để đối với các nạn nhân trong tư duy của kẻ thủ ác.',
            'Hắn không hề quan tâm người mở gói bưu phẩm là ai, họ có gia đình hay con nhỏ hay không.',
            'Trong nhật ký bí mật được mã hóa tỉ mỉ, hắn ghi lại các vụ nổ không phải bằng sự xót thương, mà bằng sự thỏa mãn lạnh lùng khi thấy thiết bị hoạt động chính xác.',
            'Đó là sự thiếu hụt hoàn toàn của thấu cảm cảm xúc, nơi sinh mạng con người bị giáng cấp thành những con số thống kê phục vụ cho sự khẳng định bản ngã.'
        ],
        [
            'Inside that ten-by-twelve-foot timber shack, Ted Kaczynski established an excruciatingly methodical munitions lab.',
            'He strictly avoided any commercially serialized components that could be traced back to retail distributors.',
            'He collected scrap plumbing pipes, blended homemade black powder from potassium chlorate and charcoal, and whittled bomb switches from scrap hardwood.',
            'Each explosive device represented a lethal handcrafted artifact requiring hundreds of hours of patient labor.',
            'Yet what chilled investigators to the bone was his absolute psychological dehumanization of the victims.',
            'He harbored zero concern for who unwrapped the packages, whether they had spouses, young children, or families.',
            'In his meticulously enciphered private journals, he cataloged explosions not with remorse, but with clinical satisfaction over mechanical success.',
            'This demonstrated a total affective empathy deficit, where human lives were reduced to cold empirical data serving his intellectual vanity.'
        ],
        [
            'わずか10フィート四方の丸太小屋の中で、テッドは戦慄するほど緻密で秩序ある兵器製造工房を築き上げていました。',
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
        'N1: Giáo sư David Gelernter (Nạn nhân sống sót - Đại học Yale) – giọng trầm uất nhưng kiên định',
        [
            'Mùa hè năm 1993, tôi bước vào văn phòng tại Đại học Yale sau một kỳ nghỉ.',
            'Trên bàn có một kiện bưu phẩm nhỏ bọc giấy nâu gửi từ California, trông không khác gì những cuốn bản thảo sách bình thường.',
            'Khi tôi vừa rạch lớp băng dính bên ngoài, một tia chớp trắng lóa xé toạc không gian cùng một tiếng nổ kinh hoàng.',
            'Tôi vĩnh viễn mất đi một phần bàn tay phải, mắt phải bị tổn thương nặng và cơ thể mang đầy vết sẹo.',
            'Nhưng điều tàn bạo nhất mà kẻ gửi bom muốn cướp đi không phải là thể xác của chúng tôi, mà là cảm giác an toàn và niềm tin vào cuộc sống.',
            'Hắn muốn gieo rắc sự hoang mang vào tâm trí của mọi học giả, biến tri thức thành một mối đe dọa thường trực.'
        ],
        [
            'In the summer of 1993, I walked into my office at Yale University after a brief vacation.',
            'On my desk lay a modest package wrapped in brown paper postmarked from California, resembling an ordinary manuscript.',
            'The instant I slit the outer tape, a blinding white flash ripped through the room accompanied by a deafening roar.',
            'I permanently lost my right hand, suffered severe trauma to my right eye, and bore lasting scars across my body.',
            'Yet the most brutal thing that bomber sought to destroy was not merely our physical flesh, but our foundational sense of security.',
            'He wanted to inject pervasive terror into every scholar mind, turning the pursuit of knowledge into a constant threat.'
        ],
        [
            '1993年の夏、私は休暇を終えてイェール大学の研究室へと戻りました。',
            '机の上にはカリフォルニアからの消印が押された茶色の包み紙の小包があり、普通の原稿のように見えました。',
            '外側のテープに切れ目を入れた瞬間、目の前で白い閃光が弾け、鼓膜を裂く轟音が部屋を包み込みました。',
            '私は右手の一部を永久に失い、右目を激しく損傷し、全身に深い傷跡を負うことになりました。',
            'しかし、爆弾魔が本当に奪おうとした最も残酷なものは私たちの肉体ではなく、日常の安全への確信そのものでした。',
            '彼はすべての学者の心に底知れぬ恐怖を植え付け、知の探求そのものを常に死の危険と隣り合わせにしようとしたのです。'
        ]
    ))

    # ==========================================
    # HỒI 3: CUỘC ĐẤU TRÍ NGÔN NGỮ & NỖI GIẰNG XÉ LƯƠNG TÂM CỦA NGƯỜI EM TRAI
    # ==========================================
    blocks.append(('ACT', 3, 'CUỘC ĐẤU TRÍ NGÔN NGỮ & NỖI GIẰNG XÉ LƯƠNG TÂM CỦA NGƯỜI EM TRAI', 'THE LINGUISTIC DUEL & THE BROTHER AGONIZING CONSCIENCE', '言語学的決闘と弟の引き裂かれた良心'))
    blocks.append(('BGM', 'BGM', 'Tiếng Cello u uất giằng xé hòa cùng nhịp Piano trầm mặc ngột ngạt.', 'Sorrowful solo cello interweaving with heavy, oppressive minimalist piano.', '悲痛なチェロの独奏が、重苦しく息詰まるミニマルピアノと絡み合う。'))
    
    blocks.append(('LOI', 'HOST',
        'chuyển sang bước ngoặt kịch tính của vụ án',
        [
            'Sau 17 năm reo rắc kinh hoàng khiến 3 người thiệt mạng và 23 người bị thương tật suốt đời, kẻ thủ ác bất ngờ đưa ra một canh bạc thế kỷ.',
            'Tháng 6 năm 1995, một bức thư nặc danh dài được gửi tới ban biên tập của hai tờ báo hàng đầu nước Mỹ: The New York Times và The Washington Post.',
            'Kẻ tự xưng là đại diện của tổ chức FC tuyên bố: Nếu hai tờ báo chấp nhận đăng toàn văn bản luận thuyết dài 35.000 từ của hắn, hắn sẽ chấm dứt vĩnh viễn các vụ đánh bom sát thương.',
            'Đây là một tình thế tiến thoái lưỡng nan chưa từng có đối với giới truyền thông và các cơ quan tư pháp Hoa Kỳ.',
            'Liệu việc nhượng bộ yêu sách của một kẻ khủng bố có tạo nên một tiền lệ nguy hiểm cho nền tự do báo chí?',
            'Sau nhiều cuộc thảo luận căng thẳng giữa Bộ trưởng Tư pháp Janet Reno và Giám đốc FBI Louis Freeh, một quyết định táo bạo đã được thông qua.',
            'Họ quyết định xuất bản bản Tuyên ngôn mang tên “Xã hội Công nghiệp và Tương lai của nó” vào ngày 19 tháng 9 năm 1995.',
            'Và chính canh bạc truyền thông này đã trở thành chiếc thòng lọng vô hình siết chặt lấy kẻ thủ ác từ nơi hắn ít ngờ tới nhất.'
        ],
        [
            'After 17 years of terror leaving three dead and twenty-three severely maimed, the elusive bomber proposed a dramatic high-stakes wager.',
            'In June 1995, anonymous letters were delivered to the editorial desks of America premier publications: The New York Times and The Washington Post.',
            'Claiming to represent the underground group FC, the author vowed to permanently cease lethal bombings if they published his 35,000-word manifesto.',
            'This created an unprecedented ethical dilemma for the American press and federal law enforcement agencies.',
            'Would acceding to a terrorist demands compromise the integrity of a free press and invite perpetual extortion?',
            'Following intense deliberations between Attorney General Janet Reno and FBI Director Louis Freeh, a bold operational gamble was authorized.',
            'They recommended publishing the manifesto entitled Industrial Society and Its Future on September 19, 1995.',
            'And that very publication became the fateful noose tightening around the killer from a quarter he least anticipated.'
        ],
        [
            '3人の命を奪い、23人に生涯消えない重傷を負わせた17年間の凶行の末、爆弾魔は突如として世紀の賭けに出ました。',
            '1995年6月、アメリカを代表する2大新聞社、ニューヨーク・タイムズとワシントン・ポストの編集部に匿名の書簡が届きました。',
            '「FC」と名乗る差出人は、自らが執筆した3万5千語におよぶ論文の全文掲載を条件に、無差別爆破作戦の完全停止を申し出たのです。',
            'これはアメリカの報道界と司法当局にとって、かつて経験したことのない前代未聞の倫理的ジレンマでした。',
            'テロリストの脅迫に屈することは、報道の自由と法治国家の原則を根底から揺るがす極めて危険な前例になりはしないか。',
            'ジャネット・レノ司法長官とルイス・フリーFBI長官による緊迫した協議の末、極めて異例の決断が下されました。',
            '1995年9月19日、「産業社会とその未来」と題されたその声明文が新聞の特別別刷りとして世に出ることになったのです。',
            'そしてこの一か八かの賭けこそが、犯人が最も予期しなかった場所からその首を絞め上げる運命の罠となったのです。'
        ]
    ))
    
    blocks.append(('LOI', 'INVESTIGATOR',
        'giải thích bước đột phá của Giám định ngôn ngữ học pháp y',
        [
            'Khi bản tuyên ngôn được công bố, một chuyên gia trẻ của FBI mang tên James R. Fitzgerald đã nhìn thấy cơ hội mở ra cánh cửa phá án.',
            'Fitzgerald là một trong những người tiên phong đặt nền móng cho chuyên ngành “Giám định Ngôn ngữ học Pháp y”.',
            'Ông hiểu rằng: Mỗi con người đều sở hữu một dấu vân tay ngôn ngữ duy nhất, được định hình bởi thói quen ngữ pháp, vốn từ vựng và cấu trúc tư duy.',
            'Fitzgerald bắt đầu phân tích từng câu chữ trong bản tuyên ngôn, bóc tách các thuật ngữ học thuật hiếm gặp và các lối diễn đạt cổ xưa.',
            'Ông nhận thấy tác giả sử dụng các biến thể chính tả từ thập niên 1950, kết hợp với các luận điểm triết học đặc trưng của giới tinh hoa học thuật.',
            'Chúng tôi không còn tìm kiếm một quả bom vật lý nữa, mà đang săn lùng tác giả của một phong cách hành văn độc nhất vô nhị.',
            'Bằng chứng ngôn ngữ học đã biến một bản tài liệu trừu tượng thành một bản đồ chỉ đường chính xác dẫn thẳng tới tâm trí kẻ thủ ác.'
        ],
        [
            'The moment the manifesto appeared in print, an innovative FBI supervisory agent named James R. Fitzgerald recognized a breakthrough opportunity.',
            'Fitzgerald was a visionary pioneer who helped forge the emerging discipline of Forensic Linguistics.',
            'He understood an essential truth: Every individual possesses a unique linguistic idiolect shaped by syntax, vocabulary, and cognition.',
            'Fitzgerald methodically scrutinized every sentence within the manifesto, isolating idiosyncratic academic terminology and archaic idioms.',
            'He observed distinctive 1950s spellings fused with philosophical diatribes characteristic of mid-century elite academia.',
            'We were no longer merely hunting an explosive device; we were hunting the author behind an unmistakable literary footprint.',
            'Linguistic evidence transformed an abstract ideological tract into an empirical psychological roadmap leading directly to the perpetrator.'
        ],
        [
            'マニフェストが活字となって世に出た瞬間、ジェームズ・R・フィッツジェラルドという若きFBI捜査官が突破口を見出しました。',
            '彼は「法言語学（Forensic Linguistics）」という新たな科学捜査手法の礎を築いた先駆者の一人でした。',
            '彼は確信していました。すべての人間は、文法上の癖、語彙の選択、思考の構造によって形作られた唯一無二の「言語の指紋」を持っていると。',
            'フィッツジェラルドは声明文のあらゆる文節を徹底的に精査し、極めて稀な学術用語や古風な言い回しを抽出していきました。',
            '彼は、1950年代の古い綴りの特徴と、20世紀半ばのエリート学界特有の哲学的言説が融合している点に着目しました。',
            '捜査班はもはや物理的な爆弾の破片を追うのではなく、独特の文体を持つ一人の書き手を追跡し始めたのです。',
            '言語学的証拠が、抽象的な思想文書を犯人の精神世界へと直接繋がる極めて精緻な捜査の羅針盤へと変貌させました。'
        ]
    ))
    
    blocks.append(('LOI', 'ORDINARY_PERSON',
        'N2: David Kaczynski (Em trai của Ted Kaczynski) – giọng nghẹn ngào, đau đớn tột cùng',
        [
            'Vợ tôi, Linda, là người đầu tiên đọc bản tuyên ngôn trên mặt báo và cảm thấy có điều gì đó bất an đến lạnh người.',
            'Cô ấy nói với tôi rằng giọng văn căm thù công nghệ này nghe rất giống những lá thư mà anh Ted từng gửi cho tôi suốt nhiều năm.',
            'Ban đầu, tôi kiên quyết gạt phắt đi vì tin rằng anh trai mình, dù lập dị và xa lánh thế tục, không bao giờ có thể làm tổn thương ai.',
            'Nhưng khi tôi trèo lên gác xép tìm lại những bức thư cũ từ thập niên 1970 để đối chiếu, cả thế giới xung quanh tôi sụp đổ.',
            'Từng luận điểm, từng cách ngắt câu, và đặc biệt là câu thành ngữ hiếm: “You can not eat your cake and have it too” đều trùng khớp tuyệt đối.',
            'Trái tim tôi như bị xé làm đôi giữa tình thân máu mủ và trách nhiệm đạo đức trước mạng sống của những con người vô tội.',
            'Nếu tôi im lặng, tôi sẽ cứu được anh trai mình, nhưng tôi sẽ trở thành kẻ đồng lõa cho vụ đánh bom đẫm máu tiếp theo.'
        ],
        [
            'My wife, Linda, was the first to read the published manifesto and experienced a terrifying, visceral shock.',
            'She told me that the vitriolic anti-technology rhetoric sounded eerily identical to letters Ted had sent me over the decades.',
            'Initially, I vehemently dismissed her suspicions, fiercely believing my brother, however eccentric, could never harm another human being.',
            'Yet when I climbed into the attic to retrieve his old correspondence from the 1970s, my entire world violently unraveled.',
            'The arguments, the syntactic cadence, and particularly his archaic phrasing – "You can not eat your cake and have it too" – matched flawlessly.',
            'My soul was torn violently apart between fraternal love and the moral responsibility toward innocent human lives.',
            'If I stayed silent, I might protect my brother, but I would become an accomplice to the next gruesome slaughter.'
        ],
        [
            '新聞に掲載された声明文を最初に読んだ私の妻リンダは、背筋が凍るような不吉な胸騒ぎを覚えました。',
            '彼女は、技術を激しく憎悪するその独特の文調が、何年もの間に兄のテッドが私に送ってきた手紙と酷似していると告げました。',
            '当初、私はそんな疑いを断固として拒絶し、風変わりで世を捨てたとはいえ、兄が誰かを傷つけるはずがないと信じたかったのです。',
            'しかし屋根裏部屋に上がり、1970年代の兄の手紙を引っ張り出して比較した瞬間、私の周囲の世界は音を立てて崩壊しました。',
            '論理の展開、文章の区切り方、そして彼が好んで使った「ケーキを食べてしまい、なおかつ手元に残すことはできない」という古い成句までが完全に一致したのです。',
            '私の魂は、血を分けた兄への愛情と、見知らぬ人々の尊い命に対する道徳的責任との間で無残に引き裂かれました。',
            'もし私が沈黙を守れば兄の命は救えるかもしれない、しかしそれは次の惨劇の共犯者になることを意味していたのです。'
        ]
    ))
    
    blocks.append(('LOI', 'PSYCHOLOGIST',
        'giải mã sự giằng xé lương tâm và cơ chế tố giác',
        [
            'Hành động của David Kaczynski là một trong những quyết định đạo đức bi tráng và can trường nhất trong lịch sử tâm lý học tư pháp.',
            'Đây là sự sụp đổ hoàn toàn của cơ chế “Thành kiến bảo vệ người thân” trước tiếng gọi của lương tri nhân loại.',
            'David không hành động vì tiền thưởng hay sự thù hận cá nhân; ông hành động trong sự dằn vặt khôn nguôi để ngăn chặn tội ác tiếp diễn.',
            'Ông hiểu rằng việc để anh trai tiếp tục gửi bom thư sẽ chỉ vùi dập nốt phần nhân tính mong manh còn sót lại của Ted.',
            'Quyết định liên hệ với cơ quan chức năng thông qua luật sư là một sự lựa chọn mang tính chuộc lỗi cao cả.',
            'Đó là khoảnh khắc mà tình yêu thương đích thực vượt lên trên sự dung túng mù quáng để cứu lấy sinh mệnh của đồng loại.'
        ],
        [
            'David Kaczynski decision represents one of the most agonizing yet heroic moral choices in forensic history.',
            'It marked the complete collapse of familial loyalty bias under the overwhelming mandate of universal conscience.',
            'David was neither motivated by monetary reward nor personal animosity; he acted in excruciating torment solely to halt bloodshed.',
            'He understood that allowing his brother to detonate more bombs would permanently annihilate whatever fragile humanity Ted possessed.',
            'Reaching out to federal investigators through an attorney was a profound act of restorative ethical courage.',
            'It was the sublime moment when authentic compassion transcended blind indulgence to safeguard human lives.'
        ],
        [
            'デイヴィッド・カジンスキーが下した決断は、司法心理学の歴史において最も悲痛でありながら最も勇敢な道徳的選択でした。',
            'それは、人類共通の良心の呼び声の前に、身内を盲目的に庇おうとする心理的偏見が完全に打ち破られた瞬間でした。',
            'デイヴィッドは賞金や個人的な敵意から動いたのではなく、これ以上の殺戮を食い止めるため、血の滲むような葛藤の末に行動したのです。',
            'これ以上爆弾を送り続けさせれば、テッドの心に残されたかすかな人間性すら完全に滅び去ってしまうことを彼は知っていました。',
            '弁護士を通じて連邦捜査局に情報を提供した彼の行為は、崇高な贖罪の精神に満ちた道徳的決断でした。',
            'それは、盲目的な身内の甘やかしを超越し、無実の命を救うために真の愛が下した極限の選択だったのです。'
        ]
    ))

    # ==========================================
    # HỒI 4: CUỘC ĐỘT KÍCH LINCOLN & SỰ SỤP ĐỔ CỦA PHÁO ĐÀI CÔ ĐỘC
    # ==========================================
    blocks.append(('ACT', 4, 'CUỘC ĐỘT KÍCH LINCOLN & SỰ SỤP ĐỔ CỦA PHÁO ĐÀI CÔ ĐỘC', 'THE LINCOLN CABIN RAID & COLLAPSE OF THE ISOLATED FORTRESS', 'リンカーンの山小屋急襲と孤立した要塞の崩壊'))
    blocks.append(('BGM', 'BGM', 'Tiếng Bass nặng trĩu dồn dập, tiếng còi hú từ xa và tiếng bước chân rầm rập trong tuyết.', 'Heavy pulsing sub-bass, distant sirens wailing, and rapid rhythmic tactical footsteps in snow.', '重く脈打つサブベース、遠くで響くサイレン、そして雪を踏みしめる戦術部隊の緊迫した足音。'))
    
    blocks.append(('LOI', 'HOST',
        'giọng dồn dập, đưa người xem vào thời khắc quyết định',
        [
            'Dựa trên bản so sánh đối chiếu ngôn ngữ học chi tiết của David và Fitzgerald, một trát khám xét lịch sử đã được phê chuẩn.',
            'Đây là lần đầu tiên một lệnh khám xét liên bang được cấp dựa trên phân tích cấu trúc ngôn ngữ pháp y.',
            'Ngày 3 tháng 4 năm 1996, hàng chục đặc vụ liên bang vũ trang hạng nặng cùng lực lượng cảnh sát địa phương đã âm thầm bao vây khu rừng Lincoln.',
            'Họ tiếp cận căn lều gỗ của Ted Kaczynski dưới vỏ bọc của các nhân viên kiểm lâm đang đo đạc địa hình.',
            'Bên trong căn lều tối tăm, kẻ bị săn đuổi suốt 17 năm hoàn toàn không hay biết rằng mạng lưới công lý đã khép chặt quanh mình.',
            'Khi cánh cửa gỗ ọp ẹp bật mở, toàn bộ thế giới bí mật của Unabomber đã bị phơi bày trọn vẹn ra ánh sáng.'
        ],
        [
            'Armed with the forensic linguistic comparison assembled by Fitzgerald and David, a historic federal search warrant was issued.',
            'It marked the first time in United States jurisprudence that a federal warrant was granted based primarily on linguistic profiling.',
            'On April 3, 1996, dozens of heavily armed federal agents quietly cordoned off the dense pine woods outside Lincoln, Montana.',
            'They advanced toward Ted Kaczynski primitive shack disguised as surveyors and forestry personnel.',
            'Inside the dim, cramped cabin, the elusive fugitive of 17 years remained oblivious that the legal dragnet had completely closed in.',
            'As the weathered cabin door was breached, the Unabomber entire subterranean universe was dragged violently into the daylight.'
        ],
        [
            'フィッツジェラルドとデイヴィッドによってまとめられた法言語学的照合に基づき、歴史的な連邦捜索令状が発付されました。',
            '米国の司法史上、言語学的プロファイリングを主要な根拠として捜索令状が認められたのはこれが初めてのことでした。',
            '1996年4月3日、重武装した多数の連邦捜査官と地元警察が、モンタナ州リンカーンの深い松林を極秘裏に包囲しました。',
            '捜査官たちは森林測量員を装い、慎重に間合いを詰めながらテッド・カジンスキーの丸太小屋へと接近しました。',
            '薄暗く狭苦しい小屋の内部で、17年間逃げ続けた爆弾魔は司法の網が完全に閉じられたことに全く気づいていませんでした。',
            '老朽化した木製ドアが開け放たれた瞬間、ユナボマーの秘密の世界のすべてが白日の下に晒されたのです。'
        ]
    ))
    
    blocks.append(('LOI', 'INVESTIGATOR',
        'tái hiện cuộc khám xét hiện trường bên trong căn lều gỗ',
        [
            'Cảnh tượng bên trong căn lều gỗ khiến ngay cả những điều tra viên dày dạn kinh nghiệm nhất cũng phải rùng mình.',
            'Không gian nồng nặc mùi lưu huỳnh, khói bếp và rác rưởi tích tụ lâu năm.',
            'Khắp căn phòng là hàng ngàn trang tài liệu viết tay, các cuốn sổ tay nhật ký ghi chép chi tiết từng thử nghiệm hóa chất.',
            'Dưới gầm giường, chúng tôi phát hiện một quả bom đã lắp ráp hoàn chỉnh, được bọc cẩn thận và chỉ chờ ngày gửi đi bưu điện.',
            'Cùng với đó là chiếc máy chữ cơ khí hiệu Smith Corona, thiết bị đã được dùng để gõ bản Tuyên ngôn chấn động thế giới.',
            'Tất cả mọi nghi ngờ đã được xóa sạch; người đàn ông gầy gò, râu tóc lôi thôi đứng trước mặt chúng tôi chính là kẻ khủng bố khét tiếng nhất nước Mỹ.',
            'Cuộc vây bắt kết thúc trong êm đẹp mà không cần nổ một phát súng nào, khép lại chuyên án dài hơi và tốn kém nhất trong lịch sử FBI.'
        ],
        [
            'The scene confronting agents inside that cabin sent a chill down the spines of our most hardened investigators.',
            'The suffocating space was reeking of sulfur, chimney soot, and decades of accumulated neglect.',
            'Every surface was inundated with thousands of handwritten journal pages cataloging meticulous chemical experiments.',
            'Concealed under his rustic cot, we uncovered a fully armed live explosive device, securely wrapped and ready for postmarking.',
            'Alongside sat the manual Smith Corona typewriter that hammered out the notorious 35,000-word manifesto.',
            'All lingering doubt evaporated instantly; the disheveled, unkempt figure stood definitively exposed as America most wanted serial bomber.',
            'The arrest concluded peacefully without a single round discharged, culminating the longest and costliest manhunt in FBI history.'
        ],
        [
            '小屋の内部で捜査官たちが目にした光景は、百戦錬磨のベテラン捜査官たちをも戦慄させるものでした。',
            '狭い空間には硫黄の鼻を突く悪臭、薪の煤煙、そして長年蓄積された生活ゴミの臭いが充満していました。',
            '部屋の至る所に、綿密な爆発物実験の経過を記録した数万ページにも及ぶ直筆のノートが積み上げられていました。',
            '粗末なベッドの下からは、完全に組み立てられ、宛名ラベルを貼って郵送するだけの状態になった実包爆弾が発見されました。',
            'その傍らには、世界を震撼させたあの声明文を印字したスミス・コロナ社製の手動タイプライターが置かれていました。',
            'すべての疑念は一瞬にして氷解し、目の前に立つ不潔で痩せこけた男こそが、全米を震え上がらせた最重要指名手配犯だったのです。',
            '一発の銃声も鳴り響くことなく急襲は完了し、FBI史上最も長期にわたり莫大な費用を投じた捜査に幕が下ろされました。'
        ]
    ))
    
    blocks.append(('LOI', 'PSYCHOLOGIST',
        'phân tích phản ứng của Ted khi bị bắt và cơ chế tự thương hại bệnh lý',
        [
            'Khoảnh khắc bị còng tay và đưa ra trước ống kính truyền thông, Ted Kaczynski không hề bộc lộ sự sợ hãi hay ăn năn.',
            'Ánh mắt hắn toát lên sự khinh miệt lạnh lùng đối với các nhân viên công lực và xã hội xung quanh.',
            'Hắn coi mình là một tù nhân chiến tranh, một triết gia bị bức hại vì dám đứng lên chống lại guồng quay của nền văn minh.',
            'Hiện tượng tâm lý này được định nghĩa là “Sự sụp đổ cái tôi ái kỷ và Tự thương hại bệnh lý”.',
            'Kẻ ái kỷ ác tính hoàn toàn khuyết tật khả năng thấu cảm nỗi đau của người khác, nhưng lại cực kỳ nhạy cảm với sự tổn thương của chính mình.',
            'Hắn không một lần nhỏ lệ xót thương cho các nạn nhân bị tước đoạt sinh mạng, mà chỉ phẫn uất vì kế hoạch vĩ đại của mình bị phá vỡ.',
            'Đó là sự đối lập tàn nhẫn nhất giữa một bộ óc thông minh xuất chúng và một tâm hồn hoàn toàn trống rỗng đạo đức.'
        ],
        [
            'Handcuffed and paraded before television cameras, Ted Kaczynski displayed neither terror nor contrition.',
            'His unblinking gaze radiated cold contempt toward law enforcement and the civil society surrounding him.',
            'He perceived himself not as a mass killer, but as a political prisoner persecuted for defying the machinery of modern civilization.',
            'This psychological posture reflects Malignant Narcissistic Collapse coupled with Pathological Self-Pity.',
            'The malignant narcissist is utterly barren of affective empathy for others, yet hypersensitive to any injury against his own ego.',
            'He never shed a single tear for the victims whose lives he shattered, weeping only for his lost autonomy and grand crusade.',
            'This underscores the tragic dichotomy between an astonishing intellect and a soul utterly devoid of moral humanity.'
        ],
        [
            '手錠をかけられ報道陣のカメラの前に引き出された瞬間も、テッドは恐怖や後悔の色を全く見せませんでした。',
            'その冷徹な眼差しは、法執行官や彼を取り巻く市民社会に対する底知れぬ軽蔑の光を放っていました。',
            '彼は自らを凶悪な連続殺人犯ではなく、文明の巨大な歯車に立ち向かったがゆえに迫害される崇高な思想犯であると信じ込んでいたのです。',
            'この心理状態は、「悪性自己愛の破綻と病理的自己憐憫」として精神医学上定義されます。',
            '悪性自己愛者は他者の苦痛に対して完全に感情が麻痺している一方で、自分自身の自尊心が傷つけられることには極度に過敏です。',
            '彼は自らが命を奪った犠牲者たちのために涙を流すことは一度もなく、奪われた自らの自由と大義の挫折のみを嘆き憤りました。',
            'それは、神童と讃えられた卓越した知能と、道徳的温もりを完全に喪失した空虚な魂との間の残酷な断絶を示しています。'
        ]
    ))
    
    blocks.append(('LOI', 'ORDINARY_PERSON',
        'N2: David Kaczynski – giọng trầm buồn, đối diện bi kịch gia đình',
        [
            'Ngày nhìn thấy anh Ted bị giải đi trên bản tin truyền hình, mẹ tôi và tôi đã ôm nhau khóc suốt đêm.',
            'Chúng tôi đau đớn vì biết rằng người anh trai thân yêu thuở nào đã vĩnh viễn không còn nữa.',
            'Báo chí và dư luận vây kín ngôi nhà của gia đình tôi, biến cuộc sống của chúng tôi thành một cơn địa chấn kinh hoàng.',
            'Nhưng nỗi đau lớn nhất đối với tôi không phải là sự chỉ trích của người đời, mà là sự căm phẫn tột cùng của anh Ted dành cho tôi.',
            'Anh ấy coi tôi là kẻ phản bội đáng ghê tởm nhất, từ chối gặp mặt tôi và vĩnh viễn cắt đứt mọi liên lạc cho đến ngày qua đời.',
            'Dù vậy, nếu được chọn lại một ngàn lần, tôi vẫn sẽ làm điều đó; bởi vì không có tình thân nào có thể được xây dựng trên máu và nước mắt của những sinh mạng vô tội.'
        ],
        [
            'The day I watched Ted dragged away across national television, my mother and I wept in each other arms through the night.',
            'Our hearts were shattered by the agonizing realization that the beloved brother of my youth was lost forever.',
            'The media descended upon our family home like a violent tempest, turning our private grief into a global spectacle.',
            'Yet the deepest wound was not public scrutiny; it was Ted unyielding, venomous hatred directed toward me.',
            'He branded me his ultimate Judas, refusing every visitation and severing all correspondence until his dying breath.',
            'Even so, if forced to choose a thousand times over, I would make the identical choice; for no fraternal bond can be purchased with the blood of innocent lives.'
        ],
        [
            'テレビの全国ニュースで連行される兄の姿を見た日、母と私は一晩中抱き合って涙を流し続けました。',
            '幼い頃に慕っていた優しい兄はもう永遠に失われてしまったのだという無慈悲な現実に、私たちの心は粉々に砕け散りました。',
            'メディアの群れが私たちの家に押し寄せ、家族の静かな悲しみは世界中の好奇の目に晒される嵐へと変わりました。',
            'しかし私にとって最も耐え難い苦痛は世間の視線ではなく、テッドが私に向けた激しい憎悪そのものでした。',
            '彼は私を忌まわしい裏切り者と断じ、面会を拒絶し、息を引き取る最後の日まで私との言葉の交わし合いを拒み続けました。',
            'それでも、たとえ何千回生まれ変わろうとも私は同じ道を選ぶでしょう――罪なき人々の血の上に築かれる家族愛など、決して存在してはならないからです。'
        ]
    ))

    # ==========================================
    # HỒI 5: BẢN ÁN ADX FLORENCE & BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN
    # ==========================================
    blocks.append(('ACT', 5, 'BẢN ÁN ADX FLORENCE & BÀI HỌC CẢNH BÁO ĐỎ SINH TỒN', 'THE ADX FLORENCE SENTENCE & RED ALERT LESSONS FOR SURVIVAL', '重警備刑務所の終身刑と命を守る赤信号の教訓'))
    blocks.append(('BGM', 'BGM', 'Tiếng Piano độc tấu trầm buồn, sâu lắng, mang âm hưởng suy tư và thức tỉnh.', 'Somber solo piano, deep, resonant, conveying profound contemplation and awakening.', '哀愁を帯びたピアノの独奏が、深い思索と魂の覚醒を促すように静かに響き渡る。'))
    
    blocks.append(('LOI', 'HOST',
        'dẫn dắt vào phiên tòa xét xử và phán quyết cuối cùng',
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
            'On May 4, 1998, Federal Judge Garland Burrell Jr. sentenced Theodore Kaczynski to four consecutive life terms plus thirty years, without possibility of parole.',
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
            'Hồ sơ UNABOM đã khép lại, nhưng nó đã để lại những cải cách mang tính bước ngoặt cho ngành điều tra tội phạm toàn cầu.',
            'Lần đầu tiên, Giám định ngôn ngữ học pháp y được công nhận là một công cụ khoa học độc lập có giá trị chứng cứ pháp lý tuyệt đối trước tòa.',
            'Vụ án cũng thúc đẩy sự ra đời của các quy trình kiểm soát bưu chính hiện đại và hệ thống soi chiếu an ninh sân bay tiên tiến bậc nhất.',
            'Nó chứng minh rằng: Dù kẻ thủ ác có ẩn náu sâu đến đâu trong rừng rậm, chữ ký tư duy và hành vi của hắn sẽ luôn là manh mối không thể che giấu.',
            'Công lý không bao giờ lùi bước trước bất kỳ sự ngụy trang trí tuệ nào, dù đó là một kẻ mang chỉ số thông minh của một thiên tài.'
        ],
        [
            'The UNABOM investigation concluded, yet its legacy permanently transformed modern forensic investigative methodology.',
            'For the very first time, Forensic Linguistics gained formal recognition as a rigorous scientific discipline with binding courtroom evidentiary value.',
            'The ordeal also spearheaded modern postal screening protocols and revolutionized aviation security protocols across the globe.',
            'It definitively demonstrated that no matter how deep a predator conceals himself in wilderness, his cognitive behavioral signature remains indelible.',
            'Justice never cowers before intellectual arrogance, regardless of whether the perpetrator possesses the intellect of a certified genius.'
        ],
        [
            'ユナボマーの捜査ファイルは閉じられましたが、それは世界の科学捜査手法に恒久的な革命をもたらしました。',
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
            'Thứ ba, và là bài học nhân văn sâu sắc nhất: Lòng dũng cảm đạo đức phải luôn đứng trên sự bao che tình thân; sự can thiệp của gia đình chính là chiếc phao cứu sinh cuối cùng để ngăn chặn cái ác hủy diệt nhân tính.'
        ],
        [
            'From the 17-year ordeal of the Unabomber file, behavioral science distills three paramount survival imperatives for modern society:',
            'First, heed the red alerts of extreme social isolation and messianic grievances; when an individual severs social attachments while harboring ideological hatred, early intervention is critical.',
            'Second, maintain vigilance regarding anonymous mailings; never handle parcels displaying suspicious traits such as excessive postage, missing return addresses, heavy taping, or chemical odors.',
            'Third, and most profoundly humane: Moral fortitude must always transcend blind familial allegiance; courageous familial intervention remains the ultimate safeguard against the annihilation of human conscience.'
        ],
        [
            'ユナボマーがもたらした17年間の試練から、行動科学は現代社会を生きる私たちに3つの重要な生存の教訓を提示しています。',
            '第1に、極端な社会的孤立と救世主的な被害妄想が発する危険信号を見逃さないこと――身近な人が人間関係を断ち切り、社会に対する憎悪を募らせている場合は、早期の専門的介入が不可欠です。',
            '第2に、不審な差出人不明の郵便物に対する防犯意識を常に保持すること――差出人住所の欠落、過剰な切手、過度なテーピング、異臭などの異常を認めた小包には決して直接触れてはなりません。',
            'そして第3に、最も深い人間的教訓として、道徳的勇気は身内への盲目的な庇い立てに常に優先されねばならないこと――勇気ある家族の介入こそが、人間の良心が完全に破壊されるのを食い止める最後の防波堤なのです。'
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

def generate_script(lang, blocks):
    lines = []
    if lang == 'VN':
        lines.append('# KỊCH BẢN CHI TIẾT TẬP 31: HỒ SƠ TED KACZYNSKI (UNABOMBER) — CƠN CUỒNG NỘ TRÍ THỨC & BƯỚC ĐỘT PHÁ CỦA GIÁM ĐỊNH NGÔN NGỮ HỌC PHÁP Y')
        lines.append('')
        lines.append('* **Đề tài:** Thần đồng toán học Harvard sống ẩn dật gửi 16 bom thư phản đối văn minh công nghệ (1978–1995).')
        lines.append('* **Chủ đề tâm lý:** Giám định ngôn ngữ học pháp y (Forensic Linguistics), Ảo tưởng cứu thế, Sự tự cô lập cực đoan và Biến chuyển lương tâm giữa hai anh em.')
        lines.append('* **Thời lượng dự kiến:** 28 – 32 phút')
        lines.append('* **Định dạng:** Chuẩn A2 — Cấu trúc 5 Hồi chuẩn mực theo Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c) và Luật K10')
        lines.append('* **Tiêu chuẩn An toàn YouTube (Rule V9):** 100% YouTube Safe, không mô tả trực diện thương tổn thể xác hay chi tiết rùng rợn; tập trung 100% vào phân tích tâm lý học tội phạm, vi biểu cảm, chiến thuật hỏi cung và bài học phòng ngừa tội phạm.')
        lines.append('')
        lines.append('---')
        lines.append('')
        lines.append('## BẢNG PHÂN VAI VÀ CẤU TRÚC GIỌNG ĐỌC')
        lines.append('')
        lines.append('| Ký hiệu | Vai trò | Tên nhân vật thể hiện | Đặc điểm giọng đọc |')
        lines.append('| :--- | :--- | :--- | :--- |')
        lines.append('| **H** | **Dẫn chuyện (Host)** | Cú (Host Amber Eyes) | Trầm ấm, lôi cuốn, sắc sảo, dẫn dắt thấu đáo (~48% thời lượng) |')
        lines.append('| **D** | **Điều tra viên** | Sói (Điều tra viên) | Nam trung niên, dày dạn kinh nghiệm, điềm tĩnh, đanh thép (~24% thời lượng) |')
        lines.append('| **C** | **Chuyên gia Tâm lý** | Cáo (Chuyên gia tâm lý) | Nữ sắc sảo, điềm đạm, khách quan, giàu hàm lượng khoa học hành vi (~22% thời lượng) |')
        lines.append('| **N** | **Người trong cuộc** | N1 (Cư dân Lincoln / Nạn nhân) · N2 (David Kaczynski) | Chân thực, hồi hộp, giằng xé lương tâm tột cùng (~6% thời lượng) |')
        lines.append('')
        lines.append('---')
        lines.append('')
    elif lang == 'EN':
        lines.append('# FORENSIC & CRIMINAL PSYCHOLOGY AUDIO SCRIPT')
        lines.append('**Topic:** 10 Psychological Markers & Forensic Behavioral Profiling – Case File: Ted Kaczynski (Unabomber).')
        lines.append('**Version:** Standard A2c/K10 – 10 Psychological Ecosystem Markers & Comprehensive Behavioral Analysis.')
        lines.append('')
        lines.append('---')
        lines.append('')
        lines.append('## PRODUCTION BRIEF & NARRATIVE STRUCTURE')
        lines.append('')
        lines.append('| Item | Standard Configuration (Host-Driven Documentary) |')
        lines.append('| :--- | :--- |')
        lines.append('| **Episode Title** | Ep. 31: TED KACZYNSKI – Intellectual Rage & Breakthrough in Forensic Linguistics |')
        lines.append('| **Format** | Narrator-led Investigative Documentary – The **Host** leads the narrative spine, orchestrating professional analyses (Investigator, Psychologist, Ordinary Person) at key psychological junctures. |')
        lines.append('| **Estimated Duration** | 28 – 32 minutes (5 narrative acts + sound transition pauses) |')
        lines.append('| **Voice Distribution** | Host (~48%), Investigator (~24%), Psychologist (~22%), Ordinary Person (~6%: N1 Resident/Victim, N2 David Kaczynski). |')
        lines.append('')
        lines.append('---')
        lines.append('')
    elif lang == 'JA':
        lines.append('# 犯罪心理学オーディオ／ポッドキャスト台本')
        lines.append('**テーマ:** 10の心理指標と法心理行動分析――事件記録: Ted Kaczynski (Unabomber)。')
        lines.append('**バージョン:** A2c/K10基準――犯罪心理学10の生態系指標と多角的心理変容分析。')
        lines.append('')
        lines.append('---')
        lines.append('')
        lines.append('## 制作仕様とナレーション構成（PRODUCTION BRIEF）')
        lines.append('')
        lines.append('| 項目 | 標準設定（ホスト主導型ドキュメンタリー） |')
        lines.append('| :--- | :--- |')
        lines.append('| **エピソード名** | 第31話 · TED KACZYNSKI――知性の怒りと法言語学の突破口 |')
        lines.append('| **形式** | 捜査ドキュメンタリーポッドキャスト――**ホスト**が物語の中心軸を担い、感情の起伏を制御しながら、節目ごとに専門家（捜査官、心理学者、一般人）の見解を招き入れます。 |')
        lines.append('| **推定所要時間** | 28～32分（本編5幕＋場面転換音響） |')
        lines.append('| **声の配分** | ホスト（約48%）、捜査官（約24%）、心理学者（約22%）、一般人（約6%: N1 住民/被害者、N2 デイヴィッド・カジンスキー）。 |')
        lines.append('')
        lines.append('---')
        lines.append('')

    role_map = {
        'VN': {'HOST': '**HOST**', 'INVESTIGATOR': '**ĐIỀU TRA VIÊN**', 'PSYCHOLOGIST': '**CHUYÊN GIA TÂM LÝ**', 'ORDINARY_PERSON': '**NGƯỜI BÌNH THƯỜNG**'},
        'EN': {'HOST': '**HOST**', 'INVESTIGATOR': '**INVESTIGATOR**', 'PSYCHOLOGIST': '**PSYCHOLOGIST**', 'ORDINARY_PERSON': '**ORDINARY PERSON**'},
        'JA': {'HOST': '**ホスト**', 'INVESTIGATOR': '**捜査官**', 'PSYCHOLOGIST': '**心理学者**', 'ORDINARY_PERSON': '**一般人**'}
    }

    act_prefix = {
        'VN': '## HỒI',
        'EN': '## ACT',
        'JA': '## 第'
    }

    for b in blocks:
        kind = b[0]
        if kind == 'ACT':
            act_num = b[1]
            title_vn, title_en, title_ja = b[2], b[3], b[4]
            lines.append('---')
            lines.append('')
            if lang == 'VN':
                lines.append(f'## HỒI {act_num}: {title_vn}')
            elif lang == 'EN':
                lines.append(f'## ACT {act_num}: {title_en}')
            elif lang == 'JA':
                lines.append(f'## 第{act_num}幕 {title_ja}')
            lines.append('')
        elif kind in ('BGM', 'SFX'):
            desc_vn, desc_en, desc_ja = b[2], b[3], b[4]
            if lang == 'VN':
                lines.append(f'**[{kind}]:** {desc_vn}')
            elif lang == 'EN':
                lines.append(f'**[{kind}]:** {desc_en}')
            elif lang == 'JA':
                lines.append(f'**[{kind}]:** {desc_ja}')
            lines.append('')
        elif kind == 'LOI':
            role = b[1]
            dir_vn = b[2]
            s_vn, s_en, s_ja = b[3], b[4], b[5]
            
            role_str = role_map[lang][role]
            # Direction
            if lang == 'VN':
                lines.append(f'{role_str} *({dir_vn})*:')
                for s in s_vn:
                    lines.append(s)
            elif lang == 'EN':
                # Simplified direction or English
                lines.append(f'{role_str} *({dir_vn})*:')
                for s in s_en:
                    lines.append(s)
            elif lang == 'JA':
                lines.append(f'{role_str} *({dir_vn})*:')
                for s in s_ja:
                    lines.append(s)
            lines.append('')

    return '\n'.join(lines)

def main():
    blocks = build_episode_data()
    
    vn_text = generate_script('VN', blocks)
    en_text = generate_script('EN', blocks)
    ja_text = generate_script('JA', blocks)
    
    with open('01_KICH_BAN/Tap31/kichban_tap31_19112026.md', 'w', encoding='utf-8') as f:
        f.write(vn_text)
    print('Generated Tap 31 VN script.')

    with open('01_KICH_BAN/Tap31_EN/kichban_tap31_EN.md', 'w', encoding='utf-8') as f:
        f.write(en_text)
    print('Generated Tap 31 EN script.')

    with open('01_KICH_BAN/Tap31_JA/kichban_tap31_JA.md', 'w', encoding='utf-8') as f:
        f.write(ja_text)
    print('Generated Tap 31 JA script.')

if __name__ == '__main__':
    main()
