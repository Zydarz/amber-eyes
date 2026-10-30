#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Re-organise the project folder (22/10/2026). Moves only — nothing is deleted.

Every move is recorded in 90_LUU_TRU/_nhat_ky_di_chuyen.json;
`py -3 90_LUU_TRU/hoan_tac.py` moves everything back.
"""
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
W = ROOT / ".work"
A = ROOT / "90_LUU_TRU"

MOVES = [
    # standard + design
    ("PhuongAn_TaoHinh_5NhanVat.md", "00_TIEU_CHUAN/PhuongAn_TaoHinh_5NhanVat.md"),
    # scripts
    ("danh_s_ch_28_k_ch_b_n_t_m_l_t_i_ph_m.md", "01_KICH_BAN/KHO_Y_TUONG_28_HO_SO.md"),
    ("kichban_tap01_22102026.md", "01_KICH_BAN/Tap01/kichban_tap01_22102026.md"),
    ("kichban_tap01_22102026_v2.md", "01_KICH_BAN/Tap01/kichban_tap01_22102026_v2.md"),
    # episode outputs
    ("Tap01_master.mp4", "02_SAN_XUAT/Tap01/xuat_ban/Tap01_master.mp4"),
    ("Tap01_master.mp3", "02_SAN_XUAT/Tap01/xuat_ban/Tap01_master.mp3"),
    ("Tap01.srt", "02_SAN_XUAT/Tap01/xuat_ban/Tap01.srt"),
    ("thumbnail.png", "02_SAN_XUAT/Tap01/xuat_ban/thumbnail.png"),
    ("mo_ta.txt", "02_SAN_XUAT/Tap01/xuat_ban/mo_ta.txt"),
    ("nguon_tham_khao.md", "02_SAN_XUAT/Tap01/xuat_ban/nguon_tham_khao.md"),
    # archive — old plans, reports, scripts, renders, voice tests
    ("KeHoach_ThuAm_Tap01.md", "90_LUU_TRU/ke_hoach_cu/KeHoach_ThuAm_Tap01.md"),
    ("KeHoach_ThuAm_Tap01_VIDEO.md", "90_LUU_TRU/ke_hoach_cu/KeHoach_ThuAm_Tap01_VIDEO.md"),
    (".work/KeHoach_LamLai_Video_Tap01_v9_backup.md", "90_LUU_TRU/ke_hoach_cu/KeHoach_LamLai_Video_Tap01_v9.md"),
    ("channel.json", "90_LUU_TRU/ke_hoach_cu/channel_cu.json"),
    ("BAO_CAO_TAP01.md", "90_LUU_TRU/bao_cao_cu/BAO_CAO_TAP01.md"),
    ("BAO_CAO_TRINH_TU_THUC_HIEN.md", "90_LUU_TRU/bao_cao_cu/BAO_CAO_TRINH_TU_THUC_HIEN.md"),
    (".work/BAO_CAO_TAP01.md", "90_LUU_TRU/bao_cao_cu/BAO_CAO_TAP01_ban_nhap.md"),
    ("Kc_1.txt", "90_LUU_TRU/kich_ban_cu/Kc_1.txt"),
    ("Kich_ban.txt", "90_LUU_TRU/kich_ban_cu/Kich_ban.txt"),
    ("AI_video.txt", "90_LUU_TRU/kich_ban_cu/AI_video.txt"),
    ("Kc_1.mp3", "90_LUU_TRU/ban_dung_cu/Kc_1.mp3"),
    ("Kc_1_Tap01.mp3", "90_LUU_TRU/ban_dung_cu/Kc_1_Tap01.mp3"),
    ("Kc_1_Tap01.mp4", "90_LUU_TRU/ban_dung_cu/Kc_1_Tap01.mp4"),
    ("so_sanh_giong_nu", "90_LUU_TRU/thu_giong/so_sanh_giong_nu"),
    ("so_sanh_5_giong.mp3", "90_LUU_TRU/thu_giong/so_sanh_5_giong.mp3"),
    # old pipeline assets no longer used
    ("assets/gfx", "90_LUU_TRU/assets_cu/gfx"),
    ("assets/gfx2", "90_LUU_TRU/assets_cu/gfx2"),
]
CAST_OLD = ["cast_contact_sheet.jpg", "cast_contact_sheet.png", "cast_overlay_mockup.png",
            "detective_concept.jpg", "host_concept.jpg", "host_mysterious_cartoon.jpg",
            "host_owl_mascot.jpg", "host_stylized_dark_cartoon.jpg", "neighbor_concept.jpg",
            "psychologist_concept.jpg", "detective_wolf_mascot_cutout.png", "host_owl_mascot_cutout.png",
            "neighbor_sheep_mascot_cutout.png", "observer_cat_mascot_cutout.png",
            "psychologist_fox_mascot_cutout.png"]
MOVES += [(f"assets/cast/{f}", f"90_LUU_TRU/assets_cu/cast_concept/{f}") for f in CAST_OLD]

# .work: keep the current pipeline, everything else -> .work/_cu
KEEP = {"parse_kichban.py", "tts_sentences.py", "build_audio3.py", "gen_images.py", "fix_backgrounds.py",
        "make_cast_cutouts.py", "make_logo.py", "make_intro.py", "voice_audition.py", "parse_shots.py",
        "build_video3.py", "rerender_part.py", "subtitles.py", "package.py", "reorganize.py",
        "script_v2.json", "tts_manifest.json", "timeline_s.json", "shots.json",
        "bg_jobs.json", "bg_jobs2.json", "bg_jobs3.json", "audio_master.wav", "audio_mix_raw.wav",
        "audio_s", "stems", "video3", "tts_s", "gen_log", "voice_test5", "ffmpeg", "__pycache__", "_cu",
        "KeHoach_LamLai_Video_Tap01_v9_backup.md", "BAO_CAO_TAP01.md"}


def main():
    log = []
    for p in sorted(W.iterdir()):
        if p.name not in KEEP:
            MOVES.append((f".work/{p.name}", f".work/_cu/{p.name}"))
    for src, dst in MOVES:
        s, d = ROOT / src, ROOT / dst
        if not s.exists():
            print("bỏ qua (không có):", src)
            continue
        if d.exists():
            raise SystemExit(f"đích đã tồn tại, dừng: {dst}")
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.move(str(s), str(d))
        log.append({"tu": src, "den": dst})
    A.mkdir(exist_ok=True)
    (A / "_nhat_ky_di_chuyen.json").write_text(json.dumps(log, ensure_ascii=False, indent=1), encoding="utf-8")
    (A / "hoan_tac.py").write_text(
        "# Hoàn tác việc sắp xếp ngày 22/10/2026: chuyển mọi file về chỗ cũ.\n"
        "import json, shutil\nfrom pathlib import Path\n"
        "R = Path(__file__).resolve().parent.parent\n"
        "for m in reversed(json.loads((R / '90_LUU_TRU/_nhat_ky_di_chuyen.json').read_text(encoding='utf-8'))):\n"
        "    s, d = R / m['den'], R / m['tu']\n"
        "    if s.exists() and not d.exists():\n"
        "        d.parent.mkdir(parents=True, exist_ok=True); shutil.move(str(s), str(d))\n"
        "print('đã hoàn tác')\n", encoding="utf-8")
    print(f"đã chuyển {len(log)} mục")


if __name__ == "__main__":
    main()
