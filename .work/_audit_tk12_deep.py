# -*- coding: utf-8 -*-
"""Deep audit of TikTok Tap 12 scripts across VI, EN, JA."""
import pathlib, re, json

ROOT = pathlib.Path(__file__).resolve().parent.parent

def audit_files():
    configs = [
        ('02_SAN_XUAT/TIKTOK/Tap12/KE_HOACH_CLIP_TAP12.md', 'VI'),
        ('02_SAN_XUAT/TIKTOK/Tap12/SPEC_AUDIO_CLIP_TAP12.json', 'VI'),
        ('02_SAN_XUAT/TIKTOK/Tap12_EN/KE_HOACH_CLIP_TAP12_EN.md', 'EN'),
        ('02_SAN_XUAT/TIKTOK/Tap12_EN/SPEC_AUDIO_CLIP_TAP12.json', 'EN'),
        ('02_SAN_XUAT/TIKTOK/Tap12_JA/KE_HOACH_CLIP_TAP12_JA.md', 'JA'),
        ('02_SAN_XUAT/TIKTOK/Tap12_JA/SPEC_AUDIO_CLIP_TAP12.json', 'JA'),
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
                    # Break tags check <#0.35#> format
                    tags = re.findall(r'<#[^>]+#>', t)
                    for tag in tags:
                        if not re.match(r'<#\d+(\.\d+)?#>', tag):
                            print(f"  [{cid} {lid}] INVALID BREAK TAG: '{tag}'")

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

        # 4. English Grammar & Capitalization checks
        if lang == 'EN':
            # Check double words e.g. "the the", "in in"
            m_dup = re.search(r'\b(\w+)\s+\1\b', text, re.IGNORECASE)
            if m_dup and m_dup.group(1).lower() not in ('that', 'had'):
                print(f"  DUPLICATE WORD: '{m_dup.group()}'")

        # 5. Japanese Typography checks
        if lang == 'JA':
            # Check halfwidth punctuation mixing
            m_half = re.search(r'[\u3040-\u30ff\u4e00-\u9faf][,\.!\?]', text)
            if m_half:
                print(f"  HALFWIDTH PUNCTUATION IN JA: '{m_half.group()}'")

    print("\nAudit completed.")

if __name__ == '__main__':
    audit_files()
