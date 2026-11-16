# PRODUCTION PLAN EPISODE 11 · ENGLISH EDITION · "THE KEN & BARBIE KILLERS"

**Standard Applied:** `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` (Part A), `00_TIEU_CHUAN/QUY_TAC_HIGGS_MAC.md`  
**Script:** `01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md` · **Release Target:** `02_SAN_XUAT/Tap11_EN/xuat_ban/`  
**Date:** November 16, 2026

---

## B1. Episode Information

| Item | Value |
|---|---|
| Script | `01_KICH_BAN/Tap11_EN/kichban_tap11_EN.md` — 59 elements · **272 sentences** |
| Voice Engine | **Higgs Audio v3** (`bosonai/higgs-audio-v3-tts-4b` on Apple Silicon Mac MLX) — Voice Reference Set: VoxCPM2 English (`H_EN`, `D_EN`, `C_EN`, `N1_EN`, `N2_EN`). No emotion tags (M4). Pre-encoded (M1). Tail silence trimmed (M3). |
| Master Output | `02_SAN_XUAT/Tap11_EN/xuat_ban/Tap11_EN_master.mp3` (**2223.0 s / ~37 phút 02 giây** · **Integrated: ** · **True Peak: ** · **0 khoảng câm > 0.3 s**) |
| Quality Control (ASR & CER) | **Whisper Base CER:** Mean = **0.95%**, Median = **0.00%** (48/272 sentences > 2%). Target (< 2.0%). |
| Quality Control (Naturalness MOS) | **UTMOSv2 MOS:** Mean = **3.45 / 5.0** (Range: 2.60 – 4.23). Target (>= 3.0 / 5.0). |
| Pitch Separation (Rule G9) | **D (Wolf):** 83.5 Hz · **H (Owl):** 112.1 Hz ($\Delta = +5.11$ nc) · **C (Fox):** 187.5 Hz ($\Delta = +8.90$ nc). |
| Cast Roles | H: Host (Owl) · D: Investigator (Wolf) · C: Psychologist (Fox) · N1: Port Dalhousie Neighbor (Sheep) · N2: Case Prosecutor (Cat) |
| Video Structure | 59 narrative elements across 5 acts · Subtitles: `Tap11_EN.srt` |

---

## B2. Deliverable Files

1. **Master Audio:**
   - MP3: [`02_SAN_XUAT/Tap11_EN/xuat_ban/Tap11_EN_master.mp3`](xuat_ban/Tap11_EN_master.mp3)
   - WAV: [`02_SAN_XUAT/Tap11_EN/xuat_ban/Tap11_EN_master.wav`](xuat_ban/Tap11_EN_master.wav)
2. **Timeline & Subtitles:**
   - Timeline: [`.work/timeline_s_EN_t11.json`](../../.work/timeline_s_EN_t11.json) (2223.0 s)
   - Subtitles: [`02_SAN_XUAT/Tap11_EN/xuat_ban/Tap11_EN.srt`](xuat_ban/Tap11_EN.srt) (272 cues)
3. **QC Reports:**
   - Quality report: [`.work/quality_qc_utmos_ep11_en.json`](../../.work/quality_qc_utmos_ep11_en.json)
   - Listening verification list: [`02_SAN_XUAT/Tap11_EN/CanNghe_Tap11_EN_higgs.md`](xuat_ban/CanNghe_Tap11_EN_higgs.md)
