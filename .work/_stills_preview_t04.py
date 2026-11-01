"""Xem trước 83 shot TẬP 04 bằng timeline giả lập — để soi LAYOUT (chữ tràn,
đè nhau, sai nền, chữ lạ) TRƯỚC khi dựng video thật.

Timeline giả này COPY NGUYÊN VÍ soạn thuật toán bố trí của build_audio3.py
(dòng 120-163): FIRST_VOICE, INTRO, GAP_SENT/Q/SPEAKER/ACT, MAX_PAUSE,
PAUSE_AFTER, luật ACT marker (chỉ phát khi ĐỔI hồi), acts{act:[start,end]}.
Khac biet duy nhat: dung THOI LUONG WAV THAT cua Higgs (da tai ve) thay vi
uoc luong ao. => Moc shot sat voi video that, dung de bat loi bo cuc.

Cung cap --selection <json> de dung bien Higgs da chon (id -> variant) sau khi
do CER xong; mac dinh lay variant 0.

Chay:  py -3 .work/_stills_preview_t04.py [--selection .work/higgs_selection_t04.json]
"""
import json
import os
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = pathlib.Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"
TL = WORK / "timeline_s_t04.json"
SH = WORK / "shots_t04.json"
BK = WORK / "_cu" / "smoke_t04"

# --- hang so cua build_audio3.py (dong 36-50) ---
FIRST_VOICE = 23.0
INTRO = 22.41
GAP_SENT, GAP_Q, GAP_SPEAKER, GAP_ACT, MAX_PAUSE = 0.35, 0.60, 0.70, 2.0, 2.5

SEL = None
if "--selection" in sys.argv:
    i = sys.argv.index("--selection")
    SEL = json.loads(pathlib.Path(sys.argv[i + 1]).read_text(encoding="utf-8-sig"))

BK.mkdir(parents=True, exist_ok=True)
for p in (TL, SH):
    if p.exists():
        shutil.copy2(p, BK / p.name)

# ---------- du lieu ----------
script = json.loads((WORK / "script_tap04.json").read_text(encoding="utf-8-sig"))
man = {m["id"]: m for m in json.loads((WORK / "tts_manifest_t04.json").read_text(encoding="utf-8-sig"))}
acting = json.loads((WORK / "acting_tap04.json").read_text(encoding="utf-8-sig"))
PAUSE_AFTER = acting.get("_pause_after", {})

hm = json.loads((WORK / "kaggle_higgs" / "out_higgs_prod_t04" / "out_higgs_prod_t04"
                 / "higgs_manifest.json").read_text(encoding="utf-8-sig"))
best = {}
for h in hm:
    sid = h["id"]
    want = (SEL or {}).get(sid, 0)
    if sid not in best or (h.get("variant", 0) == want and best[sid].get("variant", 0) != want):
        best[sid] = h
DUR = {sid: h["duration_s"] for sid, h in best.items()}
missing_dur = [i["id"] for e in script for i in e.get("sentences", []) if i["id"] not in DUR]
if missing_dur:
    print("!! thieu thoi luong cho", len(missing_dur), "cau -> dung 3.0 s", missing_dur[:8])

# ---------- bo tri (mirror build_audio3.py dong 120-163) ----------
t = FIRST_VOICE
items, markers = [], [{"type": "INTRO", "start": 0.0, "end": INTRO}]
acts = {}
cur_act = None
pending = None
for e in script:
    act = e["act"]
    if cur_act is not None and act != cur_act:
        markers.append({"type": "ACT", "act": act, "start": round(t, 3), "end": round(t + GAP_ACT, 3)})
        t += GAP_ACT
        pending = None
    if act not in acts:
        acts[act] = [t, t]
    cur_act = act
    if e["kind"] == "NGHI":
        sec = min(e["sec"], MAX_PAUSE)
        markers.append({"type": "NGHI", "id": e["id"], "start": round(t, 3), "end": round(t + sec, 3),
                        "desc": e.get("desc", "")})
        t += sec
        pending = None
    elif e["kind"] in ("SFX", "BGM"):
        markers.append({"type": e["kind"], "id": e["id"], "at": round(t, 3), "desc": e.get("desc", "")})
    else:
        role = man[e["sentences"][0]["id"]]["role"]
        if pending:
            g = GAP_SPEAKER if pending[0] != role else GAP_SENT
            if pending[1].rstrip("”\" ").endswith("?"):
                g = max(g, GAP_Q)
            t += g
        for k, s in enumerate(e["sentences"]):
            d = DUR.get(s["id"], 3.0)
            items.append({"id": s["id"], "element": e["id"], "act": act, "role": role,
                          "start": round(t, 3), "end": round(t + d, 3), "text": man[s["id"]]["display"]})
            t += d
            t += PAUSE_AFTER.get(s["id"], 0.0)
            if k < len(e["sentences"]) - 1:
                t += GAP_Q if s["text"].rstrip("”\" ").endswith("?") else GAP_SENT
                if man[s["id"]]["emotion"] in ("sad", "fearful"):
                    t += 0.2
        pending = (role, e["sentences"][-1]["text"])
    acts[act][1] = t
end_voice = t
total = end_voice + 1.0 + 5.0 + 3.0
markers.sort(key=lambda m: m.get("start", m.get("at", 0)))
TL.write_text(json.dumps({"total": round(total, 3), "intro": INTRO, "items": items,
                           "markers": markers, "acts": acts}, ensure_ascii=False, indent=1),
              encoding="utf-8")
print("timeline gia: total=%.1fs  items=%d  markers=%d  acts=%s"
      % (total, len(items), len(markers), {k: [round(v[0], 1), round(v[1], 1)] for k, v in acts.items()}))

env = os.environ.copy()
env["AE_EP"] = "04"
env["PYTHONIOENCODING"] = "utf-8"
r = subprocess.run([sys.executable, str(WORK / "parse_shots.py")], cwd=str(ROOT), env=env,
                   capture_output=True, text=True, encoding="utf-8", errors="replace")
print("parse:", (r.stdout or "").strip()[-300:] or (r.stderr or "").strip()[-800:])
if r.returncode != 0:
    sys.exit("parse_shots that bai")

SD = WORK / "video3_t04" / "stills"
STILLS_ARG = "all"
if "--stills" in sys.argv:
    STILLS_ARG = sys.argv[sys.argv.index("--stills") + 1]
if SD.exists() and STILLS_ARG == "all":
    shutil.rmtree(SD)
r = subprocess.run([sys.executable, str(WORK / "build_video3.py"), "--stills", STILLS_ARG],
                   cwd=str(ROOT), env=env, capture_output=True, text=True,
                   encoding="utf-8", errors="replace")
print("stills:", (r.stdout or "").strip()[-400:] or (r.stderr or "").strip()[-1500:])
if SD.exists():
    print("so anh:", len(list(SD.glob("*.png"))), "->", SD)

# khoi phuc file goc (audio that se sinh lai)
for p in (TL, SH):
    b = BK / p.name
    if b.exists():
        shutil.copy2(b, p)
        print("da khoi phuc", p.name)
