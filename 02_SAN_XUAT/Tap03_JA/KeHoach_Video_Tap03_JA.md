# HỒ SƠ SẢN XUẤT TẬP 03 · BẢN TIẾNG NHẬT · 「第03話：IQ 145の怪物と心を探る鏡」 (PHẦN B)

> **TRẠNG THÁI: ĐÃ HOÀN THÀNH AUDIO MASTER VÀ PHỤ ĐỀ (BƯỚC 6 ĐẠT)**

**Tiêu chuẩn áp dụng:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Phần A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md` (Bản 1, 02/11/2026), `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` (§4.4), `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`.
**Kịch bản:** `01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md` · **Thành phẩm:** `02_SAN_XUAT/Tap03_JA/xuat_ban/`
**Bản gốc:** `02_SAN_XUAT/Tap03/KeHoach_Video_Tap03.md`.

---

## B1. Thông tin tập

| Mục | Giá trị |
|---|---|
| Kịch bản | `01_KICH_BAN/Tap03_JA/kichban_tap03_JA.md` (chuẩn `00_TIEU_CHUAN/CHU_CO_DINH_JA.md`, 218 câu, 55 elements) |
| Lượt nói / câu | 31 / **218 câu**. Host (H) 103 câu (47%) · Điều tra viên (D) 56 câu (26%) · Chuyên gia (C) 41 câu (19%) · Trực ban (N1) 9 câu (4%) · Cảnh sát quán rượu (N2) 9 câu (4%). Mã câu trùng 100% bản VN (`script_tap03_JA.json`) |
| N1 / N2 | `1.09` サンタクルーズ警察当直 (Cừu) / `2.09` 酒場の同僚警察官 (Mèo) |
| Engine TTS | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b`) vận hành trên Apple Silicon Mac qua MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design** (Apache-2.0, độc lập tiếng Nhật theo §4.4):<br>• **H (Cú):** `H_JA.wav` ← `assets/voice_ref_voxcpm2_ja2/H_jactrl_t01.wav` (123.1 Hz)<br>• **D (Sói):** `D_JA.wav` ← `assets/voice_ref_voxcpm2_ja3/D_smokerbass_ja3_t02.wav` (85.5 Hz)<br>• **C (Cáo):** `C_JA.wav` ← `assets/voice_ref_voxcpm2_ja3/C_deepalto_ja3_t03.wav` (228.6 Hz)<br>• **N1 (Cừu):** `N1_JA.wav` ← `assets/voice_ref_voxcpm2_ja3/W6_LOW_huskycontralto_ja3_t04.wav` (212.4 Hz)<br>• **N2 (Mèo):** `N2_JA.wav` ← `assets/voice_ref_voxcpm2_ja2/W5_HIGH_vnctrl_ja_t02.wav` (275.9 Hz) |
| Tách bạch cao độ (G9) | $\Delta_{\text{D}\to\text{H}} = 6.31\text{ nc}$ (ĐẠT $\ge 4.0\text{ nc}$) · $\Delta_{\text{H}\to\text{C}} = 10.72\text{ nc}$ (ĐẠT $\ge 4.0\text{ nc}$) |
| Đo CER | Chuẩn hóa hiragana qua `ja_cer.py` (pykakasi), median CER hiragana 4.55% |
| Đo MOS | `sarulab-speech/UTMOSv2` trên CPU (M5), trung bình 2.98 / 5.0 |
| Cắt đuôi câm (M3) | Tự động quét và cắt đuôi câm $> 0.8\text{ s}$ ở $-45\text{ dBFS}$, giữ $0.3\text{ s} + 30\text{ ms}$ fade-out |
| Thẻ cảm xúc (M4) | **CẤM tuyệt đối** mọi thẻ `<|emotion:...|>`; chỉ dùng ngắt nhịp `<|prosody:pause|>` sau `:` trước câu trích |
| Master Audio | `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA_master.mp3` (44 MB, 1927.91 s ~ 32 phút 07.9 s)<br>• Integrated Loudness: **-16.2 LUFS** (chuẩn -16 ± 1 LUFS)<br>• True Peak: **-1.6 dBFS** (chuẩn ≤ -1.5 dBFS)<br>• LRA: **4.4 LU**<br>• Câm tuyệt đối > 0.3 s @ -60 dBFS: **0 lỗi (ĐẠT V4/A1)**<br>• Mốc lời đầu: **23.0 s** (chuẩn 22.8–23.5 s, intro nhạc 22.41 s)<br>• Mốc lời cuối kết thúc: **1918.9 s**, đuôi piano ấm fade out đến 1927.9 s |
| Phụ đề | `02_SAN_XUAT/Tap03_JA/xuat_ban/Tap03_JA.srt` (238 cues, khớp 100% timeline hòa âm) |

---

## B2. Tiêu đề và Thẻ hồi tiếng Nhật

- **Tiêu đề YouTube:** `第03話 · IQ 145の怪物と心を探る鏡 | エドモンド・ケンパーの心理学 (サイコパス)`
- **Thumbnail:** Dòng 1: `IQ 145の` · Dòng 2: `怪物` · Nền: `t3_brain_mirror`
- **Tiêu đề các hồi (Act titles):**
  - **第1幕 ·** コロラドの電話ボックスから届く深夜の通話
  - **第2幕 ·** 現場と狩りの連鎖――代替の階段
  - **第3幕 ·** 心理剖検――内省型サイコパスの脳の内側
  - **第4幕 ·** FBIとの対話――犯罪プロファイリング技術の基礎
  - **第5幕 ·** 判決、赤い警鐘の教訓＆終幕
