# BÁO CÁO REVIEW TOÀN DIỆN KỊCH BẢN TẬP 13 ĐA NGÔN NGỮ (VN — EN — JA — KO)
### HỆ SINH THÁI 10 CHỈ DẤU TÂM LÝ & HÀNH VI — ĐỒNG BỘ CẤU TRÚC PARITY 1:1

> **Hồ sơ vụ án:** Vỏ Bọc 'Con Nhà Người Ta' & Lời Nói Dối 10 Năm — Hồ Sơ Jennifer Pan  
> **Thời điểm thẩm định:** 07/11/2026  
> **Căn cứ tiêu chuẩn:** `AGENTS.md` (Luật K1–K10, V9, L1–L10) và `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (§A2, §A2b, §A2c, §A9.2, Bẫy #118).  
> **Các tệp kịch bản được đánh giá:**  
> - Tiếng Việt (VN): [`01_KICH_BAN/Tap13/kichban_tap13_23102026.md`](kichban_tap13_23102026.md)  
> - Tiếng Anh (EN): [`01_KICH_BAN/Tap13_EN/kichban_tap13_EN.md`](../Tap13_EN/kichban_tap13_EN.md)  
> - Tiếng Nhật (JA): [`01_KICH_BAN/Tap13_JA/kichban_tap13_JA.md`](../Tap13_JA/kichban_tap13_JA.md)  
> - Tiếng Hàn (KO): [`01_KICH_BAN/Tap13_KO/kichban_tap13_KO.md`](../Tap13_KO/kichban_tap13_KO.md)

---

## 1. Bảng số đo kỹ thuật & Tính toàn vẹn Parity 1:1

Theo quy tắc **L3** (*"CẤM nói xong khi chưa đo. Mỗi bước báo số đo thật"*), toàn bộ 4 bản kịch bản được chạy qua parser chuẩn của pipeline (`.work/parse_kichban.py`) và công cụ kiểm thử độc lập (`.work/_qc_all_4scripts_tap13.py`):

| Thông số đo lường | Tiếng Việt (Gốc) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Mức độ đồng bộ |
|---|:---:|:---:|:---:|:---:|:---:|
| **Số Hồi (Acts)** | 5 | 5 | 5 | 5 | **Khớp 100% (5/5)** |
| **Tổng số phần tử (Elements)** | **50** | **50** | **50** | **50** | **Khớp 100% (50/50)** |
| **Lượt lời thoại (LOI)** | **31** | **31** | **31** | **31** | **Khớp 100% (31/31)** |
| **Tổng số câu đọc (Sentences)** | **210** | **210** | **210** | **210** | **Khớp 1:1 tuyệt đối** |
| **Số điểm ngắt nghỉ (NGHI)** | 1 (2.0s tại `2.12`) | 1 (2.0s) | 1 (2.0s) | 1 (2.0s) | **Khớp 100% (cùng giây)** |
| **Số cue âm thanh (BGM / SFX)** | 18 (6 BGM / 12 SFX) | 18 | 18 | 18 | **Khớp 100% vị trí & thứ tự** |
| **Dung lượng từ vựng** | 6.448 từ | 4.240 từ | 214 từ (tách từ CJK) | 3.459 từ | **Chuẩn văn phong bản địa** |
| **Lỗi từ cấm bạo lực (V9)** | **0 lỗi** | **0 lỗi** | **0 lỗi** | **0 lỗi** | **100% an toàn quảng cáo** |
| **Lỗi dấu ba chấm giữa câu (G1)** | **0 lỗi** | **0 lỗi** | **0 lỗi** | **0 lỗi** | **100% đạt chuẩn ngắt câu** |

---

## 2. Chi tiết phân bổ câu thoại theo từng Hồi & Nhân vật (Parity 1:1)

| Hồi (Act) | Element ID | Vai (Role) | Số câu (VN) | Số câu (EN) | Số câu (JA) | Số câu (KO) | Trạng thái Parity |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Hồi 1** | `1.02` | HOST | 7 | 7 | 7 | 7 | ✅ Khớp 1:1 |
| | `1.04` | HOST | 7 | 7 | 7 | 7 | ✅ Khớp 1:1 |
| | `1.06` | HOST | 7 | 7 | 7 | 7 | ✅ Khớp 1:1 |
| | `1.07` | ORDINARY PERSON (N1) | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| | `1.09` | HOST | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| | `1.10` | INVESTIGATOR | 5 | 5 | 5 | 5 | ✅ Khớp 1:1 |
| | `1.11` | HOST | 4 | 4 | 4 | 4 | ✅ Khớp 1:1 |
| *Tổng Hồi 1* | *7 lượt thoại* | | **42** | **42** | **42** | **42** | **Khớp 100%** |
| **Hồi 2** | `2.02` | HOST | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| | `2.04` | HOST | 8 | 8 | 8 | 8 | ✅ Khớp 1:1 |
| | `2.06` | INVESTIGATOR | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| | `2.08` | HOST | 7 | 7 | 7 | 7 | ✅ Khớp 1:1 |
| | `2.10` | INVESTIGATOR | 8 | 8 | 8 | 8 | ✅ Khớp 1:1 |
| | `2.11` | HOST | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| *Tổng Hồi 2* | *6 lượt thoại* | | **41** | **41** | **41** | **41** | **Khớp 100%** |
| **Hồi 3** | `3.02` | HOST | 5 | 5 | 5 | 5 | ✅ Khớp 1:1 |
| | `3.03` | PSYCHOLOGIST | 8 | 8 | 8 | 8 | ✅ Khớp 1:1 |
| | `3.04` | HOST | 5 | 5 | 5 | 5 | ✅ Khớp 1:1 |
| | `3.05` | PSYCHOLOGIST | 9 | 9 | 9 | 9 | ✅ Khớp 1:1 |
| | `3.06` | HOST | 5 | 5 | 5 | 5 | ✅ Khớp 1:1 |
| | `3.07` | PSYCHOLOGIST | 7 | 7 | 7 | 7 | ✅ Khớp 1:1 |
| | `3.08` | HOST | 4 | 4 | 4 | 4 | ✅ Khớp 1:1 |
| *Tổng Hồi 3* | *7 lượt thoại* | | **43** | **43** | **43** | **43** | **Khớp 100%** |
| **Hồi 4** | `4.02` | HOST | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| | `4.03` | INVESTIGATOR | 7 | 7 | 7 | 7 | ✅ Khớp 1:1 |
| | `4.05` | HOST | 5 | 5 | 5 | 5 | ✅ Khớp 1:1 |
| | `4.06` | ORDINARY PERSON (N2) | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| | `4.08` | INVESTIGATOR | 8 | 8 | 8 | 8 | ✅ Khớp 1:1 |
| | `4.09` | PSYCHOLOGIST | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| | `4.10` | HOST | 4 | 4 | 4 | 4 | ✅ Khớp 1:1 |
| *Tổng Hồi 4* | *7 lượt thoại* | | **42** | **42** | **42** | **42** | **Khớp 100%** |
| **Hồi 5** | `5.02` | HOST | 6 | 6 | 6 | 6 | ✅ Khớp 1:1 |
| | `5.03` | INVESTIGATOR | 5 | 5 | 5 | 5 | ✅ Khớp 1:1 |
| | `5.04` | PSYCHOLOGIST | 7 | 7 | 7 | 7 | ✅ Khớp 1:1 |
| | `5.05` | HOST | 24 | 24 | 24 | 24 | ✅ Khớp 1:1 |
| *Tổng Hồi 5* | *4 lượt thoại* | | **42** | **42** | **42** | **42** | **Khớp 100%** |
| **TOÀN TẬP** | **31 LOI turns** | | **210** | **210** | **210** | **210** | **100% KHỚP 1:1** |

---

## 3. Thẩm định tuân thủ Quy tắc Kênh và Cấu hình Pipeline

1. **Khớp 100% cấu hình `.work/edition.py` (`EPISODES['13']`):**
   - Khóa tóm tắt `summary`: `1.02#1` và `3.02#1` tồn tại và chứa nội dung chủ đạo của Hồi 1 và Hồi 3.
   - Vai nhân vật phụ `n_element`: `1.07` được gán chính xác cho `N1` (Bạn học thời phổ thông của Jennifer); `4.06` được gán chính xác cho `N2` (Ông Huei Hann Pan / Người cha sống sót).
   - Cue ngắt nghỉ âm thanh `2.12` thời lượng 2.0 giây khớp vị trí và nhịp kịch tính giữa Hồi 2 và Hồi 3.

2. **Tính chuyển dịch văn hóa & Chuẩn mực ngôn ngữ bản địa:**
   - **Bản Tiếng Anh (EN):** Sử dụng ngôn ngữ tài liệu điều tra trang trọng (formal investigative documentary tone), thuật ngữ tâm lý học chính xác (*Halo Effect, Tiger Parenting, Pathological Lying, Cognitive Compartmentalization, Minimization, Affective Empathy Deficit*).
   - **Bản Tiếng Nhật (JA):** Sử dụng thể kính ngữ và văn phong tường thuật chuyên sâu, danh xưng chính xác (*ハロー効果, タイガー・ペアレンティング, 空想虚言症, 認知的区画化, 責任の最小化*), nhãn vai chuẩn (*ホスト, 捜査官, 心理学者, 一般人*).
   - **Bản Tiếng Hàn (KO):** Sử dụng phong cách phân tích phóng sự điều tra chuẩn Hàn (*후광 효과, 타이거 패런팅, 병적 허언증, 인지적 구획화, 책임의 최소화*), nhãn vai chuẩn (*호스트, 수사관, 심리학자, 일반인*).

3. **Kết luận kiểm định:**
   Toàn bộ 4 bản kịch bản Tập 13 đã vượt qua 100% các cổng kiểm định chất lượng (All Green Passed). Sẵn sàng chuyển giao cho quy trình tổng hợp giọng đọc AI và dựng hình video.
