# -*- coding: utf-8 -*-
"""Validate every Vietnamese syllable against phonetic and orthographic rules."""
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

p = PK.parse_file('01_KICH_BAN/Tap10/kichban_tap10_23102026.md')
loi = [e for e in p if e['kind'] == 'LOI']

words = set()
for e in loi:
    for s in e['sentences']:
        tokens = re.findall(r'[^\s.,:;?!"“”()\'’/\\–-]+', s['text'])
        for t in tokens:
            if not t.isdigit():
                words.add(t)

known_terms = {
    'Colleen', 'Stan', 'Cameron', 'Hooker', 'Janice', 'Red', 'Bluff', 'Westwood', 'Eugene',
    'Riverside', 'Tehama', 'The', 'Company', 'Martin', 'Seligman', 'Patrick', 'Carnes',
    'Chris', 'Hatcher', 'Clarence', 'Knight', 'Richard', 'Tedeschi', 'Lawrence', 'Calhoun',
    'Gavin', 'de', 'Becker', 'Gifts', 'of', 'Life', 'Gift', 'Fear', 'Amber', 'Eyes', 'BGM',
    'California', 'Sykes', 'Matza', 'Compartmentalization', 'Growth', 'Sheriff’s', 'Office',
    'Post-Traumatic', 'Stockholm', 'Trauma', 'Bonding', 'Simple', 'County'
}

vn_words = sorted([w for w in words if w not in known_terms])

# Normalize diacritics to check syllable structure
# Mapping of accented vowels to base vowel + tone
accents = {
    'á': ('a', 'sắc'), 'à': ('a', 'huyền'), 'ả': ('a', 'hỏi'), 'ã': ('a', 'ngã'), 'ạ': ('a', 'nặng'),
    'ắ': ('ă', 'sắc'), 'ằ': ('ă', 'huyền'), 'ẳ': ('ă', 'hỏi'), 'ẵ': ('ă', 'ngã'), 'ặ': ('ă', 'nặng'),
    'ấ': ('â', 'sắc'), 'ầ': ('â', 'huyền'), 'ẩ': ('â', 'hỏi'), 'ẫ': ('â', 'ngã'), 'ậ': ('â', 'nặng'),
    'é': ('e', 'sắc'), 'è': ('e', 'huyền'), 'ẻ': ('e', 'hỏi'), 'ẽ': ('e', 'ngã'), 'ẹ': ('e', 'nặng'),
    'ế': ('ê', 'sắc'), 'ề': ('ê', 'huyền'), 'ể': ('ê', 'hỏi'), 'ễ': ('ê', 'ngã'), 'ệ': ('ê', 'nặng'),
    'í': ('i', 'sắc'), 'ì': ('i', 'huyền'), 'ỉ': ('i', 'hỏi'), 'ĩ': ('i', 'ngã'), 'ị': ('i', 'nặng'),
    'ó': ('o', 'sắc'), 'ò': ('o', 'huyền'), 'ỏ': ('o', 'hỏi'), 'õ': ('o', 'ngã'), 'ọ': ('o', 'nặng'),
    'ố': ('ô', 'sắc'), 'ồ': ('ô', 'huyền'), 'ổ': ('ô', 'hỏi'), 'ỗ': ('ô', 'ngã'), 'ộ': ('ô', 'nặng'),
    'ớ': ('ơ', 'sắc'), 'ờ': ('ơ', 'huyền'), 'ở': ('ơ', 'hỏi'), 'ỡ': ('ơ', 'ngã'), 'ợ': ('ơ', 'nặng'),
    'ú': ('u', 'sắc'), 'ù': ('u', 'huyền'), 'ủ': ('u', 'hỏi'), 'ũ': ('u', 'ngã'), 'ụ': ('u', 'nặng'),
    'ứ': ('ư', 'sắc'), 'ừ': ('ư', 'huyền'), 'ử': ('ư', 'hỏi'), 'ữ': ('ư', 'ngã'), 'ự': ('ư', 'nặng'),
    'ý': ('y', 'sắc'), 'ỳ': ('y', 'huyền'), 'ỷ': ('y', 'hỏi'), 'ỹ': ('y', 'ngã'), 'ỵ': ('y', 'nặng'),
}

# Legal initial consonants
valid_inits = {'', 'b', 'c', 'ch', 'd', 'đ', 'g', 'gh', 'gi', 'h', 'k', 'kh', 'l', 'm', 'n', 'ng', 'ngh', 'nh', 'p', 'ph', 'qu', 'r', 's', 't', 'th', 'tr', 'v', 'x'}
# Legal codas
valid_codas = {'', 'c', 'ch', 'm', 'n', 'ng', 'nh', 'p', 't', 'i', 'y', 'u', 'o'}

# Legal stop codas (c, ch, p, t) ONLY take sắc or nặng
stop_codas = {'c', 'ch', 'p', 't'}

tone_violations = []

for w in vn_words:
    low = w.lower()
    # Check stop coda with non-(sắc, nặng) tone
    # Strip tones
    base_chars = []
    tones_in_word = []
    for char in low:
        if char in accents:
            base_chars.append(accents[char][0])
            tones_in_word.append(accents[char][1])
        else:
            base_chars.append(char)
            
    base_w = "".join(base_chars)
    
    # Check if multiple different tones
    unique_tones = set(tones_in_word)
    if len(unique_tones) > 1:
        tone_violations.append((w, f"Nhiều thanh điệu trong cùng 1 âm tiết: {unique_tones}"))
        
    word_tone = tones_in_word[0] if tones_in_word else 'ngang'
    
    # Check stop coda
    for sc in ['ch', 'ng', 'nh']:
        if base_w.endswith(sc):
            if sc in ['ch'] and word_tone not in ['sắc', 'nặng']:
                tone_violations.append((w, f"Đuôi '{sc}' chỉ đi với sắc hoặc nặng, nhưng mang thanh '{word_tone}'"))
            break
    else:
        for sc in ['c', 'p', 't']:
            if base_w.endswith(sc) and word_tone not in ['sắc', 'nặng']:
                tone_violations.append((w, f"Đuôi '{sc}' chỉ đi với sắc hoặc nặng, nhưng mang thanh '{word_tone}'"))

print(f"Lỗi thanh điệu phát hiện: {len(tone_violations)}")
for tv in tone_violations:
    print(f"  {tv[0]}: {tv[1]}")
