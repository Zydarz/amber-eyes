from pathlib import Path

p = Path(".work/build_audio3.py")
content = p.read_text(encoding="utf-8")

old_186 = '    cue_112 = next(m["at"] for m in markers if m.get("id") == ED.EP["act1_cue"])'
new_186 = '''    cue_112_m = next((m for m in markers if m.get("id") == ED.EP["act1_cue"]), None)
    cue_112 = cue_112_m.get("at", cue_112_m.get("start", 23.0)) if cue_112_m else 23.0'''

old_230 = '''    # "nhạc nền dừng đột ngột" (mốc của tập): mute melodic beds, ambient floor stays
    m109 = next(m for m in markers if m.get("id") == ED.EP["silence_cue"])
    i, j = int(m109["start"] * SR), int(m109["end"] * SR)
    music[i:j] = floor[i:j]'''

new_230 = '''    # "nhạc nền dừng đột ngột" (mốc của tập): mute melodic beds, ambient floor stays
    silence_id = ED.EP.get("silence_cue")
    m109 = next((m for m in markers if m.get("id") == silence_id), None)
    if m109 and "start" in m109 and "end" in m109:
        i, j = int(m109["start"] * SR), int(m109["end"] * SR)
        music[i:j] = floor[i:j]'''

if old_186 in content and old_230 in content:
    content = content.replace(old_186, new_186, 1)
    content = content.replace(old_230, new_230, 1)
    p.write_text(content, encoding="utf-8")
    print("Patched build_audio3.py safely!")
else:
    print("ERROR: Targets not found in build_audio3.py!")
