# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY EP. 04 — INTELLECTUALIZATION (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (45 Episodes)** — Group 1: Unconscious Defense Mechanisms |
| Episode Title (EN) | **Ep. 04: Intellectualization** |
| Vietnamese Source Title | Tập 04: Trí tuệ hóa (Intellectualization) |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_tap04_tri_tue_hoa_intellectualization.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_tap04_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **208 sentences** · **41 elements** (23 turns) · 5 acts · est. ~**38.9 min** |
| Voice Cast Distribution | **Host (Owl)**: 62 sentences · **Investigator (Wolf)**: 59 sentences · **Psychologist (Fox)**: 56 sentences · **Ordinary Person N1 (Sheep)**: 13 sentences · **Ordinary Person N2 (Cat)**: 10 sentences · **Ordinary Person N3 (Street Vox Pop)**: 8 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/Tap04/bg_jobs_tlhtp_tap04.json` — **167 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **208 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_tap04_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

### ACT 1: [EN TITLE PENDING — VI Ref: THE HOOK — KHI TRÁI TIM ĐƯỢC THAY BẰNG THƯỚC ĐO (00:00 – 05:00)] (31 sentences)
- **Target Parity:** Exactly **31 sentences** matching VI sentence IDs.

### ACT 2: [EN TITLE PENDING — VI Ref: TIẾNG NÓI TỪ ĐƯỜNG PHỐ — "BẠN DÙNG LÝ TRÍ ĐỂ TRỐN TRÁNH ĐIỀU GÌ?" (05:00 – 10:30)] (43 sentences)
- **Target Parity:** Exactly **43 sentences** matching VI sentence IDs.

### ACT 3: [EN TITLE PENDING — VI Ref: SỰ TÁCH RỜI CẢM XÚC & VỤ ÁN THẾ KỶ LEOPOLD VÀ LOEB (10:30 – 18:30)] (62 sentences)
- **Target Parity:** Exactly **62 sentences** matching VI sentence IDs.

### ACT 4: [EN TITLE PENDING — VI Ref: XÃ HỘI DUY LÝ & NGUY CƠ VÔ CẢM CỦA CON NGƯỜI HIỆN ĐẠI (18:30 – 23:30)] (36 sentences)
- **Target Parity:** Exactly **36 sentences** matching VI sentence IDs.

### ACT 5: [EN TITLE PENDING — VI Ref: TẤM GƯƠNG PHẢN CHIẾU & CẢNH BÁO ĐỎ SINH TỒN (23:30 – 28:00)] (36 sentences)
- **Target Parity:** Exactly **36 sentences** matching VI sentence IDs.

