import json
import re

m = json.load(open(".work/tts_manifest_EN_t02.json", encoding="utf-8"))
s = json.load(open(".work/script_tap02_EN.json", encoding="utf-8"))

s_sents = []
for e in s:
    for sent in e.get("sentences", []):
        s_sents.append(sent)

diffs = 0
for idx, (mi, si) in enumerate(zip(m, s_sents)):
    # strip ssml pauses like <#0.15#>
    mt = re.sub(r"<#[^#]+#>", "", mi["text"]).strip()
    st = si["text"].strip()
    if mt != st:
        diffs += 1
        if diffs <= 10:
            print(f"DIFF at {mi['id']}:")
            print(f"  Manifest (TTS spoken): {mt}")
            print(f"  Script               : {st}")

print(f"Total diffs: {diffs}/{len(m)}")
