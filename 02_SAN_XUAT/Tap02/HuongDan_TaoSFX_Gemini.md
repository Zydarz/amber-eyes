# HƯỚNG DẪN TẠO TIẾNG ĐỘNG BẰNG GEMINI — TẬP 02
> **Cập nhật 23/10/2026 — file này chỉ còn là phương án DỰ PHÒNG.**
> Thực tế đã lấy đủ **32/32 mã** của tập từ **YouTube Audio Library** (Studio → Thư viện âm thanh → Hiệu ứng âm thanh) và nhập vào `assets/sfx/t2/` — bảng track, thời lượng, mức khớp và giới hạn ở `AmThanh_Tap02.md` §3.3.1.
> 12 prompt Veo bên dưới **chưa chạy**. Giữ lại để làm tiếng cho các mã mà thư viện **không có đúng vật thể** — hiện là **17 mã đang dùng bản thay thế** gần nghĩa nhất, không phải ghi âm đúng vật thể trong phim:
>
> | Mã | Bản thay thế đang dùng | Nên tạo bằng Veo để thay |
> |---|---|---|
> | `fx_gavel_triple` | Wooden Bead Hitting Series (gõ hạt gỗ) | búa tòa gõ 3 tiếng |
> | `fx_chair_scrape` | Slide On Metal Grate Series (kéo lưới kim loại) | ghế kim loại kéo trên nền |
> | `fx_door_metal_slam` | Dumpster Door Slam (đóng cánh rác) | cửa sắt đóng sầm |
> | `fx_fire_whoosh` | Wind Drawn Into Fire (gió hút lửa) | quân phục cháy |
> | `fx_metal_crush` | Glass Crush (vỡ kính) | ép xe nát |
> | `fx_window_down` | Trunk Window Open Hydraulic Hiss | hạ kính xe |
> | `fx_flashlight` | Lamp Switch On/Off | đèn pin bật |
> | `fx_paper_folder` | Clipboard (kẹp giấy) | mở túi bìa hồ sơ |
> | `fx_map_unfold` | Paper Folding (gấp giấy) | mở bản đồ |
> | `fx_photo_slide` | Feeling Paper (cầm giấy) | trượt ảnh trên bàn |
> | `fx_camera_shutter` | Play And Stop On A Camera (bấm máy) | màn trập máy ảnh |
> | `fx_heartbeat_slow` | Human Breathing Mouth (thở) | nhịp tim chậm |
> | `amb_basement` | Metal Machine Hum (máy ù) | nền tầng hầm |
> | `amb_office_night` | Ambient Hum Air Conditioner (điều hoà) | nền văn phòng đêm |
> | `amb_interrogation` | Bowling Alley Room Tone (room tone trong nhà) | nền phòng thẩm vấn |
> | `fx_stinger` | Sci Fi Vortex (xoáy sci-fi) | tiếng sting khi hé lộ |
> | `fx_sub_drop` | High To Low Sweep (quét tần số giảm) | tiếng sub-drop |
>
> Lệnh nhập cho nhánh này: `py -3 .work/import_sfx_video.py --tool "Gemini (Veo)"` — nhớ chạy thêm `py -3 .work/yt_audio_library/normalize_crest.py` sau đó để giữ crest ≤ 20 dB (xem `AmThanh_Tap02.md` §3.3.2).


**Mục đích:** thay 12 tiếng tự tổng hợp nghe chưa thật, chủ yếu là tiếng gắn với vật thật, bằng tiếng do AI video tạo. Gemini tạo video bằng mô hình **Veo**, và Veo sinh **kèm âm thanh** theo mô tả. Ta chỉ lấy phần tiếng, bỏ hình.

## Cách làm (khoảng 2–3 phút mỗi tiếng)

1. Mở Gemini → chọn tạo **video** (Veo). Nếu tài khoản của bạn không có mục này, dùng **Google Flow** hoặc **Google AI Studio** (cũng chạy Veo).
2. Dán **nguyên văn** prompt tiếng Anh của từng mục bên dưới. Veo hiểu tiếng Anh tốt nhất. Mỗi prompt đã mô tả cả hình lẫn tiếng.
3. Nghe bản kết quả. **Làm lại** nếu gặp một trong các lỗi sau:
   - có nhạc nền
   - có giọng người nói hoặc hát
   - tiếng chính quá nhỏ, hoặc bị nhạc hay gió che
   - tiếng khác hẳn mô tả (ví dụ yêu cầu búa gỗ mà ra tiếng kim loại)
4. Tải video về (MP4), **đổi tên đúng mã** ở tiêu đề mục, ví dụ `fx_gavel_triple.mp4`.
5. Đặt tất cả vào thư mục `02_SAN_XUAT/Tap02/sfx_gemini/`.
6. Báo tôi, hoặc tự chạy lệnh dưới đây. Script sẽ lấy tiếng, cắt lặng, chuẩn hoá, rồi thay vào bộ âm thanh. Bản cũ được giữ lại để quay về.
   ```
   py -3 .work/import_sfx_video.py
   ```

**Không cần làm đủ 12 mục.** Mục nào chưa có thì video vẫn dùng bản tự tổng hợp. Thứ tự ưu tiên là theo mức nghe sai trong bài kiểm tra nghe mù: 1 → 12.

**Lưu ý bản quyền:** video Veo có dấu nước ẩn SynthID của Google. Trước khi bật kiếm tiền, đọc điều khoản dùng thương mại của Gemini/Veo cho gói bạn đang dùng. Script tự ghi nguồn gốc từng file vào `provenance.json`, ở trạng thái "chưa kiểm tra thương mại".

---

## 12 tiếng cần tạo

### `fx_tire_snow` — 1. Xe lăn bánh chậm trên tuyết rồi dừng (Hồi 1, trạm kiểm soát)
```text
Close low-angle shot at night on a snowy rural road: a dark SUV rolls slowly toward the camera over packed snow and comes to a full stop, engine idling. Sound only from the scene: tyres crunching and squeaking on cold packed snow, low engine idle, light winter wind. No music, no speech, no voices.
```

### `fx_window_down` — 2. Kính xe hạ xuống (Hồi 1, câu "hạ cửa kính xuống")
```text
Night, close-up of the driver's side window of a stopped SUV in light snowfall; the window glass slides down slowly and stops. Sound only from the scene: the electric window motor whirring, a rubber seal squeak, cold wind rushing in, the engine idling quietly. No music, no speech, no voices.
```

### `fx_police_radio` — 3. Bộ đàm cảnh sát (Hồi 1)
```text
Night, close-up of a police radio clipped to an officer's dark winter jacket at a roadside checkpoint, red and blue lights reflecting on it. Sound only from the scene: radio squelch, a short burst of muffled, distorted, unintelligible dispatcher chatter, squelch off, winter wind. No music, no clear words.
```

### `fx_footsteps_snow` — 4. Bước chân trên tuyết (Hồi 1)
```text
Night, low shot of heavy winter boots walking slowly through fresh deep snow on a quiet empty suburban sidewalk, about six steps. Sound only from the scene: crisp, distinct crunching footsteps in snow, faint wind. No music, no speech, no voices.
```

### `fx_chair_scrape` — 5. Kéo ghế kim loại + đặt cốc (Hồi 4, mở đầu phòng thẩm vấn)
```text
A small bare interrogation room lit by a fluorescent tube. A metal chair is pulled back across a tiled floor, the chair creaks as someone sits off-screen, then a ceramic coffee mug is set down on a wooden table. Sound only from the scene: metal chair legs scraping on tile, chair creak, the mug landing with a solid knock, fluorescent hum. No music, no speech.
```

### `fx_gavel_triple` — 6. Búa tòa gõ ba tiếng (Hồi 5, mở đầu)
```text
An empty wood-panelled courtroom. A wooden judge's gavel strikes its wooden sound block three times, slow and deliberate, about one second apart. Sound only from the scene: three sharp wooden knocks with natural courtroom reverb, then the quiet of a large room. No music, no speech, no voices.
```

### `fx_fire_whoosh` — 7. Quân phục bắt lửa (Hồi 5, đốt quân phục)
```text
Inside a bare concrete storage room, a folded military jacket on top of a metal drum catches fire and the flames grow steadily. Sound only from the scene: ignition whoosh, fabric burning, fire crackling and roaring inside the drum, concrete room echo. No music, no speech, no voices.
```

### `fx_metal_crush` — 8. Xe bị ép nát (Hồi 5)
```text
At a winter scrapyard in daylight, a hydraulic crusher slowly flattens an old dark SUV. Sound only from the scene: hydraulic whine, heavy metal crumpling and groaning, glass cracking, deep creaks and thuds. No music, no speech, no voices.
```

### `fx_door_metal_slam` — 9. Cửa sắt đóng sầm (Hồi 1, chuyển sang Điều tra viên)
```text
A long dim police station corridor; a heavy steel door swings shut and slams, the latch clicking. Sound only from the scene: a loud deep metallic slam, latch click, corridor reverb fading out. No music, no speech, no voices.
```

### `amb_interrogation` — 10. Nền phòng thẩm vấn (chạy dưới toàn bộ Hồi 4)
```text
Static shot of an empty small interrogation room: one table, two chairs, a fluorescent tube that flickers occasionally. Sound only from the scene: steady fluorescent light buzz, air vent hum, distant muffled corridor, very quiet room tone, nothing else. No music, no speech, no voices.
```

### `amb_road_night` — 11. Nền đường quê đêm tuyết ở trạm kiểm soát (dưới cảnh trạm kiểm soát)
```text
Static wide shot of a dark snowy rural highway at night with a police checkpoint in the distance, flashing lights, snow falling. Sound only from the scene: cold winter wind, a car engine idling nearby, one distant car passing on snow. No music, no speech, no voices.
```

### `amb_winter_wind` — 12. Nền gió tuyết ngoài trời (cảnh căn cứ, thị trấn đêm)
```text
Static wide shot of an empty small-town street at night during a light snowstorm, street lamps glowing. Sound only from the scene: steady cold winter wind with occasional gusts, faint snow hiss, nothing else. No music, no speech, no voices.
```

---

## Mẹo khi Veo cứ thêm nhạc hoặc giọng nói

- Thêm vào cuối prompt: `Diegetic sound effects only. The soundtrack must contain no music at all.`
- Tách nhỏ: mỗi video chỉ một hành động. Ví dụ tạo riêng tiếng ghế và tiếng cốc, đặt tên `fx_chair_scrape.mp4` và `fx_cup_down.mp4`. Script nhận cả hai, vì `fx_cup_down` cũng là một mã có sẵn.
- Nền môi trường (`amb_…`) chỉ cần 8 giây. Script nối vòng chúng xuyên cảnh, nhưng 8 giây có thể lộ chỗ lặp. Nếu Veo cho tạo dài hơn, chọn độ dài lớn nhất.
