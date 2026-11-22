# -*- coding: utf-8 -*-
"Template and data definitions for Episodes 36-50 prompt construction."
import json, re
from pathlib import Path

# Mapping of episode metadata
EP_META = {
    36: {
        title: Hồ sơ Kip Kinkel (Tiếng nói trong tâm trí & Thurston High),
        loc: Springfield, Oregon, USA,
        keywords: [Thurston High School, Willamette Valley, Kip Kinkel, schizophrenia, hallucinations],
        target: 152,
        splits: [34, 35, 31, 28, 24]
    },
    37: {
        title: Hồ sơ Dr. Harold Shipman (Thiên thần tử thần y khoa),
        loc: Hyde, Greater Manchester, UK,
        keywords: [Donneybrook Medical Centre, Dr Shipman, diamorphine, forged will, elderly patients],
        target: 150,
        splits: [34, 34, 31, 25, 26]
    },
    38: {
        title: Hồ sơ Natascha Kampusch (3.096 ngày dưới lòng đất),
        loc: Strasshof, Vienna, Austria,
        keywords: [Strasshof underground bunker, Wolfgang Priklopil, dungeon door, escape, resilience],
        target: 152,
        splits: [34, 35, 31, 28, 24]
    },
    39: {
        title: Hồ sơ Joanna Dennehy (Nữ sát nhân Peterborough),
        loc: Peterborough and Hereford, UK,
        keywords: [Peterborough ditch, Joanna Dennehy, Green Star knife, psychopathy, fens landscape],
        target: 152,
        splits: [34, 35, 31, 28, 24]
    },
    40: {
        title: Hồ sơ Patrice Alègre (Bóng đen Toulouse & Profiling Pháp),
        loc: Toulouse, France,
        keywords: [Toulouse pink brick alleys, Gendarmerie Nationale, profiling unit, Patrice Alegre, subway],
        target: 148,
        splits: [34, 35, 31, 26, 22]
    },
    41: {
        title: Hồ sơ Quái vật Florence (Cơn ác mộng đồi Tuscany),
        loc: Florence hills, Tuscany, Italy,
        keywords: [Tuscany olive groves, Monster of Florence, couples parked in cars, Beretta 22, moonless night],
        target: 145,
        splits: [35, 32, 28, 27, 23]
    },
    42: {
        title: Hồ sơ Marc Dutroux (Ngôi nhà nỗi sợ Marcinelle),
        loc: Marcinelle and Brussels, Belgium,
        keywords: [Marcinelle dungeon house, Marc Dutroux, White March protest, judicial reform, lock],
        target: 152,
        splits: [34, 35, 31, 28, 24]
    },
    43: {
        title: Hồ sơ Peter Kürten (Quái vật Düsseldorf thời Weimar),
        loc: Düsseldorf, Germany,
        keywords: [Weimar Republic alleys, Rhine riverbank, Peter Kurten, psychoanalysis origins, Karl Berg],
        target: 146,
        splits: [33, 31, 28, 29, 25]
    },
    44: {
        title: Hồ sơ Bóng ma Heilbronn (Vụ án ô nhiễm mẫu ADN),
        loc: Heilbronn, Germany and Austria, France,
        keywords: [forensic cotton swabs, Phantom of Heilbronn, DNA contamination, cotton factory, confirmation bias],
        target: 152,
        splits: [34, 35, 31, 28, 24]
    },
    45: {
        title: Hồ sơ Moses Sithole (Sát nhân ABC & Nữ Profiler Nam Phi),
        loc: Johannesburg and Pretoria, South Africa,
        keywords: [Highveld grasslands, ABC killer, Moses Sithole, Micki Pistorius, false job interviews],
        target: 150,
        splits: [34, 35, 30, 27, 24]
    },
    46: {
        title: Hồ sơ Rosemary Ndlovu (Hợp đồng bảo hiểm đẫm máu),
        loc: Tembisa and Johannesburg, South Africa,
        keywords: [Tembisa police station, insurance policies, Rosemary Ndlovu, corrupt cop, undercover sting],
        target: 152,
        splits: [34, 35, 31, 28, 24]
    },
    47: {
        title: Hồ sơ Cedric Maake (Hội chứng tắc kè hoa Wemmer Pan),
        loc: Wemmer Pan, Johannesburg, South Africa,
        keywords: [Wemmer Pan lake, Cedric Maake, bludgeon vs firearm, Piet Byleveld, chameleon MO],
        target: 148,
        splits: [34, 32, 30, 27, 25]
    },
    48: {
        title: Hồ sơ Suzane von Richthofen (Nghịch tử dinh thự Sao Paulo),
        loc: Brooklin, Sao Paulo, Brazil,
        keywords: [luxury mansion Brooklin, Suzane von Richthofen, Cravinhos brothers, fake grief, iron bar],
        target: 152,
        splits: [34, 35, 31, 28, 24]
    },
    49: {
        title: Hồ sơ Pedro López (Quái vật Andes & Vết rạn La Violencia),
        loc: Andes mountains, Colombia, Ecuador, Peru,
        keywords: [Andes mountain passes, Pedro Lopez, La Violencia civil war, indigenous blindspots, mudslide],
        target: 146,
        splits: [33, 32, 30, 27, 24]
    },
    50: {
        title: Hồ sơ Bộ ba Garanhuns (Ảo tưởng cuồng giáo tẩy rửa dân số),
        loc: Garanhuns, Pernambuco, Brazil,
        keywords: [Garanhuns arid town, trio cult, Folie a Trois, sectarian delusion, backyard excavation],
        target: 148,
        splits: [34, 31, 29, 30, 24]
    }
}

print(Metadata definitions loaded.)
