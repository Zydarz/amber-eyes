# -*- coding: utf-8 -*-
import sys
sys.path.append(".work")
import act_vn

header = """# KỊCH BẢN AUDIO / PODCAST TÂM LÝ HỌC TỘI PHẠM
**Chủ đề:** Hệ sinh thái 10 chỉ dấu tâm lý & Hiệu ứng hào quang (Halo Effect), Khai thác lòng trắc ẩn, Ảo tưởng toàn năng & Cơ chế hối hận giao dịch – Hồ sơ Ted Bundy và Cái bẫy của chiếc nẹp tay giả.
**Phiên bản:** Chuẩn A2c/K10 — Hệ sinh thái 10 chỉ dấu tâm lý học tội phạm & Bổ sung phân tích biến chuyển tâm lý đa chiều ngày 19/11/2026.

---

## THÔNG SỐ KỸ THUẬT & CẤU TRÚC DẪN CHUYỆN (PRODUCTION BRIEF)

| Hạng mục | Thiết lập chuẩn cho tập Audio (Host-Driven Documentary) |
| :--- | :--- |
| **Tên tập (Episode Title)** | Tập 32: Ted Bundy — Cái Bẫy Của Lòng Trắc Ẩn & Ảo Tưởng Kiểm Soát Tuyệt Đối |
| **Định dạng (Format)** | Podcast Tài liệu Điều tra (Narrator-led Documentary) – **Host** nắm giữ trục xương sống kể chuyện, kết nối dữ liệu lịch sử, điều phối nhịp cảm xúc và mời các góc nhìn chuyên môn (Điều tra viên, Chuyên gia tâm lý, Người bình thường) vào đúng điểm nút kịch tính theo Hệ sinh thái 10 chỉ dấu tâm lý. |
| **Tổng thời lượng dự kiến** | 28 – 32 phút (5 hồi nội dung + các khoảng lặng chuyển cảnh âm thanh) |
| **Nhạc nền (BGM) gợi ý** | Dark Ambient ngột ngạt, Solo Cello u uất, Tiếng đàn Dương cầm tối giản (Minimalist Piano) kết hợp nhịp Drone điện tử rùng rợn, Tiếng vĩ cầm giằng xé phòng xử án, và Warm Piano ấm áp trang nghiêm đúc kết. Âm lượng: -26dB dưới giọng đọc, nâng lên -14dB ở các điểm chuyển cảnh. |
| **Cơ chế phân bổ giọng đọc** | - **Host (~48% thời lượng):** Giọng nam trầm ấm, sâu lắng, dẫn dắt câu chuyện với góc nhìn nhân văn, dư chấn xã hội, hiệu ứng hào quang và bài học sinh tồn.<br>- **Điều tra viên (~24%):** Giọng nam đanh thép, sắc lạnh, chuẩn xác, đại diện cho hồ sơ nghiệp vụ, chứng cứ hiện trường, chữ ký Signature vs MO và chiến thuật pháp lý của cơ quan thực thi pháp luật.<br>- **Chuyên gia tâm lý (~22%):** Giọng điềm đạm, mang tính học thuật sâu sắc, bóc tách ái kỷ ác tính, thấu cảm nhận thức săn mồi, sự chia ngăn tâm trí và bản chất của cơ chế hối hận giao dịch.<br>- **Người bình thường (~6%):** N1 (Carol DaRonch - Hồi 1, 6 câu) giọng nữ trẻ hoang mang nhưng kiên cường; N2 (Carole Ann Boone - Hồi 4, 8 câu) giọng nữ trung niên run rẩy, giằng xé tội lỗi tột cùng. |
| **Quy tắc trích dẫn** | Mọi trích dẫn nguyên văn trong hình phải đúng 100% so với nguồn lưu trữ. Quy ước ký hiệu: ngoặc kép “ ” = trích dẫn nguyên văn. |
| **Nguồn đối chiếu chính** | Hồ sơ Cục Điều tra Liên bang FBI (Hồ sơ Ted Bundy, Đặc vụ Bill Hagmaier) · Hồ sơ Tòa án Tối cao Bang Florida (Vụ án Chi Omega & Kimberly Leach, Thẩm phán Edward Cowart) · Lời khai của nạn nhân sống sót Carol DaRonch tại Tòa án Bang Utah · Hồi ký *The Stranger Beside Me* (Ann Rule, 1980) · Hồi ký *The Phantom Prince: My Life with Ted Bundy* (Elizabeth Kloepfer / Kendall, 1981) · Nghiên cứu Bảng kiểm Bệnh thái nhân cách PCL-R (Tiến sĩ Robert Hare) · Học thuyết *The Gift of Fear* (Gavin de Becker, 1997). |

---

---
"""

full_vn = "\n\n".join([header, act_vn.ACT1_VN, act_vn.ACT2_VN, act_vn.ACT3_VN, act_vn.ACT4_VN, act_vn.ACT5_VN])
with open("01_KICH_BAN/Tap32/kichban_tap32_19112026.md", "w", encoding="utf-8") as f:
    f.write(full_vn)

import subprocess, json
subprocess.run(["py", "-3", ".work/parse_kichban.py", "01_KICH_BAN/Tap32/kichban_tap32_19112026.md", ".work/t32_vn.json"])
d = json.load(open(".work/t32_vn.json", encoding="utf-8"))
total_sents = sum(len(x.get("sentences", [])) for x in d)
print("Generated VN sentences count:", total_sents)
