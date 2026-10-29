import io, re, sys

VIET_DIAC = set('ạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹđĐăăâêôơưĂÂÊÔƠƯ')
PAT = re.compile(r'\u2018([^\u2019\n]{2,200})\u2019|\"([^\"\n]{2,200})\"|\'([^\'\n]{2,200})\'')

for label, path in [('VN', sys.argv[1]), ('EN', sys.argv[2])]:
    t = io.open(path, encoding='utf-8').read()
    print('########', label, path)
    for m in PAT.finditer(t):
        raw = m.group(0)
        content = raw[1:-1]
        style = 'curly' if m.group(1) is not None else ('double' if m.group(2) is not None else 'straight')
        vi = any(ch in VIET_DIAC for ch in content)
        nw = len(re.findall(r'[A-Za-z]{3,}', content))
        kind = 'VN' if vi else ('EN' if nw >= 2 else '?')
        if style == 'double' and kind == '?':
            continue  # bỏ qua onomatopoeia trong ngoặc kép
        print('  [%s/%s] %s' % (style, kind, content[:130].replace('\n', ' ')))
