"""Thiết kế 20 ảnh nền bổ sung cho Tập 16 (Hồ sơ John List - Thảm kịch biệt thự Breeze Knoll)
Đưa tổng số ảnh nền từ 63 lên 83 ảnh (tỷ lệ chuẩn ~3.1 câu/ảnh, phân bổ đều 5 hồi,
loại bỏ hoàn toàn tình trạng dùng lại nền khi dựng hình theo kịch bản 257 câu).
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT / ".work"

new_20_jobs_tap16 = [
    # -------------------------------------------------------------------------
    # HỒI 1: Bổ sung 4 ảnh (12 -> 16 ảnh)
    # Bối cảnh sâu: Lò sưởi cổ điển, bàn ăn bày biện sẵn, hộp thư tuyết phủ, gác mái bà Alma
    # -------------------------------------------------------------------------
    {
        "name": "t16_breeze_knoll_snowy_porch_mail",
        "act": 1,
        "sentences": "1.02#4–#6",
        "desc": "Thềm hiên trước biệt thự Breeze Knoll ngập trong tuyết trắng tháng 12, chồng báo The Star-Ledger và thư từ ố vàng chất đống không ai nhặt, đèn hiên sáng cô độc giữa màn đêm đông.",
        "prompt": "Grim exterior shot of a Victorian mansion front porch covered in thick untouched winter snow, tall stack of uncollected yellowed newspapers and envelopes piling up beside a locked wooden front door, solitary warm porch light casting long eerie shadows into the freezing New Jersey night, quiet foreboding mystery noir."
    },
    {
        "name": "t16_breeze_knoll_grand_ballroom_empty",
        "act": 1,
        "sentences": "1.04#7–#9",
        "desc": "Phòng khiêu vũ rộng lớn dưới mái vòm kính màu Tiffany tuyệt đẹp, sàn gỗ bóng loáng hoang vắng trong tĩnh lặng rợn người, ánh sáng u tối lọt qua khung cửa sổ cao vút.",
        "prompt": "Eerie low-angle interior wide shot of an expansive abandoned Victorian grand ballroom inside Breeze Knoll mansion, high vaulted ceiling featuring an authentic Tiffany stained glass skylight casting muted jewel-toned shadows onto a cold polished hardwood floor, chilling atmospheric quiet, David Fincher psychological dread noir."
    },
    {
        "name": "t16_breeze_knoll_attic_staircase_shadows",
        "act": 1,
        "sentences": "1.06#5–#7",
        "desc": "Cầu thang gỗ hẹp dẫn lên căn hộ áp mái biệt lập của bà mẹ Alma List, bóng tối sâu thẳm ngăn cách thế giới của người mẹ già với phần còn lại của tòa nhà.",
        "prompt": "Claustrophobic interior view looking up a steep, narrow wooden staircase leading into the pitch-black attic of an old mansion, solitary dim incandescent bulb dangling from the ceiling, ominous vertical chiaroscuro shadows, psychological alienation aesthetic."
    },
    {
        "name": "t16_forensic_ballistics_evidence_markers",
        "act": 1,
        "sentences": "1.10#4–#6",
        "desc": "Các thẻ số bằng chứng hình sự màu vàng đặt cạnh vỏ đạn súng lục cỡ nòng 22 và 9mm trên sàn gỗ phòng khách, ánh đèn pin nghiệp vụ quét qua bề mặt lạnh lẽo.",
        "prompt": "Forensic close-up still life of yellow numbered evidence markers placed beside spent .22 caliber and 9mm brass bullet casings on a dark polished parquet floor, beam of an investigative flashlight cutting across harsh shadows, solemn crime scene investigation noir."
    },

    # -------------------------------------------------------------------------
    # HỒI 2: Bổ sung 4 ảnh (11 -> 15 ảnh)
    # Bối cảnh sâu: Album gia đình bị khoét mặt, chiếc xe Chevrolet tại sân bay JFK, hòm thư bưu điện
    # -------------------------------------------------------------------------
    {
        "name": "t16_carved_family_album_empty_silhouettes",
        "act": 2,
        "sentences": "2.04#3–#5",
        "desc": "Trang album ảnh bọc da gia đình mở ra trên bàn gỗ, toàn bộ vị trí khuôn mặt người cha John List đã bị lưỡi kéo khoét thủng thành những lỗ hổng đen ngòm rợn người.",
        "prompt": "Chilling macro still life of an open vintage velvet family photo album resting on a dark mahogany table, multiple framed family portraits where the father's face has been meticulously cut out with scissors leaving jagged black voids, symbolic obliteration of identity, harsh top chiaroscuro lighting."
    },
    {
        "name": "t16_chevrolet_impala_airport_parking_snow",
        "act": 2,
        "sentences": "2.06#3–#5",
        "desc": "Chiếc xe Chevrolet Impala đời 1963 bị bỏ rơi phủ đầy băng tuyết tại bãi đỗ xe dài hạn sân bay John F. Kennedy, New York, chìa khóa cắm nguyên trong ổ khóa.",
        "prompt": "Moody atmospheric wide shot of a vintage 1963 dark sedan parked abandoned in a desolate snowy JFK airport long-term parking lot at night, windshield caked in frozen sleet, distant glowing runway lights blurred through freezing winter fog, cold desolate noir palette."
    },
    {
        "name": "t16_interstate_bus_terminal_rain_neon",
        "act": 2,
        "sentences": "2.08#3–#5",
        "desc": "Bến xe buýt liên bang ngập ánh đèn mờ ảo trong đêm mưa lạnh, bóng một người đàn ông mặc âu phục xách vali bước lên chuyến xe đêm trốn chạy về miền Tây nước Mỹ.",
        "prompt": "Gritty cinematic 16:9 view of a 1970s Greyhound interstate bus terminal at midnight during heavy rain, neon glow reflecting on wet oil-slicked tarmac, lone silhouetted figure in a trench coat and fedora holding a leather suitcase stepping onto a coach, fugitive flight into anonymity."
    },
    {
        "name": "t16_cold_case_dossier_archives_dust",
        "act": 2,
        "sentences": "2.09#4–#7",
        "desc": "Hộp hồ sơ vụ án bám bụi dày trong căn phòng lưu trữ hồ sơ chưa có lời giải của cảnh sát New Jersey, những bức ảnh chụp cũ ố vàng theo năm tháng.",
        "prompt": "Atmospheric macro still life inside a dim police cold case archive basement, rows of steel shelves holding cardboard evidence boxes, thick layer of dust coating a manila folder tied with red twine, muted sepia and slate tones, passing of eighteen forgotten years."
    },

    # -------------------------------------------------------------------------
    # HỒI 3: Bổ sung 4 ảnh (11 -> 15 ảnh)
    # Bối cảnh sâu: Cuốn sổ kế toán cân đối thu chi, thánh giá gỗ trên tường, phòng khách chia ngăn
    # -------------------------------------------------------------------------
    {
        "name": "t16_accountant_ledger_red_deficit_ink",
        "act": 3,
        "sentences": "3.03#4–#6",
        "desc": "Cuốn sổ nhật ký kế toán tài chính với các con số thâm hụt ghi bằng mực đỏ thẳng tắp không một vết gạch xóa, cây bút máy đặt ngay ngắn bên lề trang sách.",
        "prompt": "Forensic still life of an open antique accounting ledger book with columns of numbers written in precise neat cursive, deep red ink entries showing catastrophic financial deficits, vintage fountain pen placed in exact parallel alignment, rigid perfectionism aesthetic."
    },
    {
        "name": "t16_lutheran_cross_austere_study_wall",
        "act": 3,
        "sentences": "3.05#4–#6",
        "desc": "Cây thánh giá gỗ Tin Lành Luther giản dị treo lẻ loi trên bức tường phòng làm việc tối om, biểu tượng đức tin bị bóp méo thành động cơ tước đoạt sinh mạng.",
        "prompt": "Stark chiaroscuro composition of a simple unadorned wooden Lutheran cross hanging on a dark wood-paneled wall, sharp diagonal sliver of pale moonlight illuminating the cross while the rest of the study remains engulfed in pitch-black shadow, moral rationalization dread."
    },
    {
        "name": "t16_cognitive_compartmentalization_cabinet",
        "act": 3,
        "sentences": "3.07#3–#5",
        "desc": "Chiếc tủ gỗ nhiều ngăn kéo phân loại hồ sơ cổ điển với một ngăn kéo khóa chặt bằng chìa đồng thau, hình tượng hóa sự chia ngăn nhận thức trong tâm trí kẻ thủ ác.",
        "prompt": "Surreal symbolic noir visual of a tall antique apothecary wooden cabinet with dozens of small labeled drawers, one single drawer bound in heavy iron chains and secured with a tarnished brass padlock, metaphor for psychological compartmentalization, dramatic side lighting."
    },
    {
        "name": "t16_suburban_church_pew_hymnal_solitude",
        "act": 3,
        "sentences": "3.08#2–#4",
        "desc": "Dãy ghế gỗ dài trong nhà thờ vắng lặng dưới ánh hoàng hôn mùa thu, cuốn sách thánh ca mở ngửa lẻ loi trên giá tựa lưng, sự bình thản giả tạo của kẻ che giấu tội ác.",
        "prompt": "Melancholic wide interior view down an empty church aisle with rows of dark polished oak pews, rays of dusty late afternoon sunlight slanting through tall arched windows, open hymn book resting on a wooden rack, eerie quiet sanctimoniousness."
    },

    # -------------------------------------------------------------------------
    # HỒI 4: Bổ sung 4 ảnh (12 -> 16 ảnh)
    # Bối cảnh sâu: Xưởng điêu khắc Frank Bender, đất sét ẩm và kính gọng sừng, máy thu hình CRT 1989
    # -------------------------------------------------------------------------
    {
        "name": "t16_frank_bender_sculpting_clay_tools",
        "act": 4,
        "sentences": "4.04#3–#5",
        "desc": "Bàn làm việc của nhà nhân chủng học pháp y Frank Bender ngổn ngang dao miết đất sét, ảnh chụp x-quang hộp sọ và cặp kính gọng sừng thập niên 70 đang ướm lên tượng sáp.",
        "prompt": "Intense forensic still life of a sculptor's cluttered studio workbench, wet sculpting clay modeling tools, calipers, vintage 1970s horn-rimmed eyeglasses resting beside a lifelike clay bust armature, warm focused workbench lamp amidst dark shadows, obsessive forensic reconstruction."
    },
    {
        "name": "t16_vintage_crt_television_broadcast_amw",
        "act": 4,
        "sentences": "4.06#3–#5",
        "desc": "Màn hình tivi ống tia âm cực CRT cổ điển trong phòng khách tối đang phát sóng chương trình America's Most Wanted ngày 21 tháng 5 năm 1989, ánh sáng quét xanh lam phản chiếu khắp căn phòng.",
        "prompt": "Atmospheric 1989 living room at night, illuminated solely by the eerie cyan scanline glow of a wood-cabinet CRT television screen broadcasting an investigative true-crime documentary, empty armchair casting deep silhouettes, historic television breakthrough."
    },
    {
        "name": "t16_colorado_neighbor_whispering_telephone",
        "act": 4,
        "sentences": "4.08#3–#5",
        "desc": "Chiếc điện thoại bàn quay số màu be gắn trên tường phòng bếp rung chuông trong đêm, bàn tay người hàng xóm Wanda Flannery nhấc máy gọi đến đường dây nóng FBI.",
        "prompt": "Tense cinematic close-up of a vintage beige rotary wall phone in a suburban kitchen at dusk, cord twisting down, hand lifting the receiver in trembling realization, dramatic shadow play, decisive moment of citizen tip-off."
    },
    {
        "name": "t16_richmond_accounting_office_desk_arrest",
        "act": 4,
        "sentences": "4.10#3–#5",
        "desc": "Bàn làm việc văn phòng kế toán tại Richmond, Virginia với máy tính bấm số cơ học, chiếc cốc cà phê và cặp còng tay số 8 bằng thép không gỉ đặt trên mặt bàn.",
        "prompt": "Grim forensic still life on an ordinary corporate office desk in Virginia, vintage adding machine with paper tape, coffee mug, and a pair of cold steel police handcuffs resting beside an open briefcase, the sudden collapse of an 18-year false identity."
    },

    # -------------------------------------------------------------------------
    # HỒI 5: Bổ sung 4 ảnh (17 -> 21 ảnh)
    # Bối cảnh sâu: Búa gỗ tòa án New Jersey, hành lang buồng giam Trenton, khu phố thanh bình thức tỉnh
    # -------------------------------------------------------------------------
    {
        "name": "t16_courtroom_gavel_mahogany_verdict",
        "act": 5,
        "sentences": "5.02#3–#5",
        "desc": "Chiếc búa gỗ thẩm phán bằng gỗ óc chó đánh mạnh xuống mặt bàn tòa án New Jersey, phán quyết 5 án tù chung thân liên tiếp khép lại hành trình công lý sau gần 2 thập kỷ.",
        "prompt": "Dramatic close-up of a heavy polished mahogany judicial gavel resting firmly on a courtroom sound block, blurred law books and wooden judge's bench in the background, stark formal chiaroscuro lighting, finality of justice."
    },
    {
        "name": "t16_state_prison_iron_bars_solitary_cell",
        "act": 5,
        "sentences": "5.03#4–#6",
        "desc": "Dãy buồng giam nhà tù bang New Jersey lạnh lẽo với những chấn song sắt nặng nề, bóng một người đàn ông già nua ngồi bất động trên giường sắt đối diện bức tường đá xám.",
        "prompt": "Bleak high-contrast black-and-white noir view down a state penitentiary cellblock corridor, heavy cast-iron bars casting sharp grid shadows across a concrete floor, solitary aged figure seated motionless in a stark cell, total irreversible isolation."
    },
    {
        "name": "t16_westfield_residential_avenue_spring",
        "act": 5,
        "sentences": "5.04#6–#8",
        "desc": "Đại lộ rợp bóng cây cổ thụ tại thị trấn Westfield hồi sinh trong buổi sớm mai thanh bình, ánh nắng ấm áp xuyên qua cành lá xua tan bóng tối u uất của quá khứ.",
        "prompt": "Gentle poetic establishing shot of a quiet tree-lined suburban avenue in Westfield, New Jersey, morning golden sunlight filtering through leafy green oak branches onto stone sidewalks, peaceful healing atmosphere, hopeful redemption noir."
    },
    {
        "name": "t16_vigilance_and_compassion_porch_lantern",
        "act": 5,
        "sentences": "5.05#15–#18",
        "desc": "Ngọn đèn lồng bằng đồng ấm áp thắp sáng trước hiên nhà trong đêm sương mờ, biểu tượng của sự thức tỉnh cộng đồng, sự đồng cảm và tình yêu thương bảo bọc đích thực.",
        "prompt": "Heartwarming yet poignant visual of a classic brass lantern glowing brightly on a front porch column, soft warm amber radiance piercing the surrounding cool night mist, symbolic beacon of vigilance, human dignity, and genuine familial care."
    }
]

if __name__ == "__main__":
    print(f"Đã định nghĩa {len(new_20_jobs_tap16)} ảnh nền bổ sung cho Tập 16:")
    for a in range(1, 6):
        act_items = [j for j in new_20_jobs_tap16 if j['act'] == a]
        print(f" - Hồi {a}: +{len(act_items)} ảnh ({act_items[0]['name']} ... {act_items[-1]['name']})")
