# -*- coding: utf-8 -*-
"""Properly update Korean script for Tap 13 with single quotes matching the file."""
from pathlib import Path

for p in [Path('01_KICH_BAN/Tap13_KO/kichban_tap13_KO.md'), Path('01_KICH_BAN/Tap13/kichban_tap13_KO.md')]:
    lines = p.read_text(encoding='utf-8').splitlines(keepends=True)
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]
        # 1.02#7
        if "후광 효과" in line and "모범 소수자" not in line:
            line = line.replace("'후광 효과'", "'후광 효과'와 '모범 소수자' 신화").replace("“후광 효과”", "“후광 효과”와 “모범 소수자” 신화")
        # 2.04#8
        if "수사 기관의 눈을 돌리기 위해 고의적인 살상 행위를" in line:
            line = "공범 집단은 '책임의 분산'과 냉혹한 도덕적 이탈을 작동시켜, 이를 집안 딸이 의뢰한 단순 용역 계약으로 치부했습니다.\n"
        # 3.07 turn
        if "**심리학자**" in line and "비인간화" in line:
            out.append("**심리학자** *(후회의 메커니즘과 병적 자기연민을 해부하며)*:\n")
            out.append("취조실에 들어섰을 때 가장 큰 의문이 제기되었습니다: 왜 제니퍼는 눈물을 흘렸으며 어떤 심리 기제가 그녀의 후회를 지배했을까요?\n")
            out.append("법심리학은 '진정한 도덕적 참회'와 '실리적 후회'를 엄격히 구분합니다.\n")
            out.append("제니퍼의 고통은 부모를 향한 공감에서 비롯된 것이 아니라, 자유에 대한 환상의 붕괴와 자기애의 파탄에서 촉발되었습니다.\n")
            out.append("완벽했던 계획의 실패에 대한 극심한 후회, 종신형에 대한 공포, 그리고 사회적 가면의 완전한 파멸에 절망한 것입니다.\n")
            out.append("초기 계산 속에서 부모는 자신의 자유와 행복을 가로막는 '장애물'로 격하되었습니다.\n")
            out.append("동시에 거액의 유산과 보험금에 대한 탐욕은 부모를 현금화할 금융 수단으로 전락시켰습니다.\n")
            out.append("인간성 파탄과 결합된 이 실리적 후회는, 자신의 처지를 한탄하는 병리적 자기연민의 눈물로 가장 적나라하게 드러났습니다.\n")
            i += 8 # skip header + 7 sentences
            continue
        out.append(line)
        i += 1
    p.write_text(''.join(out), encoding='utf-8')
    print(f"Updated {p}")
