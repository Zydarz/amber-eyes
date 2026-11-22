# -*- coding: utf-8 -*-
"""Comprehensive spellcheck, punctuation, and linguistic audit for TikTok clips of Tap 12, 13, 14, 15."""
import pathlib, re, json

ROOT = pathlib.Path(__file__).resolve().parent.parent

EPISODES = ['12', '13', '14', '15']
LANGUAGES = [
    ('VI', 'Tap{ep}', 'KE_HOACH_CLIP_TAP{ep}.md', 'SPEC_AUDIO_CLIP_TAP{ep}.json'),
    ('EN', 'Tap{ep}_EN', 'KE_HOACH_CLIP_TAP{ep}_EN.md', 'SPEC_AUDIO_CLIP_TAP{ep}.json'),
    ('JA', 'Tap{ep}_JA', 'KE_HOACH_CLIP_TAP{ep}_JA.md', 'SPEC_AUDIO_CLIP_TAP{ep}.json')
]

CONFUSING_WORDS_VI = [
    (r'\bchuẩn đoán\b', 'chẩn đoán'),
    (r'\bsơ xuất\b', 'sơ suất'),
    (r'\bxuất sứ\b', 'xuất xứ'),
    (r'\bvô hình chung\b', 'vô hình trung'),
    (r'\btựu chung\b', 'tựu trung'),
    (r'\bsáng lạng\b', 'xán lạn'),
    (r'\bdấu diếm\b', 'giấu giếm'),
    (r'\bchắp vá\b', 'chắp vá'),
    (r'\btrắp vá\b', 'chắp vá'),
    (r'\bchằng chịt\b', 'chằng chịt'),
    (r'\bgiành cho\b', 'dành cho'),
    (r'\bdành giật\b', 'giành giật'),
    (r'\bchững chạc\b', 'chững chạc'),
    (r'\btrông gai\b', 'chông gai'),
]

V9_SENSITIVE_WORDS_VI = [
    'chặt xác', 'phanh thây', 'máu me be bét', 'moi ruột', 'cắt cổ', 'chém chết', 'hiếp dâm', 'ấu dâm', 'lột da'
]

def audit_all():
    summary_report = []
    total_issues = 0

    print("================================================================================")
    print("AUDIT TOÀN DIỆN CHÍNH TẢ & NGÔN TỪ — TẬP 12, 13, 14, 15 (VI, EN, JA)")
    print("================================================================================\n")

    for ep in EPISODES:
        ep_issues = 0
        print(f"--------------------------------------------------------------------------------")
        print(f"--- KIỂM TRA TẬP {ep} ---")
        print(f"--------------------------------------------------------------------------------")

        for lang, dir_pattern, plan_pattern, spec_pattern in LANGUAGES:
            folder_name = dir_pattern.format(ep=ep)
            dir_path = ROOT / "02_SAN_XUAT" / "TIKTOK" / folder_name
            plan_file = dir_path / plan_pattern.format(ep=ep)
            spec_file = dir_path / spec_pattern.format(ep=ep)

            # 1. Kiểm tra tồn tại thư mục & file chính
            if not dir_path.exists():
                print(f"[{lang}] THIẾU THƯ MỤC: {dir_path}")
                ep_issues += 1
                continue
            if not plan_file.exists():
                print(f"[{lang}] THIẾU KẾ HOẠCH: {plan_file.name}")
                ep_issues += 1
            if not spec_file.exists():
                print(f"[{lang}] THIẾU AUDIO SPEC: {spec_file.name}")
                ep_issues += 1

            # 2. Đọc và kiểm tra văn bản kế hoạch (Markdown)
            if plan_file.exists():
                plan_text = plan_file.read_text(encoding='utf-8')
                lines = plan_text.splitlines()
                for idx, line in enumerate(lines, 1):
                    # Khoảng trắng trước dấu câu
                    m_sbp = re.search(r'([a-zA-ZÀ-ỹ0-9])\s+([,.:;?!])', line)
                    if m_sbp and not line.strip().startswith('|'):
                        print(f"  [{lang} Plan L{idx}] DẤU CÂU CÓ KHOẢNG TRẮNG TRƯỚC: '{m_sbp.group()}'")
                        ep_issues += 1
                    # Thiếu khoảng trắng sau dấu câu
                    m_msa = re.search(r'([a-zA-ZÀ-ỹ])([,;:])([a-zA-ZÀ-ỹ])', line)
                    if m_msa and not re.search(r'https?://', line) and not line.strip().startswith('|'):
                        print(f"  [{lang} Plan L{idx}] THIẾU KHOẢNG TRẮNG SAU DẤU: '{m_msa.group()}'")
                        ep_issues += 1

            # 3. Đọc và kiểm tra file SPEC_AUDIO JSON (G1, G6, Dấu câu, Cảm xúc)
            if spec_file.exists():
                spec_data = json.loads(spec_file.read_text(encoding='utf-8'))
                # Lấy master script để đối chiếu G6
                master_script_file = ROOT / ".work" / f"script_tap{ep}{'' if lang == 'VI' else '_' + lang}.json"
                master_map = {}
                if master_script_file.exists():
                    m_data = json.loads(master_script_file.read_text(encoding='utf-8'))
                    for el in m_data:
                        if "sentences" in el:
                            for s in el["sentences"]:
                                master_map[s["id"]] = s["text"]

                for cid, clip in spec_data.items():
                    for line_idx, line in enumerate(clip.get("lines", []), 1):
                        txt = line.get("text", "")
                        lid = line.get("id", "")
                        src_id = line.get("source", "")

                        # G1: Cấm dấu ba chấm
                        if "..." in txt or "…" in txt:
                            print(f"  [{lang} Spec {cid} {lid}] LỖI G1 (DẤU BA CHẤM): '{txt}'")
                            ep_issues += 1

                        # G6: Khớp từng chữ với kịch bản gốc
                        if src_id in master_map:
                            if txt != master_map[src_id]:
                                print(f"  [{lang} Spec {cid} {lid}] LỖI G6 KHÔNG KHỚP GỐC: '{txt}' != '{master_map[src_id]}'")
                                ep_issues += 1

                        # Cảm xúc an toàn G3
                        emot = line.get("emotion", "")
                        if emot not in ("neutral", "sad", "fearful", "surprised"):
                            print(f"  [{lang} Spec {cid} {lid}] LỖI G3 CẢM XÚC LẠ: '{emot}'")
                            ep_issues += 1

                        # Dấu ngoặc kép VI
                        if lang == "VI":
                            if txt.count("“") != txt.count("”"):
                                print(f"  [{lang} Spec {cid} {lid}] NGOẶC KÉP VI BẤT CÂN XỨNG: '{txt}'")
                                ep_issues += 1

            # 4. Kiểm tra các file Caption, MoTa_Dai, MoTa_Ngan
            for cid_num in range(1, 6):
                cid = f"TK{cid_num}"
                for prefix in ("Caption", "MoTa_Dai", "MoTa_Ngan"):
                    txt_path = dir_path / f"{prefix}_{cid}.txt"
                    if not txt_path.exists():
                        print(f"  [{lang}] THIẾU FILE: {txt_path.name}")
                        ep_issues += 1
                        continue
                    content = txt_path.read_text(encoding='utf-8')
                    # Kiểm tra độ dài Caption <= 2200
                    if prefix == "Caption" and len(content) > 2200:
                        print(f"  [{lang} {txt_path.name}] CAPTION QUÁ DÀI: {len(content)} > 2200")
                        ep_issues += 1

                    # Kiểm tra chính tả tiếng Việt
                    if lang == "VI":
                        for pat, correct in CONFUSING_WORDS_VI:
                            m = re.search(pat, content, re.IGNORECASE)
                            if m:
                                print(f"  [{lang} {txt_path.name}] TỪ DỄ NHẦM LẪN: '{m.group()}' -> nên là '{correct}'")
                                ep_issues += 1
                        for bad in V9_SENSITIVE_WORDS_VI:
                            if bad in content.lower():
                                print(f"  [{lang} {txt_path.name}] VI PHẠM V9 TỪ BẠO LỰC: '{bad}'")
                                ep_issues += 1

        print(f"==> Tổng số vấn đề phát hiện ở Tập {ep}: {ep_issues}\n")
        total_issues += ep_issues

    print("================================================================================")
    print(f"KẾT THÚC AUDIT: TỔNG CỘNG {total_issues} LỖI ĐƯỢC PHÁT HIỆN TRÊN CẢ 4 TẬP.")
    print("================================================================================")

if __name__ == '__main__':
    audit_all()
