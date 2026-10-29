# Báo cáo cập nhật file luật sau vòng đo giọng Tập 02 — 27/10/2026

**Phạm vi:** chỉ sửa **file luật** (`AGENTS.md` + `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md`). **Không sửa code dự án** — `edition.py` vẫn giữ `Korean_ColdYoungMan` cho vai Điều tra viên.

---

## 1. `AGENTS.md` (25.579 bytes) — sửa 6 vị trí

| Vị trí | Nội dung ghi | Vì sao |
|---|---|---|
| Mục 4 — bảng "Ba bộ giọng" | Thêm cột **CER đo (T2, 20 câu)**; tách rõ **bộ A / bộ EN / bộ Tập 01 ghim** | Trước đó chỉ ghi `voice_id` + tốc độ, không có số đo nào về chất lượng đọc tiếng Việt |
| Mục 4 — ghi chú | 1 giọng Việt gốc duy nhất; tiền tố `English_`/`Korean_` là ngôn ngữ *gốc*; **cảnh báo vai Điều tra viên là điểm yếu** (3,1%, max 28,6%) | Chặn lại suy luận sai "giọng `English_` không đọc được tiếng Việt" |
| Mục 4 — luật mới | **G12** (đo CER < 2% cho giọng ngoại ngữ đọc tiếng Việt; cấm suy giới tính/độ đúng chữ từ tên) | G8–G10 chỉ đo *danh tính* + *tách bạch*, không đo *đọc đúng tiếng Việt chưa* |
| Mục 4 — luật mới | **G13** (chọn giọng mới qua 4 lớp có số đo: CER → G8 → G9 → nghe thử bản dựng thật) | Điểm hợp vai 9/10 từng thắng nhưng vi phạm G9 → đảo thứ tự ưu tiên đo |
| Mục 7 — Q3 viết lại | 3 lỗi đo: số → `vi_numbers()` **cả hai vế**; bộ lọc Gemini `code=0`; câu < 12 từ | Một câu đúng bị tính 21,4% CER, một câu 300% nếu không chuẩn hoá |
| Mục 7 — Q6 mới | ASR không tất định → ≥ 2 lượt cho mọi kết luận về 1 câu | 3/9 câu đổi kết quả giữa 2 lượt |
| Mục 8 — T8, T9 mới | T8: `batch_text_to_audio` max **10 request/lượt**. T9: `pitch` = đổi **âm sắc**, không phải chỉnh F0; endpoint không có tham số `language` | Gửi 51 request → lỗi không nói nguyên nhân; `pitch` là gốc rễ của G5 |
| Mục 4 — mục "Chọn giọng mới" | Code **KHÔNG** gọi `get_voice_list`; vắng mặt ≠ chết; mẫu 20 câu đúng emotion/speed production; đo trên file đã xuất thì không cần tổng hợp lại | Tài liệu cũ mô tả sai luồng thật |

## 2. `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (62.651 bytes) — sửa 3 vị trí

| Vị trí | Nội dung ghi |
|---|---|
| **A4.1** | Bảng 5 giọng có thêm cột **CER đo** + F0 đo chính xác; thêm mục "Ba bộ giọng của kênh"; sửa câu *"Kho giọng chỉ có MỘT giọng tiếng Việt gốc"* → giải thích cơ chế đa ngôn ngữ; thêm "Ba vai chính nghe mù xen kẽ (Tập 07): tách bạch 10/10" |
| **A4.1b** (mục mới) | "ĐO CHẤT LƯỢNG PHÁT ÂM TIẾNG VIỆT — CER": bảng 8 bước tái lập được (kèm 3 cảnh báo đo lỗi) · kết quả 3 vai · kết quả 5 ứng viên · kết quả G8/G9 mù · ghi chú loại 2 ứng viên · kiểm sống 2 giọng legacy · phạm vi áp dụng Tập 08–29 · link 2 báo cáo |
| **A11** | Thêm **7 bẫy mới #43–#49**; sửa thứ tự bảng (23 → 25 → 24 về 23 → 24 → 25) |

### 7 bẫy mới trong A11

| # | Bẫy | Cách làm đúng |
|---|---|---|
| 43 | `batch_text_to_audio` max 10 request/lượt, lỗi không nói rõ nguyên nhân | Chia chunk 10; đọc `success_items[]` từng batch |
| 44 | Đo CER không chuẩn hoá số ở cả hai vế → phình to giả (21% / 300%) | `vi_numbers()` cho cả `ref` lẫn `hyp` |
| 45 | Bộ lọc Gemini chặn câu nhưng `code` vẫn `0` | Đọc nội dung `transcription`, cắt đuôi, loại câu khỏi mẫu |
| 46 | Vắng mặt trong `get_voice_list` ≠ giọng chết | Chỉ kết luận "chết" sau 1 lần gọi TTS thật |
| 47 | `pitch` = đổi âm sắc (timbre), không phải chỉnh F0 | Đổi F0 bằng `voice_id` + đo lại |
| 48 | ASR không tất định; `audios_understand` đổi verdict 10/45 file | ≥ 2 lượt cho kết luận từng câu; verdict AI là tín hiệu mềm |
| 49 | Đoán giới tính giọng từ tên → sai; đo F0 trên master có nhạc → nhiễu | Đo F0 thật, chỉ trên file TTS rời |

## 3. Bản sao lưu

| File | Vị trí | Ghi chú |
|---|---|---|
| `AGENTS.md.sau_27102026` | `.work/_cu/` | Trạng thái **sau** khi sửa |
| `TIEU_CHUAN_DUNG_VIDEO.md.sau_27102026` | `.work/_cu/` | Trạng thái **sau** khi sửa |
| `TIEU_CHUAN_DUNG_VIDEO.md.bak_25102026` | `.work/_cu/` | Bản **trước** mọi thay đổi hôm nay (25/10) — điểm khôi phục duy nhất cho tiêu chuẩn |

⚠ **Thiếu sót cần báo:** phiên này sửa 2 file luật **không có bản sao trước khi sửa** cho `AGENTS.md` (tiêu chuẩn thì có, bản 25/10). Bản sao chỉ tạo được *sau khi* sửa. Từ lượt này trở đi: sao lưu **trước** khi ghi đè.

## 4. Kiểm tra đã chạy

- Thứ tự bảng A11: đọc lại từ file → `1,2,…,49` liên tục, không thiếu, không trùng.
- Số cột bảng A11: mọi dòng có 4 dấu `|` (3 cột) — dòng #40 có `\|` đã escape ⇒ không vỡ markdown.
- Thứ tự luật trong `AGENTS.md`: G1–G13 · Q1–Q6 · T1–T9 — liên tục, không lệch.
- 11 file báo cáo + 2 file luật: đã verify tồn tại trên đĩa (kèm byte size).

**Chưa kiểm được:** không có công cụ render markdown nên chưa soi bằng mắt bảng render cuối cùng trên GitHub/VS Code; đã kiểm bằng đếm ký tự `|` và quét regex.

## 5. Chưa làm (cần người dùng quyết)

- **Không sửa `edition.py`** → vai Điều tra viên vẫn là `Korean_ColdYoungMan` (L4: đổi giọng cần đồng ý).
- Chưa nghe thử bản dựng thật của `English_Diligent_Man` (lớp 4 của G13) → chưa đủ điều kiện đổi giọng theo G13.
