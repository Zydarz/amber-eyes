# BÁO CÁO NGUYÊN NHÂN GỐC — GIỌNG ĐỌC TẬP 02

*23/10/2026. Phản hồi của người dùng sau khi nghe `Tap02_master.mp4`:*
1. *Giọng Host liên tục thay đổi, nghe như có tới 3 người, không phải do biến tần âm thanh.*
2. *Các giọng nam gần như giống hệt nhau.*
3. *Muốn giọng Host kiểu podcast, cuốn hút.*

## Tóm tắt

| # | Nguyên nhân gốc | Bằng chứng chính |
|---|---|---|
| **1** | **Giọng Host `audiobook_male_1` đổi "danh tính" mỗi khi đổi tham số cảm xúc hoặc cao độ.** Tập 02 dùng 15 tổ hợp cảm xúc × cao độ cho Host, nên nghe như nhiều người | Cùng một câu, 7 thiết lập → mô hình nghe mù nhận ra **6 người khác nhau**. Chỉ đọc `neutral` + cao độ 0 → **1 người** |
| **2** | **Hai giọng nam chọn trùng vùng giọng:** cùng baritone, cùng giọng miền Nam, cao độ chỉ cách ~2 nửa cung | Host 111–115 Hz · Điều tra viên 129–131 Hz. Khi Host đọc `surprised`/`happy`, cao độ vọt lên 150–176 Hz, **vượt cả** Điều tra viên |
| **3** | **Quy trình thử giọng thiếu hai phép kiểm:** độ ổn định danh tính qua các câu, và độ khác biệt giữa các vai | Tiêu chuẩn A4.2 (viết 23/10) chỉ đo biểu cảm, nhịp và CER **trên từng câu riêng lẻ**. Không ai nghe 2 câu liền nhau của cùng một vai |
| **4** | **Sửa lỗi "đều đều" của Tập 01 đã gây ra lỗi "đổi giọng" ở Tập 02.** Tập 01 chỉ dùng neutral/sad + cao độ 0 nên ổn định nhưng phẳng; Tập 02 thêm cảm xúc và cao độ để có biểu cảm, mà không kiểm xem giọng có giữ được danh tính không | Host Tập 01 nghe mù: **1 người** |

Lỗi nằm ở **quyết định của tôi khi soạn quy tắc diễn xuất** (A4.2: G3 đổi cảm xúc theo nhịp, G5 cao độ −4…+3) và ở **quy trình thử giọng**, không phải ở khâu trộn âm hay biến tần.

---

## 1. Bằng chứng

Mọi file nghe nằm ở `02_SAN_XUAT/Tap02/thu_giong_baocao/`. Mỗi file được cho mô hình nhận dạng âm thanh nghe **mù**, chỉ hỏi về danh tính người nói (bỏ qua lời): có mấy người, câu nào là ai, giọng vùng nào.

### 1.1 Phép thử có kiểm soát — cùng một câu, đổi từng tham số (`1_cung_cau_10_thiet_lap.mp3`)

Câu: *"Tại căn cứ Không quân Trenton, căn cứ không quân lớn nhất của quân đội Canada."*, tốc độ 0,88.

| # | Giọng | Cảm xúc | Cao độ | F0 đo được | Mô hình nghe ra |
|---|---|---|---:|---:|---|
| 1 | Host `audiobook_male_1` | neutral | 0 | 115 Hz | Người A — ấm, mượt, trong |
| 2 | Host | neutral | −1 | 110 Hz | **Người B** — vang, trầm |
| 3 | Host | neutral | −2 | 108 Hz | **Người C** — khàn, nặng, tối |
| 4 | Host | neutral | +1 | 150 Hz | **Người D** — nhẹ, trẻ, sáng |
| 5 | Host | surprised | 0 | 176 Hz | **Người E** — hăng hái |
| 6 | Host | happy | 0 | 167 Hz | Người E |
| 7 | Host | sad | 0 | 123 Hz | **Người F** — hơi thở, khàn, nhỏ |
| 8 | Điều tra viên `male-qn-qingse` | neutral | 0 | 131 Hz | Người G |
| 9 | Điều tra viên | neutral | −1 | 134 Hz | Người G |
| 10 | Điều tra viên | neutral | −2 | 128 Hz | Người G |

**Kết luận:**
- Với Host, **mọi** thay đổi tham số đều thành một người khác.
- Tham số cao độ +1 đẩy F0 lên **+4,5 nửa cung**; cảm xúc surprised/happy đẩy lên **+7 nửa cung**. Giọng không chỉ cao lên mà **đổi cả âm sắc**.
- Điều tra viên giữ nguyên danh tính khi đổi cao độ. Vậy độ ổn định **khác nhau theo từng giọng**, phải thử riêng từng giọng.

### 1.2 Host trong video thật

| File | Nội dung | Mô hình nghe ra |
|---|---|---|
| `4_host_tap01.mp3` | 8 câu Host Tập 01 (neutral/sad, cao độ 0) | **1 người**, miền Nam |
| `3_host_tap02_chi_neutral.mp3` | 8 câu Host Tập 02, chỉ neutral + cao độ 0 | **1 người**, miền Nam |
| `2_host_tap02_cam_xuc_tron.mp3` | 8 câu Host Tập 02, trộn cảm xúc và cao độ | **2 người, khác cả vùng miền**: A "miền Bắc, trầm khàn" ↔ B "miền Nam, trong" |

Ở file 2, cả 4 câu bị nghe thành "người A" đều có cao độ −1/−2; cả 4 câu "người B" có cao độ 0/+1. Trong toàn tập, Host dùng **15 tổ hợp** cảm xúc × cao độ:

| Tổ hợp | Số câu |
|---|---:|
| neutral −1 | 30 |
| neutral 0 | 24 |
| sad −1 | 8 |
| happy +1 | 5 |
| 11 tổ hợp còn lại | 31 |
| **Tổng** | **98** |

Vì vậy người nghe nhận ra khoảng 3 "người".

### 1.3 Hai giọng nam (`5_host_xen_dieu_tra_vien.mp3`)

Host và Điều tra viên đọc xen kẽ, đều ở neutral. Mô hình **có** phân biệt được: Host "trầm, trang nghiêm", Điều tra viên "trong, sáng hơn". Nhưng đó là khi Host đọc neutral. Số đo toàn tập:

| Vai | F0 trung vị | Dải 5–95% | Độ sáng âm sắc |
|---|---:|---:|---:|
| Host | 111 Hz | 96–159 Hz | 1.345 Hz |
| Điều tra viên | 129 Hz | 116–160 Hz | 1.686 Hz |

Hai dải cao độ **chồng lên nhau** gần như hoàn toàn trong khoảng 116–159 Hz. Khi Host đọc câu surprised/happy (lên 142–208 Hz), Host nghe trẻ và sáng hơn chính Điều tra viên. Cùng chất giọng baritone miền Nam, nên tai người nghe khó tách hai vai, nhất là khi không nhìn hình.

---

## 2. Vì sao lỗi lọt qua

| Khâu | Đã kiểm | Thiếu |
|---|---|---|
| Thử giọng 22/10 (`voice_test5`) | CER từng giọng, 1 câu/giọng | Độ ổn định, khác biệt giữa vai |
| Thử diễn xuất 23/10 (3 vòng, 74 bản) | Biểu cảm, nhịp, thanh điệu, CER — **so các bản của cùng một câu** | Nghe **nhiều câu liền nhau** của một vai với tham số khác nhau. Chính phép so "cùng câu" đã che lỗi: người chấm nghe như những "phiên bản diễn" khác nhau, không như những người khác nhau |
| Tiêu chuẩn A4.2 (G3, G5) | Cho phép đổi cảm xúc theo nhịp, cao độ −4…+3 | Không có điều kiện "giọng phải giữ danh tính" |
| Duyệt cuối | Hình, tiếng, khoảng lặng, độ to | Không nghe liền một đoạn dài theo từng vai |

---

## 3. Đề xuất sửa (chưa làm — chờ người dùng đồng ý)

### 3.1 Quy tắc mới cho tiêu chuẩn (bổ sung A4.2)

- **G8 — Ổn định danh tính.** Mỗi giọng có một **bộ tham số an toàn**, đo bằng phép thử 1.1: cùng một câu, đổi từng tham số; chỉ giữ tham số mà mô hình nghe mù vẫn nhận là cùng người.
  - Với `audiobook_male_1`, bộ an toàn chỉ có: **neutral, cao độ 0**.
  - Biểu cảm của Host lấy từ tốc độ (±0,04), khoảng lặng giữa câu, nhạc, tiếng động và cách viết câu, **không** lấy từ tham số cảm xúc hay cao độ.
- **G9 — Khác biệt giữa các vai.**
  - Hai giọng cùng giới phải cách nhau **≥ 4 nửa cung** F0 trung vị, **và** khác nhau rõ về âm sắc hoặc tuổi hoặc vùng miền.
  - Kiểm bằng file xen kẽ 2 vai × 4 câu: mô hình nghe mù phải gán đúng 8/8.
- **G10 — Nghe liền theo vai trước khi dựng.** Sau khi đọc toàn tập, ghép 10–12 câu rải đều của mỗi vai thành một file. Mô hình phải nghe ra **1 người**. Đạt mới được chạy `build_audio3`.

### 3.2 Giọng Host kiểu podcast cuốn hút

Kho giọng MiniMax chỉ có một giọng tiếng Việt gốc (nữ). Mọi giọng nam đều là giọng đa ngôn ngữ đọc tiếng Việt, và connector **không có** công cụ nhân bản hay thiết kế giọng. Vì vậy phải chọn trong kho giọng có sẵn, bằng một buổi thử mới với tiêu chí:

| Tiêu chí | Đo bằng | Ngưỡng |
|---|---|---|
| Đúng chữ | CER (`listen_audio`) | < 2% |
| Ổn định danh tính | Phép thử 1.1 với bộ tham số dự định dùng | 1 người |
| Chất "podcast" | Mô hình chấm 1–10: ấm, gần, cuốn hút, hợp tài liệu tội phạm | ≥ 7 |
| Khác Điều tra viên và Chuyên gia | G9 | 8/8 |

Ứng viên đề xuất, vì đã có số liệu đọc tiếng Việt từ các vòng trước:
- `English_magnetic_voiced_man`: Host bản tiếng Anh, bạn từng chọn vì cuốn hút; đọc tiếng Việt CER 0–6,7%.
- `English_Trustworth_Man`: CER 0%.
- `English_expressive_narrator`: CER 0–6,9%.
- `English_Deep-VoicedGentleman`: CER 1,1–3,7%.
- `audiobook_male_1` (giữ làm đối chứng, chỉ neutral + cao độ 0).

### 3.3 Phân vai lại cho khác tông

Hướng đề xuất (phải xác nhận bằng buổi thử G9):

| Vai | Tông mong muốn | Hướng chọn |
|---|---|---|
| Host | Trầm ấm, gần, kiểu podcast đêm khuya, ~95–115 Hz | Ứng viên 3.2 |
| Điều tra viên | Khác hẳn Host: hoặc trẻ, sắc, nhanh (tenor ~140–160 Hz), hoặc già, khàn, chậm | Giữ `male-qn-qingse` nếu Host mới đủ trầm (đã chứng minh ổn định); nếu không, thử giọng khác |
| Chuyên gia | Nữ, điềm tĩnh, trí thức (~200–220 Hz) | Giữ `audiobook_female_1` |
| Người bình thường N1 · N2 | Nữ trẻ, khác Chuyên gia | Giữ, nhưng kiểm G9 với Chuyên gia |

### 3.4 Việc phải làm sau khi chốt

1. Thử giọng mới: khoảng 40 câu TTS + nghe mù, khoảng 20 phút.
2. Sửa `make_acting_tap02.py`: Host chỉ dùng bộ tham số an toàn. Các vai khác dùng bộ an toàn riêng của từng giọng.
3. Đọc lại toàn bộ 98 câu của Host, cộng các vai bị đổi giọng (nếu có), khoảng 10 phút.
4. Chạy G10, rồi `build_audio3` (khoảng 10 phút).
5. **Phải dựng lại cả hình**, không thể chỉ thay tiếng. Thời lượng câu mới khác cũ, mà mốc chữ, badge và sóng âm đều bám theo thời lượng câu. Chạy `parse_shots` + `build_video3` (khoảng 60 phút), rồi `package --mux`. Bảng shot và ảnh không phải sửa.
6. Cập nhật tiêu chuẩn A4.2 với G8–G10, và ghi bẫy #23 vào A11.

---

## 4. KẾT QUẢ THỬ CHỌN GIỌNG 3 VAI (23/10/2026)

Yêu cầu của người dùng: **Host trầm ấm · Điều tra viên lạnh lùng · Chuyên gia tâm lý nhấn mạnh**, ba giọng khác hẳn nhau. Script: `.work/voice_cast_test.py` (vòng 1) và `.work/voice_cast_round2.py` (vòng 2). File nghe ở `02_SAN_XUAT/Tap02/thu_giong_vai/`.

### Vòng 1 — 22 giọng × 2 câu (neutral, cao độ 0), chấm hợp vai, đúng chữ, cuốn hút

| Vai | Hạng 1 | Hạng 2 | Giọng hiện tại |
|---|---|---|---|
| Host | `English_CaptivatingStoryteller` 9 / 9 / 9 — "baritone ấm, hơi khàn, gần gũi kiểu podcast đêm" | `English_Deep-VoicedGentleman` 8,5 | `audiobook_male_1` 6,5 — "quá cao và sáng" |
| Điều tra viên | `English_ReservedYoungMan` 9 | `Korean_ColdYoungMan` 8,5 — "phẳng, chính xác, như báo cáo pháp y" | `male-qn-qingse` 6 — "quá thân thiện" |
| Chuyên gia | `English_MatureBoss` 8,5 | `English_AssertiveQueen` 7,5 — "chín chắn, phân tích" | `audiobook_female_1` 6,5 — "hơi máy, thiếu lực nhấn" |

Loại: `Chinese (Mandarin)_News_Anchor` (sai thanh điệu), `English_ConfidentWoman` và `English_Wiselady` (đổi sang người khác giữa 2 câu).

### Vòng 2a — ổn định danh tính (cùng câu × neutral · sad · fearful · surprised, cao độ 0)

| Giọng | Số "người" nghe ra | Kết luận |
|---|---:|---|
| `English_CaptivatingStoryteller` | **1** | Ổn định |
| `Korean_ColdYoungMan` | **1** | Ổn định |
| `English_AssertiveQueen` | **1** | Ổn định |
| `English_Deep-VoicedGentleman` | 4 | Loại |
| `English_ReservedYoungMan` | 3 | Loại |
| `English_MatureBoss` | 2 | Loại |
| `Korean_IntellectualMan` | 2 | Loại |

Các giọng điểm cao nhất vòng 1 ở vai Điều tra viên (`ReservedYoungMan`) và Chuyên gia (`MatureBoss`) **không qua được** vòng ổn định. Đây chính là lỗi đã gặp với Host ở Tập 02.

### Vòng 2b — bộ ba xen kẽ (6 câu), nghe mù

| Bộ | Host · Điều tra viên · Chuyên gia | Tách bạch | Hợp vai H / D / C | Ghi chú |
|---|---|---:|---|---|
| **A** | CaptivatingStoryteller · Korean_ColdYoungMan · AssertiveQueen | **9/10**, gán đúng 6/6 | 9 / 8,5 / 8,5 | **Cả 3 giọng ổn định** |
| B | Deep-VoicedGentleman · Korean_ColdYoungMan · MatureBoss | 9/10 | 9,5 / 8,5 / 8,5 | 2/3 giọng không ổn định |
| C | CaptivatingStoryteller · ReservedYoungMan · AssertiveQueen | 10/10 | 10 / 9 / 8,5 | Điều tra viên không ổn định |

Mô hình mô tả bộ A:
- **Host:** nam, trung niên, trầm, vang, uy tín.
- **Điều tra viên:** nam trẻ, cao độ vừa, tách rời, lạnh.
- **Chuyên gia:** nữ, cao độ vừa-cao, suy ngẫm, nhấn ý.

Cao độ: Host ~100 Hz · Điều tra viên ~142 Hz (cách Host **~6 nửa cung**) · Chuyên gia ~205 Hz.

### Đề xuất: BỘ A

| Vai | Giọng | Tốc độ gốc | Bộ tham số an toàn |
|---|---|---:|---|
| Host | `English_CaptivatingStoryteller` | 0,90 | neutral · sad · fearful · surprised; **cao độ 0** |
| Điều tra viên | `Korean_ColdYoungMan` | 0,95 | neutral · sad · fearful · surprised; **cao độ 0** |
| Chuyên gia | `English_AssertiveQueen` | 0,92 | neutral · sad · fearful · surprised; **cao độ 0** |
| N1 · N2 | Giữ `Vietnamese_kindhearted_girl` (284 Hz) · `English_captivating_female1` (250 Hz) | | Cách Chuyên gia ≥ 3 nửa cung |

- Tham số cao độ ≠ 0 **chưa** được thử ổn định với 3 giọng mới, nên không dùng.
- Các cảm xúc `happy`, `angry`, `disgusted` chưa thử, nên đổi sang `neutral`.

**Lưu ý:** `English_CaptivatingStoryteller` là giọng người dùng đã loại khỏi **bản tiếng Anh** ngày 22/10 vì "đều đều". Khi đọc tiếng Việt, mô hình chấm nó cuốn hút nhất (9/10), nhưng người dùng cần tự nghe `vong2/trio_A.mp3` và `vong2/stab_H_English_CaptivatingStoryteller.mp3` để xác nhận.

---

## 5. ĐÃ ÁP DỤNG (23/10/2026 15:07)

- Người dùng chốt **bộ A**. Bộ A là giọng mặc định của kênh trong `edition.py`; Tập 01 ghim bộ giọng cũ.
- `make_acting_tap02.py`: cao độ = 0, cảm xúc chỉ neutral · sad · fearful · surprised (neutral 160 · sad 28 · fearful 14 · surprised 13).
- Đọc lại 215/215 câu. Bộ giọng cũ lưu ở `.work/_cu/audio_s_t02_giong_cu/`.
- **G10** (`.work/voice_role_check.py`):
  - Host, Điều tra viên, Chuyên gia, N1, N2: mỗi vai nghe liền ra **1 người**.
  - Xen kẽ 3 vai: gán đúng 9/9, tách bạch **10/10** (`thu_giong_kiem_vai/`).
- Dựng lại: `Tap02_master.mp4` **26:44** · −15,9 LUFS · đỉnh −1,5 dBFS · 0 khoảng câm · hình = tiếng ±0,01 s · giải mã 0 lỗi.
- Tiêu chuẩn: A4.1 (bộ A), A4.2 (G3, G5 sửa; thêm G8–G10), A11 bẫy #23.

---

## 6. SỬA ĐỌC SỐ (23/10/2026)

**Người dùng phát hiện:** "1.400" bị đọc thành "một phẩy bốn trăm". Giọng đa ngôn ngữ hiểu dấu chấm theo kiểu tiếng Anh. Cùng nguy cơ đó có ở **23 câu** chứa số (năm, ngày, số vụ, số tuổi) và ở "Elizabeth II".

**Sửa tận gốc:** `tts_sentences.vi_numbers()` đổi mọi chữ số trong **lời đọc** sang chữ tiếng Việt; phụ đề và chữ trên hình giữ nguyên chữ số.

| Kịch bản | Giọng đọc |
|---|---|
| 1.400 | một nghìn bốn trăm |
| 2009 | hai nghìn không trăm lẻ chín |
| 21 | hai mươi mốt |
| 25 | hai mươi lăm |
| Elizabeth II | Elizabeth Đệ nhị |

- Chỉ đọc lại 23 câu; bản cũ lưu ở `.work/_cu/audio_s_t02_so_cu/`.
- Nhận dạng lại 3 câu khó nhất, đều đúng: "khoảng một nghìn bốn trăm món đồ", "Elizabeth Đệ Nhị", "tháng chín năm hai nghìn không trăm lẻ bảy".
- Đưa vào tiêu chuẩn: **G11** và bẫy **#24**. Khi viết kịch bản, các ký hiệu như %, km, $ nên viết bằng chữ.
