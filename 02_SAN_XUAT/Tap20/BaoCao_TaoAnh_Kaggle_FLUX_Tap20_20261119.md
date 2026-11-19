# BÁO CÁO HOÀN TẤT TẠO 124 ẢNH NỀN FLUX.2 CHO TẬP 20 (241 CÂU THOẠI)

> **Ngày thực hiện:** 19/11/2026  
> **Chủ đề:** Hồ sơ Stephen McDaniel ('Khoảnh khắc sụp đổ trước ống kính' - Trường Luật Mercer, Macon, Georgia)  
> **Tiêu chuẩn kỹ thuật áp dụng:** `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` v1.0 (Deep Noir Chiaroscuro 2K + Post-processing)  
> **Mô hình AI:** `black-forest-labs/FLUX.2-klein-4B` trên môi trường Kaggle GPU (2 VM độc lập chạy song song 2 GPU Tesla T4)  

---

## 1. KẾT QUẢ TỔNG QUAN

- **Tổng số câu thoại kịch bản mới:** 241 câu (Hệ sinh thái 10 chỉ dấu tâm lý & hành vi A2c).
- **Tổng số ảnh nền độc bản đã tạo mới:** **124/124 ảnh** (đạt 100% mục tiêu).
- **Tỷ lệ phân bổ trung bình:** **1.94 câu / 1 ảnh nền** (trung bình ~19.8 s / ảnh) $\rightarrow$ **Triệt tiêu 100% nguy cơ lặp ảnh trong video (H22, H25).**
- **Chuẩn kích thước đồ họa:** **2112 × 1188 (16:9 2K)** bằng thuật toán nội suy **LANCZOS**, 100% đạt chuẩn QC kỹ thuật số.
- **Hậu kỳ đồ họa Noir tự động:**
  - Dìm màu bão hòa -35% (Color saturation 0.65).
  - Tăng tương phản bóng tối +15% (Contrast 1.15).
  - Phủ Noir Vignette 45% ở các góc ngoài.
  - Áp hạt phim 35mm (Gaussian noise 7.5).
- **Thư mục lưu trữ:** `assets/bg/` (từ `t20_a1_01_mercer_law_campus_dawn_fog.png` đến `t20_a5_20_endcard_investigative_archive_wall.png`).
- **Bản quyền & Hồ sơ nguồn:** Cập nhật đủ 124 bản ghi vào `provenance.json` theo luật L7.

---

## 2. PHÂN BỔ 124 ẢNH THEO 5 HỒI NỘI DUNG

| Hồi | Tên hồi | Số câu | Số ảnh | Tỷ lệ | Nội dung hình ảnh & Điểm nhấn noir |
|:---:|---|:---:|:---:|:---:|---|
| **1** | Cuộc phỏng vấn định mệnh & Tin báo từ thùng rác | 55 | **28** | 1.96 | Khuôn viên Mercer mờ sương, mặt tiền chung cư Barristers Hall, cửa khóa then cài, bóng McDaniel tiếp cận máy quay WGXA, ống kính truyền hình, mặt nạ bình thường hóa rạn nứt, phóng viên nhận tin đàm, thùng rác kim loại niêm phong, nghi phạm khuỵu xuống lề đường, đồng tử mắt mở to hoảng loạn, xe chở rác trễ giờ, xe cảnh sát tuần tra đêm, phòng thẩm vấn 12 giờ. |
| **2** | Bức tượng đá trong phòng hỏi cung & Cú sốc nhận thức | 47 | **24** | 1.96 | Camera an ninh phòng thẩm vấn, tư thế pho tượng đá bất động cực đoan, quạt trần quay đơn điệu, cơ thể hóa đá (tonic immobility), phòng đơn tĩnh lặng, kính cận vô cảm, bàn tay cứng đờ kiểm soát, khám xét căn hộ, chìa khóa vạn năng bằng đồng, góc nhìn ban công rình rập, bi khóa xước xát dưới kính hiển vi, bao bì cưa sắt rỗng, máy tính để bàn nối cáp pháp y, máy quay zoom tele bệ cửa sổ, vòng xoáy ám ảnh. |
| **3** | Giải mã tâm lý: Kẻ rình rập ngầm & Phản ứng đóng băng kỳ dị | 49 | **25** | 1.96 | Chồng hồ sơ tâm thần học pháp y, mặt nạ kịch nghệ nứt đôi, bảng đen phân tích hành vi, bóng kẻ rình rập ngõ tối, màn hình xem lén ban đêm, quân tốt cờ vua bị nghiền nát, ngai vàng ái kỷ trống không, bằng tốt nghiệp luật vỡ vụn, tủ hồ sơ chia ngăn tâm lý, giáo trình luật gáy mạ vàng, bản đồ tội ác hoàn hảo bị xóa, đồng hồ bấm giờ điều tra, áo bệnh nhân treo cạnh com-lê, mắt thú dữ dồn vào đường cùng, bóng chiếc ghế điện tử hình phạt. |
| **4** | Phán quyết chung thân & Sự trừng phạt của công lý | 54 | **27** | 2.00 | Tòa án Thượng thẩm Hạt Bibb, khán phòng xử án trang nghiêm, nghi phạm râu dài tiều tụy, núi hồ sơ bằng chứng công tố, xà lim tạm giam 3 năm, văn bản thỏa thuận nhận tội ký kết, băng ghi âm thừa nhận tội ác, tượng Nữ thần Công lý hạ kiếm, bục phát biểu luận tội, hàng ghế điều tra viên Macon, búa tòa án Thẩm phán Simms, gia đình nạn nhân ôm nhau khóc, khung ảnh tưởng niệm Lauren, áo cử nhân đơn độc, hành lang ngục tù vô tận, còng xích áp giải, tượng đồng ái kỷ sụp đổ, giọt nước mắt tự thương hại, khuôn viên trường thanh bình. |
| **5** | Bài học cảnh tỉnh & 4 Cảnh báo đỏ phòng ngừa | 36 | **20** | 1.80 | Khu vườn tưởng niệm Lauren Giddings, cải cách kiểm soát an ninh trường học, hành lang chung cư có camera cảm ứng, ngọn hải đăng cảnh giác, vòng nguyệt quế học thuật gãy đôi (khử hiệu ứng hào quang), chốt khóa an toàn cửa trong, khiên cẩm thạch trực giác (The Gift of Fear), sách Gavin de Becker, cổng sắt chốt chặt, bảng ghim 4 cảnh báo đỏ tổng quan, ống nhòm rình rập (Redflag 1), chìa khóa đột nhập (Redflag 2), rèm cửa bảo vệ ranh giới, camera an ninh cá nhân (Redflag 3), mặt nạ sắt vô cảm (Redflag 4), gương vỡ cái tôi thù hận, bàn làm việc hồ sơ kết thúc Amber Eyes, micro phòng thu cộng đồng, bức tường lưu trữ hồ sơ vụ án khổng lồ (thẻ kết). |

---

## 3. CÁC TÀI SẢN & ARTIFACT QC ĐÃ HOÀN TẤT

1. **Bộ 124 ảnh nền 2K hoàn chỉnh:** Lưu trữ tại `assets/bg/t20_a*.png`.
2. **8 Tờ Montage QC trực quan (ô 512×288):**
   - Lưu trữ tại: `02_SAN_XUAT/Tap20/qc_montage/montage_t20_sheet_1.png` đến `montage_t20_sheet_8.png`.
3. **Danh mục chi tiết đối chiếu kịch bản:** [Danh_Sach_Anh_Tap20.md](file:///d:/TEST/Gax/amber-eyes/02_SAN_XUAT/Tap20/Danh_Sach_Anh_Tap20.md).
4. **Sổ nguồn gốc bản quyền thương mại:** [provenance.json](file:///d:/TEST/Gax/amber-eyes/provenance.json) (đã cập nhật đủ 124 bản ghi).
