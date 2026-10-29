# BÁO CÁO — VÌ SAO AUDIO TIẾNG VIỆT CÓ GIỌNG NAM KHI KHO CHỈ CÓ 1 GIỌNG VIỆT

**Ngày:** 27/10/2026 · **Bổ sung cho:** `BaoCao_NguonGiongDoc_20261027.md`

---

## 1. Kết luận

**Không phải 3 giọng nam. Bản tiếng Việt có 2 giọng NAM + 3 giọng NỮ.** Đo F0 trên file TTS rời và đọc báo cáo G10 mù của chính dự án đều cho cùng kết quả.

Và câu trả lời cho "vì sao" thì **dự án đã tự ghi sẵn** trong `02_SAN_XUAT/Tap02/BaoCao_GiongDoc_Tap02.md` §3.2 (dòng 105):

> *"Kho giọng MiniMax chỉ có một giọng tiếng Việt gốc (nữ). **Mọi giọng nam đều là giọng đa ngôn ngữ đọc tiếng Việt**, và connector **không có** công cụ nhân bản hay thiết kế giọng."*

Tức là: tiền tố `English_` / `Korean_` trong `voice_id` là **ngôn ngữ gốc của giọng**, KHÔNG phải ràng buộc ngôn ngữ đầu vào. Cùng cơ chế đó được dự án tự dùng để loại `Chinese (Mandarin)_News_Anchor` với lý do *"sai thanh điệu"* (tiêu chuẩn A4.1) — một giọng Trung Quốc đọc tiếng Việt, chỉ là vang không chuẩn.

---

## 2. Đo thật — F0 trên file TTS rời (không nhạc, không SFX)

Tự tương quan, khung 40 ms, lọc 60–400 Hz, trung vị mỗi câu → trung vị theo vai.

### Tập 01 (bộ giọng cũ, ghim riêng) — 128/128 file
| Vai | `voice_id` | Ngôn ngữ gốc | F0 trung vị | Giới |
|---|---|---|---:|---|
| Host | `audiobook_male_1` | (legacy) | **114,3 Hz** | NAM |
| Điều tra viên | `male-qn-qingse` | (legacy) | **136,8 Hz** | NAM |
| Chuyên gia | `audiobook_female_1` | (legacy) | 230,2 Hz | NỮ |
| N1 | `Vietnamese_kindhearted_girl` | Vietnamese | 250,0 Hz | NỮ |
| N2 | `English_captivating_female1` | English | 231,9 Hz | NỮ |

### Tập 02–07 (bộ A) — 203/203 câu của Tập 02
| Vai | `voice_id` | Ngôn ngữ gốc | F0 trung vị | Giới |
|---|---|---|---:|---|
| Host | `English_CaptivatingStoryteller` | English | **102,6 Hz** | NAM |
| Điều tra viên | `Korean_ColdYoungMan` | Korean | **140,4 Hz** | NAM |
| Chuyên gia | `English_AssertiveQueen` | English | 207,8 Hz | NỮ |
| N1 | `Vietnamese_kindhearted_girl` | Vietnamese | 248,1 Hz | NỮ |
| N2 | `English_captivating_female1` | English | 230,3 Hz | NỮ |

Khoảng cách F0 bộ A: Host → D = **+5,4 nửa cung**, D → C = **+6,8 nửa cung** (đạt G9: ≥ 4 nửa cung).

---

## 3. Bằng chứng thứ 2 — G10 nghe mù của chính dự án

`02_SAN_XUAT/Tap0X/thu_giong_kiem_vai/report.md` — mô hình nghe **không biết** S1/S2/S3 là ai:

| Tập | S1 (Host) | S2 (Điều tra viên) | S3 (Chuyên gia) | SPEAKERS | Tách bạch |
|---|---|---|---|---:|---:|
| Tập 04 | deep mature resonant **male** | clear steady youthful **male** | clear professional expressive **female** | 3 | 10/10 |
| Tập 05 | deep mature dramatic **male** | clear youthful steady **male** | smooth articulate professional **female** | 3 | 10/10 |
| Tập 06 | deep mature dramatic **male** | clear balanced journalistic **male** | soft clear expressive **female** | 3 | 10/10 |
| **Tập 07** | **Deep mature Southern Vietnamese male** | **Clear Northern Vietnamese male narrator** | **Gentle Southern Vietnamese female voice** | 3 | 10/10 |

⇒ **2 nam + 1 nữ** trong 3 vai chính, ở cả 4 tập có báo cáo. Giọng English (Host) đọc ra giọng **Nam Việt**, giọng Korean (Điều tra viên) đọc ra giọng **Bắc Việt** — tức giọng đa ngôn ngữ **tự nhận giọng vùng tiếng Việt** khi đọc tiếng Việt. Đây là lý do người nghe thấy giọng bản ngữ chứ không thấy "giọng nước ngoài đọc tiếng Việt".

Bản EN cho kết quả tương ứng: S1 *"Resonant American male broadcaster"* · S2 *"Smooth conversational American male"* · S3 *"Formal British female audiobook narrator"*.

---

## 4. Nếu bạn nghe "3 giọng nam" — 2 giải thích có số đo

### 4.1 Bạn đang nghe **file thử giọng**, không phải tập đã dựng
`90_LUU_TRU/thu_giong/so_sanh_5_giong.mp3` (60,5 s) gộp **10 bản đọc** (2 ứng viên × 5 vai) theo `voice_audition.py:26`:
- **4 giọng nam**: `audiobook_male_1`, `English_expressive_narrator`, `male-qn-qingse`, `English_Deep-VoicedGentleman`
- 6 giọng nữ: `audiobook_female_1`, `English_CalmWoman`, `Vietnamese_kindhearted_girl`, `English_Kind-heartedGirl`, `English_captivating_female1`, `English_SereneWoman`

Đo file này → **3 nhóm F0**: 122,3 Hz (nam, 16,6 s) · 197,5 Hz (nữ ấm, 10,0 s) · 250,0 Hz (nữ, 16,5 s). Có 3 nhóm, trong đó 1 nhóm nam.

### 4.2 Giọng Chuyên gia `English_AssertiveQueen` rơi vào vùng dễ nghe nhầm là nam
207,8 Hz trung vị (p5 = 188,2 Hz) — nữ thấp nhất trong bộ, thấp hơn N2 (230 Hz) và N1 (248 Hz). Tập 01 dùng `audiobook_female_1` ở 230,2 Hz — rõ nữ hơn hẳn.

---

## 5. Rủi ro thật: độ đúng phát âm tiếng Việt của giọng ngoại ngữ

Đây mới là điểm cần canh, và nó **chưa được đo cho đủ 3 giọng bộ A**.

**Ngưỡng dự án tự đặt** (`BaoCao_GiongDoc_Tap02.md` §3.2, dòng 110): *"Đúng chữ | CER (`listen_audio`) | **< 2%**"*.

**CER đã đo** — `.work/voice_test5/report.md` (mỗi giọng 1 câu tiếng Việt):

| Vai | `voice_id` | Ngôn ngữ gốc | CER đọc tiếng Việt | Ngưỡng < 2% |
|---|---|---|---:|---|
| H | `audiobook_male_1` | (legacy) | 0,0% | đạt |
| H | `English_expressive_narrator` | English | **6,9%** | ✗ vượt 3,4× |
| D | `male-qn-qingse` | (legacy) | 0,0% | đạt |
| D | `English_Deep-VoicedGentleman` | English | **3,7%** | ✗ vượt 1,8× |
| C | `audiobook_female_1` | (legacy) | 0,0% | đạt |
| C | `English_CalmWoman` | English | **9,3%** | ✗ vượt 4,6× |
| N1 | `Vietnamese_kindhearted_girl` | Vietnamese | 0,0% | đạt |
| N1 | `English_Kind-heartedGirl` | English | 0,0% | đạt |
| N2 | `English_captivating_female1` | English | 0,0% | đạt |
| N2 | `English_SereneWoman` | English | 0,0% | đạt |

Bản chép ASR cho thấy lỗi nghe ra được: `English_CalmWoman` đọc *"Khi sinh ra Gypsy…"* thành *"**Hy sinh cho** Gypsy…"*.

**Điểm trống:** 3 giọng đang dùng hằng ngày (`English_CaptivatingStoryteller`, `Korean_ColdYoungMan`, `English_AssertiveQueen`) **không có số CER thô** trong tài liệu — vòng 1 của `BaoCao_GiongDoc_Tap02.md` chỉ chấm điểm 1–10 ("đúng chữ" 9 / 8,5 / 7,5) chứ không ghi CER. Số điểm đó có thể do mô hình chấm, không phải CER đo bằng `listen_audio` như tiêu chuẩn quy định.

**⇒ Đề xuất luật mới (G13):** *"Giọng có ngôn ngữ gốc khác vẫn phải đo CER tiếng Việt bằng `listen_audio` (ngưỡng < 2%) cho từng vai dùng nó. Không suy giới tính hay độ đúng từ tên giọng."*

---

## 6. Sai lệch của chính AI trong lượt này (AGENTS.md §10)

Lần đầu mình suy giới tính từ **tên giọng** trong catalog và **sai**: `audiobook_female_1` ra "NAM" vì chuỗi `"female"` chứa chuỗi `"male"`; `English_captivating_female1` và `Japanese_DependableWoman` cũng bị gán sai theo cùng lỗi (`"woman"` chứa `"man"`).
- **Nguyên nhân gốc:** so khớp chuỗi không phân biệt bao hàm.
- **Cách sửa:** bỏ suy đoán theo tên → **đo F0 trên file TTS rời** (mục 2) và **đọc lại báo cáo G10 mù** (mục 3). Số đo đo được là nguồn, tên giọng chỉ là nhãn.
- **Còn lại:** đo trên file master có nhạc/SFX cho 164 nhóm rác (347 Hz, 363 Hz là nhiễu SFX/harmonic) → **không dùng master để kết luận giọng**, chỉ dùng file TTS rời.

---

## 7. Việc cần bạn xác nhận

1. **Bạn nghe "3 giọng nam" ở đâu?** Tập nào, file nào (video đã đăng / `02_SAN_XUAT/TapXX/xuat_ban/` / file thử giọng trong `90_LUU_TRU/thu_giong/`)? Cho mình tập + mốc thời gian, mình khoanh vùng đúng câu đó và đo lại.
2. **Duyệt đo CER tiếng Việt cho 3 giọng bộ A** (`English_CaptivatingStoryteller`, `Korean_ColdYoungMan`, `English_AssertiveQueen`)? Cần ~30 câu mẫu × 3 vai = 30 lượt gọi `listen_audio` (có tốn credit → cần bạn duyệt trước).
3. **Có thêm luật G13** vào `AGENTS.md` + A11 tiêu chuẩn không?

---

## 8. Lệnh tái lập

```powershell
# Vai -> voice_id thật, theo từng tập
py -3 .work/_audit_voice_theo_vai.py

# F0 theo vai trên file TTS rời (Tập 01 + Tập 02)
py -3 .work/_do_f0_theo_vai_tap01_tap02.py

# Nhóm giọng trong file thử giọng
py -3 .work/_dem_nguoi_trong_file_giong.py

# Quét toàn bộ manifest VN/EN/JA/KO
py -3 .work/_quet_manifest_giong.py

# CER có sẵn của dự án
Get-Content .work\voice_test5\report.md -Encoding UTF8
```

*Báo cáo này chỉ đọc dữ liệu có sẵn + đo F0 cục bộ. Không tạo audio, không tốn credit, không sửa file nào trong dự án.*
