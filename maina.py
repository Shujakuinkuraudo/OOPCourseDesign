from utils import *
from word import *
import os
    
# 2．统计语料中的词语、词性及其频次。注意，词语可能有多个词性，要排列在一起。
WordDict = PositionsDict( pkl_to_dict("data/WordDict.pkl"))
POSDict = PositionsDict(pkl_to_dict("data/POSDict.pkl"))
WordPOSDict =  PositionsDict(pkl_to_dict("data/WordPOSDict.pkl")).sort(mode="WordPOS")
BigramDict =  PositionsDict(pkl_to_dict("data/BigramDict.pkl")).sort(mode="Bigram")

dict_to_txt([WordDict,POSDict,WordPOSDict],"result/2统计.txt")
dict_to_txt([BigramDict],"result/3Bigram.txt")