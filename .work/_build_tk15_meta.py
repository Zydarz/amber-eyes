# -*- coding: utf-8 -*-
"""Generate premium Captions and Descriptions for Tap 15 (VI, EN, JA)."""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_VI = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap15'
OUT_EN = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap15_EN'
OUT_JA = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap15_JA'

CLIPS_META = [
    {
        'id': 'TK1',
        'title_vn': 'Bí Ẩn Chiếc Máy Giặt & Dữ Liệu Kỹ Thuật Số',
        'title_en': 'The Washing Machine Mystery & Digital Forensic Evidence',
        'title_ja': '洗濯機の謎と復元されたデジタル鑑識データ',
        'signs_vn': '#7 (Thủ đoạn gây án MO) · #8 (Dấu ấn Signature & Bằng chứng kỹ thuật số)',
        'signs_en': '#7 (MO vs. Signature) · #8 (Digital Forensic Reconstruction)',
        'signs_ja': '#7（手口MO対署名Signature）· #8（デジタルフォレンジックの決定打）',
        'hook_vn': 'Ném máy ảnh vào máy giặt đang chạy nước để phi tang. Nhưng dữ liệu số không bao giờ nói dối.',
        'hook_en': 'Submerging the camera inside a running washing machine. But digital data never lies.',
        'hook_ja': '証拠隠滅のため洗濯機に沈められたカメラ。しかしデジタル鑑識は嘘をつかない。',
        'dur_vn': '69.2 s', 'dur_en': '66.0 s', 'dur_ja': '73.0 s',
        'lines_cnt': 9,
        'context_vn': "Tại hiện trường căn nhà ở Mesa (Arizona) vào mùa hè năm 2008, thủ phạm đã tìm mọi cách dọn dẹp hiện trường nhằm xóa dấu vết. Điều kỳ lạ nhất nằm ở phòng giặt là: một chiếc máy ảnh kỹ thuật số Sony Cyber-shot bị vứt chìm dưới đáy lồng giặt ngập nước đang hoạt động. Tuy nhiên, các chuyên gia phục hồi dữ liệu số đã phục hồi được toàn bộ các bức ảnh bị xóa thủ công: bức ảnh cuối cùng chụp nạn nhân lúc 17 giờ 29 phút chiều, và chỉ ít phút sau là các khung hình hỗn loạn để lộ chính diện Jodi Arias, loại bỏ hoàn toàn khả năng có kẻ thứ ba.",
        'context_en': "At the Mesa, Arizona crime scene in summer 2008, the perpetrator attempted an aggressive cleanup to eliminate evidence. The most bizarre discovery was inside the laundry room: a Sony Cyber-shot digital camera submerged beneath water in an active washing machine cycle. Forensic digital analysts successfully recovered all manually deleted photos: the final picture of Travis alive at 5:29 PM in the shower, followed minutes later by accidental chaotic frames capturing Jodi Arias herself, completely ruling out third-party intruders.",
        'context_ja': "2008年夏、アリゾナ州メサの現場で犯人は徹底的な証拠隠滅を図った。最も異様だったのは洗濯機の中：作動中の洗濯機の底にソニー製デジタルカメラが沈められていた。しかし鑑識班は手動消去された全データを秒単位で復元。午後5時29分に浴室で撮影された被害者の最後の姿と、その数分後に誤って撮影されたジョディ・アリアス自身の姿が写っており、第三者侵入の可能性は完全に粉砕された。"
    },
    {
        'id': 'TK2',
        'title_vn': 'Hành Trình Xuyên Sa Mạc & Ba Can Xăng Bí Mật',
        'title_en': 'Desert Crossing & The Three Secret Gas Cans',
        'title_ja': '砂漠越えのルートと3つの秘密のガソリン携行缶',
        'signs_vn': '#7 (Thủ đoạn xóa dấu vết) · #8 (Sự toan tính ngoại phạm tinh vi & Lạnh lùng)',
        'signs_en': '#7 (Alibi Fabrication) · #8 (Chilling Premeditation & Route Concealment)',
        'signs_ja': '#7（アリバイ偽装工作）· #8（冷酷な事前計画と電子足跡遮断）',
        'hook_vn': 'Nhuộm tóc, tắt điện thoại, mang ba can xăng qua sa mạc. Sự toan tính lạnh lùng rùng mình.',
        'hook_en': 'Dyed hair, powered-off phone, three gas cans across the desert. A chillingly premeditated journey.',
        'hook_ja': '黒染めした髪、切られた携帯電源、3つのガソリン缶。戦慄の完全犯罪計画。',
        'dur_vn': '56.7 s', 'dur_en': '64.6 s', 'dur_ja': '73.8 s',
        'lines_cnt': 8,
        'context_vn': "Để thực hiện chuyến đi định mệnh tới Arizona, Jodi Arias đã lên một kế hoạch che giấu dấu vết tỉ mỉ: thuê xe hơi tại Redding (California), mượn và mua 3 can xăng dự trữ để vượt hàng nghìn dặm sa mạc mà không để lại bất kỳ giao dịch quẹt thẻ tín dụng nào tại bang Arizona. Cô ta nhuộm tóc sang màu nâu sẫm, tắt nguồn điện thoại di động suốt chuyến đi, và sau khi gây án lập tức lái xe sang Utah gặp bạn trai mới với nụ cười rạng rỡ, đồng thời để lại tin nhắn thoại tìm kiếm Travis để dựng chứng cứ ngoại phạm hoàn hảo.",
        'context_en': "To execute her deadly trek to Arizona, Jodi Arias executed an elaborate concealment scheme: renting a car in Redding, California, acquiring three spare gas cans to cross thousands of desert miles without leaving a single credit card transaction in Arizona. She dyed her hair dark brown, kept her mobile phone powered off to defeat cell tower pings, and immediately sped to Utah to meet another romantic partner with cheerful smiles, leaving sweet voicemails on Travis's phone to fabricate an ironclad alibi.",
        'context_ja': "アリゾナへの移動にあたり、ジョディは緻密な足跡隠蔽計画を実行した。カリフォルニアでレンタカーを借り、ガソリン携行缶3つを携行してアリゾナ州内でのクレジットカード決済履歴を完全回避。髪を黒く染めて人相を変え、移動中は携帯電話の電源を切って基地局追跡を遮断。犯行後は直ちにユタ州へ向かい別の男性と笑顔で密会、被害者の携帯に甘いメッセージを残して完璧なアリバイを偽装した。"
    },
    {
        'id': 'TK3',
        'title_vn': 'Rối Loạn Ranh Giới (BPD) & Cơn Cuồng Nộ Bị Ruồng Bỏ',
        'title_en': 'Borderline Personality Disorder & Abandonment Rage',
        'title_ja': '境界性パーソナリティ障害（BPD）と見捨てられ不安の暴走',
        'signs_vn': '#6 (Ngòi nổ tâm lý) · #8 (Tư duy phân tách Splitting & Gắn kết chấn thương)',
        'signs_en': '#6 (Psychological Trigger) · #8 (BPD Splitting & Trauma Bonding Escalation)',
        'signs_ja': '#6（心理的引き金）· #8（白黒思考スプリッティングとトラウマ性愛着）',
        'hook_vn': 'Yêu say đắm buổi sáng, muốn hủy diệt buổi chiều. Giải mã tâm lý rối loạn nhân cách ranh giới.',
        'hook_en': 'Idolized in the morning, dehumanized by evening. Unraveling Borderline Personality Disorder.',
        'hook_ja': '朝の崇拝から夕方の破壊願望へ。境界性パーソナリティ障害（BPD）が引き起こす激動の深層心理。',
        'dur_vn': '62.9 s', 'dur_en': '62.1 s', 'dur_ja': '81.6 s',
        'lines_cnt': 8,
        'context_vn': "Kết luận giám định tâm thần lâm sàng tại tòa án khẳng định Jodi Arias mắc Rối loạn nhân cách ranh giới (BPD) kết hợp với các nét ái kỷ độc hại. Đặc trưng của hội chứng này là nỗi sợ hãi tột cùng trước nguy cơ bị ruồng bỏ và cơ chế tư duy phân tách trắng đen (Splitting): coi đối phương là vị thánh hoàn hảo vào buổi sáng nhưng lập tức biến họ thành quỷ dữ cần tiêu diệt khi bị từ chối. Mối quan hệ gắn kết chấn thương (Trauma bonding) đẩy cảm xúc yêu - hận xoay vòng cho đến khi bùng nổ thành cơn thịnh nộ hủy diệt tàn bạo.",
        'context_en': "Forensic clinical psychiatric evaluations confirmed Jodi Arias suffered from Borderline Personality Disorder (BPD) compounded by malignant narcissistic traits. The hallmark of BPD is an overwhelming terror of real or perceived abandonment, mediated by the cognitive defense mechanism of 'Splitting'—idolizing a partner as divine perfection one moment, then vilifying them as pure evil upon facing rejection. Their intense trauma bonding created an addictive push-pull cycle that ultimately culminated in lethal narcissistic rage.",
        'context_ja': "法廷精神医学鑑定により、ジョディ・アリアスは境界性パーソナリティ障害（BPD）と病的自己愛の特徴を併せ持つと診断された。BPDの中核は異常なまでの「見捨てられ不安」と「白黒思考（スプリッティング）」であり、相手を完璧な救済者として崇拝した直後、拒絶されるや否や絶対悪として憎悪する。トラウマ性愛着による激しい愛憎の反復が、最終的に制御不能な破壊的憤怒を爆発させた。"
    },
    {
        'id': 'TK4',
        'title_vn': 'Trò Ảo Thuật Phòng Thẩm Vấn & Phiên Tòa Truyền Hình',
        'title_en': 'Interrogation Room Acrobatics & The Media Trial',
        'title_ja': '取調室の三面記事的茶番と全米中継法廷',
        'signs_vn': '#4 (Thái độ trước bản án) · #5 (Kỹ thuật trung hòa đạo đức & Tự thương hại bệnh lý)',
        'signs_en': '#4 (Attitude to Reality) · #5 (Neutralization Theory & Pathological Self-Pity)',
        'signs_ja': '#4（判決への態度）· #5（中和の技術と病的自己憐憫の涙）',
        'hook_vn': 'Trồng cây chuối trong phòng hỏi cung, liên tục đổi kịch bản lời khai. Nước mắt của sự hối hận hay toan tính?',
        'hook_en': 'Doing headstands inside police interrogation, constantly shifting stories. Genuine tears or cold manipulation?',
        'hook_ja': '取調室での逆立ち、二転三転する供述。法廷で見せた涙は真の悔悟か、それとも計算された演技か？',
        'dur_vn': '67.2 s', 'dur_en': '67.2 s', 'dur_ja': '79.3 s',
        'lines_cnt': 8,
        'context_vn': "Trong suốt quá trình bị điều tra và xét xử, Jodi Arias liên tục thay đổi lời khai: ban đầu phủ nhận không đến Arizona, sau đó bịa ra câu chuyện hai kẻ lạ mặt đeo mặt nạ đột nhập, và cuối cùng nhận tội nhưng ngụy biện là hành vi tự vệ. Trong phòng hỏi cung khi chỉ có một mình, cô ta hát nghêu ngao và thậm chí trồng cây chuối trước camera giám sát. Tại phiên tòa truyền hình năm 2013 thu hút hàng triệu khán giả, những giọt nước mắt thực chất là hiện tượng 'Tự thương hại bệnh lý' khi cái tôi ái kỷ bị bóc trần, hoàn toàn thiếu vắng sự ăn năn chân thành.",
        'context_en': "Throughout the investigation and sensational 2013 trial, Jodi Arias repeatedly morphed her narratives: initially denying presence in Arizona, then inventing two fictitious masked intruders, and ultimately claiming battered self-defense when physical evidence left no escape. Left alone in interrogation, she sang and performed headstands before CCTV cameras. Her dramatic courtroom weeping embodied clinical 'pathological self-pity' as her omnipotent facade collapsed, wholly devoid of authentic remorse for the lost life.",
        'context_ja': "捜査と公判を通じて、ジョディの供述は変遷を極めた。「アリゾナには行っていない」という全面否定から「覆面強盗2人組の襲撃」、最終的には「正当防衛」の主張へ。取調室で1人残された際には監視カメラの前で逆立ちや独唱を行うなど異様な行動を記録された。全米が注目した2013年の裁判で見せた涙は、自己愛の虚飾が崩壊したことへの「病的自己憐憫」であり、奪われた命への真摯な悔悟は最後まで存在しなかった。"
    },
    {
        'id': 'TK5',
        'title_vn': 'Nạn Nhân Học & 4 Cảnh Báo Đỏ Mối Quan Hệ Ám Ảnh',
        'title_en': 'Victimology & 4 Red Flags of Obsessive Relationships',
        'title_ja': '被害者学と執着型関係の4つの危険信号',
        'signs_vn': '#10 (Nạn nhân học & Cảnh báo đỏ sinh tồn — Gavin de Becker)',
        'signs_en': '#10 (Victimology & Lethal Relationship Red Flags — The Gift of Fear)',
        'signs_ja': '#10（被害者学と破滅的な愛着関係から身を守る警告サイン）',
        'hook_vn': 'Bốn tín hiệu cảnh báo đỏ nhận diện kẻ săn mồi tâm lý ám ảnh để bảo vệ sinh mạng bản thân.',
        'hook_en': 'Four vital survival red flags to detect obsessive psychological predators and save your life.',
        'hook_ja': '執着型パーソナリティの罠を見抜き、生命と尊厳を守る「4つの危険信号」。',
        'dur_vn': '66.8 s', 'dur_en': '60.3 s', 'dur_ja': '70.9 s',
        'lines_cnt': 9,
        'context_vn': "Đúc kết từ thảm kịch Jodi Arias và tác phẩm kinh điển 'Món quà của nỗi sợ hãi' của Gavin de Becker, khoa học hành vi chỉ ra 4 tín hiệu cảnh báo đỏ sinh tồn: (1) Sự lý tưởng hóa dồn dập kết hợp với Hiệu ứng Tắc kè hoa (sao chép sở thích, thay đổi tôn giáo quá nhanh); (2) Xâm phạm ranh giới cá nhân và theo dõi vi tế; (3) Tư duy phân tách trắng đen và cảm xúc biến thiên cực đoan; (4) Hành vi đe dọa, rạch lốp xe hoặc phá hoại tài sản khi đối diện với nguy cơ chia tay. Trực giác bất an là chiếc khiên tự vệ sinh học quý giá nhất giúp bạn dũng cảm bước ra khỏi mối quan hệ độc hại.",
        'context_en': "Drawing from the Jodi Arias tragedy and Gavin de Becker's 'The Gift of Fear', behavioral science outlines 4 vital survival red flags: (1) Rapid idolization combined with Chameleon mimicry (copying hobbies and beliefs unnaturally fast); (2) Boundary erosion and covert surveillance; (3) Black-and-white splitting cognition and violent emotional swings; (4) Property damage, tire slashing, and explicit separation threats. Uncomfortable intuition is humanity's greatest biological defense mechanism to walk away before it is too late.",
        'context_ja': "ジョディ・アリアス事件とギャヴィン・ド・ベッカーの『The Gift of Fear』から導かれた生存のための4つの警告サイン：(1) 急激な理想化とカメレオン的同一化（趣味や信条の不自然な模倣）、(2) 境界線の侵害と日常的な監視、(3) 白黒思考と極端な感情の乱高下、(4) 別れに直面した際の脅迫やタイヤのパンク等の器物損壊。違和感を告げる直感こそ、自らの生命を守る最も強力な生物学的防衛機能である。"
    }
]

for item in CLIPS_META:
    cid = item['id']
    # 1. VI
    cap_vi = f"""{item['hook_vn']} 👁️

Tập 15 · Cơn Cuồng Ghen Rối Loạn Ranh Giới — Chỉ dấu {item['signs_vn']}.
Hồ sơ vụ án Jodi Arias có thật tại Mesa, Arizona, 100% đối chiếu hồ sơ điều tra Sở Cảnh sát Mesa và phiên tòa Hạt Maricopa.

📺 Xem tập đầy đủ (28 phút) ở link trong bio
🔎 Chỉ dấu tâm lý · {item['title_vn'].lower()} · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân.

#AmberEyes #TamLyToiPham #JodiArias #BPD #Borderline #TheGiftOfFear #Splitting #HoSoCoThat #TrueCrime

---
Ghi chú khi đăng (KHÔNG dán vào caption):
- BẬT toggle "Nội dung do AI tạo" (AI-generated content) — TikTok bắt buộc nhãn AIGC.
- Dòng nhãn AIGC ĐÃ nằm sẵn trong caption: không cần thêm khi dán.
- Link YouTube Tập 15: dán vào ô "Links / Website" trong profile TikTok.
- Ước lượng thời lượng: {item['dur_vn']} ({item['lines_cnt']} câu) — đo bằng ASR thực tế.
- File mô tả dài TikTok Studio: MoTa_Dai_{cid}.txt · Bản rút gọn: MoTa_Ngan_{cid}.txt
"""
    (OUT_VI / f'Caption_{cid}.txt').write_text(cap_vi.strip(), encoding='utf-8')

    motadai_vi = f"""HỒ SƠ TÂM LÝ HỌC TỘI PHẠM — TẬP 15: CƠN CUỒNG GHEN RỐI LOẠN NHÂN CÁCH RANH GIỚI (JODI ARIAS)
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
• Hồ sơ điều tra của Sở Cảnh sát Mesa, bang Arizona (Mesa Police Department Homicide Files)
• Báo cáo giám định kỹ thuật số thẻ nhớ máy ảnh Sony Cyber-shot (Cục Điều tra Hình sự Arizona)
• Biên bản và lời khai tuyên thệ phiên tòa hình sự Tòa Thượng thẩm Hạt Maricopa (2013 & 2015)
• Kết luận giám định tâm thần lâm sàng về Rối loạn nhân cách ranh giới (Dr. Janeen DeMarte)
• Tác phẩm điều tra tài liệu *Picture Perfect: The Jodi Arias Story* của nhà báo Shanna Hogan (2013)

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
Hồ sơ Tập 15: Vụ án Jodi Arias & Rối loạn nhân cách ranh giới BPD.
Chủ đề: {item['title_vn']}.
Xem trọn vẹn tập phim phân tích chuyên sâu 28 phút tại đường dẫn trong bio kênh Amber Eyes!
#AmberEyes #JodiArias #BPD #TamLyToiPham #TheGiftOfFear
"""
    (OUT_VI / f'MoTa_Ngan_{cid}.txt').write_text(motangan_vi.strip(), encoding='utf-8')

    # 2. EN
    cap_en = f"""{item['hook_en']} 👁️

Episode 15 · Borderline Personality & Fatal Obsession — Signs: {item['signs_en']}.
Real case in Mesa, Arizona. 100% verified via Mesa Police Department evidence & Maricopa County Superior Court records.

📺 Watch the full 28-min documentary dossier via link in bio
🔎 Psychological signs · {item['title_en'].lower()} · true crime

Content features AI narration & graphic novel visuals for psychological analysis — educational and respectful.

#AmberEyes #CriminalPsychology #JodiArias #BPD #Borderline #TheGiftOfFear #TrueCrime #MindControl

---
Posting Notes:
- Turn ON "AI-generated content" toggle on TikTok.
- YouTube Episode 15 Link: paste in profile "Website / Links" field.
- Estimated Duration: {item['dur_en']} ({item['lines_cnt']} sentences) via measured ASR speech rate.
"""
    (OUT_EN / f'Caption_{cid}.txt').write_text(cap_en.strip(), encoding='utf-8')

    motadai_en = f"""CRIMINAL PSYCHOLOGY DOSSIER — EPISODE 15: BORDERLINE PERSONALITY DISORDER & FATAL OBSESSION (JODI ARIAS)
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
• Mesa Police Department Homicide Investigation Case Files (Mesa, Arizona)
• Forensic Digital Evidence & Timestamp Recovery Report (Sony Cyber-shot Memory Card)
• Superior Court of Arizona in Maricopa County Trial Records & Transcripts (State of Arizona v. Jodi Ann Arias)
• Clinical Psychological & Psychiatric Forensic Evaluations on Borderline Personality Disorder (Dr. Janeen DeMarte)
• Investigative Work *Picture Perfect: The Jodi Arias Story* by Shanna Hogan (2013)

——————
WATCH FULL EPISODE
——————
📺 Full 28-minute documentary podcast available on Amber Eyes YouTube channel: click link in channel bio!
"""
    (OUT_EN / f'MoTa_Dai_{cid}.txt').write_text(motadai_en.strip(), encoding='utf-8')

    motangan_en = f"""{item['hook_en']}
Episode 15: Jodi Arias & Borderline Personality Disorder (BPD).
Topic: {item['title_en']}.
Watch the complete 28-min psychological breakdown via link in bio!
#AmberEyes #JodiArias #BPD #CriminalPsychology #TheGiftOfFear
"""
    (OUT_EN / f'MoTa_Ngan_{cid}.txt').write_text(motangan_en.strip(), encoding='utf-8')

    # 3. JA
    cap_ja = f"""{item['hook_ja']} 👁️

第15話 · 境界性パーソナリティ障害と愛憎の暴走 — 指標：{item['signs_ja']}。
アリゾナ州メサ警察捜査記録およびマリコパ郡上級裁判所公判記録と100%対照済みの実話事件簿。

📺 28分間の完全版解説動画はプロフ欄リンクへ
🔎 犯罪心理学指標 · {item['title_ja']} · 実話記録

本動画はAI生成の朗読とグラフィックノベル画像を用いた犯罪心理学の学術的解説コンテンツです。

#AmberEyes #犯罪心理学 #ジョディアリアス #境界性パーソナリティ障害 #BPD #ストーカー #未解決事件 #実話

---
投稿時の注意事項：
- TikTok投稿画面で「AI生成コンテンツ」のトグルを必ずONにしてください。
- YouTube第15話リンク：プロフィール欄のリンク項目に設定。
- 推定時間：{item['dur_ja']}（{item['lines_cnt']}文）実測ASR準拠。
"""
    (OUT_JA / f'Caption_{cid}.txt').write_text(cap_ja.strip(), encoding='utf-8')

    motadai_ja = f"""犯罪心理学事件ファイル — 第15話：境界性パーソナリティ障害と致命的執着（ジョディ・アリアス事件）
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
• アリゾナ州メサ市警察殺人課捜査調書（Mesa Police Department Records）
• ソニー製サイバーショット メモリーカード電子鑑識復元鑑定書
• アリゾナ州マリコパ郡上級裁判所公判記録（2013年〜2015年審理）
• 境界性パーソナリティ障害（BPD）に関する臨床精神医学鑑定書（ジェイニーン・デマルテ博士証言）
• ジャーナリスト シャナ・ホーガン著『Picture Perfect: The Jodi Arias Story』（2013）

——————
完全版ドキュメンタリーのご案内
——————
📺 28分間の完全版ポッドキャスト動画はYouTube公式チャンネル「Amber Eyes」にて公開中。プロフィール欄のリンクからご覧いただけます。
"""
    (OUT_JA / f'MoTa_Dai_{cid}.txt').write_text(motadai_ja.strip(), encoding='utf-8')

    motangan_ja = f"""{item['hook_ja']}
第15話：ジョディ・アリアス事件と境界性パーソナリティ障害（BPD）。
テーマ：{item['title_ja']}。
28分の完全版解説動画はプロフ欄リンクのYouTubeで公開中！
#AmberEyes #ジョディアリアス #境界性パーソナリティ障害 #犯罪心理学 #BPD
"""
    (OUT_JA / f'MoTa_Ngan_{cid}.txt').write_text(motangan_ja.strip(), encoding='utf-8')

print("All Captions and Descriptions successfully created for Tap 15 (VI, EN, JA).")
