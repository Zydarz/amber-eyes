#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Sinh lại 32 nền Tập 11 có chữ AI — prompt ĐÃ BỎ CHỮ.

NGUYÊN TẮC (bài học Tập 10, A11 #164):
  1) GỠ mọi thông tin chữ khỏi prompt (tên riêng, "titled", "reading", "labeled"…).
  2) Mô tả vật mang chữ thành BỀ MẶT TRƯNG (plain blank / smooth unmarked).
  3) Thêm mệnh đề "completely blank and unmarked with no writing at all".
  4) Giữ nguyên nội dung cảnh cụ thể (H19) — chỉ bỏ phần chữ.
  5) Seed RIÊNG cho từng ảnh (tránh trùng giữa 2 kernel).
"""
import json
import pathlib
import sys

ROOT = pathlib.Path(__file__).resolve().parents[1]
JOBS = ROOT / ".work" / "bg_jobs_tap11.json"
VIOL = ROOT / ".work" / "_t11" / "violations_t11.json"
OUT = ROOT / ".work" / "bg_jobs_tap11_detext32.json"

BLANK = "completely blank and unmarked with no writing at all"

NEW = {
"t11_amber_eyes_redflag_intro":
 "Minimalist graphic noir card: Iconic golden amber owl eye emblem glowing and piercing through atmospheric charcoal mist, a brass compass and small warning beacon lamps lighting up the dark, the emblem is a pure smooth embossed golden shape with no lettering or characters of any kind, " + BLANK + ", dignified graphic novel noir.",

"t11_amber_eyes_closing_dossier_bernardo":
 "Close-up still life of the dark leather investigative dossier closing solemnly on an antique oak desk, an embossed golden owl eye emblem gleaming in warm amber lamplight, the leather cover is plain smooth unlabelled leather with only a blank embossed symbol, " + BLANK + ", dignified closing frame, graphic novel noir perfection.",

"t11_calendar_counting_to_freedom":
 "Prison cell wall still life: a plain paper wall calendar whose day squares are empty and unmarked, several squares struck through by a single bold red pen slash, a shaft of barred sunlight illuminating the countdown to early freedom, the calendar shows no digits and no letters, " + BLANK + ", profound moral contrast.",

"t11_christmas_1990_halothane_bottle":
 "Chilling forensic still life of Christmas Eve 1990: a vintage amber medical glass bottle with a plain smooth blank surface standing beside an ornate crystal wine goblet on a festive mahogany sideboard, the bottle surface is entirely bare glass with no label or characters, heavy chiaroscuro ink, " + BLANK + ".",

"t11_closing_dossier_stamp":
 "A thick closed case file with plain unmarked covers lying on a dark desk, a heavy metal date stamp resting beside it whose circular face is smooth blank metal with no lettering, cold overhead light, deep shadow, no people, " + BLANK + ".",

"t11_constitutional_legal_deadlock":
 "Legal still life: a heavy leatherbound law volume with a plain blank unmarked spine and cover showing no lettering and no emblem, a heavy padlock clamped across its binding, scales of justice trapped in an unbreakable legal gridlock, solemn institutional tragedy, " + BLANK + ".",

"t11_control_room_dark_monitors":
 "A dim broadcast control room with a wall of switched-off blank dark monitors and one console indicator light, the console buttons are plain blank unlabeled squares, cold grey light, heavy shadow, no people, " + BLANK + ".",

"t11_covert_sociopath_profile":
 "Forensic psychiatric profile chart: a stylized brain anatomical diagram built only from smooth abstract cold blue zones indicating zero empathy and absence of remorse, no arrows and no callouts, the diagram is a pure graphic shape, stark graphic noir ink, clinical detachment, " + BLANK + ".",

"t11_dangerous_offender_life_sentence":
 "Judicial verdict document on aged parchment with a completely blank unmarked surface, a bold red rubber stamp lying on it whose face is smooth and blank with no lettering, an iron prison key resting on the parchment, heavy prison bars in the background, " + BLANK + ".",

"t11_deal_with_the_devil_contract":
 "Formal legal document still life: a folded aged parchment agreement with a completely blank unmarked surface, a fountain pen resting across it, dark ominous crimson and charcoal noir palette, Deal with the Devil, " + BLANK + ".",

"t11_evidence_bags_lab_bench":
 "Sealed translucent evidence bags with plain smooth blank surfaces laid on a cold stainless steel laboratory bench, tweezers and a paper cup, a bare stainless steel wall behind, sterile fluorescent light, sterile emptiness, no people, " + BLANK + ".",

"t11_february_arrest_dna_match":
 "High-contrast forensic laboratory table: an optical microscope illuminating an autoradiograph DNA membrane of matching bands glowing under ultraviolet light, beside it a closed dossier folder with a plain blank unmarked cover and folded papers turned face-down, " + BLANK + ".",

"t11_galligan_inquiry_report_reforms":
 "Dignified study still life: a bound judicial inquiry volume with a plain blank unmarked cover showing no lettering and no emblem, brass judicial scales and a plain round smooth court seal disc, a beacon of legal reform rising from profound tragedy, " + BLANK + ".",

"t11_half_truth_dossier_shadow":
 "Intriguing chiaroscuro shot of a half-opened case file illuminated by an amber banker lamp, the visible page completely blank and unmarked, half the page bathed in golden light and the other half swallowed in impenetrable pitch-black shadow, duality of truth, " + BLANK + ".",

"t11_handheld_camera_lens":
 "A macro close-up of an old handheld video camera lens half-swallowed by darkness, faint cold reflection of an empty room in the glass, the metal lens ring plain smooth unmarked metal, heavy shadow, film grain, no people, no hands, " + BLANK + ".",

"t11_haunted_new_identity_shadow":
 "Still life of a new Canadian passport lying open to an identity page that is completely blank and unmarked, surrounded by permanent looming shadows of past crimes, eternal moral exile and social ostracism, " + BLANK + ".",

"t11_investigator_nausea_monitor":
 "Over-the-shoulder noir shot of an investigator clutching the desk edge in revulsion, staring at a vintage CRT monitor glowing cold blue in a dark room, a bare wooden wall behind, screen reflected in trembling glasses, shattering of illusions, " + BLANK + ".",

"t11_joliette_prison_gate_release":
 "Exterior morning shot of imposing plain steel gates swinging open, the gate faces completely blank and unmarked with no lettering and no emblem, the silhouette of a woman walking out into a barrage of press telephoto lenses and flashing strobes, " + BLANK + ".",

"t11_ken_murray_obstruction_charge":
 "Legal study interior: a heavy oak desk with a locked steel drawer partially ajar, a legal indictment document lying face-down so only its completely blank unmarked back is visible, heavy solemn shadows, " + BLANK + ".",

"t11_map_proximity_dark_crossroads":
 "Overhead cartographic noir composition: a vintage road map rendered as a plain blank abstract grid of thin roads with no place names and no characters, a red marker circling one junction, a creeping black ink stain slowly engulfing the paper, " + BLANK + ".",

"t11_missing_evidence_dilemma":
 "Moody overhead shot of a homicide detective desk covered in open evidence envelopes holding blank photographic prints turned face-down, a magnifying glass over empty smooth fingerprint cards, a desperate search for missing links in a double homicide, " + BLANK + ".",

"t11_narcissistic_mirror_vanity":
 "Intimate noir still life of an opulent dressing room table, an ornate gold-rimmed mirror, vintage cologne bottles with plain smooth blank glass surfaces, a gold comb, and the back silhouette of a man styling his hair, harsh dramatic raking light, graphic novel ink contours, " + BLANK + ".",

"t11_outraged_citizens_protest":
 "Panoramic street protest outside the Ontario legislature, a sea of silhouetted citizens holding plain blank unmarked placards with completely bare surfaces, autumn mist, emotional anguish and public fury, graphic novel noir, " + BLANK + ".",

"t11_pleading_victim_tears":
 "Still life macro shot: a crumpled linen handkerchief damp with tears beside a cold cup of tea and a yellow legal notepad whose pages are completely blank and unmarked, calculated presentation of absolute innocence, heavy black ink rendering, " + BLANK + ".",

"t11_prosecution_clock_pressure":
 "Tense visual metaphor: a vintage brass hourglass with sands running out rapidly against a bare peeling wall, ticking pressure driving flawed prosecutorial compromise, " + BLANK + ".",

"t11_redflag1_evading_accountability":
 "Conceptual graphic noir art for Red Flag 1: a cracked porcelain shield whose face is completely plain and unmarked with no lettering, tears deflecting arrows of legitimate inquiry, evading accountability behind manufactured suffering, " + BLANK + ".",

"t11_scarborough_taskforce_archive":
 "Investigation room still life: a giant wall map of a city rendered as a plain blank abstract street grid with no place names and no characters, peppered with red pushpins and red yarn, forensic case binders with plain unmarked spines stacked on a steel desk, a desk lamp casting harsh directional light, solemn police procedural noir, " + BLANK + ".",

"t11_six_8mm_tapes_bag":
 "Forensic evidence handover still life: a brown canvas duffel bag unzipped on a police evidence locker counter revealing six 8mm magnetic video cassette tapes in plain unmarked plastic cases, a bare metal locker wall behind, autumn 1994 turning point, stark graphic noir, " + BLANK + ".",

"t11_six_tapes_on_floor":
 "Six sealed black videotape cassettes with plain smooth blank unshelled surfaces laid out in a straight row on a bare wooden floor, cold grey daylight from a window, dust motes, deep shadow, no people, " + BLANK + ".",

"t11_st_catharines_hospital_night":
 "Exterior nocturnal shot of a hospital emergency entrance canopy in pouring rain, a plain blank unmarked canopy fascia with no lettering and no emblem, an emergency red beacon reflecting off wet asphalt, somber medical sanctuary, graphic noir chiaroscuro, " + BLANK + ".",

"t11_triumphant_smile_deal_with_devil":
 "Metaphorical psychological visual: a torn parchment of a plea bargain crumbling into ash, backlit by the eerie formless glow of an interrogation monitor showing only blank light, the bitter sting of being utterly duped by a monster, " + BLANK + ".",

"t11_unholy_sacrament_altar":
 "Atmospheric symbolic visual: a dark domestic shrine surrounded by flickering black tapers, a plain undecorated stone arch, shadows converging into a grotesque temple of shared psychosis, destruction of human conscience, " + BLANK + ".",
}


def main():
    jobs = {j["name"]: j for j in json.loads(JOBS.read_text(encoding="utf-8"))}
    viol = json.loads(VIOL.read_text(encoding="utf-8"))
    out = []
    for i, v in enumerate(viol, start=1):
        n = v["name"]
        if n not in jobs:
            sys.exit(f"khong co job cho {n}")
        if n not in NEW:
            sys.exit(f"chua viet prompt moi cho {n}")
        old = jobs[n]
        out.append({
            "name": n,
            "act": old.get("act", 1),
            "sentences": old.get("sentences", ""),
            "desc": old.get("desc", ""),
            "prompt": NEW[n],
            "seed": 31000 + i,          # seed riêng, không trùng lần trước
            "why": v["why"],
            "level": v["level"],
            "prompt_cu": old["prompt"],
        })
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"ghi {OUT.relative_to(ROOT)} · {len(out)} job sinh lai")
    # kiem tra: prompt moi khong con tu khoa nghi van chu
    import re
    RX = re.compile(r"\b(titled|reading|labelled|labeled|inscribed|signed|newspaper|"
                    r"headline|written|engraved|caption|placard|signage)\b", re.I)
    for j in out:
        hit = RX.findall(j["prompt"])
        if hit:
            print(f"  CANH BAO {j['name']}: {hit}")
    print("seed:", out[0]["seed"], "->", out[-1]["seed"])


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
