import os

reports = [
    'BaoCao_ThongKe_ChiTiet_68_Tap_VuAn.md',
    '90_LUU_TRU/BaoCao_ThongKe_ChiTiet_68_Tap_VuAn_20261122.md',
    '.work/BAO_CAO_CHI_TIET_68_TAP.md'
]

for r in reports:
    if os.path.exists(r):
        c = open(r, encoding='utf-8').read()
        c = c.replace('02_SAN_XUAT/Tap', '02_SAN_XUAT/Ho_So_Toi_Pham/Tap')
        c = c.replace('02_SAN_XUAT\\Tap', '02_SAN_XUAT\\Ho_So_Toi_Pham\\Tap')
        open(r, 'w', encoding='utf-8').write(c)
        print(f"Updated {r}")

print("All reports updated successfully!")
