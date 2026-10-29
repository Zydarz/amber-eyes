import sys

with open('00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = "| 31 | Ghi provenance cho ứng viên Freesound vào sổ chính bị **skip hết** vì `file` trùng đường dẫn đích đã có dòng từ YouTube Audio Library | Ứng viên **chưa duyệt** ghi vào sổ tạm `.work/freesound_provenance.json`; chỉ `--merge` vào `provenance.json` sau khi người dùng nghe duyệt |"

new_entry = target + "\n| 32 | **Lệch pha ngữ nghĩa giữa câu thoại và hình ảnh/chữ trên hình (Tập 06: người dùng phát hiện đang nói mức lương 5$ thì hình đã chuyển sang tủ áo khoác mỏng)**: Phân bổ ranh giới câu thoại vào shot bị vội, cắt shot ở giữa hai câu cùng chủ đề hoặc đặt shot hiển thị trước khi câu thoại bắt đầu | **Rà soát đồng bộ ngữ nghĩa 100% trước khi dựng**: Mỗi khi câu thoại chuyển sang đối tượng/vật chứng/địa điểm mới thì ảnh và chữ mới chuyển theo; các câu cùng một nội dung cốt lõi (như 2 câu về mức lương 5$) phải gom trọn vẹn trong cùng 1 shot; chữ hiển thị phải lấy đúng từ câu đang đọc trong shot đó (H3, V3) |"

if target not in text:
    print("Target not found!")
    sys.exit(1)

new_text = text.replace(target, new_entry)
with open('00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Updated A11 successfully!")
