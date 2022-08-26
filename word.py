from abc import abstractmethod

from typing import overload


class Word:
    def __init__(self,Text="") -> None:
        self.Text = Text
    
    @property
    def key(self):
        return (self.Text)

class POS:    #part of speech
    def __init__(self,PoS="") -> None:
        self.POS = PoS

    @property
    def key(self):
        return (self.POS)

class WordPOS(Word,POS):
    def __init__(self, Text="",PoS="",LineSeq=0,WordSeq=0) -> None:
        Word.__init__(self,Text)
        POS.__init__(self,PoS)
        self.seq = [LineSeq,WordSeq]
    
    @property
    def key(self):
        return (self.Text,self.POS)
        
    @property
    def position(self):
        return self.seq
    
    @property
    def is_first(self):
        return self.seq[1]==0

class Bigram(WordPOS):
    def __init__(self, prev_WordPOS:WordPOS,now_WordPOS:WordPOS):
        super().__init__(prev_WordPOS.Text,prev_WordPOS.POS,prev_WordPOS.seq[0],prev_WordPOS.seq[1])
        self.AnotherText = now_WordPOS.Text
        self.AnotherPOS = now_WordPOS.POS
    
    @property
    def key(self):
        return (self.Text,self.POS,self.AnotherText,self.AnotherPOS)


class Dict:
    def __init__(self) -> None:
        self.Dict = dict()

    @abstractmethod
    def __add__(self,obj):
        pass

class PositionsDict(Dict):
    def __init__(self,other=None) -> None:
        super().__init__()
        if other:
            self.Dict = other
    
    @overload
    def __add__(self, Obj:Bigram):
        pass
    @overload
    def __add__(self,Obj:list):
        pass

    def __add__(self, Obj):
        if type(Obj)==list:
            key,position = Obj 
            if key not in self.Dict:
                self.Dict[key] = [position]
            else: 
                self.Dict[key].append(position)
        else: 
            if Obj.key not in self.Dict:
                self.Dict[Obj.key] = 1
            else: 
                self.Dict[Obj.key] += 1
        return self


    @property
    def itmes(self):
        return self.Dict.items()

    def sort(self,mode):
        if mode=="Bigram" or mode == "WordPOS":
            self.Dict = dict(sorted(self.itmes),key = lambda kv:kv[0][0])
        return self

    
    
    
        