# PRODUCTION PLAN · CRIMINAL PSYCHOLOGY SPECIAL EP. — THE CONSCIENCE SWITCH (EN EDITION)

## B1. Episode Metadata

| Field | Details |
|---|---|
| Series | **Criminal Psychology (Special Episode)** — Map of the Dark Zone & Moral Disengagement |
| Episode Title (EN) | **Special Ep.: The Conscience Switch — Can Anyone Turn Off Their Morality?** |
| Vietnamese Source Title | Tập Chuyên Đề: Công Tắc Tắt Lương Tâm — Có Phải Ai Cũng Có Thể Trở Thành Ác Quỷ? |
| Source Script (VI) | `01_KICH_BAN/TamLyHocToiPham/kichban_chuyende_tat_luong_tam.md` |
| Target EN Script | `01_KICH_BAN/TamLyHocToiPham/EN/kichban_chuyende_tat_luong_tam_EN.md` *(pending 1:1 localization)* |
| Script Scale (Parity Target) | **240 sentences** · **41 elements** (27 turns) · 5 acts · est. ~**36.0 min** |
| Voice Cast Distribution | **Psychologist (Fox)**: 95 sentences · **Host (Owl)**: 68 sentences · **Investigator (Wolf)**: 67 sentences · **Ordinary Person (N1/N2)**: 10 sentences |
| Shared Background Assets | `02_SAN_XUAT/TamLyHocToiPham/ChuyenDe_TatLuongTam/bg_jobs_chuyende_tat_luong_tam.json` — **176 image jobs** (shared across VI / EN / JA, 100% text-free per H26) |
| Safety & Visual Rules | **V9** (no graphic violence), **H1** (faceless silhouettes only), **H26** (no on-screen text except T5 stats & endcard) |

---

## B2. EN Production Checklist (Per `AGENTS.md`)

1. [ ] **EN Script Localization (Parity 1:1):** Translate and adapt to broadcast documentary English with exactly **240 sentences** matching VI IDs.
2. [ ] **Acting & Pacing (`A13`):** Create `acting_tlhtp_chuyende_tat_luong_tam_EN.json` and pass `qc_pause_gate.py --pre` (median pause ≥ 0.6 s).
3. [ ] **TTS Generation (`G10/A14`):** Synthesize with EN voice bank (Higgs Audio v3, separated EN reference clips per `QUY_TAC_AUDIO_HIGGS.md` §4.4) and pass `qc_voice_sentence.py`.
4. [ ] **Audio Mastering (`A7/H24`):** Mix to −16 ± 1 LUFS, TP ≤ −1.5 dBFS; pass `qc_voice_gap.py` and `qc_wave_gate.py`.
5. [ ] **Video Render & Packaging (`H9/H14/T15`):** Render stills & master MP4 using shared backgrounds, generate EN `.srt`, update verified chapters & source URLs in `description.txt` (≤ 5,000 chars), export to `xuat_ban/`.

---

## B3. 5-Act Structure (Parity Reference)

- **ACT 1:** Everyday Wake-Up Call — When Conscience Has a Switch (**40 sentences**)
- **ACT 2:** Map of Moral Disengagement — First 4 Masks & The Bernard Madoff Dossier (**58 sentences**)
- **ACT 3:** The 4 Most Brutal Mechanisms — Dehumanization & Compartmentalization (**50 sentences**)
- **ACT 4:** Two Experiments from Hell — Stanford, Milgram & The Existential Question (**51 sentences**)
- **ACT 5:** The Mirror of Reflection & Survival Red Flags (**41 sentences**)
