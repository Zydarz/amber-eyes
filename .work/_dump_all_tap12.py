import sys, json

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('.work/script_tap12.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

with open('.work/_all_sentences_tap12.txt', 'w', encoding='utf-8') as out:
    for act in range(1, 6):
        out.write(f"\n=================== HỒI {act} ===================\n")
        for el in elements:
            if el.get('act') == act and 'sentences' in el:
                role = el.get('role', '')
                el_id = el.get('id', '')
                out.write(f"\n--- [{el_id}] {role} ---\n")
                for s_idx, s_obj in enumerate(el['sentences'], 1):
                    if isinstance(s_obj, dict):
                        text = s_obj.get('text', '').strip()
                    else:
                        text = str(s_obj).strip()
                    out.write(f"  {el_id}#{s_idx}: {text}\n")

print("Dumped all 210 sentences to .work/_all_sentences_tap12.txt")
