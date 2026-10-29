# -*- coding: utf-8 -*-
"""Vòng 2 chọn giọng 3 vai: (1) ổn định danh tính khi đổi cảm xúc, (2) bộ ba có tách bạch không."""
import json, sys, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import voice_cast_test as V
OUT = V.OUT / "vong2"; OUT.mkdir(parents=True, exist_ok=True)
FIN = {"H": ["English_CaptivatingStoryteller", "English_Deep-VoicedGentleman"],
       "D": ["Korean_ColdYoungMan", "English_ReservedYoungMan", "Korean_IntellectualMan"],
       "C": ["English_AssertiveQueen", "English_MatureBoss"]}
EMO = ["neutral", "sad", "fearful", "surprised"]
jobs = [(r, v, e, V.ROLES[r]["cau"][0], f"{r}_{V.safe(v)}_{e}") for r in FIN for v in FIN[r] for e in EMO]
todo = [j for j in jobs if not (OUT / (j[4] + ".mp3")).exists()]
for b in range(0, len(todo), 10):
    batch = todo[b:b + 10]
    req = [{"text": t, "voice_id": v, "emotion": e, "speed": V.ROLES[r]["speed"], "pitch": 0, "volume": 1.0, "output_file": f}
           for r, v, e, t, f in batch]
    af = OUT / f"_a{b // 10}.json"; af.write_text(json.dumps({"requests": req}, ensure_ascii=False), encoding="utf-8")
    res = V.mcode(["connector", "call", "connector__matrix__batch_text_to_audio", "--args-file", str(af)])
    for it in res.get("success_items", []):
        urllib.request.urlretrieve(V.mcode(["get_asset_url", it["node_id"]], 120)["download_url"], OUT / it["file_name"])
    print("TTS", res.get("total_success"), "/", len(batch), flush=True)
def ask(path, prompt):
    url = V.mcode(["upload-temp-url", str(path)], 300)["temp_url"]
    af = OUT / "_q.json"; af.write_text(json.dumps({"audio_info": [{"url": url, "mime_type": "audio/mpeg", "prompt": prompt}]}, ensure_ascii=False), encoding="utf-8")
    r = V.mcode(["connector", "call", "connector__matrix__audios_understand", "--args-file", str(af)], 900)
    return (r.get("results") or [{}])[0].get("description", json.dumps(r)[:300])
res = {"stab": {}, "trio": {}}
for r in FIN:
    for v in FIN[r]:
        p = OUT / f"stab_{r}_{V.safe(v)}.mp3"
        V.join([OUT / f"{r}_{V.safe(v)}_{e}.mp3" for e in EMO], p)
        res["stab"][v] = ask(p, "4 readings of the SAME Vietnamese sentence, ~1 s apart. Judge only VOICE IDENTITY (timbre, age, accent). "
                                "Do all 4 sound like ONE person? Answer: number of distinct speakers, then which readings differ and how, in 2 lines.")
        print("ổn định", v, flush=True)
TRIOS = {"A": ("English_CaptivatingStoryteller", "Korean_ColdYoungMan", "English_AssertiveQueen"),
         "B": ("English_Deep-VoicedGentleman", "Korean_ColdYoungMan", "English_MatureBoss"),
         "C": ("English_CaptivatingStoryteller", "English_ReservedYoungMan", "English_AssertiveQueen")}
for k, (h, d, c) in TRIOS.items():
    clips = []
    for i in (0, 1):
        clips += [V.OUT / f"H_{V.safe(h)}_{i}.mp3", V.OUT / f"D_{V.safe(d)}_{i}.mp3", V.OUT / f"C_{V.safe(c)}_{i}.mp3"]
    p = OUT / f"trio_{k}.mp3"; V.join(clips, p)
    res["trio"][k] = ask(p, "6 Vietnamese readings ~1 s apart from a true-crime podcast. Ignore words; judge VOICE IDENTITY. "
        "1) How many distinct speakers? 2) Label each reading (S1, S2...). 3) Describe each speaker in 5 words (gender, age, pitch, character). "
        "4) Rate 1-10 how clearly distinct the speakers are from each other, and name any pair that is easy to confuse. "
        "5) Rate 1-10 each: S for reading1 as 'warm deep narrator', reading2 as 'cold detached investigator', reading3 as 'emphatic psychologist'. Compact.")
    print("bộ ba", k, flush=True)
(OUT / "ketqua.json").write_text(json.dumps(res, ensure_ascii=False, indent=1), encoding="utf-8")
