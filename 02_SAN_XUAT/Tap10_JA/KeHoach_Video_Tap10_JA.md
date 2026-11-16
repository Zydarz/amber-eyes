# PRODUCTION PLAN EPISODE 10 · JAPANESE EDITION · 「ベッド下の木箱」

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`  
**Script:** `01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md` · **Release Target:** `02_SAN_XUAT/Tap10_JA/xuat_ban/`  
**Date:** 2026年11月15日

---

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md` — 52 elements · **240 sentences** |
| Voice Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b` on Apple Silicon Mac MLX) — Voice Reference Set: VoxCPM2 Japanese (`H_JA`, `D_JA`, `C_JA`, `N1_JA`, `N2_JA`). No emotion tags (M4). Pre-encoded (M1). Tail silence trimmed (M3). |
| Master Output | `02_SAN_XUAT/Tap10_JA/xuat_ban/Tap10_JA_master.mp3` (**2293.6 s / ~38分13秒** · **Integrated: -16.2 LUFS** · **True Peak: -1.6 dBFS** · **0 khoảng câm > 0.3 s**) |
| Quality Control (ASR & CER) | **Whisper Base CER:** Mean = **7.89%**, Median = **7.10%** (203/240 sentences > 2%). Target (< 2.0%). |
| Quality Control (Naturalness MOS) | **UTMOSv2 MOS:** Mean = **2.96 / 5.0** (Range: 1.77 – 3.80). Target (>= 3.0 / 5.0). |
| Pitch Separation (Rule G9) | **D (Wolf):** 85.0 Hz · **H (Owl):** 123.4 Hz ($\Delta = +6.46$ nc) · **C (Fox):** 228.6 Hz ($\Delta = +10.67$ nc). |
| Cast Roles | H: Host (Owl) · D: Investigator (Wolf) · C: Psychologist (Fox) · N1: コリーンの友人 (Sheep) · N2: ジャニス・フッカー (Cat) |
| Video Structure | 52 narrative elements across 5 acts · Subtitles: `Tap10_JA.srt` |

---

## B2. Deliverable Files

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap10_JA/xuat_ban/Tap10_JA_master.mp3`](xuat_ban/Tap10_JA_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap10_JA/xuat_ban/Tap10_JA_master.wav`](xuat_ban/Tap10_JA_master.wav)
2. **Timeline & Subtitles:**
   - Timeline: [`.work/timeline_s_JA_t10.json`](../../.work/timeline_s_JA_t10.json) (2293.6 s)
   - Subtitles: [`02_SAN_XUAT/Tap10_JA/xuat_ban/Tap10_JA.srt`](xuat_ban/Tap10_JA.srt) (240 cues)
3. **QC Reports:**
   - Quality report: [`.work/quality_qc_utmos_ep10_ja.json`](../../.work/quality_qc_utmos_ep10_ja.json)
   - Listening verification list: [`02_SAN_XUAT/Tap10_JA/CanNghe_Tap10_JA_higgs.md`](xuat_ban/CanNghe_Tap10_JA_higgs.md)
