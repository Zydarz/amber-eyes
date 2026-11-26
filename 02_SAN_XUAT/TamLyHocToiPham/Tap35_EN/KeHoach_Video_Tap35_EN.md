# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 35 — OBEDIENCE TO AUTHORITY & GROUPTHINK (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 5: Social Psychology & Group Dynamics |
| Episode Title (EN) | **Ep. 35: Obedience to Authority & Groupthink** |
| Vietnamese Source Title | Tập 35: Tuân phục quyền lực & Tư duy nhóm (Obedience & Groupthink) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap35_tuan_phuc_va_tu_duy_nhom.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap35_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **240 sentences** · **44 elements** (24 turns) · 5 acts · est. ~**52.6 min** |
| Voice Cast Distribution | **Host (Owl)**: 79 sentences · **Psychologist (Fox)**: 67 sentences · **Investigator (Wolf)**: 49 sentences · **Ordinary Person N1 (Sheep)**: 17 sentences · **Ordinary Person N2 (Cat)**: 15 sentences · **Ordinary Person N3 (Street Vox Pop)**: 13 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap35/bg_jobs_tlhtp_tap35.json` — **166 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **240 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap35_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 04:45)] (25 sentences)
- **Target Parity:** Exactly **25 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ DÁM TỪ CHỐI LỆNH CỦA CẤP TRÊN?" (04:45 – 10:15)] (57 sentences)
- **Target Parity:** Exactly **57 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: GIẢI MÃ KHOA HỌC — MILGRAM, ZIMBARDO, TƯ DUY NHÓM & HỒ SƠ THỰC TẾ (10:15 – 19:30)] (87 sentences)
- **Target Parity:** Exactly **87 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (19:30 – 23:30)] (36 sentences)
- **Target Parity:** Exactly **36 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (23:30 – 27:30)] (35 sentences)
- **Target Parity:** Exactly **35 sentences** matching VI sentence IDs.

