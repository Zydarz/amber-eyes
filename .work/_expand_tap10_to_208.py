#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Expand Episode 10 scripts across all 4 languages (VN, EN, JA, KO) to 208 sentences (>200 sentences).
Maintains exact 1:1 Parity:
- 52 elements
- 36 LOI turns
- 208 sentences (1:1 per element)
- Strict adherence to A2c / K10, V9 (no prohibited gore), G1 (no '...').
"""

import os
import sys
import json
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# -----------------------------------------------------------------------------
# 1. READ ORIGINAL SCRIPT_TAP10.JSON
# -----------------------------------------------------------------------------
with open(ROOT / ".work" / "script_tap10.json", "r", encoding="utf-8") as f:
    data_vn = json.load(f)

print(f"Loaded script_tap10.json: {len(data_vn)} elements")

# We will define the exact additions into elements:
# 1.02: add 1 after index 3
# 1.04: add 1 after index 4
# 1.10: add 1 after index 3
# 2.02: add 1 after index 3
# 2.06: add 1 after index 3
# 2.08: add 1 after index 4
# 2.10: add 1 after index 2
# 3.05: add 1 after index 3
# 3.07: add 1 after index 3
# 3.09: add 1 after index 3
# 4.03: add 1 after index 2
# 4.07: add 1 after index 2
# 4.09: add 1 after index 2
# 5.02: add 1 after index 5
# 5.03: add 1 after index 2
# 5.05: add 1 after index 7

additions_vn = {
    "1.02": (4, "Các phương tiện truyền thông thời bấy giờ liên tục ca ngợi tinh thần tự do phóng khoáng, biến những chuyến đi nhờ xe thành biểu tượng lãng mạn của tuổi trẻ."),
    "1.04": (5, "Cô hiểu rất rõ những rủi ro tiềm ẩn trên những cung đường vắng và luôn duy trì sự cảnh giác cao độ trước những gã đàn ông xa lạ."),
    "1.10": (4, "Hắn thậm chí đã tính toán cẩn thận các khe thông khí nhỏ hẹp để nạn nhân không bị ngạt thở nhưng hoàn toàn mất khả năng định hướng."),
    "2.02": (4, "Mỗi hơi thở đều nặng trĩu bụi gỗ và cảm giác ngột ngạt như bị chôn sống từ từ trong một nấm mồ không tên."),
    "2.06": (4, "Trong trạng thái cô lập cực hạn ấy, những kích thích nhỏ nhất cũng có thể bị khuếch đại thành những cơn hoảng loạn dữ dội tột cùng."),
    "2.08": (5, "Bản hợp đồng được soạn thảo với những điều khoản pháp lý giả mạo tinh vi, đánh tráo khái niệm tội ác thành sự cam kết phục tùng tự nguyện."),
    "2.10": (3, "Nỗi sợ hãi mơ hồ về một thế lực vô hình luôn có sức tàn phá tâm lý lớn hơn gấp bội so với những chấn song sắt hữu hình."),
    "3.05": (4, "Người cha nhận thấy sự thay đổi bất thường ở con gái nhưng vì quá vui mừng trước ngày đoàn tụ nên đã không gặng hỏi sâu hơn."),
    "3.07": (4, "Khi ý niệm về sự bất lực đã ăn sâu vào tiềm thức, nạn nhân sẽ tự động từ chối mọi cơ hội tự cứu lấy chính mình."),
    "3.09": (4, "Sự chia ngăn hoàn hảo ấy cho phép hắn thản nhiên tham dự các buổi sinh hoạt cộng đồng mà không hề cảm thấy chút cắn rứt tội lỗi nào."),
    "4.03": (3, "Bản năng bảo vệ con cái của một người mẹ đã trở thành động lực mạnh mẽ nhất thôi thúc cô tìm kiếm sự thức tỉnh lương tâm."),
    "4.07": (3, "Đó là những bước chạy gấp gáp của một con người đang dồn hết chút tàn lực cuối cùng để giành lại quyền được sống như một con người."),
    "4.09": (3, "Tiến sĩ Hatcher đã chỉ ra rằng trạng thái phục tùng của nạn nhân thực chất là một chiến lược thích nghi sinh tồn thụ động được tôi luyện trong sợ hãi cực hạn."),
    "5.02": (6, "Cô kiên trì từng ngày để học lại cách tin tưởng thế giới bên ngoài và đón nhận tình yêu thương của những người xung quanh."),
    "5.03": (3, "Sự kiên cường phi thường ấy đã biến một nạn nhân bị giam cầm thành một biểu tượng bất diệt của sức mạnh phục hồi tinh thần con người."),
    "5.05": (8, "Đừng bao giờ đánh giá thấp những tín hiệu cảnh báo thầm kín mà cơ thể và tiềm thức gửi đến bạn trong những khoảnh khắc bất an."),
}

additions_en = {
    "1.02": (4, "Media outlets during that era constantly celebrated this freewheeling spirit, turning hitchhiking into a romanticized symbol of youthful adventure."),
    "1.04": (5, "She understood the latent hazards of deserted highways and remained intensely vigilant toward solitary unfamiliar men."),
    "1.10": (4, "He had even calculated narrow ventilation slots to prevent suffocation while ensuring absolute spatial disorientation."),
    "2.02": (4, "Every breath was heavy with plywood dust and the suffocating sensation of being buried alive in an unmarked grave."),
    "2.06": (4, "In that extreme sensory vacuum, the slightest ambiguous cue was magnified into overwhelming panic and existential dread."),
    "2.08": (5, "The document was drafted with quasi-legal terminology, deceptively reframing abduction and captivity into voluntary contractual servitude."),
    "2.10": (3, "The ambiguous dread of an omnipresent phantom syndicate exerted far greater coercive power than tangible iron bars."),
    "3.05": (4, "Her father perceived her uncharacteristic reserve, yet the sheer euphoria of family reunion prevented him from probing deeper."),
    "3.07": (4, "Once learned helplessness becomes deeply ingrained, victims subconsciously surrender all initiatives for self-rescue even when liberty beckons."),
    "3.09": (4, "Such seamless compartmentalization enabled him to socialize amiably in the community without experiencing a shred of moral guilt."),
    "4.03": (3, "A mother’s primal protective instinct over her daughters became the decisive catalyst prompting her moral awakening."),
    "4.07": (3, "Those were the urgent strides of a human being summoning every remnant of resolve to reclaim her stolen dignity and life."),
    "4.09": (3, "Dr. Hatcher demonstrated that her outward compliance was in fact a passive psychological adaptation strategy forged under extreme existential terror."),
    "5.02": (6, "Day after patient day, she painstakingly relearned how to trust the world and embrace genuine human compassion once more."),
    "5.03": (3, "That extraordinary resilience transformed a former captive into an enduring testament to the restorative potential of the human spirit."),
    "5.05": (8, "Never dismiss the subtle physiological warning signals that your subconscious communicates during moments of unease."),
}

additions_ja = {
    "1.02": (4, "当時のメディアは自由奔放な精神を称賛し続け、ヒッチハイクを若者の冒険のロマンチックな象徴へと仕立て上げていました。"),
    "1.04": (5, "彼女は人通りの少ない道路に潜む危険を熟知しており、見知らぬ単身の男性に対して常に強い警戒心を維持していました。"),
    "1.10": (4, "彼は犠牲者が窒息しないよう狭い通気口を緻密に設計しつつ、空間認識能力を完全に奪う構造に仕上げていました。"),
    "2.02": (4, "息を吸うたびに合板の粉塵と、名もなき墓標の下に生き埋めにされたかのような窒息感が重くのしかかりました。"),
    "2.06": (4, "その極限の感覚遮断状態においては、わずかな物音や気配さえも圧倒的なパニックと実存的恐怖へと増幅されました。"),
    "2.08": (5, "その文書は擬似的な法的用語で作成され、監禁と隷属をあたかも自発的な契約義務であるかのように巧妙に偽装していました。"),
    "2.10": (3, "偏在する影の組織への漠然とした恐怖は、目に見える鉄格子の牢獄よりもはるかに強力な心理的強制力を発揮しました。"),
    "3.05": (4, "父親は娘の不自然な変化に気づいていましたが、生きて再会できた喜びに圧倒され、深く問いただすことができませんでした。"),
    "3.07": (4, "学習性無力感が深層心理に定着すると、目の前に出口が開かれていても、自らを救い出す能動的な意欲そのものを放棄してしまいます。"),
    "3.09": (4, "その完璧な区画化により、彼は良心の呵責を一切感じることなく、地域社会で愛想よく交流することができたのです。"),
    "4.03": (3, "幼い娘たちを守らなければならないという母親の本能こそが、彼女の良心を覚醒させる最大の決定的契機となりました。"),
    "4.07": (3, "それは、奪われた人間の尊厳と命を取り戻すため、最後の気力を振り絞って踏み出した切迫した逃走の足取りでした。"),
    "4.09": (3, "ハッチャー博士は、被害者の従順な態度は極限の恐怖下で命をつなぐために培われた受動的適応戦略にほかならないと論証しました。"),
    "5.02": (6, "彼女は日々忍耐強く、外界を再び信頼し、周囲の人々の純粋な思いやりを受け入れる方法を学び直していきました。"),
    "5.03": (3, "その並外れた強靭さは、かつての囚われの被害者を、人間の精神が持つ回復力の不滅の象徴へと昇華させました。"),
    "5.05": (8, "不安を感じた瞬間に身体と潜在意識が発する微細な警告シグナルを、決して軽視してはなりません。"),
}

additions_ko = {
    "1.02": (4, "당시의 대중매체는 이러한 자유분방한 히피 정신을 끊임없이 찬양하며, 히치하이킹을 젊은 날의 낭만적인 모험의 상징으로 포장했습니다."),
    "1.04": (5, "그녀는 인적이 드문 고속도로에 도사린 잠재적 위험을 잘 알고 있었으며, 낯선 단독 남성 운전자들을 극도로 경계했습니다."),
    "1.10": (4, "그는 피해자가 질식하지 않도록 좁은 환기 구멍을 치밀하게 계산하면서도, 공간 지각 능력을 완벽히 마비시키도록 설계했습니다."),
    "2.02": (4, "숨을 들이쉴 때마다 합판 먼지와 함께 이름 없는 무덤 속에 서서히 생매장당하는 듯한 끔찍한 질식감이 엄습했습니다."),
    "2.06": (4, "그러한 극단적인 감각 차단 상태에서는 아주 미세한 자극조차도 걷잡을 수 없는 공황 발작과 실존적 공포로 증폭되었습니다."),
    "2.08": (5, "해당 문서는 교묘한 사이비 법률 용어로 작성되어, 납치와 불법 감금을 마치 자발적인 계약적 복종인 것처럼 둔갑시켰습니다."),
    "2.10": (3, "도처에 도사린 가상의 비밀 조직에 대한 막연한 공포는, 눈에 보이는 쇠창살 감옥보다 훨씬 더 강력한 심리적 구속력을 발휘했습니다."),
    "3.05": (4, "아버지는 딸의 부자연스러운 변화를 감지했으나, 살아서 돌아온 기적 같은 재회의 기쁨에 젖어 더 깊이 캐묻지 못했습니다."),
    "3.07": (4, "학습된 무기력이 무의식 깊이 뿌리내리면, 눈앞에 탈출의 기회가 열려 있어도 스스로를 구원하려는 능동적인 의지 자체를 포기하게 됩니다."),
    "3.09": (4, "그러한 완벽한 인지적 구획화 덕분에 그는 내면의 죄책감을 전혀 느끼지 않은 채, 지역 사회의 일상적인 교류에 태연히 참여할 수 있었습니다."),
    "4.03": (3, "어린 딸들을 지켜야 한다는 어머니로서의 원초적인 보호 본능이야말로, 그녀의 잠자던 양심을 일깨운 결정적인 계기가 되었습니다."),
    "4.07": (3, "그것은 빼앗긴 인간의 존엄과 삶을 되찾기 위해, 남은 마지막 모든 용기를 쥐어짜 내어 내딛은 절박한 탈출의 발걸음이었습니다."),
    "4.09": (3, "해처 박사는 피해자의 외견상 순종적인 태도가 실상은 극심한 생존 공포 속에서 목숨을 부지하기 위해 형성된 수동적 적응 기제임을 명확히 논증했습니다."),
    "5.02": (6, "그녀는 매일 인내심을 갖고 세상을 다시 신뢰하는 법을, 그리고 주위 사람들의 순수한 사랑을 가슴으로 받아들이는 법을 다시 배웠습니다."),
    "5.03": (3, "그러한 놀라운 회복탄력성은 끔찍한 속박의 피해자였던 그녀를, 인간 정신의 치유와 재건이 지닌 불멸의 상징으로 승화시켰습니다."),
    "5.05": (8, "불안감을 느끼는 순간 신체와 무의식이 보내오는 미세한 생존 경고 신호를 결코 과소평가해서는 안 됩니다."),
}

# -----------------------------------------------------------------------------
# 2. EXPAND VN SCRIPT JSON
# -----------------------------------------------------------------------------
new_data_vn = []
total_sent_vn = 0

for elem in data_vn:
    new_elem = dict(elem)
    eid = elem["id"]
    if elem.get("kind") == "LOI":
        sents = [s["text"] for s in elem["sentences"]]
        if eid in additions_vn:
            idx, text = additions_vn[eid]
            sents.insert(idx, text)
        
        # rebuild sentences
        new_elem["sentences"] = []
        for i, s_text in enumerate(sents, 1):
            new_elem["sentences"].append({
                "id": f"{eid}#{i}",
                "text": s_text,
                "words": len(s_text.split())
            })
        new_elem["text"] = " ".join(sents)
        total_sent_vn += len(sents)
    new_data_vn.append(new_elem)

print(f"Expanded VN: {total_sent_vn} sentences across {len(new_data_vn)} elements")

# Write new script_tap10.json
with open(ROOT / ".work" / "script_tap10.json", "w", encoding="utf-8") as f:
    json.dump(new_data_vn, f, ensure_ascii=False, indent=2)
print("Updated .work/script_tap10.json")

# -----------------------------------------------------------------------------
# 3. EXPAND EN SCRIPT JSON
# -----------------------------------------------------------------------------
with open(ROOT / ".work" / "script_tap10_EN.json", "r", encoding="utf-8") as f:
    data_en = json.load(f)

new_data_en = []
total_sent_en = 0

for elem in data_en:
    new_elem = dict(elem)
    eid = elem["id"]
    if elem.get("kind") == "LOI":
        sents = [s["text"] for s in elem["sentences"]]
        if eid in additions_en:
            idx, text = additions_en[eid]
            sents.insert(idx, text)
        
        new_elem["sentences"] = []
        for i, s_text in enumerate(sents, 1):
            new_elem["sentences"].append({
                "id": f"{eid}#{i}",
                "text": s_text,
                "words": len(s_text.split())
            })
        new_elem["text"] = " ".join(sents)
        total_sent_en += len(sents)
    new_data_en.append(new_elem)

print(f"Expanded EN: {total_sent_en} sentences across {len(new_data_en)} elements")

with open(ROOT / ".work" / "script_tap10_EN.json", "w", encoding="utf-8") as f:
    json.dump(new_data_en, f, ensure_ascii=False, indent=2)
print("Updated .work/script_tap10_EN.json")

# -----------------------------------------------------------------------------
# 4. REBUILD MARKDOWN SCRIPTS (VN, EN, JA, KO)
# -----------------------------------------------------------------------------
def build_markdown(lang, script_data, title, brief_desc, additions_map):
    # Read existing markdown file to preserve headers and directions
    md_lines = []
    
    if lang == "VN":
        src_path = ROOT / "01_KICH_BAN" / "Tap10" / "kichban_tap10_23102026.md"
    elif lang == "EN":
        src_path = ROOT / "01_KICH_BAN" / "Tap10_EN" / "kichban_tap10_EN.md"
    elif lang == "JA":
        src_path = ROOT / "01_KICH_BAN" / "Tap10_JA" / "kichban_tap10_JA.md"
    elif lang == "KO":
        src_path = ROOT / "01_KICH_BAN" / "Tap10_KO" / "kichban_tap10_KO.md"
    
    orig_text = src_path.read_text(encoding="utf-8")
    
    # Split into lines
    lines = orig_text.splitlines()
    
    # Find all element blocks and reconstruct
    # We can reconstruct by iterating over elements in new_data_vn
    out_lines = []
    
    # Header up to Hồi 1
    in_header = True
    act_headers = {
        1: "",
        2: "",
        3: "",
        4: "",
        5: ""
    }
    
    for l in lines:
        if l.startswith("## HỒI 1") or l.startswith("## ACT 1") or l.startswith("## 第1幕") or l.startswith("## 제1막"):
            in_header = False
            break
        out_lines.append(l)
    
    # Extract act header templates from orig_text
    act_matches = re.findall(r"(## (?:HỒI|ACT|第\d+幕|제\d+막).*?)(?=\n)", orig_text)
    for i, h in enumerate(act_matches, 1):
        act_headers[i] = h
    
    current_act = 0
    
    for elem in new_data_vn:
        eid = elem["id"]
        act = elem["act"]
        kind = elem["kind"]
        
        if act != current_act:
            current_act = act
            out_lines.append("")
            out_lines.append("---")
            out_lines.append("")
            out_lines.append(act_headers[current_act])
            out_lines.append("")
        
        if kind == "BGM":
            out_lines.append(f"**[BGM]:** {elem['desc']}")
            out_lines.append("")
        elif kind == "SFX":
            out_lines.append(f"**[SFX]:** {elem['desc']}")
            out_lines.append("")
        elif kind == "NGHI":
            out_lines.append(f"**[Nghỉ 1.5 giây – {elem['desc']}]**")
            out_lines.append("")
        elif kind == "LOI":
            role = elem["role"]
            dir_text = elem["direction"]
            
            role_header = ""
            if role == "H":
                role_header = f"**HOST** *({dir_text})*:"
            elif role == "D":
                role_header = f"**ĐIỀU TRA VIÊN** *({dir_text})*:" if lang == "VN" else (
                    f"**INVESTIGATOR** *({dir_text})*:" if lang == "EN" else (
                        f"**捜査官** *({dir_text})*:" if lang == "JA" else f"**수사관** *({dir_text})*:"
                    )
                )
            elif role == "C":
                role_header = f"**CHUYÊN GIA TÂM LÝ** *({dir_text})*:" if lang == "VN" else (
                    f"**PSYCHOLOGIST** *({dir_text})*:" if lang == "EN" else (
                        f"**犯罪心理学者** *({dir_text})*:" if lang == "JA" else f"**범죄심리학자** *({dir_text})*:"
                    )
                )
            elif role == "N":
                role_header = f"**NGƯỜI BÌNH THƯỜNG** *({dir_text})*:" if lang == "VN" else (
                    f"**EVERYDAY PERSON** *({dir_text})*:" if lang == "EN" else (
                        f"**証言者** *({dir_text})*:" if lang == "JA" else f"**일반인 증언자** *({dir_text})*:"
                    )
                )
            
            out_lines.append(role_header)
            
            # Now sentences for this language
            if lang == "VN":
                for s in elem["sentences"]:
                    out_lines.append(s["text"])
            else:
                # Get sentences from corresponding lang file or map
                # Let's read sentences from lang file
                pass
            out_lines.append("")
            
    return "\n".join(out_lines)

# Write a more direct generator for JA and KO by parsing existing sentences and inserting additions
def expand_markdown_file(src_path, dst_paths, additions_map, lang):
    content = src_path.read_text(encoding="utf-8")
    lines = content.splitlines()
    
    new_lines = []
    
    # We will identify each LOI turn by matching role lines, then track sentences
    # To be 100% precise, we know the exact LOI turn order and element ids:
    loi_ids = [e["id"] for e in data_vn if e.get("kind") == "LOI"]
    loi_idx = -1
    
    i = 0
    while i < len(lines):
        line = lines[i]
        
        # Check if line is a role header
        is_role = False
        if any(line.startswith(prefix) for prefix in [
            "**HOST**", "**ĐIỀU TRA VIÊN**", "**CHUYÊN GIA TÂM LÝ**", "**NGƯỜI BÌNH THƯỜNG**",
            "**INVESTIGATOR**", "**PSYCHOLOGIST**", "**EVERYDAY PERSON**",
            "**捜査官**", "**犯罪心理学者**", "**証言者**",
            "**수사관**", "**범죄심리학자**", "**일반인 증언자**"
        ]):
            is_role = True
            loi_idx += 1
            current_eid = loi_ids[loi_idx]
            new_lines.append(line)
            i += 1
            
            # Read sentences of this LOI turn
            sents = []
            while i < len(lines):
                s_line = lines[i].strip()
                if not s_line:
                    break
                sents.append(s_line)
                i += 1
            
            # Insert addition if present
            if current_eid in additions_map:
                ins_idx, ins_text = additions_map[current_eid]
                sents.insert(ins_idx, ins_text)
            
            for s in sents:
                new_lines.append(s)
            new_lines.append("")
            continue
        
        new_lines.append(line)
        i += 1
        
    result_text = "\n".join(new_lines).strip() + "\n"
    
    for dst in dst_paths:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(result_text, encoding="utf-8")
        print(f"Updated {dst} ({len(result_text)} chars)")

print("\n--- UPDATING ALL 4 MARKDOWN SCRIPT FILES ---")

# VN
expand_markdown_file(
    ROOT / "01_KICH_BAN" / "Tap10" / "kichban_tap10_23102026.md",
    [ROOT / "01_KICH_BAN" / "Tap10" / "kichban_tap10_23102026.md"],
    additions_vn,
    "VN"
)

# EN
expand_markdown_file(
    ROOT / "01_KICH_BAN" / "Tap10_EN" / "kichban_tap10_EN.md",
    [
        ROOT / "01_KICH_BAN" / "Tap10_EN" / "kichban_tap10_EN.md",
        ROOT / "01_KICH_BAN" / "Tap10" / "kichban_tap10_EN.md"
    ],
    additions_en,
    "EN"
)

# JA
expand_markdown_file(
    ROOT / "01_KICH_BAN" / "Tap10_JA" / "kichban_tap10_JA.md",
    [ROOT / "01_KICH_BAN" / "Tap10_JA" / "kichban_tap10_JA.md"],
    additions_ja,
    "JA"
)

# KO
expand_markdown_file(
    ROOT / "01_KICH_BAN" / "Tap10_KO" / "kichban_tap10_KO.md",
    [ROOT / "01_KICH_BAN" / "Tap10_KO" / "kichban_tap10_KO.md"],
    additions_ko,
    "KO"
)

print("\nALL 4 SCRIPTS EXPANDED TO 208 SENTENCES SUCCESSFULLY!")

