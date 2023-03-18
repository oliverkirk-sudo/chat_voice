voice_type_mapping = {
    'azu': 'azure',
    'hgf': 'huggingface'
}
character_list = {
    "0": "派蒙 Paimon (Genshin Impact)",
    "1": "特别周 Special Week (Umamusume Pretty Derby)",
    "2": "无声铃鹿 Silence Suzuka (Umamusume Pretty Derby)",
    "3": "东海帝王 Tokai Teio (Umamusume Pretty Derby)",
    "4": "丸善斯基 Maruzensky (Umamusume Pretty Derby)",
    "5": "富士奇迹 Fuji Kiseki (Umamusume Pretty Derby)",
    "6": "小栗帽 Oguri Cap (Umamusume Pretty Derby)",
    "7": "黄金船 Gold Ship (Umamusume Pretty Derby)",
    "8": "伏特加 Vodka (Umamusume Pretty Derby)",
    "9": "大和赤骥 Daiwa Scarlet (Umamusume Pretty Derby)",
    "10": "大树快车 Taiki Shuttle (Umamusume Pretty Derby)",
    "11": "草上飞 Grass Wonder (Umamusume Pretty Derby)",
    "12": "菱亚马逊 Hishi Amazon (Umamusume Pretty Derby)",
    "13": "目白麦昆 Mejiro Mcqueen (Umamusume Pretty Derby)",
    "14": "神鹰 El Condor Pasa (Umamusume Pretty Derby)",
    "15": "好歌剧 T.M. Opera O (Umamusume Pretty Derby)",
    "16": "成田白仁 Narita Brian (Umamusume Pretty Derby)",
    "17": "鲁道夫象征 Symboli Rudolf (Umamusume Pretty Derby)",
    "18": "气槽 Air Groove (Umamusume Pretty Derby)",
    "19": "爱丽数码 Agnes Digital (Umamusume Pretty Derby)",
    "20": "青云天空 Seiun Sky (Umamusume Pretty Derby)",
    "21": "玉藻十字 Tamamo Cross (Umamusume Pretty Derby)",
    "22": "美妙姿势 Fine Motion (Umamusume Pretty Derby)",
    "23": "琵琶晨光 Biwa Hayahide (Umamusume Pretty Derby)",
    "24": "重炮 Mayano Topgun (Umamusume Pretty Derby)",
    "25": "曼城茶座 Manhattan Cafe (Umamusume Pretty Derby)",
    "26": "美普波旁 Mihono Bourbon (Umamusume Pretty Derby)",
    "27": "目白雷恩 Mejiro Ryan (Umamusume Pretty Derby)",
    "28": "雪之美人 Yukino Bijin (Umamusume Pretty Derby)",
    "29": "米浴 Rice Shower (Umamusume Pretty Derby)",
    "30": "艾尼斯风神 Ines Fujin (Umamusume Pretty Derby)",
    "31": "爱丽速子 Agnes Tachyon (Umamusume Pretty Derby)",
    "32": "爱慕织姬 Admire Vega (Umamusume Pretty Derby)",
    "33": "稻荷一 Inari One (Umamusume Pretty Derby)",
    "34": "胜利奖券 Winning Ticket (Umamusume Pretty Derby)",
    "35": "空中神宫 Air Shakur (Umamusume Pretty Derby)",
    "36": "荣进闪耀 Eishin Flash (Umamusume Pretty Derby)",
    "37": "真机伶 Curren Chan (Umamusume Pretty Derby)",
    "38": "川上公主 Kawakami Princess (Umamusume Pretty Derby)",
    "39": "黄金城市 Gold City (Umamusume Pretty Derby)",
    "40": "樱花进王 Sakura Bakushin O (Umamusume Pretty Derby)",
    "41": "采珠 Seeking the Pearl (Umamusume Pretty Derby)",
    "42": "新光风 Shinko Windy (Umamusume Pretty Derby)",
    "43": "东商变革 Sweep Tosho (Umamusume Pretty Derby)",
    "44": "超级小溪 Super Creek (Umamusume Pretty Derby)",
    "45": "醒目飞鹰 Smart Falcon (Umamusume Pretty Derby)",
    "46": "荒漠英雄 Zenno Rob Roy (Umamusume Pretty Derby)",
    "47": "东瀛佐敦 Tosen Jordan (Umamusume Pretty Derby)",
    "48": "中山庆典 Nakayama Festa (Umamusume Pretty Derby)",
    "49": "成田大进 Narita Taishin (Umamusume Pretty Derby)",
    "50": "西野花 Nishino Flower (Umamusume Pretty Derby)",
    "51": "春乌拉拉 Haru Urara (Umamusume Pretty Derby)",
    "52": "青竹回忆 Bamboo Memory (Umamusume Pretty Derby)",
    "53": "待兼福来 Matikane Fukukitaru (Umamusume Pretty Derby)",
    "54": "名将怒涛 Meisho Doto (Umamusume Pretty Derby)",
    "55": "目白多伯 Mejiro Dober (Umamusume Pretty Derby)",
    "56": "优秀素质 Nice Nature (Umamusume Pretty Derby)",
    "57": "帝王光环 King Halo (Umamusume Pretty Derby)",
    "58": "待兼诗歌剧 Matikane Tannhauser (Umamusume Pretty Derby)",
    "59": "生野狄杜斯 Ikuno Dictus (Umamusume Pretty Derby)",
    "60": "目白善信 Mejiro Palmer (Umamusume Pretty Derby)",
    "61": "大拓太阳神 Daitaku Helios (Umamusume Pretty Derby)",
    "62": "双涡轮 Twin Turbo (Umamusume Pretty Derby)",
    "63": "里见光钻 Satono Diamond (Umamusume Pretty Derby)",
    "64": "北部玄驹 Kitasan Black (Umamusume Pretty Derby)",
    "65": "樱花千代王 Sakura Chiyono O (Umamusume Pretty Derby)",
    "66": "天狼星象征 Sirius Symboli (Umamusume Pretty Derby)",
    "67": "目白阿尔丹 Mejiro Ardan (Umamusume Pretty Derby)",
    "68": "八重无敌 Yaeno Muteki (Umamusume Pretty Derby)",
    "69": "鹤丸刚志 Tsurumaru Tsuyoshi (Umamusume Pretty Derby)",
    "70": "目白光明 Mejiro Bright (Umamusume Pretty Derby)",
    "71": "樱花桂冠 Sakura Laurel (Umamusume Pretty Derby)",
    "72": "成田路 Narita Top Road (Umamusume Pretty Derby)",
    "73": "也文摄辉 Yamanin Zephyr (Umamusume Pretty Derby)",
    "74": "真弓快车 Aston Machan (Umamusume Pretty Derby)",
    "75": "骏川手纲 Hayakawa Tazuna (Umamusume Pretty Derby)",
    "76": "小林历奇 Kopano Rickey (Umamusume Pretty Derby)",
    "77": "奇锐骏 Wonder Acute (Umamusume Pretty Derby)",
    "78": "秋川理事长 President Akikawa (Umamusume Pretty Derby)",
    "79": "綾地 寧々 Ayachi Nene (Sanoba Witch)",
    "80": "因幡 めぐる Inaba Meguru (Sanoba Witch)",
    "81": "椎葉 紬 Shiiba Tsumugi (Sanoba Witch)",
    "82": "仮屋 和奏 Kariya Wakama (Sanoba Witch)",
    "83": "戸隠 憧子 Togakushi Touko (Sanoba Witch)",
    "84": "九条裟罗 Kujou Sara (Genshin Impact)",
    "85": "芭芭拉 Barbara (Genshin Impact)",
    "86": "派蒙 Paimon (Genshin Impact)",
    "87": "荒泷一斗 Arataki Itto (Genshin Impact)",
    "88": "早柚 Sayu (Genshin Impact)",
    "89": "香菱 Xiangling (Genshin Impact)",
    "90": "神里绫华 Kamisato Ayaka (Genshin Impact)",
    "91": "重云 Chongyun (Genshin Impact)",
    "92": "流浪者 Wanderer (Genshin Impact)",
    "93": "优菈 Eula (Genshin Impact)",
    "94": "凝光 Ningguang (Genshin Impact)",
    "95": "钟离 Zhongli (Genshin Impact)",
    "96": "雷电将军 Raiden Shogun (Genshin Impact)",
    "97": "枫原万叶 Kaedehara Kazuha (Genshin Impact)",
    "98": "赛诺 Cyno (Genshin Impact)",
    "99": "诺艾尔 Noelle (Genshin Impact)",
    "100": "八重神子 Yae Miko (Genshin Impact)",
    "101": "凯亚 Kaeya (Genshin Impact)",
    "102": "魈 Xiao (Genshin Impact)",
    "103": "托马 Thoma (Genshin Impact)",
    "104": "可莉 Klee (Genshin Impact)",
    "105": "迪卢克 Diluc (Genshin Impact)",
    "106": "夜兰 Yelan (Genshin Impact)",
    "107": "鹿野院平藏 Shikanoin Heizou (Genshin Impact)",
    "108": "辛焱 Xinyan (Genshin Impact)",
    "109": "丽莎 Lisa (Genshin Impact)",
    "110": "云堇 Yun Jin (Genshin Impact)",
    "111": "坎蒂丝 Candace (Genshin Impact)",
    "112": "罗莎莉亚 Rosaria (Genshin Impact)",
    "113": "北斗 Beidou (Genshin Impact)",
    "114": "珊瑚宫心海 Sangonomiya Kokomi (Genshin Impact)",
    "115": "烟绯 Yanfei (Genshin Impact)",
    "116": "久岐忍 Kuki Shinobu (Genshin Impact)",
    "117": "宵宫 Yoimiya (Genshin Impact)",
    "118": "安柏 Amber (Genshin Impact)",
    "119": "迪奥娜 Diona (Genshin Impact)",
    "120": "班尼特 Bennett (Genshin Impact)",
    "121": "雷泽 Razor (Genshin Impact)",
    "122": "阿贝多 Albedo (Genshin Impact)",
    "123": "温迪 Venti (Genshin Impact)",
    "124": "空 Player Male (Genshin Impact)",
    "125": "神里绫人 Kamisato Ayato (Genshin Impact)",
    "126": "琴 Jean (Genshin Impact)",
    "127": "艾尔海森 Alhaitham (Genshin Impact)",
    "128": "莫娜 Mona (Genshin Impact)",
    "129": "妮露 Nilou (Genshin Impact)",
    "130": "胡桃 Hu Tao (Genshin Impact)",
    "131": "甘雨 Ganyu (Genshin Impact)",
    "132": "纳西妲 Nahida (Genshin Impact)",
    "133": "刻晴 Keqing (Genshin Impact)",
    "134": "荧 Player Female (Genshin Impact)",
    "135": "埃洛伊 Aloy (Genshin Impact)",
    "136": "柯莱 Collei (Genshin Impact)",
    "137": "多莉 Dori (Genshin Impact)",
    "138": "提纳里 Tighnari (Genshin Impact)",
    "139": "砂糖 Sucrose (Genshin Impact)",
    "140": "行秋 Xingqiu (Genshin Impact)",
    "141": "奥兹 Oz (Genshin Impact)",
    "142": "五郎 Gorou (Genshin Impact)",
    "143": "达达利亚 Tartalia (Genshin Impact)",
    "144": "七七 Qiqi (Genshin Impact)",
    "145": "申鹤 Shenhe (Genshin Impact)",
    "146": "莱依拉 Layla (Genshin Impact)",
    "147": "菲谢尔 Fishl (Genshin Impact)"
}
