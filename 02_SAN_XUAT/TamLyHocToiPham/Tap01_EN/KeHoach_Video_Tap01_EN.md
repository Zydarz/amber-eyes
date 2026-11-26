# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 01 — PROJECTION (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 1: Unconscious Defense Mechanisms |
| Episode Title (EN) | **Ep. 01: Projection** |
| Vietnamese Source Title | Tập 01: Phóng chiếu (Projection) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap01_phong_chieu_projection.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap01_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **230 sentences** · **47 elements** (26 turns) · 5 acts · est. ~**42.8 min** |
| Voice Cast Distribution | **Investigator (Wolf)**: 70 sentences · **Psychologist (Fox)**: 68 sentences · **Host (Owl)**: 55 sentences · **Ordinary Person N1 (Sheep)**: 14 sentences · **Ordinary Person N2 (Cat)**: 13 sentences · **Ordinary Person N3 (Street Vox Pop)**: 10 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap01/bg_jobs_tlhtp_tap01.json` — **177 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **230 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap01_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — KHI BẢN NGÃ TỰ ĐÓNG VAI NẠN NHÂN (00:00 – 05:00)] (22 sentences)
- **Target Parity:** Exactly **22 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ BIẾT PHÓNG CHIẾU LÀ GÌ KHÔNG?" (05:00 – 10:30)] (49 sentences)
- **Target Parity:** Exactly **49 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: TỪ CHIẾC GƯƠNG CỦA FREUD ĐẾN HỒ SƠ ÁN ĐẪM MÁU (10:30 – 18:30)] (74 sentences)
- **Target Parity:** Exactly **74 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI RƠI VÀO BẪY? QUỸ ĐẠO LEO THANG VÀ ĐIỂM MÙ XÃ HỘI (18:30 – 23:30)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 28:00)] (41 sentences)
- **Target Parity:** Exactly **41 sentences** matching VI sentence IDs.

