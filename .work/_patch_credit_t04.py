"""Patch (byte-level, EOL-safe) — them dong ghi cong Higgs vao mo ta YouTube.

QUY_TAC_AUDIO_HIGGS.md §2: "PHẢI ghi công trong mô tả YouTube mọi tập dùng Higgs"
  This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio

Cách làm (T7 — giữ đường cũ cho T01/T02):
  edition.py : thêm khoá "voice_credit" vào EPISODES["03"] và EPISODES["04"]
  package.py : description() chen {credit_line} ngay sau dong "Giọng đọc, hình ảnh..."
               chi khi EP co "voice_credit" → T01/T02/T03 khong co → van y hien.
Anchor khong chua EOL → script tu chen theo EOL cua file.
"""
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8", errors="replace")
HERE = pathlib.Path(r"D:\TEST\Gax\amber-eyes\.work")

CREDIT = "This audio was created with Boson AI's Higgs Audio — https://www.boson.ai/higgs-audio"


def eol_of(raw):
    return "\r\n" if "\r\n" in raw else "\n"


def patch(path, pairs):
    p = pathlib.Path(path)
    raw = p.read_text(encoding="utf-8", newline="")
    orig = raw
    eol = eol_of(raw)
    for old, new in pairs:
        n = raw.count(old)
        if n != 1:
            raise SystemExit("!! %s: anchor tim thay %d lan (can 1):\n%r" % (path, n, old[:120]))
        raw = raw.replace(old, new)
    if raw == orig:
        raise SystemExit("!! %s: khong doi gi" % path)
    p.write_text(raw, encoding="utf-8", newline="")
    print("OK %s | EOL=%r | +%d dong" % (path.name, eol, raw.count("\n") - orig.count("\n")))


# ---- edition.py: them khoá voice_credit cho EP03 + EP04 --------------------
ed = HERE / "edition.py"
src = ed.read_text(encoding="utf-8", newline="")
eol = eol_of(src)
print("edition.py BOM:", src.startswith("\ufeff"), "| EOL:", repr(eol))
if '"voice_credit"' not in src:
    # EP04: ngay sau dong text_scrim
    a_scrim = '        "text_scrim": ["1-06", "1-10", "1-15", "1-17", "2-08", "4-03", "4-07", "4-13"],'
    if src.count(a_scrim) != 1:
        raise SystemExit("!! edition.py: anchor text_scrim khong dung (%d lan)" % src.count(a_scrim))
    src = src.replace(a_scrim, a_scrim + eol + '        "voice_credit": "%s",' % CREDIT, 1)
    # EP03: ngay truoc dong "title" cua EP03
    i = src.find('"03": {')
    if i < 0:
        raise SystemExit("!! edition.py: khong tim thay EP03")
    j = src.find(eol, src.find('"title":', i))
    if j < 0:
        raise SystemExit("!! edition.py: khong tim thay dong title cua EP03")
    src = src[:j + len(eol)] + '        "voice_credit": "%s",' % CREDIT + eol + src[j + len(eol):]
    ed.write_text(src, encoding="utf-8", newline="")
    print("OK edition.py: +voice_credit cho EP03 + EP04")
else:
    print("edition.py da co voice_credit — bo qua")

# ---- package.py: chen dong ghi cong vao description() ---------------------
_pk = (HERE / "package.py")
_peol = eol_of(_pk.read_text(encoding="utf-8", newline=""))
patch(_pk, [
    ('    summary = " ".join(sents[k] for k in ED.EP["summary"])' + _peol +
     '    txt = f"""{ED.EP["title"]} | Amber eyes',
     '    summary = " ".join(sents[k] for k in ED.EP["summary"])' + _peol +
     '    credit = ED.EP.get("voice_credit", "")' + _peol +
     '    credit_line = ("\\n" + credit) if credit else ""' + _peol +
     '    txt = f"""{ED.EP["title"]} | Amber eyes'),
    ('• Giọng đọc, hình ảnh và âm nhạc được tạo cho kênh bằng công cụ AI.',
     '• Giọng đọc, hình ảnh và âm nhạc được tạo cho kênh bằng công cụ AI.' + _peol +
     '{credit_line}'),
])
