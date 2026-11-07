import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/_tap10_sentences.json', 'r', encoding='utf-8') as f:
    raw_sentences = json.load(f)

text_corpus = []
for item in raw_sentences:
    sid = item['text']['id']
    txt = item['text']['text']
    text_corpus.append((sid, txt))

# Patterns to inspect
checks = [
    ('giằng xé', r'giằng\s+xé'),
    ('xé nát', r'xé\s+nát'),
    ('sơ suất', r'sơ\s+suất'),
    ('sơ xuất', r'sơ\s+xuất'),
    ('chẩn đoán', r'chẩn\s+đoán'),
    ('chuẩn đoán', r'chuẩn\s+đoán'),
    ('xử lý', r'xử\s+lý'),
    ('sử lý', r'sử\s+lý'),
    ('chia sẻ', r'chia\s+sẻ'),
    ('chia xẻ', r'chia\s+xẻ'),
    ('xuất sắc', r'xuất\s+sắc'),
    ('suất sắc', r'suất\s+sắc'),
    ('nghiệt ngã', r'nghiệt\s+ngã'),
    ('huyễn hoặc', r'huyễn\s+hoặc'),
    ('bàng hoàng', r'bàng\s+hoàng'),
    ('ngỡ ngàng', r'ngỡ\s+ngàng'),
    ('cứu rỗi', r'cứu\s+rỗi'),
    ('cứu dỗi', r'cứu\s+dỗi'),
    ('rúng động', r'rúng\s+động'),
    ('dúng động', r'dúng\s+động'),
    ('xiềng xích', r'xiềng\s+xích'),
    ('gông cùm', r'gông\s+cùm'),
    ('bản ngã', r'bản\s+ngã'),
    ('bản ngả', r'bản\s+ngả'),
    ('sa sút', r'sa\s+sút'),
    ('xa sút', r'xa\s+sút'),
    ('tước đoạt', r'tước\s+đoạt'),
    ('răn đe', r'răn\s+đe'),
    ('dăn đe', r'dăn\s+đe'),
    ('rào cản', r'rào\s+cản'),
    ('dào cản', r'dào\s+cản'),
    ('trơ tráo', r'trơ\s+tráo'),
    ('chơ cháo', r'chơ\s+cháo'),
    ('chơ tráo', r'chơ\s+tráo'),
    ('lãnh đạm', r'lãnh\s+đạm'),
    ('lãng đạm', r'lãng\s+đạm'),
    ('thấu cảm', r'thấu\s+cảm'),
    ('tập nhiễm', r'tập\s+nhiễm'),
    ('cưỡng ép', r'cưỡng\s+ép'),
    ('quá giang', r'quá\s+giang'),
    ('quá dang', r'quá\s+dang'),
]

print("=== CHECKING COMMON SPELLING PATTERNS ===")
for name, pat in checks:
    matches = []
    for sid, txt in text_corpus:
        if re.search(pat, txt, re.IGNORECASE):
            matches.append((sid, txt))
    if matches:
        print(f"[{name}]: found {len(matches)} occurrences")
        for sid, txt in matches:
            # highlight match
            m = re.search(pat, txt, re.IGNORECASE)
            print(f"  {sid}: ...{txt[max(0, m.start()-20):min(len(txt), m.end()+20)]}...")
