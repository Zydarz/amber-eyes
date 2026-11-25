import soundfile as sf
import numpy as np

wav_path = "assets/voice_ref_voxcpm2_extra/W_MALE_YOUNG.wav"
data, sr = sf.read(".work/voxcpm_raw/W_MALE_EXTRA/male_young_take02_s456.wav")

# resample to 24000
import subprocess
subprocess.run(["ffmpeg", "-y", "-i", ".work/voxcpm_raw/W_MALE_EXTRA/male_young_take02_s456.wav", 
                "-af", "aresample=24000", "-ac", "1", wav_path], check=True)

# measure LUFS
import pyloudnorm as pyln
audio, rate = sf.read(wav_path)
meter = pyln.Meter(rate)
loudness = meter.integrated_loudness(audio)
# normalize to -18 LUFS
normalized_audio = pyln.normalize.loudness(audio, loudness, -18.0)
sf.write(wav_path, normalized_audio, rate, subtype='PCM_16')
print(f"Normalized to -18.0 LUFS, final loudness: {meter.integrated_loudness(normalized_audio):.2f} LUFS")
