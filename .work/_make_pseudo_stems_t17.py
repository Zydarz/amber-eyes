# Stems GIA cho Tap17 (VI/EN/JA): cat master theo cua so cau cua tung vai, 16 kHz mono s16.
# Chi de ve song badge khi stems that da bi don; song se lan nhac nen. KHONG dung cho QC giong (A14).
import json, subprocess, sys, glob, numpy as np
from pathlib import Path
R = Path(__file__).resolve().parents[1]; W = R/".work"
FF = glob.glob(str(W/"ffmpeg/*/bin/ffmpeg.exe"))[0]
for L, suf, d, name in (("VI", "", "Tap17", "Tap17_master"), ("EN", "_EN", "Tap17_EN", "Tap17_EN_master"), ("JA", "_JA", "Tap17_JA", "Tap17_JA_master")):
    tl = json.load(open(W/f"timeline_s{suf}_t17.json", encoding="utf-8"))
    raw = subprocess.run([FF, "-v", "error", "-i", str(R/f"02_SAN_XUAT/{d}/xuat_ban/{name}.wav"), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.int16); sr = 16000
    out = W/f"stems{suf}_t17"; out.mkdir(exist_ok=True)
    import wave
    for role in ("H", "D", "C", "N1", "N2"):
        y = np.zeros_like(x)
        for it in tl["items"]:
            if it["role"] == role:
                a, b = int(it["start"]*sr), min(len(x), int(it["end"]*sr)); y[a:b] = x[a:b]
        with wave.open(str(out/f"{role}.wav"), "wb") as wf:
            wf.setnchannels(1); wf.setsampwidth(2); wf.setframerate(sr); wf.writeframes(y.tobytes())
        print(L, role, "cau:", sum(1 for i in tl["items"] if i["role"] == role), "peak", int(np.abs(y).max()))
    (out/"_PSEUDO.txt").write_text("Stems gia cat tu master (co nhac nen) - chi de ve song badge. Sinh boi _make_pseudo_stems_t17.py 19/11/2026.\n", encoding="utf-8")
