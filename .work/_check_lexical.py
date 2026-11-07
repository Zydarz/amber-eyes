import sys, json, re
from collections import Counter

sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('.work/script_tap10.json', 'r', encoding='utf-8') as f:
    elements = json.load(f)

all_sentences = []
for el in elements:
    if 'sentences' in el:
        for s_idx, s_obj in enumerate(el['sentences'], 1):
            if isinstance(s_obj, dict):
                s_text = s_obj.get('text', '').strip()
                s_id = s_obj.get('id', f"{el['id']}#{s_idx}")
            else:
                s_text = str(s_obj).strip()
                s_id = f"{el['id']}#{s_idx}"
            role = el.get('role', '')
            act = el.get('act', 1)
            all_sentences.append((s_id, act, role, s_text))

# Let's inspect all common Vietnamese confusing words & typos
confusing_patterns = [
    (r'\bsát nhập\b', 'sáp nhập'),
    (r'\bdấu diếm\b', 'giấu giếm'),
    (r'\bgiấu diếm\b', 'giấu giếm'),
    (r'\bdấu giếm\b', 'giấu giếm'),
    (r'\bvô hình chung\b', 'vô hình trung'),
    (r'\bxoay sở\b', 'xoay xở'),
    (r'\bchẩn đoán\b', 'chẩn đoán (kiểm tra context nếu là chuẩn đoán)'),
    (r'\bchuẩn đoán\b', 'chẩn đoán'),
    (r'\btham quan\b', 'tham quan (không phải thăm quan)'),
    (r'\bthăm quan\b', 'tham quan'),
    (r'\bchắp vá\b', 'chắp vá'),
    (r'\bchấp vá\b', 'chắp vá'),
    (r'\btrăn trở\b', 'trăn trở'),
    (r'\bchăn chở\b', 'trăn trở'),
    (r'\bbạt vô âm tín\b', 'bặt vô âm tín'),
    (r'\btrực chờ\b', 'chực chờ'),
    (r'\bdành giật\b', 'tranh giành / giành giật'),
    (r'\bgiành dật\b', 'giành giật'),
    (r'\btrải nghiệm\b', 'trải nghiệm (không phải chải nghiệm)'),
    (r'\bchải nghiệm\b', 'trải nghiệm'),
    (r'\brút cục\b', 'rốt cuộc / rốt cục'),
    (r'\brốt cuộc\b', 'rốt cuộc'),
    (r'\btựu trung\b', 'tựu trung (không phải tựu chung)'),
    (r'\btựu chung\b', 'tựu trung'),
    (r'\bsuôn sẻ\b', 'suôn sẻ (không phải suông sẻ)'),
    (r'\bsuông sẻ\b', 'suôn sẻ'),
    (r'\bchững chạc\b', 'chững chạc'),
    (r'\bchững chạt\b', 'chững chạc'),
    (r'\bchần chừ\b', 'chần chừ (không phải chần trừ)'),
    (r'\bchần trừ\b', 'chần chừ'),
    (r'\bđầy ắp\b', 'đầy ắp'),
    (r'\bđầy ắp\b', 'đầy ắp'),
    (r'\bngăn nắp\b', 'ngăn nắp'),
    (r'\bngăn nắp\b', 'ngăn nắp'),
    (r'\blãng mạn\b', 'lãng mạn (không phải lãng mạng)'),
    (r'\blãng mạng\b', 'lãng mạn'),
    (r'\btỉ mỉ\b', 'tỉ mỉ / tỉ mỉ'),
    (r'\bnguội lạnh\b', 'nguội lạnh'),
    (r'\btrơ trẽn\b', 'trơ trẽn (không phải trơ trẽn / trơ trẽn)'),
    (r'\bdằn vặt\b', 'dằn vặt (không phải giằn vặt)'),
    (r'\bgiằn vặt\b', 'dằn vặt'),
    (r'\bgiằng xé\b', 'giằng xé (không phải dằng xé)'),
    (r'\bdằng xé\b', 'giằng xé'),
    (r'\bxao nhãng\b', 'xao nhãng (không phải sao nhãng)'),
    (r'\bsao nhãng\b', 'xao nhãng'),
    (r'\bbàng quang\b', 'bàng quan (nếu nói về thái độ đứng ngoài nhìn)'),
    (r'\bbàng quan\b', 'bàng quan (đúng nghĩa đứng ngoài nhìn)'),
]

print("=== KIỂM TRA CẶP TỪ DỄ LẪN ===")
for pattern, note in confusing_patterns:
    for s_id, act, role, text in all_sentences:
        m = re.search(pattern, text, re.IGNORECASE)
        if m:
            print(f"[{s_id}] Khớp '{m.group(0)}' -> Lưu ý: {note}\n  Câu: {text}\n")

# Check all foreign names in text for consistency
print("\n=== KIỂM TRA TÊN RIÊNG & ĐỊA DANH TIẾNG NƯỚC NGOÀI ===")
names_pattern = re.findall(r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b', ' '.join(s[3] for s in all_sentences))
proper_nouns = Counter(names_pattern)
for name, cnt in proper_nouns.most_common(40):
    print(f"  {name}: {cnt} lần")

