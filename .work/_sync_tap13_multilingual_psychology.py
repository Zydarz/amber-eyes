# -*- coding: utf-8 -*-
"""Update EN, JA, KO scripts for Tap 13 to align with upgraded psychological analysis in VN script."""
import sys, re, io
from pathlib import Path

# 1. Update EN Script
en_path = Path('01_KICH_BAN/Tap13_EN/kichban_tap13_EN.md')
en_text = en_path.read_text(encoding='utf-8')

# 1.02#7 EN
old_en_1027 = 'The “Halo Effect” swiftly enveloped the household, leading the outside community to revere the Pan family as an unblemished success story while remaining completely blind to the suffocating tensions within.'
new_en_1027 = 'The “Halo Effect” intertwined with the “Model Minority” myth swiftly enveloped the household, leading society to revere the Pan family as an unblemished success story while remaining completely blind to the suffocating tensions within.'

# 2.04#8 EN
old_en_2048 = 'Every operational detail was meticulously tailored to disguise the deliberate execution as a random residential break-in to misdirect law enforcement.'
new_en_2048 = 'The co-conspirators operated under cold moral disengagement and diffusion of responsibility, viewing the contract as a mere transactional service commissioned by the household daughter.'

# 3.07 EN turn
old_en_307 = """**PSYCHOLOGIST** *(clinical cadence, detailing dehumanization)*:
The most perilous development in criminal psychology is the systematic “Dehumanization” of the prospective victim.
As hatred peaked, Jennifer ceased to view her mother and father as living human beings possessed of emotional reality and the right to exist.
In her cold calculations, the couple was demoted to mere “obstacles” blocking her romantic freedom and self-determination.
Concurrently, greed for their substantial life insurance policies and estate reduced her parents to mere financial instruments to be liquidated.
A severe deficit in affective empathy extinguished any lingering filial compassion or moral remorse.
It was this chilling dehumanization that allowed her to calmly usher violent hitmen across the threshold of her family residence.
This marked the apex of moral disintegration driven by a pathological narcissistic ego backed into an inescapable corner."""

new_en_307 = """**PSYCHOLOGIST** *(clinical cadence, dissecting remorse mechanisms)*:
Upon entering the interrogation room, the core analytical question emerged: Why did Jennifer weep, and what psychological mechanism governed her remorse?
Forensic behavioral science draws a sharp distinction between Genuine Moral Remorse and Instrumental Regret.
For Jennifer Pan, anguish did not originate from empathic grief for her parents, but from the sudden collapse of her freedom fantasy and narcissistic ego.
She experienced acute regret over the disastrous failure of her plan, paralyzing terror of life imprisonment, and the utter ruin of her social facade.
In her initial calculations, her parents had been demoted to mere obstacles barring her personal freedom and romantic desires.
Simultaneously, financial greed for their insurance payouts reduced her parents to liquid assets to be monetized.
This instrumental regret, coupled with profound ethical decay, manifested transparently in tears of pathological self-pity for her own plight."""

en_text = en_text.replace(old_en_1027, new_en_1027)
en_text = en_text.replace(old_en_2048, new_en_2048)
en_text = en_text.replace(old_en_307, new_en_307)
en_path.write_text(en_text, encoding='utf-8')
print("Updated EN script.")

# 2. Update JA Script
ja_path = Path('01_KICH_BAN/Tap13_JA/kichban_tap13_JA.md')
ja_text = ja_path.read_text(encoding='utf-8')

old_ja_1027 = '「ハロー効果」は瞬く間にこの家庭を包み込み、世間はパン一家を称賛すべき成功例として眺め、内側に潜む窒息しそうな抑圧には誰も気づきませんでした。'
new_ja_1027 = '「ハロー効果」と「模範的少数派」の神話は瞬く間にこの家庭を包み込み、世間はパン一家を称賛すべき成功例として眺め、内側に潜む窒息しそうな抑圧には誰も気づきませんでした。'

old_ja_2048 = '捜査の手を撹乱するため、計画のあらゆる細部が周到に計算され、意図的な凶行は無作為の押し入り強盗へと巧妙に偽装されました。'
new_ja_2048 = '共犯者たちは「責任の拡散」と冷酷な道徳的脱関与を働かせ、この犯行を家主の娘から依頼された単なる業務請負と見なしていました。'

old_ja_307 = """**心理学者** *(臨床的かつ冷静に、非人間化の過程を解剖する)*:
犯罪心理学において最も危険な転落の一歩は、標的の「非人間化」です。
憎悪が沸点に達したとき、ジェニファーはもはや両親を感情を持ち生きる権利のある生身の人間として認識していませんでした。
彼女の冷酷な計算において、両親は幸福と自由を阻む単なる「障害物」へと格下げされたのです。
同時に、巨額の遺産と生命保険金への執着が、両親を現金化すべき金融手段へと成り下がらせました。
共感能力の著しい欠如は、親子の情愛や道徳的良心の呵責を完全に麻痺させてしまったのです。
この冷酷な非人間化こそが、彼女が自ら凶悪な刺客を自宅に引き入れることを平然と許した心理的背景でした。
これこそが、逃げ場を失った病的な自己愛が引き起こした人間性の完全な崩壊です。"""

new_ja_307 = """**心理学者** *(臨床的かつ冷静に、後悔のメカニズムを解剖する)*:
取調室に入ったとき、最大の疑問が生じました。なぜジェニファーは涙を流し、何が彼女の後悔を支配していたのか。
法心理学では、「真の道徳的悔悟」と「実利的な後悔」を明確に区別します。
ジェニファーの場合、その苦痛は両親への共感ではなく、自由への幻想の崩壊と自己愛の破綻から生じたものでした。
完璧な計画が破綻したことへの猛烈な後悔、終身刑への恐怖、そして築き上げた社会的仮面の完全な喪失に打ちのめされていたのです。
当初の計算において、両親は幸福と自由を阻む単なる「障害物」へと格下げされていました。
同時に、巨額の遺産と生命保険金への執着が、両親を換金すべき金融手段へと成り下がらせました。
人間性の荒廃と結びついた実利的な後悔は、自らの破滅を憐れむ病的な自己憐憫の涙として最も如実に現れたのです。"""

ja_text = ja_text.replace(old_ja_1027, new_ja_1027)
ja_text = ja_text.replace(old_ja_2048, new_ja_2048)
ja_text = ja_text.replace(old_ja_307, new_ja_307)
ja_path.write_text(ja_text, encoding='utf-8')
print("Updated JA script.")

# 3. Update KO Script
ko_path = Path('01_KICH_BAN/Tap13_KO/kichban_tap13_KO.md')
ko_text = ko_path.read_text(encoding='utf-8')

old_ko_1027 = '“후광 효과”는 순식간에 이 가정을 둘러쌌고, 세상은 판 씨 일가를 흠잡을 데 없는 성공 사례로 칭송하며 그 내면에 도사린 숨 막히는 억압은 전혀 알아채지 못했습니다.'
new_ko_1027 = '“후광 효과”와 “모범 소수자” 신화는 순식간에 이 가정을 둘러쌌고, 세상은 판 씨 일가를 흠잡을 데 없는 성공 사례로 칭송하며 그 내면에 도사린 숨 막히는 억압은 전혀 알아채지 못했습니다.'

old_ko_2048 = '수사 기관의 눈을 돌리기 위해 고의적인 살상 행위를 무작위 가택 강도로 위장하도록 계획의 모든 세부 사항이 치밀하게 계산되었습니다.'
new_ko_2048 = '공범 집단은 “책임의 분산”과 냉혹한 도덕적 이탈을 작동시켜, 이를 집안 딸이 의뢰한 단순 용역 계약으로 치부했습니다.'

old_ko_307 = """**심리학자** *(차분하고 학술적인 어조로 비인간화 과정을 해부하며)*:
범죄심리학에서 가장 치명적인 타락의 단계는 대상에 대한 체계적인 “비인간화”입니다.
증오가 극에 달했을 때, 제니퍼는 부모를 감정과 생존 권리를 지닌 인간으로 바라보지 않았습니다.
그녀의 차가운 계산 속에서 부모는 자신의 자유와 행복을 가로막는 “장애물”로 격하되었습니다.
동시에 거액의 유산과 보험금에 대한 탐욕은 부모를 청산해야 할 금융 수단으로 전락시켰습니다.
정서적 공감 능력의 치명적 결여는 일말의 효심이나 양심의 가책마저 완전히 마비시켰습니다.
이 냉혹한 비인간화 기제가 있었기에, 그녀는 태연히 흉악범들을 집 안으로 안내할 수 있었습니다.
이것은 막다른 골목에 몰린 병리적 자기애가 빚어낸 인간성 붕괴의 극치였습니다."""

new_ko_307 = """**심리학자** *(차분하고 학술적인 어조로 후회의 메커니즘을 해부하며)*:
취조실에 들어섰을 때 가장 큰 의문이 제기되었습니다. 왜 제니퍼는 눈물을 흘렸으며, 어떤 심리 기제가 그녀의 후회를 지배했을까요?
법심리학은 “진정한 도덕적 참회”와 “실리적 후회”를 엄격히 구분합니다.
제니퍼의 고통은 부모를 향한 공감에서 비롯된 것이 아니라, 자유에 대한 환상의 붕괴와 자기애의 파탄에서 촉발되었습니다.
완벽했던 계획의 실패에 대한 극심한 후회, 종신형에 대한 공포, 그리고 사회적 가면의 완전한 파멸에 절망한 것입니다.
초기 계산 속에서 부모는 자신의 자유와 행복을 가로막는 “장애물”로 격하되었습니다.
동시에 거액의 유산과 보험금에 대한 탐욕은 부모를 현금화할 금융 수단으로 전락시켰습니다.
인간성 파탄과 결합된 이 실리적 후회는, 자신의 처지를 한탄하는 병리적 자기연민의 눈물로 가장 적나라하게 드러났습니다."""

ko_text = ko_text.replace(old_ko_1027, new_ko_1027)
ko_text = ko_text.replace(old_ko_2048, new_ko_2048)
ko_text = ko_text.replace(old_ko_307, new_ko_307)
ko_path.write_text(ko_text, encoding='utf-8')
print("Updated KO script.")
