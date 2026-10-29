import requests, json
cid="bL3AVUIgSQ6SnXzHIQjT"
csec="TRVMxItbI2YoljN8he5ONZIAJcKgP2kfIw6XPvhK"
s=requests.Session()
s.headers.update({"User-Agent":"TruyenKyAudio/1.0"})

def probe(name, method, url, **kw):
    try:
        r = s.request(method, url, timeout=45, **kw)
        body = r.text[:400].replace("\n"," ")
        print(f"[{name}] {method} {url}\n   -> {r.status_code} | {body}\n")
        return r
    except Exception as e:
        print(f"[{name}] {method} {url}\n   -> EXC {type(e).__name__}: {e}\n")

probe("A_oauth2_post","POST","https://freesound.org/apiv2/oauth2/access_token/",
      data={"client_id":cid,"client_secret":csec,"grant_type":"client_credentials"})
probe("B_oauth2_post_noTrailing","POST","https://freesound.org/apiv2/oauth2/access_token",
      data={"client_id":cid,"client_secret":csec,"grant_type":"client_credentials"})
probe("C_apply_auth_noSlash","GET","https://freesound.org/apiv2/apply_authentication_token",
      params={"client_id":cid,"client_secret":csec,"token_name":"TruyenKyAudio"})
probe("D_apply_auth_slash","GET","https://freesound.org/apiv2/apply_authentication_token/",
      params={"client_id":cid,"client_secret":csec,"token_name":"TruyenKyAudio"})
probe("E_me_noauth","GET","https://freesound.org/apiv2/me/")
