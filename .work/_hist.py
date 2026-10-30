# -*- coding: utf-8 -*-
from pathlib import Path
mp = Path(__file__).resolve().parents[1] / ".work" / "yt_map.tsv"
hist = {}
for raw in mp.read_text(encoding="utf-8-sig").splitlines():
    p = raw.split("\t")
    if len(p) >= 6 and p[1].strip():
        ma = p[1].strip()
        hist.setdefault(ma, [])
        t = p[0].strip()
        if not hist[ma] or hist[ma][-1] != t:
            hist[ma].append(t)
codes = ["fx_sigh_emotional","fx_crowd_relief_sigh","fx_sigh_female","fx_printer_thermal",
 "fx_inkjet_printer_run","fx_crying_female_phone","fx_defib_charge_shock","fx_lab_test_kit",
 "fx_courtroom_dead_silence","amb_library_quiet","amb_female_humming_far","amb_fastfood_cafeteria",
 "amb_lawyers_discussion","amb_crowd_murmur_press","amb_crowd_outside_press_anger",
 "fx_911_call_recording_radio","fx_phone_unlock_click","fx_wooden_hinge_creak_open",
 "fx_wooden_lid_slam_latch","fx_door_slam_indoor","fx_monitor_case_close",
 "fx_evidence_measure_tape","fx_computer_beep_restore","fx_metal_lock_open","fx_modem_dialup_data"]
for c in codes:
    h = hist.get(c, [])
    print(f"{c:34s} -> {' | '.join(h)}")