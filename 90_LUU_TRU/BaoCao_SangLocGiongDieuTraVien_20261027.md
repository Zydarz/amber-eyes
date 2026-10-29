# BÁO CÁO — SÀNG LỌC GIỌNG THAY THẾ CHO VAI "ĐIỀU TRA VIÊN" (Tập 02)

**Ngày:** 27/10/2026 · **Người yêu cầu:** Wisht (đã duyệt) · **Phạm vi:** `AE_EP=02`, bản tiếng Việt
**Bổ sung cho:** `BaoCao_CER_GiongBoA_Tap02_20261027.md` (mục 6 — đề xuất "đổi vai Điều tra viên")

---

## 1. KẾT LUẬN

**Giọng `Korean_ColdYoungMan` (đang dùng cho vai Điều tra viên) LÀ ĐIỂM YẾU CỦA BỘ A — và có 3 ứng viên thay thế tốt hơn, đã đo đủ 4 tiêu chí.**

**Khuyến nghị: đổi vai Điều tra viên sang `English_Diligent_Man` kể từ Tập 08.**
Tập 03–07 đã có master (đã xuất) nên **không cần dựng lại video nào**; Tập 08–29 (22 tập) còn nguyên.

| Tiêu chí | `Korean_ColdYoungMan` (đang dùng) | **`English_Diligent_Man`** (khuyến nghị) |
|---|---|---|
| CER tiếng Việt (20 câu vai D) | 3,1% tb · max **28,6%** | **0,6%** tb · max **6,0%** |
| Số câu vượt ngưỡng 2% | 4/20 | **2/19** |
| G8 — danh tính giữ nguyên khi đổi cảm xúc | *(chưa đo riêng)* | ✅ 1 người |
| G9 — tách bạch với Host + Chuyên gia | **8–9/10** | ✅ 9/10 |
| F0 (so với Host 103 Hz) | 140 Hz (+5,4 nc) | **158 Hz (+7,7 nc)** |
| Độ ổn định F0 (dao động) | **17 Hz** (ổn định nhất) | 55 Hz |
| Có trong catalog 332 giọng? | ✅ | ✅ |

**Ngoại lệ cần cân nhắc:** `English_Diligent_Man` dao động F0 55 Hz (133–188) vs giọng hiện tại 17 Hz. Chưa có dữ liệu nào cho thấy người nghe thấy "đổi người" ở mức này (G8 mù → 1 người), nhưng **nên nghe thử bản dựng thật** trước khi áp dụng cho 22 tập.

---

## 2. Ba vai, cùng cỡ mẫu 20 câu — audio thành phẩm Tập 02

| Vai | `voice_id` | CER tb | median | max | >2% | F0 |
|---|---|---:|---:|---:|---:|---:|
| Host | `English_CaptivatingStoryteller` | **0,1%** | 0,0% | 2,0% | **0/20** | 103 Hz |
| **Điều tra viên** | **`Korean_ColdYoungMan`** | **3,1%** | 0,0% | **28,6%** | 4/20 | 140 Hz |
| Chuyên gia | `English_AssertiveQueen` | 0,9% | 0,0% | 5,4% | 4/20 | 203 Hz |

⇒ **Host gần như hoàn hảo** (0,1%, không câu nào vượt ngưỡng). **Chuyên gia tốt** (0,9%). **Điều tra viên là vết thương rõ ràng** — trung bình gấp 3 lần Chuyên gia và gấp 30 lần Host.

---

## 3. Năm ứng viên, cùng 20 câu vai D

TTS mới với **đúng emotion/speed của từng câu** trong manifest (giai lap production).

| # | `voice_id` | CER tb | max | >2% | F0 | cách Host | dao động F0 | G8 | G9 | catalog |
|---|---|---:|---:|---:|---:|---:|---:|---|---|---|
| 1 | **`English_Diligent_Man`** | **0,6%** | 6,0% | 2/19 | 158 Hz | **+7,7 nc** | 55 Hz | ✅ 1 | 9/10 | ✅ |
| 2 | `male-qn-qingse` | **0,6%** | 9,5% | 2/20 | 137 Hz | +5,0 nc | 44 Hz | ✅ 1 | **10/10** | ❌ (nhưng **còn sống**) |
| 3 | `English_DecentYoungMan` | 0,6% | 4,0% | 3/19 | 128 Hz | **+3,8 nc ✗** | 75 Hz | ✅ 1 | **10/10** | ✅ |
| 4 | `Korean_CockyGuy` | 1,6% | 20,0% | 3/20 | 152 Hz | +6,8 nc | 76 Hz | ✅ 1 | 9/10 | ✅ |
| 5 | `Korean_ColdYoungMan` *(đang dùng)* | 3,1% | 28,6% | 4/20 | 140 Hz | +5,4 nc | **17 Hz** | — | 8–9/10 | ✅ |

**Ghi chú về ứng viên bị loại:**
- `English_DecentYoungMan` — G9 mù đạt 10/10 nhưng **F0 128 Hz chỉ cách Host +3,8 nửa cung < 4** ⇒ vi phạm G9 về số đo.
- `Korean_CockyGuy` — dao động F0 **76 Hz** (cao nhất), lệch "chất giọng" rõ nhất.
- `audiobook_male_1` — CER 0,0% nhưng **F0 116 Hz chỉ cách Host +2,0 nửa cung** (G9 fail) **và** đã bị dự án loại vì đổi danh tính khi đổi cảm xúc (tiêu chuẩn A4.2 G5).

---

## 4. Sàng lọc 13 giọng nam (bước đầu, 2 câu khó nhất)

Đo trên 2 câu khó đã biết (`2.05#9` "Thứ hắn lấy đi…", `2.05#12` "…bị lờn"):

| # | `voice_id` | CER tb | max | F0 |
|---|---|---:|---:|---:|
| 1 | `audiobook_male_1` | 0,0% | 0,0% | 116 Hz |
| 2 | **`English_Diligent_Man`** | **0,0%** | 0,0% | 164 Hz |
| 3 | **`English_DecentYoungMan`** | **0,0%** | 0,0% | 147 Hz |
| 4 | **`Korean_CockyGuy`** | **0,0%** | 0,0% | 155 Hz |
| 5 | `male-qn-qingse` | 0,6% | 1,3% | 136 Hz |
| 6 | `English_ReservedYoungMan` | 2,0% | 4,0% | 122 Hz |
| 7 | `English_PatientMan` | 3,0% | 6,0% | 123 Hz |
| 8 | `Korean_DominantMan` | 7,0% | 14,0% | 127 Hz |
| 9 | `Korean_CalmGentleman` | 7,9% | 12,0% | 106 Hz |
| 10 | **`Korean_ColdYoungMan` (đang dùng)** | **8,0%** | 16,0% | 144 Hz |
| 11 | `English_FriendlyPerson` | 9,0% | 18,0% | 111 Hz |
| 12 | `English_Steadymentor` | 10,0% | 20,0% | 114 Hz |
| 13 | `Korean_IntellectualMan` | 10,6% | 20,0% | 108 Hz |

Từ catalog 332 giọng có **82 giọng nam**; mình chọn 10 ứng viên có tính cách đúng vai Sói (trầm vừa, không phải bass) + 2 giọng legacy.

### 4.1. Kiểm tra sống của 2 giọng legacy (không có trong catalog)
| `voice_id` | Kết quả TTS hôm nay |
|---|---|
| `male-qn-qingse` | ✅ **CÒN SỐNG** — 2/2 câu thành công |
| `audiobook_male_1` | ✅ **CÒN SỐNG** — 2/2 câu thành công |

⇒ Loại được rủi ro "giọng đã chết". `male-qn-qingse` vẫn là **schema default** của endpoint TTS nên chắc chắn còn hỗ trợ.

---

## 5. Bằng chứng G8 + G9 (nghe mù bằng `audios_understand`, đúng cách dự án làm)

**G8** — gộp 12 câu của một giọng, hỏi "SPEAKERS: n" (đạt = 1 người).
**G9** — xen kẽ Host · Điều tra viên · Chuyên gia (12 câu), hỏi "SPEAKERS: n" + rating tách bạch 1–10.

| `voice_id` | G8 | G9 | Mô tả mô hình nghe mù | Rating |
|---|---|---|---|---|
| `Korean_ColdYoungMan` *(đang dùng)* | — | 3 ✓ | *"cả ba chia sẻ cùng một nhịp đọc tin không cảm xúc, hơi khó phân biệt là 3 người khác nhau"* | **8/10** (lượt trước 9/10) |
| `English_Diligent_Man` | ✅ 1 | 3 ✓ | S1 mature/authoritative · S2 clear/informative/analytical · S3 precise/intellectual | **9/10** |
| `Korean_CockyGuy` | ✅ 1 | 3 ✓ | S1 deep/warm storyteller · S2 clear/measured/masculine · S3 calm/feminine | 9/10 |
| `English_DecentYoungMan` | ✅ 1 | 3 ✓ | S1 deep/resonant/formal · S2 clear/expressive/storytelling · S3 calm/articulate/female | **10/10** |
| `male-qn-qingse` | ✅ 1 | 3 ✓ | S1 deep/resonant/mature · S2 clear/steady/**natural** · S3 smooth/articulate/female | **10/10** |

⇒ **Mọi ứng viên đều đạt G8 và G9.** Giọng **đang dùng** là giọng bị chấm *thấp nhất* về khả năng phân biệt — vì cả 3 vai đều dùng giọng **Hàn Quốc/English** cùng một nhịp đọc "tin không cảm xúc".

---

## 6. Sai lệch của chính AI trong lượt này (AGENTS.md §10)

| # | Sai lệch | Nguyên nhân gốc | Đã sửa |
|---|---|---|---|
| 1 | `batch_text_to_audio` báo lỗi khi gửi 51 request | **Schema giới hạn `maxItems: 10` mỗi lượt gọi** | Chia batch 10 request/lượt → chạy lại, OK |
| 2 | 2 câu có **CER 100%** | `transcription` bị **bộ lọc Gemini chặn** (câu *"Xâm nhập khi có người ở nhà"*), `code` vẫn là `0` | Phát hiện qua raw JSON, loại khỏi mẫu, tính lại |
| 3 | Báo cáo trước ghi `Korean_ColdYoungMan` = 3,0% trên **15 câu** | Mẫu 15 câu **cố tình lấy câu khó** → phóng đại | Đo đủ **51 câu** vai D = **1,7%** tb; và 20 câu cùng mẫu với ứng viên = 3,1% |
| 4 | Lần đầu báo "2 giọng legacy có thể đã chết" | Chỉ suy từ danh mục live | Đã kiểm tra bằng TTS thật → **cả 2 còn sống** |
| 5 | Script G8/G9 chạy ra 0 ứng viên | Đọc nhầm `rows.json` thay vì `rows2.json` | Sửa → 4 ứng viên đều được test |

---

## 7. Đề xuất hành động

| # | Việc | Cơ sở | Mức độ |
|---|---|---|---|
| 1 | **Đổi vai Điều tra viên → `English_Diligent_Man` cho Tập 08 trở đi** | CER 0,6% (thấp nhất), G8 ✅, G9 9/10, cách Host +7,7 nc, có trong catalog | **Cao** — không tốn dựng lại Tập 03–07 đã xuất |
| 2 | **Nghe thử 1 bản dựng thật** của `English_Diligent_Man` với đủ cảm xúc trước khi áp dụng cho 22 tập | Dao động F0 55 Hz vs 17 Hz của giọng hiện tại — G8 mù đạt nhưng chưa có bản dựng thật để nghe | **Bắt buộc** |
| 3 | **Dựng lại Tập 02 nếu muốn đồng bộ** | Hiện Tập 02 đã xuất với giọng cũ; đổi giọng = đọc lại 51 câu + dựng lại video (~1 giờ) | Tùy — có thể bỏ |
| 4 | **Giữ `male-qn-qingse` làm phương án dự phòng** | CER 0,6%, G9 10/10, còn sống — nhưng có tiền sử bị loại: *"giọng nam Mandarin; phát âm tiếng Việt ở mức chấp nhận được nhưng **không tự nhiên**"* (`90_LUU_TRU/ke_hoach_cu/KeHoach_ThuAm_Tap01.md:80`) | Tham khảo |
| 5 | **Sửa lỗi G7** (tên riêng tiếng Anh trong lời đọc) — 46 câu trên Tập 01–05 | Độc lập với giọng, giảm lỗi cho cả 3 vai | Nên làm |
| 6 | **Ghi luật G13** + cảnh báo phương pháp `vi_numbers()` vào `AGENTS.md` / A11 | Lỗ hổng đã được chứng minh có thật | Nên làm |
| 7 | **Không cần** đổi Host hay Chuyên gia | Host 0,1% (0/20 vượt ngưỡng), Chuyên gia 0,9% | — |

### 7.1. Rủi ro cần nói thẳng khi đổi sang giọng English
Hiện 2 vai nam là **1 English + 1 Korean** → khán giả Việt nghe 2 "accent" khác nhau. Nếu đổi D sang English, **cả 2 vai nam cùng nét English** ⇒ giảm khác biệt về *accent* (dù mô hình nghe mù vẫn chấm tách bạch 9/10 về *timbre*).
Vì vậy **bước 2 ở trên không được bỏ**: nghe thử bản dựng thật và tự đánh giá độ khác biệt accent với Host.

---

## 8. Giới hạn của phép đo

- **Mẫu 20 câu/vai** cho ứng viên (51 câu cho baseline vai D). Đủ để phân biệt rõ, **chưa đủ** để khẳng định "giọng này hoàn hảo".
- **CER là proxy của độ đúng chữ, không phải thẩm mỹ nghe.** Bằng chứng mạnh nhất: dự án đã nghe thật và loại `male-qn-qingse` vì *"không tự nhiên"* dù CER 0,0%.
- **ASR không tất định**: 3/9 câu vượt ngưỡng đổi kết quả giữa 2 lượt; G9 rating của baseline đổi 8→9 giữa 2 lượt. Mọi kết luận về 1 câu cần ≥ 2 lượt.
- **Câu ngắn phóng đại tỉ lệ lỗi**: `2.05#2` chỉ 6 từ → 1 lỗi = 20%+ CER.
- **Bộ lọc nội dung của Gemini có thể chặn câu** về nội dung nhạy cảm ("Xâm nhập khi có người ở nhà") với `code = 0` ⇒ phải kiểm `transcription` chứ không chỉ mã lỗi.

---

## 9. File sinh ra

| File | Nội dung |
|---|---|
| `.work/cer_sang_loc_giong_nam/report.md` | Sàng lọc 13 giọng nam (2 câu) |
| `.work/cer_xac_minh_giong_nam/report2.md` | Xác minh 4 ứng viên + baseline (20 câu) |
| `.work/cer_xac_minh_giong_nam/report_final.md` | Tổng hợp có tách câu ngắn |
| `.work/cer_xac_minh_giong_nam/rows2.json` | Dữ liệu đầy đủ 100 dòng (ref/hyp/CER/F0) |
| `.work/cer_xac_minh_giong_nam/rows_hc.json` | Dữ liệu 40 câu Host + Chuyên gia |
| `.work/g8_g9_kiem_tra_giong/report.md` | G8/G9 nghe mù — baseline + 4 ứng viên |
| `.work/g8_g9_kiem_tra_giong/results.json` | Kết quả G8/G9 dạng máy |
| `.work/_sang_loc_giong_nam.py` · `_xac_minh_giong_nam_fix.py` · `_g8_g9_kiem_tra_giong.py` · `_do_cer_H_C_20cau.py` · `_phan_tich_on_dinh_f0.py` | Script tái lập |

## 10. Lệnh tái lập

```powershell
$env:AE_EP="02"; $env:PYTHONIOENCODING="utf-8"
py -3 .work/_sang_loc_giong_nam.py       # sàng lọc 13 giọng nam
py -3 .work/_xac_minh_giong_nam_fix.py   # xác minh 4 ứng viên, 20 câu
py -3 .work/_do_cer_H_C_20cau.py         # Host + Chuyên gia
py -3 .work/_phan_tich_on_dinh_f0.py     # ổn định F0 theo cảm xúc (G8 sơ bộ)
py -3 .work/_g8_g9_kiem_tra_giong.py    # G8/G9 nghe mù
```

**Chi phí lượt này:** ~13 lượt TTS (đối chứng) + ~90 lượt ASR + ~150 lượt TTS ứng viên + 10 lượt `audios_understand` ≈ **260 lượt connector**.

*Không sửa file nào trong dự án. Không đổi giọng nào trong code.*
