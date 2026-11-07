import sys, json, re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('.work/script_tap10.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

print("=== KIỂM TRA LẶP TỪ BẤT THƯỜNG / LỖI GÕ PHÍM ===")
for el in elements:
    if 'sentences' in el:
        for s_idx, s_obj in enumerate(el['sentences'], 1):
            if isinstance(s_obj, dict):
                text = s_obj.get('text', '').strip()
                s_id = s_obj.get('id', f"{el['id']}#{s_idx}")
            else:
                text = str(s_obj).strip()
                s_id = f"{el['id']}#{s_idx}"
            
            # Find duplicate consecutive words
            words = text.split()
            for i in range(len(words) - 1):
                w1 = re.sub(r'[^\w\s]', '', words[i]).lower()
                w2 = re.sub(r'[^\w\s]', '', words[i+1]).lower()
                if w1 == w2 and w1:
                    # Filter out natural reduplicated words in Vietnamese:
                    # ngày ngày, người người, từng từng, từ từ, mãi mãi, dần dần, v.v.
                    natural = {'từ', 'mãi', 'ngày', 'người', 'dần', 'chầm', 'lần', 'rất'}
                    if w1 not in natural:
                        print(f"[{s_id}] Lặp từ: '{words[i]} {words[i+1]}' trong câu:\n  {text}\n")
                        
            # Check consecutive syllables with partial match or typing stutter
            # e.g. xé xé, vv
            m = re.findall(r'(\b\w+\b)\s+\1\b', text, re.IGNORECASE)
            for dup in m:
                if dup.lower() not in {'từ', 'mãi', 'ngày', 'người', 'dần', 'chầm', 'lần', 'rất'}:
                    print(f"[{s_id}] Lặp âm: '{dup}' trong câu:\n  {text}\n")
