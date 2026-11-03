import os, pathlib, time, subprocess
D = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cB")
def sizes():
    return sum(os.path.getsize(p) for p in D.glob("part_*.mp4")), sorted((p.name, os.path.getsize(p)) for p in D.glob("part_*.mp4"))
s0, l0 = sizes()
t0 = time.time()
time.sleep(45)
s1, l1 = sizes()
dt = time.time() - t0
print(f"t={dt:.1f}s  {s0/1e6:.1f} MB -> {s1/1e6:.1f} MB  toc do {((s1-s0)/1e6/dt):.2f} MB/s")
for n, s in l1: print("   ", n, f"{s/1e6:.1f} MB")
# so voi chunk A hoan tat
A = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\video3_EN_t03_cA")
ca = sorted((p.name, os.path.getsize(p)) for p in A.glob("part_*.mp4"))
print("chunk A parts:", [(n, round(s/1e6,1)) for n,s in ca], "tong", round(sum(s for _,s in ca)/1e6,1), "MB")
