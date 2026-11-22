import json

data = json.load(open('.work/_episodes_data_final.json', encoding='utf-8'))

lines = []
lines.append("# BÁO CÁO TOÀN DIỆN CÁC VỤ ÁN TRONG HỆ THỐNG SẢN XUẤT AMBER EYES (TẬP 01 – TẬP 68)\n")
lines.append("> **Ngày trích xuất:** 22/11/2026\n")
lines.append("> **Hệ thống dữ liệu:** Quét từ `01_KICH_BAN/`, `02_SAN_XUAT/`, `.work/shots*.json`, `assets/bg/` và các hồ sơ kế hoạch `KeHoach_Video_TapXX.md`.\n\n")

lines.append("## 1. TỔNG QUAN HỆ THỐNG\n")
lines.append(f"- **Tổng số tập hồ sơ vụ án:** 68 tập (Tập 01 đến Tập 68)\n")
lines.append(f"- **Tổng số câu thoại hiện tại:** {sum(r['sentences'] for r in data):,} câu\n")
lines.append(f"- **Tổng số ảnh nền (Background/Art) đã dựng & lưu trữ:** {sum(r['images'] for r in data):,} ảnh (trong `assets/bg/` và `assets/bg/_raw/`)\n")
lines.append(f"- **Tổng số shot theo quy tắc chuẩn hóa:** {sum(r['shots_rule'] for r in data if isinstance(r['shots_rule'], int)):,} shots\n\n")

lines.append("## 2. BẢNG CHI TIẾT TỪNG TẬP\n\n")
lines.append("| Tập | Tên tập / Vụ án | Quốc gia | Số câu thoại | Số ảnh đã dựng | Số shot theo quy tắc | Ghi chú trạng thái |\n")
lines.append("|:---:|:---|:---:|:---:|:---:|:---:|:---|\n")

for r in data:
    status = "Đã xuất bản / Master" if r['ep'] <= 2 else ("Đã lập shot & TTS" if r['shots'] > 0 else ("Đã có ảnh nền" if r['images'] > 0 else "Kịch bản hoàn tất"))
    lines.append(f"| **Tap {r['ep']:02d}** | {r['clean_title']} | {r['country']} | {r['sentences']} | {r['images']} | {r['shots_rule']} | {status} |\n")

lines.append("\n---\n")
lines.append("## 3. QUY TẮC TÍNH SỐ SHOT CỦA KÊNH AMBER EYES\n")
lines.append("- **Đối với các tập đã lập bảng shot (`shots.json` / `shots_tXX.json` hoặc mục B6 hồ sơ):** Số shot lấy chính xác từ bảng timeline đã neo với audio master.\n")
lines.append("- **Đối với các tập đang ở giai đoạn kịch bản:** Theo Tiêu chuẩn dựng video Amber eyes (Mục A6 / B5), mỗi câu thoại tương ứng 1 shot nội dung (H6/V3 chữ nguyên văn), cộng thêm 4 shot chuyển hồi (Act 2, 3, 4, 5) và 1 shot thẻ kết (Closing Card H12). Do đó: `Số shot chuẩn = Số câu thoại + 5`.\n")

report_content = "".join(lines)
open('.work/_report_episodes.md', 'w', encoding='utf-8').write(report_content)
print('Report generated successfully!')
