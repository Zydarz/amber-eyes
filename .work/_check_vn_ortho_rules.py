# -*- coding: utf-8 -*-
"""Check Vietnamese orthographic spelling rules on all vocabulary."""
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('.work/_vn_vocab_tap10.txt', 'r', encoding='utf-8') as f:
    words = [line.strip() for line in f if line.strip()]

# Mapping accented vowels to their base letter
base_map = {
    'a': 'a', 'à': 'a', 'á': 'a', 'ả': 'a', 'ã': 'a', 'ạ': 'a',
    'ă': 'ă', 'ằ': 'ă', 'ắ': 'ă', 'ẳ': 'ă', 'ẵ': 'ă', 'ặ': 'ă',
    'â': 'â', 'ầ': 'â', 'ấ': 'â', 'ẩ': 'â', 'ẫ': 'â', 'ậ': 'â',
    'e': 'e', 'è': 'e', 'é': 'e', 'ẻ': 'e', 'ẽ': 'e', 'ẹ': 'e',
    'ê': 'ê', 'ề': 'ê', 'ế': 'ê', 'ể': 'ê', 'ễ': 'ê', 'ệ': 'ê',
    'i': 'i', 'ì': 'i', 'í': 'i', 'ỉ': 'i', 'ĩ': 'i', 'ị': 'i',
    'o': 'o', 'ò': 'o', 'ó': 'o', 'ỏ': 'o', 'õ': 'o', 'ọ': 'o',
    'ô': 'ô', 'ồ': 'ô', 'ố': 'ô', 'ổ': 'ô', 'ỗ': 'ô', 'ộ': 'ô',
    'ơ': 'ơ', 'ờ': 'ơ', 'ớ': 'ơ', 'ở': 'ơ', 'ỡ': 'ơ', 'ợ': 'ơ',
    'u': 'u', 'ù': 'u', 'ú': 'u', 'ủ': 'u', 'ũ': 'u', 'ụ': 'u',
    'ư': 'ư', 'ừ': 'ư', 'ứ': 'ư', 'ử': 'ư', 'ữ': 'ư', 'ự': 'ư',
    'y': 'y', 'ỳ': 'y', 'ý': 'y', 'ỷ': 'y', 'ỹ': 'y', 'ỵ': 'y',
}

rule_errors = []

for w in words:
    low = w.lower()
    # convert accented characters to base
    base = "".join(base_map.get(c, c) for c in low)
    
    # Rule 1: c followed by e, ê, i, y (should be k)
    if re.search(r'\bc[eêiy]', base):
        rule_errors.append((w, "Chữ 'c' đi với e, ê, i, y (phải là k)"))
        
    # Rule 2: k followed by a, ă, â, o, ô, ơ, u, ư (should be c)
    # (except loanwords or proper names)
    if re.search(r'\bk[aăâoôơuư]', base):
        rule_errors.append((w, "Chữ 'k' đi với a, ă, â, o, ô, ơ, u, ư (phải là c)"))
        
    # Rule 3: g followed by e, ê, i, y (should be gh, except 'gi' which is initial 'gi')
    if re.search(r'\bg[eêy]', base):
        rule_errors.append((w, "Chữ 'g' đi với e, ê, y (phải là gh)"))
    # check 'gi' followed by consonant
    if re.search(r'\bgi[^aăâeêioôơuưy]', base):
        rule_errors.append((w, "'gi' không có nguyên âm theo sau"))
        
    # Rule 4: gh followed by a, ă, â, o, ô, ơ, u, ư (should be g)
    if re.search(r'\bgh[aăâoôơuư]', base):
        rule_errors.append((w, "Chữ 'gh' đi với a, ă, â, o, ô, ơ, u, ư (phải là g)"))
        
    # Rule 5: ng followed by e, ê, i, y (should be ngh)
    if re.search(r'\bng[eêiy]', base):
        rule_errors.append((w, "Chữ 'ng' đi với e, ê, i, y (phải là ngh)"))
        
    # Rule 6: ngh followed by a, ă, â, o, ô, ơ, u, ư (should be ng)
    if re.search(r'\bngh[aăâoôơuư]', base):
        rule_errors.append((w, "Chữ 'ngh' đi với a, ă, â, o, ô, ơ, u, ư (phải là ng)"))
        
    # Rule 7: qu without vowel
    if re.search(r'\bqu[^aăâeêioôơuưy]', base):
        rule_errors.append((w, "'qu' không có nguyên âm theo sau"))

print(f"Số lỗi vi phạm quy tắc chính tả cơ bản: {len(rule_errors)}")
for re_err in rule_errors:
    print(f"  {re_err[0]}: {re_err[1]}")
