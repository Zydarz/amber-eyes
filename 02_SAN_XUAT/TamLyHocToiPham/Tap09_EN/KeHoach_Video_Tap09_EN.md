# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 09 — MINIMIZATION (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 1: Unconscious Defense Mechanisms |
| Episode Title (EN) | **Ep. 09: Minimization** |
| Vietnamese Source Title | Tập 09: Giảm thiểu hóa (Minimization) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap09_giam_thieu_hoa_minimization.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap09_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **243 sentences** · **37 elements** (23 turns) · 5 acts · est. ~**36.6 min** |
| Voice Cast Distribution | **Host (Owl)**: 93 sentences · **Psychologist (Fox)**: 82 sentences · **Investigator (Wolf)**: 36 sentences · **Ordinary Person N1 (Sheep)**: 12 sentences · **Ordinary Person N2 (Cat)**: 10 sentences · **Ordinary Person N3 (Street Vox Pop)**: 10 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap09/bg_jobs_tlhtp_tap09.json` — **53 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **243 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap09_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — CÂU NÓI DỐI NGUY HIỂM NHẤT THẾ GIAN (40 câu)] (40 sentences)
- **Target Parity:** Exactly **40 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ NGHĨ MÌNH LÀM QUÁ LÊN?" (48 câu)] (49 sentences)
- **Target Parity:** Exactly **49 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: THỦ THUẬT THU NHỎ TỘI LỖI & HỒ SƠ BẠO HÀNH GIA ĐÌNH (58 câu)] (60 sentences)
- **Target Parity:** Exactly **60 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI COI NHẸ NỖI ĐAU CỦA NHAU? AI CŨNG CÓ NGUY CƠ? (50 câu)] (50 sentences)
- **Target Parity:** Exactly **50 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TỔNG KẾT NHÓM 1 & CẢNH BÁO ĐỎ SINH TỒN (44 câu)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

