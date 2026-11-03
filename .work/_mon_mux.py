import os, pathlib, time
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\02_SAN_XUAT\Tap03_EN\xuat_ban\Tap03_EN_master.mp4")
for i in range(6):
    print(f"[{time.strftime('%H:%M:%S')}] {os.path.getsize(p) if p.exists() else -1} byte", flush=True)
    time.sleep(20)
