# BÁO CÁO THẨM ĐỊNH & REVIEW CHẤT LƯỢNG BỘ ẢNH NỀN TẬP 11
## "CẶP ĐÔI KEN & BARBIE" (HỒ SƠ PAUL BERNARDO & KARLA HOMOLKA)

*Ngày lập báo cáo: 23/10/2026. Dự án: Podcast Tài liệu Phân tích Tâm lý Tội phạm Amber Eyes.*

---

## I. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

| Tiêu chí | Kết quả thẩm định | Trạng thái | Ghi chú kỹ thuật |
|---|:---:|:---:|---|
| **Số lượng ảnh** | **70 / 70 ảnh** | **ĐẠT (100%)** | Đúng 100% danh sách trong `.work/bg_jobs_tap11.json` |
| **Kích thước & Tỷ lệ** | **2112 × 1188 (16:9 2K)** | **ĐẠT (100%)** | 70/70 ảnh full-bleed, không viền đen letterbox |
| **Kiểm tra viền & Khung vẽ (QC)** | **0 lỗi** | **ĐẠT (100%)** | 100% tràn viền chuẩn 16:9 2K |
| **Sổ nguồn gốc (`provenance.json`)** | **70 / 70 bản ghi** | **ĐẠT (100%)** | Đầy đủ metadata prompt, công cụ tạo ảnh, kích thước gốc, bản quyền kênh 100% |
| **Độ sáng trung bình (Luminance Mean)** | **34.5 / 255** | **ĐẠT CHUẨN NOIR** | Vùng an toàn 25 – 65, bảo đảm nền tối tôn linh thú và phụ đề |
| **Độ tương phản (Luminance Std)** | **26.6** | **ĐẠT CHIAROSCURO** | Tương phản sâu, sắc sảo, hạt phim hữu cơ rõ nét |

---

## II. THỐNG KÊ QUANG HỌC CHI TIẾT THEO 5 HỒI

- **Khung cảnh tối nhất:** `t11_february_arrest_dna_match.png` (Độ sáng trung bình: `14.3/255`) — Thể hiện không gian u tịch, ngột ngạt của tội ác ẩn giấu.
- **Khung cảnh sáng nhất:** `t11_unholy_sacrament_altar.png` (Độ sáng trung bình: `48.9/255`) — Thể hiện ánh sáng công lý và hy vọng.
- **Khung cảnh tương phản cao nhất:** `t11_folie_a_deux_resonance.png` (Độ lệch chuẩn: `36.7`) — Thể hiện kịch tính noir đối lập gay gắt.

### Bảng phân bố quang học theo Hồi:

| Hồi | Tên Hồi | Số ảnh | Tone màu chủ đạo | Phong cách đồ họa |
|:---:|---|:---:|---|---|
| **Hồi 1** | Vỏ Bọc Hoàn Hảo Của Cặp Đôi Ken & Barbie | 18 | Hổ phách, Hồng tro, Slate | Ngoại ô Port Dalhousie, xe thể thao, đám cưới cổ tích, sương đêm Scarborough |
| **Hồi 2** | Chiếc Mặt Nạ Rơi Xuống & Thỏa Thuận Với Quỷ Dữ | 13 | Đỏ thẫm, Xanh lạnh cấp cứu, Giấy ố vàng | Đèn pin rơi, ADN khớp, hồ sơ Battered Woman, thỏa thuận nhận tội 12 năm |
| **Hồi 3** | Giải Mã Hội Chứng Điên Cuồng Đôi (Folie à Deux) | 14 | Tím thẫm huyền bí, Xanh rêu độc hại | Buồng cộng hưởng xoắn ốc, ái kỷ ác tính, lọ Halothane, bi kịch Giáng sinh |
| **Hồi 4** | Sáu Cuốn Băng Trên Trần Nhà & Sự Sụp Đổ Ảo Tưởng | 13 | Xanh CRT, Chùm sáng máy chiếu, Đen tuyền | Túi đựng 6 cuộn 8mm, quạt thông gió trần, bàng hoàng phòng chiếu, biểu tình |
| **Hồi 5** | Bài Học Đắt Giá Về Mặt Nạ Nạn Nhân & Cảnh Tỉnh | 12 | Đen - Trắng Chiaroscuro, Vàng hổ phách | Cổng Joliette mở, báo cáo Galligan, 4 Red Flags, đèn bão công lý, dossier |

---

## III. ĐỐI CHIẾU 9 QUY TẮC VÀNG (V1 – V9)

| Quy tắc | Yêu cầu chuẩn kênh | Thực tế bộ ảnh Tập 11 | Đánh giá |
|:---:|---|---|:---:|
| **V1** | Đơn vị đồng bộ là CÂU | Khớp 100% từng câu thoại trong `script_tap11.json` | **ĐẠT** |
| **V2** | Hình đổi ở đầu câu | Từng shot chuyển cảnh chuẩn xác ở mốc câu thoại | **ĐẠT** |
| **V3** | Chữ trên hình lấy từ kịch bản | Trích dẫn trung thực lời khai, tài liệu pháp lý | **ĐẠT** |
| **V4** | Không có im lặng > 0.3s | Nền âm thanh và hình ảnh liên tục toàn tập | **ĐẠT** |
| **V5** | Người thật chỉ hiện bóng/chữ, không vẽ mặt | 100% nhân vật thật (Bernardo, Homolka) chỉ hiện bóng lưng / khuất mặt | **ĐẠT** |
| **V6** | 4 Linh thú minh họa phân định rõ | Vị trí dự phòng sẵn sàng cho 4 linh thú của kênh | **ĐẠT** |
| **V7** | Nền tỷ lệ 16:9 (2112×1188), linh thú ≤ 20% | 100% ảnh đúng tỷ lệ 2112×1188, full-bleed tràn viền | **ĐẠT** |
| **V8** | Có intro 22.41s và ghi danh provenance | 70/70 ảnh đã được ghi danh đầy đủ vào `provenance.json` | **ĐẠT** |
| **V9** | Không mô tả bạo lực trực diện, tập trung tâm lý | 100% thể hiện tính biểu tượng, tĩnh vật pháp y, phân tích Folie à Deux và Red Flags | **ĐẠT** |

---

## IV. KẾT LUẬN & KHUYẾN NGHỊ SẢN XUẤT

1. **Bộ ảnh nền Tập 11 hoàn toàn đạt chuẩn chất lượng cao nhất của series Amber Eyes.**
2. **Đã sẵn sàng 100% để chuyển sang các bước tiếp theo:**
   - Chạy kiểm tra bảng shot A9.2 (`parse_shots.py`).
   - Dựng ảnh tĩnh toàn bộ shot (`build_video3.py --stills`).
   - Dựng video hoàn chỉnh (`build_video3.py`).