# PRODUCTION PLAN EPISODE 12 · ENGLISH EDITION · "THE JONESTOWN TRAGEDY"

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`  
**Script:** `01_KICH_BAN/Tap12_EN/kichban_tap12_EN.md` · **Release Target:** `02_SAN_XUAT/Tap12_EN/xuat_ban/`  
**Date:** November 14, 2026

---

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap12_EN/kichban_tap12_EN.md` — 53 elements · **249 sentences** |
| Voice Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b` on Apple Silicon Mac MLX) — Voice Reference Set: VoxCPM2 English (`H_EN`, `D_EN`, `C_EN`, `N1_EN`, `N2_EN`). No emotion tags (M4). Pre-encoded (M1). Tail silence trimmed (M3). |
| Master Output | `02_SAN_XUAT/Tap12_EN/xuat_ban/Tap12_EN_master.mp3` (**2080.5 s / ~34 min 40 s** · **Integrated: -16.2 LUFS** · **True Peak: -1.7 dBFS** · **0 silences > 0.3 s**) |
| Quality Control (ASR & CER) | **Whisper Base CER:** Mean = **0.44%**, Median = **0.00%** (16/249 sentences > 2%). Target (< 2.0%). |
| Quality Control (Naturalness MOS) | **UTMOSv2 MOS:** Mean = **3.49 / 5.0** (Range: 2.33 – 4.16). Target (>= 3.0 / 5.0). |
| Pitch Separation (Rule G9) | **D (Wolf):** 82.2 Hz · **H (Owl):** 112.1 Hz ($\Delta = +5.38$ nc) · **C (Fox):** 187.5 Hz ($\Delta = +8.90$ nc). |
| Cast Roles | H: Host (Owl) · D: Investigator (Wolf) · C: Psychologist (Fox) · N1: Leslie Wagner-Wilson, Former Peoples Temple Member (Sheep) · N2: FBI Investigator (Cat) |
| Video Structure | 53 narrative elements across 5 acts · Subtitles: `Tap12_EN.srt` |

---

## B2. Deliverable Files

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap12_EN/xuat_ban/Tap12_EN_master.mp3`](xuat_ban/Tap12_EN_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap12_EN/xuat_ban/Tap12_EN_master.wav`](xuat_ban/Tap12_EN_master.wav)
2. **Timeline & Subtitles:**
   - Timeline: [`.work/timeline_s_EN_t12.json`](../../.work/timeline_s_EN_t12.json) (2080.5 s)
   - Subtitles: [`02_SAN_XUAT/Tap12_EN/xuat_ban/Tap12_EN.srt`](xuat_ban/Tap12_EN.srt) (249 cues)
3. **QC Reports:**
   - Quality report: [`.work/quality_qc_utmos_ep12_en.json`](../../.work/quality_qc_utmos_ep12_en.json)
   - Listening verification list: [`02_SAN_XUAT/Tap12_EN/CanNghe_Tap12_EN_higgs.md`](xuat_ban/CanNghe_Tap12_EN_higgs.md)
