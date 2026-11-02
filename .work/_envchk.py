import wave, numpy as np
from pathlib import Path
W = Path(r"D:\TEST\Gax\amber-eyes\.work")
FPS = 30; ENV_CHUNK = 1 << 20
def old(role):
    with wave.open(str(W/"stems_t03"/f"{role}.wav")) as wf:
        x = np.frombuffer(wf.readframes(wf.getnframes()), np.int16).astype(np.float32) / 32768
        sr = wf.getframerate()
    hop = sr // FPS; n = len(x) // hop
    e = np.sqrt((x[: n * hop].reshape(n, hop) ** 2).mean(axis=1))
    return np.clip(e / 0.12, 0, 1)
def new(role):
    with wave.open(str(W/"stems_t03"/f"{role}.wav")) as wf:
        sr = wf.getframerate(); hop = sr // FPS; n = wf.getnframes() // hop
        e = np.zeros(n, dtype=np.float32); rows = max(1, ENV_CHUNK // hop); done = 0
        while done < n:
            k = min(rows, n - done)
            a = np.frombuffer(wf.readframes(k * hop), np.int16)
            if a.size < k * hop:
                k = a.size // hop
                if k <= 0: break
                a = a[: k * hop]
            blk = a.astype(np.float32) / 32768
            e[done:done+k] = np.sqrt((blk.reshape(k, hop) ** 2).mean(axis=1))
            done += k
    return np.clip(e / 0.12, 0, 1)
ok = True
for r in ("H","D","C","N1","N2"):
    o, n = old(r), new(r)
    d = float(np.max(np.abs(o.astype(np.float64) - n.astype(np.float64))))
    good = o.size == n.size and d < 1e-6
    ok = ok and good
    print(f"  {r}: len old={o.size} new={n.size}  max|sai lech|={d:.3e}  {'OK' if good else 'SAI'}")
print("=> ENVELOPE GIONG HET" if ok else "=> VAN KHAC")
