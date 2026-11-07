# -*- coding: utf-8 -*-
"""
Comprehensive spellcheck and typographical audit for Episode 09 across all 4 languages:
- Vietnamese (VN): 01_KICH_BAN/Tap09/kichban_tap09_23102026.md
- English (EN): 01_KICH_BAN/Tap09_EN/kichban_tap09_EN.md
- Japanese (JA): 01_KICH_BAN/Tap09_JA/kichban_tap09_JA.md
- Korean (KO): 01_KICH_BAN/Tap09_KO/kichban_tap09_KO.md
- Descriptions & Metadata: 02_SAN_XUAT/Tap09/ and .work/edition.py
"""

import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / ".work"))
import parse_kichban as PK

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

def audit_file(lang, path):
    print(f"\n{'='*60}\nAUDITING {lang}: {path.name}\n{'='*60}")
    content = path.read_text(encoding="utf-8")
    parsed = PK.parse_file(str(path))
    loi_elements = [e for e in parsed if e["kind"] == "LOI"]
    
    issues = []
    
    # 1. Bracket & Quote symmetry
    pairs = [("(", ")"), ("[", "]"), ("{", "}")]
    for l_sym, r_sym in pairs:
        c_l = content.count(l_sym)
        c_r = content.count(r_sym)
        if c_l != c_r:
            issues.append(("BRACKET_ASYMMETRY", f"Mismatch '{l_sym}' ({c_l}) != '{r_sym}' ({c_r})"))
            
    # Check quotes
    if lang in ["VN", "EN"]:
        c_dq = content.count('"')
        if c_dq % 2 != 0:
            issues.append(("QUOTE_ASYMMETRY", f"Odd number of straight double quotes: {c_dq}"))
        c_open_curly = content.count('“')
        c_close_curly = content.count('”')
        if c_open_curly != c_close_curly:
            issues.append(("QUOTE_ASYMMETRY", f"Curly quotes mismatch: “ ({c_open_curly}) != ” ({c_close_curly})"))
    elif lang == "JA":
        c_lq = content.count('「')
        c_rq = content.count('」')
        if c_lq != c_rq:
            issues.append(("QUOTE_ASYMMETRY", f"Japanese quotes mismatch: 「 ({c_lq}) != 」 ({c_rq})"))
    elif lang == "KO":
        c_lq = content.count('‘')
        c_rq = content.count('’')
        if c_lq != c_rq:
            issues.append(("QUOTE_ASYMMETRY", f"Korean quotes mismatch: ‘ ({c_lq}) != ’ ({c_rq})"))
            
    # 2. Sentence-level audit
    all_sentences = []
    for elem in loi_elements:
        for s in elem["sentences"]:
            sid = s["id"]
            txt = s["text"]
            all_sentences.append((sid, txt))
            
            # Check double spaces
            if "  " in txt:
                issues.append(("DOUBLE_SPACE", f"{sid}: Double space found in '{txt}'"))
                
            # Check trailing space before punctuation
            if re.search(r'\s+[,.;:!?]', txt):
                issues.append(("SPACE_BEFORE_PUNCT", f"{sid}: Space before punctuation in '{txt}'"))
                
            # Check starting with lowercase (except numbers/quotes)
            trimmed = txt.strip()
            # strip leading quotes or punctuation
            first_char = re.sub(r'^[\"“‘\'\[\(]+', '', trimmed)
            if first_char and first_char[0].isalpha() and first_char[0].islower():
                issues.append(("LOWERCASE_START", f"{sid}: Starts with lowercase: '{txt}'"))
                
            # Check ending punctuation
            if lang in ["VN", "EN"]:
                if not re.search(r'[\.!\?\"\'”’\)]$', trimmed):
                    issues.append(("NO_ENDING_PUNCT", f"{sid}: Missing ending punctuation in '{txt}'"))
            elif lang == "JA":
                if not re.search(r'[。！？）]$', trimmed):
                    issues.append(("NO_ENDING_PUNCT", f"{sid}: JA missing ending punctuation (。) in '{txt}'"))
            elif lang == "KO":
                if not re.search(r'[\.!\?’\)]$', trimmed):
                    issues.append(("NO_ENDING_PUNCT", f"{sid}: KO missing ending punctuation (.) in '{txt}'"))
                    
            # Check for ellipsis in spoken text (Rule G1)
            if "..." in txt or "…" in txt:
                issues.append(("ELLIPSIS_G1", f"{sid}: Contains ellipsis: '{txt}'"))
                
            # Check for raw markdown formatting leaked into spoken text
            if any(md in txt for md in ["**", "##", "__", "```"]):
                issues.append(("RAW_MARKDOWN", f"{sid}: Raw markdown syntax in spoken text: '{txt}'"))

    # 3. Repeated words check
    if lang in ["VN", "EN"]:
        for sid, txt in all_sentences:
            words = re.findall(r'\b[a-zA-ZàáảãạăằắẳẵặâầấẩẫậèéẻẽẹêềếểễệìíỉĩịòóỏõọôồốổỗộơờớởỡợùúủũụưừứửữựỳýỷỹỵđĐ]+\b', txt)
            for i in range(len(words)-1):
                w1 = words[i].lower()
                w2 = words[i+1].lower()
                if w1 == w2 and len(w1) > 2:
                    # check legitimate reduplications in Vietnamese
                    legit_vn = {"ngày ngày", "từng từng", "năm năm", "người người", "nhà nhà", "lớp lớp", "đoàn đoàn"}
                    phrase = f"{w1} {w2}"
                    if phrase not in legit_vn:
                        issues.append(("REPEATED_WORD", f"{sid}: Repeated word '{w1} {w2}' in: '{txt}'"))

    print(f"Total sentences audited: {len(all_sentences)}")
    print(f"Total issues found: {len(issues)}")
    for cat, desc in issues:
        print(f"  [{cat}] {desc}")
        
    return issues, all_sentences

def audit_vietnamese_spelling(all_sentences):
    print(f"\n{'='*60}\nDEEP VIETNAMESE LEXICAL & SPELLING SCAN\n{'='*60}")
    
    # Common Vietnamese spelling confusion patterns:
    # tr vs ch, s vs x, d vs gi vs r, c/k/q, hỏi vs ngã
    # Let's inspect words and check for common spelling traps
    typo_candidates = []
    
    # Predefined known typos in Vietnamese
    known_typos = {
        "xơ suất": "sơ suất",
        "sơ xuất": "sơ suất",
        "xơ xuất": "sơ suất",
        "xắp xếp": "sắp xếp",
        "chia sẻ": "chia sẻ",
        "chia xẻ": "chia sẻ",
        "suất sắc": "xuất sắc",
        "dấu diếm": "giấu giếm",
        "dấu giếm": "giấu giếm",
        "giấu diếm": "giấu giếm",
        "dàn dựng": "dàn dựng",
        "giàn dựng": "dàn dựng",
        "giành giật": "giành giật",
        "dành giật": "giành giật",
        "lãng mạng": "lãng mạn",
        "bàng hoàng": "bàng hoàng",
        "bàng hoang": "bàng hoàng",
        "chân thực": "chân thực",
        "chân thật": "chân thật",
        "hoang tưởng": "hoang tưởng",
        "hoan tưởng": "hoang tưởng",
        "phi nhân tính": "phi nhân tính",
        "khuyết tật": "khuyết tật",
        "ám ảnh": "ám ảnh",
        "bản ngã": "bản ngã",
        "bản ngả": "bản ngã",
        "tẩy não": "tẩy não",
        "thao túng": "thao túng",
        "ngụy biện": "ngụy biện",
        "nguỵ biện": "ngụy biện",
        "kịch tính": "kịch tính",
        "kịch nghệ": "kịch nghệ",
        "chủ mưu": "chủ mưu",
        "trực tiếp": "trực tiếp",
        "gián tiếp": "gián tiếp",
        "thảm kịch": "thảm kịch",
        "thảm sát": "thảm sát",
        "xác lập": "xác lập",
        "sác lập": "xác lập",
        "phán quyết": "phán quyết",
        "tư pháp": "tư pháp",
        "lương tri": "lương tri",
        "lương tâm": "lương tâm",
    }
    
    # Common proper nouns whitelist
    proper_nouns_vn = {
        "Charles", "Manson", "Sharon", "Tate", "Roman", "Polanski",
        "Terry", "Melcher", "Vincent", "Bugliosi", "Susan", "Atkins",
        "Patricia", "Krenwinkel", "Leslie", "Van", "Houten", "Tex", "Watson",
        "Linda", "Kasabian", "Bernard", "Crowe", "Gary", "Hinman",
        "Jay", "Sebring", "Abigail", "Folger", "Wojciech", "Frykowski",
        "Steven", "Parent", "Leno", "Rosemary", "LaBianca", "Spahn", "Ranch",
        "Death", "Valley", "Barker", "Cielo", "Drive", "Waverly",
        "Los", "Angeles", "California", "Beverly", "Hills",
        "George", "Older", "Anderson", "Corcoran", "Gavin", "Becker",
        "The", "Beatles", "Helter", "Skelter", "White", "Album",
        "PIG", "RISE", "HEALTER", "SKELTER", "LSD", "Sykes", "Matza",
        "Love", "Bombing", "Creepy", "Crawling", "Gift", "Fear",
        "Host", "Cú", "Sói", "Cáo", "Cừu", "Mèo"
    }
    
    word_freq = {}
    suspicious_words = []
    
    for sid, txt in all_sentences:
        # Check known typos in txt
        for typo, correct in known_typos.items():
            if re.search(r'\b' + re.escape(typo) + r'\b', txt, re.IGNORECASE):
                if typo != correct:
                    typo_candidates.append((sid, f"Found '{typo}' (should be '{correct}')", txt))
                    
        # Tokenize words
        raw_words = re.findall(r'\b[\w\-]+\b', txt)
        for w in raw_words:
            if not w.isdigit():
                word_freq[w] = word_freq.get(w, 0) + 1
                
    print(f"Total unique words scanned in VN: {len(word_freq)}")
    print(f"Known typo matches: {len(typo_candidates)}")
    for sid, msg, txt in typo_candidates:
        print(f"  {sid}: {msg}")
        
    return typo_candidates

def audit_descriptions():
    print(f"\n{'='*60}\nAUDITING DESCRIPTIONS & METADATA\n{'='*60}")
    desc_files = [
        ROOT / "02_SAN_XUAT" / "Tap09" / "mo_ta.txt",
        ROOT / "02_SAN_XUAT" / "Tap09_EN" / "mo_ta.txt",
        ROOT / "02_SAN_XUAT" / "Tap09_JA" / "mo_ta.txt",
        ROOT / "02_SAN_XUAT" / "Tap09_KO" / "mo_ta.txt",
        ROOT / "02_SAN_XUAT" / "Tap09_EN" / "CHU_CO_DINH_EN.md",
    ]
    
    for p in desc_files:
        if not p.exists():
            print(f"MISSING: {p}")
            continue
        txt = p.read_text(encoding="utf-8")
        print(f"{p.name} ({p.parent.name}): length = {len(txt)} chars")
        if "mo_ta.txt" in p.name:
            if len(txt) > 5000:
                print(f"  [ERROR] Exceeds 5000 chars limit: {len(txt)}")
            else:
                print(f"  [OK] Under 5000 chars limit.")
                
        # Check double spaces
        d_sp = txt.count("  ")
        if d_sp > 0:
            print(f"  [NOTE] {d_sp} double spaces found in {p.name}")

def main():
    files = [
        ("VN", ROOT / "01_KICH_BAN" / "Tap09" / "kichban_tap09_23102026.md"),
        ("EN", ROOT / "01_KICH_BAN" / "Tap09_EN" / "kichban_tap09_EN.md"),
        ("JA", ROOT / "01_KICH_BAN" / "Tap09_JA" / "kichban_tap09_JA.md"),
        ("KO", ROOT / "01_KICH_BAN" / "Tap09_KO" / "kichban_tap09_KO.md"),
    ]
    
    all_issues = {}
    vn_sentences = []
    
    for lang, path in files:
        issues, sents = audit_file(lang, path)
        all_issues[lang] = issues
        if lang == "VN":
            vn_sentences = sents
            
    vn_typos = audit_vietnamese_spelling(vn_sentences)
    audit_descriptions()
    
    print("\n" + "="*60)
    print("FINAL SUMMARY REPORT")
    print("="*60)
    total_issues = sum(len(v) for v in all_issues.values()) + len(vn_typos)
    print(f"Total issues across all files: {total_issues}")
    if total_issues == 0:
        print(">>> 100% CLEAN - ZERO SPELLING, PUNCTUATION OR FORMATTING DEFECTS FOUND! <<<")

if __name__ == "__main__":
    main()
