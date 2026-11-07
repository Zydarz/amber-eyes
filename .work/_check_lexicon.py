import sys, re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('01_KICH_BAN/Tap10/kichban_tap10_23102026.md', 'r', encoding='utf-8') as f:
    text = f.read()

words = re.findall(r'[A-Za-zÀ-ỹ]+', text)
foreign_words = {
    'audio', 'podcast', 'host', 'driven', 'documentary', 'narrator', 'led',
    'dark', 'ambient', 'solo', 'cello', 'minimalist', 'piano', 'drone', 'warm', 'db',
    'colleen', 'stan', 'the', 'company', 'girl', 'in', 'box', 'tehama', 'county',
    'sheriff', 's', 'office', 'clarence', 'knight', 'chris', 'hatcher', 'simple', 'gifts',
    'of', 'life', 'jim', 'green', 'martin', 'seligman', 'patrick', 'carnes', 'richard',
    'tedeschi', 'lawrence', 'calhoun', 'gift', 'fear', 'gavin', 'de', 'becker',
    'bgm', 'sfx', 'nghi', 'learned', 'helplessness', 'trauma', 'bonding',
    'compartmentalization', 'post', 'traumatic', 'growth', 'eugene', 'oregon', 'california',
    'westwood', 'red', 'bluff', 'cameron', 'hooker', 'janice', 'riverside', 'sykes',
    'matza', 'amber', 'eyes', 'modus', 'operandi', 'signature', 'mo', 'route', 'dodge', 'van',
    'waterbed', 'headbox', 'theory', 'mind', 'coercive', 'control',
    'stockholm', 'waterbeds', 'plywood', 'brief', 'format', 'act', 'n1', 'n2'
}

unique_vn = sorted(set(w.lower() for w in words if w.lower() not in foreign_words))

# Let's inspect syllables that end with rare rhymes or have questionable spellings
# Common Vietnamese initials: b, c, ch, d, đ, g, gh, h, k, kh, l, m, n, ng, ngh, nh, p, ph, qu, r, s, t, th, tr, v, x
# Check if any syllable has invalid initial or rhyme
invalid_initials = []
for s in unique_vn:
    # check valid initial
    m = re.match(r'^(ngh|ng|gh|ch|kh|nh|ph|qu|th|tr|[bcdđghklmnpqrstvx])', s)
    if not m:
        # vowel initial
        if not re.match(r'^[aăâeêioôơuưyáàảãạắằẳẵặấầẩẫậéèẻẽẹếềểễệíìỉĩịóòỏõọốồổỗộớờởỡợúùủũụứừửữựýỳỷỹỵ]', s):
            invalid_initials.append(s)

print(f"Invalid initials: {invalid_initials}")

# Let's check syllables that occur only once or twice, and print them out to inspect
word_counts = {}
for w in words:
    wl = w.lower()
    if wl not in foreign_words:
        word_counts[wl] = word_counts.get(wl, 0) + 1

rare = [w for w, c in word_counts.items() if c == 1]
print(f"Total rare syllables (appearing once): {len(rare)}")
print("Sample of 100 rare syllables:")
print(', '.join(rare[:100]))
