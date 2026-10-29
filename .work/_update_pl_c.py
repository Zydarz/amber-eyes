from pathlib import Path

p = Path("02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md")
text = p.read_text(encoding="utf-8")

prefix = text.split("## PHỤ LỤC C (Tập 05)")[0]

new_part = """## PHỤ LỤC C (Tập 05) — KẾT QUẢ SẢN XUẤT & ĐO LƯỜNG QC (BƯỚC 10 - 11)

- **Thời gian hoàn thành:** 24/10/2026 · **Dựng lại chuẩn hóa H13 (Khớp 3 chiều Ảnh — Chữ — Lời thoại):** 25/10/2026.
- **Thành phẩm video:** `02_SAN_XUAT/Tap05/xuat_ban/Tap05_master.mp4` (505,16 MB · 529.697.842 bytes).
- **Thông số kỹ thuật:**
  - Định dạng: MP4 (H.264 High Profile, YUV420p, 1920×1080 @ 30.0 fps).
  - Tổng số khung hình: 43.742 frames.
  - Thời lượng container: **1.458,067 s** (24 phút 18,067 giây).
  - Thời lượng video: 1.458,067 s · Thời lượng audio: 1.458,048 s.
  - **Độ lệch hình / tiếng:** 0,0187 s (Chuẩn $\\le$ 0,05 s $\\rightarrow$ **ĐẠT**).
  - Bitrate tổng: 2.906,3 kbps.
  - **Kiểm tra giải mã (FFmpeg decode check):** **0 lỗi** trên toàn bộ 43.742 khung hình (ĐẠT 100%).
- **Kiểm định đồng bộ 3 chiều (Rule H13, H3, H6):**
  - Đã khắc phục 100% các lỗi trượt pha ở Hồi 1 (Shot 1-02, 1-03) và Hồi 2 (Shot 2-03 $\\rightarrow$ 2-06, Shot 2-08 $\\rightarrow$ 2-13).
  - Khớp 1-to-1 từng câu thoại với đúng ảnh nền minh họa và chữ hiển thị.
  - Tận dụng hiệu ứng chuyển cảnh `bg2` hòa tan mượt mà cho các shot 2 vế: Thư viện $\\rightarrow$ Thùng rác công viên (Shot 2-06) và Nhà thờ $\\rightarrow$ Bục giảng (Shot 2-10).
  - Điểm lệch từ vựng / ngữ nghĩa: **0 cảnh báo**.
- **Thành phẩm âm thanh:** `02_SAN_XUAT/Tap05/xuat_ban/Tap05_master.mp3` (34,99 MB).
  - Độ to tích hợp (Integrated Loudness): **−16,18 LUFS** (Chuẩn −16 $\\pm$ 1 LUFS $\\rightarrow$ **ĐẠT**).
  - Đỉnh thực (True Peak): **−0,72 dBFS** (Chuẩn $\\le$ −1,5 dBFS theo limiter).
  - Khoảng lặng bất thường ($> 0,3$ s tại $-60$ dB): **0** (ĐẠT chuẩn V4).
- **G10 / G9 Thử giọng & Kiểm vai mù:**
  - 5/5 vai đạt chuẩn 1 người xuyên suốt (Host, Điều tra viên, Chuyên gia, N1, N2).
  - Độ tách bạch 3 vai chính đạt 10/10 (F0 chênh lệch rõ rệt, không nhầm lẫn).
  - Báo cáo chi tiết: `02_SAN_XUAT/Tap05/thu_giong_kiem_vai/report.md`.
- **Tài sản đi kèm xuất bản:**
  - Phụ đề: `02_SAN_XUAT/Tap05/xuat_ban/Tap05.srt` (347 đoạn).
  - Thumbnail: `02_SAN_XUAT/Tap05/xuat_ban/thumbnail.png` (nền `t5_purple_floppy_disk`).
  - Mô tả YouTube: `02_SAN_XUAT/Tap05/xuat_ban/mo_ta.txt`.
  - Nguồn tham khảo: `02_SAN_XUAT/Tap05/xuat_ban/nguon_tham_khao.md`.
  - Bảng ảnh tĩnh (Contact Sheet): `02_SAN_XUAT/Tap05/contact_sheet_stills_t05.png` (83 shot).
"""

p.write_text(prefix + new_part, encoding="utf-8")
print("SUCCESS: Updated Phụ lục C via prefix split!")
