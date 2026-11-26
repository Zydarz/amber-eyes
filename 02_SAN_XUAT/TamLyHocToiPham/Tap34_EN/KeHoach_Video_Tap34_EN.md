# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 34 — DEINDIVIDUATION (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 5: Social Psychology & Group Dynamics |
| Episode Title (EN) | **Ep. 34: Deindividuation** |
| Vietnamese Source Title | Tập 34: Phi cá nhân hóa (Deindividuation) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap34_phi_ca_nhan_hoa_deindividuation.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap34_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **243 sentences** · **49 elements** (32 turns) · 5 acts · est. ~**35.4 min** |
| Voice Cast Distribution | **Host (Owl)**: 146 sentences · **Psychologist (Fox)**: 42 sentences · **Investigator (Wolf)**: 37 sentences · **Ordinary Person N1 (Sheep)**: 7 sentences · **Ordinary Person N2 (Cat)**: 7 sentences · **Ordinary Person N3 (Street Vox Pop)**: 4 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap34/bg_jobs_tlhtp_tap34.json` — **175 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **243 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap34_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 04:30)] (41 sentences)
- **Target Parity:** Exactly **41 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ DÁM LÀM ĐIỀU ÁC KHI KHÔNG AI BIẾT MÌNH LÀ AI?" (04:30 – 09:15)] (48 sentences)
- **Target Parity:** Exactly **48 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC VỀ DEINDIVIDUATION & HAI THẢM ÁN ĐÁM ĐÔNG (09:15 – 14:15)] (59 sentences)
- **Target Parity:** Exactly **59 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (14:15 – 19:15)] (51 sentences)
- **Target Parity:** Exactly **51 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (19:15 – 25:30)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

