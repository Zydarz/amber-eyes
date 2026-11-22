# -*- coding: utf-8 -*-
"""Update Captions and Descriptions for Tap 12 (VI, EN, JA) following premium standard."""

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT_VI = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap12'
OUT_EN = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap12_EN'
OUT_JA = ROOT / '02_SAN_XUAT' / 'TIKTOK' / 'Tap12_JA'

CLIPS_META = [
    {
        'id': 'TK1',
        'title_vn': 'Vỏ bọc Bác ái và Điểm mù Chính trị của Peoples Temple',
        'title_en': 'Charitable Illusion & Political Blind Spots of Peoples Temple',
        'title_ja': '慈善の仮面と人民寺院の政治的盲点',
        'signs_vn': '#1 (Ảnh hưởng xã hội) · #9 (Hiệu ứng Hào quang & Điểm mù chính trị)',
        'signs_en': '#1 (Social Impact) · #9 (Halo Effect & Political Blind Spots)',
        'signs_ja': '#1（社会的影響）· #9（ハロー効果と政治的盲点）',
        'hook_vn': 'Nhận nuôi trẻ em đa chủng tộc, mở bếp ăn từ thiện. Tại sao cả xã hội bị ru ngủ?',
        'hook_en': 'Rainbow family, soup kitchens, political alliances. Why was an entire city completely blinded?',
        'hook_ja': '人種融和の理想郷、慈善活動の英雄。なぜ社会全体が完璧に欺かれたのか？',
        'dur_vn': '74.8 s', 'dur_en': '58.5 s', 'dur_ja': '75.3 s',
        'lines_cnt': 7,
        'context_vn': 'Jim Jones thành lập Đền thờ Nhân dân (Peoples Temple) tại Indiana rồi chuyển về San Francisco, nổi lên như một biểu tượng hòa hợp chủng tộc và bác ái tiến bộ. Hắn nhận nuôi nhiều trẻ em thuộc các sắc tộc khác nhau gọi là “Gia đình Cầu vồng”, điều hành các bếp ăn từ thiện và trại dưỡng lão. Vỏ bọc đạo đức hoàn hảo cùng khối phiếu bầu kỷ luật đã giúp Jones được bổ nhiệm làm Chủ tịch Ủy ban Nhà ở San Francisco. Hiệu ứng Hào quang và nỗi sợ bị chụp mũ kỳ thị đã làm tê liệt hoàn toàn chức năng giám sát của các cơ quan công quyền suốt nhiều năm.',
        'context_en': 'Jim Jones founded the Peoples Temple, presenting it as a progressive beacon of racial harmony and social justice. Adopting children of diverse races as his "Rainbow Family", he operated free dining halls and drug rehab centers in San Francisco. This flawless moral facade earned him the chairmanship of the San Francisco Housing Authority. The resulting Halo Effect and political blind spots completely paralyzed law enforcement oversight for years.',
        'context_ja': 'ジム・ジョーンズは「人民寺院」を設立し、人種融和と平等を掲げる進歩的指導者として台頭した。異人種の子どもたちを養子に迎え「虹の家族」と称し、無料食堂や高齢者施設を運営。この道徳的仮面と強固な組織票によりサンフランシスコ住宅局長に就任。強烈なハロー効果と政治的盲点により、捜査機関や社会の監視機能は長年にわたり完全に麻痺した。'
    },
    {
        'id': 'TK2',
        'title_vn': 'Thiên đường Rừng sâu hay Trại giam Tâm lý Khép kín?',
        'title_en': 'Jungle Paradise or Closed Psychological Prison?',
        'title_ja': '密林の楽園か、それとも閉鎖された心理的監獄か？',
        'signs_vn': '#2 (Vật hóa nạn nhân) · #3 (Phá hủy liên kết thân tộc & Kiểm soát cưỡng bách)',
        'signs_en': '#2 (Victim Objectification) · #3 (Severing Family Bonds & Coercive Control)',
        'signs_ja': '#2（被害者の物象化）· #3（家族解体と強迫的支配）',
        'hook_vn': 'Bán hết nhà cửa, giao nộp hộ chiếu. Khi thiên đường hóa thành chiếc lồng giam không lối thoát.',
        'hook_en': 'Homes sold, passports confiscated. When paradise turned into an inescapable jungle cage.',
        'hook_ja': '財産を売り払い、旅券を没収される。約束の地が逃げ場なき牢獄と化した瞬間。',
        'dur_vn': '63.5 s', 'dur_en': '57.8 s', 'dur_ja': '72.8 s',
        'lines_cnt': 8,
        'context_vn': 'Tại Jonestown (Guyana), các tín đồ bị cô lập hoàn toàn giữa rừng nhiệt đới xích đạo. Ban quản lý thu giữ toàn bộ hộ chiếu và tài sản ngay tại cổng vào. Tín đồ phải lao động khổ sai 11 tiếng mỗi ngày dưới nắng gắt, khẩu phần chỉ có cơm trắng chan nước dùng loãng, trong khi các tay súng an ninh tuần tra cẩn mật ngày đêm. Những buổi “Thanh lọc tâm trí” cưỡng bức sỉ nhục công khai và ép buộc tố cáo người thân đã chặt đứt hoàn toàn mạng lưới hỗ trợ gia đình ruột thịt.',
        'context_en': 'In the remote jungle of Guyana, Jonestown residents were subjected to absolute isolation. Passports and money were confiscated at entry. Devotees endured 11 hours of forced daily labor under brutal tropical heat on meager rations, surrounded by armed guards. Weekly "Catharsis sessions" forced members into public humiliation and mutual denunciation, shattering all familial ties and creating total dependence on Jones.',
        'context_ja': 'ガイアナ奥地のジョーンズタウンに到着した信者たちは、入り口でパスポートと全財産を没収された。赤道直下の過酷な環境で1日11時間の重労働を強いられ、食事は薄いスープと白米のみ。周囲は武装警備隊に24時間監視されていた。「精神浄化」と呼ばれる集会では公然の侮辱と家族への告発が強制され、親族間の絆は徹底的に解体された。'
    },
    {
        'id': 'TK3',
        'title_vn': 'Tư duy Tập thể (Groupthink) & Bẫy Tâm lý Milgram',
        'title_en': 'Groupthink & The Milgram Obedience Trap',
        'title_ja': '集団浅慮（グループシンク）とミルグラム服従の罠',
        'signs_vn': '#6 (Ngòi nổ tâm lý) · #8 (Quỹ đạo kiểm soát cưỡng bách & Tư duy tập thể)',
        'signs_en': '#6 (Psychological Trigger) · #8 (Coercive Escalation & Groupthink)',
        'signs_ja': '#6（心理的引き金）· #8（統制のエスカレーションと集団浅慮）',
        'hook_vn': 'Tại sao 918 con người cùng bước vào chỗ chết mà không phản kháng? Bí ẩn tâm lý học bầy đàn.',
        'hook_en': 'Why did 918 people walk into destruction without mass revolt? The anatomy of group obedience.',
        'hook_ja': 'なぜ918人もの人間が抵抗せず破滅へ向かったのか？ 群集心理の暗黒メカニズム。',
        'dur_vn': '64.1 s', 'dur_en': '52.4 s', 'dur_ja': '85.4 s',
        'lines_cnt': 8,
        'context_vn': 'Thảm kịch Jonestown minh chứng cho hai hiện tượng tâm lý kinh điển: “Sự phục tùng quyền lực” (Thí nghiệm Stanley Milgram) và “Tư duy tập thể” (Groupthink của Irving Janis). Khi đối diện quyền lực được coi là hợp pháp, con người có xu hướng chuyển giao trách nhiệm đạo đức sang kẻ ra lệnh. Áp lực đồng thuận nội bộ đã triệt tiêu tư duy phản biện độc lập. Kết hợp với kỹ thuật “Leo thang cam kết” (Foot-in-the-Door), các tín đồ từng bước nhượng bộ những yêu sách nhỏ cho đến khi tự nguyện bước vào chiếc bẫy hủy diệt tập thể.',
        'context_en': 'The Jonestown tragedy clinically illustrates Stanley Milgram\'s Obedience to Authority and Irving Janis\'s Groupthink. When facing perceived legitimate authority, individuals transfer moral agency to the commander. Internal group pressure crushed dissenting voices, creating massive cognitive blind spots. Through "Foot-in-the-Door" escalating commitment, followers surrendered autonomy incrementally until trapped in blind compliance.',
        'context_ja': 'ジョーンズタウンの悲劇は、スタンレー・ミルグラムの「権威への服従実験」とアーヴィング・ジャニスの「集団浅慮（グループシンク）」の極限例である。人間は正当と信じた権威の前で道徳的責任を放棄する傾向を持つ。集団の調和と忠誠が最優先される中で批判的思考は圧殺され、フット・イン・ザ・ドア（段階的要請）の罠によって自発的盲従へと追い込まれていった。'
    },
    {
        'id': 'TK4',
        'title_vn': 'Cuộn băng Tử thần Q 042 & Tiếng nói Phản kháng Đơn độc',
        'title_en': 'Death Tape Q 042 & The Solitary Voice of Defiance',
        'title_ja': '死のテープQ042と孤立した抵抗の声',
        'signs_vn': '#4 (Thái độ trước bản án) · #5 (Hệ thống tự bào chữa & Lương tri độc lập)',
        'signs_en': '#4 (Attitude to Outcome) · #5 (Neutralization & Independent Conscience)',
        'signs_ja': '#4（結末への態度）· #5（自己正当化と独立した良心）',
        'hook_vn': 'Băng cassette giải mật 44 phút của FBI. Người phụ nữ duy nhất dám đứng lên chất vấn giáo chủ.',
        'hook_en': 'The FBI\'s 44-minute declassified death tape. The lone woman who stood up to question the leader.',
        'hook_ja': 'FBI機密解除テープQ042・44分間の肉声。教祖に立ち向かった唯一の女性。',
        'dur_vn': '76.2 s', 'dur_en': '64.4 s', 'dur_ja': '80.3 s',
        'lines_cnt': 8,
        'context_vn': 'Cuộn băng cassette Q 042 do FBI giải mật dài 44 phút ghi lại toàn bộ âm thanh buổi chiều định mệnh 18/11/1978. Giữa không gian hoảng loạn và sự phục tùng của hàng trăm người, bà Christine Miller (60 tuổi) đã dũng cảm bước lên micro chất vấn trực diện Jim Jones: “Tôi cảm thấy chừng nào còn có sự sống, con người vẫn còn có hy vọng.” Hành động phản kháng phi thường này đại diện cho Lương tri Độc lập, đối lập hoàn toàn với cơ chế ngụy biện đổ lỗi cho hoàn cảnh của kẻ thủ ác.',
        'context_en': 'The FBI declassified cassette tape Q 042 (44 minutes) captures the raw audio of November 18, 1978. Amidst overwhelming conformity, 60-year-old Christine Miller boldly stepped to the microphone to confront Jim Jones directly: "I feel that as long as there is life, there is hope." Her defiance embodies independent moral conscience, standing in stark contrast to Jones\'s narcissistic neutralization and externalization of blame.',
        'context_ja': 'FBIが機密解除した44分間のカセットテープ「Q042」には、1978年11月18日の現場の肉声が生々しく刻まれている。数百人が盲従する中、60歳の信者クリスティーン・ミラーがマイクの前に進み出てジム・ジョーンズに公然と抗議した。「命がある限り、人間には希望があるはずです」。この孤立した抵抗は、責任転嫁に終始した教祖とは対照的な「独立した良心」の輝きであった。'
    },
    {
        'id': 'TK5',
        'title_vn': 'Nạn nhân học & 4 Cảnh báo Đỏ Sinh tồn',
        'title_en': 'Victimology & 4 Survival Red Flags',
        'title_ja': '被害者学と生き残るための4つの危険信号',
        'signs_vn': '#10 (Nạn nhân học & Cảnh báo đỏ sinh tồn — Gavin de Becker)',
        'signs_en': '#10 (Victimology & Survival Red Flags — Gavin de Becker)',
        'signs_ja': '#10（被害者学と生存のための危険信号 — ギャヴィン・ド・ベッカー）',
        'hook_vn': 'Bốn tín hiệu cảnh báo đỏ để không bao giờ rơi vào chiếc bẫy thao túng tâm lý cực đoan.',
        'hook_en': 'Four psychological red flags to never fall prey to coercive mind control.',
        'hook_ja': '破壊的カルトや心理操作の罠から命を守る「4つの危険信号」。',
        'dur_vn': '82.6 s', 'dur_en': '68.7 s', 'dur_ja': '81.8 s',
        'lines_cnt': 10,
        'context_vn': 'Đúc kết từ thảm kịch Jonestown và học thuyết "The Gift of Fear" (Gavin de Becker), kênh Amber Eyes chỉ ra 4 dấu hiệu cảnh báo đỏ sinh tồn: (1) Chiến thuật cô lập hoàn toàn khỏi mạng lưới xã hội và gia đình; (2) Tước đoạt tài chính, giấy tờ và phương tiện tự chủ; (3) Làm suy kiệt thể chất và thiếu ngủ nhằm triệt tiêu phản biện; (4) Thần thánh hóa người đứng đầu và trừng phạt tiếng nói hoài nghi. Trực giác bất an là món quà sinh tồn quý giá nhất giúp bạn dũng cảm dừng lại trước cạm bẫy thao túng.',
        'context_en': 'Drawing from Jonestown and Gavin de Becker\'s "The Gift of Fear", Amber Eyes highlights 4 vital survival red flags: (1) Total isolation from social and family support; (2) Financial confiscation and surrender of personal autonomy; (3) Chronic sleep deprivation and physical exhaustion crushing critical thinking; (4) Deification of the leader and severe punishment of doubt. Uncomfortable intuition is humanity\'s greatest survival gift to walk away from manipulation.',
        'context_ja': 'ジョーンズタウンの悲劇とギャヴィン・ド・ベッカーの『The Gift of Fear』から導き出された4つの危険信号：(1) 親族や社会支援網からの完全な孤立化、(2) 財産・身分証の没収による自立手段の剥奪、(3) 過労と睡眠不足による批判的思考力の組織的破壊、(4) 指導者の絶対神格化と疑問に対する処罰。違和感を告げる直感こそ、自己の生命と尊厳を守る最大の防壁である。'
    }
]

for item in CLIPS_META:
    cid = item['id']
    # 1. VI
    cap_vi = f"""{item['hook_vn']} 👁️

Tập 12 · Thảm Kịch Jonestown — Chỉ dấu {item['signs_vn']}.
Hồ sơ vụ án có thật tại Guyana, 100% dữ liệu đối chiếu Báo cáo Hạ viện Hoa Kỳ & Cuộn băng tử thần giải mật FBI Q 042.

📺 Xem tập đầy đủ (34 phút) ở link trong bio
🔎 Chỉ dấu tâm lý · {item['title_vn'].lower()} · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân.

#AmberEyes #TamLyToiPham #Jonestown #JimJones #Groupthink #TheGiftOfFear #HoSoCoThat #TrueCrime

---
Ghi chú khi đăng (KHÔNG dán vào caption):
- BẬT toggle "Nội dung do AI tạo" (AI-generated content) — TikTok bắt buộc nhãn AIGC.
- Dòng nhãn AIGC ĐÃ nằm sẵn trong caption: không cần thêm khi dán.
- Link YouTube Tập 12: dán vào ô "Links / Website" trong profile TikTok.
- Ước lượng thời lượng: {item['dur_vn']} ({item['lines_cnt']} câu) — đo bằng ASR thực tế.
- File mô tả dài TikTok Studio: MoTa_Dai_{cid}.txt · Bản rút gọn: MoTa_Ngan_{cid}.txt
"""
    (OUT_VI / f'Caption_{cid}.txt').write_text(cap_vi.strip(), encoding='utf-8')

    motadai_vi = f"""HỒ SƠ TÂM LÝ HỌC TỘI PHẠM — TẬP 12: THẢM KỊCH JONESTOWN (JIM JONES & PEOPLES TEMPLE)
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
• Báo cáo điều tra của Ủy ban Đối ngoại Hạ viện Hoa Kỳ (House Committee on Foreign Affairs, 1979)
• Hồ sơ giải mật của Cục Điều tra Liên bang FBI (RYMUR - Ryan Murder Investigation)
• Bản ghi âm cuộn băng cassette giải mật FBI Q 042 (Death Tape) ngày 18/11/1978
• Lời khai tuyên thệ của Deborah Layton (Layton Affidavit, 1978) & Hồi ký Slavery of Faith của Leslie Wagner-Wilson (2009)
• Giáo trình Tâm lý học Xã hội (Stanley Milgram, Irving Janis) & Tác phẩm The Gift of Fear (Gavin de Becker)

——————
XEM TẬP ĐẦY ĐỦ
——————
📺 Video phân tích podcast tài liệu hoàn chỉnh (34 phút) có mặt trên kênh YouTube Amber Eyes: xem tại đường link trong phần tiểu sử (bio)!

——————
LƯU Ý QUY CHUẨN
——————
Nội dung do AI hỗ trợ tạo hình đồ họa noir và giọng đọc, dùng cho mục đích giáo dục nhận thức và phân tích tâm lý học tội phạm — không cổ xúy bạo lực, tuyệt đối bảo vệ nhân phẩm nạn nhân.
"""
    (OUT_VI / f'MoTa_Dai_{cid}.txt').write_text(motadai_vi.strip(), encoding='utf-8')

    motangan_vi = f"""{item['hook_vn']}
Hồ sơ Tập 12: Thảm kịch Jonestown & Cuộn băng tử thần Q 042.
Chủ đề: {item['title_vn']}.
Xem trọn vẹn tập phim phân tích chuyên sâu 34 phút tại đường dẫn trong bio kênh Amber Eyes!
#AmberEyes #Jonestown #JimJones #TamLyToiPham #TheGiftOfFear
"""
    (OUT_VI / f'MoTa_Ngan_{cid}.txt').write_text(motangan_vi.strip(), encoding='utf-8')

    # 2. EN
    cap_en = f"""{item['hook_en']} 👁️

Episode 12 · Jonestown Tragedy — Signs: {item['signs_en']}.
Real historical case, verified with US House Foreign Affairs Report & FBI Declassified Death Tape Q 042.

📺 Watch the full 34-min investigative dossier via link in bio
🔎 Psychological signs · {item['title_en'].lower()} · true crime

Content features AI narration & graphic novel visuals for psychological analysis — educational and respectful.

#AmberEyes #CriminalPsychology #Jonestown #JimJones #Groupthink #TheGiftOfFear #TrueCrime #MindControl

---
Posting Notes:
- Turn ON "AI-generated content" toggle on TikTok.
- YouTube Episode 12 Link: paste in profile "Website / Links" field.
- Estimated Duration: {item['dur_en']} ({item['lines_cnt']} sentences) via measured ASR speech rate.
"""
    (OUT_EN / f'Caption_{cid}.txt').write_text(cap_en.strip(), encoding='utf-8')

    motadai_en = f"""CRIMINAL PSYCHOLOGY DOSSIER — EPISODE 12: THE JONESTOWN TRAGEDY (JIM JONES & PEOPLES TEMPLE)
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
• US House Committee on Foreign Affairs Investigative Report (1979)
• Federal Bureau of Investigation (FBI) RYMUR Declassified Records
• Audio Transcript & Recording of FBI Declassified Cassette Q 042 (Death Tape, Nov 18, 1978)
• Deborah Layton Sworn Affidavit (1978) & Leslie Wagner-Wilson Memoir Slavery of Faith (2009)
• Social Psychology Literature (Stanley Milgram, Irving Janis) & The Gift of Fear by Gavin de Becker

——————
WATCH FULL EPISODE
——————
📺 Full 34-minute documentary podcast available on Amber Eyes YouTube channel: click link in channel bio!
"""
    (OUT_EN / f'MoTa_Dai_{cid}.txt').write_text(motadai_en.strip(), encoding='utf-8')

    motangan_en = f"""{item['hook_en']}
Episode 12: Jonestown & Death Tape Q 042.
Topic: {item['title_en']}.
Watch the complete 34-min psychological breakdown via link in bio!
#AmberEyes #Jonestown #JimJones #CriminalPsychology #MindControl
"""
    (OUT_EN / f'MoTa_Ngan_{cid}.txt').write_text(motangan_en.strip(), encoding='utf-8')

    # 3. JA
    cap_ja = f"""{item['hook_ja']} 👁️

第12話 · ジョーンズタウンの悲劇 — 指標：{item['signs_ja']}。
米下院外交委員会報告書およびFBI機密解除死のテープQ042と100%対照済みの実話記録。

📺 34分間の完全版解説動画はプロフ欄リンクへ
🔎 犯罪心理学指標 · {item['title_ja']} · 実話記録

本動画はAI生成の朗読とグラフィックノベル画像を用いた犯罪心理学の学術的解説コンテンツです。

#AmberEyes #犯罪心理学 #ジョーンズタウン #ジムジョーンズ #マインドコントロール #集団浅慮 #未解決事件 #実話

---
投稿時の注意事項：
- TikTok投稿画面で「AI生成コンテンツ」のトグルを必ずONにしてください。
- YouTube第12話リンク：プロフィール欄のリンク項目に設定。
- 推定時間：{item['dur_ja']}（{item['lines_cnt']}文）実測ASR準拠。
"""
    (OUT_JA / f'Caption_{cid}.txt').write_text(cap_ja.strip(), encoding='utf-8')

    motadai_ja = f"""犯罪心理学事件ファイル — 第12話：ジョーンズタウンの悲劇（ジム・ジョーンズと人民寺院）
クリップ分析 {cid}：{item['title_ja']}
深層心理指標：{item['signs_ja']}

{item['hook_ja']}

——————
歴史的背景と行動心理学分析
——————
{item['context_ja']}

——————
公式参照資料・機密解除記録
——————
• 米国下院外交委員会公式調査報告書（House Committee on Foreign Affairs, 1979）
• 連邦捜査局（FBI）機密解除文書（RYMUR - ライアン議員殺害調査）
• 1978年11月18日録音 FBI機密解除カセットテープQ042（死のテープ）
• デボラ・レイトン宣誓供述書（1978）＆レスリー・ワーグナー＝ウィルソン手記『Slavery of Faith』
• 社会心理学理論（スタンレー・ミルグラム、アーヴィング・ジャニス）＆ギャヴィン・ド・ベッカー『The Gift of Fear』

——————
完全版ドキュメンタリーのご案内
——————
📺 34分間の完全版ポッドキャスト動画はYouTube公式チャンネル「Amber Eyes」にて公開中。プロフィール欄のリンクからご覧いただけます。
"""
    (OUT_JA / f'MoTa_Dai_{cid}.txt').write_text(motadai_ja.strip(), encoding='utf-8')

    motangan_ja = f"""{item['hook_ja']}
第12話：ジョーンズタウンの悲劇と死のテープQ042。
テーマ：{item['title_ja']}。
34分の完全版解説動画はプロフ欄リンクのYouTubeで公開中！
#AmberEyes #ジョーンズタウン #マインドコントロール #犯罪心理学 #集団浅慮
"""
    (OUT_JA / f'MoTa_Ngan_{cid}.txt').write_text(motangan_ja.strip(), encoding='utf-8')

print("All Captions and Descriptions successfully updated for VI, EN, JA.")
