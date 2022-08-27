from word import *
from utils import *
import re
import os

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

## 分词转换为对象,保存为生语料
text_obj = []
for i in range(len(text)):
    for j in range(len(text[i])):
        word_temp,pos_temp = text[i][j].split("/")
        article+=word_temp+" "
        text_obj.append(WordAndPOS(word_temp,pos_temp,i,j))
    article+="\n"
    for j in range(len(text[i])):
        word_temp,pos_temp = text[i][j].split("/")
        article+=pos_temp+" "
    article+="\n"

if not os.path.exists("result/4生语料_val.txt"):
    with open("result/4生语料_val.txt","w",encoding="utf-8") as f:
        f.write(article)

# 创建统计字典
WordDict = PositionsDict()
POSDict = PositionsDict()
WordAndPOSDict = PositionsDict()
BigramDict = PositionsDict()

# 统计
obj_prev = None
for obj in text_obj:
    if obj_prev and not obj.is_first:
        BigramDict+Bigram(obj_prev,obj)
    WordAndPOSDict+obj
    POSDict+POS(obj.POS)
    WordDict+Word(obj.Text)
    obj_prev = obj

#保存字典
BigramDict.print()

BigramDict.to_pkl("data/BigramDict.pkl")
WordAndPOSDict.to_pkl("data/WordAndPOSDict.pkl")
WordDict.to_pkl("data/WordDict.pkl")
POSDict.to_pkl("data/POSDict.pkl")

# 2．统计语料中的词语、词性及其频次。注意，词语可能有多个词性，要排列在一起。
#排序
BigramDict.sort(mode="Bigram")
WordAndPOSDict.sort(mode="WordPOS")
dict_to_txt([WordDict,POSDict,WordAndPOSDict],"result/2统计.txt")
dict_to_txt([BigramDict],"result/3Bigram.txt")
    







    # 5．利用网络，搜索当前词语切分及其词性标注性能好的2个软件，对生语料进行标注。

    # 6．设计方法，比较分析这2个软件的性能哪个更好。
