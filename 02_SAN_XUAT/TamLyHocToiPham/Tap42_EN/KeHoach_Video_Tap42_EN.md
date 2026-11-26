# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 42 — HEROSTRATUS SYNDROME & COPYCAT EFFECT (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 6: Crime Scene Behavior & Offender Profiling |
| Episode Title (EN) | **Ep. 42: Herostratus Syndrome & Copycat Effect** |
| Vietnamese Source Title | Tập 42: Hội chứng Herostratus & Hiệu ứng bắt chước (Copycat Effect) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap42_hoi_chung_herostratus_copycat.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap42_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **225 sentences** · **39 elements** (21 turns) · 5 acts · est. ~**40.2 min** |
| Voice Cast Distribution | **Host (Owl)**: 96 sentences · **Psychologist (Fox)**: 53 sentences · **Investigator (Wolf)**: 39 sentences · **Ordinary Person (Vox Pop)**: 37 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap42/bg_jobs_tlhtp_tap42.json` — **0 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **225 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap42_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — NGỌN LỬA CỦA KẺ KHÁT DANH (00:00 – 05:00)] (51 sentences)
- **Target Parity:** Exactly **51 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — KHÁT KHAO NỔI TIẾNG BẰNG MỌI GIÁ (05:00 – 10:00)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC VỀ HIỆU ỨNG WERTHER & SỰ LÂY NHIỄM TRUYỀN THÔNG (10:00 – 16:30)] (59 sentences)
- **Target Parity:** Exactly **59 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: CƠ CHẾ TÂM LÝ SÂU THẲM & CUỘC CHIẾN CHỐNG LÂY NHIỄM (16:30 – 21:30)] (37 sentences)
- **Target Parity:** Exactly **37 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (21:30 – 26:30)] (34 sentences)
- **Target Parity:** Exactly **34 sentences** matching VI sentence IDs.

