import requests
KEY="TRVMxItbI2YoljN8he5ONZIAJcKgP2kfIw6XPvhK"
s=requests.Session(); s.headers.update({"Authorization":f"Token {KEY}","User-Agent":"TruyenKyAudio/1.0"})
u="https://freesound.org/apiv2/sounds/346641/download/"
r=s.get(u, timeout=90, allow_redirects=True, stream=True)
print("download ->", r.status_code, r.headers.get("Content-Type"), r.headers.get("Content-Length"))
print("final url:", r.url[:160])
try:
    chunk=next(r.iter_content(8192)); print("bytes:", len(chunk), "head:", chunk[:8])
except Exception as e: print("EXC", e)

print("\n-- rate limit probe: 6 quick calls --")
for i in range(6):
    rr=s.get("https://freesound.org/apiv2/search/text/", params={"query":"door","fields":"id","page_size":1}, timeout=30)
    print(f"  call{i+1}: {rr.status_code} | rem={rr.headers.get('X-RateLimit-Remaining')} lim={rr.headers.get('X-RateLimit-Limit')} retry={rr.headers.get('Retry-After')}")
