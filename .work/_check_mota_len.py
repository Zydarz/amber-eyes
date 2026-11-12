import sys
sys.stdout.reconfigure(encoding='utf-8')
paths = [
    '02_SAN_XUAT/Tap01/mo_ta.txt',
    '02_SAN_XUAT/Tap01/xuat_ban/mo_ta.txt',
    '02_SAN_XUAT/Tap01_EN/mo_ta.txt',
    '02_SAN_XUAT/Tap01_JA/mo_ta.txt',
    '02_SAN_XUAT/Tap01_KO/mo_ta.txt',
    '02_SAN_XUAT/Tap02/xuat_ban/mo_ta.txt'
]
for p in paths:
    try:
        content = open(p, encoding='utf-8').read()
        print(f"{p}: {len(content)} characters, {len(content.encode('utf-8'))} bytes")
    except Exception as e:
        print(f"{p}: Error {e}")
