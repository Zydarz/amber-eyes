# -*- coding: utf-8 -*-
import sys
sys.path.append('.work')
from _act1 import ACT1_TURNS
from _act1_ext import ACT1_EXT_TURNS
from _act2 import ACT2_TURNS
from _act2_ext import ACT2_EXT_TURNS
from _act3 import ACT3_TURNS
from _act3_ext import ACT3_EXT_TURNS
from _act4 import ACT4_TURNS
from _act4_ext import ACT4_EXT_TURNS
from _act5 import ACT5_TURNS
from _act5_ext import ACT5_EXT_TURNS
from _add_turns import ADD_TURNS_ACT2, ADD_TURNS_ACT3, ADD_TURNS_ACT4, ADD_TURNS_ACT5

act1 = ACT1_TURNS[:1] + ACT1_EXT_TURNS[:1] + ACT1_TURNS[1:2] + ACT1_EXT_TURNS[1:2] + ACT1_TURNS[2:3] + ACT1_TURNS[3:] + ACT1_EXT_TURNS[2:]
act2 = ACT2_TURNS[:1] + ACT2_EXT_TURNS[:1] + ACT2_TURNS[1:2] + ACT2_EXT_TURNS[1:2] + ACT2_TURNS[2:] + ACT2_EXT_TURNS[2:] + ADD_TURNS_ACT2
act3 = ACT3_TURNS[:1] + ACT3_EXT_TURNS[:1] + ACT3_TURNS[1:2] + ACT3_EXT_TURNS[1:2] + ACT3_TURNS[2:] + ACT3_EXT_TURNS[2:] + ADD_TURNS_ACT3
act4 = ACT4_TURNS[:1] + ACT4_TURNS[1:2] + ACT4_EXT_TURNS[:1] + ACT4_TURNS[2:] + ACT4_EXT_TURNS[1:] + ADD_TURNS_ACT4
act5 = ACT5_TURNS[:1] + ACT5_EXT_TURNS[:1] + ACT5_EXT_TURNS[1:2] + ACT5_TURNS[1:2] + ADD_TURNS_ACT5 + ACT5_TURNS[2:]

acts_data = [act1, act2, act3, act4, act5]

act_titles_vn = [
    'HỒI 1: ÁN MẠNG TRÊN TẦNG THƯỢNG & ĐIỂM MÙ ĐÔ THỊ',
    'HỒI 2: VỎ BỌC THƯ SINH & CẠM BẪY CỦA SỰ QUEN THUỘC',
    'HỒI 3: CUỘC ĐẤU TRÍ TRONG PHÒNG THẨM VẤN & SỰ SỤP ĐỔ BẢN NGÃ',
    'HỒI 4: BẢN CHẤT SỰ HỐI HẬN & BI KỊCH HAI NGƯỜI CHA',
    'HỒI 5: BẢN ÁN TỐI HẬU, SỰ THA THỨ & BÀI HỌC CẢNH BÁO ĐỎ'
]

act_titles_en = [
    'ACT 1: THE ROOFTOP TRAGEDY AND THE URBAN BLIND SPOT',
    'ACT 2: THE SCHOLARLY FACADE AND THE FAMILIARITY TRAP',
    'ACT 3: DUEL IN THE INTERROGATION ROOM AND THE COLLAPSE OF THE EGO',
    'ACT 4: THE NATURE OF REMORSE AND THE TRAGEDY OF TWO FATHERS',
    'ACT 5: THE ULTIMATE VERDICT, REDEMPTIVE FORGIVENESS AND SURVIVAL PRINCIPLES'
]

act_titles_ja = [
    '第1幕：屋上の悲劇と現代都市の盲点',
    '第2幕：優等生の仮面と親密性の罠',
    '第3幕：取調室の心理戦とエゴの崩壊',
    '第4幕：後悔の本質と二人の父親の悲劇',
    '第5幕：最終判決、赦しの救済と生存への警戒原則'
]

bgm_vn = [
    'Tiếng Dark Ambient âm u, tiếng nhịp tim đập chậm và tiếng tích tắc đồng hồ kim loại ngột ngạt.',
    'Tiếng đàn Cello trầm u uất hòa cùng tiếng piano tối giản ngột ngạt và nhịp drone điện tử rùng rợn.',
    'Tiếng bass nặng trĩu, tiếng đồng hồ tích tắc dồn dập tạo không khí ngột ngạt của phòng hỏi cung.',
    'Âm thanh vĩ cầm dồn dập, giằng xé, tái hiện cuộc khủng hoảng lương tâm nghẹt thở và bi kịch gia đình.',
    'Tiếng Piano độc tấu trầm buồn, sâu lắng, mang âm hưởng suy tư, thức tỉnh và nhân văn cao cả.'
]

bgm_en = [
    'Suffocating Dark Ambient, slow heartbeat pulsations, and the oppressive ticking of a metallic clock.',
    'Somber Solo Cello blending with minimalist suffocating piano and an eerie electronic drone.',
    'Heavy bass pulses and rapid clock ticking recreating the suffocating atmosphere of an interrogation room.',
    'Harrowing and turbulent courtroom violin capturing intense crises of conscience and family tragedy.',
    'Warm and solemn minimalist piano resonating with deep reflection, awakening, and sublime human grace.'
]

bgm_ja = [
    '息苦しいダーク・アンビエント、静かに刻まれる心拍音、そして金属製時計の緊迫した秒針の音。',
    '陰鬱なチェロ・ソロ、息苦しいミニマル・ピアノ、そして戦慄を誘う電子ドローンの重層音。',
    '重厚なベース音と急速に刻まれる秒針が再現する、取調室特有の息詰まる心理戦の空気。',
    '法廷の激しい葛藤と家族の引き裂かれる悲劇を表現する、緊迫したバイオリンの旋律。',
    '深い内省と覚醒、そして崇高な人間愛の余韻を静かに響かせる温かなミニマル・ピアノ。'
]

# 1. Write VN script
with open('01_KICH_BAN/Tap34/kichban_tap34_19112026.md', 'w', encoding='utf-8') as f:
    f.write('# KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM\n')
    f.write('**Chủ đề:** Hệ sinh thái 10 chỉ dấu tâm lý & Vỏ bọc sinh viên ưu tú, Sự phân ngăn tâm trí (Compartmentalization) & Bản chất sự ăn năn – Hồ sơ Nguyễn Đức Nghĩa và Vụ án chung cư G4.\n')
    f.write('**Phiên bản:** Chuẩn A2c/K10 — Hệ sinh thái 10 chỉ dấu tâm lý học tội phạm & Bổ sung phân tích biến chuyển tâm lý đa chiều ngày 20/11/2026.\n\n')
    f.write('---\n\n')
    f.write('## THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN (PRODUCTION BRIEF)\n\n')
    f.write('| Hạng mục | Thiết lập chuẩn cho tập Audio (Host-Driven Documentary) |\n')
    f.write('| :--- | :--- |\n')
    f.write('| **Tên tập (Episode Title)** | Tập 34: Vỏ Bọc Sinh Viên Ưu Tú & Sự Tê Liệt Cảm Xúc Sau Chiếc Kính Cận (Hồ Sơ Nguyễn Đức Nghĩa) |\n')
    f.write('| **Định dạng (Format)** | Podcast Tài liệu Điều tra (Narrator-led Documentary) – **Host** nắm giữ trục xương sống kể chuyện, kết nối dữ liệu lịch sử, điều phối nhịp cảm xúc và mời các góc nhìn chuyên môn (Điều tra viên, Chuyên gia tâm lý, Người bình thường) vào đúng điểm nút kịch tính theo Hệ sinh thái 10 chỉ dấu tâm lý. |\n')
    f.write('| **Tổng thời lượng dự kiến** | 26 – 30 phút (5 hồi nội dung + các khoảng lặng chuyển cảnh âm thanh) |\n')
    f.write('| **Nhạc nền (BGM) gợi ý** | Dark Ambient ngột ngạt, Solo Cello u uất, Tiếng đàn Dương cầm tối giản kết hợp nhịp Drone điện tử rùng rợn, Tiếng vĩ cầm giằng xé phòng xử án, và Warm Piano ấm áp trang nghiêm đúc kết. Âm lượng: -26dB dưới giọng đọc, nâng lên -14dB ở các điểm chuyển cảnh. |\n')
    f.write('| **Cơ chế phân bổ giọng đọc** | - **Host (~48% thời lượng):** Giọng nam trầm ấm, sâu lắng, dẫn dắt câu chuyện với góc nhìn nhân văn, dư chấn xã hội, hiệu ứng hào quang và bài học sinh tồn.<br>- **Điều tra viên (~24%):** Giọng nam đanh thép, sắc lạnh, chuẩn xác, đại diện cho hồ sơ nghiệp vụ, chứng cứ hiện trường, chữ ký Signature vs MO và chiến thuật pháp lý của Phòng Cảnh sát hình sự Công an Hà Nội.<br>- **Chuyên gia tâm lý (~22%):** Giọng điềm đạm, mang tính học thuật sâu sắc, bóc tách cơ chế phân ngăn tâm trí, sự tha hóa nhân cách, hiệu ứng hào quang trí thức và bản chất sự hối hận của kẻ thủ ác.<br>- **Người bình thường (~6%):** N1 (Cư dân chung cư G4 - Hồi 1, Hồi 5) giọng bàng hoàng, suy tư; N2 (Hoàng Thị Yến - Hồi 4) giọng nữ trẻ run rẩy, giằng xé tội lỗi tột cùng. |\n')
    f.write('| **Quy tắc trích dẫn** | Mọi trích dẫn nguyên văn trong hình phải đúng 100% so với nguồn lưu trữ. Quy ước ký hiệu: ngoặc kép “ ” = trích dẫn nguyên văn. |\n')
    f.write('| **Nguồn đối chiếu chính** | Hồ sơ vụ án của Phòng Cảnh sát hình sự (PC45) Công an TP. Hà Nội năm 2010 · Bản án sơ thẩm của TAND TP. Hà Nội tháng 7/2010 · Bản án phúc thẩm của TAND Tối cao tháng 11/2010 · Lời khai của các nhân chứng và cơ quan giám định kỹ thuật hình sự · Giáo trình Tâm lý học Pháp y và Khoa học Hành vi Tội phạm. |\n\n')
    f.write('---\n\n')
    for act_idx in range(5):
        f.write(f'## {act_titles_vn[act_idx]}\n\n')
        f.write(f'**[BGM]:** {bgm_vn[act_idx]}\n\n')
        for speaker_vn, speaker_en, speaker_ja, dir_vn, dir_en, dir_ja, lines_vn, lines_en, lines_ja in acts_data[act_idx]:
            f.write(f'**{speaker_vn}** *({dir_vn})*:\n')
            for line in lines_vn:
                f.write(f'{line}\n')
            f.write('\n')
        f.write('---\n\n')

# 2. Write EN script
with open('01_KICH_BAN/Tap34_EN/kichban_tap34_EN.md', 'w', encoding='utf-8') as f:
    f.write('# CRIMINAL PSYCHOLOGY AUDIO / PODCAST SCRIPT\n')
    f.write('**Theme:** The 10 Psychological Indicators & The Scholarly Facade, Cognitive Compartmentalization & The Nature of Remorse – The Nguyen Duc Nghia Case and the G4 Apartment Homicide.\n')
    f.write('**Edition:** Standard A2c/K10 — Criminal Psychological Ecology & Safety Rule V9 (November 20, 2026).\n\n')
    f.write('---\n\n')
    f.write('## PRODUCTION BRIEF & NARRATIVE STRUCTURE\n\n')
    f.write('| Category | Standard Setup for Audio Episode (Host-Driven Documentary) |\n')
    f.write('| :--- | :--- |\n')
    f.write('| **Episode Title** | Episode 34: The Scholarly Facade & Emotional Callosity Behind Spectacles (The Nguyen Duc Nghia Case) |\n')
    f.write('| **Format** | Investigative Documentary Podcast (Narrator-led Documentary) – The **Host** maintains the narrative backbone, connecting historical data, regulating emotional pacing, and bringing in specialized perspectives (Investigator, Psychologist, Ordinary Person) at precise dramatic beats according to the 10 Psychological Indicators. |\n')
    f.write('| **Estimated Total Duration** | 26 – 30 minutes (5 narrative acts + dramatic audio transitions) |\n')
    f.write('| **Suggested Background Music (BGM)** | Suffocating Dark Ambient, Somber Solo Cello, Minimalist Piano blended with chilling Electronic Drone, Harrowing Courtroom Violin, and Warm Piano for solemn reflection. Volume: -26dB under narration, rising to -14dB at scene transitions. |\n')
    f.write('| **Voice Allocation Mechanism** | - **Host (~48% duration):** Warm, deep, reflective male voice, guiding the narrative with a humanistic lens, social aftermath, halo effect, and survival lessons.<br>- **Investigator (~24%):** Sharp, cold, authoritative male voice representing casework files, physical evidence, Signature vs MO, and legal strategy of the Hanoi Police Criminal Investigation Department.<br>- **Psychologist (~22%):** Calm, deeply academic female voice deconstructing cognitive compartmentalization, depersonalization, the intellectual halo effect, and the true psychological mechanics of remorse.<br>- **Ordinary Person (~6%):** N1 (G4 tower resident - Act 1, Act 5) bewildered, reflective voice; N2 (Hoang Thi Yen - Act 4) youthful, trembling female voice in profound guilt and disorientation. |\n')
    f.write('| **Quotation Rule** | All verbatim quotes on screen must match archival sources 100%. Formatting convention: \'…\' = verbatim quote. |\n')
    f.write('| **Key Reference Sources** | Case Files of the Hanoi Police Criminal Investigation Department (PC45, 2010) · First-Instance Trial Records of Hanoi People\'s Court (July 2010) · Appellate Trial Records of the Supreme People\'s Court (November 2010) · Statements of Forensic Examiners and Eyewitnesses · Forensic Criminal Psychology & Behavioral Sciences Frameworks. |\n\n')
    f.write('---\n\n')
    for act_idx in range(5):
        f.write(f'## {act_titles_en[act_idx]}\n\n')
        f.write(f'**[BGM]:** {bgm_en[act_idx]}\n\n')
        for speaker_vn, speaker_en, speaker_ja, dir_vn, dir_en, dir_ja, lines_vn, lines_en, lines_ja in acts_data[act_idx]:
            f.write(f'**{speaker_en}** *({dir_en})*:\n')
            for line in lines_en:
                f.write(f'{line}\n')
            f.write('\n')
        f.write('---\n\n')

# 3. Write JA script
with open('01_KICH_BAN/Tap34_JA/kichban_tap34_JA.md', 'w', encoding='utf-8') as f:
    f.write('# 犯罪心理学オーディオ／ポッドキャスト台本\n')
    f.write('**テーマ：** 10大心理指標生態系＆エリート学生の仮面、認知的区画化（Compartmentalization）と後悔の本質 — グエン・ドゥック・ギア事件とG4マンション凶行録。\n')
    f.write('**バージョン：** 標準A2c/K10 — 犯罪心理生態系＆安全基準V9（2026年11月20日）。\n\n')
    f.write('---\n\n')
    f.write('## 制作仕様とナレーション構成（PRODUCTION BRIEF）\n\n')
    f.write('| 項目 | 音声エピソード標準設定（Host-Driven Documentary） |\n')
    f.write('| :--- | :--- |\n')
    f.write('| **エピソード名** | 第34話：優等生の仮面と眼鏡の奥の感情麻痺（グエン・ドゥック・ギア事件） |\n')
    f.write('| **フォーマット** | 調査ドキュメンタリー・ポッドキャスト（Narrator-led Documentary） – **ホスト**が物語の根幹を担い、歴史的資料を繋ぎ、感情の起伏を調和させ、10大心理指標に基づいて専門的視点（捜査官、心理学者、一般人）を的確な劇的転換点へと招き入れます。 |\n')
    f.write('| **予定総時間** | 26 – 30分（5幕構成＋緊迫した音響の間） |\n')
    f.write('| **推奨BGM** | 息苦しいダーク・アンビエント、陰鬱なチェロ・ソロ、戦慄する電子ドローンを融合させたミニマル・ピアノ、緊迫した法廷のバイオリン、そして厳粛な回顧を告げる温かなピアノ。音量：ナレーション下 -26dB、場面転換点 -14dB。 |\n')
    f.write('| **キャスト構成** | - **ホスト（全体の約48%）：** 深みと温かみのある男性の声。人道的な視点、社会的余波、ハロー効果、生存への教訓を通じて物語を導きます。<br>- **捜査官（約24%）：** 冷徹で鋭敏、正確無比な男性の声。ハノイ市警察刑事局の実地捜査記録、物的証拠、シグネチャー対MO、法廷戦略を代弁します。<br>- **心理学者（約22%）：** 穏やかで深い学術性を備えた女性の声。認知的区画化、没個性化、知的ハロー効果、後悔の真の心理力動を解剖します。<br>- **一般人（約6%）：** N1（G4マンション住民 - 第1幕、第5幕）動揺と内省を語る声；N2（ホアン・ティ・イエン - 第4幕）罪悪感と混乱に震える若い女性の声。 |\n')
    f.write('| **引用規則** | 画面上に表示されるすべての逐語的引用は、公式記録と100%一致していなければなりません。表記規定：「…」＝逐語的引用。 |\n')
    f.write('| **主要参照資料** | ハノイ市警察刑事局（PC45）2010年捜査記録 · ハノイ市人民裁判所2010年7月第一審判決書 · ベトナム最高人民裁判所2010年11月控訴審判決書 · 鑑識専門官および目撃者の公式証言 · 司法犯罪心理学および行動科学教程。 |\n\n')
    f.write('---\n\n')
    for act_idx in range(5):
        f.write(f'## {act_titles_ja[act_idx]}\n\n')
        f.write(f'**[BGM]:** {bgm_ja[act_idx]}\n\n')
        for speaker_vn, speaker_en, speaker_ja, dir_vn, dir_en, dir_ja, lines_vn, lines_en, lines_ja in acts_data[act_idx]:
            f.write(f'**{speaker_ja}** *({dir_ja})*:\n')
            for line in lines_ja:
                f.write(f'{line}\n')
            f.write('\n')
        f.write('---\n\n')

print('All 3 script files generated successfully!')
