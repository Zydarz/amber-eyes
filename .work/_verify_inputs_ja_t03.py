import hashlib, os, time, json

root = r'D:/TEST/Gax/amber-eyes'
files = [
    '.work/timeline_s_JA_t03.json',
    '.work/shots_JA_t03.json',
    '.work/build_video3.py',
    '.work/edition.py',
    '.work/package.py',
    '.work/parse_shots.py',
    '.work/subtitles.py',
    '02_SAN_XUAT/Tap03_JA/KeHoach_Video_Tap03_JA.md',
    '.work/shots_text_tap03_JA.json',
    '.work/audio_master_JA_t03.wav',
    'assets/brand/intro_kenh_JA_t03.mov',
]
for f in files:
    p = os.path.join(root, f)
    if not os.path.exists(p):
        print('MISSING  ', f)
        continue
    b = open(p, 'rb').read()
    mt = time.strftime('%H:%M:%S', time.localtime(os.path.getmtime(p)))
    print('%-52s %s %10d B  %s' % (f, mt, len(b), hashlib.sha256(b).hexdigest()[:12]))

# noi dung quan trong
tl = json.load(open(os.path.join(root, '.work/timeline_s_JA_t03.json'), encoding='utf-8'))
print('\ntimeline.total =', tl.get('total'))
shots = json.load(open(os.path.join(root, '.work/shots_JA_t03.json'), encoding='utf-8'))
if isinstance(shots, dict):
    print('shots keys:', list(shots.keys())[:10])
    arr = shots.get('shots', [])
else:
    arr = shots
print('shots count =', len(arr))
last = arr[-1]
print('last shot id =', last.get('id'), 'end =', last.get('end'), 'dur =', last.get('dur'))
print('shot ids unique =', len(set(s.get('id') for s in arr)) == len(arr))
