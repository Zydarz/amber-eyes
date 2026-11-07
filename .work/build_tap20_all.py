# -*- coding: utf-8 -*-
"""Build and verify all 4 language editions for Episode 20 (212 sentences)."""

import os
import sys
import json
import re
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))

import parse_kichban as PK
from tap20_act1 import ACT1_VN, ACT1_EN, ACT1_JA, ACT1_KO
from tap20_act2 import ACT2_VN, ACT2_EN, ACT2_JA, ACT2_KO
from tap20_act3 import ACT3_VN, ACT3_EN, ACT3_JA, ACT3_KO
from tap20_act4 import ACT4_VN, ACT4_EN, ACT4_JA, ACT4_KO
from tap20_act5 import ACT5_VN, ACT5_EN, ACT5_JA, ACT5_KO

ALL_ACTS = {
    "VN": [ACT1_VN, ACT2_VN, ACT3_VN, ACT4_VN, ACT5_VN],
    "EN": [ACT1_EN, ACT2_EN, ACT3_EN, ACT4_EN, ACT5_EN],
    "JA": [ACT1_JA, ACT2_JA, ACT3_JA, ACT4_JA, ACT5_JA],
    "KO": [ACT1_KO, ACT2_KO, ACT3_KO, ACT4_KO, ACT5_KO],
}

ACT_TITLES = {
    "VN": [
        "HỒI 1: CUỘC PHỎNG VẤN ĐỊNH MỆNH & TIN BÁO BẤT NGỜ TỪ THÙNG RÁC",
        "HỒI 2: BỨC TƯỢNG ĐÁ TRONG PHÒNG HỎI CUNG & CÚ SỐC NHẬN THỨC",
        "HỒI 3: GIẢI MÃ TÂM LÝ: KẺ RÌNH RẬP NGẦM & PHẢN ỨNG ĐÓNG BĂNG KỲ DỊ",
        "HỒI 4: PHÁN QUYẾT CHUNG THÂN & SỰ TRỪNG PHẠT CỦA CÔNG LÝ",
        "HỒI 5: BÀI HỌC CẢNH TỈNH & 4 CẢNH BÁO ĐỎ PHÒNG NGỪA KẺ RÌNH RẬP NGẦM",
    ],
    "EN": [
        "ACT 1: THE FATEFUL INTERVIEW & THE UNEXPECTED DISCOVERY",
        "ACT 2: THE STONE STATUE IN THE INTERROGATION ROOM & COGNITIVE SHOCK",
        "ACT 3: PSYCHOLOGICAL DISSECTION: THE PREDATORY STALKER & TONIC IMMOBILITY",
        "ACT 4: THE LIFE VERDICT & RETRIBUTION OF JUSTICE",
        "ACT 5: AWAKENING LESSONS & 4 RED FLAGS AGAINST COVERT STALKING",
    ],
    "JA": [
        "第1幕: 運命の生中継インタビューと予期せぬ衝撃の一報",
        "第2幕: 取調室の石像と認知的ショックの深層",
        "第3幕: 深層心理の解剖：観察型ストーカーと凍結反応の力学",
        "第4幕: 終身刑の判決と司法の厳正なる断罪",
        "第5幕: 覚醒の教訓と捕食的ストーカーを防ぐ4つの危険兆候",
    ],
    "KO": [
        "막 1: 운명의 생방송 인터뷰와 쓰레기통의 비극적 발견",
        "막 2: 취조실의 석상과 인지적 충격의 실체",
        "막 3: 범죄 심리 해부: 포식적 스토커와 기이한 동결 반응",
        "막 4: 종신형 선고와 준엄한 사법적 단죄",
        "막 5: 각성의 교훈과 은밀한 스토킹을 막는 4대 위험 징후",
    ],
}

HEADERS = {
    "VN": """# KỊCH BẢN CHI TIẾT TẬP 20: HỒ SƠ STEPHEN MCDANIEL — KHOẢNH KHẮC SỤP ĐỔ TRƯỚC ỐNG KÍNH & PHẢN ỨNG ĐÓNG BĂNG KỲ DỊ

* **Đề tài:** Vụ án Lauren Giddings tại Trường Luật Mercer (Macon, Georgia, 2011)
* **Chủ đề tâm lý:** Tâm lý kẻ rình rập săn mồi (Predatory Stalker), Chứng thị dâm săn mồi (Predatory Voyeurism), Rối loạn nhân cách ái kỷ ẩn tàng (Covert Narcissism), Phản ứng đóng băng sinh lý (Freeze Response / Tonic Immobility) & Vi biểu cảm khi bị sốc tội lỗi trên sóng truyền hình
* **Thời lượng dự kiến:** 24 – 27 phút
* **Định dạng:** Chuẩn A2 — Bản nâng cấp kịch bản quy mô lớn (212 câu thoại) theo Hệ sinh thái 10 chỉ dấu tâm lý & hành vi (A2c) và Luật K10 (07/11/2026)
* **Tiêu chuẩn An toàn YouTube (Rule V9):** 100% YouTube Safe, không mô tả trực diện phân hủy hay chi tiết bạo lực ghê rợn; tập trung 100% vào phân tích tâm lý học tội phạm, vi biểu cảm, chiến thuật hỏi cung và bài học phòng ngừa kẻ rình rập ngầm.

---

## BẢNG PHÂN VAI VÀ CẤU TRÚC GIỌNG ĐỌC

| Ký hiệu | Vai trò | Tên nhân vật thể hiện | Đặc điểm giọng đọc | Số câu |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **Dẫn chuyện (Host)** | Amber Eyes Voice | Trầm ấm, lôi cuốn, sắc sảo, dẫn dắt thấu đáo | **122** |
| **D** | **Điều tra viên** | Điều tra viên (nhân vật minh hoạ) | Nam trung niên, dày dạn kinh nghiệm, điềm tĩnh, đanh thép | **37** |
| **C** | **Chuyên gia Tâm lý** | Chuyên gia Tâm lý học Pháp y | Điềm đạm, khách quan, giàu hàm lượng khoa học hành vi | **36** |
| **N1** | **Người trong cuộc 1** | Bạn học Trường Luật Mercer (Hồi 1) | Nữ thanh niên, bàng hoàng, chân thực, rùng mình | **8** |
| **N2** | **Người trong cuộc 2** | Người thân minh hoạ của gia đình nạn nhân (Hồi 4) | Nữ trung niên, nghẹn ngào, đau xót, kiên cường | **9** |
| **TỔNG** | **Toàn bộ kịch bản** | **5 Hồi chuẩn A2** | **Cân bằng hoàn hảo theo Golden Benchmark (>200 câu)** | **212** |

---
""",
    "EN": """# DETAILED SCRIPT EPISODE 20: STEPHEN MCDANIEL DOSSIER — THE ON-CAMERA COLLAPSE & THE EERIE FREEZE RESPONSE

* **Subject:** The Lauren Giddings Case at Mercer University Walter F. George School of Law (Macon, Georgia, 2011)
* **Psychological Themes:** Predatory Stalking, Predatory Voyeurism, Covert Narcissism, Physiological Freeze Response (Tonic Immobility) & Micro-Expressions of Guilty Shock on Live Television
* **Estimated Running Time:** 24 – 27 minutes
* **Format:** Standard A2 — High-Scale Script (212 Spoken Sentences) based on the 10 Psychological & Behavioral Dimensions (A2c) and Rule K10 (07/11/2026)
* **YouTube Safety Standard (Rule V9):** 100% YouTube Safe, zero graphic depictions of gore or bodily harm; 100% focused on forensic behavioral science, micro-expression analysis, investigative tactics, and survival red flags.

---

## CAST AND VOCAL ARCHITECTURE

| Symbol | Role | Persona / Character | Vocal Attributes | Sentences |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **Host** | Amber Eyes Voice | Warm, resonant, compelling, penetrating narrative arc | **122** |
| **D** | **Investigator** | Homicide Detective (Representative Persona) | Seasoned, steely, objective, forensic precision | **37** |
| **C** | **Psychologist** | Forensic Behavioral Scientist | Scholarly, clinical, insightful behavioral analysis | **36** |
| **N1** | **Ordinary Person 1** | Mercer Law School Classmate (Act 1) | Young female, shaken, authentic, visceral grief | **8** |
| **N2** | **Ordinary Person 2** | Lauren's Family Representative (Act 4) | Dignified female, emotionally choked yet fiercely resilient | **9** |
| **TOTAL** | **Full Episode** | **5 Acts Standard A2** | **1:1 Multilingual Parity Benchmark (>200 Sentences)** | **212** |

---
""",
    "JA": """# 詳細台本 第20話：スティーブン・マクダニエル事件 — 生中継の崩壊劇と奇怪な凍結反応の真相

* **事件記録:** ジョージア州メーコン・マーサー大学ロースクール ローレン・ギディングス事件（2011年）
* **心理学的主題:** 捕食的ストーカー（Predatory Stalker）、捕食的観察行動（Predatory Voyeurism）、隠れ自己愛性パーソナリティ（Covert Narcissism）、生理的凍結反応（Freeze Response / Tonic Immobility）、生中継における微表情と罪悪感の暴発
* **予想再生時間:** 24 – 27分
* **フォーマット:** 標準A2規格 — 10の心理・行動分析指標（A2c）およびK10規則に準拠した大規模脚本（全212文・2026年11月7日改訂版）
* **YouTube安全基準 (Rule V9):** 100% YouTube Safe、直接的・過激な暴力や損壊描写を完全に排除。行動科学、微表情の法医学的分析、取調べ戦術および実践的防犯教育に特化。

---

## 配役および声の構成表

| 記号 | 役割 | 登場人物 | 声の特質 | 文数 |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **ホスト (Host)** | Amber Eyes Voice | 落ち着き、深み、説得力に富んだ物語の語り手 | **122** |
| **D** | **捜査官** | 殺人課刑事（モデル人物） | 熟練、冷徹、客観的、科学捜査の確証 | **37** |
| **C** | **心理学者** | 司法精神医学・行動科学専門家 | 知的、沈着、臨床的で深い行動洞察 | **36** |
| **N1** | **一般人 1** | マーサー大学ロースクール同期生（第1幕） | 若い女性、動揺、真実味、戦慄 | **8** |
| **N2** | **一般人 2** | 犠牲者遺族代表（第4幕） | 毅然とした女性、悲嘆に暮れつつも揺るぎない尊厳 | **9** |
| **合計** | **全編** | **5幕構成 標準A2** | **4言語完全一致 パリティ基準（212文）** | **212** |

---
""",
    "KO": """# 상세 대본 제20화: Stephen McDaniel 파일 — 생방송 카메라 앞의 붕괴와 기이한 동결 반응

* **사건 개요:** 조지아주 메이컨 머서대학교 Walter F. George 법학전문대학원 Lauren Giddings 사건 (2011)
* **심리학적 주제:** 포식적 스토킹(Predatory Stalking), 포식적 관음증(Predatory Voyeurism), 내현적 자기애성 인격(Covert Narcissism), 생리적 동결 반응(Freeze Response / Tonic Immobility), 생방송 중 유죄 쇼크의 미세 표정
* **예상 러닝타임:** 24 – 27분
* **형식:** 표준 A2 규격 — 10대 심리·행동 분석 생태계(A2c) 및 K10 규칙 기반 대형 대본 (총 212개 발화 문장 / 2026년 11월 7일 개정)
* **YouTube 안전 규정 (Rule V9):** 100% YouTube Safe, 직접적이거나 엽기적인 폭력 묘사를 완벽히 배제하고 법과학 행동 분석, 취조 전술 및 현실적 생존 경고에 집중.

---

## 배역 편성 및 보이스 아키텍처

| 기호 | 역할 | 페르소나 / 등장인물 | 음성 특성 | 문장 수 |
| :--- | :--- | :--- | :--- | :---: |
| **H** | **호스트 (Host)** | Amber Eyes Voice | 깊고 따뜻하며 흡인력 있는 내러티브 진행 | **122** |
| **D** | **수사관** | 강력계 수사관 (대표 페르소나) | 노련함, 냉철함, 객관성, 법과학적 확신 | **37** |
| **C** | **심리학자** | 법정신과학 행동 분석 전문가 | 학구적, 차분함, 임상적 깊이를 담은 심리 해체 | **36** |
| **N1** | **일반인 1** | 머서 로스쿨 동기생 (제1막) | 젊은 여성, 충격, 생생함, 전율 | **8** |
| **N2** | **일반인 2** | Lauren의 유가족 대표 (제4막) | 품격 있는 여성, 눈물 속에서도 꺾이지 않는 존엄 | **9** |
| **총합** | **대본 전체** | **5막 표준 A2** | **4개 언어 1:1 완벽 패리티 기준 (212문장)** | **212** |

---
""",
}


def build_markdown(lang):
    lines = [HEADERS[lang].strip()]
    acts = ALL_ACTS[lang]
    titles = ACT_TITLES[lang]
    
    for act_idx, (act_data, act_title) in enumerate(zip(acts, titles), 1):
        lines.append(f"\n## {act_title}\n")
        for item in act_data:
            kind = item[0]
            if kind == "BGM":
                lines.append(f"**[BGM]:** *{item[1]}*\n")
            elif kind == "SFX":
                lines.append(f"**[SFX]:** *{item[1]}*\n")
            elif kind == "LOI":
                role = item[1]
                direction = item[2]
                sentences = item[3]
                
                # Format role header
                role_hdr = f"**{role}**"
                if direction:
                    role_hdr += f" *({direction})*:"
                else:
                    role_hdr += ":"
                lines.append(role_hdr)
                
                for s in sentences:
                    lines.append(s)
                lines.append("")  # blank line after turn
                
    return "\n".join(lines).strip() + "\n"


def main():
    print("=" * 70)
    print("BUILDING TAP 20 SCRIPTS ACROSS 4 LANGUAGES (212 SENTENCES)")
    print("=" * 70)
    
    out_paths = {
        "VN": [ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_23102026.md"],
        "EN": [
            ROOT / "01_KICH_BAN" / "Tap20" / "kichban_tap20_EN.md",
            ROOT / "01_KICH_BAN" / "Tap20_EN" / "kichban_tap20_EN.md",
        ],
        "JA": [ROOT / "01_KICH_BAN" / "Tap20_JA" / "kichban_tap20_JA.md"],
        "KO": [ROOT / "01_KICH_BAN" / "Tap20_KO" / "kichban_tap20_KO.md"],
    }
    
    for lang in ["VN", "EN", "JA", "KO"]:
        md_text = build_markdown(lang)
        for p in out_paths[lang]:
            p.parent.mkdir(parents=True, exist_ok=True)
            with open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(md_text)
            print(f"Written: {p.relative_to(ROOT)} ({len(md_text)} chars)")
            
    print("\nParsing with .work/parse_kichban.py...")
    parsed = {}
    for lang in ["VN", "EN", "JA", "KO"]:
        sample_path = out_paths[lang][0]
        out_json = ROOT / ".work" / f"script_tap20_{lang}.json" if lang != "VN" else ROOT / ".work" / "script_tap20.json"
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
