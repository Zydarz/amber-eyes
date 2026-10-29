# -*- coding: utf-8 -*-
import json

with open(".work/timeline_s_t06.json", encoding="utf-8") as f:
    tl = json.load(f)

with open(".work/shots_t06.json", encoding="utf-8") as f:
    sh = json.load(f)

sent_map = {it["id"]: it for it in tl["items"]}

# Rà soát từng shot:
# Kiểm tra:
# 1. Câu thoại đang nói về nhân vật/vật chứng gì?
# 2. Ảnh nền là gì?
# 3. Tiêu đề hiển thị là gì?

mismatches = []

for s in sh["shots"]:
    sid = s["id"]
    bg = s["bg"]
    sents = s.get("sentences", [])
    if not sents:
        continue
    
    # lấy text các câu
    texts = [sent_map[sid_c]["text"] for sid_c in sents if sid_c in sent_map]
    combined_text = " ".join(texts)
    
    # Text hiển thị
    segs = s.get("segments", [])
    display_words = []
    for seg in segs:
        for el in seg.get("elems", []):
            if len(el) > 1:
                display_words.append(el[1])
    display_str = " · ".join(display_words)
    
    # Kiểm tra một số từ khóa đặc thù
    # Ví dụ:
    # - Nếu câu nói về "nhẫn JAS" mà ảnh không phải nhẫn
    # - Nếu câu nói về "vôi bột" mà ảnh không phải vôi bột
    # - Nếu câu nói về "còng tay" mà ảnh không phải còng tay
    # - Nếu câu nói về "bãi đỗ xe" mà ảnh là cái khác
    # - Nếu câu nói về "phòng thẩm vấn" mà ảnh là xe hơi
    
    mismatches.append({
        "shot": sid,
        "bg": bg,
        "sents": sents,
        "display": display_str,
        "text_summary": combined_text[:120]
    })

print(f"Tổng số shot rà soát: {len(mismatches)}")
