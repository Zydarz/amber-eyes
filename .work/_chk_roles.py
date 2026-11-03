import re, pathlib
p = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work\edition.py")
src = p.read_text(encoding="utf-8")
eps = re.findall(r'"(\d{2})"\s*:\s*\{', src)
# tim cac block EPISODES["NN"]
have = set()
for m in re.finditer(r'"(\d{2})"\s*:\s*\{', src):
    # lay 4000 ky tu sau do de tim roles_en
    seg = src[m.start(): m.start()+6000]
    if "roles_en" in seg.split('"roles_en"',1)[0] or '"roles_en"' in seg:
        # can dung: chi dem neu roles_en nam TRONG block (truoc dong ket)
        depth = 0; end = m.start()
        for i in range(m.end()-1, len(src)):
            if src[i] == '{': depth += 1
            elif src[i] == '}':
                depth -= 1
                if depth == 0: end = i; break
        blk = src[m.start():end]
        if '"roles_en"' in blk:
            have.add(m.group(1))
print("EPISODES co roles_en:", sorted(have))
print("TAP THIEU roles_en:", sorted(set(eps) - have))
