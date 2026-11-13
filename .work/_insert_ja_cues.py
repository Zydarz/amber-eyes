# -*- coding: utf-8 -*-
import sys, re
sys.path.insert(0, '.work')
import _qc_ja
from pathlib import Path

with open('01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
for i, l in enumerate(lines):
    # 1. Before "このような凶行の息苦しい闇の中で..."
    if l.startswith("このような凶行の息苦しい闇の中で"):
        new_lines.append("\n**ホスト** *(感情を込め、気高い不屈の精神を称える)*:\n")
    # 2. Before "行動科学の視点から言えば..."
    elif l.startswith("行動科学の視点から言えば"):
        new_lines.append("\n**心理学者** *(映像署名の病理学的メカニズムを分析する)*:\n")
    # 3. Before "実の姉がなぜ妹を罠に誘い込み..."
    elif l.startswith("実の姉がなぜ妹を罠に誘い込み"):
        new_lines.append("\n**心理学者** *(深層の区画化と道徳的昏睡を解き明かす)*:\n")
    # 4. Before "心理学の視点から見れば、Karla Homolkaの12年..."
    elif l.startswith("心理学の視点から見れば"):
        new_lines.append("\n**心理学者** *(学術的な視点から、エゴの崩壊と被害者の仮面を対比させる)*:\n")
    new_lines.append(l)

with open('01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md', 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

vn = Path('01_KICH_BAN/Tap11/kichban_tap11_23102026.md')
ja = Path('01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md')
c_vn = _qc_ja.shape_count(vn)
c_ja = _qc_ja.shape_count(ja)
print("c_vn:", c_vn)
print("c_ja:", c_ja)
diff = {k: (c_vn.get(k, 0), c_ja.get(k, 0)) for k in c_vn if c_vn.get(k, 0) != c_ja.get(k, 0)}
print("diff:", diff)
