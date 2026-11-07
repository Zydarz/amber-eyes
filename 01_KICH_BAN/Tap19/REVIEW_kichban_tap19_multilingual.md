# BÁO CÁO THẨM TRA ĐA NGÔN NGỮ KỊCH BẢN TẬP 19 (VN · EN · JA · KO)

*Ngày lập: 07/11/2026. Phiên bản: Chuẩn A2b (Parity 1:1 tuyệt đối giữa 4 ngôn ngữ).*  
*Công cụ thẩm tra: `.work/_qc_all_4scripts_tap19.py` kết hợp thư viện `parse_kichban.py`.*

---

## 1. Bảng đo lường kỹ thuật 4 ngôn ngữ

| Tiêu chí kỹ thuật | Tiếng Việt (VN) | Tiếng Anh (EN) | Tiếng Nhật (JA) | Tiếng Hàn (KO) | Trạng thái Parity |
|---|:---:|:---:|:---:|:---:|:---:|
| **Đường dẫn kịch bản** | `01_KICH_BAN/Tap19/kichban_tap19_23102026.md` | `01_KICH_BAN/Tap19_EN/kichban_tap19_EN.md` | `01_KICH_BAN/Tap19_JA/kichban_tap19_JA.md` | `01_KICH_BAN/Tap19_KO/kichban_tap19_KO.md` | — |
| **Tổng số phần tử (Elements)** | **51** | **51** | **51** | **51** |  100% Khớp 1:1 |
| **Lượt lời thoại (LOI)** | **32** | **32** | **32** | **32** |  100% Khớp 1:1 |
| **Tổng số câu thoại (Sentences)** | **210** | **210** | **210** | **210** |  100% Khớp 1:1 |
| **Tổng số từ (Words)** | 6.299 | 3.679 | 226 | 3.075 |  Cân đối tự nhiên |
| **Lỗi từ cấm (V9)** | **0** | **0** | **0** | **0** |  100% An toàn V9 |
| **Dấu chấm lửng trong câu (G1)** | **0** | **0** | **0** | **0** |  100% Không ellipsis |
| **Kết quả kiểm thử QC** | **PASS** | **PASS** | **PASS** | **PASS** |  ALL GREEN |

---

## 2. Đối soát cấu trúc phân hồi (Act-by-Act Breakdown)

Cả 4 bản ngôn ngữ đều tuân thủ chính xác từng câu trên từng phần tử trong toàn bộ 5 hồi:

| Hồi / Màn | Elements | LOI Turns | Số câu thoại | Phân bổ vai chi tiết |
|---|:---:|:---:|:---:|---|
| **Hồi 1 / Act 1 / 第1幕 / 막 1** | 12 | 7 | **42 câu** | `1.02` (H: 7), `1.04` (H: 7), `1.06` (H: 7), `1.07` (N1: 6), `1.09` (H: 6), `1.10` (D: 5), `1.11` (H: 4) |
| **Hồi 2 / Act 2 / 第2幕 / 막 2** | 11 | 6 | **42 câu** | `2.02` (H: 7), `2.04` (H: 7), `2.06` (D: 7), `2.08` (H: 7), `2.09` (D: 7), `2.10` (H: 7) |
| **Hồi 3 / Act 3 / 第3幕 / 막 3** | 9 | 7 | **42 câu** | `3.02` (H: 5), `3.03` (C: 8), `3.04` (H: 5), `3.05` (C: 8), `3.06` (H: 5), `3.07` (C: 7), `3.08` (H: 4) |
| **Hồi 4 / Act 4 / 第4幕 / 막 4** | 13 | 8 | **42 câu** | `4.02` (H: 6), `4.04` (H: 5), `4.06` (D: 6), `4.08` (H: 5), `4.09` (N2: 6), `4.10` (D: 5), `4.11` (C: 5), `4.12` (H: 4) |
| **Hồi 5 / Act 5 / 第5幕 / 막 5** | 6 | 4 | **42 câu** | `5.02` (H: 6), `5.03` (D: 5), `5.04` (C: 7), `5.05` (H: 24) |
| **TỔNG CỘNG** | **51** | **32** | **210 câu** | **H: 128 câu (~61%) · D: 35 câu (~17%) · C: 35 câu (~17%) · N: 12 câu (~5%)** |

---

## 3. Kiểm tra tương thích cấu hình sản xuất (`edition.py`)

- **Khóa tóm tắt (`summary`):** Khóa `1.02#1` và `3.02#1` tồn tại chính xác trên cả 4 kịch bản. Khi chạy lệnh `package.py --mux` sẽ không xảy ra lỗi `KeyError`.
- **Nhân vật bình thường (`n_element`):**
  - `1.07`: Được gán cho **N1** (Học sinh sống sót thảm kịch Parkland) trên cả 4 ngôn ngữ.
  - `4.09`: Được gán cho **N2** (Bồi thẩm viên / Người quan sát phiên tòa) trên cả 4 ngôn ngữ.
- **Thẻ nhạc và hiệu ứng (`BGM` & `SFX`):** Toàn bộ nhãn hiệu ứng được giữ đồng bộ 100% bằng tiếng Anh để bộ dựng video (`build_video3.py` và `build_audio3.py`) nhận diện chính xác các cue chuyển cảnh.
- **Điểm chuyển hồi và mốc âm thanh:**
  - `act1_cue`: `1.10` tồn tại chính xác.
  - `silence_cue`: `1.06` tồn tại chính xác.
  - `click_cues`: `1.03` và `4.05` tồn tại chính xác.

---

## 4. Kết luận thẩm tra đa ngữ

- Bộ kịch bản 4 ngôn ngữ của Tập 19 đã đạt trạng thái **Parity tuyệt đối 1:1**.
- Sẵn sàng phục vụ quy trình thu âm TTS (Higgs Audio / MiniMax) và dựng timeline phụ đề độc lập cho từng thị trường (Việt Nam, Quốc tế, Nhật Bản, Hàn Quốc) mà không có bất kỳ rủi ro lệch mốc thời gian hay lỗi cú pháp nào.
