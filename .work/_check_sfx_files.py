from pathlib import Path

sfx = Path("assets/sfx")
files = [
    "amb_hospital_monitor_heartbeat.wav",
    "t2/amb_office_night.wav",
    "t3/amb_pipe_drain.wav",
    "t2/amb_interrogation.wav",
    "t2/amb_courtroom.wav",
    "fx_ambulance_siren_distant.wav",
    "t2/fx_sub_drop.wav",
    "t2/fx_stinger.wav",
    "keyboard_night.wav",
    "card_flip.wav",
    "t3/fx_cassette_button.wav",
    "fx_stamp_wood.wav",
    "lock_door.wav",
    "t3/fx_paper_fold.wav",
    "footsteps.wav",
    "folder_close.wav",
    "fx_glasses_clink.wav",
    "heartbeat_slow.wav",
    "t2/fx_door_metal_slam.wav",
    "t2/fx_chair_scrape.wav",
    "fx_handcuff_snap.wav",
    "t2/fx_gavel_triple.wav"
]
missing = [f for f in files if not (sfx / f).exists()]
print("Missing:", missing)
if not missing:
    print("ALL 22 SFX FILES EXIST!")
