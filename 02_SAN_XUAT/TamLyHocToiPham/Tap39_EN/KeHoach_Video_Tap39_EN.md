# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 39 — SYMBOLIC UNDOING (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 6: Crime Scene Behavior & Offender Profiling |
| Episode Title (EN) | **Ep. 39: Symbolic Undoing** |
| Vietnamese Source Title | Tập 39: Hành vi Hủy bỏ biểu tượng (Undoing) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap39_undoing_huy_bo_bieu_tuong.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap39_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **222 sentences** · **34 elements** (19 turns) · 5 acts · est. ~**36.2 min** |
| Voice Cast Distribution | **Host (Owl)**: 96 sentences · **Psychologist (Fox)**: 54 sentences · **Investigator (Wolf)**: 28 sentences · **Ordinary Person N1 (Sheep)**: 17 sentences · **Ordinary Person N2 (Cat)**: 15 sentences · **Ordinary Person N3 (Street Vox Pop)**: 12 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap39/bg_jobs_tlhtp_tap39.json` — **175 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **222 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap39_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 05:00)] (32 sentences)
- **Target Parity:** Exactly **32 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN ĐÃ TỪNG CỐ GẮNG BÙ ĐẮP MỘT TỔN THƯƠNG KHÔNG THỂ CỨU VÃN?" (05:00 – 10:30)] (52 sentences)
- **Target Parity:** Exactly **52 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC PHÂN TÂM VỀ CƠ CHẾ UNDOING & DẤU VẾT HIỆN TRƯỜNG ÁN MẠNG (10:30 – 16:30)] (60 sentences)
- **Target Parity:** Exactly **60 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (16:30 – 22:00)] (42 sentences)
- **Target Parity:** Exactly **42 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (22:00 – 26:30)] (36 sentences)
- **Target Parity:** Exactly **36 sentences** matching VI sentence IDs.

