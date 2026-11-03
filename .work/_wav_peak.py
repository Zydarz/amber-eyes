import numpy as np, wave, pathlib
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\audio_master_EN_t03.wav")
import soundfile as sf
d, sr = sf.read(str(p), always_2d=True)
mono = d.mean(axis=1)
a = np.abs(mono)
print("SR", sr, "mau", len(a))
print("sample peak (dBFS):", round(20*np.log10(a.max()+1e-12), 2))
idx = int(np.argmax(a))
print("vi tri max:", round(idx/sr, 3), "s")
# dem so mau vuot cac nguong
for th in (-1.5, -2.0, -3.0, -4.0, -6.0):
    lim = 10**(th/20)
    n = int((a > lim).sum())
    print(f"  mau > {th} dBFS: {n} ({100*n/len(a):.5f}%)")
# 10 mau lon nhat
top = np.argpartition(a, -10)[-10:]
top = top[np.argsort(-a[top])]
print("top-10 vi tri (s):", [round(t/sr,3) for t in top])
