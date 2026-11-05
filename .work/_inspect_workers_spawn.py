from pathlib import Path
lines = Path(".work/build_video3.py").read_text(encoding="utf-8").splitlines()
for i, l in enumerate(lines):
    if "Process(" in l or "Pool(" in l or "workers" in l and "jobs" in l:
        for j in range(max(0, i-5), min(len(lines), i+25)):
            print(f"{j+1}: {lines[j]}")
        break
