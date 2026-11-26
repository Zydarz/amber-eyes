# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 40 — CRIME SCENE STAGING (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 6: Crime Scene Behavior & Offender Profiling |
| Episode Title (EN) | **Ep. 40: Crime Scene Staging** |
| Vietnamese Source Title | Tập 40: Dàn dựng hiện trường (Staging) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap40_staging_dan_dung_hien_truong.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap40_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **243 sentences** · **30 elements** (18 turns) · 5 acts · est. ~**37.4 min** |
| Voice Cast Distribution | **Host (Owl)**: 112 sentences · **Psychologist (Fox)**: 56 sentences · **Investigator (Wolf)**: 41 sentences · **Ordinary Person N1 (Sheep)**: 14 sentences · **Ordinary Person N2 (Cat)**: 11 sentences · **Ordinary Person N3 (Street Vox Pop)**: 9 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap40/bg_jobs_tlhtp_tap40.json` — **175 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **243 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap40_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (44 câu)] (45 sentences)
- **Target Parity:** Exactly **45 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN ĐÃ TỪNG DỰNG CHUYỆN ĐỂ CHE ĐẬY LỖI LẦM?" (46 câu)] (46 sentences)
- **Target Parity:** Exactly **46 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC PHÁC HỌA TÂM LÝ VỀ STAGING & KỸ THUẬT BÓC TRẦN CỦA ĐIỀU TRA VIÊN (58 câu)] (59 sentences)
- **Target Parity:** Exactly **59 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (46 câu)] (46 sentences)
- **Target Parity:** Exactly **46 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (46 câu)] (47 sentences)
- **Target Parity:** Exactly **47 sentences** matching VI sentence IDs.

