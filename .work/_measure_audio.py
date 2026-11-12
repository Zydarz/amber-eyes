import subprocess, re, json

FF = ".work/ffmpeg/ffmpeg-n9.0-latest-win64-lgpl-shared-9.0/bin/ffmpeg.exe"
files = [
    ("VI", ".work/audio_master_t09.wav"),
    ("EN", ".work/audio_master_EN_t09.wav"),
    ("JA", ".work/audio_master_JA_t09.wav")
]

for lang, fn in files:
    cmd = [FF, "-hide_banner", "-i", fn, "-af", "loudnorm=print_format=json", "-f", "null", "-"]
    p = subprocess.run(cmd, capture_output=True, text=True)
    m = re.findall(r"\{[\s\S]*?\}", p.stderr)
    if m:
        data = json.loads(m[-1])
        print(f"{lang}: I={data.get('input_i')} LUFS, TP={data.get('input_tp')} dBFS, LRA={data.get('input_lra')}")
