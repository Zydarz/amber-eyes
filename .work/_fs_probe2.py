import requests, json
cid="bL3AVUIgSQ6SnXzHIQjT"
csec="TRVMxItbI2YoljN8he5ONZIAJcKgP2kfIw6XPvhK"
s=requests.Session(); s.headers.update({"User-Agent":"TruyenKyAudio/1.0"})

def probe(name, method, url, **kw):
    try:
        r = s.request(method, url, timeout=45, **kw)
        print(f"[{name}] {method} {url} -> {r.status_code} | {r.text[:300]}\n")
    except Exception as e:
        print(f"[{name}] {method} {url} -> EXC {type(e).__name__}: {e}\n")

# token auth variants
probe("T1_post_token","POST","https://freesound.org/apiv2/apply_authentication_token/",
      data={"client_id":cid,"client_secret":csec,"token_name":"TruyenKyAudio"})
probe("T2_post_token_root","POST","https://freesound.org/apply_authentication_token/",
      data={"client_id":cid,"client_secret":csec,"token_name":"TruyenKyAudio"})
probe("T3_oauth2_get","GET","https://freesound.org/apiv2/oauth2/access_token/",
      params={"client_id":cid,"client_secret":csec,"grant_type":"client_credentials"})
probe("T4_oauth2_post_auth","POST","https://freesound.org/apiv2/oauth2/access_token/",
      auth=(cid,csec), data={"grant_type":"client_credentials"})
probe("T5_oauth2_post_pw","POST","https://freesound.org/apiv2/oauth2/access_token/",
      data={"username":cid,"password":csec,"grant_type":"client_credentials"})
probe("T6_oauth2_post_tokenonly","POST","https://freesound.org/apiv2/oauth2/access_token/",
      data={"client_id":cid,"client_secret":csec})
# does /apiv2/ work at all?
probe("T7_search_noauth","GET","https://freesound.org/apiv2/search/text/",
      params={"query":"rain","fields":"id,name"})
