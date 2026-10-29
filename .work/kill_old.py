import subprocess

print("Killing ffmpeg processes...")
subprocess.run("taskkill /F /IM ffmpeg.exe /T", shell=True)

old_pids = [2024, 5316, 5660, 5968, 8408, 11088, 15564, 17480, 17876, 18288, 19316, 19996, 20080, 20436, 21940, 22868]
for p in old_pids:
    subprocess.run(f"taskkill /F /PID {p} /T", shell=True)

print("Processes cleared.")
