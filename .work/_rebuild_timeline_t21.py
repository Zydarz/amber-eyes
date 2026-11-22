# Dung timeline Tap21 (VI/EN/JA) tu SRT cua master (T21: khong tin uoc luong). Khong co timeline_s_t21 san -> tao moi tu script_tap21*.json.
# Ghep cue->cau theo thu tu chu + doi chieu nang luong voi master mp3.
import json, re, subprocess, unicodedata
from pathlib import Path
import numpy as np
W = Path(__file__).parent; R = W.parent
FF = r"C:\Users\ADMIN\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\imageio_ffmpeg\binaries\ffmpeg-win-x86_64-v7.1.exe"
CFG = {"": ("Tap21", "script_tap21.json"), "EN": ("Tap21_EN", "script_tap21_EN.json"), "JA": ("Tap21_JA", "script_tap21_JA.json")}
NEL = {"1.07": "N1", "4.09": "N2"}
def norm(s): return re.sub(r"[\W_]+", "", unicodedata.normalize("NFC", s)).lower()
def mp3dur(p):
    r = subprocess.run([FF, "-i", str(p)], capture_output=True, text=True).stderr
    m = re.search(r"Duration: (\d+):(\d+):([\d.]+)", r); return int(m[1])*3600+int(m[2])*60+float(m[3])
rep = {}
for lang, (d, sf) in CFG.items():
    suf = f"_{lang}" if lang else ""
    script = json.load(open(W/sf, encoding="utf-8"))
    items = []; seq = []   # seq: (element dict) ordered
    for e in script:
        if e["kind"] == "LOI":
            role = NEL.get(e["id"], e["role"])
            for s in e["sentences"]:
                items.append({"id": s["id"], "element": e["id"], "act": int(e["act"]), "role": role, "text": s["text"]})
        seq.append(e)
    tx = open(R/f"02_SAN_XUAT/{d}/xuat_ban/{d}.srt", encoding="utf-8").read().replace("\r\n", "\n")
    cues = []
    for m in re.finditer(r"(\d+)\n(\d\d):(\d\d):(\d\d),(\d+) --> (\d\d):(\d\d):(\d\d),(\d+)\n(.*?)(?:\n\n|\Z)", tx, re.S):
        a = int(m[2])*3600+int(m[3])*60+int(m[4])+int(m[5])/1000; b = int(m[6])*3600+int(m[7])*60+int(m[8])+int(m[9])/1000
        txt = re.sub(r"^\[[^\]]+\]\s*", "", m[10].replace("\n", " ")); txt = re.sub(r"<\|[^|]*\|>", "", txt); cues.append((a, b, norm(txt)))
    ci = 0; bad = []
    for it in items:
        target = norm(it["text"]); got = ""; first = ci
        while ci < len(cues) and len(got) < len(target):
            got += cues[ci][2]; ci += 1
        if abs(len(got)-len(target)) > max(3, 0.03*len(target)) or got[:8] != target[:8]: bad.append(it["id"])
        it["start"] = round(cues[first][0], 3); it["end"] = round(cues[ci-1][1], 3)
    leftover = len(cues) - ci
    mp3 = R/f"02_SAN_XUAT/{d}/xuat_ban/{d}_master.mp3"; tot = round(mp3dur(mp3), 2)
    # markers
    markers = [{"type": "INTRO", "start": 0.0, "end": 22.41}]
    starts = {i["id"]: i["start"] for i in items}
    def next_start(eid):
        for e in seq[seq.index(next(x for x in seq if x["id"] == eid))+1:]:
            if e["kind"] == "LOI" and e["sentences"]: return starts[e["sentences"][0]["id"]]
        return items[-1]["end"] + 0.8
    acts = {}
    for it in items:
        a = acts.setdefault(str(it["act"]), [it["start"], it["end"]]); a[1] = it["end"]
    for e in seq:
        if e["kind"] in ("BGM", "SFX"):
            markers.append({"type": e["kind"], "id": e["id"], "at": round(next_start(e["id"]), 3), "desc": e.get("desc", "")})
    for n in range(1, 5):
        a_end = acts[str(n)][1]; b_start = acts[str(n+1)][0]
        markers.append({"type": "ACT", "act": n+1, "start": round(a_end, 3), "end": round(b_start, 3)})
    markers.sort(key=lambda m: m.get("start", m.get("at", 0)))
    acts[str(len(acts))][1] = round(acts[str(len(acts))][1] + 0.8, 3)
    t = {"total": tot, "intro": 22.41, "items": items, "markers": markers, "acts": acts, "_master": "srt_measured_t21_20261122"}
    json.dump(t, open(W/f"timeline_s{suf}_t21.json", "w", encoding="utf-8", newline="\n"), ensure_ascii=False, indent=1)
    raw = subprocess.run([FF, "-v", "error", "-i", str(mp3), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.int16).astype(np.float32)/32768; fr = 320
    rms = np.sqrt(np.convolve(x**2, np.ones(fr)/fr, "same")[::fr]); thr = max(0.01, np.percentile(rms, 20)*2.5); v = rms > thr
    inv = []; gapv = []; prev_end = 0
    for it in items:
        a, b = int(it["start"]*50), int(it["end"]*50); inv.append(v[a:b].mean())
        if prev_end and a-prev_end > 10: gapv.append(v[prev_end+3:a-3].mean())
        prev_end = b
    # khoang giong dai nhat ngoai item (mat giong?)
    rep[lang or "VI"] = dict(cues=len(cues), items=len(items), leftover_cues=leftover, text_mismatch=bad[:10], n_bad=len(bad), total=tot,
        last_end=items[-1]["end"], voiced_in_items=round(float(np.mean(inv)), 3), min_item=round(float(min(inv)), 3),
        argmin=items[int(np.argmin(inv))]["id"], voiced_in_gaps=round(float(np.mean(gapv)), 3) if gapv else None)
    print(lang or "VI", rep[lang or "VI"], flush=True)
