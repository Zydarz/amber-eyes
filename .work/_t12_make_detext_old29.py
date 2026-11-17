# -*- coding: utf-8 -*-
"""Tập 12 — vá 29 nền CŨ (13/11) có chữ AI theo bảng §4.5 của BaoCao_QC_Tap12_20261116.md.

Nguyên tắc (A11 #171 + #175 + #179 + #180):
  1. GIỮ bối cảnh + chất noir của từng nền, chỉ thay vật thể mang chữ.
  2. Vật thể bắt buộc cho cốt truyện ⇒ giữ nhưng làm bề mặt TRƠN TRỐNG.
  3. Vật thể chính là "chỗ chữ" ⇒ BỎ HẲN khỏi khung hình (đổi bố cục).
  4. KHÔNG nhắc tên vật thể mang chữ trong prompt (printed/flyer/sign/label/marked/
     badge/emblem/inscribed/typed/notes/passbook/deed/envelope/telegram/appeal/
     names/card/volts/degrees/seal/stamp/map of/number/dial…) vì chính từ đó gời AI vẽ.
  5. Thêm "completely blank and unmarked with no writing at all" khi còn vật thể.

2 biến thể mỗi nền (cùng prompt, seed khác) ⇒ chọn ảnh sạch nhất.
Ghi:
  .work/bg_jobs_tap12_old29.json   (58 job cho Kaggle)
  .work/bg_jobs_tap12_v2.json       (cap nhat prompt chinh)
"""
import json
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
ROOT = Path(__file__).resolve().parents[1]
JOBS_V2 = ROOT / ".work/bg_jobs_tap12_v2.json"
OUT = ROOT / ".work/bg_jobs_tap12_old29.json"

# name -> (desc tieng Viet, prompt moi)
PATCH = {
    "t12_amber_eyes_closing_dossier_jonestown": (
        "Cảnh kết chương trình: hồ sơ da đóng trên bàn sồi tối, bìa trơn hoàn toàn không khắc gì, ánh nến ấm rọi ngang da.",
        "Amber Eyes closing scene, a dark leather-bound case folder lying closed on a dark oak desk, its cover completely plain and blank with no writing on it, a soft warm amber lamp glow falling across the leather, elegant noir documentary mood, fine film grain.",
    ),
    "t12_charity_soup_kitchen_bread": (
        "Ấm soup nóng và bánh cắt trên thớt gỗ trong bếp chung, bóng đèn vàng ấm, không có tờ rơi.",
        "Warm still life of a steaming metal soup kettle, sliced bread on a worn cutting board, a rustic communal kitchen table, soft amber hanging bulb lighting, nostalgic humanitarian benevolence facade, dark linework.",
    ),
    "t12_concerned_relatives_alliance": (
        "Bức tường ghim ảnh gia đình đen trắng trên bảng cork, ảnh trơn không chữ, đèn bàn tạo bóng cứng.",
        "Forensic evidence scene of plain unmarked black-and-white family photographs pinned to a corkboard, a bare metal desk lamp casting hard shadows, somber documentary noir.",
    ),
    "t12_congressman_leo_ryan_briefing": (
        "Bàn họp Quốc hội nhìn từ trên xuống: hồ sơ da đóng, tờ giấy trắng trơn và bản đồ gấp không chữ.",
        "Official congressional briefing desk seen from above, a plain closed leather folder, a stack of completely blank loose sheets, a folded blank chart, resolute moral duty tone, crisp chiaroscuro.",
    ),
    "t12_confiscated_passports_trunk": (
        "Rương quân sự xanh mở toàn bên trong làm các quyển sổ bìa xanh trơn không chữ, ổ khóa đồng nặng trên vành.",
        "Forensic macro still life of an open heavy green military footlocker filled with closed plain unmarked booklets of dull blue leather, leather wallets and folded blank papers, a heavy brass padlock resting on the rim, symbol of total loss of civic identity, dark chiaroscuro.",
    ),
    "t12_entering_armed_compound_gate": (
        "Vòm cổng gỗ rustic trong sương sớm, không treo bảng, lối xe lần bùn dẫn vào rừng rậm.",
        "Cinematic shot of a rustic wooden archway entrance to a jungle agricultural compound, weathered bare timber with nothing mounted on it, morning mist half-shrouding the structure, muddy tire tracks leading into dense suffocating jungle foliage, ominous frontier threshold.",
    ),
    "t12_fallen_reporters_and_ryan": (
        "Máy quay tin tức bị móp nằm sát vai đường sỏi, thân máy trơn không nhãn, ống kính vỡ phản chiếu trời xám.",
        "Solemn forensic still life, a dented shoulder-mounted news camera lying on the gravel shoulder with a completely plain unmarked body, cracked lens reflecting overcast sky, a small plain metal pin in red dust, solemn historical tragedy, respectful documentary angle.",
    ),
    "t12_fbi_evidence_tape_q042": (
        "Cuộn băng cassette trong túi niêm phong kỹ thuật, mặt túi trơn hoàn toàn, nằm trên bàn thép cạnh thước đo.",
        "Forensic still life of an authentic 1970s compact cassette tape inside a sealed clear evidence plastic bag whose surface is completely blank and unmarked with no writing at all, resting on a stainless steel examination table beside a forensic ruler, stark clinical noir.",
    ),
    "t12_impenetrable_geographical_isolation": (
        "Sơ đồ địa lý cổ kiểu: nét mực dày, bờ biển trơn không chữ, một vòng tròn đỏ nhỏ giữa rừng.",
        "Cartographic forensic diagram of northwestern Guyana rendered as an antique topographer chart of dense ink hatching and blank unlabelled coastline, hundreds of miles of roadless jungle shown as solid texture, a single small crimson circle of light in the middle, total geographic isolation.",
    ),
    "t12_habituation_death_desensitization": (
        "Bảng đen phấn vẽ đường cong đi xuống, trục trơn không nét chữ, khắc học sư phạm.",
        "Scientific psychological chart etched on a vintage blackboard, a single descending curve drawn in chalk over bare empty axes, habituation and psychological erosion of survival instinct, chalkboard noir.",
    ),
    "t12_memorial_918_names_monolith": (
        "Khối đá bia nhớ to lớn, mặt đá nhẵn hoàn toàn không khắc gì, nắng sớm xuyên qua lá cây.",
        "Monumental plain stone marker with a completely smooth blank uncarved face, morning sunlight breaking through green leaves above, casting golden warmth on gray stone, eternal memory and historical reflection.",
    ),
    "t12_milgram_experiment_shock_generator": (
        "Bàn điều khiển máy kích thích thí nghiệm 1960s, nút gạt cũ và mặt bảng điều khiển trơn trọn.",
        "Forensic close-up of a 1960s laboratory shock generator console, vintage toggle switches and a completely plain blank unmarked control panel, harsh raking laboratory light, psychological obedience paradigm.",
    ),
    "t12_moral_compass_unbroken": (
        "La bàn đồng cổ phát sáng trên đá tải, mặt la bàn trơn hoàn toàn, kim chỉ hướng Bắc, ánh hổ phách đẩy lùi bóng tối.",
        "Glowing antique brass navigational compass resting on a dark slate surface, a completely plain blank unmarked circular face, needle pointing steadily true, radiating a warm amber luminescence that pushes back creeping pitch-black shadows, unbroken personal conscience.",
    ),
    "t12_moral_courage_candle_in_dark": (
        "Nến cháy kiên định giữa bóng tối xoáy cuồn, ánh sáng ấm rọi lên tường trơn.",
        "Poetic chiaroscuro composition of a solitary lit candle flame standing firm amidst violent swirling shadows of darkness, warm amber glow spilling across a bare blank wall, unbroken conscience.",
    ),
    "t12_nbc_camera_recording_facade": (
        "Máy quay 16mm vai đen người hướng về gia đình đa thế hệ ngồi ăn picnic, đèn đỏ ghi hình sáng, thân máy trơn.",
        "Shoulder-mounted 16mm news camera in silhouette pointing toward smiling multigenerational families seated at communal picnic tables, camera body completely plain and unmarked, red recording tally light glowing, fragile illusion of peace captured on celluloid.",
    ),
    "t12_new_west_investigative_draft": (
        "Bàn làm việc điều tra nửa đêm: máy đánh chữ cũ cạnh chồng giấy trắng trơn, kính lúp, cuộn phim 35mm.",
        "Journalistic investigative desktop at midnight, a vintage typewriter beside a stack of completely blank unmarked loose sheets, a magnifying glass, rolls of 35mm film negatives, urgent investigative tension, moody slate and amber noir.",
    ),
    "t12_paranoia_cracking_dictator_mind": (
        "Chân dung tối của thủ lĩnh trong cabin gỗ, mặt khuất trong bóng, tay nắm chặt bàn, lọ thuốc trơn và giấy trắng.",
        "Psychological noir portrait of the cult leader in a dark claustrophobic wooden cabin, face obscured by heavy shadows and dark sunglasses, trembling white-knuckled hands gripping the table edge, small plain unmarked pill bottles and blank scattered sheets of paper, spiraling paranoia.",
    ),
    "t12_prefrontal_cortex_impairment": (
        "Sơ đồ giải phẫu não hình nghiêng, vẽ nét mực thuần không chú thích, vùng vỏ trước trước chìm trong bóng nứt.",
        "Forensic neurobiology diagram of a human profile brain map rendered as plain anatomical ink linework with no annotations and no lettering, the prefrontal cortex area dimmed and engulfed in fractured ink shadows, illustrating the scientific failure of executive function under chronic starvation and sleep deprivation.",
    ),
    "t12_press_corps_cameras_microphones": (
        "Dụng cụ phóng sự: máy quay 16mm nặng thân trơn, máy ảnh rangefinder 35mm, micro định hướng, sẵn sàng ngoài hiểm trường.",
        "Journalistic field equipment still life, a heavy 16mm television news film camera with a completely plain unmarked body, 35mm rangefinder cameras with telephoto lenses, a directional microphone, ready for hostile environment fact-finding mission.",
    ),
    "t12_property_surrender_passbooks": (
        "Chồng sổ tiết kiệm bìa trơn, giấy tờ gấp trắng và bìu thư kín trống trên bàn gỗ sẫm, ánh đèn bàn xiên gay.",
        "Forensic still life of stacked plain unmarked 1970s bank savings booklets with completely blank covers, folded blank papers, and sealed blank envelopes piled on a dark mahogany desk, harsh raking desk lamp light, systemic financial dispossession aesthetic.",
    ),
    "t12_redflag1_total_social_isolation": (
        "Mạng nhện sắt cắt ngang dây điện thoại và dây ảnh gia đình, đèn cảnh báo đỏ rực trong bóng tối xanh.",
        "Conceptual noir warning visual: severe iron spiderweb grid severing telephone lines and family photograph strings, a glowing crimson alert beacon cutting across cold slate darkness, Red Flag 1 Total Social Isolation.",
    ),
    "t12_redflag3_escalating_commitment_trap": (
        "Bánh răng cương công nghiệp nghiền đồng hồ mặt trơn, tiền vàng và mảnh giấy gấp trắng vào cơ máy tối.",
        "Conceptual noir warning visual: interlocking heavy industrial gear teeth relentlessly dragging timepieces with completely blank unmarked faces, gold coins, and folded blank slips into dark machinery, Red Flag 3 Escalating Commitment Sunk Cost Trap.",
    ),
    "t12_secret_note_folded_slip": (
        "Hai tay lén đưa cho nhau một mảnh giấy nhỏ nhăn trong bóng tối, mặt giấy trơn hoàn toàn.",
        "Tense forensic macro shot of two hands brushing secretly in shadowy darkness, passing a tiny creased paper slip that is completely blank and unmarked with no writing at all, high-contrast ink chiaroscuro, pulse of danger.",
    ),
    "t12_us_capitol_congressional_hearing": (
        "Phòng điều trần Quốc hội Mỹ: bục gỗ chạm khắc, ghế da, chồng sách bìa gáy trơn.",
        "Prestigious interior of a US Capitol congressional hearing chamber, carved wooden dais, leather chairs, thick bound volumes with completely plain blank spines, solemn pursuit of legal reform.",
    ),
    "t12_utopian_promise_mirage": (
        "Bức tranh thiên đường rực rỡ bong tróc lộ gỗ mục rừng tối, tranh trơn không chữ.",
        "Surreal split-toned composition showing an ethereal painted picture of a tropical paradise with blooming orchards and golden sunlight, the painted scene plain with no lettering, peeling and curling at the edges to reveal rotting dark jungle timber beneath, tragic illusion of promised utopia.",
    ),
    "t12_loudspeaker_horns_tower": (
        "Cột gỗ cao gắn nhiều loa kèn, dây điện rủ xuống, trời xám tím u ám.",
        "Low-angle dramatic shot of a tall weathered bare wooden pole mounted with multiple metallic public-address horn loudspeakers, wires dangling against an overcast bruised sky, sound waves visually implied through ink hatching, constant surveillance and brainwashing.",
    ),
    "t12_redflag2_silenced_critical_thinking": (
        "Bút máy vàng gãy mũi, mực đen loang trên trang sổ trắng, bên cạnh ổ khóa thép trơn, nét đỏ cảnh báo.",
        "Conceptual noir warning visual: broken gold fountain pen nib with spilled black ink pooling across a blank journal page, beside a heavy metal padlock with a completely plain smooth body, glowing crimson accent, Red Flag 2 Silenced Critical Thinking.",
    ),
    "t12_sunk_cost_entrapment_quicksand": (
        "Bàn tay với đưa ra nắm lấy huy hiệu vàng ảo, mặt huy hiệu trơn, chìm dần trong bùn đen.",
        "Poignant conceptual graphic illustration of an outstretched hand grasping an illusory shining golden medallion with a completely plain smooth unmarked face while sinking inexorably into dark quicksand of collective delusion and self-justification, high-contrast ink crosshatching.",
    ),
    "t12_truck_evacuation_muddy_road": (
        "Xe tải bắn đầy bùn lao trên đường rừng, đuôi xe trơn không chữ, hành khách bám chặt lan can.",
        "Exterior shot of a mud-splattered flatbed truck speeding down a rutted jungle road away from the compound, the rear of the truck completely plain with no writing or marks, passengers holding tight to wooden rails in anxious silence, spray of red mud, frantic race toward evacuation.",
    ),
}

SEED_A = 36000
SEED_B = 36100

jobs = json.loads(JOBS_V2.read_text(encoding="utf-8"))
by = {j["name"]: j for j in jobs}
out = []
missing = [n for n in PATCH if n not in by]
if missing:
    raise SystemExit(f"khong tim thay job: {missing}")
for i, (name, (desc, prompt)) in enumerate(PATCH.items()):
    by[name]["desc"] = desc
    by[name]["prompt"] = prompt
    for tag, seed in (("a", SEED_A + i), ("b", SEED_B + i)):
        j = dict(by[name])
        j["name"] = f"{name}_{tag}"
        j["prompt"] = prompt
        j["desc"] = desc
        j["seed"] = seed
        out.append(j)

JOBS_V2.write_text(json.dumps(jobs, ensure_ascii=False, indent=1), encoding="utf-8")
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"{len(PATCH)} nen cu x 2 bien the = {len(out)} anh")
print(f"seed {SEED_A}..{SEED_A + len(PATCH) - 1} va {SEED_B}..{SEED_B + len(PATCH) - 1}")
print(f"-> {OUT.name}")
