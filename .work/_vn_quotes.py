import io, re, sys

SRC = {'01': 'Tap01/kichban_tap01_22102026_v2.md',
       '02': 'Tap02/kichban_tap02_22102026.md',
       '03': 'Tap03/kichban_tap03_22102026.md'}
for n in range(4, 30):
    SRC['%02d' % n] = 'Tap%02d/kichban_tap%02d_23102026.md' % (n, n)

# bắt cả 3 kiểu nháy, theo thứ tự xuất hiện; bỏ qua dấu nháy đơn làm dấu nháy từ (apostrophe)
PAT = re.compile(r'\u2018([^\u2019\n]{2,200})\u2019|\"([^\"\n]{2,200})\"|\'([^\'\n]{2,200})\'')
VIET_DIAC = set('ạảấầẩẫậắằẳẵặẹẻẽếềểễệỉịọỏốồổỗộớờởỡợụủứừửữựỳỵỷỹđĐăăâêôơưĂÂÊÔƠƯ')

tap = sys.argv[1]
t = io.open('01_KICH_BAN/' + SRC[tap], encoding='utf-8').read()
for m in PAT.finditer(t):
    raw = m.group(0)
    content = raw[1:-1]
    style = 'curly' if m.group(1) is not None else ('double' if m.group(2) is not None else 'straight')
    vi = any(ch in VIET_DIAC for ch in content)
    has_ascii_words = len(re.findall(r'[A-Za-z]{3,}', content)) >= 2
    kind = 'VN' if vi else ('EN' if has_ascii_words else '?')
    ctx = t[max(0, m.start() - 55):m.start()].replace('\n', ' | ')[-55:]
    print('[%s/%s] %s' % (style, kind, content[:120].replace('\n', ' ')))
    print('      ...ctx: %s' % ctx)
