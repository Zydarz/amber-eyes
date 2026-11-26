# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 10 — DEHUMANIZATION (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 2: Moral Disengagement |
| Episode Title (EN) | **Ep. 10: Dehumanization** |
| Vietnamese Source Title | Tập 10: Phi nhân hóa (Dehumanization) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap10_phi_nhan_hoa_dehumanization.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap10_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **242 sentences** · **37 elements** (23 turns) · 5 acts · est. ~**36.1 min** |
| Voice Cast Distribution | **Host (Owl)**: 92 sentences · **Psychologist (Fox)**: 82 sentences · **Investigator (Wolf)**: 36 sentences · **Ordinary Person N1 (Sheep)**: 12 sentences · **Ordinary Person N2 (Cat)**: 10 sentences · **Ordinary Person N3 (Street Vox Pop)**: 10 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap10/bg_jobs_tlhtp_tap10.json` — **49 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **242 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap10_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — BƯỚC ĐẦU TIÊN CỦA MỌI TỘI ÁC DIỆT CHỦNG (40 câu)] (40 sentences)
- **Target Parity:** Exactly **40 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ COI NGƯỜI KHÁC LÀ CON NGƯỜI?" (48 câu)] (49 sentences)
- **Target Parity:** Exactly **49 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC NÃO BỘ VỀ SỰ VÔ CẢM & HỒ SƠ SÁT NHÂN MẪU VẬT (58 câu)] (59 sentences)
- **Target Parity:** Exactly **59 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI DỄ PHI NHÂN HÓA NHAU? AI CŨNG CÓ NGUY CƠ? (50 câu)] (50 sentences)
- **Target Parity:** Exactly **50 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (44 câu)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

