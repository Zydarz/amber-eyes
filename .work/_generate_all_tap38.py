# -*- coding: utf-8 -*-
"""
Builder that writes out:
1. 01_KICH_BAN/Tap38/kichban_tap38_19112026.md (VN)
2. 01_KICH_BAN/Tap38_EN/kichban_tap38_EN.md (EN)
3. 01_KICH_BAN/Tap38_JA/kichban_tap38_JA.md (JA)
4. .work/script_tap38.json (VN)
5. .work/script_tap38_EN.json (EN)
6. .work/script_tap38_JA.json (JA)
And verifies sentence parsing with parse_kichban.py.
"""

import os
import sys
import json
from pathlib import Path

sys.path.insert(0, '.work')
import _tap38_act1
import _tap38_act2_5
import _tap38_act1_en
import _tap38_act2_5_en
import _tap38_act1_ja
import _tap38_act2_5_ja
import parse_kichban

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

def render_markdown(title, subtitle, brief_table, acts, act_titles, lang):
    out = []
    out.append(f"# {title}")
    out.append(f"**{subtitle[0]}:** {subtitle[1]}")
    out.append(f"**{subtitle[2]}:** {subtitle[3]}")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"## {brief_table['heading']}")
    out.append("")
    out.append(f"| {brief_table['col1']} | {brief_table['col2']} |")
    out.append("| :--- | :--- |")
    for row in brief_table['rows']:
        out.append(f"| **{row[0]}** | {row[1]} |")
    out.append("")
    out.append("---")
    out.append("")

    role_headers = {
        'VN': {
            'H': "**HOST** *(chậm rãi, giọng trầm ấm gợi mở không gian lịch sử)*:",
            'D': "**ĐIỀU TRA VIÊN** *(giọng nam sắc bén, tái hiện không gian hiện trường)*:",
            'C': "**CHUYÊN GIA TÂM LÝ** *(phân tích chuyên sâu về cơ chế hành vi)*:",
            'N': "**NGƯỜI BÌNH THƯỜNG** *(giọng hồi hộp, nghẹn ngào)*:",
        },
        'EN': {
            'H': "**HOST** *(slowly, in a warm and reflective documentary tone)*:",
            'D': "**INVESTIGATOR** *(sharp and cold, reconstructing physical evidence)*:",
            'C': "**PSYCHOLOGIST** *(in-depth forensic behavioral analysis)*:",
            'N': "**ORDINARY PERSON** *(youthful voice filled with grief and tension)*:",
        },
        'JA': {
            'H': "**ホスト** *(低く落ち着いた声で、歴史的ドキュメンタリーの空間を切り拓くように)*:",
            'D': "**捜査官** *(鋭く冷静な声で、客観的な証拠を再構築するように)*:",
            'C': "**心理学者** *(行動科学と深層心理の専門的見地から)*:",
            'N': "**一般人** *(緊迫した息遣いと痛切な響きを帯びて)*:",
        }
    }

    act_prefix = {
        'VN': 'HỒI',
        'EN': 'ACT',
        'JA': '第'
    }

    for act_idx, act_items in enumerate(acts, 1):
        if lang == 'JA':
            out.append(f"## 第{act_idx}幕：{act_titles[act_idx-1]}")
        else:
            out.append(f"## {act_prefix[lang]} {act_idx}: {act_titles[act_idx-1]}")
        out.append("")

        for item in act_items:
            kind = item[0]
            if kind == 'BGM':
                out.append(f"**[BGM]:** {item[1]}")
                out.append("")
            elif kind == 'SFX':
                out.append(f"**[SFX]:** {item[1]}")
                out.append("")
            elif kind == 'NGHI':
                if lang == 'VN':
                    out.append(f"**[Nghỉ 1.5 giây – {item[1]}]**")
                elif lang == 'EN':
                    out.append(f"**[Pause 1.5 seconds – {item[1]}]**")
                elif lang == 'JA':
                    out.append(f"**[休止 1.5秒 – {item[1]}]**")
                out.append("")
            elif kind == 'LOI':
                role = item[1]
                header = role_headers[lang].get(role, f"**{role}**:")
                out.append(header)
                for sent in item[2]:
                    out.append(sent)
                out.append("")
        out.append("---")
        out.append("")

    return "\n".join(out)

# 1. VN
vn_acts = [_tap38_act1.get_acts(), _tap38_act2_5.get_act2(), _tap38_act2_5.get_act3(), _tap38_act2_5.get_act4(), _tap38_act2_5.get_act5()]
vn_act_titles = [
    "SỰ BIẾN MẤT BÊN ĐƯỜNG VÀ CHIẾC BẪY TRẮNG NGOẠI Ô VIENNA",
    "3.096 NGÀY DƯỚI HẦM NGẦM 5M² VÀ CHIẾN LƯỢC SINH TỒN KÉP",
    "CỬA SỔ CƠ HỘI VÀNG VÀ CUỘC ĐÀO THOÁT NGOÀN MỤC",
    "SỰ SỤP ĐỔ CỦA ẢO TƯỞNG TOÀN NĂNG VÀ BẢN ÁN TRÊN ĐƯỜNG RAY",
    "NGỌN NẾN NHÂN BẢN VÀ BÀI HỌC THỨC TỈNH XÃ HỘI"
]
vn_brief = {
    'heading': "THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN (PRODUCTION BRIEF)",
    'col1': "Hạng mục",
    'col2': "Thiết lập chuẩn cho tập Audio (Host-Driven Documentary)",
    'rows': [
        ("Tên tập (Episode Title)", "Tập 38: Hồ Sơ Natascha Kampusch — 3.096 Ngày Dưới Lòng Đất & Ý Chí Sinh Tồn Đánh Bại Thao Túng"),
        ("Định dạng (Format)", "Podcast Tài liệu Điều tra (Narrator-led Documentary) – Host giữ trục dẫn chuyện chính, phối hợp cùng Điều tra viên, Chuyên gia tâm lý và Nhân chứng theo Hệ sinh thái 10 chỉ dấu tâm lý."),
        ("Tổng thời lượng dự kiến", "28 – 32 phút (5 hồi chuẩn A2c, 240 câu thoại)"),
        ("Nhạc nền (BGM) gợi ý", "Dark Ambient lạnh lẽo, Cello u uất, Dương cầm tối giản (Minimalist Piano) căng thẳng, Vĩ cầm giằng xé phòng xét hỏi, và Piano ấm áp trang trọng đúc kết."),
        ("Cơ chế phân bổ giọng đọc", "Host (Cú) ~52%, Điều tra viên (Sói) ~21%, Chuyên gia tâm lý (Cáo) ~22%, Người bình thường (N1/N2) ~5%."),
    ]
}
vn_md = render_markdown(
    "KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM",
    ("Chủ đề", "Hệ sinh thái 10 chỉ dấu tâm lý & Bản năng sinh tồn đánh bại thao túng toàn năng – Hồ sơ Natascha Kampusch & Wolfgang Priklopil",
     "Phiên bản", "Chuẩn A2c/K10 — Hệ sinh thái 10 chỉ dấu tâm lý học tội phạm & Bổ sung phân tích biến chuyển tâm lý 5 chủ thể (240 câu thoại)"),
    vn_brief, vn_acts, vn_act_titles, 'VN'
)

# 2. EN
en_acts = [_tap38_act1_en.get_acts_en(), _tap38_act2_5_en.get_act2_en(), _tap38_act2_5_en.get_act3_en(), _tap38_act2_5_en.get_act4_en(), _tap38_act2_5_en.get_act5_en()]
en_act_titles = [
    "THE FATEFUL ABDUCTION AND THE WHITE SUBURBAN TRAP",
    "3,096 DAYS IN A SUBTERRANEAN BUNKER AND DUAL SURVIVAL DEFENSE",
    "THE GOLDEN WINDOW OF OPPORTUNITY AND THE DARING FLIGHT",
    "THE SHATTERING OF OMNIPOTENCE AND RAILWAY SUICIDE",
    "THE SOLITARY CANDLE AND SOCIETAL LESSONS OF REBIRTH"
]
en_brief = {
    'heading': "PRODUCTION BRIEF & NARRATIVE STRUCTURE",
    'col1': "Component",
    'col2': "Production Specification (Host-Driven Documentary)",
    'rows': [
        ("Episode Title", "Episode 38: Natascha Kampusch — 3,096 Days Underground & The Indomitable Spirit Defeating Mind Control"),
        ("Format", "Investigative Documentary Podcast — Host-led structure integrated with Forensic Investigator, Psychologist, and Eyewitness accounts following the 10-Indicator Behavioral Ecosystem."),
        ("Estimated Duration", "28 – 32 minutes (5-Act structure, exactly 240 sentences)"),
        ("Musical Mood (BGM)", "Subterranean Dark Ambient, Mournful Cello, Minimalist Tension Piano, Strident Agitated Violins, and Warm Solemn Epilogue Piano."),
        ("Voice Cast Allocation", "Host ~52%, Forensic Investigator ~21%, Behavioral Psychologist ~22%, Ordinary Person/Insider ~5%."),
    ]
}
en_md = render_markdown(
    "FORENSIC CRIMINAL PSYCHOLOGY PODCAST SCRIPT",
    ("Theme", "10-Indicator Behavioral Ecosystem & Active Survival Defeating Coercive Mind Control – Case of Natascha Kampusch & Wolfgang Priklopil",
     "Version", "Standard A2c/K10 — Multi-perspective Behavioral Analysis Across 5 Entities (Full 240 Sentences)"),
    en_brief, en_acts, en_act_titles, 'EN'
)

# 3. JA
ja_acts = [_tap38_act1_ja.get_acts_ja(), _tap38_act2_5_ja.get_act2_ja(), _tap38_act2_5_ja.get_act3_ja(), _tap38_act2_5_ja.get_act4_ja(), _tap38_act2_5_ja.get_act5_ja()]
ja_act_titles = [
    "運命の白昼拉致とウィーン郊外の罠",
    "地下室の3096日と二重精神の生存適応戦略",
    "黄金の機会の窓と白昼の決死脱出劇",
    "万能妄想の崩壊と線路上の自死",
    "一筋のロウソクと人間の尊厳の再生"
]
ja_brief = {
    'heading': "制作仕様とナレーション構成（PRODUCTION BRIEF）",
    'col1': "項目",
    'col2': "設定内容（ホスト主導型ドキュメンタリー）",
    'rows': [
        ("エピソード名", "第38話：ナターシャ・カンプシュ事件 — 地下の3096日とマインドコントロールを打ち砕いた生存の意志"),
        ("フォーマット", "調査ドキュメンタリー・ポッドキャスト — ホストが主軸を担い、捜査官、心理学者、一般人と連携する10指標心理行動生態系モデル。"),
        ("想定総尺", "28〜32分（5幕構成、完全一致240センテンス）"),
        ("推奨BGM", "冷徹なダークアンビエント、哀愁のチェロ、緊迫のミニマルピアノ、激動のバイオリン、そして再生を告げる温かなエピローグピアノ。"),
        ("キャスト配分", "ホスト ~52%、捜査官 ~21%、心理専門家 ~22%、一般人 ~5%。"),
    ]
}
ja_md = render_markdown(
    "犯罪心理学オーディオ／ポッドキャスト台本",
    ("テーマ", "10指標心理生態系モデル＆全能的支配を打ち破る生存適応本能 — ナターシャ・カンプシュ＆ヴォルフガング・プリクロピル事件記録",
     "バージョン", "標準A2c/K10準拠 — 5主体の心理変容を解剖する240センテンス完全版（多言語対応）"),
    ja_brief, ja_acts, ja_act_titles, 'JA'
)

# Write files
vn_path = ROOT / "01_KICH_BAN" / "Tap38" / "kichban_tap38_19112026.md"
en_path = ROOT / "01_KICH_BAN" / "Tap38_EN" / "kichban_tap38_EN.md"
ja_path = ROOT / "01_KICH_BAN" / "Tap38_JA" / "kichban_tap38_JA.md"

with open(vn_path, "w", encoding="utf-8") as f:
    f.write(vn_md)
print(f"Written: {vn_path}")

with open(en_path, "w", encoding="utf-8") as f:
    f.write(en_md)
print(f"Written: {en_path}")

with open(ja_path, "w", encoding="utf-8") as f:
    f.write(ja_md)
print(f"Written: {ja_path}")

# Now parse and verify each file
for path in [vn_path, en_path, ja_path]:
    parsed = parse_kichban.parse_file(str(path))
    s_cnt = sum(len(x.get('sentences', [])) for x in parsed if isinstance(x, dict))
    print(f"Parsed {path.name}: {len(parsed)} elements, {s_cnt} sentences")
    assert len(parsed) == 52, f"Expected 52 elements, got {len(parsed)}"
    assert s_cnt == 240, f"Expected 240 sentences, got {s_cnt}"

# Generate json scripts
parsed_vn = parse_kichban.parse_file(str(vn_path))
parsed_en = parse_kichban.parse_file(str(en_path))
parsed_ja = parse_kichban.parse_file(str(ja_path))

with open(ROOT / ".work" / "script_tap38.json", "w", encoding="utf-8") as f:
    json.dump(parsed_vn, f, indent=2, ensure_ascii=False)
with open(ROOT / ".work" / "script_tap38_EN.json", "w", encoding="utf-8") as f:
    json.dump(parsed_en, f, indent=2, ensure_ascii=False)
with open(ROOT / ".work" / "script_tap38_JA.json", "w", encoding="utf-8") as f:
    json.dump(parsed_ja, f, indent=2, ensure_ascii=False)

print("Saved script_tap38.json, script_tap38_EN.json, script_tap38_JA.json successfully!")
