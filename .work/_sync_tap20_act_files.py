# -*- coding: utf-8 -*-
"""Sync tap20_act*.py and build_tap20_all.py with current 241-sentence scripts."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"

SCRIPTS = {
    "VN": json.loads((WORK / "script_tap20.json").read_text(encoding="utf-8")),
    "EN": json.loads((WORK / "script_tap20_EN.json").read_text(encoding="utf-8")),
    "JA": json.loads((WORK / "script_tap20_JA.json").read_text(encoding="utf-8")),
    "KO": json.loads((WORK / "script_tap20_KO.json").read_text(encoding="utf-8")),
}

ACT_ELEMENTS = {act: {} for act in range(1, 6)}

# Map role codes to full role name for generator compatibility
ROLE_NAMES = {
    "VN": {"H": "HOST", "D": "ĐIỀU TRA VIÊN", "C": "CHUYÊN GIA TÂM LÝ", "N": "NGƯỜI BÌNH THƯỜNG"},
    "EN": {"H": "HOST", "D": "DETECTIVE", "C": "PSYCHOLOGIST", "N": "PERSON INVOLVED"},
    "JA": {"H": "ホスト", "D": "捜査官", "C": "心理学者", "N": "一般人"},
    "KO": {"H": "진행자", "D": "수사관", "C": "프로파일러", "N": "일반인"},
}

for lang, elements in SCRIPTS.items():
    for el in elements:
        act = int(el["id"].split(".")[0])
        if lang not in ACT_ELEMENTS[act]:
            ACT_ELEMENTS[act][lang] = []
        
        kind = el["kind"]
        if kind in ("BGM", "SFX"):
            desc = el.get("desc", "").strip("*")
            ACT_ELEMENTS[act][lang].append((kind, desc))
        elif kind == "LOI":
            role_code = el.get("role", "H")
            role_name = ROLE_NAMES[lang].get(role_code, role_code)
            direction = el.get("direction", "")
            sents = [s["text"] for s in el["sentences"]]
            ACT_ELEMENTS[act][lang].append(("LOI", role_name, direction, sents))

# Write tap20_act1.py to tap20_act5.py
for act in range(1, 6):
    act_file = WORK / f"tap20_act{act}.py"
    lines = [
        "# -*- coding: utf-8 -*-",
        f'"""Act {act} data for Episode 20 (241 sentences across VN, EN, JA, KO)."""',
        "",
    ]
    for lang in ["VN", "EN", "JA", "KO"]:
        var_name = f"ACT{act}_{lang}"
        lines.append(f"{var_name} = [")
        for item in ACT_ELEMENTS[act][lang]:
            if item[0] in ("BGM", "SFX"):
                kind, txt = item
                lines.append(f'    ({json.dumps(kind, ensure_ascii=False)}, {json.dumps(txt, ensure_ascii=False)}),')
            else:
                kind, role, sdir, sents = item
                lines.append(f'    ({json.dumps(kind, ensure_ascii=False)}, {json.dumps(role, ensure_ascii=False)}, {json.dumps(sdir, ensure_ascii=False)}, [')
                for s in sents:
                    lines.append(f'        {json.dumps(s, ensure_ascii=False)},')
                lines.append("    ]),")
        lines.append("]")
        lines.append("")
    
    act_file.write_text("\n".join(lines), encoding="utf-8")
    print(f"Updated {act_file.name}")

# Now update build_tap20_all.py headers
bld_file = WORK / "build_tap20_all.py"
content = bld_file.read_text(encoding="utf-8")
content = content.replace("212 sentences", "241 sentences")
content = content.replace("212 câu thoại", "241 câu thoại")
content = content.replace("212文", "241文")
content = content.replace("212개 발화 문장", "241개 발화 문장")
content = content.replace("212", "241")

bld_file.write_text(content, encoding="utf-8")
print("Updated build_tap20_all.py")
