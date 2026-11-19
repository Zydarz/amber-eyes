# -*- coding: utf-8 -*-
"""
Additions data for Tap 29: Exactly 75 sentences across Act 1, 2, 3, 4, 5.
Brings total sentences from 165 to exactly 240.
Maintains exact 1:1 parity between VN, EN, and JA.
"""

# Format:
# additions = {
#    turn_id: [
#       {
#          'pos': insertion_index,
#          'vn': "Vietnamese sentence text.",
#          'en': "English sentence text.",
#          'ja': "Japanese sentence text."
#       }, ...
#    ]
# }

ADDITIONS = {
    # ==========================================
    # ACT 1: +17 sentences (39 -> 56)
    # ==========================================
    '1.02': [
        {
            'pos': 2,
            'vn': 'Khuôn mặt người đàn ông đẫm mồ hôi, co giật từng hồi vì sang chấn tâm lý cấp tính sau nhiều giờ bị giam cầm trong căn phòng tử thần.',
            'en': 'The man\'s face was drenched in sweat, twitching repeatedly from acute psychological trauma after hours of confinement in that room of death.',
            'ja': '男の顔は汗に濡れ、死の部屋に何時間も監禁された後の急性心理的トラウマにより、何度も痙攣していた。'
        },
        {
            'pos': 4,
            'vn': 'Vật chứng kim loại lạnh lẽo đó như một dấu ấn tàn bạo của sự khống chế và tước đoạt tự do.',
            'en': 'That cold metal evidence stood as a brutal hallmark of subjugation and the violent deprivation of freedom.',
            'ja': 'その冷たい金属の物証は、拘束と自由の剥奪を示す残酷な痕跡そのものだった。'
        },
        {
            'pos': 7, # at end
            'vn': 'Lời cầu cứu thất thanh xé toang sự im ắng của bóng đêm, báo hiệu một vết nứt kinh hoàng sắp hé lộ trong lòng thành phố.',
            'en': 'His frantic plea shattered the stillness of the night, signaling a horrifying fissure about to tear through the city.',
            'ja': 'その悲痛な叫び声は夜の静寂を引き裂き、都市の深部で恐ろしい亀裂が開きつつあることを告げていた。'
        }
    ],
    '1.04': [
        {
            'pos': 3,
            'vn': 'Người lạ mặt tạo cho đối phương một ảo giác an toàn hoàn hảo bằng thái độ khiêm nhường và giọng nói nhẹ nhàng.',
            'en': 'The stranger cultivated a perfect illusion of safety through his modest demeanor and gentle tone of voice.',
            'ja': 'その見知らぬ男は、謙虚な態度と穏やかな口調によって、完璧な安全の錯覚を作り出していた。'
        },
        {
            'pos': 6,
            'vn': 'Thứ mùi tanh nồng của sự phân hủy bị che đậy vụng về bằng chất tẩy rửa nồng nặc khiến cơ thể nạn nhân lập tức kích hoạt phản xạ báo động.',
            'en': 'The pungent stench of decay, clumsily masked beneath harsh cleaning chemicals, instantly triggered the victim\'s primal alarm reflexes.',
            'ja': '強い洗剤で不器用に隠された腐敗の異臭が、被害者の生体防御反応を瞬時に作動させた。'
        },
        {
            'pos': 9, # at end
            'vn': 'Âm thanh u ám từ màn hình hòa lẫn với tiếng kim loại va chạm biến căn phòng thành một cái bẫy tâm lý ngột ngạt không lối thoát.',
            'en': 'Somber sounds from the screen blended with the clink of metal, transforming the apartment into a suffocating psychological trap with no escape.',
            'ja': 'テレビ画面から流れる不気味な音と金属音が混ざり合い、その部屋を逃げ場のない息苦しい心理的罠へと変貌させていた。'
        }
    ],
    '1.06': [
        {
            'pos': 2,
            'vn': 'Edwards hiểu rằng bất kỳ dấu hiệu hoảng loạn nào cũng có thể kích động cơn thịnh nộ bạo lực của kẻ đang nắm giữ sinh mạng mình.',
            'en': 'Edwards realized that any display of panic could instantly trigger a violent rage in the man who held his life in his hands.',
            'ja': 'エドワーズは、パニックの兆候を見せれば、自らの命を握る男の暴力的な激高を引き起こしかねないと理解していた。'
        },
        {
            'pos': 4,
            'vn': 'Anh khéo léo dùng những lời an ủi để ru ngủ cơn nghi ngờ ái kỷ của kẻ săn mồi.',
            'en': 'He deftly used soothing words to pacify the predator\'s narcissistic paranoia.',
            'ja': '彼は巧みな慰めの言葉を用い、捕食者の自己愛的な猜疑心を巧みに鎮めた。'
        },
        {
            'pos': 7, # before last sent
            'vn': 'Đó là một quyết định sinh tử xuất phát từ trực giác sinh tồn phi thường trong khoảnh khắc cận kề cái chết.',
            'en': 'It was a life-or-death decision born of extraordinary survival intuition in the face of imminent demise.',
            'ja': 'それは死の淵において、並外れた生存本能が生み出した生死を分ける決断だった。'
        }
    ],
    '1.09': [
        {
            'pos': 3,
            'vn': 'Vẻ ngoài lịch thiệp và dáng vẻ nhút nhát của người chủ nhà đã dựng nên một tấm bình phong che giấu hoàn hảo.',
            'en': 'The occupant\'s polite demeanor and seemingly shy appearance constructed an impeccable facade of innocence.',
            'ja': '部屋の主の礼儀正しい物腰と内気そうな外見は、完璧な隠れ蓑となっていた。'
        },
        {
            'pos': 6,
            'vn': 'Nhưng bản năng nghiệp vụ mách bảo người sĩ quan rằng sự bình thản quá mức trước cáo buộc bạo lực luôn là dấu hiệu bất thường.',
            'en': 'Yet seasoned police instincts warned the officer that unnatural composure in the face of violent accusations is always an alarming signal.',
            'ja': 'しかし、暴力の告発を前にした不自然なほどの冷静さは異常な兆候であると、警察官の直感が警告していた。'
        },
        {
            'pos': 8, # at end
            'vn': 'Những bức ảnh lưu giữ chiến tích tàn độc ấy chính là bằng chứng tố giác sự tha hóa tột cùng của nhân tính.',
            'en': 'Those photographs documenting his cruel trophies stood as undeniable proof of the ultimate degradation of humanity.',
            'ja': '残虐な戦利品を記録したそれらの写真は、人間性の極限の堕落を告発する動かぬ証拠だった。'
        }
    ],
    '1.10': [
        {
            'pos': 2,
            'vn': 'Mùi hóa chất công nghiệp và sự lạnh lẽo bao trùm không gian khiến bất cứ ai bước vào cũng phải rùng mình.',
            'en': 'The pervasive stench of industrial chemicals and the eerie chill filling the room made everyone present shudder.',
            'ja': '立ち込める工業用化学薬品の異臭と異様な冷気は、足を踏み入れた者すべてを戦慄させた。'
        },
        {
            'pos': 4,
            'vn': 'Kẻ thủ ác đã biến chính không gian sinh hoạt hằng ngày thành một nhà xưởng tội ác khép kín.',
            'en': 'The perpetrator had turned his everyday living space into a secluded workshop of heinous crime.',
            'ja': '犯人は自らの日常生活の空間を、密閉された凶悪犯罪の作業場へと変貌させていた。'
        }
    ],
    '1.11': [
        {
            'pos': 1,
            'vn': 'Sự yên bình giả tạo của khu phố trung tâm lập tức tan vỡ khi hàng loạt xe cảnh sát phong tỏa tòa nhà.',
            'en': 'The artificial tranquility of the downtown neighborhood shattered instantly as police cruisers cordoned off the building.',
            'ja': '多数の警察車両が建物を包囲するや否や、下町の不自然な平穏は瞬時に砕け散った。'
        },
        {
            'pos': 3,
            'vn': 'Người dân xung quanh bàng hoàng nhận ra bóng ma tội ác bấy lâu nay đã sống cạnh họ mà không hề bị phát giác.',
            'en': 'Surrounding residents realized in horror that a phantom of evil had lived alongside them completely undetected.',
            'ja': '近隣住民たちは、邪悪の亡霊が何の疑いも持たれずにすぐ隣で暮らしていたという事実に戦慄した。'
        },
        {
            'pos': 5, # at end
            'vn': 'Câu hỏi nhức nhối nhất lúc này là làm thế nào một cá nhân có thể che giấu bóng tối kinh hoàng ấy suốt hơn một thập kỷ.',
            'en': 'The most agonizing question now was how an individual could conceal such horrific darkness for well over a decade.',
            'ja': '今や最も重い問いは、一人の人間がどのようにして10年以上もの間、この戦慄すべき闇を隠し続けられたのかということだった。'
        }
    ],

    # ==========================================
    # ACT 2: +15 sentences (29 -> 44)
    # ==========================================
    '2.02': [
        {
            'pos': 1,
            'vn': 'Căn phòng hỏi cung nhỏ hẹp trở thành không gian đối thoại sinh tử giữa trật tự pháp lý và sự hỗn loạn tâm thần.',
            'en': 'The cramped interrogation room became the stage for an existential dialogue between legal order and psychological chaos.',
            'ja': 'その狭い取調室は、法的秩序と精神的混沌が対峙する生死をかけた対話の場となった。'
        },
        {
            'pos': 3,
            'vn': 'Sự im lặng ban đầu của nghi phạm phản ánh một cơ chế phòng vệ tự động trước nguy cơ bị phán xét.',
            'en': 'The suspect\'s initial silence reflected an automatic defense mechanism guarding against impending judgment.',
            'ja': '容疑者の当初の沈黙は、迫りくる裁きに対する自動的な防衛機制を反映していた。'
        }
    ],
    '2.04': [
        {
            'pos': 2,
            'vn': 'Kennedy hiểu rằng việc đối đầu gay gắt chỉ làm nghi phạm khép chặt cánh cửa giao tiếp.',
            'en': 'Kennedy understood that hostile confrontation would only cause the suspect to withdraw completely.',
            'ja': 'ケネディ捜査官は、敵対的な尋問は容疑者の心の扉を完全に閉ざしてしまうだけだと理解していた。'
        },
        {
            'pos': 4,
            'vn': 'Sự tôn trọng cơ bản dành cho nhân phẩm đối phương đã phá vỡ bức tường phòng thủ kiên cố nhất.',
            'en': 'Basic respect shown for human dignity breached the suspect\'s most fortified psychological defenses.',
            'ja': '人間の尊厳に対する基本的な敬意が、容疑者の最も堅固な心理的防壁を打ち破った。'
        },
        {
            'pos': 8, # at end
            'vn': 'Việc nghi phạm từ chối sự can thiệp của luật sư là dấu hiệu đầu tiên cho thấy nhu cầu tự thú đang bùng nổ.',
            'en': 'His refusal of legal representation was the first sign that an overwhelming urge to confess was breaking through.',
            'ja': '弁護士の同席を拒否したことは、告白したいという抑えがたい衝動が噴出し始めた最初の兆候だった。'
        }
    ],
    '2.05': [
        {
            'pos': 2,
            'vn': 'Dahmer không hề biểu lộ sự thách thức hay tìm cách chối bỏ trách nhiệm hình sự.',
            'en': 'Dahmer displayed no defiance and made no attempt to shirk criminal responsibility.',
            'ja': 'ダーマーは反抗的な態度を見せることもなく、刑事責任を回避しようともしなかった。'
        },
        {
            'pos': 5,
            'vn': 'Những bản vẽ chi tiết do chính tay hắn phác thảo đã giúp cảnh sát tái hiện đầy đủ từng manh mối.',
            'en': 'Detailed diagrams drawn by his own hand enabled investigators to piece together every elusive clue.',
            'ja': '彼自身の自筆による詳細な見取り図が、捜査陣によるすべての手がかりの完全な再構成を可能にした。'
        }
    ],
    '2.06': [
        {
            'pos': 1,
            'vn': 'Sự kiện người mẹ bỏ đi và người cha vắng nhà đã để lại một vết nứt tình cảm vĩnh viễn không thể hàn gắn.',
            'en': 'His mother\'s departure and his father\'s absence left a permanent, irreparable emotional fracture.',
            'ja': '母親の失踪と父親の不在は、生涯決して埋まることのない感情的な亀裂を残した。'
        },
        {
            'pos': 4,
            'vn': 'Cơn hoảng loạn bị bỏ rơi trỗi dậy như một cơn lốc hủy diệt khi người bạn mới quen chuẩn bị rời khỏi căn nhà.',
            'en': 'Terror of abandonment erupted like a catastrophic vortex the moment his newfound acquaintance prepared to leave.',
            'ja': '知り合ったばかりの友人が家を立ち去ろうとした瞬間、見捨てられる恐怖が破滅の渦のように爆発した。'
        }
    ],
    '2.07': [
        {
            'pos': 2,
            'vn': 'Mục tiêu của hắn không phải là hành hạ thể xác nạn nhân, mà là ngăn chặn sự chia lìa bằng mọi giá.',
            'en': 'His objective was never physical torture, but preventing separation at any cost.',
            'ja': '彼の目的は決して肉体的な拷問ではなく、いかなる代償を払ってでも別離を阻止することだった。'
        },
        {
            'pos': 5,
            'vn': 'Ảo tưởng biến tha nhân thành một vật thể vĩnh cửu bên mình đã bắt rễ sâu sắc từ vụ án đầu tiên này.',
            'en': 'The delusion of turning another human into a permanent possession took deep root from that very first homicide.',
            'ja': '他者を自己の永遠の所有物に変えるという妄想は、この最初の殺人によって深く根を下ろした。'
        }
    ],
    '2.08': [
        {
            'pos': 2,
            'vn': 'Chất cồn liều cao đóng vai trò như một hóa chất gây tê liệt lương tri trước khi hắn bước qua ranh giới cấm kỵ.',
            'en': 'High doses of alcohol served as a chemical anesthetic for his conscience before he crossed forbidden boundaries.',
            'ja': '大量のアルコールは、禁忌の境界を踏み越える前に良心を麻痺させる化学的麻酔薬の役割を果たしていた。'
        },
        {
            'pos': 4,
            'vn': 'Hắn ghê tởm hành vi của chính mình nhưng hoàn toàn bất lực trước cơn nghiện quyền lực kiểm soát con người.',
            'en': 'He loathed his own actions yet remained utterly powerless against an addiction to absolute control over humans.',
            'ja': '彼は自らの行為を嫌悪しながらも、他者を完全に支配するという中毒に対して全く無力だった。'
        },
        {
            'pos': 6,
            'vn': 'Sự mâu thuẫn nội tâm gay gắt giữa sự ghê sợ và dục vọng thống trị đã đẩy tâm trí hắn vào vùng tối tăm nhất.',
            'en': 'Severe internal conflict between revulsion and the thirst for dominance plunged his mind into the deepest abyss.',
            'ja': '自己嫌悪と支配欲との間の激しい内面葛藤が、彼の精神を最も暗い深淵へと突き落とした。'
        },
        {
            'pos': 9, # at end
            'vn': 'Sau mỗi lần gây án, nỗi cô đơn lại quay trở lại gặm nhấm tâm hồn hắn với sự tàn nhẫn gấp bội.',
            'en': 'After every crime, isolation returned to gnaw at his soul with compounded ruthlessness.',
            'ja': '凶行を終えるたびに、孤独は倍加した残酷さで彼の魂を再び激しく苛んだ。'
        }
    ],

    # ==========================================
    # ACT 3: +22 sentences (32 -> 54)
    # ==========================================
    '3.02': [
        {
            'pos': 1,
            'vn': 'Các chuyên gia tâm thần học pháp y phải đối mặt với một câu hỏi hóc búa về ranh giới giữa bệnh lý và sự tàn ác.',
            'en': 'Forensic psychiatrists were confronted with a perplexing dilemma on the boundary between pathology and cruelty.',
            'ja': '法医学精神医学の専門家たちは、精神病理と残酷さの境界を巡る難解な問いに直面した。'
        },
        {
            'pos': 3,
            'vn': 'Cần phải bóc tách từng tầng nhận thức để thấu hiểu căn nguyên của một nhân cách bị biến dạng nghiêm trọng.',
            'en': 'Every cognitive layer had to be unraveled to grasp the roots of a profoundly distorted personality.',
            'ja': '著しく歪められた人格の根源を把握するためには、認知的階層を一層ずつ解き明かす必要があった。'
        }
    ],
    '3.03': [
        {
            'pos': 2,
            'vn': 'Người mắc chứng rối loạn nhân cách ranh giới thường trải qua những cơn hoảng loạn tột độ khi đối diện với nguy cơ chia ly.',
            'en': 'Individuals suffering from borderline personality disorder frequently experience extreme panic when facing separation.',
            'ja': '境界性パーソナリティ障害の患者は、別離の危機に直面した際、しばしば極度のパニックを経験する。'
        },
        {
            'pos': 4,
            'vn': 'Khoảng trống cảm xúc thời niên thiếu đã biến thành một hố đen nuốt chửng khả năng thiết lập mối quan hệ lành mạnh.',
            'en': 'An emotional void from youth transformed into a black hole swallowing any capacity for healthy relationships.',
            'ja': '幼少期の感情的空白は、健全な人間関係を構築する能力を飲み込むブラックホールと化した。'
        },
        {
            'pos': 6,
            'vn': 'Dahmer không thể chịu đựng được ý niệm rằng đối phương có quyền tự do lựa chọn bước ra khỏi cuộc đời hắn.',
            'en': 'Dahmer could not endure the notion that others possessed the autonomy to walk out of his life.',
            'ja': 'ダーマーは、相手が自らの人生から立ち去る自由意志を持っているという概念に耐えられなかった。'
        },
        {
            'pos': 8,
            'vn': 'Hắn nhìn nhận sự từ chối không phải như một hành vi giao tiếp xã hội bình thường, mà như một đòn hủy diệt bản ngã.',
            'en': 'He viewed rejection not as normal social discourse, but as an annihilating strike against his very existence.',
            'ja': '彼は拒絶を通常の対人関係としてではなく、自己の存在そのものを消滅させる打撃として捉えていた。'
        },
        {
            'pos': 10,
            'vn': 'Ảo tưởng sở hữu tuyệt đối sinh ra từ chính sự bất lực thảm hại trong việc tìm kiếm sự thấu cảm của tha nhân.',
            'en': 'Delusions of absolute possession stemmed directly from a pathetic inability to achieve genuine human empathy.',
            'ja': '絶対的な所有の妄想は、他者との真の共感を得られないという絶望的な無能力から生じたものだった。'
        },
        {
            'pos': 12,
            'vn': 'Nỗi đau đớn cô độc khiến hắn tìm mọi cách để biến con người thành những vật trưng bày câm lặng.',
            'en': 'Agonizing isolation drove him to reduce dynamic human beings into muted, passive displays.',
            'ja': '耐えがたい孤独が、生きた人間を物言わぬ受動的な展示物へと変えようとする衝動へと彼を駆り立てた。'
        },
        {
            'pos': 13,
            'vn': 'Đây là sự biểu hiện cực đoan nhất của hội chứng sợ chia ly biến tướng thành hành vi săn mồi.',
            'en': 'This represents the most extreme manifestation of separation anxiety mutated into predatory behavior.',
            'ja': 'これは、捕食的行動へと変異した分離不安症候群の最も極端な現れである。'
        }
    ],
    '3.04': [
        {
            'pos': 1,
            'vn': 'Sự biến dạng nhân cách này đã đẩy kẻ thủ ác lún sâu vào một vòng xoáy bệnh hoạn không thể tự dứt ra.',
            'en': 'This severe personality deformation plunged the killer into a pathological vortex from which he could not escape.',
            'ja': 'この深刻な人格の歪みは、殺人者を自力では抜け出せない病理的な渦の中へと沈めていった。'
        }
    ],
    '3.05': [
        {
            'pos': 2,
            'vn': 'Hiện tượng khách thể hóa này cho phép kẻ thủ ác tước bỏ hoàn toàn nhân tính của người đối diện.',
            'en': 'This objectification process allowed the offender to strip his victims entirely of their human essence.',
            'ja': 'この客体化のプロセスにより、犯人は目の前の人間から人間性を完全に剥奪することができた。'
        },
        {
            'pos': 4,
            'vn': 'Một vật thể vô tri sẽ không bao giờ biết phán xét, không tranh cãi và quan trọng nhất là không bao giờ rời bỏ hắn.',
            'en': 'An inanimate object would never judge, never argue, and above all, never abandon him.',
            'ja': '無生物の物体であれば、彼を批判することも、口論することも、そして何よりも彼を見捨てることもない。'
        },
        {
            'pos': 6,
            'vn': 'Sự lệch lạc nhận thức này phản ánh một nỗ lực tuyệt vọng nhằm trốn tránh cảm giác bị tổn thương tinh thần.',
            'en': 'This cognitive distortion reflected a desperate attempt to evade profound emotional vulnerability.',
            'ja': 'この認知の歪みは、深い精神的傷つきやすさから逃れようとする必死の試みを反映していた。'
        },
        {
            'pos': 8,
            'vn': 'Những thí nghiệm vô nhân tính được tiến hành chỉ để tạo ra một sinh thể ngoan ngoãn phục tùng tuyệt đối.',
            'en': 'Inhumane procedures were carried out solely to fashion a completely docile, obedient entity.',
            'ja': '非人道的な実験は、ただ完全に受動的で服従する存在を作り出すためだけに行われた。'
        },
        {
            'pos': 10,
            'vn': 'Khi những nỗ lực bệnh lý đó liên tiếp thất bại, hắn rơi vào trạng thái bế tắc và hoảng loạn nhận thức.',
            'en': 'When those pathological experiments inevitably failed, he plunged into utter cognitive despair and panic.',
            'ja': 'それらの病理的試みがことごとく失敗した時、彼は深刻な認知的絶望とパニックに陥った。'
        },
        {
            'pos': 12,
            'vn': 'Tội ác tiếp theo lại được thực hiện như một phản ứng dây chuyền để lấp đầy hố sâu thất vọng.',
            'en': 'Subsequent homicides were executed in a chain reaction to bridge an ever-widening chasm of disappointment.',
            'ja': '広がり続ける失望の溝を埋めるため、連鎖反応のように次の犯行が繰り返された。'
        },
        {
            'pos': 13,
            'vn': 'Đó là một mê cung nhận thức khép kín, nơi mỗi bước đi sai lầm lại đòi hỏi một tội ác lớn hơn để che đậy.',
            'en': 'It was a closed cognitive maze where each misstep demanded a greater atrocity to sustain the illusion.',
            'ja': 'それは閉ざされた認知的迷宮であり、一度の誤った歩みが錯覚を維持するためにより大きな凶行を要求した。'
        },
        {
            'pos': 14,
            'vn': 'Hắn trở thành tù nhân của chính những ảo tưởng bệnh hoạn do bộ não méo mó của mình sản sinh ra.',
            'en': 'He became the helpless prisoner of the very macabre fantasies generated by his distorted psyche.',
            'ja': '彼は、自らの歪んだ精神が生み出した不気味な妄想の無力な囚人となったのである。'
        }
    ],
    '3.06': [
        {
            'pos': 1,
            'vn': 'Sự phân tách tâm lý này là lời giải thích then chốt cho lối sống hai mặt của Jeffrey Dahmer suốt nhiều năm.',
            'en': 'This psychological division provides the pivotal explanation for Jeffrey Dahmer\'s double life over so many years.',
            'ja': 'この心理的分断こそが、長年にわたるジェフリー・ダーマーの二重生活を解き明かす極めて重要な説明である。'
        }
    ],
    '3.07': [
        {
            'pos': 2,
            'vn': 'Cơ chế chia ngăn nhận thức giúp bộ não cô lập cảm giác tội lỗi ra khỏi đời sống sinh hoạt thường nhật.',
            'en': 'Compartmentalization enabled his brain to insulate guilt away from ordinary day-to-day existence.',
            'ja': '区画化の機制は、彼の脳が日常の平穏な生活から罪悪感を隔離することを可能にした。'
        },
        {
            'pos': 5,
            'vn': 'Hắn cư xử hoàn toàn nhã nhặn tại nơi làm việc như một con người bình thường không tì vết.',
            'en': 'He behaved with impeccable politeness at his workplace like an utterly ordinary, blameless citizen.',
            'ja': '職場では非の打ち所がないほど礼儀正しく振る舞い、全く普通の模範的な市民を演じていた。'
        },
        {
            'pos': 8, # at end
            'vn': 'Chính sự phân ly này đã vô hiệu hóa khả năng tự điều chỉnh hành vi và triệt tiêu mọi rào cản đạo đức.',
            'en': 'It was precisely this dissociation that disabled behavioral self-regulation and dismantled all moral barriers.',
            'ja': 'まさにこの解離こそが行動の自己制御を麻痺させ、あらゆる道徳的障壁を解体したのである。'
        }
    ],
    '3.08': [], # keep 3

    # ==========================================
    # ACT 4: +13 sentences (37 -> 50)
    # ==========================================
    '4.02': [
        {
            'pos': 2,
            'vn': 'Hàng trăm phóng viên từ khắp nơi trên thế giới đổ về tòa án để theo dõi cuộc đối đầu lịch sử.',
            'en': 'Hundreds of journalists from across the globe descended upon the courthouse to cover this historic trial.',
            'ja': 'この歴史的裁判を取材するため、世界中から数百人の記者たちが法廷へと押し寄せた。'
        },
        {
            'pos': 5,
            'vn': 'Không khí bên trong khán phòng đặc quánh sự phẫn nộ và nỗi đau đớn khôn nguôi của dư luận.',
            'en': 'The atmosphere inside the courtroom was thick with simmering outrage and inconsolable grief.',
            'ja': '法廷内の空気は、抑えきれない怒りと癒えることのない悲痛さで重苦しく張り詰めていた。'
        }
    ],
    '4.04': [
        {
            'pos': 2,
            'vn': 'Luật sư bào chữa nhấn mạnh rằng hành vi của Dahmer bắt nguồn từ những xung động tâm thần không thể kháng cự.',
            'en': 'The defense insisted that Dahmer\'s conduct stemmed from uncontrollable, irresistible psychiatric compulsions.',
            'ja': '弁護側は、ダーマーの行動が抑えることのできない精神医学的衝動に起因するものであると強調した。'
        },
        {
            'pos': 4,
            'vn': 'Họ tìm cách thuyết phục bồi thẩm đoàn rằng một nhân cách tan vỡ không thể mang đầy đủ năng lực chịu tội.',
            'en': 'They sought to convince the jury that such a fractured psyche could not bear full criminal culpability.',
            'ja': '彼らは、これほど崩壊した精神が完全な刑事責任能力を負うことはできないと陪審員を説得しようと試みた。'
        }
    ],
    '4.05': [
        {
            'pos': 4,
            'vn': 'Hắn biết rõ thời điểm nào cần che giấu hành vi và cách thức xóa bỏ dấu vết để tránh sự can thiệp của pháp luật.',
            'en': 'He knew precisely when to conceal his acts and how to obliterate traces to avoid law enforcement detection.',
            'ja': '彼は法執行機関の介入を避けるため、いつ行為を隠蔽し、どのように証拠を消し去るべきかを熟知していた。'
        }
    ],
    '4.06': [
        {
            'pos': 1,
            'vn': 'Từng nhân chứng bước lên bục khai báo mang theo những kỷ vật và câu chuyện đau xót về những người con đã mất.',
            'en': 'Witnesses took the stand one by one, bearing cherished keepsakes and heartbreaking memories of their lost sons.',
            'ja': '証人たちが次々と証言台に立ち、失われた息子たちのかけがえのない形見と胸をえぐる思い出を語った。'
        },
        {
            'pos': 3,
            'vn': 'Tiếng khóc nghẹn ngào của những người mẹ đã làm tan chảy cả những trái tim sắt đá nhất trong phòng xử.',
            'en': 'The stifled weeping of grieving mothers melted even the most hardened hearts throughout the courtroom.',
            'ja': '嘆き悲しむ母親たちの抑えきれない啜り泣きは、法廷内の最も頑なな心さえも揺さぶった。'
        }
    ],
    '4.07': [], # keep 8
    '4.09': [
        {
            'pos': 4,
            'vn': 'Mỗi bản án tù chung thân là một tuyên ngôn đanh thép khẳng định giá trị thiêng liêng của mạng sống con người.',
            'en': 'Each consecutive life sentence stood as an unyielding affirmation of the sacred value of human life.',
            'ja': '言い渡された連続終身刑の判決の一つひとつが、人命の尊厳な価値を主張する毅然とした宣言であった。'
        }
    ],
    '4.10': [
        {
            'pos': 1,
            'vn': 'Sự phân định rạch ròi giữa bệnh lý tâm thần và trách nhiệm đạo đức là cốt lõi của công lý văn minh.',
            'en': 'The lucid demarcation between psychiatric pathology and moral culpability forms the bedrock of civilized justice.',
            'ja': '精神病理と道徳的責任との間の明快な線引きこそが、文明社会における正義の根幹をなすものである。'
        },
        {
            'pos': 3,
            'vn': 'Một kẻ có thể chịu đựng những rối loạn sâu sắc nhưng vẫn phải đối mặt với sự trừng phạt nếu còn khả năng lựa chọn hành vi.',
            'en': 'A perpetrator may suffer profound disorders yet must face retribution if the capacity for behavioral choice remains.',
            'ja': '深い精神障害を抱えていたとしても、行動を選択する能力が残されている限り、犯人は罰を受けねばならない。'
        },
        {
            'pos': 5, # at end
            'vn': 'Pháp luật không cho phép bất kỳ ai lấy tổn thương cá nhân làm cái cớ để hủy hoại tự do của người khác.',
            'en': 'The law never permits anyone to utilize personal anguish as a license to extinguish the freedom of others.',
            'ja': '法は、自らの苦悩を口実にして他者の自由を奪う行為を決して容認しないのである。'
        }
    ],
    '4.11': [
        {
            'pos': 1,
            'vn': 'Những ngày tháng cuối đời sau song sắt là thời gian duy nhất Dahmer buộc phải đối diện trần trụi với chính mình.',
            'en': 'His final days behind bars were the only time Dahmer was forced to confront his naked, unvarnished self.',
            'ja': '鉄格子の背後で過ごした最期の日々は、ダーマーが飾りのない自らの生身の姿と向き合わざるを得ない唯一の時間だった。'
        },
        {
            'pos': 3, # at end
            'vn': 'Cái chết bất ngờ đã đặt dấu chấm hết cho cuộc đời tăm tối nhưng mở ra những câu hỏi sâu sắc về nhân tính.',
            'en': 'His abrupt death brought an end to a wretched existence while opening profound inquiries into the human condition.',
            'ja': 'その突然の死は悲惨な生涯に幕を下ろしたが、同時に人間性に関する深遠な問いを投げかけたのである。'
        }
    ],

    # ==========================================
    # ACT 5: +8 sentences (28 -> 36)
    # ==========================================
    '5.02': [
        {
            'pos': 1,
            'vn': 'Thảm kịch này mãi mãi khắc ghi như một vết sẹo đau đớn trong ký ức của các gia đình và toàn xã hội.',
            'en': 'This tragedy remains forever etched as a painful scar in the collective memory of families and society.',
            'ja': 'この悲劇は、遺族たちと社会全体の記憶の中に、痛ましい傷跡として永遠に刻まれている。'
        },
        {
            'pos': 4,
            'vn': 'Sự thiếu cảnh giác của cộng đồng và sự rạn nứt trong các mối liên kết xã hội đã tạo nên mảnh đất màu mỡ cho tội ác.',
            'en': 'Community lapses and frayed social bonds provided fertile ground for evil to fester undetected.',
            'ja': '地域社会の警戒の弛緩と希薄化した人間関係が、悪が人知れず増殖する肥沃な土壌を提供してしまった。'
        }
    ],
    '5.03': [
        {
            'pos': 2,
            'vn': 'Sự thờ ơ hay định kiến trong việc tiếp nhận thông tin từ người dân có thể phải trả giá bằng sinh mạng con người.',
            'en': 'Indifference or prejudice when processing citizen reports can extract an unbearable toll in human lives.',
            'ja': '市民からの通報を処理する際の無関心や偏見は、人命という取り返しのつかない代償を要求しかねない。'
        }
    ],
    '5.04': [
        {
            'pos': 1,
            'vn': 'Mỗi sự cô lập cảm xúc kéo dài đều là một tín hiệu báo động cần được xã hội lắng nghe và sẻ chia kịp thời.',
            'en': 'Prolonged emotional isolation is an urgent distress signal demanding timely societal awareness and intervention.',
            'ja': '長期化する感情的孤立は、社会によるタイムリーな気づきと介入を求める緊急の救難信号である。'
        },
        {
            'pos': 4,
            'vn': 'Một cộng đồng lành mạnh là nơi mọi cá nhân đều được kết nối và không ai bị bỏ rơi trong tuyệt vọng.',
            'en': 'A healthy society is one where every individual is connected and no one is left to suffer in despair.',
            'ja': '健全な社会とは、すべての個人が繋がりを持ち、誰一人として絶望の中に放置されない場所である。'
        },
        {
            'pos': 6, # at end
            'vn': 'Đó là trách nhiệm chung của cả gia đình, nhà trường và toàn bộ hệ thống an sinh xã hội.',
            'en': 'That is the shared responsibility of families, schools, and the entire social welfare system.',
            'ja': 'それは家庭、学校、そして社会福祉システム全体が共有すべき責任なのである。'
        }
    ],
    '5.05': [
        {
            'pos': 2,
            'vn': 'Sự hiểu biết sâu sắc về các thủ thuật tâm lý của kẻ săn mồi là vũ khí phòng vệ hiệu quả nhất.',
            'en': 'A thorough comprehension of predatory psychological tactics constitutes the most potent defensive shield.',
            'ja': '捕食者の心理的手法に対する深い理解こそが、最も効果的な自己防衛の盾となる。'
        },
        {
            'pos': 12,
            'vn': 'Sự nhạy bén với những bất thường xung quanh sẽ giúp bảo vệ chính bản thân và những người thân yêu.',
            'en': 'Keen vigilance toward environmental oddities safeguards both oneself and those we cherish.',
            'ja': '周囲の異常に対する鋭敏な警戒心が、自分自身と愛する人々を守ることに繋がる。'
        }
    ]
}
