import sys, time, os
sys.path.insert(0, r"D:\TEST\Gax\amber-eyes\.work")
os.environ["AE_EP"]="03"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
import build_video3 as B
s = B.SH[40]; t = (s["start"]+s["end"])/2; fi = int(t*B.FPS)
print("shot:", s["id"], s["template"], s["bg"], s["camera"])
t0=time.perf_counter()
for _ in range(3): B.bg_frame(s, t, fi)
print(f"bg_frame: {(time.perf_counter()-t0)/3*1000:.1f} ms")
t0=time.perf_counter()
for _ in range(3): B.render(fi)
dt=(time.perf_counter()-t0)/3
print(f"render(): {dt*1000:.1f} ms -> {1/dt:.1f} fps (1 worker, co tai build chay)")
