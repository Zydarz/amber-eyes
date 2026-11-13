# -*- coding: utf-8 -*-
import subprocess, sys, re
sys.path.insert(0, '.work')
import parse_kichban as PK

# Read original JA script
txt = subprocess.check_output(['git', 'show', 'HEAD:01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md'], encoding='utf-8')
ja_orig = PK.parse_lines(txt.splitlines())

# Map original elements by id
orig_map = {el['id']: el for el in ja_orig}

# Define new sentences for the added/expanded turns
new_turns = {
    '1.07': [
        "社会心理学の観点から見れば、Bayview Drive 57番地のピンクの家の仮面は、『ハロー効果』と『郊外の盲点』に関する古典的な研究事例と言えます。",
        "人間の脳には先天的な認知の偏りがあり、若く美しく社会的地位のある職に就き洗練された物腰を持つ人物は、内面も高潔であると無意識に思い込んでしまうのです。",
        "PaulとKarlaが生身のケンとバービーという完璧な偶像をまとったとき、彼らは地域社会の防衛本能を完全に麻痺させる目に見えない盾を築き上げました。",
        "暗い路地に潜む薄汚れた不審者には誰もが警戒しますが、夕暮れ時に笑顔で犬を散歩させバラの垣根を手入れする中流階級の若夫婦に対しては、完全に警戒を解いてしまうのです。"
    ],
    '1.08': [
        "そしてその盲信の代償として、オンタリオ州南部は5年もの間、集団的な疑心暗鬼と恐怖に包まれることになりました。",
        "かつて平穏だった湖畔の通りは、突如として見えない恐怖が徘徊する狩場へと変貌したのです。",
        "親たちは娘を一人で登校させることを恐れ、バス停や公園では人々が互いに疑いの目を向け合いました。",
        "日常の安心感が根底から崩れ去ったとき、悪魔は醜い化け物の姿ではなく白昼の御伽噺のような馬車の上から微笑みかけていたという戦慄の真実を人々は突きつけられました。"
    ],
    '2.06_add': [
        "このような凶行の息苦しい闇の中で、カナダの司法史は勇気の灯火としてKristen Frenchの名を永遠に記憶しています。",
        "その15歳の少女は決して絶望に屈することなく、命乞いをして尊厳を捨てることもありませんでした。",
        "並外れた強靭な意志をもって、Kristenは自らの尊厳を守るため最後の息を引き取る瞬間まで勇敢に戦い抜きました。",
        "彼女が犯人の肉体に刻みつけた抵抗の爪痕は、Paul BernardoのDNAを捉え、彼を法の裁きへと引きずり出すかけがえのない法医学の鍵となったのです。",
        "Kristenの気高い姿は、たとえ肉体が監禁されようとも、人間の尊厳と誇りは何者にも奪い去ることのできないものであることを私たちに教えてくれます。"
    ],
    '2.09_add': [
        "行動科学の視点から言えば、家庭用ビデオカメラを用いて犯行の一部始終を記録し続けた異常なこだわりこそ、極度の人格歪曲を反映した『心理的署名（シグネチャー）』にほかなりません。",
        "Paul Bernardoにとって、そのカメラは単なる記録媒体ではなく、自己顕示欲を満たす『神経学的トロフィー』でした。",
        "サディスティックな自己愛パーソナリティを持つ者は自らの無力感に対する無意識の恐怖を常に抱えており、日常の卑小さに直面するたび、映像を見返すことで全能の支配幻想を再点火していたのです。",
        "そしてKarla Homolkaにとって、自ら画角を調整し犠牲者に冷酷な指示を浴びせ続けた行為は、捕食者の対等な共犯者として他者の運命を握ることに歪んだ権力快感を見出していたという堕落を告発する明白な証拠です。"
    ],
    '3.06_add': [
        "実の姉がなぜ妹を罠に誘い込み、その後で悲嘆に暮れる遺族のように葬儀で涙を流すことができたのか、多くの人々が疑問に思うはずです。",
        "その答えは、『極端な区画化（コンパートメンタリゼーション）』と『中和の技術』にあります。",
        "Karla Homolkaの頭脳の中では、家族を愛する心優しい女性としての世界と夜の冷酷な共犯者としての世界が、病理学的な鋼鉄の壁で完全に切り離されていました。",
        "彼女は妹のTammyを差し出すことはPaulの暗い渇望を宥め自らのピンクの結婚生活を守るための『必要な犠牲』なのだと自己正当化し、自らの良心を歪んだ論理で麻痺させました。",
        "人間が自己愛的な依存のために血の絆や最低限の人倫を踏みにじるとき、その精神は完全な『道徳的昏睡』へと陥ります。",
        "彼らの目にはもはや助けを求める無辜の命は映らず、自らの利己的な自我を守るための障害物か道具にしか見えなくなるのです。"
    ],
    '4.06': [
        "なぜKarla Homolkaは1993年の司法取引の際、捜査官たちの前で激しく号泣し、胸を引き裂くような後悔を見せたのでしょうか。",
        "この女の精神の深層では、いったい何が起きていたのでしょうか。",
        "なぜ後悔したのか。",
        "それは虐待された被害者としての真の良心の目覚めだったのか、それとも司法史上で最も冷酷に計算された心理劇だったのでしょうか。",
        "先生、この現象の根底にある心理メカニズムの本質とは何だったのでしょうか。"
    ],
    '4.07': [
        "これこそが司法心理学における最大の難問です。",
        "私たちは二つの概念を明確に区別しなければなりません、すなわち『真の後悔』と『被害者面による操作』です。",
        "他の事件では、共犯者が支配者から解放された際、通常は『道徳的トラウマ』を経験し、自らの所業に対する激しい自己嫌悪に苛まれ法の裁きを甘受します。",
        "しかしKarla Homolkaの場合、行動科学の専門家たちは『女性特有の精神病質（サイコパシー）』と『悪性自己愛』が融合した典型的な症例と診断しています。",
        "1993年の交渉の席で彼女が流した涙は、TammyやLeslie、Kristenの命を悼むものでは決してありませんでした。",
        "それは『病理学的な自己憐憫』であり、Paulによる懐中電灯での暴行によって愛の幻想が打ち砕かれた後、自らが終身刑に直面することへの恐怖から泣いていたにすぎません。",
        "彼女は司法制度の最大の盲点を瞬時に見抜き、社会は身体に傷を負った美しい若い女性に対して無条件の寛容と同情を注ぎがちであるという点を利用しました。",
        "『虐待された女性の症候群』の衣をまとうことで、彼女は自ら能動的に加担した凶行を抵抗不能な強要によるものへと巧妙にすり替えました。",
        "Karlaの後悔とは、12年という懲役と引き換えに自由への切符を買い取るための、冷徹に計算された商取引にすぎなかったのです。"
    ],
    '4.08': [
        "そしてその司法の悲劇は、決定的な証拠を握っていた者たちの道徳的苦悩によって、いっそう苦渋に満ちたものとなりました。",
        "1993年5月、弁護士のKen Murrayが天井裏から6本のビデオテープを回収したとき、彼は職業倫理の恐るべき罠に嵌まり込みました。",
        "一方には弁護士と依頼人間の厳格な秘密保持特権があり、もう一方には冷酷な共犯者が検察全体を欺いている現実を前にした人間としての良心がありました。",
        "彼がそれらのテープを17か月間金庫に秘匿したことが、結果として『悪魔との取引』の承認を許してしまったのです。",
        "それは痛烈な教訓を物語っています、すなわち法の技術的規則が人間の良心や客観的真実から切り離されたとき、正義そのものが凶悪犯の犠牲者となり果てるということです。"
    ],
    '5.04': [
        "しかし、その苦渋に満ちた司法取引が覆せないものとなった後も、親子の神聖な愛の絆は不屈の歴史を紡ぎ出しました。",
        "Kristen Frenchの両親であるDougとDonna French夫妻は、胸を引き裂かれる絶望に屈することはありませんでした。",
        "彼らは気高く立ち上がり、底知れぬ喪失感を、娘とすべての犠牲者の尊厳を守るための粘り強い法廷闘争へと昇華させたのです。",
        "証拠のビデオテープを永久に封印し破棄させるため最後まで戦い抜き、愛する我が子の苦しみが大衆の好奇の目に晒されることを断固として阻止しました。",
        "さらに、ナイアガラ地域に設立されたKristen French児童保護センターは、数十年にわたり何千人もの傷ついた子どもたちを救い、癒し続けています。",
        "それこそが、破壊の闇に対する不滅の愛の偉大な勝利なのです。"
    ],
    '5.07_add': [
        "2005年7月4日、Karla Homolkaが12年の刑期を満了して刑務所の門を出たとき、彼女は司法の手続き上は勝利したかもしれませんが、人類の良心の法廷においては永遠の敗北者となりました。",
        "何千人ものカナダ市民が猛烈な怒りとともに街頭へ繰り出し、抗議の声を上げました。",
        "肉体的な監禁は終わっても、社会的追放という判決は彼女の最後の息まで追い続けることになります。",
        "Leanne Bordelaisと名を変えカリブ海の孤島へ逃亡しようとも、凶行の影と欺瞞の記憶は常に彼女を捕らえ続けました。",
        "地域社会は明確なメッセージを突きつけ、人間は芝居がかった涙に一時的に欺かれることはあっても、時間と真実は必ず無辜の魂の尊厳を取り戻すという事実を宣言しました。",
        "自己の利己的な欲望のために他者の命を奪った者に対し、社会の良心が許しを与えることは決してありません。"
    ]
}

# Read VN script to get exact sequence of elements
vn = PK.parse_file('01_KICH_BAN/Tap11/kichban_tap11_23102026.md')

# Generate output lines
out = []
out.append("# 犯罪心理学オーディオ／ポッドキャスト台本 — 日本語版")
out.append("**テーマ：** 10の心理的指標と行動エスカレーションの法則――Paul Bernardo & Karla Homolka事件（『ケンとバービー』および『悪魔との取引』）")
out.append("**原文:** `01_KICH_BAN/Tap11/kichban_tap11_23102026.md`。ベトナム語版と完全1:1対応（同一構造・同一ID・同一文数）。")
out.append("**事実・法務チェック:** 公開された裁判記録、オンタリオ州警察の捜査資料、および公的学術文献に基づく客観的記述。")
out.append("**バージョン：** 基準A2c/K10――10の心理・行動生態系および多次元心理変容分析を統合した最新改訂版（2026年11月13日）。")
out.append("")
out.append("---")
out.append("")
out.append("## 制作仕様とナレーション構成（PRODUCTION BRIEF）")
out.append("")
out.append("| 項目 | オーディオ番組の標準設定（ホスト主導のドキュメンタリー） |")
out.append("| :--- | :--- |")
out.append("| **エピソード名** | 第11話：ケンとバービー――共有妄想（フォリー・ドゥ）と悪魔との取引（Paul Bernardo & Karla Homolka事件簿） |")
out.append("| **形式** | 調査ドキュメンタリー型ポッドキャスト（ナレーター主導型ドキュメンタリー）――**ホスト**が物語の背骨を担い、感情の流れを整え、物語の鍵となる緊張の局面ごとに専門家の視点（捜査官、心理学者、一般人）を招く。 |")
out.append("| **想定総時間** | 28 – 32分（5つの本編章＋音声による場面転換） |")
out.append("| **BGM設定** | Dark Ambient, 重厚なチェロ, ミニマルピアノ, サブベースドローン。ナレーション下では-26dB、場面転換では-14dB。 |")
out.append("| **キャスト構成** | - **ホスト（約48%）：** 温かく低い声、物語の主軸と人間的洞察<br>- **捜査官（約24%）：** 冷徹で事実重視の声、現場検証と手口対署名<br>- **心理学者（約22%）：** 学術的で深い声、共有妄想（フォリー・ドゥ）と被害者面の病理解剖<br>- **一般人（約6%）：** N1（第1幕：愕然とする近隣住民、4文）、N2（第4幕：苦渋に満ちた検察官、5文） |")
out.append("| **引用ルール** | 劇中のすべての引用文は記録と100%一致。引用符『 』で明記。 |")
out.append("| **主要参照元** | ナイアガラ地域警察およびトロント警察の捜査記録 · オンタリオ州上級裁判所の判決記録（Patrick Galligan裁判官、Archie Campbell裁判官） · Campbell報告書（1996） · Galligan報告書（1996） · 『Invisible Darkness』（Stephen Williams） · 『Deadly Innocence』（Scott Burnside & Alan Cairns） · 『The Gift of Fear』（Gavin de Becker）。 |")
out.append("")
out.append("---")
out.append("")

# Helper for element text
# Map VN element to corresponding text in JA
# Act 1
out.append("## 第1幕：つかみ――『ケンとバービー』完璧な仮面の裏側 (00:00 – 05:20)")
out.append("")
out.append("**[BGM]:** *静寂の中に哀愁を帯びたチェロの旋律がゆっくりと響き、オンタリオ湖畔の冷たい風の音と重なり合う。*")
out.append("")
out.append("**[SFX]:** *乾杯のグラスが触れ合う軽快な音、野外の結婚祝宴で陽気に流れるダンス音楽の響き。*")
out.append("")
out.append("**ホスト** *(穏やかで深みのある声で、追憶の空間を静かに切り開く)*:")
for s in orig_map['1.03']['sentences']: out.append(s['text'])
out.append("")
out.append("**[Nghỉ 1.5 giây – khoảng lặng kịch tính]**")
out.append("")
out.append("**ホスト** *(声のトーンを落とし、忍び寄る破滅の気配を告げる)*:")
for s in orig_map['1.05']['sentences']: out.append(s['text'])
out.append("")
out.append("**一般人** *(N1: Port Dalhousieの近隣住民、若い女性の愕然とし詰まるような声)*:")
for s in orig_map['1.06']['sentences']: out.append(s['text'])
out.append("")
out.append("**心理学者** *(学術的で深みのある落ち着いた声)*:")
for s in new_turns['1.07']: out.append(s)
out.append("")
out.append("**ホスト** *(重々しく思索に富んだ声)*:")
for s in new_turns['1.08']: out.append(s)
out.append("")
out.append("**[SFX]:** *サイレンが夜の静寂を切り裂き、捜査資料が次々と激しくめくられる音。*")
out.append("")
out.append("**ホスト** *(低く張り詰めた声で、戦慄の対比を際立たせる)*:")
for s in orig_map['1.08']['sentences']: out.append(s['text'])
out.append("")
out.append("**[Nghỉ 1.5 giây – khoảng lặng kịch tính]**")
out.append("")
out.append("**捜査官** *(冷徹で鋭い声で、警察の実務記録を再現する)*:")
for s in orig_map['1.10']['sentences']: out.append(s['text'])
out.append("")
out.append("**ホスト** *(憂慮を帯びた声で、世論の激震を語る)*:")
for s in orig_map['1.11']['sentences']: out.append(s['text'])
out.append("")
out.append("**[SFX]:** *重い鉄の扉が硬く閉ざされる決定的な響き。*")
out.append("")
out.append("**ホスト** *(威厳を保ち、深層分析の主題へと導く)*:")
for s in orig_map['1.13']['sentences']: out.append(s['text'])
out.append("")

# Act 2
out.append("## 第2幕：現場検証とエスカレーションの深淵――4段階の凶行 (05:20 – 11:00)")
out.append("")
out.append("**[BGM]:** *冷たく爪弾かれるミニマルピアノの旋律に、夜の静寂の中で鈍く響くキーボードの打鍵音が交錯する。*")
out.append("")
out.append("**ホスト** *(抑制の効いた低い声で、現場の行動分析へと導く)*:")
for s in orig_map['2.02']['sentences']: out.append(s['text'])
out.append("")
out.append("**[SFX]:** *紙の捜査資料がめくられる音と、マウスのクリック音。*")
out.append("")
out.append("**捜査官** *(冷徹で断固たる声で、証拠事実をひとつひとつ強調する)*:")
for s in orig_map['2.04']['sentences']: out.append(s['text'])
out.append("")
out.append("**[Nghỉ 1.5 giây – khoảng lặng kịch tính]**")
out.append("")
out.append("**ホスト** *(沈痛な面持ちで、犠牲者の尊厳と勇気を称える)*:")
for s in orig_map['2.06']['sentences']: out.append(s['text'])
for s in new_turns['2.06_add']: out.append(s)
out.append("")
out.append("**捜査官** *(力強く、犯行の手口と心理的署名を明確に区別する)*:")
for s in orig_map['2.07']['sentences']: out.append(s['text'])
out.append("")
out.append("**[SFX]:** *ビデオカセットが回転するかすかな摩擦音と、機械式カメラのシャッター音。*")
out.append("")
out.append("**心理学者** *(学術的な視点から、映像証拠の深層心理を解剖する)*:")
for s in orig_map['2.09']['sentences']: out.append(s['text'])
for s in new_turns['2.09_add']: out.append(s)
out.append("")
out.append("**ホスト** *(低く落ち着いた声で、精神病理の分析へと繋ぐ)*:")
for s in orig_map['2.10']['sentences']: out.append(s['text'])
out.append("")
out.append("**[BGM]:** *チェロの不穏な低音が深く響き渡り、息の詰まるようなサブベースへと移り変わる。*")
out.append("")
out.append("**捜査官** *(冷徹に現場の全体像を締めくくり、心理ファイルを開く)*:")
for s in orig_map['2.12']['sentences']: out.append(s['text'])
out.append("")

# Act 3
out.append("## 第3幕：病理的同盟の解明――共有妄想と道徳的中和 (11:00 – 16:40)")
out.append("")
out.append("**[BGM]:** *重苦しく哀愁を帯びたチェロの低音がサブベースと重なり合い、精神分析の手術室のような緊張感を醸し出す。*")
out.append("")
out.append("**ホスト** *(問題の核心を突き、心理分析のメスを入れる)*:")
for s in orig_map['3.02']['sentences']: out.append(s['text'])
out.append("")
out.append("**[Nghỉ 1.5 giây – khoảng lặng kịch tính]**")
out.append("")
out.append("**心理学者** *(明晰で学術的な声で、共有妄想現象を解剖する)*:")
for s in orig_map['3.04']['sentences']: out.append(s['text'])
out.append("")
out.append("**ホスト** *(沈痛に思索を深め、犠牲者のモノ化の深層に迫る)*:")
for s in orig_map['3.05']['sentences']: out.append(s['text'])
out.append("")
out.append("**心理学者** *(鋭い洞察で、モノ化、区画化、自己正当化の罠を暴く)*:")
for s in orig_map['3.06']['sentences']: out.append(s['text'])
for s in new_turns['3.06_add']: out.append(s)
out.append("")
out.append("**[SFX]:** *鏡のガラスが粉々に砕け散る鋭い音と、乾いた金属の衝突音。*")
out.append("")
out.append("**捜査官** *(冷徹に、心理的破綻と捜査の転換点を語る)*:")
for s in orig_map['3.08']['sentences']: out.append(s['text'])
out.append("")
out.append("**ホスト** *(緊張感を孕み、取調室と司法取引の転換点へと導く)*:")
for s in orig_map['3.09']['sentences']: out.append(s['text'])
out.append("")
out.append("**[BGM]:** *重いピアノの一音が静かに響き、静まり返った闇の中へと溶けて消えていく。*")
out.append("")
out.append("**心理学者** *(簡潔に締めくくり、裏切りの計算高い心理を暴く)*:")
for s in orig_map['3.11']['sentences']: out.append(s['text'])
out.append("")

# Act 4
out.append("## 第4幕：悪魔との取引と被害者の仮面の崩壊 (16:40 – 23:30)")
out.append("")
out.append("**[BGM]:** *激しく引き裂かれるようなヴァイオリンの旋律が、息詰まる世論の混乱と歴史的司法危機を物語る。*")
out.append("")
out.append("**ホスト** *(緊迫感を高め、検察が直面した息苦しい重圧を伝える)*:")
for s in orig_map['4.02']['sentences']: out.append(s['text'])
out.append("")
out.append("**[SFX]:** *書類の上を走るペンの摩擦音と、重々しく響く司法の捺印音。*")
out.append("")
out.append("**捜査官** *(力強い声で、捜査陣の過ちと論争を呼んだ協定を述懐する)*:")
for s in orig_map['4.04']['sentences']: out.append(s['text'])
out.append("")
out.append("**[Nghỉ 1.5 giây – khoảng lặng kịch tính]**")
out.append("")
out.append("**ホスト** *(厳粛な声で、心理変容の本質的な問いを投げかける)*:")
for s in new_turns['4.06']: out.append(s)
out.append("")
out.append("**心理学者** *(分析的な口調で、真の後悔と被害者面の偽装を対比させる)*:")
for s in new_turns['4.07']: out.append(s)
out.append("")
out.append("**捜査官** *(証拠保有者の倫理的葛藤に触れる)*:")
for s in new_turns['4.08']: out.append(s)
out.append("")
out.append("**ホスト** *(謎めいた抑揚で、6本のビデオテープの衝撃を語る)*:")
for s in orig_map['4.06']['sentences']: out.append(s['text'])
out.append("")
out.append("**捜査官** *(冷徹に、証拠の発見と暗い会議室の衝撃を再現する)*:")
for s in orig_map['4.07']['sentences']: out.append(s['text'])
out.append("")
out.append("**一般人** *(N2: 検察関係者／捜査官、憤怒と後悔に声を震わせる中年男性)*:")
for s in orig_map['4.08']['sentences']: out.append(s['text'])
out.append("")
out.append("**[SFX]:** *テープの早送り音が甲高く響き、会議机を叩きつける激しい音が鳴り響く。*")
out.append("")
out.append("**心理学者** *(学術的に被害者面の崩壊を分析する)*:")
for s in orig_map['4.10']['sentences']: out.append(s['text'])
out.append("")
out.append("**ホスト** *(毅然とした声で、世論の嵐と司法的ジレンマを語る)*:")
for s in orig_map['4.11']['sentences']: out.append(s['text'])
out.append("")
out.append("**[BGM]:** *張り詰めたヴァイオリンの音が鳴り響き、裁判所の冷たい鐘の音へと沈んでいく。*")
out.append("")

# Act 5
out.append("## 第5幕：判決と司法の遺産――4つの赤い警告 (23:30 – 30:00)")
out.append("")
out.append("**[BGM]:** *法廷に厳かに響き渡る裁判官の木槌の音に続き、深く心に染み入るピアノの調べが静かな覚醒を促す。*")
out.append("")
out.append("**ホスト** *(堂々たる威厳を保ち、司法の最終判決を告げる)*:")
for s in orig_map['5.02']['sentences']: out.append(s['text'])
out.append("")
out.append("**[Nghỉ 1.5 giây – khoảng lặng kịch tính]**")
out.append("")
out.append("**ホスト** *(感情を込め、犠牲者の家族を称える)*:")
for s in new_turns['5.04']: out.append(s)
out.append("")
out.append("**捜査官** *(冷徹に、Karlaの釈放後の実態と歴史的司法改革を振り返る)*:")
for s in orig_map['5.04']['sentences']: out.append(s['text'])
out.append("")
out.append("**[SFX]:** *調査報告書の分厚いページがめくられる音と、重い溜息の響き。*")
out.append("")
out.append("**心理学者** *(社会の良心の判決と仮面の崩壊を総括する)*:")
for s in new_turns['5.07_add']: out.append(s)
for s in orig_map['5.06']['sentences']: out.append(s['text'])
out.append("")
out.append("**ホスト** *(威厳を保ち、The Gift of Fearに基づく4つの生存警告を提示する)*:")
for s in orig_map['5.07']['sentences']: out.append(s['text'])
out.append("")
out.append("**[Nghỉ 1.5 giây – khoảng lặng kịch tính]**")
out.append("")
out.append("**ホスト** *(温かく感動的な声で、人間的メッセージとともに番組を締めくくる)*:")
for s in orig_map['5.09']['sentences']: out.append(s['text'])
out.append("")
out.append("**[SFX]:** *事件記録のファイルがカチリと硬く閉じられ、録音機の停止音が続く。*")
out.append("**[BGM]:** *哀愁を帯びたピアノの旋律が5秒間静かに響き渡り、やがてフェードアウトして消えていく。*")
out.append("")

full_ja = "\n".join(out)
with open('01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md', 'w', encoding='utf-8') as f:
    f.write(full_ja)
print("Wrote 01_KICH_BAN/Tap11_JA/kichban_tap11_JA.md successfully!")

# Test parse
p_ja = PK.parse_lines(full_ja.splitlines())
print(f"Generated JA: {len(p_ja)} elements, {sum(len(e.get('sentences', [])) for e in p_ja)} sentences")
