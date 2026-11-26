# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 33 — PSYCHOSIS & COMMAND HALLUCINATIONS (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 4: Personality Disorders & Dark Tetrad Pathology |
| Episode Title (EN) | **Ep. 33: Psychosis & Command Hallucinations** |
| Vietnamese Source Title | Tập 33: Loạn thần & Ảo giác ra lệnh (Psychosis & Command Hallucinations) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap33_loan_than_va_hoang_tuong.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap33_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **242 sentences** · **50 elements** (33 turns) · 5 acts · est. ~**36.8 min** |
| Voice Cast Distribution | **Host (Owl)**: 140 sentences · **Psychologist (Fox)**: 53 sentences · **Investigator (Wolf)**: 31 sentences · **Ordinary Person N1 (Sheep)**: 7 sentences · **Ordinary Person N2 (Cat)**: 6 sentences · **Ordinary Person N3 (Street Vox Pop)**: 5 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap33/bg_jobs_tlhtp_tap33.json` — **175 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **242 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap33_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 04:30)] (41 sentences)
- **Target Parity:** Exactly **41 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "RANH GIỚI BỆNH TÂM THẦN VÀ TRÁCH NHIỆM HÌNH SỰ" (04:30 – 09:15)] (48 sentences)
- **Target Parity:** Exactly **48 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC THẦN KINH VỀ LOẠN THẦN & BI KỊCH ANDREA YATES (09:15 – 14:15)] (58 sentences)
- **Target Parity:** Exactly **58 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (14:15 – 19:15)] (50 sentences)
- **Target Parity:** Exactly **50 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (19:15 – 25:30)] (45 sentences)
- **Target Parity:** Exactly **45 sentences** matching VI sentence IDs.

