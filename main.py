from utils import *
from word import *
import os
    
# 2．统计语料中的词语、词性及其频次。注意，词语可能有多个词性，要排列在一起。
WordDict = PositionsDict( pkl_to_dict("WordDict.pkl"))
POSDict = PositionsDict(pkl_to_dict("POSDict.pkl"))
WordPOSDict =  PositionsDict(dict(sorted(pkl_to_dict("WordPOSDict.pkl").items(),key = lambda kv:kv[0][0],reverse=True)))

if not os.path.exists("2统计.txt"):
    with open("2统计.txt","w",encoding="utf-8") as f:
        for items in [WordDict.itmes,POSDict.itmes,WordPOSDict.itmes]:
            string = ""
            for k,v in items:
                string+=str(k)+" "+str(len(v))+"  "
            string +='\n'
            f.write(string)