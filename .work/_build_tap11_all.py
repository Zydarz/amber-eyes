# -*- coding: utf-8 -*-
"""Tổng hợp và sinh 4 kịch bản đa ngôn ngữ cho Tập 11 (VN, EN, JA, KO)."""
import os, sys, io, re, json
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')

from _tap11_act1 import ACT1_ELEMENTS
from _tap11_act2 import ACT2_ELEMENTS
from _tap11_act3 import ACT3_ELEMENTS
from _tap11_act4 import ACT4_ELEMENTS
from _tap11_act5 import ACT5_ELEMENTS

ALL_ACTS = [
    (1, ACT1_ELEMENTS, {
        "vn": "HỒI 1: THE HOOK – VỎ BỌC HOÀN HẢO CỦA CẶP ĐÔI KEN & BARBIE (00:00 – 05:00)",
        "en": "ACT 1: THE HOOK — THE PERFECT FACADE OF KEN & BARBIE (00:00 – 05:00)",
        "ja": "第1幕：つかみ――『ケンとバービー』完璧な仮面の裏側 (00:00 – 05:00)",
        "ko": "막 1: 훅(Hook) – 켄과 바비 완벽한 가면의 이면 (00:00 – 05:00)"
    }),
    (2, ACT2_ELEMENTS, {
        "vn": "HỒI 2: HIỆN TRƯỜNG & VỰC THẲM LEO THANG – 4 NẤC THANG TỘI ÁC (05:00 – 10:00)",
        "en": "ACT 2: THE CRIME SCENE & THE ESCALATION ABYSS — 4 STAGES OF DEPRAVITY (05:00 – 10:00)",
        "ja": "第2幕：犯行現場と深まるエスカレーション――4段階の凶行の軌跡 (05:00 – 10:00)",
        "ko": "막 2: 현장 분석과 파멸의 에스컬레이션 – 범죄의 4단계 궤적 (05:00 – 10:00)"
    }),
    (3, ACT3_ELEMENTS, {
        "vn": "HỒI 3: GIẢI MÃ LIÊN MINH BỆNH HOẠN – ĐIÊN CUỒNG ĐÔI & TRUNG HÒA ĐẠO ĐỨC (10:00 – 15:30)",
        "en": "ACT 3: DISSECTING THE SYMBIOTIC ALLIANCE — FOLIE À DEUX & MORAL NEUTRALIZATION (10:00 – 15:30)",
        "ja": "第3幕：病的な共生の解剖――共有妄想（フォリー・ドゥ）と道徳の中和 (10:00 – 15:30)",
        "ko": "막 3: 병적 공생 관계의 해부 – 감응성 정신병과 도덕적 중화 (10:00 – 15:30)"
    }),
    (4, ACT4_ELEMENTS, {
        "vn": "HỒI 4: THỎA THUẬN VỚI QUỶ DỮ & SỰ SỤP ĐỔ CỦA MẶT NẠ NẠN NHÂN (15:30 – 21:00)",
        "en": "ACT 4: THE DEAL WITH THE DEVIL & THE COLLAPSE OF THE VICTIM MASK (15:30 – 21:00)",
        "ja": "第4幕：悪魔との取引と被害者面の崩壊 (15:30 – 21:00)",
        "ko": "막 4: 악마와의 거래와 산산조각 난 피해자 가면 (15:30 – 21:00)"
    }),
    (5, ACT5_ELEMENTS, {
        "vn": "HỒI 5: PHÁN QUYẾT, DI CHỨNG TƯ PHÁP & BÀI HỌC CẢNH BÁO ĐỎ (21:00 – 26:30)",
        "en": "ACT 5: VERDICT, INSTITUTIONAL RECKONING & SURVIVAL RED FLAGS (21:00 – 26:30)",
        "ja": "第5幕：判決、制度の刷新と生存のための4つの赤い警告 (21:00 – 26:30)",
        "ko": "막 5: 사법 판결, 제도의 쇄신과 생존의 적신호 (21:00 – 26:30)"
    })
]

ROLE_MAP = {
    "VN": {
        "HOST": "**HOST**",
        "ĐIỀU TRA VIÊN": "**ĐIỀU TRA VIÊN**",
        "CHUYÊN GIA TÂM LÝ": "**CHUYÊN GIA TÂM LÝ**",
        "NGƯỜI BÌNH THƯỜNG": "**NGƯỜI BÌNH THƯỜNG**"
    },
    "EN": {
        "HOST": "**HOST**",
        "ĐIỀU TRA VIÊN": "**INVESTIGATOR**",
        "CHUYÊN GIA TÂM LÝ": "**PSYCHOLOGIST**",
        "NGƯỜI BÌNH THƯỜNG": "**ORDINARY PERSON**"
    },
    "JA": {
        "HOST": "**ホスト**",
        "ĐIỀU TRA VIÊN": "**捜査官**",
        "CHUYÊN GIA TÂM LÝ": "**心理学者**",
        "NGƯỜI BÌNH THƯỜNG": "**一般人**"
    },
    "KO": {
        "HOST": "**호스트**",
        "ĐIỀU TRA VIÊN": "**수사관**",
        "CHUYÊN GIA TÂM LÝ": "**심리학자**",
        "NGƯỜI BÌNH THƯỜNG": "**일반인**"
    }
}

HEADER_VN = """# KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM
**Chủ đề:** Hệ sinh thái 10 chỉ dấu tâm lý & Quy luật leo thang hành vi — Hồ sơ Paul Bernardo & Karla Homolka ('Ken và Barbie' và 'Thỏa thuận với Quỷ dữ').
**Phiên bản:** Chuẩn A2 — Bản tái cấu trúc toàn diện theo Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c) và Tiêu chuẩn an toàn YouTube V9 (ngày 07/11/2026).

---

## THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN (PRODUCTION BRIEF)

| Hạng mục | Thiết lập chuẩn cho tập Audio (Host-Driven Documentary) |
| :--- | :--- |
| **Tên tập (Episode Title)** | Tập 11: Cặp Đôi Ken & Barbie — Hội Chứng Điên Cuồng Đôi & Thỏa Thuận Với Quỷ Dữ (Hồ Sơ Paul Bernardo & Karla Homolka) |
| **Định dạng (Format)** | Podcast Tài liệu Điều tra (Narrator-led Documentary) – **Host** nắm giữ mạch truyện chính, kết nối tư liệu lịch sử, phân tích tâm lý học xã hội chuyên sâu, luân chuyển nhịp hài hòa giữa Điều tra viên, Chuyên gia tâm lý và Nhân chứng. |
| **Tổng thời lượng dự kiến** | 25 – 28 phút (5 hồi nội dung + các khoảng lặng âm thanh kịch tính) |
| **Nhạc nền (BGM) gợi ý** | Dark Ambient ngột ngạt, Tiếng cello giằng xé, Tiếng đàn Dương cầm tối giản (Minimalist Piano) kết hợp nhịp Drone điện tử rùng rợn. Âm lượng: -26dB dưới giọng đọc, nâng lên -14dB ở các điểm chuyển cảnh. |
| **Cơ chế phân bổ giọng đọc** | - **Host (~48% thời lượng):** Giọng nam trầm ấm, sâu lắng, dẫn dắt câu chuyện với góc nhìn nhân văn, triết học và sự cảnh báo trước những chiếc mặt nạ độc hại.<br>- **Điều tra viên (~26%):** Giọng nam chững chạc, sắc bén, tái hiện góc nhìn nghiệp vụ thực địa của Cảnh sát Hoàng gia Canada (RCMP) và Cơ quan Cảnh sát Khu vực Niagara/Toronto.<br>- **Chuyên gia tâm lý (~22%):** Giọng điềm đạm, học thuật, bóc tách hiện tượng Folie à Deux, cơ chế đóng vai nạn nhân và sự thao túng lòng trắc ẩn.<br>- **Người bình thường (~4%):** N1 (Người hàng xóm tại Port Dalhousie - Hồi 1) giọng nữ ngỡ ngàng trước vẻ ngoài hào nhoáng của cặp đôi; N2 (Điều tra viên / Công tố viên nhận án - Hồi 4) giọng nam uất nghẹn, cay đắng khi sự thật trong cuộn băng bị phơi bày. |

---
"""

HEADER_EN = """# CRIMINAL PSYCHOLOGY AUDIO / PODCAST SCRIPT — ENGLISH EDITION
**Topic:** The 10 Psychological Markers & Behavioral Escalation — The Case of Paul Bernardo & Karla Homolka ("Ken & Barbie" and the "Deal with the Devil").
**Translated from:** `01_KICH_BAN/Tap11/kichban_tap11_23102026.md`. One English sentence for every Vietnamese sentence, same structure, same IDs.
**Fact and legal review:** Based on public trial reporting, Ontario Court transcripts, and verified judicial archives; analysis of real people is framed within behavioral science frameworks.

---

## PRODUCTION BRIEF

| Item | Standard setting (host-driven documentary) |
| :--- | :--- |
| **Episode title** | Episode 11: The Ken & Barbie Killers — Folie à Deux & The Deal with the Devil (Paul Bernardo & Karla Homolka File) |
| **Format** | Narrator-led investigative documentary — the **Host** carries the core narrative, pacing emotional beats and introducing each expert perspective (Investigator, Psychologist, Ordinary person) at pivotal dramatic moments. |
| **Duration** | 25 – 28 minutes (5 acts + dramatic sound pauses) |
| **BGM Setting** | Dark Ambient, brooding cello, minimalist piano, electronic sub-bass drone. Music ducked to -26dB under speech, rising to -14dB during scene transitions. |
| **Voices** | Host (narration, social reflection) · Investigator (forensic methodology, MO vs Signature) · Psychologist (Folie à Deux, manipulative victimhood) · Ordinary person (N1: shocked neighbor; N2: remorseful prosecutor). |

---
"""

HEADER_JA = """# 犯罪心理学オーディオ／ポッドキャスト台本 — 日本語版
**テーマ：** 10の心理的指標と行動エスカレーションの法則――Paul Bernardo & Karla Homolka事件（『ケンとバービー』および『悪魔との取引』）
**原文:** `01_KICH_BAN/TAP11/kichban_tap11_23102026.md`。ベトナム語版と完全1:1対応（同一構造・同一ID・同一文数）。
**事実・法務チェック:** 公開された裁判記録、オンタリオ州警察の捜査資料、および公的学術文献に基づく客観的記述。
**バージョン：** 基準A2――10の心理・行動生態系（A2c）およびYouTube V9安全基準に基づく全面再構築版（2026年11月7日）。

---

## 制作仕様とナレーション構成（PRODUCTION BRIEF）

| 項目 | オーディオ番組の標準設定（ホスト主導のドキュメンタリー） |
| :--- | :--- |
| **エピソード名** | 第11話：ケンとバービー――共有妄想（フォリー・ドゥ）と悪魔との取引（Paul Bernardo & Karla Homolka事件簿） |
| **形式** | 調査ドキュメンタリー型ポッドキャスト（ナレーター主導型ドキュメンタリー）――**ホスト**が物語の背骨を担い、感情の流れを整え、物語の鍵となる緊張の局面ごとに専門家の視点（捜査官、心理学者、一般人）を招く。 |
| **想定総時間** | 25 – 28分（5つの本編章＋音声による場面転換） |
| **BGM設定** | Dark Ambient, 重厚なチェロ, ミニマルピアノ, サブベースドローン。ナレーション下では-26dB、場面転換では-14dB。 |
| **キャスト構成** | - **ホスト（約48%）：** 温かく低い声、物語の主軸と人間的洞察<br>- **捜査官（約26%）：** 冷徹で事実重視の声、現場検証と手口対署名<br>- **心理学者（約22%）：** 学術的で深い声、共有妄想（フォリー・ドゥ）と被害者面の病理解剖<br>- **一般人（約4%）：** N1（第1幕：愕然とする近隣住民）、N2（第4幕：苦渋に満ちた検察官） |

---
"""

HEADER_KO = """# 범죄심리 오디오 / 팟캐스트 스크립트 — 한국어판
**주제:** 심리 지표 10대 생태계 & 행동 에스컬레이션의 법칙 — Paul Bernardo & Karla Homolka 사건 (‘켄과 바비’ 및 ‘악마와의 거래’)
**원본:** `01_KICH_BAN/Tap11/kichban_tap11_23102026.md` 기반. 베트남어 원문과 1:1 완벽 일치 (동일 구조, 동일 ID, 동일 문장 수).
**사실 및 법률 검토:** 공개된 온타리오 법원 공판 기록, 경찰 수사 보고서 및 공인된 행동과학 분석 자료를 바탕으로 구성.
**버전:** 기준 A2 — 심리 지표 10대 생태계(A2c) 및 유튜브 V9 안전 기준에 맞춘 전면 재구성본(2026년 11월 7일).

---

## 제작 브리프(PRODUCTION BRIEF)

| 항목 | 기준 설정(내레이터 주도 다큐멘터리) |
| :--- | :--- |
| **에피소드 제목** | 11화: 켄과 바비 커플 — 감응성 정신병(폴리 아 되)과 악마와의 거래 (Paul Bernardo & Karla Homolka 사건 파일) |
| **형식** | 다큐멘터리 팟캐스트(내레이터 주도) – **호스트**가 이야기의 중심축을 잡고, 감정적 호흡을 조절하며 각 전문 관점(수사관, 심리학자, 일반인)을 가장 극적인 전환점에 불러들인다. |
| **예상 길이** | 25 – 28분 (5개 파트 + 전환 음악 및 침묵) |
| **배경음악(BGM) 설정** | 다크 앰비언트, 처절한 첼로, 미니멀 피아노, 서브베이스 드론. 내레이션 음성 아래 -26dB, 장면 전환부 -14dB. |
| **음성 배분 방식** | - **호스트(약 48%):** 낮고 따뜻하며 사색적인 목소리, 사건의 거시적 맥락과 인간적 성찰<br>- **수사관(약 26%):** 냉정하고 명확한 목소리, 수사 기록 및 범행 수법 대 시그니처 분석<br>- **심리학자(약 22%):** 차분하고 학문적인 목소리, 폴리 아 되와 피해자 코스프레의 심리 부검<br>- **일반인(약 4%):** N1(1막: 경악한 이웃 주민), N2(4막: 회한에 찬 검찰 수사관) |

---
"""

def generate_markdown(lang):
    lines = []
    if lang == "VN":
        lines.append(HEADER_VN.strip())
    elif lang == "EN":
        lines.append(HEADER_EN.strip())
    elif lang == "JA":
        lines.append(HEADER_JA.strip())
    elif lang == "KO":
        lines.append(HEADER_KO.strip())

    for act_num, elements, titles in ALL_ACTS:
        lines.append("")
        lines.append(f"## {titles[lang.lower()]}")
        lines.append("")
        
        for el in elements:
            kind = el["kind"]
            if kind == "BGM":
                desc = el[f"desc_{lang.lower()}"]
                lines.append(f"**[BGM]:** *{desc}*")
                lines.append("")
            elif kind == "SFX":
                desc = el[f"desc_{lang.lower()}"]
                lines.append(f"**[SFX]:** *{desc}*")
                lines.append("")
            elif kind == "NGHI":
                sec = el["sec"]
                if lang == "VN":
                    desc = f" – {el['desc_vn']}" if el.get("desc_vn") else ""
                    lines.append(f"**[Nghỉ {sec} giây{desc}]**")
                elif lang == "EN":
                    lines.append(f"**[Pause {sec} seconds]**")
                elif lang == "JA":
                    lines.append(f"**[休止 {sec}秒]**")
                elif lang == "KO":
                    lines.append(f"**[정지 {sec}초]**")
                lines.append("")
            elif kind == "LOI":
                role_key = el["role"]
                role_hdr = ROLE_MAP[lang][role_key]
                direction = el.get(f"direction_{lang.lower()}", "")
                if direction:
                    lines.append(f"{role_hdr} *({direction})*:")
                else:
                    lines.append(f"{role_hdr}:")
                
                sents = el[f"sents_{lang.lower()}"]
                for s in sents:
                    lines.append(s)
                lines.append("")
                
    return "\n".join(lines).strip() + "\n"

print("Generating 4 scripts...")
vn_md = generate_markdown("VN")
en_md = generate_markdown("EN")
ja_md = generate_markdown("JA")
ko_md = generate_markdown("KO")

out_files = [
    ("VN", "01_KICH_BAN/Tap11/kichban_tap11_23102026.md", vn_md),
    ("EN_sub", "01_KICH_BAN/Tap11/kichban_tap11_EN.md", en_md),
    ("EN", "01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md", en_md),
    ("JA", "01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md", ja_md),
    ("KO", "01_KICH_BAN/Tap11_KO/kichban_tap11_KO.md", ko_md),
]

for label, path, content in out_files:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Written: {path} ({len(content)} chars)")

print("\n>>> All 4 script files generated successfully! <<<")
