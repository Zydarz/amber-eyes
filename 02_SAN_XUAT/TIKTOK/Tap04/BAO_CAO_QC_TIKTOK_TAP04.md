# BÁO CÁO DỰNG CLIP TIKTOK — TẬP 04 (VN · EN · JA)

*Ngày: 27/11/2026 · 15 clip 9:16 (5 clip × 3 ngôn ngữ) · có logo kênh theo **H29***
*Kế hoạch: `Tap04/KE_HOACH_CLIP_TAP04.md` · `Tap04_EN/KE_HOACH_CLIP_TAP04_EN.md` · `Tap04_JA/KE_HOACH_CLIP_TAP04_JA.md`*
*Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 4 (Bước 4–7) · Luật logo: `AGENTS.md` H29 · A11 #198, #199*

---

## 1. Tóm tắt

| Hạng mục | Kết quả đo thật |
|---|---|
| Số clip dựng | **15/15** (VN 5 · EN 5 · JA 5) — file `TKn_video.mp4` trong 3 thư mục ngôn ngữ |
| Kết cấu | **1080×1920 · h264 + aac · 30,00 fps** — 15/15 đúng |
| Thời lượng | **68,83 – 88,28 s** (mục tiêu 60–90 s · cổng QC 45–95 s) — 15/15 trong ngưỡng |
| Âm lượng trên mp4 cuối | **−16,4 … −16,0 LUFS** (ngưỡng −16 ± 1) · true peak **−4,4 … −4,0 dBFS** (trần −1,5) — 15/15 đạt |
| Khoảng câm > 0,3 s @ −60 dB | **0** trên cả 15 clip |
| Lệch hình/tiếng | **0,00 s** (video bắt đầu tại 0,000; sai khác ≤ 0,05 s) |
| Giải mã | **0 lỗi** cả 15 file |
| **Logo kênh (H29)** | **15/15 có mặt** — đo bằng cách dựng lại frame gốc và so pixel (mục 4) |
| Chữ trên khung (H26) | **0** — ngoài vùng logo, **0,000–0,001 %** pixel lệch ⇒ không có chữ/overlay nào thêm vào |
| Dung lượng | 21,6 – 31,7 MB/clip (trần 500 MB) |
| **Lỗi còn lại** | **2 lỗi T13 (từ cấm) ở clip VN** · **1 lỗi audio nghiêm trọng ở EN TK2** (mục 5) |

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
| EN | TK2 | 70,90 s | 23,5 | −16,0 | −4,2 | 0 | ✓ | ĐẠT *(nhưng audio lỗi — mục 5)* |
| EN | TK3 | 75,13 s | 26,5 | −16,1 | −4,3 | 0 | ✓ | ĐẠT |
| EN | TK4 | 73,60 s | 25,4 | −16,2 | −4,2 | 0 | ✓ | ĐẠT |
| EN | TK5 | 68,83 s | 21,6 | −16,1 | −4,1 | 0 | ✓ | ĐẠT |
| JA | TK1 | 81,37 s | 31,7 | −16,3 | −4,2 | 0 | ✓ | ĐẠT |
| JA | TK2 | 84,90 s | 30,1 | −16,0 | −4,4 | 0 | ✓ | ĐẠT |
| JA | TK3 | 88,28 s | 31,4 | −16,0 | −4,3 | 0 | ✓ | ĐẠT |
| JA | TK4 | 83,48 s | 28,3 | −16,4 | −4,2 | 0 | ✓ | ĐẠT |
| JA | TK5 | 80,90 s | 26,3 | −16,0 | −4,4 | 0 | ✓ | ĐẠT |

**Tổng: 13/15 clip đạt trọn 14 cổng · 2 clip VN trượt cổng T13 (từ cấm) — lỗi kịch bản, không phải lỗi dựng.**

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

### 5.1. LỖI NGHIÊM TRỌNG — clip EN TK2 thiếu 2 câu, đuôi 14,76 s chỉ có nhạc nền

| Đo được | Số |
|---|---|
| Số câu trong `SPEC_AUDIO_CLIP_TAP04.json` | **11** |
| Số câu thật sự có trong `Tap04_EN/TK2_master_audio.mp3` | **9** |
| Lời dừng ở | **56,14 s** — đúng câu `TK2.01#9` ("…one of the most prolific serial killers in history.") |
| Đuôi file | **70,90 s** ⇒ **14,76 s không có lời**, chỉ có bed nhạc nền (RMS −19,6 … −20,3 dBFS) |
| Câu thiếu | `TK2.01#10` (vai C — *"Through the lens of criminal psychology, Charles Cullen exhibited classic hallmarks of psychological "Objectification" and severe dehumanization."*) · `TK2.01#11` (CTA vai H — *"Episode four of Amber Eyes. Watch the full documentary via the bio link."*) |

**Đã loại trừ:** không phải lỗi render (video đúng 9 shot theo timeline) · không phải lỗi ASR (chạy ASR riêng trên đoạn 54–71 s: chỉ ra đúng câu #9 rồi im) · không phải lỗi splice (các clip EN khác đủ 9/11, 10/10, 9/9 câu).

**Không có bản WAV nào trên máy để vá:** `.work/audio_s_tk_t04_en/` đã bị xoá · WAV câu `2.11#1` của tập chính (`s2_11_01.wav`) không còn · `audio_master_EN_t04.wav` đã bị xoá trong đợt dọn media · output Higgs cũ chỉ còn log, không còn WAV.

**Cách sửa duy nhất đúng chuẩn:** sinh lại 2 câu bằng **Higgs Audio v3** (đúng engine + đúng giọng vai C/H của bộ EN) rồi chèn vào master. Engine này của dự án **chạy trên Kaggle GPU** (hoặc Apple MLX — máy này không có). Tôi **đã dừng theo yêu cầu, không tự chạy tiếp**.

> **Lưu ý:** một kernel Kaggle đã được push **trước** khi có chỉ đạo dừng (`chiduong2026/amber-eyes-higgs-fix-en-tk02-t04-kaggle-gpu` + dataset `chiduong2026/amber-eyes-higgs-fix-en-tk02-t04`). Watcher đã tắt. **Cần hủy kernel đó trên Kaggle UI** nếu không dùng.

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
| 1 | **Nhạc nền không truy vết được** | `SPEC_AUDIO_CLIP_TAP04.json` ghi `bgm: "bgm_ambient_tension.mp3"` — nhưng file **không tồn tại** trong `assets/bgm/` lẫn `.work/` (đã bị xoá). Đối chiếu tương quan envelope với 11 BGM còn lại trong `assets/bgm/`: **không ứng viên nào khớp** (|corr| 0,24–0,44) ⇒ bed là BGM MiniMax đã mất file nguồn | **Vi phạm T9/L7** — không chứng minh được nguồn âm thanh của clip. Cần user xác nhận: bed này có phải BGM MiniMax (đã kiểm tra thương mại) không, và có cho phép đăng TikTok không |
| 2 | **Khoảng nghỉ giữa câu dài hơn spec** | 8 vị trí trên 15 clip có gap 1,6–2,9 s (spec 0,5–0,7 s) | **KHÔNG vi phạm T6**: `silencedetect` cho 0 khoảng câm > 0,3 s @ −60 dB ⇒ các khoảng nghỉ này **có bed nhạc nền**, không phải im lặng. Vẫn ghi ra để user biết |

---

## 6. Việc còn lại (người dùng)

1. **Quyết định về EN TK2** — 3 lựa chọn: (a) cho phép chạy Kaggle Higgs để sinh 2 câu rồi chèn lại + dựng lại clip; (b) dùng 9 câu hiện có (đuôi cắt bớt, mất 2 câu) — **vi phạm G6** (lời đọc phải khớp câu gốc); (c) giữ nguyên và để đuôi 14,76 s trống có nhạc nền — **không đạt chuẩn đăng**.
2. **Quyết định về từ cấm `sát hại`** ở VN TK1/TK3 — có thay câu trong kịch bản (cần duyệt) hay chấp nhận ngoại lệ cho clip TikTok.
3. **Xác nhận nguồn nhạc nền** (mục 5.3 #1).
4. **Hủy kernel Kaggle** đã push (nếu không dùng): `chiduong2026/amber-eyes-higgs-fix-en-tk02-t04-kaggle-gpu`.
5. **Caption/mô tả**: 5 file caption mỗi ngôn ngữ vẫn là placeholder — chưa điền link YouTube Tập 04 (Bước 8 của kế hoạch).
6. **Không commit media** (L10): 15 mp4 + 15 timeline + ảnh QC đều bị `.gitignore` loại — chỉ commit tài liệu + script.

---

## 7. Script đã tạo (`.work/`)

`_audit_tk04_assets.py` (kiểm ảnh nền) · `_tk_asr_timeline_t04.py` (dựng timeline) · `_build_tk_tap04_video_notext.py` (dựng clip + logo H29) · `_audit_audio_tk04.py` (quét audio 15 master) · `_qc_tk_tap04_clip.py` (14 cổng T1–T14 + H26 + H29) · `_qc_tk04_frames/` (khung hình QC)

Báo cáo máy đọc: `.work/_qc_tk04_clip.json` · `.work/_audit_audio_tk04.json`
