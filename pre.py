from word import *
from utils import *
import re
import os

if __name__=="__main__":
    text = []

    #1  把注音去掉 把[]及其后面的标注去掉。
    with open("1998-01-2003版-带音.txt","rb") as f:
        while True:
            line = f.readline().decode("gb2312","ignore")
            if not line:
                break
            line = re.sub("\{(.+?)\}","",line) #去除注音
            line = re.sub("\[(.+?)\][a-z]+",lambda x:x.group(1),line) #去除标注
            line = re.sub("\\n","",line) #去除换行
            words = line.split() #空格分词
            if words == []:
                continue
            text.append(words)
    
    #4 生成生语料
    article = ""
    
    ## 分词转换为对象
    text_obj = []
    for i in range(len(text)):
        for j in range(len(text[i])):
            word_temp,pos_temp = text[i][j].split("/")
            article+=word_temp
            text_obj.append(WordPOS(word_temp,pos_temp,i,j))
        article+="\n"
    
    if not os.path.exists("4生语料.txt"):
        with open("4生语料.txt","w",encoding="utf-8") as f:
            f.write(article)

    WordDict = PositionsDict()
    POSDict = PositionsDict()
    WordPOSDict = PositionsDict()

    for obj in text_obj:
        WordPOSDict+[obj.key,obj.position]
        POSDict+[obj.POS,obj.position]
        WordDict+[obj.Text,obj.position]

    #保存字典
    
    dict_to_pkl(WordPOSDict.Dict,"WordPOSDict.pkl")
    dict_to_pkl(WordDict.Dict,"WordDict.pkl")
    dict_to_pkl(POSDict.Dict,"POSDict.pkl")
    






    # 3．统计语料中的bigram，即语料中的两个词语（及其词性）共现的频次。如：贵州 ns  南部 f  100
    # 表示贵州/ns  南部/f 在语料中出现100次。

    # 4．去掉语料中的词性标注，形成生语料（即没有标注的语料）。

    # 5．利用网络，搜索当前词语切分及其词性标注性能好的2个软件，对生语料进行标注。

    # 6．设计方法，比较分析这2个软件的性能哪个更好。
