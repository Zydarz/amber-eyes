# BÁO CÁO — TẬP 02: GIỌNG ĐỌC & CÁC BIẾN ĐỔI TRONG CODE

**Ngày:** 27/10/2026 · **Phạm vi:** `AE_EP=02` (bản tiếng Việt) · 203 câu
**Bổ sung cho:** `BaoCao_NguonGiongDoc_20261027.md`, `BaoCao_GiongDaSoNhieu_20261027.md`

---

## 1. Trả lời câu hỏi: "MiniMax chỉ có 1 giọng nữ, và code .py đang biến đổi" — đúng hay sai?

| Mệnh đề | Kết luận | Bằng chứng |
|---|---|---|
| MiniMax **chỉ có 1 giọng nữ** | ✅ **ĐÚNG** (nếu giới hạn trong catalog 332 giọng: đúng **1** giọng mang nhãn tiếng Việt, và giọng đó là nữ) | `get_voice_list` → 332 giọng; tiền tố `Vietnamese` chỉ có **1**: `Vietnamese_kindhearted_girl` ("Kind-hearted girl"). Tập 02: giọng này đọc **4/203 câu (2,0%)**, chỉ cho vai N1 |
| MiniMax **chỉ có 1 giọng đọc được tiếng Việt** | ❌ **SAI** | Giọng hệ thống đa ngôn ngữ. G10 mù Tập 07 nghe Host (giọng `English_`) thành *"Deep mature **Southern Vietnamese** male"* và Điều tra viên (giọng `Korean_`) thành *"Clear **Northern Vietnamese** male narrator"* |
| **Code .py đang biến đổi giọng** | ❌ **SAI** — .py **chọn** giọng + biến đổi **TEXT**, không biến đổi giọng | `edition.py:1078` `CAST` hardcode → `tts_sentences.py:91` `voice, base = CAST[role]`. Phép "giọng nước ngoài → đọc tiếng Việt" nằm trong **engine MiniMax**, không nằm trong .py |
| **Code .py đang biến đổi văn bản lời đọc** | ✅ **ĐÚNG** | Mục 3 bên dưới — đo được từng bước |

**Câu trả lời thẳng:** kết luận của bạn **đúng một nửa**. "Chỉ 1 giọng nữ Việt" thì đúng. "Code .py biến đổi" thì đúng nếu là biến đổi **văn bản**, sai nếu là biến đổi **giọng**.

---

## 2. Tập 02 dùng giọng gì — đọc từ code, không đọc từ tài liệu

`edition.py:180` → `"cast": None` ⇒ Tập 02 dùng **bộ A mặc định** (không ghim riêng, khác Tập 01).

| Vai | `voice_id` | Ngôn ngữ gốc | Câu | Tỉ lệ | F0 (đo) | Giới |
|---|---|---|---:|---:|---:|---|
| Host (Cú) | `English_CaptivatingStoryteller` | English | 95 | 46,8% | **102,6 Hz** | NAM |
| Điều tra viên (Sói) | `Korean_ColdYoungMan` | Korean | 51 | 25,1% | **140,4 Hz** | NAM |
| Chuyên gia (Cáo) | `English_AssertiveQueen` | English | 49 | 24,1% | 207,8 Hz | NỮ |
| N1 (Cừu) | `Vietnamese_kindhearted_girl` | **Vietnamese** | 4 | 2,0% | 248,1 Hz | NỮ |
| N2 (Mèo) | `English_captivating_female1` | English | 4 | 2,0% | 230,3 Hz | NỮ |

⇒ **2 giọng nam + 3 giọng nữ.** Giọng Việt bản địa duy nhất chiếm **2,0%** số câu, thuộc vai phụ N1.

---

## 3. Code .py biến đổi gì trên bản VN Tập 02 (đo từng bước)

Thứ tự trong `tts_sentences.py:plan_items()`:

| # | Bước | Dòng | Tác động lên Tập 02 VN | Số đo |
|---|---|---|---|---|
| 1 | Bỏ dấu ngoặc kép thông minh `“ ” ‘ ’ "` | 93 | bỏ ngoặc kép khỏi lời đọc | toàn bộ câu có ngoặc kép |
| 2 | `TTS_FIX` (lời đọc riêng theo id) | 94 | **KHÔNG áp** — `edition.py:1105`: `TTS_FIX = (EP.get("tts_fix", {}) if EN else {})` ⇒ VN = `{}` | **0 mục** |
| 3 | `ACT[s["id"]]` → emotion + lệch tốc độ + cao độ + `alt` | 98–101 | Áp `acting_tap02.json` (203 mục) | **10 câu** có `alt` (lời đọc riêng) |
| 4 | `pause_tags()` | 103 | **KHÔNG áp** — chỉ chạy khi `ED.EN` | 0 |
| 5 | `vi_numbers()` — số → chữ | 105 | Đổi "46" → "bốn mươi sáu", "2009" → "hai nghìn không trăm lẻ chín", "Elizabeth II" → "Elizabeth Đệ nhị" | **22 câu** |

**Kết quả G6 (lời đọc ≠ câu gốc): 23/203 câu** — 22 do đổi số→chữ (được G11 cho phép), 1 do `ACT['alt']` bỏ chú thích `(Signature)` ở câu `2.07#3`.

**Còn sót trong lời đọc sau khi .py xử lý: 9 câu còn chữ số** — nhưng **không phải lỗi**: chúng nằm trong thẻ ngắt `<#0.35#>` (ví dụ `4.08#6` → `"...bức ảnh dấu giày tuyết... và nói: <#0.35#> Chúng giống hệt nhau."` — số "35" là tham số thẻ, không phải số cần đọc).

**Kiểm tra G4 (tốc độ lệch gốc trong −0,06 … +0,02) — đạt toàn bộ:**

| Vai | Tốc độ gốc | Thực tế | Lệch |
|---|---:|---|---|
| Host | 0,90 | 0,84–0,88 | −0,06 … −0,02 ✓ |
| Điều tra viên | 0,95 | 0,89–0,92 | −0,06 … −0,03 ✓ |
| Chuyên gia | 0,92 | 0,86–0,90 | −0,06 … −0,02 ✓ |
| N1 | 0,95 | 0,90–0,92 | −0,05 … −0,03 ✓ |
| N2 | 0,95 | 0,89–0,93 | −0,06 … −0,02 ✓ |

**Kiểm tra G5 (cao độ = 0) — đạt 100%:** `pitch` = 0 ở cả 203/203 câu.

---

## 4. Hai lỗi thật trong Tập 02 (đã có file mp3 xuất)

### 4.1 G1 — 3 câu còn dấu `...` trong lời đọc
| id | Vai | Lời đọc |
|---|---|---|
| `1.07#3` | N1 | *"Nhưng sau khi mọi chuyện vỡ lở... mỗi lần nhớ lại ánh mắt bình thản…"* |
| `1.08#1` | Host | *"Thế nhưng... có ai ngờ rằng người đàn ông khoác trên mình bộ quân phục…"* |
| `4.06#3` | N2 | *"Cho đến khi sự thật được công bố... cảm giác đó kinh hoàng hơn bất cứ cơn ác mộng nào."* |

Luật G1: *"**CẤM** `...` và thẻ ngắt `<#s#>` giữa câu."* Cả 3 nằm ở **đầu mệnh đề** (chấp phổi tự nhiên của văn xuôi) nên thiệt hại ít hơn hậu quả G1 cảnh báo — nhưng vẫn vi phạm chữ nghĩa, và **đã được đọc vào file mp3**.

### 4.2 G7 — 2 câu còn chú thích tiếng Anh trong ngoặc
| id | Vai | Lời đọc |
|---|---|---|
| `2.08#2` | Điều tra viên | *"…nhu cầu giữ lại Chiến lợi phẩm **(Trophies)** là một phần chữ ký tâm lý…"* |
| `3.11#1` | Chuyên gia | *"Đó là Ái kỷ ác tính **(Malignant Narcissism)** kết hợp Phức cảm Chúa trời **(God Complex)**…"* |

Luật G7: *"Không để giọng Việt đọc tiếng Anh dài; **bỏ chú thích tiếng Anh trong ngoặc khỏi lời đọc**."* Câu `3.11#1` đọc **3 cụm tiếng Anh** bằng giọng nữ tiếng Việt.

**Bằng chứng cơ chế đã hoạt động 1 lần:** câu `2.07#3` có `ACT['alt']` bỏ `(Signature)` → đúng chuẩn G7. Tức là dự án **biết cách sửa**, chỉ là sót 2 câu.

**Cả 5 câu đều đã có file mp3 trong `audio_s_t02/`** ⇒ lỗi đã vào thành phẩm `Tap02_master.mp4`.

### 4.3 Không phải lỗi riêng của Tập 02 — mang tính hệ thống
| Tập | Câu | G1 (`...`) | G7 (ngoặc tiếng Anh) |
|---|---:|---:|---:|
| Tập 01 | 128 | 4 | 8 |
| **Tập 02** | **203** | **3** | **2** |
| Tập 03 | 220 | 4 | **25** |
| Tập 04 | 161 | 0 | 4 |
| Tập 05 | 164 | 4 | 7 |
| Tập 06 | 165 | 0 | 0 |
| Tập 07 | 164 | 0 | 0 |
| **Tổng** | | **15** | **46** |

Tập 06–07 sạch (mới nhất) ⇒ luật được áp dụng từ đó; Tập 01–05 **chưa được sửa lại**. Tập 03 nặng nhất (25 câu).

---

## 5. Rủi ro còn mở của Tập 02: chưa có CER tiếng Việt cho 3 giọng bộ A

| Vai | `voice_id` | CER tiếng Việt đã đo | Ngưỡng dự án |
|---|---|---:|---|
| Host | `English_CaptivatingStoryteller` | **chưa có số thô** | < 2% |
| Điều tra viên | `Korean_ColdYoungMan` | **chưa có số thô** | < 2% |
| Chuyên gia | `English_AssertiveQueen` | **chưa có số thô** | < 2% |
| N1 | `Vietnamese_kindhearted_girl` | 0,0% | ✓ |
| N2 | `English_captivating_female1` | 0,0% | ✓ |

Bằng chứng giọng ngoại ngữ đọc tiếng Việt **có thể vượt ngưỡng**: `English_CalmWoman` **9,3%**, `English_expressive_narrator` **6,9%**, `English_Deep-VoicedGentleman` **3,7%** (`.work/voice_test5/report.md`).

Vòng 1 của `BaoCao_GiongDoc_Tap02.md` chỉ chấm điểm 1–10 ("đúng chữ" 9 / 8,5 / 7,5) — chấm bằng mô hình, không phải `listen_audio` như tiêu chuẩn quy định.

---

## 5.5. Cơ chế chính xác: không có bước "chuyển qua tiếng Việt" (đối chiếu tài liệu MiniMax)

**Công thức:** *ngôn ngữ đến từ **TEXT**, chất giọng (timbre) đến từ **`voice_id`**.*

| Tầng | Quyết định bởi | Ví dụ ở Tập 02 |
|---|---|---|
| Ngôn ngữ + ngữ âm (thanh điệu, nguyên âm) | **văn bản đầu vào** — engine tự nhận diện | "Người đàn ông 46 tuổi…" → tiếng Việt |
| Chất giọng / danh tính người nói | **`voice_id`** trong kho | `English_CaptivatingStoryteller` |

**Bằng chứng từ tài liệu MiniMax:**
- Tham số `language_boost` (mặc định `null`): *"If the language type is unknown, set to `"auto"` and the model will automatically detect it."* → có cơ chế **tự nhận diện ngôn ngữ**.
- Connector `batch_text_to_audio` và `synthesize_speech` **không expose** `language_boost` ⇒ chạy ở chế độ auto-detect.
- MiniMax mô tả: *"speech models … supporting 40 languages and 300+ system voices"*, *"具备卓越的跨语言能力"* (năng lực xuyên ngôn ngữ).
- Ví dụ chính thức của MiniMax: `voice_id: "English_expressive_narrator"` + `language_boost: "auto"` + text tiếng Trung.

⇒ **Không có bước "chuyển".** Engine *tổng hợp* (synthesis) timbre nước ngoài bằng ngữ âm tiếng Việt, phát âm lại từ đầu. Không phải dịch, không phải đổi giọng một bản thu sẵn, không phải voice clone (tiêu chuẩn A4.1 xác nhận connector **không có** công cụ nhân bản hay thiết kế giọng).

**Hệ quả thực tế (vì sao phải đo CER):** chất lượng phát âm tiếng Việt là **kết quả render ngữ âm Việt bằng timbre nước ngoài** — nhãn `English_`/`Korean_` **không bảo đảm** gì về độ đúng. Bằng chứng: `English_CalmWoman` 9,3% · `English_expressive_narrator` 6,9% · `English_Deep-VoicedGentleman` 3,7%.

**Với 2 vai nam, không có lựa chọn thay thế:** kho chỉ có 1 giọng Việt (`Vietnamese_kindhearted_girl`) và đó là giọng **nữ**. Không thể làm Host/Điều tra viên bằng giọng Việt bản địa.

### 5.6. Phát hiện thêm: tham số `pitch` của connector là **đổi âm sắc**, không phải chỉnh F0

Connector `pitch` ∈ [−12, 12] map sang `voice_setting.pitch` của MiniMax — mô tả: *"合成音频的语调，取值越大，语速越快"* (dịch chuyển âm sắc, **0 = giữ nguyên âm sắc gốc**).

⇒ Đây chính là lý do luật G5 bắt **"cao độ = 0"**: `pitch ≠ 0` là **đổi người** (đổi timbre), không phải chỉnh cao độ tự nhiên. Bằng chứng trong tiêu chuẩn A4.2 G5 khớp 100%: `audiobook_male_1` pitch +1 → F0 +4,5 nửa cung **và đổi người**; −1/−2 → đổi sang giọng miền Bắc khàn.

**Tập 02 đang đạt**: `pitch` = 0 ở **203/203 câu**.

*(Ghi chú: MiniMax API gốc còn có `pronunciation_dict` để ghim cách đọc/nghĩa thanh, và `emotion` có thêm `calm`/`fluent`/`whisper` — connector không expose. Dự án chỉ dùng 4 cảm xúc an toàn của G3, phù hợp.)*

---

## 1.5. Giải thích đơn giản: vấn đề khi dùng giọng nước ngoài để đọc tiếng Việt

### Hình dung
Tưởng tượng một **diễn viên Mỹ rất giỏi đọc tiếng Việt** được thu âm cho lời thoại tiếng Việt. Câu chữ anh ta đọc **đúng từng chữ**, không sai chữ nào. Nhưng người ta vẫn nghe ra: **thanh điệu anh ta đặt không chuẩn, cách anh ta nuốt chữ hơi lạ, ngữ điệu không có nhịp của người bản xứ.** Đó chính xác là tình huống của dự án này.

- **Host** = diễn viên Mỹ đọc tiếng Việt (`English_CaptivatingStoryteller`)
- **Điều tra viên** = diễn viên Hàn Quốc đọc tiếng Việt (`Korean_ColdYoungMan`)
- **Chuyên gia / N1 / N2** = giọng nữ, 2 trong 3 giọng cũng là "diễn viên nước ngoài"

### Cơ chế thật (1 dòng)
> **Ngôn ngữ do CHỮ quyết định. Chất giọng do `voice_id` quyết định.** Không có bước "chuyển" nào cả — engine nhận chữ tiếng Việt và *sinh ra* tiếng Việt bằng cái giọng đã chọn.

### Vì sao vẫn là vấn đề — 4 điểm cụ thể

| # | Vấn đề | Biểu hiện với khán giả Việt | Bằng chứng |
|---|---|---|---|
| 1 | **Thanh điệu tiếng Việt** (ngôn ngữ có 6 thanh, thanh mang nghĩa) | Nghe "sai sắc", phải dựng lại từ ngữ cảnh | Bằng chứng mạnh nhất là CER: `English_CalmWoman` **9,3%**, `English_expressive_narrator` **6,9%**, `English_Deep-VoicedGentleman` **3,7%** — vẫn là tiếng Việt *đúng chữ*, nhưng đúng chữ ≠ phát âm chuẩn |
| 2 | **Accent vùng không kiểm soát được** | Lúc nghe ra giọng Nam, lúc giọng Bắc, không nhất quán giữa các tập | G10 mù Tập 07: Host (giọng English) → *"Deep mature **Southern Vietnamese** male"*; Điều tra viên (giọng Korean) → *"Clear **Northern Vietnamese** male narrator"*. Connector **không expose** `language_boost` ⇒ không có đường chỉnh |
| 3 | **Từ vựng chuyên ngành / tiếng Anh xen kẽ** | Đọc "Trophies", "Malignant Narcissism" bằng giọng nước ngoài → lộ rõ, và có thể đọc sai | Luật G7 đã cấm nhưng còn sót 2 câu ở Tập 02 (`2.08#2`, `3.11#1`) |
| 4 | **Ngữ điệu, nhịp câu** | Đều đều, thiếu nhấn nhá, thiếu "nhịp Việt" | G10 chỉ đánh giá *phân biệt được giọng* (10/10), không đánh giá *tự nhiên* |

### Điều quan trọng: đây là **rủi ro**, không phải lỗi đã biết
MiniMax làm tốt — nhiều giọng đọc tiếng Việt **đúng 100% chữ** (`audiobook_male_1`, `male-qn-qingse`, `audiobook_female_1` đều CER **0,0%**; `Vietnamese_kindhearted_girl` 0,0%). Nhưng **3 giọng bộ A đang dùng hằng ngày chưa từng được đo CER** ⇒ chưa biết chất lượng phát âm thực tế.

### Vì sao vẫn chọn bộ A — đánh đổi đã đo được

| Tiêu chí | Bộ cũ (`audiobook_male_1` + `male-qn-qingse`) | Bộ A (`English_CaptivatingStoryteller` + `Korean_ColdYoungMan`) |
|---|---|---|
| **Độ đúng chữ tiếng Việt (CER)** | **0,0%** ✓ | **chưa đo** ✗ |
| **Ổn định danh tính (G8)** | ✗ 7 thiết lập → 6 "người" (đổi người khi đổi cảm xúc) | ✓ ổn định |
| **Tách bạch Host ↔ Điều tra viên (G9)** | ✗ chỉ **3,1 nửa cung** (đo được) | ✓ **5,4 nửa cung** |
| **Còn trong catalog live 332 giọng?** | ✗ vắng mặt (rủi ro chết) | ✓ có |

⇒ Bộ A thắng 2/3 tiêu chí nhưng **đánh đổi bằng tiêu chí chưa kiểm chứng**. Đây chính là lỗ hổng cần đóng.

### Điều không đổi được
Kho chỉ có **1 giọng Việt** và đó là giọng **nữ** ⇒ **2 vai nam buộc phải dùng giọng nước ngoài.** Không phải lựa chọn thẩm mỹ, mà là ràng buộc của kho. (Lựa chọn thay thế duy nhất cho vai nam: `male-qn-qingse` — CER 0%, đã chứng minh ổn định — nhưng **không có trong catalog live**, rủi ro chết.)

### Việc làm được (rẻ → đắt)
1. **Đo CER cho 3 giọng bộ A** (~30 câu mẫu/vài, dùng `cer()` + `listen_audio` sẵn có) — đóng lỗ hổng, biết ngay có cần đổi hay không.
2. **Sửa 2 câu G7 của Tập 02** (bỏ chú thích tiếng Anh trong ngoặc) — rẻ, giảm rõ vấn đề #3.
3. **Nếu `Korean_ColdYoungMan` đọc sai** → cân nhắc đưa vai Điều tra viên về `male-qn-qingse` (CER 0%, ổn định), chấp nhận rủi ro "không có trong catalog". Cần kiểm tra sống của nó bằng 1 call TTS thật.
4. **Không sửa được**: 2 vai nam sẽ luôn là giọng nước ngoài cho tới khi MiniMax có thêm giọng Việt nam.

---

## 6. Việc cần làm với Tập 02

| # | Việc | Mức độ | Ghi chú |
|---|---|---|---|
| 1 | Sửa **3 câu G1** + **2 câu G7** của Tập 02 (thêm `alt` vào `acting_tap02.json` cho 5 câu này) | Nên làm | Sửa xong **phải đọc lại 5 câu** + **dựng lại video** (độ dài câu đổi → mốc chữ/sóng âm lệch) |
| 2 | Đo CER tiếng Việt cho 3 giọng bộ A | Cần duyệt credit | ~30 câu mẫu/vai, dùng `listen_audio` + `cer()` sẵn có trong `voice_audition.py` |
| 3 | Quét lại 5 tập cũ (Tập 01–05) — 15 câu G1 + 46 câu G7 | Nên làm | Tập 03 nặng nhất |
| 4 | Thêm luật **G13**: giọng ngoại ngữ đọc tiếng Việt phải đo CER bằng `listen_audio` (ngưỡng < 2%); không suy giới tính/độ đúng từ tên giọng | Nên làm | AGENTS.md §4 + A11 tiêu chuẩn |

**Cảnh báo về việc sửa lời đọc:** `BaoCao_GiongDoc_Tap02.md` §3.4 bước 5 ghi rõ — *"**Phải dựng lại cả hình**, không thể chỉ thay tiếng. Thời lượng câu mới khác cũ, mà mốc chữ, badge và sóng âm đều bám theo thời lượng câu."* ⇒ sửa 5 câu này tốn ~60 phút dựng lại Tập 02.

---

## 7. Lệnh tái lập

```powershell
$env:AE_EP="02"; $env:PYTHONIOENCODING="utf-8"
py -3 .work/_phan_tich_tap02.py      # phân bố vai/giọng/cảm xúc/nhịp, kiểm G6/G1/G7
py -3 .work/_bien_doi_tap02.py        # truy vết từng bước biến đổi của .py
py -3 .work\_quet_loi_g1_g7_tat_ca_tap.py   # quét lỗi G1/G7 mọi tập VN
py -3 .work/_do_f0_theo_vai_tap01_tap02.py   # đo F0 theo vai
```

*Báo cáo này chỉ đọc dữ liệu có sẵn + đo F0 cục bộ. Không tạo audio, không tốn credit, không sửa file nào trong dự án.*
