# -*- coding: utf-8 -*-
"""Script to replace element content in EN, JA, and KO markdown files cleanly."""
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Import the update dictionaries
from _replace_multilingual import EN_UPDATES, JA_UPDATES, KO_UPDATES

def update_file(path, updates, role_pattern, act_pattern):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out = []
    act = 0
    el_idx = 0
    in_target_loi = False
    target_id = None
    
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        
        # Check Act header
        m_act = re.match(act_pattern, s)
        if m_act:
            act = int(m_act.group(1))
            el_idx = 0
            in_target_loi = False
            out.append(line)
            i += 1
            continue
            
        # Check BGM / SFX / NGHI
        if re.match(r'^\*\*\[(SFX|BGM)\]:\*\*', s) or re.match(r'^\*\*\[(?:Nghỉ|Pause|정지|休止)', s):
            el_idx += 1
            in_target_loi = False
            out.append(line)
            i += 1
            continue
            
        # Check Role header
        m_role = re.match(role_pattern, s)
        if m_role and act > 0:
            el_idx += 1
            cur_id = f"{act}.{el_idx:02d}"
            out.append(line) # output the header
            if cur_id in updates:
                in_target_loi = True
                target_id = cur_id
                # Append the new content
                out.append(updates[cur_id].strip() + '\n\n')
                # Skip original lines until next element header, act header, or delimiter
                i += 1
                while i < len(lines):
                    nxt = lines[i].strip()
                    if (re.match(role_pattern, nxt) or 
                        re.match(r'^\*\*\[(SFX|BGM)\]:\*\*', nxt) or 
                        re.match(r'^\*\*\[(?:Nghỉ|Pause|정지|休止)', nxt) or 
                        re.match(act_pattern, nxt) or 
                        nxt.startswith('---')):
                        break
                    i += 1
                in_target_loi = False
                continue
            else:
                in_target_loi = False
                i += 1
                continue
                
        out.append(line)
        i += 1
        
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(out)
    print(f"Updated: {path}")

# Run update on EN
update_file(
    '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md',
    EN_UPDATES,
    r'^\*\*(?:HOST|INVESTIGATOR|PSYCHOLOGIST|ORDINARY PERSON)\*\*',
    r'^## ACT\s*(\d)'
)

# Run update on JA
update_file(
    '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md',
    JA_UPDATES,
    r'^\*\*(?:ホスト|捜査官|心理学者|一般人)\*\*',
    r'^## 第(\d)幕'
)

# Run update on KO
update_file(
    '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md',
    KO_UPDATES,
    r'^\*\*(?:호스트|수사관|심리학자|일반인)\*\*',
    r'^## 막\s*(\d)'
)
