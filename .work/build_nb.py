"""Builder notebook Kaggle cho Higgs Audio v3 — DUNG CHUNG cho pilot v6 va san xuat.

Mot builder, nhieu cau hinh:
  python .work/build_nb.py --mode pilot_v6
  python .work/build_nb.py --mode prod

Cau hinh (CFG) quyet dinh:
  SPEC_NAME    file spec trong dataset (danh sach item + gen_params)
  PAYLOAD_NAME file payload trong dataset (items: id -> text/emotion/ref_wav)
  OUT_NAME     ten thu muc output trong /kaggle/working
  NB_NAME      ten notebook sinh ra
  N_WORKERS    so tien trinh worker (pilot = 1, san xuat = 2)

Ke tu cho LAI: worker.py lay tu .work/higgs_worker.py (ban track duoc).
Verify cuoi: moi code cell phai compile, va khong con placeholder.
"""
import argparse
import ast
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = pathlib.Path(__file__).resolve().parent        # .work/
ROOT = HERE.parent
WORKER_SRC = (HERE / "higgs_worker.py").read_text(encoding="utf-8")

CFG = {
    "pilot_v6": {
        "SPEC_NAME": "pilot_spec_v6.json",
        "PAYLOAD_NAME": "pilot_payload_v6.json",
        "OUT_NAME": "out_higgs_v6",
        "NB_NAME": "higgs_pilot_v6_kaggle.ipynb",
        "N_WORKERS": 1,
        "TITLE": "PILOT v6 — do F0 clone + CER cho 4 clip moi (G9 Tap 02)",
        "MD": """# PILOT v6 — 4 clip tham chieu moi + bien the dich cao do cho vai N1

Do F0 **clone thuc** (khong phai cua clip) cho:
  * H <- M_LOW.wav (nam rat tram) · D <- M_HIGH.wav (nam cao)
  * N1 <- W6_LOW.wav + 4 bien the hao cao do (S25/S30/S35/S40)
  * N2 <- W5_HIGH.wav (nu cao)

Ket qua quyet dinh thang tu **phe gan vai** cho Tap 02 (G9 >= 4 nua cung cho
ca 3 cap nua: C / N1 / N2).

Chay **1 tien trinh** (pilot nho, dung 1 GPU de so sanh nhat quan).

Ket qua khong phu thuoc card nao: seed co dinh theo `(id|role|ref|temp|variant)`.
""",
    },
    "smoke": {
        "SPEC_NAME": "prod_spec_smoke.json",
        "PAYLOAD_NAME": "higgs_payload_smoke.json",
        "OUT_NAME": "out_higgs_smoke",
        "NB_NAME": "higgs_smoke_kaggle.ipynb",
        "N_WORKERS": 2,
        "TITLE": "SMOKE — kiem duong 2 GPU (12 file)",
        "MD": """# SMOKE TEST — kiem duong 2 GPU truoc luot san xuat that

12 file (6 cau x 2 ban, du 5 vai + 1 cau co the emotion) chay tren **2 tien trinh / 2 GPU**.
Dung de chung minh duong chay 2 GPU + merge + catch-up hoat dong truoc khi sinh 406 file.

Ket qua khong phu thuoc card nao: seed co dinh theo `(id|role|ref|temp|variant)`.
""",
    },
    "v7": {
        "SPEC_NAME": "pilot_spec_v7.json",
        "PAYLOAD_NAME": "pilot_payload_v7.json",
        "OUT_NAME": "out_higgs_v7",
        "NB_NAME": "higgs_pilot_v7_kaggle.ipynb",
        "N_WORKERS": 1,
        "TITLE": "PILOT v7 — ban clone W4/W2 cho kit nghe mu H3",
        "MD": """# PILOT v7 — ban clone cua W4 va W2

V7 (QUY_TAC_GIONG_MAU_VOXCPM2.md) yeu cau nguhe mu 4 cap:
**H<->D · H<->W4 · D<->W4 · W2<->C**.

`W4` (nam 50) va `W2` (nu 50) khong phai vai cua Tap 02 => can ban CLONE cua chung
de so voi giong moi cua H/D/C.

Ket qua khong phu thuoc card nao: seed co dinh theo `(id|role|ref|temp|variant)`.
""",
    },
    "v8": {
        "SPEC_NAME": "pilot_spec_v8.json",
        "PAYLOAD_NAME": "pilot_payload_v8.json",
        "OUT_NAME": "out_higgs_v8",
        "NB_NAME": "higgs_pilot_v8_kaggle.ipynb",
        "N_WORKERS": 1,
        "TITLE": "PILOT v8 — bien the TD-PSOLA cho vai N1",
        "MD": """# PILOT v8 — bien the TD-PSOLA thay cho phase vocoder

Pilot v6: clone tu W6_LOW_S25..S40 (phase vocoder) co **CER 9,5-12,5%**, trong khi
chinh clip goc ASR = **0,00%** => phase vocoder lam nhieu, khong phai loi noi dung.
V8 do lai voi bien the **TD-PSOLA** (giai thuoc so + resample FFT) — giu duong bao hinh
am, khong nhoa pha pha.

Do F0 clone thuc + CER cho 3 bien the: -2.0 / -2.5 / -3.0 nua cung.

Ket qua khong phu thuoc card nao: seed co dinh theo `(id|role|ref|temp|variant)`.
""",
    },
    "prod": {
        "SPEC_NAME": "prod_spec.json",
        "PAYLOAD_NAME": "higgs_payload_t02.json",
        "OUT_NAME": "out_higgs_prod",
        "NB_NAME": "higgs_prod_kaggle.ipynb",
        "N_WORKERS": 2,
        "TITLE": "SAN XUAT Tap 02 — Higgs Audio v3 (2 GPU song song)",
        "MD": """# SAN XUAT Tap 02 — Higgs Audio v3 (2 GPU song song)

Sinh toan bo cau thoai Tap 02 theo §7 (2 ban/cau; cau he lo 3 ban).
Chay **2 tien trinh** moi tien trinh 1 GPU (Kaggle cap 2x Tesla T4) => thoi gian giam ~2 lan.

Ket qua khong phu thuoc card nao: seed co dinh theo `(id|role|ref|temp|variant)`
=> moi cau cho cung ket qua bat ke card nao sinh.
""",
    },
    "r2": {
        "SPEC_NAME": "prod_spec_r2.json",
        "PAYLOAD_NAME": "higgs_payload_r2.json",
        "OUT_NAME": "out_higgs_r2",
        "NB_NAME": "higgs_r2_kaggle.ipynb",
        "N_WORKERS": 2,
        "TITLE": "SAN XUAT Tap 02 vong 2 — cau trượt CER (Higgs Audio v3)",
        "MD": """# SAN XUAT Tap 02 — VONG 2 (Higgs Audio v3)

§7: cau co ban tot nhat van vuot CER 2% -> sinh them **2 ban** voi seed khac
(bien 3,4). Khong ghi de ban cu.

Ket qua khong phu thuoc card nao: seed co dinh theo `(id|role|ref|temp|variant)`.
""",
    },
}

p = argparse.ArgumentParser()
p.add_argument("--mode", required=True, choices=sorted(CFG))
args = p.parse_args()
C = CFG[args.mode]
SPEC_NAME = C["SPEC_NAME"]
PAYLOAD_NAME = C["PAYLOAD_NAME"]
OUT_NAME = C["OUT_NAME"]
NB_NAME = C["NB_NAME"]
N_WORKERS_FIXED = C["N_WORKERS"]

# ------------------------------------------------------------------ cells
C1_ENV = '''# ============================================================
# CELL 1 — moi truong + thong tin GPU
# ============================================================
import os, sys, json, time, shutil, subprocess, hashlib, glob
import numpy as np

print("python  :", sys.version.split()[0], "| exe:", sys.executable)
for path in ("/kaggle/working", "/kaggle/input", "/tmp"):
    try:
        u = shutil.disk_usage(path)
        print(f"disk {path}: con {u.free/1e9:.1f} GB / tong {u.total/1e9:.1f} GB")
    except Exception as e:
        print("disk", path, "loi:", e)

try:
    import torch
    print("torch   :", torch.__version__, "| cuda build:", torch.version.cuda)
    print("cuda avail:", torch.cuda.is_available())
    if torch.cuda.is_available():
        N_GPU = torch.cuda.device_count()
        print("VISIBLE GPU COUNT:", N_GPU)
        for i in range(N_GPU):
            p = torch.cuda.get_device_properties(i)
            bf16 = torch.cuda.is_bf16_supported()
            print(f"  GPU{i}: {p.name}  VRAM {p.total_memory/1e9:.1f} GB  cc=sm_{p.major}{p.minor}  bf16={bf16}")
        assert N_GPU >= 1, "khong co GPU"
    else:
        raise RuntimeError("CUDA khong dung -> bat Accelerator: GPU trong Settings")
except Exception as e:
    raise SystemExit(f"LOI torch/GPU: {e}")

print("--- cay /kaggle/input (2 cap) ---")
for root, dirs, files in os.walk("/kaggle/input"):
    if root.count("/") <= 4:
        print(" ", root, "->", sorted(files)[:8])
'''

C2_INSTALL = '''# ============================================================
# CELL 2 — cai dependencies (1 lan cho ca 2 tien trinh)
# ============================================================
!pip install -q --no-input --upgrade "transformers>=5.22" "accelerate>=1.10" "soundfile>=0.13" "huggingface_hub>=0.34"

import torch, transformers, soundfile
print("transformers :", transformers.__version__)
print("torch        :", torch.__version__)
print("soundfile    :", soundfile.__version__)
assert torch.cuda.is_available(), "Chua bat GPU"
'''

C3_DOWNLOAD = '''# ============================================================
# CELL 3 — tai TRONG SO GOC 1 LAN (2 worker dung chung)
# ============================================================
from huggingface_hub import snapshot_download, hf_hub_download

ORIG = "bosonai/higgs-tts-3-4b"
PORT = "multimodalart/higgs-audio-v3-tts-4b-transformers"

MODEL_ROOT = "/tmp/higgs_model"
os.makedirs(MODEL_ROOT, exist_ok=True)
t0 = time.time()
model_dir = snapshot_download(ORIG, local_dir=MODEL_ROOT, max_workers=8)
print(f"trong so goc -> {model_dir}  ({time.time()-t0:.0f}s)")

for fn in ("configuration_higgs_multimodal_qwen3.py", "modeling_higgs_multimodal_qwen3.py"):
    pp = hf_hub_download(PORT, fn, local_dir=model_dir)
    print("loader:", os.path.basename(pp), os.path.getsize(pp), "bytes")

cfg_path = os.path.join(model_dir, "config.json")
cfg = json.load(open(cfg_path, encoding="utf-8"))
cfg["auto_map"] = {
    "AutoConfig": "configuration_higgs_multimodal_qwen3.HiggsMultimodalQwen3Config",
    "AutoModel": "modeling_higgs_multimodal_qwen3.HiggsMultimodalQwen3ForConditionalGeneration",
    "AutoModelForCausalLM": "modeling_higgs_multimodal_qwen3.HiggsMultimodalQwen3ForConditionalGeneration",
}
json.dump(cfg, open(cfg_path, "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print("auto_map da them:", list(cfg["auto_map"].keys()))
print("model_type:", cfg.get("model_type"), "| sample_rate:", cfg.get("sample_rate"))
'''

C4_TASKS = '''# ============================================================
# CELL 4 — tim dataset + dung danh sach task
# ============================================================
def find_dir_containing(filename):
    for root, dirs, files in os.walk("/kaggle/input"):
        if filename in files:
            return root
    return None

REF_DIR = find_dir_containing("__SPEC_NAME__")
print("REF_DIR =", REF_DIR)
assert REF_DIR, "khong tim thay __SPEC_NAME__ trong /kaggle/input"

SPEC = json.load(open(os.path.join(REF_DIR, "__SPEC_NAME__"), encoding="utf-8-sig"))
PAYLOAD = json.load(open(os.path.join(REF_DIR, "__PAYLOAD_NAME__"), encoding="utf-8-sig"))
ITEMS = {it["id"]: it for it in PAYLOAD["items"]}
GP = SPEC["gen_params"]
SR = int(GP["sample_rate"])
TEMP_BY_ROLE = GP.get("temp_by_role", {})
TEMP_DEFAULT = float(GP["temperature"])
VARIANTS = SPEC.get("variants", [0, 1])
print("items:", len(ITEMS), "| variants:", VARIANTS, "| temp_by_role:", TEMP_BY_ROLE)

TASKS = []
for sid in SPEC["items"]:
    it = ITEMS[sid]
    role = it["role"]
    ref = it["ref_wav"]
    temp = float(TEMP_BY_ROLE.get(role, TEMP_DEFAULT))
    # so ban rieng theo cau (§7): cau trich/he lo -> 3 ban, con lai 2 ban
    vs = SPEC.get("variants_by_item", {}).get(sid, VARIANTS)
    for vi in vs:
        key = f"{sid}__{role}__{ref.replace('.wav','')}__{temp:.1f}__s{vi}"
        TASKS.append({"idx": len(TASKS), "key": key, "id": sid, "role": role,
                      "ref_wav": ref, "temp": temp, "variant": vi,
                      "max_new_tokens": int(GP["max_new_tokens"]), "sr": SR})

TASKS_PATH = "/kaggle/working/tasks.json"
json.dump(TASKS, open(TASKS_PATH, "w", encoding="utf-8"), ensure_ascii=False)
print("TASKS:", len(TASKS), "->", TASKS_PATH)
from collections import Counter
print("theo vai:", dict(Counter(t["role"] for t in TASKS)))
print("theo clip:", dict(Counter(t["ref_wav"] for t in TASKS)))
'''

C5_WORKER = '''# ============================================================
# CELL 5 — ghi worker.py (1 file, moi tien trinh chay chung)
# ============================================================
# Worker nhung dang BASE64: an toan voi moi noi dung (khong dung chuoi
# """ trong worker se lam vo chuoi nhung cua cell).
import base64
WORKER = "/kaggle/working/worker.py"
open(WORKER, "wb").write(base64.b64decode("__WORKER_B64__"))
print("worker.py:", os.path.getsize(WORKER), "bytes")
print("dong dau:", open(WORKER, encoding="utf-8").read().splitlines()[0])
'''

C6_LAUNCH = '''# ============================================================
# CELL 6 — khoi dong N tien trinh
# ============================================================
N_WORKERS = min(int(N_GPU), __N_WORKERS__)
print("so tien trinh:", N_WORKERS, "| GPU count:", N_GPU)

PAYLOAD_PATH = os.path.join(REF_DIR, "__PAYLOAD_NAME__")
procs = []
for s in range(N_WORKERS):
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = str(s)      # moi tien trinh 1 card
    env["PYTHONUNBUFFERED"] = "1"
    env["TOKENIZERS_PARALLELISM"] = "false"
    logf = open(f"/kaggle/working/worker_{s}.log", "w", encoding="utf-8")
    cmd = [sys.executable, WORKER,
           "--shard", str(s), "--n-shards", str(N_WORKERS),
           "--out", f"/kaggle/working/shard_{s}",
           "--model-dir", MODEL_ROOT, "--ref-dir", REF_DIR,
           "--payload", PAYLOAD_PATH, "--tasks", TASKS_PATH,
           "--top-p", str(GP["top_p"]), "--top-k", str(GP["top_k"]),
           "--fade-ms", str(GP["fade_in_ms"])]
    pr = subprocess.Popen(cmd, stdout=logf, stderr=subprocess.STDOUT, env=env,
                          start_new_session=True)
    procs.append({"shard": s, "proc": pr, "log": logf,
                   "log_path": f"/kaggle/working/worker_{s}.log"})
    print(f"launch shard {s}: pid={pr.pid} CUDA_VISIBLE_DEVICES={s}")
    if N_WORKERS > 1:
        time.sleep(50)      # tranh 2 tien trinh cung nap model -> peak RAM
print("da launch, bat dau doi...")
'''

C7_WAIT = '''# ============================================================
# CELL 7 — doi ca cac tien trinh, in log
# ============================================================
rcs = {}
for w in procs:
    rc = w["proc"].wait()
    rcs[w["shard"]] = rc
    w["log"].close()
    print(f"shard {w['shard']} exit={rc}")
for w in procs:
    print("=" * 80)
    print("LOG", w["log_path"])
    print("=" * 80)
    try:
        print(open(w["log_path"], encoding="utf-8", errors="replace").read()[-4000:])
    except Exception as e:
        print("doc log loi:", e)
print("exit codes:", rcs)
'''

C8_MERGE = '''# ============================================================
# CELL 8 — gop manifest + gop file wav + tim task thieu
# ============================================================
OUT = "/kaggle/working/__OUT_NAME__"
os.makedirs(OUT, exist_ok=True)

def collect(shard_dir):
    man_p = os.path.join(shard_dir, "manifest.json")
    if not os.path.exists(man_p):
        return []
    return json.load(open(man_p, encoding="utf-8"))

rows = []
for s in range(N_WORKERS):
    sd = f"/kaggle/working/shard_{s}"
    rs = collect(sd)
    print(f"shard_{s}: {len(rs)} dong manifest")
    rows.extend(rs)

merged = {}
for r in rows:
    merged[r["key"]] = r          # trung key -> giu ban cuoi
rows = list(merged.values())

n_moved = 0
for r in rows:
    if not r.get("ok"):
        continue
    src = os.path.join(f"/kaggle/working/shard_{r.get('shard',0)}", r["file"])
    if os.path.exists(src):
        shutil.copy2(src, os.path.join(OUT, r["file"]))
        n_moved += 1
print("da gop file wav:", n_moved, "->", OUT)

MAN_P = os.path.join(OUT, "higgs_manifest.json")
json.dump(rows, open(MAN_P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

done = {r["key"] for r in rows if r.get("ok")}
missing = [t["key"] for t in TASKS if t["key"] not in done]
print("task:", len(TASKS), "| xong:", len(done), "| THIEU:", len(missing))
if missing:
    MP = "/kaggle/working/missing.json"
    json.dump(missing, open(MP, "w", encoding="utf-8"))
    print("da ghi", MP)
'''

C9_CATCHUP = '''# ============================================================
# CELL 9 — CATCH-UP: chay lai task thieu tren GPU0 (1 tien trinh)
# ============================================================
MP = "/kaggle/working/missing.json"
if os.path.exists(MP) and len(json.load(open(MP, encoding="utf-8"))):
    env = os.environ.copy()
    env["CUDA_VISIBLE_DEVICES"] = "0"
    env["PYTHONUNBUFFERED"] = "1"
    env["TOKENIZERS_PARALLELISM"] = "false"
    logf = open("/kaggle/working/worker_cu.log", "w", encoding="utf-8")
    cmd = [sys.executable, WORKER,
           "--shard", "0", "--n-shards", "1", "--only", MP,
           "--out", "/kaggle/working/shard_cu",
           "--model-dir", MODEL_ROOT, "--ref-dir", REF_DIR,
           "--payload", os.path.join(REF_DIR, "__PAYLOAD_NAME__"),
           "--tasks", TASKS_PATH,
           "--top-p", str(GP["top_p"]), "--top-k", str(GP["top_k"]),
           "--fade-ms", str(GP["fade_in_ms"])]
    pr = subprocess.Popen(cmd, stdout=logf, stderr=subprocess.STDOUT, env=env,
                          start_new_session=True)
    rc = pr.wait()
    logf.close()
    print("catch-up exit:", rc)
    print(open("/kaggle/working/worker_cu.log", encoding="utf-8", errors="replace").read()[-3000:])

    cu = collect("/kaggle/working/shard_cu")
    print("catch-up them dong:", len(cu))
    m2 = {r["key"]: r for r in rows}
    for r in cu:
        m2[r["key"]] = r
        if r.get("ok"):
            src = os.path.join("/kaggle/working/shard_cu", r["file"])
            if os.path.exists(src):
                shutil.copy2(src, os.path.join(OUT, r["file"]))
    rows = list(m2.values())
    json.dump(rows, open(MAN_P, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    done = {r["key"] for r in rows if r.get("ok")}
    missing = [t["key"] for t in TASKS if t["key"] not in done]
    print("sau catch-up -> xong:", len(done), "| con thieu:", len(missing))
else:
    print("khong co task thieu -> bo qua catch-up")
'''

C10_SUMMARY = '''# ============================================================
# CELL 10 — tong hop + QC + don model khoi output
# ============================================================
from collections import Counter

ok = [r for r in rows if r.get("ok")]
bad = [r for r in rows if not r.get("ok")]
durs = [r["duration_s"] for r in ok]
gens = [r["gen_s"] for r in ok]
over47 = [r for r in ok if r["duration_s"] > 47]
under05 = [r for r in ok if r["duration_s"] < 0.5]
overpeak = [r for r in ok if r["peak_dbfs"] > -1.5]
longest = sorted(ok, key=lambda r: -r["duration_s"])[:8]

summary = {
    "n_task": len(TASKS), "n_ok": len(ok), "n_fail": len(bad),
    "n_workers": N_WORKERS, "gpu_count": N_GPU,
    "exit_codes": rcs,
    "total_gen_s": round(sum(gens), 1),
    "sec_per_file": round(sum(gens) / len(ok), 2) if ok else 0,
    "dur_min": round(min(durs), 2) if durs else 0,
    "dur_max": round(max(durs), 2) if durs else 0,
    "over_47s": len(over47), "under_0_5s": len(under05),
    "over_peak": len(overpeak),
    "missing": len(missing),
}
json.dump(summary, open(os.path.join(OUT, "higgs_summary.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)

print(json.dumps(summary, ensure_ascii=False, indent=1))
print()
print("theo vai x clip:")
agg = {}
for r in ok:
    k = (r["role"], r["ref_wav"])
    agg.setdefault(k, []).append(r)
for k in sorted(agg):
    v = agg[k]
    ds = sorted(x["duration_s"] for x in v)
    gs = sum(x["gen_s"] for x in v)
    print("  %-3s %-16s n=%-4d dur %5.1f-%5.1f s | gen %6.1f s | %.1f s/file" % (
        k[0], k[1], len(v), ds[0], ds[-1], gs, gs / len(v)))

print()
print("8 file dai nhat:")
for r in longest:
    print("   %-58s %6.2f s" % (r["key"], r["duration_s"]))
if bad:
    print()
    print("FAIL:")
    for r in bad[:20]:
        print("   ", r["key"], "->", r.get("error", "")[:160])

# don model + thu muc shard (chi con wav + json trong output)
try:
    shutil.rmtree(MODEL_ROOT, ignore_errors=True)
except Exception as e:
    print("loi xoa model dir:", e)
for s in list(range(N_WORKERS)) + ["cu"]:
    shutil.rmtree(f"/kaggle/working/shard_{s}", ignore_errors=True)
for s in range(N_WORKERS):
    p = f"/kaggle/working/worker_{s}.log"
    if os.path.exists(p):
        shutil.copy2(p, os.path.join(OUT, f"worker_{s}.log"))
print("disk /kaggle/working con lai:", round(shutil.disk_usage("/kaggle/working").free / 1e9, 1), "GB")
print("file trong output:", len(os.listdir(OUT)))
'''

CELLS = [
    ("markdown", C["MD"]),
    ("code", C1_ENV),
    ("code", C2_INSTALL),
    ("code", C3_DOWNLOAD),
    ("code", C4_TASKS),
    ("code", C5_WORKER),
    ("code", C6_LAUNCH),
    ("code", C7_WAIT),
    ("code", C8_MERGE),
    ("code", C9_CATCHUP),
    ("code", C10_SUMMARY),
]


def md(text):
    return {"cell_type": "markdown", "metadata": {}, "source": text.splitlines(keepends=True)}


def code(text):
    return {"cell_type": "code", "execution_count": None, "metadata": {},
            "outputs": [], "source": text.splitlines(keepends=True)}


nb = {
    "cells": [md(t) if k == "markdown" else code(t) for k, t in CELLS],
    "metadata": {
        "kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"},
        "language_info": {"name": "python", "version": "3.11"},
    },
    "nbformat": 4,
    "nbformat_minor": 5,
}

# thay placeholder trong TAT CA cell (khong chi lan xuat hien dau tien)
import base64  # noqa: E402
subs = {
    "__SPEC_NAME__": SPEC_NAME,
    "__PAYLOAD_NAME__": PAYLOAD_NAME,
    "__OUT_NAME__": OUT_NAME,
    "__N_WORKERS__": str(N_WORKERS_FIXED),
    "__WORKER_B64__": base64.b64encode(WORKER_SRC.encode("utf-8")).decode("ascii"),
}
for c in nb["cells"]:
    if c["cell_type"] != "code":
        continue
    for k, v in subs.items():
        c["source"] = [s.replace(k, v) for s in c["source"]]

OUT_NB = HERE / NB_NAME
OUT_NB.write_text(json.dumps(nb, ensure_ascii=False, indent=1), encoding="utf-8")
print("wrote", OUT_NB, OUT_NB.stat().st_size, "bytes |", len(nb["cells"]), "cells")

# ------------------------------------------------------------------ verify
blob = json.dumps(nb)
problems = []
for ph in list(subs) + ["__WORKER_B64__"]:
    if ph in blob:
        problems.append("placeholder con lai: %s" % ph)
for name, val in (("SPEC_NAME", SPEC_NAME), ("PAYLOAD_NAME", PAYLOAD_NAME),
                  ("OUT_NAME", OUT_NAME)):
    if val not in blob:
        problems.append("thieu chuoi %s (%s)" % (name, val))
if "worker.py" not in blob:
    problems.append("thieu worker.py")

# worker phai parse duoc VA khoi phuc trung nguyen tu base64 trong notebook
try:
    ast.parse(WORKER_SRC)
except SyntaxError as e:
    problems.append("worker khong compile: %s" % e)
b64_in_nb = ""
for c in nb["cells"]:
    if c["cell_type"] != "code":
        continue
    for s in c["source"]:
        if "base64.b64decode(" in s:
            b64_in_nb = s.split('base64.b64decode("')[1].split('")')[0]
if not b64_in_nb:
    problems.append("khong tim thay base64 worker trong notebook")
else:
    try:
        recovered = base64.b64decode(b64_in_nb).decode("utf-8")
    except Exception as e:
        recovered = ""
        problems.append("base64 worker khong decode duoc: %s" % e)
    if recovered != WORKER_SRC:
        problems.append("worker khoi phuc tu notebook KHONG giong file nguon")

bad_cells = []
for i, c in enumerate(nb["cells"]):
    if c["cell_type"] != "code":
        continue
    src = "\n".join(s for s in c["source"] if not s.lstrip().startswith(("!", "%")))
    try:
        ast.parse(src)
    except SyntaxError as e:
        line = src.splitlines()[e.lineno - 1][:100] if e.lineno and e.lineno <= len(src.splitlines()) else "?"
        bad_cells.append((i, "%s | dong: %s" % (e, line)))
if bad_cells:
    problems.append("cell khong compile: %s" % bad_cells)

# worker phai parse duoc
try:
    ast.parse(WORKER_SRC)
except SyntaxError as e:
    problems.append("worker khong compile: %s" % e)

print("verify:", "OK — tat ca dieu kien dat" if not problems else problems)
if problems:
    raise SystemExit(1)
