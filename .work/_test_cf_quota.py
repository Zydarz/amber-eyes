#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gọi thử Cloudflare FLUX 1 lần để xem NỘI DUNG lỗi 429 (hết quota ngày hay rate-limit)."""
import json
import sys
import urllib.error
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / ".work"))
import flux_client

pool = flux_client.get_account_pool()
print(f"pool: {len(pool)} account")
for i, acc in enumerate(pool):
    url = f"https://api.cloudflare.com/client/v4/accounts/{acc['id']}/ai/run/{flux_client.DEFAULT_MODEL}"
    payload = json.dumps({"prompt": "a small dark ceramic mask on a wooden table, noir", "steps": 1}).encode()
    req = urllib.request.Request(url, data=payload, headers={
        "Authorization": f"Bearer {acc['token']}", "Content-Type": "application/json"}, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = json.loads(resp.read().decode())
            ok = data.get("success")
            print(f"[{i+1}] {acc['id'][:8]}... HTTP 200 success={ok}")
            if ok:
                print("   -> ACCOUNT NAY CON QUOTA, dung duoc.")
                break
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        print(f"[{i+1}] {acc['id'][:8]}... HTTP {e.code}")
        print("   ", body[:400].replace("\n", " "))
    except Exception as e:
        print(f"[{i+1}] {acc['id'][:8]}... LOI: {e}")
