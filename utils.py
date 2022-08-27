from dataclasses import dataclass
import json
import pickle
import os

from pyparsing import Or

def dict_to_pkl(dict,file):
    with open(file, "wb") as tf:
        pickle.dump(dict,tf)

def pkl_to_dict(file):
    with open(file, "rb") as tf:
        return pickle.load(tf)

def dict_to_txt(dicts,file,mode=""):
    if not os.path.exists(file):
        with open(file,"w",encoding="utf-8") as f:
            for dict in dicts:
                string = ""
                if mode=="len":
                    for k,v in dict.items:
                        string+=str(k)+" "+str(len(v))+"  "
                else:
                    for k,v in dict.items:
                        string+=str(k)+" "+str(v)+"  "
                string +='\n'
                f.write(string)


class Evaluation:
    def __init__(self,Name) -> None:
        self.Name = Name
        self.CorrectCount = 0
        self.OriginalCount = 0
        self.TestCount = 0
        self.P = 0
        self.R = 0
        self.F1 = 0

    def report(self):
        self.P = self.CorrectCount/self.TestCount
        self.R = self.CorrectCount/self.OriginalCount
        self.F1 = 2*self.P*self.R/(self.P+self.R)
        return f"Model:{self.Name}          P:{self.P},R:{self.R},F1:{self.F1}"



class LineEvaluation(Evaluation):
    def __init__(self, Name) -> None:
        super().__init__(Name)
    
    
    def compare(self,OriginalIndex:list,TestIndex:list):
        self.OriginalCount += len(OriginalIndex)
        self.TestCount += len(TestIndex)


        #统计正确词汇
        for item in TestIndex:
            if item in OriginalIndex:
                self.CorrectCount += 1

class WordLineEvaluation(LineEvaluation):
    def __init__(self, Name) -> None:
        super().__init__(Name)

    def list_to_index(self,l:list) -> list:
        LIndex = []
        index = 0
        for item in l:
            WordIndex = [index]
            index+=len(item)
            WordIndex.append(index)
            WordIndex.append(item)
            LIndex.append(WordIndex)
        return LIndex
    
    def compare(self,Original,Test):
        OriginalIndex = self.list_to_index(Original)
        TestIndex = self.list_to_index(Test)
        super().compare(OriginalIndex,TestIndex)

class POSLineEvaluation(LineEvaluation):
    def __init__(self, Name) -> None:
        super().__init__(Name)
    
    def list_to_index(self,Word:list,POS:list):
        LIndex = []
        index = 0
        for i in range(len(Word)):
            WordIndex = [index]
            index+=len(Word[i])
            WordIndex.append(index)
            WordIndex.append(POS[i])
            LIndex.append(WordIndex)
        return LIndex

    def compare(self,OriginalWord,OriginalPOS,TestWord,TestPOS):
        OriginalIndex = self.list_to_index(OriginalWord,OriginalPOS)
        TestIndex = self.list_to_index(TestWord,TestPOS)
        super().compare(OriginalIndex,TestIndex)


        

    
if __name__ == "__main__":
    A = LineEvaluation("123")
    a = ["123","123","2223"]
    b = ["123","123","2","223"]
    A.compare(a,b)
    print(A.report())

    
    