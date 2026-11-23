# -*- coding: utf-8 -*-
"""Tập 12 — dùng lại 4 nền đang "thừa" (H22 ①: mọi ảnh sinh phải có shot dùng).

Cổng --plan báo 4 job không shot nào dùng:
  t12_armed_guards_crossbow_perimeter · t12_crumbling_facade_tension
  t12_leo_ryan_podium_applause        · t12_redflag2_silenced_critical_thinking
Các nền này là "bản dư" của bảng ánh xạ cũ (make_bg_jobs_tap12.py) — nội dung
vẫn khớp cảnh nếu gán lại đúng câu, nên DÙNG LẠI thay vì xoá (A11 #167).

Ánh xạ lại (nội dung khớp nguyên văn câu):
  1.07#6  "…luôn có những tay súng thuộc đội an ninh tuần tra cẩn mật ngày đêm"
          → t12_armed_guards_crossbow_perimeter
  2.02#5  "…sự giằng xé nghẹt thở giữa nỗi khát khao được giải cứu" (mặt tiền xác xưởng)
          → t12_crumbling_facade_tension
  1.10#6  "…đại diện các gia đình nạn nhân cùng nhiều phóng viên…"
          → t12_nbc_camera_recording_facade   (1.10#7 giữ press_corps_cameras_microphones)
  2.04#6  "…trước bục giảng giữa Nghị sĩ Ryan và Jim Jones"
          → t12_leo_ryan_podium_applause     (2.04#7 giữ confrontation_at_lectern)
  5.05#4  "…biến tổ chức thành điểm tựa duy nhất chi phối toàn bộ…"
          → t12_redflag2_silenced_critical_thinking

Dùng: py -3 .work/_t12_reuse_unused.py [--apply]
"""
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / "02_SAN_XUAT/Ho_So_Toi_Pham/Tap12/KeHoach_Video_Tap12.md"
BACKUP = ROOT / ".work/_cu/t12_reuse_20261116"

# (mã câu, mã nền MỚI cho câu đó)
REASSIGN = [
    ("1.07#6", "t12_armed_guards_crossbow_perimeter"),
    ("2.02#5", "t12_crumbling_facade_tension"),
    ("1.10#6", "t12_nbc_camera_recording_facade"),
    ("2.04#6", "t12_leo_ryan_podium_applause"),
    ("5.05#4", "t12_redflag2_silenced_critical_thinking"),
]

ROW = re.compile(r"^(\|\s*[1-5]-\d+\s*\|.*)$")


def main():
    apply_ = "--apply" in sys.argv
    text = PLAN.read_text(encoding="utf-8")
    out = []
    done = set()
    for line in text.split("\n"):
        m = ROW.match(line)
        if m:
            cells = line.split("|")
            for i, c in enumerate(cells):
                if "`t12_" in c or "`t1" in c:
                    cau = None
                    for cc in cells[1:4]:
                        mm = re.search(r"`([0-9]+\.[0-9]+#[0-9]+)`", cc)
                        if mm:
                            cau = mm.group(1)
                            break
                    if cau:
                        for target, newbg in REASSIGN:
                            if cau == target and target not in done:
                                cells[i] = re.sub(r"`t\d+_[a-z0-9_]+`", f"`{newbg}`", cells[i])
                                done.add(target)
                                break
            line = "|".join(cells)
        out.append(line)
    new_text = "\n".join(out)
    missing = [t for t, _ in REASSIGN if t not in done]
    print(f"đổi được {len(done)}/{len(REASSIGN)} dòng", f"thiếu: {missing}" if missing else "")
    if not apply_:
        print("DRY-RUN — chạy lại với --apply để ghi.")
        return
    assert not missing, f"thiếu câu: {missing}"
    BACKUP.mkdir(parents=True, exist_ok=True)
    shutil.copy2(PLAN, BACKUP / PLAN.name)
    PLAN.write_text(new_text, encoding="utf-8")
    print(f"đã ghi {PLAN.name} (bản sao: {BACKUP})")


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    main()
