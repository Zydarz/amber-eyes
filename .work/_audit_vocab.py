# -*- coding: utf-8 -*-
"""Check Vietnamese vocabulary and grammar details."""
import io, sys
from pathlib import Path

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.path.insert(0, '.work')
import parse_kichban as PK

def audit_vocab(path_str):
    p = Path(path_str)
    parsed = PK.parse_file(str(p))
    print(f"\nAUDIT VOCABULARY FOR: {path_str}")
    
    # Danh sách từ kiểm tra
    words_to_watch = [
        'rối loạn', 'ranh giới', 'bất ổn', 'thao túng', 'cưỡng chế',
        'chia ngăn', 'vật hóa', 'phi nhân hóa', 'ái kỷ', 'phân mảnh',
        'nghiệt ngã', 'suy kiệt', 'dinh dưỡng', 'xích', 'ổ khóa', 'thẩm vấn',
        'công tố viên', 'biện lý', 'bồi thẩm đoàn', 'thẩm phán', 'phán quyết'
    ]
    
    loi = [e for e in parsed if e['kind'] == 'LOI']
    all_sents = [s for e in loi for s in e['sentences']]
    
    # In một số câu dài hoặc có cấu trúc phức tạp
    long_sents = [s for s in all_sents if s['words'] > 35]
    print(f"Total sentences: {len(all_sents)}")
    print(f"Sentences with > 35 words: {len(long_sents)}")
    for s in long_sents:
        print(f"  [{s['id']} - {s['words']}w] {s['text']}")

print("--- TẬP 15 VN ---")
audit_vocab("01_KICH_BAN/Tap15/kichban_tap15_23102026.md")

print("--- TẬP 17 VN ---")
audit_vocab("01_KICH_BAN/Tap17/kichban_tap17_23102026.md")
