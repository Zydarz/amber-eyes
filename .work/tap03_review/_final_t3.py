import wave, glob, os
for f in sorted(glob.glob(r"D:\TEST\Gax\Audi\assets\sfx\t3\*.wav")):
    w = wave.open(f, "rb")
    print(f"{os.path.basename(f):<26} ch={w.getnchannels()} rate={w.getframerate()} bits={w.getsampwidth()*8} dur={w.getnframes()/w.getframerate():6.1f}s  {os.path.getsize(f)/1048576:6.1f} MB")
    w.close()
