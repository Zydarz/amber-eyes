# KẾ HOẠCH CLIP TIKTOK — TẬP 02 · "ĐẠI TÁ HAI MẶT"

*Ngày: 20/11/2026 · Trạng thái: **kịch bản đã viết, chờ người dùng duyệt trước khi đọc giọng** (L4)*
*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap02/SPEC_AUDIO_CLIP_TAP02.json`*
*Nguồn duy nhất của mọi dữ kiện: `.work/script_tap02.json` (203 câu, đã đối chiếu `02_SAN_XUAT/Tap02/nguon_tham_khao.md`)*
*Sinh tự động bởi `.work/_build_tk_tap02.py` — sửa kịch bản thì sửa file đó rồi chạy lại, đừng sửa tay file này.*

---

## 0. Tóm tắt chốt

| Hạng mục | Giá trị |
|---|---|
| Số clip | **5 clip** (TK1–TK4 chính + TK5 clip kết) |
| Tổng câu | **53 câu** đọc giọng |
| Độ dài | Ước lượng 62.5–82.6 s/clip (mục tiêu 65–90 s · cổng QC 45–95 s) |
| Chủ đề | Mỗi clip = **1 chỉ dấu tâm lý** của Tập 02 (K10) |
| Ngôn ngữ | Tiếng Việt · vai H / D / C / N2 |
| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2 — đúng giọng của Tập 02** (không dùng bộ A MiniMax) |
| Hình | Nền dọc 9:16 `tk02_*` (26 nền dùng trong clip, mục 7) · Pillow vẽ chữ |
| Chi phí | **0 đồng** (Kaggle GPU có sẵn) — trừ thời gian chờ GPU |
| Việc cần người dùng | Tạo **53 file WAV** theo `SPEC_AUDIO_CLIP_TAP02.json` (mục 5) · điền link YouTube Tập 02 (mục 13) |

---

## 1. Vì sao viết lời dẫn mới cho clip, không cắt từ audio tập

| Phương án | Đánh giá |
|---|---|
| **A — Lời dẫn mới cho clip (CHỌN)** | Hook 3 giây đúng chuẩn TikTok; 1 clip = 1 chỉ dấu; chỉ cần **53 câu ngắn** thay vì 203 câu; V3 đảm bảo mọi câu trong clip truy được về kịch bản tập |
| B — Cắt nguyên đoạn từ audio tập | Lời dẫn tập viết để *nghe*, không phải để *giữ chân*; không có hook 3 giây ⇒ **trượt đối với TikTok**; 203 câu / 25 phút không cắt được trong 45–90 s mà giữ được cả 10 chỉ dấu |

⇒ Chọn A. **Mọi dữ kiện trong lời đọc phải truy được về `.work/script_tap02.json`** — không thêm tên riêng, số liệu hay chi tiết mới (K1/K2).

---

## 2. Năm clip và chỉ dấu tâm lý tương ứng (K10)

| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng |
|---|---|---|---|---|
| **TK1** | #8 · #6 | Quỹ đạo leo thang hành vi + ngòi nổ tâm lý (Precipitating Trigger) | *"Bốn nấc thang. Rồi một vụ án mạng."* | 81.5 s · 12 câu |
| **TK2** | #9 · #1 | Hiệu ứng hào quang + ảnh hưởng xã hội (dư chấn tập thể) | *"Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào."* | 76.0 s · 11 câu |
| **TK3** | #5 · #3 | Hệ thống tự bào chữa (Neutralization) + cơ chế chia ngăn (Compartmentalization) | *"Hai cuộc đời. Một câu chuyện để tự bào chữa."* | 79.0 s · 12 câu |
| **TK4** | #4 · #1 | Sự sụp đổ cái tôi ái kỷ (Narcissistic Collapse) + bản án tâm lý | *"Không một lời xin lỗi nào nhắc tới nạn nhân."* | 82.6 s · 10 câu |
| **TK5** | #10 | Nạn nhân học & bài học sinh tồn (ranh giới + trực giác) | *"Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó."* | 62.5 s · 8 câu |

**Thứ tự đăng:** TK2 → TK1 → TK4 → TK3 → TK5 (TK2 có hook mạnh nhất để thu hút; TK5 là clip lưu/chia sẻ để khép lại chuỗi).

---

## 3. Diễn xuất từng clip (lời đọc + hình + âm)

> Quy ước vai: **H** = Host (Cú) · **D** = Điều tra viên (Sói) · **C** = Chuyên gia tâm lý (Cáo) · **N2** = Khán giả (Mèo)
> `pause_after` = thời gian im lặng chèn **giữa hai câu** (0,2–1,2 s — luật G2). Emotion chỉ dùng 4 giá trị an toàn (G3). Tốc độ lệch −0,06…+0,02 (G4). **Cao độ luôn = 0** (G5).
> Mỗi câu bắt đầu bằng mã câu `TKx.01#z` — dùng làm tên file WAV và mã câu trong hồ sơ.
> **Ước lượng = số từ sau khi đổi số→chữ × tỉ lệ đọc đo thật của vai đó** (mục 3.6).

### 3.1 CLIP TK1 — "Bốn nấc thang. Rồi một vụ án mạng"

*Ước lượng 81.5 s (12 câu) · BGM `bgm_piano_minimal.mp3` (Hồi 2 — bed tập: bgm_piano_minimal.mp3) · SFX: amb_winter_wind.wav (nền) · fx_tension_tick.wav · fx_stinger.wav · fx_sub_drop.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK1.01#1` | H | neutral | -0.02 | 0.5 | Bốn nấc thang. Tám mươi hai vụ trộm. Rồi một vụ án mạng. | 2.05#1 · 2.05#7 · 5.07#5 |
| `TK1.01#2` | H | neutral | -0.02 | 0.6 | Hắn không bắt đầu bằng bạo lực. Hắn bắt đầu bằng việc đứng ngoài cửa sổ ban đêm. | 2.05#2 · 2.05#3 · 5.07#5 |
| `TK1.01#3` | D | neutral | -0.03 | 0.6 | Nấc thang thứ nhất: nhìn trộm ban đêm, đứng ngoài bóng tối rình rập phụ nữ qua khung cửa sổ. | 2.05#2 · 2.05#3 |
| `TK1.01#4` | D | neutral | -0.03 | 0.6 | Nấc thang thứ hai: đột nhập lấy đồ riêng tư. Hắn không lấy tiền hay trang sức. Hắn lấy đồ lót và đồ riêng tư của phụ nữ. | 2.05#4 · 2.05#8 · 2.05#9 |
| `TK1.01#5` | D | neutral | -0.03 | 0.5 | Nghi thức lặp lại y hệt ở mọi căn nhà: chụp ảnh, lấy đồ, rồi ghi chép lại. | 2.05#10 |
| `TK1.01#6` | C | neutral | -0.02 | 0.6 | Khi hành vi cũ trở nên quen thuộc, hắn rơi vào trạng thái đói ảo tưởng, buộc phải tăng liều lượng rủi ro để tìm lại khoái cảm ban đầu. | 3.05#7 · 3.05#8 · 3.05#9 |
| `TK1.01#7` | D | neutral | -0.03 | 0.6 | Nấc thang thứ ba: tháng 9 năm 2009, hắn đột nhập vào nhà lúc có người ở nhà. | 2.05#11 · 2.05#12 · 2.05#13 |
| `TK1.01#8` | D | neutral | -0.03 | 0.7 | Và nấc thang thứ tư: cuối tháng 11 năm 2009, nạn nhân là Marie-France Comeau, nữ hạ sĩ ba mươi bảy tuổi phục vụ ngay trong căn cứ mà hắn chỉ huy. | 2.05#14 · 2.05#15 |
| `TK1.01#9` | H | neutral | -0.02 | 0.6 | Chỉ hai tháng sau đó, nạn nhân tiếp theo là Jessica Lloyd. | 2.05#16 |
| `TK1.01#10` | C | neutral | -0.02 | 0.6 | Tháng 7 năm 2009, khi hắn được thăng cấp chỉ huy trưởng căn cứ Trenton, đó là ngòi nổ tâm lý: cảm giác quyền lực tối cao cùng áp lực công việc đã đánh sập chốt chặn kiểm soát cuối cùng. | 1.03#4 · 3.05#10 |
| `TK1.01#11` | H | neutral | -0.02 | 0.7 | Tội ác không bao giờ bắt đầu từ một vụ án mạng. Nó bắt đầu từ một cái nhìn trộm không bị trừng phạt. | 5.07#5 · 5.07#6 |
| `TK1.01#12` | H | neutral | -0.02 | 0.0 | Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK1.01#1` | `tk02_escalation_stairs` | still | 3.8 s |
| `TK1.01#2` | `tk02_escalation_stairs` | pull | 5.3 s |
| `TK1.01#3` | `tk02_open_window` | push | 5.2 s |
| `TK1.01#4` | `tk02_drawer_dark` | pan | 7.3 s |
| `TK1.01#5` | `tk02_folder_tree` | still | 4.7 s |
| `TK1.01#6` | `tk02_brain_neural` | push | 7.2 s |
| `TK1.01#7` | `tk02_open_window` | pan | 6.0 s |
| `TK1.01#8` | `tk02_two_chairs` | still | 9.9 s |
| `TK1.01#9` | `tk02_house_missing` | pull | 3.5 s |
| `TK1.01#10` | `tk02_oath_hall` | push | 11.0 s |
| `TK1.01#11` | `tk02_escalation_stairs` | push | 7.0 s |
| `TK1.01#12` | `tk02_podcast_desk` | still | 4.1 s |

**Thẻ chữ trên hình (overlay card):**
- `TK1.01#1` → *"4 NẤC THANG · 82 VỤ · 1 ÁN MẠNG"* (3.0 s)
- `TK1.01#3` → *"NẤC THỨ NHẤT — NHÌN TRỘM BAN ĐÊM"* (2.5 s)
- `TK1.01#4` → *"NẤC THỨ HAI — ĐỘT NHẬP LẤY ĐỒ RIÊNG TƯ"* (2.5 s)
- `TK1.01#7` → *"NẤC THỨ BA — XÂM NHẬP KHI CÓ NGƯỜI Ở NHÀ"* (2.5 s)
- `TK1.01#8` → *"NẤC THỨ TƯ — NẠN NHÂN CUỐI CÙNG"* (2.5 s)
- `TK1.01#10` → *"NGÒI NỔ TÂM LÝ · THÁNG 7/2009"* (2.5 s)

**Nguồn dữ kiện:** 2.04#3 · 2.05#1-#16 · 3.05#4-#10 · 5.07#5-#6 · nguon_tham_khao.md (R. v. Williams 2010 ONSC 5946)

### 3.2 CLIP TK2 — "Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào"

*Ước lượng 76.0 s (11 câu) · BGM `bgm_sub_drone.mp3` (Hồi 1 — bed tập: bgm_sub_drone.mp3) · SFX: amb_road_night.wav (nền) · fx_tire_snow.wav · fx_window_down.wav · fx_flashlight.wav · fx_police_radio.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK2.01#1` | H | neutral | -0.02 | 0.5 | Vân lốp xe trùng khớp. Và cảnh sát vẫn kính cẩn chào cho người đàn ông đó đi. | 1.14#4 · 1.14#5 |
| `TK2.01#2` | H | neutral | -0.02 | 0.6 | Tháng 7 năm 2009, Đại tá Russell Williams nhận quyền chỉ huy tối cao căn cứ không quân Trenton. | 1.03#1 · 1.03#4 |
| `TK2.01#3` | H | neutral | -0.02 | 0.6 | Ông từng lái chuyên cơ đưa đón Nữ hoàng Anh Elizabeth II. | 1.05#1 |
| `TK2.01#4` | D | neutral | -0.03 | 0.6 | Đêm 28 tháng 1 năm 2010, Jessica Lloyd, hai mươi bảy tuổi, biến mất khỏi nhà riêng ở Belleville. | 1.10#1 · 1.10#2 |
| `TK2.01#5` | D | neutral | -0.03 | 0.7 | Cảnh sát không tìm ra manh mối nào trong những ngày đầu tiên. Một tuần sau đó, tối ngày 4 tháng 2, họ lập trạm kiểm soát lưu động suốt đêm, chỉ để săn một dấu vết: vệt vân lốp xe hiếm gặp trên nền tuyết. | 1.12#1 · 1.12#2 · 1.12#3 |
| `TK2.01#6` | D | neutral | -0.03 | 0.6 | Trong dòng xe qua trạm đêm hôm đó có một chiếc Nissan Pathfinder, thay vì chiếc BMW thường ngày. | 1.14#1 · 1.14#2 |
| `TK2.01#7` | D | neutral | -0.03 | 0.5 | Người ngồi sau vô-lăng hạ cửa kính xuống — chính là chỉ huy trưởng căn cứ không quân Trenton. | 1.14#3 |
| `TK2.01#8` | H | neutral | -0.02 | 0.5 | Vân lốp xe của ông ta trông rất giống dấu vết trên tuyết. | 1.14#4 |
| `TK2.01#9` | D | neutral | -0.03 | 0.7 | Nhưng trước một sĩ quan cấp cao, các sĩ quan tuần tra không thể giữ ông ta lại — họ chỉ ghi nhận rồi kính cẩn chào cho đi. Và trong ba ngày tiếp theo, ông ta vẫn là một vị đại tá tự do. | 1.14#5 · 1.14#6 |
| `TK2.01#10` | C | neutral | -0.02 | 0.7 | Hiệu ứng hào quang: tấm khiên vô hình khiến cả xã hội lẫn cơ quan thực thi pháp luật bị che mắt nhiều năm ròng. | 1.08#4 |
| `TK2.01#11` | H | neutral | -0.02 | 0.0 | Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK2.01#1` | `tk02_checkpoint` | still | 5.3 s |
| `TK2.01#2` | `tk02_oath_hall` | pull | 7.0 s |
| `TK2.01#3` | `tk02_oath_hall` | pan | 3.8 s |
| `TK2.01#4` | `tk02_house_missing` | still | 6.5 s |
| `TK2.01#5` | `tk02_checkpoint` | push | 12.0 s |
| `TK2.01#6` | `tk02_suv_stop` | still | 4.9 s |
| `TK2.01#7` | `tk02_suv_stop` | push | 4.9 s |
| `TK2.01#8` | `tk02_tire_track` | still | 3.8 s |
| `TK2.01#9` | `tk02_checkpoint` | pan | 11.7 s |
| `TK2.01#10` | `tk02_siren_wall` | push | 6.0 s |
| `TK2.01#11` | `tk02_podcast_desk` | still | 4.1 s |

**Thẻ chữ trên hình (overlay card):**
- `TK2.01#5` → *"TRẠM KIỂM SOÁT LƯU ĐỘNG · ĐÊM 4/2"* (2.5 s)
- `TK2.01#9` → *"CHỈ GHI NHẬN THÔNG TIN — RỒI KÍNH CẨN CHÀO"* (2.5 s)
- `TK2.01#10` → *"HIỆU ỨNG HÀO QUANG"* (3.0 s)

**Nguồn dữ kiện:** 1.03#1-#4 · 1.05#1-#4 · 1.08#4 · 1.10#1-#3 · 1.12#1-#3 · 1.14#1-#7 · 1.17#1-#3 · nguon_tham_khao.md (OPP + Belleville Police)

### 3.3 CLIP TK3 — "Hai cuộc đời. Một câu chuyện để tự bào chữa"

*Ước lượng 79.0 s (12 câu) · BGM `bgm_cello_sad_v2.mp3` (Hồi 3 — bed tập: bgm_cello_sad_v2.mp3) · SFX: amb_basement.wav (nền) · fx_drawer_open.wav · fx_stinger.wav · fx_hdd_spin.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK3.01#1` | H | neutral | -0.02 | 0.5 | Hai cuộc đời. Một cơ thể. Một câu chuyện để tự bào chữa. | 3.08#1 · 3.08#8 |
| `TK3.01#2` | H | neutral | -0.02 | 0.7 | Trước khi phân tích: không tồn tại chẩn đoán lâm sàng công khai nào về Russell Williams. Đây là khung lý thuyết, không phải phán xét. | 3.04#1 · 3.04#2 |
| `TK3.01#3` | C | neutral | -0.02 | 0.7 | Trong tâm lý học, phân mảnh tâm trí là cơ chế phòng vệ khóa chặt hai luồng nhận thức và cảm xúc trái ngược nhau vào hai ngăn kéo. | 3.08#2 |
| `TK3.01#4` | C | neutral | -0.02 | 0.6 | Ngăn kéo thứ nhất là vị đại tá: người chỉ huy mẫu mực, người chồng chăm sóc vườn tược. | 3.08#4 |
| `TK3.01#5` | C | neutral | -0.02 | 0.6 | Ngăn kéo thứ hai là kẻ săn mồi bóng đêm, nơi hắn giải phóng những xung lực tàn bạo nhất. | 3.08#5 |
| `TK3.01#6` | C | neutral | -0.02 | 0.7 | Khi ở ngăn kéo này, hắn đóng chặt cánh cửa của ngăn kéo kia, rồi dùng người vợ và cuộc hôn nhân chuẩn mực làm lá chắn. | 3.08#6 · 3.08#7 |
| `TK3.01#7` | C | neutral | -0.02 | 0.8 | Để lương tri không lên tiếng, hắn trung hòa đạo đức. Trong tám mươi hai vụ đầu, hắn tự nhủ: <#0.35#> mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm. | 3.08#8 |
| `TK3.01#8` | C | neutral | -0.02 | 0.7 | Đến khi có án mạng, hắn lại tự biện minh rằng nạn nhân đã thấy mặt mình, ép mình phải ra tay để tự vệ. | 3.08#9 |
| `TK3.01#9` | C | neutral | -0.02 | 0.5 | Và chính vì vậy, cuối cùng hắn không thể tự giải thích một cách có lương tri. | 3.08#10 |
| `TK3.01#10` | C | sad | -0.04 | 0.9 | Khi thám tử hỏi vì sao mình làm những việc đó, câu trả lời trong bản ghi thẩm vấn trống rỗng: <#0.35#> Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng. | 3.08#11 |
| `TK3.01#11` | C | sad | -0.04 | 0.7 | Đó là câu trả lời trơ trẽn nhất, phơi bày sự ngắt kết nối đạo đức của kẻ săn mồi này. | 3.08#12 |
| `TK3.01#12` | H | neutral | -0.02 | 0.0 | Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK3.01#1` | `tk02_two_drawers` | still | 3.8 s |
| `TK3.01#2` | `tk02_two_masks` | pull | 7.6 s |
| `TK3.01#3` | `tk02_brain_neural` | push | 7.0 s |
| `TK3.01#4` | `tk02_command_chair` | pan | 4.6 s |
| `TK3.01#5` | `tk02_stairs_dark` | push | 4.8 s |
| `TK3.01#6` | `tk02_two_drawers` | still | 6.5 s |
| `TK3.01#7` | `tk02_drawer_dark` | pull | 8.4 s |
| `TK3.01#8` | `tk02_hidden_drive` | pan | 6.0 s |
| `TK3.01#9` | `tk02_two_drawers` | still | 4.1 s |
| `TK3.01#10` | `tk02_interrogation_early` | push | 9.8 s |
| `TK3.01#11` | `tk02_head_down` | pull | 5.0 s |
| `TK3.01#12` | `tk02_podcast_desk` | still | 4.1 s |

**Thẻ chữ trên hình (overlay card):**
- `TK3.01#3` → *"PHÂN MẢNH TÂM TRÍ (COMPARTMENTALIZATION)"* (3.0 s)
- `TK3.01#4` → *"NGĂN KÉO THỨ NHẤT — ĐẠI TÁ"* (2.5 s)
- `TK3.01#5` → *"NGĂN KÉO THỨ HAI — KẺ SĂN MỒI BÓNG ĐÊM"* (2.5 s)
- `TK3.01#7` → *"TRUNG HÒA ĐẠO ĐỨC (NEUTRALIZATION)"* (3.0 s)
- `TK3.01#8` → *"“MỘT MÓN KỶ NIỆM”"* (2.5 s)
- `TK3.01#10` → *"“TÔI KHÔNG BIẾT CÂU TRẢ LỜI”"* (2.5 s)

**Nguồn dữ kiện:** 3.04#1-#2 · 3.08#1-#13 · nguon_tham_khao.md (bản ghi thẩm vấn 07/02/2010)

### 3.4 CLIP TK4 — "Không một lời xin lỗi nào nhắc tới nạn nhân"

*Ước lượng 82.6 s (10 câu) · BGM `bgm_piano_warm.mp3` (Hồi 5 — bed tập: bgm_piano_warm.mp3) · SFX: amb_courtroom.wav (nền) · fx_gavel_triple.wav · fx_fire_whoosh.wav · amb_fire.wav · fx_heartbeat_slow.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK4.01#1` | H | neutral | -0.02 | 0.6 | Không một lời xin lỗi nào nhắc tới nạn nhân. | 4.11#6 · 4.11#7 |
| `TK4.01#2` | C | sad | -0.04 | 0.8 | Trong phòng thẩm vấn, nỗi lo hắn thốt ra chỉ xoay quanh việc người vợ nhìn nhận hắn ra sao, và sự sụp đổ danh tiếng của căn cứ quân sự. Hắn không nhắc đến nỗi đau của người phụ nữ hay gia đình nạn nhân. | 4.11#6 · 4.11#7 |
| `TK4.01#3` | C | sad | -0.04 | 0.8 | Đó không phải sự ăn năn hối cải chân chính, mà là sự thương hại bản thân tột độ khi tấm mặt nạ danh dự xây suốt hai mươi lăm năm vỡ vụn. | 4.11#8 · 4.11#9 |
| `TK4.01#4` | H | neutral | -0.02 | 0.6 | Ngày 18 tháng 10 năm 2010, hắn nhận tội trước tòan bộ 88 cáo buộc. | 5.02#1 · 5.02#3 |
| `TK4.01#5` | H | neutral | -0.02 | 0.8 | Ba ngày sau, thẩm phán tuyên hai mức tù chung thân chạy song song cho hai tội danh nghiêm trọng nhất, cộng thêm các mức tù khác. Mức án chung thân với hai mươi lăm năm không được xét ân xá. | 5.02#4 · 5.02#5 |
| `TK4.01#6` | H | neutral | -0.02 | 0.6 | Nhưng bản án lớn nhất với một kẻ ái kỷ như hắn là sự sụp đổ về danh dự và quyền lực: quân hàm bị thu hồi, huân chương bị cắt thành từng mảnh. | 5.04#1 · 5.04#2 · 5.04#3 |
| `TK4.01#7` | H | neutral | -0.02 | 0.7 | Quân đội Canada còn làm một việc chưa từng có tiền lệ: đốt toàn bộ quân phục và trang phục mang tên hắn tại một lò tiêu hủy tài liệu mật. | 5.04#5 |
| `TK4.01#8` | D | neutral | -0.03 | 0.7 | Theo người phát ngôn quân đội Hubert Genest: không có nghi lễ chính thức, cũng không có ảnh chụp. | 5.04#6 · 5.04#7 |
| `TK4.01#9` | C | neutral | -0.02 | 0.6 | Về mặt tâm lý, đó là biểu hiện kinh điển của sự sụp đổ cái tôi ái kỷ: khi không còn quyền kiểm soát, kẻ săn mồi chỉ còn lại sự tự thương hại. | 5.06#4 |
| `TK4.01#10` | H | neutral | -0.02 | 0.0 | Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK4.01#1` | `tk02_interrogation_early` | still | 2.9 s |
| `TK4.01#2` | `tk02_two_chairs` | pull | 11.0 s |
| `TK4.01#3` | `tk02_head_down` | push | 7.9 s |
| `TK4.01#4` | `tk02_courtroom` | still | 6.4 s |
| `TK4.01#5` | `tk02_gavel` | push | 12.0 s |
| `TK4.01#6` | `tk02_courtroom` | pan | 9.9 s |
| `TK4.01#7` | `tk02_uniform_fire` | still | 9.1 s |
| `TK4.01#8` | `tk02_uniform_fire` | pan | 4.9 s |
| `TK4.01#9` | `tk02_brain_neural` | pull | 8.1 s |
| `TK4.01#10` | `tk02_podcast_desk` | still | 4.1 s |

**Thẻ chữ trên hình (overlay card):**
- `TK4.01#1` → *"KHÔNG MỘT LỜI XIN LỖI NÀO NHẮC TỚI NẠN NHÂN"* (3.0 s)
- `TK4.01#3` → *"KHÔNG PHẢI ĂN NĂN — LÀ TỰ THƯƠNG HẠI BẢN THÂN"* (2.5 s)
- `TK4.01#4` → *"88 CÁO BUỘC"* (2.5 s)
- `TK4.01#5` → *"CHUNG THÂN 25 NĂM — KHÔNG ĐƯỢC XÉT ÂN XÁ"* (2.5 s)
- `TK4.01#7` → *"ĐỐT TOÀN BỘ QUÂN PHỤC MANG TÊN HẮN"* (2.5 s)
- `TK4.01#9` → *"SỤP ĐỔ CÁI TÔI ÁI KỶ (NARCISSISTIC COLLAPSE)"* (3.0 s)

**Nguồn dữ kiện:** 4.11#1-#9 · 5.02#1-#6 · 5.04#1-#9 · 5.06#1-#4 · nguon_tham_khao.md (phán quyết 21/10/2010 · thông cáo Bộ Quốc phòng)

### 3.5 CLIP TK5 — "Hãy luôn tin vào trực giác của bạn"

*Ước lượng 62.5 s (8 câu) · BGM `bgm_ambient_deep.mp3` (Hồi 5 — bed tập: bgm_piano_warm.mp3 (clip kết, dùng ambient_deep để tách tiếng với TK4)) · SFX: amb_road_night.wav (nền) · fx_tension_tick.wav · fx_stinger.wav · fx_heartbeat_slow.wav*

| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |
|---|---|---|---|---|---|---|
| `TK5.01#1` | H | neutral | -0.02 | 0.6 | Nếu bạn cảm thấy một sự bất an mơ hồ, nếu ranh giới riêng tư của bạn bị xâm phạm dù chỉ nhỏ nhất, đừng hợp lý hóa hay coi thường nó. | 5.08#4 |
| `TK5.01#2` | D | neutral | -0.03 | 0.6 | Trong vụ án này, trước khi sự thật vỡ lở, thị trấn Tweed đã sống trong một nỗi bất an mơ hồ đến ngạt thở. | 4.06#1 |
| `TK5.01#3` | N2 | sad | -0.04 | 0.8 | Đồ đạc riêng tư thỉnh thoảng bị xáo trộn, cửa nẻo có dấu cạy phá nhưng không mất tiền bạc. Chúng tôi tưởng mình đang hoang tưởng. | 4.06#2 · 4.06#3 |
| `TK5.01#4` | H | neutral | -0.02 | 0.8 | Tội ác không bao giờ bắt đầu từ một vụ án mạng. Nó luôn bắt đầu từ những bước lấn ranh giới rất nhỏ: một cái nhìn trộm, một lần lục lọi đồ riêng tư, một sự xâm phạm không bị trừng phạt. | 5.07#5 · 5.07#6 |
| `TK5.01#5` | C | neutral | -0.02 | 0.7 | Địa vị, bằng cấp hay quân hàm lộng lẫy chỉ là lớp áo khoác xã hội, không phải tấm bảo chứng cho sự lương thiện của một tâm hồn. | 5.07#4 |
| `TK5.01#6` | D | neutral | -0.03 | 0.6 | Sự kiêu hãnh của một kẻ ái kỷ luôn để lại dấu vết. | 5.08#2 |
| `TK5.01#7` | D | neutral | -0.03 | 0.8 | Hãy luôn tin vào trực giác của bạn. Trực giác sinh tồn chính là hệ thống cảnh báo sớm giúp bảo vệ mạng sống của chúng ta. | 5.08#3 · 5.08#5 |
| `TK5.01#8` | H | neutral | -0.02 | 0.0 | Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio. | CTA — không phải dữ kiện |

| Nền | Chuyển động | Ước lượng |
|---|---|---|
| `TK5.01#1` | `tk02_red_flags` | still | 9.3 s |
| `TK5.01#2` | `tk02_town_snow` | pull | 6.5 s |
| `TK5.01#3` | `tk02_cottage_search` | push | 7.7 s |
| `TK5.01#4` | `tk02_escalation_stairs` | pan | 12.6 s |
| `TK5.01#5` | `tk02_oath_hall` | pull | 7.0 s |
| `TK5.01#6` | `tk02_escalation_stairs` | pan | 3.4 s |
| `TK5.01#7` | `tk02_red_flags` | still | 7.0 s |
| `TK5.01#8` | `tk02_podcast_desk` | still | 4.1 s |

**Thẻ chữ trên hình (overlay card):**
- `TK5.01#1` → *"ĐỪNG HỢP LÝ HÓA SỰ BẤT AN"* (2.5 s)
- `TK5.01#2` → *"DẤU HIỆU SỚM: BẤT AN MƠ HỒ"* (2.5 s)
- `TK5.01#4` → *"TỘI ÁC BẮT ĐẦU TỪ NHỮNG BƯỚC RẤT NHỎ"* (2.5 s)
- `TK5.01#7` → *"HÃY LUÔN TIN VÀO TRỰC GIÁC CỦA BẠN"* (3.0 s)

**Nguồn dữ kiện:** 4.06#1-#4 · 5.07#4-#6 · 5.08#2-#5 · nguon_tham_khao.md (The Gift of Fear)

---

### 3.6 Thời lượng — cách đo, không phải cảm tính

Ước lượng dựa trên **số đo thật** của chính tập 02, không phải trên cảm tính:

| Vai | Số giây / từ (đo trên master Tập 02) | Tương đương |
|---|---|---|
| H | 0.2921 s/từ | 3.42 từ/giây |
| D | 0.2600 s/từ | 3.85 từ/giây |
| C | 0.2397 s/từ | 4.17 từ/giây |
| N2 | 0.2868 s/từ | 3.49 từ/giây |

* Nguồn: `.work/timeline_s_t02.json` — timeline **đo bằng ASR trên mp4 thành phẩm** Tập 02 (203 câu).
* Số từ đếm **sau khi đổi số → chữ** (`vi_numbers`) — đúng phần TTS đọc ra tiếng.
* **Kiểm chéo (leave-one-out) trên 203 câu thật:** sai số tuyệt đối trung bình 11,0 %/câu, trung vị 6,7 %.
* **Mô phỏng mức clip (nhóm 13 câu, 2.000 lần):** MAE 3,7 % · trung vị 3,1 % · p90 7,3 % ⇒ **sai số kỳ vọng của một clip 80 s là ±5,8 s**.
* ⇒ Số đo **thật** của clip chỉ có sau khi sinh WAV: cộng `dur` từng file + `pause_after`, rồi đo lại trên mp4 cuối (A7).

---

## 4. Bố cục màn hình 9:16 (1080 × 1920)

Áp dụng safe zone của TikTok (bám template In-Feed, thiết kế theo trường hợp xấu nhất):

| Thành phần | Vị trí (x, y) | Cỡ chữ | Ghi chú |
|---|---|---|---|
| **Chữ hook** (0–3 s) | x 120–780, y 300–700 | 76 px đậm, tối đa 2 dòng | có `text_scrim`; chữ Pillow vẽ sau, **không** để AI vẽ chữ |
| **Phụ đề burn-in** | x 120–780, y 1.020–1.230 | 52 px, tối đa 2 dòng | nền scrim mờ 35 %; **nguyên văn** lời đọc (G6) |
| **Thẻ chữ overlay** | x 120–780, y 780–980 | 44 px | card tối 60 %, bo góc 12 px, hiện 2,5–3 s rồi fade 0,4 s |
| **Logo** | x 120–260, y 60–160 | — | tránh x > 780 (nút like/comment/share) |
| **Nền** | phủ kín 1080×1920 | — | nền dọc `tk02_*`; nếu chưa có thì dùng phương án B: blur-fill + zoom 4 % |

Chuyển động `pull` / `push` / `pan` / `still` dùng đúng bộ của pipeline hiện tại (`.work/build_video3.py`).

> **Luật V3 áp cho clip:** mọi con số trên thẻ overlay phải có trong câu đang đọc (đã kiểm ở mục 10).

---

## 5. Chỉ dẫn tạo audio (phần người dùng làm)

> **Mục tiêu:** 53 câu → 53 file WAV 24 kHz mono.

### 5.1 Engine: Higgs Audio v3 + giọng mẫu VoxCPM2 (đúng giọng của Tập 02)

| Tham số | Giá trị |
|---|---|
| Mô hình | `bosonai/higgs-tts-3-4b` (Higgs Audio v3) |
| Dataset giọng mẫu | `chiduong2026/amber-eyes-voice-ref-voxcpm2` (đã có sẵn, `ready`) |
| Vai → clip tham chiếu | **H → `assets/voice_ref_voxcpm2/H.wav`** · **D → `assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav`** · **C → `assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav`** · **N1 → `assets/voice_ref_voxcpm2_g9/W6_LOW.wav`** · **N2 → `assets/voice_ref_voxcpm2_g9/W5_HIGH.wav`** |
| temperature / top_p / top_k | 0,8 / 0,95 / 50 |
| max_new_tokens | 1.196 (≈ 47 s — dư cho câu ngắn) |
| sample_rate | 24.000 Hz · `fade_in_ms` 30 · `fade_out_ms` 15 |
| Seed | `sha256(id\|role\|ref\|temp\|vN)` → `int(hex[:8],16)`; **sinh 2 bản/câu** (v0, v1) |
| Cấm | mọi thẻ `<\|emotion:...\|>` — **chỉ** dùng `<\|prosody:pause\|>` sau dấu `:` trước câu trích |

> **Khác Tập 01:** Tập 02 dùng **bộ giọng mới** cho vai D và C (`D_NEW_subbass-husky_t02`, `C_NEW_alto-brisk_t03` — đã qua G9 cho tập này). Clip Tập 02 phải dùng **đúng hai file này**, nếu không giọng clip sẽ lệch giọng tập trên YouTube.

### 5.2 Quy ước đặt tên & thư mục (bắt buộc để dựng được video)

```
.work/audio_s_tk_t02/
├── TK1.01_01.wav      # <clip>.<câu>_<số câu>.wav   (mã "TK1.01#1" → "TK1.01_01.wav")
├── TK1.01_02.wav
├── …
└── manifest_tk_t02.json
```

`manifest_tk_t02.json` (mỗi dòng một câu):

```json
{"id": "TK1.01#1", "vai": "H", "file": "TK1.01_01.wav", "dur": 6.42,
 "emotion": "neutral", "speed": -0.02, "pause_after": 0.5, "variant": 0}
```

### 5.3 Cổng kiểm audio (bắt buộc trước khi dựng video)

| Cổng | Ngưỡng | Cách đo |
|---|---|---|
| Đủ file | 53/53 WAV + manifest | đếm file |
| Định dạng | 24.000 Hz, mono, PCM 16-bit | `ffprobe` |
| Độ dài mỗi câu | 1,5–14 s | đo trên file |
| Tổng clip | 45–95 s (mục tiêu 65–90 s) | cộng `dur` + `pause_after` |
| CER | **< 2 %** mỗi câu (G12) | Whisper (`measure_cer_prod.py`) |
| F0 / G9 | H–D ≥ 4 nc · C–H ≥ 4 nc · C–D ≥ 4 nc | `check_higgs_f0.py` |
| Nghe mù (G10) | mỗi vai nghe liền ra **1 người**, 3 vai tách bạch | tai người |
| Không câm | 0 khoảng > 0,3 s ở −60 dB trong clip | `qc_pause_gate.py --pre` |
| Lời đọc | đúng **nguyên văn** dòng trong `SPEC_AUDIO_CLIP_TAP02.json` (G6) | so từng chữ |

---

## 6. Âm thanh nền của clip (bản quyền — áp dụng tuyệt đối)

| Nguồn | Clip TikTok |
|---|---|
| BGM MiniMax (9 file trong `assets/bgm/`) | ✅ dùng được — **có điều kiện**: phải xác minh quyền thương mại của bề mặt đã sinh (mục 2.4 kế hoạch mẹ — **vẫn chưa làm**) |
| SFX tự tổng hợp `assets/sfx/t2/_code/` | ✅ dùng được — của chính kênh |
| SFX Freesound **CC0** | ✅ dùng được |
| **SFX trong `assets/sfx/t2/`** (không phải `_code/`) | ❌ **YouTube Audio Library ⇒ cấm trên TikTok** |
| `bgm_guitar_acoustic_60s.mp3`, `bgm_church_organ.mp3` | ❌ **YouTube Audio Library ⇒ cấm trên TikTok** |
| Nhạc trending | ❌ không dùng |

> **Đây là bẫy dễ sai nhất của Tập 02:** tập dùng SFX ở `assets/sfx/t2/*.wav` (bản YouTube Audio Library). Folder `_code/` **cùng tên file, bản tự tổng hợp** — clip TikTok phải lấy từ `_code/`.

Mức: giọng −16 LUFS (đo trên mp4 cuối) · BGM −26 dB khi có lời, nâng −14 dB ở nghỉ 0,8–1,2 s trước câu chốt · **luôn có lớp nền môi trường** bên dưới (A1/V4: cấm câm tuyệt đối > 0,3 s).

---

## 7. Nền dọc 9:16 cần tạo (`tk02_*`)

Tập 01 đã có 16 nền dọc `tk01_*` trong `assets/bg/` (1080×1920). Tập 02 cần **27 nền** cùng phong cách:

| Nền dọc cần tạo | Nguồn 16:9 trong `assets/bg/_raw/` | Dùng cho | File nguồn có sẵn? |
|---|---|---|---|
| `tk02_brain_neural` | `t2_brain_neural` | TK1 · TK3 · TK4 | ✅ |
| `tk02_checkpoint` | `t2_checkpoint` | TK2 | ✅ |
| `tk02_command_chair` | `t2_command_chair` | TK3 | ✅ |
| `tk02_cottage_search` | `t2_cottage_search` | TK5 | ✅ |
| `tk02_courtroom` | `t2_courtroom` | TK4 | ✅ |
| `tk02_drawer_dark` | `t2_drawer_dark` | TK1 · TK3 | ✅ |
| `tk02_escalation_stairs` | `t2_escalation_stairs` | TK1 · TK5 | ✅ |
| `tk02_folder_tree` | `t2_folder_tree` | TK1 | ✅ |
| `tk02_gavel` | `t2_gavel` | TK4 | ✅ |
| `tk02_head_down` | `t2_head_down` | TK3 · TK4 | ✅ |
| `tk02_hidden_drive` | `t2_hidden_drive` | TK3 | ✅ |
| `tk02_house_missing` | `t2_house_missing` | TK1 · TK2 | ✅ |
| `tk02_interrogation_early` | `t2_interrogation_early` | TK3 · TK4 | ✅ |
| `tk02_medals_cut` | `t2_medals_cut` | (dự phòng) | ✅ |
| `tk02_oath_hall` | `t2_oath_hall` | TK1 · TK2 · TK5 | ✅ |
| `tk02_open_window` | `t2_open_window` | TK1 | ✅ |
| `tk02_podcast_desk` | `t2_podcast_desk` | TK1 · TK2 · TK3 · TK4 · TK5 | ✅ |
| `tk02_red_flags` | `t2_red_flags` | TK5 | ✅ |
| `tk02_siren_wall` | `t2_siren_wall` | TK2 | ✅ |
| `tk02_stairs_dark` | `t2_stairs_dark` | TK3 | ✅ |
| `tk02_suv_stop` | `t2_suv_stop` | TK2 | ✅ |
| `tk02_tire_track` | `t2_tire_track` | TK2 | ✅ |
| `tk02_town_snow` | `t2_town_snow` | TK5 | ✅ |
| `tk02_two_chairs` | `t2_two_chairs` | TK1 · TK4 | ✅ |
| `tk02_two_drawers` | `t2_two_drawers` | TK3 | ✅ |
| `tk02_two_masks` | `t2_two_masks` | TK3 | ✅ |
| `tk02_uniform_fire` | `t2_uniform_fire` | TK4 | ✅ |

**Quy trình tạo:**

1. Sinh nền dọc bằng pipeline FLUX Kaggle sẵn có (`.work/bg_jobs_tap02.json` → kernel) — 1080×1920, ~26 ảnh. Prompt phải **không có chữ** (AI vẽ chữ rác); chữ trên hình luôn do Pillow vẽ sau.
2. Nền phải **có nội dung cảnh**, không được là gradient trừu tượng (H19).
3. Người thật trong nền phải là **bóng**, mặt chìm hoàn toàn (V5) — các nền `t2_two_chairs`, `t2_head_down`, `t2_suv_stop` đã có sẵn bóng đúng cách.
4. Ghi mỗi ảnh mới vào `provenance.json` (L7).

> ⚠ **Phát hiện khi rà soát (20/11/2026):** bản 16:9 đã xử lý `assets/bg/t2_*.png` **không còn trong `assets/bg/`** — chỉ còn ảnh gốc `assets/bg/_raw/t2_*` (2752×1536). Clip dọc không cần bản 16:9, nhưng nếu dựng theo **phương án B (blur-fill)** thì lấy trực tiếp từ `_raw/` được. Nếu muốn dùng lại pipeline cũ thì phải chạy lại `fix_backgrounds.py`.

---

## 8. Caption + hashtag (sẵn sàng dán)

**TK1** (422 ký tự)

```
Bốn nấc thang. Rồi một vụ án mạng. 👁️

Tập 02 · Đại tá hai mặt — chỉ dấu #8: quỹ đạo leo thang hành vi.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · leo thang hành vi · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.

#AmberEyes #TamLyToiPham #HosoCoThat #Escalation #QuyDaoLeoThang #TrueCrime #MoiTuanMotTap
```

**TK2** (430 ký tự)

```
Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào. 👁️

Tập 02 · Đại tá hai mặt — chỉ dấu #9: hiệu ứng hào quang.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · hiệu ứng hào quang · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.

#AmberEyes #TamLyToiPham #HosoCoThat #HieuUngHaoQuang #QuanDoi #TrueCrime #MoiTuanMotTap
```

**TK3** (440 ký tự)

```
Hai cuộc đời. Một câu chuyện để tự bào chữa. 👁️

Tập 02 · Đại tá hai mặt — chỉ dấu #5: hệ thống tự bào chữa.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · phân mảnh tâm trí · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.

#AmberEyes #TamLyToiPham #HosoCoThat #Compartmentalization #SelfJustification #TrueCrime #MoiTuanMotTap
```

**TK4** (425 ký tự)

```
Không một lời xin lỗi nào nhắc tới nạn nhân. 👁️

Tập 02 · Đại tá hai mặt — chỉ dấu #4: sụp đổ cái tôi ái kỷ.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · sụp đổ cái tôi · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.

#AmberEyes #TamLyToiPham #HosoCoThat #NarcissisticCollapse #BanAn #TrueCrime #MoiTuanMotTap
```

**TK5** (422 ký tự)

```
Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó. 👁️

Tập 02 · Đại tá hai mặt — chỉ dấu #10: bài học sinh tồn.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · trực giác sinh tồn · hồ sơ có thật

Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.

#AmberEyes #TamLyToiPham #HosoCoThat #TrucGiac #CanhGiuAnToan #TrueCrime #MoiTuanMotTap
```

> **Bắt buộc kèm theo mỗi caption:** dòng *"Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự."* + bật toggle **"AI-generated content"** khi đăng (TikTok bắt buộc ghi nhãn AIGC).
> Bản mô tả dài cho ô Description của TikTok Studio: `MoTa_Dai_TK*.txt` (mục 13).
> Bản mô tả **ngắn** (rút gọn, theo chuẩn Tập 01): `MoTa_Ngan_TK*.txt` (mục 8b).

---

## 8b. Mô tả ngắn (bản rút gọn, theo chuẩn `Tap01/MoTa_Dai_TK1.txt`)

> Bản mô tả ngắn dùng khi: TikTok Studio hiển thị phần đầu mô tả dài bị cắt, hoặc đăng lại clip ở nơi khác cần bản gọn. Bản dài vẫn là bản chính để dán vào ô Description.

**TK1 — MoTa_Ngan_TK1.txt** (1424 ký tự)

```
Bốn nấc thang. Tám mươi hai vụ trộm. Rồi một vụ án mạng. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #8: quỹ đạo leo thang hành vi.

Hồ sơ này tái dựng được bốn nấc thang, mỗi nấc là một bước lấn ranh giới rất nhỏ, không bị trừng phạt, và không bị ai chặn lại:
• NẤC 1 — nhìn trộm ban đêm: đứng ngoài bóng tối để rình rập phụ nữ qua khung cửa sổ.
• NẤC 2 — từ 9/2007 đến 11/2009, tổng cộng 82 vụ trộm đồ riêng tư. Không lấy tiền, không lấy trang sức quý giá. Nghi thức lặp lại y hệt ở mọi căn nhà: chụp ảnh, lấy đồ, rồi ghi chép lại tỉ mỉ.
• NẤC 3 — xâm nhập khi có người ở nhà, tháng 9/2009.
• NẤC 4 — đoạt mạng nạn nhân: cuối tháng 11/2009, nữ hạ sĩ Marie-France Comeau, 37 tuổi. Chỉ hai tháng sau đó là Jessica Lloyd.

Bước ngoặt của hồ sơ này: khi hành vi cũ trở nên quen thuộc, cơ chế "đói ảo tưởng" buộc hắn phải tăng liều lượng rủi ro để tìm lại khoái cảm ban đầu. Và ngòi nổ tâm lý nằm đúng chỗ đáng lẽ phải chặn hắn lại — tháng 7/2009, hắn được thăng cấp chỉ huy trưởng căn cứ không quân Trenton.

Theo bạn, ở nấc thang nào thì hành vi của một người còn có thể bị chặn lại? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #QuyDaoLeoThang #TrueCrime
```

**TK2 — MoTa_Ngan_TK2.txt** (1525 ký tự)

```
Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #9: hiệu ứng hào quang.

Đêm 28/01/2010, Jessica Lloyd — nữ nhân viên 27 tuổi, sống một mình ở Belleville — biến mất khỏi nhà riêng. Một tuần sau đó, vào tối 4/2, cảnh sát lập một trạm kiểm soát lưu động kéo dài suốt đêm, săn một dấu vết duy nhất: vệt vân lốp xe địa hình hiếm gặp in hằn trên nền tuyết.
• Trong dòng xe đi qua trạm có một chiếc Nissan Pathfinder — chủ xe lái chiếc Pathfinder thay vì chiếc BMW mà ông ta vẫn thường đi.
• Vân lốp xe của ông ta rất giống dấu vết trên tuyết. Nhưng trước một sĩ quan cấp cao đĩnh đạc, các sĩ quan tuần tra không thể giữ ông ta lại — họ chỉ ghi nhận thông tin rồi kính cẩn chào cho đi.

Bước ngoặt của hồ sơ này: đây là hiệu ứng hào quang — một tấm khiên vô hình khiến cả xã hội lẫn cơ quan thực thi pháp luật bị che mắt suốt nhiều năm ròng. Quân phục đại tá lộng lẫy, chiến công lái chuyên cơ cho Hoàng gia và Thủ tướng, tiếng tay quân đội từng đứng nghiêm chào — không một thứ nào là bằng chứng cho sự lương thiện của một tâm hồn.

Theo bạn, vì sao một chiếc quân hàm lộng lẫy lại khiến cả cơ quan thực thi pháp luật không dám hỏi một câu? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #HieuUngHaoQuang #TrueCrime
```

**TK3 — MoTa_Ngan_TK3.txt** (1578 ký tự)

```
Hai cuộc đời. Một cơ thể. Một câu chuyện để tự bào chữa. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #5: hệ thống tự bào chữa.

Trước khi phân tích, một điều phải nói rõ: không tồn tại một chẩn đoán lâm sàng công khai nào về Russell Williams. Các khung lý thuyết dưới đây là công cụ phân tích phổ biến trong tâm lý học tội phạm — chúng giúp ta đặt câu hỏi đúng, chứ không phải một sự phán xét đã được cơ quan chuyên môn xác nhận.
• Phân mảnh tâm trí (compartmentalization): bộ não khóa hai luồng nhận thức trái ngược vào hai ngăn kéo hoàn toàn biệt lập — người chỉ huy mẫu mực và kẻ săn mồi bóng đêm.
• Trung hòa đạo đức (neutralization): trong 82 vụ trộm đầu tiên, hắn tự nhủ "mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm". Đến khi xảy ra án mạng, hắn lại tự biện minh rằng nạn nhân đã thấy mặt mình, cô ta ép mình phải ra tay để tự vệ.

Bước ngoặt của hồ sơ này: vì lương tri đã bị khóa trong ngăn kéo kia, hắn không thể tự giải thích một cách có lương tri. Câu trả lời trong bản ghi thẩm vấn trống rỗng đến lạnh người: "Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng."

Theo bạn, ranh giới nào tách một lời giải thích có lương tri khỏi một hệ thống tự bào chữa? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #Compartmentalization #TrueCrime
```

**TK4 — MoTa_Ngan_TK4.txt** (1544 ký tự)

```
Không một lời xin lỗi nào nhắc tới nạn nhân. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #4: sụp đổ cái tôi ái kỷ.

Khi chiếc ổ cứng bị tìm thấy, bức tường ngăn cách giữa hai ngăn kéo tâm trí vỡ vụn. Và câu hỏi quan trọng nhất mà bản án không trả lời được, là thái độ của hắn.
• Trong phòng thẩm vấn, những nỗi lo hắn thốt ra chỉ xoay quanh việc người vợ nhìn nhận hắn ra sao, và sự sụp đổ danh tiếng của căn cứ quân sự. Hắn không hề nhắc đến nỗi đau đớn cùng cực của những người phụ nữ hay gia đình nạn nhân.
• Tháng 10/2010, Tòa Thượng thẩm Ontario xét xử tại thị trấn Belleville, thẩm phán Robert Scott. Ngày 21/10, mức án chung thân 25 năm — đúng mức tối thiểu mà luật hình sự Canada bắt buộc cho tội danh nghiêm trọng nhất.
• Bản án lớn nhất là sự sụp đổ hoàn toàn về danh dự và quyền lực: quân hàm bị toàn quyền Canada thu hồi, huân chương bị cắt thành từng mảnh, tiểu sử bị gỡ khỏi trang web Bộ Quốc phòng ngay sau khi hắn bị bắt.

Bước ngoặt của hồ sơ này: đó không phải là sự ăn năn hối cải chân chính. Đó là sự thương hại bản thân tột độ khi nhận ra tấm mặt nạ danh dự hắn dày công xây dựng suốt hai mươi lăm năm đã vỡ vụn.

Theo bạn, khi nào sự hối hận biến thành công cụ để tự bảo vệ? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #NarcissisticCollapse #TrueCrime
```

**TK5 — MoTa_Ngan_TK5.txt** (1360 ký tự)

```
Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #10: bài học sinh tồn.

Trước khi sự thật vỡ lở, thị trấn Tweed sống trong một nỗi bất an mơ hồ. Đồ đạc riêng tư thỉnh thoảng bị xáo trộn, cửa nẻo có dấu cạy phá — nhưng không mất tiền bạc. Người dân tưởng mình đang hoang tưởng.
• Dấu hiệu sớm nhất: ranh giới riêng tư bị xâm phạm lặp đi lặp lại, nhưng không đi kèm thiệt hại vật chất — nên rất dễ bị bỏ qua.
• Tội ác không bao giờ bắt đầu từ một vụ án mạng. Nó luôn bắt đầu từ những bước lấn ranh giới rất nhỏ, không bị trừng phạt.
• Địa vị, bằng cấp hay quân hàm lộng lẫy chỉ là lớp áo khoác xã hội, không phải tấm bảo chứng cho sự lương thiện của một tâm hồn.

Bước ngoặt của hồ sơ này: nếu bạn cảm thấy một sự bất an mơ hồ, nếu ranh giới riêng tư của bạn bị xâm phạm dù chỉ nhỏ nhất, đừng hợp lý hóa hay coi thường nó. Trực giác sinh tồn chính là hệ thống cảnh báo sớm giúp bảo vệ mạng sống của chúng ta.

Theo bạn, tín hiệu cảnh báo nào trong đời thường mà bạn thường bỏ qua nhất? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #TrucGiac #TrueCrime
```

---

## 9. Hợp đồng giữa phần audio và phần dựng video

| Người làm | Việc | Bàn giao |
|---|---|---|
| **Người dùng** | Tạo 53 WAV + `manifest_tk_t02.json` theo mục 5 | `.work/audio_s_tk_t02/` |
| **AI (sau khi được duyệt)** | Sinh nền dọc `tk02_*`, dựng 5 clip 9:16, chạy 14 cổng QC | `02_SAN_XUAT/TIKTOK/Tap02/clip0*_TK*.mp4` + `BaoCao_QC_TikTok_Tap02.md` |

**Quy tắc dựng video bám tiêu chuẩn:** H6 (chữ = nguyên văn lời đọc) · H9 (đo tương phản chữ, bật `text_scrim` nếu cần) · A1 (0 khoảng câm > 0,3 s) · A7 (−16 LUFS, TP ≤ −1,5 dBFS) · G6 (lời đọc không đổi chữ) · **L10 (không commit media)**.

---

## 10. Cổng QC clip (14 mục — đo thật, không "nói xong" khi chưa đo)

| # | Kiểm | Ngưỡng | Trạng thái khi sinh kịch bản |
|---|---|---|---|
| 1 | Khung / tỉ lệ | 1080 × 1920, 9:16 | chưa dựng |
| 2 | Codec / fps | H.264 + AAC, 30 fps | chưa dựng |
| 3 | Dung lượng | ≤ 500 MB | chưa dựng |
| 4 | Độ dài | 45–95 s (mục tiêu 65–90 s) | ✅ ước lượng TK1 82 / TK2 76 / TK3 79 / TK4 83 / TK5 62 s |
| 5 | Âm lượng | −16 ± 1 LUFS · true peak ≤ −1,5 dBFS | chưa có audio |
| 6 | Khoảng câm | 0 khoảng > 0,3 s @ −60 dB | chưa có audio |
| 7 | Lệch hình/tiếng | ≤ 0,05 s | chưa dựng |
| 8 | Giải mã | 0 lỗi | chưa dựng |
| 9 | **Safe zone** | mọi chữ trong x 120–780, y 240–1.260 | chưa dựng |
| 10 | **Watermark** | 0 khung chứa watermark nền tảng khác | chưa dựng |
| 11 | **Chữ** | 0 chữ rác · 0 chữ trùng · 0 chữ chìm (đo tương phản) | chưa dựng |
| 12 | **Mặt người thật** | 0 vi phạm | chưa dựng |
| 13 | **Từ cấm V9** | 0 từ trong danh sách A9.2 | ✅ đã kiểm tự động (mục 11) |
| 14 | **Hook** | 3 giây đầu có chữ hook đọc được ở 100 % khung | ✅ hook ≤ 12 từ, 5/5 clip |

**Riêng cho Tập 02:** mọi dữ kiện trong lời đọc phải truy được về `.work/script_tap02.json` + `02_SAN_XUAT/Tap02/nguon_tham_khao.md` (K1/K2); **không** thêm tên riêng, số liệu hay chi tiết mới ngoài hai file này.

---

## 11. Tự kiểm kịch bản (đã chạy, có số đo)

| # | Kiểm | Kết quả |
|---|---|---|
| 1 | Từ cấm V9/A9.2 trong lời đọc + caption + mô tả dài + mô tả ngắn | ✅ 0 lỗi |
| 2 | G1 — ≤ 1 thẻ `<#0.35#>`/câu, sau dấu ':', không có '...' | ✅ 0 lỗi |
| 3 | G3 (4 emotion an toàn) · G4 (speed −0,06…+0,02) · G5 (pitch = 0) | ✅ 0 lỗi |
| 4 | V3 — số trên thẻ overlay phải có trong câu được trỏ tới | ✅ 0 lỗi |
| 5 | Hook ≤ 12 từ (mục 3.2 kế hoạch mẹ) | ✅ 5/5 đạt |
| 6 | Caption ≤ 2.200 ký tự (Content Posting API) | ✅ 5/5 đạt |
| 7 | Hashtag 5–8, có #AmberEyes + #HosoCoThat (mục 3.4) | ✅ 5/5 đạt |
| 7b | Dòng nhãn AIGC nằm trong thân caption (luật T3) | ✅ 5/5 đạt |
| 8 | Độ dài clip trong cổng 45–95 s (ước lượng có cơ sở đo) | ✅ 5/5 đạt |
| 9 | Nguồn 16:9 của 27 nền dọc `tk02_*` có trong `_raw/` | ✅ 27/27 có file |
| 10 | K10 — mỗi clip ≥ 1 chỉ dấu tâm lý | ✅ 5/5 đạt — phủ chỉ dấu #1, #3, #4, #5, #6, #8, #9, #10 |
| 11 | K5 — clip TK3 có câu cảnh báo “không có chẩn đoán lâm sàng công khai” | ✅ có |
| 12 | K2 — 2 câu trích phải nguyên văn trong kịch bản tập | ✅ 2/2 nguyên văn |
| 13 | G6 — .md và .json cùng sinh từ MỘT nguồn (`.work/_build_tk_tap02.py`) | ✅ không thể lệch — chung generator |
| 14 | L3 — thời lượng có số đo thật làm cơ sở (timeline Tập 02 đo bằng ASR) | ✅ tỉ lệ đọc đo trên 203 câu thật · LOO MAE 11,0 %/câu · mô phỏng clip MAE 3,7 % |
| 15 | Mô tả ngắn — dòng 1 = hook (chữ trên hình / lời đọc câu 1), khớp bản dài, 900–1.600 ký tự | ✅ 5/5 đạt |
| 16 | Mô tả dài — dòng đầu = hook (chữ trên hình / lời đọc câu 1) | ✅ 5/5 đạt |

---

## 12. Lịch trình đề xuất

| Tuần | Việc | Người |
|---|---|---|
| 1 | Người dùng tạo audio + duyệt văn bản lời dẫn · AI sinh nền dọc `tk02_*` | Người dùng + AI |
| 2 | AI dựng 5 clip → đo 14 cổng QC → người dùng duyệt hình + nghe giọng | AI → Người dùng |
| 3 | Đăng TK2 + TK1 (2 clip/tuần) · ghi số đo vào `BangTheoDoi_TikTok.csv` | Người dùng |
| 4 | Đăng TK4 + TK3 + TK5 · quyết định có làm nền dọc FLUX phương án A cho các tập sau không | Người dùng |

---

## 13. Việc CẦN NGƯỜI DÙNG QUYẾT ĐỊNH / XÁC NHẬN (L4)

| # | Việc | Vì sao cần người dùng |
|---|---|---|
| 1 | **Link YouTube Tập 02** | Chưa tồn tại trong repo. Caption + mô tả dài đang để placeholder `[LINK_TẬP 02 — cần điền]`. **Không tự bịa link** (L2). |
| 2 | **Xung đột thương hiệu lốp xe trong kịch bản tập** | Kịch bản `1.17#1` ghi *"hoa văn lốp xe địa hình Kumho"*, còn `nguon_tham_khao.md` ghi *"Yokohama IG20"*. Clip **không** nêu thương hiệu nào (nên an toàn), nhưng kịch bản tập nên được sửa cho khớp. |
| 3 | **Xác minh quyền thương mại BGM MiniMax** | Mục 2.4 kế hoạch mẹ — việc này **chưa làm**. Nếu 9 file BGM sinh từ app consumer không có gói thương mại thì phải thay bằng SFX tự tổng hợp. |
| 4 | **Nền dọc `tk02_*`** | Chưa có. Cần sinh 26 nền (mục 7) hoặc chấp nhận phương án B blur-fill từ `_raw/`. |
| 5 | **Mức độ nhạy cảm của TK4** | Clip nói về bản án; đã **tránh** nêu chi tiết tội danh (dùng “hai tội danh nghiêm trọng nhất”) và **không** nhắc chi tiết tự sát trong nhà tù (chỉ giữ “sụp đổ cái tôi ái kỷ”). Cần xác nhận mức này trước khi đăng. |
| 6 | **Số clip** | Đang 5 (TK1–TK5). TK5 là clip kết — có thể giữ lại làm clip thưởng sau khi 4 clip chính đã đo. |

---

## 14. Tài liệu liên quan

- `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` — kế hoạch mẹ (spec TikTok, chính sách, cổng QC, rủi ro)
- `02_SAN_XUAT/TIKTOK/Tap01/KE_HOACH_CLIP_TAP01.md` — khuôn mẫu của bộ này (Tập 01)
- `02_SAN_XUAT/TIKTOK/Tap02/SPEC_AUDIO_CLIP_TAP02.json` — **bảng đặc tả audio máy đọc được**
- `.work/_build_tk_tap02.py` — **nguồn sự thật** của kịch bản này (sinh ra cả .md lẫn .json)
- `01_KICH_BAN/Tap02/kichban_tap02_22102026.md` — kịch bản gốc Tập 02 (nguồn dữ kiện)
- `02_SAN_XUAT/Tap02/nguon_tham_khao.md` — nguồn đối chiếu dữ kiện
- `01_KICH_BAN/Tap02/REVIEW_kichban_tap02_10chiau.md` — bảng 10 chỉ dấu của Tập 02
- `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` — quy trình Higgs P0–P10 (Kaggle)
- `AGENTS.md` — L4/L5/L6/L7/L10 · K1–K10 · G1–G13 · A1–A13 · H6/H9/H17
