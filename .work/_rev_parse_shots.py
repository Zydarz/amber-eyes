import json, re, sys
from pathlib import Path
sys.stdout.reconfigure(encoding='utf-8')

print("=== 6. THỬ NGHIỆM CHẠY PARSE_SHOTS VỚI KEHOACH_VIDEO_TAP05.MD ===")
sys.path.insert(0, '.work')

# Create a temporary timeline for dry-run testing of parse_shots
script = json.load(open(".work/script_tap05.json", encoding="utf-8"))
items = []
markers = [{"type": "INTRO", "start": 0.0, "end": 22.41}]
t = 23.0
acts = {}
cur_act = None
for e in script:
    act = e["act"]
    if cur_act is not None and act != cur_act:
        markers.append({"type": "ACT", "act": act, "start": round(t, 3), "end": round(t + 2.0, 3)})
        t += 2.0
    cur_act = act
    if act not in acts:
        acts[act] = [t, t]
    if e["kind"] == "NGHI":
        markers.append({"type": "NGHI", "id": e["id"], "start": round(t, 3), "end": round(t + e["sec"], 3), "desc": e.get("desc", "")})
        t += e["sec"]
    elif e["kind"] in ("SFX", "BGM"):
        markers.append({"type": e["kind"], "id": e["id"], "at": round(t, 3), "desc": e.get("desc", "")})
    else:
        for s in e["sentences"]:
            d = 3.0  # estimate 3s per sentence
            items.append({"id": s["id"], "element": e["id"], "act": act, "role": e["role"], "start": round(t, 3), "end": round(t + d, 3), "text": s["text"]})
            t += d + 0.35
    acts[act][1] = t

dummy_tl = {
    "total": round(t + 9.0, 3),
    "intro": 22.41,
    "items": items,
    "markers": markers,
    "acts": {str(k): [round(a, 3), round(b, 3)] for k, (a, b) in acts.items()}
}

Path(".work/timeline_s_t05.json").write_text(json.dumps(dummy_tl, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"Đã tạo dummy timeline: {len(items)} câu, tổng thời lượng mô phỏng: {dummy_tl['total']:.1f} s")

# Now run parse_shots logic with AE_EP=05
import os
os.environ["AE_EP"] = "05"
import edition as ED
# Re-import parse_shots logic
from parse_shots import sent_range, parse_text, cells

PLAN = Path("02_SAN_XUAT/Tap05/KeHoach_Video_Tap05.md")
TL = dummy_tl
SENT = {it["id"]: it for it in TL["items"]}
MARK = {m.get("id"): m for m in TL["markers"] if m.get("id")}
ACTS = [m for m in TL["markers"] if m["type"] == "ACT"]
BG_FILES = {p.stem for p in Path("assets/bg").glob("*.png")}

text = PLAN.read_text(encoding="utf-8")
m = re.search(r"^## 6\. DANH SÁCH SHOT.*$", text, re.M)
sec = text[m.end():]
sec = sec[: re.search(r"^\*\*Tổng:", sec, re.M).start()]
rows = [cells(l) for l in sec.splitlines() if re.match(r"\|\s*[1-5]-\d+", l)]

shots = []
first_voice = TL["items"][0]["start"]
end_voice = TL["items"][-1]["end"]
for r in rows:
    sid, cau, vai, mau, nen, chu, beat, nv, tr = (r + [""] * 9)[:9]
    act = int(sid.split("-")[0])
    sents = sent_range(cau)
    if sents:
        start = SENT[sents[0]]["start"] - 0.20
        end = SENT[sents[-1]]["end"]
    elif "chuyển hồi" in cau:
        m = next(a for a in ACTS if a["act"] == act + 1)
        start, end = m["start"], m["end"]
    elif sid == "1-00":
        start, end = 20.5, first_voice - 0.20
    elif r is rows[-1]:
        start, end = end_voice, TL["total"]
    else:
        codes = re.findall(r"`(\d\.\d+)`", cau)
        ms = [MARK[c] for c in codes if c in MARK and "start" in MARK[c]]
        if not ms:
            raise SystemExit(f"không tìm thấy mốc cho {sid}: {cau}")
        start, end = ms[0]["start"], ms[-1]["end"]
    tm = re.search(r"T(\d+)", mau)
    template = f"T{tm.group(1)}" if tm else None
    codes = re.findall(r"`([a-z_0-9]+)`", nen)
    bg = next((c for c in codes if c in BG_FILES), None)
    if bg is None and template == "T10":
        bg = "void"
    cam = ("hero" if "hero" in mau else "pull" if "`pull`" in nen else "pan" if "`pan`" in nen else "still" if "`still`" in nen else "push")
    shots.append({"id": sid, "act": act, "start": round(start, 3), "end": round(end, 3), "sentences": sents, "bg": bg, "template": template})

print(f"-> PARSE THÀNH CÔNG: {len(shots)} shot!")
missing_bgs = [s['id'] for s in shots if s['bg'] is None and not s.get('hold')]
print(f"Shot thiếu nền: {len(missing_bgs)}")
