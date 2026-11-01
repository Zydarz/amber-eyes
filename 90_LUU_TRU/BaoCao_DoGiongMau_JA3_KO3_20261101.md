# Báo cáo đo giọng mẫu vòng 3 JA/KO (ja3, ko3): vai D, C, N1 — 01/11/2026

Nguồn: `assets/voice_ref_voxcpm2_ja3/`, `_ko3/` (40 take mỗi bộ; Mac commit `f98ac1a`; log `.work/voxcpm_ja3_run.log`, `_ko3_run.log`: 40 dòng, 0 lỗi).
Đo như vòng ja2/ko2: `voxcpm_do_mau.measure(final=True)` + YIN, dải F0 ±6%. **Chưa đo CER** (chưa có ASR/chuẩn hoá JA/KO).
Kiểm chéo: `D_subbasshusky_ja3_t01/t02` ra đúng số của `D_jactrl_t01/t02` (ja2) — cùng câu mô tả + seed ⇒ VoxCPM2 tất định, phép đo ổn định.

Dải mục tiêu: D 78–88 · C 200–218 · N1 148–182 Hz.

## Kết quả

| Vai | JA (ja3) | KO (ko3) |
|---|---|---|
| D | ✅ `D_smokerbass_ja3_t02` AC 87,4 / YIN 88,9 · 27,0 s · chuẩn file đạt (F0 dao động 7,1 nc → nghe lại độ trung tính). Dự phòng `D_lowgrowl_ja3_t01` 93,0 / 93,4. 4 take khác trong dải nhưng sàn ồn −41…−50 dB hoặc dài > 28 s → loại | ❌ 16/16 take ≥ 101 Hz. Thấp nhất `D_smokerbass_ko3_t01` 101,9 / 104,4, lại lỗi −19,4 LUFS |
| C | ✅ `C_contralto_ja3_t04` 225,4 / 226,6 (sát mép trên). Dự phòng `C_deepalto_ja3_t03` 228,6 / 234,6. Lời đọc rút gọn: mọi take 19–23 s | ✅ `C_contralto_ko3_t04` 216,2 / 224,5 · `C_deepalto_ko3_t04` 225,4 / 226,2 |
| N1 | ❌ 0/12 trong dải. Thấp nhất `W6_LOW_huskycontralto_ja3_t04` 202,5 / 204,6 | ❌ 0/12. Thấp nhất `W6_LOW_lowwarm_ko3_t01` 205,1 / 208,4 · `W6_LOW_huskycontralto_ko3_t01` 205,1 / 205,6 |

Lỗi chuẩn file khác: JA `C_deepalto_ja3_t01/t02/t04` −19,5…−20,1 LUFS, vài take −16,1…−16,9 LUFS.

## Đánh giá theo G9 (cặp vai liền kề, Higgs §0 #2)

- **D~H trên giọng mẫu chỉ ~2,7 nc** (JA: D 88,9 vs H 103,7). Nhưng theo Tập 02 VN, Higgs giữ gần nguyên D rất trầm (89→91 Hz) và kéo H ~107 lên ~125–130 Hz ⇒ trên bản đọc có thể đạt ≥ 4 nc. **Chỉ kết luận được sau khi chạy thử Higgs** (§0 #1: đo trên bản Higgs đọc).
- **N1 ngoài dải nhưng có thể không cần dải đó.** Dải 148–182 Hz đặt ra để tách C với N1; ở Tập 02, N1 **không bao giờ đứng cạnh C** (chỉ cạnh H). N1 ~205 Hz vẫn cách H (~125 Hz bản đọc) và N2 (~288 Hz) xa. C~N1 trên giọng mẫu chỉ ~1,7–1,9 nc. Cần người dùng quyết định có chấp nhận không.
- **KO thiếu D.** VoxCPM2 đọc tiếng Hàn chưa cho giọng nam nào dưới 101 Hz qua 24 take (ko2 + ko3). Giọng D ~102–104 Hz nằm đúng vùng Higgs dồn về ~125 Hz ⇒ trùng H.

## Bộ ứng viên

| Vai | JA | KO |
|---|---|---|
| H | `ja2/H_vnctrl_ja_t02` | `ko2/H_koctrl_t01` |
| D | `ja3/D_smokerbass_ja3_t02` | **chưa có** |
| C | `ja3/C_contralto_ja3_t04` | `ko3/C_contralto_ko3_t04` |
| N1 | `ja3/W6_LOW_huskycontralto_ja3_t04` (ngoài dải, chờ quyết định) | `ko3/W6_LOW_huskycontralto_ko3_t01` (như JA) |
| N2 | `ja2/W5_HIGH_vnctrl_ja_t02` | `ko2/W5_HIGH_vnctrl_ko_t02` |

## Bước tiếp
1. Người dùng nghe các ứng viên (danh tính, độ trung tính).
2. JA: đủ 5 vai ⇒ cần tham số hoá chuỗi Higgs cho `AE_LANG=ja` + CER tiếng Nhật, rồi chạy thử 1 hồi đo F0/G9 trên bản đọc.
3. KO: vòng D riêng (nhiều seed hơn cho `smokerbass`/`bassgravel`), hoặc đo thử Higgs với D ~102 Hz trước khi tốn thêm lượt Mac.
