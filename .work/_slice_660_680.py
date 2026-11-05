import soundfile as sf
from faster_whisper import WhisperModel

data, sr = sf.read('.work/speech_full_en_t02_16k.wav', start=int(660 * 16000), stop=int(680 * 16000))
m = WhisperModel('base', device='cpu', compute_type='int8')
segs, _ = m.transcribe(data, language='en', vad_filter=False, word_timestamps=True)
for s in segs:
    print(f"{s.start + 660:.2f} - {s.end + 660:.2f}: {s.text}")
    for w in s.words:
        print(f"   {w.start + 660:.2f} - {w.end + 660:.2f}: {w.word}")
