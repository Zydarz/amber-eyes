# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 29 — EROTOMANIA (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 4: Personality Disorders & Dark Tetrad Pathology |
| Episode Title (EN) | **Ep. 29: Erotomania** |
| Vietnamese Source Title | Tập 29: Ảo tưởng cuồng yêu (Erotomania) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap29_ao_tuong_cuong_yeu_erotomania.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap29_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **242 sentences** · **42 elements** (29 turns) · 5 acts · est. ~**41.7 min** |
| Voice Cast Distribution | **Host (Owl)**: 105 sentences · **Psychologist (Fox)**: 57 sentences · **Investigator (Wolf)**: 51 sentences · **Ordinary Person N1 (Sheep)**: 14 sentences · **Ordinary Person N2 (Cat)**: 10 sentences · **Ordinary Person N3 (Street Vox Pop)**: 5 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap29/bg_jobs_tlhtp_tap29.json` — **175 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **242 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap29_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — LÁ THƯ TÌNH DƯỚI BÁNH XE TỔNG THỐNG (00:00 – 04:30)] (40 sentences)
- **Target Parity:** Exactly **40 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ TỪNG BỊ ÁM ẢNH BỞI MỘT NGƯỜI BÁM ĐUÔI?" (04:30 – 09:15)] (49 sentences)
- **Target Parity:** Exactly **49 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC VỀ HỘI CHỨNG DE CLÉRAMBAULT & SÁU PHÁT SÚNG CỦA HINCKLEY (09:15 – 14:15)] (58 sentences)
- **Target Parity:** Exactly **58 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI CUỒNG YÊU MỘT BÓNG HÌNH? AI CŨNG CÓ NGUY CƠ? (14:15 – 19:15)] (51 sentences)
- **Target Parity:** Exactly **51 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (19:15 – 25:00)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

