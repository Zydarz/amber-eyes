# BÁO CÁO HOÀN TẤT TẠO ẢNH NỀN FLUX.2 CHO TẬP 18 (240 CÂU THOẠI)

> **Ngày thực hiện:** 15/11/2026  
> **Chủ đề:** Hồ sơ Lori Vallow & Chad Daybell ('Thảm kịch Rexburg, Idaho' - Folie à Deux & Lời Tiên Tri Ngày Tận Thế)  
> **Tiêu chuẩn kỹ thuật áp dụng:** `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` v1.0 (Deep Noir Chiaroscuro 2K)  
> **Mô hình AI:** `black-forest-labs/FLUX.2-klein-4B` trên môi trường Kaggle GPU  

---

## 1. KẾT QUẢ TỔNG QUAN

- **Tổng số câu thoại kịch bản mới:** 240 câu (Hệ sinh thái 10 chỉ dấu tâm lý & hành vi A2c).
- **Tổng số ảnh nền đã tạo mới:** **80/80 ảnh nền độc bản** (đạt 100% mục tiêu).
- **Tỷ lệ phân bổ trung bình:** **3.0 câu / 1 ảnh nền** $\rightarrow$ **Triệt tiêu hoàn toàn nguy cơ lặp ảnh khi dựng video.**
- **Chuẩn kích thước đồ họa:** **2112 × 1188 (16:9 2K)** bằng thuật toán nội suy **LANCZOS**, 100% đạt chuẩn QC kỹ thuật số.
- **Thư mục lưu trữ:** `assets/bg/` (từ `t18_kauai_beach_wedding_dusk_shadows.png` đến `t18_endcard_investigative_archive_wall.png`).
- **Bản quyền & Hồ sơ nguồn:** Cập nhật đủ 80 bản ghi vào `provenance.json` theo luật L7.

---

## 2. PHÂN BỔ 80 ẢNH THEO 5 HỒI NỘI DUNG

| Hồi | Tên hồi | Số câu | Số ảnh | Tỷ lệ | Nội dung hình ảnh & Điểm nhấn noir |
|:---:|---|:---:|:---:|:---:|---|
| **1** | Bãi Biển Hawaii và Bí Ẩn Hai Đứa Trẻ Biến Mất | 46 | **16** | 2.88 | Bãi biển Kauai hoàng hôn lạnh, nhẫn cưới trên cát, xích đu trẻ em quạnh quẽ, màn hình FaceTime bị ngắt, hiện trường nổ súng Arizona, đơn kiện Cassandra, tháp chuông Rexburg, đồ chơi bé JJ, lệnh truy nã dán cột đèn, bản đồ FBI, cổng trang trại Salem. |
| **2** | Mảnh Đất Định Mệnh và Nỗi Đau Khai Quật | 44 | **16** | 2.75 | Đoàn xe FBI vây ráp, gương chiếu hậu xe thể thao của Chad, còng số tám trên nắp capo, hố đào nghĩa địa thú cưng, khay nhôm pháp y mẩu vải đồ ngủ đỏ bé JJ, hố đốt than tro, báo cáo tử thi đóng dấu đỏ, kho tự quản, rừng thông Yellowstone, sao kê ngân hàng an sinh xã hội, căn phòng trọ tồi tàn của Alex Cox, khai quật bà Tammy, nấc thang 3 bậc tội ác. |
| **3** | Mê Cung Cuồng Tín và Bản Ngã Vĩ Cuồng | 50 | **16** | 3.12 | Bục hội thảo Salt Lake 2018, bóng đen cặp đôi trên hành lang khách sạn, nút thắt Folie à Deux, cuộn giấy da 144.000 linh hồn, sổ tay Ánh sáng & Bóng tối, ảnh gia đình rạn nứt bị bóng đen che mặt, mặt nạ đất sét vỡ vụn (Thuyết Zombie), búp bê vải bị bỏ rơi (Dehumanization), thánh giá bọc dây thép gai, tủ gỗ chia ngăn nhận thức, ống nghe nhà tù Colby Ryan, xẻng đào huyệt nghĩa trang, gương vỡ bản sắc mẫu tử, Tòa án Ada County. |
| **4** | Bản Án Trần Thế và Sự Sụp Đổ Của Ảo Tưởng | 63 | **18** | 3.50 | Chồng hồ sơ công tố Ada County, bàn bị cáo trống trơn không nhân chứng, phong bì phán quyết bồi thẩm đoàn, micro bục phát biểu ngày tuyên án, búa tòa Thẩm phán Boyce tuyên 3 án chung thân, tháp canh Trại giam Pocatello, thông báo án tử hình Chad Daybell, màn chiếu bản đồ định vị GPS, bàn nghị án bồi thẩm đoàn, phiếu biểu quyết có tội, cuộn băng cassette ghi âm Melanie Gibb, lệnh tử hình đóng dấu nổi Fremont, xà lim tử tù Kuna, tượng sáp sụp đổ (Narcissistic Collapse), cánh cửa sắt đóng chặt, 4 chiếc ghế trống tưởng niệm. |
| **5** | Di Sản Công Lý và Bốn Lá Chắn Sinh Tồn | 37 | **14** | 2.64 | Công viên tưởng niệm Tylee & JJ, biển đồng hoa cương, mái vòm Quốc hội Idaho, huy hiệu bảo vệ trẻ thơ, khiên cẩm thạch tư duy phản biện, đêm thắp nến cộng đồng, bảng điều tra **4 Cảnh báo đỏ sinh tồn The Gift of Fear** (Quyền trượng giả gãy đôi, Dây thừng liên kết gia đình bị cắt đứt, Đồng hồ mặt trời tận thế nứt vỡ, Sách kinh thánh khoét rỗng giấu biên lai tài chính), bình minh đồng lúa mì vàng Idaho, hồ sơ kết thúc Amber Eyes, thẻ kết endcard. |

---

## 3. CÁC TÀI SẢN VÀ ARTIFACT ĐÃ HOÀN TẤT

1. **Bộ ảnh 2K hoàn chỉnh:** `assets/bg/t18_*.png` (80 file).
2. **Contact Sheet kiểm định trực quan:** [contact_sheet_t18.png](file:///d:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap18/contact_sheet_t18.png) (kích thước lưới 10×8).
3. **Danh mục chi tiết đối chiếu kịch bản:** [Danh_Sach_Anh_Tap18.md](file:///d:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap18/Danh_Sach_Anh_Tap18.md).
4. **Nhật ký pháp lý thương mại:** [provenance.json](file:///d:/TEST/Gax/amber-eyes/provenance.json) (đủ 80 dòng ghi chú prompt, seed, engine, chuẩn 2112×1188).
