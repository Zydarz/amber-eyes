import sys, pathlib, soundfile as sf
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work"); sys.path.insert(0, r"D:\TEST\Gax\amber-eyes")
import edition as ED
d = ED.w("stems")
print("ED.w('stems') =", d, "| ton tai:", pathlib.Path(d).exists())
for p in sorted(pathlib.Path(d).glob("*.wav")):
    i = sf.info(str(p))
    print("   %-18s %d Hz | %d kenh | %s | %.1f s" % (p.name, i.samplerate, i.channels, i.subtype, i.frames/i.samplerate))
