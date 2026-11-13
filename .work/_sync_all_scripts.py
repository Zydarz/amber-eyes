# -*- coding: utf-8 -*-
"""Standalone script to update and synchronize all 4 scripts for Tap 10 to 240 sentences."""
import sys, io, re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

EN_UPDATES = {
    '1.02': """In the nineteen seventies, America was living through the golden age of nomadic hitchhiking culture along the sunlit freeways of the West Coast.
Young hitchhikers standing by the shoulder with backpacks, thumbs out, became an iconic symbol of boundless freedom for an entire generation.
People offered their complete trust to complete strangers in a remarkably innocent and natural fashion.
They sincerely believed that behind every steering wheel sat a decent fellow traveler ready to share the open road.
Media outlets during that era constantly celebrated this freewheeling spirit, turning hitchhiking into a romanticized symbol of youthful adventure.
Yet, that very collective innocence inadvertently created a treacherous “Social Blindspot”.
In peaceful Western towns like Red Bluff, people lived with an ingrained assumption that danger belonged only to distant, crime-ridden metropolitan areas.
The tranquil expanse of endless pine forests and the rustic rhythm of community life wove a comforting veil of security that unwittingly dulled people's natural survival instincts.
Everyone believed they truly knew their neighbor across the fence, confident that behind every lit window lay an honest, wholesome family.
That very collective lapse in vigilance transformed the tranquil region into an ideal sanctuary where evil could hide in plain sight.
Those vast sun-drenched freeways turned into ideal hunting grounds for patient and ruthless predators.
One of the most extraordinary and harrowing kidnappings in American legal history began from just such a fateful ride.""",

    '2.04': """The wooden detention box was designed and assembled by Cameron Hooker himself using thick, heavy-duty structural plywood.
He hid this box directly beneath the massive waterbed in their master bedroom.
The immense weight of the waterbed above rendered pushing open the lid from inside completely impossible.
He enforced absolute physical dominance: Colleen was permitted out of the box only for brief intervals each day to perform domestic chores under rigid surveillance.
Yet in a tragic paradox, Colleen Stan was not the only captive inside that house.
Just above the wooden box, in that very bedroom, Janice Hooker was trapped in her own invisible psychological cage constructed by her husband.
Having been abused from her youth, the young wife severed her own moral compass, turning complicity into a cowardly shield to divert the brunt of violence onto another woman's body.
Each night on that waterbed, the faint rustling from beneath the floorboards drove an invisible knife into what little remained of her conscience.
Behavioral crime scene analysis demonstrates that this was a classic manifestation of “Modus Operandi” intertwined with “Psychological Signature”.
He transformed an ordinary domestic space into an impenetrable underground prison.""",

    '2.06': """From the standpoint of behavioral psychology, confining a human being to darkness and cramped isolation over years triggers “Extreme Sensory Deprivation”.
When the human brain is cut off from typical sensory inputs, the fundamental concepts of time and space completely disintegrate.
The captive rapidly loses orientation, unable to distinguish between day and night, reality and hallucination.
This state of sensory exhaustion shatters natural psychological defense mechanisms.
Confronted with an unimaginably brutal captivity, the human mind is forced to activate an ultimate survival defense known as “Dissociation”.
Colleen Stan learned to sever her conscious soul from the physical shell enduring agony in suffocating darkness.
Through an extraordinary power of visualization, she roamed the meadows of her childhood, recited remembered prayers, and built an impregnable spiritual fortress within herself.
Preserving that internal sphere of spiritual freedom prevented her core humanity from being obliterated by sadistic control.
Under such extreme sensory deprivation, the faintest auditory stimulus can trigger overwhelming waves of terror.
At the same time, this brutality reflects the most extreme manifestation of “Objectification and Dehumanization”.
The perpetrator suffered from severe deficits in “Theory of Mind” and a complete absence of affective empathy.
He never viewed Colleen as a sentient human being experiencing pain, but demoted her to an exclusive proprietary object serving his sadomasochistic cravings for dominance.""",

    '3.07': """The key to unlocking this paradox lies in the landmark psychological doctrine of “Learned Helplessness”, discovered by Professor Martin Seligman.
In his research, Seligman demonstrated that when an organism experiences prolonged suffering where early resistance proves entirely futile, the nervous system learns to surrender.
The brain establishes an absolute conviction that suffering is inevitable and that no conscious action can alter reality.
When an authentic avenue of escape finally swings open, the subject remains paralyzed and incapable of stepping across the threshold to freedom.
Once learned helplessness embeds itself into the subconscious, the victim reflexively rejects opportunities to rescue themselves.
From the standpoint of cognitive psychology, the family's silence during the nineteen eighty-one visit also stemmed from a phenomenon known as the “Relief Blindspot”.
After four grueling years of despair, Colleen's sudden reappearance unleashed such an overwhelming surge of positive emotion that her father unconsciously activated a “Normalcy Bias”, brushing aside her strained demeanor.
The cultural backdrop of the late nineteen seventies, with thousands of youths joining communal lifestyle groups and alternative religious movements, served as a perfect smokescreen that lulled the family's suspicions.
For Colleen, the family visit was perceived as a treacherous “Loyalty Test” engineered by “The Company”.
She was convinced that a single errant plea for help would prompt underground agents to execute her parents and siblings.
Silence and obediently returning to the wooden box was seen as the ultimate sacrifice to preserve her family's lives.""",

    '3.08': """Alongside learned helplessness, a second psychological mechanism binding Colleen throughout those years was extreme “Trauma Bonding”.
The concept, formulated by Doctor Patrick Carnes, illuminates the paradoxical attachment between captives and their abusers.
Cameron Hooker deployed a calculated cycle of manipulation: alternating between severe punishment and unexpected, intermittent drops of indulgence.
He occasionally allowed her outside for fresh air, gave her small gifts, or offered praise when she exhibited submissiveness.
And perhaps, the most harrowing paradox of all: In the victim's exhausted psyche, the wooden box beneath the bed sometimes became a “Twisted Sanctuary”.
Because outside the box, she faced constant terror from unpredictable punishments and the scrutiny of an overwhelming world.
Only inside that confined darkness was she temporarily sheltered in an internal sanctuary, believing her endurance protected the lives of her loved ones.
In the absolute abyss of deprivation, those fleeting crumbs of kindness transformed the captor into the sole “Savior” upon whom survival depended.""",

    '4.03': """The person who fractured that seemingly impenetrable fortress was none other than Janice Hooker, Cameron's wife and accomplice.
Janice had known Cameron since she was fifteen and had herself been manipulated and coerced under his psychological dominance for years.
However, when Cameron began voicing ambitions to kidnap a second young woman to expand his twisted fantasy, Janice was seized by overwhelming panic.
Interrogation records later revealed that Cameron's demand to abduct a second young woman dealt a fatal blow to the “Cognitive Dissonance” Janice had maintained for seven years.
She realized his predatory escalation would never cease, and a second captive would permanently transform her home into an inescapable house of horrors.
Her two young daughters were growing up, and the terrifying prospect of them being corrupted or becoming his next victims pushed the young mother past her breaking point.
A mother's protective instinct toward her children became the ultimate catalyst awakening her dormant conscience.
The terror of escalating atrocities and seven years of accumulated guilt crushed her psychological defenses.
Janice sought out a local church pastor to unburden her conscience and seek spiritual guidance.""",

    '4.04': """The pastor urged Janice to confront the truth and immediately terminate her complicity before it was too late.
The pastor's counsel served as an “External Moral Anchor”, tearing away the grotesque normalization that Cameron had drilled into her mind for more than a decade.
The breaking point arrived in early August nineteen eighty-four, during Cameron's absence from the home.
Janice realized that continuing silence would bury not only Colleen, but the future of her own young daughters in an abyss of criminality.
She resolved to take a courageous step that irrevocably altered the course of the case.""",

    '4.05': """Imagine the agonizing torment of a woman realizing the domestic life she fought to preserve was built on the living burial of her conscience.
I was so terrified of Cameron that I became deaf and blind, comforting myself that as long as I obeyed, our children would be safe.
I was silent, I was complicit, and I became an active part of that horrific crime for seven long years.
But seeing that ravenous predatory hunger in his eyes, watching my two toddler daughters playing innocently on the rug, a cold truth seized me: This monster will never stop.
Each day seeing Colleen in that darkness, my conscience felt torn by thousands of sharp blades.
If I did not find the courage to end this nightmare, my soul would burn forever in the fires of unforgivable guilt.
In that defining moment, I realized I could not remain a coward for a single second longer.
I held Colleen's hand and spoke the truth: ‘Cameron does not belong to any Company, it was all his twisted lie to keep you enslaved.’""",

    '4.09': """During the historic nineteen eighty-five trial in Tehama County Superior Court, Cameron Hooker maintained his shameless narcissistic arrogance.
He stubbornly pleaded not guilty, brazenly asserting that Colleen had stayed willingly and that the slave contract was a mutual agreement.
Through the lens of forensic psychology, Janice Hooker's repentance reflects the deeply conflicted duality of human nature.
She experienced authentic moral awakening when freeing Colleen in August nineteen eighty-four, yet waited nearly three months to surrender once her attorney secured a full immunity agreement.
It was a complex intersection between genuine remorse and the pragmatic survival drive of a mother desperate to remain with her young children.
Confronting these self-serving fabrications, forensic psychologist Doctor Chris Hatcher delivered pivotal expert testimony before the jury.
Doctor Hatcher demonstrated that the victim's compliant behavior was a passive survival adaptation forged under chronic terror.
His expert testimony deconstructed the mechanisms of “Coercive Control and Thought Reform”, enabling the jury to understand why a captive's will to resist becomes paralyzed.
The deceitful veneer of voluntary consent was completely obliterated under the light of justice.""",

    '4.10': """Faced with incontrovertible physical evidence and compelling testimony from both women, Judge Clarence Knight pronounced the most severe sentence available under law.
Cameron Hooker was sentenced to one hundred and four years in state prison for multiple counts of kidnapping, sexual assault, and unlawful imprisonment.
As the judicial gavel came down, the predator experienced total “Narcissistic Collapse” and “Pathological Self-Pity”.
He shed no tears for the seven stolen years of his victim's youth, weeping only for his own lost freedom and shattered fantasies of omnipotence.
The predator who locked another human being in darkness was now permanently imprisoned within the cage of his own pathological narcissism.
The sentence of the century fell upon the perpetrator as a just and decisive retribution of the law.""",

    '5.03': """Colleen Stan's miraculous recovery stands as living proof of the doctrine of “Post-Traumatic Growth”, pioneered by psychologists Richard Tedeschi and Lawrence Calhoun.
This framework asserts that individuals who survive profound catastrophe can, through meaningful purpose and supportive connection, not only heal but forge extraordinary inner resilience.
Colleen preserved her humanity inside that wooden box through rich imagination, memories of family, and unshakeable spiritual faith.
By learning to make peace with her scars and forgiving her past powerlessness, Colleen transformed the wooden box from a symbol of bondage into an enduring monument to the resilience of human dignity.
That indomitable spirit turned a traumatized captive into a timeless symbol of psychological resilience.
She reflected that true healing does not mean erasing painful memories, but learning to live alongside one's scars and turning them into strength for tomorrow.
Her journey is chronicled in her memoir, *The Simple Gifts of Life*, serving as a beacon of hope for countless souls navigating deep despair.""",

    '5.04': """In legal and societal terms, the Colleen Stan case marked a watershed moment in the awareness of international law enforcement.
The case laid foundational groundwork for modern statutes addressing “Coercive Control” and non-physical psychological abuse.
It warned society that impenetrable prisons need not have iron bars, but can be forged from manipulation, fear, and manufactured isolation.
The case compels society to confront the devastating cost of apathy hiding behind the shield of domestic privacy.
Coercive control cannot thrive for seven years without the quiet complicity of averted eyes and community avoidance.
Cameron Hooker's subsequent parole petitions over the decades were repeatedly denied, affirming justice's unyielding stance against crimes of psychological subjugation."""
}

JA_UPDATES = {
    '1.02': """1970年代のアメリカは、西海岸の陽光あふれるハイウェイ沿いを旅する自由なヒッチハイク文化の黄金期を迎えていました。
バックパックを背負った若者たちが路肩に立ち、親指を立てて車を待つ姿は、一世代の限りなき自由を象徴する象徴的な光景でした。
人々は見知らぬ他者に対して、ごく自然に、そして無垢な信頼を寄せていたのです。
誰もが、ハンドルの向こう側に座るドライバーは旅路を分かち合ってくれる心優しい同乗者であると信じて疑いませんでした。
当時のメディアは自由奔放な精神を称賛し続け、ヒッチハイクを若者の冒険のロマンチックな象徴へと仕立て上げていました。
しかし、その社会全体の無邪気さこそが、極めて危険な「社会的盲点」を生み出すことになります。
レッドブラフのような穏やかな西部の町では、危険は遠く離れた犯罪都市だけのものだという思い込みが根深く共有されていました。
果てしなく広がる松林の静けさと素朴な共同体の暮らしは、人々の警戒心を無意識に鈍らせる安らぎのベールを織りなしていました。
誰もが垣根越しに隣人を理解していると信じ、明かりの灯る窓の向こうには誠実で温かな家庭があることを微塵も疑いませんでした。
まさにその集団的な油断こそが、この静謐な地を、悪意が白昼堂々と身を潜める完璧な隠れ蓑へと変えてしまったのです。
どこまでも続く陽光に照らされたハイウェイは、冷酷な捕食者たちにとって格好の狩り場と化していたのです。
アメリカ司法史上、最も奇怪で衝撃的な誘拐事件の一つは、まさにそのような一台の運命的な車から始まりました。""",

    '2.04': """被害者を監禁していた木箱は、キャメロン・フッカー自身が厚みのある頑丈な構造用合板を用いて設計し組み立てたものでした。
彼はこの木箱を、寝室の巨大なウォーターベッドの真下に隠していました。
上部にあるウォーターベッドの圧倒的な重量により、被害者が内側から蓋を押し開けることは絶対に不可能でした。
彼は絶対的な身体的支配を確立し、コリーンには厳格な監視下で家事を行うわずかな時間だけ木箱から出ることを許していたのです。
しかし悲劇的な逆説として、あの家の中で囚われの身となっていたのはコリーン・スタンだけではありませんでした。
木箱のすぐ上のベッドルームで、ジャニス・フッカーもまた、夫によって築かれた目に見えない心理的な檻に閉じ込められていたのです。
少女時代から支配と暴力を受けてきた若き妻は、良心の回路を遮断し、夫の暴力が別の女性へと向けられることを卑怯な防壁にしていました。
毎夜、ウォーターベッドに横たわる彼女の耳に届く床下からの微かな身じろぎは、残された良心を切り刻む不可視の刃でした。
犯行現場の行動分析は、これが「犯行の手口（MO）」と「心理的シグネチャー」が結合した典型的な表れであることを示しています。
彼は家庭という私的空間を、何者も侵入できない難攻不落の地下牢獄へと変貌させたのです。""",

    '2.06': """行動心理学の視点から見れば、人間を長期間にわたり暗闇と狭小な空間に閉じ込めることは、「極限の感覚遮断」を引き起こします。
脳が通常の感覚刺激から完全に孤立すると、時間と空間の概念は完全に崩壊します。
被害者は急速に見当識を失い、昼と夜、現実と幻覚の区別がつかなくなっていきます。
この感覚の極度の枯渇は、人間が本来備えている心理的防衛機制を完全に破壊します。
想像を絶する過酷な監禁に直面したとき、人間の脳は「心理的分離」、すなわち「解離（Dissociation）」という究極の防衛機制を発動させます。
コリーン・スタンは、息苦しい暗闇の中で苦痛に耐える肉体から、自身の意識ある魂を切り離す術を身につけました。
卓越したイメージの力によって、彼女は幼少期の草原を駆け巡り、記憶の中の祈りを唱え、内なる難攻不落の精神的要塞を築き上げたのです。
内なる精神的自由を守り抜くことこそが、残酷な支配によって彼女の人間性が完全に破壊されるのを食い止めました。
そのような極限の孤立状態では、極めて微小な刺激であっても、制御不能な激しいパニックへと増幅されてしまいます。
同時にそれは、被害者を最も残虐なレベルで「客体化し非人間化」したメカニズムを反映しています。
犯人は「心の理論」に深刻な欠陥を抱えており、他者への感情的共感能力が完全に欠如していました。
彼はコリーンを感じる心と痛みを持った人間として認識せず、自らの支配欲を満たすための独占的な道具へと貶めていたのです。""",

    '3.07': """この逆説を解き明かす鍵こそ、マーティン・セリグマン教授が発見した古典的心理学理論「学習性無力感（Learned Helplessness）」です。
セリグマンはその研究において、初期の抵抗が無力であるような持続的な苦痛を受け続けると、神経系は自動的に諦めることを学習すると指摘しました。
脳は、運命は不可避であり、自らのいかなる行動も現実を変えることはできないという絶対的な信念を構築します。
やがて真の逃回路が目の前に開かれたとしても、その生命体の意志は麻痺したままであり、自由への境界を自ら踏み出す力を失ってしまうのです。
無力感の観念が潜在意識に深く根付くと、被害者は自らを救うあらゆる好機を無意識に拒絶してしまいます。
認知心理学の観点から言えば、1981年の訪問時に家族が見せた沈黙もまた、「安堵による盲点（Relief Blindspot）」と呼ばれる現象によるものでした。
4年間の絶望の果てに娘が生きて帰ってきたという激しい歓喜は、父親の正常性バイアスを無意識に作動させ、コリーンのぎこちない態度を見過ごさせました。
さらに1970年代後半の文化背景として、多くの若者が共同生活や新興宗教運動に参加していた事実が、家族の疑念を完璧に覆い隠す煙幕となったのです。
コリーンにとって、実家への帰省は組織「ザ・カンパニー」が仕掛けた狡猾な「忠誠心テスト」として認識されていました。
不用意な救助要請を一度でも口にすれば、潜入工作員によって家族全員が危害を加えられると固く信じ込んでいたのです。
沈黙を守り、再び木箱へと戻ることこそが、愛する家族の命を守るための至高の犠牲的行動でした。""",

    '3.08': """学習性無力感とともに、あの歳月を通じてコリーンを縛り続けた第二の心理的メカニズムは、極限の「トラウマ・ボンディング（外傷的絆）」でした。
パトリック・カーンズ博士が提唱したこの概念は、被害者と支配者との間に生じる逆説的な心理的愛着を解明するものです。
キャメロン・フッカーは、過酷な懲罰と予期せぬ散発的な恩恵を巧みに交錯させる操作サイクルを弄していました。
時折外の空気を吸わせ、ささやかな贈り物を与え、あるいは従順さに対して甘い言葉をかけるといった行為です。
そして最も痛ましい逆説として、極限まで消耗した被害者の心理において、ベッド下の木箱は時に「歪んだ避難所」へと変貌していました。
なぜなら箱の外に出れば、予測不能な懲罰の恐怖や、圧倒的な外部世界の視線に直面しなければならなかったからです。
あの閉ざされた暗闇の中に身を潜めている間だけ、彼女は内なる聖域へと引きこもり、耐え忍ぶことで愛する家族の命を守っていると信じることができたのです。
極限の剥奪の深淵において、それらのわずかな情けは、監禁者を生存のために縋りつく唯一の「救済者」へと仕立て上げました。""",

    '4.03': """その強固な防壁を揺るがしたのは、他ならぬキャメロンの妻であり共犯者でもあったジャニス・フッカーでした。
ジャニスは15歳の時にキャメロンと知り合い、彼女自身も長年にわたり彼の心理的支配と操作の被害者でした。
しかし、キャメロンが歪んだ妄想世界を拡大しようと、二人目の若い女性を誘拐する野心を露わにし始めた時、ジャニスは極度のパニックに陥りました。
後の尋問記録によれば、キャメロンが二人目の若い女性を誘拐しようと画策したことが、ジャニスが7年間保ち続けてきた「認知的不協和」に致命的な亀裂を入れました。
彼女は夫の異常な支配欲が決して終わらないことを悟り、二人目の犠牲者が現れれば家庭が完全な地獄へと堕ちることを理解したのです。
すくすくと育つ幼い二人の娘が、やがて父親の歪んだ欲望の犠牲になるかもしれないという恐怖が、母親としての限界点を超えさせました。
我が子を守りたいという母親の本能こそが、彼女に良心の目覚めを促す最も強烈な原動力となったのです。
犯罪のエスカレーションへの恐怖と、7年間にわたり積み重なった罪の重荷が、彼女の心理的防衛機制を打ち砕きました。
ジャニスは良心の呵責を打ち明け救いを求めるため、地元の教会の牧師を訪ねました。""",

    '4.04': """牧師はジャニスに対し、真実と向き合い、手遅れになる前に共犯関係を直ちに断ち切るよう強く促しました。
牧師の助言は「外的な道徳の錨」として機能し、10年以上にわたってキャメロンが彼女の心に植え付けたグロテスクな正常化の呪縛を打ち砕きました。
決定的な瞬間は、キャメロンが家を留守にしていた1984年8月初旬に訪れました。
沈黙を守り続ければ、コリーンだけでなく、愛する幼い娘たちの未来までもが犯罪の深淵に呑み込まれてしまうことを彼女は悟ったのです。
彼女は事態を根本から覆す勇敢な行動に出ることを決意しました。""",

    '4.05': """自分が必死に守ろうとしていた家庭が、実は良心の生埋めの上に築かれていたと気づいた女性の、張り裂けんばかりの苦悶を想像してください。
私はキャメロンを恐れるあまり自ら目と耳を塞ぎ、従順でさえいれば子供たちは安全なのだと言い聞かせてきました。
私は沈黙し、手を貸し、7年もの長きにわたりあの恐ろしい犯罪の共犯者となり果てていたのです。
しかし、新たな獲物を求める彼の飢えた目つきと、絨毯の上で無邪気に遊ぶ幼い二人の娘を見たとき、あの怪物が止まることは決してないという冷徹な真実が私を貫きました。
暗闇の中にいるコリーンの姿を目にするたび、私の良心は何千本もの刃で切り裂かれる思いでした。
もし今この悪夢を断ち切る勇気を持たなければ、私の魂は取り返しのつかない罪の炎の中で永遠に焼かれ続けるでしょう。
その決定的な瞬間に、私はもう一秒たりとも卑怯者であり続けることはできないと悟ったのです。
私はコリーンの手を握りしめ、「キャメロンはザ・カンパニーなどという組織に所属してはおらず、あなたを奴隷として縛り付けるための卑劣な嘘にすぎない」と真実を告げました。""",

    '4.09': """1985年にカリフォルニア州テハマ郡上級裁判所で行われた歴史的公判において、キャメロン・フッカーはなおも破廉恥な自己愛の本性を剥き出しにしました。
彼は頑なに無罪を主張し、コリーンは自らの意志で家に留まっていたのであり、奴隷契約は双方の合意によるものだと厚顔無恥に言い張ったのです。
司法心理学の視点から見れば、ジャニス・フッカーの悔悛は、人間の本性が抱える深い葛藤と二面性を如実に映し出しています。
彼女は1984年8月にコリーンを脱出させた際に真の道徳的目覚めを経験しましたが、弁護士を通じて完全な免責合意を取り付けるまで、自首を3ヶ月近く遅らせました。
それは贖罪への純粋な倫理的衝動と、幼い子供たちのそばに残りたいという母親としての現実的な生存本能との、複雑な交差点だったのです。
これら欺瞞に満ちた詭弁に対し、司法心理学者のクリス・ハッチャー博士が陪審員の前で決定的な専門証言を行いました。
ハッチャー博士は、被害者の従順な状態は、極度の恐怖の中で培われた受動的な適応生存戦略に他ならないと指摘しました。
彼の専門証言は「強制的コントロールと洗脳」の力学を解剖し、被害者の抵抗意志がいかにして麻痺させられたかを陪審員に理解させました。
自発的な同意という偽りの仮面は、司法の光の前に完全に剥ぎ取られたのです。""",

    '4.10': """揺るぎない物的証拠と二人の女性による明晰な証言の前に、クラレンス・ナイト判事は法の下で最も厳格な刑を言い渡しました。
キャメロン・フッカーには、度重なる誘拐と人権蹂躙の罪により、合計104年の懲役刑が科されました。
法廷に裁判長の木槌が響き渡った瞬間、冷酷な捕食者は「自己愛の完全な崩壊」と「病的な自己憐憫」へと転落しました。
彼は被害者から奪い去った青春の7年間に対して涙を流すことは一切なく、ただ自らの失われた自由と全能感への未練に打ちひしがれるばかりでした。
他者を暗闇の中に閉じ込めた捕食者は、今や自らの病的な自己愛という名の檻の中に、永遠に幽閉されることとなったのです。
世紀の判決は、法の断固たる正義として、冷酷な加害者の頭上に下されたのです。""",

    '5.03': """コリーン・スタンの奇跡的な回復は、心理学者リチャード・テデスキとローレンス・カルホーンが提唱した「外傷後成長（Post-Traumatic Growth）」の最も鮮やかな生証言です。
この理論は、人間が過酷な惨劇を経験したとしても、生きる意味の拠り所と愛を見出すならば、単に回復するにとどまらず、精神の深層において並外れた内なる強さを培うことができると主張します。
コリーンは豊かな想像力、家族への想い、そして揺るぎない信仰によって、木箱の中でも自らの人間性を守り抜きました。
心の傷跡と和解し、過去の無力だった自分を許すことを学んだコリーンは、木箱を屈辱の象徴から人間の尊厳の不滅性を称える記念碑へと昇華させました。
その不屈の精神力は、傷ついた囚われの被害者を、人間の精神的回復力の不滅の象徴へと変貌させたのです。
彼女はかつて、真の回復とは苦痛に満ちた過去を消し去ることではなく、傷跡とともに生きる術を学び、それらを明日へ進む力へと変えることだと語りました。
彼女の歩みは自叙伝『人生のささやかな贈り物』に記され、深い絶望の淵にある数え切れない魂にとって希望の灯台となっています。""",

    '5.04': """司法と社会の観点から、コリーン・スタン事件の記録は、国際的な法執行機関の認識に歴史的な転換点をもたらしました。
この事件は、「強制的コントロール」や「非身体的心理的暴力」に関する現代の法制化に極めて重要な礎を築きました。
それは、堅牢な牢獄とは必ずしも鉄格子を必要とするものではなく、巧妙な心理操作、恐怖、そして情報遮断によって築かれうるのだという警鐘を鳴らしています。
この事件は、家庭のプライバシーという盾の背後に隠された無関心の恐るべき代償を、現代社会に鋭く突きつけています。
強制的コントロールという支配の罠は、周囲の視線の逸らしや地域の不干渉という静かな加担なしには、7年もの歳月を生き延びることはできなかったのです。
その後の数十年にわたるキャメロン・フッカーの仮釈放申請はいずれも断固として却下され、人間を支配する罪に対する司法の妥協なき厳罰姿勢が証明され続けています。"""
}

KO_UPDATES = {
    '1.02': """1970년대 미국은 서부 해안의 햇살 가득한 고속도로를 따라 자유롭게 여행하던 히치하이킹 문화의 황금기를 누리고 있었습니다.
배낭을 멘 젊은이들이 길가에 서서 엄지손가락을 들어 올리는 모습은 한 세대의 끝없는 자유를 상징하는 대표적인 풍경이었습니다.
사람들은 낯선 타인에게 지극히 자연스럽고 순수한 신뢰를 보냈습니다.
누구나 운전대 너머에 앉아 있는 운전자가 여정을 함께 나누어 줄 선량한 길동무일 것이라 믿어 의심치 않았습니다.
당시의 대중매체는 이러한 자유분방한 히피 정신을 끊임없이 찬양하며, 히치하이킹을 젊은 날의 낭만적인 모험의 상징으로 포장했습니다.
하지만 그러한 사회적 순진함이야말로 치명적인 “사회적 맹점”을 만들어 냈습니다.
Red Bluff와 같은 평화로운 서부의 소도시에서는 위험이란 오직 멀리 떨어진 대도시의 범죄일 뿐이라는 믿음이 깊게 자리 잡고 있었습니다.
끝없이 펼쳐진 소나무 숲의 고요함과 소박한 공동체의 삶은 사람들의 자연스러운 생존 경계심을 무의식중에 마비시키는 안락한 장막을 형성했습니다.
누구나 울타리 너머의 이웃을 잘 알고 있다고 믿었으며, 불 켜진 창문 뒤에는 늘 정직하고 온화한 가정이 존재한다고 굳게 믿었습니다.
바로 그러한 집단적 방심이야말로 이 평온한 지역을 악이 대낮에 숨어들 수 있는 완벽한 은신처로 만들어 버렸습니다.
끝없이 펼쳐진 눈부신 고속도로는 냉혹한 포식자들에게 더없이 완벽한 사냥터로 변모하고 있었던 것입니다.
미국 사법 역사상 가장 기괴하고 충격적인 납치 사건 중 하나는 바로 그러한 운명적인 차량 한 대에서 시작되었습니다.""",

    '2.04': """피해자를 감금한 나무 상자는 Cameron Hooker가 두껍고 견고한 합판을 이용해 직접 설계하고 제작한 것이었습니다.
그는 이 상자를 부부 침실의 거대한 물침대 바로 밑에 숨겨 두었습니다.
물침대의 엄청난 무게 때문에 피해자가 안쪽에서 뚜껑을 밀어 올리는 것은 절대로 불가능했습니다.
그는 절대적인 육체적 지배를 확립하여, Colleen Stan에게는 엄격한 감시 아래 집안일을 하는 짧은 시간 동안만 상자 밖으로 나오는 것을 허용했습니다.
하지만 비극적인 역설로서, 그 집에서 갇혀 지낸 사람은 Colleen Stan 한 사람만이 아니었습니다.
나무 상자 바로 위 침실에서 Janice Hooker 역시 남편이 구축해 놓은 보이지 않는 심리적 감옥에 갇혀 있었습니다.
어린 시절부터 학대와 통제를 받아 온 젊은 아내는 양심의 회로를 차단하고, 범죄에 가담하는 비겁한 방패를 통해 남편의 폭력을 다른 여성에게 전가했습니다.
매일 밤 물침대에 누워 바닥 밑에서 들려오는 미세한 뒤척임 소리를 들을 때마다, 그녀의 가슴에는 남은 양심을 후벼 파는 보이지 않는 칼날이 꽂혔습니다.
현장 행동 분석에 따르면 이는 “범행 수법(MO)”과 “심리적 시그니처”가 결합된 전형적인 형태였습니다.
그는 가정이라는 사적인 공간을 그 누구도 뚫을 수 없는 지하 감옥으로 탈바꿈시켰습니다.""",

    '2.06': """행동심리학적 관점에서 볼 때, 인간을 오랜 세월 동안 암흑과 비좁은 공간에 가두는 것은 “극단적인 감각 박탈”을 초래합니다.
뇌가 일반적인 감각 자극으로부터 완전히 고립되면 시간과 공간의 개념이 완전히 붕괴합니다.
피해자는 빠르게 지남력을 상실하고 낮과 밤, 현실과 환각을 분간하지 못하게 됩니다.
이러한 극도의 감각 고갈은 인간의 자연스러운 심리적 방어기제를 산산조각 냅니다.
상상조차 할 수 없는 가혹한 감금에 직면했을 때, 인간의 뇌는 “심리적 분리”, 즉 “해리(Dissociation)”라는 궁극적인 생존 방어기제를 작동시킵니다.
Colleen Stan은 숨 막히는 어둠 속에서 고통받는 육체로부터 자신의 의식 있는 영혼을 분리하는 법을 배웠습니다.
비범한 시각화 능력을 통해 그녀는 어린 시절의 초원을 거닐고, 기억 속의 기도를 암송하며 자신만의 난공불락의 영적 요새를 구축했습니다.
내면의 정신적 자유를 지켜낸 것만이 가학적인 통제 속에서 그녀의 인간성이 송두리째 파괴되는 것을 막아 주었습니다.
그러한 극단적인 고립 상태에서는 아주 작은 자극조차도 통제할 수 없는 극심한 공황으로 증폭될 수 있습니다.
동시에 이는 피해자를 가장 잔혹한 수준에서 “사물화하고 비인간화”한 메커니즘을 반영합니다.
가해자는 “마음 이론”에 심각한 결함이 있었으며 공감 능력이 완전히 결여되어 있었습니다.
그는 Colleen Stan을 고통을 느끼는 인간으로 보지 않고, 자신의 권력욕을 충족하기 위한 독점적인 장난감으로 전락시켰던 것입니다.""",

    '3.07': """이 역설을 푸는 열쇠는 Martin Seligman 교수가 발견한 기념비적인 심리학 이론인 “학습된 무기력(Learned Helplessness)”입니다.
Seligman은 연구를 통해 초기 저항이 무력화되는 지속적인 고통을 겪으면 신경계가 포기하는 법을 학습한다고 밝혔습니다.
뇌는 고통이 불가피하며 자신의 어떤 행동도 현실을 바꿀 수 없다는 절대적인 확신을 구축합니다.
마침내 진정한 탈출구가 열렸을 때에도 대상은 여전히 의지가 마비되어 자유의 문턱을 스스로 넘지 못합니다.
무기력의 관념이 잠재의식에 깊이 뿌리내리면 피해자는 스스로를 구원할 기회를 무의식적으로 거부하게 됩니다.
인지심리학적 관점에서 볼 때, 1981년 방문 당시 가족들이 보여 준 침묵 역시 “안도에 의한 맹점(Relief Blindspot)”이라 불리는 현상에서 비롯되었습니다.
4년 동안 절망에 빠져 있던 딸이 살아 돌아왔다는 감격은 아버지의 “정상성 편향”을 무의식중에 촉발하여 딸의 어색한 몸짓을 그냥 넘기게 만들었습니다.
1970년대 후반 수많은 젊은이가 공동체 생활이나 신흥 종교 운동에 참여하던 문화적 배경은 가족들의 의심을 완벽하게 잠재우는 연막이 되었습니다.
Colleen Stan에게 친정 방문은 The Company가 파놓은 교활한 “충성심 시험”으로 인식되었습니다.
그녀는 단 한 번이라도 구조를 요청하면 비밀 요원들이 가족들을 몰살할 것이라 굳게 믿었습니다.
침묵을 지키고 다시 나무 상자로 돌아가는 것이야말로 사랑하는 가족의 목숨을 지키기 위한 최고의 희생이었습니다.""",

    '3.08': """학습된 무기력과 함께 그 세월 동안 Colleen Stan을 옭아맨 두 번째 심리 메커니즘은 극단적인 “외상적 유대(Trauma Bonding)”였습니다.
Patrick Carnes 박사가 정립한 이 개념은 피해자와 가해자 사이에 형성되는 역설적인 애착을 설명합니다.
Cameron Hooker는 가혹한 징벌과 예상치 못한 간헐적 호의를 번갈아 제공하는 교활한 조종 주기를 활용했습니다.
때때로 바깥공기를 쐬어 주거나 작은 선물을 건네고, 순종할 때 칭찬을 아끼지 않는 방식이었습니다.
그리고 가장 가슴 아픈 역설로서, 지칠 대로 지친 피해자의 심리 속에서 침대 밑 나무 상자는 때때로 “기괴한 피난처”가 되기도 했습니다.
왜냐하면 상자 밖으로 나가면 예측할 수 없는 징벌의 공포와 감당하기 힘든 세상의 시선에 직면해야 했기 때문입니다.
그 갇힌 어둠 속에 웅크리고 있을 때에만 그녀는 내면의 성소로 숨어들어, 자신이 인내함으로써 사랑하는 가족의 목숨을 지키고 있다고 믿을 수 있었습니다.
극단적인 결핍의 심연 속에서 그러한 작은 호의는 가해자를 생존을 위해 매달려야 하는 유일한 “구원자”로 착각하게 만들었습니다.""",

    '4.03': """그 견고한 벽을 무너뜨린 사람은 다름 아닌 Cameron Hooker의 아내이자 공범이었던 Janice Hooker였습니다.
Janice Hooker는 열다섯 살 때 Cameron Hooker를 만났으며, 그녀 자신 또한 수년간 그의 심리적 지배와 학대의 피해자였습니다.
하지만 Cameron Hooker가 두 번째 젊은 여성을 납치해 노예 하렘을 확장하겠다는 야망을 드러내기 시작하자 Janice Hooker는 극심한 공황 상태에 빠졌습니다.
이후의 신문 기록에 따르면, Cameron Hooker가 두 번째 젊은 여성을 납치하겠다고 선언한 것이 Janice Hooker가 7년 동안 유지해 온 “인지 부조화”에 치명타를 가했습니다.
그녀는 남편의 병적인 포식 욕구가 결코 멈추지 않을 것이며, 두 번째 희생자가 생기면 집이 영원한 지옥으로 변할 것임을 깨달았습니다.
무럭무럭 자라는 어린 두 딸이 결국 아버지의 희생양이 될지도 모른다는 공포는 어머니로서의 한계점을 완전히 무너뜨렸습니다.
아이들을 지키려는 모성 본능이야말로 양심을 일깨운 가장 강력한 원동력이었습니다.
범죄의 확대에 대한 공포와 7년 동안 짓눌려 온 죄책감의 무게는 그녀의 방어기제를 산산조각 냈습니다.
Janice Hooker는 양심의 가책을 털어놓고 구원을 얻기 위해 지역 교회의 목사를 찾아갔습니다.""",

    '4.04': """목사는 Janice Hooker에게 진실을 마주하고 너무 늦기 전에 공범 행위를 즉시 중단하라고 강력히 권고했습니다.
목사의 조언은 “외적 도덕의 닻” 역할을 하여, Cameron Hooker가 십여 년 동안 그녀의 머릿속에 주입해 온 기괴한 정상화의 최면을 산산조각 냈습니다.
결정적인 순간은 Cameron Hooker가 집을 비운 1984년 8월 초에 찾아왔습니다.
침묵을 지킨다면 Colleen Stan뿐만 아니라 자신의 어린 딸들의 미래까지도 범죄의 심연에 묻히게 될 것임을 깨달았습니다.
그녀는 상황을 완전히 뒤바꿀 용기 있는 결단을 내렸습니다.""",

    '4.05': """자신이 필사적으로 지키려 했던 가정이 사실은 양심을 생매장한 토대 위에 세워졌음을 깨달은 한 여성의 찢어지는 고통을 상상해 보십시오.
저는 Cameron Hooker가 너무나 두려워 스스로 눈과 귀를 닫았고, 복종하기만 하면 아이들은 안전할 것이라고 스스로를 위로했습니다.
저는 침묵했고, 방조했으며, 7년이라는 긴 세월 동안 그 끔찍한 범죄의 공범자가 되어 있었습니다.
하지만 새로운 사냥감을 갈망하는 그의 번뜩이는 눈빛과 양탄자 위에서 천진하게 놀고 있는 어린 두 딸을 보았을 때, 이 괴물은 결코 멈추지 않을 것이라는 차디찬 진실이 저를 덮쳤습니다.
어둠 속에 갇힌 Colleen Stan을 볼 때마다 제 양심은 수천 개의 칼날에 베이는 듯했습니다.
만약 지금 이 악몽을 끝낼 용기를 내지 않는다면, 제 영혼은 영원히 죄악의 불길 속에서 타오를 것이었습니다.
그 결정적인 순간에 저는 더 이상 비겁하게 숨어 있을 수 없다는 것을 깨달았습니다.
저는 Colleen Stan의 손을 잡고 “Cameron Hooker는 The Company라는 조직에 속해 있지 않으며, 당신을 노예로 묶어 두기 위한 그의 추악한 거짓말일 뿐입니다”라고 진실을 말했습니다.""",

    '4.09': """1985년 California주 Tehama County 상급법원에서 열린 역사적인 공판에서 Cameron Hooker는 여전히 뻔뻔한 자기애적 오만을 드러냈습니다.
그는 끝까지 무죄를 주장하며, Colleen Stan이 자발적으로 머물렀고 계약서는 양측의 합의였다고 뻔뻔스럽게 주장했습니다.
사법심리학의 관점에서 볼 때 Janice Hooker의 참회는 인간 본성이 지닌 깊은 갈등과 이중성을 극명하게 보여 줍니다.
그녀는 1984년 8월 Colleen Stan을 탈출시킬 때 진정한 도덕적 각성을 경험했지만, 변호사를 통해 완전한 면책 합의를 받아낼 때까지 3개월 가까이 자수를 미뤘습니다.
그것은 속죄를 향한 순수한 윤리적 충동과 어린 자식들 곁에 남고자 하는 어머니로서의 현실적인 생존 본능 사이의 복잡한 교차점이었습니다.
이러한 기만적인 궤변에 맞서 법심리학자 Chris Hatcher 박사가 배심원단 앞에서 결정적인 전문 증언을 내놓았습니다.
Hatcher 박사는 피해자의 순종적인 태도가 만성적인 공포 속에서 형성된 수동적인 생존 전략에 불과하다고 지적했습니다.
그의 전문 증언은 “강압적 통제와 세뇌”의 메커니즘을 해부하여, 배심원단이 피해자의 저항 의지가 마비된 이유를 명확히 이해하도록 도왔습니다.
자발적 동의라는 거짓 가면은 정의의 빛 앞에서 완전히 벗겨졌습니다.""",

    '4.10': """반박할 수 없는 물적 증거와 두 여성의 명확한 증언 앞에서 Clarence Knight 판사는 법이 허용하는 가장 엄격한 형벌을 선고했습니다.
Cameron Hooker는 납치와 인권 유린 등 여러 혐의로 총 104년의 징역형을 선고받았습니다.
법정에 판사의 의사봉 소리가 울려 퍼지는 순간, 포식자는 “자기애의 완전한 붕괴”와 “병적인 자기연민”에 빠져들었습니다.
그는 피해자가 빼앗긴 7년의 청춘에 대해서는 단 한 방울의 눈물도 흘리지 않고, 오직 자신의 자유와 전능감의 상실만을 한탄했습니다.
타인을 어둠 속에 가두었던 포식자는 이제 자신의 병적인 자기애라는 감옥 속에 영원히 갇히게 되었습니다.
세기의 판결은 사법의 준엄한 정의로서 가해자의 머리 위에 단호하게 내려졌습니다.""",

    '5.03': """Colleen Stan의 기적적인 회복은 심리학자 Richard Tedeschi와 Lawrence Calhoun이 정립한 “외상 후 성장(Post-Traumatic Growth)”의 가장 살아 있는 증거입니다.
이 이론은 인간이 극심한 비극을 겪더라도 삶의 의미와 사랑을 찾는다면 단순히 회복하는 것을 넘어 영혼 깊은 곳에서 비범한 내면의 힘을 길러낼 수 있다고 강조합니다.
Colleen Stan은 풍부한 상상력, 가족에 대한 기억, 흔들리지 않는 신앙을 통해 나무 상자 안에서도 인간성을 온전히 지켜냈습니다.
상처와 화해하고 과거의 무력했던 자신을 용서하는 법을 배움으로써, Colleen Stan은 나무 상자를 굴종의 상징에서 인간 존엄성의 불멸성을 증명하는 기념비로 탈바꿈시켰습니다.
그 불굴의 회복력은 상처 입은 피해자를 인간 정신의 회복력을 상징하는 영원한 표상으로 바꾸어 놓았습니다.
그녀는 진정한 치유란 고통스러운 과거를 지우는 것이 아니라, 상처와 평화롭게 살아가는 법을 배우고 그것을 내일로 나아가는 힘으로 바꾸는 것이라고 회고했습니다.
그녀의 여정은 자서전 『인생의 소박한 선물』에 오롯이 담겨, 깊은 절망 속에 있는 수많은 영혼에게 희망의 등대가 되고 있습니다.""",

    '5.04': """사법과 사회적 측면에서 Colleen Stan 사건은 전 세계 사법기관의 인식에 역사적인 전환점을 마련했습니다.
이 사건은 “강압적 통제”와 “비물리적 심리적 학대”에 관한 현대 법률의 제정에 결정적인 토대를 놓았습니다.
견고한 감옥이란 반드시 쇠창살로만 만들어지는 것이 아니며, 교활한 심리 조종과 공포, 정보의 고립으로 구축될 수 있음을 사회에 경고했습니다.
이 사건은 가정의 사생활이라는 방패 뒤에 숨은 무관심이 치러야 할 참혹한 대가를 현대 사회에 준엄하게 묻고 있습니다.
강압적 통제라는 범죄는 주변의 외면과 지역사회의 회피라는 조용한 동조 없이는 7년이라는 긴 세월을 버텨낼 수 없었을 것입니다.
이후 수십 년 동안 이어진 Cameron Hooker의 가석방 신청은 모두 단호하게 기각되어, 인간을 통제하고 억압한 범죄에 대한 사법 정의의 단호한 원칙을 증명하고 있습니다."""
}

def update_file(path, updates, role_pattern, act_pattern):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out = []
    act = 0
    el_idx = 0
    
    i = 0
    while i < len(lines):
        line = lines[i]
        s = line.strip()
        
        # Check Act header
        m_act = re.match(act_pattern, s)
        if m_act:
            act = int(m_act.group(1))
            el_idx = 0
            out.append(line)
            i += 1
            continue
            
        # Check BGM / SFX / NGHI
        if re.match(r'^\*\*\[(SFX|BGM)\]:\*\*', s) or re.match(r'^\*\*\[(?:Nghỉ|Pause|정지|休止)', s):
            el_idx += 1
            out.append(line)
            i += 1
            continue
            
        # Check Role header
        m_role = re.match(role_pattern, s)
        if m_role and act > 0:
            el_idx += 1
            cur_id = f"{act}.{el_idx:02d}"
            out.append(line) # output the header
            if cur_id in updates:
                out.append(updates[cur_id].strip() + '\n\n')
                # Skip original lines until next element header, act header, or delimiter
                i += 1
                while i < len(lines):
                    nxt = lines[i].strip()
                    if (re.match(role_pattern, nxt) or 
                        re.match(r'^\*\*\[(SFX|BGM)\]:\*\*', nxt) or 
                        re.match(r'^\*\*\[(?:Nghỉ|Pause|정지|休止)', nxt) or 
                        re.match(act_pattern, nxt) or 
                        nxt.startswith('---')):
                        break
                    i += 1
                continue
            else:
                i += 1
                continue
                
        out.append(line)
        i += 1
        
    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(out)
    print(f"Updated: {path}")

# Run update on EN
update_file(
    '01_KICH_BAN/Tap10_EN/kichban_tap10_EN.md',
    EN_UPDATES,
    r'^\*\*(?:HOST|INVESTIGATOR|PSYCHOLOGIST|ORDINARY PERSON)\*\*',
    r'^## ACT\s*(\d)'
)

# Run update on JA
update_file(
    '01_KICH_BAN/Tap10_JA/kichban_tap10_JA.md',
    JA_UPDATES,
    r'^\*\*(?:ホスト|捜査官|心理学者|一般人)\*\*',
    r'^## 第(\d)幕'
)

# Run update on KO
update_file(
    '01_KICH_BAN/Tap10_KO/kichban_tap10_KO.md',
    KO_UPDATES,
    r'^\*\*(?:호스트|수사관|심리학자|일반인)\*\*',
    r'^## 막\s*(\d)'
)
