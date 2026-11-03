import os, pathlib, time, shutil
D = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cB")
A = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cA")
tgt = sum(os.path.getsize(p) for p in A.glob("part_*.mp4"))
out = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cB\chunkB.mp4")
for i in range(20):
    s = sum(os.path.getsize(p) for p in D.glob("part_*.mp4"))
    if out.exists():
        print(f"[{time.strftime('%H:%M:%S')}] chunkB.mp4 XONG = {os.path.getsize(out)/1e6:.1f} MB", flush=True)
        break
    print(f"[{time.strftime('%H:%M:%S')}] {s/1e6:7.1f}/{tgt/1e6:.0f} MB ({100*s/tgt:5.1f}%)", flush=True)
    time.sleep(45)
u = shutil.disk_usage(r"D:\TEST\Gax\amber-eyes")
print(f"\nDia: free {u.free/1e9:.1f} GB / total {u.total/1e9:.1f} GB")
