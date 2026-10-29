from pathlib import Path

p = Path(".work/build_audio3.py")
content = p.read_text(encoding="utf-8")

old_click = '''    for cid in ED.EP["click_cues"]:
        at = next(m["at"] for m in markers if m.get("id") == cid)
        place(sfx, c, at - 0.30)'''

new_click = '''    for cid in ED.EP["click_cues"]:
        m_at = next((m["at"] for m in markers if m.get("id") == cid), None)
        if m_at is None:
            m_at = next((it["start"] for it in items if it.get("id") == cid or it.get("element") == cid), None)
        if m_at is not None:
            place(sfx, c, m_at - 0.30)'''

if old_click in content:
    content = content.replace(old_click, new_click, 1)
    p.write_text(content, encoding="utf-8")
    print("Patched click_cues in build_audio3.py successfully!")
else:
    print("ERROR: old_click not found in build_audio3.py!")
