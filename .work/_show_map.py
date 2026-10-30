from pathlib import Path
mp = Path(__file__).resolve().parents[1] / ".work" / "yt_map.tsv"
out = {}
for raw in mp.read_text(encoding="utf-8-sig").splitlines():
    p = raw.split("\t")
    if len(p) < 6 or not p[1].strip():
        continue
    out[p[1].strip()] = (p[0].strip(), p[2].strip(), p[4].strip(), p[5].strip())
codes = ["fx_sigh_female","fx_sigh_emotional","fx_crowd_relief_sigh","fx_printer_thermal",
         "fx_inkjet_printer_run","amb_library_quiet","fx_courtroom_dead_silence",
         "fx_defib_charge_shock","amb_camera_crew_press","amb_fastfood_cafeteria",
         "amb_lawyers_discussion","amb_crowd_outside_press_anger"]
for c in codes:
    print(f"{c:34s} <- {out[c][0]:32s} | {out[c][1]:14s} | {out[c][2]:22s} | {out[c][3]}s")