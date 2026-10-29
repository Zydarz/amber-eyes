import os
import sys
import re
import json

sys.stdout.reconfigure(encoding="utf-8")

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KICHBAN_DIR = os.path.join(ROOT, "01_KICH_BAN")

episodes_summary = {}

for ep in range(14, 30):
    ep_dir = os.path.join(KICHBAN_DIR, f"Tap{ep:02d}")
    vn_file = [f for f in os.listdir(ep_dir) if f.startswith("kichban") and not f.endswith("_EN.md") and f.endswith(".md")][0]
    content = open(os.path.join(ep_dir, vn_file), encoding="utf-8").read()

    # Title
    m_title = re.search(r"\*\*Tên tập \(Episode Title\)\*\*\s*\|\s*(.+)", content)
    if not m_title:
        m_title = re.search(r"#\s*KỊCH BẢN CHI TIẾT TẬP\s*\d+:\s*(.+)", content)
    title = m_title.group(1).strip() if m_title else f"Tập {ep}"

    # Theme
    m_theme = re.search(r"\*\*Chủ đề:\*\*\s*(.+)", content)
    if not m_theme:
        m_theme = re.search(r"\*\s*\*\*Chủ đề tâm lý:\*\*\s*(.+)", content)
    theme = m_theme.group(1).strip() if m_theme else ""

    # Split into Acts
    act_matches = list(re.finditer(r"##\s*HỒI\s*(\d+)[:\s]*([^\n]+)", content))
    acts = []
    for i, m in enumerate(act_matches):
        act_num = int(m.group(1))
        act_title = m.group(2).strip()
        start_idx = m.end()
        end_idx = act_matches[i+1].start() if i+1 < len(act_matches) else len(content)
        act_text = content[start_idx:end_idx]
        
        # Extract turns in this act
        turns = re.findall(r"\*\*([A-ZĐ\s]+)\*\*\s*(?:\*\((.*?)\)\*)?:", act_text)
        acts.append({
            "act": act_num,
            "title": act_title,
            "turn_count": len(turns),
            "speakers": [t[0].strip() for t in turns],
            "char_len": len(act_text)
        })

    episodes_summary[ep] = {
        "title": title,
        "theme": theme,
        "acts": acts
    }

print(json.dumps(episodes_summary, ensure_ascii=False, indent=2))
