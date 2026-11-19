# Báo cáo QC audio clip TikTok TK1 (Tập 01) — 18/11/2026

> Người lập: AI · Dữ liệu đo thật từ file người dùng tạo · Không sửa bất kỳ audio nào.

---

## 0. Tóm tắt nhanh

| Hạng mục | Kết quả |
|---|---|
| **File** | `02_SAN_XUAT/TIKTOK/Tap01/TK1_master_audio.wav` (+ `.mp3` 256 kbps) |
| **Độ dài** | 66,60 s (cổng 45–95 s · target TK1 65–85 s) ✅ |
| **Cổng đạt** | T5 âm lượng · T6 khoảng câm · T4 độ dài · G6 khớp spec · G9 tách bạch giọng |
| **Cổng KHÔNG đạt** | **G12 — CER < 2 % mỗi câu: 11/12 câu có TB ≥ 2 %, TB toàn clip 6,72 %** |
| **Lỗi phát âm THẬT** (lặp ở ≥ 2 lượt ASR) | `TK1.01#4`, `#5` (vai D) · `#7`, `#9`, `#10` (vai C) · `#12` (vai H) |
| **Kết luận hành động** | **Dựng hình được** (âm thanh sạch, đủ loudness, 3 vai tách bạch rõ) — nhưng nên **sinh lại 6 câu nêu trên** trước khi đăng, vì lỗi nằm ở thanh điệu/từ bị nuốt, người xem TikTok sẽ nghe rõ |

---

## 1. File và dấu vân tay (L7)

| File | Định dạng | Dung lượng | SHA-256 |
|---|---|---|---|
| `TK1_master_audio.wav` | pcm_s16le · 48 000 Hz · 2 kênh · 16 bit | 12,79 MB | `33E5DD0912B13C1B1E771589A012F975C1F3D5BCA15D8404F010217B0039612E` |
| `TK1_master_audio.mp3` | mp3 · 48 000 Hz · 2 kênh · 256 kbps | 2,13 MB | `F068782C5A37C2452F569890AFD0571FC35B3748D6E43DAAC399DFE55DED689E` |

Lệch WAV–MP3 = **0,000 s** (đồng bộ tuyệt đối).

---

## 2. Bảng cổng QC (đo thật, không "nói xong")

| Cổng | Kiểm | Ngưỡng | Đo được | KQ |
|---|---|---|---|---|
| T4 | Độ dài clip | 45–95 s (target 65–85) | 66,60 s | ✅ |
| T5 | Âm lượng tích hợp | −16 ± 1 LUFS | **−16,0 LUFS** | ✅ |
| T5 | True peak | ≤ −1,5 dBFS | **−4,5 dBFS** | ✅ |
| T5 | Đỉnh biên / DC | không clip | biên 0,595 · DC 0,000281 | ✅ |
| T6 | Khoảng câm (ngưỡng −60 dB, ≥ 0,3 s) | 0 | **0 khoảng** (file gốc vô) | ✅ |
| G6 | Khớp timeline ↔ spec | 100 % | 12/12 câu · 0 lỗi text · 0 lỗi vai · 0 lỗi pause · 0 sai gap | ✅ |
| G9 | Tách bạch 3 vai (F0 trung vị) | mỗi cặp ≥ 4 nửa cung | H–D 7,34 · C–H 8,07 · C–D 15,41 nc (min **7,34 nc**) | ✅ |
| G10 | Nghe mù — mỗi vai ra 1 người | tai người | **CHƯA LÀM** (cần người dùng nghe) | ⏳ |
| G12 | CER mỗi câu | < 2 % | TB 6,72 % · trung vị 5,75 % · **11/12 câu ≥ 2 %** | ❌ |
| — | Nhiễu nền | thấp | RMS 0,3–2,0 s = −17,9 dBFS | ✅ |

**Lưu ý về ngưỡng G12.** Ngưỡng 2 % là ngưỡng *mà kế hoạch TikTok đặt ra* (`KE_HOACH_CLIP_TAP01.md` §9). Thực tế pipeline Higgs tiếng Việt của dự án đang dùng cảnh báo ở **15 %** cho một câu (`.work/generate_higgs_prod_t01vi.py:255`) vì lỗi còn lại phần lớn do ASR đọc sai thanh, không phải do TTS sai. Theo nghĩa đó **chất lượng phát âm của TK1 nằm trong vùng chấp nhận được của pipeline** — nhưng vẫn **không đạt** ngưỡng G12 đã chốt, và có 6 câu có lỗi nghe ra được.

---

## 3. Nhịp đọc và F0 theo vai

| Câu | Vai | Từ | Thời lượng | Từ/s | F0 (Hz) |
|---|---|---:|---:|---:|---:|
| TK1.01#1 | H | 20 | 5,68 | 3,52 | 134,1 |
| TK1.01#2 | H | 20 | 5,48 | 3,65 | 132,4 |
| TK1.01#3 | D | 19 | 4,60 | 4,13 | 83,5 |
| TK1.01#4 | D | 9 | 2,96 | 3,04 | 86,6 |
| TK1.01#5 | D | 19 | 5,32 | 3,57 | 89,1 |
| TK1.01#6 | C | 19 | 4,44 | 4,28 | 213,3 |
| TK1.01#7 | C | 20 | 4,56 | 4,39 | 189,7 |
| TK1.01#8 | C | 24 | 5,72 | 4,20 | 201,7 |
| TK1.01#9 | C | 20 | 4,52 | 4,42 | 222,2 |
| TK1.01#10 | C | 32 | 7,80 | 4,10 | 214,3 |
| TK1.01#11 | C | 18 | 4,24 | 4,25 | 208,7 |
| TK1.01#12 | H | 14 | 5,08 | 2,76 | 119,0 |

- **F0 trung vị:** H = 132,4 Hz (3 câu) · D = 86,6 Hz (3 câu) · C = 211,0 Hz (6 câu).
- **G9:** khoảng cách nhỏ nhất 7,34 nửa cung (H–D) — vượt ngưỡng 4 nc ⇒ 3 vai tách bạch rõ, không cần đổi giọng.
- **Nhịp đọc:** 2,76–4,42 từ/s, trung bình ~3,8 từ/s. Câu chậm nhất là `#12` (2,76 từ/s — câu CTA "Tập một của Amber Eyes…"). Câu này cũng là câu lỗi nhiều nhất, nên khi sinh lại nên tách thành hai câu.
- Câu `#4` chỉ 9 từ / 2,96 s → theo A4.1b ("câu < 12 từ: 1 lỗi = 20 %+ CER") lỗi của câu này bị phóng to, cần tách riêng khi báo cáo.

---

## 4. CER chi tiết — 3 lượt ASR độc lập (A4.1b: ≥ 2 lượt trước khi kết luận)

Ba lượt: **L1** = faster-whisper `small` (beam 5) · **L2** = `small` (beam 5, temperature 0,4) · **L3** = `base` (beam 5, model khác hẳn).
Chuẩn hoá `vi_numbers()` áp cho **cả hai vế** (theo bài học #44 của tiêu chuẩn).

| Câu | Vai | L1 | L2 | L3 | TB | Chênh | Đánh giá |
|---|---|---:|---:|---:|---:|---|---|
| TK1.01#1 | H | 5,68 | 5,68 | 4,55 | 5,30 | ổn | ⚠ nhẹ |
| TK1.01#2 | H | 0,00 | 0,00 | 3,70 | 1,23 | lệch | ✅ ổn (nhiễu ASR) |
| TK1.01#3 | D | 1,16 | 1,16 | 16,28 | 6,20 | lệch | ✅ ổn (nhiễu model base) |
| TK1.01#4 | D | 10,87 | 10,87 | 10,87 | **10,87** | ổn | ❌ lỗi thật |
| TK1.01#5 | D | 9,09 | 6,82 | 12,50 | 9,47 | lệch | ❌ lỗi thật (thanh điệu) |
| TK1.01#6 | C | 4,00 | 4,00 | 6,67 | 4,89 | ổn | ⚠ nhẹ (sai thanh "tách") |
| TK1.01#7 | C | 4,82 | 4,82 | 6,02 | 5,22 | ổn | ❌ lỗi thật |
| TK1.01#8 | C | 0,00 | 0,00 | 1,01 | 0,34 | ổn | ✅ |
| TK1.01#9 | C | 8,97 | 10,26 | 10,26 | **9,83** | ổn | ❌ lỗi thật |
| TK1.01#10 | C | 8,45 | 8,45 | 12,68 | 9,86 | lệch | ❌ lỗi thật |
| TK1.01#11 | C | 0,00 | 0,00 | 3,95 | 1,32 | lệch | ✅ ổn (nhiễu ASR) |
| TK1.01#12 | H | 12,50 | 14,29 | 21,43 | **16,07** | lệch | ❌ lỗi thật |

**TB 3 lượt: 6,72 % · trung vị 5,75 % · cả clip: 11/12 câu ≥ 2 % (trừ #8).**

### 4.1 Bản chép từng câu (lượt L1 — `small`) và chẩn đoán

| Câu | ASR nghe được | Chẩn đoán |
|---|---|---|
| #1 | "Sau 48 giờ truy **tiệm**, cô ấy bước vào phòng **thẳng vấn** bằng đôi chân của chính mình." | thanh điệu sai ở "tìm" và "thẩm" — lỗi thật nhưng nhẹ, người nghe vẫn hiểu |
| #2 | khớp 100 % | ✅ |
| #3 | "…toàn bộ nhận thức của chúng tôi **sắp** đổ." | "sập"→"sắp": sai thanh nhẹ |
| #4 | "**IPC** Rose Blanchard, không hề ngồi trên xe **lăng**." | tên riêng bị ASR nghe sai (lỗi ASR) **+ "lăn"→"lăng"** (sai thanh, lỗi thật) |
| #5 | "**Tụ ta** tự bước đi **vẫn trải** bằng chính đôi chân của mình, **phòng thái** hoàn toàn bình thường." | "Cô ta"→"Tụ ta", "vững chãi"→"vẫn trải", "phong thái"→"phòng thái" — sai thanh rõ |
| #6 | "…tâm lý học tội phạm **tắt làm 2** khái niệm…" | "tách"→"tắt" (sai thanh) |
| #7 | "**Cũ đoạn** là những gì kẻ phạm tội làm để thực hiện hành vi và **nế** tránh sự trừng phạt." | "Thủ"→"Cũ"/"Ủu" (âm đầu bị nuốt), "né"→"nế" (sai thanh) |
| #8 | khớp 100 % | ✅ |
| #9 | "**ưu ký** tâm lý thì bất biến, sinh ra để thỏa mãn **dù cầu** cảm xúc bệnh lý cốt **lợi**." | "Chữ" bị nuốt thành "ưu", "nhu cầu"→"dù cầu", "lõi"→"lợi" — lỗi thật |
| #10 | "**của bà ta** là **tức đoạt** tuổi trưởng thành: **khai mang** ngày sinh, biến cô con gái **20** tuổi thành một đứa trẻ **16** tuổi…" | "Chữ ký"→"của bà ta" (2 từ bị nuốt!), "tước"→"tức", "khai man"→"khai mang" — lỗi thật |
| #11 | khớp 100 % | ✅ |
| #12 | "**Một** của Amber **Ice**, xem **hỗ sơ** đầy đủ ở link trong bio." | "Tập một"→"Một" (chữ "Tập" bị nuốt), "Amber Eyes"→"Amber Ice" (tên thương hiệu bị sai), "hồ sơ"→"hỗ sơ" — lỗi thật, nghe rõ |

---

## 5. Lỗi cần xử lý và cách xử lý

> Không tự sinh lại audio: máy dựng hiện tại **không có GPU** ⇒ không chạy được Higgs Audio v3 (`QUY_TAC_AUDIO_HIGGS.md` §PHẠM VI). Người dùng sinh lại trên Kaggle.

| Ưu tiên | Câu | Vấn đề | Cách xử lý đề xuất |
|---|---|---|---|
| **P0** | #9, #10 | Vai C nuốt âm đầu "**Chữ** ký" ("ưu ký", "từ ký", "của bà ta") | Sinh lại 2 câu này bằng **giọng mẫu C khác** (`C2_AB05` / `C2_LE02` / `C2_LE03` — cùng bộ `.work/kaggle_higgs/dataset_voxcpm2/`), giữ nguyên lời đọc. Nếu vẫn lỗi: dùng thẻ emotion/speed khác cho câu. **Không tự đổi từ "chữ ký"** — thuật ngữ này có nguồn (Flasterstein 2007, `nguon_tham_khao.md`). |
| **P0** | #12 | "Tập" bị nuốt + tên thương hiệu "Amber **Ice**" | Sinh lại; cách chắc ăn: tách thành 2 câu — "Tập một." / "Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio." — và để **khoảng nghỉ 0,4 s** sau "Tập một". |
| **P1** | #7 | "Thủ đoạn"→"Ủu/Cũ đoạn" | Sinh lại bằng seed khác (bộ C dùng seed 42 hoặc 7 theo bài học #54) hoặc giọng C khác. |
| **P1** | #5 | "Cô ta"/"vững chãi"/"phong thái" sai thanh (vai D) | Sinh lại với seed khác cho vai D (`D3_SH`), hoặc chấp nhận — nghe vẫn hiểu. |
| **P2** | #4 | "lăn"→"lăng"; "Gypsy" bị ASR nghe sai | "Gypsy Rose Blanchard" là **tên riêng người thật** — kiểm tra cách đọc khi sinh (tiếng Việt: "Gypsy Rose Blanchard", không phiên âm). Có thể giữ nguyên vì lỗi chính là của ASR. |
| **P2** | #1, #3, #6 | Sai thanh nhẹ ("tìm"→"tiệm", "sập"→"sắp", "tách"→"tắt") | Không bắt buộc sửa; người nghe bình thường vẫn hiểu. Có thể giữ. |

**Đề xuất cho người dùng:** nghe 6 câu P0/P1 (`#4, #5, #7, #9, #10, #12`) một lượt trước khi quyết định sinh lại. Nếu nghe thấy rõ → sinh lại theo bảng trên, giữ nguyên `timeline_tk1.json` (các mốc thời gian sẽ lệch, cần chạy lại `.work/_qc_tk1_audio.py` + `.work/_qc_tk1_cer.py`).

---

## 6. Cổng chưa kiểm được

| Cổng | Vì sao chưa | Cách làm |
|---|---|---|
| **G10** (nghe mù, mỗi vai 1 người) | Cần tai người | Ghép 12 câu của từng vai thành 3 file ngắn, nghe phải ra đúng 1 giọng |
| **G8** (mỗi giọng có bộ tham số an toàn) | Cần nghe | Kiểm câu #11 (emotion `sad`) so với #8/#9 (neutral) của vai C: cùng một người, không đổi giới/tim |
| **Đo lại LUFS/true peak trên mp4 cuối** | Chưa có mp4 | Sau khi dựng video, đo lại trên file mp4 (A7) |
| **ASR chuẩn của dự án** (`connector__matrix__listen_audio`) | Tốn credit MiniMax ⇒ cần người dùng duyệt trước (L4) | Nếu muốn đối chiếu chuẩn dự án, chạy 12 câu qua MiniMax listen |

---

## 7. Bài học (L6)

**BẪY ĐO — truyền mảng numpy 48 kHz cho faster-whisper khiến CER báo 72–104 %, tưởng audio hỏng.**
`faster-whisper` 1.2.1 **không có tham số `sampling_rate`**; khi `transcribe()` nhận `numpy.ndarray`, nó **giả định audio đã là 16 kHz**. Truyền mảng đọc từ file 48 kHz ⇒ tiếng bị chậm 3×, cao độ hạ, ASR ra toàn văn bản vô nghĩa ("Hãy subscribe cho kênh Ghiền Mì Gõ") và CER 70–100 %. Người đọc báo cáo dễ kết luận sai "audio không đọc được".

- **Cách đúng:** cắt từng câu ra **file WAV 16 kHz mono** (ffmpeg) rồi đọc file đó bằng `wave` → truyền mảng đã đúng tần số. Hoặc truyền đường dẫn file (nhưng cách này chết với `PyAV` quá cũ: `av.container.core.open() got an unexpected keyword argument 'metadata_errors'` trên Python 3.14 + `av` cũ).
- **Dấu hiệu nhận biết:** ASR tự nhận diện ngôn ngữ là `en`/`ja`/`la` với xác suất thấp, và bản chép lặp lại cụm vô nghĩa ⇒ **lỗi đường truyền audio, không phải lỗi TTS**.
- **Bài học thứ hai:** ASR **không tất định** — cùng một câu cho CER 0,00 % ở `small` và 16,28 % ở `base` ⇒ mọi kết luận về 1 câu phải có **≥ 2 lượt ASR độc lập** (đúng chuẩn A4.1b).

---

## 8. File liên quan & cách tái lập

| File | Vai trò |
|---|---|
| `02_SAN_XUAT/TIKTOK/Tap01/TK1_master_audio.wav` | audio gốc (không sửa) |
| `02_SAN_XUAT/TIKTOK/Tap01/TK1_master_audio.mp3` | bản MP3 upload TikTok |
| `02_SAN_XUAT/TIKTOK/Tap01/timeline_tk1.json` | 12 câu · vai · start/end · pause · text |
| `02_SAN_XUAT/TIKTOK/Tap01/SPEC_AUDIO_CLIP_TAP01.json` | đặc tả audio (nguồn đối chiếu G6) |
| `.work/_qc_tk1_audio.py` | đo hình thức · loudness · khoảng câm · khớp spec · F0/G9 · nhịp đọc |
| `.work/_qc_tk1_cer.py` | đo CER (G12) 1 lượt, chuẩn hoá `vi_numbers()` 2 vế |
| `.work/_qc_tk1_cer_multiround.py` | đo CER 3 lượt ASR độc lập (small ×2 + base) |
| `.work/_qc_tk1_audio_out.txt` | log đo thô của QC tổng |
| `.work/_qc_tk1_cer_rows.json` · `.work/_qc_tk1_cer_multiround.json` | dữ liệu đo dạng máy đọc được |
| `.work/_diag_tk1_audio.py` | chẩn đoán phổ (RMS/crest/flatness/centroid) |

**Tái lập:**

```powershell
py -3 .work\_qc_tk1_audio.py          # QC tổng (nhanh)
py -3 .work\_qc_tk1_cer.py            # CER 1 lượt (~10 phút, CPU)
py -3 .work\_qc_tk1_cer_multiround.py # CER 3 lượt (~20 phút, CPU)
```

**Lưu ý L10:** file `.wav` / `.mp3` là media ⇒ **không commit**. Chỉ commit tài liệu + script + `provenance.json`.
