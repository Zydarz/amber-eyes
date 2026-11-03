import os, pathlib, time
D = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cB")
A = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cA")
tgt = sum(os.path.getsize(p) for p in A.glob("part_*.mp4"))
for i in range(4):
    s = sum(os.path.getsize(p) for p in D.glob("part_*.mp4"))
    done = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cB\chunkB.mp4").exists()
    print(f"[{time.strftime('%H:%M:%S')}] chunkB parts = {s/1e6:7.1f} MB / ~{tgt/1e6:.0f} MB ({100*s/tgt:5.1f}%)  chunkB.mp4={'CO' if done else 'chua'}", flush=True)
    if done: break
    time.sleep(60)
