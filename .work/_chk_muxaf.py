import os, subprocess, sys
W = r"D:\TEST\Gax\amber-eyes\.work"
for lang in ("vi", "en", "ja", "ko"):
    code = ("import os,sys;sys.path.insert(0,'" + W.replace("\\", "\\\\") + "');"
            "os.environ['AE_EP']='03';os.environ['AE_LANG']='" + lang + "';"
            "import edition as ED;print(ED.EP.get('mux_af','<MAC DINH - dung chung>'))")
    r = subprocess.run([sys.executable, "-c", code], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    print(f"AE_LANG={lang}: {(r.stdout.strip() or r.stderr.strip()[:150])}")
