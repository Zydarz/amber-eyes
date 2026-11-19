# -*- coding: utf-8 -*-
"""
Generate and update all Tap 29 script files to 240 sentences:
1. 01_KICH_BAN/Tap29/kichban_tap29_23102026.md (VN)
2. 01_KICH_BAN/Tap29/kichban_tap29_EN.md (EN)
3. 01_KICH_BAN/Tap29_EN/kichban_tap29_EN.md (EN copy)
4. 01_KICH_BAN/Tap29_JA/kichban_tap29_JA.md (JA)
5. .work/script_tap29.json (VN parsed)
6. .work/script_tap29_JA.json (JA parsed)
"""

import os
import re
import json
import sys

sys.path.append('.work')
from _t29_additions import ADDITIONS

def main():
    vn_ja = json.load(open('.work/_t29_orig_vn_ja.json', encoding='utf-8'))
    en = json.load(open('.work/_t29_orig_en.json', encoding='utf-8'))

    # Build 240-sentence lists for each turn
    turns_data = []
    total_vn = 0
    total_en = 0
    total_ja = 0

    for i, t in enumerate(vn_ja):
        tid = t['id']
        adds = ADDITIONS.get(tid, [])
        cur_vn = list(t['vn'])
        cur_en = list(en[i])
        cur_ja = list(t['ja'])
        for item in adds:
            pos = item['pos']
            cur_vn.insert(pos, item['vn'])
            cur_en.insert(pos, item['en'])
            cur_ja.insert(pos, item['ja'])
        
        assert len(cur_vn) == len(cur_en) == len(cur_ja), f"Mismatch in turn {i} ({tid})"
        turns_data.append({
            'id': tid,
            'act': t['act'],
            'role': t['role'],
            'vn': cur_vn,
            'en': cur_en,
            'ja': cur_ja
        })
        total_vn += len(cur_vn)
        total_en += len(cur_en)
        total_ja += len(cur_ja)

    print(f"Total sentences across 32 turns: VN={total_vn}, EN={total_en}, JA={total_ja}")
    assert total_vn == 240, f"Expected 240, got {total_vn}"

    # 1. Update 01_KICH_BAN/Tap29/kichban_tap29_23102026.md
    update_vn_script(turns_data)

    # 2. Update 01_KICH_BAN/Tap29/kichban_tap29_EN.md & Tap29_EN
    update_en_script(turns_data)

    # 3. Update 01_KICH_BAN/Tap29_JA/kichban_tap29_JA.md
    update_ja_script(turns_data)

    # 4. Update .work/script_tap29.json
    update_script_json('.work/script_tap29.json', turns_data, 'vn')

    # 5. Update .work/script_tap29_JA.json
    update_script_json('.work/script_tap29_JA.json', turns_data, 'ja')

    print("ALL FILES SUCCESSFULLY UPDATED TO 240 SENTENCES!")

def update_vn_script(turns_data):
    src_path = '01_KICH_BAN/Tap29/kichban_tap29_23102026.md'
    lines = open(src_path, encoding='utf-8').read().splitlines()

    new_lines = []
    turn_idx = 0
    in_turn = False

    for line in lines:
        strip_l = line.strip()
        # Header replacements
        if 'Tổng: đúng 165 câu' in line:
            line = line.replace('Tổng: đúng 165 câu', 'Tổng: đúng 240 câu')
            line = line.replace('Host: 95 câu, D: 28 câu, C: 27 câu, N: 15 câu', 'Host: 137 câu, D: 37 câu, C: 51 câu, N: 15 câu')
        if '| **H** | **Dẫn chuyện (Host)** |' in line:
            new_lines.append('| **H** | **Dẫn chuyện (Host)** | Amber Eyes Voice | Trầm ấm, kịch tính, sắc sảo, dẫn dắt nhân văn sâu sắc | **137** |')
            continue
        if '| **D** | **Điều tra viên** |' in line:
            new_lines.append('| **D** | **Điều tra viên** | Điều tra viên kể lại hồ sơ (không nhập vai Thám tử Patrick Kennedy — K3) | Nam trung niên, điềm tĩnh, dày dạn kinh nghiệm, sắc bén | **37** |')
            continue
        if '| **C** | **Chuyên gia Tâm lý** |' in line:
            new_lines.append('| **C** | **Chuyên gia Tâm lý** | Bác sĩ Tâm thần học Pháp y & Tâm lý học Tội phạm | Điềm đạm, khách quan, giàu hàm lượng khoa học hành vi | **51** |')
            continue
        if '| **TỔNG** | **Toàn bộ kịch bản** |' in line:
            new_lines.append('| **TỔNG** | **Toàn bộ kịch bản** | **5 Hồi chuẩn A2c/K10** | **Cân bằng hoàn hảo theo Golden Benchmark** | **240** |')
            continue

        if strip_l.startswith('**HOST** *(') or strip_l.startswith('**ĐIỀU TRA VIÊN** *(') or strip_l.startswith('**CHUYÊN GIA TÂM LÝ** *(') or strip_l.startswith('**NGƯỜI BÌNH THƯỜNG** *('):
            new_lines.append(line)
            # Insert all sentences for this turn
            for s in turns_data[turn_idx]['vn']:
                new_lines.append(s)
            turn_idx += 1
            in_turn = True
            continue

        if in_turn:
            if strip_l == '' or strip_l.startswith('**[') or strip_l.startswith('##') or strip_l.startswith('---'):
                in_turn = False
                new_lines.append(line)
            # otherwise it was an old sentence line, skip it
            continue

        new_lines.append(line)

    assert turn_idx == 32, f"Expected 32 turns, got {turn_idx}"
    out_content = '\n'.join(new_lines) + '\n'
    open(src_path, 'w', encoding='utf-8').write(out_content)
    print(f"Updated {src_path} (lines: {len(new_lines)})")

def update_en_script(turns_data):
    src_path = '01_KICH_BAN/Tap29/kichban_tap29_EN.md'
    lines = open(src_path, encoding='utf-8').read().splitlines()

    new_lines = []
    turn_idx = 0
    in_turn = False

    for line in lines:
        strip_l = line.strip()
        if 'Total: exactly 165 sentences' in line:
            line = line.replace('Total: exactly 165 sentences', 'Total: exactly 240 sentences')
            line = line.replace('Host: 95 sentences, D: 28 sentences, C: 27 sentences, N: 15 sentences', 'Host: 137 sentences, D: 37 sentences, C: 51 sentences, N: 15 sentences')
        if '| **H** | **Narrator (Host)** |' in line:
            new_lines.append('| **H** | **Narrator (Host)** | Amber Eyes Voice | Warm, dramatic, incisive, leading with deep humanity | **137** |')
            continue
        if '| **D** | **Investigator** |' in line:
            new_lines.append('| **D** | **Investigator** | Case officer recounting the Milwaukee file (third-person per K3) | Middle-aged male, calm, seasoned, incisive | **37** |')
            continue
        if '| **C** | **Psychologist** |' in line:
            new_lines.append('| **C** | **Psychologist** | Forensic Psychiatrist & Criminal Psychologist | Composed, objective, rich in behavioral science insights | **51** |')
            continue
        if '| **TOTAL** | **Entire Script** |' in line:
            new_lines.append('| **TOTAL** | **Entire Script** | **5 Acts A2c/K10** | **Balanced per Golden Benchmark** | **240** |')
            continue

        if strip_l.startswith('**HOST** *(') or strip_l.startswith('**INVESTIGATOR** *(') or strip_l.startswith('**PSYCHOLOGIST** *(') or strip_l.startswith('**ORDINARY PERSON** *('):
            new_lines.append(line)
            # Insert all sentences for this turn
            for s in turns_data[turn_idx]['en']:
                new_lines.append(s)
            turn_idx += 1
            in_turn = True
            continue

        if in_turn:
            if strip_l == '' or strip_l.startswith('**[') or strip_l.startswith('##') or strip_l.startswith('---'):
                in_turn = False
                new_lines.append(line)
            # skip old sentences
            continue

        new_lines.append(line)

    assert turn_idx == 32, f"Expected 32 turns in EN, got {turn_idx}"
    out_content = '\n'.join(new_lines) + '\n'
    open(src_path, 'w', encoding='utf-8').write(out_content)
    open('01_KICH_BAN/Tap29_EN/kichban_tap29_EN.md', 'w', encoding='utf-8').write(out_content)
    print(f"Updated {src_path} and Tap29_EN copy (lines: {len(new_lines)})")

def update_ja_script(turns_data):
    src_path = '01_KICH_BAN/Tap29_JA/kichban_tap29_JA.md'
    lines = open(src_path, encoding='utf-8').read().splitlines()

    new_lines = []
    turn_idx = 0
    in_turn = False

    for line in lines:
        strip_l = line.strip()
        if '合計：正確に165文' in line:
            line = line.replace('合計：正確に165文', '合計：正確に240文')
            line = line.replace('Host：95文、D：28文、C：27文、N：15文', 'Host：137文、D：37文、C：51文、N：15文')
        if '| **H** | **進行役 (Host)** |' in line:
            new_lines.append('| **H** | **進行役 (Host)** | Amber Eyes Voice | 低く温かみがあり、ドラマチックで鋭く、人間味深く導く | **137** |')
            continue
        if '| **D** | **捜査官** |' in line:
            new_lines.append('| **D** | **捜査官** | ミルウォーキー事件記録を語る捜査官 (K3に従い、ケネディ捜査官へのなりきりはしない) | 中年男性、沈着冷静、経験豊富で鋭利 | **37** |')
            continue
        if '| **C** | **心理専門家** |' in line:
            new_lines.append('| **C** | **心理専門家** | 司法精神科医 & 犯罪心理学者 | 落ち着いて客観的、行動科学の知見に富む | **51** |')
            continue
        if '| **合計** | **脚本全体** |' in line:
            new_lines.append('| **合計** | **脚本全体** | **A2c/K10標準5幕** | **ゴールデンベンチマークに完全合致** | **240** |')
            continue

        if any(strip_l.startswith(p) for p in ('**ホスト**', '**捜査官**', '**心理学者**', '**心理専門家**', '**一般人**')):
            new_lines.append(line)
            # Insert all sentences for this turn
            for s in turns_data[turn_idx]['ja']:
                new_lines.append(s)
            turn_idx += 1
            in_turn = True
            continue

        if in_turn:
            if strip_l == '' or strip_l.startswith('**[') or strip_l.startswith('##') or strip_l.startswith('---'):
                in_turn = False
                new_lines.append(line)
            # skip old sentences
            continue

        new_lines.append(line)

    assert turn_idx == 32, f"Expected 32 turns in JA, got {turn_idx}"
    out_content = '\n'.join(new_lines) + '\n'
    open(src_path, 'w', encoding='utf-8').write(out_content)
    print(f"Updated {src_path} (lines: {len(new_lines)})")

def update_script_json(json_path, turns_data, lang_key):
    data = json.load(open(json_path, encoding='utf-8'))
    turn_map = {t['id']: t for t in turns_data}

    total_sents = 0
    for elem in data:
        if elem.get('kind') == 'LOI':
            eid = elem['id']
            tinfo = turn_map[eid]
            sents_list = []
            for s_idx, stext in enumerate(tinfo[lang_key]):
                sid = f"{eid}#{s_idx + 1}"
                words = len(stext.split()) if lang_key != 'ja' else 1
                sents_list.append({
                    'id': sid,
                    'text': stext,
                    'words': words
                })
            elem['sentences'] = sents_list
            total_sents += len(sents_list)

    print(f"Updated {json_path}: Total LOI sentences = {total_sents}")
    assert total_sents == 240, f"Expected 240 in {json_path}, got {total_sents}"
    json.dump(data, open(json_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)

if __name__ == '__main__':
    main()
