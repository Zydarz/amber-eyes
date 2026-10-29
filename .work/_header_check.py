import io, re, os

SRC = {'01': 'Tap01/kichban_tap01_22102026_v2.md',
       '02': 'Tap02/kichban_tap02_22102026.md',
       '03': 'Tap03/kichban_tap03_22102026.md'}
for n in range(4, 30):
    SRC['%02d' % n] = 'Tap%02d/kichban_tap%02d_23102026.md' % (n, n)

bad = 0
for tap in sorted(SRC):
    kp = '01_KICH_BAN/Tap%s_KO/kichban_tap%s_KO.md' % (tap, tap)
    if not os.path.exists(kp):
        print('Tap%s: MISSING' % tap)
        bad += 1
        continue
    t = io.open(kp, encoding='utf-8').read()
    head = t.split('\n## 막 1')[0]
    if int(tap) <= 18:
        need = ['# 범죄심리 오디오 / 팟캐스트 스크립트 — 한국어판',
                '**주제:**', '**원본:**', '## 제작 브리프(PRODUCTION BRIEF)']
        ok = all(x in head for x in need) and ('**버전:**' in head or '**사실 및 법률 검토:**' in head)
        detail = [x for x in need if x not in head]
        if '**버전:**' not in head and '**사실 및 법률 검토:**' not in head:
            detail.append('**버전:**/**사실 및 법률 검토:**')
    else:
        need = ['## 배역표 및 음성 구성']
        ok = head.startswith('# ') and all(x in head for x in need) and re.search(r'^\* \*\*.+:\*\*', head, re.M)
        detail = [x for x in need if x not in head]
        if not head.startswith('# '):
            detail.append('# title')
        if not re.search(r'^\* \*\*.+:\*\*', head, re.M):
            detail.append('bullet meta')
    # thống kê role label + act + pause
    roles = sorted(set(re.findall(r'^\*\*(\w+)\*\*', t, re.M)))
    acts = sorted(set(int(x) for x in re.findall(r'^## 막 (\d+)', t, re.M)))
    pauses = sorted(set(re.findall(r'\*\*\[정지 ([\d.]+)초\]\*\*', t)))
    print('Tap%s %-5s roles=%-42s acts=%s pauses=%s %s' % (
        tap, 'OK' if ok else 'BAD', ','.join(roles), acts, pauses, ('<- ' + ','.join(detail)) if detail else ''))
    if not ok:
        bad += 1
print()
print('header problems:', bad)
