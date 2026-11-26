# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 20 — HERO / SAVIOR COMPLEX (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 3: Manipulation & Coercive Control |
| Episode Title (EN) | **Ep. 20: Hero / Savior Complex** |
| Vietnamese Source Title | Tập 20: Hội chứng Đấng cứu thế (Hero / Savior Complex) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap20_hoi_chung_dang_cuu_the_hero_complex.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap20_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **244 sentences** · **37 elements** (23 turns) · 5 acts · est. ~**31.6 min** |
| Voice Cast Distribution | **Psychologist (Fox)**: 93 sentences · **Host (Owl)**: 89 sentences · **Investigator (Wolf)**: 31 sentences · **Ordinary Person N1 (Sheep)**: 11 sentences · **Ordinary Person N2 (Cat)**: 10 sentences · **Ordinary Person N3 (Street Vox Pop)**: 10 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap20/bg_jobs_tlhtp_tap20.json` — **40 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **244 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap20_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — KẺ ĐỐT NHÀ ĐỂ LÀM ANH HÙNG CỨU HỎA (40 câu)] (40 sentences)
- **Target Parity:** Exactly **40 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN CÓ TỪNG GẶP KẺ THÍCH ĐÓNG VAI VỊ CỨU TINH?" (48 câu)] (48 sentences)
- **Target Parity:** Exactly **48 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC VỀ ẢO TƯỞNG QUYỀN LỰC & SÁT NHÂN Y TẾ CHARLES CULLEN (58 câu)] (59 sentences)
- **Target Parity:** Exactly **59 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI NGHIỆN LÀM NGƯỜI HÙNG? AI CŨNG CÓ NGUY CƠ? (50 câu)] (53 sentences)
- **Target Parity:** Exactly **53 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (44 câu)] (44 sentences)
- **Target Parity:** Exactly **44 sentences** matching VI sentence IDs.

