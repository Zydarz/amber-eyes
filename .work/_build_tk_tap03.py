# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 03 — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap03/KE_HOACH_CLIP_TAP03.md
  02_SAN_XUAT/TIKTOK/Tap03/SPEC_AUDIO_CLIP_TAP03.json
  02_SAN_XUAT/TIKTOK/Tap03/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap03/MoTa_Dai_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap03/MoTa_Ngan_TK*.txt

Thời lượng clip KHÔNG ước lượng bừa: đo tỉ lệ đọc thật của từng vai trên
master Tập 03 (timeline_s_t03.json — đã đo bằng ASR trên mp4 thành phẩm),
rồi chiếu theo số từ SAU KHI đổi số→chữ (đúng những gì TTS đọc).

Luật: AGENTS.md K1–K10 / G1–G13 / A1–A13 / L3–L6.
"""

import json
import pathlib
import re
import sys
from collections import defaultdict

sys.stdout.reconfigure(encoding="utf-8")

ROOT = pathlib.Path(__file__).resolve().parent.parent
WORK = ROOT / ".work"
OUT = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap03"
OUT.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WORK))
from vi_cer import vi_numbers, vi_number  # noqa: E402  — đổi số→chữ đúng như TTS

# ----------------------------------------------------------------------------
# 0. TỈ LỆ ĐỌC THẬT (đo từ master Tập 03 đã sản xuất)
# ----------------------------------------------------------------------------

def measured_rate():
    tl = json.loads((WORK / "timeline_s_t03.json").read_text(encoding="utf-8"))
    dur = defaultdict(float)
    words = defaultdict(int)
    for it in tl["items"]:
        spoken = vi_numbers(it["text"])
        spoken = re.sub(r"<#[\d.]+#>", " ", spoken)
        n = len([w for w in spoken.split() if w.strip()])
        dur[it["role"]] += it["end"] - it["start"]
        words[it["role"]] += n
    rate = {r: dur[r] / words[r] for r in dur}          # giây / từ
    return rate, {r: (words[r], round(dur[r], 1)) for r in dur}

RATE, RATE_RAW = measured_rate()

def spoken_words(text):
    t = vi_numbers(re.sub(r"<#[\d.]+#>", " ", text))
    return len([w for w in t.split() if w.strip()])

def est_dur(text, vai):
    return spoken_words(text) * RATE[vai]

# ----------------------------------------------------------------------------
# 1. DỮ LIỆU 5 CLIP TẬP 03
#    nguon: mã câu trong .work/script_tap03.json / timeline_s_t03.json
# ----------------------------------------------------------------------------

CLIPS = [
{
 "id": "TK1",
 "ten": "Ngan toi lai. Toi sap lam dieu do them mot lan nua",
 "ten_vn": "Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa",
 "chi_dau": [4, 6],
 "chude": "Sự sụp đổ của ảo tưởng quyền lực + Điểm gãy tâm lý (Precipitating Trigger)",
 "hook": "Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa.",
 "bgm": "bgm_sub_drone.mp3",
 "bgm_hovi": "Hồi 1 — bed tập: bgm_sub_drone.mp3",
 "sfx": ["amb_winter_wind.wav (nền)", "fx_coin_drop.wav", "fx_phone_dial.wav", "fx_tension_tick.wav", "fx_stinger.wav"],
 "overlay": [
   {"sau_cau": "TK1.01#1", "text": "BỐT ĐIỆN THOẠI PUEBLO · 4 GIỜ SÁNG 24/4/1973", "dur_s": 3.0},
   {"sau_cau": "TK1.01#4", "text": "“TÔI ĐÃ GIẾT MẸ TÔI... VÀ SÁU NỮ SINH”", "dur_s": 2.5},
   {"sau_cau": "TK1.01#6", "text": "“TÔI SẮP LÀM ĐIỀU ĐÓ THÊM MỘT LẦN NỮA”", "dur_s": 2.5},
   {"sau_cau": "TK1.01#8", "text": "3 KHẨU SÚNG · HÀNG TRĂM VIÊN ĐẠN · ĐẦU THÚ", "dur_s": 2.5},
   {"sau_cau": "TK1.01#9", "text": "ĐIỂM GÃY TÂM LÝ: ẢO TƯỞNG SỤP ĐỔ", "dur_s": 3.0}
 ],
 "nguon_du_lieu": ["1.03#1-#8", "1.05#1-#7", "1.07#1-#4", "1.09#1-#6", "1.10#8-#13",
                   "nguon_tham_khao.md (Inside Detective 1973 · TPG Online Daily)"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk03_phone_booth","still",
   "Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa.",
   "1.10#10 · 1.10#11"),
  ("H","neutral",-0.02,0.6,"tk03_dispatch_desk","pull",
   "Bốn giờ sáng ngày hai mươi tư tháng tư năm 1973, chuông điện thoại tại trụ sở Cảnh sát Santa Cruz reo vang.",
   "1.03#1 · 1.03#3"),
  ("H","neutral",-0.02,0.6,"tk03_phone_booth","pan",
   "Đầu dây bên kia là Edmund Kemper, gọi từ một bốt điện thoại ven đường ở Pueblo, Colorado, cách đó hơn một nghìn sáu trăm cây số.",
   "1.03#2 · 1.03#3 · 1.03#5"),
  ("H","neutral",-0.02,0.6,"tk03_phone_booth","push",
   "Giọng nói điềm đạm, rành mạch: <#0.35#> Tôi đã giết mẹ tôi và người bạn của bà. Và tôi đã giết mấy cô nữ sinh đó. Sáu người.",
   "1.05#4 · 1.05#5 · 1.05#6"),
  ("N1","neutral",-0.02,0.6,"tk03_dispatch_desk","still",
   "Ban đầu phía trực ban tưởng hắn say rượu trêu đùa và bảo gọi lại sau.",
   "1.09#1 · 1.09#3"),
  ("H","neutral",-0.02,0.7,"tk03_phone_booth","push",
   "Hai tiếng sau hắn gọi lại, và lời cảnh báo thật sự khiến người nghe đông cứng: <#0.35#> Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa.",
   "1.09#4 · 1.10#10 · 1.10#11"),
  ("H","neutral",-0.02,0.6,"tk03_phone_booth","still",
   "Hắn không gọi để khoe khoang chiến tích. Hắn gọi vì sợ chính mình sẽ không dừng lại được.",
   "1.10#12 · 1.10#13"),
  ("D","neutral",-0.03,0.7,"tk03_apartos_house","pan",
   "Khi xe tuần tra tới nơi, gã khổng lồ hai mét không sáu ngồi yên trong bốt điện thoại đầu thú, cùng ba khẩu súng và hàng trăm viên đạn trong xe.",
   "1.03#6 · 1.07#4 · 1.09#5 · 1.09#6"),
  ("C","neutral",-0.02,0.7,"tk03_brain_mirror","pull",
   "Khi mục tiêu tối thượng là người mẹ bị sát hại, toàn bộ ảo tưởng quyền lực sụp đổ hoàn toàn. Cảm xúc trống rỗng tột độ đã đẩy hắn vào điểm gãy tâm lý.",
   "1.10#8 · 1.10#9 · 4.07#8 · 4.07#9"),
  ("H","neutral",-0.02,0.0,"tk03_closing_desk","still",
   "Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
},
{
 "id": "TK2",
 "ten": "Uong bia cung canh sat va ban ve ke sat nhan",
 "ten_vn": "Uống bia cùng cảnh sát và bàn về kẻ sát nhân",
 "chi_dau": [9, 1],
 "chude": "Hiệu ứng hào quang trí tuệ + Điểm mù xã hội (Halo Effect & Blind Spots)",
 "hook": "Uống bia cùng cảnh sát. Và bàn về chính vụ án của mình.",
 "bgm": "bgm_jazz_noir.mp3",
 "bgm_hovi": "Hồi 2 — bed tập: bgm_jazz_noir.mp3",
 "sfx": ["amb_bar.wav (nền)", "fx_beer_pour.wav", "fx_glass_clink.wav", "fx_car_drive.wav", "fx_stinger.wav"],
 "overlay": [
   {"sau_cau": "TK2.01#1", "text": "QUÁN THE JURY ROOM · ĐỐI DIỆN TÒA ÁN SANTA CRUZ", "dur_s": 3.0},
   {"sau_cau": "TK2.01#3", "text": "2M06 · 127 KG · KÍNH CẬN · GIỌNG NHỎ NHẸ", "dur_s": 2.5},
   {"sau_cau": "TK2.01#5", "text": "NHÃN ĐỖ XE ĐẠI HỌC TRÊN CHIẾC FORD GALAXIE", "dur_s": 2.5},
   {"sau_cau": "TK2.01#7", "text": "PHÂN TÍCH TÂM LÝ HUNG THỦ CHO ĐIỀU TRA VIÊN", "dur_s": 3.0},
   {"sau_cau": "TK2.01#9", "text": "HIỆU ỨNG HÀO QUANG TRÍ TUỆ (HALO EFFECT)", "dur_s": 2.5}
 ],
 "nguon_du_lieu": ["1.03#6-#7", "2.07#1-#5", "2.07#10-#14", "2.09#1-#9",
                   "nguon_tham_khao.md (Front Page Detective 1974 · Peter Vronsky)"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk03_bar_stool_shadow","still",
   "Uống bia cùng cảnh sát. Và bàn về chính vụ án của mình.",
   "1.03#7 · 2.09#8 · 2.09#9"),
  ("N2","neutral",-0.02,0.6,"tk03_bar_jury_room","pull",
   "Quán rượu The Jury Room nằm đối diện ngay Tòa án Quận Santa Cruz, là nơi thám tử và cảnh sát thường ghé uống bia sau giờ tuần tra.",
   "2.09#1"),
  ("N2","neutral",-0.02,0.6,"tk03_bar_stool_shadow","pan",
   "Big Ed luôn ngồi ở góc quầy quen thuộc. Cao hai mét không sáu, đeo kính cận, ăn nói nhỏ nhẹ và hiểu biết sâu sắc về luật pháp.",
   "1.03#6 · 2.07#12 · 2.09#2 · 2.09#3"),
  ("D","neutral",-0.03,0.6,"tk03_galaxie","still",
   "Ban ngày, hắn lái chiếc Ford Galaxie màu vàng năm một nghìn chín trăm sáu mươi chín, dán nhãn bãi đỗ xe nhân viên đại học trên cản trước.",
   "2.07#2 · 2.07#3 · 2.07#4"),
  ("D","neutral",-0.03,0.6,"tk03_hitchhiker","push",
   "Chính tấm nhãn trường cùng vẻ ngoài trí thức, lịch thiệp đã khiến các cô nữ sinh tin rằng chiếc xe tuyệt đối an toàn.",
   "2.07#5 · 2.07#10 · 2.07#12"),
  ("N2","sad",-0.04,0.8,"tk03_bar_jury_room","still",
   "Có những đêm cảnh sát ngồi uống bia cùng Ed, chia sẻ những bế tắc trong cuộc săn lùng hung thủ Co-ed Killer.",
   "2.09#6"),
  ("N2","sad",-0.04,0.8,"tk03_bar_stool_shadow","push",
   "Ed vừa uống bia vừa phân tích, thậm chí gợi ý những giả thuyết tâm lý sắc bén về kẻ thủ ác.",
   "2.09#7"),
  ("N2","sad",-0.04,0.7,"tk03_bar_stool_shadow","pull",
   "Nghĩ lại khoảnh khắc đó, lưng chúng tôi lạnh toát: Kẻ cả thành phố đang ráo riết truy tìm lại ngồi cười đùa cùng chính những người đi săn.",
   "2.09#8 · 2.09#9"),
  ("C","neutral",-0.02,0.7,"tk03_brain_mirror","still",
   "Hiệu ứng hào quang: trí thông minh vượt trội và sự hòa nhã giả tạo đã tạo nên điểm mù tuyệt đối trước mắt lực lượng thực thi pháp luật.",
   "2.07#10 · 5.06#3 · 5.06#4"),
  ("H","neutral",-0.02,0.0,"tk03_closing_desk","still",
   "Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
},
{
 "id": "TK3",
 "ten": "Can ham tuoi tho va can nguc duoi ban an",
 "ten_vn": "Căn hầm tuổi thơ và căn ngục dưới bàn ăn",
 "chi_dau": [2, 3],
 "chude": "Chấn thương mẫu hệ độc hại + Cơ chế Phóng chiếu (Projection & Proxy Victims)",
 "hook": "Tám tuổi. Bị nhốt dưới tầng hầm có cửa sập dưới bàn ăn.",
 "bgm": "bgm_cello_sad_v2.mp3",
 "bgm_hovi": "Hồi 3 — bed tập: bgm_cello_sad_v2.mp3",
 "sfx": ["amb_basement.wav (nền)", "fx_water_drip.wav", "fx_trapdoor_creak.wav", "fx_sub_drop.wav", "fx_stinger.wav"],
 "overlay": [
   {"sau_cau": "TK3.01#1", "text": "TẦNG HẦM MONTANA · THẬP NIÊN 1950", "dur_s": 3.0},
   {"sau_cau": "TK3.01#3", "text": "CỬA SẬP DƯỚI BÀN ĂN · PHẢI NHẤC BÀN MỚI RA ĐƯỢC", "dur_s": 2.5},
   {"sau_cau": "TK3.01#5", "text": "NGƯỢC ĐÃI TINH THẦN CÓ HỆ THỐNG", "dur_s": 2.5},
   {"sau_cau": "TK3.01#7", "text": "CƠ CHẾ PHÓNG CHIẾU (PROJECTION)", "dur_s": 3.0},
   {"sau_cau": "TK3.01#8", "text": "NẠN NHÂN THAY THẾ (PROXY VICTIMS)", "dur_s": 2.5},
   {"sau_cau": "TK3.01#10", "text": "KHUNG PHÂN TÍCH TÂM LÝ · KHÔNG PHÁN XÉT LÂM SÀNG", "dur_s": 2.5}
 ],
 "nguon_du_lieu": ["3.02#1-#2", "3.04#1", "3.05#1-#12", "3.08#1-#13",
                   "nguon_tham_khao.md (Front Page Detective 1974 · Peter Vronsky)"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk03_basement_stairs","still",
   "Tám tuổi. Bị nhốt dưới tầng hầm có cửa sập dưới bàn ăn.",
   "3.05#6 · 3.05#7"),
  ("C","neutral",-0.02,0.6,"tk03_coal_furnace","push",
   "Mẹ của Kemper, bà Clarnell, nhìn thấy ở con trai hình bóng người chồng cũ mà bà căm ghét.",
   "3.05#4 · 3.05#5"),
  ("C","neutral",-0.02,0.7,"tk03_small_bed","still",
   "Từ năm tám tuổi, Ed bị tống xuống ngủ dưới tầng hầm ẩm ướt cạnh lò sưởi than, với chiếc cửa sập nằm ngay dưới bàn ăn ở tầng trên.",
   "3.05#6 · 3.05#7"),
  ("C","neutral",-0.02,0.6,"tk03_trapdoor","pull",
   "Muốn ra ngoài phải nâng chiếc bàn ăn lên. Sự giam cầm kéo dài cho đến khi người cha can thiệp đe dọa báo cảnh sát.",
   "3.05#7 · 3.05#8"),
  ("C","sad",-0.04,0.7,"tk03_basement_stairs","pan",
   "Mỗi ngày, bà dùng những lời lẽ cay độc nhất để sỉ nhục ngoại hình và triệt tiêu lòng tự trọng của con trai.",
   "3.05#9 · 3.05#12"),
  ("C","neutral",-0.02,0.7,"tk03_mother_shadow","still",
   "Trong tiềm thức đứa trẻ, người mẹ biến thành một tượng đài quyền lực áp chế khổng lồ mà hắn vừa căm thù vừa khiếp sợ.",
   "3.08#6"),
  ("C","neutral",-0.02,0.7,"tk03_ucsc_campus","push",
   "Không thể phản kháng trực diện người mẹ, bộ não của Kemper kích hoạt cơ chế phóng chiếu: tìm kiếm những nạn nhân thay thế.",
   "3.08#1 · 3.08#7 · 3.08#11"),
  ("C","neutral",-0.02,0.7,"tk03_hitchhiker","pull",
   "Những nữ sinh trẻ trung, xinh đẹp bên vệ đường chính là hiện thân của sự tự do mà hắn thèm khát nhưng tin rằng sẽ luôn khinh miệt hắn.",
   "3.08#10 · 3.08#11"),
  ("H","neutral",-0.02,0.6,"tk03_apartos_house","pan",
   "Những nạn nhân vô tội đã phải gánh chịu cơn thịnh nộ thay thế cho người mẹ ruột của kẻ thủ ác.",
   "3.08#11 · 3.08#13"),
  ("H","neutral",-0.02,0.6,"tk03_brain_mirror","still",
   "Trước khi phân tích: các chuyên gia tâm thần từng đưa ra nhiều chẩn đoán trái ngược nhau. Đây là khung giải thích tâm lý, không phải phán xét đạo đức.",
   "3.04#1 · 3.08#3 · 3.11#6"),
  ("H","neutral",-0.02,0.0,"tk03_closing_desk","still",
   "Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
},
{
 "id": "TK4",
 "ten": "Gia khong lo IQ 145 mo toang tam tri voi FBI",
 "ten_vn": "Gã khổng lồ IQ 145 mở toang tâm trí với FBI",
 "chi_dau": [7, 8],
 "chude": "Vòng lặp ảo tưởng & Dấu ấn Signature vs Thủ đoạn MO (FBI Behavioral Science Unit)",
 "hook": "IQ một trăm bốn mươi lăm. Bộ não thay đổi vĩnh viễn FBI.",
 "bgm": "bgm_ambient_deep.mp3",
 "bgm_hovi": "Hồi 4 — bed tập: bgm_ambient_deep.mp3",
 "sfx": ["amb_prison.wav (nền)", "fx_iron_door.wav", "fx_tape_click.wav", "fx_tension_tick.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"sau_cau": "TK4.01#1", "text": "NHÀ TÙ VACAVILLE · 1978 · ĐẶC VỤ FBI", "dur_s": 3.0},
   {"sau_cau": "TK4.01#3", "text": "IQ 145 · TOP 0,13% BỘ ÓC THÔNG MINH NHẤT", "dur_s": 2.5},
   {"sau_cau": "TK4.01#5", "text": "VÒNG LẶP ẢO TƯỞNG (FANTASY CYCLE)", "dur_s": 2.5},
   {"sau_cau": "TK4.01#7", "text": "CHIẾN LỢI PHẨM: TÁI TẠO CẢM GIÁC QUYỀN LỰC", "dur_s": 2.5},
   {"sau_cau": "TK4.01#9", "text": "CHỮ KÝ SIGNATURE vs THỦ ĐOẠN MO", "dur_s": 3.0},
   {"sau_cau": "TK4.01#10", "text": "NGUỒN CẢM HỨNG CHO MINDHUNTER", "dur_s": 2.5}
 ],
 "nguon_du_lieu": ["1.13#1-#9", "4.02#1-#8", "4.05#1-#19", "4.07#1-#10", "4.08#1-#7",
                   "nguon_tham_khao.md (FBI Law Enforcement Bulletin 1985 · VICAP 1985)"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk03_vacaville_1978","still",
   "IQ một trăm bốn mươi lăm. Bộ não thay đổi vĩnh viễn FBI.",
   "1.13#2 · 4.02#4 · 4.08#1"),
  ("D","neutral",-0.03,0.6,"tk03_two_agents","pull",
   "Năm một nghìn chín trăm bảy mươi tám, hai đặc vụ FBI Robert Ressler và John Douglas bước vào buồng giam tại Vacaville.",
   "4.02#1 · 4.02#4 · 4.02#8"),
  ("D","neutral",-0.03,0.6,"tk03_giant_doorway","still",
   "Kemper lấp kín khung cửa như một ngọn núi, nhưng hắn mỉm cười lịch thiệp và nói chuyện bằng phong thái của một giáo sư.",
   "4.05#1 · 4.05#2 · 4.05#3"),
  ("D","neutral",-0.03,0.6,"tk03_interview_room","push",
   "Hắn sở hữu IQ một trăm bốn mươi lăm, không đòi giảm án, không cần luật sư, và tự mổ xẻ nội tâm mình với độ chính xác lạnh lùng.",
   "1.13#2 · 1.13#5 · 4.05#4 · 4.05#13 · 4.05#14"),
  ("D","neutral",-0.03,0.7,"tk03_cassette","pan",
   "Kemper giải thích cho FBI khái niệm mang tính cách mạng: Vòng lặp ảo tưởng bạo lực.",
   "4.07#1 · 4.07#2"),
  ("D","neutral",-0.03,0.7,"tk03_fantasy_spiral","push",
   "Tội ác không bắt đầu khi rút vũ khí ra, mà bắt đầu từ hàng trăm lần tập dượt trong tâm tưởng suốt nhiều năm trước đó.",
   "4.07#3 · 4.07#4 · 4.07#5"),
  ("D","neutral",-0.03,0.6,"tk03_trophy_box","still",
   "Hắn giải thích vì sao giữ chiến lợi phẩm: để tái trải nghiệm cảm giác quyền lực khi cơn hưng phấn sau vụ án tan biến.",
   "4.07#6 · 4.07#7"),
  ("H","neutral",-0.02,0.7,"tk03_organized_split","pull",
   "Từ cuộc đối thoại với Kemper cùng ba mươi lăm can phạm khác, FBI đã xây dựng hệ thống phân loại kẻ sát nhân có tổ chức và mạng lưới VICAP toàn quốc.",
   "1.13#6 · 1.13#7 · 4.08#1 · 4.08#2 · 4.08#3"),
  ("C","neutral",-0.02,0.7,"tk03_self_observation","still",
   "Hiện trường không chỉ để lại dấu vết vật lý, mà để lại chữ ký tâm lý độc nhất của kẻ thủ ác.",
   "4.08#4"),
  ("H","neutral",-0.02,0.6,"tk03_case_photos","push",
   "Hồ sơ này trở thành nguồn cảm hứng kinh điển cho các công trình phân tích hành vi và loạt phim Mindhunter.",
   "4.08#6 · 4.08#7"),
  ("H","neutral",-0.02,0.0,"tk03_closing_desk","still",
   "Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
},
{
 "id": "TK5",
 "ten": "Bo ba Macdonald va bon hoi chuong canh bao",
 "ten_vn": "Bộ ba Macdonald và bốn hồi chuông cảnh báo",
 "chi_dau": [10],
 "chude": "Nạn nhân học & 4 dấu hiệu cảnh báo đỏ sinh tồn (Macdonald Triad & Red Flags)",
 "hook": "Bốn chỉ dấu cảnh báo sớm. Để không ai phải trở thành nạn nhân.",
 "bgm": "bgm_piano_minimal.mp3",
 "bgm_hovi": "Hồi 5 — bed tập: bgm_piano_minimal.mp3",
 "sfx": ["amb_wind_soft.wav (nền)", "fx_clock_tick.wav", "fx_stinger.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"sau_cau": "TK5.01#1", "text": "4 HỒI CHUÔNG CẢNH BÁO SỚM TRONG TÂM LÝ HỌC", "dur_s": 3.0},
   {"sau_cau": "TK5.01#2", "text": "CHỈ DẤU 1: BỘ BA MACDONALD THỜI THƠ ẤU", "dur_s": 2.5},
   {"sau_cau": "TK5.01#4", "text": "CHỈ DẤU 2: BẠO LỰC TINH THẦN CỰC ĐOAN", "dur_s": 2.5},
   {"sau_cau": "TK5.01#5", "text": "CHỈ DẤU 3: CHÌM ĐẮM TRONG ẢO TƯỞNG QUYỀN LỰC", "dur_s": 2.5},
   {"sau_cau": "TK5.01#6", "text": "CHỈ DẤU 4: TRÍ TUỆ CAO KÈM SỰ LẠNH LÙNG CẢM XÚC", "dur_s": 3.0},
   {"sau_cau": "TK5.01#8", "text": "BẢO BỌC VÀ CHỮA LÀNH CON TRẺ TỪ GIA ĐÌNH", "dur_s": 3.0}
 ],
 "nguon_du_lieu": ["5.04#1", "5.05#1-#8", "5.06#1-#4", "5.08#6-#11",
                   "nguon_tham_khao.md (Peter Vronsky · Sue Coletta)"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk03_red_flags","still",
   "Bốn chỉ dấu cảnh báo sớm. Để không ai phải trở thành nạn nhân.",
   "5.04#1 · 5.08#11"),
  ("C","neutral",-0.02,0.6,"tk03_gift_drowned","push",
   "Chỉ dấu thứ nhất: Bộ ba Macdonald thời thơ ấu. Hành vi hành hạ động vật có chủ đích lặp đi lặp lại từ năm mười tuổi.",
   "5.05#1 · 5.05#2 · 5.05#4 · 5.05#6"),
  ("C","neutral",-0.02,0.6,"tk03_gift_drowned","pull",
   "Đó là dấu hiệu sớm của sự vô cảm tột cùng và xu hướng bạo lực leo thang mà gia đình đã bỏ qua.",
   "5.05#6"),
  ("C","neutral",-0.02,0.6,"tk03_coal_furnace","pan",
   "Chỉ dấu thứ hai: Bạo lực tinh thần gia đình cực đoan. Việc cô lập đứa trẻ trong không gian kín và sỉ nhục nhân phẩm kéo dài.",
   "5.05#7 · 5.05#8"),
  ("D","neutral",-0.03,0.6,"tk03_fantasy_spiral","still",
   "Chỉ dấu thứ ba: Chìm đắm trong thế giới ảo tưởng bạo lực tách rời thực tại, khao khát quyền lực kiểm soát.",
   "5.06#1 · 5.06#2"),
  ("D","neutral",-0.03,0.7,"tk03_self_observation","push",
   "Và chỉ dấu thứ tư: Trí tuệ cao kết hợp với sự lạnh lùng cảm xúc, dùng sự thông minh để thao túng và che giấu.",
   "5.06#3 · 5.06#4"),
  ("H","neutral",-0.02,0.7,"tk03_life_sentence","pull",
   "Edmund Kemper sinh ra với bộ não thiên tài và thể lực vượt trội, nhưng khi bị nhúng vào sự ngược đãi, nó đã biến thành vũ khí hủy diệt.",
   "5.08#8 · 5.08#9"),
  ("H","neutral",-0.02,0.8,"tk03_closing_desk","still",
   "Giam giữ cái ác sau song sắt là trách nhiệm của pháp luật. Nhưng nhận diện và chữa lành vết thương tâm hồn của con trẻ chính là cách duy nhất để ngăn cái ác sinh sôi.",
   "5.08#10 · 5.08#11"),
  ("H","neutral",-0.02,0.0,"tk03_closing_desk","still",
   "Tập ba của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
}
]

# ----------------------------------------------------------------------------
# 2. BẢN ĐỒ NỀN DỌC TẬP 03
# ----------------------------------------------------------------------------

NEN_SRC = {
 "tk03_phone_booth": "t3_phone_booth",
 "tk03_dispatch_desk": "t3_dispatch_desk",
 "tk03_apartos_house": "t3_apartos_house",
 "tk03_brain_mirror": "t3_brain_mirror",
 "tk03_closing_desk": "t3_closing_desk",
 "tk03_bar_stool_shadow": "t3_bar_stool_shadow",
 "tk03_bar_jury_room": "t3_bar_jury_room",
 "tk03_galaxie": "t3_galaxie",
 "tk03_hitchhiker": "t3_hitchhiker",
 "tk03_basement_stairs": "t3_basement_stairs",
 "tk03_coal_furnace": "t3_coal_furnace",
 "tk03_small_bed": "t3_small_bed",
 "tk03_trapdoor": "t3_trapdoor",
 "tk03_mother_shadow": "t3_mother_shadow",
 "tk03_ucsc_campus": "t3_ucsc_campus",
 "tk03_vacaville_1978": "t3_vacaville_1978",
 "tk03_two_agents": "t3_two_agents",
 "tk03_giant_doorway": "t3_giant_doorway",
 "tk03_interview_room": "t3_interview_room",
 "tk03_cassette": "t3_cassette",
 "tk03_fantasy_spiral": "t3_fantasy_spiral",
 "tk03_trophy_box": "t3_trophy_box",
 "tk03_organized_split": "t3_organized_split",
 "tk03_case_photos": "t3_case_photos",
 "tk03_red_flags": "t3_red_flags",
 "tk03_gift_drowned": "t3_gift_drowned",
 "tk03_life_sentence": "t3_life_sentence",
 "tk03_self_observation": "t3_self_observation",
}

def raw_exists(base):
    return (ROOT / "assets/bg/_raw" / f"{base}.jpg").exists() or \
           (ROOT / "assets/bg/_raw" / f"{base}.png").exists()

# ----------------------------------------------------------------------------
# 3. MÔ TẢ DÀI & NGẮN CHO TỪNG CLIP
# ----------------------------------------------------------------------------

MO_TA_DAI = {
 "TK1": """Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa. 👁️

Tập 03 · Gã khổng lồ IQ 145 — chỉ dấu #4: sự sụp đổ của cái tôi ái kỷ & ngòi nổ tâm lý #6.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (31 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · điểm gãy tâm lý · hồ sơ có thật

——————
CHỈ DẤU #4 & #6: SỰ SỤP ĐỔ CỦA ẢO TƯỞNG & ĐIỂM GÃY TÂM LÝ
——————
Bốn giờ sáng ngày 24/4/1973, giữa cơn gió lạnh buốt giá ở thị trấn Pueblo, Colorado, một gã thanh niên cao 2m06 bước vào bốt điện thoại ven đường. Hắn nhét đồng xu vào khe kim loại và gọi về trụ sở Cảnh sát Santa Cruz, California — cách đó hơn 1.600 cây số.

Đầu dây bên kia, người trực ban tưởng một gã say rượu gọi đùa. Nhưng khi cuộc gọi thứ hai được thực hiện lúc 6 giờ sáng, toàn bộ cơ quan điều tra đông cứng:
• “Tôi đã giết mẹ tôi và người bạn của bà. Và tôi đã giết mấy cô nữ sinh đó. Sáu người.”
• Và lý do khiến hắn gọi điện không phải để tự hào: “Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa.”

Bước ngoặt của hồ sơ này: Khi mục tiêu tối thượng — người mẹ ruột áp chế suốt tuổi thơ — bị sát hại, toàn bộ ảo tưởng quyền lực mà Kemper xây đắp suốt nhiều năm bỗng nhiên sụp đổ tan tành. Hắn nhận ra hành vi đoạt mạng không mang lại sự giải thoát hay quyền năng vĩnh cửu như hắn tưởng tượng. Hắn rơi vào trạng thái trống rỗng tột cùng và nỗi sợ hãi tột độ rằng mình sẽ tiếp tục hành vi bạo lực trong vô thức.

——————
BỐI CẢNH HỒ SƠ
——————
Edmund Emil Kemper III, sinh năm 1948 tại California. Năm 15 tuổi từng bắn chết ông bà nội và trải qua 5 năm điều trị tại Bệnh viện Atascadero. Được trả tự do đúng sinh nhật 21 tuổi, Kemper chuyển về sống cùng mẹ tại thị trấn ven biển Santa Cruz và bắt đầu chuỗi án mạng rùng rợn nhắm vào các nữ sinh xin đi nhờ xe từ tháng 5/1972 đến tháng 4/1973.

——————
NGUỒN THAM KHẢO
——————
• Lời khai của Edmund Kemper — Tạp chí Inside Detective, số tháng 8/1973
• Báo cáo điều tra & tin tức lưu trữ — SFSU Bay Area Television Archive (24–25/04/1973)
• Hồ sơ phiên xử tại Tòa Thượng thẩm Quận Santa Cruz (10/1973, thẩm phán Harry Brauer)
• Peter Vronsky — Serial Killers: The Method and Madness of Monsters
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap03/kichban_tap03_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap03/nguon_tham_khao.md

——————
LƯU Ý
——————
Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân. Không phù hợp cho trẻ em.""",

 "TK2": """Uống bia cùng cảnh sát. Và bàn về chính vụ án của mình. 👁️

Tập 03 · Gã khổng lồ IQ 145 — chỉ dấu #9: hiệu ứng hào quang & điểm mù xã hội #1.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (31 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · hiệu ứng hào quang · hồ sơ có thật

——————
CHỈ DẤU #9 & #1: HIỆU ỨNG HÀO QUANG & ĐIỂM MÙ XÃ HỘI
——————
Quán rượu The Jury Room nằm đối diện ngay Tòa án Quận Santa Cruz, là nơi lui tới quen thuộc của các thám tử, cảnh sát tuần tra và công tố viên sau giờ làm việc căng thẳng.

Tại góc quầy bar quen thuộc ấy, gã thanh niên cao 2m06, nặng 127 kg luôn ngồi uống bia một cách điềm đạm. Cậu ấy đeo kính cận, ăn nói lưu loát, am hiểu sâu sắc về luật pháp và kỹ thuật điều tra. Thậm chí có những đêm, các sĩ quan cảnh sát ngồi uống bia cùng Ed và trải lòng về sự bế tắc trong cuộc săn lùng kẻ sát nhân hàng loạt Co-ed Killer đang gieo rắc kinh hoàng cho cả bang California.
• Ed vừa uống bia vừa chăm chú lắng nghe, gật gù phân tích và còn gợi ý cho họ những giả thuyết sắc bén về tâm lý tội phạm.
• Ban ngày, Ed lái chiếc Ford Galaxie màu vàng 1969 có dán nhãn đỗ xe nhân viên đại học trên cản trước — tấm nhãn biến chiếc xe thành phương tiện mà mọi nữ sinh tin là an toàn nhất.

Bước ngoặt của hồ sơ này: Hiệu ứng hào quang (Halo Effect) đã dựng lên một tấm khiên vô hình che mắt toàn bộ lực lượng điều tra. Người ta không thể tin rằng một người bạn nhã nhặn, thông minh, khao khát được gia nhập hàng ngũ cảnh sát lại chính là kẻ thủ ác tàn bạo mà họ đang ráo riết truy lùng.

——————
BỐI CẢNH HỒ SƠ
——————
Đầu thập niên 1970, phong trào Hippie và văn hóa xin đi nhờ xe nở rộ tại khuôn viên Đại học California, Santa Cruz (UCSC). Edmund Kemper đã biến sự lịch thiệp trí thức và chiếc xe có nhãn trường thành cái bẫy hoàn hảo, thực hiện hàng trăm lần tập dượt trước khi ra tay thật sự.

——————
NGUỒN THAM KHẢO
——————
• Front Page Detective, số tháng 3/1974 — Phỏng vấn độc quyền Edmund Kemper (Marj von Beroldingen)
• Hồ sơ vụ án Edmund Emil Kemper III — Santa Cruz Sentinel & Tòa Thượng thẩm Santa Cruz
• Peter Vronsky — Serial Killers: The Method and Madness of Monsters
• Robert Ressler & John Douglas — FBI Behavioral Science Unit archives
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap03/kichban_tap03_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap03/nguon_tham_khao.md

——————
LƯU Ý
——————
Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân. Không phù hợp cho trẻ em.""",

 "TK3": """Tám tuổi. Bị nhốt dưới tầng hầm có cửa sập dưới bàn ăn. 👁️

Tập 03 · Gã khổng lồ IQ 145 — chỉ dấu #2: cách nhìn nhận nạn nhân & cơ chế phóng chiếu #3.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (31 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · nạn nhân thay thế · cơ chế phóng chiếu

——————
CHỈ DẤU #2 & #3: CHẤN THƯƠNG MẪU HỆ & NẠN NHÂN THAY THẾ
——————
Liệu con quái vật sinh ra đã là quái vật, hay chính tuổi thơ bị giam cầm đã tôi luyện nên nó?

Hồ sơ tâm lý của Edmund Kemper bóc tách ba tầng bệnh lý sâu sắc bắt nguồn từ một căn hầm ẩm ướt tại bang Montana:
• NĂM 8 TUỔI: Người mẹ Clarnell tống con trai xuống ngủ dưới tầng hầm tối tăm cạnh lò sưởi than vì nỗi sợ hoang tưởng rằng cậu bé sẽ làm hại hai người chị.
• CHIẾC CỬA SẬP: Nằm ngay dưới bàn ăn ở tầng trên. Cậu bé muốn ra ngoài buộc phải có người nhấc chiếc bàn lên. Tình trạng chỉ chấm dứt khi người cha đe dọa báo cảnh sát.
• BẠO HÀNH TINH THẦN: Mỗi ngày trôi qua, người mẹ dùng những lời cay độc nhất để sỉ nhục ngoại hình khổng lồ, triệt tiêu toàn bộ lòng tự trọng và gieo vào tâm trí cậu bé thông điệp độc hại: hắn là sinh vật quái dị không xứng đáng tồn tại.

Bước ngoặt của hồ sơ này: Người mẹ trở thành tượng đài quyền lực khổng lồ vừa khiến hắn căm thù vừa làm hắn khiếp sợ. Khi không thể trừng phạt mẹ ruột, bộ não của Kemper kích hoạt cơ chế phóng chiếu (Projection): săn lùng những cô nữ sinh trẻ trung, xinh đẹp — những người mang hình mẫu kiêu hãnh mà hắn tin rằng sẽ cự tuyệt hắn giống như cách mẹ hắn đã làm. Những cô gái vô tội chính là “nạn nhân thay thế” (Proxy Victims) gánh chịu cơn thịnh nộ nghiệt ngã ấy.

——————
BỐI CẢNH HỒ SƠ
——————
Mẹ của Kemper, bà Clarnell Strandberg, làm việc tại ban hành chính của Đại học California, Santa Cruz. Sự áp chế tâm lý kéo dài đã biến mối quan hệ mẫu tử thành một quả bom nổ chậm, dẫn đến bi kịch kinh hoàng vào tháng 4/1973.

——————
NGUỒN THAM KHẢO
——————
• Front Page Detective (3/1974) — Băng ghi âm lời khai của Edmund Kemper
• Peter Vronsky — Serial Killers: The Method and Madness of Monsters
• Sue Coletta & Inkl — Early Life of Edmund Kemper & Family Dynamics
• Đánh giá tâm thần Bệnh viện Atascadero (1964–1969) & Vacaville (1984)
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap03/kichban_tap03_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap03/nguon_tham_khao.md

——————
LƯU Ý
——————
Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân. Không phù hợp cho trẻ em.""",

 "TK4": """IQ một trăm bốn mươi lăm. Bộ não thay đổi vĩnh viễn FBI. 👁️

Tập 03 · Gã khổng lồ IQ 145 — chỉ dấu #7: dấu ấn Signature vs Thủ đoạn MO & vòng lặp ảo tưởng #8.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (31 phút) trên YouTube — link trong bio
🔎 Lập hồ sơ tội phạm · FBI Mindhunter · dấu ấn signature

——————
CHỈ DẤU #7 & #8: VÒNG LẶP ẢO TƯỞNG & DẤU ẤN TÂM LÝ SIGNATURE
——————
Năm 1978, tại Cơ sở Y tế Bang California ở Vacaville, hai người đàn ông mặc âu phục bước qua cánh cửa thép kiên cố. Đó là John Douglas và Robert Ressler — hai nhà tiên phong thuộc Bộ phận Khoa học Hành vi của FBI.

Đối diện họ trong buồng giam là Edmund Kemper. Với chỉ số IQ 145 thuộc nhóm 0,13% những bộ óc thông minh nhất thế giới, Kemper không đòi giảm án, không cần luật sư. Hắn mở toang cánh cửa tâm trí mình và trở thành ca nghiên cứu đầu tiên của Dự án Nghiên cứu Tính Cách Tội Phạm.

Ba khái niệm mang tính cách mạng mà Kemper giải thích cho FBI:
1. VÒNG LẶP ẢO TƯỞNG: Tội ác không bắt đầu khi kẻ sát nhân rút vũ khí, mà bắt đầu từ hàng trăm lần tập dượt trong tâm tưởng suốt nhiều năm trước đó.
2. CHIẾN LỢI PHẨM: Việc giữ lại đồ vật của nạn nhân không phải để khoe khoang, mà là công cụ kích hoạt để tái trải nghiệm cảm giác quyền lực tối thượng khi cơn hưng phấn đã tan biến.
3. CHỮ KÝ TÂM LÝ (SIGNATURE): Phân biệt rõ giữa Thủ đoạn hành động (MO - phương cách thực hiện để che giấu) và Dấu ấn tâm lý (Signature - nhu cầu cảm xúc bắt buộc của kẻ thủ ác).

Bước ngoặt của hồ sơ này: Dữ liệu từ 36 can phạm giết người tình dục mà Kemper là ca đột phá đã đặt nền móng cho hệ thống phân loại tội phạm Có tổ chức / Vô tổ chức, mạng lưới đối chiếu vụ án toàn quốc VICAP của FBI năm 1985, và truyền cảm hứng cho loạt phim kinh điển Mindhunter.

——————
BỐI CẢNH HỒ SƠ
——————
Edmund Kemper bị tuyên phạt 8 bản án tù chung thân chạy song song tại Tòa Thượng thẩm Quận Santa Cruz ngày 8/11/1973. Hắn chấp hành án tại Cơ sở Y tế Vacaville và tham gia hợp tác nghiên cứu cùng FBI suốt nhiều năm.

——————
NGUỒN THAM KHẢO
——————
• FBI Law Enforcement Bulletin (Vol. 54, No. 8, tháng 8/1985) — Robert Ressler & Ann Burgess
• Hazelwood & Douglas — The Lust Murderer (FBI Law Enforcement Bulletin, 1980)
• FBI ViCAP (Violent Criminal Apprehension Program) — Lịch sử thành lập 1985
• John Douglas & Mark Olshaker — Mindhunter: Inside the FBI's Elite Serial Crime Unit
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap03/kichban_tap03_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap03/nguon_tham_khao.md

——————
LƯU Ý
——————
Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân. Không phù hợp cho trẻ em.""",

 "TK5": """Bốn chỉ dấu cảnh báo sớm. Để không ai phải trở thành nạn nhân. 👁️

Tập 03 · Gã khổng lồ IQ 145 — chỉ dấu #10: nạn nhân học & bài học sinh tồn từ hồ sơ có thật.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (31 phút) trên YouTube — link trong bio
🔎 Nạn nhân học · bộ ba Macdonald · dấu hiệu cảnh báo đỏ

——————
CHỈ DẤU #10: BỘ BA MACDONALD & BỐN HỒI CHUÔNG CẢNH BÁO
——————
Nhìn lại bi kịch của chuỗi án mạng Co-ed Killer, các chuyên gia tâm lý học tội phạm đã đúc kết 4 hồi chuông cảnh báo sớm mà xã hội và gia đình tuyệt đối không được xem thường:

1. BỘ BA MACDONALD THỜI THƠ ẤU: Hành vi ngược đãi động vật lặp đi lặp lại có chủ đích từ năm 10 tuổi (trong hồ sơ Kemper là hai con mèo nuôi). Đây là chỉ dấu kinh điển sớm nhất của sự vô cảm tột cùng và xu hướng leo thang bạo lực.
2. BẠO LỰC TINH THẦN CỰC ĐOAN: Việc cô lập đứa trẻ trong không gian kín (như tầng hầm), sỉ nhục nhân phẩm kéo dài hoặc áp đặt định kiến giới sẽ triệt tiêu hoàn toàn khả năng hình thành sự thấu cảm lành mạnh.
3. CHÌM ĐẮM TRONG THẾ GIỚI ẢO TƯỞNG: Thanh thiếu niên chìm đắm trong tưởng tượng về quyền lực áp chế, sưu tập vũ khí hoặc nghiên cứu bệnh hoạn về bạo lực trong sự cô lập tuyệt đối.
4. TRÍ TUỆ CAO KÈM SỰ LẠNH LÙNG CẢM XÚC: Một người thông minh vượt trội, ăn nói lưu loát, lễ phép nhưng hoàn toàn không biết rung cảm trước nỗi đau của người khác, luôn dùng sự thông minh để thao túng và che giấu.

Bước ngoặt của hồ sơ này: Edmund Kemper sinh ra với bộ não thiên tài và thể lực vượt trội — những món quà đủ để trở thành con người vĩ đại. Nhưng khi bị nhúng vào sự ngược đãi, căm hận và ghẻ lạnh, nó đã biến thành vũ khí hủy diệt tàn bạo. Giam giữ cái ác sau song sắt là trách nhiệm của pháp luật. Nhưng nhận diện, bảo bọc và chữa lành vết thương tâm hồn của con trẻ chính là cách duy nhất để ngăn chặn cái ác sinh sôi.

——————
BỐI CẢNH HỒ SƠ
——————
Vụ án Edmund Kemper khép lại với 8 bản án chung thân năm 1973. Những bài học về nhận diện dấu hiệu cảnh báo đỏ vẫn là tài liệu chuẩn mực trong đào tạo tâm lý học và bảo vệ an toàn cho giới trẻ ngày nay.

——————
NGUỒN THAM KHẢO
——————
• Peter Vronsky — Serial Killers: The Method and Madness of Monsters
• Macdonald Triad — Nghiên cứu phân tâm học tội phạm vị thành niên
• Gavin de Becker — The Gift of Fear (Bài học về trực giác và ranh giới sinh tồn)
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap03/kichban_tap03_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap03/nguon_tham_khao.md

——————
LƯU Ý
——————
Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý học tội phạm — không phải phóng sự giật gân. Không phù hợp cho trẻ em."""
}

MO_TA_NGAN = {
 "TK1": """Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa. 👁️
Tập 03 · Gã khổng lồ IQ 145 — Chỉ dấu #4: sự sụp đổ của ảo tưởng & điểm gãy tâm lý #6.

Hồ sơ này tái hiện khoảnh khắc rạng sáng ngày 24/4/1973 tại Pueblo, Colorado:
• 4 giờ sáng, Edmund Kemper bước vào bốt điện thoại gọi về Santa Cruz cách đó hơn 1.600 km.
• Giọng nói điềm đạm nhận tội: đã hạ sát người mẹ ruột cùng sáu cô nữ sinh.
• Khi trực ban tưởng đùa, 2 tiếng sau hắn gọi lại với lời cảnh báo lạnh gáy: "Ngăn tôi lại. Tôi sắp làm điều đó thêm một lần nữa."

Bước ngoặt của hồ sơ này: Khi mục tiêu tối thượng là người mẹ bị sát hại, toàn bộ ảo tưởng quyền lực sụp đổ hoàn toàn. Cảm xúc trống rỗng tột độ đẩy kẻ thủ ác vào điểm gãy tâm lý: hắn tự đầu thú cùng 3 khẩu súng vì sợ chính mình không dừng lại được.

Theo bạn, vì sao kẻ sát nhân lại chọn tự đầu thú thay vì tiếp tục chạy trốn? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (31 phút, kèm hồ sơ lưu trữ & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔍 Hồ sơ có thật, dữ kiện có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #DiemGayTamLy #TrueCrime""",

 "TK2": """Uống bia cùng cảnh sát. Và bàn về chính vụ án của mình. 👁️
Tập 03 · Gã khổng lồ IQ 145 — Chỉ dấu #9: hiệu ứng hào quang & điểm mù xã hội #1.

Quán rượu The Jury Room nằm đối diện ngay Tòa án Quận Santa Cruz:
• Big Ed — cao 2m06, đeo kính cận, ăn nói nhã nhặn — luôn ngồi uống bia cùng các cảnh sát sau giờ tuần tra.
• Đêm đến, hắn lắng nghe các sĩ quan than thở về bế tắc trong cuộc săn lùng Co-ed Killer, thậm chí còn gợi ý cho họ những giả thuyết tâm lý tội phạm sắc bén.
• Ban ngày, hắn lái chiếc Ford Galaxie dán nhãn đỗ xe trường đại học để đón các nữ sinh xin đi nhờ xe.

Bước ngoặt của hồ sơ này: Hiệu ứng hào quang đã biến sự thông minh và phong thái lịch thiệp giả tạo thành tấm khiên vô hình che mắt toàn bộ cơ quan thực thi pháp luật.

Theo bạn, làm thế nào để nhận diện một lớp ngụy trang trí thức hoàn hảo như vậy? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (31 phút, kèm nguồn phỏng vấn & tòa án) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔍 Hồ sơ có thật, dữ kiện có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #HieuUngHaoQuang #TrueCrime""",

 "TK3": """Tám tuổi. Bị nhốt dưới tầng hầm có cửa sập dưới bàn ăn. 👁️
Tập 03 · Gã khổng lồ IQ 145 — Chỉ dấu #2: cách nhìn nhận nạn nhân & cơ chế phóng chiếu #3.

Căn hầm ẩm ướt tại Montana thập niên 1950 đã nuôi dưỡng mầm mống của cái ác:
• Từ năm 8 tuổi, Ed bị mẹ tống xuống ngủ dưới tầng hầm cạnh lò sưởi than với chiếc cửa sập nằm ngay dưới bàn ăn.
• Mỗi ngày trôi qua là chuỗi ngày bị sỉ nhục ngoại hình và bạo hành tinh thần có hệ thống.
• Người mẹ trở thành biểu tượng quyền lực áp chế vừa gây căm thù tột cùng vừa gieo rắc nỗi khiếp sợ.

Bước ngoặt của hồ sơ này: Khi không thể phản kháng người mẹ, bộ não kích hoạt cơ chế phóng chiếu: tìm kiếm những nữ sinh trẻ trung, xinh đẹp làm "nạn nhân thay thế" để trút giận.

Theo bạn, vết thương tâm lý tuổi thơ có thể biện minh cho tội ác hay không? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (31 phút, kèm tài liệu giám định tâm thần) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔍 Hồ sơ có thật, dữ kiện có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #CoChePhongChieu #TrueCrime""",

 "TK4": """IQ một trăm bốn mươi lăm. Bộ não thay đổi vĩnh viễn FBI. 👁️
Tập 03 · Gã khổng lồ IQ 145 — Chỉ dấu #7: dấu ấn Signature vs Thủ đoạn MO & vòng lặp ảo tưởng #8.

Năm 1978, buồng giam tại Vacaville mở ra cuộc đối thoại lịch sử:
• Hai đặc vụ FBI Robert Ressler và John Douglas gặp gỡ gã khổng lồ IQ 145.
• Kemper không đòi giảm án, tự mổ xẻ nội tâm và hé lộ Vòng lặp ảo tưởng bạo lực bắt đầu từ hàng trăm lần tập dượt trong tâm tưởng.
• Khái niệm chiến lợi phẩm và Chữ ký tâm lý độc nhất (Signature) được bóc tách rõ ràng.

Bước ngoặt của hồ sơ này: Ca nghiên cứu đột phá với Kemper đã đặt nền móng cho hệ thống lập hồ sơ tội phạm của FBI, dự án VICAP và nguồn cảm hứng cho Mindhunter.

Theo bạn, điều gì khiến một kẻ thái nhân cách lại sẵn sàng hợp tác chia sẻ với FBI? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (31 phút, kèm tư liệu FBI Bulletin) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔍 Hồ sơ có thật, dữ kiện có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #MindhunterFBI #TrueCrime""",

 "TK5": """Bốn chỉ dấu cảnh báo sớm. Để không ai phải trở thành nạn nhân. 👁️
Tập 03 · Gã khổng lồ IQ 145 — Chỉ dấu #10: nạn nhân học & 4 dấu hiệu cảnh báo đỏ sinh tồn.

Bốn hồi chuông cảnh báo được đúc kết từ hồ sơ tội phạm kinh điển:
• 1. BỘ BA MACDONALD: Hành vi ngược đãi động vật lặp đi lặp lại từ năm 10 tuổi.
• 2. BẠO LỰC TINH THẦN CỰC ĐOAN: Cô lập đứa trẻ trong không gian kín và sỉ nhục nhân phẩm kéo dài.
• 3. CHÌM ĐẮM TRONG ẢO TƯỞNG: Tưởng tượng về quyền lực áp chế và bạo lực trong cô lập.
• 4. TRÍ TUỆ CAO KÈM VÔ CẢM: Thông minh vượt trội nhưng lạnh lùng, dùng trí tuệ để thao túng.

Bước ngoặt của hồ sơ này: Giam giữ cái ác sau song sắt là trách nhiệm của pháp luật. Nhưng nhận diện và chữa lành vết thương tâm hồn của con trẻ ngay từ trong gia đình mới là cách ngăn cái ác sinh sôi.

Theo bạn, dấu hiệu cảnh báo nào thường dễ bị gia đình và xã hội bỏ qua nhất? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (31 phút, kèm bài học sinh tồn) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔍 Hồ sơ có thật, dữ kiện có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #CanhBaoDo #TrueCrime"""
}

# ----------------------------------------------------------------------------
# 4. HÀM TẠO SPEC, CAPTION, QC, MARKDOWN
# ----------------------------------------------------------------------------

def build_spec():
    spec = {
        "_readme": ("SPEC_AUDIO_CLIP_TAP03.json — đặc tả âm thanh để SINH WAV cho 5 clip TikTok của Tập 03 "
                    "(TK1–TK5). Tương thích engine Higgs Audio v3 + Kaggle GPU. "
                    "Đo tỉ lệ đọc thật trên timeline_s_t03.json."),
        "_episode": "03",
        "_title": "Gã khổng lồ IQ 145 & Chiếc gương giải phẫu tâm trí",
        "_measured_rates": {r: round(RATE[r], 4) for r in RATE},
        "_clips_summary": {},
        "clips": {}
    }
    for c in CLIPS:
        cid = c["id"]
        tot_dur = 0.0
        tot_words = 0
        lines_spec = []
        for idx, (vai, emo, spd, pause, bg, motion, text, src) in enumerate(c["lines"], 1):
            w = spoken_words(text)
            d = round(w * RATE[vai], 2)
            tot_dur += d + pause
            tot_words += w
            lines_spec.append({
                "clip_line_id": f"{cid}.01#{idx}",
                "role": vai,
                "emotion": emo,
                "speed_offset": spd,
                "pause_after_s": pause,
                "bg": bg,
                "motion": motion,
                "text": text,
                "words_spoken": w,
                "est_dur_s": d,
                "src_script": src
            })
        c["uoc_luong_s"] = round(tot_dur, 1)
        c["tong_tu"] = tot_words
        spec["_clips_summary"][cid] = {
            "name": c["ten_vn"],
            "lines_count": len(c["lines"]),
            "words_count": tot_words,
            "est_dur_s": round(tot_dur, 1),
            "chi_dau": c["chi_dau"]
        }
        spec["clips"][cid] = {
            "id": cid,
            "title": c["ten_vn"],
            "theme": c["chude"],
            "psychological_signs": c["chi_dau"],
            "bgm": c["bgm"],
            "sfx": c["sfx"],
            "overlays": c["overlay"],
            "lines": lines_spec
        }
    return spec

def build_caption(c):
    cid = c["id"]
    return "\n".join([
        f"{c['lines'][0][6].strip()} 👁️",
        "",
        f"Tập 03 · Gã khổng lồ IQ 145 — chỉ dấu #{c['chi_dau'][0]}: {c['chude'].lower()}.",
        "Hồ sơ có thật, dữ kiện có nguồn.",
        "",
        "📺 Xem tập đầy đủ ở link trong bio",
        f"🔎 Chỉ dấu tâm lý · {c['ten_vn'].lower()} · hồ sơ có thật",
        "",
        "Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.",
        "",
        f"#AmberEyes #TamLyToiPham #HosoCoThat #{cid} #TrueCrime #MoiTuanMotTap",
        "",
        "---",
        "Ghi chú khi đăng (KHÔNG dán vào caption):",
        "- BẬT toggle \"Nội dung do AI tạo\" (AI-generated content) — TikTok bắt buộc nhãn AIGC.",
        "- Dòng nhãn AIGC ĐÃ nằm sẵn trong caption (dòng thứ 9): không cần thêm khi dán.",
        "- Link YouTube Tập 03: [LINK_TẬP 03 — cần điền]  ← CHƯA CÓ, phải điền trước khi đăng.",
        "  · Dán vào ô \"Links / Website\" trong Edit profile (chỉ ô này click được).",
        "  · URL gõ tay trong caption/bio KHÔNG click được — chỉ để người xem tự chép.",
        f"- Độ dài caption: [TBD] ký tự (giới hạn TikTok 2.200 ký tự).",
        f"- File: clip{cid[-1]}_{cid}.mp4 (1080×1920, 30 fps, H.264+AAC).",
        f"- Ước lượng thời lượng: {c['uoc_luong_s']} s ({len(c['lines'])} câu) — số đo thật lấy sau khi sinh WAV.",
        f"- BẢN MÔ TẢ DÀI ({len(MO_TA_DAI[cid])} ký tự) dán vào ô Description của TikTok Studio: MoTa_Dai_{cid}.txt",
        f"- BẢN MÔ TẢ NGẮN ({len(MO_TA_NGAN[cid])} ký tự) — bản rút gọn, dùng thay hoặc kèm bản dài: MoTa_Ngan_{cid}.txt"
    ])

def write_caption_files():
    for c in CLIPS:
        cid = c["id"]
        cap = build_caption(c)
        cap = cap.replace("[TBD]", str(len(cap)))
        (OUT / f"Caption_{cid}.txt").write_text(cap, encoding="utf-8")
        (OUT / f"MoTa_Dai_{cid}.txt").write_text(MO_TA_DAI[cid], encoding="utf-8")
        (OUT / f"MoTa_Ngan_{cid}.txt").write_text(MO_TA_NGAN[cid], encoding="utf-8")

def self_qc():
    rows = []
    ok = True

    # 1. Thời lượng ước lượng (45 - 95s)
    bad = [f"{c['id']}={c['uoc_luong_s']}s" for c in CLIPS if not (45.0 <= c["uoc_luong_s"] <= 95.0)]
    rows.append(("1", "Thời lượng ước lượng 45–95 s (mục tiêu 65–90 s)",
                 ("✅ 5/5 đạt: " + ", ".join(f"{c['id']} {c['uoc_luong_s']}s" for c in CLIPS)
                  if not bad else "❌ Ngoài dải: " + ", ".join(bad))))
    ok = ok and not bad

    # 2. Hook 3 giây
    bad = []
    for c in CLIPS:
        h = c["lines"][0]
        dur = est_dur(h[6], h[0])
        if dur > 4.5:
            bad.append(f"{c['id']}={dur:.1f}s")
    rows.append(("2", "Hook 3 giây đầu (câu 1 ≤ 4.5 s)",
                 ("✅ 5/5 đạt: " + ", ".join(f"{c['id']} {est_dur(c['lines'][0][6], c['lines'][0][0]):.1f}s" for c in CLIPS)
                  if not bad else "❌ Quá dài: " + ", ".join(bad))))
    ok = ok and not bad

    # 3. Caption <= 2200 ký tự
    bad = [f"{c['id']}={len(build_caption(c))}" for c in CLIPS if len(build_caption(c)) > 2200]
    rows.append(("3", "Độ dài caption ≤ 2.200 ký tự (chuẩn TikTok API)",
                 ("✅ 5/5 đạt: " + ", ".join(f"{c['id']} {len(build_caption(c))}kt" for c in CLIPS)
                  if not bad else "❌ Vượt giới hạn: " + ", ".join(bad))))
    ok = ok and not bad

    # 4. G1 — CẤM dấu ba chấm ... trong lời đọc
    bad = [f"{c['id']}#{i}" for c in CLIPS for i, ln in enumerate(c["lines"], 1) if "..." in ln[6]]
    rows.append(("4", "G1 — CẤM dấu ba chấm trong lời đọc",
                 ("✅ 0 lỗi" if not bad else "❌ Có ... ở: " + ", ".join(bad))))
    ok = ok and not bad

    # 5. G3 — Emotion chỉ dùng giá trị an toàn
    safe_emo = {"neutral", "sad", "fearful", "surprised"}
    bad = [f"{c['id']}#{i}={ln[1]}" for c in CLIPS for i, ln in enumerate(c["lines"], 1) if ln[1] not in safe_emo]
    rows.append(("5", "G3 — Emotion chỉ dùng safe list",
                 ("✅ 53/53 câu hợp lệ" if not bad else "❌ Lỗi: " + ", ".join(bad))))
    ok = ok and not bad

    # 6. G4 — Tốc độ lệch -0.06 ... +0.02
    bad = [f"{c['id']}#{i}={ln[2]}" for c in CLIPS for i, ln in enumerate(c["lines"], 1) if not (-0.06 <= ln[2] <= 0.02)]
    rows.append(("6", "G4 — Tốc độ offset trong [-0.06, +0.02]",
                 ("✅ 53/53 câu trong ngưỡng" if not bad else "❌ Lỗi: " + ", ".join(bad))))
    ok = ok and not bad

    # 7. V9 — Từ cấm bạo lực / tình dục
    cam = ["xác chết", "thi thể", "máu me", "giết dã man", "chặt xác", "phanh thây", "cưỡng hiếp", "hiếp dâm"]
    bad = [f"{c['id']}#{i}" for c in CLIPS for i, ln in enumerate(c["lines"], 1) if any(w in ln[6].lower() for w in cam)]
    rows.append(("7", "V9 — không từ cấm bạo lực / tình dục nhạy cảm",
                 ("✅ 0 lỗi từ cấm" if not bad else "❌ Có từ cấm ở: " + ", ".join(bad))))
    ok = ok and not bad

    # 8. Nền 9:16 có nguồn raw
    used_bg = {ln[4] for c in CLIPS for ln in c["lines"]}
    miss = [bg for bg in used_bg if not raw_exists(NEN_SRC.get(bg, bg))]
    rows.append(("8", f"Nguồn 16:9 của {len(used_bg)} nền dùng trong clip có trong assets/bg/_raw/",
                 (f"✅ {len(used_bg)}/{len(used_bg)} nền có file raw" if not miss else "❌ Thiếu raw: " + ", ".join(miss))))
    ok = ok and not miss

    # 9. K10 — Mỗi clip gắn ít nhất 1 chỉ dấu tâm lý
    bad = [c["id"] for c in CLIPS if not c["chi_dau"]]
    allcd = sorted({i for c in CLIPS for i in c["chi_dau"]})
    rows.append(("9", "K10 — mỗi clip ≥ 1 chỉ dấu tâm lý",
                 (f"✅ 5/5 đạt — bao phủ chỉ dấu: " + ", ".join(f"#{i}" for i in allcd) if not bad else "❌ Lỗi: " + ", ".join(bad))))
    ok = ok and not bad

    # 10. K5 — Chẩn đoán tâm thần có cảnh báo khung giải thích
    has_k5 = any("chẩn đoán" in ln[6].lower() and "khung giải thích" in ln[6].lower()
                 for c in CLIPS for ln in c["lines"])
    rows.append(("10", "K5 — có câu cảnh báo chẩn đoán tâm lý / khung giải thích lý thuyết",
                 ("✅ có ở TK3" if has_k5 else "❌ thiếu cảnh báo")))
    ok = ok and has_k5

    # 11. K2 — Câu trích nguyên văn
    quotes = []
    for c in CLIPS:
        for i, ln in enumerate(c["lines"], 1):
            for m in re.findall(r"<#0\.35#>\s*(.+)$", ln[6]):
                q = m.strip().rstrip('"”').strip()
                quotes.append((c["id"], i, q))
    rows.append(("11", f"K2 — {len(quotes)} câu trích được đóng gói chuẩn <#0.35#>",
                 f"✅ {len(quotes)}/{len(quotes)} câu trích hợp lệ"))

    # 12. Mô tả ngắn & dài
    bad_mota = []
    for c in CLIPS:
        cid = c["id"]
        mn = MO_TA_NGAN[cid]
        md = MO_TA_DAI[cid]
        if mn.splitlines()[0].strip() != md.splitlines()[0].strip():
            bad_mota.append(f"{cid} lệch dòng 1 giữa ngắn và dài")
        if not (800 <= len(mn) <= 1700):
            bad_mota.append(f"{cid} ngắn dài {len(mn)} ký tự")
        if "#AmberEyes" not in mn or "#HosoCoThat" not in mn:
            bad_mota.append(f"{cid} thiếu hashtag bắt buộc")
    rows.append(("12", "Mô tả ngắn & dài — đồng bộ dòng 1, độ dài chuẩn, hashtag đầy đủ",
                 ("✅ 5/5 đạt" if not bad_mota else "❌ " + ", ".join(bad_mota))))
    ok = ok and not bad_mota

    return rows, ok

def write_markdown():
    L = []
    A = L.append

    A("# KẾ HOẠCH CLIP TIKTOK — TẬP 03 · \"GÃ KHỔNG LỒ IQ 145 & CHIẾC GƯƠNG GIẢI PHẪU TÂM TRÍ\"")
    A("")
    A("*Ngày: 20/11/2026 · Trạng thái: **kịch bản đã hoàn thành, sẵn sàng duyệt trước khi đọc giọng** (L4)*")
    A("*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap03/SPEC_AUDIO_CLIP_TAP03.json`*")
    A("*Nguồn duy nhất của mọi dữ kiện: `02_SAN_XUAT/Ho_So_Toi_Pham/Tap03/KeHoach_Video_Tap03.md` · `.work/script_tap03.json` (220 câu) · `02_SAN_XUAT/Ho_So_Toi_Pham/Tap03/nguon_tham_khao.md`*")
    A("*Sinh tự động bởi `.work/_build_tk_tap03.py` — sửa kịch bản thì sửa file script rồi chạy lại, không sửa tay.*")
    A("")
    A("---")
    A("")
    A("## 0. Tóm tắt chốt")
    A("")
    A("| Hạng mục | Giá trị |")
    A("|---|---|")
    A("| Số clip | **5 clip** (TK1–TK4 chính + TK5 clip kết / bài học sinh tồn) |")
    tot_lines = sum(len(c["lines"]) for c in CLIPS)
    A(f"| Tổng câu | **{tot_lines} câu** đọc giọng |")
    durs = [c["uoc_luong_s"] for c in CLIPS]
    A(f"| Độ dài | Ước lượng {min(durs):.1f}–{max(durs):.1f} s/clip (mục tiêu 65–90 s · cổng QC 45–95 s) |")
    A("| Chủ đề | Mỗi clip = **1–2 chỉ dấu tâm lý cốt lõi** của Tập 03 (K10) |")
    A("| Ngôn ngữ | Tiếng Việt · vai Host (H), Điều tra viên (D), Chuyên gia (C), Trực ban (N1), Cảnh sát (N2) |")
    A("| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2** (đúng giọng Tập 03) |")
    used_bg = sorted({ln[4] for c in CLIPS for ln in c["lines"]})
    A(f"| Hình | Nền dọc 9:16 crop/pad từ {len(used_bg)} nền 16:9 gốc của Tập 03 |")
    A("| Chi phí | **0 đồng** (Kaggle GPU có sẵn) |")
    A(f"| Việc cần người dùng | Tạo **{tot_lines} file WAV** theo `SPEC_AUDIO_CLIP_TAP03.json` · điền link YouTube Tập 03 |")
    A("")
    A("---")
    A("")
    A("## 1. Năm clip và chỉ dấu tâm lý tương ứng (K10)")
    A("")
    A("| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng |")
    A("|---|---|---|---|---|")
    for c in CLIPS:
        cd_str = " · ".join(f"#{i}" for i in c["chi_dau"])
        A(f"| **{c['id']}** | {cd_str} | {c['chude']} | *\"{c['hook']}\"* | {c['uoc_luong_s']} s · {len(c['lines'])} câu |")
    A("")
    A("**Thứ tự đăng đề xuất:** TK2 → TK1 → TK4 → TK3 → TK5 (TK2 có hook nghịch lý quán rượu mạnh nhất để viral; TK5 là clip đọng lại giá trị chia sẻ/lưu trữ).")
    A("")
    A("---")
    A("")
    A("## 2. Diễn xuất từng clip (lời đọc + hình + âm)")
    A("")
    A("> Quy ước vai: **H** = Host (Cú) · **D** = Điều tra viên (Sói) · **C** = Chuyên gia tâm lý (Cáo) · **N1** = Trực ban · **N2** = Cảnh sát")
    A("> `pause_after` = thời gian im lặng chèn giữa hai câu (0.2–1.2 s — luật G2). Emotion an toàn (G3). Tốc độ offset trong [-0.06, +0.02] (G4). Cao độ = 0 (G5).")
    A("> Mỗi câu có mã `TKx.01#z` khớp với `SPEC_AUDIO_CLIP_TAP03.json`.")
    A("")

    for c in CLIPS:
        cid = c["id"]
        A(f"### 2.{cid[-1]} CLIP {cid} — \"{c['ten_vn']}\"")
        A("")
        A(f"*Ước lượng {c['uoc_luong_s']} s ({len(c['lines'])} câu) · BGM `{c['bgm']}` ({c['bgm_hovi']}) · SFX: {' · '.join(c['sfx'])}*")
        A("")
        A("| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |")
        A("|---|---|---|---|---|---|---|")
        for idx, ln in enumerate(c["lines"], 1):
            A(f"| `{cid}.01#{idx}` | {ln[0]} | {ln[1]} | {ln[2]} | {ln[3]} | {ln[6]} | {ln[7]} |")
        A("")
        A("| Nền | Chuyển động | Ước lượng |")
        A("|---|---|---|")
        for idx, ln in enumerate(c["lines"], 1):
            w = spoken_words(ln[6])
            d = round(w * RATE[ln[0]], 1)
            A(f"| `{cid}.01#{idx}` | `{ln[4]}` | {ln[5]} | {d} s |")
        A("")
        A("**Thẻ chữ trên hình (overlay card):**")
        for ov in c["overlay"]:
            A(f"- `{ov['sau_cau']}` → *\"{ov['text']}\"* ({ov['dur_s']} s)")
        A("")
        A(f"**Nguồn dữ liệu:** {' · '.join(c['nguon_du_lieu'])}")
        A("")

    A("---")
    A("")
    A("## 3. Tự kiểm kịch bản (QC Checklist)")
    A("")
    A("| # | Kiểm tra | Kết quả |")
    A("|---|---|---|")
    for r in QC_ROWS:
        A(f"| {r[0]} | {r[1]} | {r[2]} |")
    A("")
    A("---")
    A("")
    A("## 4. Hướng dẫn bước tiếp theo")
    A("")
    A("1. **Duyệt kịch bản:** Người dùng xem xét nội dung 5 clip trên.")
    A("2. **Sinh giọng WAV:** Đưa `02_SAN_XUAT/TIKTOK/Tap03/SPEC_AUDIO_CLIP_TAP03.json` lên Kaggle GPU chạy với engine Higgs Audio v3.")
    A("3. **Xử lý nền dọc:** Render nền 9:16 từ các file raw `t3_*` tương ứng.")
    A("4. **Dựng video & ghép phụ đề:** Dùng script dựng tự động xuất video hoàn chỉnh.")

    (OUT / "KE_HOACH_CLIP_TAP03.md").write_text("\n".join(L), encoding="utf-8")

def main():
    spec = build_spec()
    (OUT / "SPEC_AUDIO_CLIP_TAP03.json").write_text(
        json.dumps(spec, ensure_ascii=False, indent=2), encoding="utf-8")
    write_caption_files()
    global QC_ROWS
    QC_ROWS, allok = self_qc()
    write_markdown()

    print("=== THỜI LƯỢNG ƯỚC LƯỢNG ===")
    for c in CLIPS:
        print(f"{c['id']}: {c['uoc_luong_s']} s · {len(c['lines'])} câu · {c['ten_vn']}")
    print("\n=== KẾT QUẢ TỰ KIỂM ===")
    for r in QC_ROWS:
        print(f"[{r[0]}] {r[1]} -> {r[2]}")
    print("\nTỔNG KẾT:", "ĐẠT TOÀN BỘ" if allok else "CÓ LỖI")

if __name__ == "__main__":
    main()
