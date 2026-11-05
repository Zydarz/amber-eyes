import json

t = json.load(open(".work/temp_verify_en_t02.json", encoding="utf-8"))
b = json.load(open(".work/_cu/script_tap02_EN_bak.json", encoding="utf-8"))

for et, eb in zip(t, b):
    if et != eb:
        print(f"Diff in element {et['id']}:")
        st = [s['id'] for s in et.get('sentences', [])]
        sb = [s['id'] for s in eb.get('sentences', [])]
        print(f"  t sentences: {st}")
        print(f"  b sentences: {sb}")
