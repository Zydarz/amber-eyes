# -*- coding: utf-8 -*-
"""Deep audit of TikTok Tap 13 scripts across VI, EN, JA."""
import pathlib, re, json

ROOT = pathlib.Path(__file__).resolve().parent.parent

def audit_files():
    configs = [
        ('02_SAN_XUAT/TIKTOK/Tap13/KE_HOACH_CLIP_TAP13.md', 'VI'),
        ('02_SAN_XUAT/TIKTOK/Tap13/SPEC_AUDIO_CLIP_TAP13.json', 'VI'),
        ('02_SAN_XUAT/TIKTOK/Tap13_EN/KE_HOACH_CLIP_TAP13_EN.md', 'EN'),
        ('02_SAN_XUAT/TIKTOK/Tap13_EN/SPEC_AUDIO_CLIP_TAP13.json', 'EN'),
        ('02_SAN_XUAT/TIKTOK/Tap13_JA/KE_HOACH_CLIP_TAP13_JA.md', 'JA'),
        ('02_SAN_XUAT/TIKTOK/Tap13_JA/SPEC_AUDIO_CLIP_TAP13.json', 'JA'),
    ]

    for rel_path, lang in configs:
        p = ROOT / rel_path
        if not p.exists():
            print(f"File not found: {p}")
            continue
        text = p.read_text(encoding='utf-8')
        print(f"\n==========================================")
        print(f"AUDITING: {rel_path} [{lang}]")
        print(f"==========================================")

        # 1. Punctuation & Typography
        lines = text.splitlines()
        for idx, line in enumerate(lines, 1):
            if not line.strip().startswith('|'):
                # Space before punctuation (, . : ; ? !)
                m_sbp = re.search(r'([a-zA-ZÀ-ỹ0-9])\s+([,.:;?!])', line)
                if m_sbp:
                    print(f"  [L{idx}] SPACE_BEFORE_PUNCT: '{m_sbp.group()}' -> '{line[:80]}'")
                # Missing space after punctuation
                m_msa = re.search(r'([a-zA-ZÀ-ỹ])([,;:])([a-zA-ZÀ-ỹ])', line)
                if m_msa and not re.search(r'https?://', line):
                    print(f"  [L{idx}] MISSING_SPACE_AFTER: '{m_msa.group()}' -> '{line[:80]}'")

        # 2. Check JSON specifically for TTS rules
        if 'SPEC_AUDIO' in rel_path:
            data = json.loads(text)
            for cid, clip in data.items():
                for line in clip.get('lines', []):
                    t = line.get('text', '')
                    lid = line.get('id', '')
                    # G1 rule: Ellipsis forbidden
                    if '...' in t or '…' in t:
                        print(f"  [{cid} {lid}] G1 VIOLATION (Ellipsis): '{t}'")
                    # Quotes balance
                    if t.count('“') != t.count('”'):
                        print(f"  [{cid} {lid}] UNBALANCED VI QUOTES: '{t}'")

        # 3. Vietnamese spelling & vocabulary checks
        if lang == 'VI':
            confusing = [
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
            ]
            for pat, rec in confusing:
                m = re.search(pat, text, re.IGNORECASE)
                if m:
                    print(f"  CONFUSING SPELLING: found '{m.group()}' (khuyến nghị: '{rec}')")

    print("\nAudit completed.")

if __name__ == '__main__':
    audit_files()
