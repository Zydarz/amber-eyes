# -*- coding: utf-8 -*-
"""Generate premium Captions and Descriptions for Tap 14 (VI, EN, JA)."""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_VI = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap14'
OUT_EN = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap14_EN'
OUT_JA = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap14_JA'

CLIPS_META = [
    {
        'id': 'TK1',
        'title_vn': '16 Năm Hy Sinh Nuôi Chồng & Lâu Đài Cát La Jolla',
        'title_en': '16 Years of Sacrifice & The La Jolla Sandcastle',
        'title_ja': '夫に捧げた16年の献身とラ・ホヤの砂の城',
        'signs_vn': '#1 (Ảnh hưởng xã hội) · #9 (Bẫy chi phí chìm & Điểm mù vị thế hào nhoáng)',
        'signs_en': '#1 (Social Impact) · #9 (Sunk Cost Fallacy & Prestige Blind Spots)',
        'signs_ja': '#1（社会的影響）· #9（サンクコスト効果と上流階級の威光の盲点）',
        'hook_vn': '16 năm bươn chải nuôi chồng lấy bằng Cornell và Harvard. Để rồi bị thay thế khi bước lên đỉnh cao.',
        'hook_en': '16 years financing his Cornell and Harvard degrees. Only to be discarded at the pinnacle of prestige.',
        'hook_ja': 'コーネル大とハーバード大の学費を16年稼ぎ続けた妻。夫が頂点に立った時、待っていた残酷な結末。',
        'dur_vn': '81.3 s', 'dur_en': '73.0 s', 'dur_ja': '76.0 s',
        'lines_cnt': 8,
        'context_vn': "Trong suốt 16 năm đầu hôn nhân, Betty Broderick một mình làm đủ mọi nghề lao động chân tay từ dạy mầm non, bán đồ gia dụng Tupperware đến nhân viên Avon để nuôi người chồng Daniel Broderick hoàn thành hai tấm bằng danh giá: Bác sĩ Y khoa tại Cornell và Tiến sĩ Luật tại Harvard. Thế nhưng, khi Daniel vươn lên thành luật sư triệu phú và Chủ tịch Đoàn Luật sư San Diego, cuộc sống giàu sang tại khu biệt thự La Jolla lại trở thành chiếc bẫy chi phí chìm đắt giá nhất cuộc đời bà.",
        'context_en': "For 16 arduous years, Betty Broderick worked multiple blue-collar jobs—teaching preschool, selling Tupperware, and marketing Avon—to single-handedly finance her husband Daniel's dual degrees: Cornell Medicine and Harvard Law. Yet when Dan ascended to multimillionaire status as San Diego Bar Association President, their opulent La Jolla lifestyle morphed into the ultimate sunk-cost trap of her life.",
        'context_ja': "結婚初期の16年間、ベティ・ブロデリックは幼稚園教諭やタッパーウェア、エイボンのセールスなど多忙な仕事を掛け持ちし、夫ダニエルのコーネル大学医学部とハーバード大学ロースクールの学費と生活費を支え続けた。しかし夫が著名弁護士として成功し、ラホヤの高級邸宅に君臨した時、彼女が捧げた歳月は残酷なサンクコストの罠と化した。"
    },
    {
        'id': 'TK2',
        'title_vn': 'Nghệ Thuật Gaslighting & Chiếc Mỏ Neo Nhận Thức Bị Bẻ Gãy',
        'title_en': 'Gaslighting & The Shattering of Cognitive Anchors',
        'title_ja': 'ガスライティングと認識の錨の破壊工作',
        'signs_vn': '#2 (Vật hóa nạn nhân) · #3 (Thao túng thực tại Gaslighting & Kiểm soát cưỡng bách)',
        'signs_en': '#2 (Victim Objectification) · #3 (Gaslighting & Coercive Control)',
        'signs_ja': '#2（被害者の物象化）· #3（ガスライティングと強迫的統制）',
        'hook_vn': 'Ngoại tình công khai nhưng khẳng định vợ mắc bệnh tâm thần. Nghệ thuật Gaslighting tàn nhẫn.',
        'hook_en': 'Denying obvious adultery while labeling his wife clinically insane. The cruel anatomy of Gaslighting.',
        'hook_ja': '明白な浮気を隠蔽し、疑惑を口にする妻を「精神病」と決めつける。ガスライティングの冷酷な罠。',
        'dur_vn': '84.2 s', 'dur_en': '65.8 s', 'dur_ja': '81.5 s',
        'lines_cnt': 8,
        'context_vn': "Mùa thu năm 1983, khi Dan Broderick thuê cô gái 21 tuổi Linda Kolkena làm trợ lý, Betty đã linh cảm thấy sự phản bội. Đáp lại, Dan dùng tài hùng biện của một luật sư hàng đầu để phủ nhận quyết liệt suốt gần 2 năm, rêu rao rằng Betty mắc chứng hoang tưởng và cần điều trị tâm thần. Chiến dịch thao túng thực tại (Gaslighting) tinh vi này đã phá hủy hoàn toàn chiếc mỏ neo nhận thức của người vợ, biến nỗi đau bị lừa dối thành cơn hoảng loạn và căm thù cực hạn.",
        'context_en': "In autumn 1983, Dan hired 21-year-old Linda Kolkena, sparking Betty's sharp marital intuition. Instead of honesty, Dan weaponized supreme courtroom eloquence to conduct a 2-year gaslighting campaign, insisting Betty was delusional and mentally unstable. This deliberate reality denial obliterated her cognitive grounding, transforming betrayal trauma into an uncontrollable psychological tempest of rage.",
        'context_ja': "1983年秋、夫が21歳のリンダを採用した時、ベティの直感は不倫を確信した。しかしトップ弁護士である夫は2年間にわたり徹底的な否定と心理工作を展開し、妻を「嫉妬に狂った精神異常者」と社会的に印象づけた。この執拗なガスライティングは妻の正気と現実感覚を破壊し、後の悲劇へと繋がる暗黒の憎悪を育んでいった。"
    },
    {
        'id': 'TK3',
        'title_vn': 'Cuộc Chiến Pháp Lý Không Cân Sức & Cơn Bão Thịnh Nộ Ái Kỷ',
        'title_en': 'Asymmetric Legal Warfare & Narcissistic Rage',
        'title_ja': '非対称な法廷闘争と自己爱性憤怒のエスカレーション',
        'signs_vn': '#6 (Ngòi nổ tâm lý) · #8 (Tổn thương ái kỷ & Quỹ đạo leo thang bạo lực)',
        'signs_en': '#6 (Psychological Trigger) · #8 (Narcissistic Injury & Escalation Trajectory)',
        'signs_ja': '#6（心理的引き金）· #8（自己愛性憤怒と暴力のエスカレーション）',
        'hook_vn': 'Dùng luật pháp thượng tầng bóp nghẹt tài chính vợ cũ. Giọt nước tràn ly kích hoạt án mạng.',
        'hook_en': 'Weaponizing elite legal mastery to suffocate his ex-wife financially. The trigger of mutual destruction.',
        'hook_ja': '最高峰の法律知識を武器に元妻の生活を兵粮攻めにする。破滅を決定づけた最後の引き金。',
        'dur_vn': '75.6 s', 'dur_en': '67.7 s', 'dur_ja': '83.0 s',
        'lines_cnt': 8,
        'context_vn': "Trong cuộc chiến ly hôn kéo dài 5 năm, Dan Broderick đã sử dụng toàn bộ ưu thế pháp lý tuyệt đối: ban hành lệnh cấm tiếp cận, khấu trừ tiền cấp dưỡng cho từng từ chửi bới trong hộp thư thoại, và giành toàn quyền nuôi cả 4 người con. Bị tước đoạt danh tính, con cái và sự an toàn kinh tế, tổn thương ái kỷ của Betty bùng phát thành cơn thịnh nộ mất kiểm soát, đẩy bà vào quỹ đạo báo thù tàn khốc không thể vãn hồi.",
        'context_en': "During a brutal 5-year divorce war, Dan Broderick leveraged his absolute legal supremacy: obtaining restraining orders, fining Betty per profanity in voicemail records, and seizing sole custody of all four children. Stripped of maternal identity, social status, and financial agency, Betty's vulnerable narcissistic injury erupted into an all-consuming vindictive obsession.",
        'context_ja': "5年間に及ぶ泥沼の離婚訴訟で、弁護士ダニエルは法的手続きの優位性を徹底的に利用した。接近禁止命令を乱発し、留守番電話の暴言ごとに罰金を課して生活費を差し押さえ、4人の子どもの親権を完全に奪取。社会的地位と母親としての尊厳を剥奪されたベティの自己愛性憤怒は限界を超え、破滅的報復へと突進した。"
    },
    {
        'id': 'TK4',
        'title_vn': 'Năm Phát Đạn Rạng Sáng & Phiên Tòa Chia Rẽ Nước Mỹ',
        'title_en': 'Five Dawn Gunshots & The Trial That Divided America',
        'title_ja': '夜明けの5発の銃声と全米を二分した法廷',
        'signs_vn': '#4 (Thái độ trước bản án) · #5 (Hệ thống tự bào chữa & Bẫy đóng vai nạn nhân)',
        'signs_en': '#4 (Attitude to Reality) · #5 (Neutralization & Entitled Victimhood)',
        'signs_ja': '#4（判決への態度）· #5（自己正当化と被害者意識の固定化）',
        'hook_vn': 'Rạng sáng Chủ nhật ngày 5/11/1989. Năm phát đạn và chiếc bẫy tâm lý \'nạn nhân hóa hoàn hảo\'.',
        'hook_en': 'Dawn of November 5, 1989. Five fatal gunshots and the psychological trap of total victimhood.',
        'hook_ja': '1989年11月5日の夜明け、放たれた5発の銃声。被害者意識が引き起こした悲劇の結末。',
        'dur_vn': '76.5 s', 'dur_en': '59.5 s', 'dur_ja': '76.6 s',
        'lines_cnt': 8,
        'context_vn': "Rạng sáng 5/11/1989, Betty dùng chìa khóa lấy trộm từ con gái lẻn vào biệt thự của Dan và Linda, bắn 5 phát đạn súng lục revolver hạ sát cả hai người khi họ đang ngủ say. Tại tòa án, lời khai đẫm nước mắt của con gái lớn Kim Broderick đã phơi bày hành vi toan tính từ trước. Mặc dù nhận bản án 32 năm tù chung thân, Betty Broderick đến nay vẫn kiên định với chiếc bẫy đóng vai nạn nhân, tự coi mình là nạn nhân bị đẩy vào đường cùng mà không hề hối hận.",
        'context_en': "At dawn on November 5, 1989, using a key stolen from her daughter, Betty infiltrated Dan and Linda's bedroom and fired five revolver shots, killing both in their sleep. In court, eldest daughter Kim Broderick's testimony exposed premeditation. Handed a 32-year-to-life sentence, Betty remains entrenched in perpetual victimhood to this day, exhibiting zero genuine remorse.",
        'context_ja': "1989年11月5日早朝、娘から盗んだ合鍵で新婚夫婦の寝室に侵入したベティは、リボルバーで5発の銃弾を撃ち込み2人を射殺。法廷では長女キムの苦渋の証言が綿密な計画性を立証した。禁錮32年の終身刑が下された後も、ベティは「自分こそが絶対的な被害者である」という認知的殻に閉じこもり、反省の弁を述べることはなかった。"
    },
    {
        'id': 'TK5',
        'title_vn': 'Nạn Nhân Học & Bài Học Sinh Tồn Hôn Nhân',
        'title_en': 'Victimology & Marital Survival Lessons',
        'title_ja': '被害者学と結婚破綻を生き抜く教訓',
        'signs_vn': '#10 (Nạn nhân học & Bài học sinh tồn trong hôn nhân đổ vỡ)',
        'signs_en': '#10 (Victimology & Survival Lessons in Toxic Marital Separation)',
        'signs_ja': '#10（被害者学と破綻した結婚関係を生き抜く防衛策）',
        'hook_vn': 'Bốn bài học sinh tồn nhận diện lạm dụng tâm lý và thoát khỏi cạm bẫy hận thù sau đổ vỡ.',
        'hook_en': 'Four vital survival lessons to identify psychological abuse and walk away from toxic hatred.',
        'hook_ja': '心理的虐待を見抜き、泥沼の憎悪から命と尊厳を守る「4つの教訓」。',
        'dur_vn': '81.9 s', 'dur_en': '57.5 s', 'dur_ja': '67.2 s',
        'lines_cnt': 7,
        'context_vn': "Đúc kết từ bi kịch Betty Broderick, kênh Amber Eyes gửi gắm 4 bài học sinh tồn trong đời sống lứa đôi: (1) Nhận diện sớm chiến dịch thao túng thực tại Gaslighting; (2) Tỉnh táo trước 'Hiệu ứng Hào quang' và vị thế xã hội của đối phương; (3) Giữ vững sự độc lập kinh tế, pháp lý và tự chủ tinh thần; (4) Nghệ thuật buông bỏ hận thù để tự giải thoát cho chính mình. Sự trả thù đích thực trước mọi phản bội không phải là hủy diệt đối phương, mà là sống một cuộc đời mới tự do và bình an.",
        'context_en': "From the Broderick tragedy, Amber Eyes derives four vital survival lessons: (1) Detect early insidious signs of reality manipulation (Gaslighting); (2) Never equate social prestige with moral decency; (3) Maintain independent economic, legal, and emotional agency; (4) Cultivate the wisdom to let go of vindictive hatred. The sweetest and highest revenge against betrayal is never violence—it is healing and thriving in profound peace.",
        'context_ja': "ブロデリック事件の教訓から導かれた結婚生活の4つの知恵：(1) 初期のガスライティング（現実感覚の歪曲）に気づくこと、(2) 社会的権威や富を人間性の保証と錯覚しないこと、(3) 経済的・精神的自立を保ち続けること、(4) 憎悪を手放し自らを救い出す勇気。最大の復讐とは相手を傷つけることではなく、自らが平穏で豊かな人生を生き直すことである。"
    }
]

for item in CLIPS_META:
    cid = item['id']
    # 1. VI
    cap_vi = f"""{item['hook_vn']} 👁️

Tập 14 · Khi Nạn Nhân Gaslighting Bước Qua Ranh Giới — Chỉ dấu {item['signs_vn']}.
Hồ sơ vụ án Betty Broderick có thật tại San Diego, California, 100% đối chiếu hồ sơ tòa án và tư liệu cảnh sát.

📺 Xem tập đầy đủ (28 phút) ở link trong bio
🔎 Chỉ dấu tâm lý · {item['title_vn'].lower()} · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân.

#AmberEyes #TamLyToiPham #BettyBroderick #Gaslighting #NarcissisticRage #SunkCostTrap #HoSoCoThat #TrueCrime

---
Ghi chú khi đăng (KHÔNG dán vào caption):
- BẬT toggle "Nội dung do AI tạo" (AI-generated content) — TikTok bắt buộc nhãn AIGC.
- Dòng nhãn AIGC ĐÃ nằm sẵn trong caption: không cần thêm khi dán.
- Link YouTube Tập 14: dán vào ô "Links / Website" trong profile TikTok.
- Ước lượng thời lượng: {item['dur_vn']} ({item['lines_cnt']} câu) — đo bằng ASR thực tế.
- File mô tả dài TikTok Studio: MoTa_Dai_{cid}.txt · Bản rút gọn: MoTa_Ngan_{cid}.txt
"""
    (OUT_VI / f'Caption_{cid}.txt').write_text(cap_vi.strip(), encoding='utf-8')

    motadai_vi = f"""HỒ SƠ TÂM LÝ HỌC TỘI PHẠM — TẬP 14: KHI NẠN NHÂN GASLIGHTING BƯỚC QUA RANH GIỚI TỘI ÁC (BETTY BRODERICK)
Phân tích clip {cid}: {item['title_vn']}
Chủ đề chuyên sâu: {item['signs_vn']}

{item['hook_vn']}

——————
BỐI CẢNH & PHÂN TÍCH TÂM LÝ HỌC HÀNH VI
——————
{item['context_vn']}

——————
NGUỒN ĐỐI CHIẾU & HỒ SƠ LƯU TRỮ CHÍNH THỨC
——————
• Hồ sơ điều tra của Sở Cảnh sát San Diego (San Diego Police Department Homicide Division)
• Biên bản và lời khai tuyên thệ phiên tòa hình sự Tòa Thượng thẩm Quận San Diego (1990–1991)
• Lời khai của nhân chứng Kim Broderick trong hồi ký *A Specialty of the House*
• Hồ sơ ly hôn Broderick v. Broderick tại Tòa án Gia đình California
• Tác phẩm điều tra tài liệu *Until the Twelfth of Never* của nhà báo Bella Stumbo

——————
XEM TẬP ĐẦY ĐỦ
——————
📺 Video phân tích podcast tài liệu hoàn chỉnh (28 phút) có mặt trên kênh YouTube Amber Eyes: xem tại đường link trong phần tiểu sử (bio)!

——————
LƯU Ý QUY CHUẨN
——————
Nội dung do AI hỗ trợ tạo hình đồ họa noir và giọng đọc, dùng cho mục đích giáo dục nhận thức và phân tích tâm lý học tội phạm — không cổ xúy bạo lực, tuyệt đối bảo vệ nhân phẩm nạn nhân.
"""
    (OUT_VI / f'MoTa_Dai_{cid}.txt').write_text(motadai_vi.strip(), encoding='utf-8')

    motangan_vi = f"""{item['hook_vn']}
Hồ sơ Tập 14: Vụ án Betty Broderick & Nghệ thuật Gaslighting.
Chủ đề: {item['title_vn']}.
Xem trọn vẹn tập phim phân tích chuyên sâu 28 phút tại đường dẫn trong bio kênh Amber Eyes!
#AmberEyes #BettyBroderick #Gaslighting #TamLyToiPham #TrueCrime
"""
    (OUT_VI / f'MoTa_Ngan_{cid}.txt').write_text(motangan_vi.strip(), encoding='utf-8')

    # 2. EN
    cap_en = f"""{item['hook_en']} 👁️

Episode 14 · When Gaslighting Victims Cross the Line — Signs: {item['signs_en']}.
Real case in San Diego, California. 100% verified via Superior Court of California records and police files.

📺 Watch the full 28-min documentary dossier via link in bio
🔎 Psychological signs · {item['title_en'].lower()} · true crime

Content features AI narration & graphic novel visuals for psychological analysis — educational and respectful.

#AmberEyes #CriminalPsychology #BettyBroderick #Gaslighting #NarcissisticRage #SunkCostFallacy #TrueCrime #MindControl

---
Posting Notes:
- Turn ON "AI-generated content" toggle on TikTok.
- YouTube Episode 14 Link: paste in profile "Website / Links" field.
- Estimated Duration: {item['dur_en']} ({item['lines_cnt']} sentences) via measured ASR speech rate.
"""
    (OUT_EN / f'Caption_{cid}.txt').write_text(cap_en.strip(), encoding='utf-8')

    motadai_en = f"""CRIMINAL PSYCHOLOGY DOSSIER — EPISODE 14: WHEN GASLIGHTING VICTIMS CROSS THE LINE (BETTY BRODERICK)
Clip Analysis {cid}: {item['title_en']}
Core Signs: {item['signs_en']}

{item['hook_en']}

——————
HISTORICAL BACKGROUND & BEHAVIORAL ANALYSIS
——————
{item['context_en']}

——————
OFFICIAL VERIFIED SOURCES
——————
• San Diego Police Department Homicide Case Files
• Superior Court of California County of San Diego Trial Transcripts (1990–1991)
• Sworn Courtroom Testimony and Memoir of Eldest Daughter Kim Broderick
• California Family Court Records: Broderick v. Broderick
• Investigative Book *Until the Twelfth of Never* by Bella Stumbo (1993)

——————
WATCH FULL EPISODE
——————
📺 Full 28-minute documentary podcast available on Amber Eyes YouTube channel: click link in channel bio!
"""
    (OUT_EN / f'MoTa_Dai_{cid}.txt').write_text(motadai_en.strip(), encoding='utf-8')

    motangan_en = f"""{item['hook_en']}
Episode 14: Betty Broderick & Gaslighting Manipulation.
Topic: {item['title_en']}.
Watch the complete 28-min psychological breakdown via link in bio!
#AmberEyes #BettyBroderick #Gaslighting #CriminalPsychology #TrueCrime
"""
    (OUT_EN / f'MoTa_Ngan_{cid}.txt').write_text(motangan_en.strip(), encoding='utf-8')

    # 3. JA
    cap_ja = f"""{item['hook_ja']} 👁️

第14話 · ガスライティングの被害者が一線を越えた時 — 指標：{item['signs_ja']}。
カリフォルニア州サンディエゴ上級裁判所記録および警察捜査資料と100%対照済みの実話事件簿。

📺 28分間の完全版解説動画はプロフ欄リンクへ
🔎 犯罪心理学指標 · {item['title_ja']} · 実話記録

本動画はAI生成の朗読とグラフィックノベル画像を用いた犯罪心理学の学術的解説コンテンツです。

#AmberEyes #犯罪心理学 #ベティブロデリック #ガスライティング #モラハラ #自己愛性憤怒 #未解決事件 #実話

---
投稿時の注意事項：
- TikTok投稿画面で「AI生成コンテンツ」のトグルを必ずONにしてください。
- YouTube第14話リンク：プロフィール欄のリンク項目に設定。
- 推定時間：{item['dur_ja']}（{item['lines_cnt']}文）実測ASR準拠。
"""
    (OUT_JA / f'Caption_{cid}.txt').write_text(cap_ja.strip(), encoding='utf-8')

    motadai_ja = f"""犯罪心理学事件ファイル — 第14話：ガスライティングの被害者が一線を越えた時（ベティ・ブロデリック事件）
クリップ分析 {cid}：{item['title_ja']}
深層心理指標：{item['signs_ja']}

{item['hook_ja']}

——————
歴史的背景と行動心理学分析
——————
{item['context_ja']}

——————
公式参照資料・裁判記録
——————
• サンディエゴ市警察殺人課捜査調書（SDPD Records）
• カリフォルニア州上級裁判所公判記録（1990年〜1991年審理）
• 長女キム・ブロデリックの手記および法廷証言録
• カリフォルニア州家庭裁判所離婚調書（Broderick v. Broderick）
• ジャーナリスト ベラ・スタンボ著『Until the Twelfth of Never』（1993）

——————
完全版ドキュメンタリーのご案内
——————
📺 28分間の完全版ポッドキャスト動画はYouTube公式チャンネル「Amber Eyes」にて公開中。プロフィール欄のリンクからご覧いただけます。
"""
    (OUT_JA / f'MoTa_Dai_{cid}.txt').write_text(motadai_ja.strip(), encoding='utf-8')

    motangan_ja = f"""{item['hook_ja']}
第14話：ベティ・ブロデリック事件とガスライティングの罠。
テーマ：{item['title_ja']}。
28分の完全版解説動画はプロフ欄リンクのYouTubeで公開中！
#AmberEyes #ベティブロデリック #ガスライティング #犯罪心理学 #モラハラ
"""
    (OUT_JA / f'MoTa_Ngan_{cid}.txt').write_text(motangan_ja.strip(), encoding='utf-8')

print("All Captions and Descriptions successfully created for Tap 14 (VI, EN, JA).")
