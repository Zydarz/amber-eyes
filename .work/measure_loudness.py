import subprocess, re

def check_file(path):
    cmd = ['ffmpeg', '-hide_banner', '-i', path, '-af', 'loudnorm=I=-16:TP=-1.5:LRA=11:print_format=summary', '-f', 'null', '-']
    res = subprocess.run(cmd, capture_output=True, text=True)
    out = res.stderr
    i = re.search(r"Input Integrated:\s+([-\d.]+)\s+LUFS", out)
    tp = re.search(r"Input True Peak:\s+([-\d.]+)\s+dBFS", out)
    lra = re.search(r"Input LRA:\s+([-\d.]+)\s+LU", out)
    i_val = i.group(1) if i else "N/A"
    tp_val = tp.group(1) if tp else "N/A"
    lra_val = lra.group(1) if lra else "N/A"
    print(f"{path}: Integrated = {i_val} LUFS | True Peak = {tp_val} dBFS | LRA = {lra_val} LU")

check_file('02_SAN_XUAT/Tap19/xuat_ban/Tap19_master.mp3')
check_file('02_SAN_XUAT/Tap19_EN/xuat_ban/Tap19_EN_master.mp3')
check_file('02_SAN_XUAT/Tap19_JA/xuat_ban/Tap19_JA_master.mp3')
