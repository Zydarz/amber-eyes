#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Them dong provenance cho audio TK1 (TikTok Tap 01).

Doc lai provenance.json ngay truoc khi ghi (L5) -> ghi -> kiem tra.
Backup: .work/_cu/tk01_provenance_20261118_1900/provenance.json.bak
"""
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

ROOT = pathlib.Path(__file__).resolve().parent.parent
PROV = ROOT / "provenance.json"

WAV = "02_SAN_XUAT/TIKTOK/Tap01/TK1_master_audio.wav"
MP3 = "02_SAN_XUAT/TIKTOK/Tap01/TK1_master_audio.mp3"

entries = [
    {
        "file": WAV,
        "loai": "audio master clip TikTok TK1 (mo khoa 16:9 -> 9:16, 66,60 s)",
        "cong_cu": "TTS theo SPEC_AUDIO_CLIP_TAP01.json (engine Higgs Audio v3 + giong mau VoxCPM2, vai H/D/C); file do nguoi dung tao va dat vao thu muc san xuat - chua xac minh lai engine/seed thuc te tren may nguoi dung",
        "ngay": "2026-11-18",
        "prompt": "12 cau theo SPEC_AUDIO_CLIP_TAP01.json (clip TK1), giong mau: H=H.wav, D=D3_SH.wav, C=C2_AB03.wav",
        "seed": None,
        "mo_ta": "master audio TK1 - 66,60 s, pcm_s16le 48 kHz stereo, -16,0 LUFS, true peak -4,5 dBFS; QC: 12/12 cau khop spec 100%, 0 khoang cam >= 0,3 s, G9 tat ca cap >= 4 nua cung (min 7,34 nc)",
        "font": None,
        "dieu_khoan": "TTS Higgs Audio v3 chi chay tren Kaggle GPU (QUY_TAC_AUDIO_HIGGS.md); may dung video hien tai khong co GPU -> khong tai tao duoc file nay tai cho. Cach dung lai clip nay: dung lai timeline_tk1.json lam chu thoi gian de khoat them BGM/SFX va burn-in chu.",
        "kiem_tra_thuong_mai": "dat (QC 18/11/2026: xem 02_SAN_XUAT/TIKTOK/Tap01/BaoCao_QC_TK1_Audio_20261118.md)"
    },
    {
        "file": MP3,
        "loai": "ban MP3 xuat cho TikTok TK1 (256 kbps, 48 kHz stereo)",
        "cong_cu": "FFmpeg 9.0 (dong bo tu WAV master, lech 0,000 s)",
        "ngay": "2026-11-18",
        "prompt": None,
        "seed": None,
        "mo_ta": "MP3 256 kbps - 66,60 s - dung de upload TikTok (nhe hon WAV 12,79 MB)",
        "font": None,
        "dieu_khoan": "Bao dam kenh dung file MP3 nay cho clip TK1; WAV giu nguyen ban de khoat them am thanh nen.",
        "kiem_tra_thuong_mai": "dat (do lai tren MP3: -16,0 LUFS, true peak -4,5 dBFS, lech WAV-MP3 0,000 s)"
    },
]


def main():
    data = json.loads(PROV.read_text(encoding="utf-8"))
    n0 = len(data)
    existing = {e.get("file") for e in data}
    added = []
    for e in entries:
        if e["file"] in existing:
            print("  da co dong -> bo qua: %s" % e["file"])
            continue
        data.append(e)
        added.append(e["file"])
    PROV.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    print("  provenance: %d -> %d dong (them %d)" % (n0, len(data), len(added)))
    for f in added:
        print("   + %s" % f)


if __name__ == "__main__":
    main()
