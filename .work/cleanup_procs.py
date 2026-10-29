import os
import psutil

current_pid = os.getpid()
print(f"Current script PID: {current_pid}")

# Kill any ffmpeg process
for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
    try:
        pname = proc.info['name'].lower()
        pid = proc.info['pid']
        if pid == current_pid:
            continue
        if 'ffmpeg' in pname:
            print(f"Killing ffmpeg process {pid}")
            proc.kill()
        elif 'python' in pname:
            cmdline = " ".join(proc.info['cmdline'] or []).lower()
            if 'build_video3.py' in cmdline or 'multiprocessing' in cmdline:
                print(f"Killing old python worker {pid}: {cmdline[:80]}")
                proc.kill()
    except (psutil.NoSuchProcess, psutil.AccessDenied):
        pass

print("Cleanup complete.")
