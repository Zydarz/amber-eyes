#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh lại 23 ảnh nền Tập 36 vi phạm H26 (khung hình không có chữ) — lần 2.

Bài học từ lần 1: prompt ghi "blank / unmarked / no readable marks" KHÔNG đủ —
FLUX vẫn vẽ chữ lên giấy tờ, nhãn hộp, biển số, màn hình, logo FBI.
Cách đúng: BỎ HẲN vật mang chữ khỏi khung hình (không có giấy tờ, không màn hình,
không biển số trong tầm nhìn, không khung ảnh, không biển hiệu) + thêm negative mạnh.

Quy trình: dời ảnh cũ -> .work/_cu/bg_old_<ngày>/t36_replaced_v2/ -> sửa prompt trong
bg_jobs_tap36.json -> sinh lại cùng tên -> cập nhật provenance.json.
"""
import json
import shutil
import sys
import time
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
sys.path.insert(0, str(WORK))
from flux_client import generate_16_9_background, get_credentials, DEFAULT_MODEL  # noqa: E402

BG = ROOT / "assets" / "bg"
JOBS_FILE = WORK / "bg_jobs_tap36.json"
PROV_FILE = ROOT / "provenance.json"
OLD_DIR = WORK / "_cu" / f"bg_old_{date.today().strftime('%Y%m%d')}" / "t36_replaced_v2"

NEG = (" strictly no text of any kind, no letters, no words, no numbers, no handwriting, "
       "no logos, no emblems, no signage, no labels, no labels on boxes or folders, "
       "no license plate characters, no stickers, no posters, no printed papers, "
       "no screens, no monitors, every surface completely blank and unmarked")

CAR = " the car is seen from the side with the license plate area out of view, plain unmarked body panels, no lettering or badge on any panel"

FIX = {
    "t36_a1_08_parked_car_closed_windows_misted":
        "Close view of a vintage car parked on a quiet night road seen from the side, "
        "windows fogged with condensation, no occupants visible, calm false sense of safety, "
        "moonless dark" + CAR + NEG,
    "t36_a1_12_lone_car_parked_foot_of_hill_1968":
        "A small vintage compact car parked silently at the foot of a dark hill on a rural Italian track in 1968, "
        "seen from the side with the plate area out of view, interior dark, no people visible, "
        "stillness before disaster" + CAR + NEG,
    "t36_a1_13_shadow_emerging_from_thicket":
        "A pitch-black faceless silhouette standing motionless at the edge of a thick thicket beside a distant parked car "
        "seen from the side, rural Italy 1968 night, utterly silent and ominous" + CAR + NEG,
    "t36_a1_19_abandoned_car_valuables_untouched":
        "Interior view of an empty vintage car on a country track, a leather handbag and a small closed jewelry box "
        "resting untouched on the plain seat, dawn light through the windows, bare seat surfaces, no stickers, no people" + NEG,
    "t36_a1_20_evidence_markers_shell_casings_grass":
        "Macro close view of small brass shell casings half buried in dewy grass at early light, "
        "shallow depth of field, empty grass and bare soil around them, no tags, no flags, no markers" + NEG,
    "t36_a2_03_second_car_parked_dark_escalation":
        "A second small vintage car parked alone on a dark hillside road at night in 1974 seen from the side, "
        "an enormous black shadow gradually spreading over the road ahead" + CAR + NEG,
    "t36_a2_07_young_driver_avoiding_hill_pullouts_dusk":
        "Dusk on a Florence suburban road, a small car seen from the side hurrying past empty hill pullouts, "
        "one distant silhouette of a young driver glancing nervously at the darkening hills, fear spreading" + CAR + NEG,
    "t36_a2_12_evidence_table_ammo_box_pistol_outline":
        "Evidence table in a forensic lab, an open plain cardboard tray of loose brass casings on bare steel, "
        "a pistol outline projected as light on the wall, empty bare table edges" + NEG,
    "t36_a2_15_camper_van_dark_roadside_1983":
        "A small vintage camper van parked by a dark roadside near Giogoli in Tuscany seen from the side, 1983, "
        "curtains drawn, smooth blank body panels, only a vague blurred shape behind misted glass, no people" + NEG,
    "t36_a2_20_repressed_rural_village_square_night":
        "Rural 1970s Italian village square at night, a stern church and a plain shuttered building with no signboard, "
        "a silhouette of a man getting into a car seen from the side alone toward the dark forest road, "
        "oppressive conservative society" + CAR + NEG,
    "t36_a2_23_man_turned_away_from_police_station_door":
        "A silhouette of a man turned away from the lit doorway of a plain stone building at night, standing in the dark "
        "street holding his hat, bare wall with no signboard and no plaque, shame and fear, Italian town" + NEG,
    "t36_a2_32_patrol_car_hill_road_exhausted_vigil":
        "A plain unmarked vintage car parked on a dark hill road at 3 a.m. seen from the side, steam from a thermos on the "
        "bonnet, a tired silhouette of an investigator leaning on the hood, sleeping hills around, exhausted vigil, "
        "no light bar, no badge, no lettering on the body" + NEG,
    "t36_a3_09_envelope_cut_out_letters_blank_collage":
        "Top-down view of a dark wooden desk with a single plain envelope and a fan of torn blank paper scraps, "
        "a pair of scissors and a small bottle of glue beside it under a lamp, bare empty desk edges, anonymous threat concept" + NEG,
    "t36_a3_20_detective_timeline_gaps_calendar_wall":
        "A bare dark wall with empty wooden clips and a taut thin red string stretched across it, a single hanging lamp, "
        "a silhouette studying the empty wall patiently, completely bare wall with nothing pinned on it" + NEG,
    "t36_a3_29_quantico_profile_1989_loner_manual_laborer_map":
        "A dim bare office in 1989 with a plain corkboard covered by completely unmarked blank sheets arranged as a loose "
        "human outline, a small wooden toy car and a plain hill contour map on a bare wooden table, one cold desk lamp, "
        "heavy shadow, no computer, no screens, no pictures, no frames, no emblems" + NEG,
    "t36_a3_31_fbi_report_shelved_dusty_local_police_office":
        "A dusty provincial Italian police office with tall shelves of plain closed folders and one thick closed dossier, "
        "a bare wooden desk, silhouettes of two detectives studying vague blurred scribbles of mystic symbols on the wall, "
        "plain blank walls, no badge, no emblem" + NEG,
    "t36_a4_07_police_station_summons_nervous_silhouette":
        "A small Italian police station at night, a nervous silhouette sitting alone in a hard chair across a bare desk "
        "under a swinging lamp, the officers' silhouettes frozen in surprise, completely bare walls with nothing hanging on them" + NEG,
    "t36_a4_08_alliance_of_shadows_three_silhouettes_hills":
        "Three dark silhouettes standing apart on a night hilltop in 1980s Tuscany with a parked old car behind them "
        "seen from the side, faces hidden entirely, sinister alliance, distant lights of Florence" + CAR + NEG,
    "t36_a4_16_haunting_cars_in_dark_lane_dream_fog":
        "Dreamlike foggy night lane lined with several empty ghostly old cars seen from the side with softly glowing windows "
        "fading in the mist, no people, haunting curse concept" + CAR + NEG,
    "t36_a4_34_independent_expert_reviewing_contradictions_desk":
        "A criminologist's silhouette at a bare wooden desk with a lamp and a magnifying glass held over an empty blotter, "
        "completely bare desk with nothing on it, concern about contradictions" + NEG,
    "t36_a5_03_grieving_family_home_photo_frame_empty_chair":
        "Modest Italian living room at dusk, an empty chair by a window beside a plain sideboard holding a small blank vase, "
        "silhouettes of elderly parents seated apart, bare walls with no pictures, long unresolved grief" + NEG,
    "t36_a5_05_science_progress_forensic_modern_lab_awakening":
        "Modern forensic laboratory with glassware, sample racks and a microscope, a silhouette of a scientist at work, "
        "warm sunrise light through the window, no screens, no monitors, no consoles, progress and awakening" + NEG,
    "t36_a5_07_collective_scar_tuscan_town_square_dusk_memorial":
        "Tuscan town square at dusk with a few silhouettes quietly gathered around a memorial wreath of white flowers, "
        "a plain stone civic building with shuttered windows and no signboard lit on one side, scar and reform" + NEG,
}


def update_provenance(rec):
    prov = json.loads(PROV_FILE.read_text(encoding="utf-8"))
    by_file = {r["file"]: i for i, r in enumerate(prov)}
    entry = {
        "file": rec["file"], "loai": "nền 16:9 dùng chung 4 ngôn ngữ",
        "cong_cu": f"Cloudflare Workers AI ({DEFAULT_MODEL})", "ngay": str(date.today()),
        "prompt": rec["prompt"], "seed": None, "nguon_anh_tham_chieu": None,
        "kich_thuoc_goc": [2112, 1188], "dieu_khoan": "Cloudflare Workers AI Terms of Service",
        "kiem_tra_thuong_mai": "đạt",
        "ghi_chu": "Sinh nền bằng Cloudflare FLUX.1 schnell, chuẩn Deep Noir H21/H25/H26, crop 16:9 và resize 2112x1188",
    }
    if rec["file"] in by_file:
        prov[by_file[rec["file"]]] = entry
    else:
        prov.append(entry)
    PROV_FILE.write_text(json.dumps(prov, ensure_ascii=False, indent=2), encoding="utf-8")


def main():
    if not get_credentials()[0]:
        print("LỖI: thiếu Cloudflare credentials")
        sys.exit(1)
    jobs = json.loads(JOBS_FILE.read_text(encoding="utf-8"))
    OLD_DIR.mkdir(parents=True, exist_ok=True)

    missing = [n for n in FIX if not any(j["name"] == n for j in jobs)]
    if missing:
        print("LỖI: không tìm thấy job:", missing)
        sys.exit(1)

    for j in jobs:
        if j["name"] not in FIX:
            continue
        old = BG / f"{j['name']}.png"
        if old.exists():
            shutil.move(str(old), str(OLD_DIR / old.name))
        j["prompt"] = FIX[j["name"]]
    JOBS_FILE.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"-> Đã dời {len(FIX)} ảnh cũ -> {OLD_DIR.relative_to(ROOT)} và cập nhật prompt")

    ok, fail = 0, 0
    for j in jobs:
        if j["name"] not in FIX:
            continue
        dst = BG / f"{j['name']}.png"
        t0 = time.perf_counter()
        try:
            img = generate_16_9_background(prompt=j["prompt"], steps=4,
                                           out_size=(2112, 1188), with_noir_style=True)
            img.save(dst, "PNG", optimize=True)
            print(f"XONG {j['name']} ({dst.stat().st_size//1024} KB, {time.perf_counter()-t0:.1f}s)", flush=True)
            update_provenance({"file": f"assets/bg/{j['name']}.png", "prompt": j["prompt"]})
            ok += 1
        except Exception as e:
            print(f"LỖI {j['name']}: {e}", flush=True)
            fail += 1
    print(f"\nHOÀN TẤT: {ok} thành công, {fail} lỗi / {len(FIX)} ảnh.")


if __name__ == "__main__":
    main()
