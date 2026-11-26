# BÁO CÁO THẨM ĐỊNH & REVIEW CHẤT LƯỢNG BỘ ẢNH NỀN TẬP 24
## "KÝ ỨC KẺ SÁT NHÂN HWASEONG" (HWASEONG, GYEONGGI, HÀN QUỐC)

*Ngày lập báo cáo: 2026-11-25 (bản cập nhật, thay thế bản 24/10/2026 mô tả bộ ảnh `t24_lee_choon_jae_*` đã không còn trên đĩa).*
*Dự án: Podcast Tài liệu Phân tích Tâm lý Tội phạm Amber Eyes.*

---

## I. TỔNG QUAN ĐÁNH GIÁ (EXECUTIVE SUMMARY)

| Tiêu chí | Kết quả thẩm định | Trạng thái | Ghi chú kỹ thuật |
|---|:---:|:---:|---|
| **Số lượng ảnh** | **155 / 155 ảnh** | **ĐẠT (100%)** | Toàn bộ `assets/bg/t24_*.png` đều được dùng, 0 ảnh thừa (H22) |
| **Kích thước & Tỷ lệ** | **2112 × 1188 (16:9 2K)** | **ĐẠT (100%)** | 155/155 ảnh full-bleed, không viền đen letterbox |
| **Kiểm tra viền & Khung vẽ (QC)** | **0 lỗi** | **ĐẠT (100%)** | `qc_bg.py t24` báo 8 ảnh có dải tối sát viền — đã soi mắt, đều là **nội dung cảnh** (tường, cột, trời đêm), KHÔNG phải letterbox |
| **Sổ nguồn gốc (`provenance.json`)** | **155 / 155 bản ghi** | **ĐẠT (100%)** | Đầy đủ metadata prompt, công cụ tạo ảnh, kích thước gốc; bản quyền kênh 100% tự chủ |
| **Phủ câu thoại** | **246 / 246 câu** | **ĐẠT (100%)** | 1 bảng shot phục vụ cả VN / EN / JA (H25 · A8.1(c)) |
| **Tần suất nền (H22)** | **1.6 shot/nền** | **ĐẠT** | Mục tiêu 1,5–2 shot/nền; không nền nào vượt 3 shot hoặc 30 s |
| **QC nội dung ảnh (H2/H19/H26)** | **81/155 ảnh (52%)** | **KHÔNG ĐẠT — người dùng chốt giữ nguyên** | Xem mục III; quyết định của người dùng ngày 25/11/2026 |

---

## II. PHÂN BỔ ẢNH THEO 5 HỒI

Cột *Nền* là ảnh nền dùng chung cho cả 3 ngôn ngữ (VN / EN / JA); mã shot và thứ tự giữ nguyên 100%.

### HỒI 1: NHỮNG CÁNH ĐỒNG ĐÊM HWASEONG & 33 NĂM TRONG SƯƠNG MÙ — 37 ảnh / 58 shot

- `t24_a1_23_rural_village_lane_fog_23`:
  - Shot `1-01` · `1.02#1` (15,8 s) · Cú · Host · mẫu T1 · camera `still` — *Vào những năm cuối thập niên 1980, tại vùng nông thôn Hwaseong thuộc tỉnh Gyeonggi, cách thủ đô Seoul không xa, một bầu không khí u ám và tang thương …*
  - Shot `1-44` · `1.11#5` (5,6 s) · Cú · Host · mẫu T1 · camera `pull` — *Khoa học hiện đại đã đánh thức những bằng chứng câm lặng mà thời gian tưởng chừng đã xóa nhòa.*
- `t24_a1_01_desolate_rice_paddies_mist_01`:
  - Shot `1-02` · `1.02#2` (14,0 s) · Cú · Host · mẫu T1 · camera `pan` — *Bắt đầu từ mùa thu năm 1986 đến mùa xuân năm 1991, một chuỗi mười vụ án mạng kinh hoàng đã liên tiếp xảy ra dọc theo những cánh đồng lúa và những con …*
- `t24_a1_02_rural_village_lane_fog_02`:
  - Shot `1-03` · `1.02#3` (10,0 s) · Cú · Host · mẫu T1 · camera `push` — *Nạn nhân đều là những người phụ nữ thuộc nhiều độ tuổi khác nhau, bị kẻ thủ ác bí mật phục kích khi đang trên đường đi làm về hoặc băng qua đồng vắng …*
  - Shot `1-04` · `1.02#4` (7,1 s) · Cú · Host · mẫu T1 · camera `pull` — *Chuỗi án mạng lặp lại ấy đã biến Hwaseong thành một vùng đất của nỗi ám ảnh kinh hoàng nhất trong lịch sử Hàn Quốc.*
- `t24_a1_03_gravel_road_twilight_03`:
  - Shot `1-05` · `1.02#5` (10,4 s) · Cú · Host · mẫu T1 · camera `still` — *Cứ mỗi khi hoàng hôn buông xuống, không một người phụ nữ nào dám bước chân ra khỏi ngưỡng cửa, và những lời đồn thổi về chiếc áo màu đỏ lan khắp các l…*
  - Shot `1-06` · `1.02#6` (7,4 s) · Cú · Host · mẫu T1 · camera `pan` — *Đó là vụ án từng trở thành nguồn cảm hứng cho bộ phim “Hồi ức kẻ sát nhân” năm 2003.*
- `t24_a1_04_desolate_rice_paddies_mist_04`:
  - Shot `1-07` · `1.02#7` (9,4 s) · Cú · Host · mẫu T1 · camera `push` — *Khi ấy, Hàn Quốc đang trong thời kỳ chuyển mình phát triển mạnh mẽ, nhưng hệ thống chiếu sáng nông thôn và camera an ninh gần như là con số không.*
  - Shot `1-08` · `1.02#8` (9,0 s) · Cú · Host · mẫu T1 · camera `pull` — *Sự thiếu thốn hạ tầng kỹ thuật đã vô tình biến những cánh đồng lúa bạt ngàn thành địa bàn săn mồi hoàn hảo cho một con quái vật ẩn danh.*
- `t24_a1_05_police_patrol_rural_search_05`:
  - Shot `1-09` · `1.04#1` (8,8 s) · Cú · Host · mẫu T1 · camera `still` — *Để truy lùng bóng ma tội ác vô hình ấy, chính phủ Hàn Quốc thời điểm đó đã phát động một chiến dịch điều tra quy mô chưa từng có tiền lệ.*
  - Shot `1-10` · `1.04#2` (4,3 s) · Cú · Host · mẫu T1 · camera `pan` — *Hơn hai triệu lượt cảnh sát đã được huy động trong suốt quá trình điều tra.*
- `t24_a1_06_police_patrol_rural_search_06`:
  - Shot `1-11` · `1.04#3` (3,9 s) · Cú · Host · mẫu T1 · camera `push` — *Hơn hai mươi mốt nghìn người đã bị điều tra trong suốt nhiều năm ròng rã.*
  - Shot `1-12` · `1.04#4` (7,1 s) · Cú · Host · mẫu T1 · camera `pull` — *Lực lượng điều tra phải chịu áp lực dư luận khủng khiếp, nhiều thám tử đã dành cả sự nghiệp để tìm kẻ thủ ác.*
- `t24_a1_07_police_patrol_rural_search_07`:
  - Shot `1-13` · `1.04#5` (2,8 s) · Cú · Host · mẫu T1 · camera `still` — *Sự bế tắc kéo dài khiến nhiều người kiệt sức.*
  - Shot `1-14` · `1.04#6` (7,0 s) · Cú · Host · mẫu T1 · camera `pan` — *Đau đớn hơn, một mẫu vật chứng bị lẫn tạp chất đã khiến cảnh sát tin chắc rằng hung thủ mang nhóm máu B.*
- `t24_a1_08_police_patrol_rural_search_08`:
  - Shot `1-15` · `1.04#7` (8,2 s) · Cú · Host · mẫu T1 · camera `push` — *Sai lầm kỹ thuật ban đầu ấy đã trở thành một điểm mù định kiến chết người, che mắt toàn bộ lực lượng điều tra suốt nhiều thập kỷ.*
  - Shot `1-16` · `1.05#1` (10,8 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Dưới góc độ tâm lý học nhận thức, bi kịch ba mươi ba năm bế tắc của hồ sơ Hwaseong khởi nguồn từ một hiện tượng tâm lý kinh điển mang tên “Hội chứng Đ…*
- `t24_a1_09_police_patrol_rural_search_09`:
  - Shot `1-17` · `1.05#2` (8,2 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Khi một kết quả giám định pháp y sơ khai ban đầu kết luận hung thủ mang nhóm máu B, toàn bộ lực lượng điều tra đã vô thức rơi vào chiếc bẫy “Thiên kiế…*
  - Shot `1-18` · `1.05#3` (6,4 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Họ tự động loại bỏ mọi dấu hiệu đáng ngờ của những người mang nhóm máu khác, tạo nên một điểm mù chết người trong tư duy logic.*
- `t24_a1_10_rain_drenched_crossroad_10`:
  - Shot `1-19` · `1.05#4` (8,7 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Chính sự tự tin mù quáng vào một giả định chưa được kiểm chứng độc lập đã vô tình trao tấm thẻ bài miễn tử cho kẻ thủ ác mang nhóm máu O tự do lướt qu…*
  - Shot `1-20` · `1.06#1` (11,7 s) · Cú · Host · mẫu T1 · camera `pull` — *Và để xoa dịu nỗi bất an tột cùng trước một hiểm họa vô hình, tâm lý đám đông tại Hwaseong thời bấy giờ đã tự dệt nên huyền thoại về chiếc áo màu đỏ t…*
- `t24_a1_11_shadowy_window_heavy_curtains_11`:
  - Shot `1-21` · `1.06#2` (16,0 s) · Cú · Host · mẫu T1 · camera `still` — *Trong khoa học hành vi, đó là phản xạ tự trấn an vô thức của con người: khi đối diện với cái ác ngẫu nhiên không thể lường trước, não bộ buộc phải bám…*
- `t24_a1_12_police_patrol_rural_search_12`:
  - Shot `1-22` · `1.06#3` (9,4 s) · Cú · Host · mẫu T1 · camera `pan` — *Nhưng cái giá của sự huyễn hoặc ấy là sự rạn nứt hoàn toàn của lòng tin cộng đồng, biến từng ánh mắt hàng xóm thân quen thành nỗi ngờ vực khôn nguôi.*
  - Shot `1-23` · `1.06#4` (8,9 s) · Cú · Host · mẫu T1 · camera `push` — *Nhưng bất chấp mọi nỗ lực của con người, hung thủ dường như luôn đi trước lực lượng cảnh sát một bước và biến mất không dấu vết vào màn sương mù dày đ…*
- `t24_a1_13_rural_village_lane_fog_13`:
  - Shot `1-24` · `1.06#5` (12,8 s) · Cú · Host · mẫu T1 · camera `pull` — *Năm 2006, thời hiệu truy tố mười lăm năm theo luật pháp Hàn Quốc lúc bấy giờ đối với vụ án Hwaseong chính thức hết hạn, để lại một vết thương không có…*
  - Shot `1-25` · `1.08#1` (10,4 s) · Cú · Host · mẫu T1 · camera `still` — *Suốt hơn ba thập kỷ, vụ án Hwaseong bị coi là một thất bại đau đớn nhất của ngành tư pháp và là một vết nhơ khó gột rửa trong ký ức của xã hội Hàn Quố…*
- `t24_a1_14_rural_village_lane_fog_14`:
  - Shot `1-26` · `1.08#2` (8,1 s) · Cú · Host · mẫu T1 · camera `pan` — *Những gia đình nạn nhân phải sống trong nỗi đau đớn giằng xé từng ngày mà không biết ai là kẻ đã cướp đi sinh mệnh của người thân yêu.*
  - Shot `1-27` · `1.08#3` (8,0 s) · Cú · Host · mẫu T1 · camera `push` — *Người dân địa phương luôn phải sống trong sự nghi kỵ lẫn nhau, không biết liệu kẻ sát nhân có đang thản nhiên đi lại giữa cộng đồng hay không.*
- `t24_a1_15_dark_detention_interrogation_room_15`:
  - Shot `1-28` · `1.08#4` (8,4 s) · Cú · Host · mẫu T1 · camera `pull` — *Nỗi hoang tưởng tập thể bao trùm khắp các thôn xóm, biến những người hàng xóm tối lửa tắt đèn có nhau trở thành đối tượng bị dè chừng.*
  - Shot `1-29` · `1.08#5` (8,4 s) · Cú · Host · mẫu T1 · camera `still` — *Cảm giác an toàn của xã hội bị phá vỡ hoàn toàn, để lại vết sẹo tâm lý sâu hoắm trong lòng nhiều thế hệ người dân Hàn Quốc.*
- `t24_a1_16_police_patrol_rural_search_16`:
  - Shot `1-30` · `1.08#6` (9,0 s) · Cú · Host · mẫu T1 · camera `pan` — *Sự bất lực của công lý tưởng chừng như đã vĩnh viễn bị chôn vùi theo lớp bụi thời gian và sự già đi của những người điều tra thế hệ cũ.*
  - Shot `1-31` · `1.08#7` (6,2 s) · Cú · Host · mẫu T1 · camera `push` — *Nhưng những người thực thi pháp luật chân chính thì chưa bao giờ cho phép mình được quyền bỏ cuộc trước sự thật.*
- `t24_a1_17_desolate_rice_paddies_mist_17`:
  - Shot `1-32` · `1.09#1` (6,3 s) · N · mẫu T1 · camera `pull` — *Hãy hình dung ký ức của một người phụ nữ từng sống tại Hwaseong trong thập niên 1980.*
  - Shot `1-33` · `1.09#2` (9,2 s) · N · mẫu T1 · camera `still` — *Cứ mỗi lần nghe thấy tiếng còi xe cảnh sát hay tiếng xôn xao ngoài cánh đồng, lòng chúng tôi như thắt lại vì biết rằng lại có thêm một người hàng xóm …*
- `t24_a1_18_rain_drenched_crossroad_18`:
  - Shot `1-34` · `1.09#3` (3,7 s) · N · mẫu T1 · camera `pan` — *Cha mẹ không bao giờ cho các chị em gái ra ngoài sau khi trời tối.*
  - Shot `1-35` · `1.09#4` (4,9 s) · N · mẫu T1 · camera `push` — *Người ta đồn rằng kẻ sát nhân nhắm vào những phụ nữ mặc đồ màu đỏ trong những đêm mưa.*
- `t24_a1_19_rural_village_lane_fog_19`:
  - Shot `1-36` · `1.09#5` (8,6 s) · N · mẫu T1 · camera `pull` — *Bầu không khí nghi kỵ bao trùm khắp nơi, đàn ông trong làng nhìn nhau với ánh mắt dè chừng, lo sợ người quen biết cạnh nhà chính là con quỷ dữ.*
  - Shot `1-37` · `1.09#6` (7,2 s) · N · mẫu T1 · camera `still` — *Tiếng chó sủa vu vơ ngoài bờ ruộng hay một bóng người lướt qua dưới ánh trăng cũng đủ khiến cả gia đình run rẩy chèn cửa.*
- `t24_a1_20_rural_village_lane_fog_20`:
  - Shot `1-38` · `1.09#7` (9,3 s) · N · mẫu T1 · camera `pan` — *Suốt ba mươi ba năm trời, chúng tôi sống trong sự day dứt và cay đắng khi nghĩ rằng kẻ thủ ác sẽ mang theo bí mật xuống mồ mà không bị trừng phạt.*
  - Shot `1-39` · `1.09#8` (7,6 s) · N · mẫu T1 · camera `push` — *Nhưng sâu thẳm trong lòng, chúng tôi vẫn luôn hy vọng rằng trời cao có mắt và sự thật một ngày nào đó sẽ phải bước ra ánh sáng.*
- `t24_a1_21_police_patrol_rural_search_21`:
  - Shot `1-40` · `1.11#1` (7,1 s) · Cú · Host · mẫu T1 · camera `pull` — *Niềm hy vọng mong manh ấy cuối cùng đã được đền đáp nhờ vào sự tiến bộ vượt bậc của công nghệ khoa học hình sự hiện đại.*
  - Shot `1-41` · `1.11#2` (10,5 s) · Cú · Host · mẫu T1 · camera `still` — *Năm 2019, Cảnh sát tỉnh Gyeonggi Nambu gửi các mẫu vật chứng còn lưu giữ từ ba thập kỷ trước đến Viện Khoa học Pháp y Quốc gia Hàn Quốc.*
- `t24_a1_22_forensic_dna_laboratory_22`:
  - Shot `1-42` · `1.11#3` (9,5 s) · Cú · Host · mẫu T1 · camera `pan` — *Bằng công nghệ phân tích ADN mới, các chuyên gia đã trích xuất được ADN từ vật chứng của các vụ án số năm, số bảy và số chín.*
  - Shot `1-43` · `1.11#4` (8,7 s) · Cú · Host · mẫu T1 · camera `push` — *Các giám định viên pháp y đã tỉ mỉ phục hồi những phân tử ADN siêu vi lượng sau hơn ba mươi năm ngủ yên trong kho lưu trữ vật chứng.*
- `t24_a1_24_forensic_dna_laboratory_24`:
  - Shot `1-45` · `1.11#6` (8,0 s) · Cú · Host · mẫu T1 · camera `still` — *Dữ liệu ADN này lập tức được đối chiếu với cơ sở dữ liệu phạm nhân quốc gia và trả về một kết quả trùng khớp.*
- `t24_a1_25_busan_prison_steel_corridor_25`:
  - Shot `1-46` · `1.11#7` (9,7 s) · Cú · Host · mẫu T1 · camera `pan` — *Kẻ sát nhân không phải là một hồn ma vô hình, mà là một tù nhân đang thụ án chung thân tại Trại giam Busan mang tên Lee Choon-jae.*
- `t24_a1_26_rural_village_lane_fog_26`:
  - Shot `1-47` · `1.11#8` (9,3 s) · Cú · Host · mẫu T1 · camera `push` — *Một cuộc đối đầu tâm lý cân não mới chính thức mở màn bên trong bốn bức tường trại giam, chấm dứt chuỗi ngày ba mươi ba năm lẩn trốn dưới bóng tối.*
- `t24_a1_27_police_patrol_rural_search_27`:
  - Shot `1-48` · `1.12#1` (4,8 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Hãy hình dung cảm giác của một điều tra viên khi kết quả ADN trùng khớp với Lee Choon-jae.*
- `t24_a1_28_rural_village_lane_fog_28`:
  - Shot `1-49` · `1.12#2` (9,1 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Người đàn ông này năm mươi sáu tuổi, đã bị kết án tù chung thân từ năm 1994 vì tước đoạt mạng sống của em vợ tại thành phố Cheongju.*
- `t24_a1_29_busan_prison_steel_corridor_29`:
  - Shot `1-50` · `1.12#3` (6,7 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Trong suốt hai mươi lăm năm thụ án tại Trại giam Busan, Lee Choon-jae được mô tả là một phạm nhân kiểu mẫu, trầm lặng.*
- `t24_a1_30_prison_cell_embroidery_desk_30`:
  - Shot `1-51` · `1.12#4` (6,8 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Hắn chưa từng vi phạm bất kỳ nội quy trại giam nào, luôn chăm chỉ thêu ren và thậm chí từng được xếp vào diện xét giảm án.*
- `t24_a1_31_busan_prison_steel_corridor_31`:
  - Shot `1-52` · `1.12#5` (5,8 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Một vỏ bọc lương thiện hoàn hảo đến mức khiến các giám thị nhà tù không mảy may nghi ngờ về quá khứ đen tối của hắn.*
- `t24_a1_32_rural_village_lane_fog_32`:
  - Shot `1-53` · `1.12#6` (12,3 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Tuy nhiên, rào cản pháp lý lớn nhất thời điểm đó là thời hiệu truy tố đối với toàn bộ các vụ án Hwaseong đều đã hết hạn từ năm 2006, đồng nghĩa với vi…*
- `t24_a1_33_busan_prison_steel_corridor_33`:
  - Shot `1-54` · `1.12#7` (5,8 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Mục tiêu khi bước vào Trại giam Busan là tìm lại sự thật cho các nạn nhân và gia đình của họ.*
- `t24_a1_34_police_patrol_rural_search_34`:
  - Shot `1-55` · `1.13#1` (5,7 s) · Cú · Host · mẫu T1 · camera `push` — *Một đội điều tra viên cùng các chuyên gia phân tích tâm lý tội phạm đã lên đường đến Busan.*
- `t24_a1_35_claustrophobic_interrogation_room_35`:
  - Shot `1-56` · `1.13#2` (8,2 s) · Cú · Host · mẫu T1 · camera `pull` — *Nhưng điều mà họ sắp sửa đối mặt bên trong phòng thẩm vấn không phải là sự chối cãi ngoan cố hay những giọt nước mắt hối hận muộn màng.*
- `t24_a1_36_rural_village_lane_fog_36`:
  - Shot `1-57` · `1.13#3` (7,2 s) · Cú · Host · mẫu T1 · camera `still` — *Đó là một thái độ bình thản đến rợn người của một kẻ sát nhân hàng loạt tự hào về những tội ác mà mình đã thực hiện.*
- `t24_a1_37_claustrophobic_interrogation_room_37`:
  - Shot `1-58` · `1.13#4` (9,3 s) · Cú · Host · mẫu T1 · camera `pan` — *Một cuộc đấu trí cân não mở ra để bóc trần bản chất thật sự của con quỷ đội lốt người sau ba thập kỷ giấu mình trong sương mù.*

### HỒI 2: CUỘC ĐẤU TRÍ TẠI TRẠI GIAM BUSAN & LỜI TỰ BẠCH LẠNH GÁY — 30 ảnh / 48 shot

- `t24_a2_01_police_patrol_rural_search_01`:
  - Shot `2-01` · `2.02#1` (13,3 s) · Cú · Host · mẫu T1 · camera `push` — *Trong những ngày đầu tiên khi các điều tra viên đến Trại giam Busan, Lee Choon-jae vẫn tiếp tục duy trì vẻ ngoài của một tù nhân hiền lành và hoàn toà…*
  - Shot `2-02` · `2.02#2` (9,8 s) · Cú · Host · mẫu T1 · camera `pull` — *Hắn biết rất rõ luật pháp, hiểu rằng thời hiệu truy tố đã trôi qua và tin rằng cảnh sát không thể làm gì được một người đang thụ án chung thân như hắn…*
- `t24_a2_02_prison_visitation_glass_partition_02`:
  - Shot `2-03` · `2.02#3` (6,3 s) · Cú · Host · mẫu T1 · camera `still` — *Hắn chào hỏi lễ phép, mỉm cười nhẹ nhàng và đóng vai một người đàn ông vô tội bị làm phiền.*
  - Shot `2-04` · `2.02#4` (8,4 s) · Cú · Host · mẫu T1 · camera `pan` — *Sự bình thản trơ tráo ấy là một bức tường phòng vệ kiên cố được xây dựng bằng hai mươi lăm năm kinh nghiệm che giấu bản chất thật.*
- `t24_a2_03_police_patrol_rural_search_03`:
  - Shot `2-05` · `2.02#5` (5,6 s) · Cú · Host · mẫu T1 · camera `push` — *Để phá vỡ bức tường phòng vệ ấy, cảnh sát đã huy động các chuyên gia phân tích tâm lý tội phạm.*
  - Shot `2-06` · `2.04#1` (7,0 s) · Cú · Host · mẫu T1 · camera `pull` — *Các chuyên gia phân tích tâm lý tội phạm đã dành nhiều buổi trò chuyện để xây dựng lòng tin với Lee Choon-jae.*
- `t24_a2_04_prison_visitation_glass_partition_04`:
  - Shot `2-07` · `2.04#2` (10,4 s) · Cú · Host · mẫu T1 · camera `still` — *Họ không vội vàng chất vấn về các vụ án mạng, mà kiên nhẫn xây dựng mối quan hệ tin cậy, lắng nghe những tâm tư của một kẻ bị giam cầm suốt một phần t…*
  - Shot `2-08` · `2.04#3` (6,6 s) · Cú · Host · mẫu T1 · camera `pan` — *Theo các nhà phân tích, sự lắng nghe ấy chạm tới điểm yếu tâm lý của kẻ sát nhân: khao khát được công nhận.*
- `t24_a2_05_claustrophobic_interrogation_room_05`:
  - Shot `2-09` · `2.04#4` (8,0 s) · Cú · Host · mẫu T1 · camera `push` — *Chuyên gia tâm lý đã khéo léo biến phòng thẩm vấn thành một không gian nơi Lee Choon-jae cảm thấy cái tôi của mình được tôn trọng.*
  - Shot `2-10` · `2.04#5` (8,8 s) · Cú · Host · mẫu T1 · camera `pull` — *Khi chiếc mặt nạ tù nhân kiểu mẫu dần được gỡ bỏ, sự kiêu ngạo bệnh lý bên trong hắn bắt đầu tìm kiếm cơ hội trỗi dậy.*
- `t24_a2_06_police_patrol_rural_search_06`:
  - Shot `2-11` · `2.04#6` (10,2 s) · Cú · Host · mẫu T1 · camera `still` — *Khi các điều tra viên đặt trước mặt hắn những kết quả giám định ADN không thể chối cãi, bức tường kiên cố cuối cùng trong tâm trí Lee Choon-jae bắt đầ…*
  - Shot `2-12` · `2.04#7` (2,0 s) · Cú · Host · mẫu T1 · camera `pan` — *Cuối cùng, hắn bắt đầu thừa nhận.*
- `t24_a2_07_busan_prison_steel_corridor_07`:
  - Shot `2-13` · `2.04#8` (3,8 s) · Cú · Host · mẫu T1 · camera `push` — *Lời thú nhận ấy khiến tất cả mọi người có mặt phải sững sờ.*
  - Shot `2-14` · `2.04#9` (10,7 s) · Cú · Host · mẫu T1 · camera `pull` — *Một kẻ đã im lặng suốt hai mươi lăm năm sau song sắt, chưa từng hé răng nửa lời về quá khứ đen tối, tại sao lại đột ngột mở lòng khai nhận toàn bộ tội…*
- `t24_a2_08_prison_visitation_glass_partition_08`:
  - Shot `2-15` · `2.04#10` (5,4 s) · Cú · Host · mẫu T1 · camera `still` — *Liệu đó có phải là sự thức tỉnh muộn màng của lương tri trước thềm xế bóng cuộc đời?*
  - Shot `2-16` · `2.04#11` (5,7 s) · Cú · Host · mẫu T1 · camera `pan` — *Hay sâu thẳm bên dưới lời tự bạch lạnh lùng ấy lại là một cơ chế tâm lý hoàn toàn khác biệt?*
- `t24_a2_09_prison_visitation_glass_partition_09`:
  - Shot `2-17` · `2.05#1` (6,7 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Khoa học tâm lý học tội phạm khẳng định rằng: lời thú nhận của Lee Choon-jae hoàn toàn không xuất phát từ sự ăn năn hay hối hận chân thực.*
  - Shot `2-18` · `2.05#2` (7,5 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Bởi lẽ sự hối hận thực tâm đòi hỏi năng lực thấu cảm nỗi đau của nạn nhân — một phẩm chất tinh thần mà một kẻ ái kỷ ác tính hoàn toàn khuyết tật.*
- `t24_a2_10_prison_visitation_glass_partition_10`:
  - Shot `2-19` · `2.05#3` (7,2 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Động lực thực sự của hắn bắt nguồn từ sự sụp đổ nhu cầu che giấu khi thời hiệu truy tố đã chính thức hết hạn từ năm 2006.*
  - Shot `2-20` · `2.05#4` (9,6 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Khi nhận thức được rằng luật pháp không thể tuyên thêm bất kỳ án tử hình nào đối với mình, nỗi sợ hãi pháp lý trong hắn biến mất, nhường chỗ cho sự tr…*
- `t24_a2_11_police_patrol_rural_search_11`:
  - Shot `2-21` · `2.05#5` (9,9 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Hắn xem phòng thẩm vấn như một sân khấu tôn vinh quyền lực đen tối, nơi hắn có thể thỏa mãn cơn đói được công nhận bằng cách chứng minh mình đã vượt m…*
  - Shot `2-22` · `2.07#1` (3,5 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Kể từ đó, Lee Choon-jae bắt đầu một màn thú tội đáng kinh ngạc.*
- `t24_a2_12_police_patrol_rural_search_12`:
  - Shot `2-23` · `2.07#2` (9,0 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Hắn không chỉ thừa nhận toàn bộ mười vụ án mạng tại Hwaseong mà cảnh sát đang điều tra, mà còn khai thêm bốn vụ án mạng khác cùng hàng chục vụ xâm hại…*
  - Shot `2-24` · `2.07#3` (3,0 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Hắn còn vẽ lại sơ đồ một số hiện trường sau hơn ba mươi năm.*
- `t24_a2_13_police_patrol_rural_search_13`:
  - Shot `2-25` · `2.07#4` (6,7 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Hắn mô tả chính xác từng bụi cây, từng con mương và hướng gió của các đêm gây án mà không cần nhìn tài liệu điều tra.*
  - Shot `2-26` · `2.07#5` (9,2 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Sự chính xác tuyệt đối ấy chứng minh rằng những ký ức đen tối đó đã được hắn tua đi tua lại hàng nghìn lần trong tâm trí như những chiến lợi phẩm tinh…*
- `t24_a2_14_police_patrol_rural_search_14`:
  - Shot `2-27` · `2.07#6` (4,2 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Theo cảnh sát, hắn kể lại với một giọng điệu bình thản, không tỏ ra ăn năn.*
  - Shot `2-28` · `2.07#7` (4,4 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Năm xưa, cảnh sát từng nhiều lần đi ngang qua mặt hắn mà không hề hay biết.*
- `t24_a2_15_police_patrol_rural_search_15`:
  - Shot `2-29` · `2.09#1` (9,8 s) · Cú · Host · mẫu T1 · camera `push` — *Lời thú tội tự nguyện và thái độ tự mãn của Lee Choon-jae đã phơi bày một sự thật trớ trêu đến cay đắng của công tác điều tra thời kỳ đó.*
  - Shot `2-30` · `2.09#2` (9,8 s) · Cú · Host · mẫu T1 · camera `pull` — *Trong những năm tháng gây án, Lee Choon-jae từng ba lần bị cảnh sát địa phương chặn lại thẩm vấn vì nằm trong danh sách cư dân địa phương có biểu hiện…*
- `t24_a2_16_police_patrol_rural_search_16`:
  - Shot `2-31` · `2.09#3` (6,5 s) · Cú · Host · mẫu T1 · camera `still` — *Tuy nhiên, hắn đều được bỏ qua, một phần vì kết quả xét nghiệm vật chứng khi ấy không khớp với hắn.*
  - Shot `2-32` · `2.09#4` (7,7 s) · Cú · Host · mẫu T1 · camera `pan` — *Cảnh sát thời bấy giờ chỉ tập trung săn lùng người nhóm máu B, trong khi Lee Choon-jae thực tế lại mang nhóm máu O.*
- `t24_a2_17_forensic_investigation_desk_17`:
  - Shot `2-33` · `2.09#5` (8,4 s) · Cú · Host · mẫu T1 · camera `push` — *Chính sự sai lệch về nhóm máu đã trở thành tấm thẻ kim bài miễn tử giúp con quái vật tự do đi lại và tiếp tục gieo rắc tội ác.*
  - Shot `2-34` · `2.09#6` (10,6 s) · Cú · Host · mẫu T1 · camera `pull` — *Sự non kém về kỹ thuật hình sự và sự tin tưởng mù quáng vào những phán đoán cảm tính thời điểm đó đã để tuột mất kẻ sát nhân nguy hiểm nhất qua kẽ tay…*
- `t24_a2_18_police_patrol_rural_search_18`:
  - Shot `2-35` · `2.09#7` (7,4 s) · Cú · Host · mẫu T1 · camera `still` — *Và hậu quả của những sai lầm ấy là thêm những sinh mệnh vô tội bị tước đoạt trong sự bất lực của cả một hệ thống.*
  - Shot `2-36` · `2.10#1` (6,3 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Hãy hình dung câu hỏi của một điều tra viên: tại sao lại thú nhận khi luật pháp không còn có thể tuyên phạt thêm?*
- `t24_a2_19_forensic_dna_laboratory_19`:
  - Shot `2-37` · `2.10#2` (6,3 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Theo báo chí, Lee Choon-jae cho rằng khi ADN đã xuất hiện thì việc che giấu không còn ý nghĩa gì nữa.*
- `t24_a2_20_police_patrol_rural_search_20`:
  - Shot `2-38` · `2.10#3` (6,8 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Thậm chí hắn còn hỏi ngược lại điều tra viên với vẻ mặt ngạo nghễ: “Tôi cứ nghĩ các ông phải bắt được tôi từ lâu rồi chứ.”*
- `t24_a2_21_prison_visitation_glass_partition_21`:
  - Shot `2-39` · `2.10#4` (4,7 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Một số chuyên gia cho rằng nhu cầu được ghi nhận cũng thôi thúc hắn phơi bày sự thật.*
- `t24_a2_22_police_patrol_rural_search_22`:
  - Shot `2-40` · `2.10#5` (4,8 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Nhưng lời thú tội của hắn cũng làm lộ ra một sai lầm khác của ngành cảnh sát suốt ba thập kỷ.*
- `t24_a2_23_dark_detention_interrogation_room_23`:
  - Shot `2-41` · `2.11#1` (13,1 s) · Cú · Host · mẫu T1 · camera `push` — *Trong số mười vụ án mạng tại Hwaseong, vụ án số tám xảy ra vào năm 1988 từng được cơ quan chức năng tuyên bố phá án thành công với việc bắt giữ một th…*
- `t24_a2_24_dark_detention_interrogation_room_24`:
  - Shot `2-42` · `2.11#2` (8,5 s) · Cú · Host · mẫu T1 · camera `pull` — *Người đàn ông khuyết tật ấy đã bị ép cung và phải ngồi tù oan suốt hai mươi năm ròng rã cho một tội ác mà mình không hề gây ra.*
- `t24_a2_25_police_patrol_rural_search_25`:
  - Shot `2-43` · `2.11#3` (10,0 s) · Cú · Host · mẫu T1 · camera `still` — *Khi ấy, cảnh sát vì áp lực phá án đã dùng nhục hình, bỏ đói và tước đoạt giấc ngủ để bức cung một thanh niên nghèo khó không có khả năng tự vệ.*
- `t24_a2_26_prison_visitation_glass_partition_26`:
  - Shot `2-44` · `2.11#4` (6,1 s) · Cú · Host · mẫu T1 · camera `pan` — *Một bản án bất công đã cướp đi toàn bộ tuổi trẻ, danh dự và tương lai của một con người vô tội.*
- `t24_a2_27_dark_detention_interrogation_room_27`:
  - Shot `2-45` · `2.11#5` (9,5 s) · Cú · Host · mẫu T1 · camera `push` — *Việc Lee Choon-jae khẳng định chính mình mới là kẻ thực hiện vụ án số tám đã mở toang cánh cửa cho một cuộc đại phẫu tư pháp chấn động toàn quốc.*
- `t24_a2_28_prison_visitation_glass_partition_28`:
  - Shot `2-46` · `2.11#6` (5,1 s) · Cú · Host · mẫu T1 · camera `pull` — *Sự thật lịch sử cuối cùng đã được bóc trần dưới ánh sáng của khoa học và lương tri.*
- `t24_a2_29_shadowy_window_heavy_curtains_29`:
  - Shot `2-47` · `2.11#7` (9,3 s) · Cú · Host · mẫu T1 · camera `still` — *Các chuyên gia tâm lý học tội phạm đã bắt tay vào giải mã cấu trúc nhân cách của Lee Choon-jae: Một kẻ sát nhân hàng loạt kiểm soát quyền lực điển hìn…*
- `t24_a2_30_prison_visitation_glass_partition_30`:
  - Shot `2-48` · `2.11#8` (7,1 s) · Cú · Host · mẫu T1 · camera `pan` — *Đó là nơi bóng tối của sự tàn độc cá nhân gặp gỡ những lỗ hổng chết người của một hệ thống tư pháp non trẻ.*

### HỒI 3: GIẢI MÃ TÂM LÝ: KẺ SÁT NHÂN KIỂM SOÁT QUYỀN LỰC & NGHỊCH LÝ THÚ TỘI — 31 ảnh / 49 shot

- `t24_a3_01_forensic_investigation_desk_01`:
  - Shot `3-01` · `3.02#1` (12,2 s) · Cú · Host · mẫu T1 · camera `push` — *Hồ sơ Lee Choon-jae đã cung cấp cho ngành khoa học hành vi quốc tế một nghiên cứu điển hình về dạng tội phạm sát nhân hàng loạt kiểm soát quyền lực, h…*
  - Shot `3-02` · `3.02#2` (12,5 s) · Cú · Host · mẫu T1 · camera `pull` — *Khác với những kẻ giết người vì động cơ tài chính hay ảo giác tâm thần, loại tội phạm này tìm kiếm sự thỏa mãn tối thượng thông qua việc thống trị và …*
- `t24_a3_02_dark_detention_interrogation_room_02`:
  - Shot `3-03` · `3.02#3` (3,9 s) · Cú · Host · mẫu T1 · camera `still` — *Bề ngoài của Lee Choon-jae trong đời sống thường nhật hoàn toàn mờ nhạt.*
  - Shot `3-04` · `3.02#4` (8,5 s) · Cú · Host · mẫu T1 · camera `pan` — *Bộ não của hắn vận hành theo cơ chế chia ngăn nhận thức cực đoan: một bên là người em rể ngoan ngoãn, một bên là kẻ săn mồi máu lạnh.*
- `t24_a3_03_prison_cell_embroidery_desk_03`:
  - Shot `3-05` · `3.02#5` (8,6 s) · Cú · Host · mẫu T1 · camera `push` — *Nhưng bên dưới lớp vỏ bọc bình thường ấy là một thế giới nội tâm cuộn trào những ham muốn quyền lực bệnh hoạn và sự hung bạo bị dồn nén.*
  - Shot `3-06` · `3.03#1` (9,9 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Trong khung phân loại của Holmes và DeBurger, kẻ sát nhân kiểm soát quyền lực được mô tả là xem việc chi phối sự sống và cái chết của người khác như m…*
- `t24_a3_04_behavioral_science_study_desk_04`:
  - Shot `3-07` · `3.03#2` (4,6 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Khung lý thuyết này giả định rằng kẻ phạm tội thường cảm thấy mình thất bại trong cuộc sống hàng ngày.*
  - Shot `3-08` · `3.03#3` (6,0 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Để bù đắp cho cảm giác bất lực trong thực tế, kẻ phạm tội tìm kiếm cảm giác toàn năng bằng cách nhắm vào người yếu thế.*
- `t24_a3_05_behavioral_science_study_desk_05`:
  - Shot `3-09` · `3.03#4` (3,2 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Đó là cách giải thích thường được dùng cho những kẻ như Lee Choon-jae.*
  - Shot `3-10` · `3.03#5` (5,2 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Về mặt hành vi, cần phân biệt rạch ròi giữa thủ đoạn gây án và chữ ký tâm lý của hung thủ.*
- `t24_a3_06_behavioral_science_study_desk_06`:
  - Shot `3-11` · `3.03#6` (9,1 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Thủ đoạn gây án là việc hắn chọn bờ ruộng vắng, đêm tối và xóa dấu vết để tẩu thoát; nhưng chữ ký tâm lý lại là việc trói nạn nhân bằng chính vật dụng…*
  - Shot `3-12` · `3.03#7` (7,2 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Hành vi thắt nút ấy không nhằm phục vụ mục đích trốn chạy, mà là dấu ấn bệnh lý để khẳng định sự thống trị tuyệt đối lên thân xác nạn nhân.*
- `t24_a3_07_behavioral_science_study_desk_07`:
  - Shot `3-13` · `3.03#8` (8,3 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Sự lặp đi lặp lại của hành vi phạm tội qua mười bốn vụ án mạng không phải là nhu cầu sinh lý đơn thuần, mà là một cơn nghiện tâm lý nguy hiểm về sự th…*
  - Shot `3-14` · `3.03#9` (4,3 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Chuỗi hành vi ấy mang đặc điểm thường được mô tả trong khái niệm nhân cách chống đối xã hội.*
- `t24_a3_08_police_patrol_rural_search_08`:
  - Shot `3-15` · `3.04#1` (10,8 s) · Cú · Host · mẫu T1 · camera `still` — *Nhưng điều khiến giới tâm lý học kinh ngạc nhất ở Lee Choon-jae không chỉ là chuỗi hành vi trong quá khứ, mà là thái độ của hắn khi đối diện với cơ qu…*
  - Shot `3-16` · `3.04#2` (5,3 s) · Cú · Host · mẫu T1 · camera `pan` — *Thay vì lo sợ hay hối hận, hắn tỏ ra bình thản khi kể lại tội ác của mình.*
- `t24_a3_09_behavioral_science_study_desk_09`:
  - Shot `3-17` · `3.04#3` (7,7 s) · Cú · Host · mẫu T1 · camera `push` — *Hắn sử dụng kỹ thuật trung hòa đạo đức, xem việc tước đoạt mạng sống người khác như một phản xạ tự nhiên không thể kiềm chế.*
  - Shot `3-18` · `3.04#4` (7,4 s) · Cú · Host · mẫu T1 · camera `pull` — *Nghịch lý tâm lý này được các chuyên gia giải mã dưới góc độ của sự tự mãn khi hết thời hiệu truy tố.*
- `t24_a3_10_shadowy_window_heavy_curtains_10`:
  - Shot `3-19` · `3.05#1` (8,6 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Khi một kẻ sát nhân kiểm soát quyền lực nhận thức được rằng luật pháp không còn có thể trừng phạt thêm đối với hành vi của mình, cơ chế phòng vệ sợ hã…*
  - Shot `3-20` · `3.05#2` (4,7 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Thay vào đó, nhu cầu được công nhận quyền lực đen tối sẽ trỗi dậy mạnh mẽ hơn bao giờ hết.*
- `t24_a3_11_police_patrol_rural_search_11`:
  - Shot `3-21` · `3.05#3` (3,5 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Suốt ba mươi ba năm, Lee Choon-jae đã giữ kín bí mật ấy.*
  - Shot `3-22` · `3.05#4` (4,9 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Việc cảnh sát tìm đến với bằng chứng ADN có thể đã trở thành dịp để hắn bước ra ánh sáng.*
- `t24_a3_12_shadowy_window_heavy_curtains_12`:
  - Shot `3-23` · `3.05#5` (6,3 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Tội ác của Lee Choon-jae phát triển theo một chu kỳ ảo tưởng và quỹ đạo leo thang điển hình của kẻ sát nhân hàng loạt.*
  - Shot `3-24` · `3.05#6` (9,2 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Ban đầu chỉ là những hành vi rình mò, nhìn trộm và quấy rối; nhưng khi não bộ quen liều, hắn rơi vào trạng thái đói ảo tưởng và buộc phải leo thang sa…*
- `t24_a3_13_crime_scene_confession_sketch_13`:
  - Shot `3-25` · `3.05#7` (3,0 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Có ý kiến cho rằng hắn không thú tội vì lương tâm cắn rứt.*
  - Shot `3-26` · `3.05#8` (4,8 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Những sơ đồ hắn vẽ lại có thể được hiểu là cách hắn sống lại cảm giác kiểm soát năm xưa.*
- `t24_a3_14_behavioral_science_study_desk_14`:
  - Shot `3-27` · `3.05#9` (3,4 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Điều này mang đặc điểm thường được mô tả trong khái niệm ái kỷ ác tính.*
  - Shot `3-28` · `3.06#1` (5,4 s) · Cú · Host · mẫu T1 · camera `pan` — *Sự tự mãn lạnh lùng của Lee Choon-jae đã phơi bày bản chất lạnh lùng của một kẻ săn mồi.*
- `t24_a3_15_dark_detention_interrogation_room_15`:
  - Shot `3-29` · `3.06#2` (10,0 s) · Cú · Host · mẫu T1 · camera `push` — *Nhưng chính sự kiêu ngạo ấy đã vô tình trao lại chiếc chìa khóa công lý cho một người đàn ông vô tội đã phải chịu đựng nỗi oan khuất thấu tận trời xan…*
  - Shot `3-30` · `3.06#3` (7,1 s) · Cú · Host · mẫu T1 · camera `pull` — *Ảo tưởng quyền lực của kẻ thủ ác cuối cùng đã bị đánh sập trước sức mạnh bền bỉ của lòng kiên trinh và sự thật.*
- `t24_a3_16_crime_scene_confession_sketch_16`:
  - Shot `3-31` · `3.07#1` (9,2 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Trường hợp của Yoon Sung-yeo, người bị kết án oan trong vụ án số tám, là một minh chứng đau xót cho hiện tượng Lời thú tội cưỡng bức, hay Coerced Conf…*
  - Shot `3-32` · `3.07#2` (9,0 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Theo lời ông Yoon và kết luận sau này, ông đã bị đối xử hà khắc, không được ngủ và bị ép cung năm 1989, nên đã ký vào bản nhận tội giả.*
- `t24_a3_17_dark_detention_interrogation_room_17`:
  - Shot `3-33` · `3.07#3` (5,6 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Tâm lý con người khi bị đẩy vào giới hạn cùng cực có thể chấp nhận cáo buộc sai trái chỉ để chấm dứt áp lực trước mắt.*
  - Shot `3-34` · `3.07#4` (8,0 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Dưới sự tra tấn kéo dài và sự cô lập hoàn toàn, não bộ nạn nhân rơi vào trạng thái suy sụp ý chí và tê liệt khả năng phòng vệ nhận thức.*
- `t24_a3_18_dark_detention_interrogation_room_18`:
  - Shot `3-35` · `3.07#5` (7,8 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Khi nỗi đau thể xác vượt quá ngưỡng chịu đựng, bản năng sinh tồn ngắn hạn sẽ thôi thúc con người đầu hàng dù biết cái giá phải trả là danh dự cả đời.*
  - Shot `3-36` · `3.07#6` (8,5 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Để hiểu được tại sao một người vô tội như ông Yoon Sung-yeo lại chấp nhận ký vào bản nhận tội giết người, chúng ta phải nhìn thẳng vào giới hạn chịu đ…*
- `t24_a3_19_dark_detention_interrogation_room_19`:
  - Shot `3-37` · `3.07#7` (8,0 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Dưới sự tra tấn thể xác liên tục và ba ngày ba đêm bị tước đoạt giấc ngủ hoàn toàn, não bộ con người sẽ rơi vào trạng thái “Suy kiệt Tài nguyên Nhận t…*
- `t24_a3_20_behavioral_science_study_desk_20`:
  - Shot `3-38` · `3.07#8` (12,1 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Khi ấy, cơ chế “Chiết khấu Tương lai” sẽ chiếm lĩnh ý thức: nạn nhân không còn khả năng đo lường hậu quả của hai mươi năm tù ngục phía trước, mà chỉ k…*
- `t24_a3_21_shadowy_window_heavy_curtains_21`:
  - Shot `3-39` · `3.07#9` (7,0 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Ký vào bản nhận tội giả không phải là sự hèn nhát, mà là sự đầu hàng bi thảm của một cơ thể sinh học trước bạo lực vượt ngưỡng chịu đựng.*
- `t24_a3_22_dark_detention_interrogation_room_22`:
  - Shot `3-40` · `3.08#1` (7,5 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Đau đớn hơn cả, những người bức cung năm ấy không phải là những kẻ tội phạm đường phố, mà là những nhân viên công quyền nhân danh công lý.*
- `t24_a3_23_behavioral_science_study_desk_23`:
  - Shot `3-41` · `3.08#2` (10,9 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Dưới áp lực chỉ tiêu phá án nghẹt thở của thời đại, họ đã tự cho phép mình hạ thấp chuẩn mực đạo đức, biến một thanh niên tàn tật nghèo khổ thành vật …*
- `t24_a3_24_behavioral_science_study_desk_24`:
  - Shot `3-42` · `3.08#3` (12,6 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Sự tha hóa từng bước ấy là lời cảnh tỉnh muôn đời cho ngành tư pháp: khi công lý bị chi phối bởi áp lực thành tích và định kiến chủ quan, người thực t…*
- `t24_a3_25_dark_detention_interrogation_room_25`:
  - Shot `3-43` · `3.08#4` (4,1 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Lời thú nhận của Lee Choon-jae đã mở đường giải oan cho người bị hàm oan.*
- `t24_a3_26_behavioral_science_study_desk_26`:
  - Shot `3-44` · `3.08#5` (7,0 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Nó khẳng định rằng khoa học hình sự và đạo đức tư pháp phải luôn đi đôi với nhau để bảo vệ sự thật và quyền con người.*
- `t24_a3_27_suwon_courtroom_judicial_benches_27`:
  - Shot `3-45` · `3.08#6` (5,4 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Và phòng xử án tại Tòa án Suwon đã trở thành nơi chứng kiến khoảnh khắc công lý lịch sử được phục hồi.*
- `t24_a3_28_forensic_dna_laboratory_28`:
  - Shot `3-46` · `3.09#1` (8,2 s) · Cú · Host · mẫu T1 · camera `pull` — *Những phân tích tâm lý học pháp y đã khép lại bức tranh chân dung toàn diện về kẻ sát nhân Hwaseong và những bi kịch đi kèm.*
- `t24_a3_29_forensic_investigation_desk_29`:
  - Shot `3-47` · `3.09#2` (10,4 s) · Cú · Host · mẫu T1 · camera `still` — *Giờ là lúc cả đất nước Hàn Quốc hướng về phiên tòa tái thẩm lịch sử để trả lại danh dự cho người vô tội và chính thức khép lại trang hồ sơ u ám nhất t…*
- `t24_a3_30_behavioral_science_study_desk_30`:
  - Shot `3-48` · `3.09#3` (7,8 s) · Cú · Host · mẫu T1 · camera `pan` — *Đó là một phiên tòa không có án phạt mới cho kẻ thủ ác, nhưng mang lại sự thanh thản tối thượng cho lương tri của cả một dân tộc.*
- `t24_a3_31_behavioral_science_study_desk_31`:
  - Shot `3-49` · `3.09#4` (7,7 s) · Cú · Host · mẫu T1 · camera `push` — *Một khoảnh khắc mà sự thật và phẩm giá con người cuối cùng cũng giành lại vị thế thiêng liêng trước bóng tối của bạo quyền và sai lầm.*

### HỒI 4: PHIÊN TÒA GIẢI OAN THẾ KỶ & LỜI XIN LỖI CỦA CÔNG LÝ — 35 ảnh / 56 shot

- `t24_a4_01_dark_detention_interrogation_room_01`:
  - Shot `4-01` · `4.02#1` (7,5 s) · Cú · Host · mẫu T1 · camera `pull` — *Năm 2020, phiên tòa tái thẩm đã diễn ra tại Tòa án Quận Suwon thuộc tỉnh Gyeonggi.*
  - Shot `4-02` · `4.02#2` (10,9 s) · Cú · Host · mẫu T1 · camera `still` — *Ngồi ở hàng ghế bị cáo không phải là một tội phạm nguy hiểm, mà là ông Yoon Sung-yeo, người đàn ông năm mươi ba tuổi bị khuyết tật ở chân, sau hai mươ…*
- `t24_a4_02_busan_prison_steel_corridor_02`:
  - Shot `4-03` · `4.02#3` (11,4 s) · Cú · Host · mẫu T1 · camera `pan` — *Để làm sáng tỏ sự thật, tòa án đã triệu tập một nhân chứng đặc biệt: Lee Choon-jae, kẻ sát nhân đang thụ án chung thân, được áp giải từ nhà tù đến phò…*
  - Shot `4-04` · `4.02#4` (5,7 s) · Cú · Host · mẫu T1 · camera `push` — *Tháng 11 năm 2020, Lee Choon-jae lần đầu ra làm chứng công khai.*
- `t24_a4_03_dark_detention_interrogation_room_03`:
  - Shot `4-05` · `4.02#5` (4,4 s) · Cú · Host · mẫu T1 · camera `pull` — *Trước tòa, hắn khẳng định chính mình là thủ phạm của vụ án số tám.*
  - Shot `4-06` · `4.02#6` (9,2 s) · Cú · Host · mẫu T1 · camera `still` — *Lần đầu tiên sau hơn ba thập kỷ, kẻ sát nhân thật sự và người bị hàm oan ngồi cách nhau chỉ vài mét trong cùng một căn phòng xử án.*
- `t24_a4_04_dark_detention_interrogation_room_04`:
  - Shot `4-07` · `4.02#7` (8,0 s) · Cú · Host · mẫu T1 · camera `pan` — *Lời tuyên bố đanh thép ấy vang lên giữa sự im lặng tuyệt đối của phòng xử án, làm rung động trái tim của nhiều người dân Hàn Quốc.*
  - Shot `4-08` · `4.04#1` (6,2 s) · Cú · Host · mẫu T1 · camera `push` — *Ngày 17 tháng 12 năm 2020, tòa án tuyên ông Yoon Sung-yeo vô tội.*
- `t24_a4_05_suwon_courtroom_judicial_benches_05`:
  - Shot `4-09` · `4.04#2` (7,0 s) · Cú · Host · mẫu T1 · camera `pull` — *Hội đồng xét xử đã công khai xin lỗi ông Yoon vì những sai lầm nghiêm trọng của hệ thống tư pháp năm xưa.*
  - Shot `4-10` · `4.04#3` (10,0 s) · Cú · Host · mẫu T1 · camera `still` — *Sau hơn ba mươi năm mang trên mình bản án kẻ giết người, ông cuối cùng đã có thể ngẩng cao đầu bước ra khỏi tòa án trong tư cách của một công dân tron…*
- `t24_a4_06_dark_detention_interrogation_room_06`:
  - Shot `4-11` · `4.04#4` (8,8 s) · Cú · Host · mẫu T1 · camera `pan` — *Những giọt nước mắt lăn dài trên gò má nhăn nheo của người đàn ông đã dành trọn nửa đời người để đấu tranh đòi lại tên tuổi của chính mình.*
  - Shot `4-12` · `4.04#5` (5,0 s) · Cú · Host · mẫu T1 · camera `push` — *Phán quyết ấy đã khép lại một trong những vụ án oan đau đớn nhất lịch sử hiện đại.*
- `t24_a4_07_police_patrol_rural_search_07`:
  - Shot `4-13` · `4.06#1` (8,9 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Tháng 7 năm 2020, khi công bố kết quả điều tra cuối cùng, Giám đốc Cảnh sát tỉnh Gyeonggi Nambu Bae Yong-ju đã tổ chức họp báo.*
  - Shot `4-14` · `4.06#2` (2,4 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Ông đã cúi đầu đưa ra lời xin lỗi công khai.*
- `t24_a4_08_police_patrol_rural_search_08`:
  - Shot `4-15` · `4.06#3` (6,7 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Lời xin lỗi gửi tới các nạn nhân và gia đình của họ, vì cảnh sát đã không tìm ra sự thật sớm hơn.*
  - Shot `4-16` · `4.06#4` (6,2 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Lời xin lỗi cũng gửi tới ông Yoon Sung-yeo và những người từng bị đối xử sai trái trong quá trình điều tra năm xưa.*
- `t24_a4_09_police_patrol_rural_search_09`:
  - Shot `4-17` · `4.06#5` (6,9 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Trước ống kính truyền hình cả nước, các sĩ quan cảnh sát thế hệ sau đã gập mình tạ tội trước nỗi đau khôn nguôi của người dân.*
  - Shot `4-18` · `4.06#6` (8,3 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Đó là một khoảnh khắc đau xót nhưng vô cùng cần thiết để lực lượng cảnh sát đối diện với lịch sử và xây dựng lại niềm tin đã mất trong lòng nhân dân.*
- `t24_a4_10_police_patrol_rural_search_10`:
  - Shot `4-19` · `4.06#7` (7,8 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Lời xin lỗi muộn màng ấy là minh chứng cho thấy công lý dù có đến muộn màng nhưng sự thật thì không bao giờ có thể bị bóp méo vĩnh viễn.*
  - Shot `4-20` · `4.07#1` (11,2 s) · Cú · Host · mẫu T1 · camera `push` — *Ba mươi năm đè nén, ba mươi năm bưng bít sai lầm, điều gì đã thúc đẩy những người đứng đầu lực lượng cảnh sát cúi gập mình tạ tội trước nhân dân trong…*
- `t24_a4_11_police_patrol_rural_search_11`:
  - Shot `4-21` · `4.07#2` (6,4 s) · Cú · Host · mẫu T1 · camera `pull` — *Đâu là cơ chế tâm lý thực sự đã phá vỡ bức tường im lặng kiên cố của một hệ thống công quyền?*
  - Shot `4-22` · `4.08#1` (10,5 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Sự thức tỉnh và hối hận của lực lượng cảnh sát trong hồ sơ Hwaseong xuất phát từ sự sụp đổ hoàn toàn của cơ chế “Tự Huyễn hoặc Nhận thức” trước sức mạ…*
- `t24_a4_12_police_patrol_rural_search_12`:
  - Shot `4-23` · `4.08#2` (6,9 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Suốt ba thập kỷ, những người điều tra năm xưa có thể đã tự an ủi lương tâm rằng họ chỉ vô tình phạm sai sót nghiệp vụ.*
  - Shot `4-24` · `4.08#3` (9,9 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Nhưng khi ADN của Lee Choon-jae trùng khớp tuyệt đối, và khi chính kẻ sát nhân mô tả tường tận vụ án số tám mà không cần tài liệu, bức tường ngụy biện…*
- `t24_a4_13_police_patrol_rural_search_13`:
  - Shot `4-25` · `4.08#4` (10,0 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Các sĩ quan cảnh sát phải đối diện trực diện với “Chấn thương Đạo đức” — trạng thái sụp đổ nhân cách khi nhận ra chính đôi bàn tay mình đã gián tiếp h…*
- `t24_a4_14_official_police_press_conference_14`:
  - Shot `4-26` · `4.08#5` (10,9 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Lời xin lỗi công khai và cái cúi đầu gập mình trước ống kính không chỉ là một hành vi trách nhiệm pháp lý, mà là một nhu cầu tâm lý bức thiết để giải …*
  - Shot `4-27` · `4.10#1` (8,0 s) · Cú · Host · mẫu T1 · camera `pan` — *Lee Choon-jae không thể bị tuyên thêm bản án mới do thời hiệu truy tố đã hết hạn từ năm 2006.*
- `t24_a4_15_suwon_courtroom_judicial_benches_15`:
  - Shot `4-28` · `4.10#2` (5,6 s) · Cú · Host · mẫu T1 · camera `push` — *Nhưng hắn vẫn đang chấp hành bản án tù chung thân cho vụ án năm 1994.*
  - Shot `4-29` · `4.10#3` (9,9 s) · Cú · Host · mẫu T1 · camera `pull` — *Bản án của tòa án có thể bị giới hạn bởi thời hiệu, nhưng bản án của lương tâm và lịch sử sẽ vĩnh viễn khắc ghi tên hắn như một vết nhơ muôn đời.*
- `t24_a4_16_hall_of_justice_marble_corridor_16`:
  - Shot `4-30` · `4.10#4` (5,2 s) · Cú · Host · mẫu T1 · camera `still` — *Hãy hình dung những gì một người bạn lâu năm của ông Yoon chứng kiến suốt hành trình ấy.*
  - Shot `4-31` · `4.11#1` (5,1 s) · N · mẫu T1 · camera `pan` — *Suốt hơn ba mươi năm, cuộc đời của ông Yoon giống như một chuỗi ngày dài tăm tối.*
- `t24_a4_17_hall_of_justice_marble_corridor_17`:
  - Shot `4-32` · `4.11#2` (8,1 s) · N · mẫu T1 · camera `push` — *Ông chỉ là một thanh niên nghèo làm việc tại tiệm sửa chữa nông cụ, bị khuyết tật ở chân, thế nhưng đã bị ép nhận tội thay cho kẻ khác.*
  - Shot `4-33` · `4.11#3` (6,6 s) · N · mẫu T1 · camera `pull` — *Ông đã phải ngồi tù hai mươi năm, mất đi tuổi trẻ, và khi ra tù vẫn phải sống dưới ánh mắt kỳ thị.*
- `t24_a4_18_hall_of_justice_marble_corridor_18`:
  - Shot `4-34` · `4.11#4` (5,0 s) · N · mẫu T1 · camera `still` — *Nhưng niềm tin vào sự trong sạch của bản thân đã giúp ông chờ đợi ngày sự thật được phơi bày.*
  - Shot `4-35` · `4.11#5` (5,6 s) · N · mẫu T1 · camera `pan` — *Giây phút tòa tuyên ông vô tội, tảng đá đè nặng suốt hơn nửa đời người cuối cùng đã được dỡ bỏ.*
- `t24_a4_19_hall_of_justice_marble_corridor_19`:
  - Shot `4-36` · `4.11#6` (3,8 s) · N · mẫu T1 · camera `push` — *Không khoản bồi thường nào có thể bù đắp lại hai mươi năm thanh xuân bị cướp mất.*
  - Shot `4-37` · `4.11#7` (3,4 s) · N · mẫu T1 · camera `pull` — *Nhưng điều quan trọng nhất là danh dự của ông đã được phục hồi.*
- `t24_a4_20_dark_detention_interrogation_room_20`:
  - Shot `4-38` · `4.11#8` (6,5 s) · N · mẫu T1 · camera `still` — *Ông muốn nhắn nhủ rằng dù trong hoàn cảnh tăm tối nhất, xin đừng bao giờ từ bỏ niềm tin vào lẽ phải và công lý.*
  - Shot `4-39` · `4.11#9` (4,7 s) · N · mẫu T1 · camera `pan` — *Hy vọng rằng sẽ không còn người vô tội nào phải trải qua nỗi oan khuất như ông.*
- `t24_a4_21_police_patrol_rural_search_21`:
  - Shot `4-40` · `4.11#10` (11,4 s) · N · mẫu T1 · camera `push` — *Khi đứng trong phòng xử án năm 2020, nhìn thấy người điều tra năm xưa cúi đầu rơi nước mắt trước mặt mình, ngọn lửa uất hận trong lòng tôi dường như t…*
  - Shot `4-41` · `4.11#11` (8,9 s) · N · mẫu T1 · camera `pull` — *Tôi nhận ra rằng sự thù hận không thể mang hai mươi năm thanh xuân đã mất quay trở lại, mà chỉ tiếp tục giam cầm tâm hồn tôi trong ngục tối của quá kh…*
- `t24_a4_22_official_police_press_conference_22`:
  - Shot `4-42` · `4.11#12` (10,9 s) · N · mẫu T1 · camera `still` — *Lời xin lỗi muộn màng của họ, dù không thể bù đắp những trận đòn roi trong đêm lạnh năm 1989, nhưng đã trả lại cho tôi phẩm giá thiêng liêng của một c…*
  - Shot `4-43` · `4.11#13` (10,7 s) · N · mẫu T1 · camera `pan` — *Tôi tha thứ không phải vì tội lỗi ấy có thể dễ dàng xóa bỏ, mà là để giải thoát cho chính mình và để những người lầm lạc có cơ hội được chuộc lại phần…*
- `t24_a4_23_hall_of_justice_marble_corridor_23`:
  - Shot `4-44` · `4.12#1` (5,4 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Vụ án Hwaseong là một trong những vụ án gắn liền với các cuộc tranh luận về cải cách tư pháp tại Hàn Quốc.*
- `t24_a4_24_hall_of_justice_marble_corridor_24`:
  - Shot `4-45` · `4.12#2` (8,9 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Năm 2015, Quốc hội Hàn Quốc thông qua Đạo luật Taewan, bãi bỏ thời hiệu truy tố đối với các tội giết người có thể bị tử hình.*
- `t24_a4_25_hall_of_justice_marble_corridor_25`:
  - Shot `4-46` · `4.12#3` (6,0 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Điều này đồng nghĩa với việc những kẻ phạm tội như vậy có thể bị truy tố bất kể thời gian trôi qua bao lâu.*
- `t24_a4_26_hall_of_justice_marble_corridor_26`:
  - Shot `4-47` · `4.12#4` (8,0 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Đạo luật này là bước ngoặt pháp lý lịch sử, khẳng định rằng không bao giờ có vùng an toàn thời gian cho những tội ác cướp đi mạng sống con người.*
- `t24_a4_27_claustrophobic_interrogation_room_27`:
  - Shot `4-48` · `4.12#5` (5,6 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Đồng thời, việc ghi âm, ghi hình thẩm vấn ngày càng được áp dụng rộng rãi để ngăn ép cung.*
- `t24_a4_28_hall_of_justice_marble_corridor_28`:
  - Shot `4-49` · `4.12#6` (4,7 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Đó là sự tiến bộ được đánh đổi bằng nước mắt và nỗi đau thương của cả một thế hệ.*
- `t24_a4_29_police_patrol_rural_search_29`:
  - Shot `4-50` · `4.13#1` (9,7 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Bài học lớn nhất từ hồ sơ Lee Choon-jae là lời cảnh tỉnh về sự nguy hiểm của việc điều tra dựa trên định kiến chủ quan và sự tự tin mù quáng vào các s…*
- `t24_a4_30_forensic_dna_laboratory_30`:
  - Shot `4-51` · `4.13#2` (8,6 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Khoa học pháp y hiện đại, đặc biệt là công nghệ ADN và kỹ thuật phác họa chân dung tâm lý học tội phạm, là những công cụ sống còn để bảo vệ sự thật kh…*
- `t24_a4_31_hall_of_justice_marble_corridor_31`:
  - Shot `4-52` · `4.13#3` (6,3 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Một nền tư pháp tiến bộ phải luôn biết hoài nghi các phán đoán chủ quan và tuyệt đối tôn trọng các chứng cứ vật chất độc lập.*
- `t24_a4_32_hall_of_justice_marble_corridor_32`:
  - Shot `4-53` · `4.13#4` (7,8 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Sự kết hợp giữa đạo đức nghề nghiệp và khoa học chính xác là nền tảng vững chắc nhất để ngăn ngừa tội ác và bảo vệ phẩm giá của những người vô tội.*
- `t24_a4_33_hall_of_justice_marble_corridor_33`:
  - Shot `4-54` · `4.14#1` (3,1 s) · Cú · Host · mẫu T1 · camera `still` — *Ba mươi ba năm trong sương mù đã chính thức khép lại.*
- `t24_a4_34_hall_of_justice_marble_corridor_34`:
  - Shot `4-55` · `4.14#2` (9,7 s) · Cú · Host · mẫu T1 · camera `pan` — *Tên tuổi và nhân phẩm của những người phụ nữ xấu số năm xưa cuối cùng đã được trả lại sự trong sạch và tôn kính mà họ xứng đáng được nhận.*
- `t24_a4_35_hall_of_justice_marble_corridor_35`:
  - Shot `4-56` · `4.14#3` (8,9 s) · Cú · Host · mẫu T1 · camera `push` — *Nhưng những bài học về an toàn cộng đồng và sự cảnh giác trước những kẻ thủ ác ẩn mình thì vẫn luôn là di sản vô giá cần được khắc sâu.*

### HỒI 5: BÀI HỌC CẢNH TỈNH & 4 CẢNH BÁO ĐỎ PHÒNG NGỪA TỘI PHẠM SĂN MỒI BAN ĐÊM — 22 ảnh / 35 shot

- `t24_a5_01_modern_hwaseong_smart_security_dawn_01`:
  - Shot `5-01` · `5.02#1` (6,6 s) · Cú · Host · mẫu T1 · camera `pull` — *Ngày hôm nay, vùng nông thôn Hwaseong năm xưa đã trở thành một thành phố hiện đại của tỉnh Gyeonggi.*
  - Shot `5-02` · `5.02#2` (4,1 s) · Cú · Host · mẫu T1 · camera `still` — *Ký ức về những người phụ nữ xấu số vẫn còn đó trong lòng người dân.*
- `t24_a5_02_modern_hwaseong_smart_security_dawn_02`:
  - Shot `5-03` · `5.02#3` (7,1 s) · Cú · Host · mẫu T1 · camera `pan` — *Nỗi đau thương của quá khứ là lời nhắc về tầm quan trọng của chiếu sáng và an ninh trên những con đường vắng.*
  - Shot `5-04` · `5.02#4` (9,1 s) · Cú · Host · mẫu T1 · camera `push` — *Những con đường liên thôn từng chìm trong bóng tối nay đã được thắp sáng rực rỡ bởi hệ thống đèn đường và camera an ninh hiện đại.*
- `t24_a5_03_police_patrol_rural_search_03`:
  - Shot `5-05` · `5.02#5` (10,5 s) · Cú · Host · mẫu T1 · camera `pull` — *Ký ức về vụ án không phải để gieo rắc sự sợ hãi, mà là ngọn đuốc soi đường cho ý thức cảnh giác và sự đoàn kết bảo vệ sự an toàn của cộng đồng.*
  - Shot `5-06` · `5.03#1` (8,7 s) · Sói · Điều tra viên · mẫu T1 · camera `still` — *Dưới góc độ thực thi pháp luật, bài học sâu sắc nhất là lực lượng cảnh sát phải luôn giữ vững tinh thần trách nhiệm và không bao giờ được phép tự mãn …*
- `t24_a5_04_forensic_dna_laboratory_04`:
  - Shot `5-07` · `5.03#2` (8,3 s) · Sói · Điều tra viên · mẫu T1 · camera `pan` — *Sự phát triển không ngừng của khoa học công nghệ giám định hình sự chính là vũ khí tối thượng giúp chúng ta lật lại những vụ án bế tắc trong quá khứ.*
  - Shot `5-08` · `5.03#3` (8,5 s) · Sói · Điều tra viên · mẫu T1 · camera `push` — *Mọi mẫu vật chứng dù là nhỏ nhất cũng cần được bảo quản cẩn trọng, bởi vì khoa học tương lai sẽ có thể giải mã những điều mà hôm nay ta chưa làm được.*
- `t24_a5_05_forensic_investigation_desk_05`:
  - Shot `5-09` · `5.03#4` (6,0 s) · Sói · Điều tra viên · mẫu T1 · camera `pull` — *Những hồ sơ án mạng chưa có lời giải vẫn cần được rà soát để mọi tội ác đều phải trả giá trước pháp luật.*
  - Shot `5-10` · `5.04#1` (7,6 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Những kẻ phạm tội săn mồi ban đêm thường tận dụng sự cô lập địa lý, bóng tối và sự lơ là mất cảnh giác của nạn nhân để thực hiện hành vi bạo lực.*
- `t24_a5_06_dark_isolated_sidewalk_night_06`:
  - Shot `5-11` · `5.04#2` (6,9 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Chúng thường có xu hướng thăm dò địa hình từ trước, quan sát thói quen sinh hoạt và chọn những thời điểm nạn nhân yếu thế nhất để ra tay.*
  - Shot `5-12` · `5.04#3` (9,4 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Tâm lý học hành vi chỉ ra rằng bản năng sinh tồn và trực giác bất an của con người là một món quà tiến hóa vô giá để cảnh báo nguy hiểm trước khi não …*
- `t24_a5_07_modern_hwaseong_smart_security_dawn_07`:
  - Shot `5-13` · `5.04#4` (8,7 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Việc nâng cao ý thức tự bảo vệ bản thân, thay đổi lộ trình di chuyển và tránh đi một mình qua các khu vực vắng vẻ vào ban đêm là những kỹ năng sinh tồ…*
  - Shot `5-14` · `5.04#5` (8,3 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `still` — *Sự quan tâm, hỗ trợ của gia đình và việc xây dựng những cộng đồng dân cư gắn kết chính là bức tường thành vững chắc nhất ngăn chặn bước chân của kẻ th…*
- `t24_a5_08_forensic_investigation_desk_08`:
  - Shot `5-15` · `5.04#6` (8,7 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pan` — *Hồ sơ Lee Choon-jae khép lại không chỉ bằng chiến thắng của công nghệ ADN, mà bằng sự trỗi dậy của lòng trắc ẩn và sự dũng cảm đối diện với sự thật củ…*
  - Shot `5-16` · `5.04#7` (8,3 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `push` — *Một xã hội trưởng thành không phải là một xã hội không bao giờ phạm sai lầm, mà là một xã hội dám nhìn thẳng vào vết sẹo của chính mình để cải cách và…*
- `t24_a5_09_dark_detention_interrogation_room_09`:
  - Shot `5-17` · `5.04#8` (13,3 s) · Cáo · Chuyên gia tâm lý · mẫu T1 · camera `pull` — *Sự tự do và danh dự của ông Yoon Sung-yeo là lời nhắc nhở thiêng liêng rằng: giá trị tối thượng của công lý không nằm ở bản án trừng phạt kẻ ác, mà nằ…*
- `t24_a5_10_rain_drenched_crossroad_10`:
  - Shot `5-18` · `5.05#1` (16,5 s) · Cú · Host · mẫu T1 · camera `still` — *Để giúp quý vị khán giả, đặc biệt là phụ nữ và các bạn trẻ, nâng cao cảnh giác và bảo vệ an toàn cho bản thân khi di chuyển vào ban đêm, kênh Amber Ey…*
  - Shot `5-19` · `5.05#2` (7,6 s) · Cú · Host · mẫu T1 · camera `pan` — *Dấu hiệu thứ nhất: Thói quen di chuyển một mình trên những cung đường cố định qua các khu vực hẻo lánh và thiếu ánh sáng.*
- `t24_a5_11_modern_hwaseong_smart_security_dawn_11`:
  - Shot `5-20` · `5.05#3` (9,1 s) · Cú · Host · mẫu T1 · camera `push` — *Những kẻ săn mồi thường kiên nhẫn theo dõi lịch trình sinh hoạt hàng ngày của mục tiêu để tìm ra những khoảng thời gian và địa điểm sơ hở nhất.*
  - Shot `5-21` · `5.05#4` (8,8 s) · Cú · Host · mẫu T1 · camera `pull` — *Hãy luôn chủ động thay đổi lộ trình, tránh đi qua những con đường mòn tối tăm và luôn thông báo lịch trình di chuyển cho người thân khi phải về muộn.*
- `t24_a5_12_night_street_creeping_silhouette_12`:
  - Shot `5-22` · `5.05#5` (7,4 s) · Cú · Host · mẫu T1 · camera `still` — *Dấu hiệu thứ hai: Linh cảm về sự hiện diện của một đối tượng bám đuôi hoặc xuất hiện trùng hợp nhiều lần trên đường về nhà.*
  - Shot `5-23` · `5.05#6` (9,9 s) · Cú · Host · mẫu T1 · camera `pan` — *Nếu bạn phát hiện có bóng người đi theo phía sau, có xe máy hoặc ô tô chạy chậm lại bất thường bên cạnh, tuyệt đối không được chủ quan hay giả vờ như …*
- `t24_a5_13_police_patrol_rural_search_13`:
  - Shot `5-24` · `5.05#7` (10,0 s) · Cú · Host · mẫu T1 · camera `push` — *Hãy lập tức di chuyển nhanh về phía những nơi có ánh sáng, có cửa hàng tiện lợi hoặc có đông người qua lại và gọi điện thoại ngay cho người thân hoặc …*
  - Shot `5-25` · `5.05#8` (8,2 s) · Cú · Host · mẫu T1 · camera `pull` — *Dấu hiệu thứ ba: Sự lơ là mất cảnh giác khi sử dụng tai nghe hoặc điện thoại di động khi đang đi bộ một mình trong đêm.*
- `t24_a5_14_empty_subway_underpass_14`:
  - Shot `5-26` · `5.05#9` (11,3 s) · Cú · Host · mẫu T1 · camera `still` — *Việc đeo tai nghe âm lượng lớn hoặc mải mê nhìn vào màn hình điện thoại sẽ làm triệt tiêu hoàn toàn khả năng nghe nhìn và phản xạ tự nhiên của bạn trư…*
  - Shot `5-27` · `5.05#10` (7,2 s) · Cú · Host · mẫu T1 · camera `pan` — *Hãy luôn giữ đôi mắt quan sát, đôi tai lắng nghe và luôn ở trong trạng thái sẵn sàng phản ứng trước mọi tình huống bất ngờ.*
- `t24_a5_15_shadowy_window_heavy_curtains_15`:
  - Shot `5-28` · `5.05#11` (7,8 s) · Cú · Host · mẫu T1 · camera `push` — *Dấu hiệu thứ tư: Những thói quen sinh hoạt bất thường và hành vi bạo lực âm thầm của những người quen biết trong môi trường xung quanh.*
- `t24_a5_16_shadowy_window_heavy_curtains_16`:
  - Shot `5-29` · `5.05#12` (7,3 s) · Cú · Host · mẫu T1 · camera `pull` — *Theo báo chí Hàn Quốc, Lee Choon-jae từng có hành vi bạo lực gia đình trước khi bị bắt năm 1994.*
- `t24_a5_17_dark_detention_interrogation_room_17`:
  - Shot `5-30` · `5.05#13` (10,6 s) · Cú · Host · mẫu T1 · camera `still` — *Khi một người xung quanh bộc lộ xu hướng kiểm soát cực đoan, sự hung bạo với phụ nữ hoặc động vật, đó là một nhân cách tiềm ẩn nguy cơ bùng phát tội p…*
- `t24_a5_18_modern_hwaseong_smart_security_dawn_18`:
  - Shot `5-31` · `5.05#14` (8,6 s) · Cú · Host · mẫu T1 · camera `pan` — *Nhận diện sớm những vi tín hiệu bất thường ấy và kiên quyết vạch rõ ranh giới an toàn là chiếc khiên bảo vệ vững chắc nhất cho chính bạn.*
- `t24_a5_19_modern_hwaseong_smart_security_dawn_19`:
  - Shot `5-32` · `5.05#15` (9,6 s) · Cú · Host · mẫu T1 · camera `push` — *Sự an toàn của mỗi người phụ nữ khi trở về nhà sau một ngày làm việc phải luôn là tiêu chuẩn tối thiểu của một xã hội văn minh và bình yên.*
- `t24_a5_20_forensic_investigation_desk_20`:
  - Shot `5-33` · `5.05#16` (9,4 s) · Cú · Host · mẫu T1 · camera `pull` — *Cảm ơn quý vị đã dành thời gian đồng hành cùng Amber Eyes trong tập hồ sơ tâm lý học tội phạm đầy day dứt và mang đậm giá trị nhân văn ngày hôm nay.*
- `t24_a5_21_modern_hwaseong_smart_security_dawn_21`:
  - Shot `5-34` · `5.05#17` (10,4 s) · Cú · Host · mẫu T1 · camera `still` — *Hãy nhấn nút đăng ký kênh, bật chuông thông báo và chia sẻ video ý nghĩa này đến những người thân xung quanh bạn để cùng nhau lan tỏa ý thức an toàn t…*
- `t24_a5_22_forensic_investigation_desk_22`:
  - Shot `5-35` · `5.05#18` (4,5 s) · Cú · Host · mẫu T1 · camera `pan` — *Xin chào tạm biệt và hẹn gặp lại quý vị trong những tập hồ sơ tiếp theo.*

---

## III. QC NỘI DUNG ẢNH (H2 / H19 / H26) — ĐÃ BÁO CÁO, NGƯỜI DÙNG CHỐT GIỮ NGUYÊN

| Nhóm | Số ảnh | Vấn đề |
|---|:---:|---|
| **A** — chữ AI đọc được rõ | 57 | Biển `POLICE`, xe cảnh sát có chữ, tờ giấy/màn hình có chữ (vi phạm H2/H26) |
| **B** — dấu hiệu chữ / pseudo-text | 22 | Chữ quá nhỏ hoặc giả chữ |
| **F** — lộ mặt | 5 | Vi phạm mục 6 AGENTS (nhân vật nền phải bị che/khuất) |
| **C** — sai bối cảnh (H19) | 1 | `t24_a4_28` có biển `CALIFORNIA` — toà án Mỹ trong vụ án Hwaseong (Hàn Quốc) |

Chi tiết từng ảnh: [`BAO_CAO_QC_ANH_NEN_TAP24_H26_20261125.md`](BAO_CAO_QC_ANH_NEN_TAP24_H26_20261125.md).

> **Quyết định người dùng (25/11/2026):** giữ nguyên toàn bộ 155 ảnh nền hiện có, không sinh lại ảnh nào. Hệ quả trực tiếp: mục 4 của cổng `qc_bg_mapping.py` (22/155 ảnh dùng prompt chung thay vì prompt riêng) chưa thể đóng — cần ghi nhận ngoại lệ này trong hồ sơ phát hành.

---

## IV. KẾT LUẬN & ĐỀ XUẤT SẢN XUẤT

1. **Đồng bộ kịch bản:** 246 shot phủ đúng 246 câu thoại của Tập 24; mã câu `1.02#1` … `5.05#18` trùng khớp 100% giữa VN / EN / JA.
2. **Bảo toàn pháp lý & bản quyền thương mại:** toàn bộ ảnh tạo nội bộ bằng Cloudflare Workers AI FLUX, 100% tự chủ, không dùng tài sản bên thứ ba.
3. **Sẵn sàng dựng video:** bộ ảnh lưu tại `assets/bg/t24_*.png` (155 file, 2112×1188); contact sheet tại `02_SAN_XUAT/Ho_So_Toi_Pham/Tap24/contact_sheet_t24.png`.
4. **Thời lượng:** VN 2203,30 s · EN 2137,38 s · JA 2444,66 s — khớp đúng thời lượng master audio từng ngôn ngữ (timeline dựng lại từ SRT, sai số 0,000 s).
5. **Ngoại lệ cần ghi nhận:** H26 (khung hình không có chữ) chưa đạt trên 81/155 ảnh; H10 (shot 3–15 s) có 4/246 shot VN, 2/246 EN, 4/246 JA vượt 15 s do câu thoại dài.
6. **Quyết định của người dùng:**
   - 25/11/2026 — Giữ nguyên 155 ảnh nền ⇒ chấp nhận ngoại lệ H26 và M4 của `qc_bg_mapping.py` (22/155 prompt mẫu chung).
   - 25/11/2026 — Chấp nhận lỗi tiêu đề đỏ ở intro JA (8 ô vuông thiếu glyph, lỗi có sẵn trong `intro_kenh_JA_t18.mov` dùng chung Tập 16/17/18); nội dung intro tiếng Nhật hiển thị đúng.
   - 26/11/2026 — **Dựng lại cả 3 video, tuần tự từng video, bắt buộc có dải sóng giọng nói.** Đã dùng `make_pseudo_stems.py` (chuẩn dự án #186, cùng cơ chế Tập 11/T13–T18) → cổng H24 `qc_wave_gate.py` **ĐẠT cả 3 ngôn ngữ** (chạm trần 1,5–3,2 %, lệch chuẩn 0,25–0,28, p95 0,90) → dựng lại 6 lô/ngôn ngữ → đóng gói lại → verify `_verify_final_t24.py` **ĐẠT**; trích 3 khung liên tiếp trong 1 câu thoại từ `*_master.mp4` xác nhận **dải sóng đổi hình giữa các khung**. Không tốn credit, không đổi giọng, không sửa `build_video3.py`. A14 vẫn kiểm bằng cổng thay thế `qc_master_voice_presence.py` (ĐẠT cả 3 ngôn ngữ) — ghi rõ là **kiểm thay thế**, vì stem giả còn lẫn nhạc/SFX trong cửa sổ câu.
