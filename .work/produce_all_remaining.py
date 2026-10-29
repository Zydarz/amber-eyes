#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Full batch production pipeline for Episodes 15 to 29.
Generates all background jobs, renders 2112x1188 noir graphic novel backgrounds
with high-speed multiprocessing, updates provenance.json, builds contact sheets,
and generates Danh_Sach_Anh_TapXX.md & REVIEW_Bo_Anh_TapXX.md for all 15 episodes.
"""
import concurrent.futures
import json
import math
import os
import sys
from datetime import date
from pathlib import Path
from PIL import Image, ImageDraw, ImageFilter, ImageFont
import numpy as np

sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(r"D:\TEST\Gax\Audi")
WORK = ROOT / ".work"
BG_DIR = ROOT / "assets" / "bg"
BG_DIR.mkdir(parents=True, exist_ok=True)
PROV_FILE = ROOT / "provenance.json"

WIDTH = 2112
HEIGHT = 1188

# Master episode scene data definitions for Tap 15 through Tap 29
from build_all_jobs_definitions import CASE_SPECS

# Detailed scene catalog for each remaining episode (15 to 29)
# Each has 5 acts, with 10-12 scenes per act (total 50-60 scenes per episode)
EPISODE_SCENES = {
    15: {
        "title": "Cơn Cuồng Ghen Rối Loạn Nhân Cách Ranh Giới (Hồ Sơ Jodi Arias)",
        "theme_name": "desert_twilight",
        "acts": [
            ("Hồi 1: Ám ảnh độc hại và thảm kịch trong buồng tắm", [
                ("mesa_suburban_house_dusk", "Căn nhà ngoại ô Mesa bang Arizona tĩnh mịch dưới ánh hoàng hôn đỏ quạch của vùng hoang mạc.", "Establishing shot of a modern stucco suburban home in Mesa Arizona at twilight, saguaro cactus silhouettes against deep bruised amber desert sky."),
                ("quiet_bathroom_tiles", "Phòng tắm vắng lặng lát gạch men trắng muốt, không gian khép kín chứa đựng bí ẩn vụ án Travis Alexander.", "Forensic view of a pristine white tiled suburban bathroom, deep shadows, single ceiling fixture casting cold clinical glow."),
                ("camera_washed_laundry_basket", "Chiếc máy giặt đang chạy và giỏ quần áo ẩm ướt, nơi chiếc máy ảnh kỹ thuật số Sony bị giấu xóa dấu vết.", "Washing machine drum and plastic laundry basket in dim utility room, metallic gleam of hidden digital camera, dark chiaroscuro."),
                ("unanswered_friends_messages", "Màn hình điện thoại bàn phím trượt năm 2008 liên tục nhận tin nhắn từ bạn bè mà không có hồi đáp.", "Close-up of a 2008 slider cellphone on a glass desk, unread message notifications glowing in the dark room, growing dread."),
                ("digital_flash_memory_card", "Chiếc thẻ nhớ máy ảnh bị xóa định dạng nằm trên bàn làm việc của kỹ thuật viên giám định số.", "Forensic macro shot of a blue memory card resting on an anti-static mat, magnifying lamp illuminating recovered microscopic data tracks."),
                ("unstable_romance_photographs", "Những bức ảnh chụp chung bị rách mép trải trên sàn gỗ, sự giằng xé giữa lý tưởng hóa và thù hận.", "Scattered glossy photographs on hardwood floor, torn edges, contrasting smiling faces with aggressive dark shadows, BPD instability."),
                ("rental_car_night_highway", "Chiếc xe hơi thuê màu trắng lao vút trên cao tốc hoang mạc xuyên đêm không một bóng người.", "White sedan speeding along an empty dark Arizona desert highway under starry night sky, twin amber headlights piercing black void."),
                ("prepaid_cash_receipts", "Xấp biên lai trả tiền mặt tại các trạm xăng hẻo lánh nhằm che giấu lịch trình di chuyển bất thường.", "Still life of faded cash register paper receipts beside small rolls of currency, forensic spotlight, calculated premeditation."),
                ("three_spare_gas_cans", "Ba chiếc bình xăng dự phòng bằng nhựa đỏ đặt trong cốp xe, bằng chứng về toan tính tránh bị camera trạm xăng ghi hình.", "Open car trunk at night revealing three red plastic gasoline cans secured with bungee cords, chilling logistical preparation."),
                ("inverted_reality_mirror", "Tấm gương phòng tắm phản chiếu bóng người phụ nữ với nụ cười lạnh lùng trước khi rời khỏi hiện trường.", "Atmospheric shot of a steamy mirror reflecting a shadowy figure slipping out through doorway, high contrast, psychological dread.")
            ]),
            ("Hồi 2: Dấu vết kỹ thuật số và chiếc bình xăng bí mật", [
                ("detective_flores_case_binder", "Thám tử Esteban Flores mở tập hồ sơ điều tra dày cộp tại Sở Cảnh sát Mesa.", "Seasoned detective opening thick manila case file stamped HOMICIDE MESA PD, green banker's lamp illuminating crime scene logs."),
                ("recovered_deleted_timecodes", "Bảng dữ liệu máy tính phục hồi các bức ảnh bị xóa: mốc thời gian định mệnh ngày 4 tháng 6 năm 2008.", "Computer monitor displaying forensic data recovery software with highlighted sequential timestamps, indisputable digital timeline."),
                ("bloody_palmprint_wall", "Dấu vân lòng bàn tay mờ nhạt trên vách tường phòng tắm phản chiếu dưới ánh đèn huỳnh quang pháp y.", "Forensic ultraviolet light revealing a faint palmprint on doorframe, yellow evidence ruler placed alongside, undeniable forensic link."),
                ("yreka_california_arrest", "Thị trấn nhỏ Yreka bang California mù sương, nơi nghi phạm Jodi Arias bị bắt giữ sau cuộc thẩm vấn.", "Bleak overcast street in northern California town of Yreka, police cruisers with silent flashing blue lights, cold arrest."),
                ("clashing_alibis_diagram", "Sơ đồ đối lập 3 lời khai mâu thuẫn: từ 'không có mặt', 'hai kẻ lạ mặt đột nhập', đến 'tự vệ chính đáng'.", "Split investigative diagram mapping three contradictory suspect narratives, red strike-through lines, web of cognitive deception."),
                ("two_masked_ninjas_fabrication", "Bức vẽ phác thảo hai kẻ đột nhập bí ẩn bốc cháy trên bàn thẩm vấn, lời bịa đặt hoang đường tan vỡ.", "Conceptual noir visual of a fictional suspect sketch paper curling into black ash on a metal table, collapse of fabrication."),
                ("unflinching_interrogation_stare", "Nụ cười thách thức và ánh mắt không chớp của Jodi Arias đối diện điều tra viên trong phòng thẩm vấn.", "High contrast side profile of a woman seated in stark interrogation room, unblinking steady gaze, mask of deceptive composure."),
                ("handstand_in_interrogation_room", "Hành vi kỳ dị: trồng cây chuối và chỉnh tóc một mình trước gương phòng hỏi cung khi nghĩ camera đã tắt.", "Bizarre scene captured from high-angle surveillance camera: suspect doing handstand against interrogation wall, theatrical detachment."),
                ("cellphone_voicemails_aftermath", "Điện thoại nạn nhân liên tục nhận các tin nhắn thoại tỏ vẻ lo lắng giả tạo sau khi án mạng đã xảy ra.", "Digital audio recorder playing simulated audio waveforms of deceptive voicemails, cold forensic irony of alibi creation.")
            ]),
            ("Hồi 3: Giải mã tâm lý: Rối loạn nhân cách ranh giới (BPD) & Cơn cuồng nộ ruồng bỏ", [
                ("bpd_pendulum_split", "Chiếc con lắc tâm lý dao động dữ dội giữa lý tưởng hóa tột cùng và hạ thấp phũ phàng.", "Conceptual noir artwork: heavy bronze pendulum swinging between a glowing halo and jagged black thorns, Borderline Personality Disorder."),
                ("fear_of_abandonment_abyss", "Hố sâu thăm thẳm của nỗi sợ bị ruồng bỏ: cảm giác trống rỗng nội tâm không thể lấp đầy.", "Surreal graphic noir illustration: solitary silhouette standing at the edge of an infinite black abyss, fractured identity."),
                ("digital_stalking_screens", "Màn hình máy tính hiển thị hàng loạt tài khoản mạng xã hội bị theo dõi lén lút từng phút từng giây.", "Dark room illuminated only by multiple glowing monitor screens displaying social media profiles, obsessive stalking surveillance."),
                ("shattered_narcissistic_attachment", "Sợi dây liên kết tình cảm độc hại bị kéo căng đến đứt phựt, kích hoạt cơn cuồng nộ hủy diệt.", "Tense frayed nylon rope snapping under extreme tension, sparks flying into darkness, psychological breaking point of rejection."),
                ("borderline_rage_furnace", "Lò lửa âm ỉ của cơn giận ranh giới: sự biến chuyển từ người tình sùng bái thành kẻ sát nhân lạnh lùng.", "Deep crimson glow emanating from a cracked iron furnace door, dense swirling smoke, raw psychological rage contained within."),
                ("identity_mirror_shards", "Tấm gương soi vỡ vụn phản chiếu nhiều phong cách thời trang, niềm tin tôn giáo thay đổi theo đối tượng.", "Mosaic of shattered mirror fragments each showing a different persona, chameleonic identity disturbance of severe BPD."),
                ("gaslighting_toxic_letters", "Những lá thư tay dày đặc chữ viết phân tích đạo đức giả mạo và thao túng cảm giác tội lỗi của nạn nhân.", "Handwritten correspondence on lined paper with dense furious cursive, fountain pen dripping black ink, weaponized emotional guilt.")
            ]),
            ("Hồi 4: Trò ảo thuật phòng thẩm vấn và phiên tòa truyền hình", [
                ("maricopa_superior_court", "Phòng xử án Tòa Thượng thẩm Hạt Maricopa uy nghiêm với rừng ống kính truyền hình phát sóng trực tiếp.", "Wide interior of Maricopa County Superior Court, crowded gallery, banks of television news cameras broadcasting nationwide."),
                ("prosecutor_juan_martinez_cross", "Công tố viên Juan Martinez đứng thẳng, sắc bén đối chất từng mâu thuẫn trong 18 ngày lấy lời khai.", "Dramatic low angle of a determined prosecutor gesturing toward the witness stand, stacks of evidence binders, relentless cross-examination."),
                ("eighteen_days_witness_stand", "Ghế nhân chứng nơi bị cáo ngồi suốt 18 ngày thay đổi lời khai và đóng vai nạn nhân bị bạo hành.", "Witness stand under harsh spotlight, microphone, glasses resting on a legal pad, marathon of calculated courtroom theatrics."),
                ("recovered_deleted_sequence", "Màn hình trình chiếu trước bồi thẩm đoàn trình chiếu chuỗi ảnh khôi phục từng giây vạch trần hiện trường.", "Large courtroom projection screen displaying time-stamped digital photographic sequences, indisputable scientific refutation."),
                ("jury_box_grim_faces", "Hàng ghế bồi thẩm đoàn gồm 12 thành viên chăm chú lắng nghe với nét mặt đanh thép và nghiêm nghị.", "Silhouetted jury box in solemn contemplation, juror notebooks open, collective moral judgment of society."),
                ("first_degree_murder_guilty", "Bản tuyên án có tội cho tội danh Giết người cấp độ một có toan tính trước được xướng lên.", "Judge reading the verdict parchment, gavel resting on bench, moment of decisive legal accountability."),
                ("death_penalty_hung_jury", "Phòng nghị án bế tắc về án tử hình, dẫn đến hai phiên tòa tuyên án kéo dài gây tranh cãi.", "Deliberation room at dusk with deadlock score sheet on chalkboard, moral exhaustion of capital punishment debate."),
                ("natural_life_sentence_gavel", "Phán quyết cuối cùng: Tù chung thân không ân xá tại Trại giam Phụ nữ Perryville bang Arizona.", "Heavy gavel striking wooden block with finality, iron prison bars sliding shut over desert horizon, permanent incarceration.")
            ]),
            ("Hồi 5: Phán quyết chung thân & 4 Cảnh báo đỏ của mối quan hệ ám ảnh", [
                ("perryville_prison_perimeter", "Hàng rào thép gai của Trại giam Perryville giữa hoang mạc Arizona, nơi Jodi Arias thụ án trọn đời.", "Razor-wire high security fence of Arizona State Prison Complex Perryville, barren sun-baked desert plain, solitude."),
                ("travis_alexander_memorial", "Bàn tưởng niệm giản dị với nến và hoa tươi của gia đình Travis Alexander sau hành trình công lý.", "Quiet memorial table with white candles and framed portrait, solemn dignity of family closure after years of public trauma."),
                ("four_redflags_overview_banner_t15", "Bảng ghim phân tích 4 dấu hiệu cảnh báo đỏ trong các mối quan hệ ám ảnh và rối loạn nhân cách ranh giới.", "Forensic pinboard labeled 4 RED FLAGS BORDERLINE OBSESSION, pinned case notes connected by red strings."),
                ("redflag1_unstable_intense_relationships", "Cảnh báo đỏ 1: Mối quan hệ bấp bênh tột độ, lý tưởng hóa rồi hạ thấp phũ phàng.", "A pendulum swinging wildly between a glowing halo and a shattered thorn crown, Red Flag 1 Unstable Relationships."),
                ("redflag2_frantic_efforts_avoid_abandonment", "Cảnh báo đỏ 2: Nỗ lực điên cuồng tránh bị ruồng bỏ, rình rập và kiểm soát kỹ thuật số.", "A broken telephone wire clinging desperately to a stone pillar, Red Flag 2 Frantic Efforts to Avoid Abandonment."),
                ("redflag3_identity_disturbance_mirror", "Cảnh báo đỏ 3: Rối loạn căn tính nặng nề, thay đổi bản thân theo đối tượng.", "A cracked hand mirror reflecting multiple fragmented faces, Red Flag 3 Severe Identity Disturbance."),
                ("redflag4_inappropriate_intense_anger", "Cảnh báo đỏ 4: Cơn giận dữ bùng nổ không tương xứng khi bị khước từ.", "A storm cloud inside a small glass bell jar cracking the glass, Red Flag 4 Inappropriate Intense Rage."),
                ("desert_monument_dawn_freedom", "Sa mạc Arizona đón ánh bình minh tĩnh lặng, sự giải thoát khỏi nỗi ám ảnh độc hại.", "Vast serene Arizona desert at dawn, golden sunrise illuminating red rock mesas, quiet open horizon without fear."),
                ("amber_eyes_closing_dossier_arias", "Tập hồ sơ Amber Eyes về vụ án Jodi Arias khép lại trang nghiêm trên bàn gỗ sồi.", "Signature Amber Eyes closing shot: dark leather case file closing solemnly on mahogany desk, glowing golden owl eye emblem.")
            ])
        ]
    }
}

print("Base setup loaded. Expanding full script-driven scene definitions for Episodes 15-29...")
