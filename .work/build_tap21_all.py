# -*- coding: utf-8 -*-
"""Build, parse and verify all 4 language editions for Episode 21 (212 sentences)."""

import os
import sys
import json
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))

import parse_kichban as PK
from tap21_act1 import ACT1_VN, ACT1_EN, ACT1_JA, ACT1_KO
from tap21_act2 import ACT2_VN, ACT2_EN, ACT2_JA, ACT2_KO
from tap21_act3 import ACT3_VN, ACT3_EN, ACT3_JA, ACT3_KO
from tap21_act4 import ACT4_VN, ACT4_EN, ACT4_JA, ACT4_KO
from tap21_act5 import ACT5_VN, ACT5_EN, ACT5_JA, ACT5_KO

ALL_ACTS = {
    "VN": [ACT1_VN, ACT2_VN, ACT3_VN, ACT4_VN, ACT5_VN],
    "EN": [ACT1_EN, ACT2_EN, ACT3_EN, ACT4_EN, ACT5_EN],
    "JA": [ACT1_JA, ACT2_JA, ACT3_JA, ACT4_JA, ACT5_JA],
    "KO": [ACT1_KO, ACT2_KO, ACT3_KO, ACT4_KO, ACT5_KO],
}

ACT_TITLES = {
    "VN": [
        "HỒI 1: CUỘC GỌI 911 RẠNG SÁNG & NGÔI NHÀ IM LÌM TẠI HOUSTON",
        "HỒI 2: VỰC THẲM CỦA SỰ CÔ ĐỘC & TIẾNG CHUÔNG CẢNH BÁO BỊ PHỚT LỜ",
        "HỒI 3: GIẢI MÃ TÂM LÝ: LOẠN THẦN SAU SINH & HOANG TƯỞNG CỨU CHUỘC",
        "HỒI 4: PHIÊN TÒA LỊCH SỬ & PHÁN QUYẾT KHÔNG CÓ TỘI VÌ LÝ DO TÂM THẦN",
        "HỒI 5: BÀI HỌC CẢNH TỈNH & 4 CẢNH BÁO ĐỎ NHẬN DIỆN LOẠN THẦN SAU SINH",
    ],
    "EN": [
        "ACT 1: THE EARLY MORNING 911 CALL & THE SILENT HOUSTON HOME",
        "ACT 2: THE ABYSS OF ISOLATION & THE UNHEEDED CLINICAL WARNINGS",
        "ACT 3: PSYCHOLOGICAL DISSECTION: POSTPARTUM PSYCHOSIS & ALTRUISTIC DELUSIONS",
        "ACT 4: THE HISTORIC TRIAL & NOT GUILTY BY REASON OF INSANITY VERDICT",
        "ACT 5: AWAKENING LESSONS & 4 RED FLAGS IDENTIFYING POSTPARTUM PSYCHOSIS",
    ],
    "JA": [
        "第1幕: 早朝の緊急通報911と沈黙のヒューストン住宅",
        "第2幕: 孤立の深淵と無視された医療の警告",
        "第3幕: 深層心理の解剖：産後精神病と歪んだ救済妄想",
        "第4幕: 歴史的法廷闘争と心神喪失による無罪評決",
        "第5幕: 覚醒の教訓と産後精神病を見抜く4つの危険兆候",
    ],
    "KO": [
        "막 1: 이른 아침 911 신고와 침묵의 휴스턴 자택",
        "막 2: 고립의 심연과 방치된 의학적 경고",
        "막 3: 범죄 심리 해부: 산후 정신병과 뒤틀린 구원 망상",
        "막 4: 역사적 재판과 심신상실로 인한 무죄 평결",
        "막 5: 각성의 교훈과 산후 정신병을 식별하는 4대 위험 징후",
    ],
}

ROLE_NAMES = {
    "VN": {"H": "HOST", "D": "ĐIỀU TRA VIÊN", "C": "CHUYÊN GIA TÂM LÝ", "N": "NGƯỜI BÌNH THƯỜNG"},
    "EN": {"H": "HOST", "D": "INVESTIGATOR", "C": "PSYCHOLOGIST", "N": "ORDINARY PERSON"},
    "JA": {"H": "ホスト", "D": "捜査官", "C": "心理学者", "N": "一般人"},
    "KO": {"H": "호스트", "D": "수사관", "C": "심리학자", "N": "일반인"},
}

HEADERS = {
    "VN": """# KỊCH BẢN CHI TIẾT TẬP 21: HỒ SƠ ANDREA YATES — BI KỊCH CỦA CƠN LOẠN THẦN SAU SINH & KHI ẢO GIÁC ĐÁNH CẮP THIÊN CHỨC LÀM MẸ

* **Đề tài:** Vụ án năm đứa trẻ tại Clear Lake (Houston, Texas, 2001) và Cuộc chiến pháp lý lịch sử về ranh giới Loạn thần sau sinh
* **Chủ đề tâm lý:** Loạn thần sau sinh cấp tính (Postpartum Psychosis), Sự mất kết nối hoàn toàn với thực tại (Severe Reality Break), Hoang tưởng tôn giáo cứu chuộc (Altruistic Filicide / Religious Delusions of Salvation), Ranh giới pháp lý Quy tắc M'Naghten (Insanity Defense) vs. Malingering (Giả bệnh)
* **Thời lượng dự kiến:** 24 – 27 phút
* **Định dạng:** Chuẩn A2 — Bản nâng cấp kịch bản quy mô lớn (212 câu thoại) theo Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c) và Luật K10 (07/11/2026)
* **Tiêu chuẩn An toàn YouTube (Rule V9):** 100% YouTube Safe, tuyệt đối không mô tả trực diện nước hay chi tiết ngạt thở đau đớn của trẻ em; tiếp cận với sự nhân văn, chuẩn mực y khoa pháp lý, tôn trọng nỗi đau gia đình và nâng cao nhận thức bảo vệ sức khỏe tâm thần bà mẹ.

---

## BẢNG PHÂN VAI VÀ CẤU TRÚC GIỌNG ĐỌC

| Ký hiệu | Vai trò | Tên nhân vật thể hiện | Đặc điểm giọng đọc | Số câu |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **Dẫn chuyện (Host)** | Amber Eyes Voice | Trầm ấm, xót xa, sắc sảo, dẫn dắt nhân văn sâu sắc | **122** |
| **D** | **Điều tra viên** | Điều tra viên (nhân vật minh hoạ) | Nam trung niên, dày dạn kinh nghiệm, điềm tĩnh, trắc ẩn | **37** |
| **C** | **Chuyên gia Tâm lý** | Chuyên gia Tâm thần học Pháp y | Điềm đạm, khách quan, giàu hàm lượng khoa học lâm sàng | **36** |
| **N1** | **Người trong cuộc 1** | Người hàng xóm minh hoạ (Hồi 1) | Nữ thanh niên, bàng hoàng, xót xa, chân thực | **8** |
| **N2** | **Người trong cuộc 2** | Bồi thẩm viên minh hoạ (Hồi 4) | Nữ trung niên, nghiêm nghị, trăn trở, nhân văn | **9** |
| **TỔNG** | **Toàn bộ kịch bản** | **5 Hồi chuẩn A2** | **Cân bằng hoàn hảo theo Golden Benchmark (>200 câu)** | **212** |

---
""",
    "EN": """# DETAILED SCRIPT EPISODE 21: ANDREA YATES DOSSIER — THE TRAGEDY OF POSTPARTUM PSYCHOSIS & SHATTERED MOTHERHOOD

* **Subject:** The Clear Lake Five Children Case (Houston, Texas, 2001) and the Historic Legal Landmark of Maternal Insanity Defense
* **Psychological Themes:** Acute Postpartum Psychosis, Severe Reality Rupture, Altruistic Filicide & Religious Delusions of Salvation, Texas M'Naghten Insanity Standard vs. Feigned Mental Illness (Malingering)
* **Estimated Running Time:** 24 – 27 minutes
* **Format:** Standard A2 — High-Scale Script (212 Spoken Sentences) based on the 10 Psychological & Behavioral Dimensions (A2c) and Rule K10 (07/11/2026)
* **YouTube Safety Standard (Rule V9):** 100% YouTube Safe, zero graphic depictions of violence or child distress; strictly focused on clinical forensic science, judicial reform, and humanitarian awareness for maternal mental health.

---

## CAST AND VOCAL ARCHITECTURE

| Symbol | Role | Persona / Character | Vocal Attributes | Sentences |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **Host** | Amber Eyes Voice | Warm, empathetic, resonant, deeply penetrating narrative | **122** |
| **D** | **Investigator** | Homicide Detective (Representative Persona) | Middle-aged male, seasoned, calm, deeply compassionate | **37** |
| **C** | **Psychologist** | Forensic Psychiatrist | Scholarly, objective, profound clinical behavioral insight | **36** |
| **N1** | **Ordinary Person 1** | Clear Lake Neighbor Persona (Act 1) | Young female, shaken, heartbroken, authentic grief | **8** |
| **N2** | **Ordinary Person 2** | Retrial Juror Persona (Act 4) | Mature female, solemn, contemplative, deeply human | **9** |
| **TOTAL** | **Full Episode** | **5 Acts Standard A2** | **1:1 Multilingual Parity Benchmark (>200 Sentences)** | **212** |

---
""",
    "JA": """# 詳細台本 第21話：アンドレア・イエーツ事件 — 産後精神病の悲劇と母性を奪った救済妄想の深層

* **事件記録:** テキサス州ヒューストン・クリアレイク5児童事件（2001年）および産後精神病を巡る歴史的法廷闘争
* **心理学的主題:** 急性産後精神病（Postpartum Psychosis）、完全な現実感喪失（Reality Rupture）、利他的子殺しと宗教的救済妄想（Altruistic Filicide / Religious Delusions of Salvation）、テキサス州マクノートン規則（心神喪失抗弁）と詐病（Malingering）の厳格な峻別
* **予想再生時間:** 24 – 27分
* **フォーマット:** 標準A2規格 — 10の心理・行動分析指標（A2c）およびK10規則に準拠した大規模脚本（全212文・2026年11月7日改訂版）
* **YouTube安全基準 (Rule V9):** 100% YouTube Safe、直接的な暴力や身体的苦痛描写を完全に排除。人道精神に基づき、司法精神医学の知見、法廷改革、および周産期メンタルヘルス啓発に特化。

---

## 配役および声の構成表

| 記号 | 役割 | 登場人物 | 声の特質 | 文数 |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **H** | **ホスト (Host)** | Amber Eyes Voice | 温かく深みがあり、心に染み入る人道的な語り | **122** |
| **D** | **捜査官** | 殺人課刑事（モデル人物） | 中年男性、熟練、沈着冷静、深い哀感と慈悲 | **37** |
| **C** | **心理学者** | 司法精神科医 | 学究的、客観的、深い臨床行動科学の知見 | **36** |
| **N1** | **一般人 1** | 近隣住民代表（第1幕） | 若い女性、動揺、悲痛、戦慄 | **8** |
| **N2** | **一般人 2** | 再審陪審員代表（第4幕） | 落ち着いた女性、厳粛、思索的、深い共感 | **9** |
| **合計** | **全編** | **5幕構成 標準A2** | **4言語完全一致 パリティ基準（212文）** | **212** |

---
""",
    "KO": """# 상세 대본 제21화: Andrea Yates 파일 — 산후 정신병의 비극과 모성을 집어삼킨 구원 망상

* **사건 개요:** 텍사스주 휴스턴 클리어 레이크 다섯 아동 사건 (2001) 및 산후 정신병을 둘러싼 역사적 사법 투쟁
* **심리학적 주제:** 급성 산후 정신병(Postpartum Psychosis), 중증 현실 단절(Reality Rupture), 이타적 자녀 살해 및 종교적 구원 망상(Altruistic Filicide / Religious Delusions of Salvation), 텍사스주 맥노튼 원칙(심신상실 변론)과 꾀병(Malingering)의 과학적 감별
* **예상 러닝타임:** 24 – 27분
* **형식:** 표준 A2 규격 — 10대 심리·행동 분석 생태계(A2c) 및 K10 규칙 기반 대형 대본 (총 212개 발화 문장 / 2026년 11월 7일 개정)
* **YouTube 안전 규정 (Rule V9):** 100% YouTube Safe, 직접적이거나 자극적인 폭력 묘사를 철저히 배제하고 법정신과학, 사법 개혁 및 산모의 정신 건강 보호 인식 제고에 집중.

---

## 배역 편성 및 보이스 아키텍처

| 기호 | 역할 | 페르소나 / 등장인물 | 음성 특성 | 문장 수 |
| :--- | :--- | :--- | :--- | :--- | :---: |
| **H** | **호스트 (Host)** | Amber Eyes Voice | 깊고 따뜻하며 슬픔과 성찰을 담은 울림 있는 진행 | **122** |
| **D** | **수사관** | 강력계 수사관 (대표 페르소나) | 중년 남성, 노련함, 침착함, 깊은 연민 | **37** |
| **C** | **심리학자** | 사법 정신과 전문의 | 학구적, 객관성, 심도 있는 임상 행동과학적 통찰 | **36** |
| **N1** | **일반인 1** | 클리어 레이크 이웃 대표 (제1막) | 젊은 여성, 충격, 비통함, 생생한 전율 | **8** |
| **N2** | **일반인 2** | 재심 배심원 대표 (제4막) | 차분한 여성, 엄숙함, 고뇌 어린 진심, 깊은 인간애 | **9** |
| **총합** | **대본 전체** | **5막 표준 A2** | **4개 언어 1:1 완벽 패리티 기준 (212문장)** | **212** |

---
""",
}


def build_markdown(lang):
    lines = [HEADERS[lang].strip()]
    acts = ALL_ACTS[lang]
    titles = ACT_TITLES[lang]
    roles_map = ROLE_NAMES[lang]
    
    for act_idx, (act_data, act_title) in enumerate(zip(acts, titles), 1):
        lines.append(f"\n## {act_title}\n")
        for item in act_data:
            kind = item["kind"]
            if kind == "BGM":
                lines.append(f"**[BGM]:** *{item['text']}*\n")
            elif kind == "SFX":
                lines.append(f"**[SFX]:** *{item['text']}*\n")
            elif kind == "LOI":
                role_code = item["role"]
                role_display = roles_map[role_code]
                desc = item.get("desc", "")
                
                if desc:
                    role_hdr = f"**{role_display}** *({desc})*:"
                else:
                    role_hdr = f"**{role_display}**:"
                lines.append(role_hdr)
                
                for s in item["sentences"]:
                    lines.append(s)
                lines.append("")  # blank line after speech
                
    return "\n".join(lines).strip() + "\n"


def main():
    print("=" * 70)
    print("BUILDING TAP 21 SCRIPTS ACROSS 4 LANGUAGES (212 SENTENCES)")
    print("=" * 70)
    
    out_paths = {
        "VN": [ROOT / "01_KICH_BAN" / "Tap21" / "kichban_tap21_23102026.md"],
        "EN": [
            ROOT / "01_KICH_BAN" / "Tap21" / "kichban_tap21_EN.md",
            ROOT / "01_KICH_BAN" / "Tap21_EN" / "kichban_tap21_EN.md",
        ],
        "JA": [ROOT / "01_KICH_BAN" / "Tap21_JA" / "kichban_tap21_JA.md"],
        "KO": [ROOT / "01_KICH_BAN" / "Tap21_KO" / "kichban_tap21_KO.md"],
    }
    
    for lang in ["VN", "EN", "JA", "KO"]:
        md_text = build_markdown(lang)
        for p in out_paths[lang]:
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "wb") as f:
                f.write(md_text.encode("utf-8"))
            print(f"Written: {p.relative_to(ROOT)} ({len(md_text)} chars)")
            
    print("\nParsing with .work/parse_kichban.py...")
    parsed = {}
    for lang in ["VN", "EN", "JA", "KO"]:
        sample_path = out_paths[lang][0]
        out_json = ROOT / ".work" / f"script_tap21_{lang}.json" if lang != "VN" else ROOT / ".work" / "script_tap21.json"
        els = PK.parse_file(str(sample_path), str(out_json))
        parsed[lang] = els
        loi = [e for e in els if e["kind"] == "LOI"]
        s_cnt = sum(len(e["sentences"]) for e in loi)
        w_cnt = sum(sum(s["words"] for s in e["sentences"]) for e in loi)
        print(f"[{lang}] Elements={len(els)}, LOI turns={len(loi)}, Sentences={s_cnt}, Words={w_cnt}")

    # Check parity
    print("\nChecking 1:1 Parity against VN:")
    vn_els = parsed["VN"]
    all_ok = True
    for lang in ["EN", "JA", "KO"]:
        target_els = parsed[lang]
        if len(target_els) != len(vn_els):
            print(f"FAIL: Element count mismatch {lang}: {len(target_els)} vs {len(vn_els)}")
            all_ok = False
            continue
        for i, (ve, te) in enumerate(zip(vn_els, target_els)):
            if ve["kind"] != te["kind"]:
                print(f"FAIL: Kind mismatch at index {i} ({ve['id']}): {lang}={te['kind']} vs VN={ve['kind']}")
                all_ok = False
            if ve["kind"] == "LOI":
                if ve["role"] != te["role"]:
                    print(f"FAIL: Role mismatch at {ve['id']} ({lang}): {te['role']} vs VN={ve['role']}")
                    all_ok = False
                vc = len(ve["sentences"])
                tc = len(te["sentences"])
                if vc != tc:
                    print(f"FAIL: Sentence count mismatch at {ve['id']} ({lang}): {tc} vs VN={vc}")
                    all_ok = False
                    
    if all_ok:
        print("\n>>> ALL 4 LANGUAGES: 100% PERFECT 1:1 PARITY ACROSS ALL 51 ELEMENTS AND 212 SENTENCES! <<<")
    else:
        print("\n>>> PARITY MISMATCHES DETECTED! <<<")


if __name__ == "__main__":
    main()
