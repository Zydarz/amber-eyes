from pathlib import Path

p = Path(".work/edition.py")
content = p.read_text(encoding="utf-8")

old = '"thumb": ("BẢN ÁN GIẾT NGƯỜI", "BẰNG TIN NHẮN"),'
new = '"thumb_bg": "t7_digital_coercion_screen", "thumb": ("BẢN ÁN GIẾT NGƯỜI", "BẰNG TIN NHẮN"),'

if old in content:
    content = content.replace(old, new, 1)
    p.write_text(content, encoding="utf-8")
    print("Added thumb_bg to edition.py")
else:
    print("ERROR: old string not found in edition.py")
