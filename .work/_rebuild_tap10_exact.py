#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rebuild Episode 10 scripts across all 4 languages (VN, EN, JA, KO) to 208 sentences.
Uses PK.parse_file on the clean backups to ensure 100% element and sentence parity.
"""

import sys
import json
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
sys.path.insert(0, ".work")
import parse_kichban as PK

ROOT = Path(r"D:\TEST\Gax\amber-eyes")

# 16 additions per language (key = element_id, value = (insert_index, sentence_text))
additions_vn = {
    "1.02": (4, "Các phương tiện truyền thông thời bấy giờ liên tục ca ngợi tinh thần tự do phóng khoáng, biến những chuyến đi nhờ xe thành biểu tượng lãng mạn của tuổi trẻ."),
    "1.04": (5, "Cô hiểu rất rõ những rủi ro tiềm ẩn trên những cung đường vắng và luôn duy trì sự cảnh giác cao độ trước những gã đàn ông xa lạ."),
    "1.10": (4, "Hắn thậm chí đã tính toán cẩn thận các khe thông khí nhỏ hẹp để nạn nhân không bị thiếu dưỡng khí nhưng hoàn toàn mất khả năng định hướng."),
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
    "1.10": (4, "He had even calculated narrow ventilation slots to maintain minimal airflow while ensuring absolute spatial disorientation."),
    "2.02": (4, "Every breath was heavy with plywood dust and the suffocating sensation of being buried alive in an unmarked grave."),
    "2.06": (4, "In that extreme sensory vacuum, the slightest ambiguous cue was magnified into overwhelming panic and existential dread."),
    "2.08": (5, "The document was drafted with quasi-legal terminology, deceptively reframing abduction and captivity into voluntary contractual servitude."),
    "2.10": (3, "The ambiguous dread of an omnipresent phantom syndicate exerted far greater coercive power than tangible iron bars."),
    "3.05": (4, "Her father perceived her uncharacteristic reserve, yet the sheer euphoria of family reunion prevented him from probing deeper."),
    "3.07": (4, "Once learned helplessness becomes deeply ingrained, victims subconsciously surrender all initiatives for self-rescue even when liberty beckons."),
    "3.09": (4, "Such seamless compartmentalization enabled him to socialize amiably in the community without experiencing a shred of moral guilt."),
    "4.03": (3, "A mother’s primal protective instinct over her daughters became the decisive catalyst prompting her moral awakening."),
    "4.07": (3, "Those were the urgent strides of a human being summoning every remnant of resolve to reclaim her stolen dignity and life."),
    "4.09": (3, "Doctor Hatcher demonstrated that her outward compliance was in fact a passive psychological adaptation strategy forged under extreme existential terror."),
    "5.02": (6, "Day after patient day, she painstakingly relearned how to trust the world and embrace genuine human compassion once more."),
    "5.03": (3, "That extraordinary resilience transformed a former captive into an enduring testament to the restorative potential of the human spirit."),
    "5.05": (8, "Never dismiss the subtle physiological warning signals that your subconscious communicates during moments of unease."),
}

additions_ja = {
    "1.02": (4, "当時のメディアは自由奔放な精神を称賛し続け、ヒッチハイクを若者の冒険のロマンチックな象徴へと仕立て上げていました。"),
    "1.04": (5, "彼女は人通りの少ない道路に潜む危険を熟知しており、見知らぬ単身の男性に対して常に強い警戒心を維持していました。"),
    "1.10": (4, "彼は犠牲者の酸欠を防ぐよう狭い通気口を緻密に設計しつつ、空間認識能力を完全に奪う構造に仕上げていました。"),
    "2.02": (4, "息を吸うたびに合板の粉塵と、名もなき墓標の下に生き埋めにされたかのような重苦しい圧迫感が重くのしかかりました。"),
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
    "1.10": (4, "그는 피해자가 최소한의 호흡을 유지하도록 좁은 환기 구멍을 치밀하게 계산하면서도, 공간 지각 능력을 완벽히 마비시키도록 설계했습니다."),
    "2.02": (4, "숨을 들이쉴 때마다 합판 먼지와 함께 이름 없는 무덤 속에 서서히 생매장당하는 듯한 끔찍한 압박감이 엄습했습니다."),
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

def rebuild_script(lang, backup_path, dst_paths, additions):
    parsed = PK.parse_file(backup_path)
    raw_backup = backup_path.read_text(encoding="utf-8")
    
    header_lines = []
    for line in raw_backup.splitlines():
        if re.match(r"^##\s+(?:HỒI|ACT|第\d+幕|제\d+막|막\s*\d+)", line):
            break
        header_lines.append(line)
    
    act_titles = {}
    for m in re.finditer(r"^(##\s*(?:HỒI|ACT|第\d+幕|제\d+막|막)\s*(\d+)[^\n]*)", raw_backup, re.MULTILINE):
        act_num = int(m.group(2))
        act_titles[act_num] = m.group(1)
        
    out_lines = list(header_lines)
    if out_lines and out_lines[-1] != "":
        out_lines.append("")
        
    current_act = 0
    
    for elem in parsed:
        act = elem["act"]
        eid = elem["id"]
        kind = elem["kind"]
        
        if act != current_act:
            current_act = act
            if out_lines and out_lines[-1] != "---":
                out_lines.append("---")
                out_lines.append("")
            out_lines.append(act_titles.get(current_act, f"## HỒI {current_act}"))
            out_lines.append("")
            
        if kind == "BGM":
            out_lines.append(f"**[BGM]:** {elem['desc']}")
            out_lines.append("")
        elif kind == "SFX":
            out_lines.append(f"**[SFX]:** {elem['desc']}")
            out_lines.append("")
        elif kind == "NGHI":
            if lang == "VN":
                out_lines.append(f"**[Nghỉ 1.5 giây – {elem['desc']}]**")
            elif lang == "EN":
                out_lines.append(f"**[Pause 1.5 seconds – {elem['desc']}]**")
            elif lang == "JA":
                out_lines.append(f"**[休止 1.5秒 – {elem['desc']}]**")
            elif lang == "KO":
                out_lines.append(f"**[정지 1.5초 – {elem['desc']}]**")
            out_lines.append("")
        elif kind == "LOI":
            role = elem["role"]
            dir_text = elem["direction"]
            
            # Exact role names according to parse_kichban.ROLES
            if lang == "VN":
                role_names = {"H": "HOST", "D": "ĐIỀU TRA VIÊN", "C": "CHUYÊN GIA TÂM LÝ", "N": "NGƯỜI BÌNH THƯỜNG"}
            elif lang == "EN":
                role_names = {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST", "N": "ORDINARY PERSON"}
            elif lang == "JA":
                role_names = {"H": "ホスト", "D": "捜査官", "C": "心理学者", "N": "一般人"}
            elif lang == "KO":
                role_names = {"H": "호스트", "D": "수사관", "C": "심리학자", "N": "일반인"}
            
            rname = role_names.get(role, "HOST")
            out_lines.append(f"**{rname}** *({dir_text})*:")
            
            # Sentences
            sents = [s["text"] for s in elem["sentences"]]
            if eid in additions:
                ins_idx, ins_txt = additions[eid]
                sents.insert(ins_idx, ins_txt)
                
            for s in sents:
                out_lines.append(s)
            out_lines.append("")
            
    content = "\n".join(out_lines).strip() + "\n"
    for dst in dst_paths:
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_text(content, encoding="utf-8")
        print(f"Rebuilt {lang} -> {dst.relative_to(ROOT)} ({len(content)} chars)")


# 1. REBUILD VN
rebuild_script(
    "VN",
    ROOT / ".work" / "_cu" / "kichban_tap10_23102026_truoc_200cau_20261107.md",
    [ROOT / "01_KICH_BAN" / "Tap10" / "kichban_tap10_23102026.md"],
    additions_vn
)

# 2. REBUILD EN
rebuild_script(
    "EN",
    ROOT / ".work" / "_cu" / "kichban_tap10_EN_truoc_200cau_20261107.md",
    [
        ROOT / "01_KICH_BAN" / "Tap10_EN" / "kichban_tap10_EN.md",
        ROOT / "01_KICH_BAN" / "Tap10" / "kichban_tap10_EN.md"
    ],
    additions_en
)

# 3. REBUILD JA
rebuild_script(
    "JA",
    ROOT / ".work" / "_cu" / "kichban_tap10_JA_truoc_200cau_20261107.md",
    [ROOT / "01_KICH_BAN" / "Tap10_JA" / "kichban_tap10_JA.md"],
    additions_ja
)

# 4. REBUILD KO
rebuild_script(
    "KO",
    ROOT / ".work" / "_cu" / "kichban_tap10_KO_truoc_200cau_20261107.md",
    [ROOT / "01_KICH_BAN" / "Tap10_KO" / "kichban_tap10_KO.md"],
    additions_ko
)

# 5. REBUILD JSON
parsed_vn = PK.parse_file(ROOT / "01_KICH_BAN" / "Tap10" / "kichban_tap10_23102026.md")
with open(ROOT / ".work" / "script_tap10.json", "w", encoding="utf-8") as f:
    json.dump(parsed_vn, f, ensure_ascii=False, indent=2)
print("Updated .work/script_tap10.json")

parsed_en = PK.parse_file(ROOT / "01_KICH_BAN" / "Tap10_EN" / "kichban_tap10_EN.md")
with open(ROOT / ".work" / "script_tap10_EN.json", "w", encoding="utf-8") as f:
    json.dump(parsed_en, f, ensure_ascii=False, indent=2)
print("Updated .work/script_tap10_EN.json")

print("\n--- REBUILD COMPLETED SUCCESSFULLY ---")
