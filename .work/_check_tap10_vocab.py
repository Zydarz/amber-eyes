import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('.work/_tap10_sentences.json', 'r', encoding='utf-8') as f:
    raw_sentences = json.load(f)

# Collect all tokens from all sentences
text_corpus = " ".join([item['text']['text'] for item in raw_sentences])

# Extract words
# Clean out punctuation
cleaned = re.sub(r'[\.,:;!\?\"“”\(\)\[\]–\-\'\’\/]', ' ', text_corpus)
tokens = cleaned.split()

print(f'Total word tokens in sentences: {len(tokens)}')
unique_tokens = sorted(list(set(tokens)))
print(f'Total unique word tokens: {len(unique_tokens)}')

# Let's inspect tokens that contain non-Vietnamese letters: f, j, w, z
foreign_letter_tokens = [w for w in unique_tokens if any(c in 'fjwzFJWZ' for c in w)]
print(f'Tokens with f, j, w, z: {len(foreign_letter_tokens)}')
print(' ', foreign_letter_tokens)

# Check tokens with numbers
number_tokens = [w for w in unique_tokens if any(c.isdigit() for c in w)]
print(f'Tokens with digits: {len(number_tokens)}')
print(' ', number_tokens)

# Let us check tone rules on Vietnamese tokens
# Stop finals: c, ch, p, t can only have sac or nang tone!
# Let's write a function to detect tone of a syllable
tones = {
    'ngang': 'aăâeêioôơuưyAĂÂEÊIOÔƠUƯY',
    'huyen': 'àằầèềìòồờùừỳÀẰẦÈỀÌÒỒỜÙỪỲ',
    'sac': 'áắấéếíóốớúứýÁẮẤÉẾÍÓỐỚÚỨÝ',
    'hoi': 'ảẳẩẻểỉỏổởủửỷẢẲẨẺỂỈỎỔỞỦỬỶ',
    'nga': 'ãẵẫẽễĩõỗỡũữỹÃẴẪẼỄĨÕỖỠŨỮỸ',
    'nang': 'ạặậẹệịọộợụựỵẠẶẬẸỆỊỌỘỢỤỰỴ'
}

def get_tone(syllable):
    for t_name, char_set in tones.items():
        if t_name == 'ngang':
            continue
        for c in char_set:
            if c in syllable:
                return t_name
    return 'ngang'

# Test stop consonants
stop_violators = []
for w in unique_tokens:
    # lower case without accents to check final
    # normalize
    tone = get_tone(w)
    # remove accents
    no_accent = w.lower()
    for accented, base in [
        ('àằầèềìòồờùừỳáắấéếíóốớúứýảẳẩẻểỉỏổởủửỷãẵẫẽễĩõỗỡũữỹạặậẹệịọộợụựỵ',
         'aaaeeiooouuyaaaeeiooouuyaaaeeiooouuyaaaeeiooouuyaaaeeiooouuy'),
        ('ăâêôơưđ', 'aaeooud')
    ]:
        for a, b in zip(accented, base):
            no_accent = no_accent.replace(a, b)
    
    if no_accent.endswith(('c', 'ch', 'p', 't')):
        # in Vietnamese, if it ends with c, ch, p, t, tone MUST be 'sac' or 'nang'
        # ignore english words
        if tone not in ('sac', 'nang') and tone != 'ngang':
            stop_violators.append((w, tone))

print(f'Stop final tone violators: {stop_violators}')
