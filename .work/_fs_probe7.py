import requests, json
KEY=open(".work/.freesound_key",encoding="utf-8").read().strip()
s=requests.Session(); s.headers.update({"Authorization":f"Token {KEY}","User-Agent":"TruyenKyAudio/1.0"})
BASE="https://freesound.org/apiv2"

r=s.get(f"{BASE}/usage/", timeout=45)
print("[usage] ->", r.status_code)
print(json.dumps(r.json(), ensure_ascii=False, indent=1))

def t(label, params):
    r=s.get(f"{BASE}/search/text/", params={**params,"page_size":4}, timeout=45)
    j=r.json()
    print(f"[{label}] count={j.get('count')}")
    for x in j.get("results",[]): print(f"     {x.get('id')} {x.get('duration',0):>7.2f}s {x.get('name','')[:50]}")
    print()

print("--- query strategies: 'hospital ventilator' ---")
t("2word", {"query":"hospital ventilator","filter":'license:"Creative Commons 0"'})
t("2word_dur30", {"query":"hospital ventilator","filter":'license:"Creative Commons 0" duration:[0 TO 30]'})
t("1word", {"query":"ventilator","filter":'license:"Creative Commons 0" duration:[0 TO 30]'})
t("or", {"query":"(hospital OR room) ventilation","filter":'license:"Creative Commons 0" duration:[0 TO 30]'})
t("tagfilter", {"query":"*","filter":'license:"Creative Commons 0" tag:ventilator duration:[0 TO 30]'})
t("hosp_vent_or", {"query":"hospital ventilation OR hum","filter":'license:"Creative Commons 0" duration:[0 TO 30]'})
