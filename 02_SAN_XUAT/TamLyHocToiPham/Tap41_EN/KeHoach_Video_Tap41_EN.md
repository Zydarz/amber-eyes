# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 41 — TROPHIES & COOLING-OFF PERIOD (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 6: Crime Scene Behavior & Offender Profiling |
| Episode Title (EN) | **Ep. 41: Trophies & Cooling-Off Period** |
| Vietnamese Source Title | Tập 41: Chiến lợi phẩm & Thời gian nguội (Trophies & Cooling-off Period) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap41_chien_loi_pham_va_cooling_off.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap41_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **178 sentences** · **35 elements** (19 turns) · 5 acts · est. ~**35.5 min** |
| Voice Cast Distribution | **Host (Owl)**: 79 sentences · **Investigator (Wolf)**: 35 sentences · **Psychologist (Fox)**: 32 sentences · **Ordinary Person N3 (Street Vox Pop)**: 12 sentences · **Ordinary Person N1 (Sheep)**: 11 sentences · **Ordinary Person N2 (Cat)**: 9 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap41/bg_jobs_tlhtp_tap41.json` — **0 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **178 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap41_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 06:00)] (43 sentences)
- **Target Parity:** Exactly **43 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "KỶ VẬT VÀ NHU CẦU NEO GIỮ CẢM XÚC" (06:00 – 12:00)] (40 sentences)
- **Target Parity:** Exactly **40 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC PHÁC HỌA TÂM LÝ VỀ CHU KỲ SÁT NHÂN & HỒ SƠ JEFFREY DAHMER (12:00 – 20:00)] (46 sentences)
- **Target Parity:** Exactly **46 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (20:00 – 25:30)] (25 sentences)
- **Target Parity:** Exactly **25 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (25:30 – 30:00)] (24 sentences)
- **Target Parity:** Exactly **24 sentences** matching VI sentence IDs.

