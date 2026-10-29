import wave
for f in [r"D:\TEST\Gax\Audi\assets\sfx\t2\amb_winter_wind.wav", r"D:\TEST\Gax\Audi\assets\sfx\t2\fx_gavel_triple.wav"]:
    try:
        w = wave.open(f, "rb")
        print(f.split("\\")[-1], "ch=", w.getnchannels(), "rate=", w.getframerate(), "bits=", w.getsampwidth()*8, "dur=%.1fs" % (w.getnframes()/w.getframerate()))
        w.close()
    except Exception as e:
        print(f, "ERR", e)
