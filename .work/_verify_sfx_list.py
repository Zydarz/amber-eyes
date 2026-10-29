from pathlib import Path

SFX = Path("assets/sfx")
files_to_check = [
    "t2/amb_winter_wind.wav",
    "typewriter.wav",
    "t2/amb_office_night.wav",
    "t2/fx_heartbeat_slow.wav",
    "t2/amb_basement.wav",
    "t3/amb_crickets_traffic.wav",
    "t05/amb_server_fan.wav",
    "t2/amb_interrogation.wav",
    "t2/amb_courtroom.wav",
    "fx_envelope_tear.wav",
    "t3/fx_cassette_button.wav",
    "clock_tick.wav",
    "t2/fx_drawer_open.wav",
    "stamp_thud.wav",
    "card_flip.wav",
    "fx_evidence_measure_tape.wav",
    "paper_rustle.wav",
    "t05/fx_floppy_disk_insert.wav",
    "keyboard_night.wav",
    "police_siren_distant.wav",
    "t05/fx_car_brake_screech.wav",
    "t2/fx_door_metal_slam.wav",
    "t2/fx_stinger.wav",
    "t2/fx_gavel_triple.wav",
    "folder_close.wav"
]

all_ok = True
for f in files_to_check:
    p = SFX / f
    if not p.exists():
        print(f"MISSING: {f}")
        all_ok = False
    else:
        print(f"EXISTS: {f}")
if all_ok:
    print("\nALL SFX FILES EXIST 100%!")
