import pathlib, json
OUT = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban")
m = json.loads(pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\_qc_measure_t03_en.json").read_text(encoding="utf-8"))
mp4 = OUT / "Tap03_EN_master.mp4"
print(f"  mp4: {mp4.stat().st_size:,} byte · {m['mp4_duration']} s · {m['video_stream']['nb_frames']} khung")
print(f"  LUFS {m['lufs']} · true peak {m['peak']} dBFS · LRA {m['lra']} · decode errors: {m['decode_errors'] or 'khong co'}")
print(f"  srt {m['srt_cues']} cue · het luc {m['srt_last_end']} s · trung lap: {len(m['srt_overlap'])}")
