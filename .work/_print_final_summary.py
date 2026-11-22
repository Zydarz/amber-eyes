import json

report = json.load(open('.work/_accurate_final_report.json', encoding='utf-8'))

total_eps = len(report)
total_sentences = sum(r['sentences'] for r in report)
total_images = sum(r['images'] for r in report)
total_shots = sum(r['shots'] for r in report)

print(f"Tổng số tập: {total_eps}")
print(f"Tổng số câu thoại: {total_sentences}")
print(f"Tổng số ảnh nền: {total_images}")
print(f"Tổng số shot: {total_shots}")
