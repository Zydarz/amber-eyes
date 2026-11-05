import re
p = r"D:/TEST/Gax/amber-eyes/.work/_build_timeline_langs_t02.py"
s = open(p, encoding="utf-8").read()
s = s.replace("def rebuild(base, S, ELEM, lang, global_scale=1.0, rate=None):",
              "def rebuild(base, S, ELEM, lang, global_scale=1.0, rate=None, ROLE=None):")
s = s.replace('"act": bitems.get(i, {}).get("act", 1),\n                              "role": bitems.get(i, {}).get("role", "H"),',
              '"act": bitems.get(i, {}).get("act", 1),\n                              "role": (ROLE or {}).get(el, bitems.get(i, {}).get("role", "H")),')
s = s.replace("S, ELEM = load_script(lang)", "S, ELEM, ROLE = load_script(lang)")
s = s.replace("S, ELEM = S_KO, ELEM_KO", "S, ELEM, ROLE = S_KO, ELEM_KO, ROLE_KO")
s = s.replace("S_KO, ELEM_KO = load_script(\"KO\")", "S_KO, ELEM_KO, ROLE_KO = load_script(\"KO\")")
s = s.replace("S_JA, _ = load_script(\"JA\")", "S_JA, _, _ = load_script(\"JA\")")
s = s.replace("S_VN, _ = load_script(\"VN\")", "S_VN, _, _ = load_script(\"VN\")")
s = s.replace("tl = rebuild(base, S, ELEM, lang, global_scale=gs, rate=rate)",
              "tl = rebuild(base, S, ELEM, lang, global_scale=gs, rate=rate, ROLE=ROLE)")
open(p, "w", encoding="utf-8", newline="").write(s)
print("patched")
