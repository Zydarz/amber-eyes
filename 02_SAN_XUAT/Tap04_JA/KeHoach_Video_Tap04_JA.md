# HỒ SƠ SẢN XUẤT TẬP 04 · BẢN TIẾNG NHẬT · 「第04話：死の天使と神のコンプレックス――9つの病院を巡った16年の沈黙の裏にある秘密」

> **TRẠNG THÁI: ĐÃ HOÀN THÀNH AUDIO MASTER VÀ PHỤ ĐỀ (BƯỚC 6 ĐẠT)**

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md` (Bản 1, 02/11/2026), `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` (§4.4), `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`.
**Kịch bản:** `01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md` · **Thành phẩm:** `02_SAN_XUAT/Tap04_JA/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap04/KeHoach_Video_Tap04.md`.

---

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap04_JA/kichban_tap04_JA.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`, 166 câu, 61 elements) |
| Lượt nói / câu | **166 câu**. Host (H) 79 câu (47.6%) · Điều tra viên (D) 44 câu (26.5%) · Chuyên gia (C) 34 câu (20.5%) · Y tá Somerset N1 (Cừu) 4 câu (2.4%) · Y tá ca đêm N2 (Mèo) 5 câu (3.0%). |
| N1 / N2 | `1.07` NỮ Y TÁ SOMERSET (Cừu) / `4.06` Y TÁ CA ĐÊM (Mèo) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) vận hành trên Apple Silicon Mac qua MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (Apache-2.0, độc lập tiếng Nhật theo §4.4):<br>• **H (Cú):** `H_JA.wav` (121.8 Hz)<br>• **D (Sói):** `D_JA.wav` (83.3 Hz)<br>• **C (Cáo):** `C_JA.wav` (227.5 Hz)<br>• **N1 (Cừu):** `N1_JA.wav` (218.2 Hz)<br>• **N2 (Mèo):** `N2_JA.wav` (289.2 Hz) |
| Tách bạch cao độ (G9) | $\Delta_{\text{D}\to\text{H}} = 6.57\text{ nc}$ (ĐẠT $\ge 4.0\text{ nc}$) · $\Delta_{\text{H}\to\text{C}} = 10.81\text{ nc}$ (ĐẠT $\ge 4.0\text{ nc}$) |
| Đo CER | Chuẩn hóa kanji số theo G11 / `ja_cer.py` (pykakasi), tự động chạy Multi-take vòng 2 cho các câu cần tối ưu |
| Đo MOS | `sarulab-speech/UTMOSv2` trên CPU (M5), trung bình **3.00 / 5.0** (min 2.04, max 3.99, ĐẠT $\ge 3.0$) |
| Cắt đuôi câm (M3) | Tự động quét và cắt đuôi câm $> 0.8\text{ s}$ ở $-45\text{ dBFS}$, giữ $0.3\text{ s} + 30\text{ ms}$ fade-out |
| Thẻ cảm xúc (M4) | **CẤM tuyệt đối** mọi thẻ `<|emotion:...|>`; chỉ dùng ngắt nhịp `<|prosody:pause|>` sau `:` trước câu trích |
| Master Audio | `02_SAN_XUAT/Tap04_JA/xuat_ban/Tap04_JA_master.mp3` (36 MB, 1581.8 s ~ 26 phút 21.8 s)<br>• Integrated Loudness: **-16.2 LUFS** (chuẩn -16 ± 1 LUFS)<br>• True Peak: **-1.8 dBFS** (chuẩn ≤ -1.5 dBFS)<br>• LRA: **4.6 LU**<br>• Câm tuyệt đối > 0.3 s @ -60 dBFS: **0 lỗi (ĐẠT V4/A1)**<br>• Mốc lời đầu: **23.0 s** (chuẩn 22.8–23.5 s, intro nhạc 22.41 s)<br>• Mốc lời cuối kết thúc: **1572.8 s**, đuôi piano ấm fade out đến 1581.8 s |
| Phụ đề | `02_SAN_XUAT/Tap04_JA/xuat_ban/Tap04_JA.srt` (188 cues, khớp 100% timeline hòa âm) |

---

## B2. Tiêu đề và Thẻ hồi tiếng Nhật

- **Tiêu đề YouTube:** `第04話 · 死の天使と神のコンプレックス――9つの病院を巡った16年の沈黙の裏にある秘密 | チャールズ・カレンの心理学`
- **Thumbnail:** Dòng 1: `死の天使` · Dòng 2: `16年の沈黙`
- **Tiêu đề các hồi (Act titles):**
  - **第1幕 ·** つかみ――模範の看護師の逆説 (23.0 s – 274.2 s)
  - **第2幕 ·** 歪んだ心理のプロファイル――神のコンプレックスと無力感の補償 (276.2 s – 666.4 s)
  - **第3幕 ·** 道徳的無効化と被害者の人間性の剥奪 (668.4 s – 966.0 s)
  - **第4幕 ·** 捜査官の心理戦と潜入看護師の勇気 (968.0 s – 1277.8 s)
  - **第5幕 ·** 終幕――法廷、制度的沈黙への警鐘、そして終幕 (1279.8 s – 1572.8 s)
