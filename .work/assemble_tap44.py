# -*- coding: utf-8 -*-
"""Generate and assemble full markdown scripts for Tap 44 in VN, EN, and JA."""

import sys
sys.path.insert(0, '.work')

from tap44_acts_1_2 import ACT1_VN, ACT2_VN
from tap44_acts_3_4_5 import ACT3_VN, ACT4_VN, ACT5_VN

from tap44_acts_1_2_en import ACT1_EN, ACT2_EN
from tap44_acts_3_4_5_en import ACT3_EN, ACT4_EN, ACT5_EN

from tap44_acts_1_2_ja import ACT1_JA, ACT2_JA
from tap44_acts_3_4_5_ja import ACT3_JA, ACT4_JA, ACT5_JA

# Role names per language
ROLE_NAMES = {
    'VN': {
        'H': 'HOST',
        'D': 'ĐIỀU TRA VIÊN',
        'C': 'CHUYÊN GIA TÂM LÝ',
        'N': 'NGƯỜI BÌNH THƯỜNG',
    },
    'EN': {
        'H': 'HOST',
        'D': 'INVESTIGATOR',
        'C': 'PSYCHOLOGIST',
        'N': 'ORDINARY PERSON',
    },
    'JA': {
        'H': 'ホスト',
        'D': '捜査官',
        'C': '心理学者',
        'N': '一般人',
    }
}

ACT_HEADINGS = {
    'VN': [
        "## HỒI 1: KHỞI NGUỒN CƠN ÁC MỘNG VÀ BÓNG MA TRONG ỐNG NGHIỆM",
        "## HỒI 2: CHÂN DUNG TÂM LÝ PHI LÝ VÀ CẠM BẪY THIÊN KIẾN XÁC NHẬN",
        "## HỒI 3: ĐIỂM MÙ THỂ CHẾ VÀ ĐIỂM GÃY TÂM LÝ KHÔNG THỂ BẢO CHỮA",
        "## HỒI 4: BỨC MÀN NHUNG RƠI XUỐNG VÀ BẢN CHẤT CỦA SỰ ĂN NĂN",
        "## HỒI 5: CÔNG LÝ ĐÍCH THỰC VÀ BÀI HỌC CẢNH BÁO ĐỎ CHO NHÂN LOẠI",
    ],
    'EN': [
        "## ACT 1: ORIGINS OF THE NIGHTMARE AND THE PHANTOM IN THE TEST TUBE",
        "## ACT 2: THE PARADOXICAL PROFILE AND THE CONFIRMATION BIAS TRAP",
        "## ACT 3: INSTITUTIONAL BLINDSPOTS AND THE UNDENIABLE TIPPING POINT",
        "## ACT 4: THE VEIL LIFTS AND THE PSYCHOLOGY OF PROFESSIONAL REMORSE",
        "## ACT 5: GENUINE JUSTICE AND RED-FLAG SURVIVAL PRINCIPLES FOR HUMANITY",
    ],
    'JA': [
        "## 第1幕：悪夢の起源と試験管の中の幻影",
        "## 第2幕：不条理なプロファイルと確証バイアスの罠",
        "## 第3幕：組織の盲点と言い逃れのできない認知的限界点",
        "## 第4幕：暴かれた幕と専門的悔恨の深層心理",
        "## 第5幕：真の正義の光と人類へのサバイバル原則",
    ]
}

HEADER_VN = """# KỊCH BẢN CHI TIẾT TẬP 44: HỒ SƠ BÓNG MA HEILBRONN — HỒ SƠ SÁT NHÂN VÔ HÌNH & BÀI HỌC VỀ Ô NHIỄM MẪU ADN

* **Đề tài:** Cuộc truy lùng nữ sát thủ vô hình để lại ADN tại 40 hiện trường ở Đức, Áo, Pháp suốt 16 năm (1993–2009).
* **Chủ đề tâm lý:** Thiên kiến xác nhận (Confirmation Bias) trong điều tra, Tầm nhìn đường hầm (Tunnel Vision), Sự sùng bái công nghệ mù quáng, Bẫy chi phí chìm, và Cơ chế hối hận chân thực của thể chế tư pháp.
* **Phiên bản:** Chuẩn A2c/K10 — Hệ sinh thái 10 chỉ dấu tâm lý học tội phạm & Bổ sung phân tích biến chuyển tâm lý đa chiều ngày 21/11/2026.
* **Thời lượng dự kiến:** 28 – 32 phút (5 Hồi chuẩn mực, 240 câu thoại)
* **Tiêu chuẩn An toàn YouTube (Rule V9):** 100% YouTube Safe, không mô tả trực diện thương tổn thể xác hay chi tiết rùng rợn; tập trung 100% vào phân tích tâm lý học tội phạm, vi biểu cảm, cạm bẫy nhận thức và bài học phòng ngừa sai lầm pháp y.

---

## BẢNG PHÂN VAI VÀ CẤU TRÚC GIỌNG ĐỌC (PRODUCTION BRIEF)

| Ký hiệu | Vai trò | Tên nhân vật thể hiện | Tỷ lệ & Đặc điểm giọng đọc |
| :--- | :--- | :--- | :--- |
| **H** | **Dẫn chuyện (Host)** | Cú (Host Amber Eyes) | ~48% thời lượng. Giọng nam trầm ấm, sâu sắc, dẫn dắt lịch sử, dư chấn xã hội, hiệu ứng hào quang công nghệ và bài học sinh tồn. |
| **D** | **Điều tra viên** | Sói (Điều tra viên) | ~24% thời lượng. Giọng nam đanh thép, sắc lạnh, chuẩn xác, đại diện cho hồ sơ nghiệp vụ cảnh sát Đức, hiện trường Heilbronn và sự sụp đổ bẫy chi phí chìm. |
| **C** | **Chuyên gia Tâm lý** | Cáo (Chuyên gia tâm lý) | ~22% thời lượng. Nữ điềm đạm, mang tính học thuật sâu sắc, bóc tách thiên kiến xác nhận, tầm nhìn đường hầm, tâm lý bầy đàn và giải mã cơ chế hối hận. |
| **N** | **Người bình thường** | Nhân chứng / Nữ công nhân nhà máy | ~6% thời lượng. N1 (Hồi 1, 5 câu: Nhân chứng tại hiện trường Heilbronn); N2 (Hồi 4, 8 câu: Nữ công nhân đóng gói tăm bông, run rẩy, giằng xé lương tâm). |

---
"""

HEADER_EN = """# DETAILED SCRIPT EPISODE 44: THE PHANTOM OF HEILBRONN — THE INVISIBLE KILLER & THE LESSON OF FORENSIC CONTAMINATION

* **Topic:** The sixteen-year international manhunt for an elusive female phantom whose DNA linked forty crime scenes across Germany, Austria, and France (1993–2009).
* **Psychological Themes:** Confirmation Bias in criminal investigations, Tunnel Vision, Uncritical Technological Deference, Sunk Cost Fallacy, and the Psychology of Institutional Remorse.
* **Edition:** Standard A2c/K10 — Ecosystem of 10 Psychological and Behavioral Indicators & Multidimensional Psychological Transformation Analysis (November 21, 2026).
* **Estimated Duration:** 28 – 32 minutes (5 Standard Acts, 240 spoken dialogue sentences)
* **YouTube Advertising Safety (Rule V9):** 100% YouTube Safe, strictly avoiding graphic physical descriptions; 100% focused on behavioral analysis, cognitive vulnerabilities, and institutional forensic safeguards.

---

## CASTING AND VOCAL PRODUCTION BRIEF

| Symbol | Role | Persona | Distribution & Vocal Dynamics |
| :--- | :--- | :--- | :--- |
| **H** | **Host (Narrator)** | Owl (Host Amber Eyes) | ~48% duration. Warm, profound documentary cadence, historical context, societal blindspots, and survival principles. |
| **D** | **Investigator** | Wolf (Investigator) | ~24% duration. Sharp, authoritative, analytical, representing German state police forensics and the confrontation with operational hubris. |
| **C** | **Psychologist** | Fox (Psychologist) | ~22% duration. Academic, poised, dissecting confirmation bias, groupthink, institutional conformity, and the mechanics of professional remorse. |
| **N** | **Ordinary Person** | Eyewitness / Factory Worker | ~6% duration. N1 (Act 1, 5 sentences: Eyewitness near Heilbronn); N2 (Act 4, 8 sentences: Elderly cotton swab packaging worker, bewildered and grieving). |

---
"""

HEADER_JA = """# 詳細台本 第44話：ハイルブロンの怪人 — 見えざる連続殺人鬼の虚像と鑑識汚染の教訓

* **テーマ：** 16年間（1993年〜2009年）にわたりドイツ、オーストリア、フランスの40箇所の事件現場を結んだ謎の女性DNAを巡る国際捜査の記録。
* **心理学的主題：** 捜査における確証バイアス、トンネル視野、科学技術への盲目的信仰、サンクコストの罠、および組織的悔恨の深層心理。
* **規格：** A2c/K10準拠 — 犯罪心理・行動の10の指標エコシステムおよび多角的心理変容分析（2026年11月21日改訂版）。
* **予定時間：** 28分〜32分（標準5幕構成、240セリフ文）
* **YouTube広告安全性基準（Rule V9）：** 100% YouTube Safe準拠。直接的な暴力描写や残酷な表現を完全排除し、行動科学、認知的脆弱性、および科学捜査の教訓に100%特化。

---

## 配役表および音声演出要領（PRODUCTION BRIEF）

| 記号 | 役割 | 演じるキャラクター | 配分および音声の特徴 |
| :--- | :--- | :--- | :--- |
| **H** | **ホスト（語り手）** | フクロウ（アンバー・アイズ・ホスト） | 約48%配分。温かく深みのある語り口、歴史的背景、社会的盲点、ハロー効果、およびサバイバル原則の総括。 |
| **D** | **捜査官** | オオカミ（捜査官） | 約24%配分。冷徹で厳格なプロフェッショナル、刑事鑑識の実務、現場検証、およびサンクコストの崩壊。 |
| **C** | **心理学者** | キツネ（心理学者） | 約22%配分。知的で落ち着いた学術的視点、確証バイアス、トンネル視野、集団浅慮の解明、および専門的後悔の深層分析。 |
| **N** | **一般人** | 目撃者 / 工場作業員 | 約6%配分。N1（第1幕、5文：ハイルブロン事件現場の目撃者）；N2（第4幕、8文：綿棒工場の高齢女性作業員、震えと良心の葛藤）。 |

---
"""

def assemble_script(lang, header, acts):
    lines = [header]
    role_map = ROLE_NAMES[lang]
    headings = ACT_HEADINGS[lang]
    
    for act_idx, act in enumerate(acts):
        lines.append(headings[act_idx])
        lines.append("")
        for item in act:
            kind = item[0]
            if kind == 'BGM':
                lines.append(f"**[BGM]:** {item[1]}")
                lines.append("")
            elif kind == 'SFX':
                lines.append(f"**[SFX]:** {item[1]}")
                lines.append("")
            elif kind == 'NGHI':
                sec = item[1]
                desc = item[2]
                if lang == 'VN':
                    lines.append(f"**[Nghỉ {sec} giây – {desc}]**")
                elif lang == 'EN':
                    lines.append(f"**[Pause {sec} seconds – {desc}]**")
                elif lang == 'JA':
                    lines.append(f"**[休止 {sec}秒 – {desc}]**")
                lines.append("")
            elif kind == 'LOI':
                role = item[1]
                direction = item[2]
                sentences = item[3]
                role_str = role_map[role]
                lines.append(f"**{role_str}** *({direction})*:")
                for s in sentences:
                    lines.append(s)
                lines.append("")
        lines.append("---")
        lines.append("")
    return "\n".join(lines)

vn_text = assemble_script('VN', HEADER_VN, [ACT1_VN, ACT2_VN, ACT3_VN, ACT4_VN, ACT5_VN])
en_text = assemble_script('EN', HEADER_EN, [ACT1_EN, ACT2_EN, ACT3_EN, ACT4_EN, ACT5_EN])
ja_text = assemble_script('JA', HEADER_JA, [ACT1_JA, ACT2_JA, ACT3_JA, ACT4_JA, ACT5_JA])

with open('01_KICH_BAN/Tap44/kichban_tap44_19112026.md', 'w', encoding='utf-8') as f:
    f.write(vn_text)

with open('01_KICH_BAN/Tap44_EN/kichban_tap44_EN.md', 'w', encoding='utf-8') as f:
    f.write(en_text)

with open('01_KICH_BAN/Tap44_JA/kichban_tap44_JA.md', 'w', encoding='utf-8') as f:
    f.write(ja_text)

print("All 3 scripts successfully assembled and saved to their respective directories.")
