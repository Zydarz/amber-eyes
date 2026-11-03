import os, pathlib, time
D = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cC")
out = D / "chunkC.mp4"
for i in range(40):
    s = sum(os.path.getsize(p) for p in D.glob("part_*.mp4"))
    if out.exists():
        print(f"[{time.strftime('%H:%M:%S')}] chunkC.mp4 XONG = {os.path.getsize(out)/1e6:.1f} MB", flush=True); break
    print(f"[{time.strftime('%H:%M:%S')}] parts = {s/1e6:7.1f} MB", flush=True)
    time.sleep(60)
