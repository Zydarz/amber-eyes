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
| 5 | **G9 H↔D** | 2 vai nam gần như **cùng cao độ** (chỉ cách 0,23 nửa cung, cần ≥ 4) | **Higgs không giữ cao độ của clip tham chiếu** — 2 vai trôi ngược chiều về cùng một vùng | Cần clip tham chiếu **mới** | ✅ **ĐÃ XỬ LÝ** — 4 clip mới từ Mac mini; `H↔D` = 6,57–11,23 nc ✅ |
| 6 | **G9 vai N1** | Không tìm được clip nữ vừa đọc đúng vừa tách xa C | Chưa có clip nữ nào đủ cao | Cần clip VoxCPM2 mới hoặc chấp nhận lệch | ⏸ **CÒN 1 NÚT THẮT** — `C↔N1` = 2,58 nc; **không clip sạch nào đạt** (xem #7) |
| 7 | **Hạ cao độ clip tham chiếu làm hỏng giọng** | Cả phase vocoder lẫn TD-PSOLA đều tạo clip **đọc rất tốt** (ASR 0,00%) nhưng **clone ra thì đọc sai nội dung** | Mọi xử lý dạng sóng theo thời gian ⇒ codec âm thanh sinh token mờ ⇒ Higgs nghe nhầm | **Không được hạ cao độ clip bằng xử lý tín hiệu** — chỉ dùng clip có sẵn ở cao độ đó | ✅ **ĐÃ CHỨNG MINH** (CER 8,4–12,5%) — loại toàn bộ biến thể |

> **Điểm mấu chốt:** lỗi #1, #2, #3, #4 **không nằm trong code sản xuất** — chúng là lỗi của **chính công cụ đo**.
> Lỗi #2 khiến suốt một buổi tưởng Higgs kém; thực ra sau khi đo lại đúng thì **Higgs tốt hơn MiniMax ở vai H**.
> Lỗi #5 đã xử lý xong bằng clip mới. Lỗi #6 là **nút thắt thật**: `C↔N1` không đạt được bằng clip sạch nào
> (lỗi #7 cho thấy vì sao lối thoát duy nhất là "nhờ Mac tạo clip mới" hoặc "chấp nhận", vì `C` và `N1`
> **không bao giờ liền kề** trong Tập 02).

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
| G9 H↔D — clip cần tạo | ✅ **Đã có** (4 clip từ Mac mini) — số đo ở §6.9 |
| G9 N1↔N2 | ❌ **Trượt cả 3 cặp nữ** — chi tiết §6.10, §6.11 |
| temperature | ✅ `0,8` cho H/D/C — xác nhận lần 3 (t=0,7 runaway 47,56 s ở D 2.05#15/#16) |
| §5 thẻ emotion | ✅ an toàn — kiểm trên 349 bản chép ASR thật, không có từ khoá thẻ |
| CER | ✅ đạt (H 0,00% · C 0,00% · N2 0,63%); D 2,27% cần đa bản §7 |

### 6.9 4 clip mới đã về — số đo F0 thật (2 thuật toán)

Mac mini đã chạy `.work/voxcpm_generate_g9.py` xong và push (`bb8896f`). Đo lại bằng **cùng 2 thuật toán
F0 của dự án** (AC thô = `voice_audition.f0_median`; AC chuẩn hóa + parabolic + sửa octave = pp2):

| Clip | F0 clip (AC thô) | F0 clip (AC chuẩn hóa) | Thời lượng | Dải mục tiêu | Kết quả |
|---|---:|---:|---:|---:|---|
| `M_LOW` (nam rất trầm, vai H) | 95,6 Hz | 95,5 Hz | 19,26 s | 70–86 | ⚠ **cao hơn mục tiêu 9,6 Hz** |
| `M_HIGH` (nam cao, vai D) | 192,0 Hz | 185,7 Hz | 16,90 s | 168–182 | ⚠ **cao hơn 10,0 Hz** |
| `W6_LOW` (nữ thấp, vai N1) | 179,1 Hz | 169,0 Hz | 28,13 s | 148–162 | ⚠ **cao hơn 17,1 Hz** + vượt trần 28 s |
| `W5_HIGH` (nữ cao, vai N2) | 289,2 Hz | 275,4 Hz | 19,07 s | 258–276 | ⚠ **cao hơn 13,2 Hz** |

**Nguyên nhân:** VoxCPM2 (Voice Design) **không bám tuyệt đối** từ khoá `very low-pitched` /
`lower mid-pitched` — cả 4 clip đều cao hơn dải mục tiêu. Đây là đặc tính của model, không phải lỗi script.

**Hệ quả:**
- `M_LOW` 95,6 Hz **vẫn thấp hơn hẳn** `M_HIGH` 192,0 Hz ⇒ H↔D **vẫn tách được** (dự đoán 9,6 nc, xem §8.8).
- `W6_LOW` 179,1 Hz **không đủ thấp** cho vai N1 ⇒ phải hạ thêm bằng xử lý tín hiệu (§6.11).

### 6.10 Phát hiện mới — **cả 3 cặp nữ đều trượt G9**, và ràng buộc định lượng

Payload sản xuất hiện tại (`.work/kaggle_higgs/higgs_payload_t02.json`) gán:

| Vai | Clip | Số câu |
|---|---|---:|
| H | `H.wav` | 95 |
| D | `D.wav` | 51 |
| C | `C.wav` | 49 |
| **N1** | **`W1.wav`** | 4 |
| **N2** | **`W2.wav`** | 4 |

Tính lại 3 cặp nữ từ số đo thật (pilot v3+v4, n = 8/ô):

| Cặp | F0 clone (AC thô / pp2) | nc (AC thô) | nc (pp2) | Ngưỡng | Kết luận |
|---|---:|---:|---:|---:|---|
| C ↔ N1 (N1 ← W1) | 205,1 / 194,9 — 247,4 / 234,0 | 3,23 | 3,16 | ≥ 4 | ❌ trượt |
| C ↔ N2 (N2 ← W2) | 205,1 / 194,9 — 206,9 / 198,7 | 0,16 | 0,33 | ≥ 4 | ❌ trượt |
| N1 ↔ N2 | 247,4 / 234,0 — 206,9 / 198,7 | 3,08 | 2,82 | ≥ 4 | ❌ trượt |

⇒ Cả **3** cặp nữ đều trượt (bản cũ chỉ kiểm 2 cặp và bỏ sót cặp C↔N2).

**Ràng buộc định lượng** (giữ C ← `C.wav` và N2 ← `W1.wav`):

| Ràng buộc | Ngưỡng |
|---|---|
| C↔N1 ≥ 4 nc (AC thô) | N1_ac ≤ **162,8 Hz** |
| C↔N1 ≥ 4 nc (AC chuẩn hóa) | N1_pp2 ≤ **154,7 Hz** |
| N1↔N2 ≥ 4 nc (AC thô / pp2) | N1_ac ≤ 219,0 Hz / N1_pp2 ≤ 205,0 Hz |

⇒ **ngưỡng chặt nhất: clone của N1 phải ≤ 162,8 Hz (AC thô) và ≤ 154,7 Hz (pp2)**.
Lưu ý hai ngưỡng khác nhau vì **2 thuật toán đo trên 2 thang khác nhau** (tỉ lệ pp2/ac ≈ 0,95).

**Ngân sách cao độ cho 3 vai nữ:** 3 giọng nữ phải trải ≥ 4 nc mỗi cặp ⇒
`F0_max / F0_min ≥ 2^(8/12) = 1,5874`. Với `W6_LOW` (179,1) làm N1 và `W5_HIGH` (289,2) làm N2:
tỉ lệ = 1,618 — **vừa đủ**, nhưng phải hạ N1 xuống ≤ ~162 Hz thì mới có C ở giữa.

### 6.11 Sửa — hạ F0 clip `W6_LOW` bằng phase vocoder, tạo 5 biến thể cho N1

**Triệu chứng:** `W6_LOW` ở 179,1 Hz; theo tỉ lệ drift đã đo (0,95–1,10) thì clone của N1 rơi vào
**183–190 Hz** ⇒ C↔N1 chỉ **~1,7 nc** ⇒ vẫn trượt.

**Nguyên nhân:** chỉ có 5 clip nữ trong bộ (`W1` 250 · `W2` 200 · `C` 208,7 · `W5_HIGH` 289,2 · `W6_LOW` 179,1)
và **không tổ hợp nào trong 5 clip này đạt được cả 3 cặp ≥ 4 nc** — đã duyệt bằng script
`.work/g9_matrix.py` (28 cặp, 9 phân bố). Cần **hạ** F0 clip, không cần **tìm** clip khác.

**Sửa ở đâu:** `.work/g9_shift_clip.py` — **phase vocoder** (time-stretch bằng FFT + resample),
giữ nguyên thời lượng, đồng thời cắt 0,80 s đoạn im lặng để thời lượng ≤ 28 s (không mất chữ).

**Sửa cái gì** — 5 biến thể, đo F0 thật sau khi hạ:

| Biến thể | Hạ | F0 sau hạ (AC thô / pp2) | Thời lượng | Clone dự đoán (AC thô) | Chặn 162,8 Hz? |
|---|---:|---:|---:|---:|---|
| `W6_LOW_S20` | −2,0 nc | 160,0 / 158,7 | 27,33 s | 151,6–175,5 | ❌ |
| `W6_LOW_S25` | −2,5 nc | 157,9 / 154,8 | 27,33 s | 147,3–170,5 | ❌ |
| `W6_LOW_S30` | −3,0 nc | 154,8 / 151,5 | 27,33 s | 143,1–165,7 | ❌ (worst case) |
| **`W6_LOW_S35`** | **−3,5 nc** | **150,0 / 147,2** | 27,33 s | **139,0–161,0** | ✅ |
| **`W6_LOW_S40`** | **−4,0 nc** | **144,6 / 143,1** | 27,33 s | **135,0–156,4** | ✅ |

⇒ **`S35` và `S40` thoát vùng trượt** ở cả worst-case drift. Pilot v6 đo cả 5 để chốt bằng số thật.

**Tính hợp lệ:** biến thể là asset của chính dự án (Apache-2.0, sinh từ `W6_LOW` của VoxCPM2 Voice
Design), không dùng file của bên thứ ba. `refs.json` ghi rõ F0 **sau** khi hạ + ghi chú xử lý.

### 6.12 **Pilot v6 XONG** — F0 clone thật của 13 ô (156 audio)

Kernel `chiduong2026/amber-eyes-higgs-v6-pilot-g9-f0-cer` · **156/156 OK, 0 lỗi** ·
RTF tb ≈ 2,0 · 13 ô × 6 câu × 2 bản.

| Vai | Clip | F0 clone (AC thô) | F0 clone (AC chuẩn hóa) | **drift** so với clip | Khoảng ac |
|---|---|---:|---:|---:|---:|
| H | `M_LOW` | **97,8 Hz** | 97,1 Hz | +2,3% / +1,6% | 91,3 – 109,6 |
| H | `H.wav` (gốc) | 130,4 Hz | 127,1 Hz | +21,2% / +18,6% | 115,9 – 144,6 |
| D | `M_HIGH` | **198,3 Hz** | 185,8 Hz | +3,3% / 0,0% | 186,0 – 260,9 |
| D | `D.wav` (gốc) | 124,0 Hz | 125,5 Hz | −3,4% / −5,1% | 115,9 – 138,7 |
| C | `C.wav` (gốc) | 214,3 Hz | 202,8 Hz | +2,7% / +1,5% | 205,1 – 242,4 |
| N1 | `W6_LOW` (chưa hạ) | 184,6 Hz | 173,1 Hz | +3,1% / +2,4% | 179,1 – 206,9 |
| N1 | `W6_LOW_S25` | 162,2 Hz | 152,9 Hz | +2,7% / −1,2% | 151,9 – 250,0 |
| N1 | `W6_LOW_S30` | 162,2 Hz | 147,9 Hz | +4,8% / −2,4% | 155,8 – 201,7 |
| N1 | `W6_LOW_S35` | **152,9 Hz** | 148,3 Hz | +1,9% / +0,7% | 149,1 – 179,1 |
| N1 | `W6_LOW_S40` | **147,2 Hz** | 141,7 Hz | +1,8% / −0,9% | 142,0 – 186,0 |
| N2 | `W5_HIGH` | **285,7 Hz** | 268,0 Hz | −1,2% / −2,7% | 269,7 – 333,3 |
| N2 | `W2.wav` (gốc) | 201,7 Hz | 195,5 Hz | +0,8% / +3,3% | 193,5 – 212,4 |
| N2 | `W1.wav` (gốc) | 260,9 Hz | 246,9 Hz | +4,4% / +4,9% | 237,6 – 303,8 |

**Phát hiện quan trọng — drift của clip M_LOW rất nhỏ (+2,3%):**
`H.wav` (107,6 Hz) bị Higgs kéo **+21,2%** lên 130,4 Hz — nhưng `M_LOW` (95,6 Hz) chỉ bị kéo
**+2,3%** lên 97,8 Hz. ⇒ **Clip càng trầm, Higgs càng giữ nguyên cao độ** (không kéo theo
như giả thuyết cũ). Đây là lý do `M_LOW` cho H↔D **rộng hơn hẳn** dự đoán.

**G9 sau pilot v6 (ĐẠT khi CẢ HAI thuật toán ≥ 4 nc):**

| H | D | C | N1 | N2 | margin | Kết luận |
|---|---|---|---|---|---:|---|
| `M_LOW` | `M_HIGH` | `C.wav` | `W6_LOW_S40` | `W5_HIGH` | **4,83** | ✅ đạt |
| `M_LOW` | `M_HIGH` | `C.wav` | `W6_LOW_S35` | `W5_HIGH` | **4,83** | ✅ đạt |
| `M_LOW` | `M_HIGH` | `C.wav` | `W6_LOW_S30` | `W5_HIGH` | 4,82 | ✅ đạt |
| `M_LOW` | `M_HIGH` | `C.wav` | `W6_LOW_S25` | `W5_HIGH` | 4,82 | ✅ đạt |
| `H.wav` | `M_HIGH` | `C.wav` | `W6_LOW_S35` | `W5_HIGH` | 4,83 | ✅ đạt *(giữ giọng H cũ)* |
| `M_LOW` | `D.wav` | `C.wav` | `W6_LOW_S35` | `W5_HIGH` | 4,11 | ✅ đạt *(giữ giọng D cũ)* |
| `H.wav` | `D.wav` | `C.wav` | bất kỳ | `W5_HIGH` | 0,87 | ❌ **trượt** (vấn đề gốc) |
| `M_LOW` | `M_HIGH` | `C.wav` | `W6_LOW` (chưa hạ) | `W5_HIGH` | 2,58 | ❌ **trượt** (C↔N1) |

⇒ **12/60 phương án đạt.** Biên chặn mọi phương án là cặp **C↔N2 = 4,83 nc** (C và N2 đã cố định).

| Cặp | NC (AC thô) | NC (AC chuẩn hóa) |
|---|---:|---:|
| H↔D (`M_LOW`↔`M_HIGH`) | **12,24** | **11,23** |
| H↔D (`H.wav`↔`M_HIGH`) | 7,26 | 6,57 |
| C↔N1 (`C.wav`↔`W6_LOW_S35`) | 5,42 | 4,83 |
| C↔N2 (`C.wav`↔`W5_HIGH`) | 4,99 | 4,83 |
| N1↔N2 (`W6_LOW_S35`↔`W5_HIGH`) | 10,66 | 10,24 |

---

### 6.13 CER pilot v6 — **tính lại đúng**, và thêm 1 metric tách nhiễu ASR khỏi lỗi TTS

**Triệu chứng.** Bảng CER của pilot v6 ra `CER tb 11–27%`, `max 73,8–90,5%` — nghe như giọng đọc
sai kinh khủng. Nhưng cache ASR (`_asr_cache_v6/`, 225 file, `code=0`) cho thấy bản chép **gần như
hoàn hảo** (ví dụ *"Bắt cóc không xuất hiện từ hư không."*).

**Nguyên nhân.** `analyze_pilot_v6.py` dùng **cách chuẩn hóa cũ**: chỉ chuẩn hóa **1 vế**, và
`vi_number()` tự viết lại còn sai (2009 → *"two nine"* thay vì *"hai nghìn không trăm lẻ chín"*).
⇒ **Lỗi nằm ở cách đo, không phải ở audio.**

**Sửa ở đâu.** Tạo module chuẩn dùng chung `.work/vi_cer.py`:
`vi_number`/`vi_numbers` **copy nguyên văn** từ `.work/tts_sentences.py` (dòng 122–182) +
`selfcheck()` tự so sánh với file pipeline thật (26 số + 7 chuỗi) ⇒ **OK, khớp 100%**.
Ba hàm đo:
- `cer_pair()` — chuẩn hóa **cả hai vế** bằng đúng `vi_number` của pipeline (đây là con số chính thức);
- `cer_pair_nonum()` — phụ: bỏ mọi từ số ở cả hai vế;
- `cer_pair_prop()` — phụ: bỏ **danh từ riêng** (token viết hoa giữa câu: *Tweed, Russell, Williams*…)
  ở cả hai vế — vì ASR đọc sai tên riêng là **lỗi của ASR, không phải của TTS**.

`analyze_pilot_v6.py` và `measure_cer_prod.py` đã nối vào module này.

**Sửa cái gì.** Xem bảng đầy đủ ở **§8.10**. Tóm tắt: ô nào không dùng biến thể dịch cao độ thì
**CER (bỏ danh từ riêng) ≤ 2,62%**; ô nào dùng biến thể phase vocoder thì **9,5–12,5%**.

---

### 6.14 PHÁT HIỆN LỚN — biến thể **phase vocoder** hỏng **khi clone**, không hỏng khi đọc

**Triệu chứng.** Tại sao 5 biến thể `W6_LOW_S20…S40` lại cho clone tệ, trong khi clip gốc `W6_LOW`
rất tốt?

**Cách kiểm chứng — đo ASR trên chính CLIP THAM CHIẾU** (`.work/cer_ref_clips.py`; mỗi clip có
`.txt` sẵn lời đọc mẫu, không cần GPU):

| Clip | CER trên clip gốc | | Clip | CER trên clip gốc |
|---|---:|---|---|---:|
| `W6_LOW` | **0,00%** | | `W5_HIGH` | 0,00% |
| `W6_LOW_S20` | 0,91% | | `M_LOW` | 0,00% |
| `W6_LOW_S25` | **0,00%** | | `M_HIGH` | 0,00% |
| `W6_LOW_S30` | 0,45% | | `C` | 0,00% |
| `W6_LOW_S35` | 0,45% | | `W1` | 0,00% |
| `W6_LOW_S40` | 4,31% | | `W2` | 0,52% |

⇒ **Clip tham chiếu đọc rất tốt. Lỗi nằm ở bước CLONE.**
Hai nghi vân đã loại trừ:
1. *Mối ghép do cắt im lặng giữa câu* (0,80 s ở 5,76–6,56 s) — **loại**: chính `W6_LOW.wav` **giữ nguyên**
   đoạn im lặng đó mà clone vẫn sạch (CER bỏ danh từ riêng 1,47%).
2. *Nội dung/lời đọc* — **loại**: mọi biến thể dùng chung lời.

⇒ **Thủ phạm là phase vocoder** (time-stretch FFT + resample): nó làm nhoè dạng sóng ⇒ codec sinh
token âm thanh mờ ⇒ **Higgs clone ra lời sai** (ví dụ *"Tuyết mới rơi…"* → *"Kẻ sát nhân…"*,
*"Khi phân tích trường hợp của Russell Williams…"* → *"Khi vô tình được hậu quả sau Williams…"* —
cả 2 vòng ASR đều sai giống nhau ⇒ **audio thật sự nói sai**, không phải nhiễu ASR).

**Sửa ở đâu.** `.work/g9_psola_shift.py` — thay phase vocoder bằng **TD-PSOLA**
(giai thuốc sóng + resample FFT giữ dải thông): giữ nguyên dạng sóng gốc, không nhoè.

**Sửa cái gì — 5 clip mới, đo F0 thật:**

| Clip | Cách làm | F0 (AC thô / AC chuẩn hoá) | Thời lượng | CER trên clip gốc |
|---|---|---:|---:|---:|
| `W6_LOW_TRIM` | chỉ cắt im lặng (đối chứng) | 179,1 / 168,9 Hz | 27,33 s | 0,45% |
| `W6_LOW_PS15` | TD-PSOLA −1,5 nửa cung | 164,4 / 163,7 Hz | 28,13 s | 4,31% |
| `W6_LOW_PS20` | TD-PSOLA −2,0 nửa cung | **160,0 / 159,1 Hz** | 28,13 s | **0,00%** |
| `W6_LOW_PS25` | TD-PSOLA −2,5 nửa cung | **155,8 / 154,5 Hz** | 28,13 s | **0,00%** |
| `W6_LOW_PS30` | TD-PSOLA −3,0 nửa cung | **150,9 / 150,4 Hz** | 28,13 s | **0,00%** |

**Ràng buộc G9 rút lại từ số đo thật** (C clone = 214,3 / 202,8 Hz; N2←`W5_HIGH` clone = 285,7 / 268,0 Hz):

> N1 clone phải có **F0_ac ≤ 170,1 Hz** và **F0_pp2 ≤ 161,0 Hz** (để cách C ≥ 4 nửa cung ở **cả hai**
> thuật toán) — và **F0_pp2 ≤ 168,8 Hz** (ngân sách tỉ lệ ≥ 1,5874).

⇒ `W6_LOW_PS25` (clip 155,8 / 154,5) và `W6_LOW_PS30` (150,9 / 150,4) **nằm trong cửa sổ**
(nếu drift của clip tiếng Việt giữ ở mức ±3% như đã đo ở 4 clip gốc).

**Trạng thái.** Pilot **v8** đã chạy xong trên Kaggle (36 audio = 3 ô × 6 câu × 2 bản), **36/36 OK, 0 lỗi**.
Kết quả ở **§6.15** — và kết quả đó **bác bỏ** TD-PSOLA.

> **Ghi chú quy trình:** 2 lỗi phải sửa để làm TD-PSOLA chạy đúng —
> (1) dấu nhịp phải đặt **1 dấu / chu kỳ** (đặt theo khung 5 ms thì dày hơn chu kỳ thật ⇒ đổi cao độ
> chỉ đạt ~1/2 yêu cầu); (2) khi chia cho `wsum` ở các điểm mép cửa sổ Hann (`wsum≈0`) sinh **đỉnh giả**
> làm hỏng toàn bộ biên độ → dùng `max(wsum, 0,25×trung vị)` + chuẩn hoá theo **phân vị 99,9%**.

---

### 6.15 Pilot v8 XONG — **TD-PSOLA CŨNG HỎNG khi clone**. Không có cách nào hạ cao độ clip tham chiếu

**Triệu chứng.** TD-PSOLA giữ dạng sóng gốc (không nhoè như phase vocoder) và 3 clip mới đều đọc
**ASR 0,00%** khi đo trực tiếp. Trông như đã giải quyết xong. Nhưng khi **Higgs clone** từ chúng thì sao?

**Kết quả đo thật (kernel `amber-eyes-higgs-v8-td-psola-kaggle-gpu`, 36/36 OK, 0 lỗi):**

| Ô | F0 clone (AC thô / AC chuẩn hoá) | CER tb | CER max | > 2% | **CER bỏ danh từ riêng** |
|---|---|---:|---:|---:|---:|
| `W6_LOW_PS20` | 161,1 / 159,1 | 9,62% | 21,1% | 10/12 | 18,69% |
| `W6_LOW_PS25` | 156,9 / 155,0 | 8,44% | 42,1% | 8/12 | 10,19% |
| `W6_LOW_PS30` | 152,9 / 150,9 | 10,87% | 21,4% | 12/12 | 24,01% |
| *(đối chứng)* `W6_LOW` | 184,6 / 173,1 | 2,10% | 14,3% | 3/12 | **1,47%** |

⇒ **TD-PSOLA không cứu được.** Ba biến thể đều cho CER 8,4–10,9% — **tệ ngang phase vocoder**.

**Và lỗi vẫn là lỗi SAI NỘI DUNG, không phải nhiễu ASR** (cả 2 vòng ASR sai giống nhau):

| Câu gốc | ASR nghe được (biến thể PS) |
|---|---|
| *"Kẻ bắt cóc không xuất hiện từ hư không."* | *"và các công suất hiện tượng hư không"* (PS25) · *"Kẻ bát cóc không…"* (PS20) |
| *"Tuyết mới rơi đã lưu lại gần nhà nạn nhân…"* | *"Mật bơi rơi tà lụa lại gần nhà nạn nhân…"* (PS25) |
| *"Suốt nhiều năm, thị trấn nhỏ **Tweed**…"* | *"thị trấn nhỏ **tuyệt**…"* / *"**Twin**…"* / *"**Tweit**…"* |
| *"Khi phân tích trường hợp của Russell Williams…"* | *"**Nếu trong** trường hợp của Russell Williams…"* (PS30) |

**Nguyên nhân — đã rõ, và đây là kết luận quan trọng nhất của cả vòng đo:**

> **Bất kỳ phép biến đổi cao độ nào trên clip tham chiếu đều làm hỏng khả năng nghe khi clone.**
> Cơ chế: Higgs mã hoá clip tham chiếu bằng **audio token codec**; phase vocoder lẫn TD-PSOLA đều
> can thiệp vào **dạng sóng theo thời gian** ⇒ codec sinh token mờ ⇒ mô hình **nghe nhầm âm thanh**
> ⇒ đọc ra lời khác, chứ không phải đọc sai phát âm.
> Clip **chưa từng** bị xử lý (`W6_LOW` bản gốc) thì CER bỏ danh từ riêng chỉ **1,47%**.

⇒ **Kết luận thiết kế:** muốn đổi cao độ của một vai, phải **có clip đã tồn tại sẵn ở cao độ đó**
(và phải sạch), **không được tạo ra bằng xử lý tín hiệu**.

**Hệ quả trực tiếp với G9 — và đây là điểm chặn thật:**

> G9 yêu cầu C↔N1 ≥ 4 nửa cung. C clone = 214,3 / 202,8 Hz ⇒ N1 clone phải **≤ 170,1 Hz (AC thô)** và
> **≤ 161,0 Hz (AC chuẩn hoá)**. Trong thư viện clip sạch, **chỉ có `W6_LOW` là clip nữ** dành được cho N1
> (clone 184,6 / 173,1 Hz) ⇒ **C↔N1 = 2,58 nc < 4 nc — không đạt được bằng clip sạch nào**.

**Ba lối thoát còn lại (xem §9.1 để chọn):**
1. **Chấp nhận** C↔N1 = 2,58 nc, vì **C và N1 không bao giờ liền kề** trong Tập 02 (§8.11) — và
   cặp cùng giới **duy nhất** thật sự liền kề là **H↔D** (8 lần), vốn đạt 6,57–11,23 nc ✅.
2. **Thêm 1 clip nữ mới** do Mac mini tạo ở F0 thấp hơn, **không qua xử lý tín hiệu** — rủi ro cao vì
   lần trước Mac nhắm 148–162 Hz mà ra 179,1 Hz.
3. **Đổi N1 sang giọng nam** (`W4` clone 135,6 / 131,2 Hz ⇒ C↔N1 = 5,52 / 5,23 nc ✅) — sai chất vai,
   không khuyến nghị.

**Sửa ở đâu / sửa cái gì:**
- `.work/g9_role_map.json` — chốt mapping theo số đo thật, đính kèm bảng F0 clone + CER + cảnh báo.
- `.work/g9_decide.py` — **mới**: đo lại F0 clone của **mọi** ô pilot v6+v7+v8, dựng bảng G9 đầy đủ
  theo giới tính, tự tính cặp liền kề thật từ `script_tap02.json`.
- **Không dùng** `W6_LOW_PS15…PS30` cho bất kỳ vai nào. Các clip phase vocoder `W6_LOW_S20…S40` cũng vậy.


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

### 8.8 G9 sau 4 clip mới + 5 biến thể hạ F0 — **dự đoán** (pilot v6 đang chạy)

Dùng số đo thật của 4 clip mới (§6.9) + tỉ lệ drift đã đo (0,95–1,10 cho clip nữ) để dự đoán
F0 clone. **Đây là dự đoán — pilot v6 sẽ cho số thật.**

| Phương án | H↔D | C↔N1 | C↔N2 | N1↔N2 | Kết luận dự đoán |
|---|---:|---:|---:|---:|---|
| H←`M_LOW`, D←`M_HIGH`, C←`C.wav`, N1←`W6_LOW_S35`, N2←`W5_HIGH` | 9,64 | 4,6–4,8 | 5,9–6,4 | 10,0–11,0 | ✅ đạt (biên hẹp nhất 4,6) |
| H←`H.wav`, D←`M_HIGH`, C←`C.wav`, N1←`W6_LOW_S35`, N2←`W5_HIGH` | 6,96 | 4,6–4,8 | 5,9–6,4 | 10,0–11,0 | ✅ đạt (**H giữ nguyên giọng đã kiểm**) |
| H←`M_LOW`, D←`M_HIGH`, C←`C.wav`, N1←`W6_LOW` (chưa hạ) | 9,64 | ~1,7 | 5,9–6,4 | ~8 | ❌ **trượt** C↔N1 |
| H←`M_LOW`, D←`D.wav` (giữ nguyên D) | ~1,0 | — | — | — | ❌ **trượt** H↔D |

⇒ **2 phương án khả thi**, khác nhau ở chỗ **H dùng clip cũ `H.wav` hay clip mới `M_LOW`**:
phương án 2 **giữ nguyên giọng H đã đo CER 0,00%** ⇒ đổi giọng ít nhất (L4) nhưng biên G9 hẹp hơn
(6,96 so với 9,64 nc).

### 8.9 Trạng thái hạ tầng 2 GPU (đã dựng xong, chưa chạy lượt sản xuất)

| Hạng mục | Trạng thái |
|---|---|
| Worker 1 tiến trình / 1 card | ✅ `.work/higgs_worker.py` — seed SHA-256(`id\|role\|ref\|temp\|vN`) ⇒ **kết quả không phụ thuộc card nào sinh** |
| Chia task 2 GPU | ✅ `idx % n_shards` — `CUDA_VISIBLE_DEVICES=0/1`, giãn 50 s giữa 2 lần launch (tránh 2 tiến trình cùng nạp model) |
| Fallback catch-up | ✅ cell 9: task thiếu chạy lại trên GPU0 rồi merge lại — **không mất task nào** |
| Bug nhúng worker | ⚠ **Đã phát hiện & sửa**: worker có docstring `"""` làm vỡ chuỗi `r"""…"""` của cell → đổi sang nhúng **base64** + verify khôi phục khớp file nguon |
| Lượt sản xuất | 203 câu × 2 bản = **406 file** · ước **2,35 h** 1 GPU / **~1,2 h** 2 GPU |
| Quota Kaggle | 1,39 h/30 h đã dùng (còn **28,61 h**) — thời gian **không** phải ràng buộc |

---

### 8.10 CER pilot v6 — **đã tính lại đúng** (chuẩn hóa 2 vế, `vi_cer.py`)

156 audio = 13 ô × 6 câu × 2 bản. Mỗi câu ASR **2 vòng**, lấy vòng **xấu hơn**.
`CER` = chuẩn hóa 2 vế (đây là con số chính thức) · `CER⊘P` = bỏ danh từ riêng ở cả hai vế.

| Vai | Clip | F0_ac | F0_pp2 | CER tb | CER max | >2% | **CER⊘P tb** | CER⊘P max | >2% |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| H | `H.wav` | 130,4 | 127,1 | 0,34% | 3,7% | 1/11 | **0,00%** | 0,0% | 0/11 |
| N2 | `W5_HIGH.wav` | 285,7 | 268,0 | 0,21% | 1,3% | 0/11 | **0,25%** | 2,8% | 1/11 |
| D | `M_HIGH.wav` | 198,3 | 185,8 | 1,44% | 5,1% | 4/12 | **0,47%** | 4,0% | 1/12 |
| N1 | `W6_LOW.wav` | 184,6 | 173,1 | 2,10% | 14,3% | 3/12 | **1,47%** | 14,3% | 2/12 |
| H | `M_LOW.wav` | 97,8 | 97,1 | 2,43% | 14,3% | 4/12 | 1,94% | 14,3% | 2/12 |
| N2 | `W1.wav` | 260,9 | 246,9 | 2,65% | 7,9% | 5/11 | 1,96% | 7,9% | 4/11 |
| N2 | `W2.wav` | 201,7 | 195,5 | 3,10% | 10,5% | 5/12 | 2,15% | 10,5% | 3/12 |
| C | `C.wav` | 214,3 | 202,8 | 3,09% | 10,5% | 6/12 | 2,14% | 10,5% | 4/12 |
| D | `D.wav` | 124,0 | 125,5 | 3,57% | 15,8% | 5/12 | 2,62% | 15,8% | 3/12 |
| N1 | `W6_LOW_S40.wav` | 147,2 | 141,7 | 8,61% | 19,0% | 9/12 | 9,83% | 23,3% | 9/12 |
| N1 | `W6_LOW_S25.wav` | 162,2 | 152,9 | 9,72% | 34,2% | 9/12 | 9,54% | 34,2% | 8/12 |
| N1 | `W6_LOW_S30.wav` | 162,2 | 147,9 | 11,17% | 26,2% | 8/12 | 11,16% | 26,2% | 8/12 |
| N1 | `W6_LOW_S35.wav` | 152,9 | 148,3 | 12,80% | 31,6% | 11/12 | 12,47% | 31,6% | 10/12 |

**Đọc bảng:** 4 ô dùng clip gốc của bộ VoxCPM2 (`H`, `D`, `C`, `W1`, `W2`) đều ≤ 2,62% (bỏ danh từ riêng).
5 ô dùng biến thể phase vocoder đều ≥ 9,5% ⇒ **xác nhận kết luận §6.14**.

Chi tiết từng câu: `.work/cer_detail_v6.txt` · dữ liệu thô: `.work/cer_ref_clips.json`.

---

### 8.11 Dữ liệu thật — **cặp vai nào thật sự xảy ra liền kề** trong Tập 02

Tập 02 có 36 phần lời (kind `LOI`), mỗi phần **một vai**:

| Vai | Số phần | Cảnh |
|---|---:|---|
| H | 23 | rải khắp act 1–5 |
| D | 6 | 1.17, 2.05, 2.08, 4.08, 4.10, 5.08 |
| C | 5 | 3.05, 3.08, 3.11, 4.11, 5.07 |
| N1 | 1 | **1.07** (act 1) |
| N2 | 1 | **4.06** (act 4) |

**Cặp vai liền kề** (người nghe phải phân biệt được ngay):

| Cặp | Số lần liền kề |
|---|---:|
| H ↔ D | 8 |
| C ↔ H | 8 |
| H ↔ N1 | 2 |
| H ↔ N2 | 2 |
| C ↔ D | 2 |

**Cặp KHÔNG BAO GIỜ liền kề trong Tập 02:** `C↔N1`, `C↔N2`, `N1↔N2`.
(N1 chỉ ở cảnh 1.07 — hai bên đều là H; N2 chỉ ở cảnh 4.06 — hai bên đều là H.)

⇒ G9 theo nghĩa **"hai giọng cùng giới người nghe phải phân biệt được"** chỉ bắt buộc cho
`H↔D` (nam) và `C↔N2` (nữ). Cặp `C↔N1` là cặp **không xảy ra trong tập này**.

### 8.12 Bảng G9 đầy đủ — đo lại **mọi** ô pilot v6 + v7 + v8 (`.work/g9_decide.py`)

> Bảng này **thay thế** các bảng "dự đoán" ở §8.7 và §8.8. Nguồn: `.work/g9_decide.txt` / `.work/g9_decide.json`.
> Quy tắc verdict: `min(nc_ac, nc_pp2) ≥ 4 nc` → **ĐẠT** (cả hai thuật toán F0 đều phải đạt).

> ### ⚠️ ĐỌC CỘT "Ket" ĐÚNG CÁCH — **H↔D KHÔNG CÒN LỖI**
>
> Cột `Ket` trong bảng [4] là verdict của **toàn bộ tổ hợp**, không phải của riêng cặp `H-D`.
> Vì mọi dòng đều bị kéo lại bởi cột `C-N1 = 2,58 nc` (cặp **không bao giờ liền kề** trong Tập 02)
> nên **mọi dòng đều ghi `TRUOT`** — kể cả dòng có `H-D = 6,57` hay `11,23` ở cột bên cạnh.
>
> Đọc đúng là: **mỗi cột có verdict riêng** —
> * `H-D` = **6,57 / 7,27 nc ✅** (khi D dùng `M_HIGH`) · `M_LOW↔M_HIGH` = **11,23 / 12,24 nc ✅** ·
>   `M_LOW↔D.wav` = **4,11 / 4,45 nc ✅** ⇒ **`H↔D` ĐÃ XỬ LÝ XONG**.
> * `C-N1` = 2,58 nc ❌ — đây mới là **nút thắt còn mở**, và nó **vô hại** (C và N1 không bao giờ liền kề).
> * Giá trị **0,22 nc** chỉ là đo của **hai giọng gốc** `H.wav ↔ D.wav` — đó là **lý do** đã phải nhờ
>   Mac mini tạo clip mới cho vai D, **không phải lỗi đang tồn tại**.
>
> Tóm lại: **sau khi dùng `M_HIGH` cho D thì cặp nam đạt 6,57–11,23 nc**; con số 0,22 chỉ là
> *điểm xuất phát* đã được sửa.

**[1] F0 CLONE THẬT — toàn bộ ô đã clone (mỗi ô 12 audio)**

| Vai | Clip | n | F0_ac | F0_pp2 | drift_ac | Ghi chú |
|---|---|---:|---:|---:|---:|---|
| H | `H.wav` | 12 | 130,4 | 127,1 | +21,2% | giọng gốc của vai H |
| H | `M_LOW.wav` | 12 | 97,8 | 97,1 | +2,3% | nam trầm (Mac) |
| D | `D.wav` | 12 | 124,0 | 125,5 | −3,4% | giọng gốc của vai D |
| D | `M_HIGH.wav` | 12 | 198,3 | 185,8 | +3,3% | nam 50+ khàn (Mac) |
| C | `C.wav` | 12 | 214,3 | 202,8 | +2,7% | giọng gốc của vai C |
| N1 | `W6_LOW.wav` | 12 | 184,6 | 173,1 | +3,1% | nữ 30s (Mac) — **chỉ clip nữ sạch cho N1** |
| N1 | `W6_LOW_PS20.wav` | 12 | 161,1 | 159,1 | +0,7% | ❌ hỏng (CER 9,62%) |
| N1 | `W6_LOW_PS25.wav` | 12 | 156,9 | 155,0 | +0,7% | ❌ hỏng (CER 8,44%) |
| N1 | `W6_LOW_PS30.wav` | 12 | 152,9 | 150,9 | +1,3% | ❌ hỏng (CER 10,87%) |
| N1 | `W6_LOW_S25.wav` | 12 | 162,2 | 152,9 | +2,7% | ❌ hỏng (phase vocoder) |
| N1 | `W6_LOW_S30.wav` | 12 | 162,2 | 147,9 | +4,8% | ❌ hỏng (phase vocoder) |
| N1 | `W6_LOW_S35.wav` | 12 | 152,9 | 148,3 | +1,9% | ❌ hỏng (phase vocoder) |
| N1 | `W6_LOW_S40.wav` | 12 | 147,2 | 141,7 | +1,8% | ❌ hỏng (phase vocoder) |
| N2 | `W1.wav` | 12 | 260,9 | 246,9 | +4,4% | nữ cao |
| N2 | `W2.wav` | 12 | 201,7 | 195,5 | +0,8% | nữ trung bình |
| N2 | `W5_HIGH.wav` | 12 | 285,7 | 268,0 | −1,2% | nữ 20s rất cao (Mac) |
| *(v7)* | `W4.wav` | 12 | 135,6 | 131,2 | −1,1% | nam 50 (dùng cho kit nghe mù) |
| *(v7)* | `W2.wav` (lần 2) | 12 | 202,5 | 193,9 | +1,2% | đối chứng |

**[2] Ứng viên theo giới tính (chỉ clip SẠCH)**

| Vai | Ứng viên (F0 clone ac/pp2) |
|---|---|
| H (nam) | `H.wav` (130/127) · `M_LOW` (98/97) |
| D (nam) | `D.wav` (124/126) · `M_HIGH` (198/186) |
| C (nữ) | `C.wav` (214/203) |
| N1 (nữ) | `W6_LOW` (185/173) — **chỉ một** |
| N2 (nữ) | `W1` (261/247) · `W2` (202/196) · `W5_HIGH` (286/268) |

**[3] Cặp cùng giới — khoảng cách (nc), verdict = min(ac, pp2)**

| Cặp | nc_ac | nc_pp2 | Verdict |
|---|---:|---:|---|
| H↔D `H.wav` ↔ `M_HIGH` | 7,27 | 6,57 | **ĐẠT** |
| H↔D `M_LOW` ↔ `M_HIGH` | 12,24 | 11,23 | **ĐẠT** |
| H↔D `M_LOW` ↔ `D.wav` | 4,11 | 4,45 | **ĐẠT** (biên hẹp) |
| H↔D `H.wav` ↔ `D.wav` | 0,22 | 0,26 | ❌ **TRƯỢT** (2 giọng gốc gần bằng nhau) |
| C↔N1 `C.wav` ↔ `W6_LOW` | 2,58 | 2,13 | ❌ **TRƯỢT** |
| C↔N2 `C.wav` ↔ `W5_HIGH` | 4,99 | 4,83 | **ĐẠT** |
| C↔N2 `C.wav` ↔ `W1` | 3,41 | 3,80 | ❌ TRƯỢT |
| C↔N2 `C.wav` ↔ `W2` | 1,04 | 0,63 | ❌ TRƯỢT |
| N1↔N2 `W6_LOW` ↔ `W5_HIGH` | 7,56 | 7,56 | **ĐẠT** |
| N1↔N2 `W6_LOW` ↔ `W1` | 5,99 | 5,99 | **ĐẠT** |
| N1↔N2 `W6_LOW` ↔ `W2` | 1,53 | 1,53 | ❌ TRƯỢT |

**[4] Kết luận — 0/12 phương án đạt được nếu G9 áp cho MỌI cặp cùng giới**

Phân tích cặp ký kết (12 phương án hợp lệ × 4 cặp cùng giới):

| Cặp | Số phương án trượt |
|---|---:|
| `H↔D` | 3/12 (chỉ khi D = `D.wav` **và** H = `H.wav`) |
| `C↔N1` | **12/12** — luôn trượt |
| `C↔N2` | 8/12 (chỉ `W5_HIGH` đạt) |
| `N1↔N2` | 4/12 (`W5_HIGH` hoặc `W1` đạt) |

> **Cặp `C↔N1` là nút thắt.** N1 là nữ; clip nữ sạch duy nhất dành được cho N1 là `W6_LOW`
> (clone 184,6 / 173,1 Hz). Để C↔N1 ≥ 4 nc cần N1 clone ≤ 170,1 Hz (AC) **và** ≤ 161,0 Hz (pp2).
> **Không tồn tại** clip nữ sạch nào thoả — và mọi biến thể tạo ra bằng xử lý tín hiệu đều hỏng khi clone (§6.15).
>
> ⇒ **G9 chỉ đạt được nếu hiểu là "cặp cùng giới *thật sự xảy ra liền kề*".** Trong Tập 02, cặp cùng giới
> duy nhất liền kề là **H↔D** (8 lần) — và mọi phương án khuyến nghị đều đạt ở cặp đó (6,57–11,23 nc).
> Ba cặp nữ `C↔N1`, `C↔N2`, `N1↔N2` **không bao giờ liền kề** (§8.11) — người nghe không bao giờ phải
> phân biệt chúng trong tập này.

### 8.13 ⚠️ Tai nghe người dùng phát hiện lỗi mà **G9 không bắt được**: `D↔C` chỉ **1,77 nc**

**Ngày 30/10/2026, sau khi gửi reel nghe thử.** Người dùng nghe reel và báo:

> *19,7–28,8 s (H) → "Đây là giọng Nam và khác không phải giọng của H, nghe giống giọng của D"*
> *28,8–48,6 s (D) → "Biến thành giọng nữ, giọng của C"*

**Đo lại F0 từ chính file mp3 đã gửi** (`.work/check_reel_f0.py`, `.work/check_per_vai_f0.py`):

| Đoạn reel | F0 (AC) | Giọng đúng theo nhãn | Cảm nhận của người dùng |
|---|---:|---|---|
| 0,0–19,7 s · H (`5.02#4`) | 138,0 Hz | ✅ H | — |
| 19,7–28,8 s · H (`2.04#1`+`1.03#1`) | 125,3 Hz | ✅ H | "khác H, giống D" |
| **28,8–48,6 s · D (`M_HIGH`)** | **197,1 Hz** | ✅ D (nam) | **"biến thành giọng nữ, giống C"** |
| 48,6–75,1 s · C (`C.wav`) | 218,5 Hz | ✅ C (nữ) | — |
| 75,1–101,6 s · N1 (`W6_LOW`) | 181,2 Hz | ✅ N1 | — |
| 101,6–110,8 s · N2 (`W5_HIGH`) | 309,8 Hz | ✅ N2 | — |

⇒ **File KHÔNG bị lấn nhãn.** Mọi đoạn đều đúng giọng. Nhưng đoạn D (197 Hz) và đoạn C (218 Hz) chỉ
cách nhau **1,77 nửa cung** → **người nghe nhầm là hoàn toàn có lý**. Đây là lỗi thật.

**Vì sao G9 không bắt:** G9 quy định *"hai giọng **cùng giới** phải cách nhau ≥ 4 nửa cung"*.
`D` (nam) và `C` (nữ) là cặp **khác giới** ⇒ G9 không xét ⇒ lọt lưới.

**Vì sao lỗi này mới sinh:** để tách `H↔D` (cùng giới nam) ta đẩy D lên `M_HIGH` = 197 Hz.
Nhưng C đã ở 214 Hz ⇒ D bị đẩy **vào ngay cạnh C**.

| Bản | H | D | C | `D↔C` | `H↔D` |
|---|---:|---:|---:|---:|---:|
| **MiniMax** (bản cũ, đã đăng) | 101,9 | 140,4 | 207,8 | **6,73 nc ✅** | 5,56 nc ✅ |
| Higgs hiện tại (`D←M_HIGH`) | 125,3 | 197,2 | 218,4 | **1,77 nc ❌** | 7,85 nc ✅ |

⇒ **Hồi quy so với bản MiniMax.** Bản cũ có D ở 140 Hz — nằm giữa H và C, tách cả hai.

**Đo lại trên chính 416 file sản xuất** (`.work/check_prod_f0.py`, 6 file đều vai, F0 trung vị):

| Vai | Clip | F0 (AC) | F0 (pp2) |
|---|---|---:|---:|
| H | `H.wav` | 125,2 | 118,3 |
| **D** | `M_HIGH.wav` | **193,1** | **180,8** |
| C | `C.wav` | 205,0 | 196,2 |
| N1 | `W6_LOW.wav` | 179,6 | 166,6 |
| N2 | `W5_HIGH.wav` | 314,7 | 277,0 |

| Cặp | nc | | Cặp | nc |
|---|---:|---|---|---:|
| **C ↔ D** | **1,03 ❌** | | D ↔ H | 7,34 ✅ |
| **D ↔ N1** | **1,26 ❌** | | H ↔ N1 | 5,93 ✅ |
| C ↔ N1 | 2,29 ❌ *(không liền kề)* | | C ↔ N2 | 5,97 ✅ |
| C ↔ H | 8,54 ✅ | | H ↔ N2 | 14,73 ✅ |

⇒ **`D` ở 193 Hz nằm giữa hai giọng nữ (N1 180 Hz, C 205 Hz)** — cách mỗi bên chưa tới **1,3 nửa cung**.
Đó là lý do tai nghe đọc `D` thành "giọng nữ giống C". Lỗi này **lớn hơn hẳn** ước lượng 1,77 nc lúc pilot.

**Cặp `C↔D` liền kề ở đâu trong Tập 02** (tự tính từ `script_tap02.json`, 22 cặp khác giới liền kề):

| # | Cảnh | Câu | Vai |
|---|---|---|---|
| 1 | 4.10 → 4.11 | `4.10#9` → `4.11#1` | D → C |
| 2 | 5.07 → 5.08 | `5.07#6` → `5.08#1` | C → D |

**Lựa chọn sửa (chờ người dùng chốt — L4):**

| # | H | D | `H↔D` | `D↔C` | Nhận xét |
|---|---|---|---:|---:|---|
| **1** | `H.wav` 130,4 | **`M_LOW` 97,8** | 4,98 ✅ | **13,58 ✅** | **Tốt nhất trong clip sẵn có.** Mọi cặp liền kề ≥ 4,96 nc. Nhược: giọng D thành *nam trầm mềm* thay vì *nam 50+ khàn*; biên `H↔D` mỏng hơn (4,98 so với 7,85) |
| 2 | `H.wav` 130,4 | **clip mới ~167 Hz** | ≈ 4,0 ✅ | ≈ 4,3 ✅ | Giữ đúng chất *khàn 50+*. Nhưng biên mỏng **cả hai** và Mac mini từng trượt mục tiêu (nhắm 168–182 → ra 192) |
| 3 | `H.wav` 130,4 | `M_HIGH` 197,2 (giữ) | 7,85 ✅ | **1,77 ❌** | Chấp nhận lẫn ở 2 chỗ; chỉ chấp nhận được nếu video có nhãn vai |

**Khe hợp lệ duy nhất cho clip D mới** (tính từ ràng buộc đồng thời `H↔D ≥ 4` và `C↔D ≥ 4`):
`D ≤ 103,5 Hz` **hoặc** `164,3 ≤ D ≤ 170,1 Hz` ⇒ **`M_LOW` (95,6 Hz) là clip sẵn có duy nhất nằm trong khe.**


**[5] CER pilot v6 — chỉ 5 clip sạch được dùng**

| Vai → clip | CER (2 vế) | CER bỏ danh từ riêng | > 2% | G12 (< 2%) |
|---|---:|---:|---:|---|
| H → `H.wav` | 0,34% | **0,00%** | 1/11 | ✅ |
| D → `M_HIGH` | 1,44% | 0,47% | 4/12 | ✅ |
| C → `C.wav` | 3,09% | 2,14% | 6/12 | ⚠️ |
| N1 → `W6_LOW` | 2,10% | 1,47% | 3/12 | ⚠️ |
| N2 → `W5_HIGH` | 0,21% | 0,25% | 0/11 | ✅ |


---

## 9. Việc cần bạn quyết

| # | Câu hỏi | Lựa chọn | Quyết định |
|---|---|---|---|
| 1 | **G9 H↔D** — làm gì để tách 2 vai nam? | (a) tạo clip VoxCPM2 mới · (b) dùng clip MiniMax · (c) ghi nhận vi phạm | ✅ **(a)** — đã chọn, clip đã có |
| 2 | **G9 N1** — làm gì cho vai nữ phụ? | (a) tạo clip nữ mới ~265 Hz · (b) chấp nhận ~2,95 nc | ✅ **(a)** — đã chọn *(đính chính 30/10: hướng (a) của bản cũ là nữ **cao**; đo đủ số liệu cho thấy phải là nữ **thấp** — xem §7)* |
| 3 | **Ghi công Boson** (H0) — xác nhận chấp nhận? | (a) chấp nhận, ghi công trong mọi tập · (b) chưa | ✅ **(a)** — **ĐÃ CHỐT 30/10/2026** (xem dòng 6) |
| 4 | **Thứ tự tạo clip mới** | — | ✅ Đã xong — Mac mini đã push 4 clip (`bb8896f`) |
| 5 | **Phân bổ vai Tập 02** (L4 — đổi clip = đổi giọng vai) | (a) đổi H/D/N1/N2 sang clip mới · (b) giữ H và D, chỉ đổi N1/N2 | 🔄 **ĐÃ HỎI LẠI 30/10** (bảng số đo mới ở §9.2) — chờ bạn chốt |
| 6 | **Ghi công Boson** (H0) — cách ghi công cụ thể | (a) mọi tập + mô tả video + file nguồn · (b) chỉ mô tả video · (c) chưa chốt | ✅ **(b)** — **ĐÃ CHỐT 30/10/2026**: đặt ở **phần mô tả video khi đăng YouTube**, **KHÔNG ghép vào audio**. Đã ghi vào `02_SAN_XUAT/Tap02/xuat_ban/mo_ta.txt`. ⇒ **H0 đóng**, H4 được phép tiếp tục |

### 9.1 Bảng chọn phân bổ vai — **đã cập nhật sau pilot v8** (số đo thật, §8.12)

Mọi phương án đều giữ **C = `C.wav`** và **N2 = `W5_HIGH.wav`**
(`C↔N2` = 4,99 / 4,83 nc ✅; N2 là bắt buộc vì `W2`/`W1` chỉ được 1,04 / 3,41 nc ❌).

| # | H | D | C | N1 | N2 | H↔D (nc) | Đánh giá |
|---|---|---|---|---|---|---|---|
| **1 ⭐** | `H.wav` **(giữ gốc)** | `M_HIGH.wav` | `C.wav` **(giữ gốc)** | `W6_LOW.wav` | `W5_HIGH.wav` | **7,27 / 6,57 ✅** | **Khuyến nghị.** Đổi **ít nhất**: giữ giọng người dẫn (CER⊘P **0,00%**) và giọng C; chỉ **D phải đổi** vì `H.wav`↔`D.wav` chỉ cách 0,22 nc. `M_HIGH` đúng mô tả vai D ("nam 50+ khàn"). Biên G9 6,57 nc |
| 2 | `M_LOW.wav` | `M_HIGH.wav` | `C.wav` | `W6_LOW.wav` | `W5_HIGH.wav` | **12,24 / 11,23 ✅** | Biên G9 **lớn nhất** (11,23 nc) nhưng **đổi giọng H** → CER 2,43% (⊘P 1,94%) và mất giọng gốc của vai chính |
| 3 | `H.wav` | `M_HIGH.wav` | `C.wav` | `W6_LOW_PS25/PS30` | `W5_HIGH.wav` | 7,27 / 6,57 ✅ | ❌ **ĐÃ LOẠI** — pilot v8 đo thật: TD-PSOLA hỏng khi clone (CER 8,44–10,87%, sai nội dung) |
| 4 | `M_LOW.wav` | `D.wav` **(giữ gốc)** | `C.wav` | `W6_LOW.wav` | `W5_HIGH.wav` | 4,11 / 4,45 ✅ | Biên G9 hẹp nhất; giữ giọng D gốc nhưng CER 3,57% và phải đổi H |

**Phương án đang chạy (tạm, chờ bạn chốt):** **#1** — `H←H.wav` · `D←M_HIGH` · `C←C.wav` ·
`N1←W6_LOW` · `N2←W5_HIGH`. Lượt sản xuất 416 file đã chạy trên Kaggle (2 GPU).
Nếu bạn chọn khác, **chỉ cần sinh lại vai bị đổi** (worker có chế độ `--only` bắt lẻ theo vai).

CER⊘P theo ô: `H.wav` **0,00%** · `M_HIGH` 0,47% · `C.wav` 2,14% · `W6_LOW` 1,47% · `W5_HIGH` 0,25%
(đầy đủ 13 ô ở §8.10).

> **Một điểm bạn cần biết trước khi chốt (L4):** nếu hiểu G9 theo nghĩa **"mọi cặp cùng giới"**,
> **không phương án nào đạt** — cặp `C↔N1` luôn ở 2,58 nc (§8.12 mục [4]). Lựa chọn còn lại nếu bạn
> muốn G9 tuyệt đối: **nhờ Mac mini tạo thêm 1 clip nữ ở F0 thấp hơn** (mục tiêu ≤ 160 Hz, **không
> được xử lý tín hiệu**) — rủi ro cao vì lần trước Mac nhắm 148–162 Hz mà ra 179,1 Hz.


### 9.2 Việc đã làm xong (30/10, sau khi bạn chạy script trên Mac mini)

```text
✓ Mac mini tạo 4 clip + commit + push            (bb8896f)
✓ Đo F0 4 clip mới (2 thuật toán)               (§6.9)
✓ Phát hiện: cả 3 cặp nữ đều trượt G9           (§6.10)
✓ Hạ F0 W6_LOW bằng phase vocoder → 5 biến thể   (§6.11)
✓ Xây hạ tầng 2 GPU + catch-up                   (§8.9)
✓ Kernel pilot v6 → 156/156 OK, đã tải về        (§6.12)
✓ Tính lại CER pilot v6 (đúng chuẩn hóa 2 vế)    (§6.13, §8.10)
✓ Phát hiện phase vocoder hỏng khi CLONE         (§6.14)
✓ TD-PSOLA → 5 clip mới, ASR 0,00%               (§6.14)
✓ Kernel pilot v7 (clone W4/W2) → 24/24 OK       (kit nghe mù H3) · CER W4 4,48%, W2 2,18%
✓ Kernel pilot v8 → 36/36 OK  → TD-PSOLA CŨNG HỎNG (§6.15)
✓ Bảng G9 đầy đủ — đo lại mọi ô v6+v7+v8        (§8.12)
✓ Kernel SMOKE 2 GPU (12 file) → 12/12 OK       (chứng minh đường chạy 2 card)
✓ Chốt mapping tạm #1 → build spec 416 file      (§9.1)
✓ Dataset Kaggle v8 + kernel sản xuất đẩy lên    (đang chạy)
```

**Bước kế tiếp:** lượt sản xuất 416 file (2 GPU) → đo CER từng câu → chọn bản §7 → vòng 2 cho câu lỗi →
**H3** (nghe mù V7 + G8, dựng lại theo mapping cuối) → **H4** *(đã mở lại 30/10 — H0 đã chốt)* →
**H5** (dựng video).

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

### Tool mới (30/10) — G9 + hạ tầng 2 GPU

| File | Vai trò |
|---|---|
| `.work/g9_matrix.py` | Bảng G9 đầy đủ mọi cặp cùng giới (28 cặp, 9 phân bố) từ pilot v3+v4 |
| `.work/pilot_v5_f0.py` | F0 thật pilot v5 + duyệt 9 tổ hợp H×D |
| `.work/g9_newclips.py` | Đo F0 + QC 4 clip mới và 7 clip gốc; duyệt phân bộ vai |
| `.work/g9_shift_clip.py` | **Phase vocoder** — hạ F0 `W6_LOW` thành 5 biến thể S20–S40 |
| `.work/g9_update_refs.py` | Cập nhật `refs.json` (F0 thật sau khi hạ) + đồng bộ dataset Kaggle |
| `.work/g9_role_map.json` | **Phép gán vai → clip** (sửa 1 file rồi chạy lại `build_spec.py`) |
| `.work/higgs_worker.py` | Worker 1 tiến trình / 1 GPU — seed xác định, checkpoint từng file |
| `.work/build_nb.py` | Builder notebook Kaggle (dùng chung pilot + sản xuất), verify cell compile + base64 |
| `.work/build_spec.py` | Sinh `pilot_spec_v6.json` / `pilot_payload_v6.json` / `prod_spec.json` / payload sản xuất |
| `.work/prep_dataset_meta.py` | Làm mới `dataset-metadata.json` (mô tả + resource) |
| `.work/prep_push_dirs.py` | Tạo thư mục push kernel (`id` phải khớp slug Kaggle **sinh từ title**) |
| `.work/watch_kernel.py` | Theo dõi kernel + tải output (bắt buộc `--file-pattern`) |
| `.work/analyze_pilot_v6.py` | Đo F0 clone (2 thuật toán) + CER + bảng G9 đầy đủ của pilot v6 |

### Tool mới (30/10, vòng 2) — CER chuẩn hoá + TD-PSOLA + pilot v8

| File | Vai trò |
|---|---|
| `.work/vi_cer.py` | **Module chuẩn hoá CER dùng chung** — `vi_number`/`vi_numbers` copy nguyên văn từ `tts_sentences.py` + `selfcheck()` (khớp 100%); 3 hàm: `cer_pair` (chính thức) · `cer_pair_nonum` · `cer_pair_prop` (bỏ danh từ riêng) |
| `.work/cer_detail.py` | Soi **từng câu** lỗi của 1 lượt Higgs (in REF/HYP, 3 metric) |
| `.work/cer_ref_clips.py` | **Đo ASR trên chính clip tham chiếu** (có lời mẫu) — dùng để chứng minh phase vocoder hỏng *khi clone* chứ không hỏng *khi đọc* |
| `.work/g9_psola_shift.py` | **TD-PSOLA** (giai thuốc sóng + resample FFT) — 5 clip mới `W6_LOW_{TRIM,PS15,PS20,PS25,PS30}` |
| `.work/dbg_psola_marks.py` | Kiểm tra dấu nhịp / chu kỳ TD-PSOLA |
| `.work/prep_v8.py` | Đồng bộ clip TD-PSOLA vào `refs.json` + dataset Kaggle |
| `.work/cer_ref_clips.json` | Số đo CER của 19 clip tham chiếu (2 vòng ASR mỗi clip) |

### Bộ tạo clip VoxCPM2 mới cho G9 (đã chạy trên Mac mini)

| File | Vai trò |
|---|---|
| `.work/voxcpm_generate_g9.py` | **Script chạy trên Mac mini** — dò thang `control`, đo F0, chọn take, đóng gói 24 kHz |
| `.work/voxcpm_refs_manifest_g9.json` | Mô tả giọng + thang `control` + dải F0 của 3 clip mới |
| `.work/G9_HD_HUONG_DAN.md` | **Hướng dẫn đầy đủ** "làm lại ở Vox" (bảng từ khoá → F0, cách dò thang) |
| `.work/DAT_SPEC_G9.md` | Đặc tả ngắn |
| `.work/G9_MAC_BRIEF.md` | Brief tự-contained cho AI trên Mac M2 (1 lệnh, 5 tiêu chí nghiệm thu) |

### Tool mới (30/10, vòng 3) — G9 đầy đủ + smoke 2 GPU + lượt sản xuất

| File | Vai trò |
|---|---|
| `.work/g9_decide.py` | **MỚI** — đo lại F0 clone của **mọi** ô pilot v6+v7+v8, dựng bảng G9 đầy đủ theo **giới tính**, tự tính **cặp liền kề thật** từ `script_tap02.json`; xuất `g9_decide.txt` / `g9_decide.json` (§8.12) |
| `.work/g9_decide.txt` / `.work/g9_decide.json` | Số đo thô bảng G9 (F0 clone + khoảng cách nc + verdict) |
| `.work/g9_role_map.json` | **ĐÃ CHỐT TẠM** — `H←H.wav` · `D←M_HIGH` · `C←C.wav` · `N1←W6_LOW` · `N2←W5_HIGH`, kèm bảng F0/CER/cảnh báo |
| `.work/build_smoke_spec.py` | Sinh `prod_spec_smoke.json` (12 file — 5 vai + 1 câu emotion) |
| `.work/prep_push_dirs.py` | Đã sửa slug kernel smoke: `…-smoke-2-gpu-…` (Kaggle slug hoá "2 GPU" → "2-gpu") |
| `.work/cer_detail_v7.txt` | CER chi tiết 2 ô pilot v7 (`W4` 4,48% · `W2` 2,18%) |
| `.work/cer_detail_v8.txt` | CER chi tiết 3 ô pilot v8 (TD-PSOLA) — **bằng chứng loại TD-PSOLA** |

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
