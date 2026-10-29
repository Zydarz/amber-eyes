import requests, json
KEY=open(".work/.freesound_key",encoding="utf-8").read().strip()
s=requests.Session(); s.headers.update({"Authorization":f"Token {KEY}","User-Agent":"TruyenKyAudio/1.0"})
BASE="https://freesound.org/apiv2/search/text/"
def t(label, params):
    r=s.get(BASE, params={**params, "page_size":3}, timeout=45)
    try: j=r.json()
    except Exception: print(f"[{label}] {r.status_code} <no json> {r.text[:150]}"); return
    if r.status_code!=200:
        print(f"[{label}] {r.status_code} {r.text[:250]}"); return
    print(f"[{label}] count={j.get('count')} results={len(j.get('results',[]))}")
    for x in j.get("results",[]): print(f"     {x.get('id')} {x.get('name','')[:45]} | {x.get('license')}")
    print()

t("no_filter", {"query":"hospital ventilator"})
t("lic_cc0_space", {"query":"hospital ventilator","filter":'license:"Creative Commons 0"'})
t("lic_cc0_bracket", {"query":"hospital ventilator","filter":"license:[Creative Commons 0 TO Creative Commons 0]"})
t("lic_cc0_01", {"query":"hospital ventilator","filter":'license:"Creative Commons 0" duration:[0 TO 30]'})
t("simple_query_noLic", {"query":"ventilator","filter":'license:"Creative Commons 0"'})
t("rain_cc0", {"query":"rain","filter":'license:"Creative Commons 0"'})
t("dur_only", {"query":"hospital ventilator","filter":"duration:[0 TO 30]"})
