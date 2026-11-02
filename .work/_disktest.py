import time, os
from pathlib import Path
p = Path(r"D:\TEST\Gax\amber-eyes\.work\_disk_speed_test.bin")
data = os.urandom(8*1024*1024)
t0=time.perf_counter()
with open(p,"wb") as f:
    for _ in range(24): f.write(data)   # 192 MB
    f.flush(); os.fsync(f.fileno())
dt=time.perf_counter()-t0
print(f"ghi 192 MB: {dt:.1f}s -> {192/dt:.1f} MB/s")
t0=time.perf_counter(); os.remove(p); print(f"xoa: {time.perf_counter()-t0:.2f}s")
