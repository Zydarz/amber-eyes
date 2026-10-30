# Báo cáo H2 — Higgs Audio v3 · Tập 02 (viết lại dễ hiểu)

**Ngày:** 30/10/2026 · **Cổng:** H2 (đo chất lượng giọng so với MiniMax)
**Báo cáo cũ:** `BaoCao_H2_Higgs_Pilot_Tap02_20261030.md` (bản này viết lại theo dạng *lỗi → nguyên nhân → sửa ở đâu*)

---

## 0. Đọc nhanh — 6 lỗi, tình trạng hiện tại

| # | Lỗi | Bạn thấy gì | Nguyên nhân gốc | Sửa ở đâu | Trạng thái |
|---|---|---|---|---|---|
| 1 | **Đường dẫn cứng** | Chạy pipeline Tập 02 → crash ngay dòng đầu | 273 file trỏ tới thư mục cũ `D:\TEST\Gax\Audi` (không còn tồn tại) | Trong chính 273 file đó | ✅ **Đã sửa + commit** |
| 2 | **Đo CER sai** | Nghĩ Higgs đọc sai 12% câu, có câu 73,8% | 4 mắt xích: pipeline đổi số→chữ, ASR trả chữ số, script chuẩn hóa 1 vế, hàm `vi_numbers` sai | Script đo CER (KHÔNG phải code sản xuất) | ✅ **Đã sửa** (cả số đo MiniMax phải tính lại) |
| 3 | **Sai nhiệt độ vai D** | Vai D đọc kém hơn MiniMax | `temperature 0,7` làm model "đọc" quá dài, lỗi 47,56 s | Chọn `temperature 0,8` + sinh 3 bản/câu | ✅ **Đã chốt** |
| 4 | **File quá dài 47 s** | 2 file dài 47,56 s | Model lặp lại thay vì dừng | Sinh 3 bản/câu, loại bản vượt 47 s | ✅ **Đã chốt** |
| 5 | **G9 H↔D** | 2 vai nam gần như **cùng cao độ** (chỉ cách 0,23 nửa cung, cần ≥ 4) | **Higgs không giữ cao độ của clip tham chiếu** — 2 vai trôi ngược chiều về cùng một vùng | Cần clip tham chiếu **mới** | ❌ **CHỜ BẠN QUYẾT** |
| 6 | **G9 vai N1** | Không tìm được clip nữ vừa đọc đúng vừa tách xa C | Chưa có clip nữ nào đủ cao | Cần clip VoxCPM2 mới hoặc chấp nhận lệch | ❌ **CHỜ BẠN QUYẾT** |

> **Điểm mấu chốt:** lỗi #1, #2, #3, #4 **không nằm trong code sản xuất** — chúng là lỗi của **chính công cụ đo**.
> Lỗi #2 khiến suốt một buổi tưởng Higgs kém; thực ra sau khi đo lại đúng thì **Higgs tốt hơn MiniMax ở vai H**.
> Lỗi #5, #6 là lỗi **thật của giọng**, không sửa được bằng code — cần quyết định của bạn.

---

## 1. Bối cảnh tối thiểu để hiểu

### 1.1 Tại sao làm lại Tập 02 bằng Higgs

Tập 02 hiện đang đọc bằng giọng **MiniMax** (dịch vụ TTS trả phí). Bạn muốn đổi sang **Higgs Audio v3** —
model mã nguồn mở của Boson, chạy trên máy mình, và nó **clone giọng từ clip tham chiếu** thay vì bị ràng buộc
vào một thư viện giọng có sẵn. Đổi được giọng thì tự quyết được "vai này nghe thế nào".

Higgs v3 cần GPU. Máy bạn không có GPU, và bản MLX-Audio chỉ chạy được trên Mac Apple Silicon.
⇒ Chạy trên **Kaggle GPU** (còn ~29,5 h/tuần, Tesla T4 16 GB).

### 1.2 "Pilot" là gì

Trước khi sinh cả 203 câu (mất ~1,5 h GPU), ta làm một **pilot 96 bản**: 5 vai × vài câu × vài nhiệt độ,
để xem trước giọng có đọc đúng không, đọc bao lâu, và hai vai có phân biệt được không.

### 1.3 Ba con số hay gặp — nghĩa là gì

| Viết tắt | Nghĩa | Ngưỡng chuẩn | Cách đo |
|---|---|---|---|
| **CER** | Tỉ lệ ký tự sai khi máy nghe lại (ASR) chép lại câu TTS đã đọc | **< 2%** mỗi vai | `listen_audio` (mô hình nghe) chép lại, so ký tự với lời gốc |
| **F0** | Cao độ giọng (Hz) — số Hz càng cao giọng càng trầm, ngược lại càng cao | — | Tự động cương tự, lấy trung vị |
| **nửa cung** | Khoảng cách giữa 2 giọng tính theo bậc nhạc. 12 nửa cung = gấp đôi tần số | **≥ 4** giữa 2 giọng cùng giới (luật G9) | `12 × log2(F0₁ / F0₂)` |

Hai người có cao độ cách nhau **4 nửa cung trở lên** thì người nghe phân biệt được ai là ai.
Dưới 4 nửa cung thì dễ lẫn — đó là lý do luật G9 tồn tại.

### 1.4 Các con số chuẩn dùng để kết luận

| Nguồn | Nội dung |
|---|---|
| `AGENTS.md` L3 | Không được viết "xong" mà không kèm số đo thật |
| `AGENTS.md` L4 | Không đổi giọng nhân vật khi chưa qua G8–G10 + G12 **và** chưa có bạn đồng ý |
| `AGENTS.md` Q3(a) | Khi đo CER, phải chuẩn hóa số cho **CẢ HAI VẾ** (lời gốc **và** bản chép) |
| `AGENTS.md` G9 | Hai giọng cùng giới phải cách nhau **≥ 4 nửa cung** |
| `QUY_TAC_AUDIO_HIGGS.md` §6 | `temperature` 0,7 (dò 0,6/0,7/0,8), `top_p` 0,95, `top_k` 50, WAV 24 kHz mono |
| `QUY_TAC_AUDIO_HIGGS.md` §7 | Mỗi câu nên sinh 2 bản (seed khác); câu hỏng thì sinh thêm tối đa 2 bản |
| `QUY_TAC_AUDIO_HIGGS.md` §8 | File phải 24 kHz, dài 0,5–47 s, không lặng > 0,3 s, không đuôi tạp âm |

---

## 2. Lỗi 1 — Pipeline Tập 02 crash vì đường dẫn cứng

**Triệu chứng.** Chạy bất kỳ bước nào của pipeline Tập 02 (`build_audio3.py`, `build_video3.py`,
`tts_sentences.py`, `subtitles.py`, `package.py`…) đều **dừng ngay dòng đầu tiên**, báo lỗi kiểu
`FileNotFoundError` trỏ tới `D:\TEST\Gax\Audi\...`.

**Nguyên nhân.** Kho code của bạn được **copy từ máy cũ** (thư mục `D:\TEST\Gax\Audi`) sang máy hiện tại
(`D:\TEST\Gax\amber-eyes`). Trong **273 file Python**, đường dẫn gốc repo được **viết cứng** dạng
`Path(r"D:\TEST\Gax\Audi\X")`. Ở máy mới, `D:\TEST\Gax\Audi` **không tồn tại** ⇒ mọi đường dẫn đó gãy.

Đây không phải lỗi Higgs. Nó là lỗi **nền tảng** — nếu không sửa thì mọi thứ bạn làm sau này cũng gãy ở bước đầu.

**Sửa ở đâu.** Trong chính 273 file đó, ở dòng khai báo `ROOT` / `OUT` / các đường dẫn tới thư mục dữ liệu.

**Sửa cái gì.** Thay đường dẫn cứng bằng đường dẫn **tự tính từ vị trí file**:

```python
# TRƯỚC — gãy khi copy sang máy khác
ROOT = Path(r"D:\TEST\Gax\Audi")

# SAU — luôn đúng vì suy ra từ chính file đang chạy
ROOT = Path(__file__).resolve().parents[2]     # số 2 = số cấp thư mục từ file lên gốc repo
```

**Cách kiểm chứng.** 801/801 file `.py` compile sạch; 12/12 script pipeline import được và `ROOT` trỏ đúng
`D:\TEST\Gax\amber-eyes`; `edition.py` xác nhận đủ `script_tap02.json`, `acting_tap02.json`,
`tts_manifest_t02.json`, `audio_s_t02`.

**Trạng thái.** ✅ Xong — commit `1e79241` + `1b3cba4`.

---

## 3. Lỗi 2 — Đo CER sai: tưởng giọng đọc sai, thật ra là **đo** sai

Đây là lỗi quan trọng nhất, vì nó làm **toàn bộ kết luận H2 ban đầu sai**.

### 3.1 Triệu chứng

Lần đo đầu (96 bản pilot) cho kết quả:

| Vai | Nhiệt độ | CER trung bình | Tệ nhất |
|---|---|---:|---:|
| H | 0,7 | **12,38%** | 73,81% |
| D | 0,7 | 4,98% | 33,18% |
| C | 0,7 | 0,88% | 4,84% |

Câu tệ nhất (`1.03#1`) nghe có vẻ hỏng nặng. Nhưng lời gốc của nó là:

> *"Tháng bảy năm hai nghìn không trăm lẻ chín."*

còn máy nghe chép lại là:

> *"tháng 7 năm 2009."*

**Câu đó hoàn toàn đúng.** Sai chỉ ở chỗ: một bên viết **chữ**, một bên viết **số**.

### 3.2 Nguyên nhân — 4 mắt xích nối tiếp nhau

```
①  .work/tts_sentences.py:105
        text = vi_numbers(text)        ← đổi SỐ thành CHỮ trước khi gửi cho TTS
        "năm 2009"  →  "năm hai nghìn không trăm lẻ chín"

②  Model đọc theo lời đã đổi → audio nghe ra: "hai nghìn không trăm lẻ chín"   ✅ đúng

③  Máy nghe (listen_audio) nghe audio đó, nhưng lại CHÉP bằng CHỮ SỐ
        "năm 2009"                                                       ← bên này là số

④  Script đo CER chỉ chuẩn hóa ① (đổi số→chữ cho lời gốc), quên chuẩn hóa ③
        ⇒ so "hai nghìn không trăm lẻ chín"  vs  "2009"
        ⇒ 73,81% lỗi, dù câu đọc hoàn hảo
```

**Mắt xích ④ đúng y như luật `AGENTS.md` Q3(a) đã cảnh báo:**

> *"SỐ — chuẩn đã qua `vi_numbers()` nên là CHỮ còn bản chép là SỐ ⇒ **phải áp `vi_numbers()` cho CẢ HAI Vế**,
> nếu không CER phình to giả (một câu hoàn toàn đúng bị tính 21%, một câu 300%)"*

### 3.3 Mắt xích 5 — hàm `vi_numbers` trong script đo còn **sai hơn nữa**

Script đo có một bản `vi_numbers` rút gọn tự viết, chia số thành nhóm 3 chữ số kiểu dịch vụ TTS:

```
"2009" → "hai" + "không trăm lẻ chín"  →  ra "hai không"   ❌ sai
```

đúng cái mà `AGENTS.md` G11 cảnh báo (*"1.400" bị đọc thành "một phẩy bốn trăm"*).

### 3.4 Hệ quả phải xử lý thêm: **số đo MiniMax cũng bị lỗi này**

Bảng MiniMax đo trước đó (H 10,79%, D 5,60%) cũng bị phình theo **đúng** mắt xích ④.
⇒ **Không thể so sánh "cũ với mới" khi cả hai cùng sai.**
⇒ Phải **tính lại MiniMax** với cùng cách chuẩn hóa mới, rồi mới so.

### 3.5 Sửa ở đâu

**Ở script đo, KHÔNG ở code sản xuất.** Code sản xuất (`tts_sentences.py`) làm đúng — nó cần số→chữ để TTS đọc
tiếng Việt tự nhiên.

| File | Vai trò |
|---|---|
| `.work/kaggle_higgs/_vi_vi.py` | **MỚI** — hàm chuẩn hóa đúng, copy nguyên `vi_number()` của `tts_sentences.py` (xử lý nghìn/triệu/tỷ, "mốt"/"tư"/"lăm") + bảng biến thể cách đọc ("mốt"→"một", "linh"→"nghìn") |
| `.work/kaggle_higgs/_recer_fixed.py` | Tính lại CER từ cache bản chép (**không** gọi ASR lại) với chuẩn hóa cả hai vế |
| `.work/kaggle_higgs/_h2_fair_compare.py` | Tính lại MiniMax cùng cách + so sánh từng câu Higgs vs MiniMax |

### 3.6 Sửa cái gì — cụ thể

```python
# TRƯỚC (sai) — chỉ chuẩn hóa 1 vế
r["text_norm"] = norm(vi_numbers(txt))     # lời gốc: số → chữ
c = cer(txt, h)                             # bản chép: giữ nguyên số   ← LỖI Ở ĐÂY

# SAU (đúng) — chuẩn hóa CẢ HAI vế, dùng đúng vi_number của pipeline
ref = norm(canon(vi_numbers(clean(txt))))        # lời gốc
hyp = norm(canon(vi_numbers(clean(h))))          # bản chép  ← thêm dòng này
c = cer(ref, hyp)
```

### 3.7 Kết quả sau khi sửa — bức tranh đảo ngược

| Vai | Nhiệt độ | **CER sau khi sửa** | Trước khi sửa |
|---|---|---:|---:|
| H | 0,7 | 2,48% | 12,08% |
| H | **0,8** | **0,00%** (8/8 câu sạch) | 1,56% |
| D | 0,7 | 0,99% | 4,85% |
| D | **0,8** | 2,27% | 2,27% |
| C | **0,8** | **0,00%** (8/8 câu sạch) | 0,00% |
| N1 ← W1 | 0,7 | 1,08% | 1,08% |
| N2 ← W1 | 0,7 | 0,63% | 0,63% |

Và MiniMax tính lại: H **0,89%** (trước: 10,79%) · D **1,72%** (trước: 5,60%) · C/N1/N2 **0,00%**.

⇒ **Higgs tốt hơn MiniMax rõ rệt ở vai H** (0,00% vs 0,89%), và tệ hơn ở D một chút (2,27% vs 1,72%, xử lý bằng lỗi 3).

---

## 4. Lỗi 3 — Chọn sai nhiệt độ cho vai D

**Triệu chứng.** Với vai D, nhiệt độ 0,7 cho CER trung bình **thấp hơn** (0,99%) so với 0,8 (2,27%) —
nghe như 0,7 tốt hơn. Nhưng đo thời lượng thì lộ ra vấn đề:

| Câu | t=0,7 | t=0,8 |
|---|---:|---:|
| `2.05#15` | **47,56 s** ❌ (quá 47 s) | 15,3 s ✅ |
| `2.05#16` | **32,6 s** ❌ (âm tiết/s 0,40 ⇒ đọc loạn) | 4,8 s ✅ |

**Nguyên nhân.** Ở nhiệt độ thấp, model bám sát lời gốc quá chặt và **không biết khi nào dừng** — nó lặp lại
(dài 47,56 s) hoặc đọc lê thê. Nhiệt độ cao hơn một chút thì model "thoát" được, đọc đúng thời lượng.

**Sửa ở đâu.** Ở tham số sinh (`gen_params` trong `pilot_spec*.json` → `CAST_HIGGS` khi chốt).

**Sửa cái gì.** Dùng **`temperature 0,8` cho cả 3 vai chính** (H, D, C) + **sinh 3 bản/câu** (§7) để có
phiên bản dự phòng cho câu vẫn lỗi. Bỏ nhiệt độ 0,7 cho D.

**Kết quả chốt.** `H = 0,8` (CER 0,00%) · `C = 0,8` (CER 0,00%) · `D = 0,8` (CER 2,27%, dùng đa bản).

---

## 5. Lỗi 4 — File quá dài 47 s

**Triệu chứng.** 2/96 file dài 47,56 s (vượt giới hạn 47 s của §8): `2.05#14` ở t=0,6 và `2.05#15` ở t=0,7.

**Nguyên nhân.** Cùng nguyên nhân với lỗi 3 — model không dừng. Đây là **hiện tượng của model**, không phải
lỗi code, nên không sửa bằng code được.

**Sửa ở đâu.** ở quy trình sinh: khi sinh 3 bản/câu, **loại bản vượt 47 s**, giữ bản đạt nhất.

**Sửa cái gì.** Thêm bước lọc theo §8 trước khi chọn bản thắng:
`0,5 s < dài < 47 s` · không lặng > 0,3 s ở −60 dB · không đuôi tạp âm.

**Đã xử lý bằng cách nào.** Đổi nhiệt độ D sang 0,8 (lỗi 3) ⇒ **không còn file nào vượt 47 s** trong 96 bản
còn lại (chỉ 2 file ở nhiệt độ 0,6/0,7 bị loại).

**Phụ cần biết.** 33/96 file có đỉnh vượt −1,5 dBFS. Bước mix (`build_audio3.py`) có loudnorm 2-pass
(`I=-16:TP=-1.5`) nên sẽ xử lý ở H4 — nhưng phải kiểm lại sau khi mix.

---

## 6. Lỗi 5 — G9 vai H ↔ vai D: hai giọng nam gần như cùng cao độ

Đây là lỗi **chưa sửa được bằng code** và là lý do bạn cần quyết.

### 6.1 Triệu chứng

Sau khi đo F0 trên **audio đã sinh ra** (không phải clip gốc):

| Vai | F0 trung vị | Khoảng cách | Yêu cầu | Kết luận |
|---|---:|---:|---:|---|
| H | 124,3 Hz | **0,23 nửa cung** | ≥ 4 | ❌ **TRƯỢT** |
| D | 122,6 Hz | | | |

Hai vai nam gần như **cùng một cao độ** ⇒ người nghe dễ lẫn. Đây là loại lỗi mà luật G9 sinh ra để chặn.

**Kiểm chéo bằng 2 thuật toán khác nhau** (để chắc chắn không phải lỗi đo):

| Thuật toán | H | D | Khoảng cách |
|---|---:|---:|---:|
| AC thô (`voice_audition.py`) | 129,0 Hz | 120,9 Hz | 1,12 nc |
| AC chuẩn hóa + nội suy parabol + sửa lỗi octave | 124,3 Hz | 122,6 Hz | **0,23 nc** |

Cả hai đều dưới 4 ⇒ **lỗi thật**.

### 6.2 Nguyên nhân — Higgs không giữ cao độ của clip tham chiếu

Đây là mắt xích quan trọng. F0 của **clip gốc** và F0 của **audio clone** lệch nhau, và lệch **ngược chiều**:

| Vai | F0 clip gốc | F0 audio clone | Lệch |
|---|---:|---:|---:|
| H | 107 Hz | 124 Hz | **+16%** |
| D | 132 Hz | 123 Hz | **−7%** |
| C | 200 Hz | 192 Hz | −4% |
| N1 ← W1 | 235 Hz | 229 Hz | −3% |

H bị đẩy **lên** 16%, D bị đẩy **xuống** 7% ⇒ hai vai **trôi ngược chiều vào cùng một vùng ~123 Hz**.
Clip gốc cách nhau 25 Hz thì âm thanh clone ra gần như trùng nhau.

*(Bổ sung: nếu **không** truyền `reference_audio`, Higgs đọc sai thanh điệu nặng — "Trở lại đan" thay vì
"Trò tôi đan". ⇒ clone là bắt buộc, không phải tuỳ chọn.)*

### 6.3 Vì sao 7 clip tham chiếu hiện có **không đủ**

Clip nam trong bộ VoxCPM2 VI có F0: H 107 Hz · W4 137 Hz · D 128 Hz · W3 162 Hz.
Cao nhất là W3 (162 Hz) → audio clone về ~150 Hz ⇒ H↔D chỉ ≈ 3,3 nc, **vẫn dưới 4**.

Muốn đạt 4 nc, cần một trong hai:
- **clip cho H** có F0 thấp hơn (audio clone về ≤ 97 Hz ⇒ clip gốc ~80 Hz), hoặc
- **clip cho D** có F0 cao hơn (audio clone về ≥ 157 Hz ⇒ clip gốc ~170 Hz).

⇒ **Cần tạo clip VoxCPM2 VI mới.** Bộ clip này sinh được bằng VoxCPM2 Voice Design trên Mac mini của bạn
(~30 phút), và là **Apache-2.0** nên không vướng gì.

### 6.4 Pilot v4 — lần đo độc lập thứ hai (bộ seed khác)

Pilot v4 sinh lại **96 bản baseline bằng bộ seed khác hẳn** (thêm `|v0` vào công thức hash seed).
Mục tiêu: chứng minh lỗi G9 H↔D **không phải do may rủi seed** mà là đặc tính của mô hình.

| Vai | F0 (bộ seed 1 — pilot v3) | F0 (bộ seed 2 — pilot v4) | Kết luận |
|---|---:|---:|---|
| H ← H.wav | 128,3 / 130,4 / 131,1 Hz | 130,4 / 130,4 / 131,1 Hz | **ổn định** |
| D ← D.wav | 120,0 / 123,1 / 117,6 Hz | 126,0 / 123,1 / 123,7 Hz | **ổn định** |
| C ← C.wav | 203,4 / 206,9 / 205,1 Hz | 208,7 / 205,1 / 208,7 Hz | **ổn định** |
| **H ↔ D** | 1,12 nc | **1,01 nc** (AC thô) · **0,04 nc** (AC chuẩn hóa) | ❌ **trượt ở cả 2 lần đo** |

⇒ **Xác nhận lỗi G9 H↔D là đặc tính mô hình, không phải nhiễu seed.** Cùng lần đó, bộ seed thứ hai cho thấy
`temperature 0,7` lại sinh file **47,6 s** cho cả H lẫn D (bộ seed 1 chỉ D bị) ⇒ củng cố lựa chọn
**`temperature 0,8`** cho cả 3 vai chính.

> ⚠ **Lỗi notebook đã phát hiện:** notebook pilot v4 nạp nhầm `pilot_spec.json` (bản v3) thay vì
> `pilot_spec_v4.json` — `REF_DIR` tìm đúng thư mục nhưng dòng `SPEC = json.load(...)` lấy sai tên file.
> Hệ quả: chạy lại spec cũ với seed mới (96 bản) thay vì 104 bản đúng đặc tả.
> Đã sửa + verify (6/6 check, 14/14 cell compile) và đẩy lại **kernel v5**.

### 6.5 Đang đo gì (pilot v5, chạy trên Kaggle)

104 bản, **chỉ đo — không gán vai** (đúng luật L4):

| Nhóm | Nội dung | Mục đích |
|---|---|---|
| **A** | H và D clone từ **W3** và từ **W4**, 8 câu mỗi cặp, t=0,8 (32 bản) | Đo F0 **thật** của audio clone khi đổi clip, thay vì suy đoán từ clip gốc |
| **B** | D (t=0,7 và t=0,8), N1, N2 × 3 biến thể seed (72 bản) | Kiểm chọn-bản-tốt-nhất có kéo D/N1/N2 về CER < 2% không |

### 6.6 Ba lựa chọn — người dùng đã chọn (a)

| | Cách làm | Đánh đổi |
|---|---|---|
| **(a)** ✅ | Tạo clip VoxCPM2 VI mới: một nam rất trầm (~80 Hz) cho **H**, **hoặc** một nam cao (~170 Hz) cho **D** | Mất ~30 phút trên Mac mini. Giữ được cả CER lẫn G9 |
| **(b)** | Dùng clip **MiniMax** làm clip tham chiếu cho Higgs | Nhanh, nhưng **cần xác nhận điều khoản**. F0 clip MiniMax: H 101 Hz · D 140 Hz — chưa chắc đủ |
| **(c)** | Ghi nhận vi phạm G9, chỉ dựa vào **nghe mù** | Nhanh nhất, nhưng vi phạm G9 |

**Đã chốt: (a).** Bộ cục: `.work/voxcpm_generate_g9.py` + `.work/voxcpm_refs_manifest_g9.json`
(dò thang `control` tự động) · hướng dẫn đầy đủ: `.work/G9_HD_HUONG_DAN.md`.

**Hướng được chọn (ưu tiên A):** hạ **H** xuống (~85 Hz) thay vì nâng D lên — vì vai H vốn được mô tả
*"low-pitched, deep chesty resonance"* nên giọng trầm hợp vai hơn, còn vai D giữ được
*"late fifties, gravelly"*. Script vẫn sinh **cả hai** bộ (`M_LOW` + `M_HIGH`) để chọn bằng số đo thật.

### 6.7 Pilot v5 XONG — trả lời được câu hỏi mấu chốt

**Kết quả kernel:** 104/104 bản OK, 0 lỗi · frame-rate 25,02 Hz · `max_new_tokens` 1196 ·
RTF tb 2,07 (max 3,15) · VRAM đỉnh 9,94 GB · tổng 1446,6 s sinh.

**Số đo F0 (n = 8 mỗi ô, temp 0,8):**

| Vai | Clip tham chiếu | F0 clip | F0 clone (AC thô) | F0 clone (AC chuẩn hóa) | Tỉ lệ |
|---|---|---:|---:|---:|---:|
| H | H.wav | 107 Hz | 131,1 Hz | 125,7 Hz | 1,22 |
| D | D.wav | 132 Hz | 123,1 Hz | 125,7 Hz | 0,93 |
| **H** | **W4.wav** | 134 Hz | **140,4 Hz** | 134,2 Hz | 1,05 |
| **D** | **W4.wav** | 134 Hz | **141,2 Hz** | 139,9 Hz | 1,06 |
| **H** | **W3.wav** | 157 Hz | **162,2 Hz** | 158,0 Hz | 1,04 |
| **D** | **W3.wav** | 157 Hz | **160,0 Hz** | 157,8 Hz | 1,02 |

**Đây là kết luận quan trọng nhất của toàn bộ đợt đo:**

> **Cùng MỘT clip tham chiếu, cho HAI vai khác nhau ⇒ F0 clone gần như y hệt**
> (W4: 140,4 vs 141,2 · W3: 162,2 vs 160,0).
> ⇒ **Cao độ audio clone do clip tham chiếu quyết định**, không phải do vai.
> ⇒ Giả thuyết "Higgs kéo mọi giọng nam về cùng một vùng ~125 Hz" **bị bác bỏ**.

**G9 H↔D — duyệt cả 9 tổ hợp (H clip × D clip):**

| H clip | D clip | H F0 | D F0 | nc (AC thô) | nc (AC chuẩn hóa) | Kết luận |
|---|---|---:|---:|---:|---:|---|
| W4 | D.wav | 140,4 | 123,1 | 2,28 | 1,13 | ❌ trượt |
| W4 | W4 | 140,4 | 141,2 | 0,10 | 0,72 | ❌ trượt |
| W4 | W3 | 140,4 | 160,0 | 2,26 | 2,80 | ❌ trượt |
| **W3** | **D.wav** | 162,2 | 123,1 | **4,78** | **3,96** | ⚠ **cảnh báo** |
| W3 | W4 | 162,2 | 141,2 | 2,40 | 2,11 | ❌ trượt |
| W3 | W3 | 162,2 | 160,0 | 0,24 | 0,02 | ❌ trượt |

**Đọc kết quả:**
1. **Clip có sẵn không cứu được H↔D.** Tổ hợp tốt nhất `H←W3 + D←D.wav` = 4,78 nc (AC thô) nhưng
   3,96 nc (AC chuẩn hóa) ⇒ chưa chắc đạt 4 nc theo cả 2 thuật toán. Hơn nữa W3 là giọng **nam trẻ**
   còn vai H là người dẫn chuyện trầm ấm ⇒ **vẫn cần clip mới**.
2. **Cơ chế đã rõ ⇒ clip mới sẽ có tác dụng.** Tỉ lệ `clone / clip` ở ref từ 132 Hz trở lên là
   **1,02–1,06** (rất ổn định). Chỉ ở ref **thấp** (H.wav 107 Hz) tỉ lệ nhảy lên **1,22**.
   ⇒ Đã **hạ dải mục tiêu của `M_LOW` từ 80–92 xuống 70–86 Hz** để chừa biên cho cú kéo lên này.
3. **Bổ phòng:** nếu `M_LOW` vẫn ra > 97 Hz thì dùng **cả `M_LOW` + `M_HIGH`** cho H và D
   (margin ~10 nc) — G9 chắc chắn đạt, đổi lại vai D thành tenor cao.

**Hai phát hiện phụ từ pilot v5:**
- **`temperature 0,7` runaway ở D 2.05#15 và 2.05#16** → 47,56 s (đúng 2 câu đã có CER cao ở pilot v3).
  Ở `temperature 0,8` hai câu này ra 2,2–15,3 s ⇒ **xác nhận lần thứ 3 rằng t=0,8 là lựa chọn đúng**.
- **43/104 file vượt −1,5 dBFS** ⇒ `build_audio3.py` (loudnorm 2-pass, TP=−1,5) sẽ xử lý ở H4;
  phải kiểm lại sau khi mix.
- Cờ `tag_words_risk` trong manifest **bị đặt sai** (nó kiểm tra *text đầu vào* vốn đã chứa thẻ, nên
  52/104 "có" là hệ quả tất yếu, không phải lỗi model). Đã kiểm lại đúng cách trên **349 bản chép ASR
  thật** trong cache: **không bản chép nào chứa từ khoá thẻ** (`emotion`/`sadness`/`fear`/`surprise`/
  `pause`/`prosody`/`style:`/`sfx:`) ⇒ **§5 an toàn**.

### 6.8 Tóm tắt trạng thái sau pilot v5

| Việc | Trạng thái |
|---|---|
| G9 H↔D — cơ chế | ✅ **Đã rõ**: F0 clone do clip tham chiếu quyết định (tỉ lệ 1,02–1,06 ở ref ≥ 132 Hz) |
| G9 H↔D — clip cần tạo | ⏳ Chờ user chạy script trên Mac mini (`M_LOW` 70–86 Hz + `M_HIGH` 168–182 Hz) |
| G9 N1↔N2 | ⏳ Cần clip **nữ trầm** `W6_LOW` (148–162 Hz) — chi tiết ở §7 |
| temperature | ✅ `0,8` cho H/D/C — xác nhận lần 3 (t=0,7 runaway 47,56 s ở D 2.05#15/#16) |
| §5 thẻ emotion | ✅ an toàn — kiểm trên 349 bản chép ASR thật, không có từ khoá thẻ |
| CER | ✅ đạt (H 0,00% · C 0,00% · N2 0,63%); D 2,27% cần đa bản §7 |

---

## 7. Lỗi 6 — Vai N1: cặp N1↔N2 chưa từng được kiểm, và phương án cũ tạo ra vi phạm mới

> **Đính chính 30/10/2026 (sau khi đo đủ số liệu).** Mục này viết lại từ đầu. Bản cũ chỉ kiểm
> **C↔N1** và **C↔N2**, bỏ sót cặp thứ ba.

### 7.1 Triệu chứng

Tập 02 có **3 vai nữ**: C (chuyên gia tâm lý), N1 (người kể thứ nhất), N2 (người kể thứ hai).
Luật **G9** (`AGENTS.md` dòng 111) áp dụng cho **mọi cặp cùng giới** ⇒ cần đủ **3 cặp**:
C↔N1 · C↔N2 · **N1↔N2**.

Đo lại **192 audio** của pilot v3 + pilot v4 (n = 8 mỗi ô N1/N2):

| Cặp | F0 hai vai | Khoảng cách (AC thô / AC chuẩn hóa) | Ngưỡng | Kết luận |
|---|---:|---:|---:|---|
| C ↔ N1 (N1 ← W1) | 205 Hz / 247 Hz | 3,25 / 3,17 nc | ≥ 4 | ❌ trượt |
| C ↔ N2 (N2 ← W1) | 205 Hz / 276 Hz | 5,13 / 4,88 nc | ≥ 4 | ✅ **đạt** |
| **N1 ↔ N2** (cả hai ← W1) | 247 Hz / 276 Hz | **1,89 / 1,71 nc** | ≥ 4 | ❌ **trượt — chưa từng được kiểm** |

Ứng viên clip nữ cho N1 (đo cả 2 bộ seed):

| Ứng viên cho N1 | CER | G9 với C | G9 với N2 (W1) | Kết luận |
|---|---:|---:|---:|---|
| **W1** (nữ trẻ, F0 235 Hz) | 1,08% ✅ | 3,25 nc ❌ | **1,89 nc ❌** | đọc đúng nhưng **không tách** được |
| W2 (nữ 50, F0 189 Hz) | 2,86% ❌ | 0,72 nc ❌ | 3,09 nc ❌ | trượt cả hai |
| W3 | 4,25% ❌ | 4,64 nc ✅ | 6,35 nc ✅ | tách được nhưng **đọc sai** — và W3 là giọng **nam**, sai giới tính vai N1 |

### 7.2 Nguyên nhân — phương án "nâng N1 lên cao" là hướng sai

Bản cũ chốt: đưa N1 lên ~258 Hz (`W5_HIGH`) để sửa C↔N1. Điều đó **đúng một nửa**:

- C (205 Hz) và N2 (276 Hz) đã cách nhau 5,13 nc ✅ ⇒ giữa chúng **không còn chỗ** để đặt N1.
  Muốn N1 cách **cả hai** ≥ 4 nc, N1 phải **≤ 163 Hz** (hoặc ≥ 348 Hz — giọng nữ soprano cực cao, không khả thi).
- Nếu đặt N1 ở 258–276 Hz thì N1 **áp sát N2** (276 Hz) ⇒ khoảng cách rơi về **~1,7 nc** ❌.
  Tức là **một vi phạm G9 mới**, chỉ đổi tên người vi phạm.

⇒ Với C = 205 Hz và N2 = 276 Hz đã chốt, N1 **bắt buộc phải là giọng nữ THẤP**, không phải cao.

### 7.3 Sửa ở đâu

Tạo clip VoxCPM2 VI nữ **thấp** — `W6_LOW`, F0 clip **148–162 Hz** (lấy chính 4 câu của N1 làm văn bản mẫu
để chất giọng khớp vai).

### 7.4 Sửa cái gì — 3 phương án, đo được luôn

| Phương án | C ↔ N1 | C ↔ N2 | N1 ↔ N2 | Clip mới cần |
|---|---:|---:|---:|---|
| **A (khuyến nghị)** `N1 ← W6_LOW` (~155 Hz), `N2 ← W1` | 4,6–4,8 ✅ | 4,9–5,1 ✅ | 9,5–9,8 ✅ | 1 clip nữ trầm |
| B `N1 ← W5_HIGH` (~265 Hz), `N2 ← W6_LOW` | 4,0 ⚠ | 4,6–4,8 ✅ | 9,5–9,8 ✅ | 2 clip (nữ cao + nữ trầm) |
| C giữ nguyên `N1 ← W1`, `N2 ← W1` | 3,25 ❌ | 5,13 ✅ | 1,89 ❌ | không đạt G9 |

⇒ Script sinh **cả `W6_LOW` lẫn `W5_HIGH`** trong cùng 1 lần chạy để bạn chọn sau khi đo.
Nếu theo khuyến nghị (A): chỉ cần `W6_LOW` cho N1; `N2` giữ `W1` (đã có sẵn, CER 0,63% ✅).

### 7.5 Lưu ý thực tế (kiểm lại kịch bản)

N1 chỉ có 4 câu, **toàn bộ ở hồi 1**; C chỉ xuất hiện ở hồi 3/4/5; N2 ở hồi 4
⇒ **N1 không bao giờ cùng hồi với C, cũng không cùng hồi với N2.** Người nghe không gặp chúng cạnh nhau.
Vì vậy đây là vấn đề **về con số luật**, không phải vấn đề về người nghe — nhưng G9 viết chung cho mọi
cặp cùng giới, nên vẫn nên sửa cho sạch.

---

## 8. Bảng số đo đầy đủ

### 8.1 CER — Higgs (96 bản, 2 lượt ASR/câu, lấy lượt xấu hơn)

| Vai | Clip | Nhiệt độ | n | CER tb | CER max | >2% | F0 (AC thô) | F0 (kiểm chéo) |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| H | H.wav | 0,6 | 8 | 1,29% | 7,14% | 2/8 | 128 Hz | 124 Hz |
| H | H.wav | 0,7 | 8 | 2,48% | 7,46% | 3/8 | 130 Hz | 123 Hz |
| **H** | **H.wav** | **0,8** | 8 | **0,00%** | **0,00%** | **0/8** | 131 Hz | 127 Hz |
| D | D.wav | 0,6 | 8 | 3,29% | 9,38% | 5/8 | 120 Hz | 123 Hz |
| D | D.wav | 0,7 | 8 | 0,99% | 5,21% | 1/8 | 123 Hz | 127 Hz |
| **D** | **D.wav** | **0,8** | 8 | 2,27% | 9,38% | 3/8 | 118 Hz | 122 Hz |
| C | C.wav | 0,6 | 8 | 1,01% | 8,06% | 1/8 | 203 Hz | 193 Hz |
| C | C.wav | 0,7 | 8 | 0,88% | 4,84% | 1/8 | 207 Hz | 197 Hz |
| **C** | **C.wav** | **0,8** | 8 | **0,00%** | **0,00%** | **0/8** | 205 Hz | 192 Hz |
| **N1** | **W1.wav** | 0,7 | 4 | 1,08% | 3,23% | 1/4 | 245 Hz | 229 Hz |
| N1 | W2.wav | 0,7 | 4 | 2,86% | 6,59% | 2/4 | 197 Hz | 190 Hz |
| N1 | W3.wav | 0,7 | 4 | 4,25% | 7,53% | 3/4 | 158 Hz | 150 Hz |
| **N2** | **W1.wav** | 0,7 | 4 | 0,63% | 2,53% | 1/4 | 276 Hz | 256 Hz |
| N2 | W2.wav | 0,7 | 4 | 1,27% | 5,06% | 1/4 | 207 Hz | 194 Hz |
| N2 | W3.wav | 0,7 | 4 | 1,58% | 6,33% | 1/4 | 165 Hz | 156 Hz |

### 8.2 MiniMax — tính lại cùng cách chuẩn hóa (32 câu pilot)

| Vai | n | CER tb | CER max | >2% | *Số cũ (bị lỗi Q3a)* |
|---|---:|---:|---:|---:|---|
| C | 8 | 0,00% | 0,00% | 0/8 | 0,00% |
| D | 8 | 1,72% | 5,69% | 3/8 | *5,60%* |
| H | 8 | 0,89% | 7,14% | 1/8 | *10,79%* |
| N1 | 4 | 0,00% | 0,00% | 0/4 | 0,00% |
| N2 | 4 | 0,00% | 0,00% | 0/4 | 0,00% |

### 8.3 So từng câu ở cấu hình đề xuất

| Vai | Higgs | MiniMax | Ai thắng |
|---|---:|---:|---|
| H (t=0,8) | 0,00% | 0,89% | **Higgs** (câu `1.03#1`: 0,00% vs 7,14%) |
| C (t=0,8) | 0,00% | 0,00% | hòa |
| D (t=0,8) | 2,27% | 1,72% | MiniMax nhẹ — xử lý bằng đa bản §7 |
| N1 (W1, t=0,7) | 1,08% | 0,00% | MiniMax (chênh 1 câu) |
| N2 (W1, t=0,7) | 0,63% | 0,00% | MiniMax (chênh 1 câu) |

Câu lỗi còn lại ở cấu hình đề xuất:
`D 2.05#15` 3,79% (MiniMax 5,69%) · `D 2.05#16` 3,39% (MiniMax 3,39%) · `D 1.17#5` 9,38% (MiniMax 0,00%) ·
`C 3.05#3` bị ASR chặn 1 lượt.

### 8.4 G9 — bảng đầy đủ

| Cặp | Higgs (audio đã clone) | MiniMax (bộ hiện tại) | Ngưỡng | Kết luận |
|---|---:|---:|---:|---|
| **H ↔ D** | **0,23 nc** | 5,54 nc | ≥ 4 | ❌ **TRƯỢT** |
| C ↔ N1 (W1) | 2,98 nc | 3,07 nc | ≥ 4 | ❌ trượt |
| C ↔ N1 (W2) | 0,19 nc | — | ≥ 4 | ❌ trượt |
| C ↔ N1 (W3) | 4,34 nc | — | ≥ 4 | ✅ *(nhưng CER 4,25% + sai giới tính)* |
| **C ↔ N2 (W1)** | **4,97 nc** | 1,78 nc | ≥ 4 | ✅ **đạt** |
| C ↔ N2 (W2) | 0,11 nc | — | ≥ 4 | ❌ trượt |
| C ↔ N2 (W3) | 3,63 nc | — | ≥ 4 | ❌ trượt |
| H/D ↔ N1/N2 | 7,36–7,92 nc | — | ≥ 4 | ✅ đạt |

### 8.5 Môi trường đo được

| Mục | Giá trị |
|---|---|
| Model | `bosonai/higgs-tts-3-4b` (trọng số **gốc**) + 2 file loader mượn từ `multimodalart/…` + `auto_map` tự thêm |
| transformers / torch | 5.22.0 / 2.11.0+cu128 |
| GPU | Tesla T4 15,6 GB (sm_75), **bf16 có** |
| Lớp model | `HiggsMultimodalQwen3ForConditionalGeneration`, `num_codebooks` = 8 |
| Frame-rate bộ giải mã | **25,02 Hz** ⇒ `max_new_tokens = int(47,5 × 25,02) + 8 = 1196` |
| VRAM đỉnh / RTF | 9,94 GB / tb 2,15 (max 2,98) |
| Sinh | 96/96 OK, 0 lỗi, tổng 1522,6 s |
| Thẻ `<|…|>` | **Có tác dụng** — bản chép không chứa từ khóa thẻ |
| API | `generate_speech(text, tok, *, reference_codes, reference_text, max_new_tokens, temperature, top_p, top_k)` — **không có** `speed_*`/`pitch_*` (⇒ G4/G5 tự đạt), **không có** tham số seed (⇒ phải `torch.manual_seed` + `torch.cuda.manual_seed_all`) |

### 8.6 Pilot v4 — bộ seed thứ 2, xác nhận lại G9 (96 bản)

| Vai | Clip | Temp | n | F0 (AC thô) | F0 (AC chuẩn hóa) | Thời lượng | So với bộ seed 1 |
|---|---|---:|---:|---:|---:|---|---|
| H | H.wav | 0,8 | 8 | 131,1 Hz | 125,7 Hz | 2,4–13,7 s | ✓ khớp (131,1) |
| D | D.wav | 0,8 | 8 | 123,7 Hz | 126,0 Hz | 2,2–14,4 s | ✓ khớp (117,6–123,1) |
| C | C.wav | 0,8 | 8 | 208,7 Hz | 198,9 Hz | 4,4–13,4 s | ✓ khớp (205,1) |
| D | D.wav | **0,7** | 8 | 123,1 Hz | 126,6 Hz | 2,2–**47,6 s** ❌ | runaway lặp lại ở seed khác |
| H | H.wav | **0,7** | 8 | 130,4 Hz | 126,1 Hz | 2,5–**47,6 s** ❌ | runaway lặp lại ở seed khác |
| N1 | W1.wav | 0,7 | 4 | 247,4 Hz | 234,9 Hz | 4,7–7,2 s | ✓ khớp (244,9) |
| N2 | W1.wav | 0,7 | 4 | 275,9 Hz | 259,6 Hz | 5,0–8,4 s | ✓ khớp (275,9) |
| N2 | W3.wav | 0,7 | 4 | 172,7 Hz | 166,3 Hz | 4,7–9,0 s | C↔N2(W3) = 3,28 nc — vẫn trượt |

**Kết luận pilot v4:**
1. **G9 H↔D trượt ở cả hai bộ seed** (1,12 nc và 1,01/0,04 nc) ⇒ **lỗi đặc tính mô hình, không phải nhiễu seed.**
2. **`temperature 0,7` sinh file 47,6 s ở cả H lẫn D, ở cả hai bộ seed** ⇒ `temperature 0,8` là lựa chọn
   đúng, không phải do may rủi.
3. F0 của các clip gốc là **ổn định qua seed** (H 131 Hz, D 121–124 Hz, C 205–209 Hz, N2←W1 276 Hz)
   ⇒ đường cong "drift" giữa clip gốc và audio clone là **đặc tính ổn định của Higgs**, dùng được để
   tính ngược F0 clip mới cần tạo.

> ⚠ **Lỗi notebook đã phát hiện & sửa:** notebook pilot v4 nạp nhầm `pilot_spec.json` (bản v3) thay vì
> `pilot_spec_v4.json` — `REF_DIR = find_dir_containing("pilot_spec_v4.json")` tìm đúng thư mục nhưng dòng
> `SPEC = json.load(open(..., "pilot_spec.json"))` lấy sai tên file ⇒ chạy lại spec cũ (96 bản, seed mới)
> thay vì 104 bản đúng đặc tả. Đã sửa, verify (6/6 check + 14/14 cell compile), đẩy lại **kernel v5**.

### 8.7 Bảng G9 đầy đủ — gộp cả 2 bộ pilot (192 audio)

Đo lại bằng 1 script duy nhất (`.work/g9_matrix.py`), 2 thuật toán F0 (AC thô + AC chuẩn hóa/parabolic),
gộp pilot v3 + pilot v4 ⇒ **n = 16** mỗi ô C/D/H, **n = 8** mỗi ô N1/N2.

**F0 thực của audio clone:**

| Vai | Clip | Temp | n | F0 (AC thô) | F0 (AC chuẩn hóa) | min–max (AC thô) |
|---|---|---:|---:|---:|---:|---|
| H | H.wav | 0,8 | 16 | 131,1 Hz | 125,7 Hz | 94,1 – 206,9 |
| D | D.wav | 0,8 | 16 | 122,4 Hz | 125,6 Hz | 109,1 – 181,8 |
| C | C.wav | 0,8 | 16 | 205,1 Hz | 194,9 Hz | 196,7 – 212,4 |
| N1 | W1.wav | 0,7 | 8 | 247,4 Hz | 234,0 Hz | 237,6 – 255,3 |
| N1 | W2.wav | 0,7 | 8 | 196,7 Hz | 189,5 Hz | 189,0 – 201,7 |
| N1 | W3.wav | 0,7 | 8 | 156,9 Hz | 149,3 Hz | 149,1 – 162,2 |
| N2 | W1.wav | 0,7 | 8 | 275,9 Hz | 258,3 Hz | 242,4 – 298,1 |
| N2 | W2.wav | 0,7 | 8 | 206,9 Hz | 198,7 Hz | 187,5 – 216,2 |
| N2 | W3.wav | 0,7 | 8 | 171,4 Hz | 165,0 Hz | 148,6 – 184,6 |

**G9 — mọi cặp cùng giới:**

| Cặp | nc (AC thô) | nc (AC chuẩn hóa) | Kết luận |
|---|---:|---:|---|
| H ↔ D | 1,19 | 0,01 | ❌ trượt |
| C ↔ N1 (W1) | 3,25 | 3,17 | ❌ trượt |
| C ↔ N2 (W1) | 5,13 | 4,88 | ✅ đạt |
| **N1 ↔ N2** (cả hai ← W1) | **1,89** | **1,71** | ❌ **trượt** |
| C ↔ N1 (W3) | 4,64 | 4,61 | ✅ *(nhưng W3 là giọng nam)* |
| N1 ↔ N2 (N1←W3, N2←W1) | 9,77 | 9,49 | ✅ đạt |

**Duyệt toàn bộ 16 phân bố (N1_clip, N2_clip) từ clip có sẵn** — duy nhất đạt đủ 3 cặp là
`N1 ← W3` + `N2 ← W1`, nhưng W3 là **giọng nam** ⇒ **không dùng được** cho vai nữ N1.
⇒ Bắt buộc phải tạo clip nữ mới.

**Khoảng F0 cần có cho clip mới (tính từ số đo trên, không ước lượng):**

| Clip mới | Điều kiện trên **audio clone** | ⇒ Dải F0 của **clip tham chiếu** |
|---|---|---|
| cho **H** | clone ≤ 97,1 Hz | 70–100 Hz → `M_LOW` (80–92) |
| cho **D** | clone ≥ 165,2 Hz | 150–190 Hz → `M_HIGH` (168–182) |
| cho **N1** | clone ≤ 162,8 Hz | 140–175 Hz → **`W6_LOW` (148–162)** |

> ⚠ Tỉ lệ `clone / clip gốc` đo được dao động **0,93 → 1,22** ở 9 tổ hợp vai × clip
> (H: 107→131 Hz **+22%**; N2←W1: 235→276 Hz **+17%**; D: 132→122 Hz **−7%**).
> ⇒ Không suy ra được chắc chắn; **mọi clip mới đều phải đo lại bằng pilot** trước khi chốt vai.

---

## 9. Việc cần bạn quyết

| # | Câu hỏi | Lựa chọn | Quyết định |
|---|---|---|---|
| 1 | **G9 H↔D** — làm gì để tách 2 vai nam? | (a) tạo clip VoxCPM2 mới · (b) dùng clip MiniMax · (c) ghi nhận vi phạm | ✅ **(a)** — đã chọn |
| 2 | **G9 N1** — làm gì cho vai nữ phụ? | (a) tạo clip nữ mới ~265 Hz · (b) chấp nhận ~2,95 nc | ✅ **(a)** — đã chọn *(đính chính 30/10: hướng (a) của bản cũ là nữ **cao**; đo đủ số liệu cho thấy phải là nữ **thấp** — xem §7)* |
| 3 | **Ghi công Boson** (H0) — xác nhận chấp nhận? | (a) chấp nhận, ghi công trong mọi tập · (b) chưa | ⏸ **(b)** — **dừng trước H4** tới khi chốt |
| 4 | **Thứ tự tạo clip mới** | — | Script sinh **cả 4 bộ** `M_LOW` + `M_HIGH` + `W6_LOW` + `W5_HIGH` trong 1 lần chạy |

**Việc bạn cần làm tiếp theo (1 lệnh trên Mac mini):**
```bash
cd /Users/duonganhhai/CodeGit/amber-eyes
/Users/duonganhhai/ai/voxcpm2_project/.venv/bin/python3 .work/voxcpm_generate_g9.py
git add assets/voice_ref_voxcpm2_g9 && git commit -m "feat(audio): them 4 clip tham chieu VoxCPM2 cho G9 (Tap 02)" && git push
```
Hướng dẫn đầy đủ: `.work/G9_HD_HUONG_DAN.md` · đặc tả ngắn: `.work/DAT_SPEC_G9.md`.

Sau khi có clip: pilot v5/v6 (đo F0 clone + CER) → chốt ánh xạ vai → **H3** (nghe mù V7 + G8) →
sinh 203 câu (3 bản/câu) → **H4** *(đang dừng chờ chốt ghi công)* → **H5** (dựng video).

---

## 10. Danh sách file liên quan

### Code sửa / tạo cho việc đo

| File | Vai trò |
|---|---|
| `.work/kaggle_higgs/_vi_vi.py` | **MỚI** — chuẩn hóa số đúng (copy `vi_number()` của pipeline) |
| `.work/kaggle_higgs/_recer_fixed.py` | Tính lại CER 2 vế từ cache |
| `.work/kaggle_higgs/_h2_fair_compare.py` | Tính lại MiniMax + so từng câu |
| `.work/kaggle_higgs/_f0_crosscheck.py` | F0 thuật toán thứ 2 (kiểm chéo) |
| `.work/kaggle_higgs/_analyze_h2.py` | Bảng chi tiết theo câu |
| `.work/kaggle_higgs/_do_cer_pilot.py` | Script đo gốc (có lỗi Q3a — giữ nguyên để đối chiếu) |
| `.work/kaggle_higgs/_build_pilot_v4.py` | Sinh `pilot_spec_v4.json` |
| `.work/kaggle_higgs/_make_nb_v4.py` → `_build_nb_v4.py` | Sinh notebook Kaggle v4 (đã sửa lỗi nạp nhầm spec) |
| `.work/kaggle_higgs/_fix_nb_v4_spec.py` | Sửa + verify notebook (6/6 check, 14/14 cell compile) |
| `.work/kaggle_higgs/_v4_f0.py` | Đo F0 pilot v4 (2 thuật toán) |
| `.work/kaggle_higgs/_wait_kernel_v4.py` / `_wait_kernel_v5.py` | Theo dõi kernel + tải **chỉ** wav/json |
| `.work/kaggle_higgs/_prepare_push_v4.py` | Chuẩn bị thư mục push (id phải khớp slug Kaggle) |

### Bộ tạo clip VoxCPM2 mới cho G9 (chạy trên Mac mini)

| File | Vai trò |
|---|---|
| `.work/voxcpm_generate_g9.py` | **Script chạy trên Mac mini** — dò thang `control`, đo F0, chọn take, đóng gói 24 kHz |
| `.work/voxcpm_refs_manifest_g9.json` | Mô tả giọng + thang `control` + dải F0 của 3 clip mới |
| `.work/G9_HD_HUONG_DAN.md` | **Hướng dẫn đầy đủ** "làm lại ở Vox" (bảng từ khoá → F0, cách dò thang) |
| `.work/DAT_SPEC_G9.md` | Đặc tả ngắn |

### Số đo thô

| File | Nội dung |
|---|---|
| `.work/kaggle_higgs/cer_pilot_rows.json` | 96 dòng, 2 bản chép ASR/câu (bản gốc, trước khi sửa Q3a) |
| `.work/kaggle_higgs/cer_pilot_rows_fixed.json` | CER sau khi sửa Q3a |
| `.work/kaggle_higgs/cer_minimax_pilot_rows.json` | MiniMax 32 câu (cache bản chép) |
| `.work/kaggle_higgs/f0_minimax_t02.json` | F0 MiniMax toàn tập (203 câu) |
| `.work/kaggle_higgs/_h2_fair.txt` | Bảng so sánh công bằng (kết quả chạy) |
| `.work/kaggle_higgs/_f0_crosscheck.txt` | Kết quả kiểm chéo F0 |
| `.work/kaggle_higgs/out_higgs_v3/out_higgs/higgs_manifest.json` | Manifest 96 bản |
| `.work/kaggle_higgs/higgs_payload_t02.json` | Payload 203 câu Tập 02 |

### Tài liệu

| File | Nội dung |
|---|---|
| `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` | Chuẩn (mục 11 đã cập nhật số đo 30/10) |
| `AGENTS.md` | Luật L2–L16, G1–G13, Q1–Q6 |
| `90_LUU_TRU/BaoCao_H2_Higgs_Pilot_Tap02_20261030.md` | Báo cáo bản đầu (bản cũ) |
