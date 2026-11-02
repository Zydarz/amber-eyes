#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem tra link nguồn còn mở được không (GET + Range, không tải hết file)."""
import sys
import urllib.request
import urllib.error

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

URLS = [
    ("ID73", "https://anotherbundyblog.com/wp-content/uploads/2026/08/594300395-edmund-kemper-inside-detective-magazine-i-ll-show-you-where-i-buried-the-pieces-of-their-bodies-1973.pdf"),
    ("FPD74", "https://anotherbundyblog.com/wp-content/uploads/2026/07/ek_front-page-detective-march-1974.pdf"),
    ("SFSU-bata", "https://library.sfsu.edu/bata-db/edmund-kemper-arrested-multiple-murders"),
    ("SFSU-diva", "https://diva.sfsu.edu/collections/sfbatv/12587"),
    ("EKS-609A", "https://edmundkemperstories.com/blog/category/609-a-ord-drive/"),
    ("TPG", "https://tpgonlinedaily.com/dark-side-history-edmund-kemper/"),
    ("LEB-1985", "https://leb.fbi.gov/file-repository/archives/august-1985.pdf"),
    ("OJP-violent", "https://www.ojp.gov/ncjrs/virtual-library/abstracts/violent-crime"),
    ("OJP-organized", "https://www.ojp.gov/ncjrs/virtual-library/abstracts/crime-scene-and-profile-characteristics-organized-and-disorganized"),
    ("FBI-vicap", "https://www.fbi.gov/how-we-investigate/behavioral-analysis"),
    ("OIG", "https://oig.justice.gov/sites/default/files/reports/24-078.pdf"),
    ("WIKI-K", "https://en.wikipedia.org/wiki/Edmund_Kemper"),
    ("BRIT", "https://www.britannica.com/biography/Edmund-Kemper"),
    ("EKS-1964", "https://edmundkemperstories.com/blog/category/1964/"),
    ("INKL", "https://www.inkl.com/news/what-drove-serial-killer-edmund-kemper-to-decapitate-his-mum-and-have-sex-with-her-head"),
    ("SUE", "https://www.suecoletta.com/early-life-of-edmund-kemper/"),
    ("AETV", "https://www.aetv.com/articles/ed-kemper"),
    ("SKC", "https://serialkillercalendar.com/Edmund%20KEMPER.php"),
    ("SOLVE", "https://www.solvethecase.org/offender/2026-104/edmund-emil-kemper-iii"),
    ("COLORADO", "https://coloradocrimepod.castos.com/episodes/episode-32-edmund-kemper-the-co-ed-killer"),
    ("CRIMEINV", "https://www.crimeandinvestigation.co.uk/article/big-ed-edmund-kemper-the-6ft-8-serial-killer"),
    ("ARCHIVE-LUST", "https://archive.org/details/1980-john-douglas-lust-murder-fbi-law-enforcement-bulletin"),
    ("VRONSKY", "https://ia801804.us.archive.org/8/items/english-collections-k-z/Serial%20Killers_%20The%20Method%20and%20Madness%20o%20-%20Peter%20Vronsky.pdf"),
]

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/126.0 Safari/537.36")

ok = bad = 0
for tag, u in URLS:
    req = urllib.request.Request(u, headers={"User-Agent": UA, "Range": "bytes=0-2047"})
    try:
        with urllib.request.urlopen(req, timeout=25) as r:
            code = r.status
            ct = r.headers.get("Content-Type", "?")
            print(f"  [{tag:13}] {code}  {ct[:40]:42} {u[:78]}")
            ok += 1
    except urllib.error.HTTPError as e:
        print(f"  [{tag:13}] HTTP {e.code}  {'':<42} {u[:78]}")
        bad += 1
    except Exception as e:
        print(f"  [{tag:13}] LOI {type(e).__name__}: {str(e)[:60]}")
        bad += 1

print(f"\nMo duoc: {ok}/{len(URLS)} · Loi: {bad}")
