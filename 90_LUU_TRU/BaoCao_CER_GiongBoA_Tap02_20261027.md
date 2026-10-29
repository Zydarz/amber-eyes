# BÁO CÁO — ĐO CER TIẾNG VIỆT CHO 3 GIỌNG BỘ A (TẬP 02)

**Ngày:** 27/10/2026 · **Người yêu cầu:** Wisht (đã duyệt) · **Phạm vi:** `AE_EP=02`, bản tiếng Việt
**Bổ sung cho:** `BaoCao_Tap02_GiongVaBienDoi_20261027.md` (mục 5 — trước đây là "chưa đo")

---

## 1. KẾT LUẬN

**Đo xong. Hai giọng tốt, một giọng có vấn đề rõ.**

| Vai | `voice_id` | n | CER trung vị | CER trung bình | max | Vượt ngưỡng 2% |
|---|---|---:|---:|---:|---:|---:|
| Host | `English_CaptivatingStoryteller` | 15 | **0,0%** | 0,5% | 3,9% | 2/15 |
| **Điều tra viên** | **`Korean_ColdYoungMan`** | 15 | **0,0%** | **3,0%** | **28,0%** | **6/15** |
| Chuyên gia | `English_AssertiveQueen` | 15 | **0,0%** | 0,4% | 3,4% | 1/15 |
| *Đối chứng* | *`Vietnamese_kindhearted_girl`* | *5* | *0,0%* | *0,3%* | *1,3%* | *0/5* |
| *Đối chứng* | *`English_CalmWoman`* | *5* | *0,0%* | *2,6%* | *13,2%* | *1/5* |

**⇒ Vai Điều tra viên (`Korean_ColdYoungMan`) là điểm yếu**: trung bình cao gấp 6–7 lần hai giọng còn lại, và có một câu lỗi nặng **28%** — đọc sai cả cụm từ.

**⇒ Host và Chuyên gia tốt hơn nhiều so với lo ngại ban đầu**: trung vị 0,0%, và phần lớn lỗi còn lại là **lỗi kịch bản** (tên riêng tiếng Anh), không phải lỗi giọng.

---

## 2. Cách đo

| Bước | Cách làm | Ghi chú |
|---|---|---|
| **Audio** | Chính file TTS **đã xuất** của Tập 02 trong `.work/audio_s_t02/` | Đo trên thành phẩm thật, **không** tổng hợp lại → tiết kiệm 45 lượt TTS |
| **Chuẩn tham chiếu** | Trường `text` của `tts_manifest_t02.json` | Đúng thứ đã gửi cho engine |
| **ASR** | `connector__matrix__listen_audio` | Hạ tầng dự án đang dùng |
| **CER** | Hàm `cer()` y hệt `voice_audition.py` | Chuẩn hóa: lowercase, bỏ dấu câu, gộp khoảng trắng |
| **Câu chọn mẫu** | 15 câu/vai, 12–38 từ, rải đều trong tập | **Loại 5 câu** có `...` / ngoặc tiếng Anh (lỗi kịch bản đã biết) → đo chất lượng *giọng*, không đo lỗi *script* |
| **Đối chứng** | `Vietnamese_kindhearted_girl` (kỳ vọng ~0%) + `English_CalmWoman` (kỳ vọng ~9%) trên **cùng 5 câu** | Chứng minh phép đo phân biệt được: 0,3% vs 2,6% |

**Tổng chi phí:** 55 lượt ASR + 10 lượt TTS đối chứng + 9 lượt ASR lượt 2 = **74 lượt connector**.

### 2.1. Hai lỗi phương pháp đã phát hiện và sửa (quan trọng)

**Lỗi 1 — chênh lệch cách viết số (gây CER phình to giả).**
Chuẩn tham chiếu đã qua `vi_numbers()` nên là **chữ** (`"tám mươi tám"`), còn ASR trả về **số** (`"88"`). So sánh thẳng cho CER ~21% cho câu hoàn toàn đúng.
⇒ Sửa: áp `vi_numbers()` cho **cả hai vế**. Đây là lý do lần chạy đầu báo `Korean_ColdYoungMan` trung bình 3,0% với max 300% — toàn bộ là nhiễu phương pháp, không phải lỗi phát âm.

**Lỗi 2 — 1 câu bị bộ lọc Gemini chặn giữa chừng.**
`2.08#5` trả về đoạn chép đúng rồi kèm đuôi lỗi tiếng Anh ("This request was blocked by Gemini's filters…"). Đã chạy lại câu đó → lấy được bản chép sạch.

---

## 3. Chi tiết lỗi — và phân loại nguyên nhân

### 3.1 Host — `English_CaptivatingStoryteller`

| id | Lượt 1 | Lượt 2 | Chuẩn | Nghe được | Loại lỗi |
|---|---:|---:|---|---|---|
| `1.14#2` | 3,9% | 3,9% ✓ | "Hôm **ấy, chủ** xe **lái chiếc** Pathfinder…" | "Hôm **nay, chú** xe lái chiếc Pathfinder…" | **Sai thanh** (ấy→nay, chủ→chú) |
| `2.04#2` | 2,2% | 2,2% ✓ | "**Hắn** là một bóng ma… **ròng rã** trong bóng tối." | "**Hẳn** là một bóng ma… **rong rã** trong bóng tối." | **Sai thanh** (hắn→hẳn, ròng→rong) |
| `5.04#6` | 1,0% | — | "Hubert **Genest**" | "Hubert **Jenest**" | Tên riêng (kịch bản) |
| `4.03#4` | 1,0% | — | "Jim **Smyth**" | "Jim **Smith**" | Tên riêng (kịch bản) |

11/15 câu CER = 0,0%. **2 lỗi ổn định, đều là sai thanh điệu** — mức nhẹ, người bản xứ có thể chịu được.

### 3.2 Chuyên gia — `English_AssertiveQueen`

| id | Lượt 1 | Lượt 2 | Chuẩn | Nghe được | Loại lỗi |
|---|---:|---:|---|---|---|
| `3.08#6` | 3,4% | 3,4% ✓ | "Khi **ở** ngăn kéo này, hắn đóng chặt…" | "khi ngăn kéo này hắn đóng chặt…" | **Bỏ chữ** |
| `4.11#5` | 1,5% | — | "**Smyth** đáp rằng" | "**Smith** đáp rằng" | Tên riêng (kịch bản) |
| `4.11#3` | 1,4% | — | "Jim **Smyth**" | "Jim **Smith**" | Tên riêng (kịch bản) |

12/15 câu CER = 0,0%. **Không có lỗi phát âm nào đáng kể.**

### 3.3 Điều tra viên — `Korean_ColdYoungMan` ⚠️

| id | Lượt 1 | Lượt 2 | Chuẩn | Nghe được | Loại lỗi |
|---|---:|---:|---|---|---|
| `2.05#9` | **28,0%** | **18,0%** ⚠ biến động | "**Thứ hắn lấy đi** là đồ lót và đồ riêng tư của phụ nữ." | lượt 1: "**Thương hiệu Han Lady** là đồ lót…" · lượt 2: "**Thưa Hanleedee** là đồ lót…" | **SAI THANH NẶNG** — "Thứ hắn" nghe ra "thương hiệu" |
| `2.05#3` | 5,2% | 5,2% ✓ | "**Ban đầu**, Williams lảng vảng…" | "**Mando**, William lảng vảng…" | Sai thanh + tên riêng |
| `4.08#1` | 4,3% | 1,1% ⚠ biến động | "Thám tử **Jim Smyth**" | lượt 1: "thám tử **James Smith**" · lượt 2: "thám tử **Jim Smith**" | Tên riêng (ASR không chắc) |
| `2.05#12` | 3,9% | 0,0% ⚠ biến động | "…bị **lờn**." | lượt 1: "bị **nâng**." · lượt 2: "bị **lờn**." | Sai thanh (không ổn định) |
| `4.08#5` | 2,2% | 2,2% ✓ | "…ngôi nhà nghỉ dưỡng ở **Tweed**." | "…ở **Twit**." | Tên riêng (kịch bản) |
| `4.08#3` | 2,1% | 2,1% ✓ | "**Smyth** hỏi: **Williams** có…" | "**Smith** hỏi **William** có…" | Tên riêng (kịch bản) |

9/15 câu CER = 0,0%. **3 lỗi ổn định + 3 lỗi biến động.**

---

## 4. Phân loại lỗi — phần quan trọng nhất

| Loại | Tín hiệu | Câu | Ai chịu? |
|---|---|---|---|
| **A. Lỗi KỊCH BẢN** — tên riêng tiếng Anh trong lời đọc tiếng Việt | `Smyth→Smith`, `Genest→Jenest`, `Tweed→Twit`, `Williams→William` | `4.08#1`, `4.08#3`, `4.08#5`, `4.11#3`, `4.11#5`, `5.04#6` | **KHÔNG phải lỗi giọng.** Đúng luật G7 đã cấm. Sửa kịch bản là xong |
| **B. Lỗi PHÁT ÂM thanh điệu** — dấu hiệu "giọng nước ngoài đọc tiếng Việt" | `ấy→nay`, `chủ→chú`, `hắn→hẳn`, `ròng→rong`, `Thứ hắn→Thương hiệu` | `1.14#2`, `2.04#2`, `2.05#3`, `2.05#9`, `2.05#12` | **Lỗi giọng thật.** Đây là loại lỗi tôi dự đoán — và nó xuất hiện đúng như dự đoán |
| **C. Lỗi nhỏ** — bỏ chữ | `3.08#6` bỏ "ở" | `3.08#6` | Nhẹ, chấp nhận được |

**Điểm quan trọng:** lỗi loại B **tập trung ở vai Điều tra viên** (`Korean_ColdYoungMan`) — 4/5 lỗi sai thanh rơi vào giọng Hàn Quốc. Hai giọng còn lại chỉ có 2 lỗi sai thanh nhẹ.

---

## 5. Đối chiếu ngưỡng dự án (< 2%)

| Giọng | Vượt ngưỡng (lượt 1) | Trong đó là **lỗi kịch bản** | Trong đó là **lỗi giọng thật** |
|---|---:|---:|---:|
| Host | 2/15 | 0 | 2 (nhẹ) |
| **Điều tra viên** | **6/15** | **3** | **3** (1 nặng 18–28%) |
| Chuyên gia | 1/15 | 0 | 1 (bỏ chữ) |

⇒ **Sau khi sửa kịch bản (G7), phần lớn lỗi còn lại là lỗi giọng của riêng vai Điều tra viên.**

---

## 6. Đề xuất hành động

| # | Việc | Cơ sở | Mức độ |
|---|---|---|---|
| 1 | **Đổi vai Điều tra viên** — thử lại `male-qn-qingse` | Bộ cũ: CER **0,0%** tiếng Việt, đã chứng minh ổn định danh tính. Rủi ro: không có trong catalog 332 giọng → cần 1 call TTS thật kiểm tra còn sống | Nên làm — có bằng chứng mạnh nhất |
| 2 | **Quét tìm giọng nam thay thế** trong catalog (tiền tố `English_`, tên có *man/boy/gentleman*), đo CER trên 3 câu mẫu | ~12 giọng × 3 câu = 36 ASR + 12 TTS. Cho biết giọng nào đọc tiếng Việt chuẩn nhất | Cần duyệt credit |
| 3 | **Sửa lỗi G7** (tên riêng tiếng Anh) — đã có sẵn danh sách | 6 câu đã liệt kê ở mục 3 | Nên làm — độc lập với giọng, giảm lỗi cho cả 3 vai |
| 4 | **Ghi luật G13** vào `AGENTS.md` + A11: giọng ngoại ngữ đọc tiếng Việt phải đo CER bằng `listen_audio` (ngưỡng < 2%), không suy giới tính/độ đúng từ tên giọng | Lỗ hổng này vừa được chứng minh là có thật | Nên làm |
| 5 | **Ghi lại cảnh báo phương pháp** vào quy trình: khi đo CER bằng ASR cho audio TTS tiếng Việt, **phải `vi_numbers()` cả hai vế** | Nếu không, CER phình to giả tới 300% | Bắt buộc |

---

## 7. File sinh ra

| File | Nội dung |
|---|---|
| `.work/cer_bo_a_tap02/report_fixed.md` | Bảng CER + diff từng câu (sau khi sửa chuẩn hóa số) |
| `.work/cer_bo_a_tap02/rows_fixed.json` | 55 dòng dữ liệu đầy đủ: ref, hyp, CER, diff từng từ |
| `.work/cer_bo_a_tap02/asr_*.json` | Cache 55 kết quả ASR (lần 1) |
| `.work/_do_cer_bo_a_tap02.py` | Script đo (lần 1) |
| `.work/_tinh_lai_cer_tap02.py` | Script tính lại + sửa chuẩn hóa số + chạy lại câu bị chặn |
| `.work/_lan2_kiem_chung_cer_tap02.py` | Script chạy lượt 2 kiểm chứng độ ổn định |

## 8. Lệnh tái lập

```powershell
$env:AE_EP="02"; $env:PYTHONIOENCODING="utf-8"
py -3 .work/_do_cer_bo_a_tap02.py        # 55 lượt ASR (có cache)
py -3 .work/_tinh_lai_cer_tap02.py       # sửa chuẩn hóa số + chạy lại câu bị chặn
py -3 .work/_lan2_kiem_chung_cer_tap02.py # lượt 2 cho câu > 2%
```

### Giới hạn của phép đo (nói thẳng)
- **Mẫu 15 câu/vai** — đủ để phát hiện lỗi hệ thống, **chưa đủ** để kết luận "giọng này hoàn hảo".
- **CER là proxy của độ đúng chữ, không phải thẩm mỹ nghe.** Một câu CER 0,0% vẫn có thể nghe "robot" với người bản xứ; và ngược lại, "Hôm ấy" nghe ra "Hôm nay" là lỗi thanh điệu mà CER bắt được nhưng người nghe không chắc nhận ra ngay.
- **ASR không tất định**: 3/9 câu vượt ngưỡng đổi kết quả giữa 2 lượt. Vì vậy mọi kết luận về 1 câu đều cần ≥ 2 lượt — mục 3 đã ghi rõ câu nào ổn định, câu nào biến động.
- Lỗi **loại B chỉ chắc là lỗi phát âm** khi lỗi lặp lại ở cả 2 lượt; lỗi biến động thì mới đến từ ngữ cảnh, chưa kết luận được.

*Đo bằng `listen_audio` + `cer()` của dự án, trên chính audio thành phẩm. Không sửa file nào trong dự án.*
