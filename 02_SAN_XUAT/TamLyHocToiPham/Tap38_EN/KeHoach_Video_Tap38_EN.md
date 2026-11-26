# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 38 — MODUS OPERANDI VS. SIGNATURE (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 6: Crime Scene Behavior & Offender Profiling |
| Episode Title (EN) | **Ep. 38: Modus Operandi vs. Signature** |
| Vietnamese Source Title | Tập 38: Phương thức gây án vs. Chữ ký (MO vs. Signature) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap38_mo_vs_signature.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap38_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **220 sentences** · **44 elements** (24 turns) · 5 acts · est. ~**49.1 min** |
| Voice Cast Distribution | **Host (Owl)**: 74 sentences · **Psychologist (Fox)**: 52 sentences · **Investigator (Wolf)**: 44 sentences · **Ordinary Person N1 (Sheep)**: 18 sentences · **Ordinary Person N2 (Cat)**: 17 sentences · **Ordinary Person N3 (Street Vox Pop)**: 15 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap38/bg_jobs_tlhtp_tap38.json` — **208 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **220 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap38_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 04:45)] (25 sentences)
- **Target Parity:** Exactly **25 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "THÓI QUEN VÀ CHỮ KÝ TÂM LÝ VÔ THỨC" (04:45 – 10:15)] (63 sentences)
- **Target Parity:** Exactly **63 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC PHÁC HỌA TÂM LÝ FBI & HAI HỒ SƠ KINH ĐIỂN (10:15 – 19:30)] (69 sentences)
- **Target Parity:** Exactly **69 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI BỊ CHI PHỐI BỞI DẤU ẤN HÀNH VI? (19:30 – 23:30)] (32 sentences)
- **Target Parity:** Exactly **32 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (23:30 – 27:30)] (31 sentences)
- **Target Parity:** Exactly **31 sentences** matching VI sentence IDs.

