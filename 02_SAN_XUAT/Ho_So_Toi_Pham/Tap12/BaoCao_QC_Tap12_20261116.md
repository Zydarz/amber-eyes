# BÁO CÁO QC ẢNH NỀN TẬP 12 — "THẢM KỊCH JONESTOWN"

*Ngày QC: 16/11/2026 · Cơ chế: Kaggle FLUX.2-klein-4B (2 kernel riêng = 2 phiên độc lập, 1 tiến trình / 1 GPU mỗi phiên)*

---

## 1. Tình trạng đầu vào

| Mục | Trước | Sau |
|---|---|---|
| Số ảnh nền trên đĩa | **83** | **152** |
| Mã nền dùng trong bảng shot | 79 | **152** |
| Shot/nền | **3,2** (vi phạm H22) | **1,64** ✅ |
| Cổng `qc_bg_usage.py --plan` | **TRƯỢT** (④ = 20 nền vượt 3 shot) | **ĐẠT** (④ = 0) |
| Job không shot nào dùng | 4 | **0** ✅ |
| Mã nền thiếu job | 0 | **0** ✅ |

---

## 2. Tách nền H25

- Bảng shot: **254 dòng · 249 câu · 5 hồi**.
- Thuật toán: cụm liền mạch (cùng mã nền ở hồi khác = cảnh khác ⇒ tách mã) → nhóm ≤ 2 shot / ≤ 30 s (≤ 28 s nếu sát thẻ chuyển hồi) → **151 nhóm + 1 nền thẻ kết = 152 mã nền**.
- **Kiểm chéo thuật toán trên Tập 11** (có audio thật): ra đúng **136 nền / 70 mã mới** — khớp lô đã sinh 16/11 ⇒ thuật toán tin cậy.
- Tập 12 **chưa có audio** ⇒ thời lượng shot **ước lượng** bằng hệ số hiệu chuẩn từ Tập 11: median 0,293 s/từ, p90 0,314 ⇒ dùng **0,32 s/từ + 0,5 s đệm**. Cổng `--plan` phải **đo lại** sau khi dựng audio thật.
- **4 ảnh "thừa" được dùng lại** (gán lại theo nguyên văn câu) thay vì xoá: `armed_guards_crossbow_perimeter` (1.07#6) · `crumbling_facade_tension` (2.02#5) · `nbc_camera_recording_facade` (1.10#6) · `leo_ryan_podium_applause` (2.04#6) · `redflag2_silenced_critical_thinking` (5.05#4) ⇒ **tiết kiệm 4 lượt sinh**, H22 ① về 0.

---

## 3. Sinh ảnh trên Kaggle (2 GPU song song)

| Lô | Kernel | Số ảnh | Seed | Thời gian |
|---|---|---|---|---|
| 1 | `chiduong2026/amber-eyes-flux2-t12-k1` | 34 | 22005–22077 | 47 phút |
| 2 | `chiduong2026/amber-eyes-flux2-t12-k2` | 35 | 22080–22152 | 47 phút |
| 3 (bỏ chữ) | `…-flux2-t12-detext-k1` / `-k2` | 3 + 4 | 33001–33007 | ~10 phút |

- **Cơ chế 2 kernel = 2 phiên Kaggle độc lập** (mỗi phiên 1 tiến trình / 1 GPU). Bằng chứng song song: 13:42:55 cả hai cùng `RUNNING`; **14:29:31 k1 COMPLETE trong khi k2 vẫn RUNNING**. Tổng 69 ảnh mất ~49 phút (≈ 75 s/ảnh); nếu tuần tự phải ~86 phút.
- Không dùng 2 worker trong cùng 1 phiên (luôn bị Linux OOM-Killer −9 — A11 #170).
- Seed khoảng riêng theo từng lô (12000+ → 22000+ → 33000+), không trùng giữa 2 kernel.

---

## 4. QC "không chữ" (H2/H5) — soi mắt 100 %

Quy trình: 5 tờ montage (4 cột × 4 hàng, ô 512 px ⇒ ~390 px sau khi resize) → soi 69 ảnh → **14 ảnh nghi** → cắt 4 góc ở độ phân giải gốc → soi zoom.

**Kết quả vòng 1: 62/69 sạch · 7/69 vi phạm (10,1 %).**

| # | Mã nền | Lỗi AI | Xử lý |
|---|---|---|---|
| 1 | `t12_archive_boxes_metal_shelf` | Ô nhãn mặt hộp lưu trữ có chữ | Vá: bỏ hẳn ô nhãn + mặt hộp trơn trọn |
| 2 | `t12_official_vehicle_closed_road` | Logo lưới xe + biển số + bảng trên cổng | Vá: lưới trơn không hãng, không biển số, cổng trơn |
| 3 | `t12_old_radio_receiver_dark` | Mặt radio có số trên dial + khung tranh trên tường có chữ | Vá: đổi thành tủ radio đóng kín, mặt trước trơn, tường không treo gì |
| 4 | `t12_reel_to_reel_archive_recorder` | Nhãn nhỏ trên mặt máy ghi âm | Vá: mặt máy trơn không nhãn, tường trống |
| 5 | `t12_sinking_bundles_muddy_road` | Nhãn trên thùng + tờ giấy có chữ | Vá: bỏ thùng/giấy, chỉ còn bó vải bọc |
| 6 | `t12_state_department_empty_corridor` | 2 khung thông báo trên tường có chữ | Vá: tường trơn không treo khung không biển |
| 7 | `t12_urgent_appeal_dark_office` | Bàn phím điện thoại có số | Vá: bàn phím trơn không số |

**Nguyên nhân chung (theo A11 #171):** prompt đã có "no text / no labels / no logos" nhưng vẫn mô tả **vật thể có sẵn "chỗ chữ"** ⇒ AI điền chữ vào. Mệnh đề phủ định không đủ; phải **bỏ hẳn vật thể / ô nhãn / khung / dial / biển số / bàn phím** và mô tả bề mặt trơn trọn.

### 4.1. Kết quả vòng 2 — 3/7 sạch tuyệt đối, 4/7 còn vết chữ AI

Soi **full-frame** (không chỉ vùng nghi) + crop 12×–16× từng nền đã sinh lại:

| Mã nền | Kết quả vòng 2 | Ghi chú |
|---|---|---|
| `t12_archive_boxes_metal_shelf` | **PASS** | Ô nhãn là khối đen rỗng, mặt hộp không chữ |
| `t12_old_radio_receiver_dark` | **PASS** | Mặt tủ kín trơn, tường không treo khung, không số trên dial |
| `t12_sinking_bundles_muddy_road` | **PASS** | Chỉ bó vải + dây thừng, không thùng/giấy có chữ |
| `t12_reel_to_reel_archive_recorder` | **TRƯỢT** | Mặt máy còn **bảng tên + hàng ký tự nhỏ + dãy số** (zoom 6× rõ) → vòng 3 |
| `t12_official_vehicle_closed_road` | **TRƯỢT** | Biển số/lưới đã sạch, nhưng nắp xe còn **badge ~12×12 px** → vòng 4 |
| `t12_urgent_appeal_dark_office` | **TRƯỢT** | Giấy trơn, nhưng **núm bàn phím còn vết trắng giống số** (zoom 12×) → vòng 4 |
| `t12_state_department_empty_corridor` | **TRƯỢT** | Khung thông báo đã bỏ, nhưng tường trái còn **khung tranh ~15×40 px có vết như chữ** (zoom 16×) → vòng 4 |

**Phân tích lỗi còn lại — 2 nguyên nhân khác nhau:**

1. **Vá bề mặt mà giữ nguyên bố cục** (máy ghi âm): vòng 2 chỉ đổi *"a completely plain front panel with no labels"* nhưng **giữ nguyên mặt phẳng điều khiển** ⇒ AI vẽ bảng tên vào đúng chỗ đó (A11 #175/#179).
2. **Vật thể nhỏ có sẵn "chỗ chữ" tự sinh** (badge ~12 px · núm bàn phím ~10 px · khung tranh ~15×40 px): dù prompt đã cấm, AI vẫn thêm — và **ở đúng cỡ mà ô montage 390 px bỏ sót** (A11 #175: nameplate 40×8 px từng bị bỏ sót).

⇒ Quyết định: **vòng 3/4 không vá bề mặt nữa mà ĐỔI BỐ CỤC** (xoay lưng máy · điện thoại úp sấp · xe đứng nghiêng / đẩy xa · hành lang nhìn thẳng không treo gì) **và KHÔNG nhắc tên vật thể mang chữ trong prompt** ("badge", "emblem", "nameplate", "keypad digits"…) vì chính từ đó gợi AI vẽ ra (A11 #171).

### 4.2. Phát hiện mới — 83 nền CŨ (sinh 13/11) chưa từng được soi sạch chữ

Trong lúc chờ GPU, đã soi **toàn bộ 83 nền có sẵn từ trước** (vòng 1 chỉ soi 69 nền mới) bằng 6 tờ montage 4×4 ô 512 px:

| Mục | Số |
|---|---|
| Nền cũ soi 100 % | **83** |
| Nền cũ có **chữ AI đọc được** (soi mắt) | **≈ 27–28 (33 %)** |
| Nền cũ có **prompt yêu cầu chữ** (quét từ khoá) | **18 (21,7 %)** |

Nền cũ dính chữ rõ nhất:

| Mã nền | Lỗi |
|---|---|
| `t12_secret_note_folded_slip` | Mảnh giấy viết tay: *"Help us get out of Jonestown."* |
| `t12_moral_courage_candle_in_dark` | Chữ trên tường: *"Life is Life's worth living"* |
| `t12_wall_francisco_temple_expansion` | Biển *"PEPPLS TEMPLE"* |
| `t12_entering_armed_compound_gate` | Biển gỗ chữ vô nghĩa |
| `t12_concerned_relatives_alliance` | Bảng tin có tiêu đề báo *"CHILDREN DEBATES"* / *"CONCERNED RELATIVES"* |
| `t12_fbi_evidence_tape_q042` | Nhãn băng: *"RYMUR FBI Record Q 042"* |
| `t12_memorial_918_names_monolith` | Bia khắc danh sách tên |
| `t12_new_west_investigative_draft` | Bản thảo đánh máy + giấy có chữ |
| `t12_property_surrender_passbooks` | Sổ tiết kiệm + giấy tờ chữ |
| `t12_press_corps_cameras_microphones` | Chữ trên máy ảnh + báo |
| `t12_confiscated_passports_trunk` | Chữ *"PASSPORT"* trên hộ chiếu |
| `t12_nbc_camera_recording_facade` | Logo trên camera |
| `t12_milgram_experiment_shock_generator` | Núm đo ghi *"VOLTS / 450 / 15…"* |
| `t12_moral_compass_unbroken` | Chữ N/E/S/W + số độ trên la bàn |
| `t12_redflag3_escalating_commitment_trap` | Số trên đồng hồ + ghi chú viết tay |
| `t12_ablation_death_desensitization` | Bảng đồ có nhãn trục + số |
| `t12_impenetrable_geographical_isolation` | Bản đồ có tên địa danh |
| `t12_utopian_promise_mirage` · `t12_charity_soup_kitchen_bread` · `t12_amber_eyes_closing_dossier_jonestown` · `t12_paranoia_cracking_dictator_man` · `t12_prefrontal_cortex_impairment` · `t12_redflag1_total_social_isolation` · `t12_fallen_reporters_and_ryan` · `t12_congressman_leo_ryan_briefing` | Chữ trên vật thể (poster · tờ rơi · bìa hồ sơ · giấy tờ · áp phích giải phẫu · badge · thẻ báo chí · sách + con dấu) |

**Nguyên nhân:** 83 nền này sinh ngày **13/11/2026** với prompt **cố ý yêu cầu chữ** ("typed label marked …", "printed community charity flyers", "inscribed with subtle lines representing 918 lost lives"…) — vi phạm nguyên tắc A11 #171 ngay từ prompt, và **chưa từng qua QC 100 %**. Danh sách: `.work/_t12/old83_textprompts.md`.

### 4.3. Vòng 3 — `reel_to_reel_archive_recorder` (2 biến thể, 2 kernel song song)

Cách vá: **xoay lưng máy** ⇒ khung hình chỉ còn **vỏ thép trơn + 2 cuộn băng**, không còn mặt phẳng điều khiển để AI đặt bảng tên. Không nhắc tên `dial / knob / nameplate` trong prompt (A11 #171).

| Biến thể | Seed | Kết quả |
|---|---|---|
| A — máy xoay 3/4 | 34001 | **SẠCH** — vỏ thép trơn, dải khe tối giữa 2 cuộn chỉ là rãnh cơ khí (zoom 16×), núm/ốc máy không ký tự. **Đã thay vào `assets/bg/`** |
| B — máy nằm nghiêng | 34002 | **SẠCH** (dự phòng) — mặt máy trơn, khe băng trống không chữ |

Cả hai biến thể đều sạch ⇒ **vòng 3 thành công**, giữ biến thể A (máy đứng trên kệ khớp mô tả shot 3.07#6–3.07#7).

> Ghi chú hạn tầm Kaggle: khi push kernel thứ 3 ⇒ lỗi *"Maximum batch GPU session count of 2 reached"* ⇒ **chỉ được chạy 2 phiên GPU đồng thời**, kernel còn lại phải đợi (A11 #181).

### 4.4. Vòng 4 — 3 nền còn lại (6 ảnh = 3 nền × 2 biến thể, 2 kernel)

Cách vá: **đổi bố cục** để vật thể "chỗ chữ" không còn xuất hiện trong khung hình:
`state_department` → hành lang nhìn thẳng, tường trơn không treo gì · `urgent_appeal` → điện thoại úp sấp / nằm nghiêng, bàn phím không lộ · `official_vehicle` → xe đứng nghiêng / đẩy xa, không biển số, thân xe trơn. Không nhắc tên `badge / emblem / nameplate / keypad digits` trong prompt (A11 #171).

| Mã nền | Biến thể | Kết quả |
|---|---|---|
| `t12_official_vehicle_closed_road` | A (seed 35005) | **SẠCH** — biển số không có, lưới không hãng, cổng trơn; chỉ còn nắp bánh tròn trừu tượng (~20 px, không ký tự). **Đã thay vào `assets/bg/`** |
| `t12_official_vehicle_closed_road` | B (seed 35006) | Sạch hơn biển số nhưng còn **badge ~40×10 px cạnh biển số** ⇒ không dùng |
| `t12_urgent_appeal_dark_office` | B (seed 35004) | **SẠCH** — giấy trơn, hồ sơ trống, bàn phím chỉ còn điểm sáng nút, không số. **Đã thay vào `assets/bg/`** |
| `t12_urgent_appeal_dark_office` | A (seed 35003) | Dự phòng (điện thoại úp sấp) |
| `t12_state_department_empty_corridor` | A (seed 35001) | **SẠCH** — hành lang nhìn thẳng, tường bê tông trơn **không khung / không biển / không bảng**, trần giáo dục + cửa gỗ. **Đã thay vào `assets/bg/`** |
| `t12_state_department_empty_corridor` | B (seed 35002) | Dự phòng (hành lang bê tông + kính) |



### 4.5. Chiến dịch vá 29 nền cũ (13/11) — 2 biến thể mỗi nền, 2 kernel

Cách vá (A11 #171 + #175 + #179 + #180): **giữ bối cảnh + chất noir**, chỉ thay vật thể mang chữ — hoặc làm bề mặt **trơn trống** (vật thể bắt buộc cho cốt truyện), hoặc **bỏ hẳn** khỏi khung hình (vật thể chính là "chỗ chữ"). **Không nhắc tên** vật thể mang chữ trong prompt (`printed / flyers / sign / label / marked / badge / emblem / inscribed / typed / notes / passbooks / deeds / envelopes / telegrams / appeals / names / card / volts / degrees / seal / stamp / map of / number`).

| Lô | Kernel | Ảnh | Seed | Kết quả |
|---|---|---|---|---|
| 1 | `…-flux2-t12-old29-k1` | 29 | 36000–36014 / 36100+ | **COMPLETE 19:46** · chờ GPU 75 phút · render 40 phút |
| 1 | `…-flux2-t12-old29-k2` | 29 | 36101–36128 | **COMPLETE 18:30** · chờ GPU 2 phút · render 39 phút |
| 2 | `…-flux2-t12-old29v5` | 8 | 36200–36303 | vòng 5 — đang chờ GPU |
| 2 | `…-flux2-t12-old29v6` | 14 | 36400–36506 | vòng 6 — đang chờ GPU |

**QC lô k2 (14 nền): 10/14 nền có biến thể sạch ⇒ đã thay vào `assets/bg/`.**

| Mã nền | Biến thể đưa vào | Ghi chú |
|---|---|---|
| `t12_loudspeaker_horns_tower` | a | Cột gỗ trơn, không tờ dán |
| `t12_nbc_camera_recording_facade` | b | Camera thân trơn |
| `t12_paranoia_cracking_dictator_mind` | b | Giấy trên bàn trơn |
| `t12_prefrontal_cortex_impairment` | b | Sơ đồ não không nhãn |
| `t12_redflag2_silenced_critical_thinking` | a | Bút + ổ khóa trơn |
| `t12_secret_note_folded_slip` | a | Mảnh giấy trơn |
| `t12_sunk_cost_entrapment_quicksand` | a | Mặt huy hiệu trơn |
| `t12_truck_evacuation_muddy_road` | b | **Biển số trống** (biến thể a có biển số ⇒ loại) |
| `t12_us_capitol_congressional_hearing` | a | Giấy rơi trên sàn trơn |
| `t12_utopian_promise_mirage` | a | Tranh bong tróc không chữ |

**QC lô k1 (14 nền): 9/14 nền có biến thể sạch ⇒ đã thay vào `assets/bg/`.**

| Mã nền | Biến thể đưa vào | Ghi chú |
|---|---|---|
| `t12_amber_eyes_closing_dossier_jonestown` | a | Bìa da trơn |
| `t12_charity_soup_kitchen_bread` | a | Bỏ tờ rơi, chỉ ấm + bánh |
| `t12_congressman_leo_ryan_briefing` | a | Bìa da + giấy trắng |
| `t12_entering_armed_compound_gate` | a | Vòm gỗ không biển |
| `t12_fallen_reporters_and_ryan` | a | Ống kính vỡ, không số |
| `t12_habituation_death_desensitization` | a | Trục bảng đen trơn |
| `t12_memorial_918_names_monolith` | a | Bia đá mặt trơn |
| `t12_moral_courage_candle_in_dark` | a | Nến + tường trơn |
| `t12_confiscated_passports_trunk` | b | Biến thể a có **chữ dập nổi trên bìa sổ** ⇒ loại |

**10/29 nền còn lại ⇒ vòng 5 + vòng 6:**

| Mã nền | Lỗi AI còn lại (đã soi zoom 8–16×) | Hướng vá tiếp |
|---|---|---|
| `t12_new_west_investigative_draft` | Chữ trên giấy trong máy đánh chữ + ống phim | **Bỏ máy đánh chữ** (phím có chữ) — vòng 5 |
| `t12_redflag1_total_social_isolation` | AI tự vẽ **badge "1" + chữ "ISOLATION"** | Bỏ cụm nhãn "Red Flag 1 …" khỏi prompt — vòng 5 |
| `t12_redflag3_escalating_commitment_trap` | **Số trên mặt đồng hồ** + chữ trên mảnh giấy | Bỏ đồng hồ; chỉ bánh răng + đĩa kim loại trơn — vòng 5 |
| `t12_press_corps_cameras_microphones` | **Vạch số trên ống kính** + màn hình có chữ hãng | Bỏ máy ảnh/màn hình; chỉ cuộn phim + micro — vòng 6 |
| `t12_property_surrender_passbooks` | Dòng chữ nhỏ trên mặt sổ (zoom 10× đọc được) | Bỏ sổ/giấy; chỉ ví da + chìa khóa + khay — vòng 6 |
| `t12_concerned_relatives_alliance` | **Caption dưới mỗi ảnh gia đình** | Cho ảnh úp sấp (chỉ thấy mặt sau trắng) — vòng 6 |
| `t12_fbi_evidence_tape_q042` | **Số trên thước đo** + nhãn băng | Bỏ thước; băng không nhãn — vòng 6 |
| `t12_milgram_experiment_shock_generator` | **Nhãn trên núm công tắc** | Chỉ thấy mặt sau máy — vòng 6 |
| `t12_moral_compass_unbroken` | **Chữ "N" trên mặt la bàn** | Dùng vỏ la bàn đóng — vòng 6 |
| `t12_impenetrable_geographical_isolation` | **Tên địa danh trên bản đồ** | Bỏ bản đồ; rừng nhìn từ trên cao — vòng 6 |

> **Bài học mới (A11 #183):** cụm nhãn trong prompt (*"Red Flag 1 Total Social Isolation"*) khiến AI **tự vẽ badge + chữ**; **phím máy đánh chữ**, **vạch số ống kính**, **thước đo**, **chữ Bắc trên la bàn**, **tên địa danh trên bản đồ** đều tự sinh chữ/số ⇒ phải **loại vật thể đó khỏi khung hình** (hoặc đổi góc nhìn), không chỉ thêm "no text".
> **Bài học #184:** ô montage ô 390 px **có** bắt được chữ/số rõ (badge "ISOLATION", số trên đồng hồ, caption dưới ảnh, chữ N) — nhưng **không** bắt được chữ ~10 px (dòng chữ trên mặt sổ, chữ dập nổi trên bìa sổ, tên địa danh nhỏ trên bản đồ) ⇒ vẫn phải crop ≥ 10× cho các nền có vật thể giấy/bìa/số đo.



### 4.6. Bảng kế hoạch vá ban đầu cho 83 nền cũ (đã triển khai ở §4.5)

Cách vá theo A11 #171 + #180: **giữ vật thể, đổi bề mặt thành trơn trống** (nếu vật thể bắt buộc cho cốt truyện) hoặc **đổi bố cục** (nếu vật thể chính là "chỗ chữ"), và **không nhắc tên** vật thể mang chữ trong prompt.

| Mã nền | Vật thể có chữ | Hướng vá |
|---|---|---|
| `t12_secret_note_folded_slip` | Mảnh giấy viết tay | Giữ mảnh giấy nhưng **trơn trắng không một nét** (chữ sẽ render sau) |
| `t12_moral_courage_candle_in_dark` | Chữ trên tường | Tường bê tông trơn, chỉ nến và bóng |
| `t12_wall_francisco_temple_expansion` | Biển "PEPPLS TEMPLE" | Biến thành **cổng bê tông trắng trơn**, không biển |
| `t12_entering_armed_compound_gate` | Biển gỗ | **Cổng gỗ không biển**, chỉ vòm cổng + bùn |
| `t12_concerned_relatives_alliance` | Bảng tin báo chí | Bỏ bảng tin, giữ **bức tường trơn + vài ảnh gia đình không khung chữ** |
| `t12_fbi_evidence_tape_q042` | Nhãn băng | Giữ cuộn băng nhưng **nhãn trơn không chữ** |
| `t12_memorial_918_names_monolith` | Bia khắc danh sách | **Bia đá trơn không khắc** |
| `t12_new_west_investigative_draft` | Bản thảo đánh máy | Giữ máy ghi nhưng **giấy trắng trơn không chữ** |
| `t12_property_surrender_passbooks` | Sổ + giấy tờ | Sổ **đóng không chữ**, giấy **trơn** |
| `t12_press_corps_cameras_microphones` | Chữ trên máy + báo | Máy ảnh **trơn không nhãn**, bỏ báo |
| `t12_confiscated_passports_trunk` | Hộ chiếu "PASSPORT" | Hộ chiếu **bìa trơn không chữ** |
| `t12_nbc_camera_recording_facade` | Logo camera | Camera **thân trơn, không logo** |
| `t12_milgram_experiment_shock_generator` | Núm đo "VOLTS/450" | Bảng điều khiển **trơn không nhãn không số** |
| `t12_moral_compass_unbroken` | La bàn N/E/S/W + độ | La bàn **mặt trơn không chữ không số** |
| `t12_redflag3_escalating_commitment_trap` | Số đồng hồ + ghi chú | Đồng hồ **mặt trơn**, bỏ mảnh ghi chú |
| `t12_ablation_death_desensitization` | Bảng đồ trục có nhãn | **Bỏ bảng**, thay bằng hình khối tối trừu tượng |
| `t12_impenetrable_geographical_isolation` | Bản đồ có tên | Bản đồ **thô sơ không nhãn** hoặc bỏ bản đồ |
| `t12_utopian_promise_mirage` | Poster thiên đường | Poster **vẽ tranh không chữ** |
| `t12_charity_soup_kitchen_bread` | Tờ rơi in chữ | **Bỏ tờ rơi**, chỉ ấm + bánh |
| `t12_amber_eyes_closing_dossier_jonestown` | Bìa hồ sơ + emblem | **Hồ sơ đóng trơn**, giữ biểu tượng mắt trừu tượng không khắc chữ |
| `t12_paranoia_cracking_dictator_man` | Giấy tờ trên bàn | Giấy **trơn trắng** |
| `t12_prefrontal_cortex_impairment` | Áp phích giải phẫu | Áp phích **hình vẽ trơn không nhãn** |
| `t12_redflag1_total_social_isolation` | Badge "FLAG 1" | **Bỏ badge**, giữ mạng nhện + ảnh không khung chữ |
| `t12_fallen_reporters_and_ryan` | Thẻ báo chí + chữ camera | **Bỏ thẻ**, camera thân trơn |
| `t12_congressman_leo_ryan_briefing` | Sách + con dấu | Sách **bìa trơn**, bỏ con dấu |
| `t12_us_capitol_congressional_hearing` | Sách in ấn | Sách **gáy trơn không chữ** |
| `t12_loudspeaker_horns_tower` | Tờ nhỏ trên cột | Cột **trơn** |
| `t12_redflag2_silenced_critical_thinking` | Chữ nhỏ trên ổ khóa | Ổ khóa **trơn** |
| `t12_sunk_cost_entrapment_quicksand` | Ký hiệu trên đồng tiền | Đồng tiền **mặt trơn** |
| `t12_truck_evacuation_muddy_road` | Vết chữ sau xe | **Không chữ**, chỉ xe + bùn |

> Chi phí dự kiến nếu duyệt: **≈ 30 lượt sinh** (2 kernel × 15 ảnh, seed 36000+), thời gian GPU ≈ 40–50 phút + hàng đợi.

---

### 4.7. Vòng 5 — 4 nền × 2 biến thể (8 ảnh) + trạng thái vòng 6

| Lô | Kernel | Ảnh | Seed | Trạng thái (đo thật) |
|---|---|---|---|---|
| vòng 5 | `chiduong2026/amber-eyes-flux2-t12-old29v5` | 8 | 36200–36303 | **COMPLETE 21:18** (bắt đầu render ~20:46 sau ~75 phút xếp hàng) |
| vòng 6 | `chiduong2026/amber-eyes-flux2-t12-old29v6` | 14 | 36400–36506 | **ĐÃ XOÁ 21:49 theo yêu cầu** — huỷ lần chạy đang QUEUED (chưa render ảnh nào). Mã nguồn kernel vẫn còn ở `.work/kaggle_flux/t12v6/` + jobs `.work/bg_jobs_tap12_old29_v6.json` ⇒ push lại bằng 1 lệnh |

**QC vòng 5 (montage 8 ảnh + crop 6–18× từng vùng nghi):**

| Mã nền | Biến thể a | Biến thể b | Kết luận |
|---|---|---|---|
| `t12_new_west_investigative_draft` | ✗ **nhãn có chữ trên cuộn phim** (nét dọc đọc được ở 12×) | ✓ sạch | **đã thay bản b** |
| `t12_redflag1_total_social_isolation` | ✓ sạch | ✓ sạch | **đã thay bản a** (b có vệt đỏ ngang như tia laser ⇒ bỏ) |
| `t12_redflag3_escalating_commitment_trap` | ✗ vết **ký tự ~10–15 px** trên mặt gông | ✓ sạch | **đã thay bản b** |
| `t12_press_corps_cameras_microphones` | ✗ **khắc chữ/số trên vòng ống kính** | ✗ như trên | **chưa sạch** — bản v6 (bỏ máy ảnh: chỉ cuộn phim + micro) đã bị huỷ theo yêu cầu dừng Kaggle |

> **Bài học mới (A11 #190) — `~/.kaggle/access_token` HẾT HẠN làm CHẾT toàn bộ lệnh Kaggle.** Lúc 21:00 access token hết hạn (12 h kể từ 21:00 ngày trước) ⇒ `kernels status` trả *"Permission 'kernels.get' was denied"*, `kernels list` trả *"Authentication required"* — **không phải lỗi quyền kernel**. Nguyên nhân: CLI ưu tiên đọc file `~/.kaggle/access_token` **trước** `credentials.json`, nên nó không tự refresh dù có `refresh_token`. Cách sửa: `.work/kaggle_flux/refresh_kaggle_token.py` (dùng SDK `generate_access_token()` → ghi lại `credentials.json` + `access_token`, có backup `.bak`).

> **Bài học mới (A11 #191) — ảnh noir quá tối ⇒ montage phải TĂNG SÁNG, không soi bản gốc.** 8 ảnh vòng 5 có luminance trung bình 39–51/255 ⇒ montage thường ra **đen xì** (nhìn như không có ảnh) dù ảnh có nội dung. Công cụ mới: `.work/_t12_bright_montage.py` (gain 2,0–2,2 + tăng tương phản, chỉ dùng để QC, **không** đụng file gốc) + `.work/_t12_crop_batch.py` (crop nhiều vùng → gộp 1 tờ để soi 1 lần).

---

### 4.8. Rút kinh nghiệm — tại sao phải gọi tạo ảnh nhiều lần?

**Số liệu quyết toán (đếm từ file job + staging trên đĩa):**

| Lô | Nền | Ảnh đã render | Seed | Kết quả |
|---|---|---|---|---|
| Lô gốc 13/11 (`bg_jobs_tap12.json`) | 83 | 83 | — | **21,7 % prompt yêu cầu chữ**; ≈ 33 % ảnh dính chữ AI |
| Lô mới (`…-new69`) | 69 | 69 | 22005–22152 | 7 nền dính chữ (10,1 %) |
| Vòng 2 (`…-detext-k1/k2`) | 7 | 7 | 33001–33007 | 4/7 **vẫn còn vết** khi soi full-frame |
| Vòng 3 (`…-detext3-k1/k2`) | 1 | 2 | 34001–34002 | sạch |
| Vòng 4 (`…-detext4-k1/k2`) | 3 | 6 | 35001–35006 | 3/3 sạch |
| Chiến dịch vá 29 nền cũ (`…-old29-k1/k2`) | 29 | 58 | 36000–36128 | **19/29 sạch ngay** ⇒ 39 ảnh bị bỏ (67 %) |
| Vòng 5 (`…-old29v5`) | 4 | 8 | 36200–36303 | 3/4 sạch ⇒ 5 ảnh bị bỏ |
| Vòng 6 (`…-old29v6`) | 7 | **0** (bị huỷ) | 36400–36506 | — |
| **TỔNG** | **152** | **233 ảnh** | | **81 ảnh thừa = 34,9 %** |

**Chi phí thật của 81 ảnh thừa:** 81 × ~75 s/ảnh ≈ **101 phút GPU** lãng phí, chưa kể **hàng đợi GPU** đo được ở các lô: detext3 **56 phút** · detext4 **78 phút** · old29-k1 **75 phút** · old29v5 **75 phút** ⇒ **≈ 4,7 giờ chờ** (giới hạn 2 phiên GPU/tài khoản buộc các vòng phải xếp nối).

**5 nguyên nhân, xếp theo số lượt sinh lãng phí:**

1. **QC chỉ làm 1/3 việc trước khi promote — 83 nền lô 13/11 chưa từng qua cổng chữ.** Chiến dịch vá 29 nền (58 ảnh) = **24,9 % tổng lượt sinh cả tập** chỉ để bù cho ảnh cũ *chưa ai kiểm*. ⇒ Quy tắc: **không ảnh nào được coi là xong nếu chưa soi full-frame + crop ≥ 12×**; nền sinh từ lô cũ phải QC cùng lô mới, không mặc định "đạt".
2. **Mệnh đề phủ định ("no text / no labels") KHÔNG cứu được vật thể có sẵn "chỗ chữ".** 22/69 prompt lô mới đã ghi phủ định mà vẫn dính. Danh sách vật thể tự sinh chữ đã gặp: hộ chiếu mở · bảng tin · bìa sổ · **vòng ống kính** · mặt đồng hồ · thước đo · la bàn · **cuộn phim** · nhãn băng · badge · núm bàn phím · khung tranh · nameplate. ⇒ Quy tắc: **mô tả bề mặt TRƯNG của vật thể mang chữ, hoặc bỏ hẳn vật thể khỏi khung hình — và không nhắc tên vật thể mang chữ**.
3. **Cụm NHÃN trong prompt bị AI dùng làm chữ để vẽ.** *"Red Flag 1 Total Social Isolation"* ⇒ badge "1" + chữ "ISOLATION"; *"Q 042"* ⇒ nhãn băng "RYMUR FBI Record Q 042"; *"New West Magazine"* ⇒ tên tạp chí trên bìa. ⇒ Quy tắc: cụm nhãn là **dữ liệu để vẽ**, không phải mô tả — bỏ khỏi prompt.
4. **Ngưỡng QC quá thô ở vòng 1 ⇒ cùng một nhóm nền phải sinh tới 3 lần.** Montage ô 390 px bỏ sót chữ ~10 px ⇒ 4/7 ảnh "PASS" thực ra còn vết ⇒ vòng 2 sinh lại 7 ảnh + vòng 3/4 sinh thêm 8 ảnh cho cùng 3 nền (**15 lượt = 6,4 %**). ⇒ Quy tắc: soi **full-frame + crop 8–16×** ngay từ ảnh đầu tiên, dùng bản **tăng sáng** cho ảnh tối (A11 #191).
5. **Dùng 2 biến thể/nền *thay vì* sửa prompt tới nơi.** 2 biến thể (cùng prompt, khác seed) đặc biệt hiệu quả khi AI đặt chữ ở **1 vị trí** (bản kia sạch): 4/7 ở vòng 2, 19/29 ở chiến dịch vá. Nhưng tốn **gấp đôi lượt sinh**, tỉ lệ dùng 33–38 % (39/58 và 5/8 ảnh bị bỏ). ⇒ Quy tắc: **sinh 2 biến thể/nền ngay từ đầu** (1 lô lớn) thay vì vá nhiều vòng — rẻ hơn về tổng lượt, và **sửa prompt theo (2)(3) vẫn là bắt buộc**, không thay thế được bước này.

**Quy trình "đúng 1 lần" (áp dụng từ tập sau) — 5 bước TRƯỚC khi push:**

1. **Quét prompt** bằng `.work/_t12_prompt_textscan.py` (từ khoá: `printed/flyers/marked/labeled/inscribed/typed/notes/…`) ⇒ sửa hết trước khi sinh (lô 13/11: 18/83 = 21,7 % dính).
2. **Không cụm nhãn + không tên vật thể mang chữ**; vật thể có sẵn chỗ chữ ⇒ **đổi bố cục** (úp sấp · bỏ · xoay lưng · chỉ mặt sau).
3. **Sinh 2 biến thể/nền ngay** trong đúng 2 kernel song song (tận dụng 2 GPU, giảm số vòng).
4. **QC bắt buộc trước khi promote**: montage (để lập danh sách nghi) → **crop 8–16× từng vùng có giấy/bìa/thước/ống kính/la bàn/phim/ảnh ghim** → dùng **bản tăng sáng** cho ảnh noir tối.
5. **QC 100 % toàn bộ nền của tập**, kể cả nền sinh ở lô trước — không "mặc định đạt" cho ảnh cũ.

> **A11 #192** ghi lại 5 nguyên nhân + quy trình 5 bước này. Ước tính nếu áp dụng từ đầu: **152 ảnh thay vì 233** (−34,9 % lượt sinh, −101 phút GPU, −4,7 giờ chờ hàng đợi).

---

## 5. QC kích thước & đủ file

```
job trong bg_jobs_tap12_v2.json : 152
đúng kích thước 2112x1188       : 152
thiếu file                      : 0
sai kích thước                  : 0
file t12_* thừa (không có job)  : 0
```

---

## 6. Việc còn lại

- [x] **Vòng 2–4 QC**: 7 ảnh sinh lại → soi full-frame + crop 12–16× ⇒ **4/7 còn vết** ⇒ vòng 3–4 vá bằng **đổi bố cục** ⇒ **4/4 nền đã sạch chữ** (máy ghi âm · xe · điện thoại · hành lang).
- [x] **83 nền cũ (13/11)**: quét 100 % ⇒ **18/83 prompt yêu cầu chữ**, ≈ **27–28/83 ảnh dính chữ AI** ⇒ đã vá **29 nền** (2 biến thể/nền = 58 ảnh, 2 kernel `…-old29-k1` + `…-old29-k2`) ⇒ **19/29 nền sạch ngay** đã thay vào `assets/bg/`.
- [x] **Vòng 5** (4 nền × 2 = 8 ảnh, seed 36200–36303, kernel `…-old29v5` COMPLETE 21:18): QC xong ⇒ **3 nền sạch** đã thay vào `assets/bg/` (`new_west` b · `redflag1` a · `redflag3` b).
- [ ] **7 nền vẫn còn chữ AI** (`press_corps` · `concerned_relatives` · `fbi_evidence` · `milgram` · `moral_compass` · `impenetrable` · `property_surrender`): bản vá đã viết xong (`.work/bg_jobs_tap12_old29_v6.json`, 14 ảnh, seed 36400–36506) + kernel dựng sẵn (`.work/kaggle_flux/t12v6/`) nhưng **vòng 6 đã bị huỷ 21:49 theo yêu cầu dừng Kaggle** ⇒ push lại bằng:
  `py -3 .work/kaggle_flux/make_kernel_t12_single.py --jobs .work/bg_jobs_tap12_old29_v6.json --id chiduong2026/amber-eyes-flux2-t12-old29v6 --prefix flux2_tap12_old29v6 --dir .work/kaggle_flux/t12v6` → `kaggle kernels push -p .work/kaggle_flux/t12v6`.
- [ ] Sau khi dựng audio thật: chạy lại `qc_bg_usage.py --plan` (H25) và `parse_shots.py` (H22) cho Tập 12.
- [ ] Tập 12 chưa có bảng shot EN/JA ⇒ dựng 3 ngôn ngữ sau khi có audio (nền dùng chung 100% — H17).

---

## 7. Tài liệu liên quan

- `00_TIEU_CHUAN/QUY_TAC_TAO_ANH_KAGGLE_FLUX.md` (v1.0) — chuẩn tạo ảnh Kaggle FLUX.
- `00_TIEU_CHUAN/TIEU_CHUAN_DUNG_VIDEO.md` — A11 #163–#189 (H25, H22, quy tắc bỏ chữ, A11 #180–#182 & #188–#189 cho Tập 12).
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap12/KeHoach_Video_Tap12.md` — bảng shot đã tách (152 mã nền).
- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap12/Danh_Sach_Anh_Tap12.md` — danh sách 152 ảnh + ánh xạ mốc câu.
- `provenance.json` — **152 dòng nền Tập 12** (prompt, seed, công cụ, điều khoản, đã kiểm thương mại); 0 trùng `file`, 0 thiếu seed, 0 file không tồn tại.
