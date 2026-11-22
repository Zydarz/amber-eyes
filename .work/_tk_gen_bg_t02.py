# -*- coding: utf-8 -*-
"""Sinh lai ANH NEN AI cho Tap 02 (18 anh con dung phong crop 16:9).
G6: prompt lay tu file request cu .work/_tk_img_req_t02_b3.json (nguon su that).
Buoc: upload ref local -> temp_url -> generate_image -> giu node_id -> download.
"""
import io, json, os, subprocess, shutil, sys, time

ROOT = r"D:/TEST/Gax/amber-eyes"
RAW = os.path.join(ROOT, "assets/bg/_raw")
OUT = os.path.join(ROOT, ".work/tk_img_raw_t02")
REQ = os.path.join(ROOT, ".work/_tk_img_req_t02_b3.json")
MT = shutil.which("mcode-tools")

# 18 nen con dung phong -> file goc 16:9
PAIRS = [
    ("tk02_podcast_desk", "t2_podcast_desk.jpg"),
    ("tk02_checkpoint", "t2_checkpoint.png"),
    ("tk02_suv_stop", "t2_suv_stop.png"),
    ("tk02_tire_track", "t2_tire_track.png"),
    ("tk02_siren_wall", "t2_siren_wall.jpg"),
    ("tk02_two_drawers", "t2_two_drawers.jpg"),
    ("tk02_two_masks", "t2_two_masks.jpg"),
    ("tk02_command_chair", "t2_command_chair.jpg"),
    ("tk02_stairs_dark", "t2_stairs_dark.jpg"),
    ("tk02_hidden_drive", "t2_hidden_drive.jpg"),
    ("tk02_interrogation_early", "t2_interrogation_early.jpg"),
    ("tk02_head_down", "t2_head_down.png"),
    ("tk02_courtroom", "t2_courtroom.png"),
    ("tk02_gavel", "t2_gavel.png"),
    ("tk02_uniform_fire", "t2_uniform_fire.png"),
    ("tk02_red_flags", "t2_red_flags.jpg"),
    ("tk02_town_snow", "t2_town_snow.png"),
    ("tk02_cottage_search", "t2_cottage_search.jpg"),
]

MIME = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}


def sh(args, timeout=600):
    p = subprocess.run(args, shell=True, capture_output=True, text=True,
                       encoding="utf-8", errors="replace", timeout=timeout)
    return p.returncode, p.stdout, p.stderr


def run_json(args, timeout=600):
    rc, out, err = sh(args, timeout)
    txt = out.strip()
    if not txt:
        txt = err.strip()
    try:
        return rc, json.loads(txt)
    except Exception:
        return rc, {"_raw": txt}


def read_json_any(path):
    for enc in ("utf-8", "utf-8-sig", "utf-16"):
        try:
            return json.load(io.open(path, encoding=enc))
        except Exception:
            continue
    raise IOError("khong doc duoc %s" % path)


def upload(path):
    rc, j = run_json([MT, "upload_temp_url", path])
    if rc != 0 or not isinstance(j, dict):
        return None
    return j.get("temp_url") or j.get("url")


def build(name, ref_file, url):
    src = read_json_any(REQ)
    prompt = src["requests"][0]["prompt"]
    mime = MIME[os.path.splitext(ref_file)[1].lower().lstrip(".")]
    return {
        "prompt": prompt,
        "reference_images": [{"url": url, "mime_type": mime}],
        "aspect_ratio": "9:16",
        "area": "2K",
        "n": 1,
        "output_format": "jpeg",
        "output_file": name,
    }


def generate(reqs, tag):
    af = os.path.join(ROOT, ".work/_tk_img_req_%s.json" % tag)
    rf = os.path.join(ROOT, ".work/_tk_img_receipt_%s.json" % tag)
    with io.open(af, "w", encoding="utf-8", newline="\n") as f:
        json.dump({"requests": reqs}, f, ensure_ascii=False)
    rc, j = run_json([MT, "connector", "call", "connector__matrix__generate_image",
                      "--args-file", af], timeout=900)
    with io.open(rf, "w", encoding="utf-8", newline="\n") as f:
        json.dump(j, f, ensure_ascii=False, indent=1)
    return rc, j


def summarize(j):
    if not isinstance(j, dict):
        return str(j)[:400]
    out = []
    for k in ("code", "message", "status", "error"):
        if k in j:
            out.append("%s=%s" % (k, str(j[k])[:220]))
    si = j.get("success_items")
    if si is not None:
        out.append("success_items=%d" % len(si))
        for it in si[:8]:
            out.append("   %s -> %s" % (it.get("file_name"), it.get("node_id")))
    fi = j.get("failed_items")
    if fi is not None:
        out.append("failed_items=%d" % len(fi))
        for it in fi[:8]:
            out.append("   %s" % str(it)[:220])
    return "\n".join(out) if out else json.dumps(j, ensure_ascii=False)[:600]


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else "test"
    os.makedirs(OUT, exist_ok=True)
    if mode == "test":
        name, ref = PAIRS[0]
        p = os.path.join(RAW, ref)
        print("upload:", p)
        u = upload(p)
        print("temp_url:", (u or "")[:120])
        if not u:
            print("THAT BAI upload")
            sys.exit(2)
        rc, j = generate([build(name, ref, u)], "probe")
        print("rc=", rc)
        print(summarize(j))
    elif mode == "run":
        # probe da sinh xong PAIRS[0] -> receipt "probe" doi ten cho khop quy uoc
        probe = os.path.join(ROOT, ".work/_tk_img_receipt_probe.json")
        if os.path.exists(probe):
            os.replace(probe, os.path.join(ROOT, ".work/_tk_img_receipt_t02_b4.json"))
            print("receipt probe -> _tk_img_receipt_t02_b4.json")
        todo = PAIRS[1:]
        BATCH = 6
        tag = 5
        for i in range(0, len(todo), BATCH):
            chunk = todo[i:i + BATCH]
            reqs = []
            for name, ref in chunk:
                p = os.path.join(RAW, ref)
                u = upload(p)
                if not u:
                    print("UPLOAD FAIL", ref)
                    continue
                reqs.append(build(name, ref, u))
                print("upload ok:", ref)
            if not reqs:
                continue
            rc, j = generate(reqs, "t02_b%d" % tag)
            print("--- batch", tag, "rc=", rc)
            print(summarize(j))
            tag += 1
    elif mode == "receipt":
        # doi ten receipt probe -> b4 (dung khi can chay lai tu dau)
        print("xem .work/_tk_img_receipt_*.json")
