import os
import re

from utils import *
from word import *

text = []

# 1  把注音去掉 把[]及其后面的标注去掉。
print("正在去除注音及标注")
with open("1998-01-2003版-带音.txt", "rb") as f:
    while True:
        line = f.readline().decode("gb2312", "ignore")
        if not line:
            break
        line = re.sub("\{(.+?)\}", "", line)  # 去除注音
        line = re.sub("\[(.+?)\][a-z]+", lambda x: x.group(1), line)  # 去除标注
        line = re.sub("\\n", "", line)  # 去除换行
        words = line.split()  # 空格分词
        if words == []:
            continue
        text.append(words)

# 4 生成生语料
article = ""

# 分词转换为对象,保存为生语料
print("正在生成生语料")
text_obj = []
for i in range(len(text)):
    POSLine = ""
    for j in range(len(text[i])):
        word_temp, pos_temp = text[i][j].split("/")
        article += word_temp+" "
        POSLine += pos_temp + " "
        text_obj.append(WordAndPOS(word_temp, pos_temp, i, j))
    article += "\n"+POSLine+"\n"

if not os.path.exists("result/4生语料_val.txt"):
    with open("result/4生语料_val.txt", "w", encoding="utf-8") as f:
        f.write(article)

# 创建统计字典
Dicts = [PositionsDict("Word"), PositionsDict("POS"), PositionsDict("WordAndPOS"), PositionsDict("BigramDict")]

print("正在统计语料")

# 统计
obj_prev = None
for obj in text_obj:
    Dicts[0]+Word(obj)
    Dicts[1]+POS(obj)
    Dicts[2]+obj
    if obj_prev and not obj.is_first:
        Dicts[3]+Bigram(obj_prev, obj)
    obj_prev = obj

print("正在排序")

# 保存，排序
for d in Dicts:
    d.print()
    # d.to_pkl(f"data/{d.Name}Dict.pkl")
    d.sort(mode=d.Name)

# 2．统计语料中的词语、词性及其频次。注意，词语可能有多个词性，要排列在一起。

print("正在保存结果")

# 保存结果
IOtools.dict_to_txt(Dicts[0:3], "result/2统计.txt")
IOtools.dict_to_txt([Dicts[3]], "result/3Bigram.txt")
