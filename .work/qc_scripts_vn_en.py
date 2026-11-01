import sys, re
sys.path.append('.work')
from parse_kichban import parse_file

def qc_script(path, lang="VN"):
    print(f"\n==========================================")
    print(f"QC SCRIPT: {path} ({lang})")
    print(f"==========================================")
    
    parsed = parse_file(path)
    total_elements = len(parsed)
    total_sentences = sum(len(x.get('sentences', [])) for x in parsed)
    
    print(f"Elements: {total_elements}")
    print(f"Sentences: {total_sentences}")
    
    # Check forbidden words for VN (V9 / A9.2)
    forbidden_vn = ["máu", "thi thể", "đập tan", "đập loạn", "tự sát", "cắt cổ", "chặt", "bóp cổ"]
    forbidden_en = ["blood", "corpse", "decapitat", "strangl", "suicide"]
    
    hits = []
    unbalanced_quotes = []
    mid_sentence_dots = []
    
    for el in parsed:
        sents = el.get('sentences', [])
        for s in sents:
            sid = s.get('id')
            txt = s.get('text', '')
            
            # Check forbidden
            target_list = forbidden_vn if lang == "VN" else forbidden_en
            for fb in target_list:
                if re.search(r'\b' + re.escape(fb) + r'\b', txt, re.IGNORECASE):
                    hits.append(f"{sid}: forbidden word '{fb}' in '{txt}'")
                    
            # Check mid-sentence dots
            if "..." in txt or "…" in txt:
                mid_sentence_dots.append(f"{sid}: ellipsis in '{txt}'")
                
            # Check quotes balance
            q_straight = txt.count('"')
            q_curly_open = txt.count('“')
            q_curly_close = txt.count('”')
            if q_straight % 2 != 0 or q_curly_open != q_curly_close:
                unbalanced_quotes.append(f"{sid}: unbalanced quotes in '{txt}'")
                
    print(f"Forbidden hits: {len(hits)}")
    for h in hits:
        print(f"  - {h}")
        
    print(f"Ellipsis (G1) hits: {len(mid_sentence_dots)}")
    for d in mid_sentence_dots:
        print(f"  - {d}")
        
    print(f"Unbalanced quote hits: {len(unbalanced_quotes)}")
    for u in unbalanced_quotes:
        print(f"  - {u}")
        
    return len(hits) == 0 and len(mid_sentence_dots) == 0 and len(unbalanced_quotes) == 0

ok_vn = qc_script('01_KICH_BAN/Tap04/kichban_tap04_23102026.md', "VN")
ok_en = qc_script('01_KICH_BAN/Tap04_EN/kichban_tap04_EN.md', "EN")

print(f"\nFinal result: VN={'PASS' if ok_vn else 'FAIL'}, EN={'PASS' if ok_en else 'FAIL'}")
