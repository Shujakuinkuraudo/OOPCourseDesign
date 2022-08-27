from word import *
from utils import *
import re
import os
import jieba
import jieba.posseg as posseg

text = []
WordEva = WordLineEvaluation("jieba")
POSEva = POSLineEvaluation("jieba")

with open("result/4生语料_val.txt","r",encoding="utf-8") as f:

    count = 0

    while True:

        count+=1
        if(count %5==0):
            print(count)


        Text = f.readline()
        if not Text:
            break
        TextSplit = Text.split()
        POSSplit = f.readline().split()
        TextUnion = ""
        for item in TextSplit:
            TextUnion+=item 
        WordEva.compare(TextSplit,jieba.lcut(TextUnion))

        TestTextSplit = []
        TestPOSSplit = []
        for word,POS in posseg.lcut(TextUnion):
            TestTextSplit.append(word)
            TestPOSSplit.append(POS)
        
        POSEva.compare(TextSplit,POSSplit,TestTextSplit,TestPOSSplit)

print(WordEva.report())
print(POSEva.report())

    