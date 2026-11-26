# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 44 — LEARNED HELPLESSNESS (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 7: Victimology & Survival Psychology |
| Episode Title (EN) | **Ep. 44: Learned Helplessness** |
| Vietnamese Source Title | Tập 44: Sự bất lực tập nhiễm (Learned Helplessness) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap44_su_bat_luc_tap_nhiem.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap44_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **215 sentences** · **33 elements** (18 turns) · 5 acts · est. ~**35.5 min** |
| Voice Cast Distribution | **Host (Owl)**: 94 sentences · **Psychologist (Fox)**: 47 sentences · **Investigator (Wolf)**: 39 sentences · **Ordinary Person N1 (Sheep)**: 14 sentences · **Ordinary Person N2 (Cat)**: 12 sentences · **Ordinary Person N3 (Street Vox Pop)**: 9 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap44/bg_jobs_tlhtp_tap44.json` — **0 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **215 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap44_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — ĐIỂM NÚT CỦA SỰ THẬT (00:00 – 05:00)] (46 sentences)
- **Target Parity:** Exactly **46 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN ĐÃ TỪNG TỪ BỎ VÌ TIN RẰNG MÌNH KHÔNG THỂ?" (05:00 – 10:30)] (42 sentences)
- **Target Parity:** Exactly **42 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: THÍ NGHIỆM SELIGMAN & 3.096 NGÀY ĐỊA NGỤC CỦA NATASCHA KAMPUSCH (10:30 – 16:30)] (58 sentences)
- **Target Parity:** Exactly **58 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? AI CŨNG CÓ NGUY CƠ? (16:30 – 21:30)] (33 sentences)
- **Target Parity:** Exactly **33 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: CẢNH BÁO ĐỎ SINH TỒN & BÀI HỌC CUỘC SỐNG (21:30 – 27:00)] (36 sentences)
- **Target Parity:** Exactly **36 sentences** matching VI sentence IDs.

