# Dung lai timeline Tap15 tu SRT cua master (T20: timeline cu la uoc luong). Ghep cue->cau theo thu tu + do chieu nang luong.
import json, re, subprocess, wave, sys, unicodedata
from pathlib import Path
import numpy as np
W = Path(__file__).parent; R = W.parent
FF = r"C:\Users\ADMIN\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
CFG = {"": "Tap15", "EN": "Tap15_EN", "JA": "Tap15_JA"}
def norm(s): return re.sub(r"[\W_]+", "", unicodedata.normalize("NFC", s)).lower()
def mp3dur(p):
    r = subprocess.run([FF, "-i", str(p)], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r); return int(m[1])*3600+int(m[2])*60+float(m[3])
rep = {}
for lang, d in CFG.items():
    suf = f"_{lang}" if lang else ""
    t = json.load(open(W/f"timeline_s{suf}_t15.json", encoding="utf-8"))
    tx = open(R/f"02_SAN_XUAT/{d}/xuat_ban/{d}.srt", encoding="utf-8").read()
    cues = []
    for m in re.finditer(r"(\d+)\n(\d\d):(\d\d):(\d\d),(\d+) --> (\d\d):(\d\d):(\d\d),(\d+)\n(.*?)(?:\n\n|\Z)", tx, re.S):
        a = int(m[2])*3600+int(m[3])*60+int(m[4])+int(m[5])/1000; b = int(m[6])*3600+int(m[7])*60+int(m[8])+int(m[9])/1000
        txt = re.sub(r"^\[[^\]]+\]\s*", "", m[10].replace("\n", " ")); cues.append((a, b, norm(txt)))
    ci = 0; new = []; bad = 0
    for it in t["items"]:
        target = norm(it["text"]); got = ""; first = ci
        while ci < len(cues) and len(got) < len(target):
            got += cues[ci][2]; ci += 1
        if abs(len(got)-len(target)) > max(3, 0.03*len(target)) or not (got[:12] == target[:12]): bad += 1
        new.append((cues[first][0], cues[ci-1][1]))
    assert ci == len(cues), (lang, ci, len(cues))
    old = [(i["start"], i["end"]) for i in t["items"]]
    def shift(x):
        for (o, _), (n, _) in zip(old, new):
            if o >= x - 1e-6: return x + (n - o)
        return x + (new[-1][1] - old[-1][1])
    for it, (a, b) in zip(t["items"], new): it["start"], it["end"] = round(a, 3), round(b, 3)
    for mk in t["markers"]:
        for k in ("start", "end", "at"):
            if k in mk and mk.get("type") != "INTRO": mk[k] = round(shift(mk[k]), 3)
    acts = {}
    for it in t["items"]:
        a = acts.setdefault(str(it["act"]), [it["start"], it["end"]]); a[1] = it["end"]
    t["acts"] = acts
    mp3 = R/f"02_SAN_XUAT/{d}/xuat_ban/{d}_master.mp3"; tot = round(mp3dur(mp3), 2)
    t["total"] = tot; t["_master"] = "srt_measured_t15_20261118"
    json.dump(t, open(W/f"timeline_s{suf}_t15.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    # doi chieu nang luong
    raw = subprocess.run([FF, "-v", "error", "-i", str(mp3), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32)/32768; fr = 320
    rms = np.sqrt(np.convolve(x**2, np.ones(fr)/fr, "same")[::fr]); thr = max(0.01, np.percentile(rms, 20)*2.5); v = rms > thr
    inv = []; gapv = []
    prev_end = 0
    for it in t["items"]:
        a, b = int(it["start"]*50), int(it["end"]*50); inv.append(v[a:b].mean())
        if prev_end and a-prev_end > 10: gapv.append(v[prev_end+3:a-3].mean())
        prev_end = b
    rep[lang or "VI"] = dict(cues=len(cues), items=len(t["items"]), text_mismatch=bad, total=tot, last_end=t["items"][-1]["end"],
        voiced_in_items=round(float(np.mean(inv)), 3), min_item=round(float(min(inv)), 3), voiced_in_gaps=round(float(np.mean(gapv)), 3))
    print(lang or "VI", rep[lang or "VI"])
