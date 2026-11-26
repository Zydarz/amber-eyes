# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 43 — STOCKHOLM SYNDROME (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 7: Victimology & Survival Psychology |
| Episode Title (EN) | **Ep. 43: Stockholm Syndrome** |
| Vietnamese Source Title | Tập 43: Hội chứng Stockholm (Stockholm Syndrome) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap43_hoi_chung_stockholm.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap43_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **242 sentences** · **28 elements** (17 turns) · 5 acts · est. ~**37.1 min** |
| Voice Cast Distribution | **Host (Owl)**: 85 sentences · **Psychologist (Fox)**: 68 sentences · **Investigator (Wolf)**: 49 sentences · **Ordinary Person N2 (Cat)**: 14 sentences · **Ordinary Person N3 (Street Vox Pop)**: 14 sentences · **Ordinary Person N1 (Sheep)**: 12 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap43/bg_jobs_tlhtp_tap43.json` — **175 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **242 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap43_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — KHI NẠN NHÂN ĐỨNG RA BẢO VỆ KẺ BẮT CÓC] (59 sentences)
- **Target Parity:** Exactly **59 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — BẠN CÓ THỂ YÊU KẺ ĐANG DÍ SÚNG VÀO ĐẦU MÌNH?] (49 sentences)
- **Target Parity:** Exactly **49 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: KHOA HỌC SINH TỒN VÔ THỨC & SÁU NGÀY CÂN NÃO TẠI NORRMALMSTORG] (73 sentences)
- **Target Parity:** Exactly **73 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: VÌ SAO CON NGƯỜI DỄ THÔNG CẢM VỚI KẺ ÁP BỨC?] (38 sentences)
- **Target Parity:** Exactly **38 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN] (23 sentences)
- **Target Parity:** Exactly **23 sentences** matching VI sentence IDs.

