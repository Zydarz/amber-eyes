# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 05 — DISPLACEMENT (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 1: Unconscious Defense Mechanisms |
| Episode Title (EN) | **Ep. 05: Displacement** |
| Vietnamese Source Title | Tập 05: Chuyển dịch (Displacement) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap05_chuyen_dich_displacement.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap05_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **215 sentences** · **43 elements** (24 turns) · 5 acts · est. ~**37.6 min** |
| Voice Cast Distribution | **Host (Owl)**: 62 sentences · **Psychologist (Fox)**: 59 sentences · **Investigator (Wolf)**: 55 sentences · **Ordinary Person N1 (Sheep)**: 15 sentences · **Ordinary Person N2 (Cat)**: 13 sentences · **Ordinary Person N3 (Street Vox Pop)**: 11 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap05/bg_jobs_tlhtp_tap05.json` — **162 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **215 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap05_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — CƠN GIẬN TÌM KẺ YẾU THẾ (00:00 – 05:00)] (27 sentences)
- **Target Parity:** Exactly **27 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN ĐÃ TRÚT GIẬN LÊN AI?" (05:00 – 10:30)] (53 sentences)
- **Target Parity:** Exactly **53 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: GÂY HẤN CHUYỂN DỊCH & THẢM KỊCH LUBY'S CAFETERIA NĂM 1991 (10:30 – 18:30)] (58 sentences)
- **Target Parity:** Exactly **58 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: QUY LUẬT DÒNG CHẢY NĂNG LƯỢNG & KẺ BẠO CHÚA SAU CÁNH CỬA (18:30 – 23:30)] (35 sentences)
- **Target Parity:** Exactly **35 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 28:00)] (42 sentences)
- **Target Parity:** Exactly **42 sentences** matching VI sentence IDs.

