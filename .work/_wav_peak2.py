import numpy as np, pathlib, soundfile as sf
p = r"D:\TEST\Gax\amber-eyes\.work\audio_master_EN_t03.wav"
d, sr = sf.read(p, always_2d=True)
for c in range(d.shape[1]):
    a = np.abs(d[:, c])
    pk = 20*np.log10(a.max()+1e-12)
    idx = int(np.argmax(a))
    print(f"kenh {c}: peak {pk:.2f} dBFS tai {idx/sr:.3f} s · mau >-2.0dBFS: {int((a>10**(-2/20)).sum())}")
a = np.abs(d).max(axis=1)
for th in (-1.5,-2.0,-2.5,-3.0,-3.5,-4.0):
    n = int((a > 10**(th/20)).sum())
    print(f"  {th} dBFS: {n} mau ({100*n/len(a):.5f}%)")
