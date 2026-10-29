import requests, json
KEY="TRVMxItbI2YoljN8he5ONZIAJcKgP2kfIw6XPvhK"
s=requests.Session(); s.headers.update({"Authorization":f"Token {KEY}","User-Agent":"TruyenKyAudio/1.0"})

r=s.get("https://freesound.org/apiv2/sounds/346641/", params={"fields":"id,name,duration,license,license_attribution,previews,content,download,username,tags,type"}, timeout=45)
print("[detail] ->", r.status_code)
j=r.json()
for k,v in j.items():
    if k=="tags": v=v[:6]
    print(f"  {k}: {str(v)[:220]}")

print("\n[content HEAD]")
try:
    c=j.get("content") or ""
    if c:
        h=s.head(c, timeout=45, allow_redirects=True)
        print("  ", h.status_code, h.headers.get("Content-Type"), h.headers.get("Content-Length"), c)
except Exception as e:
    print("   EXC", e)

print("\n[preview hq mp3 HEAD]")
try:
    p=j["previews"]["preview-hq-mp3"]
    h=s.head(p, timeout=45, allow_redirects=True)
    print("  ", h.status_code, h.headers.get("Content-Type"), h.headers.get("Content-Length"))
    g=s.get(p, timeout=60, stream=True)
    chunk=next(g.iter_content(4096))
    print("   downloaded bytes:", len(chunk), "head:", chunk[:4])
except Exception as e:
    print("   EXC", e)
