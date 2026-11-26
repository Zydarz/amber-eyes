# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 37 — THE BYSTANDER EFFECT (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 5: Social Psychology & Group Dynamics |
| Episode Title (EN) | **Ep. 37: The Bystander Effect** |
| Vietnamese Source Title | Tập 37: Hiệu ứng người ngoài cuộc (Bystander Effect) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap37_hieu_ung_nguoi_ngoai_cuoc_bystander.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap37_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **227 sentences** · **40 elements** (23 turns) · 5 acts · est. ~**48.9 min** |
| Voice Cast Distribution | **Psychologist (Fox)**: 72 sentences · **Host (Owl)**: 57 sentences · **Investigator (Wolf)**: 50 sentences · **Ordinary Person N1 (Sheep)**: 19 sentences · **Ordinary Person N2 (Cat)**: 15 sentences · **Ordinary Person N3 (Street Vox Pop)**: 14 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap37/bg_jobs_tlhtp_tap37.json` — **140 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **227 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap37_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — TIẾNG KÊU CỨU TRONG ĐÊM ĐÔNG NEW YORK (00:00 – 04:45)] (27 sentences)
- **Target Parity:** Exactly **27 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ DÁM LÀ NGƯỜI ĐẦU TIÊN BƯỚC RA?" (04:45 – 10:15)] (61 sentences)
- **Target Parity:** Exactly **61 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC THỰC NGHIỆM, NGHIÊN CỨU HIỆN ĐẠI & SỰ THẬT VỤ ÁN KITTY GENOVESE (10:15 – 19:30)] (79 sentences)
- **Target Parity:** Exactly **79 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI DO DỰ TRƯỚC SỰ NGUY HIỂM? AI CŨNG CÓ NGUY CƠ? (19:30 – 23:30)] (29 sentences)
- **Target Parity:** Exactly **29 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 27:30)] (31 sentences)
- **Target Parity:** Exactly **31 sentences** matching VI sentence IDs.

