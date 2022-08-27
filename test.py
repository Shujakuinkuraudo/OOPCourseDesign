from word import *
from utils import *

jiebaWordEva = SegLineEvaluation("jieba-Word")
jiebaPOSEva = POSLineEvaluation("jieba-POS")
snowWordEva = SegLineEvaluation("snow-Word")
snowPOSEva = POSLineEvaluation("snow-POS")

with open("result/4生语料_val.txt","r",encoding="utf-8") as f:

    count = 0

    while True:

        #试验记录
        count+=1
        if(count %200==0):
            print(count)
            with open("result/5模型评估.txt","a",encoding="utf-8") as fw:
                string = str(count)+"   "+jiebaWordEva.report()+"   "+jiebaPOSEva.report()+"   "+snowWordEva.report()+"   "+snowPOSEva.report()+"\n"
                fw.write(string)

        Text = f.readline()
        if not Text:
            break
        TextSplit = Text.split()
        POSSplit = f.readline().split()

        #合并字符串
        TextUnion = ""
        for item in TextSplit:
            TextUnion+=item 
        
        #snownlp
        Textseg,TestTextSplit,TestPOSSplit = utils.SegTools.SnownlpSeg(TextUnion)        
        snowPOSEva.compare(TextSplit,POSSplit,TestTextSplit,TestPOSSplit)
        snowWordEva.compare(TextSplit,Textseg)

        #jieba
        TextSeg,TestTextSplit,TestPOSSplit = utils.SegTools.JiebaSeg(TextUnion)        
        jiebaPOSEva.compare(TextSplit,POSSplit,TestTextSplit,TestPOSSplit)
        jiebaWordEva.compare(TextSplit,Textseg)

        


    