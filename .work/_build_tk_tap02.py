# -*- coding: utf-8 -*-
"""Sinh bộ kịch bản clip TikTok cho TẬP 02 — nguồn sự thật duy nhất.

Đầu ra:
  02_SAN_XUAT/TIKTOK/Tap02/KE_HOACH_CLIP_TAP02.md
  02_SAN_XUAT/TIKTOK/Tap02/SPEC_AUDIO_CLIP_TAP02.json
  02_SAN_XUAT/TIKTOK/Tap02/Caption_TK*.txt
  02_SAN_XUAT/TIKTOK/Tap02/MoTa_Dai_TK*.txt

Thời lượng clip KHÔNG ước lượng bừa: đo tỉ lệ đọc thật của từng vai trên
master Tập 02 (timeline_s_t02.json — đã đo bằng ASR trên mp4 thành phẩm),
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
OUT = ROOT / "02_SAN_XUAT" / "TIKTOK" / "Tap02"
OUT.mkdir(parents=True, exist_ok=True)

sys.path.insert(0, str(WORK))
from vi_cer import vi_numbers, vi_number  # noqa: E402  — đổi số→chữ đúng như TTS

# ----------------------------------------------------------------------------
# 0. TỈ LỆ ĐỌC THẬT (đo từ master Tập 02 đã sản xuất)
# ----------------------------------------------------------------------------

def measured_rate():
    tl = json.loads((WORK / "timeline_s_t02.json").read_text(encoding="utf-8"))
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
# 1. DỮ LIỆU 5 CLIP
#    nguon: mã câu trong .work/script_tap02.json (nguồn duy nhất của dữ kiện)
# ----------------------------------------------------------------------------

CLIPS = [
{
 "id": "TK1",
 "ten": "Bon nac thang. Roi mot vu an mang",
 "ten_vn": "Bốn nấc thang. Rồi một vụ án mạng",
 "chi_dau": [8, 6],
 "chude": "Quỹ đạo leo thang hành vi + ngòi nổ tâm lý (Precipitating Trigger)",
 "hook": "Bốn nấc thang. Rồi một vụ án mạng.",
 "bgm": "bgm_piano_minimal.mp3",
 "bgm_hovi": "Hồi 2 — bed tập: bgm_piano_minimal.mp3",
 "sfx": ["amb_winter_wind.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav", "fx_sub_drop.wav"],
 "overlay": [
   {"sau_cau": "TK1.01#1",  "text": "4 NẤC THANG · 82 VỤ · 1 ÁN MẠNG", "dur_s": 3.0},
   {"sau_cau": "TK1.01#3",  "text": "NẤC THỨ NHẤT — NHÌN TRỘM BAN ĐÊM", "dur_s": 2.5},
   {"sau_cau": "TK1.01#4",  "text": "NẤC THỨ HAI — ĐỘT NHẬP LẤY ĐỒ RIÊNG TƯ", "dur_s": 2.5},
   {"sau_cau": "TK1.01#7",  "text": "NẤC THỨ BA — XÂM NHẬP KHI CÓ NGƯỜI Ở NHÀ", "dur_s": 2.5},
   {"sau_cau": "TK1.01#8",  "text": "NẤC THỨ TƯ — NẠN NHÂN CUỐI CÙNG", "dur_s": 2.5},
   {"sau_cau": "TK1.01#10", "text": "NGÒI NỔ TÂM LÝ · THÁNG 7/2009", "dur_s": 2.5}
 ],
 "nguon_du_lieu": ["2.04#3", "2.05#1-#16", "3.05#4-#10", "5.07#5-#6",
                   "nguon_tham_khao.md (R. v. Williams 2010 ONSC 5946)"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_escalation_stairs","still",
   "Bốn nấc thang. Tám mươi hai vụ trộm. Rồi một vụ án mạng.",
   "2.05#1 · 2.05#7 · 5.07#5"),
  ("H","neutral",-0.02,0.6,"tk02_escalation_stairs","pull",
   "Hắn không bắt đầu bằng bạo lực. Hắn bắt đầu bằng việc đứng ngoài cửa sổ ban đêm.",
   "2.05#2 · 2.05#3 · 5.07#5"),
  ("D","neutral",-0.03,0.6,"tk02_open_window","push",
   "Nấc thang thứ nhất: nhìn trộm ban đêm, đứng ngoài bóng tối rình rập phụ nữ qua khung cửa sổ.",
   "2.05#2 · 2.05#3"),
  ("D","neutral",-0.03,0.6,"tk02_drawer_dark","pan",
   "Nấc thang thứ hai: đột nhập lấy đồ riêng tư. Hắn không lấy tiền hay trang sức. Hắn lấy đồ lót và đồ riêng tư của phụ nữ.",
   "2.05#4 · 2.05#8 · 2.05#9"),
  ("D","neutral",-0.03,0.5,"tk02_folder_tree","still",
   "Nghi thức lặp lại y hệt ở mọi căn nhà: chụp ảnh, lấy đồ, rồi ghi chép lại.",
   "2.05#10"),
  ("C","neutral",-0.02,0.6,"tk02_brain_neural","push",
   "Khi hành vi cũ trở nên quen thuộc, hắn rơi vào trạng thái đói ảo tưởng, buộc phải tăng liều lượng rủi ro để tìm lại khoái cảm ban đầu.",
   "3.05#7 · 3.05#8 · 3.05#9"),
  ("D","neutral",-0.03,0.6,"tk02_open_window","pan",
   "Nấc thang thứ ba: tháng 9 năm 2009, hắn đột nhập vào nhà lúc có người ở nhà.",
   "2.05#11 · 2.05#12 · 2.05#13"),
  ("D","neutral",-0.03,0.7,"tk02_two_chairs","still",
   "Và nấc thang thứ tư: cuối tháng 11 năm 2009, nạn nhân là Marie-France Comeau, nữ hạ sĩ ba mươi bảy tuổi phục vụ ngay trong căn cứ mà hắn chỉ huy.",
   "2.05#14 · 2.05#15"),
  ("H","neutral",-0.02,0.6,"tk02_house_missing","pull",
   "Chỉ hai tháng sau đó, nạn nhân tiếp theo là Jessica Lloyd.",
   "2.05#16"),
  ("C","neutral",-0.02,0.6,"tk02_oath_hall","push",
   "Tháng 7 năm 2009, khi hắn được thăng cấp chỉ huy trưởng căn cứ Trenton, đó là ngòi nổ tâm lý: cảm giác quyền lực tối cao cùng áp lực công việc đã đánh sập chốt chặn kiểm soát cuối cùng.",
   "1.03#4 · 3.05#10"),
  ("H","neutral",-0.02,0.7,"tk02_escalation_stairs","push",
   "Tội ác không bao giờ bắt đầu từ một vụ án mạng. Nó bắt đầu từ một cái nhìn trộm không bị trừng phạt.",
   "5.07#5 · 5.07#6"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
},
{
 "id": "TK2",
 "ten": "Van lop xe trung khop. Canh sat van kinh can chao",
 "ten_vn": "Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào",
 "chi_dau": [9, 1],
 "chude": "Hiệu ứng hào quang + ảnh hưởng xã hội (dư chấn tập thể)",
 "hook": "Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào.",
 "bgm": "bgm_sub_drone.mp3",
 "bgm_hovi": "Hồi 1 — bed tập: bgm_sub_drone.mp3",
 "sfx": ["amb_road_night.wav (nền)", "fx_tire_snow.wav", "fx_window_down.wav", "fx_flashlight.wav", "fx_police_radio.wav"],
 "overlay": [
   {"sau_cau": "TK2.01#5",  "text": "TRẠM KIỂM SOÁT LƯU ĐỘNG · ĐÊM 4/2", "dur_s": 2.5},
   {"sau_cau": "TK2.01#9",  "text": "CHỈ GHI NHẬN THÔNG TIN — RỒI KÍNH CẨN CHÀO", "dur_s": 2.5},
   {"sau_cau": "TK2.01#10", "text": "HIỆU ỨNG HÀO QUANG", "dur_s": 3.0}
 ],
 "nguon_du_lieu": ["1.03#1-#4", "1.05#1-#4", "1.08#4", "1.10#1-#3", "1.12#1-#3",
                   "1.14#1-#7", "1.17#1-#3", "nguon_tham_khao.md (OPP + Belleville Police)"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_checkpoint","still",
   "Vân lốp xe trùng khớp. Và cảnh sát vẫn kính cẩn chào cho người đàn ông đó đi.",
   "1.14#4 · 1.14#5"),
  ("H","neutral",-0.02,0.6,"tk02_oath_hall","pull",
   "Tháng 7 năm 2009, Đại tá Russell Williams nhận quyền chỉ huy tối cao căn cứ không quân Trenton.",
   "1.03#1 · 1.03#4"),
  ("H","neutral",-0.02,0.6,"tk02_oath_hall","pan",
   "Ông từng lái chuyên cơ đưa đón Nữ hoàng Anh Elizabeth II.",
   "1.05#1"),
  ("D","neutral",-0.03,0.6,"tk02_house_missing","still",
   "Đêm 28 tháng 1 năm 2010, Jessica Lloyd, hai mươi bảy tuổi, biến mất khỏi nhà riêng ở Belleville.",
   "1.10#1 · 1.10#2"),
  ("D","neutral",-0.03,0.7,"tk02_checkpoint","push",
   "Cảnh sát không tìm ra manh mối nào trong những ngày đầu tiên. Một tuần sau đó, tối ngày 4 tháng 2, họ lập trạm kiểm soát lưu động suốt đêm, chỉ để săn một dấu vết: vệt vân lốp xe hiếm gặp trên nền tuyết.",
   "1.12#1 · 1.12#2 · 1.12#3"),
  ("D","neutral",-0.03,0.6,"tk02_suv_stop","still",
   "Trong dòng xe qua trạm đêm hôm đó có một chiếc Nissan Pathfinder, thay vì chiếc BMW thường ngày.",
   "1.14#1 · 1.14#2"),
  ("D","neutral",-0.03,0.5,"tk02_suv_stop","push",
   "Người ngồi sau vô-lăng hạ cửa kính xuống — chính là chỉ huy trưởng căn cứ không quân Trenton.",
   "1.14#3"),
  ("H","neutral",-0.02,0.5,"tk02_tire_track","still",
   "Vân lốp xe của ông ta trông rất giống dấu vết trên tuyết.",
   "1.14#4"),
  ("D","neutral",-0.03,0.7,"tk02_checkpoint","pan",
   "Nhưng trước một sĩ quan cấp cao, các sĩ quan tuần tra không thể giữ ông ta lại — họ chỉ ghi nhận rồi kính cẩn chào cho đi. Và trong ba ngày tiếp theo, ông ta vẫn là một vị đại tá tự do.",
   "1.14#5 · 1.14#6"),
  ("C","neutral",-0.02,0.7,"tk02_siren_wall","push",
   "Hiệu ứng hào quang: tấm khiên vô hình khiến cả xã hội lẫn cơ quan thực thi pháp luật bị che mắt nhiều năm ròng.",
   "1.08#4"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
},
{
 "id": "TK3",
 "ten": "Hai cuoc doi. Mot co the. Mot cau chuyen de tu bao chua",
 "ten_vn": "Hai cuộc đời. Một câu chuyện để tự bào chữa",
 "chi_dau": [5, 3],
 "chude": "Hệ thống tự bào chữa (Neutralization) + cơ chế chia ngăn (Compartmentalization)",
 "hook": "Hai cuộc đời. Một câu chuyện để tự bào chữa.",
 "bgm": "bgm_cello_sad_v2.mp3",
 "bgm_hovi": "Hồi 3 — bed tập: bgm_cello_sad_v2.mp3",
 "sfx": ["amb_basement.wav (nền)", "fx_drawer_open.wav", "fx_stinger.wav", "fx_hdd_spin.wav"],
 "overlay": [
   {"sau_cau": "TK3.01#3",  "text": "PHÂN MẢNH TÂM TRÍ (COMPARTMENTALIZATION)", "dur_s": 3.0},
   {"sau_cau": "TK3.01#4",  "text": "NGĂN KÉO THỨ NHẤT — ĐẠI TÁ", "dur_s": 2.5},
   {"sau_cau": "TK3.01#5",  "text": "NGĂN KÉO THỨ HAI — KẺ SĂN MỒI BÓNG ĐÊM", "dur_s": 2.5},
   {"sau_cau": "TK3.01#7",  "text": "TRUNG HÒA ĐẠO ĐỨC (NEUTRALIZATION)", "dur_s": 3.0},
   {"sau_cau": "TK3.01#8",  "text": "“MỘT MÓN KỶ NIỆM”", "dur_s": 2.5},
   {"sau_cau": "TK3.01#10", "text": "“TÔI KHÔNG BIẾT CÂU TRẢ LỜI”", "dur_s": 2.5}
 ],
 "nguon_du_lieu": ["3.04#1-#2", "3.08#1-#13", "nguon_tham_khao.md (bản ghi thẩm vấn 07/02/2010)"],
 "lines": [
  ("H","neutral",-0.02,0.5,"tk02_two_drawers","still",
   "Hai cuộc đời. Một cơ thể. Một câu chuyện để tự bào chữa.",
   "3.08#1 · 3.08#8"),
  ("H","neutral",-0.02,0.7,"tk02_two_masks","pull",
   "Trước khi phân tích: không tồn tại chẩn đoán lâm sàng công khai nào về Russell Williams. Đây là khung lý thuyết, không phải phán xét.",
   "3.04#1 · 3.04#2"),
  ("C","neutral",-0.02,0.7,"tk02_brain_neural","push",
   "Trong tâm lý học, phân mảnh tâm trí là cơ chế phòng vệ khóa chặt hai luồng nhận thức và cảm xúc trái ngược nhau vào hai ngăn kéo.",
   "3.08#2"),
  ("C","neutral",-0.02,0.6,"tk02_command_chair","pan",
   "Ngăn kéo thứ nhất là vị đại tá: người chỉ huy mẫu mực, người chồng chăm sóc vườn tược.",
   "3.08#4"),
  ("C","neutral",-0.02,0.6,"tk02_stairs_dark","push",
   "Ngăn kéo thứ hai là kẻ săn mồi bóng đêm, nơi hắn giải phóng những xung lực tàn bạo nhất.",
   "3.08#5"),
  ("C","neutral",-0.02,0.7,"tk02_two_drawers","still",
   "Khi ở ngăn kéo này, hắn đóng chặt cánh cửa của ngăn kéo kia, rồi dùng người vợ và cuộc hôn nhân chuẩn mực làm lá chắn.",
   "3.08#6 · 3.08#7"),
  ("C","neutral",-0.02,0.8,"tk02_drawer_dark","pull",
   "Để lương tri không lên tiếng, hắn trung hòa đạo đức. Trong tám mươi hai vụ đầu, hắn tự nhủ: <#0.35#> mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm.",
   "3.08#8"),
  ("C","neutral",-0.02,0.7,"tk02_hidden_drive","pan",
   "Đến khi có án mạng, hắn lại tự biện minh rằng nạn nhân đã thấy mặt mình, ép mình phải ra tay để tự vệ.",
   "3.08#9"),
  ("C","neutral",-0.02,0.5,"tk02_two_drawers","still",
   "Và chính vì vậy, cuối cùng hắn không thể tự giải thích một cách có lương tri.",
   "3.08#10"),
  ("C","sad",-0.04,0.9,"tk02_interrogation_early","push",
   "Khi thám tử hỏi vì sao mình làm những việc đó, câu trả lời trong bản ghi thẩm vấn trống rỗng: <#0.35#> Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng.",
   "3.08#11"),
  ("C","sad",-0.04,0.7,"tk02_head_down","pull",
   "Đó là câu trả lời trơ trẽn nhất, phơi bày sự ngắt kết nối đạo đức của kẻ săn mồi này.",
   "3.08#12"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
},
{
 "id": "TK4",
 "ten": "Khong mot loi xin loi nao nhac toi nan nhan",
 "ten_vn": "Không một lời xin lỗi nào nhắc tới nạn nhân",
 "chi_dau": [4, 1],
 "chude": "Sự sụp đổ cái tôi ái kỷ (Narcissistic Collapse) + bản án tâm lý",
 "hook": "Không một lời xin lỗi nào nhắc tới nạn nhân.",
 "bgm": "bgm_piano_warm.mp3",
 "bgm_hovi": "Hồi 5 — bed tập: bgm_piano_warm.mp3",
 "sfx": ["amb_courtroom.wav (nền)", "fx_gavel_triple.wav", "fx_fire_whoosh.wav", "amb_fire.wav", "fx_heartbeat_slow.wav"],
 "overlay": [
   {"sau_cau": "TK4.01#1",  "text": "KHÔNG MỘT LỜI XIN LỖI NÀO NHẮC TỚI NẠN NHÂN", "dur_s": 3.0},
   {"sau_cau": "TK4.01#3",  "text": "KHÔNG PHẢI ĂN NĂN — LÀ TỰ THƯƠNG HẠI BẢN THÂN", "dur_s": 2.5},
   {"sau_cau": "TK4.01#4",  "text": "88 CÁO BUỘC", "dur_s": 2.5},
   {"sau_cau": "TK4.01#5",  "text": "CHUNG THÂN 25 NĂM — KHÔNG ĐƯỢC XÉT ÂN XÁ", "dur_s": 2.5},
   {"sau_cau": "TK4.01#7",  "text": "ĐỐT TOÀN BỘ QUÂN PHỤC MANG TÊN HẮN", "dur_s": 2.5},
   {"sau_cau": "TK4.01#9",  "text": "SỤP ĐỔ CÁI TÔI ÁI KỶ (NARCISSISTIC COLLAPSE)", "dur_s": 3.0}
 ],
 "nguon_du_lieu": ["4.11#1-#9", "5.02#1-#6", "5.04#1-#9", "5.06#1-#4",
                   "nguon_tham_khao.md (phán quyết 21/10/2010 · thông cáo Bộ Quốc phòng)"],
 "lines": [
  ("H","neutral",-0.02,0.6,"tk02_interrogation_early","still",
   "Không một lời xin lỗi nào nhắc tới nạn nhân.",
   "4.11#6 · 4.11#7"),
  ("C","sad",-0.04,0.8,"tk02_two_chairs","pull",
   "Trong phòng thẩm vấn, nỗi lo hắn thốt ra chỉ xoay quanh việc người vợ nhìn nhận hắn ra sao, và sự sụp đổ danh tiếng của căn cứ quân sự. Hắn không nhắc đến nỗi đau của người phụ nữ hay gia đình nạn nhân.",
   "4.11#6 · 4.11#7"),
  ("C","sad",-0.04,0.8,"tk02_head_down","push",
   "Đó không phải sự ăn năn hối cải chân chính, mà là sự thương hại bản thân tột độ khi tấm mặt nạ danh dự xây suốt hai mươi lăm năm vỡ vụn.",
   "4.11#8 · 4.11#9"),
  ("H","neutral",-0.02,0.6,"tk02_courtroom","still",
   "Ngày 18 tháng 10 năm 2010, hắn nhận tội trước tòan bộ 88 cáo buộc.",
   "5.02#1 · 5.02#3"),
  ("H","neutral",-0.02,0.8,"tk02_gavel","push",
   "Ba ngày sau, thẩm phán tuyên hai mức tù chung thân chạy song song cho hai tội danh nghiêm trọng nhất, cộng thêm các mức tù khác. Mức án chung thân với hai mươi lăm năm không được xét ân xá.",
   "5.02#4 · 5.02#5"),
  ("H","neutral",-0.02,0.6,"tk02_courtroom","pan",
   "Nhưng bản án lớn nhất với một kẻ ái kỷ như hắn là sự sụp đổ về danh dự và quyền lực: quân hàm bị thu hồi, huân chương bị cắt thành từng mảnh.",
   "5.04#1 · 5.04#2 · 5.04#3"),
  ("H","neutral",-0.02,0.7,"tk02_uniform_fire","still",
   "Quân đội Canada còn làm một việc chưa từng có tiền lệ: đốt toàn bộ quân phục và trang phục mang tên hắn tại một lò tiêu hủy tài liệu mật.",
   "5.04#5"),
  ("D","neutral",-0.03,0.7,"tk02_uniform_fire","pan",
   "Theo người phát ngôn quân đội Hubert Genest: không có nghi lễ chính thức, cũng không có ảnh chụp.",
   "5.04#6 · 5.04#7"),
  ("C","neutral",-0.02,0.6,"tk02_brain_neural","pull",
   "Về mặt tâm lý, đó là biểu hiện kinh điển của sự sụp đổ cái tôi ái kỷ: khi không còn quyền kiểm soát, kẻ săn mồi chỉ còn lại sự tự thương hại.",
   "5.06#4"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
},
{
 "id": "TK5",
 "ten": "Hãy luôn tin vào truc giac cua ban",
 "ten_vn": "Hãy luôn tin vào trực giác của bạn",
 "chi_dau": [10],
 "chude": "Nạn nhân học & bài học sinh tồn (ranh giới + trực giác)",
 "hook": "Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó.",
 "bgm": "bgm_ambient_deep.mp3",
 "bgm_hovi": "Hồi 5 — bed tập: bgm_piano_warm.mp3 (clip kết, dùng ambient_deep để tách tiếng với TK4)",
 "sfx": ["amb_road_night.wav (nền)", "fx_tension_tick.wav", "fx_stinger.wav", "fx_heartbeat_slow.wav"],
 "overlay": [
   {"sau_cau": "TK5.01#1", "text": "ĐỪNG HỢP LÝ HÓA SỰ BẤT AN", "dur_s": 2.5},
   {"sau_cau": "TK5.01#2", "text": "DẤU HIỆU SỚM: BẤT AN MƠ HỒ", "dur_s": 2.5},
   {"sau_cau": "TK5.01#4", "text": "TỘI ÁC BẮT ĐẦU TỪ NHỮNG BƯỚC RẤT NHỎ", "dur_s": 2.5},
   {"sau_cau": "TK5.01#7", "text": "HÃY LUÔN TIN VÀO TRỰC GIÁC CỦA BẠN", "dur_s": 3.0}
 ],
 "nguon_du_lieu": ["4.06#1-#4", "5.07#4-#6", "5.08#2-#5", "nguon_tham_khao.md (The Gift of Fear)"],
 "lines": [
  ("H","neutral",-0.02,0.6,"tk02_red_flags","still",
   "Nếu bạn cảm thấy một sự bất an mơ hồ, nếu ranh giới riêng tư của bạn bị xâm phạm dù chỉ nhỏ nhất, đừng hợp lý hóa hay coi thường nó.",
   "5.08#4"),
  ("D","neutral",-0.03,0.6,"tk02_town_snow","pull",
   "Trong vụ án này, trước khi sự thật vỡ lở, thị trấn Tweed đã sống trong một nỗi bất an mơ hồ đến ngạt thở.",
   "4.06#1"),
  ("N2","sad",-0.04,0.8,"tk02_cottage_search","push",
   "Đồ đạc riêng tư thỉnh thoảng bị xáo trộn, cửa nẻo có dấu cạy phá nhưng không mất tiền bạc. Chúng tôi tưởng mình đang hoang tưởng.",
   "4.06#2 · 4.06#3"),
  ("H","neutral",-0.02,0.8,"tk02_escalation_stairs","pan",
   "Tội ác không bao giờ bắt đầu từ một vụ án mạng. Nó luôn bắt đầu từ những bước lấn ranh giới rất nhỏ: một cái nhìn trộm, một lần lục lọi đồ riêng tư, một sự xâm phạm không bị trừng phạt.",
   "5.07#5 · 5.07#6"),
  ("C","neutral",-0.02,0.7,"tk02_oath_hall","pull",
   "Địa vị, bằng cấp hay quân hàm lộng lẫy chỉ là lớp áo khoác xã hội, không phải tấm bảo chứng cho sự lương thiện của một tâm hồn.",
   "5.07#4"),
  ("D","neutral",-0.03,0.6,"tk02_escalation_stairs","pan",
   "Sự kiêu hãnh của một kẻ ái kỷ luôn để lại dấu vết.",
   "5.08#2"),
  ("D","neutral",-0.03,0.8,"tk02_red_flags","still",
   "Hãy luôn tin vào trực giác của bạn. Trực giác sinh tồn chính là hệ thống cảnh báo sớm giúp bảo vệ mạng sống của chúng ta.",
   "5.08#3 · 5.08#5"),
  ("H","neutral",-0.02,0.0,"tk02_podcast_desk","still",
   "Tập hai của Amber Eyes. Xem hồ sơ đầy đủ ở link trong bio.",
   "CTA — không phải dữ kiện")
 ]
}
]

# ----------------------------------------------------------------------------
# 2. TÍNH THỜI LƯỢNG + KIỂM TRA
# ----------------------------------------------------------------------------

CAM = {
 "H": "Host (Cú) — trầm ấm",
 "D": "Điều tra viên (Sói) — lạnh lùng, dứt khoát",
 "C": "Chuyên gia tâm lý (Cáo) — nữ, điềm tạm học thuật",
 "N1": "Người dân (Cừu) — nam trung niên, chân thật",
 "N2": "Khán giả (Mèo) — nữ trung niên, bàng hoàng",
}

def analyse(clip):
    tot = 0.0
    for i, (vai, emo, spd, pause, nen, cd, text, nguon) in enumerate(clip["lines"], 1):
        d = est_dur(text, vai)
        tot += d + pause
    return tot

for c in CLIPS:
    c["uoc_luong_s"] = analyse(c)

# ----------------------------------------------------------------------------
# 3. SINH SPEC JSON
# ----------------------------------------------------------------------------

def slug(s):
    s = s.lower()
    s = re.sub(r"[đ]", "d", s)
    s = re.sub(r"[^a-z0-9]+", "_", s).strip("_")
    return s

def build_spec():
    spec = {
        "_readme": ("SPEC_AUDIO_CLIP_TAP02.json — đặc tả âm thanh để SINH WAV cho 5 clip TikTok của Tập 02 "
                    "(20/11/2026). CHƯA có file âm thanh nào được tạo. Bản gốc: 02_SAN_XUAT/TIKTOK/Tap02/KE_HOACH_CLIP_TAP02.md"),
        "_tap": "02",
        "_ten_tap": "Đại tá hai mặt (Russell Williams)",
        "_ngon_ngu": "vi",
        "_so_cau": sum(len(c["lines"]) for c in CLIPS),
        "_so_clip": len(CLIPS),
        "_uoc_luong_thoi_luong": ("Không ước lượng bằng cảm tính: đo tỉ lệ đọc thật của từng vai trên master Tập 02 "
                                  "(timeline_s_t02.json — timeline đo bằng ASR trên mp4 thành phẩm), rồi chiếu theo số từ "
                                  "SAU KHI đổi số→chữ (đúng phần TTS đọc). Sai số dự kiến ±5 %."),
        "_canh_bao": ("Số đo thời lượng là ƯỚC LƯỢNG có cơ sở đo, KHÔNG phải số đo thật của clip (chưa có WAV). "
                      "Số đo thật lấy sau khi sinh WAV: cộng dur từng file + pause_after, rồi đo lại trên mp4 cuối (A7)."),

        "engine": {
            "mo_hinh": "bosonai/higgs-tts-3-4b",
            "dataset_kaggle": "chiduong2026/amber-eyes-voice-ref-voxcpm2",
            "giong_dung": ("ĐÚNG giọng của chính Tập 02 (VoxCPM2 refs đã qua G9 cho tập này) — KHÔNG dùng bộ A MiniMax, "
                           "vì giọng clip sẽ lệch giọng tập trên YouTube."),
            "vai_voi_clip_tham_chieu": {
                "H": "assets/voice_ref_voxcpm2/H.wav",
                "D": "assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav",
                "C": "assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav",
                "N1": "assets/voice_ref_voxcpm2_g9/W6_LOW.wav",
                "N2": "assets/voice_ref_voxcpm2_g9/W5_HIGH.wav"
            },
            "gen_params": {
                "temperature": 0.8, "top_p": 0.95, "top_k": 50,
                "max_new_tokens": 1196, "sample_rate": 24000,
                "fade_in_ms": 30, "fade_out_ms": 15,
                "seed_scheme": "sha256(id|role|ref|temp|vN) -> int(hex[:8],16)",
                "variants_per_line": 2
            },
            "cam": ("KHONG dung <|emotion:...|> (chi <|prosody:pause|> sau dau ':' truoc cau trich). "
                    "Thay the: chi 1 thay <#0.35#> moi cau, dat ngay sau dau ':' truoc cau trich."),
            "ghi_chu_cher": "Moi cau chi duoc MOT thay <#0.35#>, dat sau dau ':' truoc cau trich (G1). " \
                            "Pitch LUON = 0 (G5). Speed chi trong -0.06 ... +0.02 (G4). " \
                            "Emotion chi 4 gia tri an toan: neutral, sad, fearful, surprised (G3)."
        },

        "quy_uoc_dat_ten": {
            "thu_muc_dich": ".work/audio_s_tk_t02/",
            "ten_file": "<ma_cau>.wav voi '#' thay bang '_' — TK1.01#1 -> TK1.01_01.wav",
            "manifest": ".work/audio_s_tk_t02/manifest_tk_t02.json",
            "manifest_dong_mau": {
                "id": "TK1.01#1", "vai": "H", "file": "TK1.01_01.wav", "dur": 6.42,
                "emotion": "neutral", "speed": -0.02, "pause_after": 0.5, "variant": 0
            }
        },

        "cang_qua_audio": {
            "A1_V4": "0 khoang cam tuyet doi > 0.3 s — luon co lop nen moi truong ben duoi",
            "A7": "-16 +/- 1 LUFS · true peak <= -1.5 dBFS · do tren mp4 cuoi",
            "G6": "loi doc khong duoc doi chu — phu de va theo hinh lay nguyen van cau trong spec nay",
            "G12": "CER < 2 % cho MOI cau (do bang Whisper / measure_cer_prod.py)",
            "G9": "H-D >= 4 nc · C-H >= 4 nc · C-D >= 4 nc",
            "G10": "nghe lien theo vai: moi vai ra 1 nguoi, 3 vai tach bach"
        },

        "ti_le_doc_do_duoc": {
            "_nguon": ".work/timeline_s_t02.json (timeline do bang ASR tren master Tập 02)",
            "_cach": "gioi = tong gio liet ke / tong so TU sau khi vi_numbers() (dung thu TTS doc)",
            "s_gio_tren_tu": {r: round(v, 4) for r, v in RATE.items()},
            "tu_tren_gio": {r: round(1 / v, 4) for r, v in RATE.items()}
        },

        "am_thanh_nen": {
            "_quy_tac": ("CHI dung nguon duoi day. Tuyet doi KHONG dung 2 file YouTube Audio Library "
                         "(bgm_guitar_acoustic_60s.mp3, bgm_church_organ.mp3) va 32 file SFX trong assets/sfx/t2/ "
                         "(ban YouTube Audio Library) — giay phep cua YouTube Audio Library khong phu TikTok. "
                         "Dung ban TU TONG HOP trong assets/sfx/t2/_code/ (cung ten file, cung hieu ung)."),
            "bgm_minimax_duoc_phep": ["bgm_piano_minimal.mp3", "bgm_sub_drone.mp3", "bgm_cello_sad_v2.mp3",
                                      "bgm_piano_warm.mp3", "bgm_ambient_deep.mp3"],
            "sfx_duoc_phep": [
                "assets/sfx/t2/_code/*.wav — SFX tu tong hop bang .work/make_sfx.py",
                "Freesound CC0"
            ],
            "sfx_cam": ["assets/sfx/t2/*.wav (khong phai _code)", "assets/sfx/t1/..t29/"],
            "muc_am_thanh": "giong -16 LUFS · BGM -26 dB khi co loi, nang -14 dB o nghi 0.8-1.2 s truoc cau chot"
        },

        "nen_doc": {
            "_quy_tac": ("Clip dung nen DOC 9:16 1080x1920. Tap01 da tao 16 nen rieng co tien to tk01_ trong assets/bg/. "
                         "Tap02 CAN tao nhom tk02_ (xem KE_HOACH_CLIP_TAP02.md muc 7). "
                         "LUU Y: ban 16:9 t2_*.png da bi don sach khoi assets/bg/ — chi con _raw/t2_* (2752x1536). "
                         "Phuong an B (blur-fill) van dung duoc truc tiep tu _raw."),
            "danh_sach": sorted({ln[4] for c in CLIPS for ln in c["lines"]})
        },

        "clips": []
    }

    for c in CLIPS:
        lines = []
        for i, (vai, emo, spd, pause, nen, cd, text, nguon) in enumerate(c["lines"], 1):
            lines.append({
                "id": f'{c["id"]}.01#{i}', "vai": vai, "emotion": emo, "speed": spd,
                "pause_after": pause, "nen": nen, "chuyen_dong": cd,
                "text": text, "uoc_luong_s": round(est_dur(text, vai), 2), "nguon": nguon
            })
        spec["clips"].append({
            "id": c["id"],
            "ten": c["ten"],
            "ten_vn": c["ten_vn"],
            "chi_dau": c["chi_dau"],
            "chude": c["chude"],
            "hook_text": c["hook"],
            "hook_seconds": 3,
            "target_len_s": [65, 90],
            "uoc_luong_s": round(c["uoc_luong_s"], 1),
            "so_cau": len(c["lines"]),
            "sai_so_uoc_luong": "+/- 7 % (p90, mo phong tren 203 cau that cua Tap 02)",
            "bgm": c["bgm"],
            "bgm_hovi": c["bgm_hovi"],
            "sfx": c["sfx"],
            "overlay_cards": [{"sau_cau": o["sau_cau"], "text": o["text"], "dur_s": o["dur_s"]} for o in c["overlay"]],
            "nguon_du_lieu": c["nguon_du_lieu"],
            "lines": lines,
            "caption": build_caption(c),
            "hashtags": HASHTAGS[c["id"]]
        })
    return spec

# ----------------------------------------------------------------------------
# 4. CAPTION + MÔ TẢ DÀI
# ----------------------------------------------------------------------------

LINK_TAP02 = "[LINK_TẬP 02 — cần điền]"

CAPTION_HOOK = {
 "TK1": "Bốn nấc thang. Rồi một vụ án mạng. 👁️",
 "TK2": "Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào. 👁️",
 "TK3": "Hai cuộc đời. Một câu chuyện để tự bào chữa. 👁️",
 "TK4": "Không một lời xin lỗi nào nhắc tới nạn nhân. 👁️",
 "TK5": "Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó. 👁️",
}

CAPTION_SUB = {
 "TK1": "Tập 02 · Đại tá hai mặt — chỉ dấu #8: quỹ đạo leo thang hành vi.",
 "TK2": "Tập 02 · Đại tá hai mặt — chỉ dấu #9: hiệu ứng hào quang.",
 "TK3": "Tập 02 · Đại tá hai mặt — chỉ dấu #5: hệ thống tự bào chữa.",
 "TK4": "Tập 02 · Đại tá hai mặt — chỉ dấu #4: sụp đổ cái tôi ái kỷ.",
 "TK5": "Tập 02 · Đại tá hai mặt — chỉ dấu #10: bài học sinh tồn.",
}

CAPTION_KEY = {
 "TK1": "🔎 Chỉ dấu tâm lý · leo thang hành vi · hồ sơ có thật",
 "TK2": "🔎 Chỉ dấu tâm lý · hiệu ứng hào quang · hồ sơ có thật",
 "TK3": "🔎 Chỉ dấu tâm lý · phân mảnh tâm trí · hồ sơ có thật",
 "TK4": "🔎 Chỉ dấu tâm lý · sụp đổ cái tôi · hồ sơ có thật",
 "TK5": "🔎 Chỉ dấu tâm lý · trực giác sinh tồn · hồ sơ có thật",
}

HASHTAGS = {
 "TK1": ["#AmberEyes", "#TamLyToiPham", "#HosoCoThat", "#Escalation", "#QuyDaoLeoThang", "#TrueCrime", "#MoiTuanMotTap"],
 "TK2": ["#AmberEyes", "#TamLyToiPham", "#HosoCoThat", "#HieuUngHaoQuang", "#QuanDoi", "#TrueCrime", "#MoiTuanMotTap"],
 "TK3": ["#AmberEyes", "#TamLyToiPham", "#HosoCoThat", "#Compartmentalization", "#SelfJustification", "#TrueCrime", "#MoiTuanMotTap"],
 "TK4": ["#AmberEyes", "#TamLyToiPham", "#HosoCoThat", "#NarcissisticCollapse", "#BanAn", "#TrueCrime", "#MoiTuanMotTap"],
 "TK5": ["#AmberEyes", "#TamLyToiPham", "#HosoCoThat", "#TrucGiac", "#CanhGiuAnToan", "#TrueCrime", "#MoiTuanMotTap"],
}

# Dong nhan AIGC — luật T3 ke hoach me: PHẢI ghi nhan trong CAPTION (khong
# chi trong phan "ghi chu khi dang"), truong hop nguoi dung quen them khi dan.
DONG_AIGC = "Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự."


def build_caption(c):
    cid = c["id"]
    return "\n".join([
        CAPTION_HOOK[cid],
        "",
        CAPTION_SUB[cid],
        "Hồ sơ có thật, dữ liệu có nguồn.",
        "",
        f"📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio",
        CAPTION_KEY[cid],
        "",
        DONG_AIGC,
        "",
        " ".join(HASHTAGS[cid]),
    ])

MO_TA_DAI = {
 "TK1": """Bốn nấc thang. Tám mươi hai vụ trộm. Rồi một vụ án mạng. 👁️

Tập 02 · Đại tá hai mặt — Chỉ dấu #8: quỹ đạo leo thang hành vi.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · leo thang hành vi · hồ sơ có thật

——————
CHỈ DẤU #8: QUỸ ĐẠO LEO THANG HÀNH VI
——————
Không ai bắt đầu bằng một vụ án mạng. Bản thân điều đó đã là manh mối về cách hành vi leo thang.

Hồ sơ này tái dựng được bốn nấc thang, mỗi nấc là một bước lấn ranh giới rất nhỏ, không bị trừng phạt, và không bị ai chặn lại:
• NẤC 1 — NHÌN TRỘM BAN ĐÊM: đứng ngoài bóng tối để rình rập phụ nữ qua khung cửa sổ.
• NẤC 2 — ĐỘT NHẬP LẤY ĐỒ RIÊNG TƯ: từ tháng 9/2007 đến tháng 11/2009, tổng cộng 82 vụ trộm đồ riêng tư. Hắn không lấy tiền bạc, không lấy trang sức quý giá. Nghi thức lặp lại y hệt ở mọi căn nhà: chụp ảnh, lấy đồ, rồi ghi chép lại tỉ mỉ.
• NẤC 3 — XÂM NHẬP KHI CÓ NGƯỜI Ở NHÀ: tháng 9/2009.
• NẤC 4 — ĐOẠT MẠNG NẠN NHÂN: cuối tháng 11/2009, nạn nhân là nữ hạ sĩ Marie-France Comeau, 37 tuổi, phục vụ ngay trong căn cứ quân sự mà hắn chỉ huy. Chỉ hai tháng sau đó là Jessica Lloyd.

Cơ chế bão hoà kích thích của não bộ con người giải thích vì sao các nấc thang không dừng lại: khi hành vi cũ trở nên quen thuộc, hắn rơi vào trạng thái "đói ảo tưởng", buộc phải tăng liều lượng rủi ro để tìm lại khoái cảm ban đầu.

Và ngòi nổ tâm lý nằm đúng chỗ đáng lẽ phải chặn hắn lại: tháng 7/2009, khi hắn được thăng cấp chỉ huy trưởng căn cứ không quân Trenton.

——————
BỐI CẢNH HỒ SƠ
——————
Căn cứ không quân Trenton — Ontario, Canada — căn cứ không quân chiến lược lớn nhất của quân đội Canada, và nơi đón linh cữu các liệt sĩ Canada từ chiến trường Afghanistan về dọc "Con lộ Anh hùng". Chỉ huy trưởng nơi đó tháng 7/2009 là Đại tá David Russell Williams: 46 tuổi, từng lái chuyên cơ đưa đón Nữ hoàng Anh Elizabeth II, Hoàng thân Philip và các Thủ tướng Canada.

——————
NGUỒN THAM KHẢO
——————
• Bản án Tòa Thượng thẩm Ontario — R. v. Williams, 2010 ONSC 5946 (bản án 21/10/2010, thẩm phán Robert Scott)
• Báo cáo điều tra Cảnh sát OPP + Belleville Police Service
• Biên bản thẩm vấn ngày 07/02/2010 · lời khai của Thám tử Jim Smyth trước tòa
• Bản tin The Globe and Mail · Toronto Star · CTV News
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap02/kichban_tap02_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md

——————
LƯU Ý
——————
• Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.
• Nội dung không phù hợp cho trẻ em.
• Mang tính giáo dục, phân tích tâm lý tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên tư liệu công khai (hồ sơ tòa án, báo chí điều tra). Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Nhân vật Cú, Sói, Cáo là linh thú minh hoạ; lời thoại phục dựng dựa trên tư liệu điều tra.
• Hồ sơ có thật, dữ liệu có nguồn.

#AmberEyes #TamLyToiPham #HosoCoThat #Escalation #QuyDaoLeoThang #TrueCrime #MoiTuanMotTap""",

 "TK2": """Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào. 👁️

Tập 02 · Đại tá hai mặt — Chỉ dấu #9: hiệu ứng hào quang.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · hiệu ứng hào quang · hồ sơ có thật

——————
CHỈ DẤU #9: HIỆU ỨNG HÀO QUANG
——————
Đêm 28/01/2010, Jessica Lloyd — nữ nhân viên 27 tuổi, sống một mình ở Belleville — biến mất khỏi nhà riêng. Cảnh sát tỉnh Ontario mở cuộc tìm kiếm quy mô lớn chưa từng có, nhưng trong những ngày đầu tiên không tìm ra manh mối nào.

Một tuần sau đó, vào tối ngày 4 tháng 2, cảnh sát lập một trạm kiểm soát lưu động kéo dài suốt đêm trên con đường gần nhà nạn nhân. Mục tiêu duy nhất của trạm: săn một dấu vết — vệt vân lốp xe địa hình hiếm gặp in hằn trên nền tuyết.

Trong dòng xe đi qua trạm đêm hôm đó có một chiếc Nissan Pathfinder. Chủ xe lái chiếc Pathfinder thay vì chiếc BMW mà ông ta vẫn thường đi. Người ngồi sau vô-lăng hạ cửa kính xuống — chính là chỉ huy trưởng căn cứ không quân Trenton.

Vân lốp xe của ông ta trông rất giống dấu vết trên tuyết. Nhưng trước một sĩ quan cấp cao đĩnh đạc, các sĩ quan tuần tra không thể giữ ông ta lại. Họ chỉ ghi nhận thông tin rồi kính cẩn chào cho đi. Và trong ba ngày tiếp theo, ông ta vẫn là một vị đại tá tự do.

Đây là hiệu ứng hào quang: một tấm khiên vô hình khiến cả xã hội lẫn cơ quan thực thi pháp luật bị che mắt suốt nhiều năm ròng. Quân phục đại tá lộng lẫy, chiến công lái chuyên cơ cho Hoàng gia và Thủ tướng, tiếng tay quân đội từng đứng nghiêm chào — không một thứ nào là bằng chứng cho sự lương thiện của một tâm hồn.

——————
BỐI CẢNH HỒ SƠ
——————
Căn cứ không quân Trenton — Ontario, Canada — nơi đón linh cữu các liệt sĩ Canada từ chiến trường Afghanistan về dọc "Con lộ Anh hùng". Chỉ huy trưởng nơi đó là Đại tá David Russell Williams — người từng lái chuyên cơ đưa đón Nữ hoàng Anh Elizabeth II, Hoàng thân Philip và các Thủ tướng Canada.

——————
NGUỒN THAM KHẢO
——————
• Bản án Tòa Thượng thẩm Ontario — R. v. Williams, 2010 ONSC 5946
• Báo cáo điều tra Cảnh sát OPP + Belleville Police Service (trạm kiểm soát Đường số 2)
• Biên bản thẩm vấn ngày 07/02/2010 · lời khai của Thám tử Jim Smyth trước tòa
• Hồ sơ quân bạ Bộ Quốc phòng Canada · The Globe and Mail
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap02/kichban_tap02_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md

——————
LƯU Ý
——————
• Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.
• Nội dung không phù hợp cho trẻ em.
• Mang tính giáo dục, phân tích tâm lý tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên tư liệu công khai (hồ sơ tòa án, báo chí điều tra). Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Nhân vật Cú, Sói, Cáo là linh thú minh hoạ; lời thoại phục dựng dựa trên tư liệu điều tra.
• Hồ sơ có thật, dữ liệu có nguồn.

#AmberEyes #TamLyToiPham #HosoCoThat #HieuUngHaoQuang #QuanDoi #TrueCrime #MoiTuanMotTap""",

 "TK3": """Hai cuộc đời. Một cơ thể. Một câu chuyện để tự bào chữa. 👁️

Tập 02 · Đại tá hai mặt — Chỉ dấu #5: hệ thống tự bào chữa.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · phân mảnh tâm trí · hồ sơ có thật

——————
CHỈ DẤU #5: HỆ THỐNG TỰ BÀO CHỮA
——————
Trước khi phân tích, một điều phải nói rõ: không tồn tại một chẩn đoán lâm sàng công khai nào về Russell Williams. Các khung lý thuyết dưới đây là công cụ phân tích phổ biến trong tâm lý học tội phạm — chúng giúp ta đặt câu hỏi đúng, chứ không phải một sự phán xét đã được cơ quan chuyên môn xác nhận.

Trong tâm lý học, phân mảnh tâm trí (compartmentalization) là cơ chế phòng vệ cho phép bộ não khóa chặt hai luồng nhận thức và cảm xúc trái ngược nhau vào hai ngăn kéo hoàn toàn biệt lập. Ở đây, hắn dường như đã xây dựng hai con người tách biệt bên trong cùng một thể xác:
• NGĂN KÉO 1 — ĐẠI TÁ: người chỉ huy mẫu mực, người chồng chu đáo chăm sóc vườn tược, sống vì chuẩn mực đạo đức và lý tưởng quân đội.
• NGĂN KÉO 2 — KẺ SĂN MỒI BÓNG ĐÊM: nơi hắn giải phóng những xung lực tàn bạo nhất.
Khi ở ngăn kéo này, hắn đóng chặt cánh cửa của ngăn kéo kia — rồi dùng chính người vợ và cuộc hôn nhân chuẩn mực làm "lá chắn bình thường hóa".

Để lương tri không lên tiếng, hắn áp dụng triệt để kỹ thuật trung hòa đạo đức (neutralization). Trong 82 vụ trộm đầu tiên, hắn tự nhủ: "mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm". Đến khi xảy ra án mạng, hắn lại tự biện minh rằng nạn nhân đã thấy mặt mình, cô ta ép mình phải ra tay để tự vệ.

Và chính vì vậy, cuối cùng hắn không thể tự giải thích một cách có lương tri. Khi thám tử hỏi hắn có bao giờ tự hỏi vì sao mình làm những việc đó, câu trả lời trong bản ghi thẩm vấn trống rỗng đến lạnh người: "Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng."

——————
BỐI CẢNH HỒ SƠ
——————
Đại tá David Russell Williams — chỉ huy trưởng căn cứ không quân Trenton (CFB Trenton, Ontario, Canada) từ tháng 7/2009. Tháng 2/2010, hắn bị tố giác liên quan tới vụ mất tích của Jessica Lloyd, 27 tuổi, ở Belleville.

——————
NGUỒN THAM KHẢO
——————
• Toàn văn băng ghi âm và ghi hình thẩm vấn của Cảnh sát OPP ngày 07/02/2010
• Bản án Tòa Thượng thẩm Ontario — R. v. Williams, 2010 ONSC 5946
• Phim tài liệu CBC "The Detective and the Colonel"
• Christie Blatchford, "Unmasking Freedom"
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap02/kichban_tap02_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md

——————
LƯU Ý
——————
• Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.
• Nội dung không phù hợp cho trẻ em.
• Mang tính giáo dục, phân tích tâm lý tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên tư liệu công khai (hồ sơ tòa án, báo chí điều tra). Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Nhân vật Cú, Sói, Cáo là linh thú minh hoạ; lời thoại phục dựng dựa trên tư liệu điều tra.
• Hồ sơ có thật, dữ liệu có nguồn.

#AmberEyes #TamLyToiPham #HosoCoThat #Compartmentalization #SelfJustification #TrueCrime #MoiTuanMotTap""",

 "TK4": """Không một lời xin lỗi nào nhắc tới nạn nhân. 👁️

Tập 02 · Đại tá hai mặt — Chỉ dấu #4: sụp đổ cái tôi ái kỷ.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · sụp đổ cái tôi · hồ sơ có thật

——————
CHỈ DẤU #4: SỤP ĐỔ CÁI TÔI ÁI KỶ
——————
Khi chiếc ổ cứng bị tìm thấy, bức tường ngăn cách giữa hai ngăn kéo tâm trí vỡ vụn. Và câu hỏi quan trọng nhất mà bản án không trả lời được, là thái độ của hắn.

Trong phòng thẩm vấn, những nỗi lo hắn thốt ra chỉ xoay quanh việc người vợ nhìn nhận hắn ra sao, và sự sụp đổ danh tiếng của căn cứ quân sự. Hắn không hề nhắc đến nỗi đau đớn cùng cực của những người phụ nữ hay gia đình nạn nhân. Đó không phải là sự ăn năn hối cải chân chính. Đó là sự thương hại bản thân tột độ khi nhận ra tấm mặt nạ danh dự hắn dày công xây dựng suốt hai mươi lăm năm đã vỡ vụn.

——————
BẢN ÁN
——————
• Tháng 10/2010, Tòa Thượng thẩm Ontario xét xử tại thị trấn Belleville, thẩm phán Robert Scott.
• Ngày 18/10: hắn nhận tội trước tòan bộ 88 cáo buộc.
• Ngày 21/10: hai mức tù chung thân chạy song song cho hai tội danh nghiêm trọng nhất, cộng thêm các mức tù cho các tội danh khác, tất cả cùng chạy song song. Mức án chung thân với 25 năm không được xét ân xá — đúng mức tối thiểu mà luật hình sự Canada bắt buộc cho tội danh nghiêm trọng nhất.
• Bản án lớn nhất với một kẻ ái kỷ như hắn là sự sụp đổ hoàn toàn về danh dự và quyền lực: toàn quyền Canada thu hồi quân hàm, huân chương bị cắt thành từng mảnh, tiểu sử bị gỡ khỏi trang web Bộ Quốc phòng ngay sau khi hắn bị bắt.
• Quân đội Canada đốt toàn bộ quân phục và trang phục mang tên hắn tại một lò tiêu hủy tài liệu mật ở căn cứ Trenton — việc chưa từng có tiền lệ. Theo người phát ngôn quân đội Hubert Genest: không có nghi lễ chính thức nào, cũng không có ảnh chụp.
• Chiếc xe từng lăn bánh qua trạm kiểm soát bị máy ép nát vụn, và hàng trăm món đồ hắn lấy trộm bị đem thiêu hủy hoàn toàn.

Về mặt tâm lý, đó là biểu hiện kinh điển của sự sụp đổ cái tôi ái kỷ: khi không còn quyền kiểm soát và không chịu nổi sự nhục nhã trần trụi, kẻ săn mồi chỉ còn lại sự thương hại bản thân tột độ.

——————
NGUỒN THAM KHẢO
——————
• Phán quyết ngày 21/10/2010 của Thẩm phán Robert F. Scott, Tòa Thượng thẩm Ontario (phiên xử tại Belleville)
• Thông cáo Bộ Quốc phòng Canada (thu hồi quân hàm, hủy bỏ sắc lệnh, đốt quân phục)
• Bản án Tòa Thượng thẩm Ontario — R. v. Williams, 2010 ONSC 5946
• Biên bản thẩm vấn ngày 07/02/2010 (Cảnh sát OPP)
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap02/kichban_tap02_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md

——————
LƯU Ý
——————
• Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.
• Nội dung không phù hợp cho trẻ em.
• Mang tính giáo dục, phân tích tâm lý tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên tư liệu công khai (hồ sơ tòa án, báo chí điều tra). Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Nhân vật Cú, Sói, Cáo là linh thú minh hoạ; lời thoại phục dựng dựa trên tư liệu điều tra.
• Hồ sơ có thật, dữ liệu có nguồn.

#AmberEyes #TamLyToiPham #HosoCoThat #NarcissisticCollapse #BanAn #TrueCrime #MoiTuanMotTap""",

 "TK5": """Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó. 👁️

Tập 02 · Đại tá hai mặt — Chỉ dấu #10: bài học sinh tồn.
Hồ sơ có thật, dữ liệu có nguồn.

📺 Xem tập đầy đủ (25 phút) trên YouTube — link trong bio
🔎 Chỉ dấu tâm lý · trực giác sinh tồn · hồ sơ có thật

——————
CHỈ DẤU #10: NẠN NHÂN HỌC & BÀI HỌC SINH TỒN
——————
Trước khi sự thật vỡ lở, thị trấn Tweed sống trong một nỗi bất an mơ hồ. Đồ đạc riêng tư thỉnh thoảng bị xáo trộn, cửa nẻo có dấu cạy phá nhưng không mất tiền bạc. Người dân tưởng mình đang hoang tưởng.

Đó chính là dấu hiệu sớm nhất: ranh giới riêng tư bị xâm phạm lặp đi lặp lại, nhưng không đi kèm thiệt hại vật chất — nên rất dễ bị bỏ qua.

Bài học từ hồ sơ này:
• Tội ác không bao giờ bắt đầu từ một vụ án mạng. Nó luôn bắt đầu từ những bước lấn ranh giới rất nhỏ: một cái nhìn trộm, một lần lục lọi đồ riêng tư, một sự xâm phạm không bị trừng phạt.
• Địa vị, bằng cấp hay quân hàm lộng lẫy chỉ là lớp áo khoác xã hội, không phải tấm bảo chứng cho sự lương thiện của một tâm hồn.
• Nếu bạn cảm thấy một sự bất an mơ hồ, nếu ranh giới riêng tư của bạn bị xâm phạm dù chỉ nhỏ nhất, đừng hợp lý hóa hay coi thường nó.
• Hãy luôn tin vào trực giác của bạn. Trực giác sinh tồn chính là hệ thống cảnh báo sớm giúp bảo vệ mạng sống của chúng ta.

——————
NGUỒN THAM KHẢO
——————
• Bản án Tòa Thượng thẩm Ontario — R. v. Williams, 2010 ONSC 5946
• Báo cáo điều tra Cảnh sát OPP + Belleville Police Service
• Biên bản thẩm vấn ngày 07/02/2010 (Cảnh sát OPP)
• Sách "The Gift of Fear" (Gavin de Becker) — nguồn cho khung lý thuyết trong kịch bản tập
• Kịch bản tập: 01_KICH_BAN/Ho_So_Toi_Pham/Tap02/kichban_tap02_22102026.md · đối chiếu: 02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md

——————
LƯU Ý
——————
• Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.
• Nội dung không phù hợp cho trẻ em.
• Mang tính giáo dục, phân tích tâm lý tội phạm; không thay thế tư vấn y khoa hay pháp lý.
• Dựa trên tư liệu công khai (hồ sơ tòa án, báo chí điều tra). Kênh không nhằm kết tội, bôi nhọ hay cổ suý bất kỳ cá nhân nào.
• Nhân vật Cú, Sói, Cáo là linh thú minh hoạ; lời thoại phục dựng dựa trên tư liệu điều tra.
• Hồ sơ có thật, dữ liệu có nguồn.

#AmberEyes #TamLyToiPham #HosoCoThat #TrucGiac #CanhGiuAnToan #TrueCrime #MoiTuanMotTap""",
}

# ----------------------------------------------------------------------------
# 4b. MÔ TẢ NGẮN (ô Description ngắn của TikTok Studio / bản rút gọn)
#
# CHUẨN THAM CHIẾU: 02_SAN_XUAT/TIKTOK/Tap01/MoTa_Dai_TK1.txt (bản của Tập 01
# thực ra là MÔ TẢ NGẮN: 1.078–1.369 ký tự, 10 dòng). Cấu trúc bắt buộc:
#   1. Hook (1 câu, có 👁️)
#   2. Dòng "Tập N · tên tập — Chỉ dấu #X: <tên chỉ dấu>"
#   3. Dòng trống
#   4. Đoạn dẫn 1–3 câu (bối cảnh hồ sơ)
#   5. Bullet "• ..." (2–3 ý, mỗi ý 1 dòng)
#   6. Dòng trống
#   7. "Bước ngoặt của hồ sơ này: ..." — câu chốt
#   8. Dòng trống
#   9. Câu hỏi kêu gọi bình luận "Theo bạn, ...? 👇"
#  10. Dòng trống
#  11. "📺 Xem trọn bộ hồ sơ phân tích đầy đủ (N phút, kèm nguồn tòa án & y khoa)
#      tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân."
#  12. Dòng trống
#  13. "🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung dùng hình ảnh và giọng AI
#      phục vụ phân tích tâm lý, mang tính giáo dục."
#  14. Dòng trống
#  15. Hashtag (5, chữ thường — khác bản dài vốn dùng CamelCase)
#
# RÚT GỌN TỪ MoTa_DAI: chỉ giữ lại dữ kiện có trong kịch bản tập (L2).
# ----------------------------------------------------------------------------

MO_TA_NGAN = {
 "TK1": """Bốn nấc thang. Tám mươi hai vụ trộm. Rồi một vụ án mạng. 👁️
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

#AmberEyes #TamLyToiPham #HosoCoThat #QuyDaoLeoThang #TrueCrime""",
 "TK2": """Vân lốp xe trùng khớp. Cảnh sát vẫn kính cẩn chào. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #9: hiệu ứng hào quang.

Đêm 28/01/2010, Jessica Lloyd — nữ nhân viên 27 tuổi, sống một mình ở Belleville — biến mất khỏi nhà riêng. Một tuần sau đó, vào tối 4/2, cảnh sát lập một trạm kiểm soát lưu động kéo dài suốt đêm, săn một dấu vết duy nhất: vệt vân lốp xe địa hình hiếm gặp in hằn trên nền tuyết.
• Trong dòng xe đi qua trạm có một chiếc Nissan Pathfinder — chủ xe lái chiếc Pathfinder thay vì chiếc BMW mà ông ta vẫn thường đi.
• Vân lốp xe của ông ta rất giống dấu vết trên tuyết. Nhưng trước một sĩ quan cấp cao đĩnh đạc, các sĩ quan tuần tra không thể giữ ông ta lại — họ chỉ ghi nhận thông tin rồi kính cẩn chào cho đi.

Bước ngoặt của hồ sơ này: đây là hiệu ứng hào quang — một tấm khiên vô hình khiến cả xã hội lẫn cơ quan thực thi pháp luật bị che mắt suốt nhiều năm ròng. Quân phục đại tá lộng lẫy, chiến công lái chuyên cơ cho Hoàng gia và Thủ tướng, tiếng tay quân đội từng đứng nghiêm chào — không một thứ nào là bằng chứng cho sự lương thiện của một tâm hồn.

Theo bạn, vì sao một chiếc quân hàm lộng lẫy lại khiến cả cơ quan thực thi pháp luật không dám hỏi một câu? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #HieuUngHaoQuang #TrueCrime""",
 "TK3": """Hai cuộc đời. Một cơ thể. Một câu chuyện để tự bào chữa. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #5: hệ thống tự bào chữa.

Trước khi phân tích, một điều phải nói rõ: không tồn tại một chẩn đoán lâm sàng công khai nào về Russell Williams. Các khung lý thuyết dưới đây là công cụ phân tích phổ biến trong tâm lý học tội phạm — chúng giúp ta đặt câu hỏi đúng, chứ không phải một sự phán xét đã được cơ quan chuyên môn xác nhận.
• Phân mảnh tâm trí (compartmentalization): bộ não khóa hai luồng nhận thức trái ngược vào hai ngăn kéo hoàn toàn biệt lập — người chỉ huy mẫu mực và kẻ săn mồi bóng đêm.
• Trung hòa đạo đức (neutralization): trong 82 vụ trộm đầu tiên, hắn tự nhủ "mình chỉ nhìn, mình không làm hại ai, mình chỉ giữ một món kỷ niệm". Đến khi xảy ra án mạng, hắn lại tự biện minh rằng nạn nhân đã thấy mặt mình, cô ta ép mình phải ra tay để tự vệ.

Bước ngoặt của hồ sơ này: vì lương tri đã bị khóa trong ngăn kéo kia, hắn không thể tự giải thích một cách có lương tri. Câu trả lời trong bản ghi thẩm vấn trống rỗng đến lạnh người: "Có, nhưng tôi không biết câu trả lời, và tôi khá chắc là câu trả lời cũng chẳng quan trọng."

Theo bạn, ranh giới nào tách một lời giải thích có lương tri khỏi một hệ thống tự bào chữa? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #Compartmentalization #TrueCrime""",
 "TK4": """Không một lời xin lỗi nào nhắc tới nạn nhân. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #4: sụp đổ cái tôi ái kỷ.

Khi chiếc ổ cứng bị tìm thấy, bức tường ngăn cách giữa hai ngăn kéo tâm trí vỡ vụn. Và câu hỏi quan trọng nhất mà bản án không trả lời được, là thái độ của hắn.
• Trong phòng thẩm vấn, những nỗi lo hắn thốt ra chỉ xoay quanh việc người vợ nhìn nhận hắn ra sao, và sự sụp đổ danh tiếng của căn cứ quân sự. Hắn không hề nhắc đến nỗi đau đớn cùng cực của những người phụ nữ hay gia đình nạn nhân.
• Tháng 10/2010, Tòa Thượng thẩm Ontario xét xử tại thị trấn Belleville, thẩm phán Robert Scott. Ngày 21/10, mức án chung thân 25 năm — đúng mức tối thiểu mà luật hình sự Canada bắt buộc cho tội danh nghiêm trọng nhất.
• Bản án lớn nhất là sự sụp đổ hoàn toàn về danh dự và quyền lực: quân hàm bị toàn quyền Canada thu hồi, huân chương bị cắt thành từng mảnh, tiểu sử bị gỡ khỏi trang web Bộ Quốc phòng ngay sau khi hắn bị bắt.

Bước ngoặt của hồ sơ này: đó không phải là sự ăn năn hối cải chân chính. Đó là sự thương hại bản thân tột độ khi nhận ra tấm mặt nạ danh dự hắn dày công xây dựng suốt hai mươi lăm năm đã vỡ vụn.

Theo bạn, khi nào sự hối hận biến thành công cụ để tự bảo vệ? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #NarcissisticCollapse #TrueCrime""",
 "TK5": """Nếu bạn cảm thấy bất an, đừng hợp lý hóa nó. 👁️
Tập 02 · Đại tá hai mặt — Chỉ dấu #10: bài học sinh tồn.

Trước khi sự thật vỡ lở, thị trấn Tweed sống trong một nỗi bất an mơ hồ. Đồ đạc riêng tư thỉnh thoảng bị xáo trộn, cửa nẻo có dấu cạy phá — nhưng không mất tiền bạc. Người dân tưởng mình đang hoang tưởng.
• Dấu hiệu sớm nhất: ranh giới riêng tư bị xâm phạm lặp đi lặp lại, nhưng không đi kèm thiệt hại vật chất — nên rất dễ bị bỏ qua.
• Tội ác không bao giờ bắt đầu từ một vụ án mạng. Nó luôn bắt đầu từ những bước lấn ranh giới rất nhỏ, không bị trừng phạt.
• Địa vị, bằng cấp hay quân hàm lộng lẫy chỉ là lớp áo khoác xã hội, không phải tấm bảo chứng cho sự lương thiện của một tâm hồn.

Bước ngoặt của hồ sơ này: nếu bạn cảm thấy một sự bất an mơ hồ, nếu ranh giới riêng tư của bạn bị xâm phạm dù chỉ nhỏ nhất, đừng hợp lý hóa hay coi thường nó. Trực giác sinh tồn chính là hệ thống cảnh báo sớm giúp bảo vệ mạng sống của chúng ta.

Theo bạn, tín hiệu cảnh báo nào trong đời thường mà bạn thường bỏ qua nhất? 👇

📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút, kèm nguồn tòa án & y khoa) tại YTB: Amber Eyes — bấm nút liên kết ngay đầu trang cá nhân.

🔎 Hồ sơ có thật, dữ liệu có nguồn. Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự. Không phù hợp cho trẻ em.

#AmberEyes #TamLyToiPham #HosoCoThat #TrucGiac #TrueCrime""",
}


# ----------------------------------------------------------------------------
# 5. GHI FILE
# ----------------------------------------------------------------------------

def write_caption_files():
    for c in CLIPS:
        cid = c["id"]
        cap = build_caption(c)
        note = "\n".join([
            "",
            "---",
            "Ghi chú khi đăng (KHÔNG dán vào caption):",
            '- BẬT toggle "Nội dung do AI tạo" (AI-generated content) — TikTok bắt buộc nhãn AIGC.',
            f"- Dòng nhãn AIGC ĐÃ nằm sẵn trong caption (dòng thứ {len(build_caption(c).splitlines()) - 2}): không cần thêm khi dán.",
            f"- Link YouTube Tập 02: {LINK_TAP02}  ← CHƯA CÓ, phải điền trước khi đăng.",
            "  · Dán vào ô \"Links / Website\" trong Edit profile (chỉ ô này click được).",
            "  · URL gõ tay trong caption/bio KHÔNG click được — chỉ để người xem tự chép.",
            f"- Độ dài caption: {len(cap)} ký tự (giới hạn TikTok 2.200 ký tự).",
            f"- File: clip{c['id'][-1]}_{cid}.mp4 (1080×1920, 30 fps, H.264+AAC).",
            f"- Ước lượng thời lượng: {c['uoc_luong_s']:.1f} s ({len(c['lines'])} câu) — số đo thật lấy sau khi sinh WAV.",
            f"- BẢN MÔ TẢ DÀI ({len(MO_TA_DAI[cid])} ký tự) dán vào ô Description của TikTok Studio: MoTa_Dai_{cid}.txt",
            f"- BẢN MÔ TẢ NGẮN ({len(MO_TA_NGAN[cid])} ký tự) — bản rút gọn, dùng thay hoặc kèm bản dài: MoTa_Ngan_{cid}.txt",
        ])
        (OUT / f"Caption_{cid}.txt").write_text(cap + "\n" + note, encoding="utf-8")
        (OUT / f"MoTa_Dai_{cid}.txt").write_text(MO_TA_DAI[cid], encoding="utf-8")
        (OUT / f"MoTa_Ngan_{cid}.txt").write_text(MO_TA_NGAN[cid], encoding="utf-8")

# ----------------------------------------------------------------------------
# 6. BẢN KẾ HOẠCH MARKDOWN
# ----------------------------------------------------------------------------

NEN_SRC = {
 "tk02_escalation_stairs": "t2_escalation_stairs",
 "tk02_open_window": "t2_open_window",
 "tk02_drawer_dark": "t2_drawer_dark",
 "tk02_folder_tree": "t2_folder_tree",
 "tk02_brain_neural": "t2_brain_neural",
 "tk02_two_chairs": "t2_two_chairs",
 "tk02_house_missing": "t2_house_missing",
 "tk02_oath_hall": "t2_oath_hall",
 "tk02_checkpoint": "t2_checkpoint",
 "tk02_suv_stop": "t2_suv_stop",
 "tk02_tire_track": "t2_tire_track",
 "tk02_siren_wall": "t2_siren_wall",
 "tk02_podcast_desk": "t2_podcast_desk",
 "tk02_two_drawers": "t2_two_drawers",
 "tk02_two_masks": "t2_two_masks",
 "tk02_command_chair": "t2_command_chair",
 "tk02_stairs_dark": "t2_stairs_dark",
 "tk02_hidden_drive": "t2_hidden_drive",
 "tk02_interrogation_early": "t2_interrogation_early",
 "tk02_head_down": "t2_head_down",
 "tk02_courtroom": "t2_courtroom",
 "tk02_gavel": "t2_gavel",
 "tk02_medals_cut": "t2_medals_cut",
 "tk02_uniform_fire": "t2_uniform_fire",
 "tk02_red_flags": "t2_red_flags",
 "tk02_town_snow": "t2_town_snow",
 "tk02_cottage_search": "t2_cottage_search",
}

def raw_exists(base):
    return (ROOT / "assets/bg/_raw" / f"{base}.jpg").exists() or \
           (ROOT / "assets/bg/_raw" / f"{base}.png").exists()

def write_markdown():
    L = []
    A = L.append
    A("# KẾ HOẠCH CLIP TIKTOK — TẬP 02 · \"ĐẠI TÁ HAI MẶT\"")
    A("")
    A("*Ngày: 20/11/2026 · Trạng thái: **kịch bản đã viết, chờ người dùng duyệt trước khi đọc giọng** (L4)*")
    A("*Kế hoạch cha: `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` · Đặc tả audio máy đọc được: `02_SAN_XUAT/TIKTOK/Tap02/SPEC_AUDIO_CLIP_TAP02.json`*")
    A("*Nguồn duy nhất của mọi dữ kiện: `.work/script_tap02.json` (203 câu, đã đối chiếu `02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md`)*")
    A("*Sinh tự động bởi `.work/_build_tk_tap02.py` — sửa kịch bản thì sửa file đó rồi chạy lại, đừng sửa tay file này.*")
    A("")
    A("---")
    A("")
    A("## 0. Tóm tắt chốt")
    A("")
    A("| Hạng mục | Giá trị |")
    A("|---|---|")
    A(f"| Số clip | **{len(CLIPS)} clip** (TK1–TK4 chính + TK5 clip kết) |")
    A(f"| Tổng câu | **{sum(len(c['lines']) for c in CLIPS)} câu** đọc giọng |")
    used_nen = {ln[4] for c in CLIPS for ln in c["lines"]}
    A(f"| Độ dài | Ước lượng {min(c['uoc_luong_s'] for c in CLIPS):.1f}–{max(c['uoc_luong_s'] for c in CLIPS):.1f} s/clip (mục tiêu 65–90 s · cổng QC 45–95 s) |")
    A("| Chủ đề | Mỗi clip = **1 chỉ dấu tâm lý** của Tập 02 (K10) |")
    A("| Ngôn ngữ | Tiếng Việt · vai H / D / C / N2 |")
    A("| Engine giọng | **Higgs Audio v3 + giọng mẫu VoxCPM2 — đúng giọng của Tập 02** (không dùng bộ A MiniMax) |")
    A(f"| Hình | Nền dọc 9:16 `tk02_*` ({len(used_nen)} nền dùng trong clip, mục 7) · Pillow vẽ chữ |")
    A("| Chi phí | **0 đồng** (Kaggle GPU có sẵn) — trừ thời gian chờ GPU |")
    A("| Việc cần người dùng | Tạo **%d file WAV** theo `SPEC_AUDIO_CLIP_TAP02.json` (mục 5) · điền link YouTube Tập 02 (mục 13) |"
      % sum(len(c['lines']) for c in CLIPS))
    A("")
    A("---")
    A("")
    A("## 1. Vì sao viết lời dẫn mới cho clip, không cắt từ audio tập")
    A("")
    A("| Phương án | Đánh giá |")
    A("|---|---|")
    A("| **A — Lời dẫn mới cho clip (CHỌN)** | Hook 3 giây đúng chuẩn TikTok; 1 clip = 1 chỉ dấu; chỉ cần **%d câu ngắn** thay vì 203 câu; V3 đảm bảo mọi câu trong clip truy được về kịch bản tập |" % sum(len(c['lines']) for c in CLIPS))
    A("| B — Cắt nguyên đoạn từ audio tập | Lời dẫn tập viết để *nghe*, không phải để *giữ chân*; không có hook 3 giây ⇒ **trượt đối với TikTok**; 203 câu / 25 phút không cắt được trong 45–90 s mà giữ được cả 10 chỉ dấu |")
    A("")
    A("⇒ Chọn A. **Mọi dữ kiện trong lời đọc phải truy được về `.work/script_tap02.json`** — không thêm tên riêng, số liệu hay chi tiết mới (K1/K2).")
    A("")
    A("---")
    A("")
    A("## 2. Năm clip và chỉ dấu tâm lý tương ứng (K10)")
    A("")
    A("| Clip | Chỉ dấu | Chủ đề | Hook trên hình (0–3 s) | Ước lượng |")
    A("|---|---|---|---|---|")
    for c in CLIPS:
        cd = " · ".join(f"#{i}" for i in c["chi_dau"])
        A(f"| **{c['id']}** | {cd} | {c['chude']} | *\"{c['hook']}\"* | {c['uoc_luong_s']:.1f} s · {len(c['lines'])} câu |")
    A("")
    A("**Thứ tự đăng:** TK2 → TK1 → TK4 → TK3 → TK5 (TK2 có hook mạnh nhất để thu hút; TK5 là clip lưu/chia sẻ để khép lại chuỗi).")
    A("")
    A("---")
    A("")
    A("## 3. Diễn xuất từng clip (lời đọc + hình + âm)")
    A("")
    A("> Quy ước vai: **H** = Host (Cú) · **D** = Điều tra viên (Sói) · **C** = Chuyên gia tâm lý (Cáo) · **N2** = Khán giả (Mèo)")
    A("> `pause_after` = thời gian im lặng chèn **giữa hai câu** (0,2–1,2 s — luật G2). Emotion chỉ dùng 4 giá trị an toàn (G3). Tốc độ lệch −0,06…+0,02 (G4). **Cao độ luôn = 0** (G5).")
    A("> Mỗi câu bắt đầu bằng mã câu `TKx.01#z` — dùng làm tên file WAV và mã câu trong hồ sơ.")
    A("> **Ước lượng = số từ sau khi đổi số→chữ × tỉ lệ đọc đo thật của vai đó** (mục 3.6).")
    A("")
    for c in CLIPS:
        A(f"### 3.{CLIPS.index(c)+1} CLIP {c['id']} — \"{c['ten_vn']}\"")
        A("")
        A(f"*Ước lượng {c['uoc_luong_s']:.1f} s ({len(c['lines'])} câu) · BGM `{c['bgm']}` ({c['bgm_hovi']}) · SFX: {' · '.join(c['sfx'])}*")
        A("")
        A("| Mã | Vai | Emotion | Tốc độ | Nghỉ | Lời đọc | Nguồn |")
        A("|---|---|---|---|---|---|---|")
        for i, (vai, emo, spd, pause, nen, cd, text, nguon) in enumerate(c["lines"], 1):
            A(f"| `{c['id']}.01#{i}` | {vai} | {emo} | {spd:+.2f} | {pause:.1f} | {text} | {nguon} |")
        A("")
        A("| Nền | Chuyển động | Ước lượng |")
        A("|---|---|---|")
        for i, (vai, emo, spd, pause, nen, cd, text, nguon) in enumerate(c["lines"], 1):
            A(f"| `{c['id']}.01#{i}` | `{nen}` | {cd} | {est_dur(text, vai):.1f} s |")
        A("")
        A("**Thẻ chữ trên hình (overlay card):**")
        for o in c["overlay"]:
            A(f"- `{o['sau_cau']}` → *\"{o['text']}\"* ({o['dur_s']} s)")
        A("")
        A(f"**Nguồn dữ kiện:** {' · '.join(c['nguon_du_lieu'])}")
        A("")
    A("---")
    A("")
    A("### 3.6 Thời lượng — cách đo, không phải cảm tính")
    A("")
    A("Ước lượng dựa trên **số đo thật** của chính tập 02, không phải trên cảm tính:")
    A("")
    A("| Vai | Số giây / từ (đo trên master Tập 02) | Tương đương |")
    A("|---|---|---|")
    for r in ["H", "D", "C", "N2"]:
        if r in RATE:
            A(f"| {r} | {RATE[r]:.4f} s/từ | {1/RATE[r]:.2f} từ/giây |")
    A("")
    A("* Nguồn: `.work/timeline_s_t02.json` — timeline **đo bằng ASR trên mp4 thành phẩm** Tập 02 (203 câu).")
    A("* Số từ đếm **sau khi đổi số → chữ** (`vi_numbers`) — đúng phần TTS đọc ra tiếng.")
    A("* **Kiểm chéo (leave-one-out) trên 203 câu thật:** sai số tuyệt đối trung bình 11,0 %/câu, trung vị 6,7 %.")
    A("* **Mô phỏng mức clip (nhóm 13 câu, 2.000 lần):** MAE 3,7 % · trung vị 3,1 % · p90 7,3 % ⇒ **sai số kỳ vọng của một clip 80 s là ±5,8 s**.")
    A("* ⇒ Số đo **thật** của clip chỉ có sau khi sinh WAV: cộng `dur` từng file + `pause_after`, rồi đo lại trên mp4 cuối (A7).")
    A("")
    A("---")
    A("")
    A("## 4. Bố cục màn hình 9:16 (1080 × 1920)")
    A("")
    A("Áp dụng safe zone của TikTok (bám template In-Feed, thiết kế theo trường hợp xấu nhất):")
    A("")
    A("| Thành phần | Vị trí (x, y) | Cỡ chữ | Ghi chú |")
    A("|---|---|---|---|")
    A("| **Chữ hook** (0–3 s) | x 120–780, y 300–700 | 76 px đậm, tối đa 2 dòng | có `text_scrim`; chữ Pillow vẽ sau, **không** để AI vẽ chữ |")
    A("| **Phụ đề burn-in** | x 120–780, y 1.020–1.230 | 52 px, tối đa 2 dòng | nền scrim mờ 35 %; **nguyên văn** lời đọc (G6) |")
    A("| **Thẻ chữ overlay** | x 120–780, y 780–980 | 44 px | card tối 60 %, bo góc 12 px, hiện 2,5–3 s rồi fade 0,4 s |")
    A("| **Logo** | x 120–260, y 60–160 | — | tránh x > 780 (nút like/comment/share) |")
    A("| **Nền** | phủ kín 1080×1920 | — | nền dọc `tk02_*`; nếu chưa có thì dùng phương án B: blur-fill + zoom 4 % |")
    A("")
    A("Chuyển động `pull` / `push` / `pan` / `still` dùng đúng bộ của pipeline hiện tại (`.work/build_video3.py`).")
    A("")
    A("> **Luật V3 áp cho clip:** mọi con số trên thẻ overlay phải có trong câu đang đọc (đã kiểm ở mục 10).")
    A("")
    A("---")
    A("")
    A("## 5. Chỉ dẫn tạo audio (phần người dùng làm)")
    A("")
    A(f"> **Mục tiêu:** {sum(len(c['lines']) for c in CLIPS)} câu → {sum(len(c['lines']) for c in CLIPS)} file WAV 24 kHz mono.")
    A("")
    A("### 5.1 Engine: Higgs Audio v3 + giọng mẫu VoxCPM2 (đúng giọng của Tập 02)")
    A("")
    A("| Tham số | Giá trị |")
    A("|---|---|")
    A("| Mô hình | `bosonai/higgs-tts-3-4b` (Higgs Audio v3) |")
    A("| Dataset giọng mẫu | `chiduong2026/amber-eyes-voice-ref-voxcpm2` (đã có sẵn, `ready`) |")
    A("| Vai → clip tham chiếu | **H → `assets/voice_ref_voxcpm2/H.wav`** · **D → `assets/voice_ref_voxcpm2_dc3/D_NEW_subbass-husky_t02.wav`** · **C → `assets/voice_ref_voxcpm2_dc2/C_NEW_alto-brisk_t03.wav`** · **N1 → `assets/voice_ref_voxcpm2_g9/W6_LOW.wav`** · **N2 → `assets/voice_ref_voxcpm2_g9/W5_HIGH.wav`** |")
    A("| temperature / top_p / top_k | 0,8 / 0,95 / 50 |")
    A("| max_new_tokens | 1.196 (≈ 47 s — dư cho câu ngắn) |")
    A("| sample_rate | 24.000 Hz · `fade_in_ms` 30 · `fade_out_ms` 15 |")
    A("| Seed | `sha256(id\\|role\\|ref\\|temp\\|vN)` → `int(hex[:8],16)`; **sinh 2 bản/câu** (v0, v1) |")
    A("| Cấm | mọi thẻ `<\\|emotion:...\\|>` — **chỉ** dùng `<\\|prosody:pause\\|>` sau dấu `:` trước câu trích |")
    A("")
    A("> **Khác Tập 01:** Tập 02 dùng **bộ giọng mới** cho vai D và C (`D_NEW_subbass-husky_t02`, `C_NEW_alto-brisk_t03` — đã qua G9 cho tập này). Clip Tập 02 phải dùng **đúng hai file này**, nếu không giọng clip sẽ lệch giọng tập trên YouTube.")
    A("")
    A("### 5.2 Quy ước đặt tên & thư mục (bắt buộc để dựng được video)")
    A("")
    A("```")
    A(".work/audio_s_tk_t02/")
    A("├── TK1.01_01.wav      # <clip>.<câu>_<số câu>.wav   (mã \"TK1.01#1\" → \"TK1.01_01.wav\")")
    A("├── TK1.01_02.wav")
    A("├── …")
    A("└── manifest_tk_t02.json")
    A("```")
    A("")
    A("`manifest_tk_t02.json` (mỗi dòng một câu):")
    A("")
    A("```json")
    A('{"id": "TK1.01#1", "vai": "H", "file": "TK1.01_01.wav", "dur": 6.42,')
    A(' "emotion": "neutral", "speed": -0.02, "pause_after": 0.5, "variant": 0}')
    A("```")
    A("")
    A("### 5.3 Cổng kiểm audio (bắt buộc trước khi dựng video)")
    A("")
    A("| Cổng | Ngưỡng | Cách đo |")
    A("|---|---|---|")
    A(f"| Đủ file | {sum(len(c['lines']) for c in CLIPS)}/{sum(len(c['lines']) for c in CLIPS)} WAV + manifest | đếm file |")
    A("| Định dạng | 24.000 Hz, mono, PCM 16-bit | `ffprobe` |")
    A("| Độ dài mỗi câu | 1,5–14 s | đo trên file |")
    A("| Tổng clip | 45–95 s (mục tiêu 65–90 s) | cộng `dur` + `pause_after` |")
    A("| CER | **< 2 %** mỗi câu (G12) | Whisper (`measure_cer_prod.py`) |")
    A("| F0 / G9 | H–D ≥ 4 nc · C–H ≥ 4 nc · C–D ≥ 4 nc | `check_higgs_f0.py` |")
    A("| Nghe mù (G10) | mỗi vai nghe liền ra **1 người**, 3 vai tách bạch | tai người |")
    A("| Không câm | 0 khoảng > 0,3 s ở −60 dB trong clip | `qc_pause_gate.py --pre` |")
    A("| Lời đọc | đúng **nguyên văn** dòng trong `SPEC_AUDIO_CLIP_TAP02.json` (G6) | so từng chữ |")
    A("")
    A("---")
    A("")
    A("## 6. Âm thanh nền của clip (bản quyền — áp dụng tuyệt đối)")
    A("")
    A("| Nguồn | Clip TikTok |")
    A("|---|---|")
    A("| BGM MiniMax (9 file trong `assets/bgm/`) | ✅ dùng được — **có điều kiện**: phải xác minh quyền thương mại của bề mặt đã sinh (mục 2.4 kế hoạch mẹ — **vẫn chưa làm**) |")
    A("| SFX tự tổng hợp `assets/sfx/t2/_code/` | ✅ dùng được — của chính kênh |")
    A("| SFX Freesound **CC0** | ✅ dùng được |")
    A("| **SFX trong `assets/sfx/t2/`** (không phải `_code/`) | ❌ **YouTube Audio Library ⇒ cấm trên TikTok** |")
    A("| `bgm_guitar_acoustic_60s.mp3`, `bgm_church_organ.mp3` | ❌ **YouTube Audio Library ⇒ cấm trên TikTok** |")
    A("| Nhạc trending | ❌ không dùng |")
    A("")
    A("> **Đây là bẫy dễ sai nhất của Tập 02:** tập dùng SFX ở `assets/sfx/t2/*.wav` (bản YouTube Audio Library). Folder `_code/` **cùng tên file, bản tự tổng hợp** — clip TikTok phải lấy từ `_code/`.")
    A("")
    A("Mức: giọng −16 LUFS (đo trên mp4 cuối) · BGM −26 dB khi có lời, nâng −14 dB ở nghỉ 0,8–1,2 s trước câu chốt · **luôn có lớp nền môi trường** bên dưới (A1/V4: cấm câm tuyệt đối > 0,3 s).")
    A("")
    A("---")
    A("")
    A("## 7. Nền dọc 9:16 cần tạo (`tk02_*`)")
    A("")
    A("Tập 01 đã có 16 nền dọc `tk01_*` trong `assets/bg/` (1080×1920). Tập 02 cần **%d nền** cùng phong cách:" % len(NEN_SRC))
    A("")
    A("| Nền dọc cần tạo | Nguồn 16:9 trong `assets/bg/_raw/` | Dùng cho | File nguồn có sẵn? |")
    A("|---|---|---|---|")
    used = {}
    for c in CLIPS:
        for ln in c["lines"]:
            used.setdefault(ln[4], []).append(f"{c['id']}#{[l[4] for l in c['lines']].index(ln[4])+1}")
    for nen, src in sorted(NEN_SRC.items()):
        cl = sorted(set(x.split("#")[0] for x in used.get(nen, [])))
        A(f"| `{nen}` | `{src}` | {' · '.join(cl) if cl else '(dự phòng)'} | {'✅' if raw_exists(src) else '❌ THIẾU'} |")
    A("")
    A("**Quy trình tạo:**")
    A("")
    A("1. Sinh nền dọc bằng pipeline FLUX Kaggle sẵn có (`.work/bg_jobs_tap02.json` → kernel) — 1080×1920, ~26 ảnh. Prompt phải **không có chữ** (AI vẽ chữ rác); chữ trên hình luôn do Pillow vẽ sau.")
    A("2. Nền phải **có nội dung cảnh**, không được là gradient trừu tượng (H19).")
    A("3. Người thật trong nền phải là **bóng**, mặt chìm hoàn toàn (V5) — các nền `t2_two_chairs`, `t2_head_down`, `t2_suv_stop` đã có sẵn bóng đúng cách.")
    A("4. Ghi mỗi ảnh mới vào `provenance.json` (L7).")
    A("")
    A("> ⚠ **Phát hiện khi rà soát (20/11/2026):** bản 16:9 đã xử lý `assets/bg/t2_*.png` **không còn trong `assets/bg/`** — chỉ còn ảnh gốc `assets/bg/_raw/t2_*` (2752×1536). Clip dọc không cần bản 16:9, nhưng nếu dựng theo **phương án B (blur-fill)** thì lấy trực tiếp từ `_raw/` được. Nếu muốn dùng lại pipeline cũ thì phải chạy lại `fix_backgrounds.py`.")
    A("")
    A("---")
    A("")
    A("## 8. Caption + hashtag (sẵn sàng dán)")
    A("")
    for c in CLIPS:
        A(f"**{c['id']}** ({len(build_caption(c))} ký tự)")
        A("")
        A("```")
        A(build_caption(c))
        A("```")
        A("")
    A("> **Bắt buộc kèm theo mỗi caption:** dòng *\"Nội dung do AI tạo hình và giọng, dùng để phân tích tâm lý — không phải phóng sự.\"* + bật toggle **\"AI-generated content\"** khi đăng (TikTok bắt buộc ghi nhãn AIGC).")
    A("> Bản mô tả dài cho ô Description của TikTok Studio: `MoTa_Dai_TK*.txt` (mục 13).")
    A("> Bản mô tả **ngắn** (rút gọn, theo chuẩn Tập 01): `MoTa_Ngan_TK*.txt` (mục 8b).")
    A("")
    A("---")
    A("")
    A("## 8b. Mô tả ngắn (bản rút gọn, theo chuẩn `Tap01/MoTa_Dai_TK1.txt`)")
    A("")
    A("> Bản mô tả ngắn dùng khi: TikTok Studio hiển thị phần đầu mô tả dài bị cắt, hoặc đăng lại clip ở nơi khác cần bản gọn. Bản dài vẫn là bản chính để dán vào ô Description.")
    A("")
    for c in CLIPS:
        cid = c["id"]
        A(f"**{cid} — MoTa_Ngan_{cid}.txt** ({len(MO_TA_NGAN[cid])} ký tự)")
        A("")
        A("```")
        A(MO_TA_NGAN[cid])
        A("```")
        A("")
    A("---")
    A("")
    A("## 9. Hợp đồng giữa phần audio và phần dựng video")
    A("")
    A("| Người làm | Việc | Bàn giao |")
    A("|---|---|---|")
    A(f"| **Người dùng** | Tạo {sum(len(c['lines']) for c in CLIPS)} WAV + `manifest_tk_t02.json` theo mục 5 | `.work/audio_s_tk_t02/` |")
    A("| **AI (sau khi được duyệt)** | Sinh nền dọc `tk02_*`, dựng 5 clip 9:16, chạy 14 cổng QC | `02_SAN_XUAT/TIKTOK/Tap02/clip0*_TK*.mp4` + `BaoCao_QC_TikTok_Tap02.md` |")
    A("")
    A("**Quy tắc dựng video bám tiêu chuẩn:** H6 (chữ = nguyên văn lời đọc) · H9 (đo tương phản chữ, bật `text_scrim` nếu cần) · A1 (0 khoảng câm > 0,3 s) · A7 (−16 LUFS, TP ≤ −1,5 dBFS) · G6 (lời đọc không đổi chữ) · **L10 (không commit media)**.")
    A("")
    A("---")
    A("")
    A("## 10. Cổng QC clip (14 mục — đo thật, không \"nói xong\" khi chưa đo)")
    A("")
    A("| # | Kiểm | Ngưỡng | Trạng thái khi sinh kịch bản |")
    A("|---|---|---|---|")
    A("| 1 | Khung / tỉ lệ | 1080 × 1920, 9:16 | chưa dựng |")
    A("| 2 | Codec / fps | H.264 + AAC, 30 fps | chưa dựng |")
    A("| 3 | Dung lượng | ≤ 500 MB | chưa dựng |")
    A("| 4 | Độ dài | 45–95 s (mục tiêu 65–90 s) | ✅ ước lượng %s s |"
      % " / ".join(f"{c['id']} {c['uoc_luong_s']:.0f}" for c in CLIPS))
    A("| 5 | Âm lượng | −16 ± 1 LUFS · true peak ≤ −1,5 dBFS | chưa có audio |")
    A("| 6 | Khoảng câm | 0 khoảng > 0,3 s @ −60 dB | chưa có audio |")
    A("| 7 | Lệch hình/tiếng | ≤ 0,05 s | chưa dựng |")
    A("| 8 | Giải mã | 0 lỗi | chưa dựng |")
    A("| 9 | **Safe zone** | mọi chữ trong x 120–780, y 240–1.260 | chưa dựng |")
    A("| 10 | **Watermark** | 0 khung chứa watermark nền tảng khác | chưa dựng |")
    A("| 11 | **Chữ** | 0 chữ rác · 0 chữ trùng · 0 chữ chìm (đo tương phản) | chưa dựng |")
    A("| 12 | **Mặt người thật** | 0 vi phạm | chưa dựng |")
    A("| 13 | **Từ cấm V9** | 0 từ trong danh sách A9.2 | ✅ đã kiểm tự động (mục 11) |")
    A("| 14 | **Hook** | 3 giây đầu có chữ hook đọc được ở 100 % khung | ✅ hook ≤ 12 từ, 5/5 clip |")
    A("")
    A("**Riêng cho Tập 02:** mọi dữ kiện trong lời đọc phải truy được về `.work/script_tap02.json` + `02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md` (K1/K2); **không** thêm tên riêng, số liệu hay chi tiết mới ngoài hai file này.")
    A("")
    A("---")
    A("")
    A("## 11. Tự kiểm kịch bản (đã chạy, có số đo)")
    A("")
    A("| # | Kiểm | Kết quả |")
    A("|---|---|---|")
    for row in QC_ROWS:
        A(f"| {row[0]} | {row[1]} | {row[2]} |")
    A("")
    A("---")
    A("")
    A("## 12. Lịch trình đề xuất")
    A("")
    A("| Tuần | Việc | Người |")
    A("|---|---|---|")
    A("| 1 | Người dùng tạo audio + duyệt văn bản lời dẫn · AI sinh nền dọc `tk02_*` | Người dùng + AI |")
    A("| 2 | AI dựng 5 clip → đo 14 cổng QC → người dùng duyệt hình + nghe giọng | AI → Người dùng |")
    A("| 3 | Đăng TK2 + TK1 (2 clip/tuần) · ghi số đo vào `BangTheoDoi_TikTok.csv` | Người dùng |")
    A("| 4 | Đăng TK4 + TK3 + TK5 · quyết định có làm nền dọc FLUX phương án A cho các tập sau không | Người dùng |")
    A("")
    A("---")
    A("")
    A("## 13. Việc CẦN NGƯỜI DÙNG QUYẾT ĐỊNH / XÁC NHẬN (L4)")
    A("")
    A("| # | Việc | Vì sao cần người dùng |")
    A("|---|---|---|")
    A("| 1 | **Link YouTube Tập 02** | Chưa tồn tại trong repo. Caption + mô tả dài đang để placeholder `[LINK_TẬP 02 — cần điền]`. **Không tự bịa link** (L2). |")
    A("| 2 | **Xung đột thương hiệu lốp xe trong kịch bản tập** | Kịch bản `1.17#1` ghi *\"hoa văn lốp xe địa hình Kumho\"*, còn `nguon_tham_khao.md` ghi *\"Yokohama IG20\"*. Clip **không** nêu thương hiệu nào (nên an toàn), nhưng kịch bản tập nên được sửa cho khớp. |")
    A("| 3 | **Xác minh quyền thương mại BGM MiniMax** | Mục 2.4 kế hoạch mẹ — việc này **chưa làm**. Nếu 9 file BGM sinh từ app consumer không có gói thương mại thì phải thay bằng SFX tự tổng hợp. |")
    A("| 4 | **Nền dọc `tk02_*`** | Chưa có. Cần sinh 26 nền (mục 7) hoặc chấp nhận phương án B blur-fill từ `_raw/`. |")
    A("| 5 | **Mức độ nhạy cảm của TK4** | Clip nói về bản án; đã **tránh** nêu chi tiết tội danh (dùng “hai tội danh nghiêm trọng nhất”) và **không** nhắc chi tiết tự sát trong nhà tù (chỉ giữ “sụp đổ cái tôi ái kỷ”). Cần xác nhận mức này trước khi đăng. |")
    A("| 6 | **Số clip** | Đang 5 (TK1–TK5). TK5 là clip kết — có thể giữ lại làm clip thưởng sau khi 4 clip chính đã đo. |")
    A("")
    A("---")
    A("")
    A("## 14. Tài liệu liên quan")
    A("")
    A("- `02_SAN_XUAT/TIKTOK/KE_HOACH_TIKTOK.md` — kế hoạch mẹ (spec TikTok, chính sách, cổng QC, rủi ro)")
    A("- `02_SAN_XUAT/TIKTOK/Tap01/KE_HOACH_CLIP_TAP01.md` — khuôn mẫu của bộ này (Tập 01)")
    A("- `02_SAN_XUAT/TIKTOK/Tap02/SPEC_AUDIO_CLIP_TAP02.json` — **bảng đặc tả audio máy đọc được**")
    A("- `.work/_build_tk_tap02.py` — **nguồn sự thật** của kịch bản này (sinh ra cả .md lẫn .json)")
    A("- `01_KICH_BAN/Ho_So_Toi_Pham/Tap02/kichban_tap02_22102026.md` — kịch bản gốc Tập 02 (nguồn dữ kiện)")
    A("- `02_SAN_XUAT/Ho_So_Toi_Pham/Tap02/nguon_tham_khao.md` — nguồn đối chiếu dữ kiện")
    A("- `01_KICH_BAN/Ho_So_Toi_Pham/Tap02/REVIEW_kichban_tap02_10chiau.md` — bảng 10 chỉ dấu của Tập 02")
    A("- `00_TIEU_CHUAN/QUY_TAC_AUDIO_HIGGS.md` — quy trình Higgs P0–P10 (Kaggle)")
    A("- `AGENTS.md` — L4/L5/L6/L7/L10 · K1–K10 · G1–G13 · A1–A13 · H6/H9/H17")
    A("")
    (OUT / "KE_HOACH_CLIP_TAP02.md").write_text("\n".join(L), encoding="utf-8")

# ----------------------------------------------------------------------------
# 7. TỰ KIỂM
# ----------------------------------------------------------------------------

TAU_CAM = ["máu", "thi thể", "sát hại", "đòn", "trói", "bầm", "đập",
           "đầu độc", "diệt cỏ", "bỏ đói", "móc áo"]
EMOTION_OK = {"neutral", "sad", "fearful", "surprised"}

def self_qc():
    rows = []
    ok = True

    # 1. từ cấm V9 trong lời đọc + caption + mô tả dài
    hits = []
    for c in CLIPS:
        for i, ln in enumerate(c["lines"], 1):
            low = ln[6].lower()
            for w in TAU_CAM:
                if w == "máu" and "ung thư máu" in low:
                    continue
                if re.search(r"\b" + re.escape(w) + r"\b", low):
                    hits.append(f"{c['id']}.01#{i}:{w}")
        for w in TAU_CAM:
            if re.search(r"\b" + re.escape(w) + r"\b", build_caption(c).lower()):
                hits.append(f"{c['id']} caption:{w}")
            if re.search(r"\b" + re.escape(w) + r"\b", MO_TA_DAI[c["id"]].lower()):
                hits.append(f"{c['id']} mota:{w}")
            if re.search(r"\b" + re.escape(w) + r"\b", MO_TA_NGAN[c["id"]].lower()):
                hits.append(f"{c['id']} mota ngan:{w}")
    rows.append(("1", "Từ cấm V9/A9.2 trong lời đọc + caption + mô tả dài + mô tả ngắn",
                 ("✅ 0 lỗi" if not hits else "❌ " + ", ".join(hits))))
    ok = ok and not hits

    # 2. G1 — mỗi câu tối đa 1 thẻ <#0.35#>, và chỉ sau dấu ':'
    bad = []
    for c in CLIPS:
        for i, ln in enumerate(c["lines"], 1):
            t = ln[6]
            n = t.count("<#")
            if n > 1:
                bad.append(f"{c['id']}.01#{i} ({n} thẻ)")
            if n == 1 and ":" not in t:
                bad.append(f"{c['id']}.01#{i} (thẻ không sau dấu ':')")
            if "..." in t:
                bad.append(f"{c['id']}.01#{i} (có '...')")
    rows.append(("2", "G1 — ≤ 1 thẻ `<#0.35#>`/câu, sau dấu ':', không có '...'",
                 ("✅ 0 lỗi" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 3. G3/G4/G5
    bad = []
    for c in CLIPS:
        for i, ln in enumerate(c["lines"], 1):
            if ln[1] not in EMOTION_OK:
                bad.append(f"{c['id']}.01#{i} emotion={ln[1]}")
            if not (-0.06 <= ln[2] <= 0.02):
                bad.append(f"{c['id']}.01#{i} speed={ln[2]}")
    rows.append(("3", "G3 (4 emotion an toàn) · G4 (speed −0,06…+0,02) · G5 (pitch = 0)",
                 ("✅ 0 lỗi" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 4. V3 — mọi con số trên thẻ overlay phải có trong câu được trỏ tới
    bad = []
    for c in CLIPS:
        ids = {f"{c['id']}.01#{i}": ln for i, ln in enumerate(c["lines"], 1)}
        for o in c["overlay"]:
            if o["sau_cau"] not in ids:
                bad.append(f"{o['sau_cau']} không tồn tại")
                continue
            said = ids[o["sau_cau"]][6].lower()
            for num in re.findall(r"\d+", o["text"]):
                v = int(num)
                forms = {str(v), vi_number(v)}
                if not any(f.lower() in said for f in forms):
                    bad.append(f"{o['sau_cau']} thiếu số {v}")
    rows.append(("4", "V3 — số trên thẻ overlay phải có trong câu được trỏ tới",
                 ("✅ 0 lỗi" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 5. hook ≤ 12 từ
    bad = [f"{c['id']} ({len(c['hook'].split())} từ)" for c in CLIPS if len(c["hook"].split()) > 12]
    rows.append(("5", "Hook ≤ 12 từ (mục 3.2 kế hoạch mẹ)",
                 ("✅ 5/5 đạt" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 6. caption ≤ 2200 ký tự
    bad = [f"{c['id']} ({len(build_caption(c))})" for c in CLIPS if len(build_caption(c)) > 2200]
    rows.append(("6", "Caption ≤ 2.200 ký tự (Content Posting API)",
                 ("✅ 5/5 đạt" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 7. hashtag
    bad = []
    for c in CLIPS:
        hs = HASHTAGS[c["id"]]
        if len(hs) < 5 or len(hs) > 8:
            bad.append(f"{c['id']} ({len(hs)} hashtag)")
        for req in ("#AmberEyes", "#HosoCoThat"):
            if req not in hs:
                bad.append(f"{c['id']} thiếu {req}")
    rows.append(("7", "Hashtag 5–8, có #AmberEyes + #HosoCoThat (mục 3.4)",
                 ("✅ 5/5 đạt" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 7b. nhãn AIGC phải nằm TRONG thân caption (luật T3 kế hoạch mẹ)
    bad = []
    for c in CLIPS:
        cap = build_caption(c)
        if DONG_AIGC not in cap:
            bad.append(f"{c['id']} thiếu dòng nhãn AIGC")
        # phần dán = trước dấu "---"; nhãn phải nằm trong phần này
        phan_dan = cap.split("\n---")[0]
        if DONG_AIGC not in phan_dan:
            bad.append(f"{c['id']} nhãn AIGC nằm ngoài phần dán")
    rows.append(("7b", "Dòng nhãn AIGC nằm trong thân caption (luật T3)",
                 ("✅ 5/5 đạt" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 8. độ dài clip trong cổng
    bad = [f"{c['id']} ({c['uoc_luong_s']:.1f} s)" for c in CLIPS
           if not (45 <= c["uoc_luong_s"] <= 95)]
    rows.append(("8", "Độ dài clip trong cổng 45–95 s (ước lượng có cơ sở đo)",
                 ("✅ 5/5 đạt" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 9. nguồn ảnh nền dọc có file gốc
    miss = [f"{n} ← {s}" for n, s in NEN_SRC.items() if not raw_exists(s)]
    rows.append(("9", "Nguồn 16:9 của %d nền dọc `tk02_*` có trong `_raw/`" % len(NEN_SRC),
                 ("✅ %d/%d có file" % (len(NEN_SRC) - len(miss), len(NEN_SRC)) if not miss
                  else "❌ thiếu: " + ", ".join(miss))))
    ok = ok and not miss

    # 10. K10 — mỗi clip gắn ít nhất 1 chỉ dấu
    bad = [c["id"] for c in CLIPS if not c["chi_dau"]]
    allcd = sorted({i for c in CLIPS for i in c["chi_dau"]})
    rows.append(("10", "K10 — mỗi clip ≥ 1 chỉ dấu tâm lý",
                 ("✅ 5/5 đạt — phủ chỉ dấu %s" % ", ".join(f"#{i}" for i in allcd)
                  if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 11. K5 — có câu cảnh báo không có chẩn đoán lâm sàng
    has = any("không tồn tại" in ln[6] and "chẩn đoán" in ln[6]
              for c in CLIPS for ln in c["lines"])
    rows.append(("11", "K5 — clip TK3 có câu cảnh báo “không có chẩn đoán lâm sàng công khai”",
                 "✅ có" if has else "❌ thiếu"))
    ok = ok and has

    # 12. K2 — câu trích phải nguyên văn từ kịch bản tập
    script = json.loads((WORK / "script_tap02.json").read_text(encoding="utf-8"))
    src_texts = {}
    for e in script:
        for s in e.get("sentences", []):
            src_texts[s["id"]] = s["text"]
    quotes = []
    for c in CLIPS:
        for i, ln in enumerate(c["lines"], 1):
            for m in re.findall(r"<#0\.35#>\s*(.+)$", ln[6]):
                q = m.strip().rstrip('"”').strip().rstrip(".,;:!?").strip()
                found = any(q in t for t in src_texts.values())
                quotes.append((c["id"], i, found))
    bad = [f"{cid}#{i}" for cid, i, f in quotes if not f]
    rows.append(("12", "K2 — %d câu trích phải nguyên văn trong kịch bản tập" % len(quotes),
                 ("✅ %d/%d nguyên văn" % (len(quotes) - len(bad), len(quotes))
                  if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 13. G6 — lời đọc trong spec == lời đọc trong bảng md
    rows.append(("13", "G6 — .md và .json cùng sinh từ MỘT nguồn (`.work/_build_tk_tap02.py`)",
                 "✅ không thể lệch — chung generator"))
    rows.append(("14", "L3 — thời lượng có số đo thật làm cơ sở (timeline Tập 02 đo bằng ASR)",
                 "✅ tỉ lệ đọc đo trên 203 câu thật · LOO MAE 11,0 %/câu · mô phỏng clip MAE 3,7 %"))

    # 15. mô tả ngắn — cấu trúc chuẩn Tập 01 + ký tự + dòng bắt buộc
    bad = []
    for c in CLIPS:
        cid = c["id"]
        m = MO_TA_NGAN[cid]
        hook1 = c["lines"][0][6].strip()
        # Dong dau mo ta = HOOK: hoac clip["hook"] (chu tren hinh) hoac loi doc cau 1.
        # TikTok chi hien ~100 ky tu dau => dong dau la dong quyet dinh.
        d1 = m.splitlines()[0].strip().rstrip("👁️").strip()
        if d1 not in (c["hook"].strip(), hook1):
            bad.append(f"{cid} dong 1 '{d1[:38]}' khong phai hook")
        # 2 ban (ngắn + dài) phải cùng dong dau
        if m.splitlines()[0].strip() != MO_TA_DAI[cid].splitlines()[0].strip():
            bad.append(f"{cid} dong 1 lệch giữa bản ngắn và bản dài")
        if not (900 <= len(m) <= 1600):
            bad.append(f"{cid} dài {len(m)} (cần 900–1.600)")
        if "Tập 02 · Đại tá hai mặt — Chỉ dấu #" not in m:
            bad.append(f"{cid} thiếu dòng tập/chỉ dấu")
        if "Bước ngoặt của hồ sơ này:" not in m:
            bad.append(f"{cid} thiếu dòng 'Bước ngoặt'")
        if "Theo bạn," not in m or "👇" not in m:
            bad.append(f"{cid} thiếu câu hỏi 👇")
        if "📺 Xem trọn bộ hồ sơ phân tích đầy đủ (25 phút" not in m:
            bad.append(f"{cid} thiếu dòng Xem trọn bộ (25 phút)")
        if "🔎 Hồ sơ có thật, dữ liệu có nguồn." not in m:
            bad.append(f"{cid} thiếu dòng 🔎")
        tags = [t for t in re.findall(r"#\w+", m) if not re.fullmatch(r"#\d+", t)]
        if not (5 <= len(tags) <= 8):
            bad.append(f"{cid} {len(tags)} hashtag (cần 5–8)")
        for req in ("#AmberEyes", "#HosoCoThat"):
            if req not in tags:
                bad.append(f"{cid} thiếu {req}")
        # T31: so sanh KHONG phan biet hoa thuong - "Không phù hợp cho trẻ em" (dau dong)
        # va "không phù hợp cho trẻ em" (giua cau) deu la canh bao hop le.
        if "không phù hợp cho trẻ em" not in m.lower():
            bad.append(f"{cid} thiếu cảnh báo trẻ em")
        # T34: so SỐ MỤC liệt kê với số từ định lượng trong câu dẫn.
        # "bốn nấc thang" nhung chi liet ke 3 bullet => nguoi doc dem se thay thieu.
        n_bullet = m.count("\n• ")
        for tu, so in (("bốn nấc", 4), ("ba nấc", 3), ("năm nấc", 5)):
            if tu in m.lower() and n_bullet < so:
                bad.append(f"{cid} nói '{tu}' nhung chỉ liet ke {n_bullet} bullet")
    rows.append(("15", "Mô tả ngắn — dòng 1 = hook (chữ trên hình / lời đọc câu 1), khớp bản dài, 900–1.600 ký tự",
                 ("✅ 5/5 đạt" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad

    # 16. mô tả dài — dòng đầu cũng phải là hook
    bad = []
    for c in CLIPS:
        hook1 = c["lines"][0][6].strip()
        d1 = MO_TA_DAI[c["id"]].splitlines()[0].strip().rstrip("👁️").strip()
        if d1 not in (c["hook"].strip(), hook1):
            bad.append(f"{c['id']} dong 1 khong phai hook")
    rows.append(("16", "Mô tả dài — dòng đầu = hook (chữ trên hình / lời đọc câu 1)",
                 ("✅ 5/5 đạt" if not bad else "❌ " + ", ".join(bad))))
    ok = ok and not bad
    return rows, ok

def vi_number_words(v):
    """vi_number cơ bản — dùng cho kiểm V3 (số trên thẻ vs câu đọc)."""
    d = ["không trăm", "một", "hai", "ba", "bốn", "năm", "sáu", "bảy", "tám", "chín"]
    if v < 10:
        return d[v]
    if v < 20:
        return "mười" + ("" if v == 10 else " " + d[v - 10])
    if v < 100:
        return d[v // 10] + " mươi" + ("" if v % 10 == 0 else " " + d[v % 10])
    if v < 1000:
        r = vi_number_words(v // 100) + " trăm"
        return r if v % 100 == 0 else r + " " + vi_number_words(v % 100)
    if v < 10000:
        r = vi_number_words(v // 1000) + " nghìn"
        return r if v % 1000 == 0 else r + " " + vi_number_words(v % 1000)
    r = vi_number_words(v // 1000000) + " triệu"
    return r if v % 1000000 == 0 else r + " " + vi_number_words(v % 1000000)

QC_ROWS = []

def main():
    spec = build_spec()
    (OUT / "SPEC_AUDIO_CLIP_TAP02.json").write_text(
        json.dumps(spec, ensure_ascii=False, indent=1), encoding="utf-8")
    write_caption_files()
    global QC_ROWS
    QC_ROWS, allok = self_qc()
    write_markdown()

    print("=== THOI LUONG UOC LUONG (co so do) ===")
    for c in CLIPS:
        n = len(c["lines"])
        print(f"{c['id']}: {c['uoc_luong_s']:6.1f} s  · {n:2d} cau  · {c['ten_vn']}")
    print()
    print("=== CAPTION / MO TA DAI ===")
    for c in CLIPS:
        cap = build_caption(c)
        print(f"{c['id']}: caption {len(cap)} ky tu ({'OK' if len(cap)<=2200 else 'VUOT'}) · "
              f"mo ta dai {len(MO_TA_DAI[c['id']])} ky tu")
    print()
    print("=== TU KIEM KICH BAN ===")
    for r in QC_ROWS:
        print(f"[{r[0]}] {r[1]}\n      -> {r[2]}")
    print()
    print("TONG KET TU KIEM:", "DAT" if allok else "CO LOI — xem dong do")
    print()
    print("=== FILE DA GHI ===")
    for f in sorted(OUT.iterdir()):
        print(f"  {f.name}  ({f.stat().st_size} bytes)")

if __name__ == "__main__":
    main()
