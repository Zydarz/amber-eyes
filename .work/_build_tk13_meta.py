# -*- coding: utf-8 -*-
"""Generate premium Captions and Descriptions for Tap 13 (VI, EN, JA)."""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_VI = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap13'
OUT_EN = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap13_EN'
OUT_JA = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap13_JA'

CLIPS_META = [
    {
        'id': 'TK1',
        'title_vn': "Vỏ bọc 'Con Nhà Người Ta' & Kỷ luật Cha Mẹ Hổ",
        'title_en': "The Golden Child Facade & Tiger Parenting Cage",
        'title_ja': "優等生の仮面とタイガーペアレンティングの檻",
        'signs_vn': '#1 (Ảnh hưởng xã hội) · #9 (Hiệu ứng Hào quang & Điểm mù gia đình)',
        'signs_en': '#1 (Social Impact) · #9 (Halo Effect & Familial Blind Spots)',
        'signs_ja': '#1（社会的影響）· #9（ハロー効果と教育熱心な家庭の盲点）',
        'hook_vn': "Huy chương trượt băng, piano xuất sắc. Chiếc lồng giam vô hình đằng sau vỏ bọc 'con nhà người ta'.",
        'hook_en': "Figure skating medals, piano prodigy. The invisible prison behind the 'golden child' illusion.",
        'hook_ja': "フィギュアスケートの栄光、ピアノの天才。完璧な「優等生」の裏に隠された見えない檻。",
        'dur_vn': '77.1 s', 'dur_en': '66.2 s', 'dur_ja': '83.0 s',
        'lines_cnt': 8,
        'context_vn': "Trong mắt hàng xóm tại thành phố Markham (Canada), Jennifer Pan là hình mẫu 'con nhà người ta' hoàn hảo với nụ cười lễ phép, huy chương trượt băng nghệ thuật và chứng chỉ piano xuất sắc. Nhưng đằng sau vỏ bọc ấy là một chiếc lồng giam khắc nghiệt từ mô hình 'Cha mẹ hổ'. Người cha Huei Hann Pan cấm tuyệt đối mọi cuộc hẹn hò, giao lưu bạn bè hay trang điểm. Nỗi sợ hãi sự phán xét và kỳ vọng cực đoan đã âm thầm bào mòn thế giới tinh thần của cô thiếu nữ suốt thời niên thiếu.",
        'context_en': "To neighbors in Markham, Ontario, Jennifer Pan was the epitome of the 'golden child'—polite, decorated in figure skating, and an accomplished pianist. Yet beneath this flawless facade lay an invisible domestic cage forged by extreme 'Tiger Parenting'. Her father strictly forbade dating, parties, makeup, and social outings. The relentless pressure and terror of failing parental expectations quietly eroded her psychological well-being throughout her adolescence.",
        'context_ja': "カナダ・オンタリオ州マーカムの隣人たちの目に、ジェニファー・パンは礼儀正しく、フィギュアスケートのメダリストでピアノの才能にも恵まれた「完璧な優等生」と映っていた。しかしその仮面の裏には、「タイガーペアレンティング（過激な教育虐待）」による冷酷な家庭内監獄が存在した。父親は友人付き合い、化粧、恋愛を一切禁止。失敗への恐怖が、思春期の彼女の心を静かに破壊していった。"
    },
    {
        'id': 'TK2',
        'title_vn': 'Tòa Tháp Dối Lừa 10 Năm & Lối Sống Hai Mặt',
        'title_en': 'The 10-Year Web of Lies & Double Life',
        'title_ja': '10年間の嘘の楼閣と二重生活の崩壊',
        'signs_vn': '#6 (Ngòi nổ tâm lý) · #8 (Quỹ đạo leo thang dối trá & Hội chứng nói dối bệnh lý)',
        'signs_en': '#6 (Psychological Trigger) · #8 (Escalating Deceit & Pathological Lying)',
        'signs_ja': '#6（心理的引き金）· #8（虚言のエスカレーションと病的虚言症）',
        'hook_vn': 'Làm giả học bạ trung học, ngụy tạo bằng đại học Dược khoa. Một lời nói dối leo thang suốt 10 năm.',
        'hook_en': 'Forging high school reports, faking pharmacy diplomas. A 10-year compounding web of deceit.',
        'hook_ja': '偽造された成績表、トロント大学の偽学位記。たった一つの嘘が10年間の楼閣となった。',
        'dur_vn': '82.0 s', 'dur_en': '74.3 s', 'dur_ja': '77.7 s',
        'lines_cnt': 8,
        'context_vn': "Khi điểm số Giải tích tụt dốc khiến cô không đủ điều kiện tốt nghiệp phổ thông, vì sợ hãi cơn thịnh nộ của người cha, Jennifer đã dùng dao rọc giấy và máy photocopy làm giả bảng điểm. Lời nói dối đầu tiên trôi qua êm thấm đã trở thành phát súng mở màn cho cả một tòa tháp lừa dối khổng lồ kéo dài 10 năm. Cô giả vờ đỗ Đại học Toronto ngành Dược, mỗi sáng xách cặp đi học nhưng thực chất ngồi đọc sách ở thư viện hoặc sang nhà bạn trai, tiếp tục làm giả cả bằng cử nhân và việc làm tại bệnh viện SickKids.",
        'context_en': "When failing high school calculus threatened to destroy her father's pride, Jennifer used razor blades and a photocopier to forge report cards. That first successful lie initiated a decade-long house of cards. She pretended to attend the University of Toronto's prestigious pharmacy program, commuting every morning only to sit in public libraries reading novels. The deception escalated into forged university diplomas and fabricated research jobs at SickKids Hospital.",
        'context_ja': "高校最後の年、微積分を落第し卒業資格を失ったジェニファーは、父親の激怒を恐れるあまりカッターとコピー機で成績表を偽造した。最初の嘘が露見しなかったことで、その後10年続く巨大な虚構が始まった。トロント大学薬学部に通うふりをして毎朝家を出ては図書館で一日を過ごし、卒業証書や小児病院の研究職まで偽造し続けた。"
    },
    {
        'id': 'TK3',
        'title_vn': 'Cuộc Gọi 911 Kỳ Lạ & Hiện Trường Đầy Sơ Hở',
        'title_en': 'The Bizarre 911 Call & Crime Scene Anomalies',
        'title_ja': '不可解な911通報と現場に残された矛盾',
        'signs_vn': '#7 (Thủ đoạn MO vs. Dấu ấn Signature) · #8 (Lỗ hổng ngụy tạo hiện trường cướp của giết người)',
        'signs_en': '#7 (MO vs. Signature) · #8 (Crime Scene Staging Anomalies)',
        'signs_ja': '#7（手口MO対署名Signature）· #8（偽装強盗現場の致命的矛盾）',
        'hook_vn': 'Bị trói hai tay sau lưng nhưng vẫn gọi được 911? Chi tiết lật tẩy màn kịch hoàn hảo.',
        'hook_en': 'Hands tied tightly behind her back, yet dialing 911? The detail unraveling the staged home invasion.',
        'hook_ja': '両手を後ろ手に縛られながらどうやって911に通報したのか？ 完璧なシナリオを崩した決定的一撃。',
        'dur_vn': '73.1 s', 'dur_en': '67.7 s', 'dur_ja': '81.8 s',
        'lines_cnt': 8,
        'context_vn': "Đêm 8/11/2010, màn kịch đột nhập có vũ trang xảy ra tại căn nhà số 238 Đại lộ Helen. Mẹ cô bị sát hại dã man còn người cha bị bắn trọng thương. Ngay sau khi hung thủ rời đi, Jennifer gọi 911 trong trạng thái hoảng loạn tột cùng. Tuy nhiên, các điều tra viên lập tức nhận ra những sơ hở chết người: cửa chính không hề bị cạy phá, tài sản giá trị không bị lục lọi, và kỳ lạ nhất là Jennifer khai mình bị trói chặt hai tay sau lưng vào tay vịn cầu thang nhưng lại có thể bấm số gọi 911 bằng điện thoại di động một cách hoàn hảo.",
        'context_en': "On November 8, 2010, a violent armed home invasion occurred at 238 Helen Avenue, leaving her mother deceased and her father critically wounded. Jennifer dialed 911 in hysterical panic. Yet detectives immediately noticed glaring anomalies: no signs of forced entry, valuables left untouched, and most bafflingly, Jennifer claimed her hands were bound tightly behind her back to the banister, yet managed to retrieve and dial her mobile phone flawlessly.",
        'context_ja': "2010年11月8日夜、マーカムの住宅で凶悪強盗事件が発生。母が射殺され父が重傷を負う中、ジェニファーは取り乱した様子で911に通報した。しかし鑑識と刑事たちは即座に致命的な矛盾に気づく。玄関にピッキング痕はなく、貴重品は手つかず。何より「両手を後ろ手に階段の手すりに縛られていた」はずの彼女が、完璧に携帯電話を取り出して通報していた。"
    },
    {
        'id': 'TK4',
        'title_vn': 'Lời Khai Của Người Cha & Màn Đấu Trí Phòng Thẩm Vấn',
        'title_en': "The Father's Testimony & Interrogation Room Showdown",
        'title_ja': '父の証言と取調室の心理戦',
        'signs_vn': '#4 (Thái độ trước bản án) · #5 (Sự thức tỉnh của người cha & Bóc trần lời ngụy biện)',
        'signs_en': "#4 (Attitude to Reality) · #5 (Father's Revelation & Shattering of Denial)",
        'signs_ja': '#4（真実への直面）· #5（生き残った父親の証言と自己正当化の破綻）',
        'hook_vn': "'Con gái tôi đi lại tự do và thì thầm với kẻ cướp.' Lời khai từ giường bệnh của người cha.",
        'hook_en': "'My daughter walked freely, whispering with the intruders.' A surviving father's testimony.",
        'hook_ja': "「娘は両手を縛られておらず、犯人と親しげに囁き合っていた」。昏睡から目覚めた父の証言。",
        'dur_vn': '68.6 s', 'dur_en': '63.9 s', 'dur_ja': '78.5 s',
        'lines_cnt': 8,
        'context_vn': "Bước ngoặt định đoạt của vụ án xảy ra khi người cha Huei Hann Pan kỳ diệu tỉnh lại từ cơn hôn mê sâu. Ký ức kinh hoàng của ông đã đập tan toàn bộ câu chuyện ngụy tạo của Jennifer: ông khẳng định tận mắt nhìn thấy con gái mình đi lại tự do trong nhà, nói chuyện thì thầm thân thiết với những tay súng mà không hề bị trói hay đe dọa. Ngày 22/11/2010, tại phòng thẩm vấn, thám tử William Goetz đối chất với các dữ liệu tin nhắn điện thoại khôi phục, buộc Jennifer Pan phải cúi đầu trước sự thật.",
        'context_en': "The case pivoted dramatically when father Huei Hann Pan miraculously awoke from his coma. His testimony shattered Jennifer's alibi: he recalled seeing Jennifer walking freely through the house, whispering cordially with the armed intruders, completely unbound. On November 22, 2010, Detective William Goetz confronted her in an 8-hour psychological interrogation with forensic cellphone evidence, systematically dismantling her defense.",
        'context_ja': "事件の風向きを決定づけたのは、昏睡から奇跡的に意識を回復した父ハンの証言だった。「娘は縛られておらず、侵入者たちと親しげに囁き合いながら家の中を自由に歩いていた」。2010年11月22日、ビル・ゲッツ刑事は復元された携帯電話の膨大な共謀メッセージを突きつけ、取調室での緊迫した心理戦の末に虚飾の城を完全崩壊させた。"
    },
    {
        'id': 'TK5',
        'title_vn': 'Nạn Nhân Học & 4 Tín Hiệu Cảnh Báo Đỏ Gia Đình',
        'title_en': 'Victimology & 4 Familial Red Flags',
        'title_ja': '被害者学と家庭内危機の4つの警告サイン',
        'signs_vn': '#10 (Nạn nhân học & Cảnh báo đỏ sinh tồn — The Gift of Fear)',
        'signs_en': '#10 (Victimology & Familial Survival Red Flags — The Gift of Fear)',
        'signs_ja': '#10（被害者学と家庭内トラウマを防ぐ4つの危険信号）',
        'hook_vn': 'Bốn tín hiệu cảnh báo đỏ nhận diện nguy cơ rạn nứt tâm lý và bạo lực ngầm trong gia đình.',
        'hook_en': 'Four vital survival red flags to prevent hidden psychological trauma in families.',
        'hook_ja': '家庭内の心理的崩壊と悲劇を防ぐ「4つの危険信号」。',
        'dur_vn': '81.5 s', 'dur_en': '67.7 s', 'dur_ja': '77.1 s',
        'lines_cnt': 10,
        'context_vn': "Đúc kết từ bi kịch Jennifer Pan, kênh Amber Eyes chỉ ra 4 dấu hiệu cảnh báo đỏ trong gia đình: (1) Tình yêu có điều kiện và sự trừng phạt cực đoan khi thất bại; (2) Chiếc mạng nhện dối trá leo thang từng ngày và lối sống hai mặt kéo dài; (3) Kiểm soát toàn diện tước đoạt quyền tự quyết cá nhân; (4) Đứt gãy giao tiếp cảm xúc và sự im lặng độc hại dưới một mái nhà. Một mái ấm thực sự phải là nơi an toàn nhất để trở về khi thất bại, chứ không phải là một phiên tòa phán xét khắc nghiệt.",
        'context_en': "Drawing from the Jennifer Pan tragedy, Amber Eyes highlights 4 vital familial red flags: (1) Conditional love tied strictly to high achievement and fear of failure; (2) Compounding webs of deceit and prolonged double lives; (3) Excessive authoritarian control crushing autonomy; (4) Toxic silence and emotional rupture under the same roof. A genuine home must be the safest sanctuary to fall when failing, not an inescapable courtroom of judgment.",
        'context_ja': "ジェニファー・パン事件の教訓から、Amber Eyesは家庭崩壊を防ぐ4つの危険信号を提示する：(1) 成績や成果にのみ与えられる条件付きの愛、(2) 日常化しエスカレートする嘘と二重生活、(3) 個人の決定権を奪う過剰な管理と抑圧、(4) 感情的対話の断絶と家庭内の冷たい沈黙。真の家庭とは、失敗した時に最も安心して帰れる避難所であるべきなのだ。"
    }
]

for item in CLIPS_META:
    cid = item['id']
    # 1. VI
    cap_vi = f"""{item['hook_vn']} 👁️

Tập 13 · Vỏ Bọc 'Con Nhà Người Ta' — Chỉ dấu {item['signs_vn']}.
Hồ sơ vụ án Jennifer Pan có thật tại Markham, Canada, 100% dữ liệu đối chiếu hồ sơ điều tra Cảnh sát Khu vực York và lời khai tòa án.

📺 Xem tập đầy đủ (28 phút) ở link trong bio
🔎 Chỉ dấu tâm lý · {item['title_vn'].lower()} · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân.

#AmberEyes #TamLyToiPham #JenniferPan #TigerParenting #Mythomania #TheGiftOfFear #HoSoCoThat #TrueCrime

---
Ghi chú khi đăng (KHÔNG dán vào caption):
- BẬT toggle "Nội dung do AI tạo" (AI-generated content) — TikTok bắt buộc nhãn AIGC.
- Dòng nhãn AIGC ĐÃ nằm sẵn trong caption: không cần thêm khi dán.
- Link YouTube Tập 13: dán vào ô "Links / Website" trong profile TikTok.
- Ước lượng thời lượng: {item['dur_vn']} ({item['lines_cnt']} câu) — đo bằng ASR thực tế.
- File mô tả dài TikTok Studio: MoTa_Dai_{cid}.txt · Bản rút gọn: MoTa_Ngan_{cid}.txt
"""
    (OUT_VI / f'Caption_{cid}.txt').write_text(cap_vi.strip(), encoding='utf-8')

    motadai_vi = f"""HỒ SƠ TÂM LÝ HỌC TỘI PHẠM — TẬP 13: VỎ BỌC 'CON NHÀ NGƯỜI TA' & LỜI NÓI DỐI 10 NĂM (JENNIFER PAN)
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
• Hồ sơ điều tra của Cục Cảnh sát Khu vực York (York Regional Police - Homicide Bureau)
• Bản ghi âm và biên bản cuộc gọi 911 đêm ngày 8/11/2010 tại 238 Đại lộ Helen, Markham
• Lời khai tuyên thệ tại tòa án của nhân chứng sống sót Huei Hann Pan (2014)
• Biên bản và video giải mật 3 buổi thẩm vấn Jennifer Pan của Thám tử William Goetz
• Tác phẩm điều tra tài liệu *A Daughter's Deadly Deception* của nhà báo Jeremy Grimaldi (2016)

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
Hồ sơ Tập 13: Vụ án Jennifer Pan & Lời nói dối 10 năm.
Chủ đề: {item['title_vn']}.
Xem trọn vẹn tập phim phân tích chuyên sâu 28 phút tại đường dẫn trong bio kênh Amber Eyes!
#AmberEyes #JenniferPan #TigerParenting #TamLyToiPham #TheGiftOfFear
"""
    (OUT_VI / f'MoTa_Ngan_{cid}.txt').write_text(motangan_vi.strip(), encoding='utf-8')

    # 2. EN
    cap_en = f"""{item['hook_en']} 👁️

Episode 13 · The Golden Child Illusion — Signs: {item['signs_en']}.
Real case in Markham, Ontario, Canada. 100% verified via York Regional Police files and trial transcripts.

📺 Watch the full 28-min documentary dossier via link in bio
🔎 Psychological signs · {item['title_en'].lower()} · true crime

Content features AI narration & graphic novel visuals for psychological analysis — educational and respectful.

#AmberEyes #CriminalPsychology #JenniferPan #TigerParenting #Mythomania #TheGiftOfFear #TrueCrime #MindControl

---
Posting Notes:
- Turn ON "AI-generated content" toggle on TikTok.
- YouTube Episode 13 Link: paste in profile "Website / Links" field.
- Estimated Duration: {item['dur_en']} ({item['lines_cnt']} sentences) via measured ASR speech rate.
"""
    (OUT_EN / f'Caption_{cid}.txt').write_text(cap_en.strip(), encoding='utf-8')

    motadai_en = f"""CRIMINAL PSYCHOLOGY DOSSIER — EPISODE 13: THE GOLDEN CHILD ILLUSION & 10-YEAR WEB OF DECEIT (JENNIFER PAN)
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
• York Regional Police Homicide Bureau Investigative Records
• Official Audio Transcripts of 911 Call on November 8, 2010 (238 Helen Avenue)
• Sworn Courtroom Testimony of Surviving Father Huei Hann Pan (Ontario Superior Court of Justice, 2014)
• Declassified Police Interrogation Tapes by Detective William Goetz
• Investigative Work *A Daughter's Deadly Deception* by Jeremy Grimaldi (2016)

——————
WATCH FULL EPISODE
——————
📺 Full 28-minute documentary podcast available on Amber Eyes YouTube channel: click link in channel bio!
"""
    (OUT_EN / f'MoTa_Dai_{cid}.txt').write_text(motadai_en.strip(), encoding='utf-8')

    motangan_en = f"""{item['hook_en']}
Episode 13: Jennifer Pan & 10-Year Web of Lies.
Topic: {item['title_en']}.
Watch the complete 28-min psychological breakdown via link in bio!
#AmberEyes #JenniferPan #TigerParenting #CriminalPsychology #Mythomania
"""
    (OUT_EN / f'MoTa_Ngan_{cid}.txt').write_text(motangan_en.strip(), encoding='utf-8')

    # 3. JA
    cap_ja = f"""{item['hook_ja']} 👁️

第13話 · 優等生の仮面と10年の嘘 — 指標：{item['signs_ja']}。
ヨーク地域警察の捜査記録および公判記録と100%対照済みの実話事件簿。

📺 28分間の完全版解説動画はプロフ欄リンクへ
🔎 犯罪心理学指標 · {item['title_ja']} · 実話記録

本動画はAI生成の朗読とグラフィックノベル画像を用いた犯罪心理学の学術的解説コンテンツです。

#AmberEyes #犯罪心理学 #ジェニファーパン #教育虐待 #タイガーペアレンティング #虚言癖 #未解決事件 #実話

---
投稿時の注意事項：
- TikTok投稿画面で「AI生成コンテンツ」のトグルを必ずONにしてください。
- YouTube第13話リンク：プロフィール欄のリンク項目に設定。
- 推定時間：{item['dur_ja']}（{item['lines_cnt']}文）実測ASR準拠。
"""
    (OUT_JA / f'Caption_{cid}.txt').write_text(cap_ja.strip(), encoding='utf-8')

    motadai_ja = f"""犯罪心理学事件ファイル — 第13話：優等生の仮面と10年間の嘘の楼閣（ジェニファー・パン事件）
クリップ分析 {cid}：{item['title_ja']}
深層心理指標：{item['signs_ja']}

{item['hook_ja']}

——————
歴史的背景と行動心理学分析
——————
{item['context_ja']}

——————
公式参照資料・公判記録
——————
• カナダ・ヨーク地域警察殺人課捜査資料（York Regional Police Records）
• 2010年11月8日 ヘレン通り238番地 911緊急通報録音記録
• 生き残った父ハン・パン（Huei Hann Pan）の法廷証言録（2014年公判）
• ビル・ゲッツ刑事によるジェニファー・パンの取調べ映像・調書
• ジャーナリスト ジェレミー・グリマルディ著『A Daughter's Deadly Deception』（2016）

——————
完全版ドキュメンタリーのご案内
——————
📺 28分間の完全版ポッドキャスト動画はYouTube公式チャンネル「Amber Eyes」にて公開中。プロフィール欄のリンクからご覧いただけます。
"""
    (OUT_JA / f'MoTa_Dai_{cid}.txt').write_text(motadai_ja.strip(), encoding='utf-8')

    motangan_ja = f"""{item['hook_ja']}
第13話：ジェニファー・パン事件と10年間の嘘。
テーマ：{item['title_ja']}。
28分の完全版解説動画はプロフ欄リンクのYouTubeで公開中！
#AmberEyes #ジェニファーパン #教育虐待 #犯罪心理学 #タイガーペアレンティング
"""
    (OUT_JA / f'MoTa_Ngan_{cid}.txt').write_text(motangan_ja.strip(), encoding='utf-8')

print("All Captions and Descriptions successfully created for Tap 13 (VI, EN, JA).")
