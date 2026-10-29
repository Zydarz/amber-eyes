from pathlib import Path

p = Path(".work/edition.py")
content = p.read_text(encoding="utf-8")

old = '"act1_cue": "1.04", "silence_cue": "1.06"'
new = '"act1_cue": "1.03", "silence_cue": "2.11"'

if old in content:
    content = content.replace(old, new, 1)
    p.write_text(content, encoding="utf-8")
    print("Updated edition.py with act1_cue=1.03 and silence_cue=2.11")
else:
    print("ERROR: old string not found in edition.py")
