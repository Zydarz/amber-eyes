import json

data = json.load(open('.work/_accurate_final_report.json', encoding='utf-8'))

# Generate an exhaustive, perfectly formatted Markdown report
lines = []
lines.append("# BÁO CÁO THỐNG KÊ CHI TIẾT & CHÍNH XÁC TOÀN BỘ 68 HỒ SƠ VỤ ÁN (AMBER EYES)\n")
lines.append("> **Thời điểm kiểm tra & chốt dữ liệu:** 22/11/2026\n")
lines.append("> **Quy trình kiểm tra độc lập:**\n")
lines.append("> 1. **Số câu thoại:** Chạy trực tiếp engine phân tách kịch bản production `parse_kichban.py` trên từng file kịch bản chính thức (`01_KICH_BAN/Ho_So_Toi_Pham/TapXX/`). Đảm bảo từng câu thoại có ID (`#1`, `#2`...) phục vụ TTS và làm phụ đề.\n")
lines.append("> 2. **Số ảnh đã dựng:** Đếm trực tiếp các file ảnh nhị phân đã sinh trên ổ đĩa (`assets/bg/` và `assets/bg/_raw/`) theo tiền tố của từng tập.\n")
lines.append("> 3. **Số shot theo quy tắc:** Đối chiếu trực tiếp với các bảng timeline đã sản xuất (`.work/shots_tXX.json`), bảng shot trong kế hoạch (`KeHoach_Video_TapXX.md`), và áp dụng công thức quy tắc dựng chuẩn Amber eyes (`Số shot = Số câu thoại + 5`) cho các tập đang ở giai đoạn tiền kỳ.\n\n")

lines.append("## I. TỔNG HỢP TOÀN HỆ THỐNG\n")
lines.append(f"- **Tổng số tập hồ sơ vụ án:** **{len(data)} tập** (Tập 01 – Tập 68)\n")
lines.append(f"- **Tổng số câu thoại đọc thực tế:** **{sum(r['sentences'] for r in data):,} câu**\n")
lines.append(f"- **Tổng số ảnh nền graphic novel noir đã dựng/chuẩn bị sẵn:** **{sum(r['images'] for r in data):,} ảnh**\n")
lines.append(f"- **Tổng số shot dựng theo quy tắc kỹ thuật:** **{sum(r['shots'] for r in data):,} shots**\n\n")

lines.append("## II. BẢNG THỐNG KÊ CHI TIẾT TỪNG TẬP (68 TẬP)\n\n")
lines.append("| Tập | Tên tập / Hồ sơ vụ án | Quốc gia | Số câu thoại | Số ảnh đã dựng | Số shot theo quy tắc | Cơ sở tính số shot |\n")
lines.append("|:---:|:---|:---:|:---:|:---:|:---:|:---|\n")

for r in data:
    lines.append(f"| **Tap {r['ep']:02d}** | {r['title']} | {r['country']} | **{r['sentences']}** | **{r['images']}** | **{r['shots']}** | {r['shot_type']} |\n")

content = "".join(lines)
open('.work/BAO_CAO_CHI_TIET_68_TAP.md', 'w', encoding='utf-8').write(content)
print("File BAO_CAO_CHI_TIET_68_TAP.md generated successfully!")
