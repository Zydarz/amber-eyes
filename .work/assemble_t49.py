# -*- coding: utf-8 -*-
import os

header = open('.work/t49_part1.txt', encoding='utf-8').read()
act1 = open('.work/t49_act1.txt', encoding='utf-8').read()
act2 = open('.work/t49_act2.txt', encoding='utf-8').read()
act3 = open('.work/t49_act3.txt', encoding='utf-8').read()
act4 = open('.work/t49_act4.txt', encoding='utf-8').read()
act5 = open('.work/t49_act5.txt', encoding='utf-8').read()

full_text = header + "\n" + act1 + "\n---\n\n" + act2 + "\n---\n\n" + act3 + "\n---\n\n" + act4 + "\n---\n\n" + act5

target_path = '01_KICH_BAN/Ho_So_Toi_Pham/Tap49/kichban_tap49_19112026.md'
with open(target_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f"Successfully assembled {target_path}, length: {len(full_text)} characters.")
