#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Quét CHỮ HÁN GIẢN THẠCH rộng hơn bộ SIMP_CHARS của pipeline.

Bộ trong pipeline chỉ có ~100 chữ, nên bỏ sót (VD 联 trong "联邦" của Tap09,
bản Nhật phải là "連邦"). Ở đây dùng bộ đầy đủ hơn: mọi chữ Trung giản thạch
KHÔNG dùng trong tiếng Nhật.

    py -3 .work/_ja_scan_simplified.py
"""
import io
import re
import sys
from pathlib import Path

ROOT = Path(r"D:\TEST\Gax\Audi")
KB = ROOT / "01_KICH_BAN"
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

# Chữ Hán giản thạch KHÔNG có trong tiếng Nhật hiện đại.
SIMP_ONLY = set(
    "爱碍袄坝罢摆败颁办绊帮绑镑谤剥饱宝报鲍辈贝钡狈备惫绷笔毕毙币闭边编贬变辩辫标"
    "鳖别瘪宾滨饼拨钵铂驳补财参蚕残惭惨灿仓沧厕层搀谗馋缠忏偿厂长肠尝畅钞车彻"
    "尘陈衬撑惩迟驰耻齿冲丑出础处触传疮闯创锤纯绰辞词赐聪葱囱从丛凑窜错达带"
    "贷担单郸掸胆惮诞弹当挡党荡档捣岛祷导盗灯邓敌涤递缔点垫电淀钓调迭谍叠钉顶"
    "锭订东动栋冻斗犊独读赌镀锻断缎兑队对吨顿钝夺堕鹅额讹恶饿儿尔饵贰发罚阀"
    "珐矾钒烦范贩饭访纺飞废费纷坟奋愤粪丰枫锋风疯冯缝讽凤肤辐抚辅赋复缚该"
    "钙盖干赶秆赣冈刚钢纲岗镐搁鸽阁铬个给龚宫巩贡钩沟构购够蛊顾剐关观馆惯贯"
    "广规硅归龟闺轨诡柜贵刽辊滚锅国过骇韩汉阂鹤贺横轰鸿红后壶护沪户哗华画划"
    "话怀坏欢环还缓换唤痪焕涣黄谎挥辉毁贿秽会烩汇讳诲绘荤浑伙获货祸击机积饥"
    "讥鸡绩极辑级挤几蓟剂济计记际继纪夹荚价驾歼监坚笺间艰缄茧检碱硷拣捡简"
    "俭减荐槛鉴践贱见键舰剑饯渐溅涧浆蒋桨奖讲酱胶浇骄娇搅铰矫侥脚饺缴绞轿较"
    "阶节茎惊经颈静镜径痉竞净纠旧驹举据锯惧剧鹃绢觉决诀绝钧军骏开凯颗壳课垦"
    "恳抠库裤夸块侩宽矿旷亏岿窥馈溃扩阔蜡腊莱来赖蓝栏拦篮阑兰澜谰揽览懒缆烂"
    "滥捞劳涝乐镭垒类泪篱离鲤礼丽厉励砾历沥隶俩联莲连镰怜涟帘敛脸链恋炼练"
    "粮凉两辆谅疗辽镣猎临邻鳞凛赁龄铃凌灵岭领馏刘龙聋咙笼垄拢陇楼娄搂篓芦"
    "卢颅庐炉掳卤虏鲁赂禄录陆驴吕铝屡缕虑滤绿峦挛孪滦乱抡轮伦仑沦纶论萝罗"
    "逻锣箩骡骆络妈玛码蚂马骂吗买麦卖迈脉瞒馒蛮满谩猫锚铆贸么霉镁门闷们锰"
    "梦谜弥觅绵缅庙灭悯闽鸣铭谬谋亩钠纳难挠脑恼闹馁腻酿鸟聂啮镊镍柠狞宁拧"
    "泞钮纽脓浓农疟诺欧鸥殴呕盘庞国刨赔喷鹏骗飘频贫苹凭评泼颇扑铺朴谱脐齐"
    "骑岂启气弃讫牵铅迁签谦钱钳浅遣谴枪呛墙抢锹桥侨窍窃钦亲寝轻氢倾请庆琼穷"
    "趋区躯驱龋趣权劝却确鹊让饶扰绕热认纫韧饪韧认荣绒软锐闰润洒萨鳃赛伞丧骚"
    "扫涩杀纱筛晒删闪陕赡缮伤赏烧绍摄慑设绅审婶肾渗声绳胜圣师狮湿诗尸时蚀实"
    "识驶势视试饰室释寿兽枢输书赎属术树竖数帅双谁税顺说硕烁丝饲耸颂讼诵苏诉"
    "肃虽随岁孙损笋缩琐锁獭挞抬摊贪滩瘫坛谭谈叹汤烫涛绦誊腾题体屉条贴铁厅听"
    "烃铜统头图涂团颓蜕脱鸵驮驼椭洼袜弯湾顽万网韦违围为潍维苇伟伪纬谓卫温"
    "闻纹稳问瓮挝蜗涡窝呜钨乌诬无芜吴坞雾务误锡牺袭习铣戏细虾辖峡侠狭厦锨"
    "鲜纤咸贤衔闲显险现献县馅羡宪线厢镶乡详响项萧销晓啸蝎协挟携胁谐写泻谢"
    "锌衅兴汹锈绣虚嘘须许绪续轩悬选癣绚学勋询寻驯训讯逊压鸦鸭哑亚讶阉烟盐严"
    "颜阎艳厌砚彦谚验鸯杨扬疡阳痒养样瑶摇尧遥窑谣药爷页业叶医铱颐遗仪彝蚁艺"
    "亿忆义诣议谊译异绎荫阴银饮樱婴鹰应缨莹萤营荧蝇赢颖哟拥佣痈踊咏涌优忧邮"
    "铀犹诱鱼渔娱与屿语狱誉预驭鸳渊辕园员圆缘远愿约跃钥岳粤悦阅云郧陨运酝晕"
    "韵杂灾载攒暂赞赃脏凿枣灶责择则泽贼赠扎札轧铡闸栅诈斋债毡盏斩辗崭栈战"
    "绽张涨帐账胀赵蛰辙锗这贞针侦诊镇阵挣睁狰帧郑证织职执纸挚掷帜质滞钟终"
    "种肿众诌轴皱昼骤朱烛嘱瞩贮铸筑驻专砖转赚桩庄装妆壮状锥赘坠缀谆浊兹资"
    "渍踪总纵邹诅组钻"
)

hits = {}
for i in range(1, 30):
    ep = "%02d" % i
    f = KB / f"Tap{ep}_JA" / f"kichban_tap{ep}_JA.md"
    if not f.exists():
        continue
    t = f.read_text(encoding="utf-8")
    for n, ln in enumerate(t.splitlines(), 1):
        s = set(ln) & SIMP_ONLY
        if s:
            hits.setdefault(ep, []).append((n, "".join(sorted(s)), ln))

if not hits:
    print("KHONG tim thay chu Han gian thach trong 29 file JA")
else:
    tot = 0
    for ep, lst in sorted(hits.items()):
        print(f"\nTap{ep}: {len(lst)} dong")
        tot += len(lst)
        for n, chars, ln in lst:
            print(f"   d{n} [{chars}] {ln[:170]}")
    print(f"\nTONG {tot} dong")
