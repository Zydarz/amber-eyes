# QUY TẮC TẠO AUDIO BẰNG HIGGS AUDIO — MAC MINI M2 16 GB (thay MiniMax)

> Dành cho mọi AI làm việc trong dự án Amber eyes. Đọc cùng `AGENTS.md`. File này **thay mục 4 (Giọng đọc) và T2, T8, T9** của AGENTS.md khi engine TTS là Higgs.
> Cấu hình đã chốt (người dùng, 27/10/2026): **Higgs Audio (Boson AI) chạy cục bộ trên Mac mini M2, RAM 16 GB, qua MLX-Audio.** Người dùng đã cài và tạo được audio.
> Nghiên cứu từ tài liệu chính thức ngày 27/10/2026 (nguồn: mục 12). Dòng ghi **CHƯA XÁC MINH** = phải đo trên máy trước khi dựa vào.
> Bản đầu (hướng API/GPU) lưu ở `.work/_cu/QUY_TAC_AUDIO_HIGGS_v1_20261027.md`.

Từ khoá: **PHẢI** · **CẤM** · **NÊN** — như AGENTS.md.

---

## 0. Nguyên tắc cao nhất

1. **"Higgs tốt hơn MiniMax" là giả thuyết, chưa phải kết luận.** Chỉ được thay MiniMax trong sản xuất khi số đo qua cổng ở mục 9 (CER < 2%, G8, G9, nghe duyệt). Bảng so sánh phải có **cùng 20 câu** đọc bằng cả hai engine.
2. **Chất lượng trước, tốc độ sau.** Máy chạy miễn phí ⇒ được phép đọc nhiều bản một câu và chọn bản tốt nhất (mục 7). Không đánh đổi chất lượng lấy thời gian.
3. **Chỉ đo, không đoán** (L2, L3).

## 1. Chọn đúng mô hình — lỗi dễ mắc nhất

| Mô hình | Tiếng Việt | Bản MLX | Dùng? |
|---|---|---|---|
| **Higgs Audio v3 / Higgs TTS 3 (4B)** — `bosonai/higgs-audio-v3-tts-4b` (= `bosonai/higgs-tts-3-4b`) | **Có**, nhóm WER/CER < 5 (số của Boson) | bf16 (~9,3 GB trọng số). MLX-Audio có hỗ trợ v3; bản chuyển MLX của bên thứ ba: `aufklarer/Higgs-TTS-3-4B-MLX-bf16` | **DÙNG** |
| Higgs Audio v2 (3B) — `mlx-community/higgs-audio-v2-3B-mlx-q8` / `-q6` | **Không xác nhận** | q8 6,2 GB · q6 4,8 GB | **CẤM** cho bản VN |

- ⚠ Hướng dẫn Higgs trong MLX-Audio **chủ yếu là v2** (các bản q8/q6 nhẹ đều là v2). Dễ tải nhầm v2 vì nhẹ hơn.
- **PHẢI kiểm và ghi vào hồ sơ tập** tên repo model đang chạy thật + phiên bản `mlx-audio` (`pip show mlx-audio`). Nếu là v2 → dừng, báo người dùng.
- Ưu tiên trọng số **gốc `bosonai/...`**. Bản bên thứ ba (`aufklarer/...`) chỉ dùng khi bản gốc không chạy được, và phải ghi `provenance.json`.
- Không có bản v3 nén MLX chính thức. Bản GGUF Q8/Q4 (`drbaph/Higgs-Audio-v3-Studio`) là cho llama.cpp, **không phải MLX** → CẤM trộn vào pipeline khi chưa đo CER riêng.

## 2. Máy M2 16 GB — vận hành

- Trọng số v3 bf16 ~9,3 GB; Boson đo bộ nhớ đỉnh **~9–12 GB trên M1 32 GB**. Trên 16 GB là **sát giới hạn** (macOS + bộ mã hoá âm thanh cũng chiếm RAM).
- **PHẢI** khi chạy loạt dài:
  - Đóng trình duyệt, IDE nặng, app khác. Chỉ **1 tiến trình Higgs** tại một thời điểm (T3).
  - **Nạp model 1 lần**, đọc tuần tự mọi câu trong cùng tiến trình Python (`mlx_audio.tts.utils.load` → lặp `model.generate`). **CẤM** gọi CLI một lần/câu (nạp lại ~9 GB mỗi câu).
  - Theo dõi swap: `sysctl vm.swapusage` trước/sau 10 câu. Swap tăng mạnh hoặc mỗi câu chậm dần → dừng, khởi động lại tiến trình. Đây là việc **tạm dừng đúng mức**, không phải lỗi giọng.
  - Ghi log ra file, chạy nền, lưu tiến độ để chạy tiếp từ câu dở (T1). File đã có thì bỏ qua.
- Đo và ghi vào hồ sơ: **giây máy / giây audio (RTF)** trên M2 sau 20 câu đầu (CHƯA XÁC MINH — số Boson/MLX đều đo trên máy khác). Dùng số này ước giờ chạy cả tập.
- **CẤM** hạ xuống bản lượng tử hoá để chạy nhanh hơn nếu bản đó chưa qua CER < 2% (mục 9).

## 3. Giấy phép (chạy cục bộ)

- Trọng số v3: *Boson Higgs Audio v3 Research and Non-Commercial License*. Chạy cục bộ để làm video cho **kênh mình sở hữu** thuộc **Creator Use Grant (mục II-A)**: được đăng và **kiếm tiền**.
- **Điều kiện bắt buộc: ghi công** trong audio hoặc chữ hiển thị rõ. Mẫu của Boson:
  `This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio`
  → **PHẢI** có trong mô tả YouTube **mọi tập** dùng Higgs. Sửa mô tả/thẻ kết là quyết định của người dùng (mục 9 AGENTS.md: thẻ miễn trừ intro CẤM sửa).
- **Clone giọng chỉ khi có đồng ý rõ ràng, kiểm chứng được** của chủ giọng; lưu hồ sơ đồng ý. **CẤM** clone giọng người trong vụ án, phóng viên, diễn viên, giọng tải từ YouTube/MiniMax/ElevenLabs.
- **CẤM** gán lời bịa cho người thật (trùng K2/K3). Giữ "Nội dung bị thay đổi hoặc tổng hợp" khi đăng.
- *Tóm tắt văn bản giấy phép, không phải tư vấn pháp lý.*

## 4. Giọng — dùng audio tham chiếu (yếu tố quyết định chất lượng số 1)

Không đưa tham chiếu thì Higgs chọn **giọng ngẫu nhiên mỗi lần** ("smart voice") ⇒ mỗi câu một người ⇒ vi phạm G8 ngay. ⇒ **PHẢI clone từ file tham chiếu cố định cho mỗi vai.** Giọng mẫu sẵn trong repo (`en_woman`, `en_man`, `en_man_deep`) là giọng Anh — chỉ để thử, không dùng sản xuất.

**Chuẩn file tham chiếu** (`assets/voice_ref/<vai>.wav` + `<vai>.txt`):

| Mục | Yêu cầu | Nguồn |
|---|---|---|
| Độ dài | **8–15 s** (MLX-Audio khuyên 5–15 s; Boson 5–30 s → lấy phần giao, tránh mép 5 s) | MLX-Audio, docs Boson |
| Ngôn ngữ | **Tiếng Việt**, người đọc giọng Việt chuẩn — để mô hình học đúng thanh điệu | suy từ cơ chế clone; CHƯA XÁC MINH bằng số đo ⇒ so với tham chiếu tiếng Anh ở bước H2 |
| Âm thanh | Sạch: không nhạc, không giọng thứ hai, không vọng phòng, không nén mạnh; không cắt cụt đầu/cuối | docs Boson |
| Định dạng | WAV mono, 24 kHz (tần số đầu ra của Higgs), 16-bit | |
| Mức | −20…−16 LUFS, đỉnh ≤ −1 dBFS | |
| Lời | `ref_text` **chép đúng từng chữ, kể cả "ờ, à"**. MLX-Audio: ref_text **bắt buộc** để căn chỉnh ổn định | MLX-Audio, docs Boson |
| Chất giọng | Đọc **đúng chất vai, cảm xúc trung tính, tốc độ production**. Tham chiếu buồn/nhanh sẽ làm mọi câu buồn/nhanh | |
| Nội dung | Câu đủ 6 thanh (ngang, huyền, sắc, hỏi, ngã, nặng), không có số, không tên nước ngoài | |

- **Bộ tham chiếu hiện tại (27/10/2026) — để giống giọng MiniMax bộ A:** `assets/voice_ref_higgs/{H,D,C,N1,N2}.wav/.txt`, sinh bằng `AE_EP=02 py -3 .work/higgs_make_refs.py` từ audio MiniMax Tập 02: chỉ câu `neutral`, không chữ số, không từ Latin, **loại câu có CER đo > 2%** (`cer_bo_a_tap02`), ưu tiên câu đã đo CER = 0. Lỗi đã gặp: lần chạy đầu chọn đúng câu "Thứ hắn lấy đi…" mà giọng Korean đọc sai thành "Thương hiệu Han Lady" (CER 28%) — **clone từ câu đọc sai thì Higgs học luôn lỗi thanh điệu**. Trạng thái: **chờ người dùng xác nhận điều khoản MiniMax cho phép dùng đầu ra làm tham chiếu** (L4); trước đó chỉ dùng để thử, không đăng.
- Triệu chứng "lẫn nam nữ, cao thấp" = đang chạy **không có `ref_audio`** (người dùng gặp 27/10/2026). Đọc bằng `.work/higgs_tts_mac.py` (luôn truyền `ref_audio` + `ref_text` theo vai, nạp model 1 lần, seed theo câu).
- Mỗi vai **một** file tham chiếu, cố định cho cả tập và cả kênh. **Đổi file tham chiếu = đổi giọng nhân vật** → L4 + G8–G13.
- Mỗi file có dòng `provenance.json`: người đọc, giấy đồng ý, ngày thu, thiết bị.
- 3 vai chính khác nhau rõ (G9: cùng giới cách ≥ 4 nửa cung F0 trung vị) **ngay từ file tham chiếu** — đo F0 tham chiếu trước khi đọc câu nào.
- Khai bộ giọng Higgs thành bộ mới trong `.work/edition.py` (ví dụ `CAST_HIGGS`: vai → đường dẫn tham chiếu). **Không** đè `CAST` và `EPISODES["01"]["cast"]` (L8, L9).

## 5. Văn bản gửi vào Higgs

| Luật | Với Higgs |
|---|---|
| **1 câu kịch bản = 1 lần sinh** | Giới hạn mặc định `max_new_frames = 1200` ≈ **48 s**. Câu dài hơn bị **cắt cụt im lặng** ⇒ kiểm độ dài (mục 8). Câu > ~300 ký tự: tách tại dấu câu, không cắt giữa ý (G1) |
| G1 | **Xoá mọi thẻ MiniMax `<#…#>`** và `...`. Thẻ lạ bị đọc thành chữ hoặc làm hỏng câu |
| G11 | Giữ `vi_numbers()`: số → chữ tiếng Việt **trước** khi gửi. Ký hiệu (%, $, km) viết bằng chữ (K7) |
| G7 | Bỏ chú thích tiếng Anh trong ngoặc; tên riêng nước ngoài NÊN phiên âm nhẹ nếu đo thấy đọc sai |
| G6 | Thẻ `<|…|>` chỉ có trong **bản gửi TTS**; phụ đề/chữ trên hình lấy câu gốc. Script so chữ **bỏ thẻ trước khi so** |
| Dấu câu | Giữ dấu chấm, phẩy, hỏi chuẩn — đó là tín hiệu ngắt nhịp tự nhiên. Không dùng nhiều dấu chấm than |

**Thẻ điều khiển** (Higgs v3, cú pháp `<|nhóm:tên|>`, chỉ 43 thẻ trong `PROMPTING.md` được nhận; thẻ khác bị đọc thành chữ):

| Loại | Quy định |
|---|---|
| Cảm xúc (G3) | Ánh xạ cố định, đặt **đầu câu**: `neutral` → không thẻ · `sad` → `<|emotion:sadness|>` · `fearful` → `<|emotion:fear|>` · `surprised` → `<|emotion:surprise|>`. **CẤM** 17 cảm xúc khác |
| Ngắt | Chỉ **một** `<|prosody:pause|>` (~0,4–0,7 s) sau dấu `:` trước câu trích. CẤM `pause`/`long_pause` ở chỗ khác (G1); kịch tính đặt giữa câu bằng `_pause_after` (G2) |
| Tốc độ (G4) | **CẤM `speed_*`** (4 nấc ×0,65–×1,4, vượt dải G4). Lệch tốc nhỏ −0,06…+0,02 làm bằng ffmpeg `atempo` sau khi đọc |
| Cao độ (G5) | **CẤM `pitch_low/high`** (−3/+2,5 nửa cung = nguy cơ "thành người khác") |
| `expressive_*`, `style:*` | CẤM khi chưa qua G8 |
| `sfx:*` | **CẤM** — tiếng động thuộc lớp SFX của `build_audio3.py`; `crying`/`screaming` trái tinh thần V9 |

- ⚠ **CHƯA XÁC MINH:** đường MLX-Audio có hiểu các thẻ `<|…|>` của v3 hay đọc chúng thành chữ. **Trước khi dùng bất kỳ thẻ nào: đọc 5 câu có thẻ, đo `listen_audio` — nếu bản chép có chữ "emotion", "sadness"… → tắt toàn bộ thẻ**, chỉ dùng câu trơn.
- Script **PHẢI** kiểm regex: mọi `<|…|>` trong văn bản gửi đi thuộc danh sách cho phép ở bảng trên; sai → dừng.

## 6. Tham số sinh

| Tham số | Giá trị khởi đầu | Ghi chú |
|---|---|---|
| `temperature` | **0,7** (mặc định MLX-Audio); Boson khuyên 0,8 cho clone | Thấp → ổn định danh tính, ít lỗi chữ, nhưng đều đều. **Dò 0,6 / 0,7 / 0,8** trên 20 câu ở bước H2, chọn mức có CER thấp nhất mà vẫn qua nghe duyệt. Ghi mức đã chọn vào `CAST_HIGGS` |
| `top_p` | 0,95 | mặc định MLX-Audio |
| `top_k` | 50 | Boson khuyên |
| `max_new_frames` | 1200 (≈ 48 s) | Đủ cho câu kịch bản; không tăng — câu dài thì tách |
| `fade_in_ms` / `fade_out_ms` | 30 | mặc định; tránh tiếng "bụp" ở mép |
| `seed` | Cố định theo câu (ví dụ hash mã câu), ghi vào manifest | Để đọc lại ra đúng bản. Cờ seed **CHƯA XÁC MINH** trên đường MLX — kiểm `--help`; nếu không có thì đặt `mx.random.seed()` trước mỗi câu |
| Đầu ra | WAV 24 kHz mono | **Không xuất mp3** (tránh nén 2 lần). Pipeline chạy `SR = 44100` ⇒ resample bằng `ffmpeg -ar 44100 -af aresample=resampler=soxr` khi nhập |

- CLI tối thiểu đã được ghi trong tài liệu MLX-Audio: `--model --text --ref_audio --ref_text`. Các cờ khác **chỉ dùng sau khi xem `python -m mlx_audio.tts.generate --help` trên máy**, ghi kết quả vào hồ sơ.

## 7. Đọc nhiều bản, chọn bản tốt nhất (lợi thế của chạy miễn phí)

- Mỗi câu NÊN sinh **2 bản** (seed khác nhau), câu hé lộ/câu trích sinh **3 bản**.
- Chọn tự động theo thứ tự: (1) CER thấp nhất qua `listen_audio` (Q3: áp `vi_numbers` cả hai vế; câu bị bộ lọc Gemini chặn thì loại khỏi chấm, chọn theo tiêu chí 2–3) · (2) không cắt cụt, không lặp chữ · (3) độ dài gần trung vị các câu cùng vai (tốc độ đều).
- Bản thắng có CER > 2% → sinh thêm tối đa 2 bản; vẫn trượt → **đánh dấu cho người dùng nghe**, không tự sửa chữ câu.
- Lưu **mọi bản**, manifest ghi bản nào được chọn và vì sao.

## 8. Kiểm tra mỗi file (thay T2)

Một câu chỉ tính **xong** khi:
1. File giải mã được (`ffprobe`), 24 kHz.
2. Độ dài > 0,5 s và **< 47 s** (chạm 48 s = nghi bị cắt bởi `max_new_frames`).
3. Tỉ lệ giây/âm tiết trong khoảng trung vị ± 35% của vai đó (bắt câu nói vội, bỏ chữ, hoặc lặp).
4. Không có khoảng lặng > 0,3 s ở −60 dB **bên trong** câu (V4), không có đuôi tạp âm/tiếng thở dài cuối câu (cắt đuôi ở −50 dB).
5. Đạt mục 7.

## 9. Quy trình chuyển đổi — có cổng, không nhảy cổng

| Bước | Việc | ĐẠT khi |
|---|---|---|
| H0 | Người dùng chốt: người đọc tham chiếu cho từng vai + giấy đồng ý · chấp nhận ghi công Boson | Ghi trong hồ sơ tập |
| H1 | Xác minh môi trường: model **v3**, `mlx-audio --help`, RAM/swap, RTF 20 câu; thẻ `<|…|>` có tác dụng hay bị đọc thành chữ | Ghi số đo vào hồ sơ |
| H2 | **So với MiniMax**: cùng 20 câu/vai, đúng emotion production. Đo CER (lượt 2 cho câu vượt ngưỡng, Q6), dò temperature (mục 6) | Mỗi vai **CER < 2%** và **không tệ hơn MiniMax** |
| H3 | G8 (1 câu × mọi cảm xúc dùng → 1 người) · G9 (≥ 4 nửa cung, F0 trung vị) · nghe mù gán vai đúng 100% (Q1, Q4) | Qua cả ba |
| H4 | Đọc 1 hồi, `voice_role_check.py` (G10), `build_audio3.py` | 0 câm > 0,3 s · −16 ± 1 LUFS · đỉnh ≤ −1,5 dBFS · người dùng nghe duyệt |
| H5 | Đọc cả tập | 100% câu qua mục 8 |

**Mốc dừng chờ người dùng:** sau H0, sau H2 (bảng so sánh Higgs vs MiniMax), sau H4.
Code: thêm nhánh engine trong `tts_sentences.py` (ví dụ `AE_TTS=higgs`), **giữ nguyên nhánh MiniMax**; không đặt `AE_TTS` → manifest Tập 01 giống hệt bản cũ (L9). Script chạy trên Mac; nếu chạy từ máy Windows thì Mac chỉ sinh audio, Windows giữ phần dựng.

## 10. Lưu trữ

- Audio Higgs vào thư mục riêng (ví dụ `audio_s_higgs/`), **CẤM ghi đè** `audio_s/` của MiniMax (L5).
- Kèm `higgs_manifest.json`: văn bản gửi đi (có thẻ), vai, file tham chiếu, model + phiên bản mlx-audio, temperature, top_p, top_k, seed, các bản đã sinh, bản được chọn, CER.
- `provenance.json` từng file: `tool: "Higgs Audio v3 (MLX, Mac mini M2)"`, `license: "Boson Higgs Audio v3 Research and Non-Commercial License — Creator Use Grant II-A"`, `attribution_required: true`, `commercial_checked: false` (đến khi người dùng xác nhận).

## 11. CHƯA biết — phải đo trên máy (L2/L3)

> **ĐÃ ĐO 30/10/2026** (đường PyTorch/transformers trên Kaggle GPU, không dùng MLX-Audio — chỉ chạy được
> trên Apple Silicon). Báo cáo đầy đủ: `90_LUU_TRU/BaoCao_H2_Higgs_Pilot_Tap02_20261030.md`.

**Đã có số đo:**

1. Model **v3** (`bosonai/higgs-tts-3-4b`, trọng số gốc; mượn 2 file loader từ
   `multimodalart/higgs-audio-v3-tts-4b-transformers` + tự thêm `auto_map`). transformers **5.22.0**,
   torch **2.11.0+cu128**, GPU **Tesla T4 15,6 GB (sm_75)**, **bf16 có**. Frame-rate bộ giải mã
   **25,02 Hz** ⇒ `max_new_tokens = int(47,5 × 25,02) + 8 = **1196**` (KHÔNG dùng `max_new_frames`).
   VRAM đỉnh **9,94 GB**, RTF tb **2,15** (max 2,98). Không dùng được GGUF (luật 1).
2. ~~RAM/swap trên M2 16 GB~~ → **bỏ đường MLX-Audio** (chỉ chạy trên Apple Silicon, máy này không có
   GPU) ⇒ chuyển sang Kaggle GPU (30 h/tuần, còn ~29,5 h).
3. **Thẻ `<|…|>`: CÓ tác dụng** — đo bằng `listen_audio`, bản chép không chứa từ khóa thẻ.
   ⚠ Nhưng **không truyền `reference_audio` thì đọc sai thanh điệu nặng** ⇒ bắt buộc clone (§4).
4. API `generate_speech(text, tok, *, reference_codes, reference_text, max_new_tokens, temperature,
   top_p, top_k)` — **không có** tham số `speed_*`/`pitch_*` ⇒ G4/G5 tự động đạt; **không có tham số seed**
   ⇒ phải `torch.manual_seed` + `torch.cuda.manual_seed_all` trước mỗi lời gọi.
   Mã hoá ref: `model._encode_reference(torch.from_numpy(arr).float().unsqueeze(0), sr)` → `[T, N]`;
   **encode 1 lần/clip rồi cache** (tiết kiệm lớn GPU).
5. **CER thật** (96 bản pilot, 2 lượt `listen_audio`, lấy lượt xấu hơn, chuẩn hóa 2 vế theo Q3a):
   **H t=0,8 → 0,00%** · **C t=0,8 → 0,00%** · **D t=0,7 → 0,99%** / t=0,8 → 2,27% ·
   **N2←W1 → 0,63%** · N1←W1 → 1,08% (MiniMax cùng chuẩn hóa: H 0,89% · D 1,72% · C/N1/N2 0,00%).
   ⇒ **Higgs tốt hơn MiniMax rõ ở vai H**; D cần đa bản §7.
6. Tham chiếu **tiếng Việt** cho thanh điệu tốt hơn: **có** — cùng model, clip VI cho CER 0,00% ở H/C.
7. ~~G8 ổn định danh tính~~ — **chưa đo** (cần nghe mù V7).

**MỚI phát hiện 30/10 — G9 KHÔNG ĐẠT ở H↔D (đo lại trên 192 audio pilot v3+v4, n=16/ô):**

* F0 **của audio đã clone** (không phải clip gốc): H **131,1 Hz**, D **122,4 Hz** ⇒ **1,19 nửa cung**
  (AC thô) / **0,01 nc** (AC chuẩn hóa + sửa octave) — cần ≥ 4.
* Cơ chế (**đã xác nhận bằng pilot v5, 104 bản**): Higgs **CÓ bắt chước cao độ** của clip tham chiếu,
  nhưng **không chính xác 1-1**. Cho **cùng một clip** vào **hai vai khác nhau** thì F0 clone gần như
  **y hệt** (W4: H 140,4 Hz vs D 141,2 Hz · W3: H 162,2 Hz vs D 160,0 Hz) ⇒ **cao độ clone do clip
  tham chiếu quyết định**. Tỉ lệ `clone / clip` = **1,02–1,06** ở ref ≥ 132 Hz, nhưng **1,22** ở ref
  thấp (H.wav 107→131 Hz) ⇒ **khi tạo clip thấp (cho vai H) phải chừa biên cho cú kéo lên này**.
* ⇒ Đổi clip tham chiếu **là đủ** để tách vai — không cần tinh chỉnh thêm tham số đọc.
* Với 7 clip VoxCPM2 VI hiện có **không thể đạt G9 cho H↔D**: tổ hợp tốt nhất là
  `H←W3 + D←D.wav` = 4,78 nc (AC thô) / 3,96 nc (AC chuẩn hóa) — *chưa chắc đạt theo cả 2 thuật toán*,
  và W3 là giọng nam trẻ ⇒ **cần clip tham chiếu mới** (H: clip **70–86 Hz** · D: clip 150–190 Hz)
  hoặc ghi nhận vi phạm (cần người dùng quyết).
* **3 vai nữ ⇒ 3 cặp phải kiểm** (C↔N1 · C↔N2 · **N1↔N2**). Cặp **N1↔N2 bị bỏ sót** trong bản đo đầu:
  N1←W1 = 247,4 Hz, N2←W1 = 275,9 Hz ⇒ **1,89 nc ❌**. `C ↔ N1` (W1) = 3,25 nc ❌ ·
  `C ↔ N2` (W1) = 5,13 nc ✅ ⇒ **N2 ← W1 chốt được**.
* ⇒ **N1 phải là giọng nữ THẤP, không phải cao.** Vì C (205 Hz) và N2 (276 Hz) đã cách nhau 5,13 nc,
  N1 phải **≤ 162,8 Hz** để cách **cả hai** ≥ 4 nc. Nếu đưa N1 lên 258–276 Hz thì N1 **áp sát N2**
  (~1,7 nc) ⇒ vi phạm G9 mới. Cần clip nữ mới `W6_LOW` (F0 clip 148–162 Hz).
* Bảng G9 đầy đủ + script đo lại được: `.work/g9_matrix.py` → `.work/g9_matrix.json` / `.work/g9_matrix.txt`.

**BẪY ĐO LẠI (rất dễ sai):** `tts_sentences.py:105` gửi **số → chữ** cho TTS, còn ASR trả **chữ số**.
Phải áp `vi_numbers()` cho **CẢ HAI VÊ** và dùng **đúng** `vi_number()` của `tts_sentences.py`
(bản rút gọn làm `"2009"` → *"two nine"*). Không sửa thì **cả Higgs lẫn MiniMax đều bị phình CER**
(câu `1.03#1` hoàn toàn đúng bị tính thành 73,8%).

**Còn chưa biết:**

6. Tham chiếu nào cho **H**, **D** và **N1** để đạt G9 (cần clip mới từ Mac mini — `M_LOW` / `M_HIGH` /
   `W6_LOW`; hoặc dùng clip MiniMax — cần xác nhận điều khoản L4; hoặc ghi nhận vi phạm).
8. G8 (nghe mù 100%) — chưa chạy.
9. Người dùng xác nhận **chấp nhận ghi công Boson** (H0) — điều khoản Creator Use Grant II-A cho phép
   thương mại nhưng **bắt buộc** ghi "This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio"
   trong mô tả mọi tập.

Lỗi mới gặp: thêm dòng vào mục 5/8/11 ở đây **và** tiêu chuẩn mục A11 (L6). Khi Higgs được chốt sản xuất: cập nhật bảng bộ giọng ở mục 4 AGENTS.md.

## 12. Nguồn (truy cập 27/10/2026)

- Model card v3: https://huggingface.co/bosonai/higgs-audio-v3-tts-4b
- Danh mục thẻ: https://huggingface.co/bosonai/higgs-tts-3-4b/blob/main/PROMPTING.md
- Hướng dẫn agent (có số RAM MLX): https://huggingface.co/bosonai/higgs-tts-3-4b/blob/main/AGENTS.md
- Giấy phép: https://huggingface.co/bosonai/higgs-tts-3-4b/blob/main/LICENSE
- MLX-Audio, mô hình Higgs: https://github.com/Blaizzy/mlx-audio/tree/main/mlx_audio/tts/models/higgs_audio
- Bản MLX bf16 bên thứ ba: https://huggingface.co/aufklarer/Higgs-TTS-3-4B-MLX-bf16
- Docs Boson (giọng, tham chiếu): https://docs.boson.ai/models/higgs-audio-tts/voices
