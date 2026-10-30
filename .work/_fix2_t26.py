#!/usr/bin/env python3
"""Final Tap26 KO fix: role line, merge over-count sentences, restore header lines."""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

KO = Path(__file__).resolve().parents[1] / "01_KICH_BAN" / "Tap26_KO" / "kichban_tap26_KO.md"
text = KO.read_text(encoding="utf-8")

# 1. role line with stray square brackets
ROLE_OLD = "[**호스트** (*지옥 같은 계약과 궁지에 몰린 부모들*):]"
ROLE_NEW = "**호스트** *(지옥 같은 계약과 궁지에 몰린 부모들)*:"
if ROLE_OLD in text:
    text = text.replace(ROLE_OLD, ROLE_NEW)
    print("role line fixed")
else:
    print("!! role line not found")

# 2. merge sentence pairs (each pair = 2 physical lines -> 1 line with ' – ')
PAIRS = [
    ("이는 잔혹한 이중 범죄였습니다.",
     "가난한 가정의 돈을 빼앗고, 동시에 피해자들의 구호분 낭비 그 자체로 이익을 취한 것입니다."),
    ("일본 사회는 충격적으로 깨달았습니다.",
     "이것은 근대 일본 역사상 규모가 가장 큰 신생아 살해 사건이라는 사실이었습니다."),
    ("이는 도덕 중화 기법의 전형적인 표양입니다.",
     "하늘을 거스르는 범죄가 고귀한 구원 행위로 다시 정의되는 자리입니다."),
    ("범죄 행동이 여러 번 반복되면 또 다른 위험한 심리기제가 나타납니다.",
     "바로 감정적 감수성 상실, 즉 Emotional Desensitization입니다."),
    ("이 기제는 조직적 범죄자의 심리와 유사합니다.",
     "이곳에서 윤리적 책임은 분산되고, 서류 행정 절차와정을 통해 정상화됩니다."),
    ("Miyuki Ishikawa는 전쟁기의 결핍을 변명할 수 없습니다.",
     "그녀는 여전히 피해자의 친족에게서 큰 지원금을 정기적으로 받고 있었습니다."),
    ("문명 사회는 물질적 풍요로 규정될 수 없습니다.",
     "그 사회가 가장 약한 아이들을 얼마나 보호하는지로 측정되어야 합니다."),
    ("건전한 보호는 반드시 투명성, 사랑과 배려, 그리고 사실 확인에 근거해야 합니다.",
     "헛된 약속이 아닙니다."),
]
for a, b in PAIRS:
    old = a + "\n" + b
    new = a + " – " + b
    if old in text:
        text = text.replace(old, new)
    else:
        print(f"!! pair not found: {a[:40]}")

# 3. restore the two header lines that got split
HEADERS = [
    ("* **형식:** 표준 A2 – 5막 – 4개의 목소리(Host: 95문, D: 28문, C: 27문, N: 15문 — N1: 7문, N2: 8문.",
     "합계: 정확히 165문)",
     "* **형식:** 표준 A2 – 5막 – 4개의 목소리(Host: 95문, D: 28문, C: 27문, N: 15문 — N1: 7문, N2: 8문, 합계: 정확히 165문)"),
    ("* **YouTube 안전 기준(Rule V9):** 100% YouTube Safe, 성적 폭력이나 신생아의 참혹한 죽음 장면을 절대 묘사하지 않음.",
     "범죄학사 연구, 행동사회학 분석, 직업 윤리의 변형, 국가 행정 책임, 이익추구 시설로부터 아동을 지키는 4가지 위험 신호에 집중.",
     "* **YouTube 안전 기준(Rule V9):** 100% YouTube Safe, 성적 폭력이나 신생아의 참혹한 죽음 장면을 절대 묘사하지 않음; 범죄학사 연구, 행동사회학 분석, 직업 윤리의 변형, 국가 행정 책임, 이익추구 시설로부터 아동을 지키는 4가지 위험 신호에 집중."),
]
for a, b, new in HEADERS:
    old = a + "\n" + b
    if old in text:
        text = text.replace(old, new)
    else:
        print(f"!! header not found: {a[:50]}")

KO.write_text(text, encoding="utf-8")
print("done")
