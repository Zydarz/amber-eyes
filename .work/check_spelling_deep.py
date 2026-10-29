#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os, sys, glob, re
from pathlib import Path

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

ROOT = Path(r"D:\TEST\Gax\Audi")

# Common proper nouns, legal / medical terms in the scripts
WHITELIST = {
    'munchausen', 'fdia', 'kemper', 'cullen', 'rader', 'gacy', 'carter', 'asahara', 'manson',
    'colleen', 'hooker', 'bernardo', 'homolka', 'jonestown', 'pan', 'broderick', 'arias',
    'turpin', 'vallow', 'daybell', 'cruz', 'mcdaniel', 'yates', 'dippolito', 'ramirez',
    'hwasong', 'hwaseong', 'choon', 'jae', 'chul', 'ishikawa', 'kotobuki', 'duong', 'luyen',
    'dahmer', 'milwaukee', 'galveston', 'wichita', 'atascadero', 'vacaville', 'somerville',
    'belleville', 'trenton', 'clarnell', 'strandberg', 'rescorla', 'ressler', 'douglas',
    'speier', 'speir', 'vecuronium', 'digoxin', 'pyxis', 'vicap', 'bsu', 'mmpi', 'macdonald',
    'triad', 'folie', 'deux', 'paraphilia', 'compartmentalization', 'infantilization',
    'gaslighting', 'malingering', 'sociopathy', 'psychopathy', 'sadism', 'masochism',
    'necrophilia', 'hybristophilia', 'schizotypal', 'borderline', 'narcissism', 'histrionic',
    'psychosis', 'postpartum', 'enuresis', 'trophies', 'souvenirs', 'stalker', 'stalking',
    'modus', 'operandi', 'signature', 'autopsy', 'forensic', 'criminology', 'dossier',
    'interrogation', 'affidavit', 'indictment', 'subpoena', 'testimony', 'parole',
    'plea', 'verdict', 'conviction', 'inmate', 'inmates', 'cellblock', 'penitentiary',
    'springfield', 'missouri', 'wisconsin', 'tweed', 'ontario', 'quebec', 'colorado',
    'pueblo', 'guyana', 'kaituma', 'georgetown', 'parkland', 'florian', 'loughren',
    'godejohn', 'flasterstein', 'seligman', 'deedee', 'gypsy', 'blanchard', 'coed',
    'cabrillo', 'fresno', 'pesce', 'luchessa', 'koo', 'schall', 'thorpe', 'liu',
    'hallett', 'brauer', 'colomy', 'chang', 'jackson', 'pogo', 'otero', 'bright',
    'fox', 'davis', 'wagar', 'hedrick', 'conrad', 'roy', 'fairhaven', 'mattapoisett',
    'sarin', 'matsumoto', 'tokyo', 'subway', 'tasmania', 'port', 'arthur', 'sharon',
    'tate', 'lafferty', 'redhook', 'shue', 'corll', 'bundy', 'toole', 'lucas',
    'lucasville', 'chikatilo', 'onoprienko', 'shipman', 'sobhraj', 'pichushkin',
    'katherine', 'knox', 'tate', 'labianca', 'folger', 'frykowski', 'sebring',
    'parent', 'kasabian', 'atkins', 'krenwinkel', 'van', 'houten', 'watson', 'grogan',
    'hinman', 'shea', 'polanski', 'melcher', 'spahn', 'barker', 'gifford', 'speck',
    'corll', 'henley', 'brooks', 'shawcross', 'alcala', 'bonin', 'kraft', 'bittaker',
    'norris', 'wuornos', 'chattanooga', 'bando', 'shoko', 'aum', 'shinrikyo', 'murai',
    'hayakawa', 'nakagawa', 'okazaki', 'tsutsumi', 'sakamoto', 'kameido', 'anthrax',
    'botulinum', 'vx', 'phosgene', 'jonestown', 'peoples', 'temple', 'marceline',
    'marxism', 'apostolic', 'socialism', 'georgetown', 'kaituma', 'ryan', 'speier',
    'holsinger', 'dwyer', 'layton', 'prokes', 'parkes', 'touchstone', 'bogues',
    'jennifer', 'pan', 'hann', 'bich', 'ha', 'felix', 'wong', 'daniel', 'marks',
    'mylvaganam', 'carty', 'crawford', 'rhodes', 'markham', 'ontario', 'ryerson',
    'maryville', 'betty', 'broderick', 'dan', 'linda', 'kolkena', 'coronado',
    'la', 'jolla', 'san', 'diego', 'notre', 'dame', 'cornell', 'jodi', 'arias',
    'travis', 'alexander', 'mormon', 'mesa', 'arizona', 'yreka', 'flores', 'martinez',
    'demarte', 'samuels', 'alyssa', 'stephen', 'lauren', 'giddings', 'mercer',
    'macon', 'georgia', 'mcdaniel', 'maryland', 'andrea', 'yates', 'rusty', 'noah',
    'john', 'paul', 'luke', 'mary', 'houston', 'texas', 'dietz', 'resnick',
    'dalia', 'dippolito', 'michael', 'boynton', 'beach', 'florida', 'wipf', 'shihadeh',
    'ramirez', 'night', 'stalker', 'el', 'paso', 'richard', 'munoz', 'pentagram',
    'san', 'francisco', 'los', 'angeles', 'whittier', 'rosemead', 'monterey',
    'park', 'lee', 'choon', 'jae', 'hwaseong', 'suwon', 'gyeonggi', 'yoo',
    'young', 'chul', 'seoul', 'sinsa', 'dong', 'gu', 'jongno', 'gangnam',
    'ishikawa', 'miyuki', 'kotobuki', 'tokyo', 'itabashi', 'shinjuku', 'postwar',
    'nguyen', 'hai', 'duong', 'vu', 'van', 'tien', 'thoai', 'my', 'le', 'chinh',
    'anh', 'quoc', 'linh', 'binh', 'phuoc', 'chon', 'thanh', 'anh', 'le',
    'van', 'luyen', 'ngoc', 'bich', 'phuong', 'thao', 'bac', 'giang', 'luc',
    'nam', 'phuong', 'dong', 'dahmer', 'jeffrey', 'lionel', 'shari', 'joyce',
    'flint', 'bath', 'ohio', 'milwaukee', 'oxford', 'marquette', 'ambassador',
    'sinthasomphone', 'edwards', 'tracy', 'boyle', 'mccann', 'scarver', 'columbia'
}

def check_words():
    print("Checking for potential typos / strange characters...")
    weird_chars = re.compile(r'[^\x00-\x7F\u2010-\u2026\u2018-\u201D\u00C0-\u024F]')
    for ep in range(1, 30):
        p = ROOT / "01_KICH_BAN" / f"Tap{ep:02d}_EN" / f"kichban_tap{ep:02d}_EN.md"
        text = open(p, encoding='utf-8').read()
        
        # Check weird chars (corrupted UTF-8 like Ã, Â, etc)
        corrupted = re.findall(r'[ÃÂÁÀẢÃẠÂẤẦẨẪẬĂẮẰẲẴẶÉÈẺẼẸÊẾỀỂỄỆÍÌỈĨỊÓÒỎÕỌÔỐỒỔỖỘƠỚỜỞỠỢÚÙỦŨỤƯỨỪỬỮỰÝỲỶỸỴĐ]', text)
        
        # Check text lines
        lines = [l for l in text.splitlines() if not l.startswith('#') and not l.startswith('|') and not l.startswith('**[')]
        
        notes = []
        if corrupted:
            # check if it's in Vietnamese names (like Nguyễn Hải Dương or Lê Văn Luyện), which is expected
            if ep not in (27, 28):
                notes.append(f"Unexpected accented characters in non-VN episode: {set(corrupted)}")
                
        if notes:
            print(f"Tap {ep:02d}: {', '.join(notes)}")
        else:
            print(f"Tap {ep:02d}: Clean")

if __name__ == '__main__':
    check_words()
