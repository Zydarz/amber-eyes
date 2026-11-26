# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 45 — FREEZE & FAWN RESPONSE (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 7: Victimology & Survival Psychology |
| Episode Title (EN) | **Ep. 45: Freeze & Fawn Response** |
| Vietnamese Source Title | Tập 45: Phản ứng Đóng băng & Lấy lòng (Freeze & Fawn Response) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap45_freeze_va_fawn_response.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap45_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **183 sentences** · **37 elements** (20 turns) · 5 acts · est. ~**28.5 min** |
| Voice Cast Distribution | **Host (Owl)**: 78 sentences · **Psychologist (Fox)**: 50 sentences · **Investigator (Wolf)**: 21 sentences · **Ordinary Person N1 (Sheep)**: 15 sentences · **Ordinary Person N2 (Cat)**: 13 sentences · **Ordinary Person N3 (Street Vox Pop)**: 6 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap45/bg_jobs_tlhtp_tap45.json` — **0 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **183 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap45_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 04:30)] (32 sentences)
- **Target Parity:** Exactly **32 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN ĐÃ TỪNG BỊ TÊ LIỆT HOẶC CỐ LẤY LÒNG KẺ BẮT NẠT?" (04:30 – 09:15)] (40 sentences)
- **Target Parity:** Exactly **40 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC POLYVAGAL VỀ 4F & CƠ CHẾ SINH TỒN NGUYÊN THỦY (09:15 – 14:15)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (14:15 – 19:15)] (31 sentences)
- **Target Parity:** Exactly **31 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG — LỜI KẾT SERIES (19:15 – 26:30)] (36 sentences)
- **Target Parity:** Exactly **36 sentences** matching VI sentence IDs.

