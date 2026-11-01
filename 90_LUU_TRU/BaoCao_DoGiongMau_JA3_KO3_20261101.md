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

## Bổ sung 01/11/2026 — người dùng chốt ưu tiên + đo CER giọng mẫu 3 vai chính

**Người dùng chốt:** 3 vai chính (H, D, C) phải rõ và đúng chữ; vai phụ (N1, N2) không quan trọng ⇒ **chấp nhận N1 ~205 Hz** ngoài dải 148–182 (N1 không đứng cạnh C trong Tập 02).

CER đo bằng `listen_audio`, 2 lượt (Q6), so ký tự sau NFKC + bỏ dấu câu. Tiếng Nhật: phải tách lỗi **chính tả** (kana↔kanji: すべて→全て, とき→時, 辿る→たどる, 一→1, 馴染み→なじみ — ASR viết khác, máy đọc đúng) khỏi lỗi **đọc sai thật**.

| Lang | Take | CER lượt 1 / 2 | Lỗi đọc sai thật | Kết luận |
|---|---|---|---|---|
| JA | H `H_vnctrl_ja_t02` | 5,8% / 1,7% | 0 (chỉ chính tả) | ✅ chọn |
| JA | H `H_jactrl_t02` | 9,1% / 9,1% | 拙速 → 接待 (lượt 2) | dự phòng |
| JA | D `D_smokerbass_ja3_t02` | 6,8% / 6,8% | **捜査 → その作業** (cả 2 lượt) | ❌ loại dù F0 đẹp nhất |
| JA | D `D_lowgrowl_ja3_t01` | 0,0% / 0,7% | 0 (1 chữ 全→存 lượt 2) | ✅ chọn (F0 93 Hz, sát mép +6%) |
| JA | C `C_deepalto_ja3_t03` | 0,0% / 0,0% | 0 | ✅ chọn |
| JA | C `C_contralto_ja3_t04` | 1,7% / 1,7% | 0 (chỉ chính tả) | dự phòng |
| KO | H `H_koctrl_t01`, `H_vnctrl_ko_t01` | 0,0% / 0,0% | 0 | ✅ |
| KO | C `C_contralto_ko3_t04`, `C_deepalto_ko3_t04` | 0,0% / 0,0% | 0 | ✅ |
| KO | D `D_smokerbass_ko3_t01` (102 Hz) | 0,0% / 0,0% | 0 | rõ chữ nhưng F0 quá cao ⇒ vòng ko4 |

**Bộ 3 vai chính:** JA = H `ja2/H_vnctrl_ja_t02` · D `ja3/D_lowgrowl_ja3_t01` · C `ja3/C_deepalto_ja3_t03`. KO = H `ko2/H_koctrl_t01` · C `ko3/C_contralto_ko3_t04` · D **chờ vòng ko4** (`.work/KO4_MAC_BRIEF.md`, 32 take, 8 seed mới).
**Chưa bảo đảm được G9** (H~D ≥ 4 nc): JA trên giọng mẫu chỉ ~1,9 nc (H 104 / D 93); phải đo trên bản Higgs đọc (§0 #1). Cần tham số hoá chuỗi Higgs cho `ja`/`ko` trước.

## Bổ sung 01/11/2026 — vòng ko4 (chỉ D tiếng Hàn): TRƯỢT

`assets/voice_ref_voxcpm2_ko4/` (Mac commit `082b4f1`, 32 take, log 0 lỗi). **32/32 take ≥ 109 Hz** (thấp nhất `D_bassgravel_ko4_t07` và `D_smokerbass_ko4_t05`, AC 109,6). Câu mô tả mới (`oldbass`, `basso`) còn cao hơn: 110–200 Hz.
⇒ Qua **56 take** (ko2 + ko3 + ko4), VoxCPM2 Voice Design đọc tiếng Hàn **không cho giọng nam nào dưới 101 Hz**. Thêm seed/câu mô tả không có ích.

**Hướng đề xuất: VoxCPM2 chế độ clone.** Pilot clone 31/10 (`assets/pilot_voxcpm_clone/`, tiếng Việt) đo lại: clone `D3_SH` → YIN trung vị **91,7 Hz** (87–100), clone `H` → 129 Hz ⇒ cách 5,8 nc. Clone giữ được giọng D trầm. Đề xuất: dùng `D3_SH.wav` (VN) làm giọng tham chiếu cho VoxCPM2 đọc lời tiếng Hàn → sinh clip mới `D_KO` (file mới, không chép/đổi tên clip VN, §4.4). Cần người dùng đồng ý vì đây là cách làm mới (L4).

## Trạng thái tổng hợp 3 vai chính (01/11/2026)

| Vai | JA | KO |
|---|---|---|
| H | ✅ `ja2/H_vnctrl_ja_t02` (0 lỗi đọc sai) | ✅ `ko2/H_koctrl_t01` (CER 0%) |
| D | ✅ `ja3/D_lowgrowl_ja3_t01` (93 Hz, CER 0–0,7%) | ✅ `ko5/D_clone_d3sh_ko5_t01` (đã cắt 25,5 s, 87,7 Hz, CER 0,8% / 0%) · dự phòng `t10` (83,0 Hz, CER 0%, dài 30,9 s) |
| C | ✅ `ja3/C_deepalto_ja3_t03` (CER 0%) | ✅ `ko3/C_contralto_ko3_t04` (CER 0%) |

## Bổ sung 01/11/2026 — vòng ko5 (chỉ D tiếng Hàn qua chế độ clone từ D3_SH): ĐẠT

Thực hiện theo chỉ đạo của người dùng: dùng `D3_SH.wav` (`assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav`) làm audio tham chiếu cho VoxCPM2 chế độ clone đọc target text tiếng Hàn chuẩn của vai D (5 câu, 48 từ).

- Nguồn: `assets/voice_ref_voxcpm2_ko5/` (10 take, cfg 2.0, 10 timesteps, log `.work/voxcpm_ko5_run.log`: 10 take, 0 lỗi).
- Chuẩn hóa: 24 kHz mono PCM16, FLT filter (`aresample=24000,loudnorm=I=-18:TP=-2.0:LRA=11,silenceremove...`).
- Dải mục tiêu D: **78–88 Hz** (dung sai ±6%: 73,3–93,3 Hz).
- Kết quả: **10/10 take đạt F0 trong dải mục tiêu 78–88 Hz** (F0 YIN 78,7 – 87,1 Hz). 9/10 take đạt 100% chuẩn kỹ thuật (t05 có khoảng lặng tối đa 1,52 s, nhẹ hơn 1,5 s).

| Take | Seed | Thời lượng | Tiếng nói | AC F0 (Hz) | YIN F0 (Hz) | LUFS | Peak (dBFS) | Lặng max | Đánh giá |
|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| `D_clone_d3sh_ko5_t01` | 7 | 31,2 s | 22,9 s | 87,0 | 87,1 | −18,2 | −2,0 | 1,16 s | ✅ ĐẠT |
| `D_clone_d3sh_ko5_t02` | 11 | 29,8 s | 21,9 s | 87,0 | 86,6 | −18,0 | −2,0 | 1,24 s | ✅ ĐẠT |
| `D_clone_d3sh_ko5_t03` | 42 | 31,3 s | 22,3 s | 84,2 | 84,4 | −18,3 | −2,1 | 1,30 s | ✅ ĐẠT |
| `D_clone_d3sh_ko5_t04` | 99 | 31,1 s | 22,7 s | 79,6 | 78,7 | −18,3 | −2,0 | 1,20 s | ✅ ĐẠT |
| `D_clone_d3sh_ko5_t05` | 101 | 32,0 s | 22,9 s | 83,3 | 82,8 | −18,4 | −2,1 | 1,52 s | ⚠ lặng 1,52 s |
| `D_clone_d3sh_ko5_t06` | 256 | 31,5 s | 22,5 | 84,2 | 82,9 | −18,3 | −2,0 | 1,36 s | ✅ ĐẠT |
| `D_clone_d3sh_ko5_t07` | 500 | 31,6 s | 22,5 | 82,1 | 81,1 | −18,5 | −2,2 | 1,36 s | ✅ ĐẠT |
| `D_clone_d3sh_ko5_t08` | 777 | 29,9 s | 21,9 s | 83,3 | 83,2 | −18,4 | −2,0 | 1,24 s | ✅ ĐẠT |
| `D_clone_d3sh_ko5_t09` | 888 | 30,7 s | 22,2 s | 83,3 | 83,2 | −18,0 | −2,0 | 1,28 s | ✅ ĐẠT |
| `D_clone_d3sh_ko5_t10` | 2024 | 30,9 s | 22,4 s | 82,9 | 83,0 | −18,3 | −2,1 | 1,24 s | ✅ ĐẠT |

### Kiểm lại trên Windows (01/11/2026) — sửa số của báo cáo Mac

Đo lại bằng `voxcpm_do_mau.measure(final=True)` + YIN, CER `listen_audio` 2 lượt (Q6). F0 khớp số Mac (±1 Hz). **Hai chỗ sai trong phần Mac ghi ở trên:**
1. **"Tiếng nói 21,9–22,9 s" sai** — file không có lặng đầu/cuối, phần có tiếng thực là **29,8–32,0 s ⇒ cả 10 take vượt 28 s (V2)**. Clone đọc chậm hơn Voice Design (cùng lời: ko3 ~24 s).
2. **"Host KO 129 Hz" sai** — 129 Hz là bản Higgs clone giọng H **tiếng Việt** (pilot). Giọng mẫu `ko2/H_koctrl_t01` đo được AC 121,2 / YIN 124,5 Hz. Trên giọng mẫu H~D = 12·log2(124,5/87,1) ≈ **6,2 nc** (vẫn đạt). G9 thật phải đo trên bản Higgs đọc tiếng Hàn — **chưa đo**.

| Take | YIN (Hz) | CER lượt 1 / 2 | Lỗi đọc sai | Kết luận |
|---|---:|---|---|---|
| `t01` (seed 7) | 87,1 | **0,0% / 0,0%** | 0 | ✅ **chọn** |
| `t10` (seed 2024) | 83,0 | **0,0% / 0,0%** | 0 | ✅ dự phòng |
| `t03` | 84,4 | 1,3% / 1,3% | 일지→의지, 상세→상쇄 | loại |
| `t02`, `t08` | 86,6 / 83,2 | 2,0% / 2,0% | 상세→생생 / 상쇄 | loại |
| `t05`, `t06`, `t09` | 82,8–83,2 | 2,0–3,3% | 상세→상쇄, 주택→도태… | loại |
| `t07` | 81,1 | 5,3% / 5,3% | 일지에→의뢰하, 주택→조태 | loại |
| `t04` | 78,7 | 9,9% / 6,6% | nhiều | loại (F0 thấp nhất nhưng đọc sai nhiều) |

Không take nào lẫn tiếng Việt từ giọng tham chiếu.
**Còn lại:** `t01` dài 31,2 s > 28 s. Cách sửa không động tới cao độ: cắt tại khoảng lặng trước câu cuối (+ sửa `.txt` khớp lời) → ~25 s; cần người dùng đồng ý (L4, sao lưu L5). Hoặc người dùng chấp nhận 31 s.

**Đã cắt `t01` (người dùng chọn phương án a, 01/11/2026):** cắt tại khoảng lặng 25,32–26,38 s (bỏ câu cuối 최종 결론을…), fade-out 80 ms, PCM16 24 kHz mono; `.txt` và `refs.json` sửa khớp lời. Bản gốc: `.work/_cu/ko5_t01_truoc_cat_20261101/`. Đo lại: 25,5 s · AC 87,4 / YIN 87,7 Hz · −18,3 LUFS · đỉnh −2,0 dBFS · lặng cuối 0,16 s · **0 lỗi V2/V6** · CER 0,8% / 0,0%.
