# -*- coding: utf-8 -*-
"""Build and verify all 4 language editions for Episode 22 (212 sentences)."""

import os
import sys
import json
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))

import parse_kichban as PK
from tap22_act1 import ACT1_VN, ACT1_EN, ACT1_JA, ACT1_KO
from tap22_act2 import ACT2_VN, ACT2_EN, ACT2_JA, ACT2_KO
from tap22_act3 import ACT3_VN, ACT3_EN, ACT3_JA, ACT3_KO
from tap22_act4 import ACT4_VN, ACT4_EN, ACT4_JA, ACT4_KO
from tap22_act5 import ACT5_VN, ACT5_EN, ACT5_JA, ACT5_KO

ALL_ACTS = {
    "VN": [ACT1_VN, ACT2_VN, ACT3_VN, ACT4_VN, ACT5_VN],
    "EN": [ACT1_EN, ACT2_EN, ACT3_EN, ACT4_EN, ACT5_EN],
    "JA": [ACT1_JA, ACT2_JA, ACT3_JA, ACT4_JA, ACT5_JA],
    "KO": [ACT1_KO, ACT2_KO, ACT3_KO, ACT4_KO, ACT5_KO],
}

ACT_TITLES = {
    "VN": [
        "HỒI 1: MÀN KỊCH HIỆN TRƯỜNG GIẢ & NƯỚC MẮT NGƯỜI VỢ MỚI CƯỚI",
        "HỒI 2: VÁN BÀI LẬT NGỬA & NGHỆ THUẬT THAO TÚNG TRƠ TRẼN (GASLIGHTING)",
        "HỒI 3: GIẢI MÃ TÂM LÝ: SỰ THAO TÚNG TRƠ TRẼN & NHÂN CÁCH ÁI KỶ ÁC TÍNH",
        "HỒI 4: CUỘC CHIẾN PHÁP LÝ 8 NĂM & BẢN ÁN 16 NĂM TÙ GIAM",
        "HỒI 5: BÀI HỌC CẢNH TỈNH & 4 CẢNH BÁO ĐỎ NHẬN DIỆN KẺ THAO TÚNG TRỤC LỢI",
    ],
    "EN": [
        "ACT 1: THE STAGED CRIME SCENE & THE NEWLYWED'S THEATRICAL TEARS",
        "ACT 2: CARDS ON THE TABLE & EXTREME GASLIGHTING PSYCHOLOGY",
        "ACT 3: PSYCHOLOGICAL DISSECTION: MALIGNANT NARCISSISM & PREDATORY EXPLOITATION",
        "ACT 4: THE 8-YEAR LEGAL WAR & THE 16-YEAR PRISON SENTENCE",
        "ACT 5: AWAKENING LESSONS & 4 RED FLAGS AGAINST ROMANTIC PREDATION",
    ],
    "JA": [
        "第1幕: 偽装殺人現場と新妻の劇的な号泣劇",
        "第2幕: 白日の下に晒された真相と極限のガスライティング",
        "第3幕: 深層心理の解剖：悪性自己愛と経済的捕食の力学",
        "第4幕: 8年に及ぶ過酷な法廷闘争と禁錮16年の断罪",
        "第5幕: 覚醒の教訓と捕食的搾取を見抜く4つの危険兆候",
    ],
    "KO": [
        "막 1: 모의 살인 현장 연출과 새댁의 극적인 오열",
        "막 2: 백일하에 드러난 진실과 극한의 가스라이팅",
        "막 3: 범죄 심리 해부: 악성 자기애와 약탈적 착취의 메커니즘",
        "막 4: 8년에 걸친 법정 전쟁과 징역 16년의 준엄한 단죄",
        "막 5: 각성의 교훈과 약탈적 심리 조작을 막는 4대 위험 징후",
    ],
}

HEADERS = {
    "VN": """# KỊCH BẢN CHI TIẾT TẬP 22: HỒ SƠ DALIA DIPPOLITO — NƯỚC MẮT CÁ SẤU CỦA KẺ THUÊ SÁT THỦ GIẾT CHỒNG & MÀN KỊCH TRƯỚC MÁY QUAY

* **Đề tài:** Vụ án dàn cảnh thuê sát thủ tại Boynton Beach (Florida, 2009)
* **Chủ đề tâm lý:** Sự thao túng trơ trẽn (*Extreme Gaslighting*), Rối loạn nhân cách chống đối xã hội kết hợp Ái kỷ ác tính (*Malignant Narcissism / ASPD*), Hiện tượng Nước mắt cá sấu & Nỗi đau mang tính trình diễn (*Crocodile Tears / Performative Grief*), Săn mồi tài chính hôn nhân (*Predatory Marriage & Financial Manipulation*), Nghịch lý chia ngăn nhận thức (*Compartmentalization*), Kỹ thuật trung hòa đạo đức (*Techniques of Neutralization*)
* **Thời lượng dự kiến:** 24 – 27 phút
* **Định dạng:** Chuẩn A2 — Bản nâng cấp kịch bản quy mô lớn (212 câu thoại) theo Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c) và Luật K10 (07/11/2026)
* **Tiêu chuẩn An toàn YouTube (Rule V9):** 100% YouTube Safe, không mô tả trực diện phương thức bạo lực ghê rợn; tập trung 100% vào phân tích tâm lý học tội phạm, vi biểu cảm, chiến thuật hỏi cung, nghiệp vụ giăng bẫy (Sting Operation) và bài học phòng ngừa các mối quan hệ độc hại trục lợi.

---

## BẢNG PHÂN VAI VÀ CẤU TRÚC GIỌNG ĐỌC

| Ký hiệu | Vai trò | Tên nhân vật thể hiện | Đặc điểm giọng đọc | Số câu |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **Dẫn chuyện (Host)** | Amber Eyes Voice | Trầm ấm, lôi cuốn, sắc sảo, dẫn dắt thấu đáo | **122** |
| **D** | **Điều tra viên** | Điều tra viên (nhân vật minh hoạ) | Nam trung niên, dày dạn kinh nghiệm, điềm tĩnh, đanh thép | **37** |
| **C** | **Chuyên gia Tâm lý** | Chuyên gia Tâm lý học Pháp y & Hành vi | Điềm đạm, khách quan, giàu hàm lượng khoa học hành vi | **36** |
| **N1** | **Người trong cuộc 1** | Người hàng xóm Boynton Beach (Hồi 1) | Nữ thanh niên, bàng hoàng, chân thực, rùng mình | **8** |
| **N2** | **Người trong cuộc 2** | Bồi thẩm viên Tòa án Palm Beach (Hồi 4) | Nữ trung niên, nghiêm nghị, đanh thép, công minh | **9** |
| **TỔNG** | **Toàn bộ kịch bản** | **5 Hồi chuẩn A2** | **Cân bằng hoàn hảo theo Golden Benchmark (>200 câu)** | **212** |

---
""",
    "EN": """# DETAILED SCRIPT EPISODE 22: DALIA DIPPOLITO DOSSIER — THE CROCODILE TEARS OF A CONTRACT HIT MASTERMIND & THE ON-CAMERA CHARADE

* **Subject:** The Staged Hitman Sting Operation in Boynton Beach (Florida, 2009)
* **Psychological Themes:** Extreme Gaslighting, Malignant Narcissism & Antisocial Personality Disorder (ASPD), Crocodile Tears & Performative Grief, Predatory Marriage & Financial Exploitation, Cognitive Compartmentalization, Techniques of Moral Neutralization
* **Estimated Running Time:** 24 – 27 minutes
* **Format:** Standard A2 — High-Scale Script (212 Spoken Sentences) based on the 10 Psychological & Behavioral Dimensions (A2c) and Rule K10 (07/11/2026)
* **YouTube Safety Standard (Rule V9):** 100% YouTube Safe, zero graphic depictions of violence or bodily harm; 100% focused on forensic behavioral science, undercover sting tradecraft, micro-expressions, and survival red flags against predatory relationships.

---

## CAST AND VOCAL ARCHITECTURE

| Symbol | Role | Persona / Character | Vocal Attributes | Sentences |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **Host** | Amber Eyes Voice | Warm, resonant, compelling, penetrating narrative arc | **122** |
| **D** | **Investigator** | Homicide Detective (Representative Persona) | Seasoned, steely, objective, forensic precision | **37** |
| **C** | **Psychologist** | Forensic Behavioral Scientist | Scholarly, clinical, insightful behavioral analysis | **36** |
| **N1** | **Ordinary Person 1** | Boynton Beach Neighbor (Act 1) | Young female, shaken, authentic, visceral shock | **8** |
| **N2** | **Ordinary Person 2** | Palm Beach County Juror (Act 4) | Mature female, firm, resolute, and dignified | **9** |
| **TOTAL** | **Full Episode** | **5 Acts Standard A2** | **1:1 Multilingual Parity Benchmark (>200 Sentences)** | **212** |

---
""",
    "JA": """# 詳細台本 第22話：ダリア・ディッポリト事件 — 夫殺害を企てた女の偽りの涙とカメラの前での大茶番

* **事件記録:** フロリダ州ボイントンビーチ 偽装殺人おとり捜査事件（2009年）
* **心理学的主題:** 極限の現実操作（Extreme Gaslighting）、悪性自己愛（Malignant Narcissism）および反社会性パーソナリティ障害（ASPD）、演技的悲嘆と偽りの涙（Crocodile Tears / Performative Grief）、捕食的偽装結婚および経済的搾取、認知的区画化（Compartmentalization）、道徳的中和技術（Techniques of Neutralization）
* **予想再生時間:** 24 – 27分
* **フォーマット:** 標準A2規格 — 10の心理・行動分析指標（A2c）およびK10規則に準拠した大規模脚本（全212文・2026年11月7日改訂版）
* **YouTube安全基準 (Rule V9):** 100% YouTube Safe、直接的・過激な暴力描写を完全に排除。行動科学、法医学的心理分析、おとり捜査戦術および実践的防犯教育に特化。

---

## 配役および声の構成表

| 記号 | 役割 | 登場人物 | 声の特質 | 文数 |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **ホスト (Host)** | Amber Eyes Voice | 落ち着き、深み、説得力に富んだ物語の語り手 | **122** |
| **D** | **捜査官** | 殺人課刑事（モデル人物） | 熟練、冷徹、客観的、科学捜査の確証 | **37** |
| **C** | **心理学者** | 司法精神医学・行動科学専門家 | 知的、沈着、臨床的で深い行動洞察 | **36** |
| **N1** | **一般人 1** | ボイントンビーチ近隣住民（第1幕） | 若い女性、動揺、真実味、戦慄 | **8** |
| **N2** | **一般人 2** | パームビーチ郡陪審員（第4幕） | 毅然とした女性、厳格、公平、高い品格 | **9** |
| **合計** | **全編** | **5幕構成 標準A2** | **4言語完全一致 パリティ基準（212文）** | **212** |

---
""",
    "KO": """# 상세 대본 제22화: Dalia Dippolito 파일 — 남편 청부살인범의 악어의 눈물과 카메라 앞의 희대의 연극

* **사건 개요:** 플로리다주 보인턴비치 모의 살인 함정 수사 사건 (2009)
* **심리학적 주제:** 극한의 가스라이팅(Extreme Gaslighting), 악성 자기애(Malignant Narcissism) 및 반사회적 성격장애(ASPD), 악어의 눈물과 연극적 비탄(Crocodile Tears / Performative Grief), 약탈적 정략결혼 및 경제적 착취, 인지적 구획화(Compartmentalization), 도덕적 중화 기법(Techniques of Neutralization)
* **예상 재생 시간:** 24 – 27분
* **포맷:** 표준 A2 규격 — 10대 범죄 심리·행동 분석 지표(A2c) 및 K10 규칙을 준수한 대형 대본(총 212개 문장, 2026년 11월 7일 개정판)
* **유튜브 안전 기준 (Rule V9):** 100% YouTube Safe, 직접적 폭력 묘사 배제. 법행동과학, 미세 표정 분석, 함정 수사 전술 및 유독한 착취 관계 예방 교육에 특화.

---

## 배역 및 보컬 구성표

| 기호 | 역할 | 등장인물 페르소나 | 음성 특성 | 문장 수 |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **진행자 (Host)** | Amber Eyes Voice | 따뜻함, 흡인력, 예리함, 깊이 있는 서사 전달 | **122** |
| **D** | **수사관** | 강력계 수사관 (모델 인물) | 노련함, 단호함, 객관적, 법과학적 엄정성 | **37** |
| **C** | **심리학자** | 법의학적 행동과학 전문가 | 침착함, 객관적, 학술적이고 깊이 있는 분석 | **36** |
| **N1** | **일반인 1** | 보인턴비치 이웃 주민 (1막) | 젊은 여성, 충격, 생생한 전율 | **8** |
| **N2** | **일반인 2** | 팜비치 카운티 법원 배심원 (4막) | 중년 여성, 단호함, 공명정대함, 엄숙한 품격 | **9** |
| **총합** | **대본 전체** | **5막 구성 표준 A2** | **4개 언어 1:1 완벽 동기화 벤치마크 (212문장)** | **212** |

---
""",
}

def render_markdown(lang):
    acts = ALL_ACTS[lang]
    titles = ACT_TITLES[lang]
    lines = [HEADERS[lang].strip(), ""]
    
    for act_idx, (act_data, act_title) in enumerate(zip(acts, titles), 1):
        lines.append(f"## {act_title}")
        lines.append("")
        for item in act_data:
            kind = item[0]
            if kind == "BGM":
                lines.append(f"**[BGM]:** *{item[1]}*")
                lines.append("")
            elif kind == "SFX":
                lines.append(f"**[SFX]:** *{item[1]}*")
                lines.append("")
            elif kind == "LOI":
                role_tag = item[1]
                note = item[2]
                sents = item[3]
                lines.append(f"**{role_tag}** *({note})*:")
                for s in sents:
                    lines.append(s)
                lines.append("")
    return "\n".join(lines).strip() + "\n"

# 1. Generate Markdown files
OUT_PATHS = {
    "VN": ROOT / "01_KICH_BAN" / "Tap22" / "kichban_tap22_23102026.md",
    "EN_DIR": ROOT / "01_KICH_BAN" / "Tap22_EN" / "kichban_tap22_EN.md",
    "EN_COPY": ROOT / "01_KICH_BAN" / "Tap22" / "kichban_tap22_EN.md",
    "JA": ROOT / "01_KICH_BAN" / "Tap22_JA" / "kichban_tap22_JA.md",
    "KO": ROOT / "01_KICH_BAN" / "Tap22_KO" / "kichban_tap22_KO.md",
}

print("Generating Markdown files for Episode 22...")
for lang in ["VN", "EN", "JA", "KO"]:
    content = render_markdown(lang)
    # Ensure unix-style newlines and no double CR
    content = content.replace("\r\n", "\n").replace("\r", "\n")
    if lang == "VN":
        OUT_PATHS["VN"].parent.mkdir(parents=True, exist_ok=True)
        open(OUT_PATHS["VN"], "w", encoding="utf-8", newline="\n").write(content)
        print(f"  Wrote {OUT_PATHS['VN'].relative_to(ROOT)} ({len(content)} chars)")
    elif lang == "EN":
        OUT_PATHS["EN_DIR"].parent.mkdir(parents=True, exist_ok=True)
        open(OUT_PATHS["EN_DIR"], "w", encoding="utf-8", newline="\n").write(content)
        open(OUT_PATHS["EN_COPY"], "w", encoding="utf-8", newline="\n").write(content)
        print(f"  Wrote {OUT_PATHS['EN_DIR'].relative_to(ROOT)} & copy in Tap22/")
    elif lang == "JA":
        OUT_PATHS["JA"].parent.mkdir(parents=True, exist_ok=True)
        open(OUT_PATHS["JA"], "w", encoding="utf-8", newline="\n").write(content)
        print(f"  Wrote {OUT_PATHS['JA'].relative_to(ROOT)} ({len(content)} chars)")
    elif lang == "KO":
        OUT_PATHS["KO"].parent.mkdir(parents=True, exist_ok=True)
        open(OUT_PATHS["KO"], "w", encoding="utf-8", newline="\n").write(content)
        print(f"  Wrote {OUT_PATHS['KO'].relative_to(ROOT)} ({len(content)} chars)")

# 2. Parse scripts to JSON using parse_kichban
print("\nParsing scripts to JSON...")
parsed_vn = PK.parse_file(str(OUT_PATHS["VN"]))
json.dump(parsed_vn, open(ROOT / ".work" / "script_tap22.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("  Wrote .work/script_tap22.json")

parsed_en = PK.parse_file(str(OUT_PATHS["EN_DIR"]))
json.dump(parsed_en, open(ROOT / ".work" / "script_tap22_EN.json", "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("  Wrote .work/script_tap22_EN.json")

print("\nBuild complete. Proceeding to audit...")
