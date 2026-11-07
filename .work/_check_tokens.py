import sys, json, re

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('.work/script_tap10.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

# Collect all tokens
all_tokens = []
sentence_dict = {}

for el in elements:
    if 'sentences' in el:
        for s_idx, s_obj in enumerate(el['sentences'], 1):
            if isinstance(s_obj, dict):
                text = s_obj.get('text', '').strip()
                s_id = s_obj.get('id', f"{el['id']}#{s_idx}")
            else:
                text = str(s_obj).strip()
                s_id = f"{el['id']}#{s_idx}"
            sentence_dict[s_id] = text
            # clean punctuation
            clean_text = re.sub(r'[“”,.:;?!\"()\[\]\'’…\-]', ' ', text)
            for w in clean_text.split():
                all_tokens.append((w, s_id))

print(f"Total tokens: {len(all_tokens)}")

# Check for single character words that might be typos (e.g. stray letters)
stray_chars = [(w, sid) for w, sid in all_tokens if len(w) == 1 and w.lower() not in {'y', 'ở', 'ả', 'ạ', 'ê', 'ô', 'ơ', 'ư', 'à', 'á', 'ó', 'ò', 'ẻ', 'ủ', 'ũ', 'ã', 'è', 'é', 'ẹ', 'ì', 'í', 'ị'}]
print(f"Stray characters: {stray_chars}")

# Check for common typing bugs like double vowels: 'ee', 'oo', 'aa', 'dd', 'ww'
typing_bugs = []
for w, sid in all_tokens:
    # ignore english proper names
    if w in {'Colleen', 'Hooker', 'Westwood', 'Eugene', 'Green'}:
        continue
    if re.search(r'(aa|ee|oo|dd|ww|jj|ss|ff|rr|xx)', w, re.IGNORECASE):
        typing_bugs.append((w, sid))
print(f"Typing bugs (telex raw): {typing_bugs}")

# Check capitalization issues inside sentences (words capitalized in the middle of a clause that are not proper nouns)
cap_issues = []
proper_set = {
    'Colleen', 'Stan', 'Cameron', 'Hooker', 'Janice', 'Oregon', 'California',
    'Eugene', 'Westwood', 'Red', 'Bluff', 'Riverside', 'Tehama', 'The', 'Company',
    'Seligman', 'Martin', 'Patrick', 'Carnes', 'Sykes', 'Matza', 'Chris', 'Hatcher',
    'Clarence', 'Knight', 'Richard', 'Tedeschi', 'Lawrence', 'Calhoun',
    'Gavin', 'Becker', 'Amber', 'Eyes', 'Hiệu', 'Hào', 'Quang', 'Điểm', 'Mù', 'Xã', 'Hội',
    'Chữ', 'Ký', 'Tâm', 'Lý', 'Ngòi', 'Nổ', 'Gãy', 'Quỹ', 'Đạo', 'Leo', 'Thang', 'Ảo', 'Tưởng',
    'Tước', 'Đoạt', 'Cảm', 'Giác', 'Cực', 'Hạn', 'Vật', 'Hóa', 'Phi', 'Nhân', 'Bản', 'Hợp', 'Đồng',
    'Nô', 'Lệ', 'Sự', 'Kiến', 'Tạo', 'Thực', 'Tại', 'Méo', 'Mó', 'Bất', 'Lực', 'Tập', 'Nhiễm',
    'Learned', 'Helplessness', 'Bài', 'Kiểm', 'Tra', 'Lòng', 'Trung', 'Thành',
    'Gắn', 'Kết', 'Chấn', 'Thương', 'Trauma', 'Bonding', 'Vị', 'Cứu', 'Tinh',
    'Chia', 'Ngăn', 'Nhận', 'Thức', 'Compartmentalization', 'Lá', 'Chắn', 'Bình', 'Thường',
    'Kỹ', 'Thuật', 'Hòa', 'Đạo', 'Đức', 'Tẩy', 'Não', 'Soạn', 'Thảo',
    'Sụp', 'Đổ', 'Cái', 'Tôi', 'Ái', 'Kỷ', 'Tự', 'Thương', 'Hại', 'Bệnh',
    'Tăng', 'Trưởng', 'Sau', 'Sang', 'Post', 'Traumatic', 'Growth',
    'Simple', 'Gifts', 'Life', 'Kiểm', 'Soát', 'Cưỡng', 'Ép', 'Bạo', 'Thể', 'Xác',
    'Gift', 'Fear', 'Dấu', 'Hiệu', 'Kẻ', 'Thù', 'Tưởng', 'Tượng', 'Thuyết', 'Trí'
}

for sid, text in sentence_dict.items():
    words = text.split()
    for idx, w in enumerate(words):
        if idx == 0:
            continue
        clean_w = re.sub(r'^[“\"\'(\[]+|[”\"\'\)\].,:;?!]+$', '', w)
        if clean_w and clean_w[0].isupper() and clean_w not in proper_set:
            # check if previous word ends with . ? !
            prev = words[idx-1]
            if not prev.endswith(('.', '?', '!', '."', '?”', '!”')):
                cap_issues.append((sid, clean_w, text))

print(f"\nUnusual mid-sentence capitalization ({len(cap_issues)}):")
for sid, cw, txt in cap_issues[:20]:
    print(f"  [{sid}] '{cw}' -> {txt}")
