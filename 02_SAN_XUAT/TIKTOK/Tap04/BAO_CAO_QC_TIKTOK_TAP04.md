# BÁO CÁO DỰNG CLIP TIKTOK — TẬP 04 (VN · EN · JA)

*Ngày: 27/11/2026 (cập nhật lần 2 — sau khi **trộn lại master EN TK2**) · 15 clip 9:16 (5 clip × 3 ngôn ngữ) · có logo kênh theo **H29***
*Kế hoạch: `Tap04/KE_HOACH_CLIP_TAP04.md` · `Tap04_EN/KE_HOACH_CLIP_TAP04_EN.md` · `Tap04_JA/KE_HOACH_CLIP_TAP04_JA.md`*
*Quy trình chung: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` mục 4 (Bước 4–7) · Luật logo: `AGENTS.md` H29 · A11 #198, #199, #200, **#201** · Luật audio: `AGENTS.md` **H30, H31***

---

## 1. Tóm tắt

| Hạng mục | Kết quả đo thật |
|---|---|
| Số clip dựng | **15/15** (VN 5 · EN 5 · JA 5) — file `TKn_video.mp4` trong 3 thư mục ngôn ngữ |
| Kết cấu | **1080×1920 · h264 + aac · 30,00 fps** — 15/15 đúng |
| Thời lượng | **68,83 – 88,28 s** (mục tiêu 60–90 s · cổng QC 45–95 s) — 15/15 trong ngưỡng |
| Âm lượng trên mp4 cuối | **−16,4 … −16,0 LUFS** (ngưỡng −16 ± 1) — **15/15 đạt** · true peak **−4,5 … −4,0 dBFS** (trần −1,5) — **15/15 đạt** |
| Khoảng câm > 0,3 s @ −60 dB | **0** trên cả **15/15 clip** (kể cả EN TK2 sau khi trộn lại master) |
| Lệch hình/tiếng | **0,00 s** (video bắt đầu tại 0,000; sai khác ≤ 0,05 s) |
| Giải mã | **0 lỗi** cả 15 file |
| **Logo kênh (H29)** | **15/15 có mặt** — đo bằng cách dựng lại frame gốc và so pixel (mục 4) |
| Chữ trên khung (H26) | **0** — ngoài vùng logo, **0,000–0,001 %** pixel lệch ⇒ không có chữ/overlay nào thêm vào |
| Dung lượng | 21,6 – 31,7 MB/clip (trần 500 MB) |
| **Lỗi còn lại** | **2 lỗi T13 (từ cấm) ở clip VN** (lỗi kịch bản, cần duyệt) · **T9/L7: nguồn nhạc nền của 14 clip còn lại không truy vết được** (mục 5.3) — EN TK2 **đã hết lỗi audio** |

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
| EN | TK2 | 72,34 s | 25,6 | −16,3 | −4,5 | 0 | ✓ | **ĐẠT** (đã trộn lại master 27/11 — mục 5.1) |
| EN | TK3 | 75,13 s | 26,5 | −16,1 | −4,3 | 0 | ✓ | ĐẠT |
| EN | TK4 | 73,60 s | 25,4 | −16,2 | −4,2 | 0 | ✓ | ĐẠT |
| EN | TK5 | 68,83 s | 21,6 | −16,1 | −4,1 | 0 | ✓ | ĐẠT |
| JA | TK1 | 81,37 s | 31,7 | −16,3 | −4,2 | 0 | ✓ | ĐẠT |
| JA | TK2 | 84,90 s | 30,1 | −16,0 | −4,4 | 0 | ✓ | ĐẠT |
| JA | TK3 | 88,28 s | 31,4 | −16,0 | −4,3 | 0 | ✓ | ĐẠT |
| JA | TK4 | 83,48 s | 28,3 | −16,4 | −4,2 | 0 | ✓ | ĐẠT |
| JA | TK5 | 80,90 s | 26,3 | −16,0 | −4,4 | 0 | ✓ | ĐẠT |

**Tổng: 13/15 clip đạt trọn 14 cổng · 2 clip VN trượt cổng T13 (từ cấm `sát hại` — lỗi có sẵn trong kịch bản, cần người dùng duyệt) · EN TK2 đã hết lỗi audio sau khi trộn lại master.**

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

### 5.1. EN TK2 — ĐÃ TRỘN LẠI MASTER (27/11) · hết lỗi T6 + true peak

**Bối cảnh 2 vòng:** (1) bản cũ báo "thiếu 2 câu"; (2) master mới 27/11 của người dùng có **đủ 11/11 câu** nhưng **không có nhạc nền** ⇒ 11 khoảng câm + true peak vượt trần. Người dùng đã **cho phép trộn lại master** ⇒ đã trộn theo đúng công thức của dự án và dựng lại clip.

| Bước | Kết quả đo thật |
|---|---|
| Nguyên nhân "thiếu 2 câu" | **Không phải audio thiếu.** `faster-whisper` transcribe **cả file** 72,34 s chỉ trả về tới **57,72 s** ⇒ 2 câu cuối bị ghi "NOI SUY". ASR riêng đuôi (58,2–72,3 s) ⇒ **nhận đủ**; ASR riêng đuôi **WAV cũ 70,90 s** ⇒ **cũng đủ 11 câu** ⇒ *không phiên bản nào thiếu câu*. Giải mã `s16le` cắt sớm hơn `f32le` ⇒ lỗi ở **cách đọc file dài** |
| Cách sửa ASR | **Cửa sổ 20,5 s** (overlap 4 s, cửa sổ cuối neo vào cuối file) + khử trùng (text, mốc) < 0,6 s ⇒ **11/11 câu khớp 100 %**, `asr_end` 72,00/72,34 s |
| Vì sao phải trộn lại | Master mới: **nền im lặng −70,6 dB**, **8,1 % file là im lặng tuyệt đối** (14 clip khác: 0,00 % / −16…−17 dB) ⇒ **không có bed nhạc nền** ⇒ 11 khoảng câm > 0,3 s (**trượt T6**) · peak **+1,25 dBFS**, **312 mẫu > 0 dBFS** (**vượt trần A7**) |
| Công thức trộn (giống Tập 03) | voice + BGM `bgm_ambient_deep.mp3` **ducking** (−24 dB khi nói / −16 dB khi nghỉ, smooth 0,2 s) + **ambience phòng kín −42 dB** ⇒ đạt A1/V4 · fade cuối 0,8 s · **loudnorm 2 lượt** I −16 / TP −1,5 / LRA 11 |
| Headroom (bắt buộc) | voice hạ về peak **−6 dBFS**, raw mix về **−3 dBFS** trước khi ghi WAV 16-bit. Nếu không: WAV clip cứng ⇒ `measured_TP` sai ⇒ **loudnorm cho kết quả sai** (đo được: peak +19,49 dBFS ⇒ TP **−12,11 dBFS** thay vì −4,5) |
| **Master sau khi trộn** | **72,34 s · 0 khoảng câm > 0,3 s @ −60 dB · 0 mẫu > 0 dBFS · peak −1,47 dBFS · I −16,0 LUFS · TP −4,48 dBFS** — đạt trọn |
| Clip sau khi dựng lại | `Tap04_EN/TK2_video.mp4` — 72,34 s · 1080×1920 · h264+aac @30,00 · **0 lỗi giải mã** · 11 shot đúng nền · logo (684, 60) · **QC 14 cổng ĐẠT** |
| Phủ đuôi 15 clip | `timeline_end` cách `speech_end` (RMS > −45 dBFS) **0,10 – 1,06 s** ⇒ **15/15 phủ đủ đuôi** |

**Một bài học phát sinh lúc trộn (đã ghi A11 #201 + H31):** chạy ASR trên **master đã trộn BGM** ⇒ **9/11 dòng lỗi** (2 `NOI SUY`, 6 `MATCH YEU`, `asr_end` 68,48/72,34 s) dù audio hoàn toàn đúng ⇒ nghi nhầm "sai timeline". Chạy lại trên **voice stem** (file giọng thuần, lưu riêng `TK2_voice_stem.mp3`) ⇒ **11/11 câu khớp 100 %**. Vì trộn không dịch/lùi voice ⇒ **mốc thời gian không đổi**, chỉ cần trỏ ASR sang stem.

**Chọn BGM:** SPEC yêu cầu `bgm_jazz_noir.mp3` — **file không còn trên đĩa** (đã xoá ở đợt dọn media). Chọn `bgm_ambient_deep.mp3`: có trên đĩa + có dòng provenance đầy đủ (MiniMax) + **là bed mà clip TK2 của Tập 03 cũng dùng** (tiền lệ trong dự án) + tông noir hợp Act 1. ⇒ **EN TK2 có nguồn nhạc nền truy vết được** (khác 14 clip còn lại — mục 5.3).

**Còn lại:** master gốc + WAV cũ lưu ở `.work/_cu/entk2_master_premix_20261127_1517/` (không xoá).
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
| 1 | **Nhạc nền không truy vết được (14/15 clip)** | `SPEC_AUDIO_CLIP_TAP04.json` ghi `bgm_ambient_tension.mp3` (TK1) / `bgm_jazz_noir.mp3` (TK2) / `bgm_sub_drone.mp3` (TK3) / `bgm_ambient_deep.mp3` (TK4) / `bgm_piano_warm.mp3` (TK5) — **`bgm_ambient_tension.mp3` và `bgm_jazz_noir.mp3` KHÔNG còn trên đĩa** (đã bị xoá ở đợt dọn media). Đối chiếu 3 cách (tương quan envelope · tương quan envelope toàn bộ khoảng nghi · **cross-correlation sóng thô** có bù lag) với 11 BGM còn lại trong `assets/bgm/`: **không ứng viên nào khớp** (\|corr\| tối đa 0,72 ở cổng khác, 0,02–0,20 ở đúng clip) ⇒ bed là BGM MiniMax đã mất file nguồn. **EN TK2 (TK2.01) đã dùng lại `bgm_ambient_deep.mp3` ⇒ nguồn truy vết được** | **Vi phạm T9/L7** cho 14 clip còn lại — không chứng minh được nguồn âm thanh. Cần user xác nhận: bed là BGM MiniMax (đã kiểm tra thương mại) không, và có cho phép đăng TikTok không |
| 2 | **Khoảng nghỉ giữa câu dài hơn spec** | 8 vị trí trên 14 clip (không tính EN TK2) có gap 1,6–2,9 s (spec 0,5–0,7 s) | **KHÔNG vi phạm T6**: `silencedetect` cho 0 khoảng câm > 0,3 s @ −60 dB ⇒ các khoảng nghỉ này **có bed nhạc nền**, không phải im lặng. Vẫn ghi ra để user biết |

---

## 6. Quyết định của người dùng (27/11/2026) + việc còn lại

### 6.1. Ba quyết định đã chốt

| # | Việc | Quyết định của người dùng | Hệ quả cho AI |
|---|---|---|---|
| 1 | **Từ cấm `sát hại` ở VN TK1/TK3** (cổng T13 trượt) | **Người dùng sẽ tự duyệt kịch bản** | AI **KHÔNG tự sửa kịch bản** (L2/L4). Khi người dùng đổi câu ⇒ phải **chạy lại TTS cho câu đó** (engine Higgs Audio v3 của dự án chỉ chạy trên Kaggle GPU/Apple MLX — máy này không có) ⇒ phải chạy lại ASR + timeline + render + QC cho clip bị ảnh hưởng |
| 2 | **Nguồn nhạc nền 14 clip còn lại** (T9/L7 — bed đã mất file nguồn) | **Người dùng sẽ xác nhận** | Chờ xác nhận. **EN TK2 đã tách riêng**: dùng `bgm_ambient_deep.mp3` (có trên đĩa + có dòng provenance đầy đủ) ⇒ EN TK2 **không còn** vướng T9/L7 |
| 3 | **Kernel Kaggle đã push** (`chiduong2026/amber-eyes-higgs-fix-en-tk02-t04-kaggle-gpu` + dataset `...-t04`) | **GIỮ, KHÔNG HỦY** | Không gọi API Kaggle để hủy. Kernel này **không còn cần thiết** vì EN TK2 đã vá xong bằng cách trộn lại master (không cần sinh lại TTS) — nhưng người dùng chọn giữ. AI **không push/không chạy** kernel đó |

> Ghi nhận cho lượt sau: quyết định "giữ kernel" **không** có nghĩa cho phép chạy/push Kaggle. Lệnh đang có hiệu lực vẫn là **dừng kết nối Kaggle** — chỉ được phép hủy khi có yêu cầu riêng, và chưa có yêu cầu đó.

### 6.2. Việc còn lại

1. **EN TK2 — ĐÃ XONG** (trộn lại master + dựng lại clip + QC 14 cổng **ĐẠT**). Xác nhận nhỏ còn treo: `bgm_ambient_deep.mp3` (MiniMax) có được phép dùng cho TikTok không — **người dùng sẽ xác nhận cùng lượt với #2**.
2. **VN TK1 / TK3** — chờ người dùng duyệt kịch bản (xem 6.1 #1).
3. **14 clip còn lại** — chờ người dùng xác nhận nguồn nhạc nền (xem 6.1 #2).
4. **Kernel Kaggle** — giữ, không hủy (xem 6.1 #3). Dataset `chiduong2026/amber-eyes-higgs-fix-en-tk02-t04` cũng giữ.
5. **Caption/mô tả**: 5 file caption mỗi ngôn ngữ vẫn là placeholder — chưa điền link YouTube Tập 04 (Bước 8 của kế hoạch).
6. **Không commit media** (L10): 15 mp4 + 15 timeline + ảnh QC đều bị `.gitignore` loại — chỉ commit tài liệu + script.

---
## 7. Script đã tạo (`.work/`)

`_audit_tk04_assets.py` (kiểm ảnh nền) · `_tk_asr_timeline_t04.py` (dựng timeline — **ASR cửa sổ + đọc mp3 + `--audio` trỏ voice stem**, A11 #200/#201) · `_build_tk_tap04_video_notext.py` (dựng clip + logo H29) · `_remix_entk2.py` (**trộn lại master**: voice + BGM ducking + ambience + loudnorm 2 lượt) · `_audit_audio_tk04.py` (quét audio 15 master) · `_qc_tk_tap04_clip.py` (14 cổng T1–T14 + H26 + H29) · `_check_tail_coverage.py` (kiểm phủ đuôi 15 clip) · `_clip_scan.py` (đếm mẫu clip) · `_silence_scan_mp3.py` (đếm khoảng câm) · `_identify_bed.py` / `_match_bed_full.py` / `_match_bed_wave.py` (truy vết bed) · `_qc_tk04_frames/` (khung hình QC)

Báo cáo máy đọc: `.work/_qc_tk04_clip.json` · `.work/_audit_audio_tk04.json`
