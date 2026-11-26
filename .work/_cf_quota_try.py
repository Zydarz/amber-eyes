"""Thử 1 request Cloudflare (nhẹ� nhất có thể) để xem quota đã reset chưa."""
import json
import sys
import urllib.request
import urllib.error
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
from flux_client import get_account_pool

MODEL = "@cf/black-forest-labs/flux-1-schnell"
pool = get_account_pool()
for i, acc in enumerate(pool):
    url = f"https://api.cloudflare.com/client/v4/accounts/{acc['id']}/ai/run/{MODEL}"
    payload = json.dumps({"prompt": "quiet empty street at dawn", "steps": 4}).encode("utf-8")
    headers = {"Authorization": f"Bearer {acc['token']}", "Content-Type": "application/json"}
    req = urllib.request.Request(url, data=payload, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=90) as resp:
            data = json.loads(resp.read().decode("utf-8"))
            ok = bool(data.get("success") and data.get("result", {}).get("image"))
            print(f"[{i}] slot{i} {acc['id'][:6]}...{acc['id'][-4:]}: {'SỐNG' if ok else 'khong co anh'}")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="ignore")
        msg = body
        try:
            msg = json.loads(body)["errors"][0]["message"]
        except Exception:
            pass
        print(f"[{i}] slot{i} {acc['id'][:6]}...{acc['id'][-4:]}: HTTP {e.code} :: {msg[:150]}")
    except Exception as ex:
        print(f"[{i}] slot{i}: ERR {ex}")
