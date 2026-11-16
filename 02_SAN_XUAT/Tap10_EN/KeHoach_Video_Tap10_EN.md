# PRODUCTION PLAN EPISODE 10 · ENGLISH EDITION · "THE WOODEN BOX UNDER THE BED"

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`  
**Script:** `01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md` · **Release Target:** `02_SAN_XUAT/Tap10_EN/xuat_ban/`  
**Date:** November 15, 2026

---

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md` — 52 elements · **240 sentences** |
| Voice Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b` on Apple Silicon Mac MLX) — Voice Reference Set: VoxCPM2 English (`H_EN`, `D_EN`, `C_EN`, `N1_EN`, `N2_EN`). No emotion tags (M4). Pre-encoded (M1). Tail silence trimmed (M3). |
| Master Output | `02_SAN_XUAT/Tap10_EN/xuat_ban/Tap10_EN_master.mp3` (**1880.9 s / ~31 phút 20 giây** · **Integrated: -16.2 LUFS** · **True Peak: -1.5 dBFS** · **0 khoảng câm > 0.3 s**) |
| Quality Control (ASR & CER) | **Whisper Base CER:** Mean = **0.66%**, Median = **0.00%** (30/240 sentences > 2%). Target (< 2.0%). |
| Quality Control (Naturalness MOS) | **UTMOSv2 MOS:** Mean = **3.41 / 5.0** (Range: 2.40 – 4.29). Target (>= 3.0 / 5.0). |
| Pitch Separation (Rule G9) | **D (Wolf):** 82.1 Hz · **H (Owl):** 112.5 Hz ($\Delta = +5.47$ nc) · **C (Fox):** 189.0 Hz ($\Delta = +8.97$ nc). |
| Cast Roles | H: Host (Owl) · D: Investigator (Wolf) · C: Psychologist (Fox) · N1: Colleen's Friend (Sheep) · N2: Janice Hooker (Cat) |
| Video Structure | 52 narrative elements across 5 acts · Subtitles: `Tap10_EN.srt` |

---

## B2. Deliverable Files

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap10_EN/xuat_ban/Tap10_EN_master.mp3`](xuat_ban/Tap10_EN_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap10_EN/xuat_ban/Tap10_EN_master.wav`](xuat_ban/Tap10_EN_master.wav)
2. **Timeline & Subtitles:**
   - Timeline: [`.work/timeline_s_EN_t10.json`](../../.work/timeline_s_EN_t10.json) (1880.9 s)
   - Subtitles: [`02_SAN_XUAT/Tap10_EN/xuat_ban/Tap10_EN.srt`](xuat_ban/Tap10_EN.srt) (240 cues)
3. **QC Reports:**
   - Quality report: [`.work/quality_qc_utmos_ep10_en.json`](../../.work/quality_qc_utmos_ep10_en.json)
   - Listening verification list: [`02_SAN_XUAT/Tap10_EN/CanNghe_Tap10_EN_higgs.md`](xuat_ban/CanNghe_Tap10_EN_higgs.md)
