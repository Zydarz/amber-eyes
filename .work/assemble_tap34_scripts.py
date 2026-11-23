# -*- coding: utf-8 -*-
"""
Assemble the 3 complete markdown files for Episode 34:
- 01_KICH_BAN/Ho_So_Toi_Pham/Tap34/kichban_tap34_19112026.md
- 01_KICH_BAN/Ho_So_Toi_Pham/Tap34_EN/kichban_tap34_EN.md
- 01_KICH_BAN/Ho_So_Toi_Pham/Tap34_JA/kichban_tap34_JA.md
"""

from generate_tap34_vn import VN_SECTIONS
from generate_tap34_en_ja import EN_SECTIONS, JA_SECTIONS

# Acts map:
# Act 1: Dlg 00..06 (7 sections)
# Act 2: Dlg 07..13 (7 sections)
# Act 3: Dlg 14..20 (7 sections)
# Act 4: Dlg 21..27 (7 sections)
# Act 5: Dlg 28..33 (6 sections)

ACT_RANGES = [
    (0, 7),
    (7, 14),
    (14, 21),
    (21, 28),
    (28, 34)
]

# Vietnamese Metadata & Structure
VN_HEADER = """# KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM
**Chủ đề:** Hệ sinh thái 10 chỉ dấu tâm lý & Vỏ bọc sinh viên ưu tú, Sự phân ngăn tâm trí (Compartmentalization) & Bản chất sự ăn năn – Hồ sơ Nguyễn Đức Nghĩa và Vụ án chung cư G4.
**Phiên bản:** Chuẩn A2c/K10 — Hệ sinh thái 10 chỉ dấu tâm lý học tội phạm & Bổ sung mở rộng phân tích 240 câu thoại ngày 22/11/2026.

---

## THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN (PRODUCTION BRIEF)

| Hạng mục | Thiết lập chuẩn cho tập Audio (Host-Driven Documentary) |
| :--- | :--- |
| **Tên tập (Episode Title)** | Tập 34: Vỏ Bọc Sinh Viên Ưu Tú & Sự Tê Liệt Cảm Xúc Sau Chiếc Kính Cận (Hồ Sơ Nguyễn Đức Nghĩa) |
| **Định dạng (Format)** | Podcast Tài liệu Điều tra (Narrator-led Documentary) – **Host** nắm giữ trục xương sống kể chuyện, kết nối dữ liệu lịch sử, điều phối nhịp cảm xúc và mời các góc nhìn chuyên môn (Điều tra viên, Chuyên gia tâm lý, Người bình thường) vào đúng điểm nút kịch tính theo Hệ sinh thái 10 chỉ dấu tâm lý. |
| **Tổng thời lượng dự kiến** | 28 – 32 phút (5 hồi nội dung + các khoảng lặng chuyển cảnh âm thanh, 240 câu thoại chuẩn) |
| **Nhạc nền (BGM) gợi ý** | Dark Ambient ngột ngạt, Solo Cello u uất, Tiếng đàn Dương cầm tối giản kết hợp nhịp Drone điện tử rùng rợn, Tiếng vĩ cầm giằng xé phòng xử án, và Warm Piano ấm áp trang nghiêm đúc kết. Âm lượng: -26dB dưới giọng đọc, nâng lên -14dB ở các điểm chuyển cảnh. |
| **Cơ chế phân bổ giọng đọc** | - **Host (~48% thời lượng):** Giọng nam trầm ấm, sâu lắng, dẫn dắt câu chuyện với góc nhìn nhân văn, dư chấn xã hội, hiệu ứng hào quang và bài học sinh tồn.<br>- **Điều tra viên (~24%):** Giọng nam đanh thép, sắc lạnh, chuẩn xác, đại diện cho hồ sơ nghiệp vụ, chứng cứ hiện trường, chữ ký Signature vs MO và chiến thuật pháp lý của Phòng Cảnh sát hình sự Công an Hà Nội.<br>- **Chuyên gia tâm lý (~22%):** Giọng điềm đạm, mang tính học thuật sâu sắc, bóc tách cơ chế phân ngăn tâm trí, sự tha hóa nhân cách, hiệu ứng hào quang trí thức và bản chất sự hối hận của kẻ thủ ác.<br>- **Người bình thường (~6%):** N1 (Cư dân chung cư G4 - Hồi 1, Hồi 5) giọng bàng hoàng, suy tư; N2 (Hoàng Thị Yến - Hồi 4) giọng nữ trẻ run rẩy, giằng xé tội lỗi tột cùng. |
| **Quy tắc trích dẫn** | Mọi trích dẫn nguyên văn trong hình phải đúng 100% so với nguồn lưu trữ. Quy ước ký hiệu: ngoặc kép “ ” = trích dẫn nguyên văn. |
| **Nguồn đối chiếu chính** | Hồ sơ vụ án của Phòng Cảnh sát hình sự (PC45) Công an TP. Hà Nội năm 2010 · Bản án sơ thẩm của TAND TP. Hà Nội tháng 7/2010 · Bản án phúc thẩm của TAND Tối cao tháng 11/2010 · Lời khai của các nhân chứng và cơ quan giám định kỹ thuật hình sự · Giáo trình Tâm lý học Pháp y và Khoa học Hành vi Tội phạm. |

---
"""

VN_ACT_TITLES = [
    ("## HỒI 1: ÁN MẠNG TRÊN TẦNG THƯỢNG & ĐIỂM MÙ ĐÔ THỊ", "**[BGM]:** Tiếng Dark Ambient âm u, tiếng nhịp tim đập chậm và tiếng tích tắc đồng hồ kim loại ngột ngạt."),
    ("## HỒI 2: VỎ BỌC THƯ SINH & CẠM BẪY CỦA SỰ QUEN THUỘC", "**[BGM]:** Tiếng đàn Cello trầm u uất hòa cùng tiếng piano tối giản ngột ngạt và nhịp drone điện tử rùng rợn."),
    ("## HỒI 3: CUỘC ĐẤU TRÍ TRONG PHÒNG THẨM VẤN & SỰ SỤP ĐỔ BẢN NGÃ", "**[BGM]:** Tiếng bass nặng trĩu, tiếng đồng hồ tích tắc dồn dập tạo không khí ngột ngạt của phòng hỏi cung."),
    ("## HỒI 4: BẢN CHẤT SỰ HỐI HẬN & BI KỊCH HAI NGƯỜI CHA", "**[BGM]:** Âm thanh vĩ cầm dồn dập, giằng xé, tái hiện cuộc khủng hoảng lương tâm nghẹt thở và bi kịch gia đình."),
    ("## HỒI 5: BẢN ÁN TỐI HẬU, SỰ THA THỨ & BÀI HỌC CẢNH BÁO ĐỎ", "**[BGM]:** Tiếng Piano độc tấu trầm buồn, sâu lắng, mang âm hưởng suy tư, thức tỉnh và nhân văn cao cả.")
]

# English Metadata & Structure
EN_HEADER = """# CRIMINAL PSYCHOLOGY AUDIO / PODCAST SCRIPT
**Theme:** The 10 Psychological Indicators & The Mask of the Elite Student, Mental Compartmentalization & The Nature of Remorse – The Nguyen Duc Nghia Case File and the G4 Apartment Murder.
**Edition:** Standard A2c/K10 — Criminal Psychology Ecosystem & 240-Sentence Master Edition November 22, 2026.

---

## PRODUCTION BRIEF & NARRATIVE STRUCTURE

| Item | Standard Specification (Narrator-led Documentary) |
| :--- | :--- |
| **Episode Title** | Episode 34: The Elite Student's Facade & Emotional Numbness Behind the Spectacles (The Nguyen Duc Nghia Dossier) |
| **Format** | Investigative Documentary Podcast – The **Host** serves as the central narrative spine, connecting historical facts, pacing emotional momentum, and inviting expert perspectives (Investigator, Criminal Psychologist, Ordinary Person) at key psychological junctures. |
| **Target Duration** | 28 – 32 minutes (5 narrative acts + sound design transitions, 240 standard dialogue sentences) |
| **Suggested BGM** | Suffocating Dark Ambient, Melancholic Solo Cello, Minimalist Piano paired with eerie sub-bass drone, Agonizing Violin in the courtroom, and Solemn Warm Piano for humanistic reflection. Volume: -26dB under narration, rising to -14dB during scene transitions. |
| **Vocal Cast Allocation** | - **Host (~48% airtime):** Warm, deep baritone, guiding the narrative with humanistic reflection, societal resonance, the halo effect, and survival lessons.<br>- **Investigator (~24%):** Sharp, authoritative, objective, representing investigative procedure, crime scene evidence, Signature vs. MO, and legal strategy of Hanoi Criminal Police (PC45).<br>- **Psychologist (~22%):** Composed, scholarly, dissecting compartmentalization, character degeneration, the intellectual halo effect, and the true anatomy of remorse.<br>- **Ordinary Person (~6%):** N1 (G4 Complex Resident - Act 1, Act 5) shaken and contemplative; N2 (Hoang Thi Yen - Act 4) youthful female voice, trembling under overwhelming guilt. |
| **Citation Protocol** | All direct on-screen quotes must match historical court and police transcripts with 100% fidelity. Notation: double quotation marks “ ” = verbatim citation. |
| **Primary Reference Sources** | Case File PC45, Hanoi City Police Department (2010) · First-Instance Judgment, Hanoi People's Court (July 2010) · Appellate Judgment, Supreme People's Court (November 2010) · Witness depositions and forensic ballistics/biology reports · Forensic Psychology and Behavioral Analysis Textbooks. |

---
"""

EN_ACT_TITLES = [
    ("## ACT 1: THE ROOFTOP TRAGEDY & URBAN BLIND SPOTS", "**[BGM]:** Suffocating Dark Ambient, a slow heartbeat rhythm, and the oppressive metallic ticking of a clock."),
    ("## ACT 2: THE SCHOLARLY FACADE & THE FAMILIARITY TRAP", "**[BGM]:** Deep melancholic cello weaving into minimalist piano and an eerie electronic drone."),
    ("## ACT 3: THE BATTLE OF WITS & COLLAPSE OF THE NARCISSISTIC EGO", "**[BGM]:** Heavy sub-bass pulse and rapid clock ticks generating a suffocating interrogation room atmosphere."),
    ("## ACT 4: THE ANATOMY OF REMORSE & TRAGEDY OF TWO FATHERS", "**[BGM]:** Torrential, agonized violin capturing an existential crisis of conscience and family devastation."),
    ("## ACT 5: THE ULTIMATE VERDICT, FORGIVENESS & SURVIVAL RED FLAGS", "**[BGM]:** Melancholic, reflective solo piano imbued with profound solemnity and humanistic redemption.")
]

# Japanese Metadata & Structure
JA_HEADER = """# 犯罪心理学オーディオ / ポッドキャスト脚本
**テーマ：** 10大心理指標生態系＆エリート学生の仮面、心の区画化（Compartmentalization）と後悔の本質 — グエン・ドゥック・ギア事件およびG4マンション殺人事件調書。
**バージョン：** 標準A2c/K10 — 犯罪心理生態系＆全240セリフ完全版（2026年11月22日改訂）。

---

## 制作仕様とナレーション構成（PRODUCTION BRIEF）

| 項目 | 音声ドラマ標準仕様（ホスト主導型ドキュメンタリー） |
| :--- | :--- |
| **エピソード名** | 第34話：エリート学生の仮面と眼鏡の奥の感情麻痺（グエン・ドゥック・ギア事件ファイル） |
| **形式** | 捜査ドキュメンタリー・ポッドキャスト — **ホスト**が物語の中心軸を担い、歴史的証拠を繋ぎ、感情の起伏を調整しながら、10大心理指標の要所ごとに専門家の視点（捜査官、犯罪心理学者、一般人）を配置する。 |
| **想定所要時間** | 28〜32分（本編5幕構成＋音響トランジション、全240セリフ完全準拠） |
| **推奨BGM** | 息苦しいダーク・アンビエント、陰鬱なチェロ独奏、ミニマル・ピアノと低音ドローン、法廷の激しいヴァイオリン、そして人間性の救済を象徴する厳かな温かいピアノ。音量：音声下-26dB、場面転換時-14dB。 |
| **声優配分** | - **ホスト（約48％）：** 低く温かみのある深みのある声。歴史的視点、社会的余波、ハロー効果、生存への教訓を人道的なまなざしで導く。<br>- **捜査官（約24％）：** 冷徹で鋭く正確な声。ハノイ市警察刑事局（PC45）の捜査調書、現場検証、シグネチャー対MO、法廷戦略を代表する。<br>- **心理学者（約22％）：** 落ち着いた学術的な声。心の区画化、人格の退行、エリートのハロー効果、後悔の真の本質を解明する。<br>- **一般人（約6％）：** N1（G4マンション住民・第1幕、第5幕）戦慄と深い省察；N2（ホアン・ティ・イエン・第4幕）激しい自責の念に震える若い女性の声。 |
| **引用規則** | 画面上に表示されるすべての直接引用は、捜査調書および裁判記録と100％一致すること。表記規約：二重引用符「 」＝原文ママ引用。 |
| **主要対照資料** | ハノイ市公安局刑事警察部（PC45）2010年事件調書 · ハノイ市人民裁判所2010年7月第一審判決書 · 最高人民裁判所2010年11月控訴審判決書 · 証人供述調書および法医学・鑑識報告書 · 司法精神医学および犯罪行動科学専門教程。 |

---
"""

JA_ACT_TITLES = [
    ("## 第1幕：屋上の悲劇と現代都市の盲点", "**[BGM]:** 息苦しいダーク・アンビエント、静かに刻む心拍音と金属製時計の圧迫的な秒針音。"),
    ("## 第2幕：好青年の仮面と親近感の罠", "**[BGM]:** 重く陰鬱なチェロ独奏、凍りつくようなミニマル・ピアノと不気味な電子ドローン。"),
    ("## 第3幕：取調室の頭脳戦と自己愛の崩壊", "**[BGM]:** 重いサブベースの脈動と激しい時計の秒針音、息詰まる取調室の緊迫感。"),
    ("## 第4幕：後悔の深層と二人の父親の悲劇", "**[BGM]:** 激しく引き裂かれるようなヴァイオリンの旋律、息苦しい良心の危機と家族の崩壊。"),
    ("## 第5幕：最終判決、魂の赦しと生存の警告", "**[BGM]:** 深く静かなピアノ独奏、深い省察と覚醒、そして崇高な人間性の光。")
]

def build_markdown(header, act_titles, sections):
    out = [header.strip(), ""]
    for act_idx, (start, end) in enumerate(ACT_RANGES):
        act_h, act_bgm = act_titles[act_idx]
        out.append(act_h)
        out.append("")
        out.append(act_bgm)
        out.append("")
        for s_idx in range(start, end):
            hdr, lines = sections[s_idx]
            out.append(hdr)
            for line in lines:
                out.append(line)
            out.append("")
        out.append("---")
        out.append("")
    return "\n".join(out)

vn_md = build_markdown(VN_HEADER, VN_ACT_TITLES, VN_SECTIONS)
en_md = build_markdown(EN_HEADER, EN_ACT_TITLES, EN_SECTIONS)
ja_md = build_markdown(JA_HEADER, JA_ACT_TITLES, JA_SECTIONS)

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap34/kichban_tap34_19112026.md', 'w', encoding='utf-8') as f:
    f.write(vn_md)

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap34_EN/kichban_tap34_EN.md', 'w', encoding='utf-8') as f:
    f.write(en_md)

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap34_JA/kichban_tap34_JA.md', 'w', encoding='utf-8') as f:
    f.write(ja_md)

print("Generated markdown files successfully.")
