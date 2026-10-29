from pathlib import Path
SFX=Path("assets/sfx")
have={p.stem for p in SFX.rglob("*.wav")}
print("tong so stem .wav trong assets/sfx (de quy):", len(have))
for c in ["amb_fastfood_cafeteria","amb_hospital_ventilator","amb_server_fan",
          "amb_carnival_ride_music_far","amb_tv_static_eerie","amb_desert_wind_dry",
          "amb_horse_hooves_distant","amb_female_humming_far","amb_wind_pines",
          "amb_megaphone_loudspeaker","amb_subway_station_jp","amb_library_quiet",
          "amb_tractor_engine","amb_small_plane_engine","amb_loudspeaker_jungle_echo",
          "amb_bus_distant","amb_train_horn_distant_night","amb_projector_room",
          "amb_lab_equipment","amb_camera_crew_press","amb_lawyers_discussion",
          "amb_crowd_excited_girls","amb_crowd_applause_court","amb_wind_chime",
          "amb_ceiling_fan","amb_highway_speed_car","amb_wind_tropical"]:
    hit=[str(p.relative_to(Path('.'))) for p in SFX.rglob(c+".wav")]
    print(f"  {c:<32} {'CO  '+str(hit) if hit else 'THIEU'}")
