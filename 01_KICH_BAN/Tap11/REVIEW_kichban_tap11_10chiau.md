# BÁO CÁO DUYỆT KỊCH BẢN TẬP 11 (BẢN TÁI CẤU TRÚC — HỆ SINH THÁI 10 CHỈ DẤU & CHIỀU SÂU TÂM LÝ ĐA CHIỀU)

*Ngày lập: 13/11/2026. Đối tượng: `01_KICH_BAN/Tap11/kichban_tap11_23102026.md`.*  
*Căn cứ quy chuẩn: `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Mục A2, A2c, A9.2).*

---

## 1. Tóm tắt thông số kỹ thuật kịch bản mới

| Mục | Đo lường thực tế | Chuẩn đối chiếu | Trạng thái |
|---|---:|---|:---:|
| **Tổng số phần tử (Elements)** | **65** | Cấu trúc 5 Hồi chuẩn hóa nâng cấp chiều sâu tâm lý | ✅ ĐẠT |
| **Lượt lời thoại (LOI)** | **39** | 39 lượt thoại phân vai cân bằng 4 giọng đọc | ✅ ĐẠT |
| **Tổng số câu (Sentences)** | **272 câu** | Đạt chuẩn dung lượng chuyên sâu $\ge 200$ câu (272 câu) | ✅ ĐẠT |
| **Tổng số từ (Word count)** | **7.410 từ** | Ước tính 3,5 từ/s $\approx$ 30,5 phút lời đọc | ✅ ĐẠT |
| **Độ an toàn quảng cáo (V9)** | **0 lỗi** | Không mô tả gore, không từ cấm A9.2 | ✅ ĐẠT |
| **Quy chuẩn ngắt giọng (G1)** | **0 lỗi** | 0 dấu ba chấm `...`, 0 ngắt vụn giữa câu `<#s#>` | ✅ ĐẠT |
| **Vai phụ N1 / N2** | `1.06` (N1 - 4 câu) / `4.08` (N2 - 5 câu) | Khai báo đúng `n_element` trong `edition.py` | ✅ ĐẠT |
| **Khoá tóm tắt (`summary`)** | `1.03#1` & `3.02#1` | Tồn tại 100% trong script (không trỏ vào SFX/BGM) | ✅ ĐẠT |
| **Khớp nối đa ngôn ngữ** | **Chuẩn hóa VN** | Nền tảng đồng bộ sang EN, JA, KO theo pipeline chuẩn | ✅ ĐẠT |

---

## 2. Bảng kiểm tra 10 Chỉ Dấu Chiều Sâu Tâm Lý & Hành Vi (A2c)

| # | Chỉ dấu tâm lý & hành vi | Vị trí thể hiện trong kịch bản | Nội dung giải phẫu cụ thể đã đưa vào |
|---|---|---|---|
| **1** | **Ảnh hưởng & Dư chấn xã hội** | `1.08`, `1.10`, `1.11`, `4.02`, `4.11`, `5.04` | - Cơn hoang tưởng tập thể (*Collective Paranoia*) bao trùm vùng Scarborough và Niagara suốt nửa thập kỷ: phụ nữ sợ hãi không dám ra đường đêm, phụ huynh nơm nớp đưa đón con.<br>- Bão dư luận toàn quốc khi thông tin 6 cuộn băng video bị rò rỉ: hàng trăm ngàn chữ ký đòi hủy thỏa thuận nhận tội.<br>- Hai cuộc điều tra độc lập mang tính lịch sử (Galligan và Campbell) dẫn đến đại cải tổ hệ thống phân tích liên kết tội phạm bạo lực ViCLAS trên toàn Canada.<br>- **Phán quyết lương tâm của xã hội (5.04):** Ngày 4/7/2005 khi Karla Homolka được trả tự do, làn sóng biểu tình và tẩy chay bùng nổ; bản án cô lập xã hội lưu đày vĩnh viễn kẻ thủ ác. |
| **2** | **Hung thủ nhìn nhận nạn nhân & Vì sao** | `2.06`, `2.09`, `3.05`, `3.06` | - **Vật hóa (Objectification) & Phi nhân hóa (Dehumanization):** Paul Bernardo xem nạn nhân như "món đồ chơi dùng một lần" để thỏa mãn cơn nghiện quyền lực.<br>- **Karla Homolka giáng cấp em gái:** Biến chính em gái ruột Tammy Homolka thành một "vật hiến tế" để củng cố liên kết tình cảm với Paul.<br>- **Khuyết tật Thuyết tâm trí (Theory of Mind):** Tiếng van xin khóc lóc của nạn nhân không kích hoạt lòng trắc ẩn mà bị xem như trở ngại phiền toái cần loại bỏ. |
| **3** | **Hung thủ nhìn nhận người thân & Chia ngăn** | `1.03`, `2.04`, `3.06`, `3.08` | - **Cơ chế chia ngăn cực đoan (Extreme Compartmentalization):** Ngăn người vợ hiền yêu động vật tại phòng khám thú y vs. Ngăn đồng lõa săn mồi lạnh lùng.<br>- Cuộc hôn nhân màu hồng và đám cưới xe ngựa cổ tích tại Niagara-on-the-Lake là **"Lá chắn bình thường hóa"** giúp Karla tự huyễn hoặc về phẩm giá bản thân.<br>- Điểm gãy gia đình: Khi bạo lực quay sang chính mình (vụ đánh bằng đèn pin tháng 1/1993), bản năng sinh tồn kích hoạt khiến Karla sẵn sàng bán đứng chồng. |
| **4** | **Thái độ trước bản án nhận được & TRỌNG TÂM CƠ CHẾ HỐI HẬN** | `4.04`, `4.08`, `4.10`, `5.02`, `5.06` | - **TRỌNG TÂM: Tại sao lại hối hận? Cơ chế tâm lý gì ở đây?**<br>  + Phân định rạch ròi giữa **Hối hận chân thực (Authentic Remorse)** (như Leslie Van Houten ở T09 hay Janice Hooker ở T10 trải qua Chấn thương đạo đức) vs. **Thao túng đóng vai nạn nhân (Manipulative Victimhood)** ở Karla.<br>  + Nước mắt của Karla tại bàn đàm phán 1993 là **Sự tự thương hại bệnh lý (Pathological Self-Pity)** — khóc vì bản thân sợ án tù chung thân sau khi trận đòn của Paul đánh sập ảo tưởng tình yêu, không phải khóc cho nạn nhân.<br>  + Karla lợi dụng định kiến giới và lòng trắc ẩn xã hội để khoác áo *Hội chứng Người phụ nữ bị Bạo hành* mua vé tự do 12 năm.<br>- **Paul Bernardo:** Sụp đổ cái tôi ái kỷ kéo dài *(Prolonged Narcissistic Collapse)*, cơ chế phòng vệ đổ lỗi ngoại tại, liên tục nộp đơn xin ân xá vô vọng và không bao giờ hối hận. |
| **5** | **Hệ thống tự bào chữa & Bẫy đạo đức nghề nghiệp** | `3.06`, `4.02`, `4.06`, `4.10` | - **Kỹ thuật trung hòa đạo đức (Neutralization):** Karla tự ru ngủ lương tri rằng mình "chỉ làm để chiều lòng chồng và giữ gìn tổ ấm", rơi vào trạng thái *Hôn mê Đạo đức (Moral Coma)*.<br>- **Xung đột đạo đức nghề nghiệp của Luật sư Ken Murray (4.06):** Giằng xé giữa đặc quyền bảo mật luật sư - thân chủ vs. lương tri con người khi cất giấu 6 cuốn băng suốt 17 tháng trong két sắt, vô tình tạo điều kiện cho "Thỏa thuận với Quỷ dữ" được phê chuẩn.<br>- **Chấn thương đạo đức của Công tố viên N2 (4.08):** Nỗi uất nghẹn cay đắng khi xem 6 cuốn băng nhận ra mình đã bị Karla dắt mũi ký hợp đồng với quỷ dữ. |
| **6** | **Ngòi nổ & Điểm gãy tâm lý (Trigger)** | `3.08` | - Tháng 1/1993: Xung đột gia đình leo thang, Paul Bernardo tấn công Karla bằng đèn pin lớn nhập viện cấp cứu.<br>- Đòn bạo lực đánh tan ảo tưởng tình yêu, kích hoạt phản ứng sinh tồn nguyên thủy: Karla bỏ trốn khỏi 57 Bayview Drive và chuẩn bị phương án phản bội để tự cứu mình. |
| **7** | **Dấu ấn Signature vs Thủ đoạn MO** | `2.07`, `2.08`, `2.09` | - **Thủ đoạn (MO - Modus Operandi):** Đe dọa, cách ly, dùng thuốc an thần động vật, dùng xi măng giấu tang vật ở kênh Lake Gibson (liên tục điều chỉnh để đối phó công an).<br>- **Dấu ấn tâm lý (Signature):** Bắt buộc phải quay video toàn bộ quá trình giam giữ; cuộn băng là **"Chiến lợi phẩm Thần kinh"** kích hoạt lại ảo tưởng quyền lực toàn năng của Paul mỗi khi xem lại, và là bằng chứng chứng nhận sự đồng lõa của Karla. |
| **8** | **Chu kỳ ảo tưởng & Quỹ đạo leo thang** | `2.02`, `2.04` | - Quỹ đạo 4 nấc thang leo thang hành vi tàn bạo trong 5 năm:<br>  * Nấc 1: Tấn công đơn lẻ đêm tối tại Scarborough (14 vụ).<br>  * Nấc 2: Thiết lập cặp đôi và xâm phạm người thân (Tammy Homolka, 1990).<br>  * Nấc 3: Bắt cóc giam giữ dài ngày tại tư gia 57 Bayview Drive (Leslie Mahaffy, 1991).<br>  * Nấc 4: Táo tợn bắt cóc công khai ban ngày tại bãi xe nhà thờ (Kristen French, 1992). |
| **9** | **Hiệu ứng Hào quang & Điểm mù xã hội** | `1.03`, `1.05`, `1.06`, `1.11`, `4.10` | - Cặp đôi Ken & Barbie tóc vàng, xe thể thao mui trần, cỗ xe ngựa cổ tích và ngôi nhà màu hồng tạo nên **Hiệu ứng Hào quang (Halo Effect)** và **Điểm mù Ngoại ô** ru ngủ trực giác cả khu phố suốt nhiều năm.<br>- Định kiến xã hội và điểm mù công tố: Cơ quan điều tra dễ tin rằng phụ nữ trẻ đẹp chỉ có thể là nạn nhân bị bạo hành, không thể là kẻ chủ mưu săn mồi máu lạnh. |
| **10** | **Nạn nhân học & Cảnh báo đỏ sinh tồn** | `2.06`, `2.07`, `5.03`, `5.06`, `5.07` | - **Tôn vinh nạn nhân:** Ghi nhận lòng dũng cảm bất khuất của Kristen French — chiến đấu quyết liệt đến hơi thở cuối cùng, để lại vết cào cấu giữ chặt mẫu ADN của Paul Bernardo làm bằng chứng pháp lý thép.<br>- **Gia đình Doug & Donna French (5.03):** Chuyển hóa nỗi đau thành *Tăng trưởng Sau Sang chấn (Post-Traumatic Growth)*, đấu tranh niêm phong tiêu hủy các cuốn băng tang vật, thành lập *Kristen French Child Advocacy Centre* bảo vệ trẻ em.<br>- **4 Cảnh báo đỏ sinh tồn (theo triết lý *The Gift of Fear*):**<br>  * Cảnh báo 1: Kẻ lạm dụng tổn thương cá nhân để biện minh cho sai trái.<br>  * Cảnh báo 2: Sự bất nhất giữa lời nói đạo đức và hành vi sau lưng.<br>  * Cảnh báo 3: Sự tiếp cận của những người có vẻ ngoài vô hại.<br>  * Cảnh báo 4: Nhận diện liên minh cộng sinh độc hại; tôn trọng trực giác bất an. |

---

## 3. Kết luận Bước 1 (Cổng kiểm duyệt kịch bản)
* Kịch bản Tập 11 đã được nâng cấp toàn diện và sâu sắc theo đúng chuẩn mực của Tập 09 và Tập 10, đáp ứng trọn vẹn yêu cầu nghiên cứu phân tích biến chuyển tâm lý của 5 chủ thể và mổ xẻ câu hỏi mấu chốt: *Tại sao lại hối hận? Cơ chế tâm lý gì ở đây?*
* Đạt 100% các tiêu chuẩn kiểm định khắt khe: Luật K1–K10, YouTube Safe V9 (0% mô tả bạo lực/gore), Chuẩn ngắt câu G1, và cân bằng phân bổ 4 vai diễn.
* Đã sẵn sàng trình duyệt để người dùng thẩm định trước khi chuyển sang các khâu đồng bộ đa ngôn ngữ và sản xuất tiếp theo.
