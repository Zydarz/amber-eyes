# HỒ SƠ SẢN XUẤT TẬP 23 JA · リチャード・ラミレス事件 (Richard Ramirez)

## B1. Thông tin tập

| Mục | Nội dung |
|---|---|
| Tên tập | **Tập 23 JA: ナイト・ストーカーの戦慄と犯罪者愛好症の深淵 (Richard Ramirez)** |
| Vụ án | Vụ án sát nhân hàng loạt Night Stalker tại California (1984–1989) |
| Chủ đề | Hội chứng say mê tội phạm (Hybristophilia), Dấu ấn Signature vs MO, Tổn thương não bộ & Phân liệt nhận thức |
| Tổng thời lượng | **2560.1 s (~42 分 40 秒)** · 5 幕 · **245 センテンス** |
| Diễn viên / Giọng | Host (フクロウ) · Sói (捜査官) · Cáo (心理専門家) · N1 (東ロサンゼルス住民) · N2 (法廷記者) |
| Engine TTS | **Higgs Audio v3** () on Apple Silicon MLX |
| Bộ giọng mẫu | **VoxCPM2 Voice Design JA** (H_JA, D_JA, C_JA, N1_JA, N2_JA) |
| Âm thanh | Stereo 3 階層: BGM 5 幕 + 環境音 (Ambience) + 効果音 (SFX) |
| Thành phẩm Master |  &  |

---

## B2. Số đo Kiểm soát Chất lượng Audio (QC Metrics)

### 1. Chuẩn hóa Âm lượng (EBUR128 Loudness)
- **Integrated Loudness ($):** **-16.2 LUFS** (基準: 569X16 \pm 1	ext{ LUFS}$ — 合格 ✅)
- **True Peak ($):** **-1.8 dBFS** (基準: $\le -1.5	ext{ dBFS}$ — 合格 ✅)
- **Loudness Range ($):** **4.4 LU**
- **無音区間 ($> 0.3	ext{ s}$ at 569X60	ext{ dBFS}$):** **0 エラー** (合格 ✅ Rule A1 / V4)
- **冒頭音声開始:** 23.0 s (Intro 22.41 s 後 — 合格 ✅)
- **音声終了:** 2551.1 s, 全体長 2560.1 s (フェードアウト完了 — 合格 ✅)

### 2. 音高分離度 & 話者識別 (G9 ルール)
- **Host ($):** F0 中央値 = **123.1 Hz**
- **捜査官 ($):** F0 中央値 = **84.7 Hz**
- **心理専門家 ($):** F0 中央値 = **230.8 Hz**
- **音高差:**
  - $\Delta_{D 	o H} = \mathbf{6.48	ext{ 半音}}$ (基準 $\ge 4.0	ext{ nc}$ — 合格 ✅)
  - $\Delta_{H 	o C} = \mathbf{10.88	ext{ 半音}}$ (基準 $\ge 4.0	ext{ nc}$ — 合格 ✅)

### 3. Whisper Base CER & 自然度 (UTMOSv2 MOS)
- **CER 中央値:** **8.54%** (CER 平均: **8.75%**).
- **Multi-take Vòng 2:** Đã tự động sinh Variant 1 và chọn take tối ưu.
- **UTMOSv2 MOS:** 平均 **2.97 / 5.0** (範囲: 2.19 – 4.19).
- **要確認センテンスリスト:** [](xuat_ban/CanNghe_Tap23_JA_higgs.md).

---

## B3. Danh mục Tệp Thành phẩm

1. **Master Audio:**
   - MP3: [](xuat_ban/Tap23_JA_master.mp3)
   - WAV: [](xuat_ban/Tap23_JA_master.wav)
2. **Dữ liệu Timeline & Phụ đề:**
   - Timeline: [](../../.work/timeline_s_JA_t23.json) (2560.1 s)
   - Phụ đề SRT: [](xuat_ban/Tap23_JA.srt) (245 センテンス)
3. **Báo cáo Giám sát:**
   - Chi tiết QC: [](../../.work/quality_qc_utmos_ep23_ja.json)
   - Bảng câu nghe duyệt: [](xuat_ban/CanNghe_Tap23_JA_higgs.md)
