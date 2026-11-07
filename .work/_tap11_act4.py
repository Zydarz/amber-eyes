# -*- coding: utf-8 -*-
"""Dữ liệu Hồi 4 Kịch bản Tập 11 (4 ngôn ngữ: VN, EN, JA, KO)."""

ACT4_ELEMENTS = [
    {
        "id": "4.01",
        "kind": "BGM",
        "desc_vn": "Âm thanh vĩ cầm dồn dập, giằng xé, tái hiện sự bàng hoàng và cuộc khủng hoảng tư pháp lịch sử.",
        "desc_en": "Tense, agitated violin phrases echoing the shockwaves of a historic judicial crisis.",
        "desc_ja": "張り詰めたバイオリンの旋律が激しく交錯し、歴史的司法危機の動揺を再現する。",
        "desc_ko": "팽팽하게 조여오는 바이올린 선율이 격정적으로 교차하며, 사법 체계의 역사적 위기가 몰고 온 충격을 재현한다."
    },
    {
        "id": "4.02",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "dẫn dắt hồi hộp, tái hiện áp lực nghẹt thở của cơ quan công tố",
        "direction_en": "suspenseful, evoking the suffocating prosecutorial pressure",
        "direction_ja": "緊張感に満ちた語り口で、検察当局の息詰まるプレッシャーを再現する",
        "direction_ko": "숨 막히는 긴장감을 담아 검찰 당국이 직면했던 극심한 압박감을 묘사하며",
        "sents_vn": [
            "Mùa xuân năm 1993, nền tư pháp tỉnh Ontario đứng trước một áp lực khủng khiếp từ dư luận và truyền thông quốc tế.",
            "Paul Bernardo đã bị bắt vì các vụ án tại Scarborough, nhưng cảnh sát hoàn toàn bế tắc trong việc tìm kiếm bằng chứng vật chất trực tiếp để buộc tội hắn giết hại Leslie Mahaffy và Kristen French.",
            "Paul giữ im lặng tuyệt đối, từ chối mọi sự hợp tác và thách thức các điều tra viên.",
            "Trong bối cảnh nghẹt thở ấy, Karla Homolka xuất hiện như một tia hy vọng duy nhất để giải mã hai vụ án mạng kinh hoàng.",
            "Được sự hậu thuẫn của các luật sư tài ba, Karla đã vận dụng hoàn hảo chiếc mặt nạ 'Hội chứng Người phụ nữ bị Bạo hành'.",
            "Cô ta trình bày những vết thương trên cơ thể do Paul gây ra, khóc lóc và khẳng định mình chỉ là một nhân chứng bất đắc dĩ bị ép buộc dưới họng súng."
        ],
        "sents_en": [
            "In the spring of 1993, the justice system of Ontario faced immense pressure from the public and international media.",
            "Paul Bernardo had been detained for the Scarborough assaults, but investigators lacked direct forensic evidence linking him to the murders of Leslie Mahaffy and Kristen French.",
            "Bernardo maintained absolute silence, refusing all cooperation and openly defying interrogation teams.",
            "Amid this suffocating deadlock, Karla Homolka emerged as the sole viable key to cracking the unsolved murders.",
            "Flanked by skilled defense counsel, Karla masterfully capitalized on the 'Battered Woman Syndrome' defense.",
            "She showcased her injuries from Bernardo's January assault, weeping copiously and asserting she was merely an unwilling witness coerced under deadly threat."
        ],
        "sents_ja": [
            "1993年の春、オンタリオ州の司法当局は世論と国際的メディアからの途方もない重圧に晒されていました。",
            "Paul Bernardoはスカーバロー事件で身柄を拘束されたものの、Leslie MahaffyとKristen Frenchの命を奪った罪に彼を直接結びつける物的証拠は完全に欠落していました。",
            "Bernardoは黙秘を貫き、一切の協力を拒んで捜査員たちを嘲笑っていました。",
            "この息詰まる膠着状態の中、Karla Homolkaが未解決の凶行を解明する唯一の鍵として浮上したのです。",
            "有能な弁護団に支えられたKarlaは、『虐待された女性の症候群』の盾をこれ以上ないほど巧みに利用しました。",
            "彼女は1月の暴行による身体の傷跡を示して激しく涙を流し、銃口の下で強いられた無力な目撃者に過ぎなかったと主張しました。"
        ],
        "sents_ko": [
            "1993년 봄, Ontario 주의 사법 체계는 들끓는 여론과 전 세계 언론의 숨 막히는 압박 앞에 직면해 있었습니다.",
            "Paul Bernardo는 Scarborough 사건으로 체포되었으나, Leslie Mahaffy와 Kristen French 살해 사건에 그를 직접 연결할 결정적 물증은 전무했습니다.",
            "Bernardo는 철저히 묵비권을 행사하며 일체의 협조를 거부한 채 수사관들을 조롱하듯 버텼습니다.",
            "이러한 절망적인 교착 상태 속에서, Karla Homolka는 미궁에 빠진 살인 사건을 해결할 유일한 열쇠로 떠올랐습니다.",
            "유능한 변호인단의 조력을 받은 Karla는 ‘매 맞는 여성 증후군’이라는 가면을 완벽하게 활용했습니다.",
            "그녀는 1월 폭행으로 인한 몸의 상흔을 내보이며 비통하게 눈물을 흘렸고, 죽음의 공포 아래 강요당한 힘없는 목격자일 뿐이었다고 호소했습니다."
        ]
    },
    {
        "id": "4.03",
        "kind": "SFX",
        "desc_vn": "Tiếng bút ký trên giấy tờ và tiếng đóng dấu tư pháp vang lên một tiếng cộp.",
        "desc_en": "Fountain pen scribbling across legal parchment, followed by the heavy thud of a judicial seal stamp.",
        "desc_ja": "公文書にペンを走らせる音、それに続いて重々しく響く司法印鑑の打捺音。",
        "desc_ko": "서류 위에 만년필로 서명하는 사각거리는 소리, 이어 묵직하게 울리는 사법 공증 직인 소리."
    },
    {
        "id": "4.04",
        "kind": "LOI",
        "role": "ĐIỀU TRA VIÊN",
        "direction_vn": "giọng đanh thép, thuật lại sai lầm nghiệp vụ và bản hợp đồng gây tranh cãi",
        "direction_en": "firm, detailing the systemic miscalculation and controversial plea deal",
        "direction_ja": "毅然とした口調で、捜査上の致命的誤算と物議を醸した司法取引を詳述する",
        "direction_ko": "단호한 목소리로 수사상의 치명적인 오판과 논란의 사법 거래를 상세히 복기하며",
        "sents_vn": [
            "Các công tố viên hàng đầu của bang Ontario lúc bấy giờ đã mắc phải một cái bẫy tâm lý kinh điển: Đánh giá quá cao lời khai nhân chứng và bị thao túng bởi vẻ ngoài yếu đuối.",
            "Họ tin rằng nếu không có lời khai của Karla, Paul Bernardo có thể sẽ thoát tội giết người cấp độ một và chỉ phải nhận mức án nhẹ cho các vụ án tại Scarborough.",
            "Mong muốn nhanh chóng đem lại công lý cho gia đình nạn nhân đã khiến cơ quan công tố đánh mất sự cẩn trọng nghề nghiệp cần thiết.",
            "Tháng 5 năm 1993, Văn phòng Tổng chưởng lý bang Ontario chính thức ký kết một bản thỏa thuận nhận tội đặc biệt với Karla Homolka.",
            "Theo thỏa thuận, Karla nhận hai tội danh Ngộ sát với tổng mức án 12 năm tù giam, để đổi lấy lời khai vạch tội chồng mình trước tòa.",
            "Đổi lại, cô ta được miễn trừ truy tố đối với mọi hành vi liên quan đến sự ra đi của em gái Tammy và hai nữ sinh vô tội.",
            "Ngay khi thông tin rò rỉ, dư luận và báo chí Canada đã cay đắng gọi bản án ấy bằng một cái tên đầy phẫn uất: 'Thỏa thuận với Quỷ dữ'.",
            "Karla Homolka bình thản bước vào trại giam với nụ cười kín đáo, tin rằng mình đã chiến thắng hệ thống pháp luật."
        ],
        "sents_en": [
            "Senior Ontario prosecutors fell victim to a textbook cognitive trap: overvaluing witness testimony while blinded by perceived feminine helplessness.",
            "They believed that without Karla's inside testimony, Paul Bernardo might escape first-degree murder convictions and face only limited sentences for Scarborough.",
            "The desperate urge to deliver closure to grieving families compromised essential professional skepticism.",
            "In May 1993, the Ontario Attorney General's office formally executed an extraordinary plea agreement with Karla Homolka.",
            "Under the deal, Karla pleaded guilty to two counts of manslaughter receiving a 12-year prison sentence in exchange for testifying against her husband.",
            "In return, she was granted blanket immunity from murder charges regarding the deaths of her sister Tammy and both abducted girls.",
            "As leaks reached the public, Canadian media bitterly christened the transaction with an indignant label: the 'Deal with the Devil'.",
            "Karla Homolka walked into custody with a subtle sense of triumph, confident she had outwitted the entire legal apparatus."
        ],
        "sents_ja": [
            "当時のオンタリオ州検察幹部たちは、証言価値を過大評価し外見上の無力さに目を奪われるという典型的な認知の罠に陥っていました。",
            "彼らは、Karlaの証言がなければPaul Bernardoが第1級殺人罪を免れ、スカーバロー事件のみの限定的な量刑で終わってしまうと恐れていました。",
            "遺族のために迅速に事件を解決したいという強い焦燥感が、必要不可欠な職業的懐疑心を鈍らせてしまったのです。",
            "1993年5月、オンタリオ州司法長官事務所はKarla Homolkaとの間で異例の司法取引を正式に締結しました。",
            "取引に基づき、Karlaは夫に対する法廷証言と引き換えに、2件の過失致死罪を認めて懲役12年の判決を受けることになりました。",
            "見返りとして、彼女は妹Tammyおよび拉致された二人の少女の死に関する訴追を永久に免除されたのです。",
            "報道が漏れ伝わるや否や、カナダの世論とメディアはこの司法取引を怒りを込めて『悪魔との取引』と名指しました。",
            "Karla Homolkaは司法制度を完全に打ち負かしたと確信し、密かな満足感を漂わせながら刑務所へと収監されていきました。"
        ],
        "sents_ko": [
            "당시 Ontario 주 검찰 지휘부는 증언의 가치를 지나치게 맹신한 채 가련해 보이는 외모의 가면을 간파하지 못하는 전형적인 인지적 함정에 빠져들었습니다.",
            "그들은 Karla의 결정적인 증언이 없다면 Paul Bernardo가 1급 살인 혐의를 벗어나 Scarborough 사건에 대한 가벼운 처벌만 받고 풀려날 수 있다고 우려했습니다.",
            "유가족에게 신속히 정의를 안겨주어야 한다는 절박감이, 검사로서 지켜야 할 냉철한 직업적 회의감을 마비시켜 버렸습니다.",
            "1993년 5월, Ontario 주 검찰총장실은 Karla Homolka와 충격적인 형량 협상 계약을 공식 체결했습니다.",
            "합의에 따라 Karla는 남편의 유죄를 입증하는 법정 증언을 제공하는 대가로, 2건의 과실치사 혐의만을 인정하며 징역 12년을 선고받았습니다.",
            "그 반대급부로 그녀는 친동생 Tammy와 납치된 두 여학생의 비극적인 죽음과 관련된 모든 살인 혐의에 대해 완전한 기소 면제 특권을 얻었습니다.",
            "이 밀약의 전모가 언론에 유출되자마자, 캐나다 사회와 언론은 깊은 분노를 담아 이를 ‘악마와의 거래’라고 명명했습니다.",
            "Karla Homolka는 자신이 국가의 사법 시스템 전체를 농락했다고 확신하며, 은밀한 승리감 속에 교도소 문을 통과했습니다."
        ]
    },
    {
        "id": "4.05",
        "kind": "NGHI",
        "sec": 1.5,
        "desc_vn": "khoảng lặng kịch tính"
    },
    {
        "id": "4.06",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "chuyển giọng bí ẩn, mở ra bước ngoặt 6 cuộn băng",
        "direction_en": "mysterious, uncovering the turning point of the hidden videotapes",
        "direction_ja": "不穏なサスペンスを帯びた声、隠蔽されたビデオテープの転換点へ",
        "direction_ko": "미스터리한 분위기를 풍기며 숨겨진 비디오테이프의 반전으로",
        "sents_vn": [
            "Thỏa thuận đã được tòa án phê chuẩn và bản án 12 năm đã chính thức có hiệu lực pháp lý.",
            "Karla trở thành nhân chứng vàng của cơ quan công tố trong phiên tòa xét xử người chồng cũ.",
            "Thế nhưng, số phận đã sắp đặt một bước ngoặt nghiệt ngã phơi bày toàn bộ sự thật đen tối ra trước ánh sáng.",
            "Mùa thu năm 1994, trong khi Paul Bernardo đang bị biệt giam chờ ngày xét xử, luật sư mới của hắn là ông John Rosen đã bàn giao cho cảnh sát một bọc tang vật chấn động.",
            "Đó là 6 cuốn băng video ghi hình bí mật được tìm thấy ngay trong ngôi nhà số 57 Bayview Drive."
        ],
        "sents_en": [
            "The plea agreement had received judicial sanction, locking the 12-year sentence into absolute legal finality.",
            "Karla was positioned as the prosecution's star witness for the upcoming trial of her former husband.",
            "Yet an astonishing twist of fate was already preparing to drag the unfiltered truth into the light.",
            "In the autumn of 1994, while Paul Bernardo awaited trial in solitary confinement, his newly appointed attorney John Rosen delivered a seismic package of evidence to police.",
            "Contained inside were 6 covert videotapes recovered directly from 57 Bayview Drive."
        ],
        "sents_ja": [
            "司法取引は裁判所の承認を得て成立し、懲役12年の判決は法的に確定したものとなりました。",
            "こうしてKarlaは、元夫の公判における検察側の最重要スター証人として位置づけられました。",
            "しかし運命の残酷な皮肉は、覆い隠されていた真実を白日の下に晒す劇的な反転を用意していたのです。",
            "1994年秋、Paul Bernardoが独房で初公判を待つ中、彼の新任弁護士John Rosenが警察へ極めて重大な証拠物件を引き渡しました。",
            "それこそが、Bayview Drive 57番地の邸内から密かに回収された6本の隠しビデオテープだったのです。"
        ],
        "sents_ko": [
            "형량 합의는 법원의 최종 승인을 거쳤고, 징역 12년의 판결은 확고한 법적 구속력을 갖추게 되었습니다.",
            "Karla는 이제 전남편 Paul Bernardo의 재판을 승리로 이끌 검찰 측의 독보적인 핵심 증인으로 자리매김했습니다.",
            "그러나 가려져 있던 추악한 진실을 역사의 심판대 위에 끌어올릴 충격적인 운명의 반전이 조용히 기다리고 있었습니다.",
            "1994년 가을, Paul Bernardo가 독방에서 재판을 기다리던 중 그의 새 변호인 John Rosen이 경찰에 메가톤급 증거물을 전격 인계했습니다.",
            "그것은 바로 Bayview Drive 57번지 자택 깊숙한 곳에서 수거된 6개의 은밀한 비디오테이프였습니다."
        ]
    },
    {
        "id": "4.07",
        "kind": "LOI",
        "role": "ĐIỀU TRA VIÊN",
        "direction_vn": "lạnh lùng, tái hiện nguồn gốc tang vật và căn phòng tối công tố",
        "direction_en": "clinical, describing the hidden cache and the dark screening room",
        "direction_ja": "冷徹に証拠の出所と検察の暗い映写室の光景を再現する",
        "direction_ko": "차분하고 냉엄한 어조로 증거의 출처와 어두운 영사실의 참상을 묘사하며",
        "sents_vn": [
            "Sáu cuốn băng định mệnh này trước đó đã được Paul Bernardo giấu kín phía sau chiếc hộp đèn gắn trên trần phòng tắm của ngôi nhà.",
            "Luật sư ban đầu của Paul là Ken Murray đã tìm thấy chúng từ tháng 5 năm 1993 nhưng đã bí mật cất giấu suốt 17 tháng vì lo ngại chúng sẽ hủy hoại thân chủ mình.",
            "Chỉ khi Paul Bernardo quyết định thay đổi luật sư bào chữa, những cuốn băng này mới được giao nộp cho cơ quan điều tra.",
            "Khi chiếc máy chiếu được bật lên trong căn phòng họp kín của cơ quan công tố, toàn bộ không gian rơi vào một sự câm lặng kinh hoàng.",
            "Những gì hiện lên trên màn hình đã đánh sập hoàn toàn vở kịch dối trá mà Karla Homolka dày công dàn dựng.",
            "Hãy lắng nghe nỗi uất nghẹn của những người từng tin vào sự vô tội của cô ta."
        ],
        "sents_en": [
            "These fateful recordings had been secreted away by Paul Bernardo behind a lighting fixture in the ceiling of the master bathroom.",
            "Bernardo's original defense lawyer Ken Murray had discovered them in May 1993 but withheld them for 17 months out of professional conflict.",
            "Only after Paul Bernardo replaced counsel were the tapes finally transferred into the custody of law enforcement.",
            "As the tapes were played inside a locked conference room, the entire prosecution team was plunged into horrifying silence.",
            "What unspooled across the screen utterly obliterated the manipulative fabrications Karla Homolka had so meticulously sold.",
            "Listen to the bitter anguish of those who had once believed her fabricated innocence."
        ],
        "sents_ja": [
            "この運命のビデオテープは、Paul Bernardoによって浴室天井の照明器具の背後の空洞に厳重に隠匿されていました。",
            "Bernardoの当初の弁護士Ken Murrayは1993年5月にこれを発見していたものの、弁護活動の葛藤から17ヶ月間にわたり秘匿し続けていたのです。",
            "Paul Bernardoが弁護士を交代させたことによって初めて、これらのテープは法執行機関へと引き渡されました。",
            "検察本部の鍵の掛かった会議室でテープが再生された瞬間、部屋全体が息を呑むような凍りついた沈黙に包まれました。",
            "画面上に映し出された生々しい光景は、Karla Homolkaが周到に演じ続けてきた嘘の劇場を完膚なきまでに叩き潰したのです。",
            "彼女の無実の涙をかつて信じてしまった者たちの、痛恨の悲痛な声をお聞きください。"
        ],
        "sents_ko": [
            "이 운명의 테이프들은 Paul Bernardo가 안방 욕실 천장의 조명 기구 뒤편 빈 공간에 정교하게 숨겨두었던 것이었습니다.",
            "Bernardo의 초기 변호인이었던 Ken Murray는 1993년 5월에 이를 찾아냈으나, 의뢰인 보호와 직업윤리 사이의 갈등 속에 17개월 동안 비밀리에 보관해 왔습니다.",
            "Paul Bernardo가 변호인을 교체한 후에야 이 테이프들은 비로소 수사 기관의 수중에 정식으로 넘어올 수 있었습니다.",
            "검찰청의 밀폐된 회의실 안에서 모니터가 켜진 순간, 회의실 안의 모든 이들은 소름 끼치는 침묵 속으로 침잠했습니다.",
            "화면 위에 여과 없이 펼쳐진 참상은, Karla Homolka가 공들여 쌓아 올린 거짓의 성채를 일순간에 무너뜨려 버렸습니다.",
            "한때 그녀의 무고함을 믿어주었던 수사 인력의 비통한 회한을 직접 들어보시겠습니다."
        ]
    },
    {
        "id": "4.08",
        "kind": "LOI",
        "role": "NGƯỜI BÌNH THƯỜNG",
        "direction_vn": "N2: Nhân viên điều tra / Công tố viên, giọng nam trung niên uất nghẹn, cay đắng",
        "direction_en": "N2: Investigator/Prosecutor, middle-aged male, deeply bitter and remorseful",
        "direction_ja": "N2：捜査員／検察関係官、中年の男性、深い苦渋と後悔に満ちた声",
        "direction_ko": "N2: 수사관/검찰 관계자, 중년 남성, 깊은 회한과 비통함이 서린 목소리",
        "sents_vn": [
            "Hãy hình dung cảm giác cay đắng tột cùng của những người làm công tố khi ngồi trong căn phòng tối ngày hôm đó.",
            "Chúng tôi từng tin vào những giọt nước mắt của một người phụ nữ run rẩy nói rằng mình bị ép buộc.",
            "Nhưng những cuốn băng cho thấy Karla tham gia một cách chủ động, thậm chí cười đùa và đưa ra những chỉ dẫn lạnh lùng cho Paul.",
            "Cô ta không hề bị đe dọa, cô ta là một kẻ đồng lõa tàn nhẫn và say mê với tội ác.",
            "Giây phút ấy, chúng tôi hiểu rằng mình đã ký một bản hợp đồng nhượng bộ với chính quỷ dữ."
        ],
        "sents_en": [
            "Imagine the suffocating bitterness of sitting in that darkened room as seasoned officers of the court.",
            "We had put our faith in the trembling tears of a young woman claiming she had been completely coerced.",
            "Yet the tapes showed Karla actively participating, smiling, and coolly offering sadistic directions to Paul.",
            "She was under no duress whatsoever; she was an active, willing partner reveling in absolute control.",
            "In that sickening second, we realized we had truly signed a pact with the devil."
        ],
        "sents_ja": [
            "法を執行する立場の者として、あの薄暗い映写室に座っていた瞬間の胸をえぐられるような苦渋を想像してみてください。",
            "私たちは、すべてを暴力で強いられたと訴えて震えていた若い女性の涙を信じてしまっていたのです。",
            "しかし映像の中のKarlaは主体的に犯行を指揮し、微笑みさえ浮かべながらPaulに冷酷な指示を出していました。",
            "脅迫など一切存在せず、彼女は絶対的な支配を楽しみ自ら進んで凶行に加担する能動的な共犯者だったのです。",
            "その胸糞の悪くなるような瞬間、私たちは自分たちが正真正銘の悪魔と契約書を交わしてしまったことを悟りました。"
        ],
        "sents_ko": [
            "법을 집행하는 자로서, 그 어두운 영사실에 앉아 있던 순간의 찢어지는 듯한 회한을 한번 상상해 보십시오.",
            "저희는 모든 것을 강압에 못 이겨 행했다고 흐느끼던 그 가련한 여인의 눈물을 진심으로 믿어주었습니다.",
            "하지만 비디오 속 Karla는 범행을 주도적으로 이끌며, 심지어 미소를 띤 채 Paul에게 냉혹한 지시를 내리고 있었습니다.",
            "그곳에 어떠한 강요나 위협도 존재하지 않았으며, 그녀는 절대적인 지배를 만끽하며 범죄에 능동적으로 뛰어든 잔혹한 공범이었습니다.",
            "가슴이 무너져 내리던 바로 그 찰나, 저희는 자신들이 진짜 악마에게 면죄부를 내어주는 계약을 맺고 말았음을 깨달았습니다."
        ]
    },
    {
        "id": "4.09",
        "kind": "SFX",
        "desc_vn": "Tiếng cuộn băng tua nhanh kêu rít lên và tiếng đập bàn phẫn nộ vang lên rầm.",
        "desc_en": "High-pitched whine of a tape rewinding fast, followed by an angry fist slamming hard on the table.",
        "desc_ja": "ビデオテープが高速で巻き戻される甲高い軋み音、続いて怒りに任せて机が激しく叩かれる轟音。",
        "desc_ko": "비디오테이프가 고속으로 감기며 내는 날카로운 마찰음, 이어 분노에 차 탁자를 쾅 하고 내리치는 소리."
    },
    {
        "id": "4.10",
        "kind": "LOI",
        "role": "CHUYÊN GIA TÂM LÝ",
        "direction_vn": "học thuật, mổ xẻ hiện tượng Thao túng đóng vai nạn nhân",
        "direction_en": "clinical, dissecting manipulative victimhood and narcissistic sociopathy",
        "direction_ja": "学術的な切れ味で、被害者面の心理操作とサイコパス的欺瞞を解剖する",
        "direction_ko": "학술적 통찰을 담아 피해자 코스프레의 조작 수법과 사이코패스적 기만을 분석하며",
        "sents_vn": [
            "Sáu cuốn băng trên trần nhà chính là sự sụp đổ hoàn toàn của chiếc mặt nạ nạn nhân.",
            "Về mặt tâm lý học hành vi, Karla Homolka đã thực hiện một chiến lược 'Thao túng đóng vai nạn nhân' ở cấp độ thượng thừa.",
            "Cô ta hiểu rất rõ điểm mù lớn nhất của lòng trắc ẩn con người: xã hội thường mặc định phụ nữ trẻ đẹp luôn là nạn nhân chứ không thể là kẻ chủ mưu tàn ác.",
            "Bằng cách lợi dụng vụ việc do Paul gây ra vào tháng 1 năm 1993, cô ta đã khéo léo biến toàn bộ quá khứ của mình thành hệ quả của sự cưỡng ép.",
            "Nhưng những thước phim chân thực đã bóc trần sự thật: cô ta không hề chịu sự tê liệt nhận thức của 'Hội chứng Người phụ nữ bị Bạo hành'.",
            "Karla hoàn toàn tỉnh táo, có năng lực phán đoán và thể hiện sự thỏa mãn quyền lực tàn bạo khi chà đạp lên đồng loại.",
            "Đó không phải là nỗi sợ hãi, mà là sự tính toán lạnh lùng của một nhân cách thái nhân cách ngụy trang hoàn hảo.",
            "Nước mắt của cô ta chỉ là công cụ để mua chuộc lòng thương hại và trốn tránh bản án chung thân."
        ],
        "sents_en": [
            "Those 6 ceiling tapes marked the catastrophic demolition of the fabricated victim facade.",
            "In behavioral psychology, Karla Homolka executed an elite demonstration of 'Manipulative Victimhood'.",
            "She astutely exploited society's profoundest blindspot: the reflexive assumption that an attractive woman must be a victim rather than a ruthless predator.",
            "By leveraging the genuine domestic battery of January 1993, she reframed her entire predatory history as involuntary compliance.",
            "Yet raw video proved definitively that she never suffered from the cognitive paralysis of 'Battered Woman Syndrome'.",
            "Karla remained lucid, calculating, and visibly stimulated by wielding absolute dominance over helpless victims.",
            "This was never about paralysis under terror; it was cold sociopathic manipulation hiding behind tears.",
            "Her tears were tactical currency spent to purchase public sympathy and escape whole-life incarceration."
        ],
        "sents_ja": [
            "あの天井裏の6本のテープこそが、捏造された被害者の仮面を完膚なきまでに粉砕した証拠でした。",
            "行動心理学において、Karla Homolkaが実行したのは極めて高度な『被害者面の心理操作』でした。",
            "彼女は人間社会の最大の盲点、すなわち魅力的な女性は冷酷な捕食者ではなく被害者であるはずだという思い込みを冷徹に利用しました。",
            "1993年1月に現実に受けた暴行を巧妙に梃子にして、自らの過去の全凶行を抵抗不能な強要の結果として再構成したのです。",
            "しかし生々しい映像は、彼女が『虐待された女性の症候群』の認知麻痺など微塵も患っていなかった事実を証明しました。",
            "Karlaは完全に理性を保ち、計算高く、無力な他者に対して絶対的な支配権力を振るうことに快感を覚えていました。",
            "そこにあったのは恐怖による服従などではなく、涙の裏に潜む冷徹なサイコパス的マニピュレーションでした。",
            "彼女の涙は同情を買い集め、終身刑の鉄格子から逃れるために計画的に投じられた戦術的通貨に過ぎなかったのです。"
        ],
        "sents_ko": [
            "천장 속에 숨겨져 있던 6개의 테이프는 날조된 피해자 가면의 완전한 파멸을 고하는 증거였습니다.",
            "행동심리학적으로 볼 때, Karla Homolka가 구사한 것은 최고 수준의 ‘피해자 코스프레’ 조작술이었습니다.",
            "그녀는 매력적인 젊은 여성은 잔혹한 포식자가 아니라 마땅히 피해자일 것이라는 사회의 가장 깊은 맹점을 정확히 꿰뚫고 이용했습니다.",
            "1993년 1월에 실제로 당했던 가정폭력 사건을 영악하게 지렛대 삼아, 자신의 과거 범죄 행적 전체를 거부할 수 없었던 강압의 결과로 둔갑시켰습니다.",
            "그러나 날것의 비디오 영상은 그녀가 ‘매 맞는 여성 증후군’의 인지적 무기력 상태와는 전혀 무관했음을 낱낱이 입증했습니다.",
            "Karla는 명민하게 상황을 인지하며 계산적으로 움직였고, 무력한 피해자들을 지배하며 잔인한 권력욕을 마음껏 충족시키고 있었습니다.",
            "그것은 결코 공포에 짓눌린 복종이 아니라, 눈물 뒤에 숨은 냉혈한 사이코패스의 완벽한 심리 조작이었습니다.",
            "그녀의 눈물은 대중의 동정심을 매수하고 종신형의 단죄를 피하기 위해 치밀하게 기획된 전술적 수단에 불과했습니다."
        ]
    },
    {
        "id": "4.11",
        "kind": "LOI",
        "role": "HOST",
        "direction_vn": "đanh thép, tái hiện cơn bão dư luận và bế tắc tư pháp",
        "direction_en": "forceful, chronicling the public firestorm and the legal stalemate",
        "direction_ja": "毅然とした力強さで、沸騰する世論の炎と司法の八方塞がりを再現する",
        "direction_ko": "단호하고 무게감 있게 들끓는 여론의 분노와 사법적 교착 상태를 전하며",
        "sents_vn": [
            "Một làn sóng thịnh nộ dữ dội chưa từng có bùng nổ khắp đất nước Canada khi thông tin về những cuốn băng bị rò rỉ.",
            "Hàng trăm ngàn người dân đã ký tên vào các bản kiến nghị đòi hủy bỏ thỏa thuận nhận tội và truy tố Karla Homolka tội giết người cấp độ một.",
            "Thế nhưng, nền tư pháp Canada lúc bấy giờ đã rơi vào một cái bẫy pháp lý bế tắc do chính mình tạo ra.",
            "Theo nguyên tắc bảo vệ quyền tố tụng và các điều khoản miễn trừ đã được tòa án đóng dấu, cơ quan công tố không thể đơn phương xé bỏ bản thỏa thuận khi Karla không vi phạm lời khai.",
            "Bản án 12 năm tù của người đàn bà trong ngôi nhà màu hồng vẫn được pháp luật bảo vệ nguyên vẹn.",
            "Trong khi đó, ngày 1 tháng 9 năm 1995, Paul Bernardo chính thức nhận phán quyết cuối cùng của công lý."
        ],
        "sents_en": [
            "An unprecedented wave of collective outrage swept across Canada as leaks about the videotapes became public knowledge.",
            "Hundreds of thousands of citizens signed furious petitions demanding the cancellation of the plea deal and the prosecution of Karla Homolka for first-degree murder.",
            "Yet Canadian jurisprudence found itself entrapped within an inescapable legal deadlock of its own making.",
            "Under foundational principles of due process and sealed binding immunity clauses, the Crown could not unilaterally revoke the contract so long as Karla honored her testimony.",
            "The 12-year sentence secured by the woman from the pink house remained unassailable under law.",
            "Meanwhile, on September 1, 1995, Paul Bernardo stood before the bench to receive the ultimate judgment of justice."
        ],
        "sents_ja": [
            "ビデオテープの存在が公に漏洩するや否や、前代未聞の怒りの大波がカナダ全土を席巻しました。",
            "数十万もの市民が署名に加わり、司法取引の破棄とKarla Homolkaに対する第1級殺人罪での起訴を猛烈に要求しました。",
            "しかし当時のカナダ司法は、自らが仕掛けた厳格な法的拘束力の罠に捕らわれて身動きが取れなくなっていました。",
            "適正手続きの原則と司法印が押された免責合意条項の下では、Karlaが法廷証言を遵守する限り、検察が一方的に契約を無効化することは不可能だったのです。",
            "ピンクの家の女が手に入れた懲役12年の刑期は、皮肉にも法によって不可侵のものとして守られ続けました。",
            "そして迎えた1995年9月1日、Paul Bernardoは遂に司法の最終審判を受けるため法廷に立ったのです。"
        ],
        "sents_ko": [
            "비디오테이프의 충격적인 진실이 세상 밖으로 새어 나가자, 전례 없는 거대한 분노의 물결이 캐나다 전역을 집어삼켰습니다.",
            "수십만 명의 시민들이 형량 협상 파기와 Karla Homolka에 대한 1급 살인 기소를 촉구하는 청원서에 분노의 서명을 남겼습니다.",
            "그러나 당시 캐나다 사법 체계는 스스로 만든 엄격한 법적 구속력의 덫에 걸려 완전히 손발이 묶여 있었습니다.",
            "적법 절차의 원칙과 법원이 보증한 면책 조항에 따라, Karla가 약속된 법정 증언을 번복하지 않는 한 검찰이 일방적으로 합의를 파기할 수는 없었습니다.",
            "분홍빛 주택의 여인이 챙긴 징역 12년의 가벼운 형벌은, 아이러니하게도 법의 엄격한 보호 아래 온전히 유지되었습니다.",
            "그사이 1995년 9월 1일, Paul Bernardo는 법의 준엄한 최종 심판을 받기 위해 피고인석에 섰습니다."
        ]
    },
    {
        "id": "4.12",
        "kind": "BGM",
        "desc_vn": "Một đoạn violin giằng xé ngân vang rồi chìm dần vào tiếng chuông điểm nhịp lạnh lẽo.",
        "desc_en": "Tense violin resonance fading slowly into the cold chiming of a clock tower.",
        "desc_ja": "激しいバイオリンの余韻が徐々に冷酷な鐘の刻みの中へと沈み込んでいく。",
        "desc_ko": "격정적인 바이올린의 잔향이 서서히 차가운 시계탑 종소리 속으로 잦아든다."
    }
]
