# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 36 — FOLIE À DEUX — SHARED DELUSION (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 5: Social Psychology & Group Dynamics |
| Episode Title (EN) | **Ep. 36: Folie à Deux — Shared Delusion** |
| Vietnamese Source Title | Tập 36: Hội chứng điên loạn chung (Folie à deux) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap36_folie_a_deux_dien_loan_chung.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap36_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **230 sentences** · **42 elements** (23 turns) · 5 acts · est. ~**53.0 min** |
| Voice Cast Distribution | **Host (Owl)**: 77 sentences · **Psychologist (Fox)**: 55 sentences · **Investigator (Wolf)**: 54 sentences · **Ordinary Person N1 (Sheep)**: 18 sentences · **Ordinary Person N2 (Cat)**: 14 sentences · **Ordinary Person N3 (Street Vox Pop)**: 12 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap36/bg_jobs_tlhtp_tap36.json` — **139 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **230 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap36_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 04:45)] (25 sentences)
- **Target Parity:** Exactly **25 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "SỰ LÂY NHIỄM TÂM LÝ TIÊU CỰC TRONG TÌNH YÊU" (04:45 – 10:15)] (57 sentences)
- **Target Parity:** Exactly **57 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC VỀ FOLIE À DEUX & HAI HỒ SƠ RÚNG ĐỘNG NƯỚC ANH (10:15 – 19:30)] (82 sentences)
- **Target Parity:** Exactly **82 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (19:30 – 23:30)] (33 sentences)
- **Target Parity:** Exactly **33 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (23:30 – 27:30)] (33 sentences)
- **Target Parity:** Exactly **33 sentences** matching VI sentence IDs.

