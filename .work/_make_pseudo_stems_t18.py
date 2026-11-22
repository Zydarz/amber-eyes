# Stems XAP XI cho Tap18 (theo tien le Tap13 huong B): audio tung cau da mat,
# nen cat master mp3 theo cua so [start,end] cua tung vai trong timeline. KHONG phai stems that.
import json, subprocess, sys, wave
from pathlib import Path
import numpy as np
W = Path(__file__).parent
FF = r"C:\Users\ADMIN\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
CFG = {"": ("timeline_s_t18.json", "02_SAN_XUAT/Tap18/xuat_ban/Tap18_master.mp3", "stems_t18"),
       "EN": ("timeline_s_EN_t18.json", "02_SAN_XUAT/Tap18_EN/xuat_ban/Tap18_EN_master.mp3", "stems_EN_t18"),
       "JA": ("timeline_s_JA_t18.json", "02_SAN_XUAT/Tap18_JA/xuat_ban/Tap18_JA_master.mp3", "stems_JA_t18")}
for lang, (tl, mp3, sd) in CFG.items():
    t = json.load(open(W / tl, encoding="utf-8"))
    raw = subprocess.run([FF, "-v", "error", "-i", str(W.parent / mp3), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    out = Path(W / sd); out.mkdir(exist_ok=True)
    for role in ("H", "D", "C", "N1", "N2"):
        y = np.zeros_like(x)
        for it in t["items"]:
            if it["role"] == role:
                a, b = int(it["start"] * 16000), int(it["end"] * 16000)
                y[a:b] = x[a:b]
        with wave.open(str(out / f"{role}.wav"), "wb") as wf:
            wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(16000)
            wf.writeframes((np.clip(y, -1, 1) * 32767).astype(np.int16).tobytes())
        print(lang or "VI", role, "n_items", sum(i["role"] == role for i in t["items"]))
