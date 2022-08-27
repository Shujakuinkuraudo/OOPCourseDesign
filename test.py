from word import *
from utils import *
import jieba
import jieba.posseg as posseg
from snownlp import SnowNLP

jiebaWordEva = WordLineEvaluation("jieba-Word")
jiebaPOSEva = POSLineEvaluation("jieba-POS")
snowWordEva = WordLineEvaluation("snow-Word")
snowPOSEva = POSLineEvaluation("snow-POS")

with open("result/4生语料_val.txt","r",encoding="utf-8") as f:

    count = 0

    while True:

        count+=1
        if(count %200==0):
            with open("result/5模型评估.txt","a",encoding="utf-8") as fw:
                string = str(count)+"   "+jiebaWordEva.report()+"   "+jiebaPOSEva.report()+"   "+snowWordEva.report()+"   "+snowPOSEva.report()+"\n"
                print(string)
                fw.write(string)

        Text = f.readline()
        if not Text:
            break
        TextSplit = Text.split()
        POSSplit = f.readline().split()
        TextUnion = ""
        for item in TextSplit:
            TextUnion+=item 
        jiebaWordEva.compare(TextSplit,jieba.lcut(TextUnion))
        Snow = SnowNLP(TextUnion)
        snowWordEva.compare(TextSplit,Snow.words)

        TestTextSplit = []
        TestPOSSplit = []
        for word,POS in posseg.lcut(TextUnion):
            TestTextSplit.append(word)
            TestPOSSplit.append(POS)
        jiebaPOSEva.compare(TextSplit,POSSplit,TestTextSplit,TestPOSSplit)

        snowTextSplit = []
        snowPOSSplit = []
        for word,POS in Snow.tags:
            snowTextSplit.append(word)
            snowPOSSplit.append(POS)
        snowPOSEva.compare(TextSplit,POSSplit,snowTextSplit,snowPOSSplit)

        


    