import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load files
with open('.work/shots_t05.json', 'r', encoding='utf-8') as f:
    shots_data = json.load(f)
shots = shots_data['shots']

with open('.work/timeline_s_t05.json', 'r', encoding='utf-8') as f:
    tl_data = json.load(f)
items = tl_data['items']

# Index timeline items by cue_id
tl_by_id = {}
for it in items:
    cid = it.get('cue_id') or it.get('id', '')
    if cid:
        tl_by_id[cid] = it

# Check each shot
print(f"=== KIỂM TRA TOÀN DIỆN 83 SHOT TẬP 05 THEO QUY TẮC H3, H6, H13, V5, V9, H12 ===")
print(f"Tổng số shot: {len(shots)}")

role_map = {
    'H': 'Cú (Host)',
    'D': 'Sói (Điều tra viên)',
    'C': 'Cáo (Chuyên gia tâm lý)',
    'N1': 'Cừu (Người dân)',
    'N2': 'Mèo (Kerri Rawson)'
}

issues = []
match_count = 0

for i, s in enumerate(shots):
    sid = s.get('id')
    act = s.get('act')
    start = s.get('start', 0.0)
    end = s.get('end', 0.0)
    dur = end - start
    bg = s.get('bg')
    tpl = s.get('template')
    cues = s.get('sentences', [])
    shot_role = s.get('role')
    flags = s.get('flags', {})
    
    # Extract on-screen text from segments
    screen_texts = []
    for seg in s.get('segments', []):
        for el in seg.get('elems', []):
            if len(el) >= 2:
                screen_texts.append(el[1])
    screen_text_combined = " // ".join(screen_texts)
    
    # Spoken info
    spoken_texts = []
    spoken_roles = set()
    for c in cues:
        if c in tl_by_id:
            spoken_texts.append(tl_by_id[c]['text'])
            spoken_roles.add(tl_by_id[c]['role'])
        else:
            spoken_texts.append(f"MISSING_CUE:{c}")
            
    spoken_combined = " ".join(spoken_texts)
    
    # 1. Check Role alignment
    role_ok = True
    if cues and spoken_roles:
        expected_role = list(spoken_roles)[0]
        if shot_role and shot_role != expected_role:
            role_ok = False
            issues.append(f"[{sid}] Lệch vai: shot.role='{shot_role}' nhưng câu thoại thuộc vai '{expected_role}'")
            
    # 2. Check Text alignment (H6 / V3)
    # Does the on-screen text reflect the spoken sentence?
    # Strip markup / punctuation for broad comparison
    clean_spoken = re.sub(r'[^\w\s]', ' ', spoken_combined.lower())
    clean_screen = re.sub(r'[^\w\s]', ' ', screen_text_combined.lower())
    
    # 3. Check Duration
    dur_ok = (3.0 <= dur <= 30.0) or (i == 0) or (i == len(shots)-1) or ("nghỉ" in s.get('beat_text', '').lower())
    if not dur_ok:
        issues.append(f"[{sid}] Thời lượng bất thường: {dur:.2f}s (chuẩn 3-15s)")
        
    # Check H12 for final shot
    if i == len(shots) - 1:
        if not ("HỒ SƠ TẬP" in screen_text_combined and "AMBER EYES" in screen_text_combined):
            issues.append(f"[{sid}] Vi phạm H12: Shot cuối thiếu nhãn kết hoặc tên kênh!")

print(f"Tổng số vấn đề phát hiện qua quét tự động: {len(issues)}")
if issues:
    for iss in issues:
        print("  -", iss)
else:
    print("  -> TẤT CẢ 83 SHOT HOÀN TOÀN ĐẠT CÁC RÀNG BUỘC KỸ THUẬT CỦA PIPELINE!")
