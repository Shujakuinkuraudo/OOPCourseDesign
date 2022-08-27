from cgitb import reset
import jieba
import re

with open("result/4生语料.txt","r") as f:
    test = f.readline()
    test = re.sub("\\n","",test)
    test = jieba.lcut(test)
