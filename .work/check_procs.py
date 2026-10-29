import subprocess

cmd = 'wmic process where "name=\'ffmpeg.exe\' or name=\'python.exe\'" get ProcessId,CommandLine'
res = subprocess.run(cmd, capture_output=True, text=True, shell=True)
for line in res.stdout.splitlines():
    if line.strip():
        print(line[:120])
