import requests, json
KEY="TRVMxItbI2YoljN8he5ONZIAJcKgP2kfIw6XPvhK"
CID="bL3AVUIgSQ6SnXzHIQjT"
s=requests.Session(); s.headers.update({"User-Agent":"TruyenKyAudio/1.0"})

def probe(name, method, url, **kw):
    try:
        r = s.request(method, url, timeout=45, **kw)
        print(f"[{name}] -> {r.status_code}")
        t=r.text
        try:
            j=r.json(); print("   ", json.dumps(j, ensure_ascii=False)[:600])
        except Exception:
            print("   ", t[:300])
        print()
        return r
    except Exception as e:
        print(f"[{name}] -> EXC {type(e).__name__}: {e}\n")

probe("M1_me_header","GET","https://freesound.org/apiv2/me/", headers={"Authorization":f"Token {KEY}"})
probe("M2_me_param","GET","https://freesound.org/apiv2/me/", params={"token":KEY})
probe("M3_search_param","GET","https://freesound.org/apiv2/search/text/",
      params={"query":"rain on window","token":KEY,"fields":"id,name,duration,license,previews","page_size":3})
probe("M4_search_header","GET","https://freesound.org/apiv2/search/text/",
      headers={"Authorization":f"Token {KEY}"}, params={"query":"thunder","fields":"id,name,duration","page_size":2})
