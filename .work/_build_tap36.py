# -*- coding: utf-8 -*-
# Assembly script to produce Tap 36 VI, EN, JA scripts
import sys, os
sys.path.insert(0, '.work')

from _act1 import ACT1_VI, ACT1_EN, ACT1_JA
from _act2 import ACT2_VI, ACT2_EN, ACT2_JA
from _act3 import ACT3_VI, ACT3_EN, ACT3_JA
from _act4 import ACT4_VI, ACT4_EN, ACT4_JA
from _act5 import ACT5_VI, ACT5_EN, ACT5_JA

HEADER_VI = """# KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM
**Chủ đề:** Hệ sinh thái 10 chỉ dấu tâm lý & Khởi phát tâm thần phân liệt sớm, Ảo giác thính giác mệnh lệnh & Bi kịch xả súng học đường — Hồ sơ Kipland Kinkel và Thảm kịch Trường Trung học Thurston 1998.
**Phiên bản:** Chuẩn A2c/K10 — Hệ sinh thái 10 chỉ dấu tâm lý học tội phạm & Bổ sung phân tích biến chuyển tâm lý đa chiều ngày 20/11/2026.

---

## THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN (PRODUCTION BRIEF)

| Hạng mục | Thiết lập chuẩn cho tập Audio (Host-Driven Documentary) |
| :--- | :--- |
| **Tên tập (Episode Title)** | Tập 36: Tiếng Nói Trong Tâm Trí — Khởi Phát Tâm Thần Phân Liệt & Cơn Địa Chấn Thurston High (Hồ Sơ Kip Kinkel) |
| **Định dạng (Format)** | Podcast Tài liệu Điều tra (Narrator-led Documentary) – **Host** nắm giữ trục xương sống kể chuyện, kết nối dữ liệu lịch sử, điều phối nhịp cảm xúc và mời các góc nhìn chuyên môn (Điều tra viên, Chuyên gia tâm lý, Người bình thường) vào đúng điểm nút kịch tính theo Hệ sinh thái 10 chỉ dấu tâm lý. |
| **Tổng thời lượng dự kiến** | 28 – 32 phút (5 hồi nội dung + các khoảng lặng chuyển cảnh âm thanh) |
| **Nhạc nền (BGM) gợi ý** | Dark Ambient ngột ngạt, Solo Cello u uất, Tiếng đàn Dương cầm tối giản (Minimalist Piano) kết hợp nhịp Drone điện tử rùng rợn, Tiếng vĩ cầm giằng xé phòng xử án, và Warm Piano ấm áp trang nghiêm đúc kết. Âm lượng: -26dB dưới giọng đọc, nâng lên -14dB ở các điểm chuyển cảnh. |
| **Cơ chế phân bổ giọng đọc** | - **Host (~48% thời lượng):** Giọng nam trầm ấm, sâu lắng, dẫn dắt câu chuyện với góc nhìn nhân văn, dư chấn xã hội, hiệu ứng hào quang và bài học sinh tồn.<br>- **Điều tra viên (~24%):** Giọng nam đanh thép, sắc lạnh, chuẩn xác, đại diện cho hồ sơ nghiệp vụ, chứng cứ hiện trường, chữ ký Signature vs MO và chiến thuật pháp lý của Sở Cảnh sát Springfield & Quận Lane.<br>- **Chuyên gia tâm lý (~22%):** Giọng điềm đạm, mang tính học thuật sâu sắc, bóc tách hiện tượng tâm thần phân liệt hoang tưởng, ảo giác thính giác mệnh lệnh, tổn thương ái kỷ, cơ chế chia ngăn và cơ chế hối hận sau 23 năm.<br>- **Người bình thường (~6%):** N1 (Bạn học trường Thurston - Hồi 1, 5 câu) giọng nữ trẻ hoang mang, bàng hoàng; N2 (Lời trần tình minh họa Kip Kinkel 2021 - Hồi 4, 8 câu) giọng nam trưởng thành trầm buồn, dằn vặt tội lỗi cùng cực. |
| **Quy tắc trích dẫn** | Mọi trích dẫn nguyên văn trong hình phải đúng 100% so với nguồn lưu trữ. Quy ước ký hiệu: ngoặc kép “ ” = trích dẫn nguyên văn. |
| **Nguồn đối chiếu chính** | Hồ sơ vụ án của Sở Cảnh sát Springfield (Springfield Police Department) · Bản ghi âm thẩm vấn của Thám tử Al Warthen 1998 · Hồ sơ tòa án Quận Lane (Lane County Circuit Court, Thẩm phán Jack Mattison) · Báo cáo giám định tâm thần của Tiến sĩ Orin Bolstad & Tiến sĩ William Sack · Phỏng vấn độc quyền độc lập trên The Huffington Post (tháng 6/2021) · Phóng sự điều tra PBS Frontline: "The Killer at Thurston High" (2000) · Lý thuyết Phát triển Thần kinh Vị thành niên (Laurence Steinberg) · Học thuyết The Gift of Fear (Gavin de Becker). |

---

---

"""

HEADER_EN = """# FORENSIC PSYCHOLOGY AUDIO / PODCAST SCRIPT
**Theme:** 10 Psychological Indicators Ecosystem & Early-Onset Paranoid Schizophrenia, Command Auditory Hallucinations & The Thurston High Tragedy — The Case of Kipland Kinkel.
**Version:** Standard A2c/K10 — Forensic Behavioral Ecosystem & Multilingual Depth Analysis (November 20, 2026).

---

## PRODUCTION BRIEF & NARRATIVE STRUCTURE

| Category | Standard Specifications for Audio Episode (Host-Driven Documentary) |
| :--- | :--- |
| **Episode Title** | Episode 36: Voices in the Mind — Early-Onset Psychosis & The Thurston High Catastrophe (The Kip Kinkel Case) |
| **Format** | Investigative Documentary Podcast (Narrator-led Documentary) – **Host** anchors the core narrative spine, connecting historical evidence, balancing emotional dynamics, and inviting professional perspectives (Investigator, Psychologist, Ordinary Person) at precise dramatic nodes. |
| **Estimated Runtime** | 28 – 32 minutes (5 narrative acts + tense acoustic scene transitions) |
| **Recommended BGM** | Oppressive Dark Ambient, Somber Solo Cello, Minimalist Piano fused with chilling electronic drones, Agonizing Courtroom Violins, and Warm Solemn Piano for final reflections. Volume: -26dB under speech, rising to -14dB at scene shifts. |
| **Cast Distribution** | - **Host (~48% duration):** Deep, warm, resonant male voice. Guides the narrative through humanistic perspectives, social reverberations, halo effects, and survival wisdom.<br>- **Investigator (~24%):** Sharp, clinical, authoritative male voice. Articulates Springfield Police & Lane County investigative casework, ballistics, physical evidence, and legal tactics.<br>- **Psychologist (~22%):** Poised, scholarly female voice. Dissects early-onset paranoid schizophrenia, command auditory hallucinations, narcissistic mortification, compartmentalization, and the neurobiology of remorse.<br>- **Ordinary Person (~6%):** N1 (Thurston High Classmate - Act 1, 5 lines) young female voice trembling in shock; N2 (Kip Kinkel Monologue 2021 - Act 4, 8 lines) mature male voice steeped in profound remorse and guilt. |
| **Quotation Rules** | Every verbatim quotation displayed must match official archives 100%. Protocol: “ ” = verbatim citation. |
| **Primary Reference Sources** | Springfield Police Department Case Files · Detective Al Warthen 1998 Interrogation Audio · Lane County Circuit Court Records (Judge Jack Mattison) · Forensic Psychiatric Evaluations by Dr. Orin Bolstad & Dr. William Sack · The Huffington Post Exclusive Investigation (June 2021) · PBS Frontline: "The Killer at Thurston High" (2000) · Adolescent Brain Cognitive Development Studies (Laurence Steinberg) · The Gift of Fear (Gavin de Becker). |

---

---

"""

HEADER_JA = """# 犯罪心理学オーディオ／ポッドキャスト台本
**テーマ：** 10大心理指標生態系＆早期発症型統合失調症、命令性幻聴とサーストン高校銃撃事件の悲劇 — キップ・キンケル事件の記録。
**バージョン：** 標準A2c/K10 — 犯罪心理生態系＆多角的心理変容分析（2026年11月20日）。

---

## 制作仕様とナレーション構成（PRODUCTION BRIEF）

| 項目 | 音声エピソード標準設定（Host-Driven Documentary） |
| :--- | :--- |
| **エピソード名** | 第36話：心の中の声 — 早期発症型統合失調症とサーストン高校の激震（キップ・キンケル事件） |
| **フォーマット** | 調査ドキュメンタリー・ポッドキャスト（Narrator-led Documentary） – **ホスト**が物語の根幹を担い、歴史的資料を繋ぎ、感情の起伏を調和させ、10大心理指標に基づいて専門的視点（捜査官、心理学者、一般人）を的確な劇的転換点へと招き入れます。 |
| **予定総時間** | 28 – 32分（5幕構成＋緊迫した音響の間） |
| **推奨BGM** | 息苦しいダーク・アンビエント、陰鬱なチェロ・ソロ、戦慄する電子ドローンを融合させたミニマル・ピアノ、緊迫した法廷のバイオリン、そして厳粛な回顧を告げる温かなピアノ。音量：ナレーション下 -26dB、場面転換点 -14dB。 |
| **キャスト構成** | - **ホスト（全体の約48%）：** 深みと温かみのある男性の声。人道的な視点、社会的余波、ハロー効果、生存への教訓を通じて物語を導きます。<br>- **捜査官（約24%）：** 冷徹で鋭敏、正確無比な男性の声。スプリングフィールド警察およびレーン郡の実地捜査記録、物的証拠、シグネチャー対MO、法廷戦略を代弁します。<br>- **心理学者（約22%）：** 穏やかで深い学術性を備えた女性の声。早期発症型統合失調症、命令性幻聴、自己愛的損傷、認知的区画化、23年後の悔悟の神経科学を解剖します。<br>- **一般人（約6%）：** N1（サーストン高校の同級生 - 第1幕、5文）衝撃と恐怖に震える若い女性の声；N2（キップ・キンケルの告白2021年 - 第4幕、8文）罪悪感に苛まれ深く苦悩する成熟した男性の声。 |
| **引用規則** | 画面上に表示されるすべての逐語的引用は、公式記録と100%一致していなければなりません。表記規定：「…」＝逐語的引用。 |
| **主要参照資料** | スプリングフィールド警察事件記録 · アル・ワーセン捜査官による1998年取調べ録音 · レーン郡巡回裁判所記録（ジャック・マティソン判事） · オーリン・ボルスタッド博士＆ウィリアム・サック博士による精神鑑定記録 · ハフィントン・ポスト独占インタビュー（2021年6月） · PBSフロントライン『サーストン高校の殺人犯』（2000年） · 思春期脳科学理論（ローレンス・スタインバーグ） · 『ギフト・オブ・フィアー』（ギャビン・デ・ベッカー）。 |

---

---

"""

def render_act(act_data):
    out = act_data["header"]
    for turn in act_data["turns"]:
        if "cue" in turn:
            out += turn["cue"]
        else:
            role = turn["role"]
            direction = turn.get("direction", "")
            dir_str = f" *({direction})*" if direction else ""
            out += f"**{role}**{dir_str}:\n"
            for line in turn["lines"]:
                out += f"{line}\n"
            out += "\n"
    return out

# Generate files
vn_content = HEADER_VI + render_act(ACT1_VI) + render_act(ACT2_VI) + render_act(ACT3_VI) + render_act(ACT4_VI) + render_act(ACT5_VI)
en_content = HEADER_EN + render_act(ACT1_EN) + render_act(ACT2_EN) + render_act(ACT3_EN) + render_act(ACT4_EN) + render_act(ACT5_EN)
ja_content = HEADER_JA + render_act(ACT1_JA) + render_act(ACT2_JA) + render_act(ACT3_JA) + render_act(ACT4_JA) + render_act(ACT5_JA)

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap36/kichban_tap36_19112026.md', 'w', encoding='utf-8') as f:
    f.write(vn_content)

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap36_EN/kichban_tap36_EN.md', 'w', encoding='utf-8') as f:
    f.write(en_content)

with open('01_KICH_BAN/Ho_So_Toi_Pham/Tap36_JA/kichban_tap36_JA.md', 'w', encoding='utf-8') as f:
    f.write(ja_content)

print("Generated all 3 scripts successfully.")
