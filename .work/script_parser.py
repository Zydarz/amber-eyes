# -*- coding: utf-8 -*-
"Parse script into segmented visual beats for each act."
import json, re
from pathlib import Path

def parse_episode_narrative_beats(ep_num):
    path = Path(f01_KICH_BAN/Ho_So_Toi_Pham/Tap{ep_num}/kichban_tap{ep_num}_19112026.md)
    txt = path.read_text(encoding=utf-8)
    acts_raw = re.split(r## HỒI \d.*, txt)[1:]
    
    act_data = []
    for act_idx, a in enumerate(acts_raw, 1):
        lines = [l.strip() for l in a.splitlines() if l.strip() and not l.startswith(**[) and not l.startswith(**) and not l.startswith(#) and not l.startswith(---)]
        act_data.append(lines)
    return act_data

print(Script parser ready.)
