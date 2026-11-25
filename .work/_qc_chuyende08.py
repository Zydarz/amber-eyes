import sys
sys.path.append('.work')
from parse_kichban import parse_file

base = '01_KICH_BAN/BayTamLyVaHanhVi/ChuyenDe08_NanNhanHoc_CamNangSinhTon'
print('=== BANG TONG HOP KIEM DO SO CAU CHUYEN DE 08 (TAP 81 DEN TAP 90) ===')
all_passed = True
for i in range(81, 91):
    path = f'{base}/Tap{i:02d}/kichban_tap{i:02d}.md'
    res = parse_file(path, '.work/_temp.json')
    sents = [s for e in res for s in e.get('sentences', [])]
    status = 'PASSED' if len(sents) >= 200 else 'FAILED'
    if status == 'FAILED':
        all_passed = False
    print(f'Tap {i:02d}: elements = {len(res):2d} | sentences = {len(sents):3d} | Status: {status}')

print('======================================================================')
print(f'KET QUA TONG THE: {"10/10 TAP DAT CHUAN XUAT SAC (>= 200 CAU)" if all_passed else "CO TAP CHUA DAT"}')
