import json

data = json.load(open('.work/_episodes_data_final.json', encoding='utf-8'))

total_eps = len(data)
total_sentences = sum(r['sentences'] for r in data)
total_images = sum(r['images'] for r in data)
total_shots = sum(r['shots_rule'] for r in data if isinstance(r['shots_rule'], int))

print(f"Tổng số tập: {total_eps}")
print(f"Tổng câu thoại: {total_sentences}")
print(f"Tổng ảnh nền đã dựng/chuẩn bị: {total_images}")
print(f"Tổng số shot theo quy tắc: {total_shots}")
