# -*- coding: utf-8 -*-
"""Dải nền / âm thanh MÔI TRƯỜNG nằm trong cue [BGM] và [Nghỉ …] — bổ sung sau review.
Cùng cấu trúc với DATA trong _sfx_analysis.py: (cue_id, mô tả, trạng thái, [file], ghi chú)
Trạng thái: MOI = phải tạo mới | SAN = đã có trong thư viện, tái dùng
"""
NEN = {
3: [
 ("BGM 1.01", "Gió rít lùa qua khe cửa sắt lạnh giữa đêm vắng", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Rè kim loại cổ điển của đường dây điện thoại đường dài 1970", "MOI", ["fx_phone_line_hiss_1970.wav"], "tuỳ chọn — bảng chuẩn sfx_tap03.json đã bỏ qua, dùng amb_winter_wind cho cả Hồi 1"),
 ("BGM 2.01", "Mưa rơi rả rích trên mui xe hơi", "SAN", ["t3/amb_rain_storm.wav"], "nền Hồi 2"),
 ("BGM 2.01", "Tiếng cần gạt nước kính chắn gió kêu kẽo kẹt", "SAN", ["—"], "KHÔNG CÓ track 'wiper' trong thư viện — bảng chuẩn sfx_tap03.json đã bỏ qua"),
 ("NGHI 1.11", "Chỉ còn tiếng bước chân vang vọng trong hành lang nhà tù", "SAN", ["footsteps.wav"], "đoạn nghỉ Hồi 1"),
],
4: [
 ("BGM 1.01", "Máy thở cơ học rít nhẹ đều đặn + tiếng bíp theo dõi sinh hiệu", "MOI", ["amb_hospital_ventilator.wav"], "nền Hồi 1"),
 ("NGHI 1.11", "Chỉ còn tiếng giọt nước nhỏ chậm rãi", "SAN", ["t3/amb_pipe_drain.wav"], "đoạn nghỉ Hồi 1"),
 ("NGHI 4.09", "Chuyển sang tiếng bước chân nặng nề trong phòng giam", "SAN", ["footsteps.wav"], "đoạn nghỉ Hồi 4"),
],
5: [
 ("BGM 1.01", "Máy đánh chữ cơ học lách cách gõ từng nhịp chậm rãi", "SAN", ["typewriter.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng gió đông rít từng hồi lạnh lẽo", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng nhịp tim đập chậm", "SAN", ["t2/fx_heartbeat_slow.wav"], "nền Hồi 2"),
 ("BGM 2.01", "Tiếng rè rè của cuộn băng từ phát lại bản ghi âm", "SAN", ["t3/fx_cassette_motor.wav"], "nền Hồi 2"),
 ("BGM 4.01", "Tiếng gõ phím vi tính trong phòng kỹ thuật số", "SAN", ["keyboard_night.wav"], "nền Hồi 4"),
 ("BGM 4.01", "Âm thanh quạt tản nhiệt máy chủ kêu vo ve", "MOI", ["amb_server_fan.wav"], "nền Hồi 4"),
 ("NGHI 1.11", "Chỉ còn tiếng tích tắc khô khốc của đồng hồ", "SAN", ["clock_tick.wav"], "đoạn nghỉ Hồi 1"),
],
6: [
 ("NGHI 2.12", "Tiếng còi xe cảnh sát xa xăm", "SAN", ["police_siren_distant.wav"], "đoạn nghỉ Hồi 2"),
 ("NGHI 5.05", "Tiếng thở dài trầm lặng", "MOI", ["fx_sigh_emotional.wav"], "đoạn nghỉ Hồi 5"),
],
7: [
 ("NGHI 2.11", "Tiếng thở dài buốt giá giữa đêm", "MOI", ["fx_sigh_emotional.wav"], "đoạn nghỉ Hồi 2"),
],
8: [
 ("NGHI 2.10", "Tiếng còi báo động xa xăm", "MOI", ["amb_alarm_siren_distant.wav"], "đoạn nghỉ Hồi 2 — dùng chung T12, T25"),
],
9: [
 ("BGM 2.01", "Tiếng gió sa mạc khô khốc (Spahn Ranch, Mojave)", "MOI", ["amb_desert_wind_dry.wav"], "nền Hồi 2 — KHÁC amb_wind_pines của Hồi 1"),
 ("NGHI 2.12", "Tiếng guitar bass rền rĩ u uất", "MOI", ["—"], "dùng track guitar acoustic đang cần tải cho BGM (chưa có trong assets/bgm/)"),
],
10: [
 ("BGM 1.01", "Tiếng gió rít hiu hắt trên xa lộ hoang vắng", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng kim đồng hồ tích tắc chậm rãi", "SAN", ["clock_tick.wav"], "nền Hồi 2"),
],
11: [
 ("BGM 1.01", "Tiếng gió rít hiu hắt bên bờ hồ Ontario", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng kim đồng hồ tích tắc chậm rãi", "SAN", ["clock_tick.wav"], "nền Hồi 2"),
],
12: [
 ("BGM 1.01", "Tiếng gió rít hiu hắt + âm thanh côn trùng nhiệt đới", "SAN", ["t2/amb_winter_wind.wav", "t3/amb_crickets_traffic.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng kim đồng hồ tích tắc giữa đêm rừng", "SAN", ["clock_tick.wav"], "nền Hồi 2"),
],
13: [
 ("BGM 1.01", "Tiếng tích tắc đều đặn của chiếc đồng hồ treo tường", "SAN", ["clock_tick.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng kim đồng hồ đếm từng giây vô vọng", "SAN", ["clock_tick.wav"], "nền Hồi 2"),
],
14: [
 ("BGM 1.01", "Tiếng sóng biển vỗ rì rào xa xa bên bờ biển La Jolla", "MOI", ["amb_ocean_waves_soft.wav"], "nền Hồi 1 — dùng chung T09, T18"),
],
15: [
 ("BGM 1.01", "Tiếng nước nhỏ giọt đều đặn", "SAN", ["t3/amb_pipe_drain.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng gió rít qua khe cửa sổ", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
],
16: [
 ("BGM 1.01", "Tiếng gió rít qua khe cửa sổ của tòa biệt thự cổ", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
],
17: [
 ("BGM 1.01", "Tiếng gió rít rợn người giữa đêm lạnh", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng thở gấp gáp trong bóng tối", "MOI", ["fx_breathing_tense_close.wav"], "nền Hồi 1 — dùng chung T12, T13, T19, T20, T22"),
],
18: [
 ("BGM 1.01", "Tiếng gió biển Hawaii", "MOI", ["amb_ocean_waves_soft.wav"], "nền Hồi 1 — dùng chung T09, T14"),
 ("BGM 1.01", "Tiếng chuông gió lạnh lẽo", "MOI", ["amb_wind_chime.wav"], "nền Hồi 1 — chuông gió là nốt nhạc nền, không phải tiếng động"),
],
19: [
 ("BGM 1.01", "Tiếng kim đồng hồ tích tắc nặng nề trong phòng thẩm vấn kín", "SAN", ["clock_tick.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng tích tắc đồng hồ lạnh lẽo và sắc lạnh", "SAN", ["clock_tick.wav"], "nền Hồi 2"),
],
20: [
 ("BGM 1.01", "Tiếng nhịp tim đập chậm", "SAN", ["t2/fx_heartbeat_slow.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng tích tắc đồng hồ kim loại ngột ngạt", "SAN", ["clock_tick.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng kim đồng hồ điện tử khô khốc và đều đặn", "SAN", ["clock_tick.wav"], "nền Hồi 2"),
],
21: [
 ("BGM 1.01", "Tiếng nhịp tim trầm đục", "SAN", ["t2/fx_heartbeat_slow.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng mưa rơi rả rích", "SAN", ["t3/amb_rain_storm.wav"], "nền Hồi 1"),
],
22: [
 ("BGM 2.01", "Tiếng tích tắc đồng hồ lạnh lẽo và sắc lạnh", "SAN", ["clock_tick.wav"], "nền Hồi 2"),
],
23: [
 ("BGM 1.01", "Tiếng kim đồng hồ tích tắc nặng nề", "SAN", ["clock_tick.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng còi xe cảnh sát rền rĩ trong đêm hè oi ả", "SAN", ["police_siren_distant.wav"], "nền Hồi 1"),
],
24: [
 ("BGM 1.01", "Tiếng gió thổi rít qua cánh đồng hoang vắng", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng mưa rơi rả rích", "SAN", ["t3/amb_rain_storm.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng bước chân vang vọng trong hành lang nhà tù bê tông", "SAN", ["footsteps.wav"], "nền Hồi 2"),
],
25: [
 ("BGM 1.01", "Tiếng gió rít", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng mưa rơi dồn dập trong đêm tối", "SAN", ["t3/amb_rain_storm.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng còi hú báo động", "MOI", ["amb_alarm_siren_distant.wav"], "nền Hồi 2 — dùng chung T08, T12"),
 ("BGM 2.01", "Tiếng bước chân chạy gấp gáp trên nền bê tông", "MOI", ["fx_footsteps_run_gravel.wav"], "nền Hồi 2 — dùng chung T24, T28"),
],
26: [
 ("BGM 1.01", "Tiếng gió rít qua những khu phố đổ nát", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng mưa tuyết rơi lạnh lẽo", "SAN", ["t3/amb_rain_storm.wav"], "nền Hồi 1 — lớp mưa; gió lạnh dùng amb_winter_wind_hollow ở cue 1.03"),
 ("BGM 2.01", "Tiếng máy đánh chữ lọc cọc", "SAN", ["typewriter.wav"], "nền Hồi 2"),
 ("BGM 2.01", "Tiếng bước chân trong hành lang ẩm mốc", "SAN", ["footsteps.wav"], "nền Hồi 2"),
],
27: [
 ("BGM 1.01", "Tiếng gió rít qua cánh rừng cao su bạt ngàn", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng mưa rả rích đầu mùa", "SAN", ["t3/amb_rain_storm.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng gõ bàn phím máy tính phân tích dữ liệu viễn thông", "SAN", ["keyboard_night.wav"], "nền Hồi 2"),
 ("BGM 2.01", "Tiếng bước chân trinh sát", "SAN", ["footsteps.wav"], "nền Hồi 2"),
],
28: [
 ("BGM 1.01", "Tiếng sấm rền từ xa", "MOI", ["amb_thunder_distant.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng gió bão rít qua những mái nhà tôn", "SAN", ["t2/amb_winter_wind.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng mưa như trút nước giữa đêm tối", "SAN", ["t3/amb_rain_storm.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng động cơ xe tuần tra gầm rú", "MOI", ["amb_car_engine_idle.wav"], "nền Hồi 2 — dùng chung T10, T22, T26"),
 ("BGM 2.01", "Tiếng bước chân hành quân gấp gáp trong rừng sâu", "MOI", ["fx_footsteps_chase_forest.wav"], "nền Hồi 2"),
],
29: [
 ("BGM 1.01", "Tiếng mưa đêm rả rích", "SAN", ["t3/amb_rain_storm.wav"], "nền Hồi 1"),
 ("BGM 1.01", "Tiếng còi tuần tra xa xăm của cảnh sát", "SAN", ["police_siren_distant.wav"], "nền Hồi 1"),
 ("BGM 2.01", "Tiếng gõ nhịp kim loại lạnh lẽo", "SAN", ["t2/fx_tension_tick.wav"], "nền Hồi 2"),
 ("BGM 2.01", "Tiếng quạt thông gió trong phòng hỏi cung", "MOI", ["amb_ceiling_fan.wav"], "nền Hồi 2 — dùng chung T12, T20"),
],
}
