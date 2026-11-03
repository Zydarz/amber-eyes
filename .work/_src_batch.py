#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Kiem chung hang loat URL + trich fact tu cache (Tap06 - nguon tham khao).

Usage:
  py -3 .work/_src_batch.py probe  <file_urls.txt>
  py -3 .work/_src_batch.py facts  <file_facts.json>
  py -3 .work/_src_batch.py show   <url> [keyword ...]

facts file = JSON: {"fact_id": {"kw": ["cụm1","cụm2"], "url": ["https://...", ...]}}
Ket qua: in tung dong khop theo fact -> chi dua vao context dong trich.
"""
import hashlib
import json
import re
import sys
import urllib.error
import urllib.request
from html import unescape as html_unescape
from pathlib import Path

CACHE = Path(r"D:/TEST/Gax/amber-eyes/.work/_src_cache")
CACHE.mkdir(parents=True, exist_ok=True)
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0 Safari/537.36")


def fetch(url):
    key = hashlib.sha1(url.encode()).hexdigest()[:16]
    meta = CACHE / f"{key}.meta"
    body = CACHE / f"{key}.txt"
    if meta.exists() and body.exists():
        return meta.read_text(encoding="utf-8"), body.read_text(encoding="utf-8", errors="replace")
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US,en;q=0.9"})
    status, final, err = "", url, ""
    txt = ""
    try:
        with urllib.request.urlopen(req, timeout=45) as r:
            raw = r.read()
            status = str(r.status)
            final = r.geturl()
            ctype = r.headers.get("Content-Type", "")
            txt = raw.decode("utf-8", errors="replace")
            if "html" in ctype.lower() or txt.lstrip()[:200].lower().startswith(("<!doctype", "<html")):
                txt = re.sub(r"(?is)<(script|style|nav|footer|head)[^>]*>.*?</\1>", " ", txt)
                txt = re.sub(r"(?s)<[^>]+>", " ", txt)
                txt = html_unescape(txt)
                txt = re.sub(r"[ \t\r\f\v]+", " ", txt)
                txt = re.sub(r"\n\s*\n+", "\n", txt)
    except urllib.error.HTTPError as e:
        status = f"HTTP {e.code}"
        err = str(e)
    except Exception as e:
        status = "ERR"
        err = repr(e)[:200]
    meta.write_text(f"{status}\t{final}\t{err}\t{len(txt)}", encoding="utf-8")
    body.write_text(txt, encoding="utf-8")
    return meta.read_text(encoding="utf-8"), txt


def status_of(url):
    m, _ = fetch(url)
    parts = m.split("\t")
    return parts[0], parts[1]


def sentences(txt):
    return re.split(r"(?<=[.!?])\s+|\n", txt)


def grep(url, kws, maxlen=430):
    m, txt = fetch(url)
    status = m.split("\t")[0]
    out, seen = [], set()
    for s in sentences(txt):
        low = s.lower()
        if any(k.lower() in low for k in kws):
            s2 = " ".join(s.split())
            if 20 < len(s2) < maxlen and s2 not in seen:
                seen.add(s2)
                out.append(s2)
    return status, out


def main():
    mode = sys.argv[1]
    if mode == "probe":
        urls = [u.strip() for u in Path(sys.argv[2]).read_text(encoding="utf-8-sig").splitlines()
                if u.strip() and not u.strip().startswith("#")]
        for u in urls:
            st, final = status_of(u)
            same = "" if final == u else f"  -> {final}"
            print(f"{st:>8}  {u}{same}")
    elif mode == "facts":
        facts = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8-sig"))
        for fid, spec in facts.items():
            print(f"\n### {fid}")
            for url in spec.get("url", []):
                st, hits = grep(url, spec.get("kw", []))
                print(f"  [{st}] {url}")
                for h in hits[:4]:
                    print("     -", h)
    elif mode == "show":
        st, hits = grep(sys.argv[2], sys.argv[3:])
        print(f"[{st}] {sys.argv[2]}")
        for h in hits:
            print("  -", h)
    else:
        print("mode? probe|facts|show")


if __name__ == "__main__":
    main()
