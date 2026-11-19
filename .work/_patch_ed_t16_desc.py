import shutil, re
p = r"d:\TEST\Gax\amber-eyes\.work\edition.py"
shutil.copy(p, r"d:\TEST\Gax\amber-eyes\.work\_cu\t16_pre_build_20261118\edition_before_desc.py")
s = open(p, encoding="utf-8", newline="").read()
a = s.index('    "16": {')
b = s.index('    "17": {')
blk = s[a:b]
i0 = blk.index('        "thumb": ("ĐƯA LÊN"')
i1 = blk.index('        "summary": ("1.02#1"')
new = '''        "thumb_bg": "t16_breeze_knoll_snowy_porch_mail",
        "thumb": ("SEND THEM", "TO HEAVEN") if EN else ("天国へ送るため", "家族を奪った男") if JA else ("ĐƯA LÊN", "THIÊN ĐÀNG"),
        "title": ("Ep. 16: The Man Who Annihilated His Family to 'Send Them to Heaven' — OCPD & the 18-Year Flight (The John List Case)" if EN else
                  "第16話：『家族の魂を天国へ送る』ために全てを奪った男 — 強迫性パーソナリティ障害と18年の逃亡（ジョン・リスト事件）" if JA else
                  "Tập 16: Kẻ Tước Đoạt Mạng Sống Cả Gia Đình Để 'Đưa Họ Lên Thiên Đàng' — OCPD & Cuộc Trốn Chạy 18 Năm (Hồ Sơ John List)"),
        "act_titles": ({1: "Act 1 · The Gloomy Breeze Knoll Mansion and the Horrific Discovery After a Month", 2: "Act 2 · The Vanishing of the Century and the Scissors in the Family Album",
                        3: "Act 3 · Psychological Decoding: OCPD & the Moral-Neutralization Trap", 4: "Act 4 · Frank Bender's Wax Bust and the Call from America's Most Wanted",
                        5: "Act 5 · The Costly Lesson of Control Obsession & 4 Red Flags"} if EN else
                       {1: "第1幕 · 陰鬱なBreeze Knoll邸と一か月後の戦慄の発見", 2: "第2幕 · 世紀の失踪とアルバムの顔を切り抜いたハサミ",
                        3: "第3幕 · 心理解剖：強迫性パーソナリティ障害（OCPD）と道徳的正当化の罠", 4: "第4幕 · Frank Benderの蝋像とAmerica's Most Wantedからの電話",
                        5: "第5幕 · 支配欲の代償と4つのレッドフラグ"} if JA else
                       {1: "Hồi 1 · Biệt thự u ám Breeze Knoll và khám phá kinh hoàng sau một tháng", 2: "Hồi 2 · Vụ mất tích thế kỷ và chiếc kéo cắt mặt trong album ảnh",
                        3: "Hồi 3 · Giải mã tâm lý: Rối loạn nhân cách ám ảnh cưỡng chế (OCPD) & Bẫy ngụy biện đạo đức", 4: "Hồi 4 · Bức tượng sáp của Frank Bender và cú điện thoại từ America's Most Wanted",
                        5: "Hồi 5 · Bài học đắt giá về sự cuồng kiểm soát & 4 cảnh báo đỏ"}),
        "hashtags": "#AmberEyes #TrueCrime #TamLyToiPham #JohnList #BreezeKnoll #OCPD #AmericasMostWanted #FrankBender #TheGiftOfFear #10ChiDauTamLy #CanhBaoDo #PhamVan #HoiTo",
'''
blk = blk[:i0] + new + blk[i1:]
open(p, "w", encoding="utf-8", newline="").write(s[:a] + blk + s[b:])
print("ok")
