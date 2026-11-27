# BÁO CÁO SỐ CÂU THOẠI & SỐ ẢNH NỀN CẦN THIẾT (140 TẬP — BẪY TÂM LÝ VÀ HÀNH VI)

> **Căn cứ luật shot (AGENTS.md — H22 & H25):**
> - Mặc định mỗi câu thoại có lời là 1 shot (trừ các câu liền mạch cùng khoảnh khắc có thể gộp).
> - **Mục tiêu chuẩn (H22/H25):** **1,5 – 2 shot / ảnh nền** (ceil(số câu / 2) đến ceil(số câu / 1,5)).
> - **Giới hạn tối thiểu không vi phạm trần H22 (≤ 3 shot/nền):** ceil(số câu / 3).

## 1. Tổng hợp toàn series
- **Tổng số chuyên đề:** 14
- **Tổng số tập:** 140
- **Tổng số câu thoại:** 27,393
- **Số ảnh nền tối thiểu (trần H22, 3 shot/nền):** 9,181 ảnh
- **Số ảnh nền mục tiêu chuẩn (1,5–2 shot/nền):** **13,730 – 18,311 ảnh**

## 2. Tổng hợp theo Chuyên đề
| Chuyên đề | Số tập | Tổng câu thoại | Tối thiểu H22 (3 shot/nền) | Mục tiêu chuẩn (1,5–2 shot/nền) |
|---|---:|---:|---:|---:|
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | 10 | 2,085 | 699 | 1,045 – 1,394 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | 10 | 1,925 | 647 | 965 – 1,288 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | 10 | 1,921 | 644 | 962 – 1,285 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | 10 | 1,986 | 665 | 996 – 1,327 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | 10 | 1,973 | 662 | 988 – 1,319 |
| ChuyenDe05_DauTri_PhongThamVan | 10 | 1,871 | 627 | 937 – 1,251 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | 10 | 1,819 | 608 | 913 – 1,215 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | 10 | 1,924 | 646 | 965 – 1,287 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | 10 | 1,859 | 624 | 934 – 1,242 |
| ChuyenDe09_TriNho_NhanChung_AnOan | 10 | 2,033 | 680 | 1,019 – 1,357 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | 10 | 1,937 | 649 | 969 – 1,295 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | 10 | 2,030 | 680 | 1,017 – 1,357 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | 10 | 2,015 | 674 | 1,010 – 1,346 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | 10 | 2,015 | 676 | 1,010 – 1,348 |

## 3. Chi tiết từng tập (140 tập)
| Chuyên đề | Tập | File kịch bản | Số câu thoại | Tối thiểu H22 | Mục tiêu chuẩn (1,5–2 shot/nền) |
|---|---|---|---:|---:|---:|
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap01 | kichban_tap01.md | 232 | 78 | 116 – 155 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap02 | kichban_tap02.md | 246 | 82 | 123 – 164 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap03 | kichban_tap03.md | 221 | 74 | 111 – 148 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap04 | kichban_tap04.md | 203 | 68 | 102 – 136 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap05 | kichban_tap05.md | 197 | 66 | 99 – 132 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap06 | kichban_tap06.md | 202 | 68 | 101 – 135 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap07 | kichban_tap07.md | 199 | 67 | 100 – 133 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap08 | kichban_tap08.md | 195 | 65 | 98 – 130 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap09 | kichban_tap09.md | 196 | 66 | 98 – 131 |
| ChuyenDe00_BayHaoQuang_AoTuongThuAc | Tap10 | kichban_tap10.md | 194 | 65 | 97 – 130 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap11 | kichban_tap11.md | 194 | 65 | 97 – 130 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap12 | kichban_tap12.md | 193 | 65 | 97 – 129 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap13 | kichban_tap13.md | 193 | 65 | 97 – 129 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap14 | kichban_tap14.md | 193 | 65 | 97 – 129 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap15 | kichban_tap15.md | 190 | 64 | 95 – 127 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap16 | kichban_tap16.md | 190 | 64 | 95 – 127 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap17 | kichban_tap17.md | 191 | 64 | 96 – 128 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap18 | kichban_tap18.md | 194 | 65 | 97 – 130 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap19 | kichban_tap19.md | 193 | 65 | 97 – 129 |
| ChuyenDe01_TuBaoChua_CatDutDaoDuc | Tap20 | kichban_tap20.md | 194 | 65 | 97 – 130 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap21 | kichban_tap21.md | 196 | 66 | 98 – 131 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap22 | kichban_tap22.md | 200 | 67 | 100 – 134 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap23 | kichban_tap23.md | 194 | 65 | 97 – 130 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap24 | kichban_tap24.md | 194 | 65 | 97 – 130 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap25 | kichban_tap25.md | 190 | 64 | 95 – 127 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap26 | kichban_tap26.md | 188 | 63 | 94 – 126 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap27 | kichban_tap27.md | 183 | 61 | 92 – 122 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap28 | kichban_tap28.md | 191 | 64 | 96 – 128 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap29 | kichban_tap29.md | 193 | 65 | 97 – 129 |
| ChuyenDe02_BoBaBongToi_ThaiNhanCach | Tap30 | kichban_tap30.md | 192 | 64 | 96 – 128 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap31 | kichban_tap31.md | 192 | 64 | 96 – 128 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap32 | kichban_tap32.md | 193 | 65 | 97 – 129 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap33 | kichban_tap33.md | 207 | 69 | 104 – 138 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap34 | kichban_tap34.md | 211 | 71 | 106 – 141 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap35 | kichban_tap35.md | 200 | 67 | 100 – 134 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap36 | kichban_tap36.md | 191 | 64 | 96 – 128 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap37 | kichban_tap37.md | 199 | 67 | 100 – 133 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap38 | kichban_tap38.md | 194 | 65 | 97 – 130 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap39 | kichban_tap39.md | 201 | 67 | 101 – 134 |
| ChuyenDe03_QuyDaoLeoThang_DiemGayTamLy | Tap40 | kichban_tap40.md | 198 | 66 | 99 – 132 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap41 | kichban_tap41.md | 201 | 67 | 101 – 134 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap42 | kichban_tap42.md | 194 | 65 | 97 – 130 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap43 | kichban_tap43.md | 190 | 64 | 95 – 127 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap44 | kichban_tap44.md | 196 | 66 | 98 – 131 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap45 | kichban_tap45.md | 199 | 67 | 100 – 133 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap46 | kichban_tap46.md | 198 | 66 | 99 – 132 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap47 | kichban_tap47.md | 197 | 66 | 99 – 132 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap48 | kichban_tap48.md | 196 | 66 | 98 – 131 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap49 | kichban_tap49.md | 202 | 68 | 101 – 135 |
| ChuyenDe04_ThaoTung_KiemSoatTamLy | Tap50 | kichban_tap50.md | 200 | 67 | 100 – 134 |
| ChuyenDe05_DauTri_PhongThamVan | Tap51 | kichban_tap51.md | 192 | 64 | 96 – 128 |
| ChuyenDe05_DauTri_PhongThamVan | Tap52 | kichban_tap52.md | 196 | 66 | 98 – 131 |
| ChuyenDe05_DauTri_PhongThamVan | Tap53 | kichban_tap53.md | 190 | 64 | 95 – 127 |
| ChuyenDe05_DauTri_PhongThamVan | Tap54 | kichban_tap54.md | 158 | 53 | 79 – 106 |
| ChuyenDe05_DauTri_PhongThamVan | Tap55 | kichban_tap55.md | 192 | 64 | 96 – 128 |
| ChuyenDe05_DauTri_PhongThamVan | Tap56 | kichban_tap56.md | 177 | 59 | 89 – 118 |
| ChuyenDe05_DauTri_PhongThamVan | Tap57 | kichban_tap57.md | 190 | 64 | 95 – 127 |
| ChuyenDe05_DauTri_PhongThamVan | Tap58 | kichban_tap58.md | 197 | 66 | 99 – 132 |
| ChuyenDe05_DauTri_PhongThamVan | Tap59 | kichban_tap59.md | 194 | 65 | 97 – 130 |
| ChuyenDe05_DauTri_PhongThamVan | Tap60 | kichban_tap60.md | 185 | 62 | 93 – 124 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap61 | kichban_tap61.md | 176 | 59 | 88 – 118 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap62 | kichban_tap62.md | 165 | 55 | 83 – 110 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap63 | kichban_tap63.md | 177 | 59 | 89 – 118 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap64 | kichban_tap64.md | 179 | 60 | 90 – 120 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap65 | kichban_tap65.md | 183 | 61 | 92 – 122 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap66 | kichban_tap66.md | 189 | 63 | 95 – 126 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap67 | kichban_tap67.md | 191 | 64 | 96 – 128 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap68 | kichban_tap68.md | 186 | 62 | 93 – 124 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap69 | kichban_tap69.md | 190 | 64 | 95 – 127 |
| ChuyenDe06_TamLyHocHienTruong_HanhViPhapY | Tap70 | kichban_tap70.md | 183 | 61 | 92 – 122 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap71 | kichban_tap71.md | 191 | 64 | 96 – 128 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap72 | kichban_tap72.md | 191 | 64 | 96 – 128 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap73 | kichban_tap73.md | 188 | 63 | 94 – 126 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap74 | kichban_tap74.md | 197 | 66 | 99 – 132 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap75 | kichban_tap75.md | 196 | 66 | 98 – 131 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap76 | kichban_tap76.md | 183 | 61 | 92 – 122 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap77 | kichban_tap77.md | 196 | 66 | 98 – 131 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap78 | kichban_tap78.md | 187 | 63 | 94 – 125 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap79 | kichban_tap79.md | 196 | 66 | 98 – 131 |
| ChuyenDe07_TamLyHocDamDong_DiemMuXaHoi | Tap80 | kichban_tap80.md | 199 | 67 | 100 – 133 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap81 | kichban_tap81.md | 178 | 60 | 89 – 119 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap82 | kichban_tap82.md | 189 | 63 | 95 – 126 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap83 | kichban_tap83.md | 163 | 55 | 82 – 109 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap84 | kichban_tap84.md | 183 | 61 | 92 – 122 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap85 | kichban_tap85.md | 193 | 65 | 97 – 129 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap86 | kichban_tap86.md | 193 | 65 | 97 – 129 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap87 | kichban_tap87.md | 191 | 64 | 96 – 128 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap88 | kichban_tap88.md | 195 | 65 | 98 – 130 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap89 | kichban_tap89.md | 187 | 63 | 94 – 125 |
| ChuyenDe08_NanNhanHoc_CamNangSinhTon | Tap90 | kichban_tap90.md | 187 | 63 | 94 – 125 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap91 | kichban_tap91.md | 205 | 69 | 103 – 137 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap92 | kichban_tap92.md | 214 | 72 | 107 – 143 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap93 | kichban_tap93.md | 207 | 69 | 104 – 138 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap94 | kichban_tap94.md | 204 | 68 | 102 – 136 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap95 | kichban_tap95.md | 203 | 68 | 102 – 136 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap96 | kichban_tap96.md | 198 | 66 | 99 – 132 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap97 | kichban_tap97.md | 205 | 69 | 103 – 137 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap98 | kichban_tap98.md | 204 | 68 | 102 – 136 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap99 | kichban_tap99.md | 201 | 67 | 101 – 134 |
| ChuyenDe09_TriNho_NhanChung_AnOan | Tap100 | kichban_tap100.md | 192 | 64 | 96 – 128 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap101 | kichban_tap101.md | 188 | 63 | 94 – 126 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap102 | kichban_tap102.md | 192 | 64 | 96 – 128 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap103 | kichban_tap103.md | 193 | 65 | 97 – 129 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap104 | kichban_tap104.md | 190 | 64 | 95 – 127 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap105 | kichban_tap105.md | 194 | 65 | 97 – 130 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap106 | kichban_tap106.md | 186 | 62 | 93 – 124 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap107 | kichban_tap107.md | 194 | 65 | 97 – 130 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap108 | kichban_tap108.md | 202 | 68 | 101 – 135 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap109 | kichban_tap109.md | 198 | 66 | 99 – 132 |
| ChuyenDe10_TamThanHocPhapY_RanhGioiBenhLy | Tap110 | kichban_tap110.md | 200 | 67 | 100 – 134 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap111 | kichban_tap111.md | 203 | 68 | 102 – 136 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap112 | kichban_tap112.md | 204 | 68 | 102 – 136 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap113 | kichban_tap113.md | 202 | 68 | 101 – 135 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap114 | kichban_tap114.md | 203 | 68 | 102 – 136 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap115 | kichban_tap115.md | 202 | 68 | 101 – 135 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap116 | kichban_tap116.md | 202 | 68 | 101 – 135 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap117 | kichban_tap117.md | 204 | 68 | 102 – 136 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap118 | kichban_tap118.md | 203 | 68 | 102 – 136 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap119 | kichban_tap119.md | 204 | 68 | 102 – 136 |
| ChuyenDe11_SinhHocThanKinh_TamLyHocPhatTrien | Tap120 | kichban_tap120.md | 203 | 68 | 102 – 136 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap121 | kichban_tap121.md | 203 | 68 | 102 – 136 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap122 | kichban_tap122.md | 200 | 67 | 100 – 134 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap123 | kichban_tap123.md | 199 | 67 | 100 – 133 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap124 | kichban_tap124.md | 198 | 66 | 99 – 132 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap125 | kichban_tap125.md | 202 | 68 | 101 – 135 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap126 | kichban_tap126.md | 201 | 67 | 101 – 134 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap127 | kichban_tap127.md | 203 | 68 | 102 – 136 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap128 | kichban_tap128.md | 204 | 68 | 102 – 136 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap129 | kichban_tap129.md | 204 | 68 | 102 – 136 |
| ChuyenDe12_TamLyDongPham_CongHuongDienLoan_NhaTu | Tap130 | kichban_tap130.md | 201 | 67 | 101 – 134 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap131 | kichban_tap131.md | 197 | 66 | 99 – 132 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap132 | kichban_tap132.md | 198 | 66 | 99 – 132 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap133 | kichban_tap133.md | 199 | 67 | 100 – 133 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap134 | kichban_tap134.md | 200 | 67 | 100 – 134 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap135 | kichban_tap135.md | 203 | 68 | 102 – 136 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap136 | kichban_tap136.md | 205 | 69 | 103 – 137 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap137 | kichban_tap137.md | 200 | 67 | 100 – 134 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap138 | kichban_tap138.md | 202 | 68 | 101 – 135 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap139 | kichban_tap139.md | 205 | 69 | 103 – 137 |
| ChuyenDe13_KyNgheXaHoi_TamLyToiPhamKyNguyenSo | Tap140 | kichban_tap140.md | 206 | 69 | 103 – 138 |