# BÁO CÁO DỰNG CLIP TIKTOK — TẬP 04 (VN · EN · JA)

*Ngày: 27/11/2026 (cập nhật sau khi dựng lại EN TK2) · 15 clip 9:16 (5 clip × 3 ngôn ngữ) · có logo kênh theo **H29***
*Kế hoạch: `Tap04/KE_HOACH_CLIP_TAP04.md` · `Tap04_EN/KE_HOACH_CLIP_TAP04_EN.md` · `Tap04_JA/KE_HOACH_CLIP_TAP04_JA.md`*
*Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 4 (Bước 4–7) · Luật logo: `AGENTS.md` H29 · A11 #198, #199, **#200** (ASR cửa sổ + nguồn mp3)*

---

## 1. Tóm tắt

| Hạng mục | Kết quả đo thật |
|---|---|
| Số clip dựng | **15/15** (VN 5 · EN 5 · JA 5) — file `TKn_video.mp4` trong 3 thư mục ngôn ngữ |
| Kết cấu | **1080×1920 · h264 + aac · 30,00 fps** — 15/15 đúng |
| Thời lượng | **68,83 – 88,28 s** (mục tiêu 60–90 s · cổng QC 45–95 s) — 15/15 trong ngưỡng |
| Âm lượng trên mp4 cuối | **−16,4 … −16,0 LUFS** (ngưỡng −16 ± 1) — 15/15 đạt · true peak **−4,4 … −1,8 dBFS** (trần −1,5) — **14/15 đạt, EN TK2 trượt** |
| Khoảng câm > 0,3 s @ −60 dB | **0** trên 14 clip · **11 khoảng** trên EN TK2 (master mới không có nhạc nền — mục 5.1) |
| Lệch hình/tiếng | **0,00 s** (video bắt đầu tại 0,000; sai khác ≤ 0,05 s) |
| Giải mã | **0 lỗi** cả 15 file |
| **Logo kênh (H29)** | **15/15 có mặt** — đo bằng cách dựng lại frame gốc và so pixel (mục 4) |
| Chữ trên khung (H26) | **0** — ngoài vùng logo, **0,000–0,001 %** pixel lệch ⇒ không có chữ/overlay nào thêm vào |
| Dung lượng | 21,6 – 31,7 MB/clip (trần 500 MB) |
| **Lỗi còn lại** | **2 lỗi T13 (từ cấm) ở clip VN** · **1 lỗi T6 (khoảng câm) + true peak vượt trần ở EN TK2** (mục 5.1) · từ cấm + BGM (mục 5.2, 5.3) |

**Tiền cảnh:** 23 nền dọc `assets/bg/tk04_*.png` (23/23 tồn tại, đúng 1080×1920, đủ 48/48 shot × 3 ngôn ngữ) — báo cáo nền: `BAO_CAO_ANH_NEN_DOC_TAP04.md`.

---

## 2. Quy trình đã chạy (tái lập được)

| Bước | Lệnh | Kết quả |
|---|---|---|
| 1 | `py -3 .work/_audit_tk04_assets.py` | 23/23 nền tồn tại · 48/48 shot × 3 ngôn ngữ · 3 spec khớp kế hoạch · provenance 23/23 |
| 2 | `py -3 .work/_tk_asr_timeline_t04.py --lang VN\|EN\|JA --write` | Dựng **15 `timeline_tkN.json`** bằng ASR (faster-whisper small) + Needleman–Wunsch. VN 0 dòng lỗi · EN 2 dòng lỗi (xem mục 5) · JA 5 dòng match yếu nhưng **đều có mốc thật** (JA căn theo ký tự) |
| 3 | `py -3 .work/_build_tk_tap04_video_notext.py <VN\|EN\|JA>` | Dựng **15 mp4** — nền dọc gốc + camera `still/push/pull/pan` + master audio sẵn có + **logo H29** |
| 4 | `py -3 .work/_audit_audio_tk04.py` | Quét audio 15 master (mục 5) |
| 5 | `py -3 .work/_qc_tk_tap04_clip.py VN EN JA` | **14 cổng T1–T14 + H26 + H29** trên 15 clip (mục 3) |

> **Vì sao phải chạy ASR lại:** WAV từng câu của clip TikTok (`audio_s_tk_t04_*`) **đã bị xoá** trong đợt dọn media ⇒ không còn manifest/mốc thời gian ⇒ dựng lại từ master audio bằng ASR + căn Needleman–Wunsch (đúng cách Tập 03 đã làm).

---

## 3. Bảng kết quả đo 15 clip

| Ngôn ngữ | Clip | Thời lượng | MB | LUFS | TP dBFS | Câm | Logo | **Kết quả 14 cổng** |
|---|---|---:|---:|---:|---:|---:|---|---|
| VN | TK1 | 70,53 s | 27,0 | −16,1 | −4,2 | 0 | ✓ | **TRƯỢT T13** (`sát hại`) |
| VN | TK2 | 81,10 s | 29,1 | −16,0 | −4,4 | 0 | ✓ | ĐẠT |
| VN | TK3 | 87,77 s | 30,6 | −16,0 | −4,4 | 0 | ✓ | **TRƯỢT T13** (`sát hại`) |
| VN | TK4 | 72,24 s | 25,2 | −16,1 | −4,2 | 0 | ✓ | ĐẠT |
| VN | TK5 | 79,27 s | 27,2 | −16,0 | −4,3 | 0 | ✓ | ĐẠT |
| EN | TK1 | 70,68 s | 29,6 | −16,3 | −4,0 | 0 | ✓ | ĐẠT |
| EN | TK2 | 72,34 s | 25,6 | −16,3 | **−1,8** | **11** | ✓ | **TRƯỢT T6** (11 khoảng câm) — audio mới (mục 5.1) |
| EN | TK3 | 75,13 s | 26,5 | −16,1 | −4,3 | 0 | ✓ | ĐẠT |
| EN | TK4 | 73,60 s | 25,4 | −16,2 | −4,2 | 0 | ✓ | ĐẠT |
| EN | TK5 | 68,83 s | 21,6 | −16,1 | −4,1 | 0 | ✓ | ĐẠT |
| JA | TK1 | 81,37 s | 31,7 | −16,3 | −4,2 | 0 | ✓ | ĐẠT |
| JA | TK2 | 84,90 s | 30,1 | −16,0 | −4,4 | 0 | ✓ | ĐẠT |
| JA | TK3 | 88,28 s | 31,4 | −16,0 | −4,3 | 0 | ✓ | ĐẠT |
| JA | TK4 | 83,48 s | 28,3 | −16,4 | −4,2 | 0 | ✓ | ĐẠT |
| JA | TK5 | 80,90 s | 26,3 | −16,0 | −4,4 | 0 | ✓ | ĐẠT |

**Tổng: 12/15 clip đạt trọn 14 cổng · 2 clip VN trượt cổng T13 (từ cấm) · 1 clip EN TK2 trượt cổng T6 (khoảng câm, do master audio mới) — lỗi kịch bản/audio, không phải lỗi dựng.**

### 3.1. Hai cổng N/A (có lý do, không phải bỏ qua)

| Cổng | Trạng thái | Lý do |
|---|---|---|
| **T14** hook bằng chữ trong 3 s đầu | **N/A** | H26 (20/11/2026) **cấm chữ chèn lên khung**; clip TikTok dạng nền-thuần không có hook chữ (đúng tiền lệ Tập 03). Cổng bị H26 vô hiệu hoá. |
| **T12** không có mặt người thật | **N/A (kế thừa)** | Nền `tk04_*` đã qua QC soi mắt 100 % ngày 21/11 (`BAO_CAO_ANH_NEN_DOC_TAP04.md` §5: 0 khuôn mặt lộ, 0 chữ đọc được). Clip chỉ ghép nền ⇒ không thêm mặt nào. **Không soi lại bằng mắt trong đợt này.** |

---

## 4. Bằng chứng logo (H29) — đo bằng pixel, không phải "nhìn thấy"

Cách đo (script `.work/_qc_tk_tap04_clip.py`): với mỗi clip lấy **7 khung** rải đều trong clip → dựng lại **ảnh nền gốc** đúng công thức camera của renderer (`camera_box` + `camera.push/pull/pan/still`) → ghép lại logo → so từng pixel với khung thật.

| Đại lượng | Kết quả 15 clip | Kết luận |
|---|---|---|
| Sai số **ngoài** vùng logo: tỷ lệ pixel lệch > 40/255 | **0,000 – 0,001 %** | Khung hình khớp nền **tuyệt đối** ⇒ **không có chữ/overlay/subtitle nào** bị thêm vào (chứng minh H26 + T10 + T11) |
| Sai số **trong** vùng logo so với nền-không-logo | **max 84 – 96/255** | Logo **thật sự có mặt** với độ mờ đúng (pixel sáng của logo lệch rõ) |
| Sai số **trong** vùng logo so với nền-có-logo | **mean 3,6 – 4,3** | Logo khớp **đúng** file `watermark.png` 96 px · alpha 89 (35 %) — sai số nằm trong nhiễu nén H.264 + hạt phim 35 mm |
| Logo nằm trong safe zone T6 | **15/15** | x 684–780 · y 60–156 |

**Vị trí logo trên khung dọc 9:16 — và vì sao KHÔNG dùng "góc dưới-phải" của khung 16:9:**

`build_video3.py` đặt watermark tại `(W−128, H−120)` ⇒ trên 1080×1920 ra **x 952–1048, y 1800–1896**. Nhưng trên TikTok: cột nút hành động bên phải phủ **x ≈ 940–1060, y ≈ 1060–1690**, khối caption/tên kênh phủ **y > ≈ 1520** ⇒ logo nằm trọn trong UI, **người xem không thấy**. Vì vậy đặt ở **góc trên-phải trong safe zone T6 (x 684–780, y 60–156)** — đúng `KE_HOACH_TIKTOK.md` mục 4 Bước 5 ("logo góc phải trên … tránh x > 780") và đúng tiền lệ clip Tap 01 (logo x 120–260, y 60–160). Đổi vị trí = sửa 1 dòng hằng `WM_POS` trong `.work/_build_tk_tap04_video_notext.py`. → Đã ghi vào **A11 #198** và cập nhật luật **H29**.

> **H24 (dải sóng âm thanh trên badge vai) KHÔNG áp cho clip này** — clip TikTok dạng nền-thuần không có nhân vật, không có badge vai. Chỉ áp cho video có badge vai (video chính 16:9).

---

## 5. VẤN ĐỀ AUDIO — 3 nhóm, đều gửi lại người dùng (không tự sửa)

### 5.1. EN TK2 — ĐÃ DỰNG LẠI (master mới 27/11) · còn 1 lỗi T6 + true peak vượt trần

**Bối cảnh:** bản cũ báo "thiếu 2 câu". Người dùng đã tạo lại `Tap04_EN/TK2_master_audio.mp3` (27/11/2026, 14:04) — **72,34 s** (bản cũ 70,90 s). Đo lại toàn bộ:

| Đo được | Kết quả |
|---|---|
| Số câu trong `SPEC_AUDIO_CLIP_TAP04.json` | **11** |
| Số câu thật sự có trong master mới | **11/11** — ASR căn cửa sổ 20,5 s: `#1`–`#10` khớp **100 %**, `#11` khớp **12/13 (92,3 %)** |
| Timeline dựng lại | `timeline_tk2.json` — **0 dòng NOI SUY, 0 dòng MATCH YEU**; `asr_end` 72,00 / audio 72,34 s |
| Clip render lại | `Tap04_EN/TK2_video.mp4` — 72,34 s · 1080×1920 · h264+aac @30,00 · **0 lỗi giải mã** · 11 shot đúng nền · logo (684, 60) |

**Nguyên nhân thật của lỗi "thiếu 2 câu" (không phải audio thiếu):**

| Kiểm chứng | Kết quả |
|---|---|
| ASR **cả file** mp3 mới (72,34 s) | chỉ trả về tới **57,72 s** ⇒ 2 câu cuối bị ghi "NOI SUY" |
| ASR **riêng đoạn đuôi** (58,2–72,3 s) | **nhận đủ cả 2 câu**, 100 % khớp |
| ASR **riêng đuôi WAV cũ** (50,9–70,9 s) | **nhận đủ cả 2 câu**: *"Through the lens of criminal psychology…"* 56,90–62,32 s và *"Episode 4 of Amber Eyes…"* 65,88–70,06 s ⇒ **bản WAV cũ CŨNG ĐỦ 11 câu** |
| Giải mã `s16le` vs `f32le` | `s16le` ⇒ whisper dừng ở **57,72 s**; `f32le` ⇒ tới 67,22 s (vẫn mất câu cuối) ⇒ lỗi ở **cách đọc file dài** |
| Cửa sổ 20,5 s (overlap 4 s, cửa sổ cuối neo vào cuối file) | **11/11 câu, asr_end 72,00/72,34 s** ⇒ cách sửa |

⇒ **Không phiên bản nào thiếu câu nào.** Lỗi là ASR bỏ đuôi file dài + builder đọc `.wav` (24/11) trong khi renderer đọc `.mp3` (27/11). Đã ghi **A11 #200** và sửa builder: đọc `.mp3` (đúng file renderer dùng), ASR theo cửa sổ, giải mã `f32le`, in cảnh báo khi wav/mp3 lệch > 0,05 s.

**Phủ đuôi kiểm cho cả 15 clip** (`.work/_check_tail_coverage.py`): `timeline_end` cách `speech_end` (RMS > −45 dBFS) **0,10 – 1,06 s** ⇒ **15/15 phủ đủ đuôi**, không clip nào khác bị mất câu.

**Lỗi CÒN LẠI trên master mới — cần người dùng quyết:**

| # | Lỗi | Đo được | Cổng vi phạm |
|---|---|---|---|
| 1 | **11 khoảng câm > 0,3 s** | 0,316 – 0,843 s tại 1,93 · 4,30 · 6,12 · 9,66 · 20,30 · 28,58 · 36,57 · 42,58 · 48,54 · 58,30 · 67,41 s | **T6 trượt** (cổng này đạt ở 14 clip còn lại) |
| 2 | **True peak vượt trần** | **+1,25 dBFS** (trần −1,5) · **312 mẫu > 0 dBFS** rải rác 29 đoạn · 380 mẫu > −0,1 dBFS | **A7 / trần TP** |
| 3 | **Master mới KHÔNG có nhạc nền** | nền im lặng trung bình **−70,6 dB** (14 clip khác: −16,2…−17,2 dB) · **8,1 % file là im lặng tuyệt đối** (peak < −100 dBFS; 14 clip khác: **0,00 %**) | Gốc rễ của lỗi #1 |
| 4 | **WAV cũ còn trên đĩa** | `TK2_master_audio.wav` = 70,90 s (24/11) — **lệch 1,44 s** với mp3 | Không ảnh hưởng dựng (builder đã đọc mp3) nhưng dễ nhầm |

**Vì sao không tự sửa:** (a) thêm nhạc nền / hạ đỉnh = **sửa audio** ⇒ cần người dùng duyệt; (b) `bgm_ambient_tension.mp3` **không còn trên đĩa** (mục 5.3) ⇒ không có nguồn để trộn; (c) WAV là file của người dùng.

**Cách khắc phục (đề xuất, chờ duyệt):** trộn lại nhạc nền có sẵn + `alimiter` (A11 #38: `limit=0.7943:attack=5:release=50:level=disabled:latency=1`) để peak ≤ −1,5 dBFS ⇒ xoá được cả 11 khoảng câm lẫn lỗi TP. Cần người dùng: **(1)** xác nhận nguồn nhạc nền được phép dùng, **(2)** cho phép trộn/ghi lại `TK2_master_audio.mp3`, **(3)** cho phép tạo lại `.wav` từ mp3 để hai bản đồng bộ.
### 5.2. LỖI NỘI DUNG — từ cấm A9.2 trong 2 clip VN

Cổng T13 quét từng clip theo danh sách A9.2 (`máu` ngoại trừ "ung thư máu", `thi thể`, `sát hại`, `đòn`, `trói`, `bầm`, `đập`, `đầu độc`, `diệt cỏ`, `bỏ đói`, `móc áo`…):

| Clip | Câu | Từ bị cấm | Nguyên văn |
|---|---|---|---|
| **VN TK1** | `TK1.01#6` | `sát hại` | "Tại bệnh viện Somerset, hắn mất hoàn toàn khả năng kiềm chế, **sát hại** cả những bệnh nhân trẻ tuổi đang bình phục khỏe mạnh." |
| **VN TK3** | `TK3.01#9` | `sát hại` | "Hắn thừa nhận đã dùng Digoxin và Insulin **sát hại** linh mục Florian Gall, bệnh nhân Michael Strenko và hàng chục nạn nhân khác qua nhiều năm." |

**Đây là lỗi có sẵn trong kịch bản, không phải lỗi dựng:** cụm từ nằm sẵn trong kịch bản tập chính `01_KICH_BAN/Ho_So_Toi_Pham/Tap04/kichban_tap04_23102026.md` (dòng 80 · 121 · 123 · 287) ⇒ clip TikTok chỉ thừa hưởng. Sửa cần đổi **kịch bản** ⇒ phải có người dùng duyệt (L2/L4), **AI không tự đổi**.

### 5.3. HAI ĐIỂM NHỎ — cần người dùng xác nhận (không vi phạm cổng nào)

| # | Vấn đề | Đo được | Ảnh hưởng |
|---|---|---|---|
| 1 | **Nhạc nền không truy vết được** | `SPEC_AUDIO_CLIP_TAP04.json` ghi `bgm: "bgm_ambient_tension.mp3"` — nhưng file **không tồn tại** trong `assets/bgm/` lẫn `.work/` (đã bị xoá). Đối chiếu tương quan envelope với 11 BGM còn lại trong `assets/bgm/`: **không ứng viên nào khớp** (\|corr\| 0,24–0,44) ⇒ bed là BGM MiniMax đã mất file nguồn. **Thêm 27/11:** master mới của EN TK2 **không có bed nhạc nền nào cả** (nền −70,6 dB, 8,1 % file im lặng tuyệt đối) ⇒ không phải "bed khác" mà là **thiếu bed** | **Vi phạm T9/L7** — không chứng minh được nguồn âm thanh của clip. Cần user xác nhận: bed này có phải BGM MiniMax (đã kiểm tra thương mại) không, và có cho phép đăng TikTok không |
| 2 | **Khoảng nghỉ giữa câu dài hơn spec** | 8 vị trí trên 14 clip (không tính EN TK2) có gap 1,6–2,9 s (spec 0,5–0,7 s) | **KHÔNG vi phạm T6**: `silencedetect` cho 0 khoảng câm > 0,3 s @ −60 dB ⇒ các khoảng nghỉ này **có bed nhạc nền**, không phải im lặng. Vẫn ghi ra để user biết |

---

## 6. Việc còn lại (người dùng)

1. **EN TK2 — đã dựng lại xong** (11/11 câu, 0 lỗi giải mã). Còn 2 lỗi audio trên master mới (mục 5.1): **11 khoảng câm > 0,3 s (T6)** + **true peak +1,25 dBFS (vượt trần)** — gốc rễ: master mới **không có nhạc nền**. Cần người dùng: xác nhận nguồn nhạc nền + cho phép trộn lại/hạ đỉnh master + cho phép tạo lại `.wav` từ mp3.
2. **Quyết định về từ cấm `sát hại`** ở VN TK1/TK3 — có thay câu trong kịch bản (cần duyệt) hay chấp nhận ngoại lệ cho clip TikTok.
3. **Xác nhận nguồn nhạc nền** (mục 5.3 #1).
4. **Hủy kernel Kaggle** đã push (nếu không dùng): `chiduong2026/amber-eyes-higgs-fix-en-tk02-t04-kaggle-gpu`.
5. **Caption/mô tả**: 5 file caption mỗi ngôn ngữ vẫn là placeholder — chưa điền link YouTube Tập 04 (Bước 8 của kế hoạch).
6. **Không commit media** (L10): 15 mp4 + 15 timeline + ảnh QC đều bị `.gitignore` loại — chỉ commit tài liệu + script.

---

## 7. Script đã tạo (`.work/`)

`_audit_tk04_assets.py` (kiểm ảnh nền) · `_tk_asr_timeline_t04.py` (dựng timeline — **đã đổi sang ASR cửa sổ + đọc mp3**, A11 #200) · `_build_tk_tap04_video_notext.py` (dựng clip + logo H29) · `_audit_audio_tk04.py` (quét audio 15 master) · `_qc_tk_tap04_clip.py` (14 cổng T1–T14 + H26 + H29) · `_check_tail_coverage.py` (kiểm phủ đuôi 15 clip) · `_clip_scan.py` (đếm mẫu clip) · `_silence_scan_mp3.py` (đếm khoảng câm) · `_qc_tk04_frames/` (khung hình QC)

Báo cáo máy đọc: `.work/_qc_tk04_clip.json` · `.work/_audit_audio_tk04.json`
