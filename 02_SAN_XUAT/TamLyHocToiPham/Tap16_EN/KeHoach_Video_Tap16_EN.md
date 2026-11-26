# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 16 — DISPLACEMENT OF RESPONSIBILITY (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 2: Moral Disengagement |
| Episode Title (EN) | **Ep. 16: Displacement of Responsibility** |
| Vietnamese Source Title | Tập 16: Chuyển dịch trách nhiệm (Displacement of Responsibility) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap16_chuyen_dich_trach_nhiem_displacement_of_responsibility.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap16_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **242 sentences** · **37 elements** (23 turns) · 5 acts · est. ~**32.0 min** |
| Voice Cast Distribution | **Psychologist (Fox)**: 91 sentences · **Host (Owl)**: 90 sentences · **Investigator (Wolf)**: 29 sentences · **Ordinary Person N1 (Sheep)**: 12 sentences · **Ordinary Person N2 (Cat)**: 10 sentences · **Ordinary Person N3 (Street Vox Pop)**: 10 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap16/bg_jobs_tlhtp_tap16.json` — **41 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **242 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap16_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — LỜI BÀO CHỮA PHỔ BIẾN NHẤT LỊCH SỬ (40 câu)] (40 sentences)
- **Target Parity:** Exactly **40 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ TỪNG LÀM ĐIỀU SAI VÌ BỊ ÉP BUỘC?" (48 câu)] (49 sentences)
- **Target Parity:** Exactly **49 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: THÍ NGHIỆM STANLEY MILGRAM & BẢN ÁN ADOLF EICHMANN (58 câu)] (59 sentences)
- **Target Parity:** Exactly **59 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI SỢ BẤT TUÂN? AI TRONG CHÚNG TA CŨNG CÓ NGUY CƠ? (50 câu)] (50 sentences)
- **Target Parity:** Exactly **50 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (44 câu)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

