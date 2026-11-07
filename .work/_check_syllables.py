import sys, re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# Standard Vietnamese vowels with tone marks
# Check invalid Vietnamese syllables
with open('01_KICH_BAN/Tap10/kichban_tap10_23102026.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract all words
words = re.findall(r'[A-Za-zÀ-ỹ]+', text)
print(f"Total words in markdown: {len(words)}")

# Known English / foreign words in the script:
foreign_words = {
    'Audio', 'Podcast', 'Host', 'Driven', 'Documentary', 'Narrator', 'led',
    'Dark', 'Ambient', 'Solo', 'Cello', 'Minimalist', 'Piano', 'Drone', 'Warm', 'dB',
    'Colleen', 'Stan', 'The', 'Company', 'Girl', 'in', 'the', 'Box', 'Tehama', 'County',
    'Sheriff', 's', 'Office', 'Clarence', 'Knight', 'Chris', 'Hatcher', 'Simple', 'Gifts',
    'of', 'Life', 'Jim', 'Green', 'Martin', 'Seligman', 'Patrick', 'Carnes', 'Richard',
    'Tedeschi', 'Lawrence', 'Calhoun', 'Gift', 'Fear', 'Gavin', 'de', 'Becker',
    'BGM', 'SFX', 'HOST', 'NGHI', 'Learned', 'Helplessness', 'Trauma', 'Bonding',
    'Compartmentalization', 'Post', 'Traumatic', 'Growth', 'Eugene', 'Oregon', 'California',
    'Westwood', 'Red', 'Bluff', 'Cameron', 'Hooker', 'Janice', 'Riverside', 'Sykes',
    'Matza', 'Amber', 'Eyes', 'Modus', 'Operandi', 'Signature', 'MO', 'Route', 'Dodge', 'van',
    'waterbed', 'headbox', 'water', 'bed', 'Theory', 'Mind', 'Coercive', 'Control',
    'Stockholm', 'waterbeds', 'plywood'
}

# Check unusual syllables
# In Vietnamese, syllables follow standard patterns.
# Let's list any word that contains characters not commonly found in Vietnamese words
# like f, j, w, z (outside foreign words)
unusual_words = []
for w in set(words):
    if w in foreign_words:
        continue
    if re.search(r'[fjwz]', w, re.IGNORECASE):
        unusual_words.append(w)

print(f"Words with non-Vietnamese letters: {unusual_words}")

# Let's check tone mark placement and rare syllables
# List all unique lowercase words
unique_words = sorted(set(w.lower() for w in words if w not in foreign_words and not re.search(r'[fjwz]', w, re.IGNORECASE)))
print(f"Unique Vietnamese syllables: {len(unique_words)}")

# Let's check if any word has multiple tone marks or invalid unicode decomposition
invalid_accents = []
for w in unique_words:
    # check combining accents or double accents
    # valid tones: only 1 tone per syllable
    # let's count tone marks
    tones = len(re.findall(r'[áàảãạéèẻẽẹíìỉĩịóòỏõọúùủũụýỳỷỹỵắằẳẵặấầẩẫậếềểễệốồổỗộứừửữự]', w))
    if tones > 1:
        # Note: in compound words or diphthongs, e.g. 'thoải', 'nghiệp', only one vowel has accent.
        # But if word has 2 vowels with accents like 'áè', it's an error!
        # Check if consecutive accented vowels exist
        if re.search(r'[áàảãạéèẻẽẹíìỉĩịóòỏõọúùủũụýỳỷỹỵắằẳẵặấầẩẫậếềểễệốồổỗộứừửữự]{2,}', w):
            invalid_accents.append(w)

print(f"Words with consecutive accents: {invalid_accents}")
